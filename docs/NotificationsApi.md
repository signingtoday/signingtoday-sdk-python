# signing_today_client.NotificationsApi

All URIs are relative to *https://web.sandbox.signingtoday.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notifications_dst_id_delete**](NotificationsApi.md#notifications_dst_id_delete) | **DELETE** /notifications/dst/{id} | Clear Notifications for a DST
[**notifications_dsts_get**](NotificationsApi.md#notifications_dsts_get) | **GET** /notifications/dsts | Get latest DST Notifications
[**notifications_push_token_delete**](NotificationsApi.md#notifications_push_token_delete) | **DELETE** /notifications/push-token | Clear a registered push notification token
[**notifications_push_token_post**](NotificationsApi.md#notifications_push_token_post) | **POST** /notifications/push-token | Register a token for push notifications


# **notifications_dst_id_delete**
> notifications_dst_id_delete(id)

Clear Notifications for a DST

This API notifies that a user consumed all active notifications for a DST.

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
    api_instance = signing_today_client.NotificationsApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_

    try:
        # Clear Notifications for a DST
        api_instance.notifications_dst_id_delete(id)
    except ApiException as e:
        print("Exception when calling NotificationsApi->notifications_dst_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 

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

# **notifications_dsts_get**
> NotificationsResponse notifications_dsts_get(top=top, skip=skip, count=count)

Get latest DST Notifications

This APIs allows to get latest user Notifications for DSTs sorted desc by time.

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
    api_instance = signing_today_client.NotificationsApi(api_client)
    top = 32 # int | A number of results to return. Applied after **$skip**  (optional)
skip = 64 # int | An offset into the collection of results (optional)
count = true # bool | If true, the server includes the count of all the items in the response  (optional)

    try:
        # Get latest DST Notifications
        api_response = api_instance.notifications_dsts_get(top=top, skip=skip, count=count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->notifications_dsts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **top** | **int**| A number of results to return. Applied after **$skip**  | [optional] 
 **skip** | **int**| An offset into the collection of results | [optional] 
 **count** | **bool**| If true, the server includes the count of all the items in the response  | [optional] 

### Return type

[**NotificationsResponse**](NotificationsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Last DST notifications. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_push_token_delete**
> notifications_push_token_delete(device_id)

Clear a registered push notification token

This API deregister a deviceId from the push notifications.

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
    api_instance = signing_today_client.NotificationsApi(api_client)
    device_id = '05ea656f-df69-49b1-a12b-9bf640c427c2' # str | The _deviceId_ to deregister

    try:
        # Clear a registered push notification token
        api_instance.notifications_push_token_delete(device_id)
    except ApiException as e:
        print("Exception when calling NotificationsApi->notifications_push_token_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| The _deviceId_ to deregister | 

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

# **notifications_push_token_post**
> notifications_push_token_post(inline_object6)

Register a token for push notifications

This API allows to register a token for push notifications. Only trusted deviceId can be registered. 

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
    api_instance = signing_today_client.NotificationsApi(api_client)
    inline_object6 = signing_today_client.InlineObject6() # InlineObject6 | 

    try:
        # Register a token for push notifications
        api_instance.notifications_push_token_post(inline_object6)
    except ApiException as e:
        print("Exception when calling NotificationsApi->notifications_push_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object6** | [**InlineObject6**](InlineObject6.md)|  | 

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
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

