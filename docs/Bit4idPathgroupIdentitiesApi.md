# signing_today_client.Bit4idPathgroupIdentitiesApi

All URIs are relative to *https://sandbox.signingtoday.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associate_appearance**](Bit4idPathgroupIdentitiesApi.md#associate_appearance) | **POST** /{organization-id}/identities/{identity-id}/appearance | Associate an appearance to an identity
[**associate_identity**](Bit4idPathgroupIdentitiesApi.md#associate_identity) | **POST** /{organization-id}/users/{user-id}/wallet | Associate to an user an already existing identity
[**create_token_from_identity**](Bit4idPathgroupIdentitiesApi.md#create_token_from_identity) | **POST** /{organization-id}/identities/create/token | Create an identity from token
[**delete_appearance**](Bit4idPathgroupIdentitiesApi.md#delete_appearance) | **DELETE** /{organization-id}/identities/{identity-id}/appearance | Delete the appearance of an identity
[**delete_enrollment_request**](Bit4idPathgroupIdentitiesApi.md#delete_enrollment_request) | **DELETE** /{organization-id}/identity-requests/{enrollment-id} | Delete an enrollment request
[**delete_identity**](Bit4idPathgroupIdentitiesApi.md#delete_identity) | **DELETE** /{organization-id}/identities/{identity-id} | Delete an identity
[**get_enrollment_request**](Bit4idPathgroupIdentitiesApi.md#get_enrollment_request) | **GET** /{organization-id}/identity-requests/{enrollment-id} | Get information about an enrollment request
[**get_identity**](Bit4idPathgroupIdentitiesApi.md#get_identity) | **GET** /{organization-id}/identities/{identity-id} | Get information about an identity
[**list_enrollment_requests**](Bit4idPathgroupIdentitiesApi.md#list_enrollment_requests) | **GET** /{organization-id}/identity-requests | Enumerate the enrollment requests of an organization
[**list_identities**](Bit4idPathgroupIdentitiesApi.md#list_identities) | **GET** /{organization-id}/identities | Enumerate the identities of an organization
[**list_user_enrollments**](Bit4idPathgroupIdentitiesApi.md#list_user_enrollments) | **GET** /{organization-id}/users/{user-id}/identity-requests | List the enrollments of an user
[**list_user_identities**](Bit4idPathgroupIdentitiesApi.md#list_user_identities) | **GET** /{organization-id}/users/{user-id}/wallet | Enumerate the identities of an user
[**request_enrollment**](Bit4idPathgroupIdentitiesApi.md#request_enrollment) | **POST** /{organization-id}/enroll | Submit an enrollment request


# **associate_appearance**
> InlineResponse2004 associate_appearance(organization_id, identity_id, inline_object)

Associate an appearance to an identity

Associate a signature appearance to an already existing identity through an url to an image. This appearance will be displayed on the document after the signature. 

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
api_instance = signing_today_client.Bit4idPathgroupIdentitiesApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
identity_id = signing_today_client.Id() # Id | The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity 
inline_object = signing_today_client.InlineObject() # InlineObject | 

try:
    # Associate an appearance to an identity
    api_response = api_instance.associate_appearance(organization_id, identity_id, inline_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Bit4idPathgroupIdentitiesApi->associate_appearance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **identity_id** | [**Id**](.md)| The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity  | 
 **inline_object** | [**InlineObject**](InlineObject.md)|  | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **associate_identity**
> InlineResponse2004 associate_identity(organization_id, user_id, identity_association)

Associate to an user an already existing identity

Associate to an user of the organization an already existing identity of a provider. The _provider_data_ field is an object and is different for each provider. The minimum set of information to provide as provider_data is the following:   - **aruba**     - _auth_domain_ : string     - _username_ : string     - _password_ : string   - **aruba-auto**     - _auth_domain_ : string     - _username_ : string     - _password_ : string   - **infocert**     - _username_ : string     - _password_ : string   - **namirial**     - _id_titolare_ : string     - _id_otp_ : string     - _username_ : string     - _password_ : string 

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
api_instance = signing_today_client.Bit4idPathgroupIdentitiesApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
user_id = signing_today_client.Id() # Id | The **user-id** is the uuid code that identifies a user of an organization. It is used as a path parameter to restrict the requested operation to the scope of that user 
identity_association = signing_today_client.IdentityAssociation() # IdentityAssociation | Provider data to associate

try:
    # Associate to an user an already existing identity
    api_response = api_instance.associate_identity(organization_id, user_id, identity_association)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Bit4idPathgroupIdentitiesApi->associate_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **user_id** | [**Id**](.md)| The **user-id** is the uuid code that identifies a user of an organization. It is used as a path parameter to restrict the requested operation to the scope of that user  | 
 **identity_association** | [**IdentityAssociation**](IdentityAssociation.md)| Provider data to associate | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_token_from_identity**
> InlineResponse2012 create_token_from_identity(organization_id, create_identityby_token)

Create an identity from token

This API allows to create an identity from a token. 

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
api_instance = signing_today_client.Bit4idPathgroupIdentitiesApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
create_identityby_token = signing_today_client.CreateIdentitybyToken() # CreateIdentitybyToken | Body of the request to create an identity from a token

try:
    # Create an identity from token
    api_response = api_instance.create_token_from_identity(organization_id, create_identityby_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Bit4idPathgroupIdentitiesApi->create_token_from_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **create_identityby_token** | [**CreateIdentitybyToken**](CreateIdentitybyToken.md)| Body of the request to create an identity from a token | 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_appearance**
> InlineResponse2004 delete_appearance(organization_id, identity_id)

Delete the appearance of an identity

This API allows to delete the appearance associated to an identity. 

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
api_instance = signing_today_client.Bit4idPathgroupIdentitiesApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
identity_id = signing_today_client.Id() # Id | The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity 

try:
    # Delete the appearance of an identity
    api_response = api_instance.delete_appearance(organization_id, identity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Bit4idPathgroupIdentitiesApi->delete_appearance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **identity_id** | [**Id**](.md)| The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity  | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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

# **delete_enrollment_request**
> InlineResponse2012 delete_enrollment_request(organization_id, enrollment_id)

Delete an enrollment request

This API allows to delete an enrollment request. 

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
api_instance = signing_today_client.Bit4idPathgroupIdentitiesApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
enrollment_id = signing_today_client.Id() # Id | The **enrollment-id** is the uuid code that identifies a specific enrollment request 

try:
    # Delete an enrollment request
    api_response = api_instance.delete_enrollment_request(organization_id, enrollment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Bit4idPathgroupIdentitiesApi->delete_enrollment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **enrollment_id** | [**Id**](.md)| The **enrollment-id** is the uuid code that identifies a specific enrollment request  | 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

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

# **delete_identity**
> InlineResponse2003 delete_identity(organization_id, identity_id)

Delete an identity

This API allows to delete an identity of an user. 

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
api_instance = signing_today_client.Bit4idPathgroupIdentitiesApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
identity_id = signing_today_client.Id() # Id | The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity 

try:
    # Delete an identity
    api_response = api_instance.delete_identity(organization_id, identity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Bit4idPathgroupIdentitiesApi->delete_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **identity_id** | [**Id**](.md)| The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity  | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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

# **get_enrollment_request**
> InlineResponse2011 get_enrollment_request(organization_id, enrollment_id)

Get information about an enrollment request

This API allows to get information about an enrollment request. 

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
api_instance = signing_today_client.Bit4idPathgroupIdentitiesApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
enrollment_id = signing_today_client.Id() # Id | The **enrollment-id** is the uuid code that identifies a specific enrollment request 

try:
    # Get information about an enrollment request
    api_response = api_instance.get_enrollment_request(organization_id, enrollment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Bit4idPathgroupIdentitiesApi->get_enrollment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **enrollment_id** | [**Id**](.md)| The **enrollment-id** is the uuid code that identifies a specific enrollment request  | 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

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

# **get_identity**
> InlineResponse2002 get_identity(organization_id, identity_id)

Get information about an identity

This API allows to get all the information of an identity. 

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
api_instance = signing_today_client.Bit4idPathgroupIdentitiesApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
identity_id = signing_today_client.Id() # Id | The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity 

try:
    # Get information about an identity
    api_response = api_instance.get_identity(organization_id, identity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Bit4idPathgroupIdentitiesApi->get_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **identity_id** | [**Id**](.md)| The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

# **list_enrollment_requests**
> InlineResponse2005 list_enrollment_requests(organization_id, where_provider=where_provider, where_user=where_user, where_first_name=where_first_name, where_last_name=where_last_name, where_registered_by=where_registered_by, where_fiscal_code=where_fiscal_code, page=page, count=count)

Enumerate the enrollment requests of an organization

This API allows to enumerate the enrollment requests of an organization. 

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
api_instance = signing_today_client.Bit4idPathgroupIdentitiesApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
where_provider = 'sms' # str | Returns the identity requests that have been issued by the specified provider (optional)
where_user = 'msa' # str | Returns the identity requests of the specified user, searched by its id (optional)
where_first_name = 'John' # str | Returns the identity requests of the users that have the specified first name (optional)
where_last_name = 'Doe' # str | Returns the identity requests of the users that have the specified last name (optional)
where_registered_by = 'fba' # str | Returns the identity requests registered by this user (optional)
where_fiscal_code = 'MLLSNT82P65Z404U' # str | Returns the identity requests have the specified fiscal code (optional)
page = 1 # int | Restricts the search to the chosen page (optional)
count = 100 # int | Sets the number of users per page to display (optional) (default to 100)

try:
    # Enumerate the enrollment requests of an organization
    api_response = api_instance.list_enrollment_requests(organization_id, where_provider=where_provider, where_user=where_user, where_first_name=where_first_name, where_last_name=where_last_name, where_registered_by=where_registered_by, where_fiscal_code=where_fiscal_code, page=page, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Bit4idPathgroupIdentitiesApi->list_enrollment_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **where_provider** | **str**| Returns the identity requests that have been issued by the specified provider | [optional] 
 **where_user** | **str**| Returns the identity requests of the specified user, searched by its id | [optional] 
 **where_first_name** | **str**| Returns the identity requests of the users that have the specified first name | [optional] 
 **where_last_name** | **str**| Returns the identity requests of the users that have the specified last name | [optional] 
 **where_registered_by** | **str**| Returns the identity requests registered by this user | [optional] 
 **where_fiscal_code** | **str**| Returns the identity requests have the specified fiscal code | [optional] 
 **page** | **int**| Restricts the search to the chosen page | [optional] 
 **count** | **int**| Sets the number of users per page to display | [optional] [default to 100]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

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

# **list_identities**
> InlineResponse2001 list_identities(organization_id, where_provider=where_provider, where_user=where_user, where_first_name=where_first_name, where_last_name=where_last_name, where_registered_by=where_registered_by, where_fiscal_code=where_fiscal_code, page=page, count=count)

Enumerate the identities of an organization

This API allows to enumerate all the users of an organization. It is possible to filter the data using the supported _django lookups_. 

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
api_instance = signing_today_client.Bit4idPathgroupIdentitiesApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
where_provider = 'sms' # str | Returns the identities that have been issued by the specified provider (optional)
where_user = 'msa' # str | Returns the identities of the specified user, searched by its id (optional)
where_first_name = 'John' # str | Returns the identities of the users that have the specified first name (optional)
where_last_name = 'Doe' # str | Returns the identities of the users that have the specified last name (optional)
where_registered_by = 'fba' # str | Returns the identities registered by this user (optional)
where_fiscal_code = 'MLLSNT82P65Z404U' # str | Returns the identities that have the specified fiscal code (optional)
page = 1 # int | Restricts the search to the chosen page (optional)
count = 100 # int | Sets the number of users per page to display (optional) (default to 100)

try:
    # Enumerate the identities of an organization
    api_response = api_instance.list_identities(organization_id, where_provider=where_provider, where_user=where_user, where_first_name=where_first_name, where_last_name=where_last_name, where_registered_by=where_registered_by, where_fiscal_code=where_fiscal_code, page=page, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Bit4idPathgroupIdentitiesApi->list_identities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **where_provider** | **str**| Returns the identities that have been issued by the specified provider | [optional] 
 **where_user** | **str**| Returns the identities of the specified user, searched by its id | [optional] 
 **where_first_name** | **str**| Returns the identities of the users that have the specified first name | [optional] 
 **where_last_name** | **str**| Returns the identities of the users that have the specified last name | [optional] 
 **where_registered_by** | **str**| Returns the identities registered by this user | [optional] 
 **where_fiscal_code** | **str**| Returns the identities that have the specified fiscal code | [optional] 
 **page** | **int**| Restricts the search to the chosen page | [optional] 
 **count** | **int**| Sets the number of users per page to display | [optional] [default to 100]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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

# **list_user_enrollments**
> InlineResponse2005 list_user_enrollments(organization_id, user_id, page=page, count=count)

List the enrollments of an user

This API allows to list all the enrollments of an user. 

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
api_instance = signing_today_client.Bit4idPathgroupIdentitiesApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
user_id = signing_today_client.Id() # Id | The **user-id** is the uuid code that identifies a user of an organization. It is used as a path parameter to restrict the requested operation to the scope of that user 
page = 1 # int | Restricts the search to the chosen page (optional)
count = 100 # int | Sets the number of users per page to display (optional) (default to 100)

try:
    # List the enrollments of an user
    api_response = api_instance.list_user_enrollments(organization_id, user_id, page=page, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Bit4idPathgroupIdentitiesApi->list_user_enrollments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **user_id** | [**Id**](.md)| The **user-id** is the uuid code that identifies a user of an organization. It is used as a path parameter to restrict the requested operation to the scope of that user  | 
 **page** | **int**| Restricts the search to the chosen page | [optional] 
 **count** | **int**| Sets the number of users per page to display | [optional] [default to 100]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

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

# **list_user_identities**
> InlineResponse2001 list_user_identities(organization_id, user_id, page=page, count=count)

Enumerate the identities of an user

This API allows to enumerate all the identities of an user, which are located in its wallet. 

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
api_instance = signing_today_client.Bit4idPathgroupIdentitiesApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
user_id = signing_today_client.Id() # Id | The **user-id** is the uuid code that identifies a user of an organization. It is used as a path parameter to restrict the requested operation to the scope of that user 
page = 1 # int | Restricts the search to the chosen page (optional)
count = 100 # int | Sets the number of users per page to display (optional) (default to 100)

try:
    # Enumerate the identities of an user
    api_response = api_instance.list_user_identities(organization_id, user_id, page=page, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Bit4idPathgroupIdentitiesApi->list_user_identities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **user_id** | [**Id**](.md)| The **user-id** is the uuid code that identifies a user of an organization. It is used as a path parameter to restrict the requested operation to the scope of that user  | 
 **page** | **int**| Restricts the search to the chosen page | [optional] 
 **count** | **int**| Sets the number of users per page to display | [optional] [default to 100]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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

# **request_enrollment**
> InlineResponse2011 request_enrollment(organization_id, identity_request)

Submit an enrollment request

This API allows to submit an enrollment request. The user of the request will be created if it does not exists already. 

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
api_instance = signing_today_client.Bit4idPathgroupIdentitiesApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
identity_request = signing_today_client.IdentityRequest() # IdentityRequest | The enrollment request to submit

try:
    # Submit an enrollment request
    api_response = api_instance.request_enrollment(organization_id, identity_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Bit4idPathgroupIdentitiesApi->request_enrollment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **identity_request** | [**IdentityRequest**](IdentityRequest.md)| The enrollment request to submit | 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

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

