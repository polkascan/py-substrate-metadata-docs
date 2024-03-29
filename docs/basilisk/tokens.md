
# Tokens

---------
## Calls

---------
### force_transfer
See [`Pallet::force_transfer`].
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
    'currency_id': 'u32',
    'dest': 'AccountId',
    'source': 'AccountId',
}
)
```

---------
### set_balance
See [`Pallet::set_balance`].
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
    'currency_id': 'u32',
    'new_free': 'u128',
    'new_reserved': 'u128',
    'who': 'AccountId',
}
)
```

---------
### transfer
See [`Pallet::transfer`].
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
    'currency_id': 'u32',
    'dest': 'AccountId',
}
)
```

---------
### transfer_all
See [`Pallet::transfer_all`].
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
    'currency_id': 'u32',
    'dest': 'AccountId',
    'keep_alive': 'bool',
}
)
```

---------
### transfer_keep_alive
See [`Pallet::transfer_keep_alive`].
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
    'currency_id': 'u32',
    'dest': 'AccountId',
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
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| free | `T::Balance` | ```u128```
| reserved | `T::Balance` | ```u128```

---------
### Deposited
Deposited some balance into an account
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### DustLost
An account was removed whose balance was non-zero but below
ExistentialDeposit, resulting in an outright loss.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Endowed
An account was created with some free balance.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Issued
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| amount | `T::Balance` | ```u128```

---------
### LockRemoved
Some locked funds were unlocked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| lock_id | `LockIdentifier` | ```[u8; 8]```
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```

---------
### LockSet
Some funds are locked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| lock_id | `LockIdentifier` | ```[u8; 8]```
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Locked
Some free balance was locked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Rescinded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| amount | `T::Balance` | ```u128```

---------
### ReserveRepatriated
Some reserved balance was repatriated (moved from reserved to
another account).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```
| status | `BalanceStatus` | ```('Free', 'Reserved')```

---------
### Reserved
Some balance was reserved (moved from free to reserved).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Slashed
Some balances were slashed (e.g. due to mis-behavior)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| free_amount | `T::Balance` | ```u128```
| reserved_amount | `T::Balance` | ```u128```

---------
### TotalIssuanceSet
The total issuance of an currency has been set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| amount | `T::Balance` | ```u128```

---------
### Transfer
Transfer succeeded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Unlocked
Some locked balance was freed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Unreserved
Some balance was unreserved (moved from reserved to free).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Withdrawn
Some balances were withdrawn (e.g. pay for transaction fee)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
## Storage functions

---------
### Accounts
 The balance of a token type under an account.

 NOTE: If the total is ever zero, decrease account ref account.

 NOTE: This is only used in the case that this module is used to store
 balances.

#### Python
```python
result = substrate.query(
    'Tokens', 'Accounts', ['AccountId', 'u32']
)
```

#### Return value
```python
{'free': 'u128', 'frozen': 'u128', 'reserved': 'u128'}
```
---------
### Locks
 Any liquidity locks of a token type under an account.
 NOTE: Should only be accessed when setting, changing and freeing a lock.

#### Python
```python
result = substrate.query(
    'Tokens', 'Locks', ['AccountId', 'u32']
)
```

#### Return value
```python
[{'amount': 'u128', 'id': '[u8; 8]'}]
```
---------
### Reserves
 Named reserves on some account balances.

#### Python
```python
result = substrate.query(
    'Tokens', 'Reserves', ['AccountId', 'u32']
)
```

#### Return value
```python
[{'amount': 'u128', 'id': ()}]
```
---------
### TotalIssuance
 The total issuance of a token type.

#### Python
```python
result = substrate.query(
    'Tokens', 'TotalIssuance', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### MaxLocks
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('Tokens', 'MaxLocks')
```
---------
### MaxReserves
 The maximum number of named reserves that can exist on an account.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('Tokens', 'MaxReserves')
```
---------
## Errors

---------
### AmountIntoBalanceFailed
Cannot convert Amount into Balance type

---------
### BalanceTooLow
The balance is too low

---------
### DeadAccount
Beneficiary account must pre-exist

---------
### ExistentialDeposit
Value too low to create account due to existential deposit

---------
### KeepAlive
Transfer/payment would kill account

---------
### LiquidityRestrictions
Failed because liquidity restrictions due to locking

---------
### MaxLocksExceeded
Failed because the maximum locks was exceeded

---------
### TooManyReserves

---------