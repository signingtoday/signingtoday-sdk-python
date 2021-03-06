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


class InlineObject(object):
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
        'edu_person_principal_name': 'str',
        'is_member_of': 'list[str]',
        'given_name': 'str',
        'surname': 'str',
        'org_role': 'str'
    }

    attribute_map = {
        'edu_person_principal_name': 'eduPersonPrincipalName',
        'is_member_of': 'isMemberOf',
        'given_name': 'givenName',
        'surname': 'surname',
        'org_role': 'orgRole'
    }

    def __init__(self, edu_person_principal_name=None, is_member_of=None, given_name=None, surname=None, org_role=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._edu_person_principal_name = None
        self._is_member_of = None
        self._given_name = None
        self._surname = None
        self._org_role = None
        self.discriminator = None

        if edu_person_principal_name is not None:
            self.edu_person_principal_name = edu_person_principal_name
        if is_member_of is not None:
            self.is_member_of = is_member_of
        if given_name is not None:
            self.given_name = given_name
        if surname is not None:
            self.surname = surname
        if org_role is not None:
            self.org_role = org_role

    @property
    def edu_person_principal_name(self):
        """Gets the edu_person_principal_name of this InlineObject.  # noqa: E501

        The username of the account  # noqa: E501

        :return: The edu_person_principal_name of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._edu_person_principal_name

    @edu_person_principal_name.setter
    def edu_person_principal_name(self, edu_person_principal_name):
        """Sets the edu_person_principal_name of this InlineObject.

        The username of the account  # noqa: E501

        :param edu_person_principal_name: The edu_person_principal_name of this InlineObject.  # noqa: E501
        :type: str
        """

        self._edu_person_principal_name = edu_person_principal_name

    @property
    def is_member_of(self):
        """Gets the is_member_of of this InlineObject.  # noqa: E501

        Memberships of the user  # noqa: E501

        :return: The is_member_of of this InlineObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._is_member_of

    @is_member_of.setter
    def is_member_of(self, is_member_of):
        """Sets the is_member_of of this InlineObject.

        Memberships of the user  # noqa: E501

        :param is_member_of: The is_member_of of this InlineObject.  # noqa: E501
        :type: list[str]
        """

        self._is_member_of = is_member_of

    @property
    def given_name(self):
        """Gets the given_name of this InlineObject.  # noqa: E501

        First name of the user  # noqa: E501

        :return: The given_name of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this InlineObject.

        First name of the user  # noqa: E501

        :param given_name: The given_name of this InlineObject.  # noqa: E501
        :type: str
        """

        self._given_name = given_name

    @property
    def surname(self):
        """Gets the surname of this InlineObject.  # noqa: E501

        Last name of the user  # noqa: E501

        :return: The surname of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this InlineObject.

        Last name of the user  # noqa: E501

        :param surname: The surname of this InlineObject.  # noqa: E501
        :type: str
        """

        self._surname = surname

    @property
    def org_role(self):
        """Gets the org_role of this InlineObject.  # noqa: E501

        The role of the user in the organization  # noqa: E501

        :return: The org_role of this InlineObject.  # noqa: E501
        :rtype: str
        """
        return self._org_role

    @org_role.setter
    def org_role(self, org_role):
        """Sets the org_role of this InlineObject.

        The role of the user in the organization  # noqa: E501

        :param org_role: The org_role of this InlineObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["admin", "instructor", "signer"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and org_role not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `org_role` ({0}), must be one of {1}"  # noqa: E501
                .format(org_role, allowed_values)
            )

        self._org_role = org_role

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
        if not isinstance(other, InlineObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject):
            return True

        return self.to_dict() != other.to_dict()
