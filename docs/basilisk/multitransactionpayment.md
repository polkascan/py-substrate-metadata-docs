
# MultiTransactionPayment

---------
## Calls

---------
### add_currency
See [`Pallet::add_currency`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency | `AssetIdOf<T>` | 
| price | `Price` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTransactionPayment', 'add_currency', {'currency': 'u32', 'price': 'u128'}
)
```

---------
### remove_currency
See [`Pallet::remove_currency`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency | `AssetIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTransactionPayment', 'remove_currency', {'currency': 'u32'}
)
```

---------
### set_currency
See [`Pallet::set_currency`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency | `AssetIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTransactionPayment', 'set_currency', {'currency': 'u32'}
)
```

---------
## Events

---------
### CurrencyAdded
New accepted currency added
[currency]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `AssetIdOf<T>` | ```u32```

---------
### CurrencyRemoved
Accepted currency removed
[currency]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `AssetIdOf<T>` | ```u32```

---------
### CurrencySet
CurrencySet
[who, currency]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| asset_id | `AssetIdOf<T>` | ```u32```

---------
### FeeWithdrawn
Transaction fee paid in non-native currency
[Account, Currency, Native fee amount, Non-native fee amount, Destination account]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| asset_id | `AssetIdOf<T>` | ```u32```
| native_fee_amount | `BalanceOf<T>` | ```u128```
| non_native_fee_amount | `BalanceOf<T>` | ```u128```
| destination_account_id | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### AcceptedCurrencies
 Curated list of currencies which fees can be paid mapped to corresponding fallback price

#### Python
```python
result = substrate.query(
    'MultiTransactionPayment', 'AcceptedCurrencies', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### AcceptedCurrencyPrice
 Asset prices from the spot price provider or the fallback price if the price is not available. Updated at the beginning of every block.

#### Python
```python
result = substrate.query(
    'MultiTransactionPayment', 'AcceptedCurrencyPrice', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### AccountCurrencyMap
 Account currency map

#### Python
```python
result = substrate.query(
    'MultiTransactionPayment', 'AccountCurrencyMap', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### NativeAssetId
 Native Asset
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('MultiTransactionPayment', 'NativeAssetId')
```
---------
## Errors

---------
### AlreadyAccepted
Currency is already in the list of accepted currencies.

---------
### CoreAssetNotAllowed
It is not allowed to add Core Asset as accepted currency. Core asset is accepted by design.

---------
### FallbackPriceNotFound
Fallback price was not found.

---------
### Overflow
Math overflow

---------
### UnsupportedCurrency
Selected currency is not supported.

---------
### ZeroBalance
Account balance should be non-zero.

---------
### ZeroPrice
Fallback price cannot be zero.

---------