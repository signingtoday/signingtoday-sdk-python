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
from signing_today_client.models.inline_object8 import InlineObject8  # noqa: E501
from signing_today_client.rest import ApiException

class TestInlineObject8(unittest.TestCase):
    """InlineObject8 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineObject8
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = signing_today_client.models.inline_object8.InlineObject8()  # noqa: E501
        if include_optional :
            return InlineObject8(
                example1 = 'example1'
            )
        else :
            return InlineObject8(
        )

    def testInlineObject8(self):
        """Test InlineObject8"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
