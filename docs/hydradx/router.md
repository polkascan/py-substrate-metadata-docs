
# Router

---------
## Calls

---------
### buy
Executes a buy with a series of trades specified in the route.
The price for each trade is determined by the corresponding AMM.

- `origin`: The executor of the trade
- `asset_in`: The identifier of the asset to be swapped to buy `asset_out`
- `asset_out`: The identifier of the asset to buy
- `amount_out`: The amount of `asset_out` to buy
- `max_amount_in`: The max amount of `asset_in` to spend on the buy.
- `route`: Series of [`Trade&lt;AssetId&gt;`] to be executed. A [`Trade&lt;AssetId&gt;`] specifies the asset pair (`asset_in`, `asset_out`) and the AMM (`pool`) in which the trade is executed.

Emits `RouteExecuted` when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_in | `T::AssetId` | 
| asset_out | `T::AssetId` | 
| amount_out | `T::Balance` | 
| max_amount_in | `T::Balance` | 
| route | `Vec<Trade<T::AssetId>>` | 

#### Python
```python
call = substrate.compose_call(
    'Router', 'buy', {
    'amount_out': 'u128',
    'asset_in': 'u32',
    'asset_out': 'u32',
    'max_amount_in': 'u128',
    'route': [
        {
            'asset_in': 'u32',
            'asset_out': 'u32',
            'pool': {
                'LBP': None,
                'Omnipool': None,
                'Stableswap': 'u32',
                'XYK': None,
            },
        },
    ],
}
)
```

---------
### sell
Executes a sell with a series of trades specified in the route.
The price for each trade is determined by the corresponding AMM.

- `origin`: The executor of the trade
- `asset_in`: The identifier of the asset to sell
- `asset_out`: The identifier of the asset to receive
- `amount_in`: The amount of `asset_in` to sell
- `min_amount_out`: The minimum amount of `asset_out` to receive.
- `route`: Series of [`Trade&lt;AssetId&gt;`] to be executed. A [`Trade&lt;AssetId&gt;`] specifies the asset pair (`asset_in`, `asset_out`) and the AMM (`pool`) in which the trade is executed.

Emits `RouteExecuted` when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_in | `T::AssetId` | 
| asset_out | `T::AssetId` | 
| amount_in | `T::Balance` | 
| min_amount_out | `T::Balance` | 
| route | `Vec<Trade<T::AssetId>>` | 

#### Python
```python
call = substrate.compose_call(
    'Router', 'sell', {
    'amount_in': 'u128',
    'asset_in': 'u32',
    'asset_out': 'u32',
    'min_amount_out': 'u128',
    'route': [
        {
            'asset_in': 'u32',
            'asset_out': 'u32',
            'pool': {
                'LBP': None,
                'Omnipool': None,
                'Stableswap': 'u32',
                'XYK': None,
            },
        },
    ],
}
)
```

---------
## Events

---------
### RouteExecuted
The route with trades has been successfully executed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_in | `T::AssetId` | ```u32```
| asset_out | `T::AssetId` | ```u32```
| amount_in | `T::Balance` | ```u128```
| amount_out | `T::Balance` | ```u128```

---------
## Constants

---------
### MaxNumberOfTrades
 Max limit for the number of trades within a route
#### Value
```python
3
```
#### Python
```python
constant = substrate.get_constant('Router', 'MaxNumberOfTrades')
```
---------
## Errors

---------
### InsufficientBalance
The user has not enough balance to execute the trade

---------
### InvalidRouteExecution
The route execution failed in the underlying AMM

---------
### MaxTradesExceeded
The the max number of trades limit is reached

---------
### PoolNotSupported
The AMM pool is not supported for executing trades

---------
### RouteCalculationFailed
The calculation of route trade amounts failed in the underlying AMM

---------
### RouteHasNoTrades
Route has not trades to be executed

---------
### TradingLimitReached
The trading limit has been reached

---------