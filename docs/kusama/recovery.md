
# Recovery

---------
## Calls

---------
### as_recovered
See [`Pallet::as_recovered`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `AccountIdLookupOf<T>` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Recovery', 'as_recovered', {
    'account': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'call': 'Call',
}
)
```

---------
### cancel_recovered
See [`Pallet::cancel_recovered`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Recovery', 'cancel_recovered', {
    'account': {
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
### claim_recovery
See [`Pallet::claim_recovery`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Recovery', 'claim_recovery', {
    'account': {
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
### close_recovery
See [`Pallet::close_recovery`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| rescuer | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Recovery', 'close_recovery', {
    'rescuer': {
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
### create_recovery
See [`Pallet::create_recovery`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| friends | `Vec<T::AccountId>` | 
| threshold | `u16` | 
| delay_period | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Recovery', 'create_recovery', {
    'delay_period': 'u32',
    'friends': ['AccountId'],
    'threshold': 'u16',
}
)
```

---------
### initiate_recovery
See [`Pallet::initiate_recovery`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Recovery', 'initiate_recovery', {
    'account': {
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
### remove_recovery
See [`Pallet::remove_recovery`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Recovery', 'remove_recovery', {}
)
```

---------
### set_recovered
See [`Pallet::set_recovered`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| lost | `AccountIdLookupOf<T>` | 
| rescuer | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Recovery', 'set_recovered', {
    'lost': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'rescuer': {
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
### vouch_recovery
See [`Pallet::vouch_recovery`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| lost | `AccountIdLookupOf<T>` | 
| rescuer | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Recovery', 'vouch_recovery', {
    'lost': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'rescuer': {
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
### AccountRecovered
Lost account has been successfully recovered by rescuer account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| lost_account | `T::AccountId` | ```AccountId```
| rescuer_account | `T::AccountId` | ```AccountId```

---------
### RecoveryClosed
A recovery process for lost account by rescuer account has been closed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| lost_account | `T::AccountId` | ```AccountId```
| rescuer_account | `T::AccountId` | ```AccountId```

---------
### RecoveryCreated
A recovery process has been set up for an account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
### RecoveryInitiated
A recovery process has been initiated for lost account by rescuer account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| lost_account | `T::AccountId` | ```AccountId```
| rescuer_account | `T::AccountId` | ```AccountId```

---------
### RecoveryRemoved
A recovery process has been removed for an account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| lost_account | `T::AccountId` | ```AccountId```

---------
### RecoveryVouched
A recovery process for lost account by rescuer account has been vouched for by sender.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| lost_account | `T::AccountId` | ```AccountId```
| rescuer_account | `T::AccountId` | ```AccountId```
| sender | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### ActiveRecoveries
 Active recovery attempts.

 First account is the account to be recovered, and the second account
 is the user trying to recover the account.

#### Python
```python
result = substrate.query(
    'Recovery', 'ActiveRecoveries', ['AccountId', 'AccountId']
)
```

#### Return value
```python
{'created': 'u32', 'deposit': 'u128', 'friends': ['AccountId']}
```
---------
### Proxy
 The list of allowed proxy accounts.

 Map from the user who can access it to the recovered account.

#### Python
```python
result = substrate.query(
    'Recovery', 'Proxy', ['AccountId']
)
```

#### Return value
```python
'AccountId'
```
---------
### Recoverable
 The set of recoverable accounts and their recovery configuration.

#### Python
```python
result = substrate.query(
    'Recovery', 'Recoverable', ['AccountId']
)
```

#### Return value
```python
{'delay_period': 'u32', 'deposit': 'u128', 'friends': ['AccountId'], 'threshold': 'u16'}
```
---------
## Constants

---------
### ConfigDepositBase
 The base amount of currency needed to reserve for creating a recovery configuration.

 This is held for an additional storage item whose value size is
 `2 + sizeof(BlockNumber, Balance)` bytes.
#### Value
```python
166666666500
```
#### Python
```python
constant = substrate.get_constant('Recovery', 'ConfigDepositBase')
```
---------
### FriendDepositFactor
 The amount of currency needed per additional user when creating a recovery
 configuration.

 This is held for adding `sizeof(AccountId)` bytes more into a pre-existing storage
 value.
#### Value
```python
16666666650
```
#### Python
```python
constant = substrate.get_constant('Recovery', 'FriendDepositFactor')
```
---------
### MaxFriends
 The maximum amount of friends allowed in a recovery configuration.

 NOTE: The threshold programmed in this Pallet uses u16, so it does
 not really make sense to have a limit here greater than u16::MAX.
 But also, that is a lot more than you should probably set this value
 to anyway...
#### Value
```python
9
```
#### Python
```python
constant = substrate.get_constant('Recovery', 'MaxFriends')
```
---------
### RecoveryDeposit
 The base amount of currency needed to reserve for starting a recovery.

 This is primarily held for deterring malicious recovery attempts, and should
 have a value large enough that a bad actor would choose not to place this
 deposit. It also acts to fund additional storage item whose value size is
 `sizeof(BlockNumber, Balance + T * AccountId)` bytes. Where T is a configurable
 threshold.
#### Value
```python
166666666500
```
#### Python
```python
constant = substrate.get_constant('Recovery', 'RecoveryDeposit')
```
---------
## Errors

---------
### AlreadyProxy
This account is already set up for recovery

---------
### AlreadyRecoverable
This account is already set up for recovery

---------
### AlreadyStarted
A recovery process has already started for this account

---------
### AlreadyVouched
This user has already vouched for this recovery

---------
### BadState
Some internal state is broken.

---------
### DelayPeriod
The friend must wait until the delay period to vouch for this recovery

---------
### MaxFriends
Friends list must be less than max friends

---------
### NotAllowed
User is not allowed to make a call on behalf of this account

---------
### NotEnoughFriends
Friends list must be greater than zero and threshold

---------
### NotFriend
This account is not a friend who can vouch

---------
### NotRecoverable
This account is not set up for recovery

---------
### NotSorted
Friends list must be sorted and free of duplicates

---------
### NotStarted
A recovery process has not started for this rescuer

---------
### StillActive
There are still active recovery attempts that need to be closed

---------
### Threshold
The threshold for recovering this account has not been met

---------
### ZeroThreshold
Threshold must be greater than zero

---------