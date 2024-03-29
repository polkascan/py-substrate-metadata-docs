
# Currencies

---------
## Calls

---------
### transfer
See [`Pallet::transfer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| currency_id | `CurrencyIdOf<T>` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Currencies', 'transfer', {
    'amount': 'u128',
    'currency_id': 'u32',
    'dest': 'AccountId',
}
)
```

---------
### transfer_native_currency
See [`Pallet::transfer_native_currency`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Currencies', 'transfer_native_currency', {
    'amount': 'u128',
    'dest': 'AccountId',
}
)
```

---------
### update_balance
See [`Pallet::update_balance`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| currency_id | `CurrencyIdOf<T>` | 
| amount | `AmountOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Currencies', 'update_balance', {
    'amount': 'i128',
    'currency_id': 'u32',
    'who': 'AccountId',
}
)
```

---------
## Events

---------
### BalanceUpdated
Update balance success.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `CurrencyIdOf<T>` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `AmountOf<T>` | ```i128```

---------
### Deposited
Deposit success.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `CurrencyIdOf<T>` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### Transferred
Currency transfer success.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `CurrencyIdOf<T>` | ```u32```
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### Withdrawn
Withdraw success.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `CurrencyIdOf<T>` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
## Constants

---------
### GetNativeCurrencyId
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Currencies', 'GetNativeCurrencyId')
```
---------
## Errors

---------
### AmountIntoBalanceFailed
Unable to convert the Amount type into Balance.

---------
### BalanceTooLow
Balance is too low.

---------
### DepositFailed
Deposit result is not expected

---------