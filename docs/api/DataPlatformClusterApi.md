# DataPlatformClusterApi

All URIs are relative to *https://api.ionos.com/dataplatform*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**clusters_delete**](DataPlatformClusterApi.md#clusters_delete) | **DELETE** /clusters/{clusterId} | Delete a DataPlatformCluster |
| [**clusters_find_by_id**](DataPlatformClusterApi.md#clusters_find_by_id) | **GET** /clusters/{clusterId} | Retrieve a DataPlatformCluster |
| [**clusters_get**](DataPlatformClusterApi.md#clusters_get) | **GET** /clusters | List the DataPlatformClusters |
| [**clusters_kubeconfig_find_by_cluster_id**](DataPlatformClusterApi.md#clusters_kubeconfig_find_by_cluster_id) | **GET** /clusters/{clusterId}/kubeconfig | Read the Kubeconfig |
| [**clusters_patch**](DataPlatformClusterApi.md#clusters_patch) | **PATCH** /clusters/{clusterId} | Partially Modify a DataPlatformCluster |
| [**clusters_post**](DataPlatformClusterApi.md#clusters_post) | **POST** /clusters | Create a DataPlatformCluster |


# **clusters_delete**
> ClusterResponseData clusters_delete(cluster_id)

Delete a DataPlatformCluster

Deletes the specified DataPlatformCluster by its distinct cluster ID.  The ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters. 

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
    api_instance = ionoscloud_dataplatform.DataPlatformClusterApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster. Must conform to the UUID format. 
    try:
        # Delete a DataPlatformCluster
        api_response = api_instance.clusters_delete(cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformClusterApi.clusters_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | [**str**](../models/.md)| The unique ID of the cluster. Must conform to the UUID format.  |  |

### Return type

[**ClusterResponseData**](../models/ClusterResponseData.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_find_by_id**
> ClusterResponseData clusters_find_by_id(cluster_id)

Retrieve a DataPlatformCluster

Retrieve the specified DataPlatformCluster by its distinct ID.  The cluster ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters. 

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
    api_instance = ionoscloud_dataplatform.DataPlatformClusterApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster. Must conform to the UUID format. 
    try:
        # Retrieve a DataPlatformCluster
        api_response = api_instance.clusters_find_by_id(cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformClusterApi.clusters_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | [**str**](../models/.md)| The unique ID of the cluster. Must conform to the UUID format.  |  |

### Return type

[**ClusterResponseData**](../models/ClusterResponseData.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_get**
> ClusterListResponseData clusters_get(name=name)

List the DataPlatformClusters

List all available DataPlatformClusters that can be accessed by the user.  The user might filter the request for the name of the DataPlatformCluster. If no cluster is available matching the request, the list will be empty. 

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
    api_instance = ionoscloud_dataplatform.DataPlatformClusterApi(api_client)
    try:
        # List the DataPlatformClusters
        api_response = api_instance.clusters_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformClusterApi.clusters_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **str**| Response filter to list only the clusters which include the specified name. The value is case insensitive and matched on the &#x60;name&#x60; property of the cluster. The input is limited to 63 characters with alphanumeric characters ([a-z0-9A-Z]), dashes (-), underscores (_), and dots (.) allowed.  | [optional]  |

### Return type

[**ClusterListResponseData**](../models/ClusterListResponseData.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_kubeconfig_find_by_cluster_id**
> object clusters_kubeconfig_find_by_cluster_id(cluster_id)

Read the Kubeconfig

Retrieves the Kubernetes configuration file (kubeconfig) for the specified DataPlatformCluster by its cluster ID.  The ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters. 

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
    api_instance = ionoscloud_dataplatform.DataPlatformClusterApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster. Must conform to the UUID format. 
    try:
        # Read the Kubeconfig
        api_response = api_instance.clusters_kubeconfig_find_by_cluster_id(cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformClusterApi.clusters_kubeconfig_find_by_cluster_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | [**str**](../models/.md)| The unique ID of the cluster. Must conform to the UUID format.  |  |

### Return type

**object**

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **clusters_patch**
> ClusterResponseData clusters_patch(cluster_id, patch_cluster_request)

Partially Modify a DataPlatformCluster

Modifies the specified DataPlatformCluster by its distinct cluster ID. The fields in the request body are applied to the cluster. Note that the application to the cluster itself is performed asynchronously. You can check the sync state by querying the cluster with the GET method.  The ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters. 

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
    api_instance = ionoscloud_dataplatform.DataPlatformClusterApi(api_client)
    cluster_id = 'cluster_id_example' # str | The unique ID of the cluster. Must conform to the UUID format. 
    patch_cluster_request = ionoscloud_dataplatform.PatchClusterRequest() # PatchClusterRequest | Request payload with the properties that shall be applied to an existing DataPlatformCluster. 
    try:
        # Partially Modify a DataPlatformCluster
        api_response = api_instance.clusters_patch(cluster_id, patch_cluster_request)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformClusterApi.clusters_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | [**str**](../models/.md)| The unique ID of the cluster. Must conform to the UUID format.  |  |
| **patch_cluster_request** | [**PatchClusterRequest**](../models/PatchClusterRequest.md)| Request payload with the properties that shall be applied to an existing DataPlatformCluster.  |  |

### Return type

[**ClusterResponseData**](../models/ClusterResponseData.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **clusters_post**
> ClusterResponseData clusters_post(create_cluster_request)

Create a DataPlatformCluster

Creates a new DataPlatformCluster.  The cluster will be provisioned in the data center matching the provided `datacenterID`. Therefore the data center must be created upfront and must be accessible by the user issuing the request.  To create a new virtual data center (VDC) [see](https://api.ionos.com/docs/cloud/v6/#Data-centers-post-datacenters). 

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
    api_instance = ionoscloud_dataplatform.DataPlatformClusterApi(api_client)
    create_cluster_request = ionoscloud_dataplatform.CreateClusterRequest() # CreateClusterRequest | Request payload with the properties that defines a new DataPlatformCluster and the credentials to interact with the PaaS API to create it. 
    try:
        # Create a DataPlatformCluster
        api_response = api_instance.clusters_post(create_cluster_request)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformClusterApi.clusters_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **create_cluster_request** | [**CreateClusterRequest**](../models/CreateClusterRequest.md)| Request payload with the properties that defines a new DataPlatformCluster and the credentials to interact with the PaaS API to create it.  |  |

### Return type

[**ClusterResponseData**](../models/ClusterResponseData.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

