
# SudoOrigin

---------
## Calls

---------
### sudo
Authenticates the SudoOrigin and dispatches a function call with `Root` origin.

\# &lt;weight&gt;
- O(1).
- Limited storage reads.
- One DB write (event).
- Weight of derivative `call` execution + 10,000.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'SudoOrigin', 'sudo', {'call': 'Call'}
)
```

---------
### sudo_as
Authenticates the SudoOrigin and dispatches a function call with `Signed` origin from
a given account.

\# &lt;weight&gt;
- O(1).
- Limited storage reads.
- One DB write (event).
- Weight of derivative `call` execution + 10,000.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'SudoOrigin', 'sudo_as', {
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
Authenticates the SudoOrigin and dispatches a function call with `Root` origin.
This function does not check the weight of the call, and instead allows the
SudoOrigin to specify the weight of the call.

\# &lt;weight&gt;
- O(1).
- The weight of this call is defined by the caller.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::RuntimeCall>` | 
| weight | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'SudoOrigin', 'sudo_unchecked_weight', {
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
### SuOriginDid
A sudo just took place. \[result\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### SuOriginDoAsDone
A sudo just took place. \[result\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------