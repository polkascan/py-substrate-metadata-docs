
# Xyk

---------
## Calls

---------
### activate_liquidity_v2
#### Attributes
| Name | Type |
| -------- | -------- | 
| liquidity_token_id | `TokenId` | 
| amount | `Balance` | 
| use_balance_from | `Option<ActivateKind>` | 

#### Python
```python
call = substrate.compose_call(
    'Xyk', 'activate_liquidity_v2', {
    'amount': 'u128',
    'liquidity_token_id': 'u32',
    'use_balance_from': (
        None,
        (
            'AvailableBalance',
            'StakedUnactivatedReserves',
            'UnspentReserves',
        ),
    ),
}
)
```

---------
### burn_liquidity
#### Attributes
| Name | Type |
| -------- | -------- | 
| first_asset_id | `TokenId` | 
| second_asset_id | `TokenId` | 
| liquidity_asset_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Xyk', 'burn_liquidity', {
    'first_asset_id': 'u32',
    'liquidity_asset_amount': 'u128',
    'second_asset_id': 'u32',
}
)
```

---------
### buy_asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| sold_asset_id | `TokenId` | 
| bought_asset_id | `TokenId` | 
| bought_asset_amount | `Balance` | 
| max_amount_in | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Xyk', 'buy_asset', {
    'bought_asset_amount': 'u128',
    'bought_asset_id': 'u32',
    'max_amount_in': 'u128',
    'sold_asset_id': 'u32',
}
)
```

---------
### claim_rewards_all_v2
#### Attributes
| Name | Type |
| -------- | -------- | 
| liquidity_token_id | `TokenId` | 

#### Python
```python
call = substrate.compose_call(
    'Xyk', 'claim_rewards_all_v2', {'liquidity_token_id': 'u32'}
)
```

---------
### claim_rewards_v2
#### Attributes
| Name | Type |
| -------- | -------- | 
| liquidity_token_id | `TokenId` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Xyk', 'claim_rewards_v2', {
    'amount': 'u128',
    'liquidity_token_id': 'u32',
}
)
```

---------
### compound_rewards
#### Attributes
| Name | Type |
| -------- | -------- | 
| liquidity_asset_id | `TokenId` | 
| amount_permille | `Permill` | 

#### Python
```python
call = substrate.compose_call(
    'Xyk', 'compound_rewards', {
    'amount_permille': 'u32',
    'liquidity_asset_id': 'u32',
}
)
```

---------
### create_pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| first_asset_id | `TokenId` | 
| first_asset_amount | `Balance` | 
| second_asset_id | `TokenId` | 
| second_asset_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Xyk', 'create_pool', {
    'first_asset_amount': 'u128',
    'first_asset_id': 'u32',
    'second_asset_amount': 'u128',
    'second_asset_id': 'u32',
}
)
```

---------
### deactivate_liquidity_v2
#### Attributes
| Name | Type |
| -------- | -------- | 
| liquidity_token_id | `TokenId` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Xyk', 'deactivate_liquidity_v2', {
    'amount': 'u128',
    'liquidity_token_id': 'u32',
}
)
```

---------
### mint_liquidity
#### Attributes
| Name | Type |
| -------- | -------- | 
| first_asset_id | `TokenId` | 
| second_asset_id | `TokenId` | 
| first_asset_amount | `Balance` | 
| expected_second_asset_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Xyk', 'mint_liquidity', {
    'expected_second_asset_amount': 'u128',
    'first_asset_amount': 'u128',
    'first_asset_id': 'u32',
    'second_asset_id': 'u32',
}
)
```

---------
### mint_liquidity_using_vesting_native_tokens
#### Attributes
| Name | Type |
| -------- | -------- | 
| vesting_native_asset_amount | `Balance` | 
| second_asset_id | `TokenId` | 
| expected_second_asset_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Xyk', 'mint_liquidity_using_vesting_native_tokens', {
    'expected_second_asset_amount': 'u128',
    'second_asset_id': 'u32',
    'vesting_native_asset_amount': 'u128',
}
)
```

---------
### mint_liquidity_using_vesting_native_tokens_by_vesting_index
#### Attributes
| Name | Type |
| -------- | -------- | 
| native_asset_vesting_index | `u32` | 
| vesting_native_asset_unlock_some_amount_or_all | `Option<Balance>` | 
| second_asset_id | `TokenId` | 
| expected_second_asset_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Xyk', 'mint_liquidity_using_vesting_native_tokens_by_vesting_index', {
    'expected_second_asset_amount': 'u128',
    'native_asset_vesting_index': 'u32',
    'second_asset_id': 'u32',
    'vesting_native_asset_unlock_some_amount_or_all': (
        None,
        'u128',
    ),
}
)
```

---------
### multiswap_buy_asset
Executes a multiswap buy asset in a series of buy asset atomic swaps.

Multiswaps must fee lock instead of paying transaction fees.

First the multiswap is prevalidated, if it is successful then the extrinsic is accepted
and the exchange commission will be charged upon execution on the *first* swap using *max_amount_in*.
multiswap_buy_asset cannot have two (or more) atomic swaps on the same pool.
multiswap_buy_asset prevaildation only checks for whether there are enough funds to pay for the exchange commission.
Failure to have the required amount of first asset funds will result in failure (and charging of the exchange commission).

Upon failure of an atomic swap or bad slippage, all the atomic swaps are reverted and the exchange commission is charged.
Upon such a failure, the extrinsic is marked &quot;successful&quot;, but an event for the failure is emitted

\# Args:
- `swap_token_list` - This list of tokens is the route of the atomic swaps, starting with the asset sold and ends with the asset finally bought
- `bought_asset_amount`: The amount of the last asset bought
- `max_amount_in` - The maximum amount of first asset that can be sold in order to not fail on slippage. Slippage failures still charge exchange commission.
#### Attributes
| Name | Type |
| -------- | -------- | 
| swap_token_list | `Vec<TokenId>` | 
| bought_asset_amount | `Balance` | 
| max_amount_in | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Xyk', 'multiswap_buy_asset', {
    'bought_asset_amount': 'u128',
    'max_amount_in': 'u128',
    'swap_token_list': ['u32'],
}
)
```

---------
### multiswap_sell_asset
Executes a multiswap sell asset in a series of sell asset atomic swaps.

Multiswaps must fee lock instead of paying transaction fees.

First the multiswap is prevalidated, if it is successful then the extrinsic is accepted
and the exchange commission will be charged upon execution on the **first** swap using **sold_asset_amount**.

Upon failure of an atomic swap or bad slippage, all the atomic swaps are reverted and the exchange commission is charged.
Upon such a failure, the extrinsic is marked &quot;successful&quot;, but an event for the failure is emitted

\# Args:
- `swap_token_list` - This list of tokens is the route of the atomic swaps, starting with the asset sold and ends with the asset finally bought
- `sold_asset_amount`: The amount of the first asset sold
- `min_amount_out` - The minimum amount of last asset that must be bought in order to not fail on slippage. Slippage failures still charge exchange commission.
#### Attributes
| Name | Type |
| -------- | -------- | 
| swap_token_list | `Vec<TokenId>` | 
| sold_asset_amount | `Balance` | 
| min_amount_out | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Xyk', 'multiswap_sell_asset', {
    'min_amount_out': 'u128',
    'sold_asset_amount': 'u128',
    'swap_token_list': ['u32'],
}
)
```

---------
### provide_liquidity_with_conversion
#### Attributes
| Name | Type |
| -------- | -------- | 
| liquidity_asset_id | `TokenId` | 
| provided_asset_id | `TokenId` | 
| provided_asset_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Xyk', 'provide_liquidity_with_conversion', {
    'liquidity_asset_id': 'u32',
    'provided_asset_amount': 'u128',
    'provided_asset_id': 'u32',
}
)
```

---------
### sell_asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| sold_asset_id | `TokenId` | 
| bought_asset_id | `TokenId` | 
| sold_asset_amount | `Balance` | 
| min_amount_out | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Xyk', 'sell_asset', {
    'bought_asset_id': 'u32',
    'min_amount_out': 'u128',
    'sold_asset_amount': 'u128',
    'sold_asset_id': 'u32',
}
)
```

---------
### update_pool_promotion
#### Attributes
| Name | Type |
| -------- | -------- | 
| liquidity_token_id | `TokenId` | 
| liquidity_mining_issuance_weight | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'Xyk', 'update_pool_promotion', {
    'liquidity_mining_issuance_weight': 'u8',
    'liquidity_token_id': 'u32',
}
)
```

---------
## Events

---------
### AssetsMultiBuySwapped
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Vec<TokenId>` | ```['u32']```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### AssetsMultiSellSwapped
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Vec<TokenId>` | ```['u32']```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### AssetsSwapped
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```

---------
### BuyAssetFailedDueToSlippage
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### LiquidityActivated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```

---------
### LiquidityBurned
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```

---------
### LiquidityDeactivated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```

---------
### LiquidityMinted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```

---------
### MultiBuyAssetFailedDueToSlippage
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Vec<TokenId>` | ```['u32']```
| None | `Balance` | ```u128```

---------
### MultiBuyAssetFailedOnAtomicSwap
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Vec<TokenId>` | ```['u32']```
| None | `Balance` | ```u128```

---------
### MultiSellAssetFailedDueToSlippage
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Vec<TokenId>` | ```['u32']```
| None | `Balance` | ```u128```

---------
### MultiSellAssetFailedOnAtomicSwap
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Vec<TokenId>` | ```['u32']```
| None | `Balance` | ```u128```

---------
### MultiSwapFailedDueToNotEnoughAssets
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Vec<TokenId>` | ```['u32']```
| None | `Balance` | ```u128```

---------
### PoolCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```

---------
### PoolPromotionUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenId` | ```u32```
| None | `Option<u8>` | ```(None, 'u8')```

---------
### RewardsClaimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```

---------
### SellAssetFailedDueToSlippage
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```
| None | `TokenId` | ```u32```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
## Storage functions

---------
### LiquidityAssets

#### Python
```python
result = substrate.query(
    'Xyk', 'LiquidityAssets', [('u32', 'u32')]
)
```

#### Return value
```python
(None, 'u32')
```
---------
### LiquidityMiningActivePool

#### Python
```python
result = substrate.query(
    'Xyk', 'LiquidityMiningActivePool', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### LiquidityMiningActivePoolV2

#### Python
```python
result = substrate.query(
    'Xyk', 'LiquidityMiningActivePoolV2', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### LiquidityMiningActiveUser

#### Python
```python
result = substrate.query(
    'Xyk', 'LiquidityMiningActiveUser', [('AccountId', 'u32')]
)
```

#### Return value
```python
'u128'
```
---------
### LiquidityMiningPool

#### Python
```python
result = substrate.query(
    'Xyk', 'LiquidityMiningPool', ['u32']
)
```

#### Return value
```python
('u32', '[u64; 4]', '[u64; 4]')
```
---------
### LiquidityMiningUser

#### Python
```python
result = substrate.query(
    'Xyk', 'LiquidityMiningUser', [('AccountId', 'u32')]
)
```

#### Return value
```python
('u32', '[u64; 4]', '[u64; 4]')
```
---------
### LiquidityMiningUserClaimed

#### Python
```python
result = substrate.query(
    'Xyk', 'LiquidityMiningUserClaimed', [('AccountId', 'u32')]
)
```

#### Return value
```python
'u128'
```
---------
### LiquidityMiningUserToBeClaimed

#### Python
```python
result = substrate.query(
    'Xyk', 'LiquidityMiningUserToBeClaimed', [('AccountId', 'u32')]
)
```

#### Return value
```python
'u128'
```
---------
### LiquidityPools

#### Python
```python
result = substrate.query(
    'Xyk', 'LiquidityPools', ['u32']
)
```

#### Return value
```python
(None, ('u32', 'u32'))
```
---------
### Pools

#### Python
```python
result = substrate.query(
    'Xyk', 'Pools', [('u32', 'u32')]
)
```

#### Return value
```python
('u128', 'u128')
```
---------
### RewardsInfo

#### Python
```python
result = substrate.query(
    'Xyk', 'RewardsInfo', ['AccountId', 'u32']
)
```

#### Return value
```python
{
    'activated_amount': 'u128',
    'last_checkpoint': 'u32',
    'missing_at_last_checkpoint': '[u64; 4]',
    'pool_ratio_at_last_checkpoint': '[u64; 4]',
    'rewards_already_claimed': 'u128',
    'rewards_not_yet_claimed': 'u128',
}
```
---------
## Constants

---------
### BuyAndBurnFeePercentage
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Xyk', 'BuyAndBurnFeePercentage')
```
---------
### LiquidityMiningIssuanceVault
 The account id that holds the liquidity mining issuance
#### Value
```python
'5EYCAe5ijiYetuT4xrRZx2vbVopfJjhvfsZ4546K1Mmdexb1'
```
#### Python
```python
constant = substrate.get_constant('Xyk', 'LiquidityMiningIssuanceVault')
```
---------
### PoolFeePercentage
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('Xyk', 'PoolFeePercentage')
```
---------
### RewardsDistributionPeriod
#### Value
```python
1200
```
#### Python
```python
constant = substrate.get_constant('Xyk', 'RewardsDistributionPeriod')
```
---------
### RewardsMigrateAccount
#### Value
```python
'5CPKwH7Dcru4msJaMcAsn5suNeXLrdME3tFg1djPyneHrwRY'
```
#### Python
```python
constant = substrate.get_constant('Xyk', 'RewardsMigrateAccount')
```
---------
### TreasuryFeePercentage
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Xyk', 'TreasuryFeePercentage')
```
---------
## Errors

---------
### AssetAlreadyExists
Asset already exists

---------
### AssetDoesNotExists
Asset does not exists

---------
### CalculateCumulativeWorkMaxRatioMathError

---------
### CalculateRewardsAllMathError

---------
### CalculateRewardsMathError

---------
### DisallowedPool
Pool considting of passed tokens id is blacklisted

---------
### DivisionByZero
Division by zero

---------
### FunctionNotAvailableForThisToken
Asset id is blacklisted

---------
### InsufficientInputAmount
Insufficient input amount

---------
### InsufficientOutputAmount
Insufficient output amount

---------
### LiquidityCheckpointMathError

---------
### LiquidityTokenCreationFailed
Liquidity token creation failed

---------
### MathOverflow
Math overflow

---------
### MultiBuyAssetCantHaveSamePoolAtomicSwaps

---------
### MultiSwapCantHaveSameTokenConsequetively

---------
### MultiSwapFailedOnBadSlippage

---------
### MultiSwapNotEnoughAssets

---------
### MultiswapShouldBeAtleastTwoHops

---------
### NoRights

---------
### NoSuchLiquidityAsset
No such liquidity asset exists

---------
### NoSuchPool
No such pool exists

---------
### NonSlippageMultiSwapFailure

---------
### NotAPromotedPool
Not a promoted pool

---------
### NotEnoughAssets
Not enought assets

---------
### NotEnoughReserve
Not enought reserve

---------
### NotEnoughRewardsEarned
Not enough rewards earned

---------
### NotMangataLiquidityAsset
Unexpected failure

---------
### PastTimeCalculation
Past time calculation

---------
### PoolAlreadyExists
Pool already Exists

---------
### PoolAlreadyPromoted
Pool already promoted

---------
### SameAsset
Asset ids cannot be the same

---------
### SecondAssetAmountExceededExpectations
Second asset amount exceeded expectations

---------
### SoldAmountTooLow
Sold Amount too low

---------
### TradingBlockedByMaintenanceMode
Trading blocked by maintenance mode

---------
### UnexpectedFailure
Unexpected failure

---------
### ZeroAmount
Zero amount is not supported

---------