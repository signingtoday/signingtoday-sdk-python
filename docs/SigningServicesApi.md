# signing_today_client.SigningServicesApi

All URIs are relative to *https://web.sandbox.signingtoday.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sign_service_open**](SigningServicesApi.md#sign_service_open) | **POST** /sign-service/open | sign-service open post
[**sign_service_open_id**](SigningServicesApi.md#sign_service_open_id) | **POST** /sign-service/open/{transaction-id} | sign-service-open-transaction-id post
[**signature_id_perform_id_post**](SigningServicesApi.md#signature_id_perform_id_post) | **POST** /sign-service/{signature-id}/perform/{identity-id} | sign-service-signature-id-perform-identity-id post


# **sign_service_open**
> object sign_service_open()

sign-service open post

description bla bla

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
    api_instance = signing_today_client.SigningServicesApi(api_client)
    
    try:
        # sign-service open post
        api_response = api_instance.sign_service_open()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SigningServicesApi->sign_service_open: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_service_open_id**
> object sign_service_open_id(transaction_id)

sign-service-open-transaction-id post

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
    api_instance = signing_today_client.SigningServicesApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # sign-service-open-transaction-id post
        api_response = api_instance.sign_service_open_id(transaction_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SigningServicesApi->sign_service_open_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | 

### Return type

**object**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signature_id_perform_id_post**
> object signature_id_perform_id_post(signature_id, identity_id, inline_object8=inline_object8)

sign-service-signature-id-perform-identity-id post

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
    api_instance = signing_today_client.SigningServicesApi(api_client)
    signature_id = 'signature_id_example' # str | 
identity_id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | 
inline_object8 = signing_today_client.InlineObject8() # InlineObject8 |  (optional)

    try:
        # sign-service-signature-id-perform-identity-id post
        api_response = api_instance.signature_id_perform_id_post(signature_id, identity_id, inline_object8=inline_object8)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SigningServicesApi->signature_id_perform_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signature_id** | **str**|  | 
 **identity_id** | **str**|  | 
 **inline_object8** | [**InlineObject8**](InlineObject8.md)|  | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

