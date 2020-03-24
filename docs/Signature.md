# Signature

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **int** | It is a reference for internal use | [optional] [readonly] 
**document_id** | **int** | Id of the document | [optional] 
**signature_request_id** | **int** | Id of the requested signature | [optional] 
**signed_at** | **datetime** | Indicates when the DST has been signed | [optional] 
**declined_reason** | **str** |  | [optional] 
**status** | **str** | Status of the signature, which can be _signed_ or _declined_ | [optional] [readonly] 
**extra_data** | **dict(str, object)** | Extra data of the signature | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


