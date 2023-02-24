
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
| liquidity_mining_issuance_weight | `Option<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Xyk', 'update_pool_promotion', {
    'liquidity_mining_issuance_weight': (
        None,
        'u8',
    ),
    'liquidity_token_id': 'u32',
}
)
```

---------
## Events

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
### NoRights

---------
### NoSuchLiquidityAsset
No such liquidity asset exists

---------
### NoSuchPool
No such pool exists

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
### UnexpectedFailure
Unexpected failure

---------
### ZeroAmount
Zero amount is not supported

---------