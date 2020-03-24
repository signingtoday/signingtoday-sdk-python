# signing_today_client.RobotApi

All URIs are relative to *https://web.sandbox.signingtoday.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**robot_configuration_put**](RobotApi.md#robot_configuration_put) | **PUT** /robot/configuration | Edit the Robot configuration


# **robot_configuration_put**
> robot_configuration_put(robot_configuration, username=username, domain=domain)

Edit the Robot configuration

This API allows to edit the Robot configuration. 

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
    api_instance = signing_today_client.RobotApi(api_client)
    robot_configuration = signing_today_client.RobotConfiguration() # RobotConfiguration | RobotConfiguration.
username = 'thirdPartApp' # str | The _username_ associated to the account (optional)
domain = 'demo' # str | The _domain_ associated to the account (optional)

    try:
        # Edit the Robot configuration
        api_instance.robot_configuration_put(robot_configuration, username=username, domain=domain)
    except ApiException as e:
        print("Exception when calling RobotApi->robot_configuration_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **robot_configuration** | [**RobotConfiguration**](RobotConfiguration.md)| RobotConfiguration. | 
 **username** | **str**| The _username_ associated to the account | [optional] 
 **domain** | **str**| The _domain_ associated to the account | [optional] 

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
**500** | Internal failure of the service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

