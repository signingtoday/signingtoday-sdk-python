# signing_today_client.DevicesApi

All URIs are relative to *https://web.sandbox.signingtoday.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_authorization_delete**](DevicesApi.md#device_authorization_delete) | **DELETE** /device/authorization | Clear a trusted device
[**device_authorization_get**](DevicesApi.md#device_authorization_get) | **GET** /device/authorization | Retrieve a challenge for authorizing a new trusted device
[**device_authorization_post**](DevicesApi.md#device_authorization_post) | **POST** /device/authorization | Register a new trusted device
[**devices_get**](DevicesApi.md#devices_get) | **GET** /devices | Get the list of trusted devices


# **device_authorization_delete**
> device_authorization_delete(device_id, user_id=user_id)

Clear a trusted device

This APIs allows to deregister a _deviceId_ of a trusted device.  It also deletes any notification push-token associated to the trusted device. 

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
    api_instance = signing_today_client.DevicesApi(api_client)
    device_id = '05ea656f-df69-49b1-a12b-9bf640c427c2' # str | The _deviceId_ to deregister
user_id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | Select the objects relative to the user specified by the parameter. If not specified will be used the id of the current authenticated user (optional)

    try:
        # Clear a trusted device
        api_instance.device_authorization_delete(device_id, user_id=user_id)
    except ApiException as e:
        print("Exception when calling DevicesApi->device_authorization_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| The _deviceId_ to deregister | 
 **user_id** | [**str**](.md)| Select the objects relative to the user specified by the parameter. If not specified will be used the id of the current authenticated user | [optional] 

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

# **device_authorization_get**
> DeviceAuthorizationResponse device_authorization_get()

Retrieve a challenge for authorizing a new trusted device

This API allows to retrieve a challenge in order to authorize a new trusted device.   - If asked in image/png the challenge is given encoded as a QR-Code image.   - An invocation of the endpoint invalidate any previous challenge.   - The challenge lasts 10 minutes. 

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
    api_instance = signing_today_client.DevicesApi(api_client)
    
    try:
        # Retrieve a challenge for authorizing a new trusted device
        api_response = api_instance.device_authorization_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->device_authorization_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeviceAuthorizationResponse**](DeviceAuthorizationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, image/png, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The challenge to be used for the authorization. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_authorization_post**
> list[str] device_authorization_post(inline_object7)

Register a new trusted device

This API allows to register a new trusted device. If the device is already present, it returns the current associated Token and updates the name. 

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
    api_instance = signing_today_client.DevicesApi(api_client)
    inline_object7 = signing_today_client.InlineObject7() # InlineObject7 | 

    try:
        # Register a new trusted device
        api_response = api_instance.device_authorization_post(inline_object7)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->device_authorization_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object7** | [**InlineObject7**](InlineObject7.md)|  | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The token to be used for next calls of the endpoint /device/authorize. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_get**
> TrustedDevicesGetResponse devices_get(user_id=user_id, top=top, skip=skip, count=count)

Get the list of trusted devices

The API allows to enumerate all the devices of a user. 

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
    api_instance = signing_today_client.DevicesApi(api_client)
    user_id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | Select the objects relative to the user specified by the parameter. If not specified will be used the id of the current authenticated user (optional)
top = 32 # int | A number of results to return. Applied after **$skip**  (optional)
skip = 64 # int | An offset into the collection of results (optional)
count = true # bool | If true, the server includes the count of all the items in the response  (optional)

    try:
        # Get the list of trusted devices
        api_response = api_instance.devices_get(user_id=user_id, top=top, skip=skip, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->devices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)| Select the objects relative to the user specified by the parameter. If not specified will be used the id of the current authenticated user | [optional] 
 **top** | **int**| A number of results to return. Applied after **$skip**  | [optional] 
 **skip** | **int**| An offset into the collection of results | [optional] 
 **count** | **bool**| If true, the server includes the count of all the items in the response  | [optional] 

### Return type

[**TrustedDevicesGetResponse**](TrustedDevicesGetResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of trusted devices. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

