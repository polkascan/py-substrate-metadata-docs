
# LBP

---------
## Calls

---------
### add_liquidity
Add liquidity to a pool.

Assets to add has to match the pool assets. At least one amount has to be non-zero.

The dispatch origin for this call must be signed by the pool owner.

Parameters:
- `pool_id`: The identifier of the pool
- `amount_a`: The identifier of the asset and the amount to add.
- `amount_b`: The identifier of the second asset and the amount to add.

Emits `LiquidityAdded` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount_a | `(AssetId, BalanceOf<T>)` | 
| amount_b | `(AssetId, BalanceOf<T>)` | 

#### Python
```python
call = substrate.compose_call(
    'LBP', 'add_liquidity', {
    'amount_a': ('u32', 'u128'),
    'amount_b': ('u32', 'u128'),
}
)
```

---------
### buy
Trade `asset_in` for `asset_out`.

Executes a swap of `asset_in` for `asset_out`. Price is determined by the pool and is
affected by the amount and the proportion of the pool assets and the weights.

Trading `fee` is distributed to the `fee_collector`.

Parameters:
- `asset_in`: The identifier of the asset being transferred from the account to the pool.
- `asset_out`: The identifier of the asset being transferred from the pool to the account.
- `amount`: The amount of `asset_out`.
- `max_limit`: maximum amount of `asset_in` to be sold in exchange for `asset_out`.

Emits `BuyExecuted` when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_out | `AssetId` | 
| asset_in | `AssetId` | 
| amount | `BalanceOf<T>` | 
| max_limit | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LBP', 'buy', {
    'amount': 'u128',
    'asset_in': 'u32',
    'asset_out': 'u32',
    'max_limit': 'u128',
}
)
```

---------
### create_pool
Create a new liquidity bootstrapping pool for given asset pair.

For any asset pair, only one pool can exist at a time.

The dispatch origin for this call must be `T::CreatePoolOrigin`.
The pool is created with initial liquidity provided by the `pool_owner` who must have
sufficient funds free.

The pool starts uninitialized and update_pool call should be called once created to set the start block.

This function should be dispatched from governing entity `T::CreatePoolOrigin`

Parameters:
- `pool_owner`: the future owner of the new pool.
- `asset_a`: { asset_id, amount } Asset ID and initial liquidity amount.
- `asset_b`: { asset_id, amount } Asset ID and initial liquidity amount.
- `initial_weight`: Initial weight of the asset_a. 1_000_000 corresponding to 1% and 100_000_000 to 100%
this should be higher than final weight
- `final_weight`: Final weight of the asset_a. 1_000_000 corresponding to 1% and 100_000_000 to 100%
this should be lower than initial weight
- `weight_curve`: The weight function used to update the LBP weights. Currently,
there is only one weight function implemented, the linear function.
- `fee`: The trading fee charged on every trade distributed to `fee_collector`.
- `fee_collector`: The account to which trading fees will be transferred.
- `repay_target`: The amount of tokens to repay to separate fee_collector account. Until this amount is
reached, fee will be increased to 20% and taken from the pool

Emits `PoolCreated` event when successful.

BEWARE: We are taking the fee from the accumulated asset. If the accumulated asset is sold to the pool,
the fee cost is transferred to the pool. If its bought from the pool the buyer bears the cost.
This increases the price of the sold asset on every trade. Make sure to only run this with
previously illiquid assets.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_owner | `T::AccountId` | 
| asset_a | `AssetId` | 
| asset_a_amount | `Balance` | 
| asset_b | `AssetId` | 
| asset_b_amount | `Balance` | 
| initial_weight | `LBPWeight` | 
| final_weight | `LBPWeight` | 
| weight_curve | `WeightCurveType` | 
| fee | `(u32, u32)` | 
| fee_collector | `T::AccountId` | 
| repay_target | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'LBP', 'create_pool', {
    'asset_a': 'u32',
    'asset_a_amount': 'u128',
    'asset_b': 'u32',
    'asset_b_amount': 'u128',
    'fee': ('u32', 'u32'),
    'fee_collector': 'AccountId',
    'final_weight': 'u32',
    'initial_weight': 'u32',
    'pool_owner': 'AccountId',
    'repay_target': 'u128',
    'weight_curve': ('Linear', ),
}
)
```

---------
### remove_liquidity
Transfer all the liquidity from a pool back to the pool owner and destroy the pool.
The pool data are also removed from the storage.

The pool can&\#x27;t be destroyed during the sale.

The dispatch origin for this call must be signed by the pool owner.

Parameters:
- `amount_a`: The identifier of the asset and the amount to add.

Emits &\#x27;LiquidityRemoved&\#x27; when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LBP', 'remove_liquidity', {'pool_id': 'AccountId'}
)
```

---------
### sell
Trade `asset_in` for `asset_out`.

Executes a swap of `asset_in` for `asset_out`. Price is determined by the pool and is
affected by the amount and proportion of the pool assets and the weights.

Trading `fee` is distributed to the `fee_collector`.

Parameters:
- `asset_in`: The identifier of the asset being transferred from the account to the pool.
- `asset_out`: The identifier of the asset being transferred from the pool to the account.
- `amount`: The amount of `asset_in`
- `max_limit`: minimum amount of `asset_out` / amount of asset_out to be obtained from the pool in exchange for `asset_in`.

Emits `SellExecuted` when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_in | `AssetId` | 
| asset_out | `AssetId` | 
| amount | `BalanceOf<T>` | 
| max_limit | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LBP', 'sell', {
    'amount': 'u128',
    'asset_in': 'u32',
    'asset_out': 'u32',
    'max_limit': 'u128',
}
)
```

---------
### update_pool_data
Update pool data of a pool.

The dispatch origin for this call must be signed by the pool owner.

The pool can be updated only if the sale has not already started.

At least one of the following optional parameters has to be specified.

Parameters:
- `pool_id`: The identifier of the pool to be updated.
- `start`: The new starting time of the sale. This parameter is optional.
- `end`: The new ending time of the sale. This parameter is optional.
- `initial_weight`: The new initial weight. This parameter is optional.
- `final_weight`: The new final weight. This parameter is optional.
- `fee`: The new trading fee charged on every trade. This parameter is optional.
- `fee_collector`: The new receiver of trading fees. This parameter is optional.

Emits `PoolUpdated` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId<T>` | 
| pool_owner | `Option<T::AccountId>` | 
| start | `Option<T::BlockNumber>` | 
| end | `Option<T::BlockNumber>` | 
| initial_weight | `Option<LBPWeight>` | 
| final_weight | `Option<LBPWeight>` | 
| fee | `Option<(u32, u32)>` | 
| fee_collector | `Option<T::AccountId>` | 
| repay_target | `Option<Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'LBP', 'update_pool_data', {
    'end': (None, 'u32'),
    'fee': (None, ('u32', 'u32')),
    'fee_collector': (
        None,
        'AccountId',
    ),
    'final_weight': (None, 'u32'),
    'initial_weight': (None, 'u32'),
    'pool_id': 'AccountId',
    'pool_owner': (None, 'AccountId'),
    'repay_target': (None, 'u128'),
    'start': (None, 'u32'),
}
)
```

---------
## Events

---------
### BuyExecuted
Purchase executed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| asset_out | `AssetId` | ```u32```
| asset_in | `AssetId` | ```u32```
| amount | `BalanceOf<T>` | ```u128```
| buy_price | `BalanceOf<T>` | ```u128```
| fee_asset | `AssetId` | ```u32```
| fee_amount | `BalanceOf<T>` | ```u128```

---------
### LiquidityAdded
New liquidity was provided to the pool.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| asset_a | `AssetId` | ```u32```
| asset_b | `AssetId` | ```u32```
| amount_a | `BalanceOf<T>` | ```u128```
| amount_b | `BalanceOf<T>` | ```u128```

---------
### LiquidityRemoved
Liquidity was removed from the pool and the pool was destroyed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| asset_a | `AssetId` | ```u32```
| asset_b | `AssetId` | ```u32```
| amount_a | `BalanceOf<T>` | ```u128```
| amount_b | `BalanceOf<T>` | ```u128```

---------
### PoolCreated
Pool was created by the `CreatePool` origin.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool | `PoolId<T>` | ```AccountId```
| data | `Pool<T::AccountId, T::BlockNumber>` | ```{'owner': 'AccountId', 'start': (None, 'u32'), 'end': (None, 'u32'), 'assets': ('u32', 'u32'), 'initial_weight': 'u32', 'final_weight': 'u32', 'weight_curve': ('Linear',), 'fee': ('u32', 'u32'), 'fee_collector': 'AccountId', 'repay_target': 'u128'}```

---------
### PoolUpdated
Pool data were updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool | `PoolId<T>` | ```AccountId```
| data | `Pool<T::AccountId, T::BlockNumber>` | ```{'owner': 'AccountId', 'start': (None, 'u32'), 'end': (None, 'u32'), 'assets': ('u32', 'u32'), 'initial_weight': 'u32', 'final_weight': 'u32', 'weight_curve': ('Linear',), 'fee': ('u32', 'u32'), 'fee_collector': 'AccountId', 'repay_target': 'u128'}```

---------
### SellExecuted
Sale executed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| asset_in | `AssetId` | ```u32```
| asset_out | `AssetId` | ```u32```
| amount | `BalanceOf<T>` | ```u128```
| sale_price | `BalanceOf<T>` | ```u128```
| fee_asset | `AssetId` | ```u32```
| fee_amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### FeeCollectorWithAsset
 Storage used for tracking existing fee collectors
 Not more than one fee collector per asset possible

#### Python
```python
result = substrate.query(
    'LBP', 'FeeCollectorWithAsset', ['AccountId', 'u32']
)
```

#### Return value
```python
'bool'
```
---------
### PoolData
 Details of a pool.

#### Python
```python
result = substrate.query(
    'LBP', 'PoolData', ['AccountId']
)
```

#### Return value
```python
{
    'assets': ('u32', 'u32'),
    'end': (None, 'u32'),
    'fee': ('u32', 'u32'),
    'fee_collector': 'AccountId',
    'final_weight': 'u32',
    'initial_weight': 'u32',
    'owner': 'AccountId',
    'repay_target': 'u128',
    'start': (None, 'u32'),
    'weight_curve': ('Linear', ),
}
```
---------
## Constants

---------
### MaxInRatio
 Max fraction of pool to sell in single transaction
#### Value
```python
3
```
#### Python
```python
constant = substrate.get_constant('LBP', 'MaxInRatio')
```
---------
### MaxOutRatio
 Max fraction of pool to buy in single transaction
#### Value
```python
3
```
#### Python
```python
constant = substrate.get_constant('LBP', 'MaxOutRatio')
```
---------
### MinPoolLiquidity
 Minimum pool liquidity, sole purpose of this is to keep the math working
#### Value
```python
1000000
```
#### Python
```python
constant = substrate.get_constant('LBP', 'MinPoolLiquidity')
```
---------
### MinTradingLimit
 Minimum trading limit, sole purpose of this is to keep the math working
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('LBP', 'MinTradingLimit')
```
---------
### repay_fee
#### Value
```python
(2, 10)
```
#### Python
```python
constant = substrate.get_constant('LBP', 'repay_fee')
```
---------
## Errors

---------
### CannotAddZeroLiquidity
Liquidity being added should not be zero

---------
### CannotCreatePoolWithSameAssets
Pool assets can not be the same

---------
### FeeAmountInvalid
Invalid fee amount

---------
### FeeCollectorWithAssetAlreadyUsed
Not more than one fee collector per asset id

---------
### InsufficientAssetBalance
Asset balance too low

---------
### InsufficientLiquidity
Liquidity has not reached the required minimum.

---------
### InsufficientTradingAmount
Amount is less than minimum trading limit.

---------
### InvalidBlockRange
Invalid block range

---------
### InvalidWeight
Weight set is out of range

---------
### MaxInRatioExceeded
Trade amount is too high

---------
### MaxOutRatioExceeded
Trade amount is too high

---------
### MaxSaleDurationExceeded
Sale duration is too long

---------
### NotOwner
Account is not a pool owner

---------
### NothingToUpdate
Nothing to update

---------
### Overflow
An unexpected integer overflow occurred

---------
### PoolAlreadyExists
Pool has been already created

---------
### PoolNotFound
Pool does not exist

---------
### SaleIsNotRunning
Sale is not running

---------
### SaleNotEnded
Sale is still in progress

---------
### SaleStarted
Sale already started

---------
### TradingLimitReached
Trading limit reached

---------
### WeightCalculationError
Calculation error

---------
### ZeroAmount
Can not perform a trade with zero amount

---------