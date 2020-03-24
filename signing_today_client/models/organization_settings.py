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


class OrganizationSettings(object):
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
        'default_dst_expire_days': 'int',
        'default_language': 'str',
        'alfresco_properties': 'OrganizationSettingsAlfrescoProperties'
    }

    attribute_map = {
        'default_dst_expire_days': 'defaultDSTExpire_days',
        'default_language': 'defaultLanguage',
        'alfresco_properties': 'alfrescoProperties'
    }

    def __init__(self, default_dst_expire_days=30, default_language=None, alfresco_properties=None, local_vars_configuration=None):  # noqa: E501
        """OrganizationSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._default_dst_expire_days = None
        self._default_language = None
        self._alfresco_properties = None
        self.discriminator = None

        if default_dst_expire_days is not None:
            self.default_dst_expire_days = default_dst_expire_days
        if default_language is not None:
            self.default_language = default_language
        if alfresco_properties is not None:
            self.alfresco_properties = alfresco_properties

    @property
    def default_dst_expire_days(self):
        """Gets the default_dst_expire_days of this OrganizationSettings.  # noqa: E501


        :return: The default_dst_expire_days of this OrganizationSettings.  # noqa: E501
        :rtype: int
        """
        return self._default_dst_expire_days

    @default_dst_expire_days.setter
    def default_dst_expire_days(self, default_dst_expire_days):
        """Sets the default_dst_expire_days of this OrganizationSettings.


        :param default_dst_expire_days: The default_dst_expire_days of this OrganizationSettings.  # noqa: E501
        :type: int
        """

        self._default_dst_expire_days = default_dst_expire_days

    @property
    def default_language(self):
        """Gets the default_language of this OrganizationSettings.  # noqa: E501


        :return: The default_language of this OrganizationSettings.  # noqa: E501
        :rtype: str
        """
        return self._default_language

    @default_language.setter
    def default_language(self, default_language):
        """Sets the default_language of this OrganizationSettings.


        :param default_language: The default_language of this OrganizationSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["it", "en", "es", "fr"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and default_language not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `default_language` ({0}), must be one of {1}"  # noqa: E501
                .format(default_language, allowed_values)
            )

        self._default_language = default_language

    @property
    def alfresco_properties(self):
        """Gets the alfresco_properties of this OrganizationSettings.  # noqa: E501


        :return: The alfresco_properties of this OrganizationSettings.  # noqa: E501
        :rtype: OrganizationSettingsAlfrescoProperties
        """
        return self._alfresco_properties

    @alfresco_properties.setter
    def alfresco_properties(self, alfresco_properties):
        """Sets the alfresco_properties of this OrganizationSettings.


        :param alfresco_properties: The alfresco_properties of this OrganizationSettings.  # noqa: E501
        :type: OrganizationSettingsAlfrescoProperties
        """

        self._alfresco_properties = alfresco_properties

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
        if not isinstance(other, OrganizationSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationSettings):
            return True

        return self.to_dict() != other.to_dict()
