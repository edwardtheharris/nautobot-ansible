#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


__metaclass__ = type

DOCUMENTATION = r"""
---
module: platform
short_description: Create or delete platforms within Nautobot
description:
  - Creates or removes platforms from Nautobot
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Mikhail Yohman (@FragmentedPacket)
version_added: "1.0.0"
extends_documentation_fragment:
  - networktocode.nautobot.fragments.base
options:
  name:
    description:
      - The name of the platform
    required: true
    type: str
    version_added: "3.0.0"
  description:
    description:
      - The description of the platform
    required: false
    type: str
    version_added: "3.0.0"
  manufacturer:
    description:
      - The manufacturer the platform will be tied to
    required: false
    type: raw
    version_added: "3.0.0"
  napalm_driver:
    description:
      - The name of the NAPALM driver to be used when using the NAPALM plugin
    required: false
    type: str
    version_added: "3.0.0"
  napalm_args:
    description:
      - The optional arguments used for NAPALM connections
    required: false
    type: dict
    version_added: "3.0.0"
"""

EXAMPLES = r"""
- name: "Test Nautobot modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create platform within Nautobot with only required information
      networktocode.nautobot.platform:
        url: http://nautobot.local
        token: thisIsMyToken
        name: Test Platform
        state: present

    - name: Create platform within Nautobot with only required information
      networktocode.nautobot.platform:
        url: http://nautobot.local
        token: thisIsMyToken
        name: Test Platform All
        manufacturer: Test Manufacturer
        napalm_driver: ios
        napalm_args:
          global_delay_factor: 2
        state: present

    - name: Delete platform within nautobot
      networktocode.nautobot.platform:
        url: http://nautobot.local
        token: thisIsMyToken
        name: Test Platform
        state: absent
"""

RETURN = r"""
platform:
  description: Serialized object as created or already existent within Nautobot
  returned: success (when I(state=present))
  type: dict
msg:
  description: Message indicating failure or info about what has been achieved
  returned: always
  type: str
"""

from ansible_collections.networktocode.nautobot.plugins.module_utils.utils import NAUTOBOT_ARG_SPEC
from ansible_collections.networktocode.nautobot.plugins.module_utils.dcim import (
    NautobotDcimModule,
    NB_PLATFORMS,
)
from ansible.module_utils.basic import AnsibleModule
from copy import deepcopy


def main():
    """
    Main entry point for module execution
    """
    argument_spec = deepcopy(NAUTOBOT_ARG_SPEC)
    argument_spec.update(
        dict(
            name=dict(required=True, type="str"),
            description=dict(required=False, type="str"),
            manufacturer=dict(required=False, type="raw"),
            napalm_driver=dict(required=False, type="str"),
            napalm_args=dict(required=False, type="dict"),
        )
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    platform = NautobotDcimModule(module, NB_PLATFORMS)
    platform.run()


if __name__ == "__main__":  # pragma: no cover
    main()
