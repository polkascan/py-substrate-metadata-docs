
# OmnipoolWarehouseLM

---------
## Events

---------
### AllRewardsDistributed
Global farm has no more rewards to distribute in the moment.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```

---------
### GlobalFarmAccRPZUpdated
Global farm accumulated reward per share was updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| accumulated_rpz | `FixedU128` | ```u128```
| total_shares_z | `Balance` | ```u128```

---------
### YieldFarmAccRPVSUpdated
Yield farm accumulated reward per valued share was updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| accumulated_rpvs | `FixedU128` | ```u128```
| total_valued_shares | `Balance` | ```u128```

---------
## Storage functions

---------
### ActiveYieldFarm
 Active(farms able to receive LP shares deposits) yield farms.

#### Python
```python
result = substrate.query(
    'OmnipoolWarehouseLM', 'ActiveYieldFarm', ['u32', 'u32']
)
```

#### Return value
```python
'u32'
```
---------
### Deposit
 Deposit details.

#### Python
```python
result = substrate.query(
    'OmnipoolWarehouseLM', 'Deposit', ['u128']
)
```

#### Return value
```python
{
    'amm_pool_id': 'u32',
    'shares': 'u128',
    'yield_farm_entries': [
        {
            'accumulated_claimed_rewards': 'u128',
            'accumulated_rpvs': 'u128',
            'entered_at': 'u32',
            'global_farm_id': 'u32',
            'stopped_at_creation': 'u32',
            'updated_at': 'u32',
            'valued_shares': 'u128',
            'yield_farm_id': 'u32',
        },
    ],
}
```
---------
### DepositSequencer

#### Python
```python
result = substrate.query(
    'OmnipoolWarehouseLM', 'DepositSequencer', []
)
```

#### Return value
```python
'u128'
```
---------
### FarmSequencer
 Id sequencer for `GlobalFarm` and `YieldFarm`.

#### Python
```python
result = substrate.query(
    'OmnipoolWarehouseLM', 'FarmSequencer', []
)
```

#### Return value
```python
'u32'
```
---------
### GlobalFarm

#### Python
```python
result = substrate.query(
    'OmnipoolWarehouseLM', 'GlobalFarm', ['u32']
)
```

#### Return value
```python
{
    'accumulated_paid_rewards': 'u128',
    'accumulated_rpz': 'u128',
    'blocks_per_period': 'u32',
    'id': 'u32',
    'incentivized_asset': 'u32',
    'live_yield_farms_count': 'u32',
    'max_reward_per_period': 'u128',
    'min_deposit': 'u128',
    'owner': 'AccountId',
    'pending_rewards': 'u128',
    'planned_yielding_periods': 'u32',
    'price_adjustment': 'u128',
    'reward_currency': 'u32',
    'state': ('Active', 'Stopped', 'Terminated'),
    'total_shares_z': 'u128',
    'total_yield_farms_count': 'u32',
    'updated_at': 'u32',
    'yield_per_period': 'u64',
}
```
---------
### YieldFarm
 Yield farm details.

#### Python
```python
result = substrate.query(
    'OmnipoolWarehouseLM', 'YieldFarm', ['u32', 'u32', 'u32']
)
```

#### Return value
```python
{
    'accumulated_rpvs': 'u128',
    'accumulated_rpz': 'u128',
    'entries_count': 'u64',
    'id': 'u32',
    'left_to_distribute': 'u128',
    'loyalty_curve': (
        None,
        {'initial_reward_percentage': 'u128', 'scale_coef': 'u32'},
    ),
    'multiplier': 'u128',
    'state': ('Active', 'Stopped', 'Terminated'),
    'total_shares': 'u128',
    'total_stopped': 'u32',
    'total_valued_shares': 'u128',
    'updated_at': 'u32',
}
```
---------
## Constants

---------
### MaxFarmEntriesPerDeposit
 Maximum number of yield farms same LP shares can be re/deposited into. This value always
 MUST BE &gt;= 1.         
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('OmnipoolWarehouseLM', 'MaxFarmEntriesPerDeposit')
```
---------
### MaxYieldFarmsPerGlobalFarm
 Max number of yield farms can exist in global farm. This includes all farms in the
 storage(active, stopped, deleted).
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('OmnipoolWarehouseLM', 'MaxYieldFarmsPerGlobalFarm')
```
---------
### MinPlannedYieldingPeriods
 Minimum number of periods to run liquidity mining program.
#### Value
```python
14440
```
#### Python
```python
constant = substrate.get_constant('OmnipoolWarehouseLM', 'MinPlannedYieldingPeriods')
```
---------
### MinTotalFarmRewards
 Minimum total rewards to distribute from global farm during liquidity mining.
#### Value
```python
100000000000000
```
#### Python
```python
constant = substrate.get_constant('OmnipoolWarehouseLM', 'MinTotalFarmRewards')
```
---------
### PalletId
 Pallet id.
#### Value
```python
'0x4f6d6e6957684c4d'
```
#### Python
```python
constant = substrate.get_constant('OmnipoolWarehouseLM', 'PalletId')
```
---------
## Errors

---------
### DoubleClaimInPeriod
Multiple claims in the same period is not allowed.

---------
### DoubleLock
Trying to lock LP shares into already locked yield farm.

---------
### ErrorGetAccountId
Account creation from id failed.

---------
### Forbidden
Account is not allowed to perform action.

---------
### GlobalFarmIsFull
Max number of yield farms in global farm was reached. Global farm can&\#x27;t accept new
yield farms until some yield farm is not removed from storage.

---------
### GlobalFarmIsNotEmpty
One or more yield farms exist in global farm.

---------
### GlobalFarmNotFound
Global farm does not exist.

---------
### IncentivizedAssetNotRegistered
`incentivized_asset` is not registered in asset registry.

---------
### InconsistentState
Action cannot be completed because unexpected error has occurred. This should be reported
to protocol maintainers.

---------
### InsufficientRewardCurrencyBalance
Reward currency balance is not sufficient.

---------
### InvalidBlocksPerPeriod
Blocks per period can&\#x27;t be 0.

---------
### InvalidDepositAmount
LP shares amount is not valid.

---------
### InvalidInitialRewardPercentage
Loyalty curve&\#x27;s initial reward percentage is not valid. Valid range is: [0, 1).

---------
### InvalidMinDeposit
Invalid min. deposit was set for global farm.

---------
### InvalidMultiplier
Yield farm multiplier can&\#x27;t be 0.

---------
### InvalidPlannedYieldingPeriods
Planned yielding periods is less than `MinPlannedYieldingPeriods`.

---------
### InvalidPriceAdjustment
Price adjustment multiplier can&\#x27;t be 0.

---------
### InvalidTotalRewards
Total rewards is less than `MinTotalFarmRewards`.

---------
### InvalidYieldPerPeriod
Yield per period can&\#x27;t be 0.

---------
### LiquidityMiningCanceled
Liquidity mining is canceled.

---------
### LiquidityMiningIsActive
Liquidity mining is not canceled.

---------
### LiquidityMiningIsNotStopped
Liquidity mining is in `active` or `terminated` state and action cannot be completed.

---------
### MaxEntriesPerDeposit
Maximum number of locks reached for deposit.

---------
### MissingIncentivizedAsset
Farm&\#x27;s `incentivized_asset` is missing in provided asset pair.

---------
### RewardCurrencyNotRegistered
`reward_currency` is not registered in asset registry.

---------
### YieldFarmAlreadyExists
Yield farm with given `amm_pool_id` already exists in global farm.

---------
### YieldFarmEntryNotFound
Yield farm entry doesn&\#x27;t exist for given deposit.

---------
### YieldFarmNotFound
Yield farm does not exist.

---------
### ZeroValuedShares
Value of deposited shares amount in reward currency can&\#x27;t be 0.

---------