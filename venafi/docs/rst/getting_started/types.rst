.. _types:

Types
=====

This module has a ``Types`` class for type hinting. The most common types are ``Config.Object`` and
``Identity.Identity``. Here is an example.

.. code-block:: python

	from typing import Optional
	from venafi import Types

	some_object_to_be_defined_later = None  # type: Optional[Types.Config.Object]
	some_identity_to_be_defined_later = None  # type: Optional[Types.Identity.Identity]

	def do_something(ident: 'Types.Identity.Identity', obj: 'Types.Config.Object') -> 'Types.Certificate.CertificateDetails':
		...
