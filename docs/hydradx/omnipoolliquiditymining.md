
# OmnipoolLiquidityMining

---------
## Calls

---------
### claim_rewards
Claim rewards from liquidity mining program for deposit represented by the `deposit_id`.

This function calculate user rewards from liquidity mining and transfer rewards to `origin`
account. Claiming multiple time the same period is not allowed.

Parameters:
- `origin`: owner of deposit.
- `deposit_id`: id of the deposit to claim rewards for.
- `yield_farm_id`: id of the yield farm to claim rewards from.

Emits `RewardClaimed` event when successful.

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
Create a new liquidity mining program with provided parameters.

`owner` account has to have at least `total_rewards` balance. These funds will be
transferred from `owner` to farm account.

The dispatch origin for this call must be `T::CreateOrigin`.
!!!WARN: `T::CreateOrigin` has power over funds of `owner`&\#x27;s account and it should be
configured to trusted origin e.g Sudo or Governance.

Parameters:
- `origin`: account allowed to create new liquidity mining program(root, governance).
- `total_rewards`: total rewards planned to distribute. These rewards will be
distributed between all yield farms in the global farm.
- `planned_yielding_periods`: planned number of periods to distribute `total_rewards`.
WARN: THIS IS NOT HARD DEADLINE. Not all rewards have to be distributed in
`planned_yielding_periods`. Rewards are distributed based on the situation in the yield
farms and can be distributed in a longer, though never in a shorter, time frame.
- `blocks_per_period`:  number of blocks in a single period. Min. number of blocks per
period is 1.
- `reward_currency`: payoff currency of rewards.
- `owner`: liq. mining farm owner. This account will be able to manage created
liquidity mining program.
- `yield_per_period`: percentage return on `reward_currency` of all farms.
- `min_deposit`: minimum amount of LP shares to be deposited into the liquidity mining by each user.
- `lrna_price_adjustment`: price adjustment between `[LRNA]` and `reward_currency`.

Emits `GlobalFarmCreated` when successful.

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
Create yield farm for given `asset_id` in the omnipool.
 
Only farm owner can perform this action.

Asset with `asset_id` has to be registered in the omnipool.
Yield farm for same `asset_id` can exist only once in the global farm.

Parameters:
- `origin`: global farm&\#x27;s owner.
- `global_farm_id`: global farm id to which a yield farm will be added.
- `asset_id`: id of a asset in the omnipool. Yield farm will be created
for this asset and user will be able to lock LP shares into this yield farm immediately.
- `multiplier`: yield farm&\#x27;s multiplier.
- `loyalty_curve`: curve to calculate loyalty multiplier to distribute rewards to users
with time incentive. `None` means no loyalty multiplier.

Emits `YieldFarmCreated` event when successful.

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
Deposit omnipool position(LP shares) to a liquidity mining.

This function transfers omnipool position from `origin` to pallet&\#x27;s account and mint NFT for
`origin` account. Minted NFT represents deposit in the liquidity mining. User can
deposit omnipool position as a whole(all the LP shares in the position).

Parameters:
- `origin`: owner of the omnipool position to deposit into the liquidity mining.
- `global_farm_id`: id of global farm to which user wants to deposit LP shares.
- `yield_farm_id`: id of yield farm to deposit to.
- `position_id`: id of the omnipool position to be deposited into the liquidity mining.

Emits `SharesDeposited` event when successful.

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
Redeposit LP shares in the already locked omnipool position.

This function create yield farm entry for existing deposit. Amount of redeposited LP
shares is same as amount shares which are already deposited in the deposit.

This function DOESN&\#x27;T create new deposit(NFT).

Parameters:
- `origin`: owner of the deposit to redeposit.
- `global_farm_id`: id of the global farm to which user wants to redeposit LP shares.
- `yield_farm_id`: id of the yield farm to redeposit to.
- `deposit_id`: identifier of the deposit to redeposit.

Emits `SharesRedeposited` event when successful.

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
Resume incentivization of the asset represented by yield farm.

This function resume incentivization of the asset from the `GlobalFarm` and
restore full functionality or the yield farm. Users will be able to deposit,
claim and withdraw again.

WARN: Yield farm(and users) is NOT rewarded for time it was stopped.

Only farm owner can perform this action.

Parameters:
- `origin`: global farm&\#x27;s owner.
- `global_farm_id`: global farm id in which yield farm will be resumed.
- `yield_farm_id`: id of the yield farm to be resumed.
- `asset_id`: id of the asset identifying yield farm in the global farm.
- `multiplier`: yield farm multiplier.

Emits `YieldFarmResumed` event when successful.

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
Stop liquidity miming for specific yield farm.

This function claims rewards from `GlobalFarm` last time and stop yield farm
incentivization from a `GlobalFarm`. Users will be able to only withdraw
shares(with claiming) after calling this function.
`deposit_shares()` and `claim_rewards()` are not allowed on stopped yield farm.
 
Only farm owner can perform this action.

Parameters:
- `origin`: global farm&\#x27;s owner.
- `global_farm_id`: farm id in which yield farm will be canceled.
- `asset_id`: id of the asset identifying yield farm in the global farm.

Emits `YieldFarmStopped` event when successful.

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
Terminate existing liq. mining program.

Only farm owner can perform this action.

WARN: To successfully terminate a global farm, farm have to be empty
(all yield farms in the global farm must be terminated).

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
    'OmnipoolLiquidityMining', 'terminate_global_farm', {'global_farm_id': 'u32'}
)
```

---------
### terminate_yield_farm
Terminate yield farm.

This function marks a yield farm as ready to be removed from storage when it&\#x27;s empty. Users will
be able to only withdraw shares(without claiming rewards from yield farm). Unpaid rewards
will be transferred back to global farm and it will be used to distribute to other yield farms.

Yield farm must be stopped before it can be terminated.

Only global farm&\#x27;s owner can perform this action. Yield farm stays in the storage until it&\#x27;s
empty(all farm entries are withdrawn). Last withdrawn from yield farm trigger removing from
the storage.

Parameters:
- `origin`: global farm&\#x27;s owner.
- `global_farm_id`: global farm id in which yield farm should be terminated.
- `yield_farm_id`: id of yield farm to be terminated.
- `asset_id`: id of the asset identifying yield farm.

Emits `YieldFarmTerminated` event when successful.

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
### update_global_farm
Update global farm&\#x27;s exchange rate between [LRNA] and `incentivized_asset`.

Only farm&\#x27;s owner can perform this action.

Parameters:
- `origin`: global farm&\#x27;s owner.
- `global_farm_id`: id of the global farm to update.
- `lrna_price_adjustment`: new value for LRNA price adjustment.

Emits `GlobalFarmUpdated` event when successful.

#### Attributes
| Name | Type |
| -------- | -------- | 
| global_farm_id | `GlobalFarmId` | 
| lrna_price_adjustment | `FixedU128` | 

#### Python
```python
call = substrate.compose_call(
    'OmnipoolLiquidityMining', 'update_global_farm', {
    'global_farm_id': 'u32',
    'lrna_price_adjustment': 'u128',
}
)
```

---------
### update_yield_farm
Update yield farm&\#x27;s multiplier.
 
Only farm owner can perform this action.

Parameters:
- `origin`: global farm&\#x27;s owner.
- `global_farm_id`: global farm id in which yield farm will be updated.
- `asset_id`: id of the asset identifying yield farm in the global farm.
- `multiplier`: new yield farm&\#x27;s multiplier.

Emits `YieldFarmUpdated` event when successful.

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
This function claim rewards and withdraw LP shares from yield farm. Omnipool position
is transferred to origin only if this is last withdraw in the deposit and deposit is
destroyed. This function claim rewards only if yield farm is not terminated and user
didn&\#x27;t already claim rewards in current period.

Unclaimable rewards represents rewards which user won&\#x27;t be able to claim because of
exiting early and these rewards will be transferred back to global farm for future
redistribution.

Parameters:
- `origin`: owner of deposit.
- `deposit_id`: id of the deposit to claim rewards for.
- `yield_farm_id`: id of the yield farm to claim rewards from.

Emits:
* `RewardClaimed` event if claimed rewards is &gt; 0
* `SharesWithdrawn` event when successful
* `DepositDestroyed` event when this was last withdraw from the deposit and deposit was
destroyed.

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
### GlobalFarmUpdated
Global farm&\#x27;s `lrna_price_adjustment` was updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `GlobalFarmId` | ```u32```
| lrna_price_adjustment | `FixedU128` | ```u128```

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
### ZeroClaimedRewards
Rewards to claim are 0.

---------