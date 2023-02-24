
# Currencies

---------
## Calls

---------
### transfer
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
        'DEXShare': ('u64', 'u64'),
        'FungibleToken': 'u64',
        'MiningResource': 'u64',
        'NativeToken': 'u64',
        'Stable': 'u64',
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
        'DEXShare': ('u64', 'u64'),
        'FungibleToken': 'u64',
        'MiningResource': 'u64',
        'NativeToken': 'u64',
        'Stable': 'u64',
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
## Events

---------
### BalanceUpdated
Update balance success. [currency_id, who, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyIdOf<T>` | ```{'NativeToken': 'u64', 'FungibleToken': 'u64', 'DEXShare': ('u64', 'u64'), 'MiningResource': 'u64', 'Stable': 'u64'}```
| None | `T::AccountId` | ```AccountId```
| None | `AmountOf<T>` | ```i128```

---------
### Deposited
Deposit success. [currency_id, who, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyIdOf<T>` | ```{'NativeToken': 'u64', 'FungibleToken': 'u64', 'DEXShare': ('u64', 'u64'), 'MiningResource': 'u64', 'Stable': 'u64'}```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### Transferred
Currency transfer success. [currency_id, from, to, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyIdOf<T>` | ```{'NativeToken': 'u64', 'FungibleToken': 'u64', 'DEXShare': ('u64', 'u64'), 'MiningResource': 'u64', 'Stable': 'u64'}```
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### Withdrawn
Withdraw success. [currency_id, who, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyIdOf<T>` | ```{'NativeToken': 'u64', 'FungibleToken': 'u64', 'DEXShare': ('u64', 'u64'), 'MiningResource': 'u64', 'Stable': 'u64'}```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
## Constants

---------
### GetNativeCurrencyId
 The native currency id
#### Value
```python
{'NativeToken': 0}
```
#### Python
```python
constant = substrate.get_constant('Currencies', 'GetNativeCurrencyId')
```
---------
## Errors

---------
### AmountIntoBalanceFailed
Conversion failed

---------
### AmountZero
Transfer amount should be non-zero

---------
### BalanceLow
Account balance must be greater than or equal to the transfer amount

---------
### BalanceTooLow
Account balance must be greater than or equal to the transfer amount

---------
### BalanceZero
Balance should be non-zero

---------
### FungibleTokenAlreadyIssued
Metaverse Currency already issued for this metaverse

---------
### InsufficientBalance
Insufficient balance

---------
### MetaverseFundIsNotAvailable
Metaverse is not available

---------
### NoAvailableTokenId
No available next token id

---------
### NoPermissionTokenIssuance
No permission to issue token

---------