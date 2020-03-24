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


class FillableForm(object):
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
        'instance_id': 'int',
        'id': 'int',
        'document_id': 'int',
        'type': 'str',
        'position_x': 'float',
        'position_y': 'float',
        'width': 'float',
        'height': 'float',
        'page': 'int',
        'signer_id': 'int',
        'to_fill': 'bool',
        'filled': 'bool',
        'invisible': 'bool',
        'extra_data': 'dict(str, object)'
    }

    attribute_map = {
        'instance_id': '_instance_id',
        'id': 'id',
        'document_id': 'documentId',
        'type': 'type',
        'position_x': 'positionX',
        'position_y': 'positionY',
        'width': 'width',
        'height': 'height',
        'page': 'page',
        'signer_id': 'signerId',
        'to_fill': 'toFill',
        'filled': 'filled',
        'invisible': 'invisible',
        'extra_data': 'extraData'
    }

    def __init__(self, instance_id=None, id=None, document_id=None, type=None, position_x=None, position_y=None, width=None, height=None, page=None, signer_id=None, to_fill=None, filled=None, invisible=None, extra_data=None, local_vars_configuration=None):  # noqa: E501
        """FillableForm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._instance_id = None
        self._id = None
        self._document_id = None
        self._type = None
        self._position_x = None
        self._position_y = None
        self._width = None
        self._height = None
        self._page = None
        self._signer_id = None
        self._to_fill = None
        self._filled = None
        self._invisible = None
        self._extra_data = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if id is not None:
            self.id = id
        if document_id is not None:
            self.document_id = document_id
        if type is not None:
            self.type = type
        if position_x is not None:
            self.position_x = position_x
        if position_y is not None:
            self.position_y = position_y
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if page is not None:
            self.page = page
        if signer_id is not None:
            self.signer_id = signer_id
        if to_fill is not None:
            self.to_fill = to_fill
        if filled is not None:
            self.filled = filled
        if invisible is not None:
            self.invisible = invisible
        if extra_data is not None:
            self.extra_data = extra_data

    @property
    def instance_id(self):
        """Gets the instance_id of this FillableForm.  # noqa: E501

        It is a reference for internal use  # noqa: E501

        :return: The instance_id of this FillableForm.  # noqa: E501
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this FillableForm.

        It is a reference for internal use  # noqa: E501

        :param instance_id: The instance_id of this FillableForm.  # noqa: E501
        :type: int
        """

        self._instance_id = instance_id

    @property
    def id(self):
        """Gets the id of this FillableForm.  # noqa: E501

        Id of the _form_  # noqa: E501

        :return: The id of this FillableForm.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FillableForm.

        Id of the _form_  # noqa: E501

        :param id: The id of this FillableForm.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def document_id(self):
        """Gets the document_id of this FillableForm.  # noqa: E501

        Id of the document  # noqa: E501

        :return: The document_id of this FillableForm.  # noqa: E501
        :rtype: int
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this FillableForm.

        Id of the document  # noqa: E501

        :param document_id: The document_id of this FillableForm.  # noqa: E501
        :type: int
        """

        self._document_id = document_id

    @property
    def type(self):
        """Gets the type of this FillableForm.  # noqa: E501

        Type of the fill form  # noqa: E501

        :return: The type of this FillableForm.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FillableForm.

        Type of the fill form  # noqa: E501

        :param type: The type of this FillableForm.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def position_x(self):
        """Gets the position_x of this FillableForm.  # noqa: E501

        Position onto the X axis of the form, expressed in percentage  # noqa: E501

        :return: The position_x of this FillableForm.  # noqa: E501
        :rtype: float
        """
        return self._position_x

    @position_x.setter
    def position_x(self, position_x):
        """Sets the position_x of this FillableForm.

        Position onto the X axis of the form, expressed in percentage  # noqa: E501

        :param position_x: The position_x of this FillableForm.  # noqa: E501
        :type: float
        """

        self._position_x = position_x

    @property
    def position_y(self):
        """Gets the position_y of this FillableForm.  # noqa: E501

        Position onto the Y axis of the form, expressed in percentage  # noqa: E501

        :return: The position_y of this FillableForm.  # noqa: E501
        :rtype: float
        """
        return self._position_y

    @position_y.setter
    def position_y(self, position_y):
        """Sets the position_y of this FillableForm.

        Position onto the Y axis of the form, expressed in percentage  # noqa: E501

        :param position_y: The position_y of this FillableForm.  # noqa: E501
        :type: float
        """

        self._position_y = position_y

    @property
    def width(self):
        """Gets the width of this FillableForm.  # noqa: E501

        Width of the form expressed in percentage  # noqa: E501

        :return: The width of this FillableForm.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this FillableForm.

        Width of the form expressed in percentage  # noqa: E501

        :param width: The width of this FillableForm.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this FillableForm.  # noqa: E501

        Height of the form expressed in percentage  # noqa: E501

        :return: The height of this FillableForm.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this FillableForm.

        Height of the form expressed in percentage  # noqa: E501

        :param height: The height of this FillableForm.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def page(self):
        """Gets the page of this FillableForm.  # noqa: E501

        Page of the document where the form is  # noqa: E501

        :return: The page of this FillableForm.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this FillableForm.

        Page of the document where the form is  # noqa: E501

        :param page: The page of this FillableForm.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def signer_id(self):
        """Gets the signer_id of this FillableForm.  # noqa: E501

        Id of the signer in the sign plan  # noqa: E501

        :return: The signer_id of this FillableForm.  # noqa: E501
        :rtype: int
        """
        return self._signer_id

    @signer_id.setter
    def signer_id(self, signer_id):
        """Sets the signer_id of this FillableForm.

        Id of the signer in the sign plan  # noqa: E501

        :param signer_id: The signer_id of this FillableForm.  # noqa: E501
        :type: int
        """

        self._signer_id = signer_id

    @property
    def to_fill(self):
        """Gets the to_fill of this FillableForm.  # noqa: E501

        **True** if the field need to be filled by the user. In case of a Signature it is **false**   # noqa: E501

        :return: The to_fill of this FillableForm.  # noqa: E501
        :rtype: bool
        """
        return self._to_fill

    @to_fill.setter
    def to_fill(self, to_fill):
        """Sets the to_fill of this FillableForm.

        **True** if the field need to be filled by the user. In case of a Signature it is **false**   # noqa: E501

        :param to_fill: The to_fill of this FillableForm.  # noqa: E501
        :type: bool
        """

        self._to_fill = to_fill

    @property
    def filled(self):
        """Gets the filled of this FillableForm.  # noqa: E501

        True ones the form has been filled  # noqa: E501

        :return: The filled of this FillableForm.  # noqa: E501
        :rtype: bool
        """
        return self._filled

    @filled.setter
    def filled(self, filled):
        """Sets the filled of this FillableForm.

        True ones the form has been filled  # noqa: E501

        :param filled: The filled of this FillableForm.  # noqa: E501
        :type: bool
        """

        self._filled = filled

    @property
    def invisible(self):
        """Gets the invisible of this FillableForm.  # noqa: E501

        True if the appearance has to be hidden  # noqa: E501

        :return: The invisible of this FillableForm.  # noqa: E501
        :rtype: bool
        """
        return self._invisible

    @invisible.setter
    def invisible(self, invisible):
        """Sets the invisible of this FillableForm.

        True if the appearance has to be hidden  # noqa: E501

        :param invisible: The invisible of this FillableForm.  # noqa: E501
        :type: bool
        """

        self._invisible = invisible

    @property
    def extra_data(self):
        """Gets the extra_data of this FillableForm.  # noqa: E501

        Extra information about the form  # noqa: E501

        :return: The extra_data of this FillableForm.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._extra_data

    @extra_data.setter
    def extra_data(self, extra_data):
        """Sets the extra_data of this FillableForm.

        Extra information about the form  # noqa: E501

        :param extra_data: The extra_data of this FillableForm.  # noqa: E501
        :type: dict(str, object)
        """

        self._extra_data = extra_data

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
        if not isinstance(other, FillableForm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FillableForm):
            return True

        return self.to_dict() != other.to_dict()