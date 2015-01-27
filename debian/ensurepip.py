#!/usr/bin/env python2
import sys

_ENSUREPIP_DISABLED_MSG = """\
ensurepip is disabled in Ubuntu for Python %s.%s.%s. Python modules are usually
handled by dpkg and apt-get:

    sudo apt-get install python-<module name>

Install the python-pip package to use pip itself.  Using pip together
with the system python might have unexpected results for any system installed
module, so use it on your own risk, or make sure to only use it in virtual
environments.
""" % sys.version_info[:3]

def _ensurepip_disabled():
    raise RuntimeError(_ENSUREPIP_DISABLED_MSG)

def version():
    _ensurepip_disabled()

def bootstrap(*args, **kwargs):
    _ensurepip_disabled()

if __name__ == "__main__":
    print _ENSUREPIP_DISABLED_MSG
    sys.exit(1)
