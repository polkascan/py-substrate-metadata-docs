
# Tokens

---------
## Calls

---------
### force_transfer
#### Attributes
| Name | Type |
| -------- | -------- | 
| source | `<T::Lookup as StaticLookup>::Source` | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| currency_id | `T::CurrencyId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Tokens', 'force_transfer', {
    'amount': 'u128',
    'currency_id': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
        'Staking': ('BlockRewards', ),
    },
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'source': {
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
### set_balance
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| currency_id | `T::CurrencyId` | 
| new_free | `T::Balance` | 
| new_reserved | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Tokens', 'set_balance', {
    'currency_id': {
        'Native': None,
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
    },
    'new_free': 'u128',
    'new_reserved': 'u128',
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
### transfer
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| currency_id | `T::CurrencyId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Tokens', 'transfer', {
    'amount': 'u128',
    'currency_id': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
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
### transfer_all
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| currency_id | `T::CurrencyId` | 
| keep_alive | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Tokens', 'transfer_all', {
    'currency_id': {
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
    },
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'keep_alive': 'bool',
}
)
```

---------
### transfer_keep_alive
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| currency_id | `T::CurrencyId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Tokens', 'transfer_keep_alive', {
    'amount': 'u128',
    'currency_id': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        None: None,
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
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
## Events

---------
### BalanceSet
A balance was set by root.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| who | `T::AccountId` | ```AccountId```
| free | `T::Balance` | ```u128```
| reserved | `T::Balance` | ```u128```

---------
### Transfer
Transfer succeeded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
## Errors

---------
### PreConditionsNotMet

---------