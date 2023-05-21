# ControlNetStableDiffusionProcessingImg2Img


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**init_images** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**resize_mode** | **int** |  | [optional]  if omitted the server will use the default value of 0
**denoising_strength** | **float** |  | [optional]  if omitted the server will use the default value of 0.75
**image_cfg_scale** | **float** |  | [optional] 
**mask** | **str** |  | [optional] 
**mask_blur** | **int** |  | [optional]  if omitted the server will use the default value of 4
**inpainting_fill** | **int** |  | [optional]  if omitted the server will use the default value of 0
**inpaint_full_res** | **bool** |  | [optional]  if omitted the server will use the default value of True
**inpaint_full_res_padding** | **int** |  | [optional]  if omitted the server will use the default value of 0
**inpainting_mask_invert** | **int** |  | [optional]  if omitted the server will use the default value of 0
**initial_noise_multiplier** | **float** |  | [optional] 
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
**include_init_images** | **bool** |  | [optional]  if omitted the server will use the default value of False
**script_name** | **str** |  | [optional] 
**send_images** | **bool** |  | [optional]  if omitted the server will use the default value of True
**save_images** | **bool** |  | [optional]  if omitted the server will use the default value of False
**alwayson_scripts** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional]  if omitted the server will use the default value of {}
**controlnet_units** | [**[ControlNetUnitRequest]**](ControlNetUnitRequest.md) | ControlNet Processing Units | [optional]  if omitted the server will use the default value of [{"input_image":"","mask":"","module":"none","model":"None","weight":1.0,"resize_mode":"Crop and Resize","lowvram":false,"processor_res":64,"threshold_a":64,"threshold_b":64,"guidance":1.0,"guidance_start":0.0,"guidance_end":1.0,"guessmode":true,"pixel_perfect":false}]
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


