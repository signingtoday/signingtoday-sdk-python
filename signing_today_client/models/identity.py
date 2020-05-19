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


class Identity(object):
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
        'id': 'str',
        'certificate': 'str',
        'not_after': 'str',
        'status': 'str',
        'next': 'str',
        'actions': 'IdentityActions',
        'provider': 'str',
        'label': 'str',
        'signature_appearance_uri': 'str',
        'provider_id': 'str',
        'provider_type': 'str',
        'provider_data': 'object',
        'provider_image': 'str',
        'send_otp_url': 'str',
        'sign_url': 'str',
        'has_been_imported': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'certificate': 'certificate',
        'not_after': 'not_after',
        'status': 'status',
        'next': 'next',
        'actions': 'actions',
        'provider': 'provider',
        'label': 'label',
        'signature_appearance_uri': 'signature_appearance_uri',
        'provider_id': 'provider_id',
        'provider_type': 'provider_type',
        'provider_data': 'provider_data',
        'provider_image': 'provider_image',
        'send_otp_url': 'send_otp_url',
        'sign_url': 'sign_url',
        'has_been_imported': 'has_been_imported'
    }

    def __init__(self, id=None, certificate=None, not_after=None, status=None, next=None, actions=None, provider=None, label=None, signature_appearance_uri=None, provider_id=None, provider_type=None, provider_data=None, provider_image=None, send_otp_url=None, sign_url=None, has_been_imported=None, local_vars_configuration=None):  # noqa: E501
        """Identity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._certificate = None
        self._not_after = None
        self._status = None
        self._next = None
        self._actions = None
        self._provider = None
        self._label = None
        self._signature_appearance_uri = None
        self._provider_id = None
        self._provider_type = None
        self._provider_data = None
        self._provider_image = None
        self._send_otp_url = None
        self._sign_url = None
        self._has_been_imported = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if certificate is not None:
            self.certificate = certificate
        if not_after is not None:
            self.not_after = not_after
        if status is not None:
            self.status = status
        if next is not None:
            self.next = next
        if actions is not None:
            self.actions = actions
        if provider is not None:
            self.provider = provider
        if label is not None:
            self.label = label
        if signature_appearance_uri is not None:
            self.signature_appearance_uri = signature_appearance_uri
        if provider_id is not None:
            self.provider_id = provider_id
        if provider_type is not None:
            self.provider_type = provider_type
        if provider_data is not None:
            self.provider_data = provider_data
        if provider_image is not None:
            self.provider_image = provider_image
        if send_otp_url is not None:
            self.send_otp_url = send_otp_url
        if sign_url is not None:
            self.sign_url = sign_url
        if has_been_imported is not None:
            self.has_been_imported = has_been_imported

    @property
    def id(self):
        """Gets the id of this Identity.  # noqa: E501

        The uuid code that identifies the Identity  # noqa: E501

        :return: The id of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Identity.

        The uuid code that identifies the Identity  # noqa: E501

        :param id: The id of this Identity.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def certificate(self):
        """Gets the certificate of this Identity.  # noqa: E501

        The X.509 certificate in PEM format of the Identity  # noqa: E501

        :return: The certificate of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this Identity.

        The X.509 certificate in PEM format of the Identity  # noqa: E501

        :param certificate: The certificate of this Identity.  # noqa: E501
        :type: str
        """

        self._certificate = certificate

    @property
    def not_after(self):
        """Gets the not_after of this Identity.  # noqa: E501

        Deadline of the Identity, expressed in ISO format  # noqa: E501

        :return: The not_after of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this Identity.

        Deadline of the Identity, expressed in ISO format  # noqa: E501

        :param not_after: The not_after of this Identity.  # noqa: E501
        :type: str
        """

        self._not_after = not_after

    @property
    def status(self):
        """Gets the status of this Identity.  # noqa: E501

        Identity status which can be one of the following. When an identity request is send, the identity is created and the status is **pending** until the provider dont approve the request. Then status of the identity changes to **active**. If for some reason an error occurs during the process, or after that, the status will be **error**   # noqa: E501

        :return: The status of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Identity.

        Identity status which can be one of the following. When an identity request is send, the identity is created and the status is **pending** until the provider dont approve the request. Then status of the identity changes to **active**. If for some reason an error occurs during the process, or after that, the status will be **error**   # noqa: E501

        :param status: The status of this Identity.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "active", "error"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def next(self):
        """Gets the next of this Identity.  # noqa: E501

        The next step to complete the activation procedure  # noqa: E501

        :return: The next of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this Identity.

        The next step to complete the activation procedure  # noqa: E501

        :param next: The next of this Identity.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def actions(self):
        """Gets the actions of this Identity.  # noqa: E501


        :return: The actions of this Identity.  # noqa: E501
        :rtype: IdentityActions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this Identity.


        :param actions: The actions of this Identity.  # noqa: E501
        :type: IdentityActions
        """

        self._actions = actions

    @property
    def provider(self):
        """Gets the provider of this Identity.  # noqa: E501

        The name of the provider that issued the certificate for the Identity  # noqa: E501

        :return: The provider of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this Identity.

        The name of the provider that issued the certificate for the Identity  # noqa: E501

        :param provider: The provider of this Identity.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def label(self):
        """Gets the label of this Identity.  # noqa: E501

        The label is an arbitrary name is possible to associate to an idenity. Doing so allows to distinguish different identities issued from the same provider during the performance of the signature in the signature tray  # noqa: E501

        :return: The label of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Identity.

        The label is an arbitrary name is possible to associate to an idenity. Doing so allows to distinguish different identities issued from the same provider during the performance of the signature in the signature tray  # noqa: E501

        :param label: The label of this Identity.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def signature_appearance_uri(self):
        """Gets the signature_appearance_uri of this Identity.  # noqa: E501

        This is the url to the image that will be impressed on the document after the performance of the signature   # noqa: E501

        :return: The signature_appearance_uri of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._signature_appearance_uri

    @signature_appearance_uri.setter
    def signature_appearance_uri(self, signature_appearance_uri):
        """Sets the signature_appearance_uri of this Identity.

        This is the url to the image that will be impressed on the document after the performance of the signature   # noqa: E501

        :param signature_appearance_uri: The signature_appearance_uri of this Identity.  # noqa: E501
        :type: str
        """

        self._signature_appearance_uri = signature_appearance_uri

    @property
    def provider_id(self):
        """Gets the provider_id of this Identity.  # noqa: E501

        _provider_id_ is the univocal name of the provider that issued the identity   # noqa: E501

        :return: The provider_id of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this Identity.

        _provider_id_ is the univocal name of the provider that issued the identity   # noqa: E501

        :param provider_id: The provider_id of this Identity.  # noqa: E501
        :type: str
        """

        self._provider_id = provider_id

    @property
    def provider_type(self):
        """Gets the provider_type of this Identity.  # noqa: E501

        Type of the provider. The most usual type is **cloud**   # noqa: E501

        :return: The provider_type of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this Identity.

        Type of the provider. The most usual type is **cloud**   # noqa: E501

        :param provider_type: The provider_type of this Identity.  # noqa: E501
        :type: str
        """

        self._provider_type = provider_type

    @property
    def provider_data(self):
        """Gets the provider_data of this Identity.  # noqa: E501

        Data of the provider that issued the certificate, it is variable from provider to provider  # noqa: E501

        :return: The provider_data of this Identity.  # noqa: E501
        :rtype: object
        """
        return self._provider_data

    @provider_data.setter
    def provider_data(self, provider_data):
        """Sets the provider_data of this Identity.

        Data of the provider that issued the certificate, it is variable from provider to provider  # noqa: E501

        :param provider_data: The provider_data of this Identity.  # noqa: E501
        :type: object
        """

        self._provider_data = provider_data

    @property
    def provider_image(self):
        """Gets the provider_image of this Identity.  # noqa: E501

        This is the logo of the provider that issued the identity  # noqa: E501

        :return: The provider_image of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._provider_image

    @provider_image.setter
    def provider_image(self, provider_image):
        """Sets the provider_image of this Identity.

        This is the logo of the provider that issued the identity  # noqa: E501

        :param provider_image: The provider_image of this Identity.  # noqa: E501
        :type: str
        """

        self._provider_image = provider_image

    @property
    def send_otp_url(self):
        """Gets the send_otp_url of this Identity.  # noqa: E501

        The url to send a one time password to the user which the identity is associated  # noqa: E501

        :return: The send_otp_url of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._send_otp_url

    @send_otp_url.setter
    def send_otp_url(self, send_otp_url):
        """Sets the send_otp_url of this Identity.

        The url to send a one time password to the user which the identity is associated  # noqa: E501

        :param send_otp_url: The send_otp_url of this Identity.  # noqa: E501
        :type: str
        """

        self._send_otp_url = send_otp_url

    @property
    def sign_url(self):
        """Gets the sign_url of this Identity.  # noqa: E501

        The url to sign a document of a digital signature transaction  # noqa: E501

        :return: The sign_url of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._sign_url

    @sign_url.setter
    def sign_url(self, sign_url):
        """Sets the sign_url of this Identity.

        The url to sign a document of a digital signature transaction  # noqa: E501

        :param sign_url: The sign_url of this Identity.  # noqa: E501
        :type: str
        """

        self._sign_url = sign_url

    @property
    def has_been_imported(self):
        """Gets the has_been_imported of this Identity.  # noqa: E501

        If the Identity has been imported from another pre-existing Identity the has_been_imported field is set to **true**  # noqa: E501

        :return: The has_been_imported of this Identity.  # noqa: E501
        :rtype: bool
        """
        return self._has_been_imported

    @has_been_imported.setter
    def has_been_imported(self, has_been_imported):
        """Sets the has_been_imported of this Identity.

        If the Identity has been imported from another pre-existing Identity the has_been_imported field is set to **true**  # noqa: E501

        :param has_been_imported: The has_been_imported of this Identity.  # noqa: E501
        :type: bool
        """

        self._has_been_imported = has_been_imported

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
        if not isinstance(other, Identity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Identity):
            return True

        return self.to_dict() != other.to_dict()
