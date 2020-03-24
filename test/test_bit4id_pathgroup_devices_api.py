# coding: utf-8

"""
    Signing Today Web

    *Signing Today* is the perfect Digital Signature Gateway. Whenever in Your workflow You need to add one or more Digital Signatures to Your document, *Signing Today* is the right choice. You prepare Your documents, *Signing Today* takes care of all the rest: send invitations (`signature tickets`) to signers, collects their signatures, send You back the signed document. Integrating *Signing Today* in Your existing applications is very easy. Just follow these API specifications and get inspired by the many examples presented hereafter.   # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import signing_today_client
from signing_today_client.api.bit4id_pathgroup_devices_api import Bit4idPathgroupDevicesApi  # noqa: E501
from signing_today_client.rest import ApiException


class TestBit4idPathgroupDevicesApi(unittest.TestCase):
    """Bit4idPathgroupDevicesApi unit test stubs"""

    def setUp(self):
        self.api = signing_today_client.api.bit4id_pathgroup_devices_api.Bit4idPathgroupDevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_device_authorization_delete(self):
        """Test case for device_authorization_delete

        Clear a trusted device  # noqa: E501
        """
        pass

    def test_device_authorization_get(self):
        """Test case for device_authorization_get

        Retrieve a challenge for authorizing a new trusted device  # noqa: E501
        """
        pass

    def test_device_authorization_post(self):
        """Test case for device_authorization_post

        Register a new trusted device  # noqa: E501
        """
        pass

    def test_devices_get(self):
        """Test case for devices_get

        Get the list of trusted devices  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
