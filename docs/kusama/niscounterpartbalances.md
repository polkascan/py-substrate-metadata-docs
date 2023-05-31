
# NisCounterpartBalances

---------
## Calls

---------
### force_set_balance
Set the regular balance of a given account.

The dispatch origin for this call is `root`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 
| new_free | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'NisCounterpartBalances', 'force_set_balance', {
    'new_free': 'u128',
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
### force_transfer
Exactly as `transfer_allow_death`, except the origin must be root and the source account
may be specified.
#### Attributes
| Name | Type |
| -------- | -------- | 
| source | `AccountIdLookupOf<T>` | 
| dest | `AccountIdLookupOf<T>` | 
| value | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'NisCounterpartBalances', 'force_transfer', {
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
    'NisCounterpartBalances', 'force_unreserve', {
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
### set_balance_deprecated
Set the regular balance of a given account; it also takes a reserved balance but this
must be the same as the account&\#x27;s current reserved balance.

The dispatch origin for this call is `root`.

WARNING: This call is DEPRECATED! Use `force_set_balance` instead.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 
| new_free | `T::Balance` | 
| old_reserved | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'NisCounterpartBalances', 'set_balance_deprecated', {
    'new_free': 'u128',
    'old_reserved': 'u128',
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
Alias for `transfer_allow_death`, provided only for name-wise compatibility.

WARNING: DEPRECATED! Will be released in approximately 3 months.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `AccountIdLookupOf<T>` | 
| value | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'NisCounterpartBalances', 'transfer', {
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
  keep the sender account alive (true).
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `AccountIdLookupOf<T>` | 
| keep_alive | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'NisCounterpartBalances', 'transfer_all', {
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
### transfer_allow_death
Transfer some liquid free balance to another account.

`transfer_allow_death` will set the `FreeBalance` of the sender and receiver.
If the sender&\#x27;s account is below the existential deposit as a result
of the transfer, the account will be reaped.

The dispatch origin for this call must be `Signed` by the transactor.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `AccountIdLookupOf<T>` | 
| value | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'NisCounterpartBalances', 'transfer_allow_death', {
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
### transfer_keep_alive
Same as the [`transfer_allow_death`] call, but with a check that the transfer will not
kill the origin account.

99% of the time you want [`transfer_allow_death`] instead.

[`transfer_allow_death`]: struct.Pallet.html\#method.transfer
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `AccountIdLookupOf<T>` | 
| value | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'NisCounterpartBalances', 'transfer_keep_alive', {
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
### upgrade_accounts
Upgrade a specified account.

- `origin`: Must be `Signed`.
- `who`: The account to be upgraded.

This will waive the transaction fee if at least all but 10% of the accounts needed to
be upgraded. (We let some not have to be upgraded just in order to allow for the
possibililty of churn).
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'NisCounterpartBalances', 'upgrade_accounts', {'who': ['AccountId']}
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

---------
### Burned
Some amount was burned from an account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

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
### Frozen
Some balance was frozen.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Issued
Total issuance was increased by `amount`, creating a credit to be balanced.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| amount | `T::Balance` | ```u128```

---------
### Locked
Some balance was locked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Minted
Some amount was minted into an account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Rescinded
Total issuance was decreased by `amount`, creating a debt to be balanced.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| amount | `T::Balance` | ```u128```

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
### Restored
Some amount was restored into an account.
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
### Suspended
Some amount was suspended from an account (it can be restored later).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Thawed
Some balance was thawed.
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
### Unlocked
Some balance was unlocked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
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
### Upgraded
An account was upgraded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

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
    'NisCounterpartBalances', 'Account', ['AccountId']
)
```

#### Return value
```python
{'flags': 'u128', 'free': 'u128', 'frozen': 'u128', 'reserved': 'u128'}
```
---------
### Freezes
 Freeze locks on account balances.

#### Python
```python
result = substrate.query(
    'NisCounterpartBalances', 'Freezes', ['AccountId']
)
```

#### Return value
```python
[{'amount': 'u128', 'id': ()}]
```
---------
### Holds
 Holds on account balances.

#### Python
```python
result = substrate.query(
    'NisCounterpartBalances', 'Holds', ['AccountId']
)
```

#### Return value
```python
[{'amount': 'u128', 'id': ()}]
```
---------
### InactiveIssuance
 The total units of outstanding deactivated balance in the system.

#### Python
```python
result = substrate.query(
    'NisCounterpartBalances', 'InactiveIssuance', []
)
```

#### Return value
```python
'u128'
```
---------
### Locks
 Any liquidity locks on some account balances.
 NOTE: Should only be accessed when setting, changing and freeing a lock.

#### Python
```python
result = substrate.query(
    'NisCounterpartBalances', 'Locks', ['AccountId']
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
    'NisCounterpartBalances', 'Reserves', ['AccountId']
)
```

#### Return value
```python
[{'amount': 'u128', 'id': '[u8; 8]'}]
```
---------
### TotalIssuance
 The total units issued in the system.

#### Python
```python
result = substrate.query(
    'NisCounterpartBalances', 'TotalIssuance', []
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
 The minimum amount required to keep an account open. MUST BE GREATER THAN ZERO!

 If you *really* need it to be zero, you can enable the feature `insecure_zero_ed` for
 this pallet. However, you do so at your own risk: this will open up a major DoS vector.
 In case you have multiple sources of provider references, you may also get unexpected
 behaviour if you set this to zero.

 Bottom line: Do yourself a favour and make it at least one!
#### Value
```python
10000000000
```
#### Python
```python
constant = substrate.get_constant('NisCounterpartBalances', 'ExistentialDeposit')
```
---------
### MaxFreezes
 The maximum number of individual freeze locks that can exist on an account at any time.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('NisCounterpartBalances', 'MaxFreezes')
```
---------
### MaxHolds
 The maximum number of holds that can exist on an account at any time.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('NisCounterpartBalances', 'MaxHolds')
```
---------
### MaxLocks
 The maximum number of locks that should exist on an account.
 Not strictly enforced, but used for weight estimation.
#### Value
```python
4
```
#### Python
```python
constant = substrate.get_constant('NisCounterpartBalances', 'MaxLocks')
```
---------
### MaxReserves
 The maximum number of named reserves that can exist on an account.
#### Value
```python
4
```
#### Python
```python
constant = substrate.get_constant('NisCounterpartBalances', 'MaxReserves')
```
---------
## Errors

---------
### DeadAccount
Beneficiary account must pre-exist.

---------
### ExistentialDeposit
Value too low to create account due to existential deposit.

---------
### ExistingVestingSchedule
A vesting schedule already exists for this account.

---------
### Expendability
Transfer/payment would kill account.

---------
### InsufficientBalance
Balance too low to send value.

---------
### LiquidityRestrictions
Account liquidity restrictions prevent withdrawal.

---------
### TooManyFreezes
Number of freezes exceed `MaxFreezes`.

---------
### TooManyHolds
Number of holds exceed `MaxHolds`.

---------
### TooManyReserves
Number of named reserves exceed `MaxReserves`.

---------
### VestingBalance
Vesting balance too high to send value.

---------