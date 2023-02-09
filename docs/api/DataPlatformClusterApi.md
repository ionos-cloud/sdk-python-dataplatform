# DataPlatformClusterApi

All URIs are relative to *https://api.ionos.com/dataplatform*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**create_cluster**](DataPlatformClusterApi.md#create_cluster) | **POST** /clusters | Create a DataPlatformCluster |
| [**delete_cluster**](DataPlatformClusterApi.md#delete_cluster) | **DELETE** /clusters/{clusterId} | Delete DataPlatformCluster |
| [**get_cluster**](DataPlatformClusterApi.md#get_cluster) | **GET** /clusters/{clusterId} | Retrieve a DataPlatformCluster |
| [**get_cluster_kubeconfig**](DataPlatformClusterApi.md#get_cluster_kubeconfig) | **GET** /clusters/{clusterId}/kubeconfig | Read the kubeconfig |
| [**get_clusters**](DataPlatformClusterApi.md#get_clusters) | **GET** /clusters | List DataPlatformCluster |
| [**patch_cluster**](DataPlatformClusterApi.md#patch_cluster) | **PATCH** /clusters/{clusterId} | Partially modify a DataPlatformCluster |


# **create_cluster**
> ClusterResponseData create_cluster(create_cluster_request)

Create a DataPlatformCluster

Creates a new DataPlatformCluster.  The cluster will be provisioned in the datacenter matching the provided `datacenterID`. Therefore the datacenter must be created upfront and must be accessible by the user issuing the request.  To create a new virtual datacenter (VDC) [see](https://api.ionos.com/docs/cloud/v6/#Data-centers-post-datacenters). 

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
        api_response = api_instance.create_cluster(create_cluster_request)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformClusterApi.create_cluster: %s\n' % e)
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

# **delete_cluster**
> ClusterResponseData delete_cluster(cluster_id)

Delete DataPlatformCluster

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
        # Delete DataPlatformCluster
        api_response = api_instance.delete_cluster(cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformClusterApi.delete_cluster: %s\n' % e)
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

# **get_cluster**
> ClusterResponseData get_cluster(cluster_id)

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
        api_response = api_instance.get_cluster(cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformClusterApi.get_cluster: %s\n' % e)
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

# **get_cluster_kubeconfig**
> str get_cluster_kubeconfig(cluster_id)

Read the kubeconfig

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
        # Read the kubeconfig
        api_response = api_instance.get_cluster_kubeconfig(cluster_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformClusterApi.get_cluster_kubeconfig: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cluster_id** | [**str**](../models/.md)| The unique ID of the cluster. Must conform to the UUID format.  |  |

### Return type

**str**

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **get_clusters**
> ClusterListResponseData get_clusters(name=name)

List DataPlatformCluster

List all available DataPlatformCluster that can be accessed by the user.  The user might filter the request for the name of the DataPlatformCluster. If no cluster is available matching the request, the list will be empty. 

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
        # List DataPlatformCluster
        api_response = api_instance.get_clusters()
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformClusterApi.get_clusters: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **str**| Response filter to list only the clusters which include the specified name. The value is case insensitive and matched on the &#x60;name&#x60; property of the cluster. The input is limited to 63 characters with alphanumeric character ([a-z0-9A-Z]) dashes (-), underscores (_), dots (.), and alphanumerics allowed.  | [optional]  |

### Return type

[**ClusterListResponseData**](../models/ClusterListResponseData.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **patch_cluster**
> ClusterResponseData patch_cluster(cluster_id, patch_cluster_request)

Partially modify a DataPlatformCluster

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
        # Partially modify a DataPlatformCluster
        api_response = api_instance.patch_cluster(cluster_id, patch_cluster_request)
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformClusterApi.patch_cluster: %s\n' % e)
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

