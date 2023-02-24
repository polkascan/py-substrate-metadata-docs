
# Balances

---------
## Calls

---------
### force_transfer
Exactly as `transfer`, except the origin must be root and the source account may be
specified.
\# &lt;weight&gt;
- Same as transfer, but additional read and write because the source account is not
  assumed to be in the overlay.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| source | `AccountIdLookupOf<T>` | 
| dest | `AccountIdLookupOf<T>` | 
| value | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Balances', 'force_transfer', {
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
    'value': 'u128',
}
)
```

---------
### force_unreserve
Unreserve some balance from a user by force.

Can only be called by ROOT.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Balances', 'force_unreserve', {
    'amount': 'u128',
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
### set_balance
Set the balances of a given account.

This will alter `FreeBalance` and `ReservedBalance` in storage. it will
also alter the total issuance of the system (`TotalIssuance`) appropriately.
If the new free or reserved balance is below the existential deposit,
it will reset the account nonce (`frame_system::AccountNonce`).

The dispatch origin for this call is `root`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 
| new_free | `T::Balance` | 
| new_reserved | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Balances', 'set_balance', {
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
Transfer some liquid free balance to another account.

`transfer` will set the `FreeBalance` of the sender and receiver.
If the sender&\#x27;s account is below the existential deposit as a result
of the transfer, the account will be reaped.

The dispatch origin for this call must be `Signed` by the transactor.

\# &lt;weight&gt;
- Dependent on arguments but not critical, given proper implementations for input config
  types. See related functions below.
- It contains a limited number of reads and writes internally and no complex
  computation.

Related functions:

  - `ensure_can_withdraw` is always called internally but has a bounded complexity.
  - Transferring balances to accounts that did not exist before will cause
    `T::OnNewAccount::on_new_account` to be called.
  - Removing enough funds from an account will trigger `T::DustRemoval::on_unbalanced`.
  - `transfer_keep_alive` works the same way as `transfer`, but has an additional check
    that the transfer will not kill the origin account.
---------------------------------
- Origin account is already in memory, so no DB operations for them.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `AccountIdLookupOf<T>` | 
| value | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Balances', 'transfer', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'value': 'u128',
}
)
```

---------
### transfer_all
Transfer the entire transferable balance from the caller account.

NOTE: This function only attempts to transfer _transferable_ balances. This means that
any locked, reserved, or existential deposits (when `keep_alive` is `true`), will not be
transferred by this function. To ensure that this function results in a killed account,
you might need to prepare the account by removing any reference counters, storage
deposits, etc...

The dispatch origin of this call must be Signed.

- `dest`: The recipient of the transfer.
- `keep_alive`: A boolean to determine if the `transfer_all` operation should send all
  of the funds the account has, causing the sender account to be killed (false), or
  transfer everything except at least the existential deposit, which will guarantee to
  keep the sender account alive (true). \# &lt;weight&gt;
- O(1). Just like transfer, but reading the user&\#x27;s transferable balance first.
  \#&lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `AccountIdLookupOf<T>` | 
| keep_alive | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Balances', 'transfer_all', {
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
Same as the [`transfer`] call, but with a check that the transfer will not kill the
origin account.

99% of the time you want [`transfer`] instead.

[`transfer`]: struct.Pallet.html\#method.transfer
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `AccountIdLookupOf<T>` | 
| value | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Balances', 'transfer_keep_alive', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'value': 'u128',
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
[{'amount': 'u128', 'id': '[u8; 16]'}]
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
0
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