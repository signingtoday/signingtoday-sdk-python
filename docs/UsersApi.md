# signing_today_client.UsersApi

All URIs are relative to *https://web.sandbox.signingtoday.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_id_delete**](UsersApi.md#user_id_delete) | **DELETE** /user/{id} | Enable or disable a User
[**user_id_get**](UsersApi.md#user_id_get) | **GET** /user/{id} | Retrieve a User
[**user_id_identities_get**](UsersApi.md#user_id_identities_get) | **GET** /user/{id}/identities | Retrieve User identities
[**user_id_put**](UsersApi.md#user_id_put) | **PUT** /user/{id} | Update a User
[**user_id_role_put**](UsersApi.md#user_id_role_put) | **PUT** /user/{id}/role | Change the User role
[**users_get**](UsersApi.md#users_get) | **GET** /users | Retrieve Users
[**users_groups_get**](UsersApi.md#users_groups_get) | **GET** /users/groups | Retrieve UserGroups
[**users_groups_post**](UsersApi.md#users_groups_post) | **POST** /users/groups | Create a new UserGroups
[**users_post**](UsersApi.md#users_post) | **POST** /users | Create a new User


# **user_id_delete**
> user_id_delete(id, enabled=enabled)

Enable or disable a User

This API allows to **enable** or **disable** a User account. 

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
    api_instance = signing_today_client.UsersApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_
enabled = False # bool | This is a _boolean_ parameter. If true the User is **enabled**  (optional) (default to False)

    try:
        # Enable or disable a User
        api_instance.user_id_delete(id, enabled=enabled)
    except ApiException as e:
        print("Exception when calling UsersApi->user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 
 **enabled** | **bool**| This is a _boolean_ parameter. If true the User is **enabled**  | [optional] [default to False]

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

# **user_id_get**
> User user_id_get(id)

Retrieve a User

This API allows to retrieve a User.

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
    api_instance = signing_today_client.UsersApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_

    try:
        # Retrieve a User
        api_response = api_instance.user_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 

### Return type

[**User**](User.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The data matching the selection parameters. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_id_identities_get**
> list[Identity] user_id_identities_get(id)

Retrieve User identities

This API allows to retrieve user identities.

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
    api_instance = signing_today_client.UsersApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_

    try:
        # Retrieve User identities
        api_response = api_instance.user_id_identities_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->user_id_identities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 

### Return type

[**list[Identity]**](Identity.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The identities associated to the user. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_id_put**
> user_id_put(id, user)

Update a User

This API allows to update a User.

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
    api_instance = signing_today_client.UsersApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_
user = signing_today_client.User() # User | User replacing current object.

    try:
        # Update a User
        api_instance.user_id_put(id, user)
    except ApiException as e:
        print("Exception when calling UsersApi->user_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 
 **user** | [**User**](User.md)| User replacing current object. | 

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

# **user_id_role_put**
> user_id_role_put(id, new_role)

Change the User role

This API allows to change the permissions associated to the users, (**capabilities**) according to predefined user roles. 

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
    api_instance = signing_today_client.UsersApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_
new_role = 'instructor' # str | The new **role** of the User. Allowed values are **admin**, **instructor**, **signer** 

    try:
        # Change the User role
        api_instance.user_id_role_put(id, new_role)
    except ApiException as e:
        print("Exception when calling UsersApi->user_id_role_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 
 **new_role** | **str**| The new **role** of the User. Allowed values are **admin**, **instructor**, **signer**  | 

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
**400** | Result of a client passing incorrect or invalid data. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get**
> UsersGetResponse users_get(top=top, skip=skip, count=count, order_by=order_by, filter=filter)

Retrieve Users

This allows to get the list of the Users of an Organization.

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
    api_instance = signing_today_client.UsersApi(api_client)
    top = 32 # int | A number of results to return. Applied after **$skip**  (optional)
skip = 64 # int | An offset into the collection of results (optional)
count = true # bool | If true, the server includes the count of all the items in the response  (optional)
order_by = '$orderBy=updatedAt' # str | An ordering definition (eg. $orderBy=updatedAt,desc) (optional)
filter = '$filter=name==\"Milk\"' # str | A filter definition (eg. $filter=name == \"Milk\" or surname == \"Bread\") (optional)

    try:
        # Retrieve Users
        api_response = api_instance.users_get(top=top, skip=skip, count=count, order_by=order_by, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **top** | **int**| A number of results to return. Applied after **$skip**  | [optional] 
 **skip** | **int**| An offset into the collection of results | [optional] 
 **count** | **bool**| If true, the server includes the count of all the items in the response  | [optional] 
 **order_by** | **str**| An ordering definition (eg. $orderBy&#x3D;updatedAt,desc) | [optional] 
 **filter** | **str**| A filter definition (eg. $filter&#x3D;name &#x3D;&#x3D; \&quot;Milk\&quot; or surname &#x3D;&#x3D; \&quot;Bread\&quot;) | [optional] 

### Return type

[**UsersGetResponse**](UsersGetResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The data matching the selection parameters. |  -  |
**400** | Result of a client passing incorrect or invalid data. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_groups_get**
> UserGroupGetResponse users_groups_get(top=top, skip=skip, count=count, order_by=order_by, filter=filter)

Retrieve UserGroups

This API allows to get the list of the UserGroups.

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
    api_instance = signing_today_client.UsersApi(api_client)
    top = 32 # int | A number of results to return. Applied after **$skip**  (optional)
skip = 64 # int | An offset into the collection of results (optional)
count = true # bool | If true, the server includes the count of all the items in the response  (optional)
order_by = '$orderBy=updatedAt' # str | An ordering definition (eg. $orderBy=updatedAt,desc) (optional)
filter = '$filter=name==\"Milk\"' # str | A filter definition (eg. $filter=name == \"Milk\" or surname == \"Bread\") (optional)

    try:
        # Retrieve UserGroups
        api_response = api_instance.users_groups_get(top=top, skip=skip, count=count, order_by=order_by, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->users_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **top** | **int**| A number of results to return. Applied after **$skip**  | [optional] 
 **skip** | **int**| An offset into the collection of results | [optional] 
 **count** | **bool**| If true, the server includes the count of all the items in the response  | [optional] 
 **order_by** | **str**| An ordering definition (eg. $orderBy&#x3D;updatedAt,desc) | [optional] 
 **filter** | **str**| A filter definition (eg. $filter&#x3D;name &#x3D;&#x3D; \&quot;Milk\&quot; or surname &#x3D;&#x3D; \&quot;Bread\&quot;) | [optional] 

### Return type

[**UserGroupGetResponse**](UserGroupGetResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The data matching the selection parameters. |  -  |
**400** | Result of a client passing incorrect or invalid data. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_groups_post**
> users_groups_post(user_group)

Create a new UserGroups

This API allows to create a new UserGroups.

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
    api_instance = signing_today_client.UsersApi(api_client)
    user_group = [signing_today_client.UserGroup()] # list[UserGroup] | UserGroup list to be added.

    try:
        # Create a new UserGroups
        api_instance.users_groups_post(user_group)
    except ApiException as e:
        print("Exception when calling UsersApi->users_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group** | [**list[UserGroup]**](UserGroup.md)| UserGroup list to be added. | 

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

# **users_post**
> str users_post(create_user_request)

Create a new User

This API allows to create a new User.

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
    api_instance = signing_today_client.UsersApi(api_client)
    create_user_request = signing_today_client.CreateUserRequest() # CreateUserRequest | 

    try:
        # Create a new User
        api_response = api_instance.users_post(create_user_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_request** | [**CreateUserRequest**](CreateUserRequest.md)|  | 

### Return type

**str**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request has been satisfyied, new resource created. |  -  |
**400** | Result of a client passing incorrect or invalid data. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

