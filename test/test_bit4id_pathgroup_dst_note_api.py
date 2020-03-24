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
from signing_today_client.api.bit4id_pathgroup_dst_note_api import Bit4idPathgroupDSTNoteApi  # noqa: E501
from signing_today_client.rest import ApiException


class TestBit4idPathgroupDSTNoteApi(unittest.TestCase):
    """Bit4idPathgroupDSTNoteApi unit test stubs"""

    def setUp(self):
        self.api = signing_today_client.api.bit4id_pathgroup_dst_note_api.Bit4idPathgroupDSTNoteApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_d_st_id_note_get(self):
        """Test case for d_st_id_note_get

        Retrieve the DSTNotes associated to the DST  # noqa: E501
        """
        pass

    def test_d_st_id_note_note_id_delete(self):
        """Test case for d_st_id_note_note_id_delete

        Delete a DSTNote  # noqa: E501
        """
        pass

    def test_d_st_id_note_note_id_put(self):
        """Test case for d_st_id_note_note_id_put

        Edit a DSTNote  # noqa: E501
        """
        pass

    def test_d_st_id_note_post(self):
        """Test case for d_st_id_note_post

        Append a new DSTNote  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()