# Options


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**samples_save** | **bool** | Always save all generated images | [optional]  if omitted the server will use the default value of True
**samples_format** | **str** | File format for images | [optional]  if omitted the server will use the default value of "png"
**samples_filename_pattern** | **str** | Images filename pattern | [optional]  if omitted the server will use the default value of ""
**save_images_add_number** | **bool** | Add number to filename when saving | [optional]  if omitted the server will use the default value of True
**grid_save** | **bool** | Always save all generated image grids | [optional]  if omitted the server will use the default value of True
**grid_format** | **str** | File format for grids | [optional]  if omitted the server will use the default value of "png"
**grid_extended_filename** | **bool** | Add extended info (seed, prompt) to filename when saving grid | [optional]  if omitted the server will use the default value of False
**grid_only_if_multiple** | **bool** | Do not save grids consisting of one picture | [optional]  if omitted the server will use the default value of True
**grid_prevent_empty_spots** | **bool** | Prevent empty spots in grid (when set to autodetect) | [optional]  if omitted the server will use the default value of False
**n_rows** | **float** | Grid row count; use -1 for autodetect and 0 for it to be same as batch size | [optional]  if omitted the server will use the default value of -1
**enable_pnginfo** | **bool** | Save text information about generation parameters as chunks to png files | [optional]  if omitted the server will use the default value of True
**save_txt** | **bool** | Create a text file next to every image with generation parameters. | [optional]  if omitted the server will use the default value of False
**save_images_before_face_restoration** | **bool** | Save a copy of image before doing face restoration. | [optional]  if omitted the server will use the default value of False
**save_images_before_highres_fix** | **bool** | Save a copy of image before applying highres fix. | [optional]  if omitted the server will use the default value of False
**save_images_before_color_correction** | **bool** | Save a copy of image before applying color correction to img2img results | [optional]  if omitted the server will use the default value of False
**save_mask** | **bool** | For inpainting, save a copy of the greyscale mask | [optional]  if omitted the server will use the default value of False
**save_mask_composite** | **bool** | For inpainting, save a masked composite | [optional]  if omitted the server will use the default value of False
**jpeg_quality** | **float** | Quality for saved jpeg images | [optional]  if omitted the server will use the default value of 80
**webp_lossless** | **bool** | Use lossless compression for webp images | [optional]  if omitted the server will use the default value of False
**export_for_4chan** | **bool** | If the saved image file size is above the limit, or its either width or height are above the limit, save a downscaled copy as JPG | [optional]  if omitted the server will use the default value of True
**img_downscale_threshold** | **float** | File size limit for the above option, MB | [optional]  if omitted the server will use the default value of 4.0
**target_side_length** | **float** | Width/height limit for the above option, in pixels | [optional]  if omitted the server will use the default value of 4000
**img_max_size_mp** | **float** | Maximum image size, in megapixels | [optional]  if omitted the server will use the default value of 200
**use_original_name_batch** | **bool** | Use original name for output filename during batch process in extras tab | [optional]  if omitted the server will use the default value of True
**use_upscaler_name_as_suffix** | **bool** | Use upscaler name as filename suffix in the extras tab | [optional]  if omitted the server will use the default value of False
**save_selected_only** | **bool** | When using &#39;Save&#39; button, only save a single selected image | [optional]  if omitted the server will use the default value of True
**do_not_add_watermark** | **bool** | Do not add watermark to images | [optional]  if omitted the server will use the default value of False
**temp_dir** | **str** | Directory for temporary images; leave empty for default | [optional]  if omitted the server will use the default value of ""
**clean_temp_dir_at_start** | **bool** | Cleanup non-default temporary directory when starting webui | [optional]  if omitted the server will use the default value of False
**outdir_samples** | **str** | Output directory for images; if empty, defaults to three directories below | [optional]  if omitted the server will use the default value of ""
**outdir_txt2img_samples** | **str** | Output directory for txt2img images | [optional]  if omitted the server will use the default value of "outputs/txt2img-images"
**outdir_img2img_samples** | **str** | Output directory for img2img images | [optional]  if omitted the server will use the default value of "outputs/img2img-images"
**outdir_extras_samples** | **str** | Output directory for images from extras tab | [optional]  if omitted the server will use the default value of "outputs/extras-images"
**outdir_grids** | **str** | Output directory for grids; if empty, defaults to two directories below | [optional]  if omitted the server will use the default value of ""
**outdir_txt2img_grids** | **str** | Output directory for txt2img grids | [optional]  if omitted the server will use the default value of "outputs/txt2img-grids"
**outdir_img2img_grids** | **str** | Output directory for img2img grids | [optional]  if omitted the server will use the default value of "outputs/img2img-grids"
**outdir_save** | **str** | Directory for saving images using the Save button | [optional]  if omitted the server will use the default value of "log/images"
**save_to_dirs** | **bool** | Save images to a subdirectory | [optional]  if omitted the server will use the default value of True
**grid_save_to_dirs** | **bool** | Save grids to a subdirectory | [optional]  if omitted the server will use the default value of True
**use_save_to_dirs_for_ui** | **bool** | When using \&quot;Save\&quot; button, save images to a subdirectory | [optional]  if omitted the server will use the default value of False
**directories_filename_pattern** | **str** | Directory name pattern | [optional]  if omitted the server will use the default value of "[date]"
**directories_max_prompt_words** | **float** | Max prompt words for [prompt_words] pattern | [optional]  if omitted the server will use the default value of 8
**esrgan_tile** | **float** | Tile size for ESRGAN upscalers. 0 &#x3D; no tiling. | [optional]  if omitted the server will use the default value of 192
**esrgan_tile_overlap** | **float** | Tile overlap, in pixels for ESRGAN upscalers. Low values &#x3D; visible seam. | [optional]  if omitted the server will use the default value of 8
**realesrgan_enabled_models** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | Select which Real-ESRGAN models to show in the web UI. (Requires restart) | [optional]  if omitted the server will use the default value of ["R-ESRGAN 4x+","R-ESRGAN 4x+ Anime6B"]
**upscaler_for_img2img** | **none_type** | Upscaler for img2img | [optional] 
**face_restoration_model** | **str** | Face restoration model | [optional]  if omitted the server will use the default value of "CodeFormer"
**code_former_weight** | **float** | CodeFormer weight parameter; 0 &#x3D; maximum effect; 1 &#x3D; minimum effect | [optional]  if omitted the server will use the default value of 0.5
**face_restoration_unload** | **bool** | Move face restoration model from VRAM into RAM after processing | [optional]  if omitted the server will use the default value of False
**show_warnings** | **bool** | Show warnings in console. | [optional]  if omitted the server will use the default value of False
**memmon_poll_rate** | **float** | VRAM usage polls per second during generation. Set to 0 to disable. | [optional]  if omitted the server will use the default value of 8
**samples_log_stdout** | **bool** | Always print all generation info to standard output | [optional]  if omitted the server will use the default value of False
**multiple_tqdm** | **bool** | Add a second progress bar to the console that shows progress for an entire job. | [optional]  if omitted the server will use the default value of True
**print_hypernet_extra** | **bool** | Print extra hypernetwork information to console. | [optional]  if omitted the server will use the default value of False
**unload_models_when_training** | **bool** | Move VAE and CLIP to RAM when training if possible. Saves VRAM. | [optional]  if omitted the server will use the default value of False
**pin_memory** | **bool** | Turn on pin_memory for DataLoader. Makes training slightly faster but can increase memory usage. | [optional]  if omitted the server will use the default value of False
**save_optimizer_state** | **bool** | Saves Optimizer state as separate *.optim file. Training of embedding or HN can be resumed with the matching optim file. | [optional]  if omitted the server will use the default value of False
**save_training_settings_to_txt** | **bool** | Save textual inversion and hypernet settings to a text file whenever training starts. | [optional]  if omitted the server will use the default value of True
**dataset_filename_word_regex** | **str** | Filename word regex | [optional]  if omitted the server will use the default value of ""
**dataset_filename_join_string** | **str** | Filename join string | [optional]  if omitted the server will use the default value of " "
**training_image_repeats_per_epoch** | **float** | Number of repeats for a single input image per epoch; used only for displaying epoch number | [optional]  if omitted the server will use the default value of 1
**training_write_csv_every** | **float** | Save an csv containing the loss to log directory every N steps, 0 to disable | [optional]  if omitted the server will use the default value of 500
**training_xattention_optimizations** | **bool** | Use cross attention optimizations while training | [optional]  if omitted the server will use the default value of False
**training_enable_tensorboard** | **bool** | Enable tensorboard logging. | [optional]  if omitted the server will use the default value of False
**training_tensorboard_save_images** | **bool** | Save generated images within tensorboard. | [optional]  if omitted the server will use the default value of False
**training_tensorboard_flush_every** | **float** | How often, in seconds, to flush the pending tensorboard events and summaries to disk. | [optional]  if omitted the server will use the default value of 120
**sd_model_checkpoint** | **str** | Stable Diffusion checkpoint | [optional] 
**sd_checkpoint_cache** | **float** | Checkpoints to cache in RAM | [optional]  if omitted the server will use the default value of 0
**sd_vae_checkpoint_cache** | **float** | VAE Checkpoints to cache in RAM | [optional]  if omitted the server will use the default value of 0
**sd_vae** | **str** | SD VAE | [optional]  if omitted the server will use the default value of "Automatic"
**sd_vae_as_default** | **bool** | Ignore selected VAE for stable diffusion checkpoints that have their own .vae.pt next to them | [optional]  if omitted the server will use the default value of True
**inpainting_mask_weight** | **float** | Inpainting conditioning mask strength | [optional]  if omitted the server will use the default value of 1.0
**initial_noise_multiplier** | **float** | Noise multiplier for img2img | [optional]  if omitted the server will use the default value of 1.0
**img2img_color_correction** | **bool** | Apply color correction to img2img results to match original colors. | [optional]  if omitted the server will use the default value of False
**img2img_fix_steps** | **bool** | With img2img, do exactly the amount of steps the slider specifies (normally you&#39;d do less with less denoising). | [optional]  if omitted the server will use the default value of False
**img2img_background_color** | **str** | With img2img, fill image&#39;s transparent parts with this color. | [optional]  if omitted the server will use the default value of "#ffffff"
**enable_quantization** | **bool** | Enable quantization in K samplers for sharper and cleaner results. This may change existing seeds. Requires restart to apply. | [optional]  if omitted the server will use the default value of False
**enable_emphasis** | **bool** | Emphasis: use (text) to make model pay more attention to text and [text] to make it pay less attention | [optional]  if omitted the server will use the default value of True
**enable_batch_seeds** | **bool** | Make K-diffusion samplers produce same images in a batch as when making a single image | [optional]  if omitted the server will use the default value of True
**comma_padding_backtrack** | **float** | Increase coherency by padding from the last comma within n tokens when using more than 75 tokens | [optional]  if omitted the server will use the default value of 20
**clip_stop_at_last_layers** | **float** | Clip skip | [optional]  if omitted the server will use the default value of 1
**upcast_attn** | **bool** | Upcast cross attention layer to float32 | [optional]  if omitted the server will use the default value of False
**use_old_emphasis_implementation** | **bool** | Use old emphasis implementation. Can be useful to reproduce old seeds. | [optional]  if omitted the server will use the default value of False
**use_old_karras_scheduler_sigmas** | **bool** | Use old karras scheduler sigmas (0.1 to 10). | [optional]  if omitted the server will use the default value of False
**no_dpmpp_sde_batch_determinism** | **bool** | Do not make DPM++ SDE deterministic across different batch sizes. | [optional]  if omitted the server will use the default value of False
**use_old_hires_fix_width_height** | **bool** | For hires fix, use width/height sliders to set final resolution rather than first pass (disables Upscale by, Resize width/height to). | [optional]  if omitted the server will use the default value of False
**interrogate_keep_models_in_memory** | **bool** | Interrogate: keep models in VRAM | [optional]  if omitted the server will use the default value of False
**interrogate_return_ranks** | **bool** | Interrogate: include ranks of model tags matches in results (Has no effect on caption-based interrogators). | [optional]  if omitted the server will use the default value of False
**interrogate_clip_num_beams** | **float** | Interrogate: num_beams for BLIP | [optional]  if omitted the server will use the default value of 1
**interrogate_clip_min_length** | **float** | Interrogate: minimum description length (excluding artists, etc..) | [optional]  if omitted the server will use the default value of 24
**interrogate_clip_max_length** | **float** | Interrogate: maximum description length | [optional]  if omitted the server will use the default value of 48
**interrogate_clip_dict_limit** | **float** | CLIP: maximum number of lines in text file (0 &#x3D; No limit) | [optional]  if omitted the server will use the default value of 1500
**interrogate_clip_skip_categories** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | CLIP: skip inquire categories | [optional]  if omitted the server will use the default value of []
**interrogate_deepbooru_score_threshold** | **float** | Interrogate: deepbooru score threshold | [optional]  if omitted the server will use the default value of 0.5
**deepbooru_sort_alpha** | **bool** | Interrogate: deepbooru sort alphabetically | [optional]  if omitted the server will use the default value of True
**deepbooru_use_spaces** | **bool** | use spaces for tags in deepbooru | [optional]  if omitted the server will use the default value of False
**deepbooru_escape** | **bool** | escape (\\) brackets in deepbooru (so they are used as literal brackets and not for emphasis) | [optional]  if omitted the server will use the default value of True
**deepbooru_filter_tags** | **str** | filter out those tags from deepbooru output (separated by comma) | [optional]  if omitted the server will use the default value of ""
**extra_networks_default_view** | **str** | Default view for Extra Networks | [optional]  if omitted the server will use the default value of "cards"
**extra_networks_default_multiplier** | **float** | Multiplier for extra networks | [optional]  if omitted the server will use the default value of 1.0
**extra_networks_card_width** | **float** | Card width for Extra Networks (px) | [optional]  if omitted the server will use the default value of 0
**extra_networks_card_height** | **float** | Card height for Extra Networks (px) | [optional]  if omitted the server will use the default value of 0
**extra_networks_add_text_separator** | **str** | Extra text to add before &lt;...&gt; when adding extra network to prompt | [optional]  if omitted the server will use the default value of " "
**sd_hypernetwork** | **str** | Add hypernetwork to prompt | [optional]  if omitted the server will use the default value of "None"
**return_grid** | **bool** | Show grid in results for web | [optional]  if omitted the server will use the default value of True
**return_mask** | **bool** | For inpainting, include the greyscale mask in results for web | [optional]  if omitted the server will use the default value of False
**return_mask_composite** | **bool** | For inpainting, include masked composite in results for web | [optional]  if omitted the server will use the default value of False
**do_not_show_images** | **bool** | Do not show any images in results for web | [optional]  if omitted the server will use the default value of False
**add_model_hash_to_info** | **bool** | Add model hash to generation information | [optional]  if omitted the server will use the default value of True
**add_model_name_to_info** | **bool** | Add model name to generation information | [optional]  if omitted the server will use the default value of True
**disable_weights_auto_swap** | **bool** | When reading generation parameters from text into UI (from PNG info or pasted text), do not change the selected model/checkpoint. | [optional]  if omitted the server will use the default value of True
**send_seed** | **bool** | Send seed when sending prompt or image to other interface | [optional]  if omitted the server will use the default value of True
**send_size** | **bool** | Send size when sending prompt or image to another interface | [optional]  if omitted the server will use the default value of True
**font** | **str** | Font for image grids that have text | [optional]  if omitted the server will use the default value of ""
**js_modal_lightbox** | **bool** | Enable full page image viewer | [optional]  if omitted the server will use the default value of True
**js_modal_lightbox_initially_zoomed** | **bool** | Show images zoomed in by default in full page image viewer | [optional]  if omitted the server will use the default value of True
**show_progress_in_title** | **bool** | Show generation progress in window title. | [optional]  if omitted the server will use the default value of True
**samplers_in_dropdown** | **bool** | Use dropdown for sampler selection instead of radio group | [optional]  if omitted the server will use the default value of True
**dimensions_and_batch_together** | **bool** | Show Width/Height and Batch sliders in same row | [optional]  if omitted the server will use the default value of True
**keyedit_precision_attention** | **float** | Ctrl+up/down precision when editing (attention:1.1) | [optional]  if omitted the server will use the default value of 0.1
**keyedit_precision_extra** | **float** | Ctrl+up/down precision when editing &lt;extra networks:0.9&gt; | [optional]  if omitted the server will use the default value of 0.05
**quicksettings** | **str** | Quicksettings list | [optional]  if omitted the server will use the default value of "sd_model_checkpoint"
**hidden_tabs** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | Hidden UI tabs (requires restart) | [optional]  if omitted the server will use the default value of []
**ui_reorder** | **str** | txt2img/img2img UI item order | [optional]  if omitted the server will use the default value of "inpaint, sampler, checkboxes, hires_fix, dimensions, cfg, seed, batch, override_settings, scripts"
**ui_extra_networks_tab_reorder** | **str** | Extra networks tab order | [optional]  if omitted the server will use the default value of ""
**localization** | **str** | Localization (requires restart) | [optional]  if omitted the server will use the default value of "None"
**show_progressbar** | **bool** | Show progressbar | [optional]  if omitted the server will use the default value of True
**live_previews_enable** | **bool** | Show live previews of the created image | [optional]  if omitted the server will use the default value of True
**show_progress_grid** | **bool** | Show previews of all images generated in a batch as a grid | [optional]  if omitted the server will use the default value of True
**show_progress_every_n_steps** | **float** | Show new live preview image every N sampling steps. Set to -1 to show after completion of batch. | [optional]  if omitted the server will use the default value of 10
**show_progress_type** | **str** | Image creation progress preview mode | [optional]  if omitted the server will use the default value of "Approx NN"
**live_preview_content** | **str** | Live preview subject | [optional]  if omitted the server will use the default value of "Prompt"
**live_preview_refresh_period** | **float** | Progressbar/preview update period, in milliseconds | [optional]  if omitted the server will use the default value of 1000
**hide_samplers** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | Hide samplers in user interface (requires restart) | [optional]  if omitted the server will use the default value of []
**eta_ddim** | **float** | eta (noise multiplier) for DDIM | [optional]  if omitted the server will use the default value of 0.0
**eta_ancestral** | **float** | eta (noise multiplier) for ancestral samplers | [optional]  if omitted the server will use the default value of 1.0
**ddim_discretize** | **str** | img2img DDIM discretize | [optional]  if omitted the server will use the default value of "uniform"
**s_churn** | **float** | sigma churn | [optional]  if omitted the server will use the default value of 0.0
**s_tmin** | **float** | sigma tmin | [optional]  if omitted the server will use the default value of 0.0
**s_noise** | **float** | sigma noise | [optional]  if omitted the server will use the default value of 1.0
**eta_noise_seed_delta** | **float** | Eta noise seed delta | [optional]  if omitted the server will use the default value of 0
**always_discard_next_to_last_sigma** | **bool** | Always discard next-to-last sigma | [optional]  if omitted the server will use the default value of False
**uni_pc_variant** | **str** | UniPC variant | [optional]  if omitted the server will use the default value of "bh1"
**uni_pc_skip_type** | **str** | UniPC skip type | [optional]  if omitted the server will use the default value of "time_uniform"
**uni_pc_order** | **float** | UniPC order (must be &lt; sampling steps) | [optional]  if omitted the server will use the default value of 3
**uni_pc_lower_order_final** | **bool** | UniPC lower order final | [optional]  if omitted the server will use the default value of True
**postprocessing_enable_in_main_ui** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | Enable postprocessing operations in txt2img and img2img tabs | [optional]  if omitted the server will use the default value of []
**postprocessing_operation_order** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | Postprocessing operation order | [optional]  if omitted the server will use the default value of []
**upscaling_max_images_in_cache** | **float** | Maximum number of images in upscaling cache | [optional]  if omitted the server will use the default value of 5
**disabled_extensions** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | Disable these extensions | [optional]  if omitted the server will use the default value of []
**disable_all_extensions** | **str** | Disable all extensions (preserves the list of disabled extensions) | [optional]  if omitted the server will use the default value of "none"
**sd_checkpoint_hash** | **str** | SHA256 hash of the current checkpoint | [optional]  if omitted the server will use the default value of ""
**sd_lyco** | **str** | Add LyCORIS to prompt | [optional]  if omitted the server will use the default value of "None"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


