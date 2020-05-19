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


class SignatureImplementationResponse(object):
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
        'profile': 'Profile',
        'provider_id': 'ProviderId',
        'position': 'Position',
        'group': 'int',
        'certificate': 'Certificate',
        'title': 'Title',
        'dst': 'Id',
        'signing_time': 'str',
        'reason': 'Reason',
        'channel': 'SignatureImplementationResponseChannel',
        'signature_text': 'str',
        'signature': 'Id',
        'signature_appearance_uri': 'SignatureAppearanceUri',
        'pades_subfilter': 'str',
        'document': 'str',
        'page': 'int',
        'identity': 'Id'
    }

    attribute_map = {
        'profile': 'profile',
        'provider_id': 'provider_id',
        'position': 'position',
        'group': 'group',
        'certificate': 'certificate',
        'title': 'title',
        'dst': 'dst',
        'signing_time': 'signing_time',
        'reason': 'reason',
        'channel': 'channel',
        'signature_text': 'signature_text',
        'signature': 'signature',
        'signature_appearance_uri': 'signature_appearance_uri',
        'pades_subfilter': 'pades_subfilter',
        'document': 'document',
        'page': 'page',
        'identity': 'identity'
    }

    def __init__(self, profile=None, provider_id=None, position=None, group=None, certificate=None, title=None, dst=None, signing_time=None, reason=None, channel=None, signature_text=None, signature=None, signature_appearance_uri=None, pades_subfilter=None, document=None, page=None, identity=None, local_vars_configuration=None):  # noqa: E501
        """SignatureImplementationResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._profile = None
        self._provider_id = None
        self._position = None
        self._group = None
        self._certificate = None
        self._title = None
        self._dst = None
        self._signing_time = None
        self._reason = None
        self._channel = None
        self._signature_text = None
        self._signature = None
        self._signature_appearance_uri = None
        self._pades_subfilter = None
        self._document = None
        self._page = None
        self._identity = None
        self.discriminator = None

        if profile is not None:
            self.profile = profile
        if provider_id is not None:
            self.provider_id = provider_id
        if position is not None:
            self.position = position
        if group is not None:
            self.group = group
        if certificate is not None:
            self.certificate = certificate
        if title is not None:
            self.title = title
        if dst is not None:
            self.dst = dst
        if signing_time is not None:
            self.signing_time = signing_time
        if reason is not None:
            self.reason = reason
        if channel is not None:
            self.channel = channel
        if signature_text is not None:
            self.signature_text = signature_text
        if signature is not None:
            self.signature = signature
        if signature_appearance_uri is not None:
            self.signature_appearance_uri = signature_appearance_uri
        if pades_subfilter is not None:
            self.pades_subfilter = pades_subfilter
        if document is not None:
            self.document = document
        if page is not None:
            self.page = page
        if identity is not None:
            self.identity = identity

    @property
    def profile(self):
        """Gets the profile of this SignatureImplementationResponse.  # noqa: E501


        :return: The profile of this SignatureImplementationResponse.  # noqa: E501
        :rtype: Profile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this SignatureImplementationResponse.


        :param profile: The profile of this SignatureImplementationResponse.  # noqa: E501
        :type: Profile
        """

        self._profile = profile

    @property
    def provider_id(self):
        """Gets the provider_id of this SignatureImplementationResponse.  # noqa: E501


        :return: The provider_id of this SignatureImplementationResponse.  # noqa: E501
        :rtype: ProviderId
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this SignatureImplementationResponse.


        :param provider_id: The provider_id of this SignatureImplementationResponse.  # noqa: E501
        :type: ProviderId
        """

        self._provider_id = provider_id

    @property
    def position(self):
        """Gets the position of this SignatureImplementationResponse.  # noqa: E501


        :return: The position of this SignatureImplementationResponse.  # noqa: E501
        :rtype: Position
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this SignatureImplementationResponse.


        :param position: The position of this SignatureImplementationResponse.  # noqa: E501
        :type: Position
        """

        self._position = position

    @property
    def group(self):
        """Gets the group of this SignatureImplementationResponse.  # noqa: E501

        Number of the groups which the signer belongs during digital signature transaction creation  # noqa: E501

        :return: The group of this SignatureImplementationResponse.  # noqa: E501
        :rtype: int
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this SignatureImplementationResponse.

        Number of the groups which the signer belongs during digital signature transaction creation  # noqa: E501

        :param group: The group of this SignatureImplementationResponse.  # noqa: E501
        :type: int
        """

        self._group = group

    @property
    def certificate(self):
        """Gets the certificate of this SignatureImplementationResponse.  # noqa: E501


        :return: The certificate of this SignatureImplementationResponse.  # noqa: E501
        :rtype: Certificate
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this SignatureImplementationResponse.


        :param certificate: The certificate of this SignatureImplementationResponse.  # noqa: E501
        :type: Certificate
        """

        self._certificate = certificate

    @property
    def title(self):
        """Gets the title of this SignatureImplementationResponse.  # noqa: E501


        :return: The title of this SignatureImplementationResponse.  # noqa: E501
        :rtype: Title
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SignatureImplementationResponse.


        :param title: The title of this SignatureImplementationResponse.  # noqa: E501
        :type: Title
        """

        self._title = title

    @property
    def dst(self):
        """Gets the dst of this SignatureImplementationResponse.  # noqa: E501


        :return: The dst of this SignatureImplementationResponse.  # noqa: E501
        :rtype: Id
        """
        return self._dst

    @dst.setter
    def dst(self, dst):
        """Sets the dst of this SignatureImplementationResponse.


        :param dst: The dst of this SignatureImplementationResponse.  # noqa: E501
        :type: Id
        """

        self._dst = dst

    @property
    def signing_time(self):
        """Gets the signing_time of this SignatureImplementationResponse.  # noqa: E501


        :return: The signing_time of this SignatureImplementationResponse.  # noqa: E501
        :rtype: str
        """
        return self._signing_time

    @signing_time.setter
    def signing_time(self, signing_time):
        """Sets the signing_time of this SignatureImplementationResponse.


        :param signing_time: The signing_time of this SignatureImplementationResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["pdf"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and signing_time not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `signing_time` ({0}), must be one of {1}"  # noqa: E501
                .format(signing_time, allowed_values)
            )

        self._signing_time = signing_time

    @property
    def reason(self):
        """Gets the reason of this SignatureImplementationResponse.  # noqa: E501


        :return: The reason of this SignatureImplementationResponse.  # noqa: E501
        :rtype: Reason
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this SignatureImplementationResponse.


        :param reason: The reason of this SignatureImplementationResponse.  # noqa: E501
        :type: Reason
        """

        self._reason = reason

    @property
    def channel(self):
        """Gets the channel of this SignatureImplementationResponse.  # noqa: E501


        :return: The channel of this SignatureImplementationResponse.  # noqa: E501
        :rtype: SignatureImplementationResponseChannel
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this SignatureImplementationResponse.


        :param channel: The channel of this SignatureImplementationResponse.  # noqa: E501
        :type: SignatureImplementationResponseChannel
        """

        self._channel = channel

    @property
    def signature_text(self):
        """Gets the signature_text of this SignatureImplementationResponse.  # noqa: E501


        :return: The signature_text of this SignatureImplementationResponse.  # noqa: E501
        :rtype: str
        """
        return self._signature_text

    @signature_text.setter
    def signature_text(self, signature_text):
        """Sets the signature_text of this SignatureImplementationResponse.


        :param signature_text: The signature_text of this SignatureImplementationResponse.  # noqa: E501
        :type: str
        """

        self._signature_text = signature_text

    @property
    def signature(self):
        """Gets the signature of this SignatureImplementationResponse.  # noqa: E501


        :return: The signature of this SignatureImplementationResponse.  # noqa: E501
        :rtype: Id
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this SignatureImplementationResponse.


        :param signature: The signature of this SignatureImplementationResponse.  # noqa: E501
        :type: Id
        """

        self._signature = signature

    @property
    def signature_appearance_uri(self):
        """Gets the signature_appearance_uri of this SignatureImplementationResponse.  # noqa: E501


        :return: The signature_appearance_uri of this SignatureImplementationResponse.  # noqa: E501
        :rtype: SignatureAppearanceUri
        """
        return self._signature_appearance_uri

    @signature_appearance_uri.setter
    def signature_appearance_uri(self, signature_appearance_uri):
        """Sets the signature_appearance_uri of this SignatureImplementationResponse.


        :param signature_appearance_uri: The signature_appearance_uri of this SignatureImplementationResponse.  # noqa: E501
        :type: SignatureAppearanceUri
        """

        self._signature_appearance_uri = signature_appearance_uri

    @property
    def pades_subfilter(self):
        """Gets the pades_subfilter of this SignatureImplementationResponse.  # noqa: E501


        :return: The pades_subfilter of this SignatureImplementationResponse.  # noqa: E501
        :rtype: str
        """
        return self._pades_subfilter

    @pades_subfilter.setter
    def pades_subfilter(self, pades_subfilter):
        """Sets the pades_subfilter of this SignatureImplementationResponse.


        :param pades_subfilter: The pades_subfilter of this SignatureImplementationResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["ETSI.CAdES.detached"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and pades_subfilter not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `pades_subfilter` ({0}), must be one of {1}"  # noqa: E501
                .format(pades_subfilter, allowed_values)
            )

        self._pades_subfilter = pades_subfilter

    @property
    def document(self):
        """Gets the document of this SignatureImplementationResponse.  # noqa: E501


        :return: The document of this SignatureImplementationResponse.  # noqa: E501
        :rtype: str
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this SignatureImplementationResponse.


        :param document: The document of this SignatureImplementationResponse.  # noqa: E501
        :type: str
        """

        self._document = document

    @property
    def page(self):
        """Gets the page of this SignatureImplementationResponse.  # noqa: E501


        :return: The page of this SignatureImplementationResponse.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this SignatureImplementationResponse.


        :param page: The page of this SignatureImplementationResponse.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def identity(self):
        """Gets the identity of this SignatureImplementationResponse.  # noqa: E501


        :return: The identity of this SignatureImplementationResponse.  # noqa: E501
        :rtype: Id
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this SignatureImplementationResponse.


        :param identity: The identity of this SignatureImplementationResponse.  # noqa: E501
        :type: Id
        """

        self._identity = identity

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
        if not isinstance(other, SignatureImplementationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignatureImplementationResponse):
            return True

        return self.to_dict() != other.to_dict()
