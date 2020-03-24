# DigitalSignatureTransaction

The **Digital Signature Transaction** is the core object at the center of every `digital signature workflow` in Signing Today. It is a `collection` element and holds every document (to be signed or just attached to the transaction) as well as the signature plan required to fulfill the transaction; how many signatures are required, are there any forms to be filled, appearance, signature sequence, signers... everything starts here. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The uuid code that identifies the Digital Signature Transaction | [optional] [readonly] 
**domain** | **str** | The _domain_ is the Organization which a user or a DST belongs | [optional] 
**title** | **str** | Title of the Digital Signature Transaction | [optional] 
**replaces** | **str** | The _DST_ which this one replaces | [optional] [readonly] 
**replaced_by** | **str** | The _DST_ which has replaces the current one | [optional] [readonly] 
**created_by_user** | **str** | The user created the Digital Signature Transaction | [optional] [readonly] 
**created_at** | **datetime** | Date of creation of the Digital Signature Transaction | [optional] [readonly] 
**documents** | [**list[Document]**](Document.md) | The _documents_ field is an array containing document objects, where everyone of them is defined as follows  | [optional] 
**published_at** | **datetime** | The _date-time_ the DST has been published | [optional] [readonly] 
**expires_at** | **datetime** | Indicates when the DST will expire | [optional] [readonly] 
**resources** | [**list[LFResource]**](LFResource.md) | An array of resources attached to the _DST_, each one defined as follows | [optional] 
**signatures** | [**list[Signature]**](Signature.md) | An array of signatures, each one defined as follows | [optional] 
**status** | **str** | Status of the _Digital Signature Transaction_ | [optional] [readonly] 
**error_message** | **str** | The explication of the occurred error | [optional] 
**deleted_at** | **datetime** | Indicates when the _DST_ has been deleted | [optional] [readonly] 
**tags** | **list[str]** | An array of tags for the _DST_. In such way is possible to tag in the same way some _DSTs_ in order to keep them organized and been easy to find them through the custom search | [optional] 
**template** | **bool** | Indicates if a template has been used to create the DST or not | [optional] 
**public_template** | **bool** | Indicates if a public template has been used to create the DST or not | [optional] 
**extra_data** | **dict(str, object)** | Extra information about the _DST_ | [optional] 
**visible_to** | **list[str]** | UUIDs of the users to which the DST is visible | [optional] 
**cc_groups** | **list[str]** | Name of groups that are informed about the DST | [optional] 
**cc_users** | **list[str]** | UUIDs of the users that are informed about the DST | [optional] 
**urgent** | **bool** | True if the DST is flagged as urgent | [optional] 
**updated_at** | **datetime** | Indicates the last update of the DST, such as the performing of a signature | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


