
# EqLockdrop

---------
## Calls

---------
### clear_lock_start
Clear `LockStart` value
WARNING! Check twice before using it!
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'EqLockdrop', 'clear_lock_start', {}
)
```

---------
### lock
Lock `amount` of Eq for lock
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'EqLockdrop', 'lock', {'amount': 'u128'}
)
```

---------
### set_auto_unlock
Enables or disables offchain worker. `true` to enable offchain worker
operations, `false` to disable.
#### Attributes
| Name | Type |
| -------- | -------- | 
| enabled | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'EqLockdrop', 'set_auto_unlock', {'enabled': 'bool'}
)
```

---------
### set_lock_start
Set `Lock
Start` in `timestamp`
- timestamp: UnixTime timestamp in seconds
WARNING! Check twice before using it!
#### Attributes
| Name | Type |
| -------- | -------- | 
| timestamp | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'EqLockdrop', 'set_lock_start', {'timestamp': 'u64'}
)
```

---------
### unlock
Unlock all account&\#x27;s locked Eq
The dispatch origin for this call must be _None_ (unsigned transaction).
#### Attributes
| Name | Type |
| -------- | -------- | 
| request | `OperationRequest<T::AccountId, T::BlockNumber>` | 
| signature | `<T::AuthorityId as RuntimeAppPublic>::Signature` | 

#### Python
```python
call = substrate.compose_call(
    'EqLockdrop', 'unlock', {
    'request': {
        'account': 'AccountId',
        'authority_index': 'u32',
        'block_num': 'u32',
        'validators_len': 'u32',
    },
    'signature': '[u8; 64]',
}
)
```

---------
### unlock_external
Unlock all account&\#x27;s locked Eq
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'EqLockdrop', 'unlock_external', {}
)
```

---------
## Events

---------
### Lock
User `who` locks `amount` of Eq
\[who, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::Balance` | ```u128```

---------
### Unlock
User `who` unlocks `amount` of Eq
\[who, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::Balance` | ```u128```

---------
## Storage functions

---------
### AutoUnlockEnabled
 Stores flag for on/off setting for offchain worker (unlocks)

#### Python
```python
result = substrate.query(
    'EqLockdrop', 'AutoUnlockEnabled', []
)
```

#### Return value
```python
'bool'
```
---------
### LockStart
 Pallet storage - start of lock program.
 Value is UnixTime timestamp in seconds

#### Python
```python
result = substrate.query(
    'EqLockdrop', 'LockStart', []
)
```

#### Return value
```python
'u64'
```
---------
### Locks
 Pallet storage - accounts locks

#### Python
```python
result = substrate.query(
    'EqLockdrop', 'Locks', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### MaxOffchainUnlocks
 This is the max amount of unlocks an offchain worker can make

#### Python
```python
result = substrate.query(
    'EqLockdrop', 'MaxOffchainUnlocks', []
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### LockDropUnsignedPriority
 Used for calculation unsigned transaction priority
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('EqLockdrop', 'LockDropUnsignedPriority')
```
---------
### LockPeriod
 Period of lock program in seconds
#### Value
```python
7776000
```
#### Python
```python
constant = substrate.get_constant('EqLockdrop', 'LockPeriod')
```
---------
### MinLockAmount
 Minimum amount to lock
#### Value
```python
10000000000
```
#### Python
```python
constant = substrate.get_constant('EqLockdrop', 'MinLockAmount')
```
---------
### PalletId
 Pallet&#x27;s AccountId for balances
#### Value
```python
'0x65712f6c6b647270'
```
#### Python
```python
constant = substrate.get_constant('EqLockdrop', 'PalletId')
```
---------
## Errors

---------
### LockAmountLow
Lock amount is lower than minimum allowed

---------
### LockPeriodNotOver
Not allowed to make unlock in the period of the lock program

---------
### LockStartNotEmpty
Lock start is already initialized

---------
### MultipleTransferWithVesting
Not allowed to make multiple locks if account has vesting schedule

---------
### OutOfLockPeriod
Not allowed to make lock not in the period of the lock program

---------