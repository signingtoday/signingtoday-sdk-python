# signing_today_api
*Signing Today* enables seamless integration of digital signatures into any
website by the use of easy requests to our API. This is the smart way of
adding digital signature support with a great user experience.


*Signing Today APIs* use HTTP methods and are RESTful based, moreover they
are protected by a *server to server authentication* standard by the use of
tokens.


*Signing Today APIs* can be used in these environments:


| Environment | Description | Endpoint |
| ----------- | ----------- | -------- |
| Sandbox     | Test environment | `https://sandbox.signingtoday.com` |
| Live        | Production environment | `https://api.signingtoday.com` |


For every single request to Signing Today has to be defined the following
*HTTP* header:
- `Authorization`, which contains the authentication token.

If the request has a body than another *HTTP* header is requested:
- `Content-Type`, with `application/json` value.


Follows an example of usage to enumerate all the user of *my-org*
organization.

**Example**

```json
$ curl https://sandbox.signingtoday.com/api/v1/my-org/users \\
    -H 'Authorization: Token <access-token>'
```

## HTTP methods used

APIs use the right HTTP verb in every situation.

| Method   | Description                    |
| -------- | ------------------------------ |
| `GET`    | Request data from a resource   |
| `POST`   | Send data to create a resource |
| `PUT`    | Update a resource              |
| `PATCH`  | Partially update a resource    |
| `DELETE` | Delete a resourse              |


## Response definition

All the response are in JSON format.
As response to a request of all users of an organization you will have a
result like this:

```json
{
    \"pagination\": {
      \"count\": 75,
      \"previous\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=1\",
      \"next\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=3\",
      \"pages\": 8,
      \"page\": 2
    },
    \"meta\": {
      \"code\": 200
    },
    \"data\": [
      {
        \"id\": \"jdo\",
        \"status\": \"enabled\",
        \"type\": \"Basic user account\",
        \"email\": johndoe@dummyemail.com,
        \"first_name\": \"John\",
        \"last_name\": \"Doe\",
        \"wallet\": [],
        \"created_by\": \"system\",
        \"owner\": false,
        \"automatic\": false,
        \"rao\": false
      },
      ...
    ]
  }
```

The JSON of the response is made of three parts:
- Pagination
- Meta
- Data

### Pagination

*Pagination* object allows to split the response into parts and then to
rebuild it sequentially by the use of `next` and `previous` parameters, by
which you get previous and following blocks. The *Pagination* is present
only if the response is a list of objects.

The general structure of *Pagination* object is the following:

```json
{
    \"pagination\": {
      \"count\": 75,
      \"previous\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=1\",
      \"next\": \"https://sandbox.signingtoday.com/api/v1/my-org/users?page=3\",
      \"pages\": 8,
      \"page\": 2
    },
    ...
  }
```

### Meta

*Meta* object is used to enrich the information about the response. In the
previous example, a successful case of response, *Meta* will have value
`status: 2XX`. In case of unsuccessful response, *Meta* will have further
information, as follows:

```json
{
    \"meta\": {
      \"code\": <HTTP STATUS CODE>,
      \"error_type\": <STATUS CODE DESCRIPTION>,
      \"error_message\": <ERROR DESCRIPTION>
    }
  }
```

### Data

*Data* object outputs as object or list of them. Contains the expected data
as requested to the API.

## Search filters

Search filters of the API have the following structure:

`where_ATTRIBUTENAME`=`VALUE`

In this way you make a case-sensitive search of *VALUE*. You can extend it
through the Django lookup, obtaining more specific filters. For example:

`where_ATTRIBUTENAME__LOOKUP`=`VALUE`

where *LOOKUP* can be replaced with `icontains` to have a partial insensitive
research, where

`where_first_name__icontains`=`CHa`

matches with every user that have the *cha* string in their name, with
no differences between capital and lower cases.

[Here](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#field-lookups)
the list of the lookups.

## Webhooks

Signing Today supports webhooks for the update of DSTs and identities status.
You can choose if to use or not webhooks and if you want to receive updates
about DSTs and/or identities. You can configurate it on application token
level, in the *webhook* field, as follows:

```json
\"webhooks\": {
  \"dst\": \"URL\",
  \"identity\": \"URL\"
  }
```

### DSTs status update

DSTs send the following status updates:
- **DST_STATUS_CHANGED**: whenever the DST changes its status
- **SIGNATURE_STATUS_CHANGED**: whenever one of the signatures changes its
status

#### DST_STATUS_CHANGED

Sends the following information:

```json
{
    \"message\": \"DST_STATUS_CHANGED\",
    \"data\": {
      \"status\": \"<DST_STATUS>\",
      \"dst\": \"<DST_ID>\",
      \"reason\": \"<DST_REASON>\"
    }
  }
```

#### SIGNATURE_STATUS_CHANGED

Sends the following information:

```json
{
    \"message\": \"SIGNATURE_STATUS_CHANGED\",
    \"data\": {
      \"status\": \"<SIGNATURE_STATUS>\",
      \"group\": <MEMBERSHIP_GROUP_INDEX>,
      \"dst\": {
        \"id\": \"<DST_ID>\",
        \"title\": \"<DST_TITLE>\"
      },
      \"signature\": \"<SIGNATURE_ID>\",
      \"signer\": \"<SIGNER_USERNAME>\",
      \"position\": \"<SIGNATURE_POSITION>\",
      \"document\": {
        \"display_name\": \"<DOCUMENT_TITLE>\",
        \"id\": \"<DOCUMENT_ID>\",
        \"order\": <DOCUMENT_INDEX>
      },
      \"automatic\": <DECLARES_IF_THE_SIGNER_IS_AUTOMATIC>,
      \"page\": \"<SIGNATURE_PAGE>\"
    }
  }
```

### Identities status update

Identities send the following status updates:
- **IDENTITY_REQUEST_ENROLLED**: whenever an identity request is activated

#### IDENTITY_REQUEST_ENROLLED

Sends the following information:

```json
{
    \"message\": \"IDENTITY_REQUEST_ENROLLED\",
    \"data\": {
      \"status\": \"<REQUEST_STATUS>\",
      \"request\": \"<REQUEST_ID>\",
      \"user\": \"<APPLICANT_USERNAME>\"
    }
  }
```

### Urlback

Sometimes may be necessary to make a redirect after an user, from the
signature tray, has completed his operations or activated a certificate.

If set, redirects could happen in 3 cases:
- after a signature or decline
- after a DST has been signed by all the signers or canceled
- after the activation of a certificate

In the first two cases the urlback returns the following information through
a data form:
- **dst-id**: id of the DST
- **dst-url**: signature_ticket of the signature
- **dst-status**: current status of the DST
- **dst-signature-id**: id of the signature
- **dst-signature-status**: current status of the signature
- **user**: username of the signer
- **decline-reason**: in case of a refused DST contains the reason of the
decline

In the last case the urlback returns the following information through a
data form:
- **user**: username of the user activated the certificate
- **identity-provider**: the provider has been used to issue the certificate
- **identity-request-id**: id of the enrollment request
- **identity-id**: id of the new identity
- **identity-label**: the label assigned to the identity
- **identity-certificate**: public key of the certificate




This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.5.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://signing.today/contacts/](https://signing.today/contacts/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import signing_today_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import signing_today_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import signing_today_client
from signing_today_client.rest import ApiException
from pprint import pprint

configuration = signing_today_client.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://sandbox.signingtoday.com/api/v1
configuration.host = "https://sandbox.signingtoday.com/api/v1"
# Enter a context with an instance of the API client
with signing_today_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signing_today_client.IdentitiesApi(api_client)
    organization_id = 'api-demo' # str | The **organization-id** represents an organization that is included in the SigninToday application, also know as **slug** and it is used as a path parameter to restrict the asked functionality to the specified organization  (default to 'api-demo')
identity_id = signing_today_client.Id() # Id | The **identity-id** is the uuid code that identifies an identity in the wallet of an user. It is, as well, used to restrict the requested operation to the scope of that identity 
inline_object = signing_today_client.InlineObject() # InlineObject | 

    try:
        # Associate an appearance to an identity
        api_response = api_instance.associate_appearance(organization_id, identity_id, inline_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IdentitiesApi->associate_appearance: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://sandbox.signingtoday.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*IdentitiesApi* | [**associate_appearance**](docs/IdentitiesApi.md#associate_appearance) | **POST** /{organization-id}/identities/{identity-id}/appearance | Associate an appearance to an identity
*IdentitiesApi* | [**associate_identity**](docs/IdentitiesApi.md#associate_identity) | **POST** /{organization-id}/users/{user-id}/wallet | Associate to an user an already existing identity
*IdentitiesApi* | [**create_token_from_identity**](docs/IdentitiesApi.md#create_token_from_identity) | **POST** /{organization-id}/identities/create/token | Create an identity from token
*IdentitiesApi* | [**delete_appearance**](docs/IdentitiesApi.md#delete_appearance) | **DELETE** /{organization-id}/identities/{identity-id}/appearance | Delete the appearance of an identity
*IdentitiesApi* | [**delete_enrollment_request**](docs/IdentitiesApi.md#delete_enrollment_request) | **DELETE** /{organization-id}/identity-requests/{enrollment-id} | Delete an enrollment request
*IdentitiesApi* | [**delete_identity**](docs/IdentitiesApi.md#delete_identity) | **DELETE** /{organization-id}/identities/{identity-id} | Delete an identity
*IdentitiesApi* | [**get_enrollment_request**](docs/IdentitiesApi.md#get_enrollment_request) | **GET** /{organization-id}/identity-requests/{enrollment-id} | Get information about an enrollment request
*IdentitiesApi* | [**get_identity**](docs/IdentitiesApi.md#get_identity) | **GET** /{organization-id}/identities/{identity-id} | Get information about an identity
*IdentitiesApi* | [**list_enrollment_requests**](docs/IdentitiesApi.md#list_enrollment_requests) | **GET** /{organization-id}/identity-requests | Enumerate the enrollment requests of an organization
*IdentitiesApi* | [**list_identities**](docs/IdentitiesApi.md#list_identities) | **GET** /{organization-id}/identities | Enumerate the identities of an organization
*IdentitiesApi* | [**list_user_enrollments**](docs/IdentitiesApi.md#list_user_enrollments) | **GET** /{organization-id}/users/{user-id}/identity-requests | List the enrollments of an user
*IdentitiesApi* | [**list_user_identities**](docs/IdentitiesApi.md#list_user_identities) | **GET** /{organization-id}/users/{user-id}/wallet | Enumerate the identities of an user
*IdentitiesApi* | [**renew_identity**](docs/IdentitiesApi.md#renew_identity) | **POST** /{organization-id}/identity-requests/{enrollment-id}/renew | Renew an Identity
*IdentitiesApi* | [**request_enrollment**](docs/IdentitiesApi.md#request_enrollment) | **POST** /{organization-id}/enroll | Submit an enrollment request
*OrganizationsApi* | [**get_organization**](docs/OrganizationsApi.md#get_organization) | **GET** /organizations/{organization-id} | Get the settings of an oraganization
*OrganizationsApi* | [**patch_organization**](docs/OrganizationsApi.md#patch_organization) | **PATCH** /organizations/{organization-id} | Edit the settings of an organization
*SignatureTransactionsApi* | [**cancel_dst**](docs/SignatureTransactionsApi.md#cancel_dst) | **POST** /{organization-id}/signature-transactions/{dst-id}/cancel | Mark a DST as canceled
*SignatureTransactionsApi* | [**create_dst**](docs/SignatureTransactionsApi.md#create_dst) | **POST** /{organization-id}/signature-transactions | Create a Digital Signature Transaction
*SignatureTransactionsApi* | [**delete_dst**](docs/SignatureTransactionsApi.md#delete_dst) | **DELETE** /{organization-id}/signature-transactions/{dst-id} | Delete a Digital Signature Transaction
*SignatureTransactionsApi* | [**delete_dst_resources**](docs/SignatureTransactionsApi.md#delete_dst_resources) | **DELETE** /{organization-id}/signature-transactions/{dst-id}/resources | Delete the resources of a DST
*SignatureTransactionsApi* | [**get_document**](docs/SignatureTransactionsApi.md#get_document) | **GET** /{organization-id}/documents/{document-id}/download | Download a document from a DST
*SignatureTransactionsApi* | [**get_dst**](docs/SignatureTransactionsApi.md#get_dst) | **GET** /{organization-id}/signature-transactions/{dst-id} | Get information about a DST
*SignatureTransactionsApi* | [**list_ds_ts**](docs/SignatureTransactionsApi.md#list_ds_ts) | **GET** /{organization-id}/signature-transactions | List the DSTs of an organization
*SignaturesApi* | [**create_channel**](docs/SignaturesApi.md#create_channel) | **POST** /{organization-id}/channels/{dst-id} | Create a channel
*SignaturesApi* | [**decline_dst**](docs/SignaturesApi.md#decline_dst) | **POST** /{organization-id}/signatures/{signature-id}/decline | Decline a Digital Signature Transaction
*SignaturesApi* | [**perform_dst**](docs/SignaturesApi.md#perform_dst) | **POST** /{organization-id}/signatures/{signature-id}/perform | Sign a DST with an automatic signer
*SignaturesApi* | [**perform_signature**](docs/SignaturesApi.md#perform_signature) | **POST** /{organization-id}/signatures/{signature-id}/perform/{identity-id} | Perform a Signature
*SignaturesApi* | [**perform_signature_with_session**](docs/SignaturesApi.md#perform_signature_with_session) | **POST** /{organization-id}/signatures/{signature-id}/session-perform | Perform a Signature with session
*TokensApi* | [**create_token**](docs/TokensApi.md#create_token) | **POST** /{organization-id}/tokens | Create an application token
*TokensApi* | [**delete_token**](docs/TokensApi.md#delete_token) | **DELETE** /{organization-id}/tokens/{token-id} | Delete a token of the organization
*TokensApi* | [**get_token**](docs/TokensApi.md#get_token) | **GET** /{organization-id}/tokens/{token-id} | Get information about a token
*TokensApi* | [**list_tokens**](docs/TokensApi.md#list_tokens) | **GET** /{organization-id}/tokens | Enumerate the tokens of an organization
*TokensApi* | [**list_user_tokens**](docs/TokensApi.md#list_user_tokens) | **GET** /{organization-id}/users/{user-id}/tokens | Enumerate the tokens of an user
*TokensApi* | [**update_token**](docs/TokensApi.md#update_token) | **PUT** /{organization-id}/tokens/{token-id} | Update the properties of a token
*UsersApi* | [**create_user**](docs/UsersApi.md#create_user) | **POST** /{organization-id}/users | Create a user of the organization
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /{organization-id}/users/{user-id} | Get information about an user
*UsersApi* | [**list_users**](docs/UsersApi.md#list_users) | **GET** /{organization-id}/users | Enumerate the users of an organization
*UsersApi* | [**update_user**](docs/UsersApi.md#update_user) | **PUT** /{organization-id}/users/{user-id} | Edit one or more user properties
*Bit4idPathgroupIdentitiesApi* | [**associate_appearance**](docs/Bit4idPathgroupIdentitiesApi.md#associate_appearance) | **POST** /{organization-id}/identities/{identity-id}/appearance | Associate an appearance to an identity
*Bit4idPathgroupIdentitiesApi* | [**associate_identity**](docs/Bit4idPathgroupIdentitiesApi.md#associate_identity) | **POST** /{organization-id}/users/{user-id}/wallet | Associate to an user an already existing identity
*Bit4idPathgroupIdentitiesApi* | [**create_token_from_identity**](docs/Bit4idPathgroupIdentitiesApi.md#create_token_from_identity) | **POST** /{organization-id}/identities/create/token | Create an identity from token
*Bit4idPathgroupIdentitiesApi* | [**delete_appearance**](docs/Bit4idPathgroupIdentitiesApi.md#delete_appearance) | **DELETE** /{organization-id}/identities/{identity-id}/appearance | Delete the appearance of an identity
*Bit4idPathgroupIdentitiesApi* | [**delete_enrollment_request**](docs/Bit4idPathgroupIdentitiesApi.md#delete_enrollment_request) | **DELETE** /{organization-id}/identity-requests/{enrollment-id} | Delete an enrollment request
*Bit4idPathgroupIdentitiesApi* | [**delete_identity**](docs/Bit4idPathgroupIdentitiesApi.md#delete_identity) | **DELETE** /{organization-id}/identities/{identity-id} | Delete an identity
*Bit4idPathgroupIdentitiesApi* | [**get_enrollment_request**](docs/Bit4idPathgroupIdentitiesApi.md#get_enrollment_request) | **GET** /{organization-id}/identity-requests/{enrollment-id} | Get information about an enrollment request
*Bit4idPathgroupIdentitiesApi* | [**get_identity**](docs/Bit4idPathgroupIdentitiesApi.md#get_identity) | **GET** /{organization-id}/identities/{identity-id} | Get information about an identity
*Bit4idPathgroupIdentitiesApi* | [**list_enrollment_requests**](docs/Bit4idPathgroupIdentitiesApi.md#list_enrollment_requests) | **GET** /{organization-id}/identity-requests | Enumerate the enrollment requests of an organization
*Bit4idPathgroupIdentitiesApi* | [**list_identities**](docs/Bit4idPathgroupIdentitiesApi.md#list_identities) | **GET** /{organization-id}/identities | Enumerate the identities of an organization
*Bit4idPathgroupIdentitiesApi* | [**list_user_enrollments**](docs/Bit4idPathgroupIdentitiesApi.md#list_user_enrollments) | **GET** /{organization-id}/users/{user-id}/identity-requests | List the enrollments of an user
*Bit4idPathgroupIdentitiesApi* | [**list_user_identities**](docs/Bit4idPathgroupIdentitiesApi.md#list_user_identities) | **GET** /{organization-id}/users/{user-id}/wallet | Enumerate the identities of an user
*Bit4idPathgroupIdentitiesApi* | [**renew_identity**](docs/Bit4idPathgroupIdentitiesApi.md#renew_identity) | **POST** /{organization-id}/identity-requests/{enrollment-id}/renew | Renew an Identity
*Bit4idPathgroupIdentitiesApi* | [**request_enrollment**](docs/Bit4idPathgroupIdentitiesApi.md#request_enrollment) | **POST** /{organization-id}/enroll | Submit an enrollment request
*Bit4idPathgroupOrganizationsApi* | [**get_organization**](docs/Bit4idPathgroupOrganizationsApi.md#get_organization) | **GET** /organizations/{organization-id} | Get the settings of an oraganization
*Bit4idPathgroupOrganizationsApi* | [**patch_organization**](docs/Bit4idPathgroupOrganizationsApi.md#patch_organization) | **PATCH** /organizations/{organization-id} | Edit the settings of an organization
*Bit4idPathgroupSignatureTransactionsApi* | [**cancel_dst**](docs/Bit4idPathgroupSignatureTransactionsApi.md#cancel_dst) | **POST** /{organization-id}/signature-transactions/{dst-id}/cancel | Mark a DST as canceled
*Bit4idPathgroupSignatureTransactionsApi* | [**create_dst**](docs/Bit4idPathgroupSignatureTransactionsApi.md#create_dst) | **POST** /{organization-id}/signature-transactions | Create a Digital Signature Transaction
*Bit4idPathgroupSignatureTransactionsApi* | [**delete_dst**](docs/Bit4idPathgroupSignatureTransactionsApi.md#delete_dst) | **DELETE** /{organization-id}/signature-transactions/{dst-id} | Delete a Digital Signature Transaction
*Bit4idPathgroupSignatureTransactionsApi* | [**delete_dst_resources**](docs/Bit4idPathgroupSignatureTransactionsApi.md#delete_dst_resources) | **DELETE** /{organization-id}/signature-transactions/{dst-id}/resources | Delete the resources of a DST
*Bit4idPathgroupSignatureTransactionsApi* | [**get_document**](docs/Bit4idPathgroupSignatureTransactionsApi.md#get_document) | **GET** /{organization-id}/documents/{document-id}/download | Download a document from a DST
*Bit4idPathgroupSignatureTransactionsApi* | [**get_dst**](docs/Bit4idPathgroupSignatureTransactionsApi.md#get_dst) | **GET** /{organization-id}/signature-transactions/{dst-id} | Get information about a DST
*Bit4idPathgroupSignatureTransactionsApi* | [**list_ds_ts**](docs/Bit4idPathgroupSignatureTransactionsApi.md#list_ds_ts) | **GET** /{organization-id}/signature-transactions | List the DSTs of an organization
*Bit4idPathgroupSignaturesApi* | [**create_channel**](docs/Bit4idPathgroupSignaturesApi.md#create_channel) | **POST** /{organization-id}/channels/{dst-id} | Create a channel
*Bit4idPathgroupSignaturesApi* | [**decline_dst**](docs/Bit4idPathgroupSignaturesApi.md#decline_dst) | **POST** /{organization-id}/signatures/{signature-id}/decline | Decline a Digital Signature Transaction
*Bit4idPathgroupSignaturesApi* | [**perform_dst**](docs/Bit4idPathgroupSignaturesApi.md#perform_dst) | **POST** /{organization-id}/signatures/{signature-id}/perform | Sign a DST with an automatic signer
*Bit4idPathgroupSignaturesApi* | [**perform_signature**](docs/Bit4idPathgroupSignaturesApi.md#perform_signature) | **POST** /{organization-id}/signatures/{signature-id}/perform/{identity-id} | Perform a Signature
*Bit4idPathgroupSignaturesApi* | [**perform_signature_with_session**](docs/Bit4idPathgroupSignaturesApi.md#perform_signature_with_session) | **POST** /{organization-id}/signatures/{signature-id}/session-perform | Perform a Signature with session
*Bit4idPathgroupTokensApi* | [**create_token**](docs/Bit4idPathgroupTokensApi.md#create_token) | **POST** /{organization-id}/tokens | Create an application token
*Bit4idPathgroupTokensApi* | [**delete_token**](docs/Bit4idPathgroupTokensApi.md#delete_token) | **DELETE** /{organization-id}/tokens/{token-id} | Delete a token of the organization
*Bit4idPathgroupTokensApi* | [**get_token**](docs/Bit4idPathgroupTokensApi.md#get_token) | **GET** /{organization-id}/tokens/{token-id} | Get information about a token
*Bit4idPathgroupTokensApi* | [**list_tokens**](docs/Bit4idPathgroupTokensApi.md#list_tokens) | **GET** /{organization-id}/tokens | Enumerate the tokens of an organization
*Bit4idPathgroupTokensApi* | [**list_user_tokens**](docs/Bit4idPathgroupTokensApi.md#list_user_tokens) | **GET** /{organization-id}/users/{user-id}/tokens | Enumerate the tokens of an user
*Bit4idPathgroupTokensApi* | [**update_token**](docs/Bit4idPathgroupTokensApi.md#update_token) | **PUT** /{organization-id}/tokens/{token-id} | Update the properties of a token
*Bit4idPathgroupUsersApi* | [**create_user**](docs/Bit4idPathgroupUsersApi.md#create_user) | **POST** /{organization-id}/users | Create a user of the organization
*Bit4idPathgroupUsersApi* | [**get_user**](docs/Bit4idPathgroupUsersApi.md#get_user) | **GET** /{organization-id}/users/{user-id} | Get information about an user
*Bit4idPathgroupUsersApi* | [**list_users**](docs/Bit4idPathgroupUsersApi.md#list_users) | **GET** /{organization-id}/users | Enumerate the users of an organization
*Bit4idPathgroupUsersApi* | [**update_user**](docs/Bit4idPathgroupUsersApi.md#update_user) | **PUT** /{organization-id}/users/{user-id} | Edit one or more user properties


## Documentation For Models

 - [AutomaticSignature](docs/AutomaticSignature.md)
 - [CreateIdentitybyToken](docs/CreateIdentitybyToken.md)
 - [CreateSignatureTransaction](docs/CreateSignatureTransaction.md)
 - [CreateToken](docs/CreateToken.md)
 - [CreateUser](docs/CreateUser.md)
 - [Document](docs/Document.md)
 - [Document1](docs/Document1.md)
 - [Identity](docs/Identity.md)
 - [IdentityActions](docs/IdentityActions.md)
 - [IdentityAssociation](docs/IdentityAssociation.md)
 - [IdentityEnroll](docs/IdentityEnroll.md)
 - [IdentityEnrollActions](docs/IdentityEnrollActions.md)
 - [IdentityRequest](docs/IdentityRequest.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [InlineObject4](docs/InlineObject4.md)
 - [InlineObject5](docs/InlineObject5.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20013Data](docs/InlineResponse20013Data.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse2009Meta](docs/InlineResponse2009Meta.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InlineResponse2011](docs/InlineResponse2011.md)
 - [InlineResponse2012](docs/InlineResponse2012.md)
 - [InlineResponse2013](docs/InlineResponse2013.md)
 - [InlineResponse2014](docs/InlineResponse2014.md)
 - [InlineResponse2014Data](docs/InlineResponse2014Data.md)
 - [InlineResponse2015](docs/InlineResponse2015.md)
 - [InlineResponse401](docs/InlineResponse401.md)
 - [InlineResponse403](docs/InlineResponse403.md)
 - [InlineResponse404](docs/InlineResponse404.md)
 - [MetaDataError](docs/MetaDataError.md)
 - [MetaDataSuccess](docs/MetaDataSuccess.md)
 - [Organization](docs/Organization.md)
 - [OrganizationSettings](docs/OrganizationSettings.md)
 - [PaginationData](docs/PaginationData.md)
 - [SMS](docs/SMS.md)
 - [Signature](docs/Signature.md)
 - [SignatureDST](docs/SignatureDST.md)
 - [SignatureDSTWhere](docs/SignatureDSTWhere.md)
 - [SignatureImplementationResponse](docs/SignatureImplementationResponse.md)
 - [SignatureImplementationResponseChannel](docs/SignatureImplementationResponseChannel.md)
 - [SignatureTransaction](docs/SignatureTransaction.md)
 - [SignatureWhere](docs/SignatureWhere.md)
 - [Token](docs/Token.md)
 - [TokenHttpOptions](docs/TokenHttpOptions.md)
 - [TokenWebhooks](docs/TokenWebhooks.md)
 - [UpdateOrganization](docs/UpdateOrganization.md)
 - [UpdateToken](docs/UpdateToken.md)
 - [UpdateUser](docs/UpdateUser.md)
 - [User](docs/User.md)


## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

smartcloud@bit4id.com


