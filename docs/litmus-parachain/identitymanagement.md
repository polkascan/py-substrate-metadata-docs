
# IdentityManagement

---------
## Calls

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
    'IdentityManagement', 'challenge_code_generated', {
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
    'IdentityManagement', 'identity_linked', {
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
    'IdentityManagement', 'identity_unlinked', {
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
    'IdentityManagement', 'identity_verified', {
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
    'IdentityManagement', 'link_identity', {
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
| func | `Vec<u8>` | 
| error | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagement', 'some_error', {'error': 'Bytes', 'func': 'Bytes'}
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
    'IdentityManagement', 'unlink_identity', {
    'encrypted_identity': 'Bytes',
    'shard': '[u8; 32]',
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
| account | `AesOutput` | 

#### Python
```python
call = substrate.compose_call(
    'IdentityManagement', 'user_shielding_key_set', {
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
### ChallengeCodeGenerated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```
| identity | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```
| code | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```

---------
### IdentityLinked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```
| identity | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```

---------
### IdentityUnlinked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```
| identity | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```

---------
### IdentityVerified
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```
| identity | `AesOutput` | ```{'ciphertext': 'Bytes', 'aad': 'Bytes', 'nonce': '[u8; 12]'}```

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
### VerifyIdentityRequested
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```[u8; 32]```

---------