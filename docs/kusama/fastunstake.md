
# FastUnstake

---------
## Calls

---------
### control
Control the operation of this pallet.

Dispatch origin must be signed by the [`Config::ControlOrigin`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| eras_to_check | `EraIndex` | 

#### Python
```python
call = substrate.compose_call(
    'FastUnstake', 'control', {'eras_to_check': 'u32'}
)
```

---------
### deregister
Deregister oneself from the fast-unstake.

This is useful if one is registered, they are still waiting, and they change their mind.

Note that the associated stash is still fully unbonded and chilled as a consequence of
calling `register_fast_unstake`. This should probably be followed by a call to
`Staking::rebond`.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'FastUnstake', 'deregister', {}
)
```

---------
### register_fast_unstake
Register oneself for fast-unstake.

The dispatch origin of this call must be signed by the controller account, similar to
`staking::unbond`.

The stash associated with the origin must have no ongoing unlocking chunks. If
successful, this will fully unbond and chill the stash. Then, it will enqueue the stash
to be checked in further blocks.

If by the time this is called, the stash is actually eligible for fast-unstake, then
they are guaranteed to remain eligible, because the call will chill them as well.

If the check works, the entire staking data is removed, i.e. the stash is fully
unstaked.

If the check fails, the stash remains chilled and waiting for being unbonded as in with
the normal staking system, but they lose part of their unbonding chunks due to consuming
the chain&\#x27;s resources.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'FastUnstake', 'register_fast_unstake', {}
)
```

---------
## Events

---------
### BatchChecked
A batch was partially checked for the given eras, but the process did not finish.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| eras | `Vec<EraIndex>` | ```['u32']```

---------
### BatchFinished
A batch of a given size was terminated.

This is always follows by a number of `Unstaked` or `Slashed` events, marking the end
of the batch. A new batch will be created upon next block.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| size | `u32` | ```u32```

---------
### InternalError
An internal error happened. Operations will be paused now.
#### Attributes
No attributes

---------
### Slashed
A staker was slashed for requesting fast-unstake whilst being exposed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| stash | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### Unstaked
A staker was unstaked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| stash | `T::AccountId` | ```AccountId```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}}```

---------
## Storage functions

---------
### CounterForQueue
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'FastUnstake', 'CounterForQueue', []
)
```

#### Return value
```python
'u32'
```
---------
### ErasToCheckPerBlock
 Number of eras to check per block.

 If set to 0, this pallet does absolutely nothing.

 Based on the amount of weight available at `on_idle`, up to this many eras of a single
 nominator might be checked.

#### Python
```python
result = substrate.query(
    'FastUnstake', 'ErasToCheckPerBlock', []
)
```

#### Return value
```python
'u32'
```
---------
### Head
 The current &quot;head of the queue&quot; being unstaked.

#### Python
```python
result = substrate.query(
    'FastUnstake', 'Head', []
)
```

#### Return value
```python
{'checked': ['u32'], 'stashes': [('AccountId', 'u128')]}
```
---------
### Queue
 The map of all accounts wishing to be unstaked.

 Keeps track of `AccountId` wishing to unstake and it&#x27;s corresponding deposit.

 TWOX-NOTE: SAFE since `AccountId` is a secure hash.

#### Python
```python
result = substrate.query(
    'FastUnstake', 'Queue', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### Deposit
 Deposit to take for unstaking, to make sure we&#x27;re able to slash the it in order to cover
 the costs of resources on unsuccessful unstake.
#### Value
```python
33333333300
```
#### Python
```python
constant = substrate.get_constant('FastUnstake', 'Deposit')
```
---------
## Errors

---------
### AlreadyHead
The provided un-staker is already in Head, and cannot deregister.

---------
### AlreadyQueued
The bonded account has already been queued.

---------
### CallNotAllowed
The call is not allowed at this point because the pallet is not active.

---------
### NotController
The provided Controller account was not found.

This means that the given account is not bonded.

---------
### NotFullyBonded
The bonded account has active unlocking chunks.

---------
### NotQueued
The provided un-staker is not in the `Queue`.

---------