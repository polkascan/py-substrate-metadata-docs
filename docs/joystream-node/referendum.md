
# Referendum

---------
## Calls

---------
### opt_out_of_voting
Permanently opt out of voting from a given account.

\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Referendum', 'opt_out_of_voting', {}
)
```

---------
### release_vote_stake
Release a locked stake.
\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Referendum', 'release_vote_stake', {}
)
```

---------
### reveal_vote
Reveal a sealed vote in the referendum.

\# &lt;weight&gt;

\#\# Weight
`O (W)` where:
- `W` is the number of `intermediate_winners` stored in the current
    `Stage::&lt;T, I&gt;::get()`
- DB:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| salt | `Vec<u8>` | 
| vote_option_id | `<T as common::membership::MembershipTypes>::MemberId` | 

#### Python
```python
call = substrate.compose_call(
    'Referendum', 'reveal_vote', {
    'salt': 'Bytes',
    'vote_option_id': 'u64',
}
)
```

---------
### vote
Cast a sealed vote in the referendum.

\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| commitment | `T::Hash` | 
| stake | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Referendum', 'vote', {
    'commitment': '[u8; 32]',
    'stake': 'u128',
}
)
```

---------
## Events

---------
### AccountOptedOutOfVoting
Account permanently opted out of voting in referendum.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```

---------
### ReferendumFinished
Referendum ended and winning option was selected
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<OptionResult<MemberId, VotePower>>` | ```[{'option_id': 'u64', 'vote_power': 'u128'}]```

---------
### ReferendumStarted
Referendum started
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```
| None | `BlockNumber` | ```u32```

---------
### ReferendumStartedForcefully
Referendum started
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```
| None | `BlockNumber` | ```u32```

---------
### RevealingStageStarted
Revealing phase has begun
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BlockNumber` | ```u32```

---------
### StakeReleased
User released his stake
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```

---------
### VoteCast
User cast a vote in referendum
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `Hash` | ```[u8; 32]```
| None | `Balance` | ```u128```

---------
### VoteRevealed
User revealed his vote
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `MemberId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
## Storage functions

---------
### AccountsOptedOut
 Accounts that permanently opted out of voting in referendum.

#### Python
```python
result = substrate.query(
    'Referendum', 'AccountsOptedOut', ['AccountId']
)
```

#### Return value
```python
()
```
---------
### Stage
 Current referendum stage.

#### Python
```python
result = substrate.query(
    'Referendum', 'Stage', []
)
```

#### Return value
```python
{
    'Inactive': None,
    'Revealing': {
        'current_cycle_id': 'u64',
        'ends_at': 'u32',
        'intermediate_winners': [{'option_id': 'u64', 'vote_power': 'u128'}],
        'started': 'u32',
        'winning_target_count': 'u32',
    },
    'Voting': {
        'current_cycle_id': 'u64',
        'ends_at': 'u32',
        'started': 'u32',
        'winning_target_count': 'u32',
    },
}
```
---------
### Votes
 Votes cast in the referendum. A new record is added to this map when a user casts a
 sealed vote.
 It is modified when a user reveals the vote&#x27;s commitment proof.
 A record is finally removed when the user unstakes, which can happen during a voting
 stage or after the current cycle ends.
 A stake for a vote can be reused in future referendum cycles.

#### Python
```python
result = substrate.query(
    'Referendum', 'Votes', ['AccountId']
)
```

#### Return value
```python
{
    'commitment': '[u8; 32]',
    'cycle_id': 'u64',
    'stake': 'u128',
    'vote_for': (None, 'u64'),
}
```
---------
## Constants

---------
### MaxSaltLength
 Maximum length of vote commitment salt. Use length that ensures uniqueness for hashing
 e.g. std::u64::MAX.
#### Value
```python
32
```
#### Python
```python
constant = substrate.get_constant('Referendum', 'MaxSaltLength')
```
---------
### MinimumStake
 Minimum stake needed for voting
#### Value
```python
1666666666660
```
#### Python
```python
constant = substrate.get_constant('Referendum', 'MinimumStake')
```
---------
### RevealStageDuration
 Duration of revealing stage (number of blocks)
#### Value
```python
43200
```
#### Python
```python
constant = substrate.get_constant('Referendum', 'RevealStageDuration')
```
---------
### StakingHandlerLockId
 Exports const - staking handler lock id.
#### Value
```python
'0x766f74696e672020'
```
#### Python
```python
constant = substrate.get_constant('Referendum', 'StakingHandlerLockId')
```
---------
### VoteStageDuration
 Duration of voting stage (number of blocks)
#### Value
```python
43200
```
#### Python
```python
constant = substrate.get_constant('Referendum', 'VoteStageDuration')
```
---------
## Errors

---------
### AccountAlreadyOptedOutOfVoting
A vote cannot be cast from an account that already opted out of voting.

---------
### AlreadyVotedThisCycle
Trying to vote multiple time in the same cycle

---------
### BadOrigin
Origin is invalid

---------
### ConflictStakesOnAccount
Staking account contains conflicting stakes.

---------
### InsufficientBalanceToStake
Account Insufficient Free Balance (now)

---------
### InsufficientStake
Insufficient stake provided to cast a vote

---------
### InvalidReveal
Salt and referendum option provided don&\#x27;t correspond to the commitment

---------
### InvalidVote
Vote for not existing option was revealed

---------
### ReferendumNotRunning
Referendum is not running when expected to

---------
### RevealingNotInProgress
Revealing stage is not in progress right now

---------
### SaltTooLong
Salt is too long

---------
### UnstakingForbidden
Unstaking has been forbidden for the user (at least for now)

---------
### UnstakingVoteInSameCycle
Invalid time to release the locked stake

---------
### VoteNotExisting
Trying to reveal vote that was not cast

---------