# DataPlatformNodePoolApi

All URIs are relative to *https://api.ionos.com/dataplatform*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**create_cluster_nodepool**](DataPlatformNodePoolApi.md#create_cluster_nodepool) | **POST** /clusters/{clusterId}/nodepools | Create a DataPlatformNodePool for a distinct DataPlatformCluster |
| [**delete_cluster_nodepool**](DataPlatformNodePoolApi.md#delete_cluster_nodepool) | **DELETE** /clusters/{clusterId}/nodepools/{nodepoolId} | Remove node pool from DataPlatformCluster. |
| [**get_cluster_nodepool**](DataPlatformNodePoolApi.md#get_cluster_nodepool) | **GET** /clusters/{clusterId}/nodepools/{nodepoolId} | Retrieve a DataPlatformNodePool |
| [**get_cluster_nodepools**](DataPlatformNodePoolApi.md#get_cluster_nodepools) | **GET** /clusters/{clusterId}/nodepools | List the DataPlatformNodePools of a  DataPlatformCluster |
| [**patch_cluster_nodepool**](DataPlatformNodePoolApi.md#patch_cluster_nodepool) | **PATCH** /clusters/{clusterId}/nodepools/{nodepoolId} | Partially modify a DataPlatformNodePool |


# **create_cluster_nodepool**
> NodePoolResponseData create_cluster_nodepool(cluster_id, create_node_pool_request)

Create a DataPlatformNodePool for a distinct DataPlatformCluster

Creates a new node pool and assignes the node pool resources exclusively to the defined managed cluster.  The cluster ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters. 

### Example

```python
from __future__ import print_function
import time
import ionoscloud_dataplatform
from ionoscloud_dataplatform.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/dataplatform
configuration = ionoscloud_dataplatform.Configuration(
    host = 'https://api.ionos.com/dataplatform',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_dataplatform.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dataplatform.DataPlatformNodePoolApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster. Must conform to the UUID format. 
    create_node_pool_request = ionoscloud_dataplatform.CreateNodePoolRequest() # CreateNodePoolRequest | Request payload with the properties that defines a DataPlatformNodePool. 
    try:
        # Create a DataPlatformNodePool for a distinct DataPlatformCluster
        api_response = api_instance.create_cluster_nodepool(cluster_id, create_node_pool_request)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformNodePoolApi.create_cluster_nodepool: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | [**str**](../models/.md)| The unique ID of the cluster. Must conform to the UUID format.  |  |
| **create_node_pool_request** | [**CreateNodePoolRequest**](../models/CreateNodePoolRequest.md)| Request payload with the properties that defines a DataPlatformNodePool.  |  |

### Return type

[**NodePoolResponseData**](../models/NodePoolResponseData.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **delete_cluster_nodepool**
> NodePoolResponseData delete_cluster_nodepool(cluster_id, nodepool_id)

Remove node pool from DataPlatformCluster.

Removes the specified node pool from the specified DataPlatformCluster and deletes the node pool afterwards.  The cluster ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters.  The node pool ID can be found in the response when a node pool is created or when you GET a list of all node pools assigned to a specific DataPlatformCluster. 

### Example

```python
from __future__ import print_function
import time
import ionoscloud_dataplatform
from ionoscloud_dataplatform.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/dataplatform
configuration = ionoscloud_dataplatform.Configuration(
    host = 'https://api.ionos.com/dataplatform',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_dataplatform.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dataplatform.DataPlatformNodePoolApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster. Must conform to the UUID format. 
    nodepool_id = 'nodepool_id_example' # str | The unique ID of the node pool. Must conform to the UUID format. 
    try:
        # Remove node pool from DataPlatformCluster.
        api_response = api_instance.delete_cluster_nodepool(cluster_id, nodepool_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformNodePoolApi.delete_cluster_nodepool: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | [**str**](../models/.md)| The unique ID of the cluster. Must conform to the UUID format.  |  |
| **nodepool_id** | [**str**](../models/.md)| The unique ID of the node pool. Must conform to the UUID format.  |  |

### Return type

[**NodePoolResponseData**](../models/NodePoolResponseData.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **get_cluster_nodepool**
> NodePoolResponseData get_cluster_nodepool(cluster_id, nodepool_id)

Retrieve a DataPlatformNodePool

Retrieve a node pool belonging to a Kubernetes cluster running Stackable by using its ID.  The cluster ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters.  The node pool ID can be found in the response when a node pool is created or when you GET a list of all node pools assigned to a specific DataPlatformCluster. 

### Example

```python
from __future__ import print_function
import time
import ionoscloud_dataplatform
from ionoscloud_dataplatform.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/dataplatform
configuration = ionoscloud_dataplatform.Configuration(
    host = 'https://api.ionos.com/dataplatform',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_dataplatform.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dataplatform.DataPlatformNodePoolApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster. Must conform to the UUID format. 
    nodepool_id = 'nodepool_id_example' # str | The unique ID of the node pool. Must conform to the UUID format. 
    try:
        # Retrieve a DataPlatformNodePool
        api_response = api_instance.get_cluster_nodepool(cluster_id, nodepool_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformNodePoolApi.get_cluster_nodepool: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | [**str**](../models/.md)| The unique ID of the cluster. Must conform to the UUID format.  |  |
| **nodepool_id** | [**str**](../models/.md)| The unique ID of the node pool. Must conform to the UUID format.  |  |

### Return type

[**NodePoolResponseData**](../models/NodePoolResponseData.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **get_cluster_nodepools**
> NodePoolListResponseData get_cluster_nodepools(cluster_id)

List the DataPlatformNodePools of a  DataPlatformCluster

List all node pools assigned to the specified DataplatformCluster by its ID.  The cluster ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters. 

### Example

```python
from __future__ import print_function
import time
import ionoscloud_dataplatform
from ionoscloud_dataplatform.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/dataplatform
configuration = ionoscloud_dataplatform.Configuration(
    host = 'https://api.ionos.com/dataplatform',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_dataplatform.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dataplatform.DataPlatformNodePoolApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster. Must conform to the UUID format. 
    try:
        # List the DataPlatformNodePools of a  DataPlatformCluster
        api_response = api_instance.get_cluster_nodepools(cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformNodePoolApi.get_cluster_nodepools: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | [**str**](../models/.md)| The unique ID of the cluster. Must conform to the UUID format.  |  |

### Return type

[**NodePoolListResponseData**](../models/NodePoolListResponseData.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **patch_cluster_nodepool**
> NodePoolResponseData patch_cluster_nodepool(cluster_id, nodepool_id, patch_node_pool_request)

Partially modify a DataPlatformNodePool

Modifies the specified node pool of a DataPlatformCluster. Update selected attributes of a node pool belonging to a Kubernetes cluster running Stackable.  The fields in the request body are applied to the cluster. Note that the application to the node pool  itself is performed asynchronously. You can check the sync state by querying the node pool with the GET method.  The cluster ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters.  The node pool ID can be found in the response when a node pool is created or when you GET a list of all node pools assigned to a specific DataPlatformCluster. 

### Example

```python
from __future__ import print_function
import time
import ionoscloud_dataplatform
from ionoscloud_dataplatform.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/dataplatform
configuration = ionoscloud_dataplatform.Configuration(
    host = 'https://api.ionos.com/dataplatform',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_dataplatform.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dataplatform.DataPlatformNodePoolApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster. Must conform to the UUID format. 
    nodepool_id = 'nodepool_id_example' # str | The unique ID of the node pool. Must conform to the UUID format. 
    patch_node_pool_request = ionoscloud_dataplatform.PatchNodePoolRequest() # PatchNodePoolRequest | Request payload with the properties that shall be applied to an existing DataPlatformNodePool. 
    try:
        # Partially modify a DataPlatformNodePool
        api_response = api_instance.patch_cluster_nodepool(cluster_id, nodepool_id, patch_node_pool_request)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformNodePoolApi.patch_cluster_nodepool: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | [**str**](../models/.md)| The unique ID of the cluster. Must conform to the UUID format.  |  |
| **nodepool_id** | [**str**](../models/.md)| The unique ID of the node pool. Must conform to the UUID format.  |  |
| **patch_node_pool_request** | [**PatchNodePoolRequest**](../models/PatchNodePoolRequest.md)| Request payload with the properties that shall be applied to an existing DataPlatformNodePool.  |  |

### Return type

[**NodePoolResponseData**](../models/NodePoolResponseData.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

