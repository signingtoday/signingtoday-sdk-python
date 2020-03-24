# coding: utf-8

"""
    Signing Today Web

    *Signing Today* is the perfect Digital Signature Gateway. Whenever in Your workflow You need to add one or more Digital Signatures to Your document, *Signing Today* is the right choice. You prepare Your documents, *Signing Today* takes care of all the rest: send invitations (`signature tickets`) to signers, collects their signatures, send You back the signed document. Integrating *Signing Today* in Your existing applications is very easy. Just follow these API specifications and get inspired by the many examples presented hereafter.   # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from signing_today_client.configuration import Configuration


class RobotConfigurationAuthentication(object):
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
        'username': 'str',
        'password': 'str',
        'auth_mode': 'str',
        'client_key': 'str',
        'client_cert': 'str'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'auth_mode': 'authMode',
        'client_key': 'clientKey',
        'client_cert': 'clientCert'
    }

    def __init__(self, username=None, password=None, auth_mode=None, client_key=None, client_cert=None, local_vars_configuration=None):  # noqa: E501
        """RobotConfigurationAuthentication - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._username = None
        self._password = None
        self._auth_mode = None
        self._client_key = None
        self._client_cert = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if auth_mode is not None:
            self.auth_mode = auth_mode
        if client_key is not None:
            self.client_key = client_key
        if client_cert is not None:
            self.client_cert = client_cert

    @property
    def username(self):
        """Gets the username of this RobotConfigurationAuthentication.  # noqa: E501

        The username for the authentication  # noqa: E501

        :return: The username of this RobotConfigurationAuthentication.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this RobotConfigurationAuthentication.

        The username for the authentication  # noqa: E501

        :param username: The username of this RobotConfigurationAuthentication.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this RobotConfigurationAuthentication.  # noqa: E501

        The password for the authentication  # noqa: E501

        :return: The password of this RobotConfigurationAuthentication.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RobotConfigurationAuthentication.

        The password for the authentication  # noqa: E501

        :param password: The password of this RobotConfigurationAuthentication.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def auth_mode(self):
        """Gets the auth_mode of this RobotConfigurationAuthentication.  # noqa: E501

        The type of authentication  # noqa: E501

        :return: The auth_mode of this RobotConfigurationAuthentication.  # noqa: E501
        :rtype: str
        """
        return self._auth_mode

    @auth_mode.setter
    def auth_mode(self, auth_mode):
        """Sets the auth_mode of this RobotConfigurationAuthentication.

        The type of authentication  # noqa: E501

        :param auth_mode: The auth_mode of this RobotConfigurationAuthentication.  # noqa: E501
        :type: str
        """
        allowed_values = ["basic", "digest"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and auth_mode not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `auth_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(auth_mode, allowed_values)
            )

        self._auth_mode = auth_mode

    @property
    def client_key(self):
        """Gets the client_key of this RobotConfigurationAuthentication.  # noqa: E501

        Client key  # noqa: E501

        :return: The client_key of this RobotConfigurationAuthentication.  # noqa: E501
        :rtype: str
        """
        return self._client_key

    @client_key.setter
    def client_key(self, client_key):
        """Sets the client_key of this RobotConfigurationAuthentication.

        Client key  # noqa: E501

        :param client_key: The client_key of this RobotConfigurationAuthentication.  # noqa: E501
        :type: str
        """

        self._client_key = client_key

    @property
    def client_cert(self):
        """Gets the client_cert of this RobotConfigurationAuthentication.  # noqa: E501

        Client certificate  # noqa: E501

        :return: The client_cert of this RobotConfigurationAuthentication.  # noqa: E501
        :rtype: str
        """
        return self._client_cert

    @client_cert.setter
    def client_cert(self, client_cert):
        """Sets the client_cert of this RobotConfigurationAuthentication.

        Client certificate  # noqa: E501

        :param client_cert: The client_cert of this RobotConfigurationAuthentication.  # noqa: E501
        :type: str
        """

        self._client_cert = client_cert

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
        if not isinstance(other, RobotConfigurationAuthentication):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RobotConfigurationAuthentication):
            return True

        return self.to_dict() != other.to_dict()