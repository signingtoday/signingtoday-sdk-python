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
from signing_today_client.models.identity import Identity  # noqa: E501
from signing_today_client.rest import ApiException

class TestIdentity(unittest.TestCase):
    """Identity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Identity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = signing_today_client.models.identity.Identity()  # noqa: E501
        if include_optional :
            return Identity(
                id = 'abd562ae-e8ab-4cfd-a688-395e06eea9ff', 
                actions = {
                    'key' : '0'
                    }, 
                provider = 'Approval Signing Today', 
                label = 'Token John Doe', 
                provider_type = 'token', 
                subject_common_name = 'John Doe', 
                issuer_common_name = 'Emicert', 
                expire_date = '2022-12-13T23:59:59Z', 
                raw_certificate = '0', 
                appearance = signing_today_client.models.lf_resource.LFResource(
                    id = '05a80817-a3a5-48fe-83c0-0df0f48a2a26', 
                    domain = 'bit4id', 
                    type = 'PDFResource', 
                    dst_uuid = 'd9b4df92-cf85-48dc-a2de-955f518a2992', 
                    title = 'Sales Contract', 
                    filename = 'contract.pdf', 
                    url = 'https://storage.myapi.com/resource/05a80817-a3a5-48fe-83c0-0df0f48a2a26', 
                    size = 1024, 
                    created_at = '2007-04-02T19:30:10Z', 
                    mimetype = 'application/pdf', 
                    pages = 3, 
                    extra_data = {"toSign":true}, ), 
                provider_data = signing_today_client.models.identity_provider_data.Identity_providerData(
                    smartcard_id = -1121978858, 
                    middleware_id = 'bit4xpki', 
                    atr = '3bff1800008131fe55006b02090403010101434e5310318065', 
                    token_info = signing_today_client.models.identity_provider_data_token_info.Identity_providerData_tokenInfo(
                        ul_min_pin_len = 4, 
                        manufacturer_id = 'Bit4id', 
                        ul_free_public_memory = 41168, 
                        serial_number = '7430010005961358', 
                        ul_total_public_memory = 80000, 
                        label = 'CNS', 
                        flags = 1037, 
                        ul_total_private_memory = 80000, 
                        model = 'JS2048 (LB)', 
                        ul_free_private_memory = 41168, 
                        ul_max_pin_len = 8, ), 
                    reader = 'Generic Smart Card Reader Interface 0', ), 
                valid = True, 
                tags = [
                    'qualified'
                    ]
            )
        else :
            return Identity(
        )

    def testIdentity(self):
        """Test Identity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
