
# VSBondAuction

---------
## Calls

---------
### clinch_order
See [`Pallet::clinch_order`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `OrderId` | 

#### Python
```python
call = substrate.compose_call(
    'VSBondAuction', 'clinch_order', {'order_id': 'u64'}
)
```

---------
### create_order
See [`Pallet::create_order`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 
| token_symbol | `TokenSymbol` | 
| first_slot | `LeasePeriod` | 
| last_slot | `LeasePeriod` | 
| amount | `BalanceOf<T, I>` | 
| total_price | `BalanceOf<T, I>` | 
| order_type | `OrderType` | 

#### Python
```python
call = substrate.compose_call(
    'VSBondAuction', 'create_order', {
    'amount': 'u128',
    'first_slot': 'u32',
    'index': 'u32',
    'last_slot': 'u32',
    'order_type': ('Sell', 'Buy'),
    'token_symbol': (
        'ASG',
        'BNC',
        'KUSD',
        'DOT',
        'KSM',
        'ETH',
        'KAR',
        'ZLK',
        'PHA',
        'RMRK',
        'MOVR',
    ),
    'total_price': 'u128',
}
)
```

---------
### force_revoke
See [`Pallet::force_revoke`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `OrderId` | 

#### Python
```python
call = substrate.compose_call(
    'VSBondAuction', 'force_revoke', {'order_id': 'u64'}
)
```

---------
### partial_clinch_order
See [`Pallet::partial_clinch_order`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `OrderId` | 
| quantity | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'VSBondAuction', 'partial_clinch_order', {
    'order_id': 'u64',
    'quantity': 'u128',
}
)
```

---------
### revoke_order
See [`Pallet::revoke_order`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `OrderId` | 

#### Python
```python
call = substrate.compose_call(
    'VSBondAuction', 'revoke_order', {'order_id': 'u64'}
)
```

---------
### set_buy_and_sell_transaction_fee_rate
See [`Pallet::set_buy_and_sell_transaction_fee_rate`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| buy_rate | `u32` | 
| sell_rate | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'VSBondAuction', 'set_buy_and_sell_transaction_fee_rate', {
    'buy_rate': 'u32',
    'sell_rate': 'u32',
}
)
```

---------
## Events

---------
### OrderClinchd
The order has been clinched.

[order_id, order_type, order_creator, order_opponent, vsbond_type,
vsbond_amount_clinched, vsbond_amount, vsbond_remain, total_price]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `OrderId` | ```u64```
| None | `OrderType` | ```('Sell', 'Buy')```
| None | `AccountIdOf<T>` | ```AccountId```
| None | `AccountIdOf<T>` | ```AccountId```
| None | `CurrencyId` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32', 'BLP': 'u32', 'Lend': 'u8'}```
| None | `BalanceOf<T, I>` | ```u128```
| None | `BalanceOf<T, I>` | ```u128```
| None | `BalanceOf<T, I>` | ```u128```
| None | `BalanceOf<T, I>` | ```u128```

---------
### OrderCreated
The order has been created.

[order_id, order_type, order_creator, vsbond_type, vsbond_amount, total_price]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `OrderId` | ```u64```
| None | `OrderType` | ```('Sell', 'Buy')```
| None | `AccountIdOf<T>` | ```AccountId```
| None | `CurrencyId` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32', 'BLP': 'u32', 'Lend': 'u8'}```
| None | `BalanceOf<T, I>` | ```u128```
| None | `BalanceOf<T, I>` | ```u128```

---------
### OrderRevoked
The order has been revoked.

[order_id, order_type, order_creator, vsbond_type, vsbond_amount, vsbond_remain,
total_price]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `OrderId` | ```u64```
| None | `OrderType` | ```('Sell', 'Buy')```
| None | `AccountIdOf<T>` | ```AccountId```
| None | `CurrencyId` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32', 'BLP': 'u32', 'Lend': 'u8'}```
| None | `BalanceOf<T, I>` | ```u128```
| None | `BalanceOf<T, I>` | ```u128```
| None | `BalanceOf<T, I>` | ```u128```

---------
### TransactionFeeRateSet
Transaction fee rate has been reset.

[buy_fee_rate, sell_fee_rate]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Permill` | ```u32```
| None | `Permill` | ```u32```

---------
## Storage functions

---------
### NextOrderId

#### Python
```python
result = substrate.query(
    'VSBondAuction', 'NextOrderId', []
)
```

#### Return value
```python
'u64'
```
---------
### TotalOrderInfos

#### Python
```python
result = substrate.query(
    'VSBondAuction', 'TotalOrderInfos', ['u64']
)
```

#### Return value
```python
{
    'amount': 'u128',
    'order_id': 'u64',
    'order_type': ('Sell', 'Buy'),
    'owner': 'AccountId',
    'remain': 'u128',
    'remain_price': 'u128',
    'total_price': 'u128',
    'vsbond': {
        'BLP': 'u32',
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Lend': 'u8',
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': ('u8', 'u32', 'u32', 'u32'),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
}
```
---------
### TransactionFee
 transaction fee rate[sellFee, buyFee]

#### Python
```python
result = substrate.query(
    'VSBondAuction', 'TransactionFee', []
)
```

#### Return value
```python
('u32', 'u32')
```
---------
### UserOrderIds

#### Python
```python
result = substrate.query(
    'VSBondAuction', 'UserOrderIds', ['AccountId', ('Sell', 'Buy')]
)
```

#### Return value
```python
['u64']
```
---------
## Constants

---------
### InvoicingCurrency
 The currency type that buyer to pay
#### Value
```python
{'Token': 'KSM'}
```
#### Python
```python
constant = substrate.get_constant('VSBondAuction', 'InvoicingCurrency')
```
---------
### MaximumOrderInTrade
 The amount of orders in-trade that user can hold
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('VSBondAuction', 'MaximumOrderInTrade')
```
---------
### MinimumAmount
 The sale or buy quantity needs to be greater than `MinimumSupply` to create an order
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('VSBondAuction', 'MinimumAmount')
```
---------
### PalletId
 ModuleID for creating sub account
#### Value
```python
'0x62662f7673626e64'
```
#### Python
```python
constant = substrate.get_constant('VSBondAuction', 'PalletId')
```
---------
### TreasuryAccount
 The account that transaction fees go into
#### Value
```python
'eCSrvbA5gGNYdM3UjBNxcBNBqGxtz3SEEfydKragtL4pJ4F'
```
#### Python
```python
constant = substrate.get_constant('VSBondAuction', 'TreasuryAccount')
```
---------
## Errors

---------
### DontHaveEnoughToPay

---------
### ExceedMaximumOrderInTrade

---------
### ForbidClinchOrderNotInTrade

---------
### ForbidClinchOrderWithinOwnership

---------
### ForbidRevokeOrderNotInTrade

---------
### ForbidRevokeOrderWithoutOwnership

---------
### InvalidRateInput

---------
### InvalidVsbond

---------
### NotEnoughAmount

---------
### NotEnoughBalanceToCreateOrder

---------
### NotFindOrderInfo

---------
### Overflow

---------
### Unexpected

---------