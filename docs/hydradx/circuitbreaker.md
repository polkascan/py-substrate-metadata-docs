
# CircuitBreaker

---------
## Calls

---------
### set_add_liquidity_limit
See [`Pallet::set_add_liquidity_limit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| liquidity_limit | `Option<(u32, u32)>` | 

#### Python
```python
call = substrate.compose_call(
    'CircuitBreaker', 'set_add_liquidity_limit', {
    'asset_id': 'u32',
    'liquidity_limit': (
        None,
        ('u32', 'u32'),
    ),
}
)
```

---------
### set_remove_liquidity_limit
See [`Pallet::set_remove_liquidity_limit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| liquidity_limit | `Option<(u32, u32)>` | 

#### Python
```python
call = substrate.compose_call(
    'CircuitBreaker', 'set_remove_liquidity_limit', {
    'asset_id': 'u32',
    'liquidity_limit': (
        None,
        ('u32', 'u32'),
    ),
}
)
```

---------
### set_trade_volume_limit
See [`Pallet::set_trade_volume_limit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| trade_volume_limit | `(u32, u32)` | 

#### Python
```python
call = substrate.compose_call(
    'CircuitBreaker', 'set_trade_volume_limit', {
    'asset_id': 'u32',
    'trade_volume_limit': (
        'u32',
        'u32',
    ),
}
)
```

---------
## Events

---------
### AddLiquidityLimitChanged
Add liquidity limit of an asset was changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| liquidity_limit | `Option<(u32, u32)>` | ```(None, ('u32', 'u32'))```

---------
### RemoveLiquidityLimitChanged
Remove liquidity limit of an asset was changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| liquidity_limit | `Option<(u32, u32)>` | ```(None, ('u32', 'u32'))```

---------
### TradeVolumeLimitChanged
Trade volume limit of an asset was changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| trade_volume_limit | `(u32, u32)` | ```('u32', 'u32')```

---------
## Storage functions

---------
### AllowedAddLiquidityAmountPerAsset
 Add liquidity volumes per asset

#### Python
```python
result = substrate.query(
    'CircuitBreaker', 'AllowedAddLiquidityAmountPerAsset', ['u32']
)
```

#### Return value
```python
{'limit': 'u128', 'liquidity': 'u128'}
```
---------
### AllowedRemoveLiquidityAmountPerAsset
 Remove liquidity volumes per asset

#### Python
```python
result = substrate.query(
    'CircuitBreaker', 'AllowedRemoveLiquidityAmountPerAsset', ['u32']
)
```

#### Return value
```python
{'limit': 'u128', 'liquidity': 'u128'}
```
---------
### AllowedTradeVolumeLimitPerAsset
 Trade volumes per asset

#### Python
```python
result = substrate.query(
    'CircuitBreaker', 'AllowedTradeVolumeLimitPerAsset', ['u32']
)
```

#### Return value
```python
{'limit': 'u128', 'volume_in': 'u128', 'volume_out': 'u128'}
```
---------
### LiquidityAddLimitPerAsset
 Liquidity limits of assets for adding liquidity.
 If not set, returns the default limit.

#### Python
```python
result = substrate.query(
    'CircuitBreaker', 'LiquidityAddLimitPerAsset', ['u32']
)
```

#### Return value
```python
(None, ('u32', 'u32'))
```
---------
### LiquidityRemoveLimitPerAsset
 Liquidity limits of assets for removing liquidity.
 If not set, returns the default limit.

#### Python
```python
result = substrate.query(
    'CircuitBreaker', 'LiquidityRemoveLimitPerAsset', ['u32']
)
```

#### Return value
```python
(None, ('u32', 'u32'))
```
---------
### TradeVolumeLimitPerAsset
 Trade volume limits of assets set by set_trade_volume_limit.
 If not set, returns the default limit.

#### Python
```python
result = substrate.query(
    'CircuitBreaker', 'TradeVolumeLimitPerAsset', ['u32']
)
```

#### Return value
```python
('u32', 'u32')
```
---------
## Constants

---------
### DefaultMaxAddLiquidityLimitPerBlock
 The maximum percentage of a pool&#x27;s liquidity that can be added in a block.
 Represented as an optional non-zero fraction (nominator, denominator) with the max value being 10_000.
 If set to None, the limits are not enforced.
#### Value
```python
(500, 10000)
```
#### Python
```python
constant = substrate.get_constant('CircuitBreaker', 'DefaultMaxAddLiquidityLimitPerBlock')
```
---------
### DefaultMaxNetTradeVolumeLimitPerBlock
 The maximum percentage of a pool&#x27;s liquidity that can be traded in a block.
 Represented as a non-zero fraction (nominator, denominator) with the max value being 10_000.
#### Value
```python
(5000, 10000)
```
#### Python
```python
constant = substrate.get_constant('CircuitBreaker', 'DefaultMaxNetTradeVolumeLimitPerBlock')
```
---------
### DefaultMaxRemoveLiquidityLimitPerBlock
 The maximum percentage of a pool&#x27;s liquidity that can be removed in a block.
 Represented as an optional non-zero fraction (nominator, denominator) with the max value being 10_000.
 If set to None, the limits are not enforced.
#### Value
```python
(500, 10000)
```
#### Python
```python
constant = substrate.get_constant('CircuitBreaker', 'DefaultMaxRemoveLiquidityLimitPerBlock')
```
---------
## Errors

---------
### InvalidLimitValue
Invalid value for a limit. Limit must be non-zero.

---------
### LiquidityLimitNotStoredForAsset
Allowed liquidity limit is not stored for asset

---------
### MaxLiquidityLimitPerBlockReached
Maximum pool&\#x27;s liquidity limit per block has been reached

---------
### NotAllowed
Asset is not allowed to have a limit

---------
### TokenInfluxLimitReached
Token trade influx per block has been reached

---------
### TokenOutflowLimitReached
Token trade outflow per block has been reached

---------