# Metadata

Metadata of the resource
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **e_tag** | **str** | The Entity Tag of the resource as defined in http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.11 | [optional]  |
| **created_date** | **datetime** | The time the resource was created, ISO 8601 timestamp (UTC). | [optional]  |
| **created_by** | **str** | The user that created the resource | [optional]  |
| **created_by_user_id** | **str** | The ID of the user that created the resource | [optional]  |
| **created_in_contract_number** | **str** | The creators contractNumber | [optional]  |
| **last_modified_date** | **datetime** | The last time the resource was modified, ISO 8601 timestamp (UTC). | [optional]  |
| **last_modified_by** | **str** | The user that last modified the resource | [optional]  |
| **last_modified_by_user_id** | **str** | The ID of the user that last modified the resource | [optional]  |
| **current_data_platform_version** | **str** | The version of the DataPlatform.  | [optional]  |
| **current_data_platform_revision** | **int** | The current dataplatform revision of a resource. This internal revision is used to rollout non-breaking internal changes. This attribute is read-only.  | [optional]  |
| **available_upgrade_versions** | **list[str]** | List of available upgrades for this cluster | [optional]  |
| **state** | **str** | State of the resource. *AVAILABLE* There are no pending modification requests for this item; *BUSY* There is at least one modification request pending and all following requests will be queued; *DEPLOYING* Resource state DEPLOYING - the resource is being created; *FAILED* Resource state FAILED - creation of the resource failed; *UPDATING* Resource state UPDATING - the resource is being updated; *FAILED_UPDATING* Resource state FAILED_UPDATING - an update to the resource was not successful; *DESTROYING* Resource state DESTROYING - the resource is being deleted; *FAILED_DESTROYING* Resource state FAILED_DESTROYING - deletion of the resource was not successful; *TERMINATED* Resource state TERMINATED - the resource was deleted.  | [optional]  |


