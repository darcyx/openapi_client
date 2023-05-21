# ModulesProgressProgressResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | 
**queued** | **bool** |  | 
**completed** | **bool** |  | 
**progress** | **float** | The progress with a range of 0 to 1 | [optional] 
**eta** | **float** |  | [optional] 
**live_preview** | **str** | Current live preview; a data: uri | [optional] 
**id_live_preview** | **int** | Send this together with next request to prevent receiving same image | [optional] 
**textinfo** | **str** | Info text used by WebUI. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


