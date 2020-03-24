# coding: utf-8

"""
    Signing Today API

    *Signing Today* enables seamless integration of digital signatures into any website by the use of easy requests to our API. This is the smart way of adding digital signature support with a great user experience.   *Signing Today APIs* use HTTP methods and are RESTful based, moreover they are protected by a *server to server authentication* standard by the use of tokens.   *Signing Today APIs* can be used in these environments:   | Environment | Description | Endpoint | | ----------- | ----------- | -------- | | Sandbox     | Test environment | `https://sandbox.signingtoday.com` | | Live        | Production environment | `https://api.signingtoday.com` |   For every single request to Signing Today has to be defined the following *HTTP* header: - `Authorization`, which contains the authentication token.  If the request has a body than another *HTTP* header is requested: - `Content-Type`, with `application/json` value.   Follows an example of usage to enumerate all the user of *my-org* organization.  **Example**  ```json $ curl https://sandbox.signingtoday.com/api/v1/my-org/users \\     -H 'Authorization: Token <access-token>' ```  ## HTTP methods used  APIs use the right HTTP verb in every situation.  | Method   | Description                    | | -------- | ------------------------------ | | `GET`    | Request data from a resource   | | `POST`   | Send data to create a resource | | `PUT`    | Update a resource              | | `PATCH`  | Partially update a resource    | | `DELETE` | Delete a resourse              |   ## Response definition  All the response are in JSON format. As response to a request of all users of an organization you will have a result like this:  ```json {     \"pagination\": {       \"count\": 75,       \"previous\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=1\",       \"next\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=3\",       \"pages\": 8,       \"page\": 2     },     \"meta\": {       \"code\": 200     },     \"data\": [       {         \"id\": \"jdo\",         \"status\": \"enabled\",         \"type\": \"Basic user account\",         \"email\": johndoe@dummyemail.com,         \"first_name\": \"John\",         \"last_name\": \"Doe\",         \"wallet\": [],         \"created_by\": \"system\",         \"owner\": false,         \"automatic\": false,         \"rao\": false       },       ...     ]   } ```  The JSON of the response is made of three parts: - Pagination - Meta - Data  ### Pagination  *Pagination* object allows to split the response into parts and then to rebuild it sequentially by the use of `next` and `previous` parameters, by which you get previous and following blocks. The *Pagination* is present only if the response is a list of objects.  The general structure of *Pagination* object is the following:  ```json {     \"pagination\": {       \"count\": 75,       \"previous\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=1\",       \"next\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=3\",       \"pages\": 8,       \"page\": 2     },     ...   } ```  ### Meta  *Meta* object is used to enrich the information about the response. In the previous example, a successful case of response, *Meta* will have value `status: 2XX`. In case of unsuccessful response, *Meta* will have further information, as follows:  ```json {     \"meta\": {       \"code\": <HTTP STATUS CODE>,       \"error_type\": <STATUS CODE DESCRIPTION>,       \"error_message\": <ERROR DESCRIPTION>     }   } ```  ### Data  *Data* object outputs as object or list of them. Contains the expected data as requested to the API.  ## Search filters  Search filters of the API have the following structure:  `where_ATTRIBUTENAME`=`VALUE`  In this way you make a case-sensitive search of *VALUE*. You can extend it through the Django lookup, obtaining more specific filters. For example:  `where_ATTRIBUTENAME__LOOKUP`=`VALUE`  where *LOOKUP* can be replaced with `icontains` to have a partial insensitive research, where  `where_first_name__icontains`=`CHa`  matches with every user that have the *cha* string in their name, with no differences between capital and lower cases.  [Here](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#field-lookups) the list of the lookups.  ## Webhooks  Signing Today supports webhooks for the update of DSTs and identities status. You can choose if to use or not webhooks and if you want to receive updates about DSTs and/or identities. You can configurate it on application token level, in the *webhook* field, as follows:  ```json \"webhooks\": {   \"dst\": \"URL\",   \"identity\": \"URL\"   } ```  ### DSTs status update  DSTs send the following status updates: - **DST_STATUS_CHANGED**: whenever the DST changes its status - **SIGNATURE_STATUS_CHANGED**: whenever one of the signatures changes its status  #### DST_STATUS_CHANGED  Sends the following information:  ```json {     \"message\": \"DST_STATUS_CHANGED\",     \"data\": {       \"status\": \"<DST_STATUS>\",       \"dst\": \"<DST_ID>\",       \"reason\": \"<DST_REASON>\"     }   } ```  #### SIGNATURE_STATUS_CHANGED  Sends the following information:  ```json {     \"message\": \"SIGNATURE_STATUS_CHANGED\",     \"data\": {       \"status\": \"<SIGNATURE_STATUS>\",       \"group\": <MEMBERSHIP_GROUP_INDEX>,       \"dst\": {         \"id\": \"<DST_ID>\",         \"title\": \"<DST_TITLE>\"       },       \"signature\": \"<SIGNATURE_ID>\",       \"signer\": \"<SIGNER_USERNAME>\",       \"position\": \"<SIGNATURE_POSITION>\",       \"document\": {         \"display_name\": \"<DOCUMENT_TITLE>\",         \"id\": \"<DOCUMENT_ID>\",         \"order\": <DOCUMENT_INDEX>       },       \"automatic\": <DECLARES_IF_THE_SIGNER_IS_AUTOMATIC>,       \"page\": \"<SIGNATURE_PAGE>\"     }   } ```  ### Identities status update  Identities send the following status updates: - **IDENTITY_REQUEST_ENROLLED**: whenever an identity request is activated  #### IDENTITY_REQUEST_ENROLLED  Sends the following information:  ```json {     \"message\": \"IDENTITY_REQUEST_ENROLLED\",     \"data\": {       \"status\": \"<REQUEST_STATUS>\",       \"request\": \"<REQUEST_ID>\",       \"user\": \"<APPLICANT_USERNAME>\"     }   } ```  ### Urlback  Sometimes may be necessary to make a redirect after an user, from the signature tray, has completed his operations or activated a certificate.  If set, redirects could happen in 3 cases: - after a signature or decline - after a DST has been signed by all the signers or canceled - after the activation of a certificate  In the first two cases the urlback returns the following information through a data form: - **dst-id**: id of the DST - **dst-url**: signature_ticket of the signature - **dst-status**: current status of the DST - **dst-signature-id**: id of the signature - **dst-signature-status**: current status of the signature - **user**: username of the signer - **decline-reason**: in case of a refused DST contains the reason of the decline  In the last case the urlback returns the following information through a data form: - **user**: username of the user activated the certificate - **identity-provider**: the provider has been used to issue the certificate - **identity-request-id**: id of the enrollment request - **identity-id**: id of the new identity - **identity-label**: the label assigned to the identity - **identity-certificate**: public key of the certificate     # noqa: E501

    The version of the OpenAPI document: 1.5.0
    Contact: smartcloud@bit4id.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from signing_today_client.configuration import Configuration


class Document(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'document_uri': 'str',
        'document_uri_options': 'object',
        'document': 'str',
        'display_name': 'str',
        'groups': 'list[list[Signature]]',
        'preview': 'str'
    }

    attribute_map = {
        'document_uri': 'document_uri',
        'document_uri_options': 'document_uri_options',
        'document': 'document',
        'display_name': 'display_name',
        'groups': 'groups',
        'preview': 'preview'
    }

    def __init__(self, document_uri=None, document_uri_options=None, document=None, display_name=None, groups=None, preview=None, local_vars_configuration=None):  # noqa: E501
        """Document - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._document_uri = None
        self._document_uri_options = None
        self._document = None
        self._display_name = None
        self._groups = None
        self._preview = None
        self.discriminator = None

        if document_uri is not None:
            self.document_uri = document_uri
        if document_uri_options is not None:
            self.document_uri_options = document_uri_options
        if document is not None:
            self.document = document
        if display_name is not None:
            self.display_name = display_name
        if groups is not None:
            self.groups = groups
        if preview is not None:
            self.preview = preview

    @property
    def document_uri(self):
        """Gets the document_uri of this Document.  # noqa: E501

        This is the url from where the document, commonly in pdf format, has been uploaded to the Digital Signature Transaction  # noqa: E501

        :return: The document_uri of this Document.  # noqa: E501
        :rtype: str
        """
        return self._document_uri

    @document_uri.setter
    def document_uri(self, document_uri):
        """Sets the document_uri of this Document.

        This is the url from where the document, commonly in pdf format, has been uploaded to the Digital Signature Transaction  # noqa: E501

        :param document_uri: The document_uri of this Document.  # noqa: E501
        :type: str
        """

        self._document_uri = document_uri

    @property
    def document_uri_options(self):
        """Gets the document_uri_options of this Document.  # noqa: E501

        Additional options about the upload of the document  # noqa: E501

        :return: The document_uri_options of this Document.  # noqa: E501
        :rtype: object
        """
        return self._document_uri_options

    @document_uri_options.setter
    def document_uri_options(self, document_uri_options):
        """Sets the document_uri_options of this Document.

        Additional options about the upload of the document  # noqa: E501

        :param document_uri_options: The document_uri_options of this Document.  # noqa: E501
        :type: object
        """

        self._document_uri_options = document_uri_options

    @property
    def document(self):
        """Gets the document of this Document.  # noqa: E501

        The url to download the document  # noqa: E501

        :return: The document of this Document.  # noqa: E501
        :rtype: str
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this Document.

        The url to download the document  # noqa: E501

        :param document: The document of this Document.  # noqa: E501
        :type: str
        """

        self._document = document

    @property
    def display_name(self):
        """Gets the display_name of this Document.  # noqa: E501

        The name associated to the document, provided during the Digital Signature Transaction creation  # noqa: E501

        :return: The display_name of this Document.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Document.

        The name associated to the document, provided during the Digital Signature Transaction creation  # noqa: E501

        :param display_name: The display_name of this Document.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def groups(self):
        """Gets the groups of this Document.  # noqa: E501

        The scheduled signatures ordered as groups of signers. The signatures of a group can be performed only once all the signatures of the previous groups have been completed   # noqa: E501

        :return: The groups of this Document.  # noqa: E501
        :rtype: list[list[Signature]]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this Document.

        The scheduled signatures ordered as groups of signers. The signatures of a group can be performed only once all the signatures of the previous groups have been completed   # noqa: E501

        :param groups: The groups of this Document.  # noqa: E501
        :type: list[list[Signature]]
        """

        self._groups = groups

    @property
    def preview(self):
        """Gets the preview of this Document.  # noqa: E501

        The preview field is a parametric url which can be used to make a preview of the documents in the client integration of SigningToday. The parameters are:   - page: the page to display   - width: the width of the page   - heigth: the heigth of the page The width and height parameters allows to display the page in a preferred size. If both are provided the first one is only use because the proportion of the page remains unchanged   # noqa: E501

        :return: The preview of this Document.  # noqa: E501
        :rtype: str
        """
        return self._preview

    @preview.setter
    def preview(self, preview):
        """Sets the preview of this Document.

        The preview field is a parametric url which can be used to make a preview of the documents in the client integration of SigningToday. The parameters are:   - page: the page to display   - width: the width of the page   - heigth: the heigth of the page The width and height parameters allows to display the page in a preferred size. If both are provided the first one is only use because the proportion of the page remains unchanged   # noqa: E501

        :param preview: The preview of this Document.  # noqa: E501
        :type: str
        """

        self._preview = preview

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Document):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Document):
            return True

        return self.to_dict() != other.to_dict()
