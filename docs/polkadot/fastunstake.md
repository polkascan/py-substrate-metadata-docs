
# FastUnstake

---------
## Calls

---------
### control
See [`Pallet::control`].
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
See [`Pallet::deregister`].
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
See [`Pallet::register_fast_unstake`].
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

 If set to 0, this pallet does absolutely nothing. Cannot be set to more than
 [`Config::MaxErasToCheckPerBlock`].

 Based on the amount of weight available at [`Pallet::on_idle`], up to this many eras are
 checked. The checking is represented by updating [`UnstakeRequest::checked`], which is
 stored in [`Head`].

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

 The head in itself can be a batch of up to [`Config::BatchSize`] stakers.

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
10000000000
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