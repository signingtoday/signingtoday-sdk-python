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


class LFResource(object):
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
        'domain': 'str',
        'type': 'str',
        'dst_uuid': 'str',
        'title': 'str',
        'filename': 'str',
        'url': 'str',
        'size': 'int',
        'created_at': 'datetime',
        'mimetype': 'str',
        'pages': 'int',
        'extra_data': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'domain': 'domain',
        'type': 'type',
        'dst_uuid': 'dstUuid',
        'title': 'title',
        'filename': 'filename',
        'url': 'url',
        'size': 'size',
        'created_at': 'createdAt',
        'mimetype': 'mimetype',
        'pages': 'pages',
        'extra_data': 'extraData'
    }

    def __init__(self, id=None, domain=None, type=None, dst_uuid=None, title=None, filename=None, url=None, size=None, created_at=None, mimetype=None, pages=None, extra_data=None, local_vars_configuration=None):  # noqa: E501
        """LFResource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._domain = None
        self._type = None
        self._dst_uuid = None
        self._title = None
        self._filename = None
        self._url = None
        self._size = None
        self._created_at = None
        self._mimetype = None
        self._pages = None
        self._extra_data = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain is not None:
            self.domain = domain
        if type is not None:
            self.type = type
        if dst_uuid is not None:
            self.dst_uuid = dst_uuid
        if title is not None:
            self.title = title
        if filename is not None:
            self.filename = filename
        if url is not None:
            self.url = url
        if size is not None:
            self.size = size
        if created_at is not None:
            self.created_at = created_at
        if mimetype is not None:
            self.mimetype = mimetype
        if pages is not None:
            self.pages = pages
        if extra_data is not None:
            self.extra_data = extra_data

    @property
    def id(self):
        """Gets the id of this LFResource.  # noqa: E501

        Unique id of the resource  # noqa: E501

        :return: The id of this LFResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LFResource.

        Unique id of the resource  # noqa: E501

        :param id: The id of this LFResource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def domain(self):
        """Gets the domain of this LFResource.  # noqa: E501

        The _domain_ is the Organization which a user or a DST belongs  # noqa: E501

        :return: The domain of this LFResource.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this LFResource.

        The _domain_ is the Organization which a user or a DST belongs  # noqa: E501

        :param domain: The domain of this LFResource.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def type(self):
        """Gets the type of this LFResource.  # noqa: E501

        Type of the resource, for example a _PDFResource_  # noqa: E501

        :return: The type of this LFResource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LFResource.

        Type of the resource, for example a _PDFResource_  # noqa: E501

        :param type: The type of this LFResource.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def dst_uuid(self):
        """Gets the dst_uuid of this LFResource.  # noqa: E501

        Unique id of the _DST_ which the resource is correlated  # noqa: E501

        :return: The dst_uuid of this LFResource.  # noqa: E501
        :rtype: str
        """
        return self._dst_uuid

    @dst_uuid.setter
    def dst_uuid(self, dst_uuid):
        """Sets the dst_uuid of this LFResource.

        Unique id of the _DST_ which the resource is correlated  # noqa: E501

        :param dst_uuid: The dst_uuid of this LFResource.  # noqa: E501
        :type: str
        """

        self._dst_uuid = dst_uuid

    @property
    def title(self):
        """Gets the title of this LFResource.  # noqa: E501

        Title of the resource  # noqa: E501

        :return: The title of this LFResource.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LFResource.

        Title of the resource  # noqa: E501

        :param title: The title of this LFResource.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def filename(self):
        """Gets the filename of this LFResource.  # noqa: E501

        Name of the file uploaded, with its extension as well  # noqa: E501

        :return: The filename of this LFResource.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this LFResource.

        Name of the file uploaded, with its extension as well  # noqa: E501

        :param filename: The filename of this LFResource.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def url(self):
        """Gets the url of this LFResource.  # noqa: E501

        Url of the resource  # noqa: E501

        :return: The url of this LFResource.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this LFResource.

        Url of the resource  # noqa: E501

        :param url: The url of this LFResource.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def size(self):
        """Gets the size of this LFResource.  # noqa: E501

        Size of the resource  # noqa: E501

        :return: The size of this LFResource.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this LFResource.

        Size of the resource  # noqa: E501

        :param size: The size of this LFResource.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def created_at(self):
        """Gets the created_at of this LFResource.  # noqa: E501

        Indicates when the resource has been uploaded  # noqa: E501

        :return: The created_at of this LFResource.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this LFResource.

        Indicates when the resource has been uploaded  # noqa: E501

        :param created_at: The created_at of this LFResource.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def mimetype(self):
        """Gets the mimetype of this LFResource.  # noqa: E501

        _MIME_ type of the resource  # noqa: E501

        :return: The mimetype of this LFResource.  # noqa: E501
        :rtype: str
        """
        return self._mimetype

    @mimetype.setter
    def mimetype(self, mimetype):
        """Sets the mimetype of this LFResource.

        _MIME_ type of the resource  # noqa: E501

        :param mimetype: The mimetype of this LFResource.  # noqa: E501
        :type: str
        """

        self._mimetype = mimetype

    @property
    def pages(self):
        """Gets the pages of this LFResource.  # noqa: E501

        Indicates how many pages the resource is  # noqa: E501

        :return: The pages of this LFResource.  # noqa: E501
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this LFResource.

        Indicates how many pages the resource is  # noqa: E501

        :param pages: The pages of this LFResource.  # noqa: E501
        :type: int
        """

        self._pages = pages

    @property
    def extra_data(self):
        """Gets the extra_data of this LFResource.  # noqa: E501

        Extra data of the resource  # noqa: E501

        :return: The extra_data of this LFResource.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._extra_data

    @extra_data.setter
    def extra_data(self, extra_data):
        """Sets the extra_data of this LFResource.

        Extra data of the resource  # noqa: E501

        :param extra_data: The extra_data of this LFResource.  # noqa: E501
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
        if not isinstance(other, LFResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LFResource):
            return True

        return self.to_dict() != other.to_dict()
