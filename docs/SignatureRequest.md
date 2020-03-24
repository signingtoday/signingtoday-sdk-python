# SignatureRequest

The association with the document is hold in the extraData of the FillableForm.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **int** | It is a reference for internal use | [optional] [readonly] 
**id** | **int** |  | [optional] 
**reason** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**signer_id** | **int** |  | [optional] 
**sign_profile** | **str** |  | [optional] 
**with_timestamp** | **bool** |  | [optional] 
**declinable** | **bool** |  | [optional] 
**restrictions** | [**list[SignatureRestriction]**](SignatureRestriction.md) |  | [optional] 
**extra_data** | **dict(str, object)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


