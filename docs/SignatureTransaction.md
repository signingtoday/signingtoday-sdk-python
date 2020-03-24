# SignatureTransaction

The Digital Signature Transaction is the object that makes possible a flow of signatures of one or more documents happen. Once there is an organization with some users, it is possible to create a dst through the definition of the document or the documents have to be signed, the signer or, eventually, the signers, grouping them, in this way it is possible to decide the order of the signatories will be followed. The status of the DST is _pending_ until all the signers have signed. Once that happens the status will change to _performed_. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The uuid code that identifies the Digital Signature Transaction | [optional] 
**documents** | [**list[Document]**](Document.md) | The _documents_ field is an array containing document objects, where everyone of them is defined as follows  | [optional] 
**archived** | **bool** | True if the DST&#39;s resources has been deleted | [optional] [default to False]
**created_by** | **str** | The user created the Digital Signature Transaction | [optional] 
**status** | **str** | The Digital Signature Transaction may have the following statuses:   - &#x60;waiting&#x60;: Not all the documents has ben uploaded and validated yet   - &#x60;pending&#x60;: The DST is ready to be signed   - &#x60;performed&#x60;: The DST has been signed by all the signers   - &#x60;expired&#x60;: The DST expired before all the signers have signed it   - &#x60;cancelled&#x60;: The DST has been canceled; the motivation is in the reason  | [optional] 
**created** | **str** | Date of creation of the Digital Signature Transaction | [optional] 
**reason** | **str** | The motivations for the cancellation may be:   - &#x60;CANNOT_DOWNLOAD_DOCUMENT&#x60;: Signing Today could not download the     document   - &#x60;INVALID_DOCUMENT&#x60;: The downloaded document is not valid   - &#x60;PROTECTED_DOCUMENT&#x60;: The document is protected by password   - &#x60;declined&#x60;: One of the documents has been refused   - &#x60;MOTIVAZIONE_ESPLICITA&#x60;: Rejected from the system with a custom     reason  | [optional] 
**title** | **str** | Title of the Digital Signature Transaction | [optional] 
**not_after** | **str** | Deadline of the Digital Signature Transaction, expressed in ISO format | [optional] 
**urlback** | **str** | The url for the redirection from signature tray when the Digital Signature Transaction is completed or refused | [optional] 
**cancelback** | **str** | If set, in the signature tray will be displayed a button that needs to go back to a third part application | [optional] 
**template_name** | **str** | A label to indicate the template used to create the Digital Signature Transaction | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


