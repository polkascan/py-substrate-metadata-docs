
# Utility

---------
## Calls

---------
### as_derivative
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `u16` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'as_derivative', {'call': 'Call', 'index': 'u16'}
)
```

---------
### batch
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'batch', {'calls': ['Call']}
)
```

---------
### batch_all
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'batch_all', {'calls': ['Call']}
)
```

---------
### dispatch_as
#### Attributes
| Name | Type |
| -------- | -------- | 
| as_origin | `Box<T::PalletsOrigin>` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'dispatch_as', {
    'as_origin': {
        'Council': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'TechnicalCommittee': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'Void': (),
        'system': {
            'None': None,
            'Root': None,
            'Signed': 'AccountId',
        },
        None: None,
    },
    'call': 'Call',
}
)
```

---------
### force_batch
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'force_batch', {'calls': ['Call']}
)
```

---------
### with_weight
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::RuntimeCall>` | 
| weight | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'with_weight', {
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
### BatchCompleted
#### Attributes
No attributes

---------
### BatchCompletedWithErrors
#### Attributes
No attributes

---------
### BatchInterrupted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `u32` | ```u32```
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
### DispatchedAs
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### ItemCompleted
#### Attributes
No attributes

---------
### ItemFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
## Constants

---------
### batched_calls_limit
#### Value
```python
10922
```
#### Python
```python
constant = substrate.get_constant('Utility', 'batched_calls_limit')
```
---------
## Errors

---------
### TooManyCalls

---------