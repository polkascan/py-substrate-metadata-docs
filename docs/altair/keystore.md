
# Keystore

---------
## Calls

---------
### add_keys
Add keys to the storages.
#### Attributes
| Name | Type |
| -------- | -------- | 
| keys | `Vec<AddKey<T::Hash>>` | 

#### Python
```python
call = substrate.compose_call(
    'Keystore', 'add_keys', {
    'keys': [
        {
            'key': 'scale_info::12',
            'key_type': (
                'ECDSA',
                'EDDSA',
            ),
            'purpose': (
                'P2PDiscovery',
                'P2PDocumentSigning',
            ),
        },
    ],
}
)
```

---------
### revoke_keys
Revoke keys with specified purpose.
#### Attributes
| Name | Type |
| -------- | -------- | 
| keys | `Vec<T::Hash>` | 
| key_purpose | `KeyPurpose` | 

#### Python
```python
call = substrate.compose_call(
    'Keystore', 'revoke_keys', {
    'key_purpose': (
        'P2PDiscovery',
        'P2PDocumentSigning',
    ),
    'keys': ['scale_info::12'],
}
)
```

---------
### set_deposit
Set a new key deposit.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_deposit | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Keystore', 'set_deposit', {'new_deposit': 'u128'}
)
```

---------
## Events

---------
### DepositSet
A deposit was set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| new_deposit | `T::Balance` | ```u128```

---------
### KeyAdded
A key was added.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| key | `T::Hash` | ```scale_info::12```
| purpose | `KeyPurpose` | ```('P2PDiscovery', 'P2PDocumentSigning')```
| key_type | `KeyType` | ```('ECDSA', 'EDDSA')```

---------
### KeyRevoked
A key was revoked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| key | `T::Hash` | ```scale_info::12```
| block_number | `T::BlockNumber` | ```u32```

---------
## Storage functions

---------
### KeyDeposit
 Stores the current deposit that will be taken when saving a key.

#### Python
```python
result = substrate.query(
    'Keystore', 'KeyDeposit', []
)
```

#### Return value
```python
'u128'
```
---------
### Keys
 Keys that are currently stored.

#### Python
```python
result = substrate.query(
    'Keystore', 'Keys', [
    'AccountId',
    (
        'scale_info::12',
        (
            'P2PDiscovery',
            'P2PDocumentSigning',
        ),
    ),
]
)
```

#### Return value
```python
{
    'deposit': 'u128',
    'key_type': ('ECDSA', 'EDDSA'),
    'purpose': ('P2PDiscovery', 'P2PDocumentSigning'),
    'revoked_at': (None, 'u32'),
}
```
---------
### LastKeyByPurpose
 Storage used for retrieving last key by purpose.

#### Python
```python
result = substrate.query(
    'Keystore', 'LastKeyByPurpose', [
    'AccountId',
    (
        'P2PDiscovery',
        'P2PDocumentSigning',
    ),
]
)
```

#### Return value
```python
'scale_info::12'
```
---------
## Constants

---------
### MaxKeys
 Maximum number of keys that can be added at a time.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Keystore', 'MaxKeys')
```
---------
## Errors

---------
### KeyAlreadyExists
The key already exists.

---------
### KeyAlreadyRevoked
The key was already revoked.

---------
### KeyNotFound
The key was not found in storage.

---------
### NoKeys
No keys were provided.

---------
### TooManyKeys
More than T::MaxKeys keys were provided.

---------