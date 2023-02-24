
# EqDex

---------
## Calls

---------
### create_order
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `Asset` | 
| order_type | `OrderType` | 
| side | `OrderSide` | 
| amount | `EqFixedU128` | 

#### Python
```python
call = substrate.compose_call(
    'EqDex', 'create_order', {
    'amount': 'u128',
    'asset': 'u64',
    'order_type': {
        'Limit': {
            'expiration_time': 'u64',
            'price': 'i64',
        },
        'Market': None,
    },
    'side': ('Buy', 'Sell'),
}
)
```

---------
### delete_order
Delete order.
The dispatch origin for this call must be _None_ (unsigned transaction).
#### Attributes
| Name | Type |
| -------- | -------- | 
| request | `OperationRequestDexDeleteOrder<T::BlockNumber, T::AccountId, T::
Balance>` | 
| signature | `<T::AuthorityId as RuntimeAppPublic>::Signature` | 

#### Python
```python
call = substrate.compose_call(
    'EqDex', 'delete_order', {
    'request': {
        'asset': 'u64',
        'authority_index': 'u32',
        'block_num': 'u32',
        'buyout': (None, 'u128'),
        'order_id': 'u64',
        'price': 'i64',
        'reason': (
            'OutOfCorridor',
            'Cancel',
            'MarginCall',
            'DisableTradingPair',
            'Match',
            'MakerError',
        ),
        'validators_len': 'u32',
        'who': 'AccountId',
    },
    'signature': '[u8; 64]',
}
)
```

---------
### delete_order_external
Delete order. This must be called by order owner or root.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `Asset` | 
| order_id | `OrderId` | 
| price | `FixedI64` | 

#### Python
```python
call = substrate.compose_call(
    'EqDex', 'delete_order_external', {
    'asset': 'u64',
    'order_id': 'u64',
    'price': 'i64',
}
)
```

---------
### update_asset_corridor
Update stored asset corridor value
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `Asset` | 
| new_corridor_value | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'EqDex', 'update_asset_corridor', {
    'asset': 'u64',
    'new_corridor_value': 'u32',
}
)
```

---------
## Events

---------
### Match
Orders matched
`[asset, taker_rest, maker_price, maker_order_id, maker, taker, maker_fee, taker_fee, exchange_amount, maker_side]`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Asset` | ```u64```
| None | `EqFixedU128` | ```u128```
| None | `FixedI64` | ```i64```
| None | `OrderId` | ```u64```
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```
| None | `EqFixedU128` | ```u128```
| None | `OrderSide` | ```('Buy', 'Sell')```

---------
### OrderCreated
Order was created
`[subaccount_id, order_id, asset, amount, price, side, created_at, expiration_time]`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `u64` | ```u64```
| None | `Asset` | ```u64```
| None | `EqFixedU128` | ```u128```
| None | `FixedI64` | ```i64```
| None | `OrderSide` | ```('Buy', 'Sell')```
| None | `u64` | ```u64```
| None | `u64` | ```u64```

---------
### OrderDeleted
Order was deleted
`[account_id, order_id, asset, reason]`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `u64` | ```u64```
| None | `Asset` | ```u64```
| None | `DeleteOrderReason` | ```('OutOfCorridor', 'Cancel', 'MarginCall', 'DisableTradingPair', 'Match', 'MakerError')```

---------
## Storage functions

---------
### ActualChunksByAsset

#### Python
```python
result = substrate.query(
    'EqDex', 'ActualChunksByAsset', ['u64']
)
```

#### Return value
```python
['u64']
```
---------
### AssetWeightByAccountId
 Keep by every asset VecMap&lt;Asset, OrderAggregateBySide&gt;

#### Python
```python
result = substrate.query(
    'EqDex', 'AssetWeightByAccountId', ['AccountId']
)
```

#### Return value
```python
[
    (
        'u64',
        {
            'buy': {'amount': 'u128', 'amount_by_price': 'u128'},
            'sell': {'amount': 'u128', 'amount_by_price': 'u128'},
        },
    ),
]
```
---------
### BestPriceByAsset

#### Python
```python
result = substrate.query(
    'EqDex', 'BestPriceByAsset', ['u64']
)
```

#### Return value
```python
{'ask': (None, 'i64'), 'bid': (None, 'i64')}
```
---------
### ChunkCorridorByAsset

#### Python
```python
result = substrate.query(
    'EqDex', 'ChunkCorridorByAsset', ['u64']
)
```

#### Return value
```python
'u32'
```
---------
### OrderIdCounter

#### Python
```python
result = substrate.query(
    'EqDex', 'OrderIdCounter', []
)
```

#### Return value
```python
'u64'
```
---------
### OrdersByAssetAndChunkKey

#### Python
```python
result = substrate.query(
    'EqDex', 'OrdersByAssetAndChunkKey', ['u64', 'u64']
)
```

#### Return value
```python
[
    {
        'account_id': 'AccountId',
        'amount': 'u128',
        'created_at': 'u64',
        'expiration_time': 'u64',
        'order_id': 'u64',
        'price': 'i64',
        'side': ('Buy', 'Sell'),
    },
]
```
---------
## Constants

---------
### DexUnsignedPriority
 Used for calculation unsigned transaction priority
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('EqDex', 'DexUnsignedPriority')
```
---------
### PenaltyFee
 Fee for deleting orders by offchain worker
#### Value
```python
10000000000
```
#### Python
```python
constant = substrate.get_constant('EqDex', 'PenaltyFee')
```
---------
### PriceStepCount
 Used for group orders in chunks. Should be positive value
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('EqDex', 'PriceStepCount')
```
---------
## Errors

---------
### AccountIsNotTrader
Only trader subaccounts may create DEX orders.

---------
### BadMargin
Insufficient margin to place an order

---------
### DexIsDisabledForAsset
Asset trading is disabled

---------
### InconsistentStorage
Inconsistent storage state

---------
### NoBestPriceForMarketOrder
There is no best price for market order

---------
### OnlyOwnerCanRemoveOrder
Only order originator may cancel an order

---------
### OrderAmountShouldBePositive
Order quantity should be a positive value

---------
### OrderAmountShouldSatisfyLot
Order amount should satisfy instrument lot size

---------
### OrderNotFound
No order found by order id and/or price

---------
### OrderPriceShouldBeInCorridor
Order price should be in a corridor

---------
### OrderPriceShouldBePositive
Order price should be a positive value

---------
### OrderPriceShouldSatisfyPriceStep
Order price should satisfy instrument price step

---------
### PriceStepShouldBePositive
Price step should be a positive value

---------