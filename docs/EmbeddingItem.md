# EmbeddingItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shape** | **int** | The length of each individual vector in the embedding | 
**vectors** | **int** | The number of vectors in the embedding | 
**step** | **int** | The number of steps that were used to train this embedding, if available | [optional] 
**sd_checkpoint** | **str** | The hash of the checkpoint this embedding was trained on, if available | [optional] 
**sd_checkpoint_name** | **str** | The name of the checkpoint this embedding was trained on, if available. Note that this is the name that was used by the trainer; for a stable identifier, use &#x60;sd_checkpoint&#x60; instead | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


