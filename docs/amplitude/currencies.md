
# Currencies

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
    'Currencies', 'transfer', {
    'amount': 'u128',
    'currency_id': {
        'Native': None,
        'XCM': (
            'KSM',
            'KAR',
            'AUSD',
            'BNC',
            'VsKSM',
            'HKO',
            'MOVR',
            'SDN',
            'KINT',
            'KBTC',
            'GENS',
            'XOR',
            'TEER',
            'KILT',
            'PHA',
            'ZTG',
            'USD',
        ),
    },
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
    'Currencies', 'transfer_native_currency', {
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
    'Currencies', 'update_balance', {
    'amount': 'i128',
    'currency_id': {
        'Native': None,
        'XCM': (
            'KSM',
            'KAR',
            'AUSD',
            'BNC',
            'VsKSM',
            'HKO',
            'MOVR',
            'SDN',
            'KINT',
            'KBTC',
            'GENS',
            'XOR',
            'TEER',
            'KILT',
            'PHA',
            'ZTG',
            'USD',
        ),
    },
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
'Native'
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