
# Farming

---------
## Calls

---------
### claim
Withdraw any accrued rewards from the reward pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_currency_id | `AssetIdOf<T>` | 
| reward_currency_id | `AssetIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'claim', {
    'pool_currency_id': 'u128',
    'reward_currency_id': 'u128',
}
)
```

---------
### deposit
Stake the pool tokens from the reward pool

- `pool_currency_id`: LP token to deposit
- `amount`: of LP token to deposit
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_currency_id | `AssetIdOf<T>` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'deposit', {
    'amount': 'u128',
    'pool_currency_id': 'u128',
}
)
```

---------
### remove_reward_schedule
Explicitly remove a reward schedule and transfer any remaining
balance to the treasury
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_currency_id | `AssetIdOf<T>` | 
| reward_currency_id | `AssetIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'remove_reward_schedule', {
    'pool_currency_id': 'u128',
    'reward_currency_id': 'u128',
}
)
```

---------
### update_reward_schedule
Create or overwrite the reward schedule, if a reward schedule
already exists for the rewards currency the duration is added
to the existing duration and the rewards per period are modified
s.t. that the total (old remaining + new) rewards are distributed
over the new total duration
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_currency_id | `AssetIdOf<T>` | 
| reward_currency_id | `AssetIdOf<T>` | 
| period_count | `u32` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'update_reward_schedule', {
    'amount': 'u128',
    'period_count': 'u32',
    'pool_currency_id': 'u128',
    'reward_currency_id': 'u128',
}
)
```

---------
### withdraw
Unstake the pool tokens from the reward pool

- `pool_currency_id`: LP token to withdraw
- `amount`: of LP token to withdraw
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_currency_id | `AssetIdOf<T>` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'withdraw', {
    'amount': 'u128',
    'pool_currency_id': 'u128',
}
)
```

---------
## Events

---------
### RewardClaimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `AccountIdOf<T>` | ```AccountId```
| pool_currency_id | `AssetIdOf<T>` | ```u128```
| reward_currency_id | `AssetIdOf<T>` | ```u128```
| amount | `BalanceOf<T>` | ```u128```

---------
### RewardDistributed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_currency_id | `AssetIdOf<T>` | ```u128```
| reward_currency_id | `AssetIdOf<T>` | ```u128```
| amount | `BalanceOf<T>` | ```u128```

---------
### RewardScheduleUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_currency_id | `AssetIdOf<T>` | ```u128```
| reward_currency_id | `AssetIdOf<T>` | ```u128```
| period_count | `u32` | ```u32```
| per_period | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### RewardSchedules

#### Python
```python
result = substrate.query(
    'Farming', 'RewardSchedules', ['u128', 'u128']
)
```

#### Return value
```python
{'per_period': 'u128', 'period_count': 'u32'}
```
---------
## Constants

---------
### FarmingPalletId
 The farming pallet id, used for deriving pool accounts.
#### Value
```python
'0x6d6f642f6661726d'
```
#### Python
```python
constant = substrate.get_constant('Farming', 'FarmingPalletId')
```
---------
### RewardPeriod
 The period to accrue rewards.
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Farming', 'RewardPeriod')
```
---------
### TreasuryAccountId
 The treasury account id for funding pools.
#### Value
```python
'5w3oyasXpSiWwVK2BKjunsjZME3r8YbELucHTeh4hYuMdJrE'
```
#### Python
```python
constant = substrate.get_constant('Farming', 'TreasuryAccountId')
```
---------
## Errors

---------
### InsufficientStake

---------