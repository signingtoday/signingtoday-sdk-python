# Organization

The Organization is a meta object of SigningToday. Every single Organization is indipendent from the others, has its token, its rao user and everything else. In this way SigningToday allows the coexistance of many different organizations.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The uuid code that identifies the Organization | [optional] 
**name** | **str** | This is an arbitrary name is possible to associate to the Organization  | [optional] 
**slug** | **str** | This is the _organization-slug_ that is used as parameter in the endpoints or in the body of the requests  | [optional] 
**settings** | [**OrganizationSettings**](OrganizationSettings.md) |  | [optional] 
**logo** | **str** | This is the url to the image is supposed to be used as logo of the Organization, for example the logo or the motto of the company is integrating SigningToday  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


