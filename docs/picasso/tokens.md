
# Tokens

---------
## Calls

---------
### force_transfer
Exactly as `transfer`, except the origin must be root and the source
account may be specified.

The dispatch origin for this call must be _Root_.

- `source`: The sender of the transfer.
- `dest`: The recipient of the transfer.
- `currency_id`: currency type.
- `amount`: free balance amount to tranfer.
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
    'currency_id': 'u128',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'source': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### set_balance
Set the balances of a given account.

This will alter `FreeBalance` and `ReservedBalance` in storage. it
will also decrease the total issuance of the system
(`TotalIssuance`). If the new free or reserved balance is below the
existential deposit, it will reap the `AccountInfo`.

The dispatch origin for this call is `root`.
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
    'currency_id': 'u128',
    'new_free': 'u128',
    'new_reserved': 'u128',
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### transfer
Transfer some liquid free balance to another account.

`transfer` will set the `FreeBalance` of the sender and receiver.
It will decrease the total issuance of the system by the
`TransferFee`. If the sender&\#x27;s account is below the existential
deposit as a result of the transfer, the account will be reaped.

The dispatch origin for this call must be `Signed` by the
transactor.

- `dest`: The recipient of the transfer.
- `currency_id`: currency type.
- `amount`: free balance amount to tranfer.
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
    'currency_id': 'u128',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### transfer_all
Transfer all remaining balance to the given account.

NOTE: This function only attempts to transfer _transferable_
balances. This means that any locked, reserved, or existential
deposits (when `keep_alive` is `true`), will not be transferred by
this function. To ensure that this function results in a killed
account, you might need to prepare the account by removing any
reference counters, storage deposits, etc...

The dispatch origin for this call must be `Signed` by the
transactor.

- `dest`: The recipient of the transfer.
- `currency_id`: currency type.
- `keep_alive`: A boolean to determine if the `transfer_all`
  operation should send all of the funds the account has, causing
  the sender account to be killed (false), or transfer everything
  except at least the existential deposit, which will guarantee to
  keep the sender account alive (true).
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
    'currency_id': 'u128',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'keep_alive': 'bool',
}
)
```

---------
### transfer_keep_alive
Same as the [`transfer`] call, but with a check that the transfer
will not kill the origin account.

99% of the time you want [`transfer`] instead.

The dispatch origin for this call must be `Signed` by the
transactor.

- `dest`: The recipient of the transfer.
- `currency_id`: currency type.
- `amount`: free balance amount to tranfer.
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
    'currency_id': 'u128',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
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
| currency_id | `T::CurrencyId` | ```u128```
| who | `T::AccountId` | ```AccountId```
| free | `T::Balance` | ```u128```
| reserved | `T::Balance` | ```u128```

---------
### Deposited
Deposited some balance into an account
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u128```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### DustLost
An account was removed whose balance was non-zero but below
ExistentialDeposit, resulting in an outright loss.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u128```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Endowed
An account was created with some free balance.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u128```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### LockRemoved
Some locked funds were unlocked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| lock_id | `LockIdentifier` | ```[u8; 8]```
| currency_id | `T::CurrencyId` | ```u128```
| who | `T::AccountId` | ```AccountId```

---------
### LockSet
Some funds are locked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| lock_id | `LockIdentifier` | ```[u8; 8]```
| currency_id | `T::CurrencyId` | ```u128```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### ReserveRepatriated
Some reserved balance was repatriated (moved from reserved to
another account).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u128```
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
| currency_id | `T::CurrencyId` | ```u128```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Slashed
Some balances were slashed (e.g. due to mis-behavior)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u128```
| who | `T::AccountId` | ```AccountId```
| free_amount | `T::Balance` | ```u128```
| reserved_amount | `T::Balance` | ```u128```

---------
### TotalIssuanceSet
The total issuance of an currency has been set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u128```
| amount | `T::Balance` | ```u128```

---------
### Transfer
Transfer succeeded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u128```
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Unreserved
Some balance was unreserved (moved from reserved to free).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u128```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Withdrawn
Some balances were withdrawn (e.g. pay for transaction fee)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u128```
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
    'Tokens', 'Accounts', ['AccountId', 'u128']
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
    'Tokens', 'Locks', ['AccountId', 'u128']
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
    'Tokens', 'Reserves', ['AccountId', 'u128']
)
```

#### Return value
```python
[{'amount': 'u128', 'id': '[u8; 8]'}]
```
---------
### TotalIssuance
 The total issuance of a token type.

#### Python
```python
result = substrate.query(
    'Tokens', 'TotalIssuance', ['u128']
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
2
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