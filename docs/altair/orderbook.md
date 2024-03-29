
# OrderBook

---------
## Calls

---------
### cancel_order
 Cancel an existing order that had been created by calling account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `T::OrderIdNonce` | 

#### Python
```python
call = substrate.compose_call(
    'OrderBook', 'cancel_order', {'order_id': 'u64'}
)
```

---------
### fill_order
Fill an existing order with the given amount.
The `amount_out` is the amount the originator of this call is
willing to buy for
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `T::OrderIdNonce` | 
| amount_out | `T::BalanceOut` | 

#### Python
```python
call = substrate.compose_call(
    'OrderBook', 'fill_order', {
    'amount_out': 'u128',
    'order_id': 'u64',
}
)
```

---------
### place_order
Create an order with the default min fulfillment amount.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_in | `T::CurrencyId` | 
| currency_out | `T::CurrencyId` | 
| amount_out | `T::BalanceOut` | 
| ratio | `OrderRatio<T::Ratio>` | 

#### Python
```python
call = substrate.compose_call(
    'OrderBook', 'place_order', {
    'amount_out': 'u128',
    'currency_in': {
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'LocalAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
    },
    'currency_out': {
        'Native': None,
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'LocalAsset': 'u32',
        'Staking': ('BlockRewards', ),
    },
    'ratio': {
        'Custom': 'u128',
        'Market': None,
    },
}
)
```

---------
### set_market_feeder
Set the market feeder for set market ratios.
The origin must be the admin origin.
#### Attributes
| Name | Type |
| -------- | -------- | 
| feeder_id | `T::FeederId` | 

#### Python
```python
call = substrate.compose_call(
    'OrderBook', 'set_market_feeder', {
    'feeder_id': {
        'system': {
            'None': None,
            'Root': None,
            'Signed': 'AccountId',
        },
        None: None,
        'Council': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'CumulusXcm': {
            'Relay': None,
            'SiblingParachain': 'u32',
        },
        'Ethereum': {
            'EthereumTransaction': '[u8; 20]',
        },
        'LiquidityPoolsGateway': {
            'AxelarRelay': {
                'Centrifuge': '[u8; 32]',
                'EVM': (
                    'u64',
                    '[u8; 20]',
                ),
            },
            'Domain': {
                'Centrifuge': '[u8; 32]',
                'EVM': (
                    'u64',
                    '[u8; 20]',
                ),
            },
        },
        'PolkadotXcm': {
            'Response': {
                'interior': {
                    'Here': None,
                    'X1': {
                        'AccountId32': 'InnerStruct',
                        'AccountIndex64': 'InnerStruct',
                        'AccountKey20': 'InnerStruct',
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'InnerStruct',
                        'GlobalConsensus': 'scale_info::153',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': 'InnerStruct',
                    },
                    'X2': (
                        'scale_info::150',
                        'scale_info::150',
                    ),
                    'X3': (
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                    ),
                    'X4': (
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                    ),
                    'X5': (
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                    ),
                    'X6': (
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                    ),
                    'X7': (
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                    ),
                    'X8': (
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                    ),
                },
                'parents': 'u8',
            },
            'Xcm': {
                'interior': {
                    'Here': None,
                    'X1': {
                        'AccountId32': 'InnerStruct',
                        'AccountIndex64': 'InnerStruct',
                        'AccountKey20': 'InnerStruct',
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'InnerStruct',
                        'GlobalConsensus': 'scale_info::153',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': 'InnerStruct',
                    },
                    'X2': (
                        'scale_info::150',
                        'scale_info::150',
                    ),
                    'X3': (
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                    ),
                    'X4': (
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                    ),
                    'X5': (
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                    ),
                    'X6': (
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                    ),
                    'X7': (
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                    ),
                    'X8': (
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                        'scale_info::150',
                    ),
                },
                'parents': 'u8',
            },
        },
        'Void': (),
    },
}
)
```

---------
### update_order
Update an existing order
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `T::OrderIdNonce` | 
| amount_out | `T::BalanceOut` | 
| ratio | `OrderRatio<T::Ratio>` | 

#### Python
```python
call = substrate.compose_call(
    'OrderBook', 'update_order', {
    'amount_out': 'u128',
    'order_id': 'u64',
    'ratio': {
        'Custom': 'u128',
        'Market': None,
    },
}
)
```

---------
## Events

---------
### FeederChanged
Event emitted when a valid trading pair is removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| feeder_id | `T::FeederId` | ```{'system': {'Root': None, 'Signed': 'AccountId', 'None': None}, None: None, 'Void': (), 'Council': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'LiquidityPoolsGateway': {'Domain': {'Centrifuge': '[u8; 32]', 'EVM': ('u64', '[u8; 20]')}, 'AxelarRelay': {'Centrifuge': '[u8; 32]', 'EVM': ('u64', '[u8; 20]')}}, 'PolkadotXcm': {'Xcm': {'parents': 'u8', 'interior': {'Here': None, 'X1': 'scale_info::150', 'X2': ('scale_info::150', 'scale_info::150'), 'X3': ('scale_info::150', 'scale_info::150', 'scale_info::150'), 'X4': ('scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150'), 'X5': ('scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150'), 'X6': ('scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150'), 'X7': ('scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150'), 'X8': ('scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150')}}, 'Response': {'parents': 'u8', 'interior': {'Here': None, 'X1': 'scale_info::150', 'X2': ('scale_info::150', 'scale_info::150'), 'X3': ('scale_info::150', 'scale_info::150', 'scale_info::150'), 'X4': ('scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150'), 'X5': ('scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150'), 'X6': ('scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150'), 'X7': ('scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150'), 'X8': ('scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150', 'scale_info::150')}}}, 'CumulusXcm': {'Relay': None, 'SiblingParachain': 'u32'}, 'Ethereum': {'EthereumTransaction': '[u8; 20]'}}```

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
| currency_in | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}```
| currency_out | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}```
| amount_out | `T::BalanceOut` | ```u128```
| min_fulfillment_amount_out | `T::BalanceOut` | ```u128```
| ratio | `OrderRatio<T::Ratio>` | ```{'Market': None, 'Custom': 'u128'}```

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
| fulfillment_amount | `T::BalanceOut` | ```u128```
| currency_in | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}```
| currency_out | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}```
| ratio | `T::Ratio` | ```u128```

---------
### OrderUpdated
Event emitted when an order is updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `T::OrderIdNonce` | ```u64```
| account | `T::AccountId` | ```AccountId```
| amount_out | `T::BalanceOut` | ```u128```
| ratio | `OrderRatio<T::Ratio>` | ```{'Market': None, 'Custom': 'u128'}```
| min_fulfillment_amount_out | `T::BalanceOut` | ```u128```

---------
## Storage functions

---------
### MarketFeederId
 Stores the market feeder id used to set with market conversion ratios

#### Python
```python
result = substrate.query(
    'OrderBook', 'MarketFeederId', []
)
```

#### Return value
```python
{
    'system': {'None': None, 'Root': None, 'Signed': 'AccountId'},
    None: None,
    'Council': {'Member': 'AccountId', 'Members': ('u32', 'u32'), '_Phantom': None},
    'CumulusXcm': {'Relay': None, 'SiblingParachain': 'u32'},
    'Ethereum': {'EthereumTransaction': '[u8; 20]'},
    'LiquidityPoolsGateway': {
        'AxelarRelay': {'Centrifuge': '[u8; 32]', 'EVM': ('u64', '[u8; 20]')},
        'Domain': {'Centrifuge': '[u8; 32]', 'EVM': ('u64', '[u8; 20]')},
    },
    'PolkadotXcm': {
        'Response': {
            'interior': {
                'Here': None,
                'X1': 'scale_info::150',
                'X2': ('scale_info::150', 'scale_info::150'),
                'X3': (
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                ),
                'X4': (
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                ),
                'X5': (
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                ),
                'X6': (
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                ),
                'X7': (
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                ),
                'X8': (
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                ),
            },
            'parents': 'u8',
        },
        'Xcm': {
            'interior': {
                'Here': None,
                'X1': 'scale_info::150',
                'X2': ('scale_info::150', 'scale_info::150'),
                'X3': (
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                ),
                'X4': (
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                ),
                'X5': (
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                ),
                'X6': (
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                ),
                'X7': (
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                ),
                'X8': (
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                    'scale_info::150',
                ),
            },
            'parents': 'u8',
        },
    },
    'Void': (),
}
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
    'amount_in': 'u128',
    'amount_out': 'u128',
    'amount_out_initial': 'u128',
    'currency_in': {
        'Native': None,
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'LocalAsset': 'u32',
        'Staking': ('BlockRewards', ),
    },
    'currency_out': {
        'Native': None,
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'LocalAsset': 'u32',
        'Staking': ('BlockRewards', ),
    },
    'order_id': 'u64',
    'placing_account': 'AccountId',
    'ratio': {'Custom': 'u128', 'Market': None},
}
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
()
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
1000000
```
#### Python
```python
constant = substrate.get_constant('OrderBook', 'OrderPairVecSize')
```
---------
## Errors

---------
### BelowMinFulfillmentAmount
Error when an account cannot reserve or transfer the amount.

---------
### FulfillAmountTooLarge
Error when the provided amount to fulfill is too large for the
order.

---------
### InvalidCurrencyId
Error when an order is placed with a currency that is not in the
`AssetRegistry`.

---------
### MarketFeederNotFound
There is not feeder set for market conversion ratios

---------
### MarketRatioNotFound
Expected a market ratio for the given pair of currencies.

---------
### OrderNotFound
Error when an operation is attempted on an order id that is not in
storage.

---------
### SameCurrencyIds
Error when order is placed attempting to exchange currencies of the
same type.

---------
### Unauthorised
Error when a user attempts an action on an order they are not
authorised to perform, such as cancelling another accounts order.

---------