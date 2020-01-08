# signing_today_client.Bit4idPathgroupUsersApi

All URIs are relative to *https://sandbox.signingtoday.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](Bit4idPathgroupUsersApi.md#create_user) | **POST** /{organization-id}/users | Create a user of the organization
[**get_user**](Bit4idPathgroupUsersApi.md#get_user) | **GET** /{organization-id}/users/{user-id} | Get information about an user
[**list_users**](Bit4idPathgroupUsersApi.md#list_users) | **GET** /{organization-id}/users | Enumerate the users of an organization
[**update_user**](Bit4idPathgroupUsersApi.md#update_user) | **PUT** /{organization-id}/users/{user-id} | Edit one or more user properties


# **create_user**
> InlineResponse2015 create_user(organization_id, create_user)

Create a user of the organization

This API allows to create a new user of the organization. 

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import signing_today_client
from signing_today_client.rest import ApiException
from pprint import pprint
configuration = signing_today_client.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://sandbox.signingtoday.com/api/v1
configuration.host = "https://sandbox.signingtoday.com/api/v1"
# Create an instance of the API class
api_instance = signing_today_client.Bit4idPathgroupUsersApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
create_user = signing_today_client.CreateUser() # CreateUser | The new user object to create

try:
    # Create a user of the organization
    api_response = api_instance.create_user(organization_id, create_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Bit4idPathgroupUsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **create_user** | [**CreateUser**](CreateUser.md)| The new user object to create | 

### Return type

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> InlineResponse2015 get_user(organization_id, user_id)

Get information about an user

This API allows to get information about an user. 

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import signing_today_client
from signing_today_client.rest import ApiException
from pprint import pprint
configuration = signing_today_client.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://sandbox.signingtoday.com/api/v1
configuration.host = "https://sandbox.signingtoday.com/api/v1"
# Create an instance of the API class
api_instance = signing_today_client.Bit4idPathgroupUsersApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
user_id = signing_today_client.Id() # Id | The **user-id** is the uuid code that identifies a user of an organization. It is used as a path parameter to restrict the requested operation to the scope of that user 

try:
    # Get information about an user
    api_response = api_instance.get_user(organization_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Bit4idPathgroupUsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **user_id** | [**Id**](.md)| The **user-id** is the uuid code that identifies a user of an organization. It is used as a path parameter to restrict the requested operation to the scope of that user  | 

### Return type

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> InlineResponse20012 list_users(organization_id, where_membership_id=where_membership_id, where_email=where_email, where_last_name=where_last_name, where_first_name=where_first_name, page=page, count=count)

Enumerate the users of an organization

This API allows to enumerate the users of an organization. 

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import signing_today_client
from signing_today_client.rest import ApiException
from pprint import pprint
configuration = signing_today_client.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://sandbox.signingtoday.com/api/v1
configuration.host = "https://sandbox.signingtoday.com/api/v1"
# Create an instance of the API class
api_instance = signing_today_client.Bit4idPathgroupUsersApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
where_membership_id = 'jdo' # str | Returns the users that have the specified id (optional)
where_email = 'test@mail.com' # str | Returns the users that have the specified email (optional)
where_last_name = 'Doe' # str | Returns the users that have the specified last name (optional)
where_first_name = 'John' # str | Returns the users that have the specified first name (optional)
page = 1 # int | Restricts the search to the chosen page (optional)
count = 100 # int | Sets the number of users per page to display (optional) (default to 100)

try:
    # Enumerate the users of an organization
    api_response = api_instance.list_users(organization_id, where_membership_id=where_membership_id, where_email=where_email, where_last_name=where_last_name, where_first_name=where_first_name, page=page, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Bit4idPathgroupUsersApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **where_membership_id** | **str**| Returns the users that have the specified id | [optional] 
 **where_email** | **str**| Returns the users that have the specified email | [optional] 
 **where_last_name** | **str**| Returns the users that have the specified last name | [optional] 
 **where_first_name** | **str**| Returns the users that have the specified first name | [optional] 
 **page** | **int**| Restricts the search to the chosen page | [optional] 
 **count** | **int**| Sets the number of users per page to display | [optional] [default to 100]

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> InlineResponse2015 update_user(organization_id, user_id, update_user)

Edit one or more user properties

This API allows to edit one or more user properties. 

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import signing_today_client
from signing_today_client.rest import ApiException
from pprint import pprint
configuration = signing_today_client.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://sandbox.signingtoday.com/api/v1
configuration.host = "https://sandbox.signingtoday.com/api/v1"
# Create an instance of the API class
api_instance = signing_today_client.Bit4idPathgroupUsersApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
user_id = signing_today_client.Id() # Id | The **user-id** is the uuid code that identifies a user of an organization. It is used as a path parameter to restrict the requested operation to the scope of that user 
update_user = signing_today_client.UpdateUser() # UpdateUser | User properties to be edited

try:
    # Edit one or more user properties
    api_response = api_instance.update_user(organization_id, user_id, update_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Bit4idPathgroupUsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **user_id** | [**Id**](.md)| The **user-id** is the uuid code that identifies a user of an organization. It is used as a path parameter to restrict the requested operation to the scope of that user  | 
 **update_user** | [**UpdateUser**](UpdateUser.md)| User properties to be edited | 

### Return type

[**InlineResponse2015**](InlineResponse2015.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

