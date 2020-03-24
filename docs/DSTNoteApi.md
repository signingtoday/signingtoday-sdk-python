# signing_today_client.DSTNoteApi

All URIs are relative to *https://web.sandbox.signingtoday.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_st_id_note_get**](DSTNoteApi.md#d_st_id_note_get) | **GET** /DST/{id}/note | Retrieve the DSTNotes associated to the DST
[**d_st_id_note_note_id_delete**](DSTNoteApi.md#d_st_id_note_note_id_delete) | **DELETE** /DST/{id}/note/{noteId} | Delete a DSTNote
[**d_st_id_note_note_id_put**](DSTNoteApi.md#d_st_id_note_note_id_put) | **PUT** /DST/{id}/note/{noteId} | Edit a DSTNote
[**d_st_id_note_post**](DSTNoteApi.md#d_st_id_note_post) | **POST** /DST/{id}/note | Append a new DSTNote


# **d_st_id_note_get**
> list[DSTNote] d_st_id_note_get(id)

Retrieve the DSTNotes associated to the DST

This API allows to retrieve the DST Notes associated to the DST.

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
    api_instance = signing_today_client.DSTNoteApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_

    try:
        # Retrieve the DSTNotes associated to the DST
        api_response = api_instance.d_st_id_note_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DSTNoteApi->d_st_id_note_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 

### Return type

[**list[DSTNote]**](DSTNote.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The DSTNotes |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_st_id_note_note_id_delete**
> d_st_id_note_note_id_delete(id, note_id)

Delete a DSTNote

This API allows to delete a DSTNote.

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
    api_instance = signing_today_client.DSTNoteApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_
note_id = 14 # int | The reference of a DSTNote

    try:
        # Delete a DSTNote
        api_instance.d_st_id_note_note_id_delete(id, note_id)
    except ApiException as e:
        print("Exception when calling DSTNoteApi->d_st_id_note_note_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 
 **note_id** | **int**| The reference of a DSTNote | 

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

# **d_st_id_note_note_id_put**
> DSTNote d_st_id_note_note_id_put(id, note_id, dst_note)

Edit a DSTNote

This API allows to edit a DSTNote.

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
    api_instance = signing_today_client.DSTNoteApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_
note_id = 14 # int | The reference of a DSTNote
dst_note = signing_today_client.DSTNote() # DSTNote | DSTNote replacing current object.

    try:
        # Edit a DSTNote
        api_response = api_instance.d_st_id_note_note_id_put(id, note_id, dst_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DSTNoteApi->d_st_id_note_note_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 
 **note_id** | **int**| The reference of a DSTNote | 
 **dst_note** | [**DSTNote**](DSTNote.md)| DSTNote replacing current object. | 

### Return type

[**DSTNote**](DSTNote.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated DSTNote. |  -  |
**400** | Result of a client passing incorrect or invalid data. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_st_id_note_post**
> DSTNote d_st_id_note_post(id, inline_object1=inline_object1)

Append a new DSTNote

This API allows to append a new DSTNote to the DST.

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
    api_instance = signing_today_client.DSTNoteApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_
inline_object1 = signing_today_client.InlineObject1() # InlineObject1 |  (optional)

    try:
        # Append a new DSTNote
        api_response = api_instance.d_st_id_note_post(id, inline_object1=inline_object1)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DSTNoteApi->d_st_id_note_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | [optional] 

### Return type

[**DSTNote**](DSTNote.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The DSTNote just added |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

