
# Recovery

---------
## Calls

---------
### as_recovered
Send a call through a recovered account.

The dispatch origin for this call must be _Signed_ and registered to
be able to make calls on behalf of the recovered account.

Parameters:
- `account`: The recovered account you want to make a call on-behalf-of.
- `call`: The call you want to make with the recovered account.
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
Cancel the ability to use `as_recovered` for `account`.

The dispatch origin for this call must be _Signed_ and registered to
be able to make calls on behalf of the recovered account.

Parameters:
- `account`: The recovered account you are able to call on-behalf-of.
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
Allow a successful rescuer to claim their recovered account.

The dispatch origin for this call must be _Signed_ and must be a &quot;rescuer&quot;
who has successfully completed the account recovery process: collected
`threshold` or more vouches, waited `delay_period` blocks since initiation.

Parameters:
- `account`: The lost account that you want to claim has been successfully recovered by
  you.
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
As the controller of a recoverable account, close an active recovery
process for your account.

Payment: By calling this function, the recoverable account will receive
the recovery deposit `RecoveryDeposit` placed by the rescuer.

The dispatch origin for this call must be _Signed_ and must be a
recoverable account with an active recovery process for it.

Parameters:
- `rescuer`: The account trying to rescue this recoverable account.
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
Create a recovery configuration for your account. This makes your account recoverable.

Payment: `ConfigDepositBase` + `FriendDepositFactor` * \#_of_friends balance
will be reserved for storing the recovery configuration. This deposit is returned
in full when the user calls `remove_recovery`.

The dispatch origin for this call must be _Signed_.

Parameters:
- `friends`: A list of friends you trust to vouch for recovery attempts. Should be
  ordered and contain no duplicate values.
- `threshold`: The number of friends that must vouch for a recovery attempt before the
  account can be recovered. Should be less than or equal to the length of the list of
  friends.
- `delay_period`: The number of blocks after a recovery attempt is initialized that
  needs to pass before the account can be recovered.
#### Attributes
| Name | Type |
| -------- | -------- | 
| friends | `Vec<T::AccountId>` | 
| threshold | `u16` | 
| delay_period | `T::BlockNumber` | 

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
Initiate the process for recovering a recoverable account.

Payment: `RecoveryDeposit` balance will be reserved for initiating the
recovery process. This deposit will always be repatriated to the account
trying to be recovered. See `close_recovery`.

The dispatch origin for this call must be _Signed_.

Parameters:
- `account`: The lost account that you want to recover. This account needs to be
  recoverable (i.e. have a recovery configuration).
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
Remove the recovery process for your account. Recovered accounts are still accessible.

NOTE: The user must make sure to call `close_recovery` on all active
recovery attempts before calling this function else it will fail.

Payment: By calling this function the recoverable account will unreserve
their recovery configuration deposit.
(`ConfigDepositBase` + `FriendDepositFactor` * \#_of_friends)

The dispatch origin for this call must be _Signed_ and must be a
recoverable account (i.e. has a recovery configuration).
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
Allow ROOT to bypass the recovery process and set an a rescuer account
for a lost account directly.

The dispatch origin for this call must be _ROOT_.

Parameters:
- `lost`: The &quot;lost account&quot; to be recovered.
- `rescuer`: The &quot;rescuer account&quot; which can call as the lost account.
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
Allow a &quot;friend&quot; of a recoverable account to vouch for an active recovery
process for that account.

The dispatch origin for this call must be _Signed_ and must be a &quot;friend&quot;
for the recoverable account.

Parameters:
- `lost`: The lost account that you want to recover.
- `rescuer`: The account trying to rescue the lost account that you want to vouch for.

The combination of these two parameters must point to an active recovery
process.
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