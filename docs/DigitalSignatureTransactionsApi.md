# signing_today_client.DigitalSignatureTransactionsApi

All URIs are relative to *https://web.sandbox.signingtoday.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_s_ts_get**](DigitalSignatureTransactionsApi.md#d_s_ts_get) | **GET** /DSTs | Retrieve DSTs
[**d_s_ts_post**](DigitalSignatureTransactionsApi.md#d_s_ts_post) | **POST** /DSTs | Create a new DST
[**d_st_id_audit_get**](DigitalSignatureTransactionsApi.md#d_st_id_audit_get) | **GET** /DST/{id}/audit | Retrieve the audit records associated to the DST
[**d_st_id_delete**](DigitalSignatureTransactionsApi.md#d_st_id_delete) | **DELETE** /DST/{id} | Delete a DST
[**d_st_id_fill_patch**](DigitalSignatureTransactionsApi.md#d_st_id_fill_patch) | **PATCH** /DST/{id}/fill | Fill a form of a DST
[**d_st_id_get**](DigitalSignatureTransactionsApi.md#d_st_id_get) | **GET** /DST/{id} | Retrieve a DST
[**d_st_id_instantiate_post**](DigitalSignatureTransactionsApi.md#d_st_id_instantiate_post) | **POST** /DST/{id}/instantiate | Instantiate a DST from a template
[**d_st_id_modify_post**](DigitalSignatureTransactionsApi.md#d_st_id_modify_post) | **POST** /DST/{id}/modify | Modify a published DST template
[**d_st_id_notify_post**](DigitalSignatureTransactionsApi.md#d_st_id_notify_post) | **POST** /DST/{id}/notify | Send notifications for a DST
[**d_st_id_publish_post**](DigitalSignatureTransactionsApi.md#d_st_id_publish_post) | **POST** /DST/{id}/publish | Publish a DST
[**d_st_id_put**](DigitalSignatureTransactionsApi.md#d_st_id_put) | **PUT** /DST/{id} | Update a DST
[**d_st_id_replace_post**](DigitalSignatureTransactionsApi.md#d_st_id_replace_post) | **POST** /DST/{id}/replace | Replace a rejected DST
[**d_st_id_sign_doc_id_sign_id_get**](DigitalSignatureTransactionsApi.md#d_st_id_sign_doc_id_sign_id_get) | **GET** /DST/{id}/sign/{docId}/{signId} | Return the address for signing
[**d_st_id_templatize_post**](DigitalSignatureTransactionsApi.md#d_st_id_templatize_post) | **POST** /DST/{id}/templatize | Create a template from a DST


# **d_s_ts_get**
> DSTsGetResponse d_s_ts_get(template=template, user_id=user_id, top=top, skip=skip, count=count, order_by=order_by, filter=filter)

Retrieve DSTs

This API allows to list the DSTs of an organization.

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
    api_instance = signing_today_client.DigitalSignatureTransactionsApi(api_client)
    template = False # bool | Select templates or instances (optional) (default to False)
user_id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | Select the objects relative to the user specified by the parameter. If not specified will be used the id of the current authenticated user (optional)
top = 32 # int | A number of results to return. Applied after **$skip**  (optional)
skip = 64 # int | An offset into the collection of results (optional)
count = true # bool | If true, the server includes the count of all the items in the response  (optional)
order_by = '$orderBy=updatedAt' # str | An ordering definition (eg. $orderBy=updatedAt,desc) (optional)
filter = '$filter=name==\"Milk\"' # str | A filter definition (eg. $filter=name == \"Milk\" or surname == \"Bread\") (optional)

    try:
        # Retrieve DSTs
        api_response = api_instance.d_s_ts_get(template=template, user_id=user_id, top=top, skip=skip, count=count, order_by=order_by, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DigitalSignatureTransactionsApi->d_s_ts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **bool**| Select templates or instances | [optional] [default to False]
 **user_id** | [**str**](.md)| Select the objects relative to the user specified by the parameter. If not specified will be used the id of the current authenticated user | [optional] 
 **top** | **int**| A number of results to return. Applied after **$skip**  | [optional] 
 **skip** | **int**| An offset into the collection of results | [optional] 
 **count** | **bool**| If true, the server includes the count of all the items in the response  | [optional] 
 **order_by** | **str**| An ordering definition (eg. $orderBy&#x3D;updatedAt,desc) | [optional] 
 **filter** | **str**| A filter definition (eg. $filter&#x3D;name &#x3D;&#x3D; \&quot;Milk\&quot; or surname &#x3D;&#x3D; \&quot;Bread\&quot;) | [optional] 

### Return type

[**DSTsGetResponse**](DSTsGetResponse.md)

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
**403** | User is not allowed to perform the request. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_s_ts_post**
> DigitalSignatureTransaction d_s_ts_post(digital_signature_transaction)

Create a new DST

This API allows to creates a new DST. A DST is created in the Draft state and then updated using PUT. Example of creation request:  ``` {   status: \"draft\",   publishedAt: null,   tags: [],   urgent: false,   template: false } ```  To add documents use the Resources Patch endpoint `/DST/{id}/resources`.  If the *template* flag is set true the DST is a Template. If the *publicTemplate* flag is set true the Template is visible to all users with rights to create a DST.  A DST is made made available to users using *publish* end point. A template generates a DST with the *instantiate* endpoint. 

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
    api_instance = signing_today_client.DigitalSignatureTransactionsApi(api_client)
    digital_signature_transaction = signing_today_client.DigitalSignatureTransaction() # DigitalSignatureTransaction | DST to append to the current resources.

    try:
        # Create a new DST
        api_response = api_instance.d_s_ts_post(digital_signature_transaction)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DigitalSignatureTransactionsApi->d_s_ts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **digital_signature_transaction** | [**DigitalSignatureTransaction**](DigitalSignatureTransaction.md)| DST to append to the current resources. | 

### Return type

[**DigitalSignatureTransaction**](DigitalSignatureTransaction.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The new DST added to the list. |  -  |
**400** | Result of a client passing incorrect or invalid data. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_st_id_audit_get**
> list[AuditRecord] d_st_id_audit_get(id)

Retrieve the audit records associated to the DST

This API allows to retrieves the audit records associated to the DST.

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
    api_instance = signing_today_client.DigitalSignatureTransactionsApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_

    try:
        # Retrieve the audit records associated to the DST
        api_response = api_instance.d_st_id_audit_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DigitalSignatureTransactionsApi->d_st_id_audit_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 

### Return type

[**list[AuditRecord]**](AuditRecord.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The audit associated to the DST sorted by date. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_st_id_delete**
> d_st_id_delete(id)

Delete a DST

This API allows to delete a DST. Actually the DST is marked as deleted thus not displayed anymore into the organization, but it will still be present in the database.

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
    api_instance = signing_today_client.DigitalSignatureTransactionsApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_

    try:
        # Delete a DST
        api_instance.d_st_id_delete(id)
    except ApiException as e:
        print("Exception when calling DigitalSignatureTransactionsApi->d_st_id_delete: %s\n" % e)
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
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_st_id_fill_patch**
> DigitalSignatureTransaction d_st_id_fill_patch(id, fillable_form)

Fill a form of a DST

This API allows to fill a form of a DST.

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
    api_instance = signing_today_client.DigitalSignatureTransactionsApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_
fillable_form = signing_today_client.FillableForm() # FillableForm | The form filled by the user.

    try:
        # Fill a form of a DST
        api_response = api_instance.d_st_id_fill_patch(id, fillable_form)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DigitalSignatureTransactionsApi->d_st_id_fill_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 
 **fillable_form** | [**FillableForm**](FillableForm.md)| The form filled by the user. | 

### Return type

[**DigitalSignatureTransaction**](DigitalSignatureTransaction.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The DST has been modified according to the operation. |  -  |
**400** | Result of a client passing incorrect or invalid data. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_st_id_get**
> DigitalSignatureTransaction d_st_id_get(id)

Retrieve a DST

This API allows to retrieve a DST.

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
    api_instance = signing_today_client.DigitalSignatureTransactionsApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_

    try:
        # Retrieve a DST
        api_response = api_instance.d_st_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DigitalSignatureTransactionsApi->d_st_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 

### Return type

[**DigitalSignatureTransaction**](DigitalSignatureTransaction.md)

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
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_st_id_instantiate_post**
> DigitalSignatureTransaction d_st_id_instantiate_post(id)

Instantiate a DST from a template

This API allows to instantiate a DST from a template by specifying the template Id.

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
    api_instance = signing_today_client.DigitalSignatureTransactionsApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_

    try:
        # Instantiate a DST from a template
        api_response = api_instance.d_st_id_instantiate_post(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DigitalSignatureTransactionsApi->d_st_id_instantiate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 

### Return type

[**DigitalSignatureTransaction**](DigitalSignatureTransaction.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new DST that has been generated as an instance of the template. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_st_id_modify_post**
> DigitalSignatureTransaction d_st_id_modify_post(id)

Modify a published DST template

This API allows to move a published DST to DRAFT, allowing the modification. This way is possible to modify a _DST Template_. 

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
    api_instance = signing_today_client.DigitalSignatureTransactionsApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_

    try:
        # Modify a published DST template
        api_response = api_instance.d_st_id_modify_post(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DigitalSignatureTransactionsApi->d_st_id_modify_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 

### Return type

[**DigitalSignatureTransaction**](DigitalSignatureTransaction.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The modified DST in DRAFT state. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_st_id_notify_post**
> d_st_id_notify_post(id)

Send notifications for a DST

This API allows to send notifications to pending users for an active _DST_.

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
    api_instance = signing_today_client.DigitalSignatureTransactionsApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_

    try:
        # Send notifications for a DST
        api_instance.d_st_id_notify_post(id)
    except ApiException as e:
        print("Exception when calling DigitalSignatureTransactionsApi->d_st_id_notify_post: %s\n" % e)
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
**400** | Result of a client passing incorrect or invalid data. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_st_id_publish_post**
> DigitalSignatureTransaction d_st_id_publish_post(id)

Publish a DST

This API allows to publish a DST, the new state becomes published. It will automatically evolve to a new state where it will be filled or signed.

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
    api_instance = signing_today_client.DigitalSignatureTransactionsApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_

    try:
        # Publish a DST
        api_response = api_instance.d_st_id_publish_post(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DigitalSignatureTransactionsApi->d_st_id_publish_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 

### Return type

[**DigitalSignatureTransaction**](DigitalSignatureTransaction.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The DST has been modified according to the operation. |  -  |
**400** | Result of a client passing incorrect or invalid data. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_st_id_put**
> DigitalSignatureTransaction d_st_id_put(id, digital_signature_transaction)

Update a DST

This API allows to update a DST.

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
    api_instance = signing_today_client.DigitalSignatureTransactionsApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_
digital_signature_transaction = signing_today_client.DigitalSignatureTransaction() # DigitalSignatureTransaction | DST replacing current object.

    try:
        # Update a DST
        api_response = api_instance.d_st_id_put(id, digital_signature_transaction)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DigitalSignatureTransactionsApi->d_st_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 
 **digital_signature_transaction** | [**DigitalSignatureTransaction**](DigitalSignatureTransaction.md)| DST replacing current object. | 

### Return type

[**DigitalSignatureTransaction**](DigitalSignatureTransaction.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated DST. |  -  |
**400** | Result of a client passing incorrect or invalid data. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_st_id_replace_post**
> DigitalSignatureTransaction d_st_id_replace_post(id)

Replace a rejected DST

This API allows to replace a rejected DST instantiating a new one. The replacing DST is created in DRAFT state.

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
    api_instance = signing_today_client.DigitalSignatureTransactionsApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_

    try:
        # Replace a rejected DST
        api_response = api_instance.d_st_id_replace_post(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DigitalSignatureTransactionsApi->d_st_id_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 

### Return type

[**DigitalSignatureTransaction**](DigitalSignatureTransaction.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new DST that has been generated as a replace of the referred DST. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_st_id_sign_doc_id_sign_id_get**
> DSTSigningAddressResponse d_st_id_sign_doc_id_sign_id_get(id, doc_id, sign_id)

Return the address for signing

This API returns the address to perform the signature.

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
    api_instance = signing_today_client.DigitalSignatureTransactionsApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_
doc_id = 3 # int | Reference to _docId_ has to be signed
sign_id = 2 # int | Reference to the signature request id

    try:
        # Return the address for signing
        api_response = api_instance.d_st_id_sign_doc_id_sign_id_get(id, doc_id, sign_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DigitalSignatureTransactionsApi->d_st_id_sign_doc_id_sign_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 
 **doc_id** | **int**| Reference to _docId_ has to be signed | 
 **sign_id** | **int**| Reference to the signature request id | 

### Return type

[**DSTSigningAddressResponse**](DSTSigningAddressResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The URL where to sign. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_st_id_templatize_post**
> DigitalSignatureTransaction d_st_id_templatize_post(id)

Create a template from a DST

This API allows to creates a new template starting from a DST. Currently implemented only for published DST templates.

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
    api_instance = signing_today_client.DigitalSignatureTransactionsApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_

    try:
        # Create a template from a DST
        api_response = api_instance.d_st_id_templatize_post(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DigitalSignatureTransactionsApi->d_st_id_templatize_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 

### Return type

[**DigitalSignatureTransaction**](DigitalSignatureTransaction.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new DST that has been generated as a template of the referred DST. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

