# signing_today_client.SignatureTransactionsApi

All URIs are relative to *https://sandbox.signingtoday.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_dst**](SignatureTransactionsApi.md#cancel_dst) | **POST** /{organization-id}/signature-transactions/{dst-id}/cancel | Mark a DST as canceled
[**create_dst**](SignatureTransactionsApi.md#create_dst) | **POST** /{organization-id}/signature-transactions | Create a Digital Signature Transaction
[**delete_dst**](SignatureTransactionsApi.md#delete_dst) | **DELETE** /{organization-id}/signature-transactions/{dst-id} | Delete a Digital Signature Transaction
[**delete_dst_resources**](SignatureTransactionsApi.md#delete_dst_resources) | **DELETE** /{organization-id}/signature-transactions/{dst-id}/resources | Delete the resources of a DST
[**get_document**](SignatureTransactionsApi.md#get_document) | **GET** /{organization-id}/documents/{document-id}/download | Download a document from a DST
[**get_dst**](SignatureTransactionsApi.md#get_dst) | **GET** /{organization-id}/signature-transactions/{dst-id} | Get information about a DST
[**list_ds_ts**](SignatureTransactionsApi.md#list_ds_ts) | **GET** /{organization-id}/signature-transactions | List the DSTs of an organization


# **cancel_dst**
> InlineResponse2013 cancel_dst(organization_id, dst_id, inline_object2)

Mark a DST as canceled

This API allows to mark a Digital Signature Transaction as canceled providing a reason. 

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
# Enter a context with an instance of the API client
with signing_today_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signing_today_client.SignatureTransactionsApi(api_client)
    organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
dst_id = signing_today_client.Id() # Id | The **dst-id** is the uuid code that identifies a digital signature transaction. It is used as a path parameter to filter the requested operation to the specified **dst** 
inline_object2 = signing_today_client.InlineObject2() # InlineObject2 | 

    try:
        # Mark a DST as canceled
        api_response = api_instance.cancel_dst(organization_id, dst_id, inline_object2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SignatureTransactionsApi->cancel_dst: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **dst_id** | [**Id**](.md)| The **dst-id** is the uuid code that identifies a digital signature transaction. It is used as a path parameter to filter the requested operation to the specified **dst**  | 
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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dst**
> InlineResponse2013 create_dst(organization_id, create_signature_transaction)

Create a Digital Signature Transaction

This API allows to create a Digital Signature Transaction. 

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
# Enter a context with an instance of the API client
with signing_today_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signing_today_client.SignatureTransactionsApi(api_client)
    organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
create_signature_transaction = signing_today_client.CreateSignatureTransaction() # CreateSignatureTransaction | The new DST to create

    try:
        # Create a Digital Signature Transaction
        api_response = api_instance.create_dst(organization_id, create_signature_transaction)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SignatureTransactionsApi->create_dst: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **create_signature_transaction** | [**CreateSignatureTransaction**](CreateSignatureTransaction.md)| The new DST to create | 

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
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dst**
> InlineResponse2009 delete_dst(organization_id, dst_id)

Delete a Digital Signature Transaction

This API allows to delete a Digital Signature Transaction. 

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
# Enter a context with an instance of the API client
with signing_today_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signing_today_client.SignatureTransactionsApi(api_client)
    organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
dst_id = signing_today_client.Id() # Id | The **dst-id** is the uuid code that identifies a digital signature transaction. It is used as a path parameter to filter the requested operation to the specified **dst** 

    try:
        # Delete a Digital Signature Transaction
        api_response = api_instance.delete_dst(organization_id, dst_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SignatureTransactionsApi->delete_dst: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **dst_id** | [**Id**](.md)| The **dst-id** is the uuid code that identifies a digital signature transaction. It is used as a path parameter to filter the requested operation to the specified **dst**  | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

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

# **delete_dst_resources**
> InlineResponse20010 delete_dst_resources(organization_id, dst_id)

Delete the resources of a DST

This API allows to delete the resources of a Digital Signature Transaction. 

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
# Enter a context with an instance of the API client
with signing_today_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signing_today_client.SignatureTransactionsApi(api_client)
    organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
dst_id = signing_today_client.Id() # Id | The **dst-id** is the uuid code that identifies a digital signature transaction. It is used as a path parameter to filter the requested operation to the specified **dst** 

    try:
        # Delete the resources of a DST
        api_response = api_instance.delete_dst_resources(organization_id, dst_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SignatureTransactionsApi->delete_dst_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **dst_id** | [**Id**](.md)| The **dst-id** is the uuid code that identifies a digital signature transaction. It is used as a path parameter to filter the requested operation to the specified **dst**  | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

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

# **get_document**
> file get_document(organization_id, document_id)

Download a document from a DST

This API allows to download a document from a digital signature transaction. The document can be downloaded before or after one or every signature have been performed. 

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
# Enter a context with an instance of the API client
with signing_today_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signing_today_client.SignatureTransactionsApi(api_client)
    organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
document_id = signing_today_client.Id() # Id | The **document-id** is the uuid code that identifies a document of a digital signature transaction. This parameter is usually used in order to download a document from a digital signature transaction 

    try:
        # Download a document from a DST
        api_response = api_instance.get_document(organization_id, document_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SignatureTransactionsApi->get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **document_id** | [**Id**](.md)| The **document-id** is the uuid code that identifies a document of a digital signature transaction. This parameter is usually used in order to download a document from a digital signature transaction  | 

### Return type

**file**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dst**
> InlineResponse2013 get_dst(organization_id, dst_id)

Get information about a DST

This API allows to get information about a Digital Signature Transaction. 

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
# Enter a context with an instance of the API client
with signing_today_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signing_today_client.SignatureTransactionsApi(api_client)
    organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
dst_id = signing_today_client.Id() # Id | The **dst-id** is the uuid code that identifies a digital signature transaction. It is used as a path parameter to filter the requested operation to the specified **dst** 

    try:
        # Get information about a DST
        api_response = api_instance.get_dst(organization_id, dst_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SignatureTransactionsApi->get_dst: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **dst_id** | [**Id**](.md)| The **dst-id** is the uuid code that identifies a digital signature transaction. It is used as a path parameter to filter the requested operation to the specified **dst**  | 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

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

# **list_ds_ts**
> InlineResponse2008 list_ds_ts(organization_id, where_signer=where_signer, where_status=where_status, where_title=where_title, where_created_by=where_created_by, where_created=where_created, where_signature_status=where_signature_status, where_document_name=where_document_name, where_reason=where_reason, where_signature_name=where_signature_name, where_signer_group=where_signer_group, page=page, count=count, where_order=where_order)

List the DSTs of an organization

This API allows to list the Digital Signature Transactions of an organization. 

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
# Enter a context with an instance of the API client
with signing_today_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signing_today_client.SignatureTransactionsApi(api_client)
    organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
where_signer = 'jdo' # str | Returns the Digital Signature Transactions where the specified user is a signer, searched by its id (optional)
where_status = 'performed' # str | Returns the Digital Signature Transactions with the specified status (optional)
where_title = 'Signature of a document' # str | Returns the Digital Signature Transactions that have the specified title (optional)
where_created_by = 'jdo@example' # str | Returns the Digital Signature Transactions created by the specified user (optional)
where_created = '2019-11-24T12:24:17.430Z' # str | Returns the Digital Signature Transactions created before, after or in the declared range (optional)
where_signature_status = 'pending' # str | Returns the Digital Signature Transactions where at least one of the signers has the queried status (optional)
where_document_name = 'Document of example' # str | Returns the Digital Signature Transactions that have into its documents the queried one (optional)
where_reason = 'where_reason_example' # str | Returns the Digital Signature Transactions with the specified reason (optional)
where_signature_name = 'John Doe' # str | Returns the Digital Signature Transactions where the specified user is a signer, searched by its name (optional)
where_signer_group = '@administrators' # str | Returns the Digital Signature Transactions that have the specified group of signers (optional)
page = 1 # int | Restricts the search to the chosen page (optional)
count = 100 # int | Sets the number of users per page to display (optional) (default to 100)
where_order = 'where_first_name' # str | The **where_order** query parameter takes one or more values separated by a comma and a space. The result will be ordered by the first value (ascending order is implied; a \"**-**\" in front of the value indicates descending order), then the second value and so on (optional)

    try:
        # List the DSTs of an organization
        api_response = api_instance.list_ds_ts(organization_id, where_signer=where_signer, where_status=where_status, where_title=where_title, where_created_by=where_created_by, where_created=where_created, where_signature_status=where_signature_status, where_document_name=where_document_name, where_reason=where_reason, where_signature_name=where_signature_name, where_signer_group=where_signer_group, page=page, count=count, where_order=where_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SignatureTransactionsApi->list_ds_ts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **where_signer** | **str**| Returns the Digital Signature Transactions where the specified user is a signer, searched by its id | [optional] 
 **where_status** | **str**| Returns the Digital Signature Transactions with the specified status | [optional] 
 **where_title** | **str**| Returns the Digital Signature Transactions that have the specified title | [optional] 
 **where_created_by** | **str**| Returns the Digital Signature Transactions created by the specified user | [optional] 
 **where_created** | **str**| Returns the Digital Signature Transactions created before, after or in the declared range | [optional] 
 **where_signature_status** | **str**| Returns the Digital Signature Transactions where at least one of the signers has the queried status | [optional] 
 **where_document_name** | **str**| Returns the Digital Signature Transactions that have into its documents the queried one | [optional] 
 **where_reason** | **str**| Returns the Digital Signature Transactions with the specified reason | [optional] 
 **where_signature_name** | **str**| Returns the Digital Signature Transactions where the specified user is a signer, searched by its name | [optional] 
 **where_signer_group** | **str**| Returns the Digital Signature Transactions that have the specified group of signers | [optional] 
 **page** | **int**| Restricts the search to the chosen page | [optional] 
 **count** | **int**| Sets the number of users per page to display | [optional] [default to 100]
 **where_order** | **str**| The **where_order** query parameter takes one or more values separated by a comma and a space. The result will be ordered by the first value (ascending order is implied; a \&quot;**-**\&quot; in front of the value indicates descending order), then the second value and so on | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

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

