**********
Venafi API
**********

Official Documentation
======================

    Please refer to the `official Venafi WebSDK documentation <https://docs.venafi.com/contentindex.php>`_ as the official documentation of the Venafi WebSDK API and Aperture API is not provided here. The API modules provided by this product simply provide an easy-to-use interface to the Venafi APIs.

Usage Guide
===========
    This product provides an interface to both the Venafi WebSDK and Aperture APIs. While all WebSDK APIs are defined in this product, not all Aperture APIs will be. When using this product the user can specify which set of APIs is preferred. Refer to the `Features` for more details.


`Calling An API`
""""""""""""""""

Given this WebSDK API
  * URL: https://somehost.com/vedsdk/Workflow/Ticket/Create
  * Method: POST

Create Authenticate object, which contains authorized WebSDK and Aperture API sessions for the specified user.

.. code-block:: python

    from venafi.api import Authenticate

    api = Authenticate(host='192.168.1.10', username='local:admin', password='passw0rd')

Example call to create a workflow ticket where "..." represents all of the arguments
to the post method. In this call "post" sends a POST request to TPP and stores the 
response in a response property that will later be used.

.. code-block:: python

    result = api.websdk.Workflow.Ticket.Create.post(...)

``result`` now contains the api.websdk.Workflow.Ticket.Create object. This object holds
the raw response in "result.json_response". This property should only be desirable if
no content or an invalid status code is expected. If 400 was expected, then:

.. code-block:: python

    assert result.json_response.status_code == 400

``result`` also contains objects that map the response objects in the content returned by
TPP. If content was expected, it could look like this:

.. code-block:: json

    {
      "GUID": "af415f09-d487-43de-ba2e-f61d089b4e68",
      "Result": 1
    }

In order to access the GUID of the new object, simply call it fro ``result``.

.. code-block:: python

    guid = result.guid

In this case, ``result.guid`` is a python property that enforces a validation of the status code of the response
and the existence of the object in the response before returning it. If an invalid response is returned or the
object does not exist as expected, an error is thrown.

Now ``guid`` can be used to get the details of the workflow ticket that was just created.

.. code-block:: python

result = api.websdk.Workflow.Ticket.Details.post(guid=guid)

There is no need to use the raw response for any sort of validation since TPP returned a ticket GUID. In other
words, there MUST be a ticket with details. In this case, the response could be:

.. code-block:: json

    {
        "ApprovalExplanation": "",
        "ApprovalFrom": "AD+VENAFI:e3fc935977cf4940bd1d0c67433a76e5",
        "ApprovalReason": "Testing workflow",
        "Approvers": [
            "AD+VENAFI:e3fc935977cf4940bd1d0c67433a76e5",
            "AD+VENAFI:f824d97c78d9364499aaa93bfd6799a8"
        ],
        "Blocking": "\\VED\\Policy\\Regression\\four.venafi.example",
        "Created": "/Date(1489096754000)/",
        "IssuedDueTo": "\\VED\\Policy\\Regression\\Stage 0",
        "Result": 1,
        "Status": "Pending",
        "Updated": "/Date(1489098779597)/"
    }

In order to get the list of approvers and status of the ticket:

.. code-block:: python

    # HTTP Status Code == 200 validated with this property.
    approvers = result.approvers
    # HTTP Status Code == 200 already validated above, so this property knows not to re-validate.
    status = result.status

It's worth noting that once the response is validated with a call to a response property, the response will not be
re-validated with subsequent calls to other properties until another response is loaded with another API call.


`Defining APIs`
"""""""""""""""

All Venafi API types (WebSDK, Aperture, etc.) are contained in the `Authenticate` class.

.. code-block:: python
    :emphasize-lines: 7,8
    :caption: authenticate.py

    from venafi.api.websdk.websdk import WebSDK
    from venafi.api.aperture.aperture import Aperture


    class Authenticate:
        def __init__(self, host: str, username=None, password=None, certificate=None, preference='websdk'):
            self.websdk = WebSDK(host=host, username=username, password=password)
            self.aperture = Aperture(host=host, username=username, password=password)
            if preference not in {'websdk', 'aperture'}:
                raise ValueError('Invalid preference. Must be one of "websdk" or "aperture".')
            self.preference = preference.lower()

            self._host = host
            self._username = username
            self._password = password
            self._certificate = certificate

        def re_authenticate(self):
            self.__init__(host=self._host, username=self._username, password=self._password, certificate=self._certificate,
                          preference=self.preference)

This class is responsible for initializing each API type, which in turn generates an authentication token for each type. This
class is designed to be used by the Venafi Features to perform all API functions. It captures the variables used to authenticate
and contains within itself the ability to re-authenticate should a token expire. Each API class (described further) knows how to
automatically re-authenticate so the programmer does not have to explicitly re-authenticate in the event of an expired token.

While Aperture API and WebSDK API follow the same structure, the following examples are WebSDK examples.

Structure
'''''''''

Every API has an endpoint and a method.
Given this WebSDK API

* URL: https://somehost.com/vedsdk/Workflow/Ticket/Details
* Method: POST
* Parameters: GUID (string)
* Returns:

.. code-block:: json

    {
        "ApprovalExplanation": "",
        "ApprovalFrom": "AD+VENAFI:e3fc935977cf4940bd1d0c67433a76e5",
        "ApprovalReason": "Testing workflow",
        "Approvers": [
             "AD+VENAFI:e3fc935977cf4940bd1d0c67433a76e5",
             "AD+VENAFI:f824d97c78d9364499aaa93bfd6799a8"
        ],
        "Blocking": "\\VED\\Policy\\Regression\\four.venafi.example",
        "Created": "/Date(1489096754000)/",
        "IssuedDueTo": "\\VED\\Policy\\Regression\\Stage 0",
        "Result": 1,
        "Status": "Pending",
        "Updated": "/Date(1489098779597)/"
    }

In order to define this **properly** in this project, follow the comments in the code block below.

Each path in the URL is its own class stemming from ``websdk.py`` (or ``aperture.py`` respectively). In this case,
WebSDK contains Workflow, which contains Ticket, which contains Details. So,

.. code-block:: python
    :caption: venafi/api/websdk/websdk.py
    :emphasize-lines: 1,9

    from venafi.api.websdk.endpoints.workflow import _Workflow
    # Other imports here.

    class WebSDK:
    def __init__(self, host: str, username=None, password=None, certificate=None):
        # Authorization happens here.

        # Other endpoints defined here.
        self.Workflow = _Workflow(self)

.. code-block:: python
    :caption: venafi/api/websdk/endpoints/workflow.py
    :emphasize-lines: 2,6,11,18,22,29,40,47,78,85,93,97

    # Type hinting is important!
    from typing import List

    # The API class stores the URL, response object, and authentication object.
    # The json_property function is a decorator that validates good responses when called.
    from venafi.api.api_base import API, json_response_property

    # Response objects are classes that define the properties of the response. If the
    # response contains a python dictionary, it is converted to a class with corresponding
    # properties.
    from venafi.properties.response_objects.worfklow import Workflow


    class _Workflow:
        def __init__(self, websdk_obj):
            # The websdk_obj is the authentication object that authorizes these calls. It must propagate to
            # each sub-class for the same reason.
            self.Ticket = self._Ticket(websdk_obj=websdk_obj)

        # This class is contained within _Workflow so the endpoint flows as a property of Workflow. The same is for
        # endpoints that follow Workflow/Ticket.
        class _Ticket:
            def __init__(self, websdk_obj):
                self.Create = self._Create(websdk_obj=websdk_obj)

            # API is inherited to initialize the URL, return codes, and authentication object, all of which are
            # required. The API object handles writing the API, validating the response, and providing the raw
            # response should the response not be valid.
            class _Details(API):
                def __init__(self, websdk_obj):
                    super().__init__(api_obj=websdk_obj, url='/Workflow/Ticket/Details', valid_return_codes=[200])

                # Each property of the response MUST be a json_response_property(). @property must come first.
                # json_response_property() performs validation of the response using the valid_return_codes
                # in __init__.
                @property
                @json_response_property()
                def approval_explanation(self) -> str:
                    # Since the return type is a string, simply return it from the json response like so.
                    return self.json_response('ApprovalExplanation')

                @property
                @json_response_property()
                def result(self):
                    # The workflow result is a result code that maps to a code description. This object is
                    # created and returned because it contains that map for logging purposes.
                    return Workflow.Result(self.json_response('Result'))

                @property
                @json_response_property()
                def arbitrary_example(self):
                    # Imagine that the response object contained a dictionary of values like this:
                    # {
                    #   'Example': {
                    #       'value1': [
                    #           'someValue',
                    #       ],
                    #       'value2': {
                    #           value: 'x'
                    #       }
                    #   }
                    # }
                    # In this case, an Example class should be created in venafi/properties/response_objects/workflow.py.
                    # The class should be a sub-class of Workflow titled by the name of the response object, in this case,
                    # Example. This should be defined for subsequent objects similarly. So,
                    #
                    # --- venafi/properties/response_objects/workflow.py ---
                    # class Workflow:
                    #     class Example:
                    #         def __init__(example_dict: dict):
                    #             if not isinstance(example_dict, dict):
                    #                 example_dict = {}
                    #             # Use get(), not []!!
                    #             self.value1 = example_dict.get('value1')  # type: List[str]  -> type hinting is important!!!
                    #             self.value2 = Value2(example_dict.get('value2'))
                    #
                    #     # class Value2 defined here with property "value".
                    return Example(self.json_response('Example))

                # All other properties go here...

                # The method used is POST, so post() is defined here with the proper parameters.
                # In this case, guid is a required string, but whenever the API parameters are
                # optional, it should also be optional here. ALWAYS suggest data types.
                def post(self, guid: str):
                    body = {
                        'GUID': guid
                    }

                    # json_response contains the raw Response object received from TPP. It comes
                    # from API._post, which is inherited. This method MUST be used as it automatically
                    # logs the URL, inputs, and outputs of the response.
                    self.json_response = self._post(data=body)

                    # Must return "self" in order to allow the recipient to access the response
                    # properties.
                    return self
