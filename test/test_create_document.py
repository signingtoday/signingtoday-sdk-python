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
from signing_today_client.models.create_document import CreateDocument  # noqa: E501
from signing_today_client.rest import ApiException

class TestCreateDocument(unittest.TestCase):
    """CreateDocument unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateDocument
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = signing_today_client.models.create_document.CreateDocument()  # noqa: E501
        if include_optional :
            return CreateDocument(
                resource = signing_today_client.models.create_document_resource.CreateDocument_resource(
                    filename = 'contract.pdf', 
                    resource_type = PDF_Document, 
                    title = 'Sales Contract', 
                    source = signing_today_client.models.create_document_source.CreateDocumentSource(
                        type = 'Embedded', 
                        embedded_data = bytes(b'blah'), 
                        source_url = '0', ), ), 
                forms = [
                    signing_today_client.models.fillable_form.FillableForm(
                        _instance_id = 1, 
                        id = 2, 
                        document_id = 3, 
                        type = 'SignatureForm', 
                        position_x = 100.00, 
                        position_y = 58.14, 
                        width = 10.1, 
                        height = 5.66, 
                        page = 1, 
                        signer_id = 1, 
                        to_fill = True, 
                        filled = False, 
                        invisible = True, 
                        extra_data = {"signatureRequestId":1}, )
                    ], 
                signature_requests = [
                    signing_today_client.models.signature_request.SignatureRequest(
                        _instance_id = 1, 
                        id = 3, 
                        reason = 'As the Buyer', 
                        description = 'The proponent', 
                        signer_id = 2, 
                        sign_profile = 'PAdES', 
                        with_timestamp = True, 
                        declinable = False, 
                        restrictions = [
                            signing_today_client.models.signature_restriction.SignatureRestriction(
                                rule = '0', 
                                operator = '0', 
                                value = '0', )
                            ], 
                        extra_data = {"st_ticketUrl":"http://signing.today/ticket/8bd4aead-ad37-42bc-b3b0-22ce3d1c9e79"}, )
                    ], 
                signer_groups = [
                    signing_today_client.models.signers_group.SignersGroup(
                        _instance_id = 1, 
                        signers = [
                            signing_today_client.models.signer.Signer(
                                _instance_id = 1, 
                                id = 1, 
                                name = 'Adam', 
                                surname = 'Smith', 
                                email = 'adam.smith@email.com', 
                                phone = '+013392213450', 
                                role = 'buyer', 
                                user_uuid = '737dc132-a3f0-11e9-a2a3-2a2ae2dbcce4', 
                                template_label = 'Buyer', )
                            ], )
                    ]
            )
        else :
            return CreateDocument(
        )

    def testCreateDocument(self):
        """Test CreateDocument"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
