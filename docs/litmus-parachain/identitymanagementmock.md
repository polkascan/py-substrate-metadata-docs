
# IdentityManagementMock

---------
## Calls

---------
### add_to_whitelist
add an account to the whitelist
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagementMock', 'add_to_whitelist', {'account': 'AccountId'}
)
```

---------
### challenge_code_generated
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `AesOutput` | 
| identity | `AesOutput` | 
| code | `AesOutput` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagementMock', 'challenge_code_generated', {
    'account': {
        'aad': 'Bytes',
        'ciphertext': 'Bytes',
        'nonce': '[u8; 12]',
    },
    'code': {
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
### identity_linked
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `AesOutput` | 
| identity | `AesOutput` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagementMock', 'identity_linked', {
    'account': {
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
### identity_unlinked
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `AesOutput` | 
| identity | `AesOutput` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagementMock', 'identity_unlinked', {
    'account': {
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
| account | `AesOutput` | 
| identity | `AesOutput` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagementMock', 'identity_verified', {
    'account': {
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
### link_identity
Link an identity
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| encrypted_identity | `Vec<u8>` | 
| encrypted_metadata | `Option<Vec<u8>>` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagementMock', 'link_identity', {
    'encrypted_identity': 'Bytes',
    'encrypted_metadata': (
        None,
        'Bytes',
    ),
    'shard': '[u8; 32]',
}
)
```

---------
### remove_from_whitelist
remove an account from the whitelist
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagementMock', 'remove_from_whitelist', {'account': 'AccountId'}
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
    'shard': '[u8; 32]',
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
### unlink_identity
Unlink an identity
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| encrypted_identity | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagementMock', 'unlink_identity', {
    'encrypted_identity': 'Bytes',
    'shard': '[u8; 32]',
}
)
```

---------
### user_shielding_key_set
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `AesOutput` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagementMock', 'user_shielding_key_set', {
    'account': {
        'aad': 'Bytes',
        'ciphertext': 'Bytes',
        'nonce': '[u8; 12]',
    },
}
)
```

---------
### verify_identity
Verify a linked identity
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
    'shard': '[u8; 32]',
}
)
```

---------
## Events

---------
### ChallengeCodeGenerated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```
| identity | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```
| code | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```

---------
### ChallengeCodeGeneratedPlain
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| identity | `Identity` | ```{'web_type': {'Web2': ('Twitter', 'Discord', 'Github'), 'Web3': {'Substrate': ('Polkadot', 'Kusama', 'Litentry', 'Litmus'), 'Evm': ('Ethereum', 'BSC')}}, 'handle': {'Address32': '[u8; 32]', 'Address20': '[u8; 20]', 'String': 'Bytes'}}```
| code | `ChallengeCode` | ```[u8; 16]```

---------
### IdentityLinked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```
| identity | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```

---------
### IdentityLinkedPlain
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| identity | `Identity` | ```{'web_type': {'Web2': ('Twitter', 'Discord', 'Github'), 'Web3': {'Substrate': ('Polkadot', 'Kusama', 'Litentry', 'Litmus'), 'Evm': ('Ethereum', 'BSC')}}, 'handle': {'Address32': '[u8; 32]', 'Address20': '[u8; 20]', 'String': 'Bytes'}}```

---------
### IdentityUnlinked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```
| identity | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```

---------
### IdentityUnlinkedPlain
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| identity | `Identity` | ```{'web_type': {'Web2': ('Twitter', 'Discord', 'Github'), 'Web3': {'Substrate': ('Polkadot', 'Kusama', 'Litentry', 'Litmus'), 'Evm': ('Ethereum', 'BSC')}}, 'handle': {'Address32': '[u8; 32]', 'Address20': '[u8; 20]', 'String': 'Bytes'}}```

---------
### IdentityVerified
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```
| identity | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```

---------
### IdentityVerifiedPlain
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| identity | `Identity` | ```{'web_type': {'Web2': ('Twitter', 'Discord', 'Github'), 'Web3': {'Substrate': ('Polkadot', 'Kusama', 'Litentry', 'Litmus'), 'Evm': ('Ethereum', 'BSC')}}, 'handle': {'Address32': '[u8; 32]', 'Address20': '[u8; 20]', 'String': 'Bytes'}}```

---------
### LinkIdentityRequested
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```[u8; 32]```

---------
### SetUserShieldingKeyRequested
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```[u8; 32]```

---------
### SomeError
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| func | `Vec<u8>` | ```Bytes```
| error | `Vec<u8>` | ```Bytes```

---------
### UnlinkIdentityRequested
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```[u8; 32]```

---------
### UserShieldingKeySet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```

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
| shard | `ShardIdentifier` | ```[u8; 32]```

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
        'handle': {
            'Address20': '[u8; 20]',
            'Address32': '[u8; 32]',
            'String': 'Bytes',
        },
        'web_type': {
            'Web2': (
                'Twitter',
                'Discord',
                'Github',
            ),
            'Web3': {
                'Evm': (
                    'Ethereum',
                    'BSC',
                ),
                'Substrate': (
                    'Polkadot',
                    'Kusama',
                    'Litentry',
                    'Litmus',
                ),
            },
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
### IDGraphs
 ID graph is per Litentry account + identity

#### Python
```python
result = substrate.query(
    'IdentityManagementMock', 'IDGraphs', [
    'AccountId',
    {
        'handle': {
            'Address20': '[u8; 20]',
            'Address32': '[u8; 32]',
            'String': 'Bytes',
        },
        'web_type': {
            'Web2': (
                'Twitter',
                'Discord',
                'Github',
            ),
            'Web3': {
                'Evm': (
                    'Ethereum',
                    'BSC',
                ),
                'Substrate': (
                    'Polkadot',
                    'Kusama',
                    'Litentry',
                    'Litmus',
                ),
            },
        },
    },
]
)
```

#### Return value
```python
{
    'is_verified': 'bool',
    'linking_request_block': (None, 'u32'),
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
### WhitelistedCallers

#### Python
```python
result = substrate.query(
    'IdentityManagementMock', 'WhitelistedCallers', ['AccountId']
)
```

#### Return value
```python
()
```
---------
## Constants

---------
### MaxVerificationDelay
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('IdentityManagementMock', 'MaxVerificationDelay')
```
---------
## Errors

---------
### CallerNotWhitelisted
caller is not in whitelist (therefore disallowed to call some extrinsics)

---------
### ChallengeCodeNotExist
the challenge code doesn&\#x27;t exist

---------
### IdentityAlreadyExist
identity already exists when linking an identity

---------
### IdentityNotExist
identity not exist when unlinking an identity

---------
### LinkingRequestBlockZero
the linking request block is zero

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
### WrongIdentityHanldeType
wrong identity handle type

---------
### WrongSignatureType
wrong signature type

---------
### WrongWeb3NetworkType
wrong web3 network type

---------