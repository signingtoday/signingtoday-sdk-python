# LFResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of the resource | [optional] 
**domain** | **str** | The _domain_ is the Organization which a user or a DST belongs | [optional] 
**type** | **str** | Type of the resource, for example a _PDFResource_ | [optional] [readonly] 
**dst_uuid** | **str** | Unique id of the _DST_ which the resource is correlated | [optional] [readonly] 
**title** | **str** | Title of the resource | [optional] 
**filename** | **str** | Name of the file uploaded, with its extension as well | [optional] 
**url** | **str** | Url of the resource | [optional] [readonly] 
**size** | **int** | Size of the resource | [optional] [readonly] 
**created_at** | **datetime** | Indicates when the resource has been uploaded | [optional] [readonly] 
**mimetype** | **str** | _MIME_ type of the resource | [optional] [readonly] 
**pages** | **int** | Indicates how many pages the resource is | [optional] 
**extra_data** | **dict(str, object)** | Extra data of the resource | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


