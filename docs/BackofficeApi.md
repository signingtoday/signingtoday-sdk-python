# signing_today_client.BackofficeApi

All URIs are relative to *https://web.sandbox.signingtoday.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organization_id_alfresco_sync_get**](BackofficeApi.md#organization_id_alfresco_sync_get) | **GET** /organization/{id}/alfrescoSync | Sync all completed DSTs on Alfresco
[**organization_id_alfresco_sync_post**](BackofficeApi.md#organization_id_alfresco_sync_post) | **POST** /organization/{id}/alfrescoSync | Sync all completed DSTs on Alfresco
[**organization_id_delete**](BackofficeApi.md#organization_id_delete) | **DELETE** /organization/{id} | Enable or disable an Organization account.
[**organization_id_get**](BackofficeApi.md#organization_id_get) | **GET** /organization/{id} | Retrieve info on one organization
[**organization_id_public_get**](BackofficeApi.md#organization_id_public_get) | **GET** /organization/public | Retrieve public resources
[**organization_id_put**](BackofficeApi.md#organization_id_put) | **PUT** /organization/{id} | Update info on one organization
[**organization_id_resource_get**](BackofficeApi.md#organization_id_resource_get) | **GET** /organization/{id}/resource | Get an organization resource
[**organization_id_resource_put**](BackofficeApi.md#organization_id_resource_put) | **PUT** /organization/{id}/resource | Create or overwrite an organization resource
[**organization_resource_id_delete**](BackofficeApi.md#organization_resource_id_delete) | **DELETE** /organization/{id}/resource | Delete an organization resource
[**organization_resources_get**](BackofficeApi.md#organization_resources_get) | **GET** /organization/{id}/resources | List all the organization resources
[**organization_tags_get**](BackofficeApi.md#organization_tags_get) | **GET** /organization/tags | Retrieve organization tags
[**organizations_get**](BackofficeApi.md#organizations_get) | **GET** /organizations | Get the list of organizations
[**organizations_post**](BackofficeApi.md#organizations_post) | **POST** /organizations | Create a new organization


# **organization_id_alfresco_sync_get**
> AlfrescoSync organization_id_alfresco_sync_get(id)

Sync all completed DSTs on Alfresco

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
    api_instance = signing_today_client.BackofficeApi(api_client)
    id = 'test_id' # str | The value of the unique id

    try:
        # Sync all completed DSTs on Alfresco
        api_response = api_instance.organization_id_alfresco_sync_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackofficeApi->organization_id_alfresco_sync_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The value of the unique id | 

### Return type

[**AlfrescoSync**](AlfrescoSync.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | OK |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_id_alfresco_sync_post**
> organization_id_alfresco_sync_post(id, alfresco_sync)

Sync all completed DSTs on Alfresco

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
    api_instance = signing_today_client.BackofficeApi(api_client)
    id = 'test_id' # str | The value of the unique id
alfresco_sync = signing_today_client.AlfrescoSync() # AlfrescoSync | Domain associated to the account.

    try:
        # Sync all completed DSTs on Alfresco
        api_instance.organization_id_alfresco_sync_post(id, alfresco_sync)
    except ApiException as e:
        print("Exception when calling BackofficeApi->organization_id_alfresco_sync_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The value of the unique id | 
 **alfresco_sync** | [**AlfrescoSync**](AlfrescoSync.md)| Domain associated to the account. | 

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
**202** | OK |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_id_delete**
> organization_id_delete(id, enabled=enabled)

Enable or disable an Organization account.

Enable or disable an Organization.

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
    api_instance = signing_today_client.BackofficeApi(api_client)
    id = 'test_id' # str | The value of the unique id
enabled = False # bool | New status to set (optional) (default to False)

    try:
        # Enable or disable an Organization account.
        api_instance.organization_id_delete(id, enabled=enabled)
    except ApiException as e:
        print("Exception when calling BackofficeApi->organization_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The value of the unique id | 
 **enabled** | **bool**| New status to set | [optional] [default to False]

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

# **organization_id_get**
> Organization organization_id_get(id)

Retrieve info on one organization

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
    api_instance = signing_today_client.BackofficeApi(api_client)
    id = 'test_id' # str | The value of the unique id

    try:
        # Retrieve info on one organization
        api_response = api_instance.organization_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackofficeApi->organization_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The value of the unique id | 

### Return type

[**Organization**](Organization.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_id_public_get**
> file organization_id_public_get(res, id=id)

Retrieve public resources

### Example

```python
from __future__ import print_function
import time
import signing_today_client
from signing_today_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with signing_today_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = signing_today_client.BackofficeApi(api_client)
    res = 'logo' # str | resource id
id = '05ea656f-df69-49b1-a12b-9bf640c427c2' # str | organization id (optional)

    try:
        # Retrieve public resources
        api_response = api_instance.organization_id_public_get(res, id=id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackofficeApi->organization_id_public_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **res** | **str**| resource id | 
 **id** | **str**| organization id | [optional] 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource content. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_id_put**
> organization_id_put(id, organization=organization)

Update info on one organization

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
    api_instance = signing_today_client.BackofficeApi(api_client)
    id = 'test_id' # str | The value of the unique id
organization = signing_today_client.Organization() # Organization |  (optional)

    try:
        # Update info on one organization
        api_instance.organization_id_put(id, organization=organization)
    except ApiException as e:
        print("Exception when calling BackofficeApi->organization_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The value of the unique id | 
 **organization** | [**Organization**](Organization.md)|  | [optional] 

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
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_id_resource_get**
> file organization_id_resource_get(id, res_path)

Get an organization resource

Get an organization resource

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
    api_instance = signing_today_client.BackofficeApi(api_client)
    id = 'test_id' # str | The value of the unique id
res_path = '05ea656f-df69-49b1-a12b-9bf640c427c2' # str | 

    try:
        # Get an organization resource
        api_response = api_instance.organization_id_resource_get(id, res_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackofficeApi->organization_id_resource_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The value of the unique id | 
 **res_path** | **str**|  | 

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
**200** | An organization resource. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_id_resource_put**
> organization_id_resource_put(id, res_path, file)

Create or overwrite an organization resource

Create or overwrite an organization resource

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
    api_instance = signing_today_client.BackofficeApi(api_client)
    id = 'test_id' # str | The value of the unique id
res_path = '05ea656f-df69-49b1-a12b-9bf640c427c2' # str | 
file = '/path/to/file' # file | The file to upload.

    try:
        # Create or overwrite an organization resource
        api_instance.organization_id_resource_put(id, res_path, file)
    except ApiException as e:
        print("Exception when calling BackofficeApi->organization_id_resource_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The value of the unique id | 
 **res_path** | **str**|  | 
 **file** | **file**| The file to upload. | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request has been satisfyied. No output. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_resource_id_delete**
> organization_resource_id_delete(id, res_path)

Delete an organization resource

Deletes a Resource.

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
    api_instance = signing_today_client.BackofficeApi(api_client)
    id = 'test_id' # str | The value of the unique id
res_path = '05ea656f-df69-49b1-a12b-9bf640c427c2' # str | 

    try:
        # Delete an organization resource
        api_instance.organization_resource_id_delete(id, res_path)
    except ApiException as e:
        print("Exception when calling BackofficeApi->organization_resource_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The value of the unique id | 
 **res_path** | **str**|  | 

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
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_resources_get**
> list[str] organization_resources_get(id)

List all the organization resources

List all the organization resources.

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
    api_instance = signing_today_client.BackofficeApi(api_client)
    id = 'test_id' # str | The value of the unique id

    try:
        # List all the organization resources
        api_response = api_instance.organization_resources_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackofficeApi->organization_resources_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The value of the unique id | 

### Return type

**list[str]**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_tags_get**
> list[str] organization_tags_get()

Retrieve organization tags

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
    api_instance = signing_today_client.BackofficeApi(api_client)
    
    try:
        # Retrieve organization tags
        api_response = api_instance.organization_tags_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackofficeApi->organization_tags_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource content. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_get**
> OrganizationsGetResponse organizations_get(top=top, skip=skip, count=count, filter=filter)

Get the list of organizations

Get the list of organizations

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
    api_instance = signing_today_client.BackofficeApi(api_client)
    top = 32 # int | A number of results to return. Applied after **$skip**  (optional)
skip = 64 # int | An offset into the collection of results (optional)
count = true # bool | If true, the server includes the count of all the items in the response  (optional)
filter = '$filter=name==\"Milk\"' # str | A filter definition (eg. $filter=name == \"Milk\" or surname == \"Bread\") (optional)

    try:
        # Get the list of organizations
        api_response = api_instance.organizations_get(top=top, skip=skip, count=count, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackofficeApi->organizations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **top** | **int**| A number of results to return. Applied after **$skip**  | [optional] 
 **skip** | **int**| An offset into the collection of results | [optional] 
 **count** | **bool**| If true, the server includes the count of all the items in the response  | [optional] 
 **filter** | **str**| A filter definition (eg. $filter&#x3D;name &#x3D;&#x3D; \&quot;Milk\&quot; or surname &#x3D;&#x3D; \&quot;Bread\&quot;) | [optional] 

### Return type

[**OrganizationsGetResponse**](OrganizationsGetResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of organizations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_post**
> organizations_post(organization=organization)

Create a new organization

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
    api_instance = signing_today_client.BackofficeApi(api_client)
    organization = signing_today_client.Organization() # Organization |  (optional)

    try:
        # Create a new organization
        api_instance.organizations_post(organization=organization)
    except ApiException as e:
        print("Exception when calling BackofficeApi->organizations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | [**Organization**](Organization.md)|  | [optional] 

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
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

