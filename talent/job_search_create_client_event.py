# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START job_search_create_client_event]

from google.cloud import talent
from google.cloud.talent import enums
import six


def create_client_event(project_id, tenant_id, request_id, event_id):
    """
    Creates a client event

    Args:
      project_id Your Google Cloud Project ID
      tenant_id Identifier of the Tenant
      request_id A unique ID generated in the API responses.
      Value should be set to the request_id from an API response.
      event_id A unique identifier, generated by the client application
    """

    client = talent.EventServiceClient()

    # project_id = 'Your Google Cloud Project ID'
    # tenant_id = 'Your Tenant ID (using tenancy is optional)'
    # request_id = '[request_id from ResponseMetadata]'
    # event_id = '[Set this to a unique identifier]'

    if isinstance(project_id, bytes):
        project_id = project_id.decode("utf-8")
    if isinstance(tenant_id, bytes):
        tenant_id = tenant_id.decode("utf-8")
    if isinstance(request_id, bytes):
        request_id = request_id.decode("utf-8")
    if isinstance(event_id, bytes):
        event_id = event_id.decode("utf-8")
    parent = f"projects/{project_id}/tenants/{tenant_id}"

    # The timestamp of the event as seconds of UTC time since Unix epoch
    # For more information on how to create google.protobuf.Timestamps
    # See:
    # https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto
    seconds = 0
    create_time = {"seconds": seconds}

    # The type of event attributed to the behavior of the end user
    type_ = enums.JobEvent.JobEventType.VIEW

    # List of job names associated with this event
    jobs_element = "projects/[Project ID]/tenants/[Tenant ID]/jobs/[Job ID]"
    jobs_element_2 = "projects/[Project ID]/tenants/[Tenant ID]/jobs/[Job ID]"
    jobs = [jobs_element, jobs_element_2]
    job_event = {"type": type_, "jobs": jobs}
    client_event = {
        "request_id": request_id,
        "event_id": event_id,
        "create_time": create_time,
        "job_event": job_event,
    }

    response = client.create_client_event(parent=parent, client_event=client_event)
    print(response)


# [END job_search_create_client_event]
