
# Dex

---------
## Calls

---------
### buy_order
Buy `units` of `asset_id` from the given `order_id`
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `OrderId` | 
| asset_id | `AssetIdOf<T>` | 
| units | `AssetBalanceOf<T>` | 
| max_fee | `CurrencyBalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Dex', 'buy_order', {
    'asset_id': 'u32',
    'max_fee': 'u128',
    'order_id': 'u128',
    'units': 'u128',
}
)
```

---------
### cancel_sell_order
Cancel an existing sell order with `order_id`
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `OrderId` | 

#### Python
```python
call = substrate.compose_call(
    'Dex', 'cancel_sell_order', {'order_id': 'u128'}
)
```

---------
### create_sell_order
Create a new sell order for given `asset_id`
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 
| units | `AssetBalanceOf<T>` | 
| price_per_unit | `CurrencyBalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Dex', 'create_sell_order', {
    'asset_id': 'u32',
    'price_per_unit': 'u128',
    'units': 'u128',
}
)
```

---------
### force_set_payment_fee
Force set PaymentFees value
Can only be called by ForceOrigin
#### Attributes
| Name | Type |
| -------- | -------- | 
| payment_fee | `Percent` | 

#### Python
```python
call = substrate.compose_call(
    'Dex', 'force_set_payment_fee', {'payment_fee': 'u8'}
)
```

---------
### force_set_purchase_fee
Force set PurchaseFee value
Can only be called by ForceOrigin
#### Attributes
| Name | Type |
| -------- | -------- | 
| purchase_fee | `CurrencyBalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Dex', 'force_set_purchase_fee', {'purchase_fee': 'u128'}
)
```

---------
## Events

---------
### BuyOrderFilled
A buy order was processed successfully
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `OrderId` | ```u128```
| units | `AssetBalanceOf<T>` | ```u128```
| price_per_unit | `CurrencyBalanceOf<T>` | ```u128```
| seller | `T::AccountId` | ```AccountId```
| buyer | `T::AccountId` | ```AccountId```

---------
### SellOrderCancelled
A sell order was cancelled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `OrderId` | ```u128```

---------
### SellOrderCreated
A new sell order has been created
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `OrderId` | ```u128```
| asset_id | `AssetIdOf<T>` | ```u32```
| units | `AssetBalanceOf<T>` | ```u128```
| price_per_unit | `CurrencyBalanceOf<T>` | ```u128```
| owner | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### OrderCount

#### Python
```python
result = substrate.query(
    'Dex', 'OrderCount', []
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
    'Dex', 'Orders', ['u128']
)
```

#### Return value
```python
{
    'asset_id': 'u32',
    'owner': 'AccountId',
    'price_per_unit': 'u128',
    'units': 'u128',
}
```
---------
### Owner

#### Python
```python
result = substrate.query(
    'Dex', 'Owner', []
)
```

#### Return value
```python
'AccountId'
```
---------
### PaymentFees

#### Python
```python
result = substrate.query(
    'Dex', 'PaymentFees', []
)
```

#### Return value
```python
'u8'
```
---------
### PurchaseFees

#### Python
```python
result = substrate.query(
    'Dex', 'PurchaseFees', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### MaxPaymentFee
 The maximum payment fee that can be set
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Dex', 'MaxPaymentFee')
```
---------
### MaxPurchaseFee
 The maximum purchase fee that can be set
#### Value
```python
10000000000000
```
#### Python
```python
constant = substrate.get_constant('Dex', 'MaxPurchaseFee')
```
---------
### MinPricePerUnit
 The minimum price per unit of asset to create a sell order
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Dex', 'MinPricePerUnit')
```
---------
### MinUnitsToCreateSellOrder
 The minimum units of asset to create a sell order
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Dex', 'MinUnitsToCreateSellOrder')
```
---------
### PalletId
 The DEX pallet id
#### Value
```python
'0x626974672f646578'
```
#### Python
```python
constant = substrate.get_constant('Dex', 'PalletId')
```
---------
### StableCurrencyId
 The CurrencyId of the stable currency we accept as payment
#### Value
```python
'USDT'
```
#### Python
```python
constant = substrate.get_constant('Dex', 'StableCurrencyId')
```
---------
## Errors

---------
### ArithmeticError
Arithmetic overflow

---------
### AssetNotPermitted
Asset not permitted to be listed

---------
### BelowMinimumPrice
Below minimum price

---------
### BelowMinimumUnits
Below minimum units

---------
### CannotSetMoreThanMaxPaymentFee
Cannot set more than the maximum payment fee

---------
### CannotSetMoreThanMaxPurchaseFee
The purchasea fee amount exceeds the limit

---------
### FeeExceedsUserLimit
The fee amount exceeds the limit set by user

---------
### InsufficientCurrency
The amount does not cover fees + transaction

---------
### InvalidAssetId
The expected asset_id does not match the order

---------
### InvalidOrderId
The orderId does not exist

---------
### InvalidOrderOwner
Only the order owner can perform this call

---------
### OrderIdOverflow
Error when calculating orderId

---------
### OrderUnitsOverflow
Error when calculating order units

---------
### SellerAndBuyerCannotBeSame
Seller and buyer cannot be same

---------