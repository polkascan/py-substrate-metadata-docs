
# Did

---------
## Calls

---------
### add_key_agreement_key
See [`Pallet::add_key_agreement_key`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_key | `DidEncryptionKey` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'add_key_agreement_key', {'new_key': {'X25519': '[u8; 32]'}}
)
```

---------
### add_service_endpoint
See [`Pallet::add_service_endpoint`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| service_endpoint | `DidEndpoint<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'add_service_endpoint', {
    'service_endpoint': {
        'id': 'Bytes',
        'service_types': ['Bytes'],
        'urls': ['Bytes'],
    },
}
)
```

---------
### change_deposit_owner
See [`Pallet::change_deposit_owner`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Did', 'change_deposit_owner', {}
)
```

---------
### create
See [`Pallet::create`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| details | `Box<DidCreationDetailsOf<T>>` | 
| signature | `DidSignature` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'create', {
    'details': {
        'did': 'AccountId',
        'new_attestation_key': (
            None,
            {
                'Account': 'AccountId',
                'Ecdsa': '[u8; 33]',
                'Ed25519': '[u8; 32]',
                'Sr25519': '[u8; 32]',
            },
        ),
        'new_delegation_key': (
            None,
            {
                'Account': 'AccountId',
                'Ecdsa': '[u8; 33]',
                'Ed25519': '[u8; 32]',
                'Sr25519': '[u8; 32]',
            },
        ),
        'new_key_agreement_keys': 'scale_info::321',
        'new_service_details': [
            {
                'id': 'Bytes',
                'service_types': [
                    'Bytes',
                ],
                'urls': ['Bytes'],
            },
        ],
        'submitter': 'AccountId',
    },
    'signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### create_from_account
See [`Pallet::create_from_account`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| authentication_key | `DidVerificationKey<AccountIdOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'create_from_account', {
    'authentication_key': {
        'Account': 'AccountId',
        'Ecdsa': '[u8; 33]',
        'Ed25519': '[u8; 32]',
        'Sr25519': '[u8; 32]',
    },
}
)
```

---------
### delete
See [`Pallet::delete`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| endpoints_to_remove | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'delete', {'endpoints_to_remove': 'u32'}
)
```

---------
### dispatch_as
See [`Pallet::dispatch_as`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| did_identifier | `DidIdentifierOf<T>` | 
| call | `Box<DidCallableOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'dispatch_as', {
    'call': 'Call',
    'did_identifier': 'AccountId',
}
)
```

---------
### reclaim_deposit
See [`Pallet::reclaim_deposit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| did_subject | `DidIdentifierOf<T>` | 
| endpoints_to_remove | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'reclaim_deposit', {
    'did_subject': 'AccountId',
    'endpoints_to_remove': 'u32',
}
)
```

---------
### remove_attestation_key
See [`Pallet::remove_attestation_key`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Did', 'remove_attestation_key', {}
)
```

---------
### remove_delegation_key
See [`Pallet::remove_delegation_key`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Did', 'remove_delegation_key', {}
)
```

---------
### remove_key_agreement_key
See [`Pallet::remove_key_agreement_key`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| key_id | `KeyIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'remove_key_agreement_key', {'key_id': 'scale_info::12'}
)
```

---------
### remove_service_endpoint
See [`Pallet::remove_service_endpoint`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| service_id | `ServiceEndpointId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'remove_service_endpoint', {'service_id': 'Bytes'}
)
```

---------
### set_attestation_key
See [`Pallet::set_attestation_key`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_key | `DidVerificationKey<AccountIdOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'set_attestation_key', {
    'new_key': {
        'Account': 'AccountId',
        'Ecdsa': '[u8; 33]',
        'Ed25519': '[u8; 32]',
        'Sr25519': '[u8; 32]',
    },
}
)
```

---------
### set_authentication_key
See [`Pallet::set_authentication_key`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_key | `DidVerificationKey<AccountIdOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'set_authentication_key', {
    'new_key': {
        'Account': 'AccountId',
        'Ecdsa': '[u8; 33]',
        'Ed25519': '[u8; 32]',
        'Sr25519': '[u8; 32]',
    },
}
)
```

---------
### set_delegation_key
See [`Pallet::set_delegation_key`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_key | `DidVerificationKey<AccountIdOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'set_delegation_key', {
    'new_key': {
        'Account': 'AccountId',
        'Ecdsa': '[u8; 33]',
        'Ed25519': '[u8; 32]',
        'Sr25519': '[u8; 32]',
    },
}
)
```

---------
### submit_did_call
See [`Pallet::submit_did_call`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| did_call | `Box<DidAuthorizedCallOperationOf<T>>` | 
| signature | `DidSignature` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'submit_did_call', {
    'did_call': {
        'block_number': 'u64',
        'call': 'Call',
        'did': 'AccountId',
        'submitter': 'AccountId',
        'tx_counter': 'u64',
    },
    'signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### update_deposit
See [`Pallet::update_deposit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| did | `DidIdentifierOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Did', 'update_deposit', {'did': 'AccountId'}
)
```

---------
## Events

---------
### DidCallDispatched
A DID-authorised call has been executed.
\[DID caller, dispatch result\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DidIdentifierOf<T>` | ```AccountId```
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}}```

---------
### DidCreated
A new DID has been created.
\[transaction signer, DID identifier\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `DidIdentifierOf<T>` | ```AccountId```

---------
### DidDeleted
A DID has been deleted.
\[DID identifier\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DidIdentifierOf<T>` | ```AccountId```

---------
### DidUpdated
A DID has been updated.
\[DID identifier\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DidIdentifierOf<T>` | ```AccountId```

---------
## Storage functions

---------
### Did
 DIDs stored on chain.

 It maps from a DID identifier to the DID details.

#### Python
```python
result = substrate.query(
    'Did', 'Did', ['AccountId']
)
```

#### Return value
```python
{
    'attestation_key': (None, 'scale_info::12'),
    'authentication_key': 'scale_info::12',
    'delegation_key': (None, 'scale_info::12'),
    'deposit': {'amount': 'u128', 'owner': 'AccountId'},
    'key_agreement_keys': 'scale_info::451',
    'last_tx_counter': 'u64',
    'public_keys': 'scale_info::459',
}
```
---------
### DidBlacklist
 The set of DIDs that have been deleted and cannot therefore be created
 again for security reasons.

 It maps from a DID identifier to a unit tuple, for the sake of tracking
 DID identifiers.

#### Python
```python
result = substrate.query(
    'Did', 'DidBlacklist', ['AccountId']
)
```

#### Return value
```python
()
```
---------
### DidEndpointsCount
 Counter of service endpoints for each DID.

 It maps from (DID identifier) to a 32-bit counter.

#### Python
```python
result = substrate.query(
    'Did', 'DidEndpointsCount', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### ServiceEndpoints
 Service endpoints associated with DIDs.

 It maps from (DID identifier, service ID) to the service details.

#### Python
```python
result = substrate.query(
    'Did', 'ServiceEndpoints', ['AccountId', 'Bytes']
)
```

#### Return value
```python
{'id': 'Bytes', 'service_types': ['Bytes'], 'urls': ['Bytes']}
```
---------
## Constants

---------
### BaseDeposit
 The amount of balance that will be taken for each DID as a deposit
 to incentivise fair use of the on chain storage. The deposits
 increase by the amount of used keys and service endpoints. The
 deposit can be reclaimed when the DID is deleted.
#### Value
```python
2000000000000000
```
#### Python
```python
constant = substrate.get_constant('Did', 'BaseDeposit')
```
---------
### Fee
 The amount of balance that will be taken for each DID as a fee to
 incentivise fair use of the on chain storage. The fee will not get
 refunded when the DID is deleted.
#### Value
```python
50000000000000
```
#### Python
```python
constant = substrate.get_constant('Did', 'Fee')
```
---------
### KeyDeposit
 The amount of balance that will be taken for each added key as a
 deposit to incentivise fair use of the on chain storage.
#### Value
```python
1750000000000
```
#### Python
```python
constant = substrate.get_constant('Did', 'KeyDeposit')
```
---------
### MaxBlocksTxValidity
 The maximum number of blocks a DID-authorized operation is
 considered valid after its creation.
#### Value
```python
300
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxBlocksTxValidity')
```
---------
### MaxNewKeyAgreementKeys
 Maximum number of key agreement keys that can be added in a creation
 operation.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxNewKeyAgreementKeys')
```
---------
### MaxNumberOfServicesPerDid
 The maximum number of services that can be stored under a DID.
#### Value
```python
25
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxNumberOfServicesPerDid')
```
---------
### MaxNumberOfTypesPerService
 The maximum number of a types description for a service endpoint.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxNumberOfTypesPerService')
```
---------
### MaxNumberOfUrlsPerService
 The maximum number of a URLs for a service endpoint.
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxNumberOfUrlsPerService')
```
---------
### MaxPublicKeysPerDid
 Maximum number of total public keys which can be stored per DID key
 identifier. This includes the ones currently used for
 authentication, key agreement, attestation, and delegation.
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxPublicKeysPerDid')
```
---------
### MaxServiceIdLength
 The maximum length of a service ID.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxServiceIdLength')
```
---------
### MaxServiceTypeLength
 The maximum length of a service type description.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxServiceTypeLength')
```
---------
### MaxServiceUrlLength
 The maximum length of a service URL.
#### Value
```python
200
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxServiceUrlLength')
```
---------
### MaxTotalKeyAgreementKeys
 Maximum number of total key agreement keys that can be stored for a
 DID subject.

 Should be greater than `MaxNewKeyAgreementKeys`.
#### Value
```python
19
```
#### Python
```python
constant = substrate.get_constant('Did', 'MaxTotalKeyAgreementKeys')
```
---------
### ServiceEndpointDeposit
 The amount of balance that will be taken for each service endpoint
 as a deposit to incentivise fair use of the on chain storage. The
 deposit can be reclaimed when the service endpoint is removed or the
 DID deleted.
#### Value
```python
81400000000000
```
#### Python
```python
constant = substrate.get_constant('Did', 'ServiceEndpointDeposit')
```
---------
## Errors

---------
### AlreadyDeleted
The DID has already been previously deleted.

---------
### AlreadyExists
The DID with the given identifier is already present on chain.

---------
### BadDidOrigin
The DID call was submitted by the wrong account

---------
### Internal
An error that is not supposed to take place, yet it happened.

---------
### InvalidDidAuthorizationCall
The call had parameters that conflicted with each other
or were invalid.

---------
### InvalidNonce
The DID operation nonce is not equal to the current DID nonce + 1.

---------
### InvalidServiceEncoding
One of the service endpoint details contains non-ASCII characters.

---------
### InvalidSignature
The DID operation signature is invalid for the payload and the
verification key provided.

---------
### InvalidSignatureFormat
The DID operation signature is not in the format the verification
key expects.

---------
### MaxKeyAgreementKeysExceeded
The maximum number of key agreements has been reached for the DID
subject.

---------
### MaxNewKeyAgreementKeysLimitExceeded
A number of new key agreement keys greater than the maximum allowed
has been provided.

---------
### MaxNumberOfServicesExceeded
The maximum number of service endpoints for a DID has been exceeded.

---------
### MaxNumberOfTypesPerServiceExceeded
The maximum number of types for a service endpoint has been
exceeded.

---------
### MaxNumberOfUrlsPerServiceExceeded
The maximum number of URLs for a service endpoint has been exceeded.

---------
### MaxPublicKeysExceeded
The maximum number of public keys for this DID key identifier has
been reached.

---------
### MaxServiceIdLengthExceeded
The service endpoint ID exceeded the maximum allowed length.

---------
### MaxServiceTypeLengthExceeded
One of the service endpoint types exceeded the maximum allowed
length.

---------
### MaxServiceUrlLengthExceeded
One of the service endpoint URLs exceeded the maximum allowed
length.

---------
### MaxStoredEndpointsCountExceeded
The number of service endpoints stored under the DID is larger than
the number of endpoints to delete.

---------
### NotFound
No DID with the given identifier is present on chain.

---------
### NotOwnerOfDeposit
Only the owner of the deposit can reclaim its reserved balance.

---------
### ServiceAlreadyExists
A service with the provided ID is already present for the given DID.

---------
### ServiceNotFound
A service with the provided ID is not present under the given DID.

---------
### TransactionExpired
The block number provided in a DID-authorized operation is invalid.

---------
### UnableToPayFees
The origin is unable to reserve the deposit and pay the fee.

---------
### UnsupportedDidAuthorizationCall
The called extrinsic does not support DID authorisation.

---------
### VerificationKeyNotFound
One or more verification keys referenced are not stored in the set
of verification keys.

---------