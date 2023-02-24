
# Multisig

---------
## Calls

---------
### approve_as_multi
Register approval for a dispatch to be made from a deterministic composite account if
approved by a total of `threshold - 1` of `other_signatories`.

Payment: `DepositBase` will be reserved if this is the first approval, plus
`threshold` times `DepositFactor`. It is returned once this dispatch happens or
is cancelled.

The dispatch origin for this call must be _Signed_.

- `threshold`: The total number of approvals for this dispatch before it is executed.
- `other_signatories`: The accounts (other than the sender) who can approve this
dispatch. May not be empty.
- `maybe_timepoint`: If this is the first approval, then this must be `None`. If it is
not the first approval, then it must be `Some`, with the timepoint (block number and
transaction index) of the first approval transaction.
- `call_hash`: The hash of the call to be executed.

NOTE: If this is the final approval, you will want to use `as_multi` instead.

\# &lt;weight&gt;
- `O(S)`.
- Up to one balance-reserve or unreserve operation.
- One passthrough operation, one insert, both `O(S)` where `S` is the number of
  signatories. `S` is capped by `MaxSignatories`, with weight being proportional.
- One encode &amp; hash, both of complexity `O(S)`.
- Up to one binary search and insert (`O(logS + S)`).
- I/O: 1 read `O(S)`, up to 1 mutate `O(S)`. Up to one remove.
- One event.
- Storage: inserts one item, value size bounded by `MaxSignatories`, with a deposit
  taken for its lifetime of `DepositBase + threshold * DepositFactor`.
----------------------------------
- DB Weight:
    - Read: Multisig Storage, [Caller Account]
    - Write: Multisig Storage, [Caller Account]
\# &lt;/weight&gt;
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
    'max_weight': 'u64',
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
Register approval for a dispatch to be made from a deterministic composite account if
approved by a total of `threshold - 1` of `other_signatories`.

If there are enough, then dispatch the call.

Payment: `DepositBase` will be reserved if this is the first approval, plus
`threshold` times `DepositFactor`. It is returned once this dispatch happens or
is cancelled.

The dispatch origin for this call must be _Signed_.

- `threshold`: The total number of approvals for this dispatch before it is executed.
- `other_signatories`: The accounts (other than the sender) who can approve this
dispatch. May not be empty.
- `maybe_timepoint`: If this is the first approval, then this must be `None`. If it is
not the first approval, then it must be `Some`, with the timepoint (block number and
transaction index) of the first approval transaction.
- `call`: The call to be executed.

NOTE: Unless this is the final approval, you will generally want to use
`approve_as_multi` instead, since it only requires a hash of the call.

Result is equivalent to the dispatched result if `threshold` is exactly `1`. Otherwise
on success, result is `Ok` and the result from the interior call, if it was executed,
may be found in the deposited `MultisigExecuted` event.

\# &lt;weight&gt;
- `O(S + Z + Call)`.
- Up to one balance-reserve or unreserve operation.
- One passthrough operation, one insert, both `O(S)` where `S` is the number of
  signatories. `S` is capped by `MaxSignatories`, with weight being proportional.
- One call encode &amp; hash, both of complexity `O(Z)` where `Z` is tx-len.
- One encode &amp; hash, both of complexity `O(S)`.
- Up to one binary search and insert (`O(logS + S)`).
- I/O: 1 read `O(S)`, up to 1 mutate `O(S)`. Up to one remove.
- One event.
- The weight of the `call`.
- Storage: inserts one item, value size bounded by `MaxSignatories`, with a deposit
  taken for its lifetime of `DepositBase + threshold * DepositFactor`.
-------------------------------
- DB Weight:
    - Reads: Multisig Storage, [Caller Account], Calls (if `store_call`)
    - Writes: Multisig Storage, [Caller Account], Calls (if `store_call`)
- Plus Call Weight
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `u16` | 
| other_signatories | `Vec<T::AccountId>` | 
| maybe_timepoint | `Option<Timepoint<T::BlockNumber>>` | 
| call | `OpaqueCall<T>` | 
| store_call | `bool` | 
| max_weight | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'Multisig', 'as_multi', {
    'call': 'Call',
    'max_weight': 'u64',
    'maybe_timepoint': (
        None,
        {
            'height': 'u32',
            'index': 'u32',
        },
    ),
    'other_signatories': ['AccountId'],
    'store_call': 'bool',
    'threshold': 'u16',
}
)
```

---------
### as_multi_threshold_1
Immediately dispatch a multi-signature call using a single approval from the caller.

The dispatch origin for this call must be _Signed_.

- `other_signatories`: The accounts (other than the sender) who are part of the
multi-signature, but do not participate in the approval process.
- `call`: The call to be executed.

Result is equivalent to the dispatched result.

\# &lt;weight&gt;
O(Z + C) where Z is the length of the call and C its execution weight.
-------------------------------
- DB Weight: None
- Plus Call Weight
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| other_signatories | `Vec<T::AccountId>` | 
| call | `Box<<T as Config>::Call>` | 

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
Cancel a pre-existing, on-going multisig transaction. Any deposit reserved previously
for this operation will be unreserved on success.

The dispatch origin for this call must be _Signed_.

- `threshold`: The total number of approvals for this dispatch before it is executed.
- `other_signatories`: The accounts (other than the sender) who can approve this
dispatch. May not be empty.
- `timepoint`: The timepoint (block number and transaction index) of the first approval
transaction for this dispatch.
- `call_hash`: The hash of the call to be executed.

\# &lt;weight&gt;
- `O(S)`.
- Up to one balance-reserve or unreserve operation.
- One passthrough operation, one insert, both `O(S)` where `S` is the number of
  signatories. `S` is capped by `MaxSignatories`, with weight being proportional.
- One encode &amp; hash, both of complexity `O(S)`.
- One event.
- I/O: 1 read `O(S)`, one remove.
- Storage: removes one item.
----------------------------------
- DB Weight:
    - Read: Multisig Storage, [Caller Account], Refund Account, Calls
    - Write: Multisig Storage, [Caller Account], Refund Account, Calls
\# &lt;/weight&gt;
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
A multisig operation has been approved by someone.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| approving | `T::AccountId` | ```AccountId```
| timepoint | `Timepoint<T::BlockNumber>` | ```{'height': 'u32', 'index': 'u32'}```
| multisig | `T::AccountId` | ```AccountId```
| call_hash | `CallHash` | ```[u8; 32]```

---------
### MultisigCancelled
A multisig operation has been cancelled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| cancelling | `T::AccountId` | ```AccountId```
| timepoint | `Timepoint<T::BlockNumber>` | ```{'height': 'u32', 'index': 'u32'}```
| multisig | `T::AccountId` | ```AccountId```
| call_hash | `CallHash` | ```[u8; 32]```

---------
### MultisigExecuted
A multisig operation has been executed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| approving | `T::AccountId` | ```AccountId```
| timepoint | `Timepoint<T::BlockNumber>` | ```{'height': 'u32', 'index': 'u32'}```
| multisig | `T::AccountId` | ```AccountId```
| call_hash | `CallHash` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

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
### Calls

#### Python
```python
result = substrate.query(
    'Multisig', 'Calls', ['[u8; 32]']
)
```

#### Return value
```python
('Call', 'AccountId', 'u128')
```
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
20008800000000000
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
3200000000000
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