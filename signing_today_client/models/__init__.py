# coding: utf-8

# flake8: noqa
"""
    Signing Today API

    *Signing Today* enables seamless integration of digital signatures into any website by the use of easy requests to our API. This is the smart way of adding digital signature support with a great user experience.   *Signing Today APIs* use HTTP methods and are RESTful based, moreover they are protected by a *server to server authentication* standard by the use of tokens.   *Signing Today APIs* can be used in these environments:   | Environment | Description | Endpoint | | ----------- | ----------- | -------- | | Sandbox     | Test environment | `https://sandbox.signingtoday.com` | | Live        | Production environment | `https://api.signingtoday.com` |   For every single request to Signing Today has to be defined the following *HTTP* header: - `Authorization`, which contains the authentication token.  If the request has a body than another *HTTP* header is requested: - `Content-Type`, with `application/json` value.   Follows an example of usage to enumerate all the user of *my-org* organization.  **Example**  ```json $ curl https://sandbox.signingtoday.com/api/v1/my-org/users \\     -H 'Authorization: Token <access-token>' ```  ## HTTP methods used  APIs use the right HTTP verb in every situation.  | Method   | Description                    | | -------- | ------------------------------ | | `GET`    | Request data from a resource   | | `POST`   | Send data to create a resource | | `PUT`    | Update a resource              | | `PATCH`  | Partially update a resource    | | `DELETE` | Delete a resourse              |   ## Response definition  All the response are in JSON format. As response to a request of all users of an organization you will have a result like this:  ```json {     \"pagination\": {       \"count\": 75,       \"previous\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=1\",       \"next\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=3\",       \"pages\": 8,       \"page\": 2     },     \"meta\": {       \"code\": 200     },     \"data\": [       {         \"id\": \"jdo\",         \"status\": \"enabled\",         \"type\": \"Basic user account\",         \"email\": johndoe@dummyemail.com,         \"first_name\": \"John\",         \"last_name\": \"Doe\",         \"wallet\": [],         \"created_by\": \"system\",         \"owner\": false,         \"automatic\": false,         \"rao\": false       },       ...     ]   } ```  The JSON of the response is made of three parts: - Pagination - Meta - Data  ### Pagination  *Pagination* object allows to split the response into parts and then to rebuild it sequentially by the use of `next` and `previous` parameters, by which you get previous and following blocks. The *Pagination* is present only if the response is a list of objects.  The general structure of *Pagination* object is the following:  ```json {     \"pagination\": {       \"count\": 75,       \"previous\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=1\",       \"next\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=3\",       \"pages\": 8,       \"page\": 2     },     ...   } ```  ### Meta  *Meta* object is used to enrich the information about the response. In the previous example, a successful case of response, *Meta* will have value `status: 2XX`. In case of unsuccessful response, *Meta* will have further information, as follows:  ```json {     \"meta\": {       \"code\": <HTTP STATUS CODE>,       \"error_type\": <STATUS CODE DESCRIPTION>,       \"error_message\": <ERROR DESCRIPTION>     }   } ```  ### Data  *Data* object outputs as object or list of them. Contains the expected data as requested to the API.  ## Search filters  Search filters of the API have the following structure:  `where_ATTRIBUTENAME`=`VALUE`  In this way you make a case-sensitive search of *VALUE*. You can extend it through the Django lookup, obtaining more specific filters. For example:  `where_ATTRIBUTENAME__LOOKUP`=`VALUE`  where *LOOKUP* can be replaced with `icontains` to have a partial insensitive research, where  `where_first_name__icontains`=`CHa`  matches with every user that have the *cha* string in their name, with no differences between capital and lower cases.  [Here](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#field-lookups) the list of the lookups.  ## Webhooks  Signing Today supports webhooks for the update of DSTs and identities status. You can choose if to use or not webhooks and if you want to receive updates about DSTs and/or identities. You can configurate it on application token level, in the *webhook* field, as follows:  ```json \"webhooks\": {   \"dst\": \"URL\",   \"identity\": \"URL\"   } ```  ### DSTs status update  DSTs send the following status updates: - **DST_STATUS_CHANGED**: whenever the DST changes its status - **SIGNATURE_STATUS_CHANGED**: whenever one of the signatures changes its status  #### DST_STATUS_CHANGED  Sends the following information:  ```json {     \"message\": \"DST_STATUS_CHANGED\",     \"data\": {       \"status\": \"<DST_STATUS>\",       \"dst\": \"<DST_ID>\",       \"reason\": \"<DST_REASON>\"     }   } ```  #### SIGNATURE_STATUS_CHANGED  Sends the following information:  ```json {     \"message\": \"SIGNATURE_STATUS_CHANGED\",     \"data\": {       \"status\": \"<SIGNATURE_STATUS>\",       \"group\": <MEMBERSHIP_GROUP_INDEX>,       \"dst\": {         \"id\": \"<DST_ID>\",         \"title\": \"<DST_TITLE>\"       },       \"signature\": \"<SIGNATURE_ID>\",       \"signer\": \"<SIGNER_USERNAME>\",       \"position\": \"<SIGNATURE_POSITION>\",       \"document\": {         \"display_name\": \"<DOCUMENT_TITLE>\",         \"id\": \"<DOCUMENT_ID>\",         \"order\": <DOCUMENT_INDEX>       },       \"automatic\": <DECLARES_IF_THE_SIGNER_IS_AUTOMATIC>,       \"page\": \"<SIGNATURE_PAGE>\"     }   } ```  ### Identities status update  Identities send the following status updates: - **IDENTITY_REQUEST_ENROLLED**: whenever an identity request is activated  #### IDENTITY_REQUEST_ENROLLED  Sends the following information:  ```json {     \"message\": \"IDENTITY_REQUEST_ENROLLED\",     \"data\": {       \"status\": \"<REQUEST_STATUS>\",       \"request\": \"<REQUEST_ID>\",       \"user\": \"<APPLICANT_USERNAME>\"     }   } ```  ### Urlback  Sometimes may be necessary to make a redirect after an user, from the signature tray, has completed his operations or activated a certificate.  If set, redirects could happen in 3 cases: - after a signature or decline - after a DST has been signed by all the signers or canceled - after the activation of a certificate  In the first two cases the urlback returns the following information through a data form: - **dst-id**: id of the DST - **dst-url**: signature_ticket of the signature - **dst-status**: current status of the DST - **dst-signature-id**: id of the signature - **dst-signature-status**: current status of the signature - **user**: username of the signer - **decline-reason**: in case of a refused DST contains the reason of the decline  In the last case the urlback returns the following information through a data form: - **user**: username of the user activated the certificate - **identity-provider**: the provider has been used to issue the certificate - **identity-request-id**: id of the enrollment request - **identity-id**: id of the new identity - **identity-label**: the label assigned to the identity - **identity-certificate**: public key of the certificate  ## SUPPORTED Provider  The supported providers are:   - *_aruba_*   - *infocert*   - *namirial*   - *uanataca*    # noqa: E501

    The version of the OpenAPI document: 1.5.0
    Contact: smartcloud@bit4id.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from signing_today_client.models.automatic_signature import AutomaticSignature
from signing_today_client.models.create_identityby_token import CreateIdentitybyToken
from signing_today_client.models.create_signature_transaction import CreateSignatureTransaction
from signing_today_client.models.create_token import CreateToken
from signing_today_client.models.create_user import CreateUser
from signing_today_client.models.document import Document
from signing_today_client.models.document1 import Document1
from signing_today_client.models.identity import Identity
from signing_today_client.models.identity_actions import IdentityActions
from signing_today_client.models.identity_association import IdentityAssociation
from signing_today_client.models.identity_enroll import IdentityEnroll
from signing_today_client.models.identity_enroll_actions import IdentityEnrollActions
from signing_today_client.models.identity_request import IdentityRequest
from signing_today_client.models.inline_object import InlineObject
from signing_today_client.models.inline_object1 import InlineObject1
from signing_today_client.models.inline_object2 import InlineObject2
from signing_today_client.models.inline_object3 import InlineObject3
from signing_today_client.models.inline_object4 import InlineObject4
from signing_today_client.models.inline_object5 import InlineObject5
from signing_today_client.models.inline_response200 import InlineResponse200
from signing_today_client.models.inline_response2001 import InlineResponse2001
from signing_today_client.models.inline_response20010 import InlineResponse20010
from signing_today_client.models.inline_response20011 import InlineResponse20011
from signing_today_client.models.inline_response20012 import InlineResponse20012
from signing_today_client.models.inline_response20013 import InlineResponse20013
from signing_today_client.models.inline_response20013_data import InlineResponse20013Data
from signing_today_client.models.inline_response2002 import InlineResponse2002
from signing_today_client.models.inline_response2003 import InlineResponse2003
from signing_today_client.models.inline_response2004 import InlineResponse2004
from signing_today_client.models.inline_response2005 import InlineResponse2005
from signing_today_client.models.inline_response2006 import InlineResponse2006
from signing_today_client.models.inline_response2007 import InlineResponse2007
from signing_today_client.models.inline_response2008 import InlineResponse2008
from signing_today_client.models.inline_response2009 import InlineResponse2009
from signing_today_client.models.inline_response2009_meta import InlineResponse2009Meta
from signing_today_client.models.inline_response201 import InlineResponse201
from signing_today_client.models.inline_response2011 import InlineResponse2011
from signing_today_client.models.inline_response2012 import InlineResponse2012
from signing_today_client.models.inline_response2013 import InlineResponse2013
from signing_today_client.models.inline_response2014 import InlineResponse2014
from signing_today_client.models.inline_response2014_data import InlineResponse2014Data
from signing_today_client.models.inline_response2015 import InlineResponse2015
from signing_today_client.models.inline_response401 import InlineResponse401
from signing_today_client.models.inline_response403 import InlineResponse403
from signing_today_client.models.inline_response404 import InlineResponse404
from signing_today_client.models.meta_data_error import MetaDataError
from signing_today_client.models.meta_data_success import MetaDataSuccess
from signing_today_client.models.organization import Organization
from signing_today_client.models.organization_settings import OrganizationSettings
from signing_today_client.models.pagination_data import PaginationData
from signing_today_client.models.sms import SMS
from signing_today_client.models.signature import Signature
from signing_today_client.models.signature_dst import SignatureDST
from signing_today_client.models.signature_dst_where import SignatureDSTWhere
from signing_today_client.models.signature_implementation_response import SignatureImplementationResponse
from signing_today_client.models.signature_implementation_response_channel import SignatureImplementationResponseChannel
from signing_today_client.models.signature_transaction import SignatureTransaction
from signing_today_client.models.signature_where import SignatureWhere
from signing_today_client.models.signature_where_font import SignatureWhereFont
from signing_today_client.models.signature_where_text import SignatureWhereText
from signing_today_client.models.token import Token
from signing_today_client.models.token_http_options import TokenHttpOptions
from signing_today_client.models.token_webhooks import TokenWebhooks
from signing_today_client.models.update_organization import UpdateOrganization
from signing_today_client.models.update_token import UpdateToken
from signing_today_client.models.update_user import UpdateUser
from signing_today_client.models.user import User
