
# Multisig

---------
## Calls

---------
### approve_as_multi
See [`Pallet::approve_as_multi`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `u16` | 
| other_signatories | `Vec<T::AccountId>` | 
| maybe_timepoint | `Option<Timepoint<BlockNumberFor<T>>>` | 
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
See [`Pallet::as_multi`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `u16` | 
| other_signatories | `Vec<T::AccountId>` | 
| maybe_timepoint | `Option<Timepoint<BlockNumberFor<T>>>` | 
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
See [`Pallet::as_multi_threshold_1`].
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
See [`Pallet::cancel_as_multi`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `u16` | 
| other_signatories | `Vec<T::AccountId>` | 
| timepoint | `Timepoint<BlockNumberFor<T>>` | 
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
A multisig operation has been approved by someone.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| approving | `T::AccountId` | ```AccountId```
| timepoint | `Timepoint<BlockNumberFor<T>>` | ```{'height': 'u32', 'index': 'u32'}```
| multisig | `T::AccountId` | ```AccountId```
| call_hash | `CallHash` | ```[u8; 32]```

---------
### MultisigCancelled
A multisig operation has been cancelled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| cancelling | `T::AccountId` | ```AccountId```
| timepoint | `Timepoint<BlockNumberFor<T>>` | ```{'height': 'u32', 'index': 'u32'}```
| multisig | `T::AccountId` | ```AccountId```
| call_hash | `CallHash` | ```[u8; 32]```

---------
### MultisigExecuted
A multisig operation has been executed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| approving | `T::AccountId` | ```AccountId```
| timepoint | `Timepoint<BlockNumberFor<T>>` | ```{'height': 'u32', 'index': 'u32'}```
| multisig | `T::AccountId` | ```AccountId```
| call_hash | `CallHash` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}}```

---------
### NewMultisig
A new multisig operation has begun.
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
 The set of open multisig operations.

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
 The base amount of currency needed to reserve for creating a multisig execution or to
 store a dispatch call for later.

 This is held for an additional storage item whose value size is
 `4 + sizeof((BlockNumber, Balance, AccountId))` bytes and whose key size is
 `32 + sizeof(AccountId)` bytes.
#### Value
```python
200880000000
```
#### Python
```python
constant = substrate.get_constant('Multisig', 'DepositBase')
```
---------
### DepositFactor
 The amount of currency needed per unit threshold when creating a multisig execution.

 This is held for adding 32 bytes more into a pre-existing storage value.
#### Value
```python
320000000
```
#### Python
```python
constant = substrate.get_constant('Multisig', 'DepositFactor')
```
---------
### MaxSignatories
 The maximum amount of signatories allowed in the multisig.
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
Call is already approved by this signatory.

---------
### AlreadyStored
The data to be stored is already stored.

---------
### MaxWeightTooLow
The maximum weight information provided was too low.

---------
### MinimumThreshold
Threshold must be 2 or greater.

---------
### NoApprovalsNeeded
Call doesn&\#x27;t need any (more) approvals.

---------
### NoTimepoint
No timepoint was given, yet the multisig operation is already underway.

---------
### NotFound
Multisig operation not found when attempting to cancel.

---------
### NotOwner
Only the account that originally created the multisig is able to cancel it.

---------
### SenderInSignatories
The sender was contained in the other signatories; it shouldn&\#x27;t be.

---------
### SignatoriesOutOfOrder
The signatories were provided out of order; they should be ordered.

---------
### TooFewSignatories
There are too few signatories in the list.

---------
### TooManySignatories
There are too many signatories in the list.

---------
### UnexpectedTimepoint
A timepoint was given, yet no multisig operation is underway.

---------
### WrongTimepoint
A different timepoint was given to the multisig operation that is underway.

---------