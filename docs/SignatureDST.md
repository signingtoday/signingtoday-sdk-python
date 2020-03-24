# SignatureDST

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**declinable** | **bool** | If true the signer is able to decline the Signature if he wants to | [optional] 
**profile** | **str** | The _profile_ field of the Signature object specifies the modality of signature is going to be performed, and can be:   - _PADES_ :     - allows to exclusively sign a pdf file with the signature     directly affixed into the document;   - _CADES_ :     - allows to sign different types of documents; the signature     is not \&quot;physically\&quot; into the document but the signature and the file     are placed together in an envelope instead, making thus a _.p7m_     extension.  | [optional] 
**display_name** | **str** | This is the name will be displayed on the signature tray associated to the Signature has to be performed. Usually is the _full name_ of the user is going to sign | [optional] 
**reason** | **str** | The reason of the Signature, or rather a motivational description associated to the Signature | [optional] 
**signer** | **str** | The user that have to sign the digital signature transaction | [optional] 
**description** | **str** | This is a simple description to attach with the Signature | [optional] 
**urlback** | **str** | The url for the redirection from Signature tray when the digital signature transaction is completed or annulled | [optional] 
**where** | [**SignatureDSTWhere**](SignatureDSTWhere.md) |  | [optional] 
**constraints** | [**object**](.md) | Particular constraints for the Signature. For example constraints about the _firs tname_ or _last name_ of the certificate associated with the identity is going to sign. The way to use this field is through the _django lookups_, for example:   - \&quot;certificate__subject_givenName__iexact&#x3D;JOHN\&quot;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


