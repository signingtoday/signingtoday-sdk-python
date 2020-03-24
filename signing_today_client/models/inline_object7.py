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


class InlineObject7(object):
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
        'challenge': 'str',
        'device_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'challenge': 'challenge',
        'device_id': 'deviceId',
        'name': 'name'
    }

    def __init__(self, challenge=None, device_id=None, name=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject7 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._challenge = None
        self._device_id = None
        self._name = None
        self.discriminator = None

        if challenge is not None:
            self.challenge = challenge
        if device_id is not None:
            self.device_id = device_id
        if name is not None:
            self.name = name

    @property
    def challenge(self):
        """Gets the challenge of this InlineObject7.  # noqa: E501

        The challenge to be used to register the device  # noqa: E501

        :return: The challenge of this InlineObject7.  # noqa: E501
        :rtype: str
        """
        return self._challenge

    @challenge.setter
    def challenge(self, challenge):
        """Sets the challenge of this InlineObject7.

        The challenge to be used to register the device  # noqa: E501

        :param challenge: The challenge of this InlineObject7.  # noqa: E501
        :type: str
        """

        self._challenge = challenge

    @property
    def device_id(self):
        """Gets the device_id of this InlineObject7.  # noqa: E501

        The id of the device  # noqa: E501

        :return: The device_id of this InlineObject7.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this InlineObject7.

        The id of the device  # noqa: E501

        :param device_id: The device_id of this InlineObject7.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def name(self):
        """Gets the name of this InlineObject7.  # noqa: E501

        An arbitrary name to be assigned to the device  # noqa: E501

        :return: The name of this InlineObject7.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineObject7.

        An arbitrary name to be assigned to the device  # noqa: E501

        :param name: The name of this InlineObject7.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, InlineObject7):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject7):
            return True

        return self.to_dict() != other.to_dict()
