# coding: utf-8

"""
    Twitter OpenAPI

    Twitter OpenAPI(Swagger) specification

    The version of the OpenAPI document: 0.0.1
    Contact: yuki@yuki0311.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import StrictStr

from twitter_openapi_python_generated.models.get_favoriters200_response import GetFavoriters200Response
from twitter_openapi_python_generated.models.get_followers200_response import GetFollowers200Response
from twitter_openapi_python_generated.models.get_retweeters200_response import GetRetweeters200Response

from twitter_openapi_python_generated.api_client import ApiClient
from twitter_openapi_python_generated.api_response import ApiResponse
from twitter_openapi_python_generated.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class UserListApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_favoriters(self, path_query_id : StrictStr, variables : StrictStr, features : StrictStr, **kwargs) -> GetFavoriters200Response:  # noqa: E501
        """get_favoriters  # noqa: E501

        get tweet favoriters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_favoriters(path_query_id, variables, features, async_req=True)
        >>> result = thread.get()

        :param path_query_id: (required)
        :type path_query_id: str
        :param variables: (required)
        :type variables: str
        :param features: (required)
        :type features: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetFavoriters200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_favoriters_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_favoriters_with_http_info(path_query_id, variables, features, **kwargs)  # noqa: E501

    @validate_arguments
    def get_favoriters_with_http_info(self, path_query_id : StrictStr, variables : StrictStr, features : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """get_favoriters  # noqa: E501

        get tweet favoriters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_favoriters_with_http_info(path_query_id, variables, features, async_req=True)
        >>> result = thread.get()

        :param path_query_id: (required)
        :type path_query_id: str
        :param variables: (required)
        :type variables: str
        :param features: (required)
        :type features: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetFavoriters200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'path_query_id',
            'variables',
            'features'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_favoriters" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['path_query_id']:
            _path_params['pathQueryId'] = _params['path_query_id']


        # process the query parameters
        _query_params = []
        if _params.get('variables') is not None:  # noqa: E501
            _query_params.append(('variables', _params['variables']))

        if _params.get('features') is not None:  # noqa: E501
            _query_params.append(('features', _params['features']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['ClientLanguage', 'Accept', 'SecFetchDest', 'Pragma', 'SecChUaPlatform', 'SecFetchMode', 'CsrfToken', 'GuestToken', 'BearerAuth', 'SecChUa', 'CookieCt0', 'ActiveUser', 'UserAgent', 'AcceptLanguage', 'SecFetchSite', 'CookieAuthToken', 'AuthType', 'CacheControl', 'SecChUaMobile', 'AcceptEncoding']  # noqa: E501

        _response_types_map = {
            '200': "GetFavoriters200Response",
        }

        return self.api_client.call_api(
            '/graphql/{pathQueryId}/Favoriters', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_followers(self, path_query_id : StrictStr, variables : StrictStr, features : StrictStr, **kwargs) -> GetFollowers200Response:  # noqa: E501
        """get_followers  # noqa: E501

        get user list of followers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_followers(path_query_id, variables, features, async_req=True)
        >>> result = thread.get()

        :param path_query_id: (required)
        :type path_query_id: str
        :param variables: (required)
        :type variables: str
        :param features: (required)
        :type features: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetFollowers200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_followers_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_followers_with_http_info(path_query_id, variables, features, **kwargs)  # noqa: E501

    @validate_arguments
    def get_followers_with_http_info(self, path_query_id : StrictStr, variables : StrictStr, features : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """get_followers  # noqa: E501

        get user list of followers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_followers_with_http_info(path_query_id, variables, features, async_req=True)
        >>> result = thread.get()

        :param path_query_id: (required)
        :type path_query_id: str
        :param variables: (required)
        :type variables: str
        :param features: (required)
        :type features: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetFollowers200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'path_query_id',
            'variables',
            'features'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_followers" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['path_query_id']:
            _path_params['pathQueryId'] = _params['path_query_id']


        # process the query parameters
        _query_params = []
        if _params.get('variables') is not None:  # noqa: E501
            _query_params.append(('variables', _params['variables']))

        if _params.get('features') is not None:  # noqa: E501
            _query_params.append(('features', _params['features']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['ClientLanguage', 'Accept', 'SecFetchDest', 'Pragma', 'SecChUaPlatform', 'SecFetchMode', 'CsrfToken', 'GuestToken', 'BearerAuth', 'SecChUa', 'CookieCt0', 'ActiveUser', 'UserAgent', 'AcceptLanguage', 'SecFetchSite', 'CookieAuthToken', 'AuthType', 'CacheControl', 'SecChUaMobile', 'AcceptEncoding']  # noqa: E501

        _response_types_map = {
            '200': "GetFollowers200Response",
        }

        return self.api_client.call_api(
            '/graphql/{pathQueryId}/Followers', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_followers_you_know(self, path_query_id : StrictStr, variables : StrictStr, features : StrictStr, field_toggles : StrictStr, **kwargs) -> GetFollowers200Response:  # noqa: E501
        """get_followers_you_know  # noqa: E501

        get followers you know  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_followers_you_know(path_query_id, variables, features, field_toggles, async_req=True)
        >>> result = thread.get()

        :param path_query_id: (required)
        :type path_query_id: str
        :param variables: (required)
        :type variables: str
        :param features: (required)
        :type features: str
        :param field_toggles: (required)
        :type field_toggles: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetFollowers200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_followers_you_know_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_followers_you_know_with_http_info(path_query_id, variables, features, field_toggles, **kwargs)  # noqa: E501

    @validate_arguments
    def get_followers_you_know_with_http_info(self, path_query_id : StrictStr, variables : StrictStr, features : StrictStr, field_toggles : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """get_followers_you_know  # noqa: E501

        get followers you know  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_followers_you_know_with_http_info(path_query_id, variables, features, field_toggles, async_req=True)
        >>> result = thread.get()

        :param path_query_id: (required)
        :type path_query_id: str
        :param variables: (required)
        :type variables: str
        :param features: (required)
        :type features: str
        :param field_toggles: (required)
        :type field_toggles: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetFollowers200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'path_query_id',
            'variables',
            'features',
            'field_toggles'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_followers_you_know" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['path_query_id']:
            _path_params['pathQueryId'] = _params['path_query_id']


        # process the query parameters
        _query_params = []
        if _params.get('variables') is not None:  # noqa: E501
            _query_params.append(('variables', _params['variables']))

        if _params.get('features') is not None:  # noqa: E501
            _query_params.append(('features', _params['features']))

        if _params.get('field_toggles') is not None:  # noqa: E501
            _query_params.append(('fieldToggles', _params['field_toggles']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['ClientLanguage', 'Accept', 'SecFetchDest', 'Pragma', 'SecChUaPlatform', 'SecFetchMode', 'CsrfToken', 'GuestToken', 'BearerAuth', 'SecChUa', 'CookieCt0', 'ActiveUser', 'UserAgent', 'AcceptLanguage', 'SecFetchSite', 'CookieAuthToken', 'AuthType', 'CacheControl', 'SecChUaMobile', 'AcceptEncoding']  # noqa: E501

        _response_types_map = {
            '200': "GetFollowers200Response",
        }

        return self.api_client.call_api(
            '/graphql/{pathQueryId}/FollowersYouKnow', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_following(self, path_query_id : StrictStr, variables : StrictStr, features : StrictStr, **kwargs) -> GetFollowers200Response:  # noqa: E501
        """get_following  # noqa: E501

        get user list of following  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_following(path_query_id, variables, features, async_req=True)
        >>> result = thread.get()

        :param path_query_id: (required)
        :type path_query_id: str
        :param variables: (required)
        :type variables: str
        :param features: (required)
        :type features: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetFollowers200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_following_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_following_with_http_info(path_query_id, variables, features, **kwargs)  # noqa: E501

    @validate_arguments
    def get_following_with_http_info(self, path_query_id : StrictStr, variables : StrictStr, features : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """get_following  # noqa: E501

        get user list of following  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_following_with_http_info(path_query_id, variables, features, async_req=True)
        >>> result = thread.get()

        :param path_query_id: (required)
        :type path_query_id: str
        :param variables: (required)
        :type variables: str
        :param features: (required)
        :type features: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetFollowers200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'path_query_id',
            'variables',
            'features'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_following" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['path_query_id']:
            _path_params['pathQueryId'] = _params['path_query_id']


        # process the query parameters
        _query_params = []
        if _params.get('variables') is not None:  # noqa: E501
            _query_params.append(('variables', _params['variables']))

        if _params.get('features') is not None:  # noqa: E501
            _query_params.append(('features', _params['features']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['ClientLanguage', 'Accept', 'SecFetchDest', 'Pragma', 'SecChUaPlatform', 'SecFetchMode', 'CsrfToken', 'GuestToken', 'BearerAuth', 'SecChUa', 'CookieCt0', 'ActiveUser', 'UserAgent', 'AcceptLanguage', 'SecFetchSite', 'CookieAuthToken', 'AuthType', 'CacheControl', 'SecChUaMobile', 'AcceptEncoding']  # noqa: E501

        _response_types_map = {
            '200': "GetFollowers200Response",
        }

        return self.api_client.call_api(
            '/graphql/{pathQueryId}/Following', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_retweeters(self, path_query_id : StrictStr, variables : StrictStr, features : StrictStr, **kwargs) -> GetRetweeters200Response:  # noqa: E501
        """get_retweeters  # noqa: E501

        get tweet retweeters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_retweeters(path_query_id, variables, features, async_req=True)
        >>> result = thread.get()

        :param path_query_id: (required)
        :type path_query_id: str
        :param variables: (required)
        :type variables: str
        :param features: (required)
        :type features: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetRetweeters200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_retweeters_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_retweeters_with_http_info(path_query_id, variables, features, **kwargs)  # noqa: E501

    @validate_arguments
    def get_retweeters_with_http_info(self, path_query_id : StrictStr, variables : StrictStr, features : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """get_retweeters  # noqa: E501

        get tweet retweeters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_retweeters_with_http_info(path_query_id, variables, features, async_req=True)
        >>> result = thread.get()

        :param path_query_id: (required)
        :type path_query_id: str
        :param variables: (required)
        :type variables: str
        :param features: (required)
        :type features: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetRetweeters200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'path_query_id',
            'variables',
            'features'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_retweeters" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['path_query_id']:
            _path_params['pathQueryId'] = _params['path_query_id']


        # process the query parameters
        _query_params = []
        if _params.get('variables') is not None:  # noqa: E501
            _query_params.append(('variables', _params['variables']))

        if _params.get('features') is not None:  # noqa: E501
            _query_params.append(('features', _params['features']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['ClientLanguage', 'Accept', 'SecFetchDest', 'Pragma', 'SecChUaPlatform', 'SecFetchMode', 'CsrfToken', 'GuestToken', 'BearerAuth', 'SecChUa', 'CookieCt0', 'ActiveUser', 'UserAgent', 'AcceptLanguage', 'SecFetchSite', 'CookieAuthToken', 'AuthType', 'CacheControl', 'SecChUaMobile', 'AcceptEncoding']  # noqa: E501

        _response_types_map = {
            '200': "GetRetweeters200Response",
        }

        return self.api_client.call_api(
            '/graphql/{pathQueryId}/Retweeters', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
