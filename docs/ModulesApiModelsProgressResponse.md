# ModulesApiModelsProgressResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**progress** | **float** | The progress with a range of 0 to 1 | 
**eta_relative** | **float** |  | 
**state** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The current state snapshot | 
**current_image** | **str** | The current image in base64 format. opts.show_progress_every_n_steps is required for this to work. | [optional] 
**textinfo** | **str** | Info text used by WebUI. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


