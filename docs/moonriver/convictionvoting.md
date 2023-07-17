
# ConvictionVoting

---------
## Calls

---------
### delegate
Delegate the voting power (with some given conviction) of the sending account for a
particular class of polls.

The balance delegated is locked for as long as it&\#x27;s delegated, and thereafter for the
time appropriate for the conviction&\#x27;s lock period.

The dispatch origin of this call must be _Signed_, and the signing account must either:
  - be delegating already; or
  - have no voting activity (if there is, then it will need to be removed/consolidated
    through `reap_vote` or `unvote`).

- `to`: The account whose voting the `target` account&\#x27;s voting power will follow.
- `class`: The class of polls to delegate. To delegate multiple classes, multiple calls
  to this function are required.
- `conviction`: The conviction that will be attached to the delegated votes. When the
  account is undelegated, the funds will be locked for the corresponding period.
- `balance`: The amount of the account&\#x27;s balance to be used in delegating. This must not
  be more than the account&\#x27;s current balance.

Emits `Delegated`.

Weight: `O(R)` where R is the number of polls the voter delegating to has
  voted on. Weight is initially charged as if maximum votes, but is refunded later.
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
    'to': '[u8; 20]',
}
)
```

---------
### remove_other_vote
Remove a vote for a poll.

If the `target` is equal to the signer, then this function is exactly equivalent to
`remove_vote`. If not equal to the signer, then the vote must have expired,
either because the poll was cancelled, because the voter lost the poll or
because the conviction period is over.

The dispatch origin of this call must be _Signed_.

- `target`: The account of the vote to be removed; this account must have voted for poll
  `index`.
- `index`: The index of poll of the vote to be removed.
- `class`: The class of the poll.

Weight: `O(R + log R)` where R is the number of polls that `target` has voted on.
  Weight is calculated for the maximum number of vote.
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
    'target': '[u8; 20]',
}
)
```

---------
### remove_vote
Remove a vote for a poll.

If:
- the poll was cancelled, or
- the poll is ongoing, or
- the poll has ended such that
  - the vote of the account was in opposition to the result; or
  - there was no conviction to the account&\#x27;s vote; or
  - the account made a split vote
...then the vote is removed cleanly and a following call to `unlock` may result in more
funds being available.

If, however, the poll has ended and:
- it finished corresponding to the vote of the account, and
- the account made a standard vote with conviction, and
- the lock period of the conviction is not over
...then the lock will be aggregated into the overall account&\#x27;s lock, which may involve
*overlocking* (where the two locks are combined into a single lock that is the maximum
of both the amount locked and the time is it locked for).

The dispatch origin of this call must be _Signed_, and the signer must have a vote
registered for poll `index`.

- `index`: The index of poll of the vote to be removed.
- `class`: Optional parameter, if given it indicates the class of the poll. For polls
  which have finished or are cancelled, this must be `Some`.

Weight: `O(R + log R)` where R is the number of polls that `target` has voted on.
  Weight is calculated for the maximum number of vote.
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
Undelegate the voting power of the sending account for a particular class of polls.

Tokens may be unlocked following once an amount of time consistent with the lock period
of the conviction with which the delegation was issued has passed.

The dispatch origin of this call must be _Signed_ and the signing account must be
currently delegating.

- `class`: The class of polls to remove the delegation from.

Emits `Undelegated`.

Weight: `O(R)` where R is the number of polls the voter delegating to has
  voted on. Weight is initially charged as if maximum votes, but is refunded later.
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
Remove the lock caused by prior voting/delegating which has expired within a particular
class.

The dispatch origin of this call must be _Signed_.

- `class`: The class of polls to unlock.
- `target`: The account to remove the lock on.

Weight: `O(R)` with R number of vote of target.
#### Attributes
| Name | Type |
| -------- | -------- | 
| class | `ClassOf<T, I>` | 
| target | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ConvictionVoting', 'unlock', {'class': 'u16', 'target': '[u8; 20]'}
)
```

---------
### vote
Vote in a poll. If `vote.is_aye()`, the vote is to enact the proposal;
otherwise it is a vote to keep the status quo.

The dispatch origin of this call must be _Signed_.

- `poll_index`: The index of the poll to vote for.
- `vote`: The vote configuration.

Weight: `O(R)` where R is the number of polls the voter has voted on.
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
| None | `T::AccountId` | ```[u8; 20]```
| None | `T::AccountId` | ```[u8; 20]```

---------
### Undelegated
An \[account\] has cancelled a previous delegation operation.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```[u8; 20]```

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
    'ConvictionVoting', 'ClassLocksFor', ['[u8; 20]']
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
    'ConvictionVoting', 'VotingFor', ['[u8; 20]', 'u16']
)
```

#### Return value
```python
{
    'Casting': {
        'delegations': {'capital': 'u128', 'votes': 'u128'},
        'prior': ('u32', 'u128'),
        'votes': [('u32', 'scale_info::210')],
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
        'target': '[u8; 20]',
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
7200
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