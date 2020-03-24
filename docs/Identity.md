# Identity

The Identity is the core object of SigningToday, because inside it there are all the information that allows an user to sign a digital signature transaction. Of course the most important information is the cerficate, which is a base64 string in PEM format. This allows to sign documents with a legal validity. The Identity has as well an expiration date, a status, which may be simply active, error, in case of problems during its emission either if the certificate has been somehow altered, or pending if the enrollment procedure has to be completed (the following steps are indicated in the 'next' field as well). Also there are information about the provider issued the Identity and fields with an url value that allows to send one time passwords or to sign digital signature transactions. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The uuid code that identifies the Identity | [optional] 
**certificate** | **str** | The X.509 certificate in PEM format of the Identity | [optional] 
**not_after** | **str** | Deadline of the Identity, expressed in ISO format | [optional] 
**status** | **str** | Identity status which can be one of the following. When an identity request is send, the identity is created and the status is **pending** until the provider dont&#39;approve the request. Then status of the identity changes to **active**. If for some reason an error occurs during the process, or after that, the status will be **error**  | [optional] 
**next** | **str** | The next step to complete the activation procedure | [optional] 
**actions** | [**IdentityActions**](IdentityActions.md) |  | [optional] 
**provider** | **str** | The name of the provider that issued the certificate for the Identity | [optional] 
**label** | **str** | The label is an arbitrary name is possible to associate to an idenity. Doing so allows to distinguish different identities issued from the same provider during the performance of the signature in the signature tray | [optional] 
**signature_appearance_uri** | **str** | This is the url to the image that will be impressed on the document after the performance of the signature  | [optional] 
**provider_id** | **str** | _provider_id_ is the univocal name of the provider that issued the identity  | [optional] 
**provider_type** | **str** | Type of the provider. The most usual type is **cloud**  | [optional] 
**provider_data** | [**object**](.md) | Data of the provider that issued the certificate, it is variable from provider to provider | [optional] 
**provider_image** | **str** | This is the logo of the provider that issued the identity | [optional] 
**send_otp_url** | **str** | The url to send a one time password to the user which the identity is associated | [optional] 
**sign_url** | **str** | The url to sign a document of a digital signature transaction | [optional] 
**has_been_imported** | **bool** | If the Identity has been imported from another pre-existing Identity the has_been_imported field is set to **true** | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


