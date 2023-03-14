
# IdentityManagement

---------
## Calls

---------
### add_delegatee
add an account to the delegatees
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagement', 'add_delegatee', {'account': 'AccountId'}
)
```

---------
### create_identity
Create an identity
We do the origin check for this extrinsic, it has to be
- either the caller him/herself, i.e. ensure_signed(origin)? == who
- or from a delegatee in the list
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| user | `T::AccountId` | 
| encrypted_identity | `Vec<u8>` | 
| encrypted_metadata | `Option<Vec<u8>>` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagement', 'create_identity', {
    'encrypted_identity': 'Bytes',
    'encrypted_metadata': (
        None,
        'Bytes',
    ),
    'shard': '[u8; 32]',
    'user': 'AccountId',
}
)
```

---------
### identity_created
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `T::AccountId` | 
| identity | `AesOutput` | 
| code | `AesOutput` | 
| id_graph | `AesOutput` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagement', 'identity_created', {
    'account': 'AccountId',
    'code': {
        'aad': 'Bytes',
        'ciphertext': 'Bytes',
        'nonce': '[u8; 12]',
    },
    'id_graph': {
        'aad': 'Bytes',
        'ciphertext': 'Bytes',
        'nonce': '[u8; 12]',
    },
    'identity': {
        'aad': 'Bytes',
        'ciphertext': 'Bytes',
        'nonce': '[u8; 12]',
    },
}
)
```

---------
### identity_removed
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `T::AccountId` | 
| identity | `AesOutput` | 
| id_graph | `AesOutput` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagement', 'identity_removed', {
    'account': 'AccountId',
    'id_graph': {
        'aad': 'Bytes',
        'ciphertext': 'Bytes',
        'nonce': '[u8; 12]',
    },
    'identity': {
        'aad': 'Bytes',
        'ciphertext': 'Bytes',
        'nonce': '[u8; 12]',
    },
}
)
```

---------
### identity_verified
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `T::AccountId` | 
| identity | `AesOutput` | 
| id_graph | `AesOutput` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagement', 'identity_verified', {
    'account': 'AccountId',
    'id_graph': {
        'aad': 'Bytes',
        'ciphertext': 'Bytes',
        'nonce': '[u8; 12]',
    },
    'identity': {
        'aad': 'Bytes',
        'ciphertext': 'Bytes',
        'nonce': '[u8; 12]',
    },
}
)
```

---------
### remove_delegatee
remove an account from the delegatees
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagement', 'remove_delegatee', {'account': 'AccountId'}
)
```

---------
### remove_identity
Remove an identity
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| encrypted_identity | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagement', 'remove_identity', {
    'encrypted_identity': 'Bytes',
    'shard': '[u8; 32]',
}
)
```

---------
### set_user_shielding_key
Set or update user&\#x27;s shielding key
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| encrypted_key | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagement', 'set_user_shielding_key', {
    'encrypted_key': 'Bytes',
    'shard': '[u8; 32]',
}
)
```

---------
### some_error
#### Attributes
| Name | Type |
| -------- | -------- | 
| error | `IMPError` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagement', 'some_error', {
    'error': {
        'CreateIdentityHandlingFailed': None,
        'DecodeHexFailed': 'Bytes',
        'HttpRequestFailed': 'Bytes',
        'InvalidIdentity': None,
        'RecoverEvmAddressFailed': None,
        'RecoverSubstratePubkeyFailed': None,
        'RemoveIdentityHandlingFailed': None,
        'SetUserShieldingKeyHandlingFailed': None,
        'UnexpectedMessage': None,
        'VerifyEvmSignatureFailed': None,
        'VerifyIdentityHandlingFailed': None,
        'VerifySubstrateSignatureFailed': None,
        'WrongIdentityHandleType': None,
        'WrongSignatureType': None,
        'WrongWeb2Handle': None,
    },
}
)
```

---------
### user_shielding_key_set
---------------------------------------------------
The following extrinsics are supposed to be called by TEE only
---------------------------------------------------
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagement', 'user_shielding_key_set', {'account': 'AccountId'}
)
```

---------
### verify_identity
Verify an identity
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| encrypted_identity | `Vec<u8>` | 
| encrypted_validation_data | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagement', 'verify_identity', {
    'encrypted_identity': 'Bytes',
    'encrypted_validation_data': 'Bytes',
    'shard': '[u8; 32]',
}
)
```

---------
## Events

---------
### CreateIdentityHandlingFailed
#### Attributes
No attributes

---------
### CreateIdentityRequested
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```[u8; 32]```

---------
### DecodeHexFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| reason | `ErrorString` | ```Bytes```

---------
### DelegateeAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
### DelegateeRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
### HttpRequestFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| reason | `ErrorString` | ```Bytes```

---------
### IdentityCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| identity | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```
| code | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```
| id_graph | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```

---------
### IdentityRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| identity | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```
| id_graph | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```

---------
### IdentityVerified
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| identity | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```
| id_graph | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```

---------
### InvalidIdentity
#### Attributes
No attributes

---------
### RecoverEvmAddressFailed
#### Attributes
No attributes

---------
### RecoverSubstratePubkeyFailed
#### Attributes
No attributes

---------
### RemoveIdentityHandlingFailed
#### Attributes
No attributes

---------
### RemoveIdentityRequested
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```[u8; 32]```

---------
### SetUserShieldingKeyHandlingFailed
#### Attributes
No attributes

---------
### SetUserShieldingKeyRequested
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```[u8; 32]```

---------
### UnexpectedMessage
#### Attributes
No attributes

---------
### UserShieldingKeySet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
### VerifyEvmSignatureFailed
#### Attributes
No attributes

---------
### VerifyIdentityHandlingFailed
#### Attributes
No attributes

---------
### VerifyIdentityRequested
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```[u8; 32]```

---------
### VerifySubstrateSignatureFailed
#### Attributes
No attributes

---------
### WrongIdentityHandleType
#### Attributes
No attributes

---------
### WrongSignatureType
#### Attributes
No attributes

---------
### WrongWeb2Handle
#### Attributes
No attributes

---------
## Storage functions

---------
### Delegatee
 delegatees who are authorised to send extrinsics(currently only `create_identity`)
 on behalf of the users

#### Python
```python
result = substrate.query(
    'IdentityManagement', 'Delegatee', ['AccountId']
)
```

#### Return value
```python
()
```
---------
## Errors

---------
### DelegateeNotExist
a delegatee doesn&\#x27;t exist

---------
### UnauthorisedUser
a `create_identity` request from unauthorised user

---------