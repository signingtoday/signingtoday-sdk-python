# signing_today_client.Bit4idPathgroupServicesApi

All URIs are relative to *https://web.sandbox.signingtoday.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_change_password_post**](Bit4idPathgroupServicesApi.md#auth_change_password_post) | **POST** /auth/changePassword | Consume a token to change the password
[**auth_password_lost_get**](Bit4idPathgroupServicesApi.md#auth_password_lost_get) | **GET** /auth/passwordLost | Request to recover own password
[**auth_password_reset_get**](Bit4idPathgroupServicesApi.md#auth_password_reset_get) | **GET** /auth/passwordReset | Reset a user password with superuser
[**auth_password_reset_post**](Bit4idPathgroupServicesApi.md#auth_password_reset_post) | **POST** /auth/passwordReset | Reset your own password
[**auth_password_token_get**](Bit4idPathgroupServicesApi.md#auth_password_token_get) | **GET** /auth/passwordToken | Get token to change password
[**auth_saml_post**](Bit4idPathgroupServicesApi.md#auth_saml_post) | **POST** /auth/saml | Register or Update a SAML user
[**auth_user**](Bit4idPathgroupServicesApi.md#auth_user) | **GET** /auth/user | Return the current logged in user
[**configuration_get**](Bit4idPathgroupServicesApi.md#configuration_get) | **GET** /service/configuration | Retrieve the App configuration
[**logout_user**](Bit4idPathgroupServicesApi.md#logout_user) | **GET** /auth/logout | Log out current user terminating the session
[**oauth_token_post**](Bit4idPathgroupServicesApi.md#oauth_token_post) | **POST** /oauth/token | Get the bearer token
[**pdf_resource_id_thumbs_get**](Bit4idPathgroupServicesApi.md#pdf_resource_id_thumbs_get) | **GET** /pdfResource/{id}/thumbs | Retrieve a Resource (of service)
[**service_change_password_post**](Bit4idPathgroupServicesApi.md#service_change_password_post) | **POST** /service/changePassword | Change the password of a service user
[**service_users_sync_post**](Bit4idPathgroupServicesApi.md#service_users_sync_post) | **POST** /service/users/sync | Sync user accounts


# **auth_change_password_post**
> auth_change_password_post(password_token, body)

Consume a token to change the password

This API allows to change the password by consuming a token.

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
    api_instance = signing_today_client.Bit4idPathgroupServicesApi(api_client)
    password_token = '05ea656f-df69-49b1-a12b-9bf640c427c2' # str | The password token issued to change password
body = 'body_example' # str | New password associated to the account (BCrypt)

    try:
        # Consume a token to change the password
        api_instance.auth_change_password_post(password_token, body)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupServicesApi->auth_change_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_token** | **str**| The password token issued to change password | 
 **body** | **str**| New password associated to the account (BCrypt) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request has been satisfyied. No output. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_password_lost_get**
> auth_password_lost_get(username, domain)

Request to recover own password

This API requests to recover the own password.

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
    api_instance = signing_today_client.Bit4idPathgroupServicesApi(api_client)
    username = 'jdo' # str | Username associated to the account
domain = 'demo' # str | Domain associated to the account

    try:
        # Request to recover own password
        api_instance.auth_password_lost_get(username, domain)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupServicesApi->auth_password_lost_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username associated to the account | 
 **domain** | **str**| Domain associated to the account | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request has been satisfyied. No output. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_password_reset_get**
> auth_password_reset_get(username, domain)

Reset a user password with superuser

This API allows to reset the password of a user. This is possible when the request is performed with a superuser.

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
    api_instance = signing_today_client.Bit4idPathgroupServicesApi(api_client)
    username = 'jdo' # str | Username associated to the account
domain = 'demo' # str | Domain associated to the account

    try:
        # Reset a user password with superuser
        api_instance.auth_password_reset_get(username, domain)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupServicesApi->auth_password_reset_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username associated to the account | 
 **domain** | **str**| Domain associated to the account | 

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
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_password_reset_post**
> auth_password_reset_post(inline_object4)

Reset your own password

This API allows to reset your own password knowing the previous one with a logged user.

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
    api_instance = signing_today_client.Bit4idPathgroupServicesApi(api_client)
    inline_object4 = signing_today_client.InlineObject4() # InlineObject4 | 

    try:
        # Reset your own password
        api_instance.auth_password_reset_post(inline_object4)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupServicesApi->auth_password_reset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object4** | [**InlineObject4**](InlineObject4.md)|  | 

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
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_password_token_get**
> list[object] auth_password_token_get()

Get token to change password

This API allows to get a password token to use in order to change a password.

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
    api_instance = signing_today_client.Bit4idPathgroupServicesApi(api_client)
    
    try:
        # Get token to change password
        api_response = api_instance.auth_password_token_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupServicesApi->auth_password_token_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A password token associated to the logged user. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_saml_post**
> auth_saml_post(domain, id_token1, id_token2)

Register or Update a SAML user

This API allows to register or Update a SAML user.

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
    api_instance = signing_today_client.Bit4idPathgroupServicesApi(api_client)
    domain = 'domain_example' # str | SAML domain
id_token1 = 'id_token1_example' # str | The BASE64-encoded SAML Reply in JSON
id_token2 = 'id_token2_example' # str | The Hex-encoded HMAC-SHA256 of the decoded IDToken1

    try:
        # Register or Update a SAML user
        api_instance.auth_saml_post(domain, id_token1, id_token2)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupServicesApi->auth_saml_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| SAML domain | 
 **id_token1** | **str**| The BASE64-encoded SAML Reply in JSON | 
 **id_token2** | **str**| The Hex-encoded HMAC-SHA256 of the decoded IDToken1 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**303** | Redirect to frontend page with new auth token (Post/Redirect/Get design pattern). |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_user**
> User auth_user()

Return the current logged in user

This API allows to retrieve the current logged in user.

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
    api_instance = signing_today_client.Bit4idPathgroupServicesApi(api_client)
    
    try:
        # Return the current logged in user
        api_response = api_instance.auth_user()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupServicesApi->auth_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**200** | Return current logged in user |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_get**
> dict(str, object) configuration_get()

Retrieve the App configuration

This API allows to get the public configuration associated to the application. 

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
    api_instance = signing_today_client.Bit4idPathgroupServicesApi(api_client)
    
    try:
        # Retrieve the App configuration
        api_response = api_instance.configuration_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupServicesApi->configuration_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_user**
> logout_user()

Log out current user terminating the session

This API allows to Log out current user.

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
    api_instance = signing_today_client.Bit4idPathgroupServicesApi(api_client)
    
    try:
        # Log out current user terminating the session
        api_instance.logout_user()
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupServicesApi->logout_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_token_post**
> InlineResponse200 oauth_token_post(username=username, password=password, grant_type=grant_type)

Get the bearer token

This API allows to get the token needed to access other APIs through the OAuth2 authentication.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import signing_today_client
from signing_today_client.rest import ApiException
from pprint import pprint
configuration = signing_today_client.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://web.sandbox.signingtoday.com/api
configuration.host = "https://web.sandbox.signingtoday.com/api"
# Enter a context with an instance of the API client
with signing_today_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signing_today_client.Bit4idPathgroupServicesApi(api_client)
    username = 'username_example' # str | The username in the form _username_@_domain_ where *domain* is the organization the user belongs to (optional)
password = 'password_example' # str | This is the actual password of the user (optional)
grant_type = 'grant_type_example' # str | A parameter that indicates the type of the grant in order to perform the basic authentication (optional)

    try:
        # Get the bearer token
        api_response = api_instance.oauth_token_post(username=username, password=password, grant_type=grant_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupServicesApi->oauth_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username in the form _username_@_domain_ where *domain* is the organization the user belongs to | [optional] 
 **password** | **str**| This is the actual password of the user | [optional] 
 **grant_type** | **str**| A parameter that indicates the type of the grant in order to perform the basic authentication | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OAuth Access Token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pdf_resource_id_thumbs_get**
> file pdf_resource_id_thumbs_get(id, page, width=width)

Retrieve a Resource (of service)

This API allows to extract thumbnails from a PDF Resource.

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
    api_instance = signing_today_client.Bit4idPathgroupServicesApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_
page = 1 # int | The page to retrieve
width = 20 # int | The output image width (optional)

    try:
        # Retrieve a Resource (of service)
        api_response = api_instance.pdf_resource_id_thumbs_get(id, page, width=width)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupServicesApi->pdf_resource_id_thumbs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 
 **page** | **int**| The page to retrieve | 
 **width** | **int**| The output image width | [optional] 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The output is a raw string. The thumbnails of the page requested for the PDF resource. |  -  |
**400** | Result of a client passing incorrect or invalid data. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_change_password_post**
> service_change_password_post(username, domain, body)

Change the password of a service user

This API allows to change the password of a **service user**. 

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
    api_instance = signing_today_client.Bit4idPathgroupServicesApi(api_client)
    username = 'jdo' # str | Username associated to the account
domain = 'demo' # str | Domain associated to the account
body = 'body_example' # str | New password associated to the account (BCrypt)

    try:
        # Change the password of a service user
        api_instance.service_change_password_post(username, domain, body)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupServicesApi->service_change_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username associated to the account | 
 **domain** | **str**| Domain associated to the account | 
 **body** | **str**| New password associated to the account (BCrypt) | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request has been satisfyied. No output. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_sync_post**
> UserSyncReport service_users_sync_post(inline_object)

Sync user accounts

This API allows to sync user accounts.

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
    api_instance = signing_today_client.Bit4idPathgroupServicesApi(api_client)
    inline_object = [signing_today_client.InlineObject()] # list[InlineObject] | User Accounts

    try:
        # Sync user accounts
        api_response = api_instance.service_users_sync_post(inline_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Bit4idPathgroupServicesApi->service_users_sync_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**list[InlineObject]**](InlineObject.md)| User Accounts | 

### Return type

[**UserSyncReport**](UserSyncReport.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report of last sync. |  -  |
**400** | Result of a client passing incorrect or invalid data. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

