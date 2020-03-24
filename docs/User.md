# User

The **User** object is the one that serializes the users of the _Organizations_. The _User_ has field that identifies the generality of the person who has been registered and uses the platform, as well as the digital identities through which he can sign documents. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the User | [optional] [readonly] 
**username** | **str** | The username of the User. The username is used to login | [optional] 
**domain** | **str** | The _domain_ is the Organization which a user or a DST belongs | [optional] 
**language** | **str** | The default language of the User | [optional] 
**name** | **str** | The name of the User | [optional] 
**surname** | **str** | The name of the User | [optional] 
**email** | **str** | The email address of the User | [optional] 
**phone** | [**BigDecimal**](BigDecimal.md) | The phone number of the User | [optional] 
**role** | **str** | The role of the User. The **admin** can create users, as well as DSTs and can sign. The **instructor** can create DSTs and sign. The **signer** can only sign documents.  | [optional] 
**groups** | [**list[UserGroup]**](UserGroup.md) | A group of users. This is useful during DSTs creation, it is possible to select a group as signers. This way all the components of that group have to sign the document | [optional] 
**capabilities** | **list[str]** | The capabilities represents the action a user is able to do | [optional] 
**created_by** | **str** | The one which created the User | [optional] [readonly] 
**created_at** | **datetime** | The date of the creation of the User | [optional] [readonly] 
**deleted_at** | **datetime** | The date of deletion of the User | [optional] [readonly] 
**automatic** | **bool** | If true the user is automatic | [optional] [readonly] 
**extra_data** | **dict(str, object)** | Extra data associated to the User | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


