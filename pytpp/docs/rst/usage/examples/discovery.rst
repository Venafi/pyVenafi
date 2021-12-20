Discovery And Placement
=======================

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.


Managing Placement Rules
------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Certificate Placement Rules
    certificate_placement_condiitons = [
        features.placement_rule_condition.common_name.matches_regex('[a-z]*\.(my-team\.){0,1}*my-domain\.com'),
        features.placement_rule_condition.organizational_unit.contains('WestRegion Engineering')
    ]

    certificate_placement_rule = features.placement_rules.create(
        name='SomeCertificateRule',
        rule_type=AttributeValues.PlacementRules.RuleType.ssh,
        device_location_dn=r'\VED\Policy\Installations\WestRegion',
        certificate_location_dn=r'\VED\Policy\Certificates\_Discovered\WestRegion\SomeTeam',
        conditions=certificate_placement_condiitons
    )

    # SSH Placement Rules
    ssh_placement_conditions = [
        features.placement_rule_condition.hostname.ends_with('my-domain.com'),
        features.placement_rule_condition.supports_ssh_v1.is_true()
    ]

    ssh_placement_rule = features.placement_rules.create(
        name='SomeSSHRule',
        rule_type=AttributeValues.PlacementRules.RuleType.ssh,
        device_location_dn=r'\VED\Policy\Installations\WestRegion',
        conditions=ssh_placement_conditions
    )

Network Discovery
-----------------

Creating Network Discovery Jobs
*******************************

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    certificate_placement_rule = features.placement_rules.get(name='SomeCertificateRule')
    ssh_placement_rule = features.placement_rules.get(name='SomeSSHRule')

    job = features.discovery.network.create(
        name='West Region Discovery',
        hosts=[
            '172.168.0.0/16',
            '192.168.123.0/24'
        ],
        ports=[80, 443, 22],  # If empty, the default is used. Check out the default in the source code.
        description='Discovery for certificates and SSH devices in the West Region.',
        contacts=['local:job-creator', 'local:west-region-team-lead'],
        default_certificate_location=r'\VED\Policy\Certificates\_Orphans',
        placement_rules=[certificate_placement_rule, ssh_placement_rule]
    )

Scheduling Network Discovery Jobs
*********************************

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Schedule this job to run at
    #  * 23:00 UTC
    #  * Every Saturday and Sunday
    #  * The 1st and 15th day of every month
    #  * May 31st
    features.discovery.network.schedule(
        job='West Region Discovery',
        hour=23,  # 24-Hour Format (11 PM) in UTC
        days_of_week=[0, 6],  # Sunday and Saturday, respectively
        days_of_month=[1, 15],
        days_of_year=['5/31']
    )

    # Blackout this job so that it does not run (or pauses) on
    #   * Mondays and Thursdays
    #   * 01:00 thru 04:00 UTC
    features.discovery.network.blackout_schedule(
        job='West Region Discovery',
        monday=list(range(1,4)),
        thursday=list(range(1, 4))
    )

    # Unschedule a job.
    features.discovery.network.unschedule(job='Deprecated Job')

Run, Pause, And Cancel Discovery Jobs
*************************************

.. warning::
    There is a known bug when running jobs using the WebSDK in that the job may actually fail to
    run and will return a "CacheEntryNotFound". There is currently no workaround, so the best
    way to avoid this problem is to schedule the job.

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    job = 'West Region Discovery'
    features.discovery.network.run_now(job=job)
    # Do some stuff...
    if features.discovery.network.is_in_progress(job=job):
        features.discovery.network.pause(job=job)
        # Do some stuff...
        features.discovery.network.resume(job=job)
    try:
        # Wait for 1 hour for the job to complete.
        features.discovery.network.wait_for_job_to_finish(job=job, timeout=(60 * 60))
    except TimeoutError:
        # Kill the job if it is running longer than expected.
        features.discovery.network.cancel(job=job)
        raise
