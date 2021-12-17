Workflows And Tickets
=====================

.. note::
    Refer to :ref:`applying_workflows` for applying workflows.

Create And Apply A Standard Workflow
------------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Create the workflow...
    workflow = features.workflow.standard.create(
        name='Stage 300 Worfklow',
        parent_folder=r'\VED\Policy\Administration\Worfkflows',
        stage=300,
        injection_command="/bin/bash /run/something.sh",
        application_class_name=Attributes.application.apache.__config_class__,
        approvers=['local:approver1', 'local:approver2'],
        macro='$Config[$Config[$WorkflowtargetDN$,"Owner Object"]$,"Contact"|"Approver"]$',
        reason_code=100
    )

    # and apply the workflow to a folder.
    features.folder.apply_workflow(
        folder=r'\VED\Policy\Certificates\MyTeam',
        workflow=workflow
    )

Create And Apply An Adaptable Workflow
--------------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Read in the file stream as bytes.
    with open('SuperAwesomeScript.ps1', 'rb') as f:
        script_content_in_bytes = f.read()

    # Create the workflow...
    workflow = features.workflow.adaptable.create(
        name='Stage 300 Worfklow',
        parent_folder=r'\VED\Policy\Administration\Worfkflows',
        stage=300,
        approvers=['local:approver1', 'local:approver2'],
        reason_code=100,
        powershell_script_name='SuperAwesomeScript',  # Name of the script minus the extension.
        powershell_script_content=script_content_in_bytes,
        use_approvers_from_powershell_script=True
    )

    # and apply the workflow to a folder.
    features.folder.apply_workflow(
        folder=r'\VED\Policy\Certificates\MyTeam',
        workflow=workflow
    )

Managing Workflow Tickets
-------------------------

.. rubric:: Create, Get, And Delete A Workflow Ticket
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Create the ticket.
    features.workflow.ticket.create(
        obj=r'\VED\Policy\Certificates\MyTeam\my-questionable-cert.com',
        workflow=r'\VED\Policy\Administration\Workflows\Stage 0 Check',
        approvers=['local:approver-1', 'local:approver-2'],
        reason=42
    )

    # Get the list of ticket names on the object.
    # Multiple tickets can possibly exist on an object.
    tickets = features.workflow.ticket.get(
        obj=r'\VED\Policy\Certificates\MyTeam\my-questionable-cert.com',
        expected_num_tickets=2  # Two or more tickets are expected to exist on this certificate.
    )

    # Delete the ticket. This neither approves nor rejects the ticket.
    features.workflow.ticket.delete(ticket_name=ticket)

.. rubric:: Get All Workflow Tickets Pending My Approval
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Get all tickets pending my approval.
    tickets = [
        features.workflow.ticket.details(ticket)
        for ticket in features.workflow.ticket.get()
    ]
    pending_my_approval = [
        ticket for ticket in tickets
        if ticket.status == AttributeValues.Workflow.Status.pending
    ]


.. rubric:: Approving And Rejecting Workflow Tickets

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Get all tickets assigned to me. This includes all tickets of all statuses
    # and not just pending tickets.
    tickets = features.workflow.ticket.get()

    # Decide whether to approve/reject each ticket based on a minimum RSA key size of 2048.
    for ticket in tickets:
        details = features.workflow.ticket.details(ticket_name=ticket)
        certificate = features.certificate.details(details.issued_due_to)

        if details.status == AttributeValues.Workflow.Status.pending:
            if certificate.key_algorithm == AttributeValues.Certificate.KeyAlgorithm.rsa and \
                    certificate.key_size >= 2048:
                features.workflow.ticket.update_status(
                    ticket_name=ticket, status=AttributeValues.Workflow.Status.approved,
                    explanation="I trust this certificate request."
                )
            else:
                features.workflow.ticket.update_status(
                    ticket_name=ticket, status=AttributeValues.Workflow.Status.rejected,
                    explanation="This certificate does not meet the key size requirements.",
                )

Creating and Deleting Reason Codes
----------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Create the reason code.
    reason_code = features.workflow.reason_code.create(
        code=42,
        description='The answer to everything.',
        name='SuperAwesomeReasonCode'
    )

    # Delete the reason code.
    features.workflow.reason_code.delete(
        code=42,
        name='SuperAwesomeReasonCode'
    )
