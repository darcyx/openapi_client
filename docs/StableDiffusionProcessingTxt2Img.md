# StableDiffusionProcessingTxt2Img


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_hr** | **bool** |  | [optional]  if omitted the server will use the default value of False
**denoising_strength** | **float** |  | [optional]  if omitted the server will use the default value of 0
**firstphase_width** | **int** |  | [optional]  if omitted the server will use the default value of 0
**firstphase_height** | **int** |  | [optional]  if omitted the server will use the default value of 0
**hr_scale** | **float** |  | [optional]  if omitted the server will use the default value of 2.0
**hr_upscaler** | **str** |  | [optional] 
**hr_second_pass_steps** | **int** |  | [optional]  if omitted the server will use the default value of 0
**hr_resize_x** | **int** |  | [optional]  if omitted the server will use the default value of 0
**hr_resize_y** | **int** |  | [optional]  if omitted the server will use the default value of 0
**prompt** | **str** |  | [optional]  if omitted the server will use the default value of ""
**styles** | **[str]** |  | [optional] 
**seed** | **int** |  | [optional]  if omitted the server will use the default value of -1
**subseed** | **int** |  | [optional]  if omitted the server will use the default value of -1
**subseed_strength** | **float** |  | [optional]  if omitted the server will use the default value of 0
**seed_resize_from_h** | **int** |  | [optional]  if omitted the server will use the default value of -1
**seed_resize_from_w** | **int** |  | [optional]  if omitted the server will use the default value of -1
**sampler_name** | **str** |  | [optional] 
**batch_size** | **int** |  | [optional]  if omitted the server will use the default value of 1
**n_iter** | **int** |  | [optional]  if omitted the server will use the default value of 1
**steps** | **int** |  | [optional]  if omitted the server will use the default value of 50
**cfg_scale** | **float** |  | [optional]  if omitted the server will use the default value of 7.0
**width** | **int** |  | [optional]  if omitted the server will use the default value of 512
**height** | **int** |  | [optional]  if omitted the server will use the default value of 512
**restore_faces** | **bool** |  | [optional]  if omitted the server will use the default value of False
**tiling** | **bool** |  | [optional]  if omitted the server will use the default value of False
**do_not_save_samples** | **bool** |  | [optional]  if omitted the server will use the default value of False
**do_not_save_grid** | **bool** |  | [optional]  if omitted the server will use the default value of False
**negative_prompt** | **str** |  | [optional] 
**eta** | **float** |  | [optional] 
**s_churn** | **float** |  | [optional]  if omitted the server will use the default value of 0.0
**s_tmax** | **float** |  | [optional] 
**s_tmin** | **float** |  | [optional]  if omitted the server will use the default value of 0.0
**s_noise** | **float** |  | [optional]  if omitted the server will use the default value of 1.0
**override_settings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**override_settings_restore_afterwards** | **bool** |  | [optional]  if omitted the server will use the default value of True
**script_args** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional]  if omitted the server will use the default value of []
**sampler_index** | **str** |  | [optional]  if omitted the server will use the default value of "Euler"
**script_name** | **str** |  | [optional] 
**send_images** | **bool** |  | [optional]  if omitted the server will use the default value of True
**save_images** | **bool** |  | [optional]  if omitted the server will use the default value of False
**alwayson_scripts** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional]  if omitted the server will use the default value of {}
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


