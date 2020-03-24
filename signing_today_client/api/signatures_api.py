# coding: utf-8

"""
    Signing Today API

    *Signing Today* enables seamless integration of digital signatures into any website by the use of easy requests to our API. This is the smart way of adding digital signature support with a great user experience.   *Signing Today APIs* use HTTP methods and are RESTful based, moreover they are protected by a *server to server authentication* standard by the use of tokens.   *Signing Today APIs* can be used in these environments:   | Environment | Description | Endpoint | | ----------- | ----------- | -------- | | Sandbox     | Test environment | `https://sandbox.signingtoday.com` | | Live        | Production environment | `https://api.signingtoday.com` |   For every single request to Signing Today has to be defined the following *HTTP* header: - `Authorization`, which contains the authentication token.  If the request has a body than another *HTTP* header is requested: - `Content-Type`, with `application/json` value.   Follows an example of usage to enumerate all the user of *my-org* organization.  **Example**  ```json $ curl https://sandbox.signingtoday.com/api/v1/my-org/users \\     -H 'Authorization: Token <access-token>' ```  ## HTTP methods used  APIs use the right HTTP verb in every situation.  | Method   | Description                    | | -------- | ------------------------------ | | `GET`    | Request data from a resource   | | `POST`   | Send data to create a resource | | `PUT`    | Update a resource              | | `PATCH`  | Partially update a resource    | | `DELETE` | Delete a resourse              |   ## Response definition  All the response are in JSON format. As response to a request of all users of an organization you will have a result like this:  ```json {     \"pagination\": {       \"count\": 75,       \"previous\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=1\",       \"next\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=3\",       \"pages\": 8,       \"page\": 2     },     \"meta\": {       \"code\": 200     },     \"data\": [       {         \"id\": \"jdo\",         \"status\": \"enabled\",         \"type\": \"Basic user account\",         \"email\": johndoe@dummyemail.com,         \"first_name\": \"John\",         \"last_name\": \"Doe\",         \"wallet\": [],         \"created_by\": \"system\",         \"owner\": false,         \"automatic\": false,         \"rao\": false       },       ...     ]   } ```  The JSON of the response is made of three parts: - Pagination - Meta - Data  ### Pagination  *Pagination* object allows to split the response into parts and then to rebuild it sequentially by the use of `next` and `previous` parameters, by which you get previous and following blocks. The *Pagination* is present only if the response is a list of objects.  The general structure of *Pagination* object is the following:  ```json {     \"pagination\": {       \"count\": 75,       \"previous\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=1\",       \"next\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=3\",       \"pages\": 8,       \"page\": 2     },     ...   } ```  ### Meta  *Meta* object is used to enrich the information about the response. In the previous example, a successful case of response, *Meta* will have value `status: 2XX`. In case of unsuccessful response, *Meta* will have further information, as follows:  ```json {     \"meta\": {       \"code\": <HTTP STATUS CODE>,       \"error_type\": <STATUS CODE DESCRIPTION>,       \"error_message\": <ERROR DESCRIPTION>     }   } ```  ### Data  *Data* object outputs as object or list of them. Contains the expected data as requested to the API.  ## Search filters  Search filters of the API have the following structure:  `where_ATTRIBUTENAME`=`VALUE`  In this way you make a case-sensitive search of *VALUE*. You can extend it through the Django lookup, obtaining more specific filters. For example:  `where_ATTRIBUTENAME__LOOKUP`=`VALUE`  where *LOOKUP* can be replaced with `icontains` to have a partial insensitive research, where  `where_first_name__icontains`=`CHa`  matches with every user that have the *cha* string in their name, with no differences between capital and lower cases.  [Here](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#field-lookups) the list of the lookups.  ## Webhooks  Signing Today supports webhooks for the update of DSTs and identities status. You can choose if to use or not webhooks and if you want to receive updates about DSTs and/or identities. You can configurate it on application token level, in the *webhook* field, as follows:  ```json \"webhooks\": {   \"dst\": \"URL\",   \"identity\": \"URL\"   } ```  ### DSTs status update  DSTs send the following status updates: - **DST_STATUS_CHANGED**: whenever the DST changes its status - **SIGNATURE_STATUS_CHANGED**: whenever one of the signatures changes its status  #### DST_STATUS_CHANGED  Sends the following information:  ```json {     \"message\": \"DST_STATUS_CHANGED\",     \"data\": {       \"status\": \"<DST_STATUS>\",       \"dst\": \"<DST_ID>\",       \"reason\": \"<DST_REASON>\"     }   } ```  #### SIGNATURE_STATUS_CHANGED  Sends the following information:  ```json {     \"message\": \"SIGNATURE_STATUS_CHANGED\",     \"data\": {       \"status\": \"<SIGNATURE_STATUS>\",       \"group\": <MEMBERSHIP_GROUP_INDEX>,       \"dst\": {         \"id\": \"<DST_ID>\",         \"title\": \"<DST_TITLE>\"       },       \"signature\": \"<SIGNATURE_ID>\",       \"signer\": \"<SIGNER_USERNAME>\",       \"position\": \"<SIGNATURE_POSITION>\",       \"document\": {         \"display_name\": \"<DOCUMENT_TITLE>\",         \"id\": \"<DOCUMENT_ID>\",         \"order\": <DOCUMENT_INDEX>       },       \"automatic\": <DECLARES_IF_THE_SIGNER_IS_AUTOMATIC>,       \"page\": \"<SIGNATURE_PAGE>\"     }   } ```  ### Identities status update  Identities send the following status updates: - **IDENTITY_REQUEST_ENROLLED**: whenever an identity request is activated  #### IDENTITY_REQUEST_ENROLLED  Sends the following information:  ```json {     \"message\": \"IDENTITY_REQUEST_ENROLLED\",     \"data\": {       \"status\": \"<REQUEST_STATUS>\",       \"request\": \"<REQUEST_ID>\",       \"user\": \"<APPLICANT_USERNAME>\"     }   } ```  ### Urlback  Sometimes may be necessary to make a redirect after an user, from the signature tray, has completed his operations or activated a certificate.  If set, redirects could happen in 3 cases: - after a signature or decline - after a DST has been signed by all the signers or canceled - after the activation of a certificate  In the first two cases the urlback returns the following information through a data form: - **dst-id**: id of the DST - **dst-url**: signature_ticket of the signature - **dst-status**: current status of the DST - **dst-signature-id**: id of the signature - **dst-signature-status**: current status of the signature - **user**: username of the signer - **decline-reason**: in case of a refused DST contains the reason of the decline  In the last case the urlback returns the following information through a data form: - **user**: username of the user activated the certificate - **identity-provider**: the provider has been used to issue the certificate - **identity-request-id**: id of the enrollment request - **identity-id**: id of the new identity - **identity-label**: the label assigned to the identity - **identity-certificate**: public key of the certificate     # noqa: E501

    The version of the OpenAPI document: 1.5.0
    Contact: smartcloud@bit4id.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from signing_today_client.api_client import ApiClient
from signing_today_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class SignaturesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_channel(self, organization_id, dst_id, **kwargs):  # noqa: E501
        """Create a channel  # noqa: E501

        This API allows to create a channel in order to dispose, by another API, the scheduling of a signature. These two APIs are used to integrate SigningToday into another application.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_channel(organization_id, dst_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id dst_id: The **dst-id** is the uuid code that identifies a digital signature transaction. It is used as a path parameter to filter the requested operation to the specified **dst**  (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2014
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_channel_with_http_info(organization_id, dst_id, **kwargs)  # noqa: E501

    def create_channel_with_http_info(self, organization_id, dst_id, **kwargs):  # noqa: E501
        """Create a channel  # noqa: E501

        This API allows to create a channel in order to dispose, by another API, the scheduling of a signature. These two APIs are used to integrate SigningToday into another application.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_channel_with_http_info(organization_id, dst_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id dst_id: The **dst-id** is the uuid code that identifies a digital signature transaction. It is used as a path parameter to filter the requested operation to the specified **dst**  (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2014, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'dst_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_channel" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if self.api_client.client_side_validation and ('organization_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['organization_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `organization_id` when calling `create_channel`")  # noqa: E501
        # verify the required parameter 'dst_id' is set
        if self.api_client.client_side_validation and ('dst_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dst_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dst_id` when calling `create_channel`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501
        if 'dst_id' in local_var_params:
            path_params['dst-id'] = local_var_params['dst_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/channels/{dst-id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2014',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def decline_dst(self, organization_id, signature_id, inline_object5, **kwargs):  # noqa: E501
        """Decline a Digital Signature Transaction  # noqa: E501

        This API allows to decline the Signature of a digital signature transaction providing a reason.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.decline_dst(organization_id, signature_id, inline_object5, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id signature_id: The **signature-id** is the uuid code that identifies a signature that has to be performed into a digital signature transaction. It is usually used in the API endpoints to perform, decline or cancel a digital signature transaction  (required)
        :param InlineObject5 inline_object5: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2013
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.decline_dst_with_http_info(organization_id, signature_id, inline_object5, **kwargs)  # noqa: E501

    def decline_dst_with_http_info(self, organization_id, signature_id, inline_object5, **kwargs):  # noqa: E501
        """Decline a Digital Signature Transaction  # noqa: E501

        This API allows to decline the Signature of a digital signature transaction providing a reason.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.decline_dst_with_http_info(organization_id, signature_id, inline_object5, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id signature_id: The **signature-id** is the uuid code that identifies a signature that has to be performed into a digital signature transaction. It is usually used in the API endpoints to perform, decline or cancel a digital signature transaction  (required)
        :param InlineObject5 inline_object5: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2013, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'signature_id', 'inline_object5']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method decline_dst" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if self.api_client.client_side_validation and ('organization_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['organization_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `organization_id` when calling `decline_dst`")  # noqa: E501
        # verify the required parameter 'signature_id' is set
        if self.api_client.client_side_validation and ('signature_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['signature_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `signature_id` when calling `decline_dst`")  # noqa: E501
        # verify the required parameter 'inline_object5' is set
        if self.api_client.client_side_validation and ('inline_object5' not in local_var_params or  # noqa: E501
                                                        local_var_params['inline_object5'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `inline_object5` when calling `decline_dst`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501
        if 'signature_id' in local_var_params:
            path_params['signature-id'] = local_var_params['signature_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'inline_object5' in local_var_params:
            body_params = local_var_params['inline_object5']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/signatures/{signature-id}/decline', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def perform_dst(self, organization_id, signature_id, automatic_signature, **kwargs):  # noqa: E501
        """Sign a DST with an automatic signer  # noqa: E501

        This API allows to sign a Digital Signature Transaction with an automatic signer certificate.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.perform_dst(organization_id, signature_id, automatic_signature, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id signature_id: The **signature-id** is the uuid code that identifies a signature that has to be performed into a digital signature transaction. It is usually used in the API endpoints to perform, decline or cancel a digital signature transaction  (required)
        :param AutomaticSignature automatic_signature: Automatic Signature description (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse20011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.perform_dst_with_http_info(organization_id, signature_id, automatic_signature, **kwargs)  # noqa: E501

    def perform_dst_with_http_info(self, organization_id, signature_id, automatic_signature, **kwargs):  # noqa: E501
        """Sign a DST with an automatic signer  # noqa: E501

        This API allows to sign a Digital Signature Transaction with an automatic signer certificate.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.perform_dst_with_http_info(organization_id, signature_id, automatic_signature, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id signature_id: The **signature-id** is the uuid code that identifies a signature that has to be performed into a digital signature transaction. It is usually used in the API endpoints to perform, decline or cancel a digital signature transaction  (required)
        :param AutomaticSignature automatic_signature: Automatic Signature description (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse20011, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'signature_id', 'automatic_signature']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method perform_dst" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if self.api_client.client_side_validation and ('organization_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['organization_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `organization_id` when calling `perform_dst`")  # noqa: E501
        # verify the required parameter 'signature_id' is set
        if self.api_client.client_side_validation and ('signature_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['signature_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `signature_id` when calling `perform_dst`")  # noqa: E501
        # verify the required parameter 'automatic_signature' is set
        if self.api_client.client_side_validation and ('automatic_signature' not in local_var_params or  # noqa: E501
                                                        local_var_params['automatic_signature'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `automatic_signature` when calling `perform_dst`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501
        if 'signature_id' in local_var_params:
            path_params['signature-id'] = local_var_params['signature_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'automatic_signature' in local_var_params:
            body_params = local_var_params['automatic_signature']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/signatures/{signature-id}/perform', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def perform_signature(self, organization_id, signature_id, identity_id, inline_object3, **kwargs):  # noqa: E501
        """Perform a Signature  # noqa: E501

        This API allows to integrate SigningToday into another application. Through this endpoint it is possible to schedule a signature into engine.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.perform_signature(organization_id, signature_id, identity_id, inline_object3, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id signature_id: The **signature-id** is the uuid code that identifies a signature that has to be performed into a digital signature transaction. It is usually used in the API endpoints to perform, decline or cancel a digital signature transaction  (required)
        :param Id identity_id: The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity  (required)
        :param InlineObject3 inline_object3: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.perform_signature_with_http_info(organization_id, signature_id, identity_id, inline_object3, **kwargs)  # noqa: E501

    def perform_signature_with_http_info(self, organization_id, signature_id, identity_id, inline_object3, **kwargs):  # noqa: E501
        """Perform a Signature  # noqa: E501

        This API allows to integrate SigningToday into another application. Through this endpoint it is possible to schedule a signature into engine.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.perform_signature_with_http_info(organization_id, signature_id, identity_id, inline_object3, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id signature_id: The **signature-id** is the uuid code that identifies a signature that has to be performed into a digital signature transaction. It is usually used in the API endpoints to perform, decline or cancel a digital signature transaction  (required)
        :param Id identity_id: The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity  (required)
        :param InlineObject3 inline_object3: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse20012, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'signature_id', 'identity_id', 'inline_object3']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method perform_signature" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if self.api_client.client_side_validation and ('organization_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['organization_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `organization_id` when calling `perform_signature`")  # noqa: E501
        # verify the required parameter 'signature_id' is set
        if self.api_client.client_side_validation and ('signature_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['signature_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `signature_id` when calling `perform_signature`")  # noqa: E501
        # verify the required parameter 'identity_id' is set
        if self.api_client.client_side_validation and ('identity_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['identity_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `identity_id` when calling `perform_signature`")  # noqa: E501
        # verify the required parameter 'inline_object3' is set
        if self.api_client.client_side_validation and ('inline_object3' not in local_var_params or  # noqa: E501
                                                        local_var_params['inline_object3'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `inline_object3` when calling `perform_signature`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501
        if 'signature_id' in local_var_params:
            path_params['signature-id'] = local_var_params['signature_id']  # noqa: E501
        if 'identity_id' in local_var_params:
            path_params['identity-id'] = local_var_params['identity_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'inline_object3' in local_var_params:
            body_params = local_var_params['inline_object3']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/signatures/{signature-id}/perform/{identity-id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def perform_signature_with_session(self, organization_id, signature_id, inline_object4, **kwargs):  # noqa: E501
        """Perform a Signature with session  # noqa: E501

        This API allows to perform one or more signatures within the same session. This way is possible, in the scenario of a simple signature for example, to perform multiple signatures using the same _one time password_.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.perform_signature_with_session(organization_id, signature_id, inline_object4, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id signature_id: The **signature-id** is the uuid code that identifies a signature that has to be performed into a digital signature transaction. It is usually used in the API endpoints to perform, decline or cancel a digital signature transaction  (required)
        :param InlineObject4 inline_object4: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.perform_signature_with_session_with_http_info(organization_id, signature_id, inline_object4, **kwargs)  # noqa: E501

    def perform_signature_with_session_with_http_info(self, organization_id, signature_id, inline_object4, **kwargs):  # noqa: E501
        """Perform a Signature with session  # noqa: E501

        This API allows to perform one or more signatures within the same session. This way is possible, in the scenario of a simple signature for example, to perform multiple signatures using the same _one time password_.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.perform_signature_with_session_with_http_info(organization_id, signature_id, inline_object4, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id signature_id: The **signature-id** is the uuid code that identifies a signature that has to be performed into a digital signature transaction. It is usually used in the API endpoints to perform, decline or cancel a digital signature transaction  (required)
        :param InlineObject4 inline_object4: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse20013, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'signature_id', 'inline_object4']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method perform_signature_with_session" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if self.api_client.client_side_validation and ('organization_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['organization_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `organization_id` when calling `perform_signature_with_session`")  # noqa: E501
        # verify the required parameter 'signature_id' is set
        if self.api_client.client_side_validation and ('signature_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['signature_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `signature_id` when calling `perform_signature_with_session`")  # noqa: E501
        # verify the required parameter 'inline_object4' is set
        if self.api_client.client_side_validation and ('inline_object4' not in local_var_params or  # noqa: E501
                                                        local_var_params['inline_object4'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `inline_object4` when calling `perform_signature_with_session`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501
        if 'signature_id' in local_var_params:
            path_params['signature-id'] = local_var_params['signature_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'inline_object4' in local_var_params:
            body_params = local_var_params['inline_object4']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/signatures/{signature-id}/session-perform', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
