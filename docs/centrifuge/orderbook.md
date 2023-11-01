
# OrderBook

---------
## Calls

---------
### add_trading_pair
Adds a valid trading pair.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_in | `T::AssetCurrencyId` | 
| asset_out | `T::AssetCurrencyId` | 
| min_order | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'OrderBook', 'add_trading_pair', {
    'asset_in': {
        'Native': None,
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
    },
    'asset_out': {
        'Native': None,
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Staking': ('BlockRewards', ),
    },
    'min_order': 'u128',
}
)
```

---------
### create_order
Create an order with the default min fulfillment amount.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_in | `T::AssetCurrencyId` | 
| asset_out | `T::AssetCurrencyId` | 
| buy_amount | `T::Balance` | 
| price | `T::SellRatio` | 

#### Python
```python
call = substrate.compose_call(
    'OrderBook', 'create_order', {
    'asset_in': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
    },
    'asset_out': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
        'Staking': ('BlockRewards', ),
    },
    'buy_amount': 'u128',
    'price': 'u128',
}
)
```

---------
### fill_order_full
Fill an existing order, fulfilling the entire order.
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `T::OrderIdNonce` | 

#### Python
```python
call = substrate.compose_call(
    'OrderBook', 'fill_order_full', {'order_id': 'u64'}
)
```

---------
### fill_order_partial
Fill an existing order, based on the provided partial buy amount.
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `T::OrderIdNonce` | 
| buy_amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'OrderBook', 'fill_order_partial', {
    'buy_amount': 'u128',
    'order_id': 'u64',
}
)
```

---------
### rm_trading_pair
Removes a valid trading pair
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_in | `T::AssetCurrencyId` | 
| asset_out | `T::AssetCurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'OrderBook', 'rm_trading_pair', {
    'asset_in': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
        'Staking': ('BlockRewards', ),
    },
    'asset_out': {
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
    },
}
)
```

---------
### update_min_order
Sets the minimum order amount for a given trading pair.
If the trading pair is not yet added this errors out.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_in | `T::AssetCurrencyId` | 
| asset_out | `T::AssetCurrencyId` | 
| min_order | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'OrderBook', 'update_min_order', {
    'asset_in': {
        'Native': None,
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Staking': ('BlockRewards', ),
    },
    'asset_out': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
    },
    'min_order': 'u128',
}
)
```

---------
### user_cancel_order
 Cancel an existing order that had been created by calling account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `T::OrderIdNonce` | 

#### Python
```python
call = substrate.compose_call(
    'OrderBook', 'user_cancel_order', {'order_id': 'u64'}
)
```

---------
### user_update_order
Update an existing order
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `T::OrderIdNonce` | 
| buy_amount | `T::Balance` | 
| price | `T::SellRatio` | 

#### Python
```python
call = substrate.compose_call(
    'OrderBook', 'user_update_order', {
    'buy_amount': 'u128',
    'order_id': 'u64',
    'price': 'u128',
}
)
```

---------
## Events

---------
### MinOrderUpdated
Event emitted when a minimum order amount for a trading pair is
updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_in | `T::AssetCurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| asset_out | `T::AssetCurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| min_order | `T::Balance` | ```u128```

---------
### OrderCancelled
Event emitted when an order is cancelled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| order_id | `T::OrderIdNonce` | ```u64```

---------
### OrderCreated
Event emitted when an order is created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `T::OrderIdNonce` | ```u64```
| creator_account | `T::AccountId` | ```AccountId```
| currency_in | `T::AssetCurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| currency_out | `T::AssetCurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| buy_amount | `T::Balance` | ```u128```
| min_fulfillment_amount | `T::Balance` | ```u128```
| sell_rate_limit | `T::SellRatio` | ```u128```

---------
### OrderFulfillment
Event emitted when an order is fulfilled.
Can be for either partial or total fulfillment.
Contains amount fulfilled, and whether fulfillment was partial or
full.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `T::OrderIdNonce` | ```u64```
| placing_account | `T::AccountId` | ```AccountId```
| fulfilling_account | `T::AccountId` | ```AccountId```
| partial_fulfillment | `bool` | ```bool```
| fulfillment_amount | `T::Balance` | ```u128```
| currency_in | `T::AssetCurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| currency_out | `T::AssetCurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| sell_rate_limit | `T::SellRatio` | ```u128```

---------
### OrderUpdated
Event emitted when an order is updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `T::OrderIdNonce` | ```u64```
| account | `T::AccountId` | ```AccountId```
| buy_amount | `T::Balance` | ```u128```
| sell_rate_limit | `T::SellRatio` | ```u128```
| min_fulfillment_amount | `T::Balance` | ```u128```

---------
### TradingPairAdded
Event emitted when a valid trading pair is added.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_in | `T::AssetCurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| asset_out | `T::AssetCurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| min_order | `T::Balance` | ```u128```

---------
### TradingPairRemoved
Event emitted when a valid trading pair is removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_in | `T::AssetCurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| asset_out | `T::AssetCurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```

---------
## Storage functions

---------
### AssetPairOrders
 Map of Vec containing OrderIds of same asset in/out pairs.
 Allows looking up orders available corresponding pairs.

 NOTE: The key order is (currency_in, currency_out).

#### Python
```python
result = substrate.query(
    'OrderBook', 'AssetPairOrders', [
    {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
    },
    {
        'Native': None,
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
    },
]
)
```

#### Return value
```python
['u64']
```
---------
### OrderIdNonceStore
 Stores OrderIdNonce for orders placed
 Given that OrderIdNonce is to ensure that all orders have a unique ID,
 we can use just one OrderIdNonce, which means that we only have one val
 in storage, and we don&#x27;t have to insert new map values upon a new
 account/currency order creation.

#### Python
```python
result = substrate.query(
    'OrderBook', 'OrderIdNonceStore', []
)
```

#### Return value
```python
'u64'
```
---------
### Orders
 Map of Orders to look up orders by their order id.

#### Python
```python
result = substrate.query(
    'OrderBook', 'Orders', ['u64']
)
```

#### Return value
```python
{
    'asset_in_id': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
        'Staking': ('BlockRewards', ),
    },
    'asset_out_id': {
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
    },
    'buy_amount': 'u128',
    'initial_buy_amount': 'u128',
    'max_sell_amount': 'u128',
    'max_sell_rate': 'u128',
    'min_fulfillment_amount': 'u128',
    'order_id': 'u64',
    'placing_account': 'AccountId',
}
```
---------
### TradingPair
 Storage of valid order pairs.
 Stores:
  - key1 -&gt; AssetIn
  - key2 -&gt; AssetOut

 Stores the minimum `buy_amount` of `asset_in` when buying
 with `asset_out`

#### Python
```python
result = substrate.query(
    'OrderBook', 'TradingPair', [
    {
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
    },
    {
        'Native': None,
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Staking': ('BlockRewards', ),
    },
]
)
```

#### Return value
```python
'u128'
```
---------
### UserOrders
 Map of orders for a particular user
 Used to query orders for a particular user using the
 account id of the user as prefix

#### Python
```python
result = substrate.query(
    'OrderBook', 'UserOrders', ['AccountId', 'u64']
)
```

#### Return value
```python
{
    'asset_in_id': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
    },
    'asset_out_id': {
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
    },
    'buy_amount': 'u128',
    'initial_buy_amount': 'u128',
    'max_sell_amount': 'u128',
    'max_sell_rate': 'u128',
    'min_fulfillment_amount': 'u128',
    'order_id': 'u64',
    'placing_account': 'AccountId',
}
```
---------
## Constants

---------
### MinFulfillmentAmountNative
 The default minimum fulfillment amount for orders.

 NOTE: The amount is expected to be denominated in native currency.
 When applying to a swap order, it will be re-denominated into the
 target currency.
#### Value
```python
10000000000000000000
```
#### Python
```python
constant = substrate.get_constant('OrderBook', 'MinFulfillmentAmountNative')
```
---------
### OrderPairVecSize
 Size of order id bounded vec in storage
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('OrderBook', 'OrderPairVecSize')
```
---------
## Errors

---------
### AssetPairOrdersOverflow
Error when the number of orders for a trading pair has exceeded the
BoundedVec size for the order pair for the currency pair in
question.

---------
### BalanceConversionErr
Error when unable to convert fee balance to asset balance when asset
out matches fee currency

---------
### BuyAmountTooLarge
Error when the provided partial buy amount is too large.

---------
### ConflictingAssetIds
Error when order is placed attempting to exchange assets of the same
type.

---------
### InsufficientAssetFunds
Error when an account specifies an invalid buy price -- currently
specified for trade, or amount to be fulfilled.

---------
### InsufficientOrderSize
Error when an order amount is too small

---------
### InvalidAssetId
Error when an order is placed with a currency that is not in the
asset registry.

---------
### InvalidBuyAmount
Error when an account cannot reserve or transfer the amount
currently `0`.

---------
### InvalidMaxPrice
Error when Max price ratio is invalid

---------
### InvalidMinimumFulfillment
Error when min order amount is invalid, currently `0`

---------
### InvalidTradingPair
Error when a trade is using an invalid trading pair.
Currently can happen when there is not a minimum order size
defined for the trading pair.

---------
### OrderNotFound
Error when an operation is attempted on an order id that is not in
storage.

---------
### Unauthorised
Error when a user attempts an action on an order they are not
authorised to perform, such as cancelling another accounts order.

---------