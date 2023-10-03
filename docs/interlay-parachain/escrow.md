
# Escrow

---------
## Calls

---------
### create_lock
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 
| unlock_height | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Escrow', 'create_lock', {
    'amount': 'u128',
    'unlock_height': 'u32',
}
)
```

---------
### increase_amount
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Escrow', 'increase_amount', {'amount': 'u128'}
)
```

---------
### increase_unlock_height
#### Attributes
| Name | Type |
| -------- | -------- | 
| unlock_height | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Escrow', 'increase_unlock_height', {'unlock_height': 'u32'}
)
```

---------
### set_account_block
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Escrow', 'set_account_block', {'who': 'AccountId'}
)
```

---------
### set_account_limit
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 
| start | `T::BlockNumber` | 
| end | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Escrow', 'set_account_limit', {
    'end': 'u32',
    'start': 'u32',
    'who': 'AccountId',
}
)
```

---------
### update_user_stake
Update the stake amount for a user.

\# Arguments

* `origin` - Sender of the transaction.
* `target_user` - The account ID of the user whose stake amount needs to be updated.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target_user | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Escrow', 'update_user_stake', {'target_user': 'AccountId'}
)
```

---------
### withdraw
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Escrow', 'withdraw', {}
)
```

---------
## Events

---------
### Deposit
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```
| unlock_height | `T::BlockNumber` | ```u32```

---------
### Withdraw
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### Blocks

#### Python
```python
result = substrate.query(
    'Escrow', 'Blocks', ['AccountId']
)
```

#### Return value
```python
'bool'
```
---------
### Epoch

#### Python
```python
result = substrate.query(
    'Escrow', 'Epoch', []
)
```

#### Return value
```python
'u32'
```
---------
### Limits

#### Python
```python
result = substrate.query(
    'Escrow', 'Limits', ['AccountId']
)
```

#### Return value
```python
('u32', 'u32')
```
---------
### Locked

#### Python
```python
result = substrate.query(
    'Escrow', 'Locked', ['AccountId']
)
```

#### Return value
```python
{'amount': 'u128', 'end': 'u32'}
```
---------
### PointHistory

#### Python
```python
result = substrate.query(
    'Escrow', 'PointHistory', ['u32']
)
```

#### Return value
```python
{'bias': 'u128', 'slope': 'u128', 'ts': 'u32'}
```
---------
### Reserved

#### Python
```python
result = substrate.query(
    'Escrow', 'Reserved', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### SlopeChanges

#### Python
```python
result = substrate.query(
    'Escrow', 'SlopeChanges', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### UserPointEpoch

#### Python
```python
result = substrate.query(
    'Escrow', 'UserPointEpoch', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### UserPointHistory

#### Python
```python
result = substrate.query(
    'Escrow', 'UserPointHistory', ['AccountId', 'u32']
)
```

#### Return value
```python
{'bias': 'u128', 'slope': 'u128', 'ts': 'u32'}
```
---------
## Constants

---------
### MaxPeriod
 The maximum time for locks.
#### Value
```python
9676800
```
#### Python
```python
constant = substrate.get_constant('Escrow', 'MaxPeriod')
```
---------
### Span
 All future times are rounded by this.
#### Value
```python
50400
```
#### Python
```python
constant = substrate.get_constant('Escrow', 'Span')
```
---------
## Errors

---------
### IncorrectPercent
Incorrect Percent

---------
### InputAmountZero
Input amount must be non-zero.

---------
### InsufficientFunds
Insufficient account balance.

---------
### LockAmountTooLow
Lock amount is too large.

---------
### LockAmountZero
Lock amount must be non-zero.

---------
### LockFound
Lock already exists.

---------
### LockHasExpired
Previous lock has expired.

---------
### LockNotExpired
Previous lock has not expired.

---------
### LockNotFound
Lock does not exist.

---------
### NotSupported
Not supported.

---------
### UnlockHeightMustIncrease
Unlock height should be greater than lock.

---------
### UnlockHeightNotInTheFuture
Unlock height is not in the future.

---------
### UnlockHeightTooFarInTheFuture
Unlock height is greater than max period.

---------