# FillableForm

Two type of fillable exists; `SignatureForm` and `TextForm`. The former represents the association with the SignatureRequest, the latter represents any editable text form field to be filled before the signature process begins.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **int** | It is a reference for internal use | [optional] [readonly] 
**id** | **int** | Id of the _form_ | [optional] 
**document_id** | **int** | Id of the document | [optional] 
**type** | **str** | Type of the fill form | [optional] 
**position_x** | **float** | Position onto the X axis of the form, expressed in percentage | [optional] 
**position_y** | **float** | Position onto the Y axis of the form, expressed in percentage | [optional] 
**width** | **float** | Width of the form expressed in percentage | [optional] 
**height** | **float** | Height of the form expressed in percentage | [optional] 
**page** | **int** | Page of the document where the form is | [optional] 
**signer_id** | **int** | Id of the signer in the sign plan | [optional] 
**to_fill** | **bool** | **True** if the field need to be filled by the user. In case of a Signature it is **false**  | [optional] 
**filled** | **bool** | True ones the form has been filled | [optional] 
**invisible** | **bool** | True if the appearance has to be hidden | [optional] 
**extra_data** | **dict(str, object)** | Extra information about the form | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


