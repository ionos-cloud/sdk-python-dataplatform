from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud_dataplatform.api_client import ApiClient
from ionoscloud_dataplatform.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DataPlatformClusterApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def clusters_delete(self, cluster_id, **kwargs):  # noqa: E501
        """Delete a DataPlatformCluster  # noqa: E501

        Deletes the specified DataPlatformCluster by its distinct cluster ID.  The ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_delete(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. Must conform to the UUID format.  (required)
        :type cluster_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ClusterResponseData
        """
        kwargs['_return_http_data_only'] = True
        return self.clusters_delete_with_http_info(cluster_id, **kwargs)  # noqa: E501

    def clusters_delete_with_http_info(self, cluster_id, **kwargs):  # noqa: E501
        """Delete a DataPlatformCluster  # noqa: E501

        Deletes the specified DataPlatformCluster by its distinct cluster ID.  The ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_delete_with_http_info(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. Must conform to the UUID format.  (required)
        :type cluster_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ClusterResponseData, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'cluster_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clusters_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `clusters_delete`")  # noqa: E501

        if self.api_client.client_side_validation and ('cluster_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['cluster_id']) > 36):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `cluster_id` when calling `clusters_delete`, length must be less than or equal to `36`")  # noqa: E501
        if self.api_client.client_side_validation and ('cluster_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['cluster_id']) < 32):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `cluster_id` when calling `clusters_delete`, length must be greater than or equal to `32`")  # noqa: E501
        if self.api_client.client_side_validation and 'cluster_id' in local_var_params and not re.search(r'^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$', local_var_params['cluster_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `cluster_id` when calling `clusters_delete`, must conform to the pattern `/^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'ClusterResponseData'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/{clusterId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def clusters_find_by_id(self, cluster_id, **kwargs):  # noqa: E501
        """Retrieve a DataPlatformCluster  # noqa: E501

        Retrieve the specified DataPlatformCluster by its distinct ID.  The cluster ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_find_by_id(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. Must conform to the UUID format.  (required)
        :type cluster_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ClusterResponseData
        """
        kwargs['_return_http_data_only'] = True
        return self.clusters_find_by_id_with_http_info(cluster_id, **kwargs)  # noqa: E501

    def clusters_find_by_id_with_http_info(self, cluster_id, **kwargs):  # noqa: E501
        """Retrieve a DataPlatformCluster  # noqa: E501

        Retrieve the specified DataPlatformCluster by its distinct ID.  The cluster ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_find_by_id_with_http_info(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. Must conform to the UUID format.  (required)
        :type cluster_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ClusterResponseData, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'cluster_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clusters_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `clusters_find_by_id`")  # noqa: E501

        if self.api_client.client_side_validation and ('cluster_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['cluster_id']) > 36):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `cluster_id` when calling `clusters_find_by_id`, length must be less than or equal to `36`")  # noqa: E501
        if self.api_client.client_side_validation and ('cluster_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['cluster_id']) < 32):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `cluster_id` when calling `clusters_find_by_id`, length must be greater than or equal to `32`")  # noqa: E501
        if self.api_client.client_side_validation and 'cluster_id' in local_var_params and not re.search(r'^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$', local_var_params['cluster_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `cluster_id` when calling `clusters_find_by_id`, must conform to the pattern `/^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'ClusterResponseData'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/{clusterId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def clusters_get(self, **kwargs):  # noqa: E501
        """List the DataPlatformClusters  # noqa: E501

        List all available DataPlatformClusters that can be accessed by the user.  The user might filter the request for the name of the DataPlatformCluster. If no cluster is available matching the request, the list will be empty.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_get(async_req=True)
        >>> result = thread.get()

        :param name: Response filter to list only the clusters which include the specified name. The value is case insensitive and matched on the `name` property of the cluster. The input is limited to 63 characters with alphanumeric characters ([a-z0-9A-Z]), dashes (-), underscores (_), and dots (.) allowed. 
        :type name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ClusterListResponseData
        """
        kwargs['_return_http_data_only'] = True
        return self.clusters_get_with_http_info(**kwargs)  # noqa: E501

    def clusters_get_with_http_info(self, **kwargs):  # noqa: E501
        """List the DataPlatformClusters  # noqa: E501

        List all available DataPlatformClusters that can be accessed by the user.  The user might filter the request for the name of the DataPlatformCluster. If no cluster is available matching the request, the list will be empty.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param name: Response filter to list only the clusters which include the specified name. The value is case insensitive and matched on the `name` property of the cluster. The input is limited to 63 characters with alphanumeric characters ([a-z0-9A-Z]), dashes (-), underscores (_), and dots (.) allowed. 
        :type name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ClusterListResponseData, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'name'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clusters_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and ('name' in local_var_params and  # noqa: E501
                                                        len(local_var_params['name']) > 63):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `name` when calling `clusters_get`, length must be less than or equal to `63`")  # noqa: E501
        if self.api_client.client_side_validation and 'name' in local_var_params and not re.search(r'^[-A-Za-z0-9_.]*$', local_var_params['name']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `name` when calling `clusters_get`, must conform to the pattern `/^[-A-Za-z0-9_.]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'ClusterListResponseData'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def clusters_kubeconfig_find_by_cluster_id(self, cluster_id, **kwargs):  # noqa: E501
        """Read the Kubeconfig  # noqa: E501

        Retrieves the Kubernetes configuration file (kubeconfig) for the specified DataPlatformCluster by its cluster ID.  The ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_kubeconfig_find_by_cluster_id(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. Must conform to the UUID format.  (required)
        :type cluster_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.clusters_kubeconfig_find_by_cluster_id_with_http_info(cluster_id, **kwargs)  # noqa: E501

    def clusters_kubeconfig_find_by_cluster_id_with_http_info(self, cluster_id, **kwargs):  # noqa: E501
        """Read the Kubeconfig  # noqa: E501

        Retrieves the Kubernetes configuration file (kubeconfig) for the specified DataPlatformCluster by its cluster ID.  The ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_kubeconfig_find_by_cluster_id_with_http_info(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. Must conform to the UUID format.  (required)
        :type cluster_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'cluster_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clusters_kubeconfig_find_by_cluster_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `clusters_kubeconfig_find_by_cluster_id`")  # noqa: E501

        if self.api_client.client_side_validation and ('cluster_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['cluster_id']) > 36):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `cluster_id` when calling `clusters_kubeconfig_find_by_cluster_id`, length must be less than or equal to `36`")  # noqa: E501
        if self.api_client.client_side_validation and ('cluster_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['cluster_id']) < 32):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `cluster_id` when calling `clusters_kubeconfig_find_by_cluster_id`, length must be greater than or equal to `32`")  # noqa: E501
        if self.api_client.client_side_validation and 'cluster_id' in local_var_params and not re.search(r'^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$', local_var_params['cluster_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `cluster_id` when calling `clusters_kubeconfig_find_by_cluster_id`, must conform to the pattern `/^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'object'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/{clusterId}/kubeconfig', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def clusters_patch(self, cluster_id, patch_cluster_request, **kwargs):  # noqa: E501
        """Partially Modify a DataPlatformCluster  # noqa: E501

        Modifies the specified DataPlatformCluster by its distinct cluster ID. The fields in the request body are applied to the cluster. Note that the application to the cluster itself is performed asynchronously. You can check the sync state by querying the cluster with the GET method.  The ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_patch(cluster_id, patch_cluster_request, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. Must conform to the UUID format.  (required)
        :type cluster_id: str
        :param patch_cluster_request: Request payload with the properties that shall be applied to an existing DataPlatformCluster.  (required)
        :type patch_cluster_request: PatchClusterRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ClusterResponseData
        """
        kwargs['_return_http_data_only'] = True
        return self.clusters_patch_with_http_info(cluster_id, patch_cluster_request, **kwargs)  # noqa: E501

    def clusters_patch_with_http_info(self, cluster_id, patch_cluster_request, **kwargs):  # noqa: E501
        """Partially Modify a DataPlatformCluster  # noqa: E501

        Modifies the specified DataPlatformCluster by its distinct cluster ID. The fields in the request body are applied to the cluster. Note that the application to the cluster itself is performed asynchronously. You can check the sync state by querying the cluster with the GET method.  The ID can be found in the response when a cluster is created or when you GET a list of all DataPlatformClusters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_patch_with_http_info(cluster_id, patch_cluster_request, async_req=True)
        >>> result = thread.get()

        :param cluster_id: The unique ID of the cluster. Must conform to the UUID format.  (required)
        :type cluster_id: str
        :param patch_cluster_request: Request payload with the properties that shall be applied to an existing DataPlatformCluster.  (required)
        :type patch_cluster_request: PatchClusterRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ClusterResponseData, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'cluster_id',
            'patch_cluster_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clusters_patch" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if self.api_client.client_side_validation and ('cluster_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['cluster_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cluster_id` when calling `clusters_patch`")  # noqa: E501
        # verify the required parameter 'patch_cluster_request' is set
        if self.api_client.client_side_validation and ('patch_cluster_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['patch_cluster_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `patch_cluster_request` when calling `clusters_patch`")  # noqa: E501

        if self.api_client.client_side_validation and ('cluster_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['cluster_id']) > 36):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `cluster_id` when calling `clusters_patch`, length must be less than or equal to `36`")  # noqa: E501
        if self.api_client.client_side_validation and ('cluster_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['cluster_id']) < 32):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `cluster_id` when calling `clusters_patch`, length must be greater than or equal to `32`")  # noqa: E501
        if self.api_client.client_side_validation and 'cluster_id' in local_var_params and not re.search(r'^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$', local_var_params['cluster_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `cluster_id` when calling `clusters_patch`, must conform to the pattern `/^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['clusterId'] = local_var_params['cluster_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'patch_cluster_request' in local_var_params:
            body_params = local_var_params['patch_cluster_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'ClusterResponseData'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters/{clusterId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def clusters_post(self, create_cluster_request, **kwargs):  # noqa: E501
        """Create a DataPlatformCluster  # noqa: E501

        Creates a new DataPlatformCluster.  The cluster will be provisioned in the data center matching the provided `datacenterID`. Therefore the data center must be created upfront and must be accessible by the user issuing the request.  To create a new virtual data center (VDC) [see](https://api.ionos.com/docs/cloud/v6/#Data-centers-post-datacenters).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_post(create_cluster_request, async_req=True)
        >>> result = thread.get()

        :param create_cluster_request: Request payload with the properties that defines a new DataPlatformCluster and the credentials to interact with the PaaS API to create it.  (required)
        :type create_cluster_request: CreateClusterRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ClusterResponseData
        """
        kwargs['_return_http_data_only'] = True
        return self.clusters_post_with_http_info(create_cluster_request, **kwargs)  # noqa: E501

    def clusters_post_with_http_info(self, create_cluster_request, **kwargs):  # noqa: E501
        """Create a DataPlatformCluster  # noqa: E501

        Creates a new DataPlatformCluster.  The cluster will be provisioned in the data center matching the provided `datacenterID`. Therefore the data center must be created upfront and must be accessible by the user issuing the request.  To create a new virtual data center (VDC) [see](https://api.ionos.com/docs/cloud/v6/#Data-centers-post-datacenters).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clusters_post_with_http_info(create_cluster_request, async_req=True)
        >>> result = thread.get()

        :param create_cluster_request: Request payload with the properties that defines a new DataPlatformCluster and the credentials to interact with the PaaS API to create it.  (required)
        :type create_cluster_request: CreateClusterRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ClusterResponseData, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'create_cluster_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clusters_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'create_cluster_request' is set
        if self.api_client.client_side_validation and ('create_cluster_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['create_cluster_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `create_cluster_request` when calling `clusters_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_cluster_request' in local_var_params:
            body_params = local_var_params['create_cluster_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        response_type = 'ClusterResponseData'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/clusters', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
