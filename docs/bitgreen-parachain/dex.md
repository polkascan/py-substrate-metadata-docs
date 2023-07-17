
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
### force_set_min_validations
Set the minimum validators required to validator a payment
#### Attributes
| Name | Type |
| -------- | -------- | 
| min_validators | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Dex', 'force_set_min_validations', {'min_validators': 'u32'}
)
```

---------
### force_set_open_order_allowed_limits
#### Attributes
| Name | Type |
| -------- | -------- | 
| level | `UserLevel` | 
| limit | `AssetBalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Dex', 'force_set_open_order_allowed_limits', {
    'level': (
        'KYCLevel1',
        'KYCLevel2',
        'Whitelist',
    ),
    'limit': 'u128',
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
### force_set_seller_payout_authority
Set the seller payout authority by force.

This function allows the seller payout authority to be set forcefully by a privileged
origin.

- `origin`: The origin of the transaction.
- `authority`: The account ID of the authority to be set as the seller payout authority.


\# Errors

This function may return an error if:

- The transaction origin is not authorized to force the operation.

\# Note

This function is intended to be called by ForceOrigin, typically through a governance
process. It sets the `authority` as the seller payout authority by storing it in the
`SellerPayoutAuthority` storage item.

Emits an `Event::SellerPayoutAuthoritySet` event on success.
#### Attributes
| Name | Type |
| -------- | -------- | 
| authority | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Dex', 'force_set_seller_payout_authority', {'authority': 'AccountId'}
)
```

---------
### record_payment_to_seller
Record a payment executed to a seller.

This function records a payment executed to a seller and performs necessary validations
and updates.

- `origin`: The origin of the transaction.
- `seller`: The account ID of the seller who received the payment.
- `payout`: A `PayoutExecutedToSeller` value representing the details of the payment.


\# Errors

This function may return an error if:

- The transaction origin is not signed by the expected authority.
- The seller payout authority has not been set.
- The `seller` has no receivables.
- The receivable amount is less than the payment amount.
- The list of seller payouts is full and cannot accommodate the new payment.

\# Note

This function performs the following steps:

- Verifies that the `origin` is signed by the expected authority, which is retrieved
  from the `SellerPayoutAuthority` storage item.
- Subtracts the payment amount from the seller&\#x27;s receivables stored in the
  `SellerReceivables` storage map.
- Adds the new payment to the list of seller payouts stored in the `SellerPayouts`
  storage map.

Emits an `Event::SellerPayoutExecuted` event on success.
#### Attributes
| Name | Type |
| -------- | -------- | 
| seller | `T::AccountId` | 
| payout | `PayoutExecutedToSellerOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Dex', 'record_payment_to_seller', {
    'payout': {
        'amount': 'u128',
        'chain_id': 'u32',
        'order_id': ['u128'],
        'recipient_address': 'Bytes',
        'tx_hash': 'Bytes',
    },
    'seller': 'AccountId',
}
)
```

---------
### set_seller_payout_preference
Set the payout preference for a seller.

This function allows a seller to set their preferred payout preference.

- `origin`: The origin of the transaction.
- `preference`: An optional `SellerPayoutPreference` value representing the desired
  payout preference.


\# Errors

This function may return an error if:

- The transaction origin is not signed.

\# Note

If a `preference` value is provided, it will be associated with the `seller` and stored
in the `SellerPayoutPreferences` storage map. If `preference` is `None`, the payout
preference for the `seller` will be removed from the storage.

Emits an `Event::SellerPayoutPreferenceSet` event on success.
#### Attributes
| Name | Type |
| -------- | -------- | 
| preference | `Option<SellerPayoutPreferenceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Dex', 'set_seller_payout_preference', {
    'preference': (
        None,
        {
            'chain_id': 'u32',
            'recipient_address': 'Bytes',
        },
    ),
}
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
### BuyOrderCreated
A buy order was processed successfully
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `OrderId` | ```u128```
| sell_order_id | `OrderId` | ```u128```
| units | `AssetBalanceOf<T>` | ```u128```
| project_id | `ProjectIdOf<T>` | ```u32```
| group_id | `GroupIdOf<T>` | ```u32```
| price_per_unit | `CurrencyBalanceOf<T>` | ```u128```
| fees_paid | `CurrencyBalanceOf<T>` | ```u128```
| total_amount | `CurrencyBalanceOf<T>` | ```u128```
| seller | `T::AccountId` | ```AccountId```
| buyer | `T::AccountId` | ```AccountId```

---------
### BuyOrderExpired
A buy order was expired and removed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `BuyOrderId` | ```u128```
| sell_order_id | `OrderId` | ```u128```
| units | `AssetBalanceOf<T>` | ```u128```
| buyer | `T::AccountId` | ```AccountId```

---------
### BuyOrderFilled
A buy order was completed successfully
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| order_id | `BuyOrderId` | ```u128```
| sell_order_id | `OrderId` | ```u128```
| units | `AssetBalanceOf<T>` | ```u128```
| project_id | `ProjectIdOf<T>` | ```u32```
| group_id | `GroupIdOf<T>` | ```u32```
| price_per_unit | `CurrencyBalanceOf<T>` | ```u128```
| fees_paid | `CurrencyBalanceOf<T>` | ```u128```
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
### SellerPayoutAuthoritySet
Authority to validate seller payout has been set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| authority | `T::AccountId` | ```AccountId```

---------
### SellerPayoutExecuted
A seller was paid
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| seller | `T::AccountId` | ```AccountId```
| payout | `PayoutExecutedToSellerOf<T>` | ```{'order_id': ['u128'], 'chain_id': 'u32', 'recipient_address': 'Bytes', 'amount': 'u128', 'tx_hash': 'Bytes'}```

---------
### SellerPayoutPreferenceSet
A seller has set payout preference
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| seller | `T::AccountId` | ```AccountId```
| preference | `Option<SellerPayoutPreferenceOf<T>>` | ```(None, {'chain_id': 'u32', 'recipient_address': 'Bytes'})```

---------
### UserOpenOrderUnitsLimitUpdated
User open order units limit set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| level | `UserLevel` | ```('KYCLevel1', 'KYCLevel2', 'Whitelist')```
| limit | `AssetBalanceOf<T>` | ```u128```

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
### BuyOrdersByUser
 storage to track the buy orders by user

#### Python
```python
result = substrate.query(
    'Dex', 'BuyOrdersByUser', ['AccountId']
)
```

#### Return value
```python
[('u128', 'u128')]
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
### SellerPayoutAuthority

#### Python
```python
result = substrate.query(
    'Dex', 'SellerPayoutAuthority', []
)
```

#### Return value
```python
'AccountId'
```
---------
### SellerPayoutPreferences

#### Python
```python
result = substrate.query(
    'Dex', 'SellerPayoutPreferences', ['AccountId']
)
```

#### Return value
```python
{'chain_id': 'u32', 'recipient_address': 'Bytes'}
```
---------
### SellerPayouts

#### Python
```python
result = substrate.query(
    'Dex', 'SellerPayouts', ['AccountId']
)
```

#### Return value
```python
[
    {
        'amount': 'u128',
        'chain_id': 'u32',
        'order_id': ['u128'],
        'recipient_address': 'Bytes',
        'tx_hash': 'Bytes',
    },
]
```
---------
### SellerReceivables

#### Python
```python
result = substrate.query(
    'Dex', 'SellerReceivables', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### UserOpenOrderUnitsAllowed
 storage to track the limit of units allowed in open orders

#### Python
```python
result = substrate.query(
    'Dex', 'UserOpenOrderUnitsAllowed', [
    (
        'KYCLevel1',
        'KYCLevel2',
        'Whitelist',
    ),
]
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
Different chainId provided when validating transaction

---------
### DuplicateValidation
Already validated

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
User not kyc authorized to perform action

---------
### NoReceivables
No receivable found for seller

---------
### NotAuthorised
not authorized to perform action

---------
### NotSellerPayoutAuthority
Not seller payment authority

---------
### OpenOrderLimitExceeded
User has too many open orders

---------
### OrderIdOverflow
Error when calculating orderId

---------
### OrderUnitsOverflow
Error when calculating order units

---------
### PaymentsListFull
Payments list is full

---------
### ReceivableLessThanPayment
receivable amount is less than payment

---------
### SellerAndBuyerCannotBeSame
Seller and buyer cannot be same

---------
### SellerPayoutAuthorityNotSet
Seller payout authority has not been set

---------
### TooManyValidatorAccounts
Exceeded the maximum allowed validator count

---------
### TxProofMismatch
TXProof provided by the validator is different from previous validation

---------
### UserOpenOrderUnitsAllowedExceeded
User has too many units as unpaid open orders

---------
### UserOpenOrderUnitsLimtNotFound
Limits for open orders not configured correctly

---------
### ValidatorAccountAlreadyExists
Duplicate validator account

---------