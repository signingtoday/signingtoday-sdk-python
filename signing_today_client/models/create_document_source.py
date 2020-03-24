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


class CreateDocumentSource(object):
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
        'type': 'str',
        'embedded_data': 'file',
        'source_url': 'str'
    }

    attribute_map = {
        'type': 'type',
        'embedded_data': 'embeddedData',
        'source_url': 'sourceURL'
    }

    def __init__(self, type=None, embedded_data=None, source_url=None, local_vars_configuration=None):  # noqa: E501
        """CreateDocumentSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._embedded_data = None
        self._source_url = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if embedded_data is not None:
            self.embedded_data = embedded_data
        if source_url is not None:
            self.source_url = source_url

    @property
    def type(self):
        """Gets the type of this CreateDocumentSource.  # noqa: E501


        :return: The type of this CreateDocumentSource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateDocumentSource.


        :param type: The type of this CreateDocumentSource.  # noqa: E501
        :type: str
        """
        allowed_values = ["Embedded", "URL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def embedded_data(self):
        """Gets the embedded_data of this CreateDocumentSource.  # noqa: E501


        :return: The embedded_data of this CreateDocumentSource.  # noqa: E501
        :rtype: file
        """
        return self._embedded_data

    @embedded_data.setter
    def embedded_data(self, embedded_data):
        """Sets the embedded_data of this CreateDocumentSource.


        :param embedded_data: The embedded_data of this CreateDocumentSource.  # noqa: E501
        :type: file
        """

        self._embedded_data = embedded_data

    @property
    def source_url(self):
        """Gets the source_url of this CreateDocumentSource.  # noqa: E501


        :return: The source_url of this CreateDocumentSource.  # noqa: E501
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        """Sets the source_url of this CreateDocumentSource.


        :param source_url: The source_url of this CreateDocumentSource.  # noqa: E501
        :type: str
        """

        self._source_url = source_url

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
        if not isinstance(other, CreateDocumentSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDocumentSource):
            return True

        return self.to_dict() != other.to_dict()
