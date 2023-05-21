"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from openapi_client.exceptions import ApiAttributeError


def lazy_import():
    from openapi_client.model.control_net_unit_request import ControlNetUnitRequest
    globals()['ControlNetUnitRequest'] = ControlNetUnitRequest


class ControlNetStableDiffusionProcessingTxt2Img(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'enable_hr': (bool,),  # noqa: E501
            'denoising_strength': (float,),  # noqa: E501
            'firstphase_width': (int,),  # noqa: E501
            'firstphase_height': (int,),  # noqa: E501
            'hr_scale': (float,),  # noqa: E501
            'hr_upscaler': (str,),  # noqa: E501
            'hr_second_pass_steps': (int,),  # noqa: E501
            'hr_resize_x': (int,),  # noqa: E501
            'hr_resize_y': (int,),  # noqa: E501
            'prompt': (str,),  # noqa: E501
            'styles': ([str],),  # noqa: E501
            'seed': (int,),  # noqa: E501
            'subseed': (int,),  # noqa: E501
            'subseed_strength': (float,),  # noqa: E501
            'seed_resize_from_h': (int,),  # noqa: E501
            'seed_resize_from_w': (int,),  # noqa: E501
            'sampler_name': (str,),  # noqa: E501
            'batch_size': (int,),  # noqa: E501
            'n_iter': (int,),  # noqa: E501
            'steps': (int,),  # noqa: E501
            'cfg_scale': (float,),  # noqa: E501
            'width': (int,),  # noqa: E501
            'height': (int,),  # noqa: E501
            'restore_faces': (bool,),  # noqa: E501
            'tiling': (bool,),  # noqa: E501
            'do_not_save_samples': (bool,),  # noqa: E501
            'do_not_save_grid': (bool,),  # noqa: E501
            'negative_prompt': (str,),  # noqa: E501
            'eta': (float,),  # noqa: E501
            's_churn': (float,),  # noqa: E501
            's_tmax': (float,),  # noqa: E501
            's_tmin': (float,),  # noqa: E501
            's_noise': (float,),  # noqa: E501
            'override_settings': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'override_settings_restore_afterwards': (bool,),  # noqa: E501
            'script_args': ([bool, date, datetime, dict, float, int, list, str, none_type],),  # noqa: E501
            'sampler_index': (str,),  # noqa: E501
            'script_name': (str,),  # noqa: E501
            'send_images': (bool,),  # noqa: E501
            'save_images': (bool,),  # noqa: E501
            'alwayson_scripts': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'controlnet_units': ([ControlNetUnitRequest],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'enable_hr': 'enable_hr',  # noqa: E501
        'denoising_strength': 'denoising_strength',  # noqa: E501
        'firstphase_width': 'firstphase_width',  # noqa: E501
        'firstphase_height': 'firstphase_height',  # noqa: E501
        'hr_scale': 'hr_scale',  # noqa: E501
        'hr_upscaler': 'hr_upscaler',  # noqa: E501
        'hr_second_pass_steps': 'hr_second_pass_steps',  # noqa: E501
        'hr_resize_x': 'hr_resize_x',  # noqa: E501
        'hr_resize_y': 'hr_resize_y',  # noqa: E501
        'prompt': 'prompt',  # noqa: E501
        'styles': 'styles',  # noqa: E501
        'seed': 'seed',  # noqa: E501
        'subseed': 'subseed',  # noqa: E501
        'subseed_strength': 'subseed_strength',  # noqa: E501
        'seed_resize_from_h': 'seed_resize_from_h',  # noqa: E501
        'seed_resize_from_w': 'seed_resize_from_w',  # noqa: E501
        'sampler_name': 'sampler_name',  # noqa: E501
        'batch_size': 'batch_size',  # noqa: E501
        'n_iter': 'n_iter',  # noqa: E501
        'steps': 'steps',  # noqa: E501
        'cfg_scale': 'cfg_scale',  # noqa: E501
        'width': 'width',  # noqa: E501
        'height': 'height',  # noqa: E501
        'restore_faces': 'restore_faces',  # noqa: E501
        'tiling': 'tiling',  # noqa: E501
        'do_not_save_samples': 'do_not_save_samples',  # noqa: E501
        'do_not_save_grid': 'do_not_save_grid',  # noqa: E501
        'negative_prompt': 'negative_prompt',  # noqa: E501
        'eta': 'eta',  # noqa: E501
        's_churn': 's_churn',  # noqa: E501
        's_tmax': 's_tmax',  # noqa: E501
        's_tmin': 's_tmin',  # noqa: E501
        's_noise': 's_noise',  # noqa: E501
        'override_settings': 'override_settings',  # noqa: E501
        'override_settings_restore_afterwards': 'override_settings_restore_afterwards',  # noqa: E501
        'script_args': 'script_args',  # noqa: E501
        'sampler_index': 'sampler_index',  # noqa: E501
        'script_name': 'script_name',  # noqa: E501
        'send_images': 'send_images',  # noqa: E501
        'save_images': 'save_images',  # noqa: E501
        'alwayson_scripts': 'alwayson_scripts',  # noqa: E501
        'controlnet_units': 'controlnet_units',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ControlNetStableDiffusionProcessingTxt2Img - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            enable_hr (bool): [optional] if omitted the server will use the default value of False  # noqa: E501
            denoising_strength (float): [optional] if omitted the server will use the default value of 0  # noqa: E501
            firstphase_width (int): [optional] if omitted the server will use the default value of 0  # noqa: E501
            firstphase_height (int): [optional] if omitted the server will use the default value of 0  # noqa: E501
            hr_scale (float): [optional] if omitted the server will use the default value of 2.0  # noqa: E501
            hr_upscaler (str): [optional]  # noqa: E501
            hr_second_pass_steps (int): [optional] if omitted the server will use the default value of 0  # noqa: E501
            hr_resize_x (int): [optional] if omitted the server will use the default value of 0  # noqa: E501
            hr_resize_y (int): [optional] if omitted the server will use the default value of 0  # noqa: E501
            prompt (str): [optional] if omitted the server will use the default value of ""  # noqa: E501
            styles ([str]): [optional]  # noqa: E501
            seed (int): [optional] if omitted the server will use the default value of -1  # noqa: E501
            subseed (int): [optional] if omitted the server will use the default value of -1  # noqa: E501
            subseed_strength (float): [optional] if omitted the server will use the default value of 0  # noqa: E501
            seed_resize_from_h (int): [optional] if omitted the server will use the default value of -1  # noqa: E501
            seed_resize_from_w (int): [optional] if omitted the server will use the default value of -1  # noqa: E501
            sampler_name (str): [optional]  # noqa: E501
            batch_size (int): [optional] if omitted the server will use the default value of 1  # noqa: E501
            n_iter (int): [optional] if omitted the server will use the default value of 1  # noqa: E501
            steps (int): [optional] if omitted the server will use the default value of 50  # noqa: E501
            cfg_scale (float): [optional] if omitted the server will use the default value of 7.0  # noqa: E501
            width (int): [optional] if omitted the server will use the default value of 512  # noqa: E501
            height (int): [optional] if omitted the server will use the default value of 512  # noqa: E501
            restore_faces (bool): [optional] if omitted the server will use the default value of False  # noqa: E501
            tiling (bool): [optional] if omitted the server will use the default value of False  # noqa: E501
            do_not_save_samples (bool): [optional] if omitted the server will use the default value of False  # noqa: E501
            do_not_save_grid (bool): [optional] if omitted the server will use the default value of False  # noqa: E501
            negative_prompt (str): [optional]  # noqa: E501
            eta (float): [optional]  # noqa: E501
            s_churn (float): [optional] if omitted the server will use the default value of 0.0  # noqa: E501
            s_tmax (float): [optional]  # noqa: E501
            s_tmin (float): [optional] if omitted the server will use the default value of 0.0  # noqa: E501
            s_noise (float): [optional] if omitted the server will use the default value of 1.0  # noqa: E501
            override_settings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            override_settings_restore_afterwards (bool): [optional] if omitted the server will use the default value of True  # noqa: E501
            script_args ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional] if omitted the server will use the default value of []  # noqa: E501
            sampler_index (str): [optional] if omitted the server will use the default value of "Euler"  # noqa: E501
            script_name (str): [optional]  # noqa: E501
            send_images (bool): [optional] if omitted the server will use the default value of True  # noqa: E501
            save_images (bool): [optional] if omitted the server will use the default value of False  # noqa: E501
            alwayson_scripts ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional] if omitted the server will use the default value of {}  # noqa: E501
            controlnet_units ([ControlNetUnitRequest]): ControlNet Processing Units. [optional] if omitted the server will use the default value of [{"input_image":"","mask":"","module":"none","model":"None","weight":1.0,"resize_mode":"Crop and Resize","lowvram":false,"processor_res":64,"threshold_a":64,"threshold_b":64,"guidance":1.0,"guidance_start":0.0,"guidance_end":1.0,"guessmode":true,"pixel_perfect":false}]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ControlNetStableDiffusionProcessingTxt2Img - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            enable_hr (bool): [optional] if omitted the server will use the default value of False  # noqa: E501
            denoising_strength (float): [optional] if omitted the server will use the default value of 0  # noqa: E501
            firstphase_width (int): [optional] if omitted the server will use the default value of 0  # noqa: E501
            firstphase_height (int): [optional] if omitted the server will use the default value of 0  # noqa: E501
            hr_scale (float): [optional] if omitted the server will use the default value of 2.0  # noqa: E501
            hr_upscaler (str): [optional]  # noqa: E501
            hr_second_pass_steps (int): [optional] if omitted the server will use the default value of 0  # noqa: E501
            hr_resize_x (int): [optional] if omitted the server will use the default value of 0  # noqa: E501
            hr_resize_y (int): [optional] if omitted the server will use the default value of 0  # noqa: E501
            prompt (str): [optional] if omitted the server will use the default value of ""  # noqa: E501
            styles ([str]): [optional]  # noqa: E501
            seed (int): [optional] if omitted the server will use the default value of -1  # noqa: E501
            subseed (int): [optional] if omitted the server will use the default value of -1  # noqa: E501
            subseed_strength (float): [optional] if omitted the server will use the default value of 0  # noqa: E501
            seed_resize_from_h (int): [optional] if omitted the server will use the default value of -1  # noqa: E501
            seed_resize_from_w (int): [optional] if omitted the server will use the default value of -1  # noqa: E501
            sampler_name (str): [optional]  # noqa: E501
            batch_size (int): [optional] if omitted the server will use the default value of 1  # noqa: E501
            n_iter (int): [optional] if omitted the server will use the default value of 1  # noqa: E501
            steps (int): [optional] if omitted the server will use the default value of 50  # noqa: E501
            cfg_scale (float): [optional] if omitted the server will use the default value of 7.0  # noqa: E501
            width (int): [optional] if omitted the server will use the default value of 512  # noqa: E501
            height (int): [optional] if omitted the server will use the default value of 512  # noqa: E501
            restore_faces (bool): [optional] if omitted the server will use the default value of False  # noqa: E501
            tiling (bool): [optional] if omitted the server will use the default value of False  # noqa: E501
            do_not_save_samples (bool): [optional] if omitted the server will use the default value of False  # noqa: E501
            do_not_save_grid (bool): [optional] if omitted the server will use the default value of False  # noqa: E501
            negative_prompt (str): [optional]  # noqa: E501
            eta (float): [optional]  # noqa: E501
            s_churn (float): [optional] if omitted the server will use the default value of 0.0  # noqa: E501
            s_tmax (float): [optional]  # noqa: E501
            s_tmin (float): [optional] if omitted the server will use the default value of 0.0  # noqa: E501
            s_noise (float): [optional] if omitted the server will use the default value of 1.0  # noqa: E501
            override_settings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            override_settings_restore_afterwards (bool): [optional] if omitted the server will use the default value of True  # noqa: E501
            script_args ([bool, date, datetime, dict, float, int, list, str, none_type]): [optional] if omitted the server will use the default value of []  # noqa: E501
            sampler_index (str): [optional] if omitted the server will use the default value of "Euler"  # noqa: E501
            script_name (str): [optional]  # noqa: E501
            send_images (bool): [optional] if omitted the server will use the default value of True  # noqa: E501
            save_images (bool): [optional] if omitted the server will use the default value of False  # noqa: E501
            alwayson_scripts ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional] if omitted the server will use the default value of {}  # noqa: E501
            controlnet_units ([ControlNetUnitRequest]): ControlNet Processing Units. [optional] if omitted the server will use the default value of [{"input_image":"","mask":"","module":"none","model":"None","weight":1.0,"resize_mode":"Crop and Resize","lowvram":false,"processor_res":64,"threshold_a":64,"threshold_b":64,"guidance":1.0,"guidance_start":0.0,"guidance_end":1.0,"guessmode":true,"pixel_perfect":false}]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")