
# Oracle

---------
## Calls

---------
### add_asset_and_info
Permissioned call to add an asset

- `asset_id`: Id for the asset
- `threshold`: Percent close to mean to be rewarded
- `min_answers`: Min answers before aggregation
- `max_answers`: Max answers to aggregate
- `block_interval`: blocks until oracle triggered
- `reward`: reward amount for correct answer
- `slash`: slash amount for bad answer
- `emit_price_changes`: emit PriceChanged event when asset price changes

Emits `DepositEvent` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| threshold | `Validated<Percent, ValidThreshold>` | 
| min_answers | `Validated<u32, ValidMinAnswers<T::MinAnswerBound>>` | 
| max_answers | `Validated<u32, ValidMaxAnswer<T::MaxAnswerBound>>` | 
| block_interval | `Validated<T::BlockNumber, ValidBlockInterval<T::StalePrice>>` | 
| reward_weight | `BalanceOf<T>` | 
| slash | `BalanceOf<T>` | 
| emit_price_changes | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Oracle', 'add_asset_and_info', {
    'asset_id': 'u128',
    'block_interval': 'u32',
    'emit_price_changes': 'bool',
    'max_answers': 'u32',
    'min_answers': 'u32',
    'reward_weight': 'u128',
    'slash': 'u128',
    'threshold': 'u8',
}
)
```

---------
### add_stake
call to add more stake from a controller

- `stake`: amount to add to stake

Emits `StakeAdded` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| stake | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Oracle', 'add_stake', {'stake': 'u128'}
)
```

---------
### adjust_rewards
Call to start rewarding Oracles.
- `annual_cost_per_oracle`: Annual cost of an Oracle.
- `num_ideal_oracles`: Number of ideal Oracles. This in fact should be higher than the
  actual ideal number so that the Oracles make a profit under ideal conditions.

Emits `RewardRateSet` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| annual_cost_per_oracle | `BalanceOf<T>` | 
| num_ideal_oracles | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'Oracle', 'adjust_rewards', {
    'annual_cost_per_oracle': 'u128',
    'num_ideal_oracles': 'u8',
}
)
```

---------
### reclaim_stake
Call to reclaim stake after proper time has passed, called from controller

Emits `StakeReclaimed` event when successful.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Oracle', 'reclaim_stake', {}
)
```

---------
### remove_stake
Call to put in a claim to remove stake, called from controller

Emits `StakeRemoved` event when successful.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Oracle', 'remove_stake', {}
)
```

---------
### set_signer
Call for a signer to be set, called from controller, adds stake.

- `signer`: signer to tie controller to

Emits `SignerSet` and `StakeAdded` events when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| signer | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Oracle', 'set_signer', {'signer': 'AccountId'}
)
```

---------
### submit_price
Call to submit a price, gas is returned if extrinsic is successful.
Should be called from offchain worker but can be called manually too.

This is an operational transaction.

- `price`: price to submit, normalized to 12 decimals
- `asset_id`: id for the asset

Emits `PriceSubmitted` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| price | `T::PriceValue` | 
| asset_id | `T::AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'Oracle', 'submit_price', {'asset_id': 'u128', 'price': 'u128'}
)
```

---------
## Events

---------
### AnswerPruned
Answer from oracle removed for staleness. \[oracle_address, price\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::PriceValue` | ```u128```

---------
### AssetInfoChange
Asset info created or changed. \[asset_id, threshold, min_answers, max_answers,
block_interval, reward, slash\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AssetId` | ```u128```
| None | `Percent` | ```u8```
| None | `u32` | ```u32```
| None | `u32` | ```u32```
| None | `T::BlockNumber` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### OracleRewarded
Oracle rewarded. \[oracle_address, asset_id, price\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AssetId` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### PriceChanged
Price changed by oracle \[asset_id, price\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AssetId` | ```u128```
| None | `T::PriceValue` | ```u128```

---------
### PriceSubmitted
Price submitted by oracle. \[oracle_address, asset_id, price\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AssetId` | ```u128```
| None | `T::PriceValue` | ```u128```

---------
### RewardingAdjustment
Rewarding Started \[rewarding start timestamp]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Moment` | ```u64```

---------
### SignerSet
Signer was set. \[signer, controller\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```

---------
### StakeAdded
Stake was added. \[added_by, amount_added, total_amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### StakeReclaimed
Stake reclaimed. \[reclaimed_by, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### StakeRemoved
Stake removed. \[removed_by, amount, block_number\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `T::BlockNumber` | ```u32```

---------
### UserSlashed
Oracle slashed. \[oracle_address, asset_id, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AssetId` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### AccumulatedRewardsPerAsset
 Mapping of signing key to stake

#### Python
```python
result = substrate.query(
    'Oracle', 'AccumulatedRewardsPerAsset', ['u128']
)
```

#### Return value
```python
'u128'
```
---------
### AnswerInTransit
 Mapping of slash amounts currently in transit

#### Python
```python
result = substrate.query(
    'Oracle', 'AnswerInTransit', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### AssetsCount
 Total amount of assets

#### Python
```python
result = substrate.query(
    'Oracle', 'AssetsCount', []
)
```

#### Return value
```python
'u32'
```
---------
### AssetsInfo
 Information about asset, including precision threshold and max/min answers

#### Python
```python
result = substrate.query(
    'Oracle', 'AssetsInfo', ['u128']
)
```

#### Return value
```python
{
    'block_interval': 'u32',
    'emit_price_changes': 'bool',
    'max_answers': 'u32',
    'min_answers': 'u32',
    'reward_weight': 'u128',
    'slash': 'u128',
    'threshold': 'u8',
}
```
---------
### ControllerToSigner
 Mapping Controller key to signer key

#### Python
```python
result = substrate.query(
    'Oracle', 'ControllerToSigner', ['AccountId']
)
```

#### Return value
```python
'AccountId'
```
---------
### DeclaredWithdraws
 Tracking withdrawal requests

#### Python
```python
result = substrate.query(
    'Oracle', 'DeclaredWithdraws', ['AccountId']
)
```

#### Return value
```python
{'stake': 'u128', 'unlock_block': 'u32'}
```
---------
### OracleStake
 Mapping of signing key to stake

#### Python
```python
result = substrate.query(
    'Oracle', 'OracleStake', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### PrePrices
 Temporary prices before aggregated

#### Python
```python
result = substrate.query(
    'Oracle', 'PrePrices', ['u128']
)
```

#### Return value
```python
[{'block': 'u32', 'price': 'u128', 'who': 'AccountId'}]
```
---------
### PriceHistory
 Price for an asset and blocknumber asset was updated at

#### Python
```python
result = substrate.query(
    'Oracle', 'PriceHistory', ['u128']
)
```

#### Return value
```python
[{'block': 'u32', 'price': 'u128'}]
```
---------
### Prices
 Price for an asset and blocknumber asset was updated at

#### Python
```python
result = substrate.query(
    'Oracle', 'Prices', ['u128']
)
```

#### Return value
```python
{'block': 'u32', 'price': 'u128'}
```
---------
### RewardTrackerStore
 Rewarding history for Oracles. Used for calculating the current block reward.

#### Python
```python
result = substrate.query(
    'Oracle', 'RewardTrackerStore', []
)
```

#### Return value
```python
{
    'current_block_reward': 'u128',
    'period': 'u64',
    'start': 'u64',
    'total_already_rewarded': 'u128',
    'total_reward_weight': 'u128',
}
```
---------
### SignerToController
 Mapping signing key to controller key

#### Python
```python
result = substrate.query(
    'Oracle', 'SignerToController', ['AccountId']
)
```

#### Return value
```python
'AccountId'
```
---------
## Constants

---------
### MaxHistory
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('Oracle', 'MaxHistory')
```
---------
### MaxPrePrices
#### Value
```python
40
```
#### Python
```python
constant = substrate.get_constant('Oracle', 'MaxPrePrices')
```
---------
### MsPerBlock
#### Value
```python
12000
```
#### Python
```python
constant = substrate.get_constant('Oracle', 'MsPerBlock')
```
---------
### PalletId
#### Value
```python
'0x706c745f6f726163'
```
#### Python
```python
constant = substrate.get_constant('Oracle', 'PalletId')
```
---------
### TwapWindow
#### Value
```python
3
```
#### Python
```python
constant = substrate.get_constant('Oracle', 'TwapWindow')
```
---------
## Errors

---------
### AlreadySet
Signer has already been set

---------
### AlreadySubmitted
Price already submitted

---------
### AnnualRewardLessThanAlreadyRewarded
Annual rewarding cost too high

---------
### ArithmeticError

---------
### AvoidPanic
Error avoids a panic

---------
### BlockIntervalLength
Block interval is less then stale price

---------
### ControllerUsed
This controller is already in use

---------
### DepthTooLarge
Too many weighted averages requested

---------
### ExceedAssetsCount
Asset count exceeded

---------
### ExceedMaxAnswers
Max answers have been exceeded

---------
### ExceedStake
Stake exceeded

---------
### ExceedThreshold
Threshold exceeded

---------
### InvalidAssetId
Invalid asset id

---------
### InvalidMinAnswers
Invalid min answers

---------
### MaxAnswersLessThanMinAnswers

---------
### MaxHistory

---------
### MaxPrePrices

---------
### MaxPrices
Max prices already reached

---------
### MustSumTo100
Price weight must sum to 100

---------
### NoPermission
No Permission

---------
### NoRewardTrackerSet
Rewarding has not started

---------
### NoStake
No stake for oracle

---------
### NotEnoughFunds
Not Enough Funds to complete action

---------
### NotEnoughStake
Not enough oracle stake for action

---------
### PriceNotFound
Price not found

---------
### PriceNotRequested
Price has not been requested

---------
### SignerUsed
This signer is already in use

---------
### StakeLocked
Stake is locked try again later

---------
### TransferError
There was an error transferring

---------
### Unknown
Unknown

---------
### UnsetController
No controller has been set

---------
### UnsetSigner
Signer has not been set

---------