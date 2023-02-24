
# Sudo

---------
## Calls

---------
### set_key
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Sudo', 'set_key', {
    'new': {
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
### sudo
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Sudo', 'sudo', {'call': 'Call'}
)
```

---------
### sudo_as
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Sudo', 'sudo_as', {
    'call': 'Call',
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
### sudo_unchecked_weight
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::RuntimeCall>` | 
| weight | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'Sudo', 'sudo_unchecked_weight', {
    'call': 'Call',
    'weight': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
## Events

---------
### KeyChanged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_sudoer | `Option<T::AccountId>` | ```(None, 'AccountId')```

---------
### Sudid
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sudo_result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### SudoAsDone
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sudo_result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
## Storage functions

---------
### Key

#### Python
```python
result = substrate.query(
    'Sudo', 'Key', []
)
```

#### Return value
```python
'AccountId'
```
---------
## Errors

---------
### RequireSudo

---------