
# Msa

---------
## Calls

---------
### add_public_key_to_msa
#### Attributes
| Name | Type |
| -------- | -------- | 
| msa_owner_public_key | `T::AccountId` | 
| msa_owner_proof | `MultiSignature` | 
| new_key_owner_proof | `MultiSignature` | 
| add_key_payload | `AddKeyData<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Msa', 'add_public_key_to_msa', {
    'add_key_payload': {
        'expiration': 'u32',
        'msa_id': 'u64',
        'new_public_key': 'AccountId',
    },
    'msa_owner_proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
    'msa_owner_public_key': 'AccountId',
    'new_key_owner_proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### create
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Msa', 'create', {}
)
```

---------
### create_provider
#### Attributes
| Name | Type |
| -------- | -------- | 
| provider_name | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Msa', 'create_provider', {'provider_name': 'Bytes'}
)
```

---------
### create_sponsored_account_with_delegation
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegator_key | `T::AccountId` | 
| proof | `MultiSignature` | 
| add_provider_payload | `AddProvider` | 

#### Python
```python
call = substrate.compose_call(
    'Msa', 'create_sponsored_account_with_delegation', {
    'add_provider_payload': {
        'authorized_msa_id': 'u64',
        'expiration': 'u32',
        'schema_ids': ['u16'],
    },
    'delegator_key': 'AccountId',
    'proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### delete_msa_public_key
#### Attributes
| Name | Type |
| -------- | -------- | 
| public_key_to_delete | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Msa', 'delete_msa_public_key', {'public_key_to_delete': 'AccountId'}
)
```

---------
### grant_delegation
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegator_key | `T::AccountId` | 
| proof | `MultiSignature` | 
| add_provider_payload | `AddProvider` | 

#### Python
```python
call = substrate.compose_call(
    'Msa', 'grant_delegation', {
    'add_provider_payload': {
        'authorized_msa_id': 'u64',
        'expiration': 'u32',
        'schema_ids': ['u16'],
    },
    'delegator_key': 'AccountId',
    'proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### grant_schema_permissions
#### Attributes
| Name | Type |
| -------- | -------- | 
| provider_msa_id | `MessageSourceId` | 
| schema_ids | `Vec<SchemaId>` | 

#### Python
```python
call = substrate.compose_call(
    'Msa', 'grant_schema_permissions', {
    'provider_msa_id': 'u64',
    'schema_ids': ['u16'],
}
)
```

---------
### retire_msa
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Msa', 'retire_msa', {}
)
```

---------
### revoke_delegation_by_delegator
#### Attributes
| Name | Type |
| -------- | -------- | 
| provider_msa_id | `MessageSourceId` | 

#### Python
```python
call = substrate.compose_call(
    'Msa', 'revoke_delegation_by_delegator', {'provider_msa_id': 'u64'}
)
```

---------
### revoke_delegation_by_provider
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegator | `MessageSourceId` | 

#### Python
```python
call = substrate.compose_call(
    'Msa', 'revoke_delegation_by_provider', {'delegator': 'u64'}
)
```

---------
### revoke_schema_permissions
#### Attributes
| Name | Type |
| -------- | -------- | 
| provider_msa_id | `MessageSourceId` | 
| schema_ids | `Vec<SchemaId>` | 

#### Python
```python
call = substrate.compose_call(
    'Msa', 'revoke_schema_permissions', {
    'provider_msa_id': 'u64',
    'schema_ids': ['u16'],
}
)
```

---------
## Events

---------
### DelegationGranted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| provider_id | `ProviderId` | ```u64```
| delegator_id | `DelegatorId` | ```u64```

---------
### DelegationRevoked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| provider_id | `ProviderId` | ```u64```
| delegator_id | `DelegatorId` | ```u64```

---------
### DelegationUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| provider_id | `ProviderId` | ```u64```
| delegator_id | `DelegatorId` | ```u64```

---------
### MsaCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```
| key | `T::AccountId` | ```AccountId```

---------
### MsaRetired
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```

---------
### ProviderCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| provider_id | `ProviderId` | ```u64```

---------
### PublicKeyAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```
| key | `T::AccountId` | ```AccountId```

---------
### PublicKeyDeleted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| key | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### CurrentMsaIdentifierMaximum

#### Python
```python
result = substrate.query(
    'Msa', 'CurrentMsaIdentifierMaximum', []
)
```

#### Return value
```python
'u64'
```
---------
### DelegatorAndProviderToDelegation

#### Python
```python
result = substrate.query(
    'Msa', 'DelegatorAndProviderToDelegation', ['u64', 'u64']
)
```

#### Return value
```python
{'revoked_at': 'u32', 'schema_permissions': 'scale_info::239'}
```
---------
### PayloadSignatureBucketCount

#### Python
```python
result = substrate.query(
    'Msa', 'PayloadSignatureBucketCount', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### PayloadSignatureRegistry

#### Python
```python
result = substrate.query(
    'Msa', 'PayloadSignatureRegistry', [
    'u32',
    {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
]
)
```

#### Return value
```python
'u32'
```
---------
### ProviderToRegistryEntry

#### Python
```python
result = substrate.query(
    'Msa', 'ProviderToRegistryEntry', ['u64']
)
```

#### Return value
```python
{'provider_name': 'Bytes'}
```
---------
### PublicKeyCountForMsaId

#### Python
```python
result = substrate.query(
    'Msa', 'PublicKeyCountForMsaId', ['u64']
)
```

#### Return value
```python
'u8'
```
---------
### PublicKeyToMsaId

#### Python
```python
result = substrate.query(
    'Msa', 'PublicKeyToMsaId', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### MaxProviderNameSize
#### Value
```python
16
```
#### Python
```python
constant = substrate.get_constant('Msa', 'MaxProviderNameSize')
```
---------
### MaxPublicKeysPerMsa
#### Value
```python
25
```
#### Python
```python
constant = substrate.get_constant('Msa', 'MaxPublicKeysPerMsa')
```
---------
### MaxSchemaGrantsPerDelegation
#### Value
```python
30
```
#### Python
```python
constant = substrate.get_constant('Msa', 'MaxSchemaGrantsPerDelegation')
```
---------
### MaxSignaturesPerBucket
#### Value
```python
50000
```
#### Python
```python
constant = substrate.get_constant('Msa', 'MaxSignaturesPerBucket')
```
---------
### MaxSignaturesStored
#### Value
```python
100000
```
#### Python
```python
constant = substrate.get_constant('Msa', 'MaxSignaturesStored')
```
---------
### MortalityWindowSize
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Msa', 'MortalityWindowSize')
```
---------
### NumberOfBuckets
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('Msa', 'NumberOfBuckets')
```
---------
## Errors

---------
### AddProviderSignatureVerificationFailed

---------
### CannotPredictValidityPastCurrentBlock

---------
### DelegationNotFound

---------
### DelegationRevoked

---------
### DuplicateProvider

---------
### DuplicateProviderRegistryEntry

---------
### ExceedsMaxProviderNameSize

---------
### ExceedsMaxSchemaGrantsPerDelegation

---------
### InvalidSchemaId

---------
### InvalidSelfProvider

---------
### InvalidSelfRemoval

---------
### InvalidSignature

---------
### KeyAlreadyRegistered

---------
### KeyLimitExceeded

---------
### MsaIdOverflow

---------
### MsaOwnershipInvalidSignature

---------
### NewKeyOwnershipInvalidSignature

---------
### NoKeyExists

---------
### NotKeyOwner

---------
### NotMsaOwner

---------
### ProofHasExpired

---------
### ProofNotYetValid

---------
### ProviderNotRegistered

---------
### SchemaNotGranted

---------
### SignatureAlreadySubmitted

---------
### SignatureRegistryLimitExceeded

---------
### UnauthorizedDelegator

---------
### UnauthorizedProvider

---------