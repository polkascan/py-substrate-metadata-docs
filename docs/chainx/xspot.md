
# XSpot

---------
## Calls

---------
### add_trading_pair
Add a new trading pair.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `CurrencyPair` | 
| pip_decimals | `u32` | 
| tick_decimals | `u32` | 
| latest_price | `T::Price` | 
| tradable | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'XSpot', 'add_trading_pair', {
    'currency_pair': {
        'base': 'u32',
        'quote': 'u32',
    },
    'latest_price': 'u128',
    'pip_decimals': 'u32',
    'tick_decimals': 'u32',
    'tradable': 'bool',
}
)
```

---------
### cancel_order
#### Attributes
| Name | Type |
| -------- | -------- | 
| pair_id | `TradingPairId` | 
| order_id | `OrderId` | 

#### Python
```python
call = substrate.compose_call(
    'XSpot', 'cancel_order', {'order_id': 'u64', 'pair_id': 'u32'}
)
```

---------
### force_cancel_order
Force cancel an order.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| pair_id | `TradingPairId` | 
| order_id | `OrderId` | 

#### Python
```python
call = substrate.compose_call(
    'XSpot', 'force_cancel_order', {
    'order_id': 'u64',
    'pair_id': 'u32',
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### put_order
#### Attributes
| Name | Type |
| -------- | -------- | 
| pair_id | `TradingPairId` | 
| order_type | `OrderType` | 
| side | `Side` | 
| amount | `BalanceOf<T>` | 
| price | `T::Price` | 

#### Python
```python
call = substrate.compose_call(
    'XSpot', 'put_order', {
    'amount': 'u128',
    'order_type': ('Limit', 'Market'),
    'pair_id': 'u32',
    'price': 'u128',
    'side': ('Buy', 'Sell'),
}
)
```

---------
### set_handicap
#### Attributes
| Name | Type |
| -------- | -------- | 
| pair_id | `TradingPairId` | 
| new | `Handicap<T::Price>` | 

#### Python
```python
call = substrate.compose_call(
    'XSpot', 'set_handicap', {
    'new': {
        'highest_bid': 'u128',
        'lowest_ask': 'u128',
    },
    'pair_id': 'u32',
}
)
```

---------
### set_price_fluctuation
#### Attributes
| Name | Type |
| -------- | -------- | 
| pair_id | `TradingPairId` | 
| new | `PriceFluctuation` | 

#### Python
```python
call = substrate.compose_call(
    'XSpot', 'set_price_fluctuation', {'new': 'u32', 'pair_id': 'u32'}
)
```

---------
### update_trading_pair
Update the trading pair profile.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pair_id | `TradingPairId` | 
| tick_decimals | `u32` | 
| tradable | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'XSpot', 'update_trading_pair', {
    'pair_id': 'u32',
    'tick_decimals': 'u32',
    'tradable': 'bool',
}
)
```

---------
## Events

---------
### CanceledOrderUpdated
There is an update to the order due to it gets canceled. [order_info]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Order<TradingPairId, T::AccountId, BalanceOf<T>, T::Price, T::
BlockNumber>` | ```{'props': {'id': 'u64', 'side': ('Buy', 'Sell'), 'price': 'u128', 'amount': 'u128', 'pair_id': 'u32', 'submitter': 'AccountId', 'order_type': ('Limit', 'Market'), 'created_at': 'u32'}, 'status': ('Created', 'PartialFill', 'Filled', 'PartialFillAndCanceled', 'Canceled'), 'remaining': 'u128', 'executed_indices': ['u64'], 'already_filled': 'u128', 'last_update_at': 'u32'}```

---------
### MakerOrderUpdated
There was an update to the order due to it gets executed. [maker_order_info]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Order<TradingPairId, T::AccountId, BalanceOf<T>, T::Price, T::
BlockNumber>` | ```{'props': {'id': 'u64', 'side': ('Buy', 'Sell'), 'price': 'u128', 'amount': 'u128', 'pair_id': 'u32', 'submitter': 'AccountId', 'order_type': ('Limit', 'Market'), 'created_at': 'u32'}, 'status': ('Created', 'PartialFill', 'Filled', 'PartialFillAndCanceled', 'Canceled'), 'remaining': 'u128', 'executed_indices': ['u64'], 'already_filled': 'u128', 'last_update_at': 'u32'}```

---------
### NewOrder
A new order was created. [order_info]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Order<TradingPairId, T::AccountId, BalanceOf<T>, T::Price, T::
BlockNumber>` | ```{'props': {'id': 'u64', 'side': ('Buy', 'Sell'), 'price': 'u128', 'amount': 'u128', 'pair_id': 'u32', 'submitter': 'AccountId', 'order_type': ('Limit', 'Market'), 'created_at': 'u32'}, 'status': ('Created', 'PartialFill', 'Filled', 'PartialFillAndCanceled', 'Canceled'), 'remaining': 'u128', 'executed_indices': ['u64'], 'already_filled': 'u128', 'last_update_at': 'u32'}```

---------
### OrderExecuted
Overall information about the maker and taker orders when there was an order execution. [order_executed_info]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `OrderExecutedInfo<T::AccountId, BalanceOf<T>, T::BlockNumber, T::
Price>` | ```{'trading_history_idx': 'u64', 'pair_id': 'u32', 'price': 'u128', 'maker': 'AccountId', 'taker': 'AccountId', 'maker_order_id': 'u64', 'taker_order_id': 'u64', 'turnover': 'u128', 'executed_at': 'u32'}```

---------
### PriceFluctuationUpdated
Price fluctuation of trading pair has been updated. [pair_id, price_fluctuation]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TradingPairId` | ```u32```
| None | `PriceFluctuation` | ```u32```

---------
### TakerOrderUpdated
There was an update to the order due to it gets executed. [taker_order_info]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Order<TradingPairId, T::AccountId, BalanceOf<T>, T::Price, T::
BlockNumber>` | ```{'props': {'id': 'u64', 'side': ('Buy', 'Sell'), 'price': 'u128', 'amount': 'u128', 'pair_id': 'u32', 'submitter': 'AccountId', 'order_type': ('Limit', 'Market'), 'created_at': 'u32'}, 'status': ('Created', 'PartialFill', 'Filled', 'PartialFillAndCanceled', 'Canceled'), 'remaining': 'u128', 'executed_indices': ['u64'], 'already_filled': 'u128', 'last_update_at': 'u32'}```

---------
### TradingPairAdded
A new trading pair is added. [pair_profile]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TradingPairProfile` | ```{'id': 'u32', 'currency_pair': {'base': 'u32', 'quote': 'u32'}, 'pip_decimals': 'u32', 'tick_decimals': 'u32', 'tradable': 'bool'}```

---------
### TradingPairUpdated
Trading pair profile has been updated. [pair_profile]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TradingPairProfile` | ```{'id': 'u32', 'currency_pair': {'base': 'u32', 'quote': 'u32'}, 'pip_decimals': 'u32', 'tick_decimals': 'u32', 'tradable': 'bool'}```

---------
## Storage functions

---------
### HandicapOf
 TradingPairId =&gt; (highest_bid, lowest_ask)

#### Python
```python
result = substrate.query(
    'XSpot', 'HandicapOf', ['u32']
)
```

#### Return value
```python
{'highest_bid': 'u128', 'lowest_ask': 'u128'}
```
---------
### NativeReserves
 Record the exact balance of reserved native coins in Spot.

#### Python
```python
result = substrate.query(
    'XSpot', 'NativeReserves', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### OrderCountOf
 Total orders made by an account.

#### Python
```python
result = substrate.query(
    'XSpot', 'OrderCountOf', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### OrderInfoOf
 Details of an user order given the account ID and order ID.

#### Python
```python
result = substrate.query(
    'XSpot', 'OrderInfoOf', ['AccountId', 'u64']
)
```

#### Return value
```python
{
    'already_filled': 'u128',
    'executed_indices': ['u64'],
    'last_update_at': 'u32',
    'props': {
        'amount': 'u128',
        'created_at': 'u32',
        'id': 'u64',
        'order_type': ('Limit', 'Market'),
        'pair_id': 'u32',
        'price': 'u128',
        'side': ('Buy', 'Sell'),
        'submitter': 'AccountId',
    },
    'remaining': 'u128',
    'status': (
        'Created',
        'PartialFill',
        'Filled',
        'PartialFillAndCanceled',
        'Canceled',
    ),
}
```
---------
### PriceFluctuationOf
 The map of trading pair ID to the price fluctuation. Use with caution!

#### Python
```python
result = substrate.query(
    'XSpot', 'PriceFluctuationOf', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### QuotationsOf
 All the accounts and the order number given the trading pair ID and price.

#### Python
```python
result = substrate.query(
    'XSpot', 'QuotationsOf', ['u32', 'u128']
)
```

#### Return value
```python
[('AccountId', 'u64')]
```
---------
### TradingHistoryIndexOf
 Total transactions has been made for a trading pair.

#### Python
```python
result = substrate.query(
    'XSpot', 'TradingHistoryIndexOf', ['u32']
)
```

#### Return value
```python
'u64'
```
---------
### TradingPairCount
 How many trading pairs so far.

#### Python
```python
result = substrate.query(
    'XSpot', 'TradingPairCount', []
)
```

#### Return value
```python
'u32'
```
---------
### TradingPairInfoOf
 (latest price, last update height) of trading pair

#### Python
```python
result = substrate.query(
    'XSpot', 'TradingPairInfoOf', ['u32']
)
```

#### Return value
```python
{'last_updated': 'u32', 'latest_price': 'u128'}
```
---------
### TradingPairOf
 The map from trading pair id to its static profile.

#### Python
```python
result = substrate.query(
    'XSpot', 'TradingPairOf', ['u32']
)
```

#### Return value
```python
{
    'currency_pair': {'base': 'u32', 'quote': 'u32'},
    'id': 'u32',
    'pip_decimals': 'u32',
    'tick_decimals': 'u32',
    'tradable': 'bool',
}
```
---------
## Errors

---------
### AssetError
Error from assets module.

---------
### CancelOrderNotAllowed
Only the orders with ZeroFill or PartialFill can be canceled.

---------
### InsufficientBalance
Can not put order if transactor&\#x27;s free token too low.

---------
### InvalidOrderId
Can not find the order given the order index.

---------
### InvalidOrderType
Invalid validator target.

---------
### InvalidPrice
Price can not be zero, and must be an integer multiple of the tick decimals.

---------
### InvalidPriceVolatility
Price volatility must be less 100.

---------
### InvalidTickdecimals
tick_decimals can not less than the one of pair.

---------
### InvalidTradingPair
The trading pair doesn&\#x27;t exist.

---------
### InvalidTradingPairAsset
Can not retrieve the asset info given the trading pair.

---------
### NonexistentTradingPair
The trading pair does not exist.

---------
### TooHighBidPrice
The bid price can not higher than the PriceVolatility of current lowest ask.

---------
### TooLowAskPrice
The ask price can not lower than the PriceVolatility of current highest bid.

---------
### TooManyBacklogOrders
Too many orders for the same price.

---------
### TradingPairAlreadyExists
The trading pair already exists.

---------
### TradingPairUntradable
The trading pair is untradable.

---------
### VolumeTooSmall
Failed to convert_base_to_quote since amount*price too small.

---------
### ZeroAmount
Amount can not be zero.

---------