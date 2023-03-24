# DataPlatformNodePoolApi

All URIs are relative to *https://api.ionos.com/dataplatform*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**clusters_nodepools_delete**](DataPlatformNodePoolApi.md#clusters_nodepools_delete) | **DELETE** /clusters/{clusterId}/nodepools/{nodepoolId} | Remove a DataPlatformNodePool from a DataPlatformCluster |
| [**clusters_nodepools_find_by_id**](DataPlatformNodePoolApi.md#clusters_nodepools_find_by_id) | **GET** /clusters/{clusterId}/nodepools/{nodepoolId} | Retrieve a DataPlatformNodePool |
| [**clusters_nodepools_get**](DataPlatformNodePoolApi.md#clusters_nodepools_get) | **GET** /clusters/{clusterId}/nodepools | List the DataPlatformNodePools of a DataPlatformCluster |
| [**clusters_nodepools_patch**](DataPlatformNodePoolApi.md#clusters_nodepools_patch) | **PATCH** /clusters/{clusterId}/nodepools/{nodepoolId} | Partially Modify a DataPlatformNodePool |
| [**clusters_nodepools_post**](DataPlatformNodePoolApi.md#clusters_nodepools_post) | **POST** /clusters/{clusterId}/nodepools | Create a DataPlatformNodePool for a distinct DataPlatformCluster |


# **clusters_nodepools_delete**
> NodePoolResponseData clusters_nodepools_delete(cluster_id, nodepool_id)

Remove a DataPlatformNodePool from a DataPlatformCluster

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
        # Remove a DataPlatformNodePool from a DataPlatformCluster
        api_response = api_instance.clusters_nodepools_delete(cluster_id, nodepool_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformNodePoolApi.clusters_nodepools_delete: %s\n' % e)
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

# **clusters_nodepools_find_by_id**
> NodePoolResponseData clusters_nodepools_find_by_id(cluster_id, nodepool_id)

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
        api_response = api_instance.clusters_nodepools_find_by_id(cluster_id, nodepool_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformNodePoolApi.clusters_nodepools_find_by_id: %s\n' % e)
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

# **clusters_nodepools_get**
> NodePoolListResponseData clusters_nodepools_get(cluster_id)

List the DataPlatformNodePools of a DataPlatformCluster

List all node pools assigned to the specified DataPlatformCluster by its ID.  The cluster ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters. 

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
        # List the DataPlatformNodePools of a DataPlatformCluster
        api_response = api_instance.clusters_nodepools_get(cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformNodePoolApi.clusters_nodepools_get: %s\n' % e)
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

# **clusters_nodepools_patch**
> NodePoolResponseData clusters_nodepools_patch(cluster_id, nodepool_id, patch_node_pool_request)

Partially Modify a DataPlatformNodePool

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
        # Partially Modify a DataPlatformNodePool
        api_response = api_instance.clusters_nodepools_patch(cluster_id, nodepool_id, patch_node_pool_request)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformNodePoolApi.clusters_nodepools_patch: %s\n' % e)
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

# **clusters_nodepools_post**
> NodePoolResponseData clusters_nodepools_post(cluster_id, create_node_pool_request)

Create a DataPlatformNodePool for a distinct DataPlatformCluster

Creates a new node pool and assigns the node pool resources exclusively to the defined managed cluster.  The cluster ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters. 

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
        api_response = api_instance.clusters_nodepools_post(cluster_id, create_node_pool_request)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformNodePoolApi.clusters_nodepools_post: %s\n' % e)
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

