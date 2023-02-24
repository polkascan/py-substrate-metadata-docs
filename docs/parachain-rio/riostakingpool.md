
# RioStakingPool

---------
## Calls

---------
### cancel_unstaking
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'RioStakingPool', 'cancel_unstaking', {'amount': 'u128'}
)
```

---------
### claim
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'RioStakingPool', 'claim', {'amount': 'u128'}
)
```

---------
### claim_fees
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'RioStakingPool', 'claim_fees', {}
)
```

---------
### create_new_strategy
#### Attributes
| Name | Type |
| -------- | -------- | 
| per_block_reward | `Balance` | 
| start_block_number | `BlockNumber` | 
| duration | `BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'RioStakingPool', 'create_new_strategy', {
    'duration': 'u32',
    'per_block_reward': 'u128',
    'start_block_number': 'u32',
}
)
```

---------
### decrease_pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'RioStakingPool', 'decrease_pool', {'amount': 'u128'}
)
```

---------
### deposit_to_stake
Deposit assets to stake.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'RioStakingPool', 'deposit_to_stake', {'amount': 'u128'}
)
```

---------
### increase_pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'RioStakingPool', 'increase_pool', {'amount': 'u128'}
)
```

---------
### initialize_simple
#### Attributes
| Name | Type |
| -------- | -------- | 
| per_block_reward | `Balance` | 
| start_block_number | `BlockNumber` | 
| duration | `BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'RioStakingPool', 'initialize_simple', {
    'duration': 'u32',
    'per_block_reward': 'u128',
    'start_block_number': 'u32',
}
)
```

---------
### set_claiming_fee_percent
#### Attributes
| Name | Type |
| -------- | -------- | 
| fee_percent | `Percent` | 

#### Python
```python
call = substrate.compose_call(
    'RioStakingPool', 'set_claiming_fee_percent', {'fee_percent': 'u8'}
)
```

---------
### stake_for_user
#### Attributes
| Name | Type |
| -------- | -------- | 
| staker | `T::AccountId` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'RioStakingPool', 'stake_for_user', {
    'amount': 'u128',
    'staker': 'AccountId',
}
)
```

---------
### unstake
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'RioStakingPool', 'unstake', {'amount': 'u128'}
)
```

---------
### update_unstaking_time
#### Attributes
| Name | Type |
| -------- | -------- | 
| unstaking_time | `Moment` | 

#### Python
```python
call = substrate.compose_call(
    'RioStakingPool', 'update_unstaking_time', {'unstaking_time': 'u64'}
)
```

---------
### withdraw_from_unstaked
Withdraw unstaked assets.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'RioStakingPool', 'withdraw_from_unstaked', {}
)
```

---------
## Events

---------
### Claimed
[account, requested_amount, claimed_amount, fee_amount, burned_amount].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### ClaimingFeePercentUpdated
[fee_percent].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Percent` | ```u8```

---------
### CurrentStrategyUpdated
[per_block_reward, start_block_number, end_block_number].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```
| None | `BlockNumber` | ```u32```
| None | `BlockNumber` | ```u32```

---------
### FeeClaimed
[receiver, amount].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### NextStrategyRemoved
Next strategy removed.
#### Attributes
No attributes

---------
### NextStrategyUpdated
[per_block_reward, start_block_number, end_block_number].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```
| None | `BlockNumber` | ```u32```
| None | `BlockNumber` | ```u32```

---------
### PoolDecreased
[amount].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
### PoolIncreased
[payer, amount].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### PriceUpdated
Price updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Price` | ```u128```

---------
### RewardsUnlocked
[amount].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
### Staked
[account, payer, staked_amount, minted_amount].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Option<T::AccountId>` | ```(None, 'AccountId')```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### Unstaked
[account, requested_amount, unstaked_amount, burned_amount].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### UnstakingCanceled
[account, amount].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### UnstakingTimeUpdated
[unstaking_time].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Moment` | ```u64```

---------
### Withdrawed
[account, amount].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
## Storage functions

---------
### ClaimingFeePercent

#### Python
```python
result = substrate.query(
    'RioStakingPool', 'ClaimingFeePercent', []
)
```

#### Return value
```python
'u8'
```
---------
### CurrentStrategy

#### Python
```python
result = substrate.query(
    'RioStakingPool', 'CurrentStrategy', []
)
```

#### Return value
```python
{
    'end_block_number': 'u32',
    'per_block_reward': 'u128',
    'start_block_number': 'u32',
}
```
---------
### FeePool

#### Python
```python
result = substrate.query(
    'RioStakingPool', 'FeePool', []
)
```

#### Return value
```python
'u128'
```
---------
### LastStakeTime

#### Python
```python
result = substrate.query(
    'RioStakingPool', 'LastStakeTime', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### LastUpdateBlockNumber

#### Python
```python
result = substrate.query(
    'RioStakingPool', 'LastUpdateBlockNumber', []
)
```

#### Return value
```python
'u32'
```
---------
### LockedRewards

#### Python
```python
result = substrate.query(
    'RioStakingPool', 'LockedRewards', []
)
```

#### Return value
```python
'u128'
```
---------
### NextStrategy

#### Python
```python
result = substrate.query(
    'RioStakingPool', 'NextStrategy', []
)
```

#### Return value
```python
{
    'end_block_number': 'u32',
    'per_block_reward': 'u128',
    'start_block_number': 'u32',
}
```
---------
### PriceStored

#### Python
```python
result = substrate.query(
    'RioStakingPool', 'PriceStored', []
)
```

#### Return value
```python
'u128'
```
---------
### TotalStaked

#### Python
```python
result = substrate.query(
    'RioStakingPool', 'TotalStaked', []
)
```

#### Return value
```python
'u128'
```
---------
### TotalUnstaked

#### Python
```python
result = substrate.query(
    'RioStakingPool', 'TotalUnstaked', []
)
```

#### Return value
```python
'u128'
```
---------
### Unstakes

#### Python
```python
result = substrate.query(
    'RioStakingPool', 'Unstakes', ['AccountId']
)
```

#### Return value
```python
{'amount': 'u128', 'applicable_at': 'u64'}
```
---------
### UnstakingTime

#### Python
```python
result = substrate.query(
    'RioStakingPool', 'UnstakingTime', []
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### DefaultPrice
 For example: 1.
#### Value
```python
1000000000000000000
```
#### Python
```python
constant = substrate.get_constant('RioStakingPool', 'DefaultPrice')
```
---------
### MaximumPerBlockReward
 For example: `MinimumStakeBalance` * 188.
#### Value
```python
1880
```
#### Python
```python
constant = substrate.get_constant('RioStakingPool', 'MaximumPerBlockReward')
```
---------
### MinimumStakeBalance
 For example: 10^12.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('RioStakingPool', 'MinimumStakeBalance')
```
---------
### PalletId
#### Value
```python
'0x70792f72696f7370'
```
#### Python
```python
constant = substrate.get_constant('RioStakingPool', 'PalletId')
```
---------
## Errors

---------
### AmountIsNotPositive
Amount is not positive.

---------
### CheckedFromIntegerFailed
Checked from integer failed.

---------
### CheckedFromRationalFailed
Checked from rational failed.

---------
### CurrentStrategyIsNotSet
Current strategy is not set.

---------
### ImposibleToCalculatePriceTotalSupplyIsZero
Imposible to calculate price, total supply zero.

---------
### IncreasePoolOverflow
Increase Pool Overflow

---------
### InvalidFeePercent
Invalid fee percent,

---------
### InvalidUnstakingTime
Invalid Unstaking Time

---------
### MinimalStakeBalanceShouldBeMoreOrEqualToOneAssetMarker
Minimal stake balance should be more or equal to one asset marker.

---------
### NextStrategyIsNotSet
Next strategy is not set.

---------
### NoFees
No fees.

---------
### NotEnoughFundsInSupply
Not enough funds in supply.

---------
### NotEnoughLockedRewards
Not enough locked rewards.

---------
### NotEnoughMarkerUnits
Not enougth marked units.

---------
### NotEnoughUnstakedBalance
Not enough unstaked balance.

---------
### PositiveImbalance
Positive imbalance.

---------
### StakeBalanceIsLessThanMinimalStake
Stake balance is less than minimal stake.

---------
### TheStrategyIsNotBeingAppliedNow
The strategy is not being applied now.

---------
### ToSmallStakingAmount
To small staking amount.

---------
### TooSmallUnstakingAmount
Too small unstaking amount.

---------
### UnstakeAmountIsZeroForAccount
Unstake amount is zero, for account.

---------
### UnstakeIsNotReleasedYetForAccount
Unstake is not released yet, for account.

---------
### VOSpDurationIsZero
Validation of strategy parameters is failed, duration is zero.

---------
### VOSpPerBlockRewardOverflow
Validation of strategy parameters is failed, per block reward overflow,

---------
### VOSpStartBlockNumberLessThanCurrent
Validation of strategy parameters is failed, start block number less than current.

---------