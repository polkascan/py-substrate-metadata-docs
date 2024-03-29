
# NeoSwaps

---------
## Calls

---------
### buy
Buy outcome tokens from the specified market.

The `amount_in` is paid in collateral. The transaction fails if the amount of outcome
tokens received is smaller than `min_amount_out`. The user must correctly specify the
number of outcomes for benchmarking reasons.

The `amount_in` parameter must also satisfy lower and upper limits due to numerical
constraints. In fact, after `amount_in` has been adjusted for fees, the following must
hold:

- `amount_in_minus_fees &lt;= EXP_NUMERICAL_LIMIT * pool.liquidity_parameter`.
- `exp(amount_in_minus_fees/pool.liquidity_parameter) - 1 + p &lt;= LN_NUMERICAL_LIMIT`,
  where `p` is the spot price of `asset_out`.

\# Parameters

- `origin`: The origin account making the purchase.
- `market_id`: Identifier for the market related to the trade.
- `asset_count`: Number of assets in the pool.
- `asset_out`: Asset to be purchased.
- `amount_in`: Amount of collateral paid by the user.
- `min_amount_out`: Minimum number of outcome tokens the user expects to receive.

\# Complexity

Depends on the implementation of `CompleteSetOperationsApi` and `ExternalFees`; when
using the canonical implementations, the runtime complexity is `O(asset_count)`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| market_id | `MarketIdOf<T>` | 
| asset_count | `AssetIndexType` | 
| asset_out | `AssetOf<T>` | 
| amount_in | `BalanceOf<T>` | 
| min_amount_out | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'NeoSwaps', 'buy', {
    'amount_in': 'u128',
    'asset_count': 'u16',
    'asset_out': {
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
    'market_id': 'u128',
    'min_amount_out': 'u128',
}
)
```

---------
### deploy_pool
Deploy a pool for the specified market and provide liquidity.

The sender specifies a vector of `spot_prices` for the market&\#x27;s outcomes in the order
given by the `MarketCommonsApi`. The transaction will fail if the spot prices don&\#x27;t add
up to exactly `BASE`.

Depending on the values in the `spot_prices`, the transaction will transfer different
amounts of each outcome to the pool. The sender specifies a maximum `amount` of outcome
tokens to spend.

Note that the sender must acquire the outcome tokens in a separate transaction by using
complete set operations. It&\#x27;s therefore convenient to batch this function together with
a `buy_complete_set` with `amount` as amount of complete sets to buy.

Deploying the pool will cost the signer an additional fee to the tune of the
collateral&\#x27;s existential deposit. This fee is placed in the pool account and ensures
that swap fees can be stored in the pool account without triggering dusting or failed
transfers.

The operation is currently limited to binary and scalar markets.

\# Complexity

`O(n)` where `n` is the number of assets in the pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| market_id | `MarketIdOf<T>` | 
| amount | `BalanceOf<T>` | 
| spot_prices | `Vec<BalanceOf<T>>` | 
| swap_fee | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'NeoSwaps', 'deploy_pool', {
    'amount': 'u128',
    'market_id': 'u128',
    'spot_prices': ['u128'],
    'swap_fee': 'u128',
}
)
```

---------
### exit
Exit the liquidity pool for the specified market.

The LP relinquishes pool shares in exchange for withdrawing outcome tokens from the
pool. The `min_amounts_out` vector specifies the minimum number of each outcome token
that the LP expects to withdraw. These minimum amounts are used to adjust the outcome
balances in the pool, taking into account the reduction in the LP&\#x27;s pool share
ownership.

The transaction will fail unless the LP withdraws their fees from the pool beforehand. A
batch transaction is very useful here.

If the LP withdraws all pool shares that exist, then the pool is afterwards destroyed. A
new pool can be deployed at any time, provided that the market is still open. If there
are funds left in the pool account (this can happen due to exit fees), the remaining
funds are destroyed.

The LP is not allowed to leave a positive but small amount liquidity in the pool. If the
liquidity parameter drops below a certain threshold, the transaction will fail. The only
solution is to withdraw _all_ liquidity and let the pool die.

\# Parameters

- `market_id`: Identifier for the market related to the pool.
- `pool_shares_amount_out`: The number of pool shares the LP will relinquish.
- `min_amounts_out`: Vector of the minimum amounts of each outcome token the LP expects
  to withdraw (with outcomes specified in the order given by `MarketCommonsApi`).

\# Complexity

`O(n + d)` where `n` is the number of assets in the pool and `d` is the depth of the
pool&\#x27;s liquidity tree, or, equivalently, `log_2(m)` where `m` is the number of liquidity
providers in the pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| market_id | `MarketIdOf<T>` | 
| pool_shares_amount_out | `BalanceOf<T>` | 
| min_amounts_out | `Vec<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'NeoSwaps', 'exit', {
    'market_id': 'u128',
    'min_amounts_out': ['u128'],
    'pool_shares_amount_out': 'u128',
}
)
```

---------
### join
Join the liquidity pool for the specified market.

The LP receives pool shares in exchange for staking outcome tokens into the pool. The
`max_amounts_in` vector specifies the maximum number of each outcome token that the LP is
willing to deposit. These amounts are used to adjust the outcome balances in the pool
according to the new proportion of pool shares owned by the LP.

Note that the user must acquire the outcome tokens in a separate transaction, either by
buying from the pool or by using complete set operations.

\# Parameters

- `market_id`: Identifier for the market related to the pool.
- `pool_shares_amount`: The number of new pool shares the LP will receive.
- `max_amounts_in`: Vector of the maximum amounts of each outcome token the LP is
  willing to deposit (with outcomes specified in the order of `MarketCommonsApi`).

\# Complexity

`O(n + d)` where `n` is the number of assets in the pool and `d` is the depth of the
pool&\#x27;s liquidity tree, or, equivalently, `log_2(m)` where `m` is the number of liquidity
providers in the pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| market_id | `MarketIdOf<T>` | 
| pool_shares_amount | `BalanceOf<T>` | 
| max_amounts_in | `Vec<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'NeoSwaps', 'join', {
    'market_id': 'u128',
    'max_amounts_in': ['u128'],
    'pool_shares_amount': 'u128',
}
)
```

---------
### sell
Sell outcome tokens to the specified market.

The `amount_in` is paid in outcome tokens. The transaction fails if the amount of outcome
tokens received is smaller than `min_amount_out`. The user must correctly specify the
number of outcomes for benchmarking reasons.

The `amount_in` parameter must also satisfy lower and upper limits due to numerical
constraints. In fact, the following must hold:

- `amount_in &lt;= EXP_NUMERICAL_LIMIT * pool.liquidity_parameter`.
- The spot price of `asset_in` is greater than `exp(-EXP_NUMERICAL_LIMIT)` before and
  after execution

\# Parameters

- `origin`: The origin account making the sale.
- `market_id`: Identifier for the market related to the trade.
- `asset_count`: Number of assets in the pool.
- `asset_in`: Asset to be sold.
- `amount_in`: Amount of outcome tokens paid by the user.
- `min_amount_out`: Minimum amount of collateral the user expects to receive.

\# Complexity

Depends on the implementation of `CompleteSetOperationsApi` and `ExternalFees`; when
using the canonical implementations, the runtime complexity is `O(asset_count)`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| market_id | `MarketIdOf<T>` | 
| asset_count | `AssetIndexType` | 
| asset_in | `AssetOf<T>` | 
| amount_in | `BalanceOf<T>` | 
| min_amount_out | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'NeoSwaps', 'sell', {
    'amount_in': 'u128',
    'asset_count': 'u16',
    'asset_in': {
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
    'market_id': 'u128',
    'min_amount_out': 'u128',
}
)
```

---------
### withdraw_fees
Withdraw swap fees from the specified market.

The transaction will fail if the caller is not a liquidity provider. Should always be
used before calling `exit`.

\# Parameters

- `market_id`: Identifier for the market related to the pool.

\# Complexity

`O(1)`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| market_id | `MarketIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'NeoSwaps', 'withdraw_fees', {'market_id': 'u128'}
)
```

---------
## Events

---------
### BuyExecuted
Informant bought a position. `amount_in` is the amount of collateral paid by `who`,
including swap and external fees.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| market_id | `MarketIdOf<T>` | ```u128```
| asset_out | `AssetOf<T>` | ```{'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32', 'ParimutuelShare': ('u128', 'u16')}```
| amount_in | `BalanceOf<T>` | ```u128```
| amount_out | `BalanceOf<T>` | ```u128```
| swap_fee_amount | `BalanceOf<T>` | ```u128```
| external_fee_amount | `BalanceOf<T>` | ```u128```

---------
### ExitExecuted
Liquidity provider left the pool.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| market_id | `MarketIdOf<T>` | ```u128```
| pool_shares_amount | `BalanceOf<T>` | ```u128```
| amounts_out | `Vec<BalanceOf<T>>` | ```['u128']```
| new_liquidity_parameter | `BalanceOf<T>` | ```u128```

---------
### FeesWithdrawn
Liquidity provider withdrew fees.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| market_id | `MarketIdOf<T>` | ```u128```
| amount | `BalanceOf<T>` | ```u128```

---------
### JoinExecuted
Liquidity provider joined the pool.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| market_id | `MarketIdOf<T>` | ```u128```
| pool_shares_amount | `BalanceOf<T>` | ```u128```
| amounts_in | `Vec<BalanceOf<T>>` | ```['u128']```
| new_liquidity_parameter | `BalanceOf<T>` | ```u128```

---------
### PoolDeployed
Pool was createed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| market_id | `MarketIdOf<T>` | ```u128```
| account_id | `T::AccountId` | ```AccountId```
| reserves | `BTreeMap<AssetOf<T>, BalanceOf<T>>` | ```scale_info::92```
| collateral | `AssetOf<T>` | ```{'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32', 'ParimutuelShare': ('u128', 'u16')}```
| liquidity_parameter | `BalanceOf<T>` | ```u128```
| pool_shares_amount | `BalanceOf<T>` | ```u128```
| swap_fee | `BalanceOf<T>` | ```u128```

---------
### PoolDestroyed
Pool was destroyed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| market_id | `MarketIdOf<T>` | ```u128```
| amounts_out | `Vec<BalanceOf<T>>` | ```['u128']```

---------
### SellExecuted
Informant sold a position. `amount_out` is the amount of collateral received by `who`,
including swap and external fees.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| market_id | `MarketIdOf<T>` | ```u128```
| asset_in | `AssetOf<T>` | ```{'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32', 'ParimutuelShare': ('u128', 'u16')}```
| amount_in | `BalanceOf<T>` | ```u128```
| amount_out | `BalanceOf<T>` | ```u128```
| swap_fee_amount | `BalanceOf<T>` | ```u128```
| external_fee_amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### Pools

#### Python
```python
result = substrate.query(
    'NeoSwaps', 'Pools', ['u128']
)
```

#### Return value
```python
{
    'account_id': 'AccountId',
    'collateral': {
        'CategoricalOutcome': ('u128', 'u16'),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'ParimutuelShare': ('u128', 'u16'),
        'PoolShare': 'u128',
        'ScalarOutcome': ('u128', ('Long', 'Short')),
        'Ztg': None,
    },
    'liquidity_parameter': 'u128',
    'liquidity_shares_manager': {
        'abandoned_nodes': ['u32'],
        'account_to_index': 'scale_info::556',
        'nodes': [
            {
                'account': (None, 'AccountId'),
                'descendant_stake': 'u128',
                'fees': 'u128',
                'lazy_fees': 'u128',
                'stake': 'u128',
            },
        ],
    },
    'reserves': 'scale_info::92',
    'swap_fee': 'u128',
}
```
---------
## Constants

---------
### MaxLiquidityTreeDepth
 The maximum allowed liquidity tree depth per pool. Each pool can support `2^(depth + 1)
 - 1` liquidity providers. **Must** be less than 16.
#### Value
```python
9
```
#### Python
```python
constant = substrate.get_constant('NeoSwaps', 'MaxLiquidityTreeDepth')
```
---------
### MaxSwapFee
#### Value
```python
1000000000
```
#### Python
```python
constant = substrate.get_constant('NeoSwaps', 'MaxSwapFee')
```
---------
### PalletId
#### Value
```python
'0x7a67652f6e656f73'
```
#### Python
```python
constant = substrate.get_constant('NeoSwaps', 'PalletId')
```
---------
## Errors

---------
### AmountInAboveMax
Amount paid is above the specified maximum.

---------
### AmountOutBelowMin
Amount received is below the specified minimum.

---------
### AssetCountAboveMax
The number of assets in the pool is above the allowed maximum.

---------
### AssetNotFound
Specified asset was not found in this pool.

---------
### DuplicatePool
Market already has an associated pool.

---------
### IncorrectAssetCount
Incorrect asset count.

---------
### IncorrectVecLen

---------
### InsufficientPoolShares
User doesn&\#x27;t own enough pool shares.

---------
### InvalidSpotPrices
Sum of spot prices is not `1`.

---------
### InvalidTradingMechanism
Market&\#x27;s trading mechanism is not LMSR.

---------
### LiquidityTooLow
The liquidity in the pool is too low.

---------
### LiquidityTreeError
An error occurred when handling the liquidty tree.

---------
### MarketNotActive
Pool can only be traded on if the market is active.

---------
### MathError
Some calculation failed. This shouldn&\#x27;t happen.

---------
### MinRelativeLiquidityThresholdViolated
The relative value of a new LP position is too low.

---------
### NotAllowed
The user is not allowed to execute this command.

---------
### NotImplemented
This feature is not yet implemented.

---------
### NumericalLimits
Some value in the operation is too large or small.

---------
### OutstandingFees
Outstanding fees prevent liquidity withdrawal.

---------
### PoolNotFound
Specified market does not have a pool.

---------
### SpotPriceAboveMax
Spot price is above the allowed maximum.

---------
### SpotPriceBelowMin
Spot price is below the allowed minimum.

---------
### SwapFeeAboveMax
Pool&\#x27;s swap fee exceeds the allowed upper limit.

---------
### SwapFeeBelowMin
Pool&\#x27;s swap fee is below the allowed lower limit.

---------
### Unexpected
This shouldn&\#x27;t happen.

---------
### ZeroAmount
Specified monetary amount is zero.

---------