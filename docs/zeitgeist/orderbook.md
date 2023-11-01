
# Orderbook

---------
## Calls

---------
### fill_order
Fill an existing order entirely (`maker_partial_fill` = None)
or partially (`maker_partial_fill` = Some(partial_amount)).

NOTE: The `maker_partial_fill` is the partial amount of what the maker wants to fill.

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
| outcome_asset | `Asset<MarketIdOf<T>>` | 
| side | `OrderSide` | 
| outcome_asset_amount | `BalanceOf<T>` | 
| base_asset_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Orderbook', 'place_order', {
    'base_asset_amount': 'u128',
    'market_id': 'u128',
    'outcome_asset': {
        'CategoricalOutcome': (
            'u128',
            'u16',
        ),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'PoolShare': 'u128',
        'ScalarOutcome': (
            'u128',
            ('Long', 'Short'),
        ),
        'Ztg': None,
    },
    'outcome_asset_amount': 'u128',
    'side': ('Bid', 'Ask'),
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
| filled | `BalanceOf<T>` | ```u128```
| unfilled_outcome_asset_amount | `BalanceOf<T>` | ```u128```
| unfilled_base_asset_amount | `BalanceOf<T>` | ```u128```

---------
### OrderPlaced
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `OrderId` | ```u128```
| order | `OrderOf<T>` | ```{'market_id': 'u128', 'side': ('Bid', 'Ask'), 'maker': 'AccountId', 'outcome_asset': {'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32'}, 'base_asset': {'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32'}, 'outcome_asset_amount': 'u128', 'base_asset_amount': 'u128'}```

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
    'base_asset': {
        'CategoricalOutcome': ('u128', 'u16'),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'PoolShare': 'u128',
        'ScalarOutcome': ('u128', ('Long', 'Short')),
        'Ztg': None,
    },
    'base_asset_amount': 'u128',
    'maker': 'AccountId',
    'market_id': 'u128',
    'outcome_asset': {
        'CategoricalOutcome': ('u128', 'u16'),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'PoolShare': 'u128',
        'ScalarOutcome': ('u128', ('Long', 'Short')),
        'Ztg': None,
    },
    'outcome_asset_amount': 'u128',
    'side': ('Bid', 'Ask'),
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
### AmountIsZero
The specified amount parameter is zero.

---------
### AmountTooHighForOrder
The specified amount parameter is too high for the order.

---------
### InvalidOutcomeAsset
The specified outcome asset is not part of the market.

---------
### InvalidScoringRule
The scoring rule is not orderbook.

---------
### MakerPartialFillTooLow
The maker partial fill leads to a too low quotient for the next order execution.

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