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


class DSTStatusChangedNotification(object):
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
        'status': 'str',
        'dst': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'status': 'status',
        'dst': 'dst',
        'reason': 'reason'
    }

    def __init__(self, status=None, dst=None, reason=None, local_vars_configuration=None):  # noqa: E501
        """DSTStatusChangedNotification - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._dst = None
        self._reason = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if dst is not None:
            self.dst = dst
        if reason is not None:
            self.reason = reason

    @property
    def status(self):
        """Gets the status of this DSTStatusChangedNotification.  # noqa: E501


        :return: The status of this DSTStatusChangedNotification.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DSTStatusChangedNotification.


        :param status: The status of this DSTStatusChangedNotification.  # noqa: E501
        :type: str
        """
        allowed_values = ["toFill", "toSign", "expired", "performed", "error"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def dst(self):
        """Gets the dst of this DSTStatusChangedNotification.  # noqa: E501


        :return: The dst of this DSTStatusChangedNotification.  # noqa: E501
        :rtype: str
        """
        return self._dst

    @dst.setter
    def dst(self, dst):
        """Sets the dst of this DSTStatusChangedNotification.


        :param dst: The dst of this DSTStatusChangedNotification.  # noqa: E501
        :type: str
        """

        self._dst = dst

    @property
    def reason(self):
        """Gets the reason of this DSTStatusChangedNotification.  # noqa: E501


        :return: The reason of this DSTStatusChangedNotification.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this DSTStatusChangedNotification.


        :param reason: The reason of this DSTStatusChangedNotification.  # noqa: E501
        :type: str
        """

        self._reason = reason

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
        if not isinstance(other, DSTStatusChangedNotification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DSTStatusChangedNotification):
            return True

        return self.to_dict() != other.to_dict()
