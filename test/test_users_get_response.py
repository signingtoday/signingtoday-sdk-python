# coding: utf-8

"""
    Signing Today Web

    *Signing Today* is the perfect Digital Signature Gateway. Whenever in Your workflow You need to add one or more Digital Signatures to Your document, *Signing Today* is the right choice. You prepare Your documents, *Signing Today* takes care of all the rest: send invitations (`signature tickets`) to signers, collects their signatures, send You back the signed document. Integrating *Signing Today* in Your existing applications is very easy. Just follow these API specifications and get inspired by the many examples presented hereafter.   # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import signing_today_client
from signing_today_client.models.users_get_response import UsersGetResponse  # noqa: E501
from signing_today_client.rest import ApiException

class TestUsersGetResponse(unittest.TestCase):
    """UsersGetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UsersGetResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = signing_today_client.models.users_get_response.UsersGetResponse()  # noqa: E501
        if include_optional :
            return UsersGetResponse(
                count = 1, 
                values = [
                    signing_today_client.models.user.User(
                        id = 'e6419924-fd1d-4c42-9fa2-88023461f5df', 
                        username = 'jdo', 
                        domain = 'bit4id', 
                        language = 'en', 
                        name = 'John', 
                        surname = 'Doe', 
                        email = 'john.doe@email.com', 
                        phone = '+013392213450', 
                        role = 'signer', 
                        groups = [
                            signing_today_client.models.user_group.UserGroup(
                                id = 1, 
                                name = 'Marketing BU', 
                                domain = 'bit4id', )
                            ], 
                        capabilities = user.pwd.clear, 
                        created_by = '9a608f1a-e42a-4d05-8e2b-1df8ec63cd5d', 
                        created_at = '2007-04-02T19:30:10Z', 
                        deleted_at = '2007-04-02T19:30:10Z', 
                        automatic = False, 
                        extra_data = {"st_uuid":"d6ebb1ed-73a4-45ba-b33a-7db8a6cdd882"}, )
                    ]
            )
        else :
            return UsersGetResponse(
        )

    def testUsersGetResponse(self):
        """Test UsersGetResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()