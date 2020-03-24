# signing_today_client.Bit4idPathgroupResourcesApi

All URIs are relative to *https://web.sandbox.signingtoday.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_st_id_resources_get**](Bit4idPathgroupResourcesApi.md#d_st_id_resources_get) | **GET** /DST/{id}/resources | Retrieve all resources associated to a DST
[**d_st_id_resources_patch**](Bit4idPathgroupResourcesApi.md#d_st_id_resources_patch) | **PATCH** /DST/{id}/resources | Append a new resource to a DST
[**d_st_resource_id_delete**](Bit4idPathgroupResourcesApi.md#d_st_resource_id_delete) | **DELETE** /DST/resource/{id} | Delete a Resource
[**resource_id_get**](Bit4idPathgroupResourcesApi.md#resource_id_get) | **GET** /resource/{id} | Retrieve a Resource
[**resource_id_put**](Bit4idPathgroupResourcesApi.md#resource_id_put) | **PUT** /resource/{id} | Update a Resource
[**user_id_identity_identity_id_appearance_delete**](Bit4idPathgroupResourcesApi.md#user_id_identity_identity_id_appearance_delete) | **DELETE** /user/{id}/identity/{identity-id}/appearance | Delete a user appearance resource.
[**user_id_identity_identity_id_appearance_get**](Bit4idPathgroupResourcesApi.md#user_id_identity_identity_id_appearance_get) | **GET** /user/{id}/identity/{identity-id}/appearance | Download an identity appearance resource
[**user_id_identity_identity_id_appearance_post**](Bit4idPathgroupResourcesApi.md#user_id_identity_identity_id_appearance_post) | **POST** /user/{id}/identity/{identity-id}/appearance | Add a graphical appearance to a user&#39;s identity


# **d_st_id_resources_get**
> file d_st_id_resources_get(id)

Retrieve all resources associated to a DST

This API allows to retrieve all resources associated to a DST.

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import signing_today_client
from signing_today_client.rest import ApiException
from pprint import pprint
configuration = signing_today_client.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://web.sandbox.signingtoday.com/api
configuration.host = "https://web.sandbox.signingtoday.com/api"
# Enter a context with an instance of the API client
with signing_today_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signing_today_client.Bit4idPathgroupResourcesApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_

    try:
        # Retrieve all resources associated to a DST
        api_response = api_instance.d_st_id_resources_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupResourcesApi->d_st_id_resources_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response body contains all resources associated to a DST into a zip file. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_st_id_resources_patch**
> DigitalSignatureTransaction d_st_id_resources_patch(id, file, filename, resource_type, title=title)

Append a new resource to a DST

This API allows to append a new Resource to a DST.

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import signing_today_client
from signing_today_client.rest import ApiException
from pprint import pprint
configuration = signing_today_client.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://web.sandbox.signingtoday.com/api
configuration.host = "https://web.sandbox.signingtoday.com/api"
# Enter a context with an instance of the API client
with signing_today_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signing_today_client.Bit4idPathgroupResourcesApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_
file = '/path/to/file' # file | The file to upload
filename = 'filename_example' # str | The name of the file
resource_type = 'resource_type_example' # str | 
title = 'title_example' # str | User-defined title of the resource. (optional)

    try:
        # Append a new resource to a DST
        api_response = api_instance.d_st_id_resources_patch(id, file, filename, resource_type, title=title)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupResourcesApi->d_st_id_resources_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 
 **file** | **file**| The file to upload | 
 **filename** | **str**| The name of the file | 
 **resource_type** | **str**|  | 
 **title** | **str**| User-defined title of the resource. | [optional] 

### Return type

[**DigitalSignatureTransaction**](DigitalSignatureTransaction.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The DST patched with the new resource. |  -  |
**400** | Result of a client passing incorrect or invalid data. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_st_resource_id_delete**
> DigitalSignatureTransaction d_st_resource_id_delete(id)

Delete a Resource

This API allows to delete a Resource.

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import signing_today_client
from signing_today_client.rest import ApiException
from pprint import pprint
configuration = signing_today_client.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://web.sandbox.signingtoday.com/api
configuration.host = "https://web.sandbox.signingtoday.com/api"
# Enter a context with an instance of the API client
with signing_today_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signing_today_client.Bit4idPathgroupResourcesApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_

    try:
        # Delete a Resource
        api_response = api_instance.d_st_resource_id_delete(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupResourcesApi->d_st_resource_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 

### Return type

[**DigitalSignatureTransaction**](DigitalSignatureTransaction.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The DST Updated. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_id_get**
> file resource_id_get(id)

Retrieve a Resource

This API allows to retrieve a Resource.

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import signing_today_client
from signing_today_client.rest import ApiException
from pprint import pprint
configuration = signing_today_client.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://web.sandbox.signingtoday.com/api
configuration.host = "https://web.sandbox.signingtoday.com/api"
# Enter a context with an instance of the API client
with signing_today_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signing_today_client.Bit4idPathgroupResourcesApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_

    try:
        # Retrieve a Resource
        api_response = api_instance.resource_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupResourcesApi->resource_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response is the binary resource file content. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_id_put**
> resource_id_put(id, lf_resource)

Update a Resource

This API allows to update a Resource.

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import signing_today_client
from signing_today_client.rest import ApiException
from pprint import pprint
configuration = signing_today_client.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://web.sandbox.signingtoday.com/api
configuration.host = "https://web.sandbox.signingtoday.com/api"
# Enter a context with an instance of the API client
with signing_today_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signing_today_client.Bit4idPathgroupResourcesApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_
lf_resource = signing_today_client.LFResource() # LFResource | Resource replacing current object.

    try:
        # Update a Resource
        api_instance.resource_id_put(id, lf_resource)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupResourcesApi->resource_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 
 **lf_resource** | [**LFResource**](LFResource.md)| Resource replacing current object. | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request has been satisfyied. No output. |  -  |
**400** | Result of a client passing incorrect or invalid data. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_id_identity_identity_id_appearance_delete**
> user_id_identity_identity_id_appearance_delete(id, identity_id)

Delete a user appearance resource.

This API allows to delete an identity appearance resource.

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import signing_today_client
from signing_today_client.rest import ApiException
from pprint import pprint
configuration = signing_today_client.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://web.sandbox.signingtoday.com/api
configuration.host = "https://web.sandbox.signingtoday.com/api"
# Enter a context with an instance of the API client
with signing_today_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signing_today_client.Bit4idPathgroupResourcesApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_
identity_id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The unique id of the _Identity_

    try:
        # Delete a user appearance resource.
        api_instance.user_id_identity_identity_id_appearance_delete(id, identity_id)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupResourcesApi->user_id_identity_identity_id_appearance_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 
 **identity_id** | [**str**](.md)| The unique id of the _Identity_ | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request has been satisfyied. No output. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_id_identity_identity_id_appearance_get**
> file user_id_identity_identity_id_appearance_get(id, identity_id)

Download an identity appearance resource

This API allows to get the identity appearance resource.

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import signing_today_client
from signing_today_client.rest import ApiException
from pprint import pprint
configuration = signing_today_client.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://web.sandbox.signingtoday.com/api
configuration.host = "https://web.sandbox.signingtoday.com/api"
# Enter a context with an instance of the API client
with signing_today_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signing_today_client.Bit4idPathgroupResourcesApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_
identity_id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The unique id of the _Identity_

    try:
        # Download an identity appearance resource
        api_response = api_instance.user_id_identity_identity_id_appearance_get(id, identity_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupResourcesApi->user_id_identity_identity_id_appearance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 
 **identity_id** | [**str**](.md)| The unique id of the _Identity_ | 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response is the binary resource file content. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_id_identity_identity_id_appearance_post**
> LFResource user_id_identity_identity_id_appearance_post(id, identity_id, file, filename, resource_type, title=title)

Add a graphical appearance to a user's identity

This API allows to add a graphical appearance to the identity of a user.

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import signing_today_client
from signing_today_client.rest import ApiException
from pprint import pprint
configuration = signing_today_client.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://web.sandbox.signingtoday.com/api
configuration.host = "https://web.sandbox.signingtoday.com/api"
# Enter a context with an instance of the API client
with signing_today_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signing_today_client.Bit4idPathgroupResourcesApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_
identity_id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The unique id of the _Identity_
file = '/path/to/file' # file | The path of the file to upload
filename = 'filename_example' # str | The name of the file
resource_type = 'resource_type_example' # str | The type of the resource
title = 'title_example' # str | User-defined title of the resource (optional)

    try:
        # Add a graphical appearance to a user's identity
        api_response = api_instance.user_id_identity_identity_id_appearance_post(id, identity_id, file, filename, resource_type, title=title)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupResourcesApi->user_id_identity_identity_id_appearance_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 
 **identity_id** | [**str**](.md)| The unique id of the _Identity_ | 
 **file** | **file**| The path of the file to upload | 
 **filename** | **str**| The name of the file | 
 **resource_type** | **str**| The type of the resource | 
 **title** | **str**| User-defined title of the resource | [optional] 

### Return type

[**LFResource**](LFResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new created Resource |  -  |
**400** | Result of a client passing incorrect or invalid data. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

