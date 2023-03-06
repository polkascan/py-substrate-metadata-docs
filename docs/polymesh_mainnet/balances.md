
# Balances

---------
## Calls

---------
### burn_account_balance
Burns the given amount of tokens from the caller&\#x27;s free, unlocked balance.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Balances', 'burn_account_balance', {'amount': 'u128'}
)
```

---------
### deposit_block_reward_reserve_balance
Move some POLYX from balance of self to balance of BRR.
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Balances', 'deposit_block_reward_reserve_balance', {'value': 'u128'}
)
```

---------
### force_transfer
Exactly as `transfer`, except the origin must be root and the source account may be
specified.

\# &lt;weight&gt;
- Same as transfer, but additional read and write because the source account is
  not assumed to be in the overlay.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| source | `<T::Lookup as StaticLookup>::Source` | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| value | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Balances', 'force_transfer', {
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
    'value': 'u128',
}
)
```

---------
### set_balance
Set the balances of a given account.

This will alter `FreeBalance` and `ReservedBalance` in storage. it will
also decrease the total issuance of the system (`TotalIssuance`).

The dispatch origin for this call is `root`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| new_free | `Balance` | 
| new_reserved | `Balance` | 

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
It will decrease the total issuance of the system by the `TransferFee`.

The dispatch origin for this call must be `Signed` by the transactor.

\# &lt;weight&gt;
- Dependent on arguments but not critical, given proper implementations for
  input config types. See related functions below.
- It contains a limited number of reads and writes internally and no complex computation.

Related functions:

  - `ensure_can_withdraw` is always called internally but has a bounded complexity.
  - Transferring balances to accounts that did not exist before will cause
     `T::OnNewAccount::on_new_account` to be called.
---------------------------------
- Base Weight: 73.64 µs, worst case scenario (account created, account removed)
- DB Weight: 1 Read and 1 Write to destination account.
- Origin account is already in memory, so no DB operations for them.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| value | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Balances', 'transfer', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'value': 'u128',
}
)
```

---------
### transfer_with_memo
Transfer the native currency with the help of identifier string
this functionality can help to differentiate the transfers.

\# &lt;weight&gt;
- Base Weight: 73.64 µs, worst case scenario (account created, account removed)
- DB Weight: 1 Read and 1 Write to destination account.
- Origin account is already in memory, so no DB operations for them.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| value | `Balance` | 
| memo | `Option<Memo>` | 

#### Python
```python
call = substrate.compose_call(
    'Balances', 'transfer_with_memo', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'memo': (None, '[u8; 32]'),
    'value': 'u128',
}
)
```

---------
## Events

---------
### AccountBalanceBurned
The account and the amount of unlocked balance of that account that was burned.
(caller Id, caller account, amount)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### BalanceSet
A balance was set by root (did, who, free, reserved).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### Endowed
An account was created with some free balance. \[did, account, free_balance]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Option<IdentityId>` | ```(None, '[u8; 32]')```
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### ReserveRepatriated
Some balance was moved from the reserve of the first account to the second account.
Final argument indicates the destination balance type.
\[from, to, balance, destination_status]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `Status` | ```('Free', 'Reserved')```

---------
### Reserved
Some balance was reserved (moved from free to reserved). \[who, value]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### Transfer
Transfer succeeded (from_did, from, to_did, to, value, memo).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Option<IdentityId>` | ```(None, '[u8; 32]')```
| None | `AccountId` | ```AccountId```
| None | `Option<IdentityId>` | ```(None, '[u8; 32]')```
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `Option<Memo>` | ```(None, '[u8; 32]')```

---------
### Unreserved
Some balance was unreserved (moved from reserved to free). \[who, value]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
## Storage functions

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
## Errors

---------
### ExistentialDeposit
Value too low to create account due to existential deposit

---------
### InsufficientBalance
Balance too low to send value

---------
### LiquidityRestrictions
Account liquidity restrictions prevent withdrawal

---------
### Overflow
Got an overflow after adding

---------
### ReceiverCddMissing
Receiver does not have a valid CDD

---------