# signing_today_client.SignaturesApi

All URIs are relative to *https://sandbox.signingtoday.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_channel**](SignaturesApi.md#create_channel) | **POST** /{organization-id}/channels/{dst-id} | Create a channel
[**decline_dst**](SignaturesApi.md#decline_dst) | **POST** /{organization-id}/signatures/{signature-id}/decline | Decline a Digital Signature Transaction
[**perform_dst**](SignaturesApi.md#perform_dst) | **POST** /{organization-id}/signatures/{signature-id}/perform | Sign a DST with an automatic signer
[**perform_signature**](SignaturesApi.md#perform_signature) | **POST** /{organization-id}/signatures/{signature-id}/perform/{identity-id} | Perform a Signature
[**perform_signature_with_session**](SignaturesApi.md#perform_signature_with_session) | **POST** /{organization-id}/signatures/{signature-id}/session-perform | Perform a Signature with session


# **create_channel**
> InlineResponse201 create_channel(organization_id, dst_id)

Create a channel

This API allows to create a channel in order to dispose, by another API, the scheduling of a signature. These two APIs are used to integrate SigningToday into another application. 

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
api_instance = signing_today_client.SignaturesApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
dst_id = signing_today_client.Id() # Id | The **dst-id** is the uuid code that identifies a digital signature transaction. It is used as a path parameter to filter the requested operation to the specified **dst** 

try:
    # Create a channel
    api_response = api_instance.create_channel(organization_id, dst_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignaturesApi->create_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **dst_id** | [**Id**](.md)| The **dst-id** is the uuid code that identifies a digital signature transaction. It is used as a path parameter to filter the requested operation to the specified **dst**  | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decline_dst**
> InlineResponse2013 decline_dst(organization_id, signature_id, inline_object2)

Decline a Digital Signature Transaction

This API allows to decline the Signature of a digital signature transaction providing a reason. 

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
api_instance = signing_today_client.SignaturesApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
signature_id = signing_today_client.Id() # Id | The **signature-id** is the uuid code that identifies a signature that has to be performed into a digital signature transaction. It is usually used in the API endpoints to perform, decline or cancel a digital signature transaction 
inline_object2 = signing_today_client.InlineObject2() # InlineObject2 | 

try:
    # Decline a Digital Signature Transaction
    api_response = api_instance.decline_dst(organization_id, signature_id, inline_object2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignaturesApi->decline_dst: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **signature_id** | [**Id**](.md)| The **signature-id** is the uuid code that identifies a signature that has to be performed into a digital signature transaction. It is usually used in the API endpoints to perform, decline or cancel a digital signature transaction  | 
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

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
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_dst**
> InlineResponse2008 perform_dst(organization_id, signature_id, automatic_signature)

Sign a DST with an automatic signer

This API allows to sign a Digital Signature Transaction with an automatic signer certificate. 

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
api_instance = signing_today_client.SignaturesApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
signature_id = signing_today_client.Id() # Id | The **signature-id** is the uuid code that identifies a signature that has to be performed into a digital signature transaction. It is usually used in the API endpoints to perform, decline or cancel a digital signature transaction 
automatic_signature = signing_today_client.AutomaticSignature() # AutomaticSignature | Automatic Signature description

try:
    # Sign a DST with an automatic signer
    api_response = api_instance.perform_dst(organization_id, signature_id, automatic_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignaturesApi->perform_dst: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **signature_id** | [**Id**](.md)| The **signature-id** is the uuid code that identifies a signature that has to be performed into a digital signature transaction. It is usually used in the API endpoints to perform, decline or cancel a digital signature transaction  | 
 **automatic_signature** | [**AutomaticSignature**](AutomaticSignature.md)| Automatic Signature description | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

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

# **perform_signature**
> InlineResponse2009 perform_signature(organization_id, signature_id, identity_id, inline_object3)

Perform a Signature

This API allows to integrate SigningToday into another application. Through this endpoint it is possible to schedule a signature into engine. 

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
api_instance = signing_today_client.SignaturesApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
signature_id = signing_today_client.Id() # Id | The **signature-id** is the uuid code that identifies a signature that has to be performed into a digital signature transaction. It is usually used in the API endpoints to perform, decline or cancel a digital signature transaction 
identity_id = signing_today_client.Id() # Id | The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity 
inline_object3 = signing_today_client.InlineObject3() # InlineObject3 | 

try:
    # Perform a Signature
    api_response = api_instance.perform_signature(organization_id, signature_id, identity_id, inline_object3)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignaturesApi->perform_signature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **signature_id** | [**Id**](.md)| The **signature-id** is the uuid code that identifies a signature that has to be performed into a digital signature transaction. It is usually used in the API endpoints to perform, decline or cancel a digital signature transaction  | 
 **identity_id** | [**Id**](.md)| The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity  | 
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

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

# **perform_signature_with_session**
> InlineResponse20010 perform_signature_with_session(organization_id, signature_id, inline_object4)

Perform a Signature with session

This API allows to perform one or more signatures within the same session. This way is possible, in the scenario of a simple signature for example, to perform multiple signatures using the same _one time password_. 

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
api_instance = signing_today_client.SignaturesApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
signature_id = signing_today_client.Id() # Id | The **signature-id** is the uuid code that identifies a signature that has to be performed into a digital signature transaction. It is usually used in the API endpoints to perform, decline or cancel a digital signature transaction 
inline_object4 = signing_today_client.InlineObject4() # InlineObject4 | 

try:
    # Perform a Signature with session
    api_response = api_instance.perform_signature_with_session(organization_id, signature_id, inline_object4)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignaturesApi->perform_signature_with_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **signature_id** | [**Id**](.md)| The **signature-id** is the uuid code that identifies a signature that has to be performed into a digital signature transaction. It is usually used in the API endpoints to perform, decline or cancel a digital signature transaction  | 
 **inline_object4** | [**InlineObject4**](InlineObject4.md)|  | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

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

