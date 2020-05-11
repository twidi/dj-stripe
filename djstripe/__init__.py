"""
.. module:: djstripe.

  :synopsis: dj-stripe - Django + Stripe Made Easy
"""
import pkg_resources
from . import checks  # noqa: Register the checks


__version__ = pkg_resources.require("dj-stripe-isshub")[0].version
