
# TokenAllowance

---------
## Calls

---------
### add_allowed_currencies
Added allowed currencies that possible to use chain extension

\# Arguments
* `currencies` - list of currency id allowed to use in chain extension
#### Attributes
| Name | Type |
| -------- | -------- | 
| currencies | `Vec<CurrencyOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'TokenAllowance', 'add_allowed_currencies', {
    'currencies': [
        {
            'Native': None,
            'Stellar': {
                'AlphaNum12': {
                    'code': '[u8; 12]',
                    'issuer': '[u8; 32]',
                },
                'AlphaNum4': {
                    'code': '[u8; 4]',
                    'issuer': '[u8; 32]',
                },
                'StellarNative': None,
            },
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
        },
    ],
}
)
```

---------
### approve
Approve an amount for another account to spend on owner&\#x27;s behalf.

\# Arguments
* `id` - the currency_id of the asset to approve
* `delegate` - the spender account to approve the asset for
* `amount` - the amount of the asset to approve
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `CurrencyOf<T>` | 
| delegate | `T::AccountId` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'TokenAllowance', 'approve', {
    'amount': 'u128',
    'delegate': 'AccountId',
    'id': {
        'Native': None,
        'Stellar': {
            'AlphaNum12': {
                'code': '[u8; 12]',
                'issuer': '[u8; 32]',
            },
            'AlphaNum4': {
                'code': '[u8; 4]',
                'issuer': '[u8; 32]',
            },
            'StellarNative': None,
        },
        'Token': 'u64',
        'XCM': 'u8',
        'ZenlinkLPToken': (
            'u8',
            'u8',
            'u8',
            'u8',
        ),
    },
}
)
```

---------
### remove_allowed_currencies
Remove allowed currencies that possible to use chain extension

\# Arguments
* `currencies` - list of currency id allowed to use in chain extension
#### Attributes
| Name | Type |
| -------- | -------- | 
| currencies | `Vec<CurrencyOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'TokenAllowance', 'remove_allowed_currencies', {
    'currencies': [
        {
            'Native': None,
            'Stellar': {
                'AlphaNum12': {
                    'code': '[u8; 12]',
                    'issuer': '[u8; 32]',
                },
                'AlphaNum4': {
                    'code': '[u8; 4]',
                    'issuer': '[u8; 32]',
                },
                'StellarNative': None,
            },
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
        },
    ],
}
)
```

---------
### transfer_from
Execute a pre-approved transfer from another account

\# Arguments
* `id` - the currency_id of the asset to transfer
* `owner` - the owner account of the asset to transfer
* `destination` - the destination account to transfer to
* `amount` - the amount of the asset to transfer
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `CurrencyOf<T>` | 
| owner | `T::AccountId` | 
| destination | `T::AccountId` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'TokenAllowance', 'transfer_from', {
    'amount': 'u128',
    'destination': 'AccountId',
    'id': {
        'Native': None,
        'Stellar': {
            'AlphaNum12': {
                'code': '[u8; 12]',
                'issuer': '[u8; 32]',
            },
            'AlphaNum4': {
                'code': '[u8; 4]',
                'issuer': '[u8; 32]',
            },
            'StellarNative': None,
        },
        'Token': 'u64',
        'XCM': 'u8',
        'ZenlinkLPToken': (
            'u8',
            'u8',
            'u8',
            'u8',
        ),
    },
    'owner': 'AccountId',
}
)
```

---------
## Events

---------
### AllowedCurrenciesAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currencies | `Vec<CurrencyOf<T>>` | ```[{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}]```

---------
### AllowedCurrenciesDeleted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currencies | `Vec<CurrencyOf<T>>` | ```[{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}]```

---------
### TransferApproved
(Additional) funds have been approved for transfer to a destination account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `CurrencyOf<T>` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}```
| source | `T::AccountId` | ```AccountId```
| delegate | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### AllowedCurrencies
 Currencies that can be used in chain extension

#### Python
```python
result = substrate.query(
    'TokenAllowance', 'AllowedCurrencies', [
    {
        'Native': None,
        'Stellar': {
            'AlphaNum12': {
                'code': '[u8; 12]',
                'issuer': '[u8; 32]',
            },
            'AlphaNum4': {
                'code': '[u8; 4]',
                'issuer': '[u8; 32]',
            },
            'StellarNative': None,
        },
        'Token': 'u64',
        'XCM': 'u8',
        'ZenlinkLPToken': (
            'u8',
            'u8',
            'u8',
            'u8',
        ),
    },
]
)
```

#### Return value
```python
()
```
---------
### Approvals
 Approved balance transfers. Balance is the amount approved for transfer.
 First key is the currency ID, second key is the owner and third key is the delegate.

#### Python
```python
result = substrate.query(
    'TokenAllowance', 'Approvals', [
    {
        'Native': None,
        'Stellar': {
            'AlphaNum12': {
                'code': '[u8; 12]',
                'issuer': '[u8; 32]',
            },
            'AlphaNum4': {
                'code': '[u8; 4]',
                'issuer': '[u8; 32]',
            },
            'StellarNative': None,
        },
        'Token': 'u64',
        'XCM': 'u8',
        'ZenlinkLPToken': (
            'u8',
            'u8',
            'u8',
            'u8',
        ),
    },
    'AccountId',
    'AccountId',
]
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### MaxAllowedCurrencies
 The maximum number of allowed currencies.
#### Value
```python
256
```
#### Python
```python
constant = substrate.get_constant('TokenAllowance', 'MaxAllowedCurrencies')
```
---------
## Errors

---------
### CurrencyNotLive

---------
### ExceedsNumberOfAllowedCurrencies

---------
### Unapproved

---------