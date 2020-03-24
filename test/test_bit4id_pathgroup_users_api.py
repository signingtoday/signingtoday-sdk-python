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
from signing_today_client.api.bit4id_pathgroup_users_api import Bit4idPathgroupUsersApi  # noqa: E501
from signing_today_client.rest import ApiException


class TestBit4idPathgroupUsersApi(unittest.TestCase):
    """Bit4idPathgroupUsersApi unit test stubs"""

    def setUp(self):
        self.api = signing_today_client.api.bit4id_pathgroup_users_api.Bit4idPathgroupUsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_user_id_delete(self):
        """Test case for user_id_delete

        Enable or disable a User  # noqa: E501
        """
        pass

    def test_user_id_get(self):
        """Test case for user_id_get

        Retrieve a User  # noqa: E501
        """
        pass

    def test_user_id_identities_get(self):
        """Test case for user_id_identities_get

        Retrieve User identities  # noqa: E501
        """
        pass

    def test_user_id_put(self):
        """Test case for user_id_put

        Update a User  # noqa: E501
        """
        pass

    def test_user_id_role_put(self):
        """Test case for user_id_role_put

        Change the User role  # noqa: E501
        """
        pass

    def test_users_get(self):
        """Test case for users_get

        Retrieve Users  # noqa: E501
        """
        pass

    def test_users_groups_get(self):
        """Test case for users_groups_get

        Retrieve UserGroups  # noqa: E501
        """
        pass

    def test_users_groups_post(self):
        """Test case for users_groups_post

        Create a new UserGroups  # noqa: E501
        """
        pass

    def test_users_post(self):
        """Test case for users_post

        Create a new User  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
