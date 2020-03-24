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
from signing_today_client.models.organization import Organization  # noqa: E501
from signing_today_client.rest import ApiException

class TestOrganization(unittest.TestCase):
    """Organization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Organization
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = signing_today_client.models.organization.Organization()  # noqa: E501
        if include_optional :
            return Organization(
                id = '0', 
                email_override_folder_path = '0', 
                name = '0', 
                contact_email = '0', 
                contact_phone = '0', 
                nation = '0', 
                city = '0', 
                deleted_at = '2007-04-02T19:30:10Z', 
                private_settings = signing_today_client.models.organization_private_settings.OrganizationPrivateSettings(
                    tags = ["important","urgent"], ), 
                public_settings = signing_today_client.models.organization_public_settings.OrganizationPublicSettings(
                    logo_path = '0', ), 
                settings = signing_today_client.models.organization_settings.OrganizationSettings(
                    default_dst_expire_days = 30, 
                    default_language = 'it', 
                    alfresco_properties = signing_today_client.models.organization_settings_alfresco_properties.OrganizationSettings_alfrescoProperties(
                        enabled = True, 
                        type = 'rest', 
                        username = '0', 
                        password = '0', 
                        base_path = '0', 
                        relative_path = '0', 
                        base_node_id = '0', ), )
            )
        else :
            return Organization(
        )

    def testOrganization(self):
        """Test Organization"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
