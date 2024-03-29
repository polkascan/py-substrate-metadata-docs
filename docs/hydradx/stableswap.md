
# Stableswap

---------
## Calls

---------
### add_liquidity
See [`Pallet::add_liquidity`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::AssetId` | 
| assets | `Vec<AssetAmount<T::AssetId>>` | 

#### Python
```python
call = substrate.compose_call(
    'Stableswap', 'add_liquidity', {
    'assets': [
        {
            'amount': 'u128',
            'asset_id': 'u32',
        },
    ],
    'pool_id': 'u32',
}
)
```

---------
### add_liquidity_shares
See [`Pallet::add_liquidity_shares`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::AssetId` | 
| shares | `Balance` | 
| asset_id | `T::AssetId` | 
| max_asset_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Stableswap', 'add_liquidity_shares', {
    'asset_id': 'u32',
    'max_asset_amount': 'u128',
    'pool_id': 'u32',
    'shares': 'u128',
}
)
```

---------
### buy
See [`Pallet::buy`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::AssetId` | 
| asset_out | `T::AssetId` | 
| asset_in | `T::AssetId` | 
| amount_out | `Balance` | 
| max_sell_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Stableswap', 'buy', {
    'amount_out': 'u128',
    'asset_in': 'u32',
    'asset_out': 'u32',
    'max_sell_amount': 'u128',
    'pool_id': 'u32',
}
)
```

---------
### create_pool
See [`Pallet::create_pool`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| share_asset | `T::AssetId` | 
| assets | `Vec<T::AssetId>` | 
| amplification | `u16` | 
| fee | `Permill` | 

#### Python
```python
call = substrate.compose_call(
    'Stableswap', 'create_pool', {
    'amplification': 'u16',
    'assets': ['u32'],
    'fee': 'u32',
    'share_asset': 'u32',
}
)
```

---------
### remove_liquidity_one_asset
See [`Pallet::remove_liquidity_one_asset`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::AssetId` | 
| asset_id | `T::AssetId` | 
| share_amount | `Balance` | 
| min_amount_out | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Stableswap', 'remove_liquidity_one_asset', {
    'asset_id': 'u32',
    'min_amount_out': 'u128',
    'pool_id': 'u32',
    'share_amount': 'u128',
}
)
```

---------
### sell
See [`Pallet::sell`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::AssetId` | 
| asset_in | `T::AssetId` | 
| asset_out | `T::AssetId` | 
| amount_in | `Balance` | 
| min_buy_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Stableswap', 'sell', {
    'amount_in': 'u128',
    'asset_in': 'u32',
    'asset_out': 'u32',
    'min_buy_amount': 'u128',
    'pool_id': 'u32',
}
)
```

---------
### set_asset_tradable_state
See [`Pallet::set_asset_tradable_state`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::AssetId` | 
| asset_id | `T::AssetId` | 
| state | `Tradability` | 

#### Python
```python
call = substrate.compose_call(
    'Stableswap', 'set_asset_tradable_state', {
    'asset_id': 'u32',
    'pool_id': 'u32',
    'state': {'bits': 'u8'},
}
)
```

---------
### update_amplification
See [`Pallet::update_amplification`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::AssetId` | 
| final_amplification | `u16` | 
| start_block | `BlockNumberFor<T>` | 
| end_block | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Stableswap', 'update_amplification', {
    'end_block': 'u32',
    'final_amplification': 'u16',
    'pool_id': 'u32',
    'start_block': 'u32',
}
)
```

---------
### update_pool_fee
See [`Pallet::update_pool_fee`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::AssetId` | 
| fee | `Permill` | 

#### Python
```python
call = substrate.compose_call(
    'Stableswap', 'update_pool_fee', {'fee': 'u32', 'pool_id': 'u32'}
)
```

---------
### withdraw_asset_amount
See [`Pallet::withdraw_asset_amount`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::AssetId` | 
| asset_id | `T::AssetId` | 
| amount | `Balance` | 
| max_share_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Stableswap', 'withdraw_asset_amount', {
    'amount': 'u128',
    'asset_id': 'u32',
    'max_share_amount': 'u128',
    'pool_id': 'u32',
}
)
```

---------
## Events

---------
### AmplificationChanging
AAmplification of a pool has been scheduled to change.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::AssetId` | ```u32```
| current_amplification | `NonZeroU16` | ```u16```
| final_amplification | `NonZeroU16` | ```u16```
| start_block | `BlockNumberFor<T>` | ```u32```
| end_block | `BlockNumberFor<T>` | ```u32```

---------
### BuyExecuted
Buy trade executed. Trade fee paid in asset entering the pool (already included in amount_in).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| pool_id | `T::AssetId` | ```u32```
| asset_in | `T::AssetId` | ```u32```
| asset_out | `T::AssetId` | ```u32```
| amount_in | `Balance` | ```u128```
| amount_out | `Balance` | ```u128```
| fee | `Balance` | ```u128```

---------
### FeeUpdated
Pool fee has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::AssetId` | ```u32```
| fee | `Permill` | ```u32```

---------
### LiquidityAdded
Liquidity of an asset was added to a pool.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::AssetId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| shares | `Balance` | ```u128```
| assets | `Vec<AssetAmount<T::AssetId>>` | ```[{'asset_id': 'u32', 'amount': 'u128'}]```

---------
### LiquidityRemoved
Liquidity removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::AssetId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| shares | `Balance` | ```u128```
| amounts | `Vec<AssetAmount<T::AssetId>>` | ```[{'asset_id': 'u32', 'amount': 'u128'}]```
| fee | `Balance` | ```u128```

---------
### PoolCreated
A pool was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::AssetId` | ```u32```
| assets | `Vec<T::AssetId>` | ```['u32']```
| amplification | `NonZeroU16` | ```u16```
| fee | `Permill` | ```u32```

---------
### SellExecuted
Sell trade executed. Trade fee paid in asset leaving the pool (already subtracted from amount_out).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| pool_id | `T::AssetId` | ```u32```
| asset_in | `T::AssetId` | ```u32```
| asset_out | `T::AssetId` | ```u32```
| amount_in | `Balance` | ```u128```
| amount_out | `Balance` | ```u128```
| fee | `Balance` | ```u128```

---------
### TradableStateUpdated
Asset&\#x27;s tradable state has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::AssetId` | ```u32```
| asset_id | `T::AssetId` | ```u32```
| state | `Tradability` | ```{'bits': 'u8'}```

---------
## Storage functions

---------
### AssetTradability
 Tradability state of pool assets.

#### Python
```python
result = substrate.query(
    'Stableswap', 'AssetTradability', ['u32', 'u32']
)
```

#### Return value
```python
{'bits': 'u8'}
```
---------
### Pools
 Existing pools

#### Python
```python
result = substrate.query(
    'Stableswap', 'Pools', ['u32']
)
```

#### Return value
```python
{
    'assets': ['u32'],
    'fee': 'u32',
    'final_amplification': 'u16',
    'final_block': 'u32',
    'initial_amplification': 'u16',
    'initial_block': 'u32',
}
```
---------
## Constants

---------
### AmplificationRange
 Amplification inclusive range. Pool&#x27;s amp can be selected from the range only.
#### Value
```python
{'end': 10000, 'start': 2}
```
#### Python
```python
constant = substrate.get_constant('Stableswap', 'AmplificationRange')
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
constant = substrate.get_constant('Stableswap', 'MinPoolLiquidity')
```
---------
### MinTradingLimit
 Minimum trading amount
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('Stableswap', 'MinTradingLimit')
```
---------
## Errors

---------
### AssetNotInPool
Asset is not in the pool.

---------
### AssetNotRegistered
One or more assets are not registered in AssetRegistry

---------
### BuyLimitNotReached
Minimum limit has not been reached during trade.

---------
### IncorrectAssets
Creating a pool with same assets or less than 2 assets is not allowed.

---------
### InsufficientBalance
Balance of an asset is not sufficient to perform a trade.

---------
### InsufficientLiquidity
Liquidity has not reached the required minimum.

---------
### InsufficientLiquidityRemaining
Insufficient liquidity left in the pool after withdrawal.

---------
### InsufficientShareBalance
Remaining balance of share asset is below asset&\#x27;s existential deposit.

---------
### InsufficientShares
Balance of a share asset is not sufficient to withdraw liquidity.

---------
### InsufficientTradingAmount
Amount is less than the minimum trading amount configured.

---------
### InvalidAmplification
Amplification is outside configured range.

---------
### InvalidAssetAmount
Invalid asset amount provided. Amount must be greater than zero.

---------
### InvalidInitialLiquidity
Initial liquidity of asset must be &gt; 0.

---------
### MaxAssetsExceeded
Maximum number of assets has been exceeded.

---------
### NotAllowed
Not allowed to perform an operation on given asset.

---------
### PastBlock
Future block number is in the past.

---------
### PoolExists
A pool with given assets already exists.

---------
### PoolNotFound
A pool with given assets does not exist.

---------
### SameAmplification
New amplification is equal to the previous value.

---------
### SellLimitExceeded
Maximum limit has been exceeded during trade.

---------
### ShareAssetInPoolAssets
Share asset is amount assets when creating a pool.

---------
### ShareAssetNotRegistered
Share asset is not registered in Registry.

---------
### SlippageLimit
Slippage protection.

---------
### UnknownDecimals
Failed to retrieve asset decimals.

---------