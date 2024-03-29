
# Orderbook

---------
## Calls

---------
### fill_order
Fill an existing order entirely (`maker_partial_fill` = None)
or partially (`maker_partial_fill` = Some(partial_amount)).

External fees are paid in the base asset.

NOTE: The `maker_partial_fill` is the partial amount
of what the maker wants to get filled.

\# Weight

Complexity: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `OrderId` | 
| maker_partial_fill | `Option<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Orderbook', 'fill_order', {
    'maker_partial_fill': (
        None,
        'u128',
    ),
    'order_id': 'u128',
}
)
```

---------
### place_order
Place a new order.

\# Weight

Complexity: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| market_id | `MarketIdOf<T>` | 
| maker_asset | `AssetOf<T>` | 
| maker_amount | `BalanceOf<T>` | 
| taker_asset | `AssetOf<T>` | 
| taker_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Orderbook', 'place_order', {
    'maker_amount': 'u128',
    'maker_asset': {
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
    'taker_amount': 'u128',
    'taker_asset': {
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
### remove_order
Removes an order.

\# Weight

Complexity: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `OrderId` | 

#### Python
```python
call = substrate.compose_call(
    'Orderbook', 'remove_order', {'order_id': 'u128'}
)
```

---------
## Events

---------
### OrderFilled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `OrderId` | ```u128```
| maker | `AccountIdOf<T>` | ```AccountId```
| taker | `AccountIdOf<T>` | ```AccountId```
| filled_maker_amount | `BalanceOf<T>` | ```u128```
| filled_taker_amount | `BalanceOf<T>` | ```u128```
| unfilled_maker_amount | `BalanceOf<T>` | ```u128```
| unfilled_taker_amount | `BalanceOf<T>` | ```u128```

---------
### OrderPlaced
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `OrderId` | ```u128```
| order | `OrderOf<T>` | ```{'market_id': 'u128', 'maker': 'AccountId', 'maker_asset': {'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32', 'ParimutuelShare': ('u128', 'u16')}, 'maker_amount': 'u128', 'taker_asset': {'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32', 'ParimutuelShare': ('u128', 'u16')}, 'taker_amount': 'u128'}```

---------
### OrderRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `OrderId` | ```u128```
| maker | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### NextOrderId

#### Python
```python
result = substrate.query(
    'Orderbook', 'NextOrderId', []
)
```

#### Return value
```python
'u128'
```
---------
### Orders

#### Python
```python
result = substrate.query(
    'Orderbook', 'Orders', ['u128']
)
```

#### Return value
```python
{
    'maker': 'AccountId',
    'maker_amount': 'u128',
    'maker_asset': {
        'CategoricalOutcome': ('u128', 'u16'),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'ParimutuelShare': ('u128', 'u16'),
        'PoolShare': 'u128',
        'ScalarOutcome': ('u128', ('Long', 'Short')),
        'Ztg': None,
    },
    'market_id': 'u128',
    'taker_amount': 'u128',
    'taker_asset': {
        'CategoricalOutcome': ('u128', 'u16'),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'ParimutuelShare': ('u128', 'u16'),
        'PoolShare': 'u128',
        'ScalarOutcome': ('u128', ('Long', 'Short')),
        'Ztg': None,
    },
}
```
---------
## Constants

---------
### PalletId
#### Value
```python
'0x7a67652f6f726462'
```
#### Python
```python
constant = substrate.get_constant('Orderbook', 'PalletId')
```
---------
## Errors

---------
### AmountTooHighForOrder
The specified amount parameter is too high for the order.

---------
### BelowMinimumBalance
The specified amount is below the minimum balance.

---------
### InvalidOutcomeAsset
The specified outcome asset is not part of the market.

---------
### InvalidScoringRule
The scoring rule is not order book.

---------
### MarketBaseAssetNotPresent
The market base asset is not present.

---------
### MarketIsNotActive
The market is not active.

---------
### NotOrderCreator
The sender is not the order creator.

---------
### OrderDoesNotExist
The order does not exist.

---------
### PartialFillNearFullFillNotAllowed
The maker partial fill leads to a too low quotient for the next order execution.

---------