
# FarmingRewards

---------
## Events

---------
### DepositStake
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u128```
| stake_id | `T::StakeId` | ```AccountId```
| amount | `T::SignedFixedPoint` | ```i128```

---------
### DistributeReward
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u128```
| amount | `T::SignedFixedPoint` | ```i128```

---------
### WithdrawReward
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u128```
| stake_id | `T::StakeId` | ```AccountId```
| currency_id | `T::CurrencyId` | ```u128```
| amount | `T::SignedFixedPoint` | ```i128```

---------
### WithdrawStake
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u128```
| stake_id | `T::StakeId` | ```AccountId```
| amount | `T::SignedFixedPoint` | ```i128```

---------
## Storage functions

---------
### RewardCurrencies
 Track the currencies used for rewards.

#### Python
```python
result = substrate.query(
    'FarmingRewards', 'RewardCurrencies', ['u128']
)
```

#### Return value
```python
'scale_info::609'
```
---------
### RewardPerToken
 Used to compute the rewards for a participant&#x27;s stake.

#### Python
```python
result = substrate.query(
    'FarmingRewards', 'RewardPerToken', ['u128', 'u128']
)
```

#### Return value
```python
'i128'
```
---------
### RewardTally
 Accounts for previous changes in stake size.

#### Python
```python
result = substrate.query(
    'FarmingRewards', 'RewardTally', ['u128', ('u128', 'AccountId')]
)
```

#### Return value
```python
'i128'
```
---------
### Stake
 The stake of a participant in this reward pool.

#### Python
```python
result = substrate.query(
    'FarmingRewards', 'Stake', [('u128', 'AccountId')]
)
```

#### Return value
```python
'i128'
```
---------
### TotalRewards
 The total unclaimed rewards distributed to this reward pool.
 NOTE: this is currently only used for integration tests.

#### Python
```python
result = substrate.query(
    'FarmingRewards', 'TotalRewards', ['u128']
)
```

#### Return value
```python
'i128'
```
---------
### TotalStake
 The total stake deposited to this reward pool.

#### Python
```python
result = substrate.query(
    'FarmingRewards', 'TotalStake', ['u128']
)
```

#### Return value
```python
'i128'
```
---------
## Constants

---------
### MaxRewardCurrencies
 The maximum number of reward currencies.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('FarmingRewards', 'MaxRewardCurrencies')
```
---------
## Errors

---------
### InsufficientFunds
Balance not sufficient to withdraw stake.

---------
### MaxRewardCurrencies
Maximum rewards currencies reached.

---------
### TryIntoIntError
Unable to convert value.

---------
### ZeroTotalStake
Cannot distribute rewards without stake.

---------