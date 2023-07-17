
# CollatorStaking

---------
## Calls

---------
### force_set_current_max_candidates
Set the current max candidates, must be within 0 and
[`MaxCandidates`](Config::MaxCandidates)

Only [`ForceOrigin`](Config::ForceOrigin) can call this function.

\# Errors

- [`Error::TooManyCandidates`] if the number of candidates is already at the maximum.
#### Attributes
| Name | Type |
| -------- | -------- | 
| max_candidates | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorStaking', 'force_set_current_max_candidates', {'max_candidates': 'u32'}
)
```

---------
### force_set_min_collator_stake
Set the minimum collator stake amount

[`T::ForceOrigin`](Config::ForceOrigin) call only
#### Attributes
| Name | Type |
| -------- | -------- | 
| min_collator_stake | `Amount<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorStaking', 'force_set_min_collator_stake', {'min_collator_stake': 'u128'}
)
```

---------
### join_candidates
Join the list of candidates for collation.

\# Errors

- [`Error::BelowMinStakeAmount`] if `amount` is below the minimum required amount.
- [`Error::NominationExists`] if nomination already exists.
- [`Error::AccountIdNotRegistered`] if `AccountId` is not registered as a collator.
- [`Error::NoAssociatedValidatorId`] if no associated validator ID for `AccountId`.
- [`Error::TooManyCandidates`] if the number of candidates is already at the maximum.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Amount<T>` | 
| rewards_cut | `Perbill` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorStaking', 'join_candidates', {
    'amount': 'u128',
    'rewards_cut': 'u32',
}
)
```

---------
### nominate
Nominate a specific candidate to be selected for collation and block production.

\# Errors

- [`Error::CandidateDoesNotExist`] if the candidate does not exist.
- [`Error::NominationExists`] if the nomination already exists.
- [`Error::BelowMinNominationStakeAmount`] if the nomination amount is below the
  minimum.
- [`Error::TooManyNominations`] if there are too many nominations for the candidate.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collator_id | `T::AccountId` | 
| amount | `Amount<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorStaking', 'nominate', {
    'amount': 'u128',
    'collator_id': 'AccountId',
}
)
```

---------
### remove_nomination
Remove a nomination previously registered for a specific collator candidate.

\# Errors

- [`Error::CandidateDoesNotExist`] if the candidate does not exist.
- [`Error::NominationDoesNotExist`] if the nomination does not exist.
- [`Error::TooManyCandidates`] if there are too many candidates in the set.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collator_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorStaking', 'remove_nomination', {'collator_id': 'AccountId'}
)
```

---------
### set_invulnerables
Force set the invulnerables.

[`ForceOrigin`](Config::ForceOrigin) call only.

\# Errors

- [`Error::TooManyInvulnerables`] if the number of invulnerables exceeds the maximum
#### Attributes
| Name | Type |
| -------- | -------- | 
| accounts | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorStaking', 'set_invulnerables', {'accounts': ['AccountId']}
)
```

---------
### unbond
Leave the collator set of this parachain.

In this case, if the calling account is already a collator, an exit
is registered so that this account is not selected for the next set of collators.
Otherwise, if the account is only a candidate, this candidate will be removed
and the nominations would be freed up.

\# Errors

- [`Error::CandidateDoesNotExist`] if candidate does not exist.
- [`Error::CannotUnbondInvulnerable`] cannot unbond an invulnerable collator.
- [`Error::ExitInProgress`] if unbonding for collator already in progress.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'CollatorStaking', 'unbond', {}
)
```

---------
## Events

---------
### CandidateJoined
A new candidate joined the list of candidates.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| amount | `Amount<T>` | ```u128```
| rewards_cut | `Perbill` | ```u32```

---------
### CandidateRemoved
Candidate was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
### CollatorSelected
A candidate has been selected to become a collator for the current round.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
### NewInvulnerables
A new list of invulnerables has been set by root.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| new | `Vec<T::AccountId>` | ```['AccountId']```

---------
### Nominated
A new nomination was registered for a specific candidate.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| collator_id | `T::AccountId` | ```AccountId```
| amount | `Amount<T>` | ```u128```

---------
### NominationRemoved
Nomination was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| collator_id | `T::AccountId` | ```AccountId```
| amount | `Amount<T>` | ```u128```

---------
### RoundFinalized
A new round was finalized
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| number | `T::BlockNumber` | ```u32```

---------
## Storage functions

---------
### Candidates
 The current set of candidates for collation.

#### Python
```python
result = substrate.query(
    'CollatorStaking', 'Candidates', []
)
```

#### Return value
```python
[
    {
        'account': 'AccountId',
        'amount': 'u128',
        'nominators': ['AccountId'],
        'rewards_cut': 'u32',
        'total_stake': 'u128',
    },
]
```
---------
### CollatorExits
 The list of collators who requested an exit.

#### Python
```python
result = substrate.query(
    'CollatorStaking', 'CollatorExits', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### Collators
 The current set of collators

#### Python
```python
result = substrate.query(
    'CollatorStaking', 'Collators', []
)
```

#### Return value
```python
[
    {
        'account': 'AccountId',
        'amount': 'u128',
        'nominators': ['AccountId'],
        'rewards_cut': 'u32',
        'total_stake': 'u128',
    },
]
```
---------
### CurrentRound
 The current round information.

#### Python
```python
result = substrate.query(
    'CollatorStaking', 'CurrentRound', []
)
```

#### Return value
```python
{
    'collators': [
        {
            'account': 'AccountId',
            'amount': 'u128',
            'nominators': ['AccountId'],
            'rewards_cut': 'u32',
            'total_stake': 'u128',
        },
    ],
    'number': 'u32',
    'starting_block': 'u32',
}
```
---------
### DesiredCandidatesCount
 The current candidate limit, must be within 0 and [`MaxCandidates`](Config::MaxCandidates)

#### Python
```python
result = substrate.query(
    'CollatorStaking', 'DesiredCandidatesCount', []
)
```

#### Return value
```python
'u32'
```
---------
### Invulnerables
 The invulnerable collators

 This is the list of collators who are invulnerable to being ejected from collation
 either by unbonding or by having less stake.

#### Python
```python
result = substrate.query(
    'CollatorStaking', 'Invulnerables', []
)
```

#### Return value
```python
[
    {
        'account': 'AccountId',
        'amount': 'u128',
        'nominators': ['AccountId'],
        'rewards_cut': 'u32',
        'total_stake': 'u128',
    },
]
```
---------
### MinCollatorStake
 The min stake amount for collators

#### Python
```python
result = substrate.query(
    'CollatorStaking', 'MinCollatorStake', []
)
```

#### Return value
```python
'u128'
```
---------
### Nominators
 The current set of nominators.

 Each nominator is allowed to nominate one collator.

#### Python
```python
result = substrate.query(
    'CollatorStaking', 'Nominators', ['AccountId']
)
```

#### Return value
```python
{'account': 'AccountId', 'amount': 'u128'}
```
---------
### SessionInfo
 The session info of collators including produced blocks and uptime

#### Python
```python
result = substrate.query(
    'CollatorStaking', 'SessionInfo', ['AccountId', 'u32']
)
```

#### Return value
```python
{'authored_block_count': 'u32', 'uptime': 'u32'}
```
---------
## Constants

---------
### CollatorExitThreshold
 The number of rounds that have to pass after the collator has requested
 unbonding for the bonded stake to be released.
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('CollatorStaking', 'CollatorExitThreshold')
```
---------
### CollatorPoolAccountId
 The [`AccountId`](frame_system::Config::AccountId) for the collator pool
#### Value
```python
'efRd63tR845wJ4KW17VFyzzS38m2zRjMbabQa5VyTNTikSqdy'
```
#### Python
```python
constant = substrate.get_constant('CollatorStaking', 'CollatorPoolAccountId')
```
---------
### DefaultMinCollatorStake
 The default minimum collator stake amount
#### Value
```python
250000000000000000000000
```
#### Python
```python
constant = substrate.get_constant('CollatorStaking', 'DefaultMinCollatorStake')
```
---------
### FeeDistributorAccountId
 The [`AccountId`](frame_system::Config::AccountId) for the fee distributor
#### Value
```python
'efRd63tR845wJTXfddgZNfNZ55o23Erydfz8esAmo1HfgMZMS'
```
#### Python
```python
constant = substrate.get_constant('CollatorStaking', 'FeeDistributorAccountId')
```
---------
### MaxCandidates
 The number of selected collators
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('CollatorStaking', 'MaxCandidates')
```
---------
### MaxCollators
 The number of selected collators
#### Value
```python
25
```
#### Python
```python
constant = substrate.get_constant('CollatorStaking', 'MaxCollators')
```
---------
### MaxInvulnerables
 Maximum number of invulnerables.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('CollatorStaking', 'MaxInvulnerables')
```
---------
### MaxNominationsPerCollator
 Maximum nominators per collator
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('CollatorStaking', 'MaxNominationsPerCollator')
```
---------
### MinNominationStakeAmount
 Minimum nomination stake required
#### Value
```python
5000000000000000000
```
#### Python
```python
constant = substrate.get_constant('CollatorStaking', 'MinNominationStakeAmount')
```
---------
### SessionPeriod
 The total number of blocks within a session
#### Value
```python
600
```
#### Python
```python
constant = substrate.get_constant('CollatorStaking', 'SessionPeriod')
```
---------
## Errors

---------
### AccountIdNotRegistered
Collators Account is not yet registered

---------
### BelowMinNominationStakeAmount
Nomination stake is below the minimum required amount.

---------
### BelowMinStakeAmount
Candidate stake is below the minimum required amount.

---------
### CandidateDoesNotExist
Candidate was not found.

---------
### CandidateExists
Candidate was already registered.

---------
### CannotUnbondInvulnerable
Cannot unbond Invulnerable

---------
### ExitInProgress
A candidate has already registered an exit.

---------
### NoAssociatedValidatorId
Account has no associated validator ID

---------
### NominationDoesNotExist
Nomination was not found.

---------
### NominationExists
Nomination was already registered.

---------
### NotCollator
Not a block producer

---------
### TooManyCandidates
Parachain reached the limit for candidates.

---------
### TooManyInvulnerables
An attempt to set too many invulnerables

---------
### TooManyNominations
Collator has reached max number of nominations

---------