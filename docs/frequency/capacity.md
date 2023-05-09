
# Capacity

---------
## Calls

---------
### set_epoch_length
#### Attributes
| Name | Type |
| -------- | -------- | 
| length | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Capacity', 'set_epoch_length', {'length': 'u32'}
)
```

---------
### stake
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `MessageSourceId` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Capacity', 'stake', {'amount': 'u128', 'target': 'u64'}
)
```

---------
### unstake
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `MessageSourceId` | 
| requested_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Capacity', 'unstake', {
    'requested_amount': 'u128',
    'target': 'u64',
}
)
```

---------
### withdraw_unstaked
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Capacity', 'withdraw_unstaked', {}
)
```

---------
## Events

---------
### CapacityWithdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```
| amount | `BalanceOf<T>` | ```u128```

---------
### EpochLengthUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| blocks | `T::BlockNumber` | ```u32```

---------
### StakeWithdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### Staked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| target | `MessageSourceId` | ```u64```
| amount | `BalanceOf<T>` | ```u128```
| capacity | `BalanceOf<T>` | ```u128```

---------
### UnStaked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| target | `MessageSourceId` | ```u64```
| amount | `BalanceOf<T>` | ```u128```
| capacity | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### CapacityLedger

#### Python
```python
result = substrate.query(
    'Capacity', 'CapacityLedger', ['u64']
)
```

#### Return value
```python
{
    'last_replenished_epoch': 'u32',
    'remaining_capacity': 'u128',
    'total_capacity_issued': 'u128',
    'total_tokens_staked': 'u128',
}
```
---------
### CurrentEpoch

#### Python
```python
result = substrate.query(
    'Capacity', 'CurrentEpoch', []
)
```

#### Return value
```python
'u32'
```
---------
### CurrentEpochInfo

#### Python
```python
result = substrate.query(
    'Capacity', 'CurrentEpochInfo', []
)
```

#### Return value
```python
{'epoch_start': 'u32'}
```
---------
### EpochLength

#### Python
```python
result = substrate.query(
    'Capacity', 'EpochLength', []
)
```

#### Return value
```python
'u32'
```
---------
### StakingAccountLedger

#### Python
```python
result = substrate.query(
    'Capacity', 'StakingAccountLedger', ['AccountId']
)
```

#### Return value
```python
{
    'active': 'u128',
    'total': 'u128',
    'unlocking': [{'thaw_at': 'u32', 'value': 'u128'}],
}
```
---------
### StakingTargetLedger

#### Python
```python
result = substrate.query(
    'Capacity', 'StakingTargetLedger', ['AccountId', 'u64']
)
```

#### Return value
```python
{'amount': 'u128', 'capacity': 'u128'}
```
---------
## Constants

---------
### CapacityPerToken
#### Value
```python
20000000
```
#### Python
```python
constant = substrate.get_constant('Capacity', 'CapacityPerToken')
```
---------
### MaxEpochLength
#### Value
```python
7200
```
#### Python
```python
constant = substrate.get_constant('Capacity', 'MaxEpochLength')
```
---------
### MaxUnlockingChunks
#### Value
```python
4
```
#### Python
```python
constant = substrate.get_constant('Capacity', 'MaxUnlockingChunks')
```
---------
### MinimumStakingAmount
#### Value
```python
1000000
```
#### Python
```python
constant = substrate.get_constant('Capacity', 'MinimumStakingAmount')
```
---------
### MinimumTokenBalance
#### Value
```python
100000000
```
#### Python
```python
constant = substrate.get_constant('Capacity', 'MinimumTokenBalance')
```
---------
### UnstakingThawPeriod
#### Value
```python
30
```
#### Python
```python
constant = substrate.get_constant('Capacity', 'UnstakingThawPeriod')
```
---------
## Errors

---------
### AmountToUnstakeExceedsAmountStaked

---------
### BalanceTooLowtoStake

---------
### IncreaseExceedsAvailable

---------
### InsufficientBalance

---------
### InsufficientStakingAmount

---------
### InvalidTarget

---------
### MaxEpochLengthExceeded

---------
### MaxUnlockingChunksExceeded

---------
### NoUnstakedTokensAvailable

---------
### NotAStakingAccount

---------
### StakerTargetRelationshipNotFound

---------
### StakingAccountNotFound

---------
### TargetCapacityNotFound

---------
### UnstakedAmountIsZero

---------
### ZeroAmountNotAllowed

---------