# CreateNodePoolProperties

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | The name of your node pool. Must be 63 characters or less and must begin and end with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between.  |  |
| **node_count** | **int** | The number of nodes that make up the node pool.  |  |
| **cpu_family** | **str** | A valid CPU family name or &#x60;AUTO&#x60; if the platform shall choose the best fitting option. Available CPU architectures can be retrieved from the data center resource.  | [optional] [default to 'AUTO'] |
| **cores_count** | **int** | The number of CPU cores per node.  | [optional] [default to 4] |
| **ram_size** | **int** | The RAM size for one node in MB. Must be set in multiples of 1024 MB, with a minimum size is of 2048 MB. | [optional] [default to 4096] |
| **availability_zone** | [**AvailabilityZone**](AvailabilityZone.md) |  | [optional]  |
| **storage_type** | [**StorageType**](StorageType.md) |  | [optional]  |
| **storage_size** | **int** | The size of the volume in GB. The size must be greater than 10 GB. | [optional] [default to 20] |
| **maintenance_window** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional]  |
| **labels** | **object** | Key-value pairs attached to the node pool resource as [Kubernetes labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)  | [optional]  |
| **annotations** | **object** | Key-value pairs attached to node pool resource as [Kubernetes annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)  | [optional]  |


