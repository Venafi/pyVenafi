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

.. code-block:: python

    HTTP/1.1 200 OK
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

.. code-block:: python

    HTTP 200 OK
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
