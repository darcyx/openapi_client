# ExtrasBatchImagesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_list** | [**[FileData]**](FileData.md) | List of images to work on. Must be Base64 strings | 
**resize_mode** | **int** | Sets the resize mode: 0 to upscale by upscaling_resize amount, 1 to upscale up to upscaling_resize_h x upscaling_resize_w. | [optional]  if omitted the server will use the default value of 0
**show_extras_results** | **bool** | Should the backend return the generated image? | [optional]  if omitted the server will use the default value of True
**gfpgan_visibility** | **float** | Sets the visibility of GFPGAN, values should be between 0 and 1. | [optional]  if omitted the server will use the default value of 0
**codeformer_visibility** | **float** | Sets the visibility of CodeFormer, values should be between 0 and 1. | [optional]  if omitted the server will use the default value of 0
**codeformer_weight** | **float** | Sets the weight of CodeFormer, values should be between 0 and 1. | [optional]  if omitted the server will use the default value of 0
**upscaling_resize** | **float** | By how much to upscale the image, only used when resize_mode&#x3D;0. | [optional]  if omitted the server will use the default value of 2
**upscaling_resize_w** | **int** | Target width for the upscaler to hit. Only used when resize_mode&#x3D;1. | [optional]  if omitted the server will use the default value of 512
**upscaling_resize_h** | **int** | Target height for the upscaler to hit. Only used when resize_mode&#x3D;1. | [optional]  if omitted the server will use the default value of 512
**upscaling_crop** | **bool** | Should the upscaler crop the image to fit in the chosen size? | [optional]  if omitted the server will use the default value of True
**upscaler_1** | **str** | The name of the main upscaler to use, it has to be one of this list: None , Lanczos , Nearest , R-ESRGAN 4x+ , R-ESRGAN 4x+ Anime6B , RRDB_ESRGAN_x4 | [optional]  if omitted the server will use the default value of "None"
**upscaler_2** | **str** | The name of the secondary upscaler to use, it has to be one of this list: None , Lanczos , Nearest , R-ESRGAN 4x+ , R-ESRGAN 4x+ Anime6B , RRDB_ESRGAN_x4 | [optional]  if omitted the server will use the default value of "None"
**extras_upscaler_2_visibility** | **float** | Sets the visibility of secondary upscaler, values should be between 0 and 1. | [optional]  if omitted the server will use the default value of 0
**upscale_first** | **bool** | Should the upscaler run before restoring faces? | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


