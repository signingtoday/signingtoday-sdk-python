# coding: utf-8

# flake8: noqa

"""
    Signing Today Web

    *Signing Today* is the perfect Digital Signature Gateway. Whenever in Your workflow You need to add one or more Digital Signatures to Your document, *Signing Today* is the right choice. You prepare Your documents, *Signing Today* takes care of all the rest: send invitations (`signature tickets`) to signers, collects their signatures, send You back the signed document. Integrating *Signing Today* in Your existing applications is very easy. Just follow these API specifications and get inspired by the many examples presented hereafter.   # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from signing_today_client.api.backoffice_api import BackofficeApi
from signing_today_client.api.dst_note_api import DSTNoteApi
from signing_today_client.api.devices_api import DevicesApi
from signing_today_client.api.digital_signature_transactions_api import DigitalSignatureTransactionsApi
from signing_today_client.api.notifications_api import NotificationsApi
from signing_today_client.api.resources_api import ResourcesApi
from signing_today_client.api.robot_api import RobotApi
from signing_today_client.api.robots_api import RobotsApi
from signing_today_client.api.services_api import ServicesApi
from signing_today_client.api.signing_services_api import SigningServicesApi
from signing_today_client.api.users_api import UsersApi
from signing_today_client.api.bit4id_pathgroup_dst_note_api import Bit4idPathgroupDSTNoteApi
from signing_today_client.api.bit4id_pathgroup_devices_api import Bit4idPathgroupDevicesApi
from signing_today_client.api.bit4id_pathgroup_digital_signature_transactions_api import Bit4idPathgroupDigitalSignatureTransactionsApi
from signing_today_client.api.bit4id_pathgroup_notifications_api import Bit4idPathgroupNotificationsApi
from signing_today_client.api.bit4id_pathgroup_resources_api import Bit4idPathgroupResourcesApi
from signing_today_client.api.bit4id_pathgroup_robots_api import Bit4idPathgroupRobotsApi
from signing_today_client.api.bit4id_pathgroup_services_api import Bit4idPathgroupServicesApi
from signing_today_client.api.bit4id_pathgroup_users_api import Bit4idPathgroupUsersApi

# import ApiClient
from signing_today_client.api_client import ApiClient
from signing_today_client.configuration import Configuration
from signing_today_client.exceptions import OpenApiException
from signing_today_client.exceptions import ApiTypeError
from signing_today_client.exceptions import ApiValueError
from signing_today_client.exceptions import ApiKeyError
from signing_today_client.exceptions import ApiException
# import models into sdk package
from signing_today_client.models.alfresco_sync import AlfrescoSync
from signing_today_client.models.audit_record import AuditRecord
from signing_today_client.models.auth_credential import AuthCredential
from signing_today_client.models.create_digital_signature_transaction import CreateDigitalSignatureTransaction
from signing_today_client.models.create_document import CreateDocument
from signing_today_client.models.create_document_resource import CreateDocumentResource
from signing_today_client.models.create_document_source import CreateDocumentSource
from signing_today_client.models.create_user_request import CreateUserRequest
from signing_today_client.models.dst_note import DSTNote
from signing_today_client.models.dst_signing_address_response import DSTSigningAddressResponse
from signing_today_client.models.dst_status_changed_notification import DSTStatusChangedNotification
from signing_today_client.models.ds_ts_get_response import DSTsGetResponse
from signing_today_client.models.device_authorization_response import DeviceAuthorizationResponse
from signing_today_client.models.digital_signature_transaction import DigitalSignatureTransaction
from signing_today_client.models.document import Document
from signing_today_client.models.error_response import ErrorResponse
from signing_today_client.models.fillable_form import FillableForm
from signing_today_client.models.identity import Identity
from signing_today_client.models.identity_provider_data import IdentityProviderData
from signing_today_client.models.identity_provider_data_token_info import IdentityProviderDataTokenInfo
from signing_today_client.models.inline_object import InlineObject
from signing_today_client.models.inline_object1 import InlineObject1
from signing_today_client.models.inline_object2 import InlineObject2
from signing_today_client.models.inline_object3 import InlineObject3
from signing_today_client.models.inline_object4 import InlineObject4
from signing_today_client.models.inline_object5 import InlineObject5
from signing_today_client.models.inline_object6 import InlineObject6
from signing_today_client.models.inline_object7 import InlineObject7
from signing_today_client.models.inline_object8 import InlineObject8
from signing_today_client.models.inline_object9 import InlineObject9
from signing_today_client.models.inline_response200 import InlineResponse200
from signing_today_client.models.instantiate_dst_template import InstantiateDSTTemplate
from signing_today_client.models.lf_resource import LFResource
from signing_today_client.models.notification_event import NotificationEvent
from signing_today_client.models.notifications_response import NotificationsResponse
from signing_today_client.models.organization import Organization
from signing_today_client.models.organization_private_settings import OrganizationPrivateSettings
from signing_today_client.models.organization_public_settings import OrganizationPublicSettings
from signing_today_client.models.organization_settings import OrganizationSettings
from signing_today_client.models.organization_settings_alfresco_properties import OrganizationSettingsAlfrescoProperties
from signing_today_client.models.organizations_get_response import OrganizationsGetResponse
from signing_today_client.models.robot_authentication_token import RobotAuthenticationToken
from signing_today_client.models.robot_configuration import RobotConfiguration
from signing_today_client.models.robot_configuration_authentication import RobotConfigurationAuthentication
from signing_today_client.models.robot_configuration_webhooks import RobotConfigurationWebhooks
from signing_today_client.models.robot_id_instantiate_roles_mapping import RobotIdInstantiateRolesMapping
from signing_today_client.models.saml_token import SAMLToken
from signing_today_client.models.saml_token_edu_person_targeted_id import SAMLTokenEduPersonTargetedID
from signing_today_client.models.service_failure_response import ServiceFailureResponse
from signing_today_client.models.signature import Signature
from signing_today_client.models.signature_request import SignatureRequest
from signing_today_client.models.signature_restriction import SignatureRestriction
from signing_today_client.models.signature_status_changed_notification import SignatureStatusChangedNotification
from signing_today_client.models.signature_status_changed_notification_document import SignatureStatusChangedNotificationDocument
from signing_today_client.models.signature_status_changed_notification_dst import SignatureStatusChangedNotificationDst
from signing_today_client.models.signer import Signer
from signing_today_client.models.signer_instance import SignerInstance
from signing_today_client.models.signer_record import SignerRecord
from signing_today_client.models.signers_group import SignersGroup
from signing_today_client.models.trusted_device import TrustedDevice
from signing_today_client.models.trusted_devices_get_response import TrustedDevicesGetResponse
from signing_today_client.models.user import User
from signing_today_client.models.user_group import UserGroup
from signing_today_client.models.user_group_get_response import UserGroupGetResponse
from signing_today_client.models.user_sync_report import UserSyncReport
from signing_today_client.models.user_sync_report_users import UserSyncReportUsers
from signing_today_client.models.users_get_response import UsersGetResponse

