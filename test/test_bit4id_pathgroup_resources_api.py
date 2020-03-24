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
from signing_today_client.api.bit4id_pathgroup_resources_api import Bit4idPathgroupResourcesApi  # noqa: E501
from signing_today_client.rest import ApiException


class TestBit4idPathgroupResourcesApi(unittest.TestCase):
    """Bit4idPathgroupResourcesApi unit test stubs"""

    def setUp(self):
        self.api = signing_today_client.api.bit4id_pathgroup_resources_api.Bit4idPathgroupResourcesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_d_st_id_resources_get(self):
        """Test case for d_st_id_resources_get

        Retrieve all resources associated to a DST  # noqa: E501
        """
        pass

    def test_d_st_id_resources_patch(self):
        """Test case for d_st_id_resources_patch

        Append a new resource to a DST  # noqa: E501
        """
        pass

    def test_d_st_resource_id_delete(self):
        """Test case for d_st_resource_id_delete

        Delete a Resource  # noqa: E501
        """
        pass

    def test_resource_id_get(self):
        """Test case for resource_id_get

        Retrieve a Resource  # noqa: E501
        """
        pass

    def test_resource_id_put(self):
        """Test case for resource_id_put

        Update a Resource  # noqa: E501
        """
        pass

    def test_user_id_identity_identity_id_appearance_delete(self):
        """Test case for user_id_identity_identity_id_appearance_delete

        Delete a user appearance resource.  # noqa: E501
        """
        pass

    def test_user_id_identity_identity_id_appearance_get(self):
        """Test case for user_id_identity_identity_id_appearance_get

        Download an identity appearance resource  # noqa: E501
        """
        pass

    def test_user_id_identity_identity_id_appearance_post(self):
        """Test case for user_id_identity_identity_id_appearance_post

        Add a graphical appearance to a user's identity  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
