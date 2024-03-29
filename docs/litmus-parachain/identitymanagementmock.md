
# IdentityManagementMock

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
    'IdentityManagementMock', 'add_delegatee', {'account': 'AccountId'}
)
```

---------
### create_identity
Create an identity
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
    'IdentityManagementMock', 'create_identity', {
    'encrypted_identity': 'Bytes',
    'encrypted_metadata': (
        None,
        'Bytes',
    ),
    'shard': 'scale_info::11',
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
    'IdentityManagementMock', 'identity_created', {
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
    'IdentityManagementMock', 'identity_removed', {
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
    'IdentityManagementMock', 'identity_verified', {
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
    'IdentityManagementMock', 'remove_delegatee', {'account': 'AccountId'}
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
    'IdentityManagementMock', 'remove_identity', {
    'encrypted_identity': 'Bytes',
    'shard': 'scale_info::11',
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
    'IdentityManagementMock', 'set_user_shielding_key', {
    'encrypted_key': 'Bytes',
    'shard': 'scale_info::11',
}
)
```

---------
### some_error
#### Attributes
| Name | Type |
| -------- | -------- | 
| func | `Vec<u8>` | 
| error | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagementMock', 'some_error', {'error': 'Bytes', 'func': 'Bytes'}
)
```

---------
### user_shielding_key_set
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagementMock', 'user_shielding_key_set', {'account': 'AccountId'}
)
```

---------
### verify_identity
Verify a created identity
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| encrypted_identity | `Vec<u8>` | 
| encrypted_validation_data | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagementMock', 'verify_identity', {
    'encrypted_identity': 'Bytes',
    'encrypted_validation_data': 'Bytes',
    'shard': 'scale_info::11',
}
)
```

---------
## Events

---------
### CreateIdentityRequested
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```scale_info::11```

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
### IdentityCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| identity | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```
| code | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```
| id_graph | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```

---------
### IdentityCreatedPlain
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| identity | `Identity` | ```{'Substrate': {'network': ('Polkadot', 'Kusama', 'Litentry', 'Litmus'), 'address': '[u8; 32]'}, 'Evm': {'network': ('Ethereum', 'BSC'), 'address': '[u8; 20]'}, 'Web2': {'network': ('Twitter', 'Discord', 'Github'), 'address': 'Bytes'}}```
| code | `ChallengeCode` | ```[u8; 16]```
| id_graph | `Vec<(Identity, IdentityContext<T>)>` | ```[({'Substrate': {'network': ('Polkadot', 'Kusama', 'Litentry', 'Litmus'), 'address': '[u8; 32]'}, 'Evm': {'network': ('Ethereum', 'BSC'), 'address': '[u8; 20]'}, 'Web2': {'network': ('Twitter', 'Discord', 'Github'), 'address': 'Bytes'}}, {'metadata': (None, 'Bytes'), 'creation_request_block': (None, 'u32'), 'verification_request_block': (None, 'u32'), 'is_verified': 'bool'})]```

---------
### IdentityRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| identity | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```
| id_graph | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```

---------
### IdentityRemovedPlain
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| identity | `Identity` | ```{'Substrate': {'network': ('Polkadot', 'Kusama', 'Litentry', 'Litmus'), 'address': '[u8; 32]'}, 'Evm': {'network': ('Ethereum', 'BSC'), 'address': '[u8; 20]'}, 'Web2': {'network': ('Twitter', 'Discord', 'Github'), 'address': 'Bytes'}}```
| id_graph | `Vec<(Identity, IdentityContext<T>)>` | ```[({'Substrate': {'network': ('Polkadot', 'Kusama', 'Litentry', 'Litmus'), 'address': '[u8; 32]'}, 'Evm': {'network': ('Ethereum', 'BSC'), 'address': '[u8; 20]'}, 'Web2': {'network': ('Twitter', 'Discord', 'Github'), 'address': 'Bytes'}}, {'metadata': (None, 'Bytes'), 'creation_request_block': (None, 'u32'), 'verification_request_block': (None, 'u32'), 'is_verified': 'bool'})]```

---------
### IdentityVerified
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| identity | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```
| id_graph | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```

---------
### IdentityVerifiedPlain
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| identity | `Identity` | ```{'Substrate': {'network': ('Polkadot', 'Kusama', 'Litentry', 'Litmus'), 'address': '[u8; 32]'}, 'Evm': {'network': ('Ethereum', 'BSC'), 'address': '[u8; 20]'}, 'Web2': {'network': ('Twitter', 'Discord', 'Github'), 'address': 'Bytes'}}```
| id_graph | `Vec<(Identity, IdentityContext<T>)>` | ```[({'Substrate': {'network': ('Polkadot', 'Kusama', 'Litentry', 'Litmus'), 'address': '[u8; 32]'}, 'Evm': {'network': ('Ethereum', 'BSC'), 'address': '[u8; 20]'}, 'Web2': {'network': ('Twitter', 'Discord', 'Github'), 'address': 'Bytes'}}, {'metadata': (None, 'Bytes'), 'creation_request_block': (None, 'u32'), 'verification_request_block': (None, 'u32'), 'is_verified': 'bool'})]```

---------
### RemoveIdentityRequested
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```scale_info::11```

---------
### SetUserShieldingKeyRequested
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```scale_info::11```

---------
### SomeError
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| func | `Vec<u8>` | ```Bytes```
| error | `Vec<u8>` | ```Bytes```

---------
### UserShieldingKeySet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
### UserShieldingKeySetPlain
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
### VerifyIdentityRequested
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```scale_info::11```

---------
## Storage functions

---------
### ChallengeCodes
 challenge code is per Litentry account + identity

#### Python
```python
result = substrate.query(
    'IdentityManagementMock', 'ChallengeCodes', [
    'AccountId',
    {
        'Evm': {
            'address': '[u8; 20]',
            'network': (
                'Ethereum',
                'BSC',
            ),
        },
        'Substrate': {
            'address': '[u8; 32]',
            'network': (
                'Polkadot',
                'Kusama',
                'Litentry',
                'Litmus',
            ),
        },
        'Web2': {
            'address': 'Bytes',
            'network': (
                'Twitter',
                'Discord',
                'Github',
            ),
        },
    },
]
)
```

#### Return value
```python
'[u8; 16]'
```
---------
### Delegatee
 delegatees who are authorised to send extrinsics(currently only `create_identity`)
 on behalf of the users

#### Python
```python
result = substrate.query(
    'IdentityManagementMock', 'Delegatee', ['AccountId']
)
```

#### Return value
```python
()
```
---------
### IDGraphs
 ID graph is per Litentry account + identity

#### Python
```python
result = substrate.query(
    'IdentityManagementMock', 'IDGraphs', [
    'AccountId',
    {
        'Evm': {
            'address': '[u8; 20]',
            'network': (
                'Ethereum',
                'BSC',
            ),
        },
        'Substrate': {
            'address': '[u8; 32]',
            'network': (
                'Polkadot',
                'Kusama',
                'Litentry',
                'Litmus',
            ),
        },
        'Web2': {
            'address': 'Bytes',
            'network': (
                'Twitter',
                'Discord',
                'Github',
            ),
        },
    },
]
)
```

#### Return value
```python
{
    'creation_request_block': (None, 'u32'),
    'is_verified': 'bool',
    'metadata': (None, 'Bytes'),
    'verification_request_block': (None, 'u32'),
}
```
---------
### UserShieldingKeys
 user shielding key is per Litentry account

#### Python
```python
result = substrate.query(
    'IdentityManagementMock', 'UserShieldingKeys', ['AccountId']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
## Constants

---------
### MaxVerificationDelay
#### Value
```python
150
```
#### Python
```python
constant = substrate.get_constant('IdentityManagementMock', 'MaxVerificationDelay')
```
---------
## Errors

---------
### ChallengeCodeNotExist
the challenge code doesn&\#x27;t exist

---------
### CreationRequestBlockZero
the creation request block is zero

---------
### DelegateeNotExist
a delegatee doesn&\#x27;t exist

---------
### IdentityAlreadyVerified
identity already verified when creating an identity

---------
### IdentityNotExist
identity not exist when removing an identity

---------
### IdentityShouldBeDisallowed
identity should be disallowed

---------
### RecoverEvmAddressFailed
fail to recover evm address

---------
### RecoverSubstratePubkeyFailed
recover substrate pubkey failed using ecdsa

---------
### ShieldingKeyDecryptionFailed
Error when decrypting using TEE&\#x27;shielding key

---------
### ShieldingKeyNotExist
no shielding key for a given AccountId

---------
### UnauthorisedUser
a `create_identity` request from unauthorised user

---------
### UnexpectedMessage
the message in validation data is unexpected

---------
### VerificationRequestTooEarly
a verification reqeust comes too early

---------
### VerificationRequestTooLate
a verification reqeust comes too late

---------
### VerifyEvmSignatureFailed
verify evm signature failed

---------
### VerifySubstrateSignatureFailed
verify substrate signature failed

---------
### WrongDecodedType
unexpected decoded type

---------
### WrongIdentityType
wrong identity type

---------
### WrongSignatureType
wrong signature type

---------