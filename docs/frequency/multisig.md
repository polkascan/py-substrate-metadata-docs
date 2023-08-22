
# Multisig

---------
## Calls

---------
### approve_as_multi
#### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `u16` | 
| other_signatories | `Vec<T::AccountId>` | 
| maybe_timepoint | `Option<Timepoint<T::BlockNumber>>` | 
| call_hash | `[u8; 32]` | 
| max_weight | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'Multisig', 'approve_as_multi', {
    'call_hash': '[u8; 32]',
    'max_weight': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
    'maybe_timepoint': (
        None,
        {
            'height': 'u32',
            'index': 'u32',
        },
    ),
    'other_signatories': ['AccountId'],
    'threshold': 'u16',
}
)
```

---------
### as_multi
#### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `u16` | 
| other_signatories | `Vec<T::AccountId>` | 
| maybe_timepoint | `Option<Timepoint<T::BlockNumber>>` | 
| call | `Box<<T as Config>::RuntimeCall>` | 
| max_weight | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'Multisig', 'as_multi', {
    'call': 'Call',
    'max_weight': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
    'maybe_timepoint': (
        None,
        {
            'height': 'u32',
            'index': 'u32',
        },
    ),
    'other_signatories': ['AccountId'],
    'threshold': 'u16',
}
)
```

---------
### as_multi_threshold_1
#### Attributes
| Name | Type |
| -------- | -------- | 
| other_signatories | `Vec<T::AccountId>` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Multisig', 'as_multi_threshold_1', {
    'call': 'Call',
    'other_signatories': ['AccountId'],
}
)
```

---------
### cancel_as_multi
#### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `u16` | 
| other_signatories | `Vec<T::AccountId>` | 
| timepoint | `Timepoint<T::BlockNumber>` | 
| call_hash | `[u8; 32]` | 

#### Python
```python
call = substrate.compose_call(
    'Multisig', 'cancel_as_multi', {
    'call_hash': '[u8; 32]',
    'other_signatories': ['AccountId'],
    'threshold': 'u16',
    'timepoint': {
        'height': 'u32',
        'index': 'u32',
    },
}
)
```

---------
## Events

---------
### MultisigApproval
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| approving | `T::AccountId` | ```AccountId```
| timepoint | `Timepoint<T::BlockNumber>` | ```{'height': 'u32', 'index': 'u32'}```
| multisig | `T::AccountId` | ```AccountId```
| call_hash | `CallHash` | ```[u8; 32]```

---------
### MultisigCancelled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| cancelling | `T::AccountId` | ```AccountId```
| timepoint | `Timepoint<T::BlockNumber>` | ```{'height': 'u32', 'index': 'u32'}```
| multisig | `T::AccountId` | ```AccountId```
| call_hash | `CallHash` | ```[u8; 32]```

---------
### MultisigExecuted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| approving | `T::AccountId` | ```AccountId```
| timepoint | `Timepoint<T::BlockNumber>` | ```{'height': 'u32', 'index': 'u32'}```
| multisig | `T::AccountId` | ```AccountId```
| call_hash | `CallHash` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### NewMultisig
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| approving | `T::AccountId` | ```AccountId```
| multisig | `T::AccountId` | ```AccountId```
| call_hash | `CallHash` | ```[u8; 32]```

---------
## Storage functions

---------
### Multisigs

#### Python
```python
result = substrate.query(
    'Multisig', 'Multisigs', ['AccountId', '[u8; 32]']
)
```

#### Return value
```python
{
    'approvals': ['AccountId'],
    'deposit': 'u128',
    'depositor': 'AccountId',
    'when': {'height': 'u32', 'index': 'u32'},
}
```
---------
## Constants

---------
### DepositBase
#### Value
```python
2008800000
```
#### Python
```python
constant = substrate.get_constant('Multisig', 'DepositBase')
```
---------
### DepositFactor
#### Value
```python
3200000
```
#### Python
```python
constant = substrate.get_constant('Multisig', 'DepositFactor')
```
---------
### MaxSignatories
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Multisig', 'MaxSignatories')
```
---------
## Errors

---------
### AlreadyApproved

---------
### AlreadyStored

---------
### MaxWeightTooLow

---------
### MinimumThreshold

---------
### NoApprovalsNeeded

---------
### NoTimepoint

---------
### NotFound

---------
### NotOwner

---------
### SenderInSignatories

---------
### SignatoriesOutOfOrder

---------
### TooFewSignatories

---------
### TooManySignatories

---------
### UnexpectedTimepoint

---------
### WrongTimepoint

---------