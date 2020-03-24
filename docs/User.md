# User

The User object is one of the components of the organization, which can sign digital signature transactions through one of the identities it got in the its wallet. Some of the most specific fields of this object are _\"automatic\"_, _\"rao\"_ and _\"owner\"_. They are boolean values. The first one indicates if the User can sign dsts into an automatic way, without passing through the signature tray. The rao field allows the User to enroll identities for the users of its organization. At last the owner field means that the token associated to the organization belongs to it and thus this particular User has administrative permissions. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The uuid code that identifies the User | 
**status** | **str** | The status of the User | [optional] 
**type** | **str** | The _type field_ identifies the permissions the User have | [optional] 
**email** | **str** | The email associated to the User | [optional] 
**first_name** | **str** | First name of the User | [optional] 
**last_name** | **str** | Last name of the User | [optional] 
**created_by** | **str** | This field shows who created the User - _user_name@organization-id_. It may be a SigningToday system User as well | [optional] 
**automatic** | **bool** | If true indicates that the User is an _automatic_ one, thus the signature procedure will be different from a regular signer | [optional] 
**owner** | **bool** | The _owner field_ gives to the User administrative permissions | [optional] 
**rao** | **bool** | The _rao field_ identifies a RAO User, the one can associate identities to the other users | [optional] 
**wallet** | [**list[Identity]**](Identity.md) | The wallet of an User identifies its portfolio of identities | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


