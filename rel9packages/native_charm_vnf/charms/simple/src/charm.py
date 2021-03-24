#!/usr/bin/env python3
##
# Copyright 2020 Canonical Ltd.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
##

import sys
import subprocess

sys.path.append("lib")

from ops.charm import CharmBase
from ops.main import main
from ops.model import ActiveStatus

class MyNativeCharm(CharmBase):

    def __init__(self, framework, key):
        super().__init__(framework, key)

        # Listen to charm events
        self.framework.observe(self.on.config_changed, self.on_config_changed)
        self.framework.observe(self.on.install, self.on_install)
        self.framework.observe(self.on.start, self.on_start)

        # Listen to the touch action event
        self.framework.observe(self.on.touch_action, self.on_touch_action)

    def on_config_changed(self, event):
        """Handle changes in configuration"""
        self.model.unit.status = ActiveStatus()

    def on_install(self, event):
        """Called when the charm is being installed"""
        self.model.unit.status = ActiveStatus()

    def on_start(self, event):
        """Called when the charm is being started"""
        self.model.unit.status = ActiveStatus()

    def on_touch_action(self, event):
        """Touch a file."""

        filename = event.params["filename"]
        try:
            subprocess.run(["touch", filename], check=True)
            event.set_results({"created": True, "filename": filename})
        except subprocess.CalledProcessError as e:
            event.fail("Action failed: {}".format(e))
        self.model.unit.status = ActiveStatus()


if __name__ == "__main__":
    main(MyNativeCharm)

