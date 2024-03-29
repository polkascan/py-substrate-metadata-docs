
# LBP

---------
## Calls

---------
### add_liquidity
See [`Pallet::add_liquidity`].
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
See [`Pallet::buy`].
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
See [`Pallet::create_pool`].
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
See [`Pallet::remove_liquidity`].
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
See [`Pallet::sell`].
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
See [`Pallet::update_pool_data`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId<T>` | 
| pool_owner | `Option<T::AccountId>` | 
| start | `Option<BlockNumberFor<T>>` | 
| end | `Option<BlockNumberFor<T>>` | 
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
| data | `Pool<T::AccountId, BlockNumberFor<T>>` | ```{'owner': 'AccountId', 'start': (None, 'u32'), 'end': (None, 'u32'), 'assets': ('u32', 'u32'), 'initial_weight': 'u32', 'final_weight': 'u32', 'weight_curve': ('Linear',), 'fee': ('u32', 'u32'), 'fee_collector': 'AccountId', 'repay_target': 'u128'}```

---------
### PoolUpdated
Pool data were updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool | `PoolId<T>` | ```AccountId```
| data | `Pool<T::AccountId, BlockNumberFor<T>>` | ```{'owner': 'AccountId', 'start': (None, 'u32'), 'end': (None, 'u32'), 'assets': ('u32', 'u32'), 'initial_weight': 'u32', 'final_weight': 'u32', 'weight_curve': ('Linear',), 'fee': ('u32', 'u32'), 'fee_collector': 'AccountId', 'repay_target': 'u128'}```

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