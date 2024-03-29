
# XYK

---------
## Calls

---------
### add_liquidity
See [`Pallet::add_liquidity`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_a | `AssetId` | 
| asset_b | `AssetId` | 
| amount_a | `Balance` | 
| amount_b_max_limit | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'XYK', 'add_liquidity', {
    'amount_a': 'u128',
    'amount_b_max_limit': 'u128',
    'asset_a': 'u32',
    'asset_b': 'u32',
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
| amount | `Balance` | 
| max_limit | `Balance` | 
| discount | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'XYK', 'buy', {
    'amount': 'u128',
    'asset_in': 'u32',
    'asset_out': 'u32',
    'discount': 'bool',
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
| asset_a | `AssetId` | 
| amount_a | `Balance` | 
| asset_b | `AssetId` | 
| amount_b | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'XYK', 'create_pool', {
    'amount_a': 'u128',
    'amount_b': 'u128',
    'asset_a': 'u32',
    'asset_b': 'u32',
}
)
```

---------
### remove_liquidity
See [`Pallet::remove_liquidity`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_a | `AssetId` | 
| asset_b | `AssetId` | 
| liquidity_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'XYK', 'remove_liquidity', {
    'asset_a': 'u32',
    'asset_b': 'u32',
    'liquidity_amount': 'u128',
}
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
| amount | `Balance` | 
| max_limit | `Balance` | 
| discount | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'XYK', 'sell', {
    'amount': 'u128',
    'asset_in': 'u32',
    'asset_out': 'u32',
    'discount': 'bool',
    'max_limit': 'u128',
}
)
```

---------
## Events

---------
### BuyExecuted
Asset purchase executed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| asset_out | `AssetId` | ```u32```
| asset_in | `AssetId` | ```u32```
| amount | `Balance` | ```u128```
| buy_price | `Balance` | ```u128```
| fee_asset | `AssetId` | ```u32```
| fee_amount | `Balance` | ```u128```
| pool | `T::AccountId` | ```AccountId```

---------
### LiquidityAdded
New liquidity was provided to the pool.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| asset_a | `AssetId` | ```u32```
| asset_b | `AssetId` | ```u32```
| amount_a | `Balance` | ```u128```
| amount_b | `Balance` | ```u128```

---------
### LiquidityRemoved
Liquidity was removed from the pool.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| asset_a | `AssetId` | ```u32```
| asset_b | `AssetId` | ```u32```
| shares | `Balance` | ```u128```

---------
### PoolCreated
Pool was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| asset_a | `AssetId` | ```u32```
| asset_b | `AssetId` | ```u32```
| initial_shares_amount | `Balance` | ```u128```
| share_token | `AssetId` | ```u32```
| pool | `T::AccountId` | ```AccountId```

---------
### PoolDestroyed
Pool was destroyed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| asset_a | `AssetId` | ```u32```
| asset_b | `AssetId` | ```u32```
| share_token | `AssetId` | ```u32```
| pool | `T::AccountId` | ```AccountId```

---------
### SellExecuted
Asset sale executed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| asset_in | `AssetId` | ```u32```
| asset_out | `AssetId` | ```u32```
| amount | `Balance` | ```u128```
| sale_price | `Balance` | ```u128```
| fee_asset | `AssetId` | ```u32```
| fee_amount | `Balance` | ```u128```
| pool | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### PoolAssets
 Asset pair in a pool.

#### Python
```python
result = substrate.query(
    'XYK', 'PoolAssets', ['AccountId']
)
```

#### Return value
```python
('u32', 'u32')
```
---------
### ShareToken
 Asset id storage for shared pool tokens

#### Python
```python
result = substrate.query(
    'XYK', 'ShareToken', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### TotalLiquidity
 Total liquidity in a pool.

#### Python
```python
result = substrate.query(
    'XYK', 'TotalLiquidity', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### GetExchangeFee
 Trading fee rate
#### Value
```python
(3, 1000)
```
#### Python
```python
constant = substrate.get_constant('XYK', 'GetExchangeFee')
```
---------
### MaxInRatio
 Max fraction of pool to sell in single transaction
#### Value
```python
3
```
#### Python
```python
constant = substrate.get_constant('XYK', 'MaxInRatio')
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
constant = substrate.get_constant('XYK', 'MaxOutRatio')
```
---------
### MinPoolLiquidity
 Minimum pool liquidity
#### Value
```python
1000000
```
#### Python
```python
constant = substrate.get_constant('XYK', 'MinPoolLiquidity')
```
---------
### MinTradingLimit
 Minimum trading limit
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('XYK', 'MinTradingLimit')
```
---------
### NativeAssetId
 Native Asset Id
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('XYK', 'NativeAssetId')
```
---------
### OracleSource
 Oracle source identifier for this pallet.
#### Value
```python
'0x687964726178796b'
```
#### Python
```python
constant = substrate.get_constant('XYK', 'OracleSource')
```
---------
## Errors

---------
### AddAssetAmountInvalid
Overflow

---------
### AssetAmountExceededLimit
Asset amount has exceeded given limit.

---------
### AssetAmountNotReachedLimit
Asset amount has not reached given limit.

---------
### BuyAssetAmountInvalid
Overflow

---------
### CannotApplyDiscount
Overflow

---------
### CannotCreatePool
Pool cannot be created due to outside factors.

---------
### CannotCreatePoolWithSameAssets
It is not allowed to create a pool between same assets.

---------
### CreatePoolAssetAmountInvalid
Overflow
Not used, kept for backward compatibility

---------
### FeeAmountInvalid
Overflow

---------
### InsufficientAssetBalance
Asset balance is not sufficient.

---------
### InsufficientLiquidity
Liquidity has not reached the required minimum.

---------
### InsufficientNativeCurrencyBalance
Not enough core asset liquidity in the pool.

---------
### InsufficientPoolAssetBalance
Not enough asset liquidity in the pool.

---------
### InsufficientTradingAmount
Amount is less than min trading limit.

---------
### InvalidLiquidityAmount
Overflow

---------
### InvalidMintedLiquidity
Overflow

---------
### MaxInRatioExceeded
Max fraction of pool to sell in single transaction has been exceeded.

---------
### MaxOutRatioExceeded
Max fraction of pool to buy in single transaction has been exceeded.

---------
### Overflow
Overflow

---------
### RemoveAssetAmountInvalid
Overflow

---------
### SellAssetAmountInvalid
Overflow

---------
### TokenPoolAlreadyExists
Liquidity pool for given assets already exists.

---------
### TokenPoolNotFound
Liquidity pool for given assets does not exist.

---------
### ZeroInitialPrice
It is not allowed to create a pool with zero initial price.
Not used, kept for backward compatibility

---------
### ZeroLiquidity
Liquidity is zero.

---------