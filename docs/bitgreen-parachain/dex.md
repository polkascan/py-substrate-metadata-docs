
# Dex

---------
## Calls

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
### create_buy_order
Buy `units` of `asset_id` from the given `order_id`
This will be called by one of the approved validators when an order is created
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
    'Dex', 'create_buy_order', {
    'asset_id': 'u32',
    'max_fee': 'u128',
    'order_id': 'u128',
    'units': 'u128',
}
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
### force_add_validator_account
Add a new account to the list of authorised Accounts
The caller must be from a permitted origin
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Dex', 'force_add_validator_account', {'account_id': 'AccountId'}
)
```

---------
### force_remove_validator_account
Remove an account from the list of authorised accounts
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Dex', 'force_remove_validator_account', {'account_id': 'AccountId'}
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
### validate_buy_order
Buy `units` of `asset_id` from the given `order_id`
This will be called by one of the approved validators when an order is created
#### Attributes
| Name | Type |
| -------- | -------- | 
| order_id | `BuyOrderId` | 
| chain_id | `u32` | 
| tx_proof | `BoundedVec<u8, T::MaxTxHashLen>` | 

#### Python
```python
call = substrate.compose_call(
    'Dex', 'validate_buy_order', {
    'chain_id': 'u32',
    'order_id': 'u128',
    'tx_proof': 'Bytes',
}
)
```

---------
## Events

---------
### BuyOrderCompleted
A buy order was completed successfully
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `BuyOrderId` | ```u128```

---------
### BuyOrderCreated
A buy order was processed successfully
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `OrderId` | ```u128```
| units | `AssetBalanceOf<T>` | ```u128```
| project_id | `ProjectIdOf<T>` | ```u32```
| group_id | `GroupIdOf<T>` | ```u32```
| price_per_unit | `CurrencyBalanceOf<T>` | ```u128```
| fees_paid | `CurrencyBalanceOf<T>` | ```u128```
| total_amount | `CurrencyBalanceOf<T>` | ```u128```
| seller | `T::AccountId` | ```AccountId```
| buyer | `T::AccountId` | ```AccountId```

---------
### BuyOrderPaymentValidated
A buy order payment was validated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `BuyOrderId` | ```u128```
| chain_id | `u32` | ```u32```
| validator | `T::AccountId` | ```AccountId```

---------
### SellOrderCancelled
A sell order was cancelled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `OrderId` | ```u128```
| seller | `T::AccountId` | ```AccountId```

---------
### SellOrderCreated
A new sell order has been created
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `OrderId` | ```u128```
| asset_id | `AssetIdOf<T>` | ```u32```
| project_id | `ProjectIdOf<T>` | ```u32```
| group_id | `GroupIdOf<T>` | ```u32```
| units | `AssetBalanceOf<T>` | ```u128```
| price_per_unit | `CurrencyBalanceOf<T>` | ```u128```
| owner | `T::AccountId` | ```AccountId```

---------
### ValidatorAccountAdded
A new ValidatorAccount has been added
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
### ValidatorAccountRemoved
An ValidatorAccount has been removed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### BuyOrderCount

#### Python
```python
result = substrate.query(
    'Dex', 'BuyOrderCount', []
)
```

#### Return value
```python
'u128'
```
---------
### BuyOrders

#### Python
```python
result = substrate.query(
    'Dex', 'BuyOrders', ['u128']
)
```

#### Return value
```python
{
    'asset_id': 'u32',
    'buyer': 'AccountId',
    'expiry_time': 'u32',
    'order_id': 'u128',
    'payment_info': (
        None,
        {'chain_id': 'u32', 'tx_proof': 'Bytes', 'validators': ['AccountId']},
    ),
    'price_per_unit': 'u128',
    'total_amount': 'u128',
    'total_fee': 'u128',
    'units': 'u128',
}
```
---------
### MinPaymentValidations

#### Python
```python
result = substrate.query(
    'Dex', 'MinPaymentValidations', []
)
```

#### Return value
```python
'u32'
```
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
### ValidatorAccounts

#### Python
```python
result = substrate.query(
    'Dex', 'ValidatorAccounts', []
)
```

#### Return value
```python
['AccountId']
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
### ChainIdMismatch

---------
### DuplicateValidation

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
### KYCAuthorisationFailed

---------
### NotAuthorised
not authorized to perform action

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
### TooManyValidatorAccounts

---------
### TxProofMismatch

---------
### ValidatorAccountAlreadyExists

---------