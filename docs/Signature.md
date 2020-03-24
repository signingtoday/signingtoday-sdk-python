# Signature

The Signature is an object of SigningToday which contains all the information needed to _digitally sign a document_. This is possible thanks to the cerficate associated to the identity in the wallet of the user is going to perform the signature. The _profile_ field of the Signature object specifies the modality of signature is going to be performed, and can be:   - _PADES_ :     - allows to exclusively sign a pdf file with the signature     directly affixed into the document;   - _CADES_ :     - allows to sign different types of documents; the signature     is not \"physically\" into the document but the signature and the file     are placed together in an envelope instead, making thus a _.p7m_     extension.  Consistently to the other objects, the Signature, as well, has a status, which is helpful to understand if the signature has been performed already or not, if it is expired or it is errored due to a miskate during the creation of the digital signature transaction or the performing of the signature itself. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The uuid code that identifies the Signature | [optional] 
**signer** | **str** | The user that have to sign the digital signature transaction | [optional] 
**signer_group** | **str** | The group which the signer belongs. This field is used in the scenario of a digital signature transaction that has multiple signatures to be performed, where the signers belongs to the same group. Let&#39;s think to the group _\&quot;teachers\&quot;_ of a school. Thus is possible to add the _signer_group_ _\&quot;teachers\&quot;_ as signers of the digital signature transaction without worrying about who really belong to that group | [optional] 
**signature_ticket** | **str** | This is the url where a signature tray is predisposed for a specific signer that have to sign a specific digital signature transaction. It is possible to set the signature tray language by the use of the **locate** query string - e.g. *?locate&#x3D;en*  | [optional] 
**automatic** | **bool** | If true indicates that the signer is an _automatic_ one, thus the signature procedure will be different from a regular signer | [optional] 
**decline_url** | **str** | This is the url to decline a digital signature transaction | [optional] 
**description_html** | **str** | This is a _html_ description to attach with the Signature | [optional] 
**status** | **str** | The status of the Signature. As the digital signature transaction is created the status of the Signature is _waiting_, if everything is legit than the status changes to _pending_, otherwise to _error_. Once the Signature is made the status changes to _performed_. If the DST expires before the Signature is performed then the status changes to _expired_ | [optional] 
**display_name** | **str** | This is the name will be displayed on the signature tray associated to the Signature has to be performed. Usually is the _full name_ of the user is going to sign | [optional] 
**profile** | **str** | The _profile_ field of the Signature object specifies the modality of signature is going to be performed, and can be:   - _PADES_ : allows to exclusively sign a pdf file with the signature     directly affixed into the document;   - _CADES_ : allows to sign different types of documents; the signature     is not \&quot;physically\&quot; into the document but the signature and the file     are placed together in an envelope instead, making thus a .p7m extension.  | [optional] 
**reason** | **str** | The reason of the Signature, or rather a motivational description associated to the Signature | [optional] 
**description** | **str** | This is a simple description to attach with the Signature | [optional] 
**declinable** | **bool** | If true the signer is able to decline the Signature if he wants to | [optional] 
**urlback** | **str** | The url for the redirection from Signature tray when the digital signature transaction is completed or annulled | [optional] 
**where** | [**SignatureWhere**](SignatureWhere.md) |  | [optional] 
**constraints** | [**object**](.md) | Particular constraints for the Signature. For example constraints about the _firs tname_ or _last name_ of the certificate associated with the identity is going to sign. The way to use this field is through the _django lookups_, for example:   - \&quot;certificate__subject_givenName__iexact&#x3D;JOHN\&quot;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


