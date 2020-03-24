# signing_today_client.RobotsApi

All URIs are relative to *https://web.sandbox.signingtoday.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**robot_authentication_delete**](RobotsApi.md#robot_authentication_delete) | **DELETE** /robot/authentication | Clear a Robot authentication lifetime token
[**robot_authentication_get**](RobotsApi.md#robot_authentication_get) | **GET** /robot/authentication | Retrieve the Robot authentication lifetime token
[**robot_configuration_get**](RobotsApi.md#robot_configuration_get) | **GET** /robot/configuration | Retrieve the Robot configuration
[**robot_ds_ts_post**](RobotsApi.md#robot_ds_ts_post) | **POST** /robot/DSTs | Create a new DST in one call
[**robot_id_instantiate_post**](RobotsApi.md#robot_id_instantiate_post) | **POST** /robot/{id}/instantiate | Instantiate a DST from a template by robot


# **robot_authentication_delete**
> robot_authentication_delete(username=username, domain=domain)

Clear a Robot authentication lifetime token

This API allows to clear the Robot authentication lifetime token.

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
    api_instance = signing_today_client.RobotsApi(api_client)
    username = 'thirdPartApp' # str | The _username_ associated to the account (optional)
domain = 'demo' # str | The _domain_ associated to the account (optional)

    try:
        # Clear a Robot authentication lifetime token
        api_instance.robot_authentication_delete(username=username, domain=domain)
    except ApiException as e:
        print("Exception when calling RobotsApi->robot_authentication_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The _username_ associated to the account | [optional] 
 **domain** | **str**| The _domain_ associated to the account | [optional] 

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

# **robot_authentication_get**
> RobotAuthenticationToken robot_authentication_get(username=username, domain=domain)

Retrieve the Robot authentication lifetime token

This API allows to generate or retrieves the Robot authentication lifetime token for the specified robot account, or the current logged in account. 

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
    api_instance = signing_today_client.RobotsApi(api_client)
    username = 'thirdPartApp' # str | The _username_ associated to the account (optional)
domain = 'demo' # str | The _domain_ associated to the account (optional)

    try:
        # Retrieve the Robot authentication lifetime token
        api_response = api_instance.robot_authentication_get(username=username, domain=domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RobotsApi->robot_authentication_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The _username_ associated to the account | [optional] 
 **domain** | **str**| The _domain_ associated to the account | [optional] 

### Return type

[**RobotAuthenticationToken**](RobotAuthenticationToken.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The lifetime robot token. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **robot_configuration_get**
> RobotConfiguration robot_configuration_get(username=username, domain=domain)

Retrieve the Robot configuration

This API allows to retrieve the Robot configuration. 

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
    api_instance = signing_today_client.RobotsApi(api_client)
    username = 'thirdPartApp' # str | The _username_ associated to the account (optional)
domain = 'demo' # str | The _domain_ associated to the account (optional)

    try:
        # Retrieve the Robot configuration
        api_response = api_instance.robot_configuration_get(username=username, domain=domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RobotsApi->robot_configuration_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The _username_ associated to the account | [optional] 
 **domain** | **str**| The _domain_ associated to the account | [optional] 

### Return type

[**RobotConfiguration**](RobotConfiguration.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Robot configuration. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **robot_ds_ts_post**
> DigitalSignatureTransaction robot_ds_ts_post(create_digital_signature_transaction)

Create a new DST in one call

This API allows to create a new DST with a more convenient interface for client applications. The purpose is to provide a method for the creation of a DST in order to semplify the integration into third part applications. 

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
    api_instance = signing_today_client.RobotsApi(api_client)
    create_digital_signature_transaction = signing_today_client.CreateDigitalSignatureTransaction() # CreateDigitalSignatureTransaction | description

    try:
        # Create a new DST in one call
        api_response = api_instance.robot_ds_ts_post(create_digital_signature_transaction)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RobotsApi->robot_ds_ts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_digital_signature_transaction** | [**CreateDigitalSignatureTransaction**](CreateDigitalSignatureTransaction.md)| description | 

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
**200** | The new DST. |  -  |
**400** | Result of a client passing incorrect or invalid data. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **robot_id_instantiate_post**
> DigitalSignatureTransaction robot_id_instantiate_post(id, instantiate_dst_template)

Instantiate a DST from a template by robot

This API allows to instantiate a DST from a template patching parts of its data structure. 

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
    api_instance = signing_today_client.RobotsApi(api_client)
    id = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4' # str | The value of _the unique id_
instantiate_dst_template = signing_today_client.InstantiateDSTTemplate() # InstantiateDSTTemplate | 

    try:
        # Instantiate a DST from a template by robot
        api_response = api_instance.robot_id_instantiate_post(id, instantiate_dst_template)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RobotsApi->robot_id_instantiate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The value of _the unique id_ | 
 **instantiate_dst_template** | [**InstantiateDSTTemplate**](InstantiateDSTTemplate.md)|  | 

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
**200** | The new DST that has been generated as an instance of the template. |  -  |
**401** | User authentication was not effective (e.g. not provided, invalid or expired). |  -  |
**403** | User is not allowed to perform the request. |  -  |
**404** | The resource was not found. |  -  |
**409** | Cannot satisfy the request because the resource is in an illegal status. |  -  |
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

