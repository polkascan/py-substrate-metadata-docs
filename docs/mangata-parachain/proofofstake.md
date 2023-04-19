
# ProofOfStake

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
    'ProofOfStake', 'activate_liquidity_v2', {
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
### claim_rewards_all_v2
#### Attributes
| Name | Type |
| -------- | -------- | 
| liquidity_token_id | `TokenId` | 

#### Python
```python
call = substrate.compose_call(
    'ProofOfStake', 'claim_rewards_all_v2', {'liquidity_token_id': 'u32'}
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
    'ProofOfStake', 'claim_rewards_v2', {
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
    'ProofOfStake', 'compound_rewards', {
    'amount_permille': 'u32',
    'liquidity_asset_id': 'u32',
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
    'ProofOfStake', 'deactivate_liquidity_v2', {
    'amount': 'u128',
    'liquidity_token_id': 'u32',
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
    'ProofOfStake', 'update_pool_promotion', {
    'liquidity_mining_issuance_weight': 'u8',
    'liquidity_token_id': 'u32',
}
)
```

---------
## Events

---------
### LiquidityActivated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
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
## Storage functions

---------
### LiquidityMiningActivePoolV2

#### Python
```python
result = substrate.query(
    'ProofOfStake', 'LiquidityMiningActivePoolV2', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### RewardsInfo

#### Python
```python
result = substrate.query(
    'ProofOfStake', 'RewardsInfo', ['AccountId', 'u32']
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
### LiquidityMiningIssuanceVault
 The account id that holds the liquidity mining issuance
#### Value
```python
'5EYCAe5ijiYetuT4xrRZx2vbVopfJjhvfsZ4546K1Mmdexb1'
```
#### Python
```python
constant = substrate.get_constant('ProofOfStake', 'LiquidityMiningIssuanceVault')
```
---------
### RewardsDistributionPeriod
#### Value
```python
1200
```
#### Python
```python
constant = substrate.get_constant('ProofOfStake', 'RewardsDistributionPeriod')
```
---------
## Errors

---------
### CalculateCumulativeWorkMaxRatioMathError

---------
### CalculateRewardsAllMathError

---------
### CalculateRewardsMathError

---------
### DivisionByZero
Division by zero

---------
### LiquidityCheckpointMathError

---------
### MathOverflow
Math overflow

---------
### NotAPromotedPool
Not a promoted pool

---------
### NotEnoughAssets
Not enought assets

---------
### NotEnoughRewardsEarned
Not enough rewards earned

---------
### PastTimeCalculation
Past time calculation

---------