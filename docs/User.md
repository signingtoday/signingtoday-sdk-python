# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatic** | **bool** | If true indicates that the User is an _automatic_ one, thus the signature procedure will be different from a regular signer | [optional] 
**created_by** | **str** | This field shows who created the User - _user_name@organization-id_. It may be a SigningToday system User as well | [optional] 
**email** | **str** | The email associated to the User | [optional] 
**first_name** | **str** | First name of the User | [optional] 
**id** | **str** | The uuid code that identifies the User | 
**last_name** | **str** | Last name of the User | [optional] 
**owner** | **bool** | The _owner field_ gives to the User administrative permissions | [optional] 
**rao** | **bool** | The _rao field_ identifies a RAO User, the one can associate identities to the other users | [optional] 
**status** | **str** | The status of the User | [optional] 
**type** | **str** | The _type field_ identifies the permissions the User have | [optional] 
**wallet** | [**list[Identity]**](Identity.md) | The wallet of an User identifies its portfolio of identities | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


