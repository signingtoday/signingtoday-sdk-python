# coding: utf-8

"""
    Signing Today API

    *Signing Today* enables seamless integration of digital signatures into any website by the use of easy requests to our API. This is the smart way of adding digital signature support with a great user experience.   *Signing Today APIs* use HTTP methods and are RESTful based, moreover they are protected by a *server to server authentication* standard by the use of tokens.   *Signing Today APIs* can be used in these environments:   | Environment | Description | Endpoint | | ----------- | ----------- | -------- | | Sandbox     | Test environment | `https://sandbox.signingtoday.com` | | Live        | Production environment | `https://api.signingtoday.com` |   For every single request to Signing Today has to be defined the following *HTTP* header: - `Authorization`, which contains the authentication token.  If the request has a body than another *HTTP* header is requested: - `Content-Type`, with `application/json` value.   Follows an example of usage to enumerate all the user of *my-org* organization.  **Example**  ```json $ curl https://sandbox.signingtoday.com/api/v1/my-org/users \\     -H 'Authorization: Token <access-token>' ```  ## HTTP methods used  APIs use the right HTTP verb in every situation.  | Method   | Description                    | | -------- | ------------------------------ | | `GET`    | Request data from a resource   | | `POST`   | Send data to create a resource | | `PUT`    | Update a resource              | | `PATCH`  | Partially update a resource    | | `DELETE` | Delete a resourse              |   ## Response definition  All the response are in JSON format. As response to a request of all users of an organization you will have a result like this:  ```json {     \"pagination\": {       \"count\": 75,       \"previous\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=1\",       \"next\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=3\",       \"pages\": 8,       \"page\": 2     },     \"meta\": {       \"code\": 200     },     \"data\": [       {         \"id\": \"jdo\",         \"status\": \"enabled\",         \"type\": \"Basic user account\",         \"email\": johndoe@dummyemail.com,         \"first_name\": \"John\",         \"last_name\": \"Doe\",         \"wallet\": [],         \"created_by\": \"system\",         \"owner\": false,         \"automatic\": false,         \"rao\": false       },       ...     ]   } ```  The JSON of the response is made of three parts: - Pagination - Meta - Data  ### Pagination  *Pagination* object allows to split the response into parts and then to rebuild it sequentially by the use of `next` and `previous` parameters, by which you get previous and following blocks. The *Pagination* is present only if the response is a list of objects.  The general structure of *Pagination* object is the following:  ```json {     \"pagination\": {       \"count\": 75,       \"previous\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=1\",       \"next\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=3\",       \"pages\": 8,       \"page\": 2     },     ...   } ```  ### Meta  *Meta* object is used to enrich the information about the response. In the previous example, a successful case of response, *Meta* will have value `status: 2XX`. In case of unsuccessful response, *Meta* will have further information, as follows:  ```json {     \"meta\": {       \"code\": <HTTP STATUS CODE>,       \"error_type\": <STATUS CODE DESCRIPTION>,       \"error_message\": <ERROR DESCRIPTION>     }   } ```  ### Data  *Data* object outputs as object or list of them. Contains the expected data as requested to the API.  ## Search filters  Search filters of the API have the following structure:  `where_ATTRIBUTENAME`=`VALUE`  In this way you make a case-sensitive search of *VALUE*. You can extend it through the Django lookup, obtaining more specific filters. For example:  `where_ATTRIBUTENAME__LOOKUP`=`VALUE`  where *LOOKUP* can be replaced with `icontains` to have a partial insensitive research, where  `where_first_name__icontains`=`CHa`  matches with every user that have the *cha* string in their name, with no differences between capital and lower cases.  [Here](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#field-lookups) the list of the lookups.  ## Webhooks  Signing Today supports webhooks for the update of DSTs and identities status. You can choose if to use or not webhooks and if you want to receive updates about DSTs and/or identities. You can configurate it on application token level, in the *webhook* field, as follows:  ```json \"webhooks\": {   \"dst\": \"URL\",   \"identity\": \"URL\"   } ```  ### DSTs status update  DSTs send the following status updates: - **DST_STATUS_CHANGED**: whenever the DST changes its status - **SIGNATURE_STATUS_CHANGED**: whenever one of the signatures changes its status  #### DST_STATUS_CHANGED  Sends the following information:  ```json {     \"message\": \"DST_STATUS_CHANGED\",     \"data\": {       \"status\": \"<DST_STATUS>\",       \"dst\": \"<DST_ID>\",       \"reason\": \"<DST_REASON>\"     }   } ```  #### SIGNATURE_STATUS_CHANGED  Sends the following information:  ```json {     \"message\": \"SIGNATURE_STATUS_CHANGED\",     \"data\": {       \"status\": \"<SIGNATURE_STATUS>\",       \"group\": <MEMBERSHIP_GROUP_INDEX>,       \"dst\": {         \"id\": \"<DST_ID>\",         \"title\": \"<DST_TITLE>\"       },       \"signature\": \"<SIGNATURE_ID>\",       \"signer\": \"<SIGNER_USERNAME>\",       \"position\": \"<SIGNATURE_POSITION>\",       \"document\": {         \"display_name\": \"<DOCUMENT_TITLE>\",         \"id\": \"<DOCUMENT_ID>\",         \"order\": <DOCUMENT_INDEX>       },       \"automatic\": <DECLARES_IF_THE_SIGNER_IS_AUTOMATIC>,       \"page\": \"<SIGNATURE_PAGE>\"     }   } ```  ### Identities status update  Identities send the following status updates: - **IDENTITY_REQUEST_ENROLLED**: whenever an identity request is activated  #### IDENTITY_REQUEST_ENROLLED  Sends the following information:  ```json {     \"message\": \"IDENTITY_REQUEST_ENROLLED\",     \"data\": {       \"status\": \"<REQUEST_STATUS>\",       \"request\": \"<REQUEST_ID>\",       \"user\": \"<APPLICANT_USERNAME>\"     }   } ```  ### Urlback  Sometimes may be necessary to make a redirect after an user, from the signature tray, has completed his operations or activated a certificate.  If set, redirects could happen in 3 cases: - after a signature or decline - after a DST has been signed by all the signers or canceled - after the activation of a certificate  In the first two cases the urlback returns the following information through a data form: - **dst-id**: id of the DST - **dst-url**: signature_ticket of the signature - **dst-status**: current status of the DST - **dst-signature-id**: id of the signature - **dst-signature-status**: current status of the signature - **user**: username of the signer - **decline-reason**: in case of a refused DST contains the reason of the decline  In the last case the urlback returns the following information through a data form: - **user**: username of the user activated the certificate - **identity-provider**: the provider has been used to issue the certificate - **identity-request-id**: id of the enrollment request - **identity-id**: id of the new identity - **identity-label**: the label assigned to the identity - **identity-certificate**: public key of the certificate  ## SUPPORTED Provider  The supported providers are:   - *_aruba_*   - *infocert*   - *namirial*   - *uanataca*    # noqa: E501

    The version of the OpenAPI document: 1.5.0
    Contact: smartcloud@bit4id.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from signing_today_client.configuration import Configuration


class SignatureDSTWhere(object):
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
        'page': 'int',
        'position': 'str',
        'image_uri': 'str',
        'text': 'list[SignatureWhereText]'
    }

    attribute_map = {
        'page': 'page',
        'position': 'position',
        'image_uri': 'image_uri',
        'text': 'text'
    }

    def __init__(self, page=None, position=None, image_uri=None, text=None, local_vars_configuration=None):  # noqa: E501
        """SignatureDSTWhere - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._page = None
        self._position = None
        self._image_uri = None
        self._text = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if position is not None:
            self.position = position
        if image_uri is not None:
            self.image_uri = image_uri
        if text is not None:
            self.text = text

    @property
    def page(self):
        """Gets the page of this SignatureDSTWhere.  # noqa: E501

        As can be guessed this is the page where to allocate the Signature  # noqa: E501

        :return: The page of this SignatureDSTWhere.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this SignatureDSTWhere.

        As can be guessed this is the page where to allocate the Signature  # noqa: E501

        :param page: The page of this SignatureDSTWhere.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def position(self):
        """Gets the position of this SignatureDSTWhere.  # noqa: E501

        This is the exact position in the choosen page where to attach the Signature. Multiple unit of measurement are provided. The format is the following:   - \"rect: 50mm, 100mm, 200mm, 150mm\"   # noqa: E501

        :return: The position of this SignatureDSTWhere.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this SignatureDSTWhere.

        This is the exact position in the choosen page where to attach the Signature. Multiple unit of measurement are provided. The format is the following:   - \"rect: 50mm, 100mm, 200mm, 150mm\"   # noqa: E501

        :param position: The position of this SignatureDSTWhere.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def image_uri(self):
        """Gets the image_uri of this SignatureDSTWhere.  # noqa: E501

        If provided this current image will be used for the signature, as a graphic appearance. This overrides the appearance definited in the Identity, which still will be the default one. If no signature appearance is provided in the Identity than will be used the default one of the Organization. If you choose to avoi the signature appearance than use this field as follows: _image_uri_: null   # noqa: E501

        :return: The image_uri of this SignatureDSTWhere.  # noqa: E501
        :rtype: str
        """
        return self._image_uri

    @image_uri.setter
    def image_uri(self, image_uri):
        """Sets the image_uri of this SignatureDSTWhere.

        If provided this current image will be used for the signature, as a graphic appearance. This overrides the appearance definited in the Identity, which still will be the default one. If no signature appearance is provided in the Identity than will be used the default one of the Organization. If you choose to avoi the signature appearance than use this field as follows: _image_uri_: null   # noqa: E501

        :param image_uri: The image_uri of this SignatureDSTWhere.  # noqa: E501
        :type: str
        """

        self._image_uri = image_uri

    @property
    def text(self):
        """Gets the text of this SignatureDSTWhere.  # noqa: E501

        The text field will be filled with a list of paragraphs that will be displayed next to the graphic signature. Each paragraph may have its own font type, font dimension, line-up and a list of rows (strings) which will compose the paragraph. It is possible to specify some _placeholders_ as well. The paragraph objects will use default font and line-up if none was specified. If no _format_ field is specified than will be used the default one:   \"format\": [     \"Signed by {subject[commonName]}\",     \"{subject[C]}\",     \"{subject[L]}\",     \"{subject[S]}\",     \"{subject[OU]}\",     \"{subject[O]}\",     \"{subject[E]}\"   ] Where {subject[...]} is a placeholder which will be filled with the certificate attirbutes. Follows the list of the placeholders:   - commonName: CommonName   - OU: OrganizationalUnit   - O: Organization   - L: Locality   - S: StateOrProvinceName   - C: CountryName   # noqa: E501

        :return: The text of this SignatureDSTWhere.  # noqa: E501
        :rtype: list[SignatureWhereText]
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SignatureDSTWhere.

        The text field will be filled with a list of paragraphs that will be displayed next to the graphic signature. Each paragraph may have its own font type, font dimension, line-up and a list of rows (strings) which will compose the paragraph. It is possible to specify some _placeholders_ as well. The paragraph objects will use default font and line-up if none was specified. If no _format_ field is specified than will be used the default one:   \"format\": [     \"Signed by {subject[commonName]}\",     \"{subject[C]}\",     \"{subject[L]}\",     \"{subject[S]}\",     \"{subject[OU]}\",     \"{subject[O]}\",     \"{subject[E]}\"   ] Where {subject[...]} is a placeholder which will be filled with the certificate attirbutes. Follows the list of the placeholders:   - commonName: CommonName   - OU: OrganizationalUnit   - O: Organization   - L: Locality   - S: StateOrProvinceName   - C: CountryName   # noqa: E501

        :param text: The text of this SignatureDSTWhere.  # noqa: E501
        :type: list[SignatureWhereText]
        """

        self._text = text

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
        if not isinstance(other, SignatureDSTWhere):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignatureDSTWhere):
            return True

        return self.to_dict() != other.to_dict()
