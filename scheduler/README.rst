Python Client for Cloud Scheduler API
================================================

|GA| |pypi| |versions| |compat_check_pypi| |compat_check_github|

`Cloud Scheduler API`_: Creates and manages jobs run on a regular recurring schedule.

- `Client Library Documentation`_
- `Product Documentation`_

.. |GA| image:: https://img.shields.io/badge/support-GA-gold.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/master/README.rst#general-availability
.. |pypi| image:: https://img.shields.io/pypi/v/google-cloud-scheduler.svg
   :target: https://pypi.org/project/google-cloud-scheduler/
.. |versions| image:: https://img.shields.io/pypi/pyversions/google-cloud-scheduler.svg
   :target: https://pypi.org/project/google-cloud-scheduler/
.. |compat_check_pypi| image:: https://python-compatibility-tools.appspot.com/one_badge_image?package=google-cloud-scheduler
   :target: https://python-compatibility-tools.appspot.com/one_badge_target?package=google-cloud-scheduler
.. |compat_check_github| image:: https://python-compatibility-tools.appspot.com/one_badge_image?package=git%2Bgit%3A//github.com/googleapis/google-cloud-python.git%23subdirectory%3Dscheduler
   :target: https://python-compatibility-tools.appspot.com/one_badge_target?package=git%2Bgit%3A//github.com/googleapis/google-cloud-python.git%23subdirectory%3Dscheduler
.. _Cloud Scheduler API: https://cloud.google.com/scheduler
.. _Client Library Documentation: https://googleapis.github.io/google-cloud-python/latest/scheduler/index.html
.. _Product Documentation:  https://cloud.google.com/scheduler

Quick Start
-----------

In order to use this library, you first need to go through the following steps:

1. `Select or create a Cloud Platform project.`_
2. `Enable billing for your project.`_
3. `Enable the Cloud Scheduler API.`_
4. `Setup Authentication.`_

.. _Select or create a Cloud Platform project.: https://console.cloud.google.com/project
.. _Enable billing for your project.: https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project
.. _Enable the Cloud Scheduler API.:  https://cloud.google.com/scheduler
.. _Setup Authentication.: https://googleapis.github.io/google-cloud-python/latest/core/auth.html

Installation
~~~~~~~~~~~~

Install this library in a `virtualenv`_ using pip. `virtualenv`_ is a tool to
create isolated Python environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With `virtualenv`_, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

.. _`virtualenv`: https://virtualenv.pypa.io/en/latest/


Supported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^
Python >= 3.5

Deprecated Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^^
Python == 2.7. Python 2.7 support will be removed on January 1, 2020.


Mac/Linux
^^^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install google-cloud-scheduler


Windows
^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install google-cloud-scheduler

Next Steps
~~~~~~~~~~

-  Read the `Client Library Documentation`_ for Cloud Scheduler API
   API to see other available methods on the client.
-  Read the `Cloud Scheduler API Product documentation`_ to learn
   more about the product and see How-to Guides.
-  View this `repository’s main README`_ to see the full list of Cloud
   APIs that we cover.

.. _Cloud Scheduler API Product documentation:  https://cloud.google.com/scheduler
.. _repository’s main README: https://github.com/googleapis/google-cloud-python/blob/master/README.rst
