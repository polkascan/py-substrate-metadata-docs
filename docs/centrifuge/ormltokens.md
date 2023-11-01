
# OrmlTokens

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
### Deposited
Deposited some balance into an account
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### DustLost
An account was removed whose balance was non-zero but below
ExistentialDeposit, resulting in an outright loss.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Endowed
An account was created with some free balance.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### LockRemoved
Some locked funds were unlocked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| lock_id | `LockIdentifier` | ```[u8; 8]```
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| who | `T::AccountId` | ```AccountId```

---------
### LockSet
Some funds are locked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| lock_id | `LockIdentifier` | ```[u8; 8]```
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Locked
Some free balance was locked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### ReserveRepatriated
Some reserved balance was repatriated (moved from reserved to
another account).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
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
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Slashed
Some balances were slashed (e.g. due to mis-behavior)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| who | `T::AccountId` | ```AccountId```
| free_amount | `T::Balance` | ```u128```
| reserved_amount | `T::Balance` | ```u128```

---------
### TotalIssuanceSet
The total issuance of an currency has been set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| amount | `T::Balance` | ```u128```

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
### Unlocked
Some locked balance was freed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Unreserved
Some balance was unreserved (moved from reserved to free).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Withdrawn
Some balances were withdrawn (e.g. pay for transaction fee)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
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
    'OrmlTokens', 'Accounts', [
    'AccountId',
    {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
    },
]
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
    'OrmlTokens', 'Locks', [
    'AccountId',
    {
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
    },
]
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
    'OrmlTokens', 'Reserves', [
    'AccountId',
    {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
    },
]
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
    'OrmlTokens', 'TotalIssuance', [
    {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
    },
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
### MaxLocks
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('OrmlTokens', 'MaxLocks')
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
constant = substrate.get_constant('OrmlTokens', 'MaxReserves')
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