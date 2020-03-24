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


class IdentityEnroll(object):
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
        'status': 'str',
        'next': 'str',
        'actions': 'IdentityEnrollActions',
        'provider': 'str',
        'label': 'str',
        'provider_type': 'str',
        'user': 'str',
        'registered_by': 'str',
        'provider_data': 'object',
        'enroll_ticket': 'str',
        'created_by': 'str',
        'urlback': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'next': 'next',
        'actions': 'actions',
        'provider': 'provider',
        'label': 'label',
        'provider_type': 'provider_type',
        'user': 'user',
        'registered_by': 'registered_by',
        'provider_data': 'provider_data',
        'enroll_ticket': 'enroll_ticket',
        'created_by': 'created_by',
        'urlback': 'urlback'
    }

    def __init__(self, id=None, status=None, next=None, actions=None, provider=None, label=None, provider_type=None, user=None, registered_by=None, provider_data=None, enroll_ticket=None, created_by=None, urlback=None, local_vars_configuration=None):  # noqa: E501
        """IdentityEnroll - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._status = None
        self._next = None
        self._actions = None
        self._provider = None
        self._label = None
        self._provider_type = None
        self._user = None
        self._registered_by = None
        self._provider_data = None
        self._enroll_ticket = None
        self._created_by = None
        self._urlback = None
        self.discriminator = None

        if id is not None:
            self.id = id
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
        if provider_type is not None:
            self.provider_type = provider_type
        if user is not None:
            self.user = user
        if registered_by is not None:
            self.registered_by = registered_by
        if provider_data is not None:
            self.provider_data = provider_data
        if enroll_ticket is not None:
            self.enroll_ticket = enroll_ticket
        if created_by is not None:
            self.created_by = created_by
        if urlback is not None:
            self.urlback = urlback

    @property
    def id(self):
        """Gets the id of this IdentityEnroll.  # noqa: E501


        :return: The id of this IdentityEnroll.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IdentityEnroll.


        :param id: The id of this IdentityEnroll.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this IdentityEnroll.  # noqa: E501


        :return: The status of this IdentityEnroll.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IdentityEnroll.


        :param status: The status of this IdentityEnroll.  # noqa: E501
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
        """Gets the next of this IdentityEnroll.  # noqa: E501


        :return: The next of this IdentityEnroll.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this IdentityEnroll.


        :param next: The next of this IdentityEnroll.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def actions(self):
        """Gets the actions of this IdentityEnroll.  # noqa: E501


        :return: The actions of this IdentityEnroll.  # noqa: E501
        :rtype: IdentityEnrollActions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this IdentityEnroll.


        :param actions: The actions of this IdentityEnroll.  # noqa: E501
        :type: IdentityEnrollActions
        """

        self._actions = actions

    @property
    def provider(self):
        """Gets the provider of this IdentityEnroll.  # noqa: E501


        :return: The provider of this IdentityEnroll.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this IdentityEnroll.


        :param provider: The provider of this IdentityEnroll.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def label(self):
        """Gets the label of this IdentityEnroll.  # noqa: E501


        :return: The label of this IdentityEnroll.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this IdentityEnroll.


        :param label: The label of this IdentityEnroll.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def provider_type(self):
        """Gets the provider_type of this IdentityEnroll.  # noqa: E501


        :return: The provider_type of this IdentityEnroll.  # noqa: E501
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this IdentityEnroll.


        :param provider_type: The provider_type of this IdentityEnroll.  # noqa: E501
        :type: str
        """

        self._provider_type = provider_type

    @property
    def user(self):
        """Gets the user of this IdentityEnroll.  # noqa: E501


        :return: The user of this IdentityEnroll.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this IdentityEnroll.


        :param user: The user of this IdentityEnroll.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def registered_by(self):
        """Gets the registered_by of this IdentityEnroll.  # noqa: E501


        :return: The registered_by of this IdentityEnroll.  # noqa: E501
        :rtype: str
        """
        return self._registered_by

    @registered_by.setter
    def registered_by(self, registered_by):
        """Sets the registered_by of this IdentityEnroll.


        :param registered_by: The registered_by of this IdentityEnroll.  # noqa: E501
        :type: str
        """

        self._registered_by = registered_by

    @property
    def provider_data(self):
        """Gets the provider_data of this IdentityEnroll.  # noqa: E501

        Data of the provider that issued the certificate, it is variable from to provider to provider  # noqa: E501

        :return: The provider_data of this IdentityEnroll.  # noqa: E501
        :rtype: object
        """
        return self._provider_data

    @provider_data.setter
    def provider_data(self, provider_data):
        """Sets the provider_data of this IdentityEnroll.

        Data of the provider that issued the certificate, it is variable from to provider to provider  # noqa: E501

        :param provider_data: The provider_data of this IdentityEnroll.  # noqa: E501
        :type: object
        """

        self._provider_data = provider_data

    @property
    def enroll_ticket(self):
        """Gets the enroll_ticket of this IdentityEnroll.  # noqa: E501


        :return: The enroll_ticket of this IdentityEnroll.  # noqa: E501
        :rtype: str
        """
        return self._enroll_ticket

    @enroll_ticket.setter
    def enroll_ticket(self, enroll_ticket):
        """Sets the enroll_ticket of this IdentityEnroll.


        :param enroll_ticket: The enroll_ticket of this IdentityEnroll.  # noqa: E501
        :type: str
        """

        self._enroll_ticket = enroll_ticket

    @property
    def created_by(self):
        """Gets the created_by of this IdentityEnroll.  # noqa: E501


        :return: The created_by of this IdentityEnroll.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this IdentityEnroll.


        :param created_by: The created_by of this IdentityEnroll.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def urlback(self):
        """Gets the urlback of this IdentityEnroll.  # noqa: E501


        :return: The urlback of this IdentityEnroll.  # noqa: E501
        :rtype: str
        """
        return self._urlback

    @urlback.setter
    def urlback(self, urlback):
        """Sets the urlback of this IdentityEnroll.


        :param urlback: The urlback of this IdentityEnroll.  # noqa: E501
        :type: str
        """

        self._urlback = urlback

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
        if not isinstance(other, IdentityEnroll):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdentityEnroll):
            return True

        return self.to_dict() != other.to_dict()
