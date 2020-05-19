# coding: utf-8

"""
    Signing Today API

    *Signing Today* enables seamless integration of digital signatures into any website by the use of easy requests to our API. This is the smart way of adding digital signature support with a great user experience.   *Signing Today APIs* use HTTP methods and are RESTful based, moreover they are protected by a *server to server authentication* standard by the use of tokens.   *Signing Today APIs* can be used in these environments:   | Environment | Description | Endpoint | | ----------- | ----------- | -------- | | Sandbox     | Test environment | `https://sandbox.signingtoday.com` | | Live        | Production environment | `https://api.signingtoday.com` |   For every single request to Signing Today has to be defined the following *HTTP* header: - `Authorization`, which contains the authentication token.  If the request has a body than another *HTTP* header is requested: - `Content-Type`, with `application/json` value.   Follows an example of usage to enumerate all the user of *my-org* organization.  **Example**  ```json $ curl https://sandbox.signingtoday.com/api/v1/my-org/users \\     -H 'Authorization: Token <access-token>' ```  ## HTTP methods used  APIs use the right HTTP verb in every situation.  | Method   | Description                    | | -------- | ------------------------------ | | `GET`    | Request data from a resource   | | `POST`   | Send data to create a resource | | `PUT`    | Update a resource              | | `PATCH`  | Partially update a resource    | | `DELETE` | Delete a resourse              |   ## Response definition  All the response are in JSON format. As response to a request of all users of an organization you will have a result like this:  ```json {     \"pagination\": {       \"count\": 75,       \"previous\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=1\",       \"next\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=3\",       \"pages\": 8,       \"page\": 2     },     \"meta\": {       \"code\": 200     },     \"data\": [       {         \"id\": \"jdo\",         \"status\": \"enabled\",         \"type\": \"Basic user account\",         \"email\": johndoe@dummyemail.com,         \"first_name\": \"John\",         \"last_name\": \"Doe\",         \"wallet\": [],         \"created_by\": \"system\",         \"owner\": false,         \"automatic\": false,         \"rao\": false       },       ...     ]   } ```  The JSON of the response is made of three parts: - Pagination - Meta - Data  ### Pagination  *Pagination* object allows to split the response into parts and then to rebuild it sequentially by the use of `next` and `previous` parameters, by which you get previous and following blocks. The *Pagination* is present only if the response is a list of objects.  The general structure of *Pagination* object is the following:  ```json {     \"pagination\": {       \"count\": 75,       \"previous\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=1\",       \"next\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=3\",       \"pages\": 8,       \"page\": 2     },     ...   } ```  ### Meta  *Meta* object is used to enrich the information about the response. In the previous example, a successful case of response, *Meta* will have value `status: 2XX`. In case of unsuccessful response, *Meta* will have further information, as follows:  ```json {     \"meta\": {       \"code\": <HTTP STATUS CODE>,       \"error_type\": <STATUS CODE DESCRIPTION>,       \"error_message\": <ERROR DESCRIPTION>     }   } ```  ### Data  *Data* object outputs as object or list of them. Contains the expected data as requested to the API.  ## Search filters  Search filters of the API have the following structure:  `where_ATTRIBUTENAME`=`VALUE`  In this way you make a case-sensitive search of *VALUE*. You can extend it through the Django lookup, obtaining more specific filters. For example:  `where_ATTRIBUTENAME__LOOKUP`=`VALUE`  where *LOOKUP* can be replaced with `icontains` to have a partial insensitive research, where  `where_first_name__icontains`=`CHa`  matches with every user that have the *cha* string in their name, with no differences between capital and lower cases.  [Here](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#field-lookups) the list of the lookups.  ## Webhooks  Signing Today supports webhooks for the update of DSTs and identities status. You can choose if to use or not webhooks and if you want to receive updates about DSTs and/or identities. You can configurate it on application token level, in the *webhook* field, as follows:  ```json \"webhooks\": {   \"dst\": \"URL\",   \"identity\": \"URL\"   } ```  ### DSTs status update  DSTs send the following status updates: - **DST_STATUS_CHANGED**: whenever the DST changes its status - **SIGNATURE_STATUS_CHANGED**: whenever one of the signatures changes its status  #### DST_STATUS_CHANGED  Sends the following information:  ```json {     \"message\": \"DST_STATUS_CHANGED\",     \"data\": {       \"status\": \"<DST_STATUS>\",       \"dst\": \"<DST_ID>\",       \"reason\": \"<DST_REASON>\"     }   } ```  #### SIGNATURE_STATUS_CHANGED  Sends the following information:  ```json {     \"message\": \"SIGNATURE_STATUS_CHANGED\",     \"data\": {       \"status\": \"<SIGNATURE_STATUS>\",       \"group\": <MEMBERSHIP_GROUP_INDEX>,       \"dst\": {         \"id\": \"<DST_ID>\",         \"title\": \"<DST_TITLE>\"       },       \"signature\": \"<SIGNATURE_ID>\",       \"signer\": \"<SIGNER_USERNAME>\",       \"position\": \"<SIGNATURE_POSITION>\",       \"document\": {         \"display_name\": \"<DOCUMENT_TITLE>\",         \"id\": \"<DOCUMENT_ID>\",         \"order\": <DOCUMENT_INDEX>       },       \"automatic\": <DECLARES_IF_THE_SIGNER_IS_AUTOMATIC>,       \"page\": \"<SIGNATURE_PAGE>\"     }   } ```  ### Identities status update  Identities send the following status updates: - **IDENTITY_REQUEST_ENROLLED**: whenever an identity request is activated  #### IDENTITY_REQUEST_ENROLLED  Sends the following information:  ```json {     \"message\": \"IDENTITY_REQUEST_ENROLLED\",     \"data\": {       \"status\": \"<REQUEST_STATUS>\",       \"request\": \"<REQUEST_ID>\",       \"user\": \"<APPLICANT_USERNAME>\"     }   } ```  ### Urlback  Sometimes may be necessary to make a redirect after an user, from the signature tray, has completed his operations or activated a certificate.  If set, redirects could happen in 3 cases: - after a signature or decline - after a DST has been signed by all the signers or canceled - after the activation of a certificate  In the first two cases the urlback returns the following information through a data form: - **dst-id**: id of the DST - **dst-url**: signature_ticket of the signature - **dst-status**: current status of the DST - **dst-signature-id**: id of the signature - **dst-signature-status**: current status of the signature - **user**: username of the signer - **decline-reason**: in case of a refused DST contains the reason of the decline  In the last case the urlback returns the following information through a data form: - **user**: username of the user activated the certificate - **identity-provider**: the provider has been used to issue the certificate - **identity-request-id**: id of the enrollment request - **identity-id**: id of the new identity - **identity-label**: the label assigned to the identity - **identity-certificate**: public key of the certificate  ## SUPPORTED Provider  The supported providers are:   - *_aruba_*   - *infocert*   - *namirial*   - *uanataca*    # noqa: E501

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


class Bit4idPathgroupSignatureTransactionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_dst(self, organization_id, dst_id, inline_object2, **kwargs):  # noqa: E501
        """Mark a DST as canceled  # noqa: E501

        This API allows to mark a Digital Signature Transaction as canceled providing a reason.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_dst(organization_id, dst_id, inline_object2, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id dst_id: The **dst-id** is the uuid code that identifies a digital signature transaction. It is used as a path parameter to filter the requested operation to the specified **dst**  (required)
        :param InlineObject2 inline_object2: (required)
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
        return self.cancel_dst_with_http_info(organization_id, dst_id, inline_object2, **kwargs)  # noqa: E501

    def cancel_dst_with_http_info(self, organization_id, dst_id, inline_object2, **kwargs):  # noqa: E501
        """Mark a DST as canceled  # noqa: E501

        This API allows to mark a Digital Signature Transaction as canceled providing a reason.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_dst_with_http_info(organization_id, dst_id, inline_object2, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id dst_id: The **dst-id** is the uuid code that identifies a digital signature transaction. It is used as a path parameter to filter the requested operation to the specified **dst**  (required)
        :param InlineObject2 inline_object2: (required)
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

        all_params = ['organization_id', 'dst_id', 'inline_object2']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_dst" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if self.api_client.client_side_validation and ('organization_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['organization_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `organization_id` when calling `cancel_dst`")  # noqa: E501
        # verify the required parameter 'dst_id' is set
        if self.api_client.client_side_validation and ('dst_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dst_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dst_id` when calling `cancel_dst`")  # noqa: E501
        # verify the required parameter 'inline_object2' is set
        if self.api_client.client_side_validation and ('inline_object2' not in local_var_params or  # noqa: E501
                                                        local_var_params['inline_object2'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `inline_object2` when calling `cancel_dst`")  # noqa: E501

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
        if 'inline_object2' in local_var_params:
            body_params = local_var_params['inline_object2']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/signature-transactions/{dst-id}/cancel', 'POST',
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

    def create_dst(self, organization_id, create_signature_transaction, **kwargs):  # noqa: E501
        """Create a Digital Signature Transaction  # noqa: E501

        This API allows to create a Digital Signature Transaction.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_dst(organization_id, create_signature_transaction, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param CreateSignatureTransaction create_signature_transaction: The new DST to create (required)
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
        return self.create_dst_with_http_info(organization_id, create_signature_transaction, **kwargs)  # noqa: E501

    def create_dst_with_http_info(self, organization_id, create_signature_transaction, **kwargs):  # noqa: E501
        """Create a Digital Signature Transaction  # noqa: E501

        This API allows to create a Digital Signature Transaction.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_dst_with_http_info(organization_id, create_signature_transaction, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param CreateSignatureTransaction create_signature_transaction: The new DST to create (required)
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

        all_params = ['organization_id', 'create_signature_transaction']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_dst" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if self.api_client.client_side_validation and ('organization_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['organization_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `organization_id` when calling `create_dst`")  # noqa: E501
        # verify the required parameter 'create_signature_transaction' is set
        if self.api_client.client_side_validation and ('create_signature_transaction' not in local_var_params or  # noqa: E501
                                                        local_var_params['create_signature_transaction'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `create_signature_transaction` when calling `create_dst`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_signature_transaction' in local_var_params:
            body_params = local_var_params['create_signature_transaction']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/signature-transactions', 'POST',
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

    def delete_dst(self, organization_id, dst_id, **kwargs):  # noqa: E501
        """Delete a Digital Signature Transaction  # noqa: E501

        This API allows to delete a Digital Signature Transaction.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_dst(organization_id, dst_id, async_req=True)
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
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_dst_with_http_info(organization_id, dst_id, **kwargs)  # noqa: E501

    def delete_dst_with_http_info(self, organization_id, dst_id, **kwargs):  # noqa: E501
        """Delete a Digital Signature Transaction  # noqa: E501

        This API allows to delete a Digital Signature Transaction.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_dst_with_http_info(organization_id, dst_id, async_req=True)
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
        :return: tuple(InlineResponse2009, status_code(int), headers(HTTPHeaderDict))
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
                    " to method delete_dst" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if self.api_client.client_side_validation and ('organization_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['organization_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `organization_id` when calling `delete_dst`")  # noqa: E501
        # verify the required parameter 'dst_id' is set
        if self.api_client.client_side_validation and ('dst_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dst_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dst_id` when calling `delete_dst`")  # noqa: E501

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
            '/{organization-id}/signature-transactions/{dst-id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2009',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_dst_resources(self, organization_id, dst_id, **kwargs):  # noqa: E501
        """Delete the resources of a DST  # noqa: E501

        This API allows to delete the resources of a Digital Signature Transaction.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_dst_resources(organization_id, dst_id, async_req=True)
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
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_dst_resources_with_http_info(organization_id, dst_id, **kwargs)  # noqa: E501

    def delete_dst_resources_with_http_info(self, organization_id, dst_id, **kwargs):  # noqa: E501
        """Delete the resources of a DST  # noqa: E501

        This API allows to delete the resources of a Digital Signature Transaction.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_dst_resources_with_http_info(organization_id, dst_id, async_req=True)
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
        :return: tuple(InlineResponse20010, status_code(int), headers(HTTPHeaderDict))
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
                    " to method delete_dst_resources" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if self.api_client.client_side_validation and ('organization_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['organization_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `organization_id` when calling `delete_dst_resources`")  # noqa: E501
        # verify the required parameter 'dst_id' is set
        if self.api_client.client_side_validation and ('dst_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dst_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dst_id` when calling `delete_dst_resources`")  # noqa: E501

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
            '/{organization-id}/signature-transactions/{dst-id}/resources', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20010',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document(self, organization_id, document_id, **kwargs):  # noqa: E501
        """Download a document from a DST  # noqa: E501

        This API allows to download a document from a digital signature transaction. The document can be downloaded before or after one or every signature have been performed.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document(organization_id, document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id document_id: The **document-id** is the uuid code that identifies a document of a digital signature transaction. This parameter is usually used in order to download a document from a digital signature transaction  (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_document_with_http_info(organization_id, document_id, **kwargs)  # noqa: E501

    def get_document_with_http_info(self, organization_id, document_id, **kwargs):  # noqa: E501
        """Download a document from a DST  # noqa: E501

        This API allows to download a document from a digital signature transaction. The document can be downloaded before or after one or every signature have been performed.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document_with_http_info(organization_id, document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param Id document_id: The **document-id** is the uuid code that identifies a document of a digital signature transaction. This parameter is usually used in order to download a document from a digital signature transaction  (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(file, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'document_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if self.api_client.client_side_validation and ('organization_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['organization_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `organization_id` when calling `get_document`")  # noqa: E501
        # verify the required parameter 'document_id' is set
        if self.api_client.client_side_validation and ('document_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['document_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `document_id` when calling `get_document`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501
        if 'document_id' in local_var_params:
            path_params['document-id'] = local_var_params['document_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/pdf', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/{organization-id}/documents/{document-id}/download', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dst(self, organization_id, dst_id, **kwargs):  # noqa: E501
        """Get information about a DST  # noqa: E501

        This API allows to get information about a Digital Signature Transaction.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dst(organization_id, dst_id, async_req=True)
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
        :return: InlineResponse2013
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_dst_with_http_info(organization_id, dst_id, **kwargs)  # noqa: E501

    def get_dst_with_http_info(self, organization_id, dst_id, **kwargs):  # noqa: E501
        """Get information about a DST  # noqa: E501

        This API allows to get information about a Digital Signature Transaction.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dst_with_http_info(organization_id, dst_id, async_req=True)
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
        :return: tuple(InlineResponse2013, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_dst" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if self.api_client.client_side_validation and ('organization_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['organization_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `organization_id` when calling `get_dst`")  # noqa: E501
        # verify the required parameter 'dst_id' is set
        if self.api_client.client_side_validation and ('dst_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dst_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dst_id` when calling `get_dst`")  # noqa: E501

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
            '/{organization-id}/signature-transactions/{dst-id}', 'GET',
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

    def list_ds_ts(self, organization_id, **kwargs):  # noqa: E501
        """List the DSTs of an organization  # noqa: E501

        This API allows to list the Digital Signature Transactions of an organization.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_ds_ts(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param str where_signer: Returns the Digital Signature Transactions where the specified user is a signer, searched by its id
        :param str where_status: Returns the Digital Signature Transactions with the specified status
        :param str where_title: Returns the Digital Signature Transactions that have the specified title
        :param str where_created_by: Returns the Digital Signature Transactions created by the specified user
        :param str where_created: Returns the Digital Signature Transactions created before, after or in the declared range
        :param str where_signature_status: Returns the Digital Signature Transactions where at least one of the signers has the queried status
        :param str where_document_name: Returns the Digital Signature Transactions that have into its documents the queried one
        :param str where_reason: Returns the Digital Signature Transactions with the specified reason
        :param str where_signature_name: Returns the Digital Signature Transactions where the specified user is a signer, searched by its name
        :param str where_signer_group: Returns the Digital Signature Transactions that have the specified group of signers
        :param int page: Restricts the search to the chosen page
        :param int count: Sets the number of users per page to display
        :param str where_order: The **where_order** query parameter takes one or more values separated by a comma and a space. The result will be ordered by the first value (ascending order is implied; a \"**-**\" in front of the value indicates descending order), then the second value and so on
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_ds_ts_with_http_info(organization_id, **kwargs)  # noqa: E501

    def list_ds_ts_with_http_info(self, organization_id, **kwargs):  # noqa: E501
        """List the DSTs of an organization  # noqa: E501

        This API allows to list the Digital Signature Transactions of an organization.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_ds_ts_with_http_info(organization_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str organization_id: The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (required)
        :param str where_signer: Returns the Digital Signature Transactions where the specified user is a signer, searched by its id
        :param str where_status: Returns the Digital Signature Transactions with the specified status
        :param str where_title: Returns the Digital Signature Transactions that have the specified title
        :param str where_created_by: Returns the Digital Signature Transactions created by the specified user
        :param str where_created: Returns the Digital Signature Transactions created before, after or in the declared range
        :param str where_signature_status: Returns the Digital Signature Transactions where at least one of the signers has the queried status
        :param str where_document_name: Returns the Digital Signature Transactions that have into its documents the queried one
        :param str where_reason: Returns the Digital Signature Transactions with the specified reason
        :param str where_signature_name: Returns the Digital Signature Transactions where the specified user is a signer, searched by its name
        :param str where_signer_group: Returns the Digital Signature Transactions that have the specified group of signers
        :param int page: Restricts the search to the chosen page
        :param int count: Sets the number of users per page to display
        :param str where_order: The **where_order** query parameter takes one or more values separated by a comma and a space. The result will be ordered by the first value (ascending order is implied; a \"**-**\" in front of the value indicates descending order), then the second value and so on
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2008, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organization_id', 'where_signer', 'where_status', 'where_title', 'where_created_by', 'where_created', 'where_signature_status', 'where_document_name', 'where_reason', 'where_signature_name', 'where_signer_group', 'page', 'count', 'where_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_ds_ts" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'organization_id' is set
        if self.api_client.client_side_validation and ('organization_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['organization_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `organization_id` when calling `list_ds_ts`")  # noqa: E501

        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `list_ds_ts`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'count' in local_var_params and local_var_params['count'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `count` when calling `list_ds_ts`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'organization_id' in local_var_params:
            path_params['organization-id'] = local_var_params['organization_id']  # noqa: E501

        query_params = []
        if 'where_signer' in local_var_params and local_var_params['where_signer'] is not None:  # noqa: E501
            query_params.append(('where_signer', local_var_params['where_signer']))  # noqa: E501
        if 'where_status' in local_var_params and local_var_params['where_status'] is not None:  # noqa: E501
            query_params.append(('where_status', local_var_params['where_status']))  # noqa: E501
        if 'where_title' in local_var_params and local_var_params['where_title'] is not None:  # noqa: E501
            query_params.append(('where_title', local_var_params['where_title']))  # noqa: E501
        if 'where_created_by' in local_var_params and local_var_params['where_created_by'] is not None:  # noqa: E501
            query_params.append(('where_created_by', local_var_params['where_created_by']))  # noqa: E501
        if 'where_created' in local_var_params and local_var_params['where_created'] is not None:  # noqa: E501
            query_params.append(('where_created', local_var_params['where_created']))  # noqa: E501
        if 'where_signature_status' in local_var_params and local_var_params['where_signature_status'] is not None:  # noqa: E501
            query_params.append(('where_signature_status', local_var_params['where_signature_status']))  # noqa: E501
        if 'where_document_name' in local_var_params and local_var_params['where_document_name'] is not None:  # noqa: E501
            query_params.append(('where_document_name', local_var_params['where_document_name']))  # noqa: E501
        if 'where_reason' in local_var_params and local_var_params['where_reason'] is not None:  # noqa: E501
            query_params.append(('where_reason', local_var_params['where_reason']))  # noqa: E501
        if 'where_signature_name' in local_var_params and local_var_params['where_signature_name'] is not None:  # noqa: E501
            query_params.append(('where_signature_name', local_var_params['where_signature_name']))  # noqa: E501
        if 'where_signer_group' in local_var_params and local_var_params['where_signer_group'] is not None:  # noqa: E501
            query_params.append(('where_signer_group', local_var_params['where_signer_group']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'count' in local_var_params and local_var_params['count'] is not None:  # noqa: E501
            query_params.append(('count', local_var_params['count']))  # noqa: E501
        if 'where_order' in local_var_params and local_var_params['where_order'] is not None:  # noqa: E501
            query_params.append(('where_order', local_var_params['where_order']))  # noqa: E501

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
            '/{organization-id}/signature-transactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2008',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
