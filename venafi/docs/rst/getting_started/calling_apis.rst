.. _using_tpp_apis:

Trust Protection Platform APIs
==============================

.. note::
    The Venafi module allows a user to authenticate to all available API sources. All WebSDK APIs are
    accessible via this module, but only certain Aperture APIs. Refer to the source code for a list of
    Aperture APIs as they are not documented here.

    Refer to the `official Venafi WebSDK documentation <https://docs.venafi.com/contentindex .php>`_
    as the official documentation of the Venafi WebSDK API.

    Refer to :ref:`authentication` for information on authenticating to the API sources.

    Refer to :ref:`api` for more details on how the APIs operate in this module.

Calling An API
''''''''''''''

The API layer is structured to follow the pattern of the target endpoint URL followed by the RESTful method.

For example::

    Given:
        METHOD: POST
        URL:    https://tppserver.mycompany.com/vedsdk/Workflow/Ticket/Create
        ARGS:   {
            "ObjectDN": "\VED\Policy\Certificates\MyCert",
            "Reason": 0,
            "Approvers": [
                {
                    "PrefixedUniversal": "local:933562f6-bad0-4552-ae3f-684ee09b8643"
                }
            ],
            "WorkflowDN":"\\VED\\Policy\\Workflows\\WF for Stage 0"
        }

Then:

.. code-block:: python

    from venafi import Authenticate

    api = Authenticate(
        host='tppserver.mycompany.com',
        username='username12',
        password='passw0rd!@#$',
        preference='websdk',
        application_id='SomeOAuthApplication',
        scope="certificate:approve,delete,discover,manage,revoke;configuration:delete,manage"
    )

    response = api.websdk.Workflow.Ticket.Create.post(
        object_dn="\\VED\\Policy\\Certificates\\MyCert",
        reason=0,
        approvers=[{
            "PrefixedUniversal": "local:{933562f6-bad0-4552-ae3f-684ee09b8643}"
        }],
        workflow_dn="\\VED\\Policy\\Workflows\\WF for Stage 0"
    )


The API Response Object
'''''''''''''''''''''''

Each call to an API yields an ``APIResponse`` object, or a direct derivative of that object. The
response object contains the following data:

* a list of valid return codes for the specific API.
* helper methods to validate against the list of valid return codes.
* the raw JSON response from Python's ``requests`` library.
* a property for each value returned in the response body.

For example::

    Given:
        API REQUEST:
            POST https://tppserver.mycompany.com/vedsdk/Metadata/Get
            {
                "DN": "\\VED\\Policy\\Certificates\\MyCert"
            }
        API RESPONSE:
            HTTP/1.1 200 OK
            {
               "Data":[

                     "Key":{
                        "AllowedValues":[

                        ],
                        "Classes":[
                           "X509 Certificate"
                        ],
                        "ConfigAttribute":"{69e06441-f8e8-482d-8a86-884f03c03d1b}",
                        "DN":"\\VED\\Metadata Root\\MetaDataObject_110916001158115",
                        "DefaultValues":[

                        ],
                        "ErrorMessage":"Value entered is not a valid Cost Center",
                        "Guid":"{69e06441-f8e8-482d-8a86-884f03c03d1b}",
                        "Help":"Cost Center is comprised of 3 letters followed by 3 numbers",
                        "Label":"Cost Center 9596",
                        "Name":"MetaDataObject_110916001158115",
                        "Policyable":true,
                        "RegularExpression":"[A-Za-z]{3}[0-9]{3}",
                        "RenderHidden":false,
                        "RenderReadOnly":false,
                        "Type":1
                     },
                     "Value":[
                        "Lab571"
                     ]
                  }
               ],
               "Locked":false,
               "Result":0
            }

Then:

    .. code-block:: python

        1  response = api.websdk.Metadata.Get.post(dn="\\VED\\Policy\\Certificates\\MyCert")
        2  guids = [data.key.guid for data in response.data]
        3  if response.is_valid_response():
        4      logger.log(f'URL: {response.json_response.url}\n'
        5                 f'Status Code: {response.json_response.status_code}\n')
        6      body = response.json_response.json()
        7  else:
        8      response.assert_valid_response()


* **Line 2:**

    The response object returned is a Python Object representation of the actual response body. In
    other words, each property of the response body is a Python instance property. Using the raw response one
    could use

    ``guids = [data['Key']['Guid'] for data in response.json_response.json()['Data']]``

    but the data can be, and should be, accessed by the properties like in the example above. Using the properties
    has a few advantages:

    #. When accessing a property from a response object for the first time, an automatic validation of the return
       codes occurs. If the status code is different than the expected status code(s), then an error is raised. This
       ensures success of the APIs as they are used. If this is undesired, then use ``response.json_response``.
    #. When using an IDE with auto-completion the properties show up. Also, this facilitates refactoring.
    #. Because there are multiple API types that have similar APIs, the object returned is consistent across all APIs.

* **Line 3:**

    Not all APIs return body content, so to validate the API ``is_valid_response()`` can be called to obtain a boolean
    type.

* **Lines 4-6:**

    The raw response can be accessed via ``response.json_response``. This object is the response object created by Python's
    ``requests`` library.

* **Line 8:**

    Not all APIs return body content, so to validate the API ``is_valid_response()`` can be called to raise an error if the
    expected status code was not returned.
