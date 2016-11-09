# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command for deleting snapshots."""
from googlecloudsdk.api_lib.compute import base_classes


class Delete(base_classes.GlobalDeleter):
  """Delete Google Compute Engine snapshots."""

  @staticmethod
  def Args(parser):
    base_classes.GlobalDeleter.Args(parser, 'compute.snapshots')

  @property
  def service(self):
    return self.compute.snapshots

  @property
  def resource_type(self):
    return 'snapshots'


Delete.detailed_help = {
    'brief': 'Delete Google Compute Engine snapshots',
    'DESCRIPTION': """\
        *{command}* deletes one or more Google Compute Engine snapshots.
        """,
}