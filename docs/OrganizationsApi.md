# signing_today_client.OrganizationsApi

All URIs are relative to *https://sandbox.signingtoday.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization**](OrganizationsApi.md#get_organization) | **GET** /organizations/{organization-id} | Get the settings of an oraganization
[**patch_organization**](OrganizationsApi.md#patch_organization) | **PATCH** /organizations/{organization-id} | Edit the settings of an organization


# **get_organization**
> InlineResponse200 get_organization(organization_id)

Get the settings of an oraganization

This API allows to obtain the settings of an organization, such as:   - _default_rao_ : the default rao user of the organization   - _dst_default_months_ : default deadline of a dst before its expiration   - _logo_ : the logo of the organization 

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
api_instance = signing_today_client.OrganizationsApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')

try:
    # Get the settings of an oraganization
    api_response = api_instance.get_organization(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

# **patch_organization**
> InlineResponse200 patch_organization(organization_id, update_organization)

Edit the settings of an organization

This API allows to edit every single setting of an organization except the **slug** field. 

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
api_instance = signing_today_client.OrganizationsApi(signing_today_client.ApiClient(configuration))
organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
update_organization = signing_today_client.UpdateOrganization() # UpdateOrganization | The settings of the organization to edit

try:
    # Edit the settings of an organization
    api_response = api_instance.patch_organization(organization_id, update_organization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->patch_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  | [default to &#39;api-demo&#39;]
 **update_organization** | [**UpdateOrganization**](UpdateOrganization.md)| The settings of the organization to edit | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

