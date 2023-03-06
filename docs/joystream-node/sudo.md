
# Sudo

---------
## Calls

---------
### set_key
Authenticates the current sudo key and sets the given AccountId (`new`) as the new sudo
key.

The dispatch origin for this call must be _Signed_.

\# &lt;weight&gt;
- O(1).
- Limited storage reads.
- One DB change.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'Sudo', 'set_key', {'new': 'AccountId'}
)
```

---------
### sudo
Authenticates the sudo key and dispatches a function call with `Root` origin.

The dispatch origin for this call must be _Signed_.

\# &lt;weight&gt;
- O(1).
- Limited storage reads.
- One DB write (event).
- Weight of derivative `call` execution + 10,000.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'Sudo', 'sudo', {'call': 'Call'}
)
```

---------
### sudo_as
Authenticates the sudo key and dispatches a function call with `Signed` origin from
a given account.

The dispatch origin for this call must be _Signed_.

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
| call | `Box<<T as Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'Sudo', 'sudo_as', {'call': 'Call', 'who': 'AccountId'}
)
```

---------
### sudo_unchecked_weight
Authenticates the sudo key and dispatches a function call with `Root` origin.
This function does not check the weight of the call, and instead allows the
Sudo user to specify the weight of the call.

The dispatch origin for this call must be _Signed_.

\# &lt;weight&gt;
- O(1).
- The weight of this call is defined by the caller.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::Call>` | 
| weight | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'Sudo', 'sudo_unchecked_weight', {'call': 'Call', 'weight': 'u64'}
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
| sudo_result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### SudoAsDone
A sudo just took place. \[result\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sudo_result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

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