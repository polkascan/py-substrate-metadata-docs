
# Parimutuel

---------
## Calls

---------
### buy
Buy parimutuel shares for the market&\#x27;s base asset.

\# Arguments

- `asset`: The outcome asset to buy the shares of.
- `amount`: The amount of base asset to spend
and of parimutuel shares to receive.
Keep in mind that there are external fees taken from this amount.

Complexity: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `Asset<MarketIdOf<T>>` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Parimutuel', 'buy', {
    'amount': 'u128',
    'asset': {
        'CategoricalOutcome': (
            'u128',
            'u16',
        ),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'ParimutuelShare': (
            'u128',
            'u16',
        ),
        'PoolShare': 'u128',
        'ScalarOutcome': (
            'u128',
            ('Long', 'Short'),
        ),
        'Ztg': None,
    },
}
)
```

---------
### claim_refunds
Refund the base asset of losing categorical outcome assets
in case that there was no account betting on the winner outcome.

\# Arguments

- `refund_asset`: The outcome asset to refund.

Complexity: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| refund_asset | `AssetOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Parimutuel', 'claim_refunds', {
    'refund_asset': {
        'CategoricalOutcome': (
            'u128',
            'u16',
        ),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'ParimutuelShare': (
            'u128',
            'u16',
        ),
        'PoolShare': 'u128',
        'ScalarOutcome': (
            'u128',
            ('Long', 'Short'),
        ),
        'Ztg': None,
    },
}
)
```

---------
### claim_rewards
Claim winnings from a resolved market.

Complexity: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| market_id | `MarketIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Parimutuel', 'claim_rewards', {'market_id': 'u128'}
)
```

---------
## Events

---------
### BalanceRefunded
A market base asset was refunded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| market_id | `MarketIdOf<T>` | ```u128```
| asset | `AssetOf<T>` | ```{'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32', 'ParimutuelShare': ('u128', 'u16')}```
| refunded_balance | `BalanceOf<T>` | ```u128```
| sender | `AccountIdOf<T>` | ```AccountId```

---------
### OutcomeBought
An outcome was bought.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| market_id | `MarketIdOf<T>` | ```u128```
| buyer | `AccountIdOf<T>` | ```AccountId```
| asset | `AssetOf<T>` | ```{'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32', 'ParimutuelShare': ('u128', 'u16')}```
| amount_minus_fees | `BalanceOf<T>` | ```u128```
| fees | `BalanceOf<T>` | ```u128```

---------
### RewardsClaimed
Rewards of the pot were claimed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| market_id | `MarketIdOf<T>` | ```u128```
| asset | `AssetOf<T>` | ```{'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32', 'ParimutuelShare': ('u128', 'u16')}```
| withdrawn_asset_balance | `BalanceOf<T>` | ```u128```
| base_asset_payoff | `BalanceOf<T>` | ```u128```
| sender | `AccountIdOf<T>` | ```AccountId```

---------
## Storage functions

---------
## Constants

---------
### MinBetSize
 The minimum amount each bet must be. Must be larger than or equal to the existential
 deposit of parimutuel shares.
#### Value
```python
5000000000
```
#### Python
```python
constant = substrate.get_constant('Parimutuel', 'MinBetSize')
```
---------
### PalletId
#### Value
```python
'0x7a67652f70726d74'
```
#### Python
```python
constant = substrate.get_constant('Parimutuel', 'PalletId')
```
---------
## Errors

---------
### AmountBelowMinimumBetSize
The specified amount is below the minimum bet size.

---------
### InconsistentState
Action cannot be completed because an unexpected error has occurred. This should be
reported to protocol maintainers.

---------
### InsufficientBalance
The specified amount can not be transferred.

---------
### InvalidOutcomeAsset
The specified asset was not found in the market assets.

---------
### InvalidScoringRule
The scoring rule is not parimutuel.

---------
### MarketIsNotActive
The market is not active.

---------
### MarketIsNotResolvedYet
The market is not resolved yet.

---------
### NoResolvedOutcome
There is no resolved outcome present for the market.

---------
### NoRewardShareOutstanding
There was no buyer for the winning outcome or all winners already claimed their rewards.
Use the `refund` extrinsic to get the initial bet back,
in case there was no buyer for the winning outcome.

---------
### NoRewardToDistribute
There is no reward to distribute.

---------
### NoWinningShares
There is no reward, because there are no winning shares.

---------
### NotCategorical
Only categorical markets are allowed for parimutuels.

---------
### NotParimutuelOutcome
The specified asset is not a parimutuel share.

---------
### RefundNotAllowed
The refund is not allowed.

---------
### RefundableBalanceIsZero
There is no balance to refund.

---------
### Unexpected
An unexpected error occured. This should never happen!
There was an internal coding mistake.

---------