
# XSystem

---------
## Calls

---------
### modify_paused
Modify the paused status of the given pallet call.

This is a root-only operation.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pallet | `Vec<u8>` | 
| call | `Option<Vec<u8>>` | 
| should_paused | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'XSystem', 'modify_paused', {
    'call': (None, 'Bytes'),
    'pallet': 'Bytes',
    'should_paused': 'bool',
}
)
```

---------
### toggle_blacklist
Toggle the blacklist status of the given account id.

This is a root-only operation.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| should_blacklist | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'XSystem', 'toggle_blacklist', {
    'should_blacklist': 'bool',
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
## Events

---------
### Blacklisted
An account was added to the blacklist. [who]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### Unblacklisted
An account was removed from the blacklist. [who]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### Blacklist
 The accounts that are blocked

#### Python
```python
result = substrate.query(
    'XSystem', 'Blacklist', ['AccountId']
)
```

#### Return value
```python
'bool'
```
---------
### NetworkProps
 Network property (Mainnet / Testnet).

#### Python
```python
result = substrate.query(
    'XSystem', 'NetworkProps', []
)
```

#### Return value
```python
('Mainnet', 'Testnet')
```
---------
### Paused
 Paused pallet call

#### Python
```python
result = substrate.query(
    'XSystem', 'Paused', ['Bytes']
)
```

#### Return value
```python
'scale_info::399'
```
---------