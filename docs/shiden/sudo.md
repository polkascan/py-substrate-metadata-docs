
# Sudo

---------
## Calls

---------
### set_key
See [`Pallet::set_key`].
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
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### sudo
See [`Pallet::sudo`].
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
See [`Pallet::sudo_as`].
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
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### sudo_unchecked_weight
See [`Pallet::sudo_unchecked_weight`].
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
The \[sudoer\] just switched identity; the old key is supplied if one existed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_sudoer | `Option<T::AccountId>` | ```(None, 'AccountId')```

---------
### Sudid
A sudo just took place. \[result\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sudo_result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}}```

---------
### SudoAsDone
A sudo just took place. \[result\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sudo_result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}}```

---------
## Storage functions

---------
### Key
 The `AccountId` of the sudo key.

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
Sender must be the Sudo account

---------