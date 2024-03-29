
# OmnipoolLiquidityMining

---------
## Calls

---------
### claim_rewards
See [`Pallet::claim_rewards`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| deposit_id | `DepositId` | 
| yield_farm_id | `YieldFarmId` | 

#### Python
```python
call = substrate.compose_call(
    'OmnipoolLiquidityMining', 'claim_rewards', {
    'deposit_id': 'u128',
    'yield_farm_id': 'u32',
}
)
```

---------
### create_global_farm
See [`Pallet::create_global_farm`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| total_rewards | `Balance` | 
| planned_yielding_periods | `PeriodOf<T>` | 
| blocks_per_period | `BlockNumberFor<T>` | 
| reward_currency | `T::AssetId` | 
| owner | `T::AccountId` | 
| yield_per_period | `Perquintill` | 
| min_deposit | `Balance` | 
| lrna_price_adjustment | `FixedU128` | 

#### Python
```python
call = substrate.compose_call(
    'OmnipoolLiquidityMining', 'create_global_farm', {
    'blocks_per_period': 'u32',
    'lrna_price_adjustment': 'u128',
    'min_deposit': 'u128',
    'owner': 'AccountId',
    'planned_yielding_periods': 'u32',
    'reward_currency': 'u32',
    'total_rewards': 'u128',
    'yield_per_period': 'u64',
}
)
```

---------
### create_yield_farm
See [`Pallet::create_yield_farm`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| global_farm_id | `GlobalFarmId` | 
| asset_id | `T::AssetId` | 
| multiplier | `FarmMultiplier` | 
| loyalty_curve | `Option<LoyaltyCurve>` | 

#### Python
```python
call = substrate.compose_call(
    'OmnipoolLiquidityMining', 'create_yield_farm', {
    'asset_id': 'u32',
    'global_farm_id': 'u32',
    'loyalty_curve': (
        None,
        {
            'initial_reward_percentage': 'u128',
            'scale_coef': 'u32',
        },
    ),
    'multiplier': 'u128',
}
)
```

---------
### deposit_shares
See [`Pallet::deposit_shares`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| global_farm_id | `GlobalFarmId` | 
| yield_farm_id | `YieldFarmId` | 
| position_id | `T::PositionItemId` | 

#### Python
```python
call = substrate.compose_call(
    'OmnipoolLiquidityMining', 'deposit_shares', {
    'global_farm_id': 'u32',
    'position_id': 'u128',
    'yield_farm_id': 'u32',
}
)
```

---------
### redeposit_shares
See [`Pallet::redeposit_shares`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| global_farm_id | `GlobalFarmId` | 
| yield_farm_id | `YieldFarmId` | 
| deposit_id | `DepositId` | 

#### Python
```python
call = substrate.compose_call(
    'OmnipoolLiquidityMining', 'redeposit_shares', {
    'deposit_id': 'u128',
    'global_farm_id': 'u32',
    'yield_farm_id': 'u32',
}
)
```

---------
### resume_yield_farm
See [`Pallet::resume_yield_farm`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| global_farm_id | `GlobalFarmId` | 
| yield_farm_id | `YieldFarmId` | 
| asset_id | `T::AssetId` | 
| multiplier | `FarmMultiplier` | 

#### Python
```python
call = substrate.compose_call(
    'OmnipoolLiquidityMining', 'resume_yield_farm', {
    'asset_id': 'u32',
    'global_farm_id': 'u32',
    'multiplier': 'u128',
    'yield_farm_id': 'u32',
}
)
```

---------
### stop_yield_farm
See [`Pallet::stop_yield_farm`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| global_farm_id | `GlobalFarmId` | 
| asset_id | `T::AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'OmnipoolLiquidityMining', 'stop_yield_farm', {
    'asset_id': 'u32',
    'global_farm_id': 'u32',
}
)
```

---------
### terminate_global_farm
See [`Pallet::terminate_global_farm`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| global_farm_id | `GlobalFarmId` | 

#### Python
```python
call = substrate.compose_call(
    'OmnipoolLiquidityMining', 'terminate_global_farm', {'global_farm_id': 'u32'}
)
```

---------
### terminate_yield_farm
See [`Pallet::terminate_yield_farm`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| global_farm_id | `GlobalFarmId` | 
| yield_farm_id | `YieldFarmId` | 
| asset_id | `T::AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'OmnipoolLiquidityMining', 'terminate_yield_farm', {
    'asset_id': 'u32',
    'global_farm_id': 'u32',
    'yield_farm_id': 'u32',
}
)
```

---------
### update_yield_farm
See [`Pallet::update_yield_farm`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| global_farm_id | `GlobalFarmId` | 
| asset_id | `T::AssetId` | 
| multiplier | `FarmMultiplier` | 

#### Python
```python
call = substrate.compose_call(
    'OmnipoolLiquidityMining', 'update_yield_farm', {
    'asset_id': 'u32',
    'global_farm_id': 'u32',
    'multiplier': 'u128',
}
)
```

---------
### withdraw_shares
See [`Pallet::withdraw_shares`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| deposit_id | `DepositId` | 
| yield_farm_id | `YieldFarmId` | 

#### Python
```python
call = substrate.compose_call(
    'OmnipoolLiquidityMining', 'withdraw_shares', {
    'deposit_id': 'u128',
    'yield_farm_id': 'u32',
}
)
```

---------
## Events

---------
### DepositDestroyed
All LP shares were unlocked and NFT representing deposit was destroyed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| deposit_id | `DepositId` | ```u128```

---------
### GlobalFarmCreated
New global farm was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `GlobalFarmId` | ```u32```
| owner | `T::AccountId` | ```AccountId```
| total_rewards | `Balance` | ```u128```
| reward_currency | `T::AssetId` | ```u32```
| yield_per_period | `Perquintill` | ```u64```
| planned_yielding_periods | `PeriodOf<T>` | ```u32```
| blocks_per_period | `BlockNumberFor<T>` | ```u32```
| max_reward_per_period | `Balance` | ```u128```
| min_deposit | `Balance` | ```u128```
| lrna_price_adjustment | `FixedU128` | ```u128```

---------
### GlobalFarmTerminated
Global farm was terminated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| reward_currency | `T::AssetId` | ```u32```
| undistributed_rewards | `Balance` | ```u128```

---------
### RewardClaimed
Rewards were claimed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| claimed | `Balance` | ```u128```
| reward_currency | `T::AssetId` | ```u32```
| deposit_id | `DepositId` | ```u128```

---------
### SharesDeposited
New LP shares(LP position) were deposited.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| deposit_id | `DepositId` | ```u128```
| asset_id | `T::AssetId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| shares_amount | `Balance` | ```u128```
| position_id | `T::PositionItemId` | ```u128```

---------
### SharesRedeposited
Already locked LP shares were redeposited to another yield farm.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| deposit_id | `DepositId` | ```u128```
| asset_id | `T::AssetId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| shares_amount | `Balance` | ```u128```
| position_id | `T::PositionItemId` | ```u128```

---------
### SharesWithdrawn
LP shares were withdrawn.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `Balance` | ```u128```
| deposit_id | `DepositId` | ```u128```

---------
### YieldFarmCreated
New yield farm was added to the farm.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| asset_id | `T::AssetId` | ```u32```
| multiplier | `FarmMultiplier` | ```u128```
| loyalty_curve | `Option<LoyaltyCurve>` | ```(None, {'initial_reward_percentage': 'u128', 'scale_coef': 'u32'})```

---------
### YieldFarmResumed
Yield farm for `asset_id` was resumed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| asset_id | `T::AssetId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| multiplier | `FarmMultiplier` | ```u128```

---------
### YieldFarmStopped
Yield farm for `asset_id` was stopped.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| asset_id | `T::AssetId` | ```u32```
| who | `T::AccountId` | ```AccountId```

---------
### YieldFarmTerminated
Yield farm was terminated from the global farm.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| asset_id | `T::AssetId` | ```u32```
| who | `T::AccountId` | ```AccountId```

---------
### YieldFarmUpdated
Yield farm multiplier was updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| asset_id | `T::AssetId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| multiplier | `FarmMultiplier` | ```u128```

---------
## Storage functions

---------
### OmniPositionId
 Map of omnipool position&#x27;s ids to LM&#x27;s deposit ids.

#### Python
```python
result = substrate.query(
    'OmnipoolLiquidityMining', 'OmniPositionId', ['u128']
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### NFTCollectionId
 NFT collection id for liquidity mining&#x27;s deposit nfts.
#### Value
```python
2584
```
#### Python
```python
constant = substrate.get_constant('OmnipoolLiquidityMining', 'NFTCollectionId')
```
---------
### OraclePeriod
 Oracle&#x27;s price aggregation period.
#### Value
```python
'TenMinutes'
```
#### Python
```python
constant = substrate.get_constant('OmnipoolLiquidityMining', 'OraclePeriod')
```
---------
### OracleSource
 Identifier of oracle data soruce
#### Value
```python
'0x6f6d6e69706f6f6c'
```
#### Python
```python
constant = substrate.get_constant('OmnipoolLiquidityMining', 'OracleSource')
```
---------
## Errors

---------
### AssetNotFound
Asset is not in the omnipool.

---------
### Forbidden
Signed account is not owner of the deposit.

---------
### InconsistentState
Action cannot be completed because unexpected error has occurred. This should be reported
to protocol maintainers.

---------
### OracleNotAvailable
Oracle could not be found for requested assets.

---------
### PriceAdjustmentNotAvailable
Oracle providing `price_adjustment` could not be found for requested assets.

---------
### ZeroClaimedRewards
Rewards to claim are 0.

---------