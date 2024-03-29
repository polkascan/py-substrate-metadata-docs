
# XYKLiquidityMining

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
    'XYKLiquidityMining', 'claim_rewards', {
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
| incentivized_asset | `AssetId` | 
| reward_currency | `AssetId` | 
| owner | `T::AccountId` | 
| yield_per_period | `Perquintill` | 
| min_deposit | `Balance` | 
| price_adjustment | `FixedU128` | 

#### Python
```python
call = substrate.compose_call(
    'XYKLiquidityMining', 'create_global_farm', {
    'blocks_per_period': 'u32',
    'incentivized_asset': 'u32',
    'min_deposit': 'u128',
    'owner': 'AccountId',
    'planned_yielding_periods': 'u32',
    'price_adjustment': 'u128',
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
| asset_pair | `AssetPair` | 
| multiplier | `FarmMultiplier` | 
| loyalty_curve | `Option<LoyaltyCurve>` | 

#### Python
```python
call = substrate.compose_call(
    'XYKLiquidityMining', 'create_yield_farm', {
    'asset_pair': {
        'asset_in': 'u32',
        'asset_out': 'u32',
    },
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
| asset_pair | `AssetPair` | 
| shares_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'XYKLiquidityMining', 'deposit_shares', {
    'asset_pair': {
        'asset_in': 'u32',
        'asset_out': 'u32',
    },
    'global_farm_id': 'u32',
    'shares_amount': 'u128',
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
| asset_pair | `AssetPair` | 
| deposit_id | `DepositId` | 

#### Python
```python
call = substrate.compose_call(
    'XYKLiquidityMining', 'redeposit_shares', {
    'asset_pair': {
        'asset_in': 'u32',
        'asset_out': 'u32',
    },
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
| asset_pair | `AssetPair` | 
| multiplier | `FarmMultiplier` | 

#### Python
```python
call = substrate.compose_call(
    'XYKLiquidityMining', 'resume_yield_farm', {
    'asset_pair': {
        'asset_in': 'u32',
        'asset_out': 'u32',
    },
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
| asset_pair | `AssetPair` | 

#### Python
```python
call = substrate.compose_call(
    'XYKLiquidityMining', 'stop_yield_farm', {
    'asset_pair': {
        'asset_in': 'u32',
        'asset_out': 'u32',
    },
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
    'XYKLiquidityMining', 'terminate_global_farm', {'global_farm_id': 'u32'}
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
| asset_pair | `AssetPair` | 

#### Python
```python
call = substrate.compose_call(
    'XYKLiquidityMining', 'terminate_yield_farm', {
    'asset_pair': {
        'asset_in': 'u32',
        'asset_out': 'u32',
    },
    'global_farm_id': 'u32',
    'yield_farm_id': 'u32',
}
)
```

---------
### update_global_farm
See [`Pallet::update_global_farm`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| global_farm_id | `GlobalFarmId` | 
| price_adjustment | `FixedU128` | 

#### Python
```python
call = substrate.compose_call(
    'XYKLiquidityMining', 'update_global_farm', {
    'global_farm_id': 'u32',
    'price_adjustment': 'u128',
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
| asset_pair | `AssetPair` | 
| multiplier | `FarmMultiplier` | 

#### Python
```python
call = substrate.compose_call(
    'XYKLiquidityMining', 'update_yield_farm', {
    'asset_pair': {
        'asset_in': 'u32',
        'asset_out': 'u32',
    },
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
| asset_pair | `AssetPair` | 

#### Python
```python
call = substrate.compose_call(
    'XYKLiquidityMining', 'withdraw_shares', {
    'asset_pair': {
        'asset_in': 'u32',
        'asset_out': 'u32',
    },
    'deposit_id': 'u128',
    'yield_farm_id': 'u32',
}
)
```

---------
## Events

---------
### DepositDestroyed
NFT representing deposit has been destroyed
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
| reward_currency | `AssetId` | ```u32```
| yield_per_period | `Perquintill` | ```u64```
| planned_yielding_periods | `PeriodOf<T>` | ```u32```
| blocks_per_period | `BlockNumberFor<T>` | ```u32```
| incentivized_asset | `AssetId` | ```u32```
| max_reward_per_period | `Balance` | ```u128```
| min_deposit | `Balance` | ```u128```
| price_adjustment | `FixedU128` | ```u128```

---------
### GlobalFarmTerminated
Global farm was terminated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| reward_currency | `AssetId` | ```u32```
| undistributed_rewards | `Balance` | ```u128```

---------
### GlobalFarmUpdated
Global farm&\#x27;s `price_adjustment` was updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `GlobalFarmId` | ```u32```
| price_adjustment | `FixedU128` | ```u128```

---------
### RewardClaimed
Rewards was claimed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| claimed | `Balance` | ```u128```
| reward_currency | `AssetId` | ```u32```
| deposit_id | `DepositId` | ```u128```

---------
### SharesDeposited
New LP tokens was deposited.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `Balance` | ```u128```
| lp_token | `AssetId` | ```u32```
| deposit_id | `DepositId` | ```u128```

---------
### SharesRedeposited
LP token was redeposited for a new yield farm entry
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `Balance` | ```u128```
| lp_token | `AssetId` | ```u32```
| deposit_id | `DepositId` | ```u128```

---------
### SharesWithdrawn
LP tokens was withdrawn.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| lp_token | `AssetId` | ```u32```
| amount | `Balance` | ```u128```
| deposit_id | `DepositId` | ```u128```

---------
### YieldFarmCreated
New yield farm was added into the farm.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| multiplier | `FarmMultiplier` | ```u128```
| asset_pair | `AssetPair` | ```{'asset_in': 'u32', 'asset_out': 'u32'}```
| loyalty_curve | `Option<LoyaltyCurve>` | ```(None, {'initial_reward_percentage': 'u128', 'scale_coef': 'u32'})```

---------
### YieldFarmResumed
Yield farm for asset pair was resumed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| asset_pair | `AssetPair` | ```{'asset_in': 'u32', 'asset_out': 'u32'}```
| multiplier | `FarmMultiplier` | ```u128```

---------
### YieldFarmStopped
Yield farm for asset pair was stopped.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| asset_pair | `AssetPair` | ```{'asset_in': 'u32', 'asset_out': 'u32'}```

---------
### YieldFarmTerminated
Yield farm was terminated from global farm.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| asset_pair | `AssetPair` | ```{'asset_in': 'u32', 'asset_out': 'u32'}```

---------
### YieldFarmUpdated
Yield farm multiplier was updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| global_farm_id | `GlobalFarmId` | ```u32```
| yield_farm_id | `YieldFarmId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| asset_pair | `AssetPair` | ```{'asset_in': 'u32', 'asset_out': 'u32'}```
| multiplier | `FarmMultiplier` | ```u128```

---------
## Constants

---------
### NftCollectionId
 NFT collection id for liq. mining deposit nfts. Has to be within the range of reserved NFT class IDs.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('XYKLiquidityMining', 'NftCollectionId')
```
---------
## Errors

---------
### AssetNotInAssetPair
Asset is not in the `AssetPair`.

---------
### CantFindDepositOwner
Nft pallet didn&\#x27;t return an owner.

---------
### CantGetXykAssets
XYK did not return assets for given pool id

---------
### DepositDataNotFound
Deposit data not found

---------
### InsufficientXykSharesBalance
Account balance of XYK pool shares is not sufficient.

---------
### InvalidAssetPair
Provided `AssetPair` is not used by the deposit.

---------
### NotDepositOwner
Account is not deposit owner.

---------
### XykPoolDoesntExist
XYK pool does not exist

---------
### ZeroClaimedRewards
Calculated reward to claim is 0.

---------