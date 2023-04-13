
# Balances

---------
## Events

---------
### BalanceSet
A balance was set by root.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| free | `T::Balance` | ```u128```
| reserved | `T::Balance` | ```u128```

---------
### Deposit
Some amount was deposited (e.g. for transaction fees).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### DustLost
An account was removed whose balance was non-zero but below ExistentialDeposit,
resulting in an outright loss.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Endowed
An account was created with some free balance.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| free_balance | `T::Balance` | ```u128```

---------
### ReserveRepatriated
Some balance was moved from the reserve of the first account to the second account.
Final argument indicates the destination balance type.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```
| destination_status | `Status` | ```('Free', 'Reserved')```

---------
### Reserved
Some balance was reserved (moved from free to reserved).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Slashed
Some amount was removed from the account (e.g. for misbehavior).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Transfer
Transfer succeeded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Unreserved
Some balance was unreserved (moved from reserved to free).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Withdraw
Some amount was withdrawn from the account (e.g. for transaction fees).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
## Storage functions

---------
### Account
 The Balances pallet example of storing the balance of an account.

 \# Example

 ```nocompile
  impl pallet_balances::Config for Runtime {
    type AccountStore = StorageMapShim&lt;Self::Account&lt;Runtime&gt;, frame_system::Provider&lt;Runtime&gt;, AccountId, Self::AccountData&lt;Balance&gt;&gt;
  }
 ```

 You can also store the balance of an account in the `System` pallet.

 \# Example

 ```nocompile
  impl pallet_balances::Config for Runtime {
   type AccountStore = System
  }
 ```

 But this comes with tradeoffs, storing account balances in the system pallet stores
 `frame_system` data alongside the account data contrary to storing account balances in the
 `Balances` pallet, which uses a `StorageMap` to store balances data only.
 NOTE: This is only used in the case that this pallet is used to store balances.

#### Python
```python
result = substrate.query(
    'Balances', 'Account', ['AccountId']
)
```

#### Return value
```python
{
    'fee_frozen': 'u128',
    'free': 'u128',
    'misc_frozen': 'u128',
    'reserved': 'u128',
}
```
---------
### Locks
 Any liquidity locks on some account balances.
 NOTE: Should only be accessed when setting, changing and freeing a lock.

#### Python
```python
result = substrate.query(
    'Balances', 'Locks', ['AccountId']
)
```

#### Return value
```python
[{'amount': 'u128', 'id': '[u8; 8]', 'reasons': ('Fee', 'Misc', 'All')}]
```
---------
### Reserves
 Named reserves on some account balances.

#### Python
```python
result = substrate.query(
    'Balances', 'Reserves', ['AccountId']
)
```

#### Return value
```python
[
    {
        'amount': 'u128',
        'id': (
            'CollatorSelection',
            'Honzon',
            'TransactionPayment',
            'TransactionPaymentDeposit',
            'Count',
        ),
    },
]
```
---------
### StorageVersion
 Storage version of the pallet.

 This is set to v2.0.0 for new networks.

#### Python
```python
result = substrate.query(
    'Balances', 'StorageVersion', []
)
```

#### Return value
```python
('V1_0_0', 'V2_0_0')
```
---------
### TotalIssuance
 The total units issued in the system.

#### Python
```python
result = substrate.query(
    'Balances', 'TotalIssuance', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### ExistentialDeposit
 The minimum amount required to keep an account open.
#### Value
```python
1000000000
```
#### Python
```python
constant = substrate.get_constant('Balances', 'ExistentialDeposit')
```
---------
### MaxLocks
 The maximum number of locks that should exist on an account.
 Not strictly enforced, but used for weight estimation.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('Balances', 'MaxLocks')
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
constant = substrate.get_constant('Balances', 'MaxReserves')
```
---------
## Errors

---------
### DeadAccount
Beneficiary account must pre-exist

---------
### ExistentialDeposit
Value too low to create account due to existential deposit

---------
### ExistingVestingSchedule
A vesting schedule already exists for this account

---------
### InsufficientBalance
Balance too low to send value

---------
### KeepAlive
Transfer/payment would kill account

---------
### LiquidityRestrictions
Account liquidity restrictions prevent withdrawal

---------
### TooManyReserves
Number of named reserves exceed MaxReserves

---------
### VestingBalance
Vesting balance too high to send value

---------