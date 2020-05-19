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


class UpdateOrganization(object):
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
        'default_rao': 'str',
        'dst_default_days': 'int',
        'signature_appearance': 'str',
        'name': 'str',
        'logo': 'str'
    }

    attribute_map = {
        'default_rao': 'default_rao',
        'dst_default_days': 'dst_default_days',
        'signature_appearance': 'signature_appearance',
        'name': 'name',
        'logo': 'logo'
    }

    def __init__(self, default_rao=None, dst_default_days=3, signature_appearance=None, name=None, logo=None, local_vars_configuration=None):  # noqa: E501
        """UpdateOrganization - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._default_rao = None
        self._dst_default_days = None
        self._signature_appearance = None
        self._name = None
        self._logo = None
        self.discriminator = None

        if default_rao is not None:
            self.default_rao = default_rao
        if dst_default_days is not None:
            self.dst_default_days = dst_default_days
        if signature_appearance is not None:
            self.signature_appearance = signature_appearance
        if name is not None:
            self.name = name
        if logo is not None:
            self.logo = logo

    @property
    def default_rao(self):
        """Gets the default_rao of this UpdateOrganization.  # noqa: E501

        This is the default *RAO* user of the Organization. A rao user is the one can associate identities to the other users   # noqa: E501

        :return: The default_rao of this UpdateOrganization.  # noqa: E501
        :rtype: str
        """
        return self._default_rao

    @default_rao.setter
    def default_rao(self, default_rao):
        """Sets the default_rao of this UpdateOrganization.

        This is the default *RAO* user of the Organization. A rao user is the one can associate identities to the other users   # noqa: E501

        :param default_rao: The default_rao of this UpdateOrganization.  # noqa: E501
        :type: str
        """

        self._default_rao = default_rao

    @property
    def dst_default_days(self):
        """Gets the dst_default_days of this UpdateOrganization.  # noqa: E501

        This is the default deadline before the expiration of a digital signature transaction  # noqa: E501

        :return: The dst_default_days of this UpdateOrganization.  # noqa: E501
        :rtype: int
        """
        return self._dst_default_days

    @dst_default_days.setter
    def dst_default_days(self, dst_default_days):
        """Sets the dst_default_days of this UpdateOrganization.

        This is the default deadline before the expiration of a digital signature transaction  # noqa: E501

        :param dst_default_days: The dst_default_days of this UpdateOrganization.  # noqa: E501
        :type: int
        """

        self._dst_default_days = dst_default_days

    @property
    def signature_appearance(self):
        """Gets the signature_appearance of this UpdateOrganization.  # noqa: E501

        This is the url to the default signature appearance will be used for every member of the organization. In the scenario of a user that owns an identity with a signature_appearance will be uset the image associated to the identity rather than the default one   # noqa: E501

        :return: The signature_appearance of this UpdateOrganization.  # noqa: E501
        :rtype: str
        """
        return self._signature_appearance

    @signature_appearance.setter
    def signature_appearance(self, signature_appearance):
        """Sets the signature_appearance of this UpdateOrganization.

        This is the url to the default signature appearance will be used for every member of the organization. In the scenario of a user that owns an identity with a signature_appearance will be uset the image associated to the identity rather than the default one   # noqa: E501

        :param signature_appearance: The signature_appearance of this UpdateOrganization.  # noqa: E501
        :type: str
        """

        self._signature_appearance = signature_appearance

    @property
    def name(self):
        """Gets the name of this UpdateOrganization.  # noqa: E501

        This is an arbitrary name is possible to associate to the Organization   # noqa: E501

        :return: The name of this UpdateOrganization.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateOrganization.

        This is an arbitrary name is possible to associate to the Organization   # noqa: E501

        :param name: The name of this UpdateOrganization.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def logo(self):
        """Gets the logo of this UpdateOrganization.  # noqa: E501

        This is the url to the image is supposed to be used as logo of the Organization, for example the logo or the motto of the company is integrating SigningToday   # noqa: E501

        :return: The logo of this UpdateOrganization.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this UpdateOrganization.

        This is the url to the image is supposed to be used as logo of the Organization, for example the logo or the motto of the company is integrating SigningToday   # noqa: E501

        :param logo: The logo of this UpdateOrganization.  # noqa: E501
        :type: str
        """

        self._logo = logo

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
        if not isinstance(other, UpdateOrganization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateOrganization):
            return True

        return self.to_dict() != other.to_dict()
