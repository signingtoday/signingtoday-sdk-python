# Token

The Token is an object that contains the information about the authorizations, thanks to which is possible to setup the authorization to use in every HTTP request or the authorization to send the webhook notifications either the authorization for the fetching of documents. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The uuid code that identifies the Token | [optional] 
**value** | **str** | This is the actual value of the Token, usually in a uuid format | [optional] 
**user** | **str** | The user whom is associated the Token | [optional] 
**webhooks** | [**TokenWebhooks**](TokenWebhooks.md) |  | [optional] 
**http_options** | [**TokenHttpOptions**](TokenHttpOptions.md) |  | [optional] 
**label** | **str** | The label assigned to the Token, that is like the name is associated to it | [optional] 
**created_by** | **str** | The user created the Token - _user_name@organization-id_ - | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


