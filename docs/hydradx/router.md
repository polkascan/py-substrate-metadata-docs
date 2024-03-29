
# Router

---------
## Calls

---------
### buy
See [`Pallet::buy`].
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
### force_insert_route
See [`Pallet::force_insert_route`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_pair | `AssetPair<T::AssetId>` | 
| new_route | `Vec<Trade<T::AssetId>>` | 

#### Python
```python
call = substrate.compose_call(
    'Router', 'force_insert_route', {
    'asset_pair': {
        'asset_in': 'u32',
        'asset_out': 'u32',
    },
    'new_route': [
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
See [`Pallet::sell`].
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
### set_route
See [`Pallet::set_route`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_pair | `AssetPair<T::AssetId>` | 
| new_route | `Vec<Trade<T::AssetId>>` | 

#### Python
```python
call = substrate.compose_call(
    'Router', 'set_route', {
    'asset_pair': {
        'asset_in': 'u32',
        'asset_out': 'u32',
    },
    'new_route': [
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
### Executed
The route with trades has been successfully executed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_in | `T::AssetId` | ```u32```
| asset_out | `T::AssetId` | ```u32```
| amount_in | `T::Balance` | ```u128```
| amount_out | `T::Balance` | ```u128```

---------
### RouteUpdated
The route with trades has been successfully executed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_ids | `Vec<T::AssetId>` | ```['u32']```

---------
## Storage functions

---------
### Routes
 Storing routes for asset pairs

#### Python
```python
result = substrate.query(
    'Router', 'Routes', [
    {
        'asset_in': 'u32',
        'asset_out': 'u32',
    },
]
)
```

#### Return value
```python
[
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
]
```
---------
## Constants

---------
### NativeAssetId
 Native Asset Id
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Router', 'NativeAssetId')
```
---------
## Errors

---------
### InsufficientAssetNotSupported
Insufficient asset is not supported for on chain routing

---------
### InsufficientBalance
The user has not enough balance to execute the trade

---------
### InvalidRoute
The route is invalid

---------
### InvalidRouteExecution
The route execution failed in the underlying AMM

---------
### MaxTradesExceeded
The the max number of trades limit is reached

---------
### NotAllowed
Trading same assets is not allowed.

---------
### PoolNotSupported
The AMM pool is not supported for executing trades

---------
### RouteCalculationFailed
The calculation of route trade amounts failed in the underlying AMM

---------
### RouteUpdateIsNotSuccessful
The route update was not successful

---------
### TradingLimitReached
The trading limit has been reached

---------