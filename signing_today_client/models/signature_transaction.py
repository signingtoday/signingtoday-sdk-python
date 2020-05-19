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


class SignatureTransaction(object):
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
        'documents': 'list[Document]',
        'archived': 'bool',
        'created_by': 'str',
        'status': 'str',
        'created': 'str',
        'reason': 'str',
        'title': 'str',
        'not_after': 'str',
        'urlback': 'str',
        'cancelback': 'str',
        'template_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'documents': 'documents',
        'archived': 'archived',
        'created_by': 'created_by',
        'status': 'status',
        'created': 'created',
        'reason': 'reason',
        'title': 'title',
        'not_after': 'not_after',
        'urlback': 'urlback',
        'cancelback': 'cancelback',
        'template_name': 'template_name'
    }

    def __init__(self, id=None, documents=None, archived=False, created_by=None, status=None, created=None, reason=None, title=None, not_after=None, urlback=None, cancelback=None, template_name=None, local_vars_configuration=None):  # noqa: E501
        """SignatureTransaction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._documents = None
        self._archived = None
        self._created_by = None
        self._status = None
        self._created = None
        self._reason = None
        self._title = None
        self._not_after = None
        self._urlback = None
        self._cancelback = None
        self._template_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if documents is not None:
            self.documents = documents
        if archived is not None:
            self.archived = archived
        if created_by is not None:
            self.created_by = created_by
        if status is not None:
            self.status = status
        if created is not None:
            self.created = created
        if reason is not None:
            self.reason = reason
        if title is not None:
            self.title = title
        if not_after is not None:
            self.not_after = not_after
        if urlback is not None:
            self.urlback = urlback
        if cancelback is not None:
            self.cancelback = cancelback
        if template_name is not None:
            self.template_name = template_name

    @property
    def id(self):
        """Gets the id of this SignatureTransaction.  # noqa: E501

        The uuid code that identifies the Digital Signature Transaction  # noqa: E501

        :return: The id of this SignatureTransaction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SignatureTransaction.

        The uuid code that identifies the Digital Signature Transaction  # noqa: E501

        :param id: The id of this SignatureTransaction.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def documents(self):
        """Gets the documents of this SignatureTransaction.  # noqa: E501

        The _documents_ field is an array containing document objects, where everyone of them is defined as follows   # noqa: E501

        :return: The documents of this SignatureTransaction.  # noqa: E501
        :rtype: list[Document]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this SignatureTransaction.

        The _documents_ field is an array containing document objects, where everyone of them is defined as follows   # noqa: E501

        :param documents: The documents of this SignatureTransaction.  # noqa: E501
        :type: list[Document]
        """

        self._documents = documents

    @property
    def archived(self):
        """Gets the archived of this SignatureTransaction.  # noqa: E501

        True if the DST's resources has been deleted  # noqa: E501

        :return: The archived of this SignatureTransaction.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this SignatureTransaction.

        True if the DST's resources has been deleted  # noqa: E501

        :param archived: The archived of this SignatureTransaction.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def created_by(self):
        """Gets the created_by of this SignatureTransaction.  # noqa: E501

        The user created the Digital Signature Transaction  # noqa: E501

        :return: The created_by of this SignatureTransaction.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this SignatureTransaction.

        The user created the Digital Signature Transaction  # noqa: E501

        :param created_by: The created_by of this SignatureTransaction.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def status(self):
        """Gets the status of this SignatureTransaction.  # noqa: E501

        The Digital Signature Transaction may have the following statuses:   - `waiting`: Not all the documents has ben uploaded and validated yet   - `pending`: The DST is ready to be signed   - `performed`: The DST has been signed by all the signers   - `expired`: The DST expired before all the signers have signed it   - `cancelled`: The DST has been canceled; the motivation is in the reason   # noqa: E501

        :return: The status of this SignatureTransaction.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SignatureTransaction.

        The Digital Signature Transaction may have the following statuses:   - `waiting`: Not all the documents has ben uploaded and validated yet   - `pending`: The DST is ready to be signed   - `performed`: The DST has been signed by all the signers   - `expired`: The DST expired before all the signers have signed it   - `cancelled`: The DST has been canceled; the motivation is in the reason   # noqa: E501

        :param status: The status of this SignatureTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["waiting", "pending", "performed", "expired", "cancelled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created(self):
        """Gets the created of this SignatureTransaction.  # noqa: E501

        Date of creation of the Digital Signature Transaction  # noqa: E501

        :return: The created of this SignatureTransaction.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SignatureTransaction.

        Date of creation of the Digital Signature Transaction  # noqa: E501

        :param created: The created of this SignatureTransaction.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def reason(self):
        """Gets the reason of this SignatureTransaction.  # noqa: E501

        The motivations for the cancellation may be:   - `CANNOT_DOWNLOAD_DOCUMENT`: Signing Today could not download the     document   - `INVALID_DOCUMENT`: The downloaded document is not valid   - `PROTECTED_DOCUMENT`: The document is protected by password   - `declined`: One of the documents has been refused   - `MOTIVAZIONE_ESPLICITA`: Rejected from the system with a custom     reason   # noqa: E501

        :return: The reason of this SignatureTransaction.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this SignatureTransaction.

        The motivations for the cancellation may be:   - `CANNOT_DOWNLOAD_DOCUMENT`: Signing Today could not download the     document   - `INVALID_DOCUMENT`: The downloaded document is not valid   - `PROTECTED_DOCUMENT`: The document is protected by password   - `declined`: One of the documents has been refused   - `MOTIVAZIONE_ESPLICITA`: Rejected from the system with a custom     reason   # noqa: E501

        :param reason: The reason of this SignatureTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["CANNOT_DOWNLOAD_DOCUMENT", "INVALID_DOCUMENT", "PROTECTED_DOCUMENT", "declined", "MOTIVAZIONE_ESPLICITA"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and reason not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reason, allowed_values)
            )

        self._reason = reason

    @property
    def title(self):
        """Gets the title of this SignatureTransaction.  # noqa: E501

        Title of the Digital Signature Transaction  # noqa: E501

        :return: The title of this SignatureTransaction.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SignatureTransaction.

        Title of the Digital Signature Transaction  # noqa: E501

        :param title: The title of this SignatureTransaction.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def not_after(self):
        """Gets the not_after of this SignatureTransaction.  # noqa: E501

        Deadline of the Digital Signature Transaction, expressed in ISO format  # noqa: E501

        :return: The not_after of this SignatureTransaction.  # noqa: E501
        :rtype: str
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this SignatureTransaction.

        Deadline of the Digital Signature Transaction, expressed in ISO format  # noqa: E501

        :param not_after: The not_after of this SignatureTransaction.  # noqa: E501
        :type: str
        """

        self._not_after = not_after

    @property
    def urlback(self):
        """Gets the urlback of this SignatureTransaction.  # noqa: E501

        The url for the redirection from signature tray when the Digital Signature Transaction is completed or refused  # noqa: E501

        :return: The urlback of this SignatureTransaction.  # noqa: E501
        :rtype: str
        """
        return self._urlback

    @urlback.setter
    def urlback(self, urlback):
        """Sets the urlback of this SignatureTransaction.

        The url for the redirection from signature tray when the Digital Signature Transaction is completed or refused  # noqa: E501

        :param urlback: The urlback of this SignatureTransaction.  # noqa: E501
        :type: str
        """

        self._urlback = urlback

    @property
    def cancelback(self):
        """Gets the cancelback of this SignatureTransaction.  # noqa: E501

        If set, in the signature tray will be displayed a button that needs to go back to a third part application  # noqa: E501

        :return: The cancelback of this SignatureTransaction.  # noqa: E501
        :rtype: str
        """
        return self._cancelback

    @cancelback.setter
    def cancelback(self, cancelback):
        """Sets the cancelback of this SignatureTransaction.

        If set, in the signature tray will be displayed a button that needs to go back to a third part application  # noqa: E501

        :param cancelback: The cancelback of this SignatureTransaction.  # noqa: E501
        :type: str
        """

        self._cancelback = cancelback

    @property
    def template_name(self):
        """Gets the template_name of this SignatureTransaction.  # noqa: E501

        A label to indicate the template used to create the Digital Signature Transaction  # noqa: E501

        :return: The template_name of this SignatureTransaction.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this SignatureTransaction.

        A label to indicate the template used to create the Digital Signature Transaction  # noqa: E501

        :param template_name: The template_name of this SignatureTransaction.  # noqa: E501
        :type: str
        """

        self._template_name = template_name

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
        if not isinstance(other, SignatureTransaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignatureTransaction):
            return True

        return self.to_dict() != other.to_dict()
