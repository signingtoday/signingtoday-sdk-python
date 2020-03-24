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


class SignatureDST(object):
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
        'declinable': 'bool',
        'profile': 'str',
        'display_name': 'str',
        'reason': 'str',
        'signer': 'str',
        'description': 'str',
        'urlback': 'str',
        'where': 'SignatureDSTWhere',
        'constraints': 'object'
    }

    attribute_map = {
        'declinable': 'declinable',
        'profile': 'profile',
        'display_name': 'display_name',
        'reason': 'reason',
        'signer': 'signer',
        'description': 'description',
        'urlback': 'urlback',
        'where': 'where',
        'constraints': 'constraints'
    }

    def __init__(self, declinable=None, profile=None, display_name=None, reason=None, signer=None, description=None, urlback=None, where=None, constraints=None, local_vars_configuration=None):  # noqa: E501
        """SignatureDST - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._declinable = None
        self._profile = None
        self._display_name = None
        self._reason = None
        self._signer = None
        self._description = None
        self._urlback = None
        self._where = None
        self._constraints = None
        self.discriminator = None

        if declinable is not None:
            self.declinable = declinable
        if profile is not None:
            self.profile = profile
        if display_name is not None:
            self.display_name = display_name
        if reason is not None:
            self.reason = reason
        if signer is not None:
            self.signer = signer
        if description is not None:
            self.description = description
        if urlback is not None:
            self.urlback = urlback
        if where is not None:
            self.where = where
        if constraints is not None:
            self.constraints = constraints

    @property
    def declinable(self):
        """Gets the declinable of this SignatureDST.  # noqa: E501

        If true the signer is able to decline the Signature if he wants to  # noqa: E501

        :return: The declinable of this SignatureDST.  # noqa: E501
        :rtype: bool
        """
        return self._declinable

    @declinable.setter
    def declinable(self, declinable):
        """Sets the declinable of this SignatureDST.

        If true the signer is able to decline the Signature if he wants to  # noqa: E501

        :param declinable: The declinable of this SignatureDST.  # noqa: E501
        :type: bool
        """

        self._declinable = declinable

    @property
    def profile(self):
        """Gets the profile of this SignatureDST.  # noqa: E501

        The _profile_ field of the Signature object specifies the modality of signature is going to be performed, and can be:   - _PADES_ :     - allows to exclusively sign a pdf file with the signature     directly affixed into the document;   - _CADES_ :     - allows to sign different types of documents; the signature     is not \"physically\" into the document but the signature and the file     are placed together in an envelope instead, making thus a _.p7m_     extension.   # noqa: E501

        :return: The profile of this SignatureDST.  # noqa: E501
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this SignatureDST.

        The _profile_ field of the Signature object specifies the modality of signature is going to be performed, and can be:   - _PADES_ :     - allows to exclusively sign a pdf file with the signature     directly affixed into the document;   - _CADES_ :     - allows to sign different types of documents; the signature     is not \"physically\" into the document but the signature and the file     are placed together in an envelope instead, making thus a _.p7m_     extension.   # noqa: E501

        :param profile: The profile of this SignatureDST.  # noqa: E501
        :type: str
        """
        allowed_values = ["pades-bes", "pades-t", "cades-bes", "cades-t"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and profile not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `profile` ({0}), must be one of {1}"  # noqa: E501
                .format(profile, allowed_values)
            )

        self._profile = profile

    @property
    def display_name(self):
        """Gets the display_name of this SignatureDST.  # noqa: E501

        This is the name will be displayed on the signature tray associated to the Signature has to be performed. Usually is the _full name_ of the user is going to sign  # noqa: E501

        :return: The display_name of this SignatureDST.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this SignatureDST.

        This is the name will be displayed on the signature tray associated to the Signature has to be performed. Usually is the _full name_ of the user is going to sign  # noqa: E501

        :param display_name: The display_name of this SignatureDST.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def reason(self):
        """Gets the reason of this SignatureDST.  # noqa: E501

        The reason of the Signature, or rather a motivational description associated to the Signature  # noqa: E501

        :return: The reason of this SignatureDST.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this SignatureDST.

        The reason of the Signature, or rather a motivational description associated to the Signature  # noqa: E501

        :param reason: The reason of this SignatureDST.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def signer(self):
        """Gets the signer of this SignatureDST.  # noqa: E501

        The user that have to sign the digital signature transaction  # noqa: E501

        :return: The signer of this SignatureDST.  # noqa: E501
        :rtype: str
        """
        return self._signer

    @signer.setter
    def signer(self, signer):
        """Sets the signer of this SignatureDST.

        The user that have to sign the digital signature transaction  # noqa: E501

        :param signer: The signer of this SignatureDST.  # noqa: E501
        :type: str
        """

        self._signer = signer

    @property
    def description(self):
        """Gets the description of this SignatureDST.  # noqa: E501

        This is a simple description to attach with the Signature  # noqa: E501

        :return: The description of this SignatureDST.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SignatureDST.

        This is a simple description to attach with the Signature  # noqa: E501

        :param description: The description of this SignatureDST.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def urlback(self):
        """Gets the urlback of this SignatureDST.  # noqa: E501

        The url for the redirection from Signature tray when the digital signature transaction is completed or annulled  # noqa: E501

        :return: The urlback of this SignatureDST.  # noqa: E501
        :rtype: str
        """
        return self._urlback

    @urlback.setter
    def urlback(self, urlback):
        """Sets the urlback of this SignatureDST.

        The url for the redirection from Signature tray when the digital signature transaction is completed or annulled  # noqa: E501

        :param urlback: The urlback of this SignatureDST.  # noqa: E501
        :type: str
        """

        self._urlback = urlback

    @property
    def where(self):
        """Gets the where of this SignatureDST.  # noqa: E501


        :return: The where of this SignatureDST.  # noqa: E501
        :rtype: SignatureDSTWhere
        """
        return self._where

    @where.setter
    def where(self, where):
        """Sets the where of this SignatureDST.


        :param where: The where of this SignatureDST.  # noqa: E501
        :type: SignatureDSTWhere
        """

        self._where = where

    @property
    def constraints(self):
        """Gets the constraints of this SignatureDST.  # noqa: E501

        Particular constraints for the Signature. For example constraints about the _firs tname_ or _last name_ of the certificate associated with the identity is going to sign. The way to use this field is through the _django lookups_, for example:   - \"certificate__subject_givenName__iexact=JOHN\"   # noqa: E501

        :return: The constraints of this SignatureDST.  # noqa: E501
        :rtype: object
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this SignatureDST.

        Particular constraints for the Signature. For example constraints about the _firs tname_ or _last name_ of the certificate associated with the identity is going to sign. The way to use this field is through the _django lookups_, for example:   - \"certificate__subject_givenName__iexact=JOHN\"   # noqa: E501

        :param constraints: The constraints of this SignatureDST.  # noqa: E501
        :type: object
        """

        self._constraints = constraints

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
        if not isinstance(other, SignatureDST):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignatureDST):
            return True

        return self.to_dict() != other.to_dict()
