# DataPlatformMetaDataApi

All URIs are relative to *https://api.ionos.com/dataplatform*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**versions_get**](DataPlatformMetaDataApi.md#versions_get) | **GET** /versions | Managed Stackable Data Platform API Versions |


# **versions_get**
> list[str] versions_get()

Managed Stackable Data Platform API Versions

Retrieves all available versions of the Managed Stackable Data Platform.

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
    api_instance = ionoscloud_dataplatform.DataPlatformMetaDataApi(api_client)
    try:
        # Managed Stackable Data Platform API Versions
        api_response = api_instance.versions_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling DataPlatformMetaDataApi.versions_get: %s\n' % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

