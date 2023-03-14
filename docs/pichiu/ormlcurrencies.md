
# OrmlCurrencies

---------
## Calls

---------
### transfer
Transfer some balance to another account under `currency_id`.

The dispatch origin for this call must be `Signed` by the
transactor.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| currency_id | `CurrencyIdOf<T>` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'OrmlCurrencies', 'transfer', {
    'amount': 'u128',
    'currency_id': (
        'KSM',
        'PCHU',
        'KAR',
        'LKSM',
        'AUSD',
        'MOVR',
        'BNC',
        'KTON',
        'RING',
    ),
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### transfer_native_currency
Transfer some native currency to another account.

The dispatch origin for this call must be `Signed` by the
transactor.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'OrmlCurrencies', 'transfer_native_currency', {
    'amount': 'u128',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### update_balance
update amount of account `who` under `currency_id`.

The dispatch origin of this call must be _Root_.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| currency_id | `CurrencyIdOf<T>` | 
| amount | `AmountOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'OrmlCurrencies', 'update_balance', {
    'amount': 'i128',
    'currency_id': (
        'KSM',
        'PCHU',
        'KAR',
        'LKSM',
        'AUSD',
        'MOVR',
        'BNC',
        'KTON',
        'RING',
    ),
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
## Constants

---------
### GetNativeCurrencyId
#### Value
```python
'PCHU'
```
#### Python
```python
constant = substrate.get_constant('OrmlCurrencies', 'GetNativeCurrencyId')
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