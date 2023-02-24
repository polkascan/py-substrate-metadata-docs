
# AssetManager

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
    'AssetManager', 'transfer', {
    'amount': 'u128',
    'currency_id': {
        'CategoricalOutcome': (
            'u128',
            'u16',
        ),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'PoolShare': 'u128',
        'ScalarOutcome': (
            'u128',
            ('Long', 'Short'),
        ),
        'Ztg': None,
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
    'AssetManager', 'transfer_native_currency', {
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
    'AssetManager', 'update_balance', {
    'amount': 'i128',
    'currency_id': {
        'CategoricalOutcome': (
            'u128',
            'u16',
        ),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'PoolShare': 'u128',
        'ScalarOutcome': (
            'u128',
            ('Long', 'Short'),
        ),
        'Ztg': None,
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
'Ztg'
```
#### Python
```python
constant = substrate.get_constant('AssetManager', 'GetNativeCurrencyId')
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