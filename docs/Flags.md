# Flags


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**f** | **bool** | &#x3D;&#x3D;SUPPRESS&#x3D;&#x3D; | [optional]  if omitted the server will use the default value of False
**update_all_extensions** | **bool** | launch.py argument: download updates for all extensions when starting the program | [optional]  if omitted the server will use the default value of False
**skip_python_version_check** | **bool** | launch.py argument: do not check python version | [optional]  if omitted the server will use the default value of False
**skip_torch_cuda_test** | **bool** | launch.py argument: do not check if CUDA is able to work properly | [optional]  if omitted the server will use the default value of False
**reinstall_xformers** | **bool** | launch.py argument: install the appropriate version of xformers even if you have some version already installed | [optional]  if omitted the server will use the default value of False
**reinstall_torch** | **bool** | launch.py argument: install the appropriate version of torch even if you have some version already installed | [optional]  if omitted the server will use the default value of False
**update_check** | **bool** | launch.py argument: chck for updates at startup | [optional]  if omitted the server will use the default value of False
**tests** | **str** | launch.py argument: run tests in the specified directory | [optional] 
**no_tests** | **bool** | launch.py argument: do not run tests even if --tests option is specified | [optional]  if omitted the server will use the default value of False
**skip_install** | **bool** | launch.py argument: skip installation of packages | [optional]  if omitted the server will use the default value of False
**data_dir** | **str** | base path where all user data is stored | [optional]  if omitted the server will use the default value of "/sd"
**config** | **str** | path to config which constructs model | [optional]  if omitted the server will use the default value of "/sd/configs/v1-inference.yaml"
**ckpt** | **str** | path to checkpoint of stable diffusion model; if specified, this checkpoint will be added to the list of checkpoints and loaded | [optional]  if omitted the server will use the default value of "/sd/model.ckpt"
**ckpt_dir** | **str** | Path to directory with stable diffusion checkpoints | [optional] 
**vae_dir** | **str** | Path to directory with VAE files | [optional] 
**gfpgan_dir** | **str** | GFPGAN directory | [optional]  if omitted the server will use the default value of "./GFPGAN"
**gfpgan_model** | **str** | GFPGAN model file name | [optional] 
**no_half** | **bool** | do not switch the model to 16-bit floats | [optional]  if omitted the server will use the default value of False
**no_half_vae** | **bool** | do not switch the VAE model to 16-bit floats | [optional]  if omitted the server will use the default value of False
**no_progressbar_hiding** | **bool** | do not hide progressbar in gradio UI (we hide it because it slows down ML if you have hardware acceleration in browser) | [optional]  if omitted the server will use the default value of False
**max_batch_count** | **int** | maximum batch count value for the UI | [optional]  if omitted the server will use the default value of 16
**embeddings_dir** | **str** | embeddings directory for textual inversion (default: embeddings) | [optional]  if omitted the server will use the default value of "/sd/embeddings"
**textual_inversion_templates_dir** | **str** | directory with textual inversion templates | [optional]  if omitted the server will use the default value of "/sd/textual_inversion_templates"
**hypernetwork_dir** | **str** | hypernetwork directory | [optional]  if omitted the server will use the default value of "/sd/models/hypernetworks"
**localizations_dir** | **str** | localizations directory | [optional]  if omitted the server will use the default value of "/sd/localizations"
**allow_code** | **bool** | allow custom script execution from webui | [optional]  if omitted the server will use the default value of False
**medvram** | **bool** | enable stable diffusion model optimizations for sacrificing a little speed for low VRM usage | [optional]  if omitted the server will use the default value of False
**lowvram** | **bool** | enable stable diffusion model optimizations for sacrificing a lot of speed for very low VRM usage | [optional]  if omitted the server will use the default value of False
**lowram** | **bool** | load stable diffusion checkpoint weights to VRAM instead of RAM | [optional]  if omitted the server will use the default value of False
**always_batch_cond_uncond** | **bool** | disables cond/uncond batching that is enabled to save memory with --medvram or --lowvram | [optional]  if omitted the server will use the default value of False
**unload_gfpgan** | **bool** | does not do anything. | [optional]  if omitted the server will use the default value of False
**precision** | **str** | evaluate at this precision | [optional]  if omitted the server will use the default value of "autocast"
**upcast_sampling** | **bool** | upcast sampling. No effect with --no-half. Usually produces similar results to --no-half with better performance while using less memory. | [optional]  if omitted the server will use the default value of False
**share** | **bool** | use share&#x3D;True for gradio and make the UI accessible through their site | [optional]  if omitted the server will use the default value of False
**ngrok** | **str** | ngrok authtoken, alternative to gradio --share | [optional] 
**ngrok_region** | **str** | The region in which ngrok should start. | [optional]  if omitted the server will use the default value of "us"
**enable_insecure_extension_access** | **bool** | enable extensions tab regardless of other options | [optional]  if omitted the server will use the default value of False
**codeformer_models_path** | **str** | Path to directory with codeformer model file(s). | [optional]  if omitted the server will use the default value of "/sd/models/Codeformer"
**gfpgan_models_path** | **str** | Path to directory with GFPGAN model file(s). | [optional]  if omitted the server will use the default value of "/sd/models/GFPGAN"
**esrgan_models_path** | **str** | Path to directory with ESRGAN model file(s). | [optional]  if omitted the server will use the default value of "/sd/models/ESRGAN"
**bsrgan_models_path** | **str** | Path to directory with BSRGAN model file(s). | [optional]  if omitted the server will use the default value of "/sd/models/BSRGAN"
**realesrgan_models_path** | **str** | Path to directory with RealESRGAN model file(s). | [optional]  if omitted the server will use the default value of "/sd/models/RealESRGAN"
**clip_models_path** | **str** | Path to directory with CLIP model file(s). | [optional] 
**xformers** | **bool** | enable xformers for cross attention layers | [optional]  if omitted the server will use the default value of False
**force_enable_xformers** | **bool** | enable xformers for cross attention layers regardless of whether the checking code thinks you can run it; do not make bug reports if this fails to work | [optional]  if omitted the server will use the default value of False
**xformers_flash_attention** | **bool** | enable xformers with Flash Attention to improve reproducibility (supported for SD2.x or variant only) | [optional]  if omitted the server will use the default value of False
**deepdanbooru** | **bool** | does not do anything | [optional]  if omitted the server will use the default value of False
**opt_split_attention** | **bool** | force-enables Doggettx&#39;s cross-attention layer optimization. By default, it&#39;s on for torch cuda. | [optional]  if omitted the server will use the default value of False
**opt_sub_quad_attention** | **bool** | enable memory efficient sub-quadratic cross-attention layer optimization | [optional]  if omitted the server will use the default value of False
**sub_quad_q_chunk_size** | **int** | query chunk size for the sub-quadratic cross-attention layer optimization to use | [optional]  if omitted the server will use the default value of 1024
**sub_quad_kv_chunk_size** | **str** | kv chunk size for the sub-quadratic cross-attention layer optimization to use | [optional] 
**sub_quad_chunk_threshold** | **str** | the percentage of VRAM threshold for the sub-quadratic cross-attention layer optimization to use chunking | [optional] 
**opt_split_attention_invokeai** | **bool** | force-enables InvokeAI&#39;s cross-attention layer optimization. By default, it&#39;s on when cuda is unavailable. | [optional]  if omitted the server will use the default value of False
**opt_split_attention_v1** | **bool** | enable older version of split attention optimization that does not consume all the VRAM it can find | [optional]  if omitted the server will use the default value of False
**opt_sdp_attention** | **bool** | enable scaled dot product cross-attention layer optimization; requires PyTorch 2.* | [optional]  if omitted the server will use the default value of False
**opt_sdp_no_mem_attention** | **bool** | enable scaled dot product cross-attention layer optimization without memory efficient attention, makes image generation deterministic; requires PyTorch 2.* | [optional]  if omitted the server will use the default value of False
**disable_opt_split_attention** | **bool** | force-disables cross-attention layer optimization | [optional]  if omitted the server will use the default value of False
**disable_nan_check** | **bool** | do not check if produced images/latent spaces have nans; useful for running without a checkpoint in CI | [optional]  if omitted the server will use the default value of False
**use_cpu** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | use CPU as torch device for specified modules | [optional]  if omitted the server will use the default value of []
**listen** | **bool** | launch gradio with 0.0.0.0 as server name, allowing to respond to network requests | [optional]  if omitted the server will use the default value of False
**port** | **str** | launch gradio with given server port, you need root/admin rights for ports &lt; 1024, defaults to 7860 if available | [optional] 
**show_negative_prompt** | **bool** | does not do anything | [optional]  if omitted the server will use the default value of False
**ui_config_file** | **str** | filename to use for ui configuration | [optional]  if omitted the server will use the default value of "/sd/ui-config.json"
**hide_ui_dir_config** | **bool** | hide directory configuration from webui | [optional]  if omitted the server will use the default value of False
**freeze_settings** | **bool** | disable editing settings | [optional]  if omitted the server will use the default value of False
**ui_settings_file** | **str** | filename to use for ui settings | [optional]  if omitted the server will use the default value of "/sd/config.json"
**gradio_debug** | **bool** | launch gradio with --debug option | [optional]  if omitted the server will use the default value of False
**gradio_auth** | **str** | set gradio authentication like \&quot;username:password\&quot;; or comma-delimit multiple like \&quot;u1:p1,u2:p2,u3:p3\&quot; | [optional] 
**gradio_auth_path** | **str** | set gradio authentication file path ex. \&quot;/path/to/auth/file\&quot; same auth format as --gradio-auth | [optional] 
**gradio_img2img_tool** | **str** | does not do anything | [optional] 
**gradio_inpaint_tool** | **str** | does not do anything | [optional] 
**opt_channelslast** | **bool** | change memory type for stable diffusion to channels last | [optional]  if omitted the server will use the default value of False
**styles_file** | **str** | filename to use for styles | [optional]  if omitted the server will use the default value of "/sd/styles.csv"
**autolaunch** | **bool** | open the webui URL in the system&#39;s default browser upon launch | [optional]  if omitted the server will use the default value of False
**theme** | **str** | launches the UI with light or dark theme | [optional] 
**use_textbox_seed** | **bool** | use textbox for seeds in UI (no up/down, but possible to input long seeds) | [optional]  if omitted the server will use the default value of False
**disable_console_progressbars** | **bool** | do not output progressbars to console | [optional]  if omitted the server will use the default value of False
**enable_console_prompts** | **bool** | print prompts to console when generating with txt2img and img2img | [optional]  if omitted the server will use the default value of False
**vae_path** | **str** | Checkpoint to use as VAE; setting this argument disables all settings related to VAE | [optional] 
**disable_safe_unpickle** | **bool** | disable checking pytorch models for malicious code | [optional]  if omitted the server will use the default value of False
**api** | **bool** | use api&#x3D;True to launch the API together with the webui (use --nowebui instead for only the API) | [optional]  if omitted the server will use the default value of False
**api_auth** | **str** | Set authentication for API like \&quot;username:password\&quot;; or comma-delimit multiple like \&quot;u1:p1,u2:p2,u3:p3\&quot; | [optional] 
**api_log** | **bool** | use api-log&#x3D;True to enable logging of all API requests | [optional]  if omitted the server will use the default value of False
**nowebui** | **bool** | use api&#x3D;True to launch the API instead of the webui | [optional]  if omitted the server will use the default value of False
**ui_debug_mode** | **bool** | Don&#39;t load model to quickly launch UI | [optional]  if omitted the server will use the default value of False
**device_id** | **str** | Select the default CUDA device to use (export CUDA_VISIBLE_DEVICES&#x3D;0,1,etc might be needed before) | [optional] 
**administrator** | **bool** | Administrator rights | [optional]  if omitted the server will use the default value of False
**cors_allow_origins** | **str** | Allowed CORS origin(s) in the form of a comma-separated list (no spaces) | [optional] 
**cors_allow_origins_regex** | **str** | Allowed CORS origin(s) in the form of a single regular expression | [optional] 
**tls_keyfile** | **str** | Partially enables TLS, requires --tls-certfile to fully function | [optional] 
**tls_certfile** | **str** | Partially enables TLS, requires --tls-keyfile to fully function | [optional] 
**server_name** | **str** | Sets hostname of server | [optional] 
**gradio_queue** | **bool** | does not do anything | [optional]  if omitted the server will use the default value of True
**no_gradio_queue** | **bool** | Disables gradio queue; causes the webpage to use http requests instead of websockets; was the defaul in earlier versions | [optional]  if omitted the server will use the default value of False
**skip_version_check** | **bool** | Do not check versions of torch and xformers | [optional]  if omitted the server will use the default value of False
**no_hashing** | **bool** | disable sha256 hashing of checkpoints to help loading performance | [optional]  if omitted the server will use the default value of False
**no_download_sd_model** | **bool** | don&#39;t download SD1.5 model even if no model is found in --ckpt-dir | [optional]  if omitted the server will use the default value of False
**web_path** | **str** | evaluate at this precision | [optional]  if omitted the server will use the default value of ""
**lyco_dir** | **str** | Path to directory with LyCORIS networks. | [optional]  if omitted the server will use the default value of "/sd/models/LyCORIS"
**addnet_max_model_count** | **int** | The maximum number of additional network model can be used. | [optional]  if omitted the server will use the default value of 5
**controlnet_dir** | **str** | Path to directory with ControlNet models | [optional] 
**controlnet_annotator_models_path** | **str** | Path to directory with annotator model directories | [optional] 
**no_half_controlnet** | **str** | do not switch the ControlNet models to 16-bit floats (only needed without --no-half) | [optional] 
**civitai_endpoint** | **str** | Endpoint for interacting with a Civitai instance | [optional]  if omitted the server will use the default value of "https://civitai.com/api/v1"
**civitai_link_endpoint** | **str** | Endpoint for interacting with a Civitai Link server | [optional]  if omitted the server will use the default value of "https://link.civitai.com/api/socketio"
**deepdanbooru_projects_path** | **str** | Path to directory with DeepDanbooru project(s). | [optional]  if omitted the server will use the default value of "/sd/models/deepdanbooru"
**ldsr_models_path** | **str** | Path to directory with LDSR model file(s). | [optional]  if omitted the server will use the default value of "/sd/models/LDSR"
**lora_dir** | **str** | Path to directory with Lora networks. | [optional]  if omitted the server will use the default value of "/sd/models/Lora"
**scunet_models_path** | **str** | Path to directory with ScuNET model file(s). | [optional]  if omitted the server will use the default value of "/sd/models/ScuNET"
**swinir_models_path** | **str** | Path to directory with SwinIR model file(s). | [optional]  if omitted the server will use the default value of "/sd/models/SwinIR"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


