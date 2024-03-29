
# ConvictionVoting

---------
## Calls

---------
### delegate
See [`Pallet::delegate`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| class | `ClassOf<T, I>` | 
| to | `AccountIdLookupOf<T>` | 
| conviction | `Conviction` | 
| balance | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'ConvictionVoting', 'delegate', {
    'balance': 'u128',
    'class': 'u16',
    'conviction': (
        'None',
        'Locked1x',
        'Locked2x',
        'Locked3x',
        'Locked4x',
        'Locked5x',
        'Locked6x',
    ),
    'to': {
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
### remove_other_vote
See [`Pallet::remove_other_vote`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `AccountIdLookupOf<T>` | 
| class | `ClassOf<T, I>` | 
| index | `PollIndexOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'ConvictionVoting', 'remove_other_vote', {
    'class': 'u16',
    'index': 'u32',
    'target': {
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
### remove_vote
See [`Pallet::remove_vote`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| class | `Option<ClassOf<T, I>>` | 
| index | `PollIndexOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'ConvictionVoting', 'remove_vote', {'class': (None, 'u16'), 'index': 'u32'}
)
```

---------
### undelegate
See [`Pallet::undelegate`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| class | `ClassOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'ConvictionVoting', 'undelegate', {'class': 'u16'}
)
```

---------
### unlock
See [`Pallet::unlock`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| class | `ClassOf<T, I>` | 
| target | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ConvictionVoting', 'unlock', {
    'class': 'u16',
    'target': {
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
### vote
See [`Pallet::vote`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| poll_index | `PollIndexOf<T, I>` | 
| vote | `AccountVote<BalanceOf<T, I>>` | 

#### Python
```python
call = substrate.compose_call(
    'ConvictionVoting', 'vote', {
    'poll_index': 'u32',
    'vote': {
        'Split': {
            'aye': 'u128',
            'nay': 'u128',
        },
        'SplitAbstain': {
            'abstain': 'u128',
            'aye': 'u128',
            'nay': 'u128',
        },
        'Standard': {
            'balance': 'u128',
            'vote': {
                'aye': 'bool',
                'conviction': (
                    'None',
                    'Locked1x',
                    'Locked2x',
                    'Locked3x',
                    'Locked4x',
                    'Locked5x',
                    'Locked6x',
                ),
            },
        },
    },
}
)
```

---------
## Events

---------
### Delegated
An account has delegated their vote to another account. \[who, target\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```

---------
### Undelegated
An \[account\] has cancelled a previous delegation operation.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### ClassLocksFor
 The voting classes which have a non-zero lock requirement and the lock amounts which they
 require. The actual amount locked on behalf of this pallet should always be the maximum of
 this list.

#### Python
```python
result = substrate.query(
    'ConvictionVoting', 'ClassLocksFor', ['AccountId']
)
```

#### Return value
```python
[('u16', 'u128')]
```
---------
### VotingFor
 All voting for a particular voter in a particular voting class. We store the balance for the
 number of votes that we have recorded.

#### Python
```python
result = substrate.query(
    'ConvictionVoting', 'VotingFor', ['AccountId', 'u16']
)
```

#### Return value
```python
{
    'Casting': {
        'delegations': {'capital': 'u128', 'votes': 'u128'},
        'prior': ('u32', 'u128'),
        'votes': [('u32', 'scale_info::138')],
    },
    'Delegating': {
        'balance': 'u128',
        'conviction': (
            'None',
            'Locked1x',
            'Locked2x',
            'Locked3x',
            'Locked4x',
            'Locked5x',
            'Locked6x',
        ),
        'delegations': {'capital': 'u128', 'votes': 'u128'},
        'prior': ('u32', 'u128'),
        'target': 'AccountId',
    },
}
```
---------
## Constants

---------
### MaxVotes
 The maximum number of concurrent votes an account may have.

 Also used to compute weight, an overly large value can lead to extrinsics with large
 weight estimation: see `delegate` for instance.
#### Value
```python
512
```
#### Python
```python
constant = substrate.get_constant('ConvictionVoting', 'MaxVotes')
```
---------
### VoteLockingPeriod
 The minimum period of vote locking.

 It should be no shorter than enactment period to ensure that in the case of an approval,
 those successful voters are locked into the consequences that their votes entail.
#### Value
```python
100800
```
#### Python
```python
constant = substrate.get_constant('ConvictionVoting', 'VoteLockingPeriod')
```
---------
## Errors

---------
### AlreadyDelegating
The account is already delegating.

---------
### AlreadyVoting
The account currently has votes attached to it and the operation cannot succeed until
these are removed, either through `unvote` or `reap_vote`.

---------
### BadClass
The class ID supplied is invalid.

---------
### ClassNeeded
The class must be supplied since it is not easily determinable from the state.

---------
### InsufficientFunds
Too high a balance was provided that the account cannot afford.

---------
### MaxVotesReached
Maximum number of votes reached.

---------
### NoPermission
The actor has no permission to conduct the action.

---------
### NoPermissionYet
The actor has no permission to conduct the action right now but will do in the future.

---------
### Nonsense
Delegation to oneself makes no sense.

---------
### NotDelegating
The account is not currently delegating.

---------
### NotOngoing
Poll is not ongoing.

---------
### NotVoter
The given account did not vote on the poll.

---------