
# XYKLiquidityMining

---------
## Calls

---------
### claim_rewards
Claim rewards from liq. mining for deposit represented by `nft_id`.

This function calculate user rewards from liq. mining and transfer rewards to `origin`
account. Claiming in the same period is allowed only once.

Parameters:
- `origin`: account owner of deposit(nft).
- `deposit_id`: nft id representing deposit in the yield farm.
- `yield_farm_id`: yield farm identifier to claim rewards from.

Emits `RewardClaimed` event when successful.
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
Create new liquidity mining program with provided parameters.

`owner` account has to have at least `total_rewards` balance. This fund will be
transferred from `owner` to farm account.

The dispatch origin for this call must be `T::CreateOrigin`.
!!!WARN: `T::CreateOrigin` has power over funds of `owner`&\#x27;s account and it should be
configured to trusted origin e.g Sudo or Governance.

Parameters:
- `origin`: global farm&\#x27;s owner.
- `total_rewards`: total rewards planned to distribute. This rewards will be
distributed between all yield farms in the global farm.
- `planned_yielding_periods`: planned number of periods to distribute `total_rewards`.
WARN: THIS IS NOT HARD DEADLINE. Not all rewards have to be distributed in
`planned_yielding_periods`. Rewards are distributed based on the situation in the yield
farms and can be distributed in a longer time frame but never in the shorter time frame.
- `blocks_per_period`:  number of blocks in a single period. Min. number of blocks per
period is 1.
- `incentivized_asset`: asset to be incentivized in XYK pools. All yield farms added into
liq. mining program have to have `incentivized_asset` in their pair.
- `reward_currency`: payoff currency of rewards.
- `owner`: liq. mining program owner.
- `yield_per_period`: percentage return on `reward_currency` of all farms p.a.
- `min_deposit`: minimum amount which can be deposited to the farm
- `price_adjustment`:
Emits `GlobalFarmCreated` event when successful.
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
Add yield farm for given `asset_pair` XYK pool.
 
Only farm owner can perform this action.

Only XYKs with `asset_pair` with `incentivized_asset` can be added into the farm. XYK
pool for `asset_pair` has to exist to successfully create yield farm.
Yield farm for same `asset_pair` can exist only once in the global farm.

Parameters:
- `origin`: global farm&\#x27;s owner.
- `farm_id`: global farm id to which a yield farm will be added.
- `asset_pair`: asset pair identifying yield farm. Liq. mining will be allowed for this
`asset_pair` and one of the assets in the pair must be `incentivized_asset`.
- `multiplier`: yield farm multiplier.
- `loyalty_curve`: curve to calculate loyalty multiplier to distribute rewards to users
with time incentive. `None` means no loyalty multiplier.

Emits `YieldFarmCreated` event when successful.
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
Deposit LP shares to a liq. mining.

This function transfers LP shares from `origin` to pallet&\#x27;s account and mint nft for
`origin` account. Minted nft represents deposit in the liq. mining.

Parameters:
- `origin`: account depositing LP shares. This account has to have at least
`shares_amount` of LP shares.
- `global_farm_id`: id of global farm to which user wants to deposit LP shares.
- `yield_farm_id`: id of yield farm to deposit to.
- `asset_pair`: asset pair identifying LP shares user wants to deposit.
- `shares_amount`: amount of LP shares user wants to deposit.

Emits `SharesDeposited` event when successful.
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
Redeposit already locked LP shares to another yield farm.

This function create yield farm entry for existing deposit. LP shares are not transferred
and amount of LP shares is based on existing deposit.

This function DOESN&\#x27;T create new deposit.

Parameters:
- `origin`: account depositing LP shares. This account have to have at least
- `global_farm_id`: global farm identifier.
- `yield_farm_id`: yield farm identifier redepositing to.
- `asset_pair`: asset pair identifying LP shares user want to deposit.
- `deposit_id`: identifier of the deposit.

Emits `SharesRedeposited` event when successful.
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
Resume yield farm for stopped yield farm.

This function resume incentivization from `GlobalFarm` and restore full functionality
for yield farm. Users will be able to deposit, claim and withdraw again.

WARN: Yield farm is NOT rewarded for time it was stopped.

Only farm owner can perform this action.

Parameters:
- `origin`: global farm&\#x27;s owner.
- `global_farm_id`: global farm id in which yield farm will be resumed.
- `yield_farm_id`: id of yield farm to be resumed.
- `asset_pair`: asset pair identifying yield farm in global farm.
- `multiplier`: yield farm multiplier in the farm.

Emits `YieldFarmResumed` event when successful.
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
Stop liq. miming for specific yield farm.

This function claims rewards from `GlobalFarm` last time and stops yield farm
incentivization from a `GlobalFarm`. Users will be able to only withdraw
shares(with claiming) after calling this function.
`deposit_shares()` and `claim_rewards()` are not allowed on canceled yield farm.
 
Only farm owner can perform this action.

Parameters:
- `origin`: global farm&\#x27;s owner.
- `global_farm_id`: farm id in which yield farm will be canceled.
- `asset_pair`: asset pair identifying yield farm in the farm.

Emits `YieldFarmStopped` event when successful.
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
Terminate existing liq. mining program.

Only farm owner can perform this action.

WARN: To successfully terminate a farm, farm have to be empty(all yield farms in he global farm must be terminated).

Parameters:
- `origin`: global farm&\#x27;s owner.
- `global_farm_id`: id of global farm to be terminated.

Emits `GlobalFarmTerminated` event when successful.
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
Remove yield farm

This function marks a yield farm as ready to be removed from storage when it&\#x27;s empty. Users will
be able to only withdraw shares(without claiming rewards from yield farm). Unpaid rewards
will be transferred back to global farm and will be used to distribute to other yield farms.

Yield farm must be stopped before calling this function.

Only global farm&\#x27;s owner can perform this action. Yield farm stays in the storage until it&\#x27;s
empty(all farm entries are withdrawn). Last withdrawn from yield farm trigger removing from
the storage.

Parameters:
- `origin`: global farm&\#x27;s owner.
- `global_farm_id`: farm id from which yield farm should be terminated.
- `yield_farm_id`: id of yield farm to be terminated.
- `asset_pair`: asset pair identifying yield farm in the global farm.

Emits `YieldFarmTerminated` event when successful.
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
Update global farm&\#x27;s prices adjustment.

Only farm&\#x27;s owner can perform this action.

Parameters:
- `origin`: global farm&\#x27;s owner.
- `global_farm_id`: id of the global farm to update
- `price_adjustment`: new value for price adjustment

Emits `GlobalFarmUpdated` event when successful.
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
Update yield farm multiplier.
 
Only farm owner can perform this action.

Parameters:
- `origin`: global farm&\#x27;s owner.
- `global_farm_id`: global farm id in which yield farm will be updated.
- `asset_pair`: asset pair identifying yield farm in global farm.
- `multiplier`: new yield farm multiplier.

Emits `YieldFarmUpdated` event when successful.
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
Withdraw LP shares from liq. mining with reward claiming if possible.

List of possible cases of transfers of LP shares and claimed rewards:

* yield farm is active(yield farm is not stopped) - claim and transfer rewards(if it
wasn&\#x27;t claimed in this period) and transfer LP shares.
* liq. mining is stopped - claim and transfer rewards(if it
wasn&\#x27;t claimed in this period) and transfer LP shares.
* yield farm was terminated - only LP shares will be transferred.
* farm was terminated - only LP shares will be transferred.

User&\#x27;s unclaimable rewards will be transferred back to global farm&\#x27;s account.

Parameters:
- `origin`: account owner of deposit(nft).
- `deposit_id`: nft id representing deposit in the yield farm.
- `yield_farm_id`: yield farm identifier to dithdraw shares from.
- `asset_pair`: asset pair identifying yield farm in global farm.

Emits:
* `RewardClaimed` if claim happen
* `SharesWithdrawn` event when successful
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