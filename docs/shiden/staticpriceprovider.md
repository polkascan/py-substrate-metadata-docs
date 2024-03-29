
# StaticPriceProvider

---------
## Calls

---------
### force_set_price
See [`Pallet::force_set_price`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| price | `FixedU64` | 

#### Python
```python
call = substrate.compose_call(
    'StaticPriceProvider', 'force_set_price', {'price': 'u64'}
)
```

---------
## Events

---------
### PriceSet
New static native currency price has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| price | `FixedU64` | ```u64```

---------
## Storage functions

---------
### ActivePrice
 Current active native currency price.

#### Python
```python
result = substrate.query(
    'StaticPriceProvider', 'ActivePrice', []
)
```

#### Return value
```python
'u64'
```
---------
## Errors

---------
### ZeroPrice
Zero is invalid value for the price (hopefully).

---------