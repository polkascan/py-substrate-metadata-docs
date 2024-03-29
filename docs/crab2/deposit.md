
# Deposit

---------
## Calls

---------
### claim
See [`Pallet::claim`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Deposit', 'claim', {}
)
```

---------
### claim_with_penalty
See [`Pallet::claim_with_penalty`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `DepositId` | 

#### Python
```python
call = substrate.compose_call(
    'Deposit', 'claim_with_penalty', {'id': 'u16'}
)
```

---------
### lock
See [`Pallet::lock`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 
| months | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'Deposit', 'lock', {'amount': 'u128', 'months': 'u8'}
)
```

---------
## Events

---------
### DepositClaimed
An expired deposit has been claimed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```[u8; 20]```
| deposit_id | `DepositId` | ```u16```

---------
### DepositClaimedWithPenalty
An unexpired deposit has been claimed by paying the KTON penalty.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```[u8; 20]```
| deposit_id | `DepositId` | ```u16```
| kton_penalty | `Balance` | ```u128```

---------
### DepositCreated
A new deposit has been created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```[u8; 20]```
| deposit_id | `DepositId` | ```u16```
| value | `Balance` | ```u128```
| start_time | `Moment` | ```u128```
| expired_time | `Moment` | ```u128```
| kton_reward | `Balance` | ```u128```

---------
## Storage functions

---------
### Deposits
 All deposits.

 The items must be sorted by the id.

#### Python
```python
result = substrate.query(
    'Deposit', 'Deposits', ['[u8; 20]']
)
```

#### Return value
```python
[
    {
        'expired_time': 'u128',
        'id': 'u16',
        'in_use': 'bool',
        'start_time': 'u128',
        'value': 'u128',
    },
]
```
---------
## Constants

---------
### MaxDeposits
 Maximum deposit count.

 In currently design, this should not be greater than `u16::MAX`.
#### Value
```python
512
```
#### Python
```python
constant = substrate.get_constant('Deposit', 'MaxDeposits')
```
---------
### MinLockingAmount
 Minimum amount to lock at least.
#### Value
```python
1000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Deposit', 'MinLockingAmount')
```
---------
## Errors

---------
### DepositAlreadyExpired
Deposit is already expired.

---------
### DepositInUse
Deposit is in use.

---------
### DepositNotFound
Deposit not found.

---------
### DepositNotInUse
Deposit is not in use.

---------
### ExceedMaxDeposits
Exceed maximum deposit count.

---------
### LockAtLeastOneMonth
Lock at least for one month.

---------
### LockAtLeastSome
Lock at least for a specific amount.

---------
### LockAtMostThirtySixMonths
Lock at most for thirty-six months.

---------