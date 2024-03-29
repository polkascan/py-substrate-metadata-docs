
# Court

---------
## Calls

---------
### appeal
Initiate an appeal for a court
if the presumptive winner of the last vote round is believed to be incorrect.
The last appeal does not trigger a new court round
but instead it marks the court mechanism for this market as failed.
If the court failed, the prediction markets pallet takes over the dispute resolution.
The prediction markets pallet might allow to trigger a global token holder vote.

\# Arguments

- `court_id`: The identifier of the court.

\# Weight

Complexity: It depends heavily on the complexity of `select_participants`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| court_id | `CourtId` | 

#### Python
```python
call = substrate.compose_call(
    'Court', 'appeal', {'court_id': 'u128'}
)
```

---------
### delegate
Join the court to become a delegator.
If the random selection algorithm chooses a delegators stake,
the caller delegates the vote power to the drawn delegated juror.
The delegator gets slashed or rewarded according to the delegated juror&\#x27;s decisions.
If the delegator is already part of the court,
the `amount` needs to be higher than the previous amount to update the delegators stake.
The `amount` of this call represents the total stake of the delegator.
If the pool is full, the lowest staked court participant is removed from the court pool.
If the `amount` is lower than the lowest staked court participant, the call fails.

\# Arguments

- `amount`: The total stake associated with the joining delegator.
- `delegations`: The list of jurors to delegate the vote power to.

\# Weight

Complexity: `O(log(n))`, where `n` is the number of jurors in the stake-weighted pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 
| delegations | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Court', 'delegate', {
    'amount': 'u128',
    'delegations': ['AccountId'],
}
)
```

---------
### denounce_vote
Denounce a juror during the voting period for which the commitment vote is known.
This is useful to punish the behaviour that jurors reveal
their commitments to others before the voting period ends.
A check of `commitment_hash == hash(juror ++ vote_item ++ salt)`
is performed for validation.

\# Arguments

- `court_id`: The identifier of the court.
- `juror`: The juror whose commitment vote might be known.
- `vote_item`: The raw vote item which should match with the commitment of the juror.
- `salt`: The hash which is used to proof that the juror did reveal
her vote during the voting period.

\# Weight

Complexity: `O(log(n))`, where `n` is the number of selected draws
in the specified court.
#### Attributes
| Name | Type |
| -------- | -------- | 
| court_id | `CourtId` | 
| juror | `AccountIdLookupOf<T>` | 
| vote_item | `VoteItem` | 
| salt | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Court', 'denounce_vote', {
    'court_id': 'u128',
    'juror': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'salt': 'scale_info::11',
    'vote_item': {
        'Binary': 'bool',
        'Outcome': {
            'Categorical': 'u16',
            'Scalar': 'u128',
        },
    },
}
)
```

---------
### exit_court
Exit the court.
The stake which is not locked by any court case is unlocked.
`prepare_exit_court` must be called before
to remove the court participant (juror or delegator) from the stake-weighted pool.

\# Arguments

- `court_participant`: The court participant,
who is assumed not to be part of the pool anymore.

\# Weight

Complexity: `O(log(n))`, where `n` is the number of jurors in the stake-weighted pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| court_participant | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Court', 'exit_court', {
    'court_participant': {
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
### join_court
Join to become a juror, who is able to get randomly selected
for court cases according to the provided stake.
If the juror is already part of the court,
the `amount` needs to be higher than the previous amount to update the juror stake.
If the juror gets selected for a court case, the juror has to vote and reveal the vote.
If the juror does not vote or reveal the vote, the juror gets slashed
by the selected multiple of `MinJurorStake` for the court.
The risked amount depends on the juror random selection algorithm,
but is at most (`MaxSelectedDraws` / 2) mulitplied by the `MinJurorStake`
for all jurors and delegators in one court.
Assume you get randomly selected on one of these `MinJurorStake`&\#x27;s.
Then you risk at most `MinJurorStake` for this court.
The probability to get selected is higher the more funds are staked.
The `amount` of this call represents the total stake of the juror.
If the pool is full, the lowest staked court participant is removed from the court pool.
If the `amount` is lower than the lowest staked court participant, the call fails.

\# Arguments

- `amount`: The total stake associated with the joining juror.

\# Weight

Complexity: `O(log(n))`, where `n` is the number of jurors in the stake-weighted pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Court', 'join_court', {'amount': 'u128'}
)
```

---------
### prepare_exit_court
Prepare as a court participant (juror or delegator) to exit the court.
When this is called the court participant is not anymore able to get drawn for new cases.
The court participant gets removed from the stake-weighted pool.
After that the court participant can exit the court.

\# Weight

Complexity: `O(log(n))`, where `n` is the number of jurors in the stake-weighted pool.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Court', 'prepare_exit_court', {}
)
```

---------
### reassign_court_stakes
Reassign the stakes of the jurors and delegators
for the selected draws of the specified court.
The losing jurors and delegators get slashed and
pay for the winning jurors and delegators.
The tardy (juror did not reveal or did not vote) or denounced jurors
and associated delegators get slashed and reward the winners.

\# Arguments

- `court_id`: The identifier of the court.

\# Weight

Complexity: O(N + M), with `N` being the number of draws and `M` being the total number of valid winners and losers.
#### Attributes
| Name | Type |
| -------- | -------- | 
| court_id | `CourtId` | 

#### Python
```python
call = substrate.compose_call(
    'Court', 'reassign_court_stakes', {'court_id': 'u128'}
)
```

---------
### reveal_vote
Reveal the commitment vote of the caller, who is a selected juror.
A check of `commitment_hash == hash(juror ++ vote_item ++ salt)`
is performed for validation.

\# Arguments

- `court_id`: The identifier of the court.
- `vote_item`: The raw vote item which should match with the commitment of the juror.
- `salt`: The hash which is used for the validation.

\# Weight

Complexity: `O(log(n))`, where `n` is the number of selected draws
in the specified court.
#### Attributes
| Name | Type |
| -------- | -------- | 
| court_id | `CourtId` | 
| vote_item | `VoteItem` | 
| salt | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Court', 'reveal_vote', {
    'court_id': 'u128',
    'salt': 'scale_info::11',
    'vote_item': {
        'Binary': 'bool',
        'Outcome': {
            'Categorical': 'u16',
            'Scalar': 'u128',
        },
    },
}
)
```

---------
### set_inflation
Set the yearly inflation rate of the court system.
This is only allowed to be called by the `MonetaryGovernanceOrigin`.

\# Arguments

- `inflation`: The desired yearly inflation rate.

\# Weight

Complexity: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| inflation | `Perbill` | 

#### Python
```python
call = substrate.compose_call(
    'Court', 'set_inflation', {'inflation': 'u32'}
)
```

---------
### vote
Vote as a randomly selected juror for a specific court case.

\# Arguments

- `court_id`: The identifier of the court.
- `commitment_vote`: A hash which consists of `juror ++ vote_item ++ salt`.

\# Weight

Complexity: `O(log(n))`, where `n` is the number of participants
in the list of random selections (draws).
#### Attributes
| Name | Type |
| -------- | -------- | 
| court_id | `CourtId` | 
| commitment_vote | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Court', 'vote', {
    'commitment_vote': 'scale_info::11',
    'court_id': 'u128',
}
)
```

---------
## Events

---------
### CourtAppealed
A market has been appealed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| court_id | `CourtId` | ```u128```
| appeal_info | `AppealOf<T>` | ```{'backer': 'AccountId', 'bond': 'u128', 'appealed_vote_item': {'Outcome': {'Categorical': 'u16', 'Scalar': 'u128'}, 'Binary': 'bool'}}```
| new_round_ends | `Option<RoundTimingOf<T>>` | ```(None, {'pre_vote': 'u64', 'vote': 'u64', 'aggregation': 'u64', 'appeal': 'u64'})```

---------
### CourtOpened
A court case was opened.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| market_id | `MarketIdOf<T>` | ```u128```
| court_info | `CourtOf<T>` | ```{'status': {'Open': None, 'Closed': {'winner': {'Outcome': {'Categorical': 'u16', 'Scalar': 'u128'}, 'Binary': 'bool'}}, 'Reassigned': None}, 'appeals': [{'backer': 'AccountId', 'bond': 'u128', 'appealed_vote_item': {'Outcome': {'Categorical': 'u16', 'Scalar': 'u128'}, 'Binary': 'bool'}}], 'round_ends': {'pre_vote': 'u64', 'vote': 'u64', 'aggregation': 'u64', 'appeal': 'u64'}, 'vote_item_type': ('Outcome', 'Binary')}```

---------
### DelegatorJoined
A delegator has delegated their stake to jurors.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```AccountId```
| stake | `BalanceOf<T>` | ```u128```
| delegated_jurors | `Vec<T::AccountId>` | ```['AccountId']```

---------
### DenouncedJurorVote
A juror vote has been denounced.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| denouncer | `T::AccountId` | ```AccountId```
| juror | `T::AccountId` | ```AccountId```
| court_id | `CourtId` | ```u128```
| vote_item | `VoteItem` | ```{'Outcome': {'Categorical': 'u16', 'Scalar': 'u128'}, 'Binary': 'bool'}```
| salt | `T::Hash` | ```scale_info::11```

---------
### ExitPrepared
A court participant prepared to exit the court.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| court_participant | `T::AccountId` | ```AccountId```

---------
### ExitedCourt
A court participant has been removed from the court.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| court_participant | `T::AccountId` | ```AccountId```
| exit_amount | `BalanceOf<T>` | ```u128```
| active_lock | `BalanceOf<T>` | ```u128```

---------
### InflationSet
The yearly inflation rate has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| inflation | `Perbill` | ```u32```

---------
### JurorJoined
A juror has been added to the court.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| juror | `T::AccountId` | ```AccountId```
| stake | `BalanceOf<T>` | ```u128```

---------
### JurorRevealedVote
A juror has revealed their vote.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| juror | `T::AccountId` | ```AccountId```
| court_id | `CourtId` | ```u128```
| vote_item | `VoteItem` | ```{'Outcome': {'Categorical': 'u16', 'Scalar': 'u128'}, 'Binary': 'bool'}```
| salt | `T::Hash` | ```scale_info::11```
| slashable_amount | `BalanceOf<T>` | ```u128```
| draw_weight | `u32` | ```u32```

---------
### JurorVoted
A juror has voted in a court.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| court_id | `CourtId` | ```u128```
| juror | `T::AccountId` | ```AccountId```
| commitment | `T::Hash` | ```scale_info::11```

---------
### MintedInCourt
A new token amount was minted for a court participant.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| court_participant | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### StakesReassigned
The juror and delegator stakes have been reassigned. The losing jurors have been slashed.
The winning jurors have been rewarded by the losers.
The losing jurors are those, who did not vote,
were denounced or did not reveal their vote.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| court_id | `CourtId` | ```u128```

---------
## Storage functions

---------
### CourtIdToMarketId
 Mapping from court id to market id.

#### Python
```python
result = substrate.query(
    'Court', 'CourtIdToMarketId', ['u128']
)
```

#### Return value
```python
'u128'
```
---------
### CourtPool
 The pool of jurors and delegators who can get randomly selected according to their stake.
 The pool is sorted by `stake` in ascending order [min, ..., max].

#### Python
```python
result = substrate.query(
    'Court', 'CourtPool', []
)
```

#### Return value
```python
[
    {
        'consumed_stake': 'u128',
        'court_participant': 'AccountId',
        'joined_at': 'u64',
        'stake': 'u128',
    },
]
```
---------
### Courts
 The general information about each court.

#### Python
```python
result = substrate.query(
    'Court', 'Courts', ['u128']
)
```

#### Return value
```python
{
    'appeals': [
        {
            'appealed_vote_item': {
                'Binary': 'bool',
                'Outcome': {'Categorical': 'u16', 'Scalar': 'u128'},
            },
            'backer': 'AccountId',
            'bond': 'u128',
        },
    ],
    'round_ends': {
        'aggregation': 'u64',
        'appeal': 'u64',
        'pre_vote': 'u64',
        'vote': 'u64',
    },
    'status': {
        'Closed': {
            'winner': {
                'Binary': 'bool',
                'Outcome': {'Categorical': 'u16', 'Scalar': 'u128'},
            },
        },
        'Open': None,
        'Reassigned': None,
    },
    'vote_item_type': ('Outcome', 'Binary'),
}
```
---------
### MarketIdToCourtId
 Mapping from market id to court id.

#### Python
```python
result = substrate.query(
    'Court', 'MarketIdToCourtId', ['u128']
)
```

#### Return value
```python
'u128'
```
---------
### NextCourtId
 The next identifier for a new court.

#### Python
```python
result = substrate.query(
    'Court', 'NextCourtId', []
)
```

#### Return value
```python
'u128'
```
---------
### Participants
 The general information about each juror and delegator.

#### Python
```python
result = substrate.query(
    'Court', 'Participants', ['AccountId']
)
```

#### Return value
```python
{
    'active_lock': 'u128',
    'delegations': (None, ['AccountId']),
    'prepare_exit_at': (None, 'u64'),
    'stake': 'u128',
}
```
---------
### RequestBlock
 The future block number when jurors should start voting.
 This is useful for the user experience of the jurors to vote for multiple courts at once.

#### Python
```python
result = substrate.query(
    'Court', 'RequestBlock', []
)
```

#### Return value
```python
'u64'
```
---------
### SelectedDraws
 The randomly selected jurors and delegators, their vote weight,
 the status about their vote and their selected and risked funds.

#### Python
```python
result = substrate.query(
    'Court', 'SelectedDraws', ['u128']
)
```

#### Return value
```python
[
    {
        'court_participant': 'AccountId',
        'slashable': 'u128',
        'vote': {
            'Delegated': {'delegated_stakes': [('AccountId', 'u128')]},
            'Denounced': {
                'commitment': 'scale_info::11',
                'salt': 'scale_info::11',
                'vote_item': {'Binary': 'bool', 'Outcome': 'scale_info::68'},
            },
            'Drawn': None,
            'Revealed': {
                'commitment': 'scale_info::11',
                'salt': 'scale_info::11',
                'vote_item': {'Binary': 'bool', 'Outcome': 'scale_info::68'},
            },
            'Secret': {'commitment': 'scale_info::11'},
        },
        'weight': 'u32',
    },
]
```
---------
### SelectionNonce
 An extra layer of pseudo randomness so that we can generate a new random seed with it.

#### Python
```python
result = substrate.query(
    'Court', 'SelectionNonce', []
)
```

#### Return value
```python
'u64'
```
---------
### YearlyInflation
 The current inflation rate.

#### Python
```python
result = substrate.query(
    'Court', 'YearlyInflation', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### AggregationPeriod
 The time in which the jurors should reveal their commitment vote.
#### Value
```python
21600
```
#### Python
```python
constant = substrate.get_constant('Court', 'AggregationPeriod')
```
---------
### AppealBond
 The required base bond in order to get an appeal initiated.
 This bond increases exponentially with the number of appeals.
#### Value
```python
20000000000000
```
#### Python
```python
constant = substrate.get_constant('Court', 'AppealBond')
```
---------
### AppealPeriod
 The time in which a court case can get appealed.
#### Value
```python
7200
```
#### Python
```python
constant = substrate.get_constant('Court', 'AppealPeriod')
```
---------
### BlocksPerYear
 The expected blocks per year to calculate the inflation emission.
#### Value
```python
2629800
```
#### Python
```python
constant = substrate.get_constant('Court', 'BlocksPerYear')
```
---------
### InflationPeriod
 The inflation period in which new tokens are minted.
#### Value
```python
216000
```
#### Python
```python
constant = substrate.get_constant('Court', 'InflationPeriod')
```
---------
### LockId
 The court lock identifier.
#### Value
```python
'0x7a67652f636f6c6b'
```
#### Python
```python
constant = substrate.get_constant('Court', 'LockId')
```
---------
### MaxAppeals
 The maximum number of appeals until a court fails.
#### Value
```python
4
```
#### Python
```python
constant = substrate.get_constant('Court', 'MaxAppeals')
```
---------
### MaxCourtParticipants
 The maximum number of jurors and delegators that can be registered.
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('Court', 'MaxCourtParticipants')
```
---------
### MaxDelegations
 The maximum number of possible delegations.
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Court', 'MaxDelegations')
```
---------
### MaxSelectedDraws
 The maximum number of randomly selected n * `MinJurorStake` (n equals all draw weights)
 out of all jurors and delegators stake. This configuration parameter should be
 the maximum necessary_draws_weight multiplied by 2.
 Each `MinJurorStake` (draw weight) out of `n * MinJurorStake` belongs
 to one juror or one delegator.
 (necessary_draws_weight = 2^(appeals_len) * 31 + 2^(appeals_len) - 1)
 Assume MaxAppeals - 1 (= 3), example: 2^3 * 31 + 2^3 - 1 = 255
 =&gt; 2 * 255 = 510 = `MaxSelectedDraws`.
 Why the multiplication by two?
 Because each draw weight is associated with one juror account id and
 potentially a delegator account id.
#### Value
```python
510
```
#### Python
```python
constant = substrate.get_constant('Court', 'MaxSelectedDraws')
```
---------
### MaxYearlyInflation
 The maximum yearly inflation rate.
#### Value
```python
100000000
```
#### Python
```python
constant = substrate.get_constant('Court', 'MaxYearlyInflation')
```
---------
### MinJurorStake
 The minimum stake a user needs to lock to become a juror.
#### Value
```python
5000000000000
```
#### Python
```python
constant = substrate.get_constant('Court', 'MinJurorStake')
```
---------
### PalletId
 Identifier of this pallet
#### Value
```python
'0x7a67652f636f7574'
```
#### Python
```python
constant = substrate.get_constant('Court', 'PalletId')
```
---------
### RequestInterval
 The global interval which schedules the start of new court vote periods.
#### Value
```python
50400
```
#### Python
```python
constant = substrate.get_constant('Court', 'RequestInterval')
```
---------
### TreasuryPalletId
 The treasury pallet identifier.
#### Value
```python
'0x7a67652f74737279'
```
#### Python
```python
constant = substrate.get_constant('Court', 'TreasuryPalletId')
```
---------
### VotePeriod
 The time in which the jurors can cast their commitment vote.
#### Value
```python
21600
```
#### Python
```python
constant = substrate.get_constant('Court', 'VotePeriod')
```
---------
## Errors

---------
### AlreadyPreparedExit
In order to exit the court the juror has to exit
the pool first with `prepare_exit_court`.

---------
### AmountBelowLastJoin
After the first join of the court the amount has to be equal or higher than the current stake.
This is to ensure the slashable amount in active court rounds
is still smaller or equal to the stake.
It is also necessary to calculate the `unconsumed` stake properly.
Otherwise a juror could just reduce the probability to get selected whenever they want.
But this has to be done by `prepare_exit_court` and `exit_court`.
Additionally, the `join_court` and `delegate` extrinsics
use `extend_lock` and not `set_lock` or `remove_lock`.
This means those extrinsics are not meant to get out, but only to get into the court.

---------
### AmountBelowLowestJuror
The amount is too low to kick the lowest juror out of the stake-weighted pool.

---------
### AmountExceedsBalance
The caller has not enough funds to join the court with the specified amount.

---------
### AppealBondExceedsBalance
The callers balance is lower than the appeal bond.

---------
### AppealedVoteItemIsNoOutcome
The appealed vote item is not an outcome.

---------
### BelowMinJurorStake
The amount is below the minimum required stake.

---------
### CallerDenouncedItself
A juror tried to denounce herself.

---------
### CallerIsNotACourtParticipant
This operation requires the caller to be a juror or delegator.

---------
### CallerNotInSelectedDraws
The caller of this function is not part of the juror draws.

---------
### CommitmentHashMismatch
The vote item and salt reveal do not match the commitment vote.

---------
### CourtAlreadyReassigned
The juror stakes of the court already got reassigned.

---------
### CourtIdToMarketIdNotFound
The court id to market id mapping was not found.

---------
### CourtNotClosed
The court is not in the closed state.

---------
### CourtNotFound
No court for this market id was found.

---------
### CourtParticipantTwiceInPool
This should not happen, because the juror account should only be once in a pool.

---------
### DelegatedToInvalidJuror
The set of delegations should contain only valid and active juror accounts.

---------
### IdenticalDelegationsNotAllowed
The set of delegations has to be distinct.

---------
### InflationExceedsMaxYearlyInflation
The inflation rate is too high.

---------
### InvalidVoteItemForBinaryCourt
The vote item is not valid for this (binary) court.

---------
### InvalidVoteItemForOutcomeCourt
The vote item is not valid for this (outcome) court.

---------
### InvalidVoteState
The caller of this extrinsic needs to be drawn or in the commitment vote state.

---------
### JurorDelegated
The juror decided to be a delegator.

---------
### JurorDidNotVote
The juror was drawn but did not manage to commitmently vote within the court.

---------
### JurorDoesNotExist
An account id does not exist on the jurors storage.

---------
### JurorNotDrawn
The juror was not randomly selected for the court.

---------
### MarketDoesNotHaveCourtMechanism
On dispute or resolution, someone tried to pass a non-court market type.

---------
### MarketIdToCourtIdNotFound
The market id to court id mapping was not found.

---------
### MarketIsNotDisputed
The market is not in a state where it can be disputed.

---------
### MarketReportNotFound
The report of the market was not found.

---------
### MaxAppealsReached
The maximum number of appeals has been reached.

---------
### MaxCourtIdReached
The maximum number of court ids is reached.

---------
### MaxCourtParticipantsReached
The maximum number of possible jurors has been reached.

---------
### MaxDelegationsReached
The maximum number of delegations is reached for this account.

---------
### NoDelegations
The call to `delegate` is not valid if no delegations are provided.

---------
### NotEnoughJurorsAndDelegatorsStake
There are not enough jurors in the pool.

---------
### NotInAggregationPeriod
This operation is only allowed in the aggregation period.

---------
### NotInAppealPeriod
This operation is only allowed in the appeal period.

---------
### NotInVotingPeriod
This operation is only allowed in the voting period.

---------
### OutcomeMismatch
The outcome does not match the market outcomes.

---------
### PrematureExit
The juror should at least wait one inflation period after the funds can be unstaked.
Otherwise hopping in and out for inflation rewards is possible.

---------
### PrepareExitAtNotPresent
The `prepare_exit_at` field is not present.

---------
### SelfDelegationNotAllowed
A delegation to the own account is not possible.

---------
### Unexpected
Action cannot be completed because an unexpected error has occurred. This should be
reported to protocol maintainers.

---------
### VoteAlreadyDenounced
The juror was already denounced.

---------
### VoteAlreadyRevealed
The vote is not commitment.

---------
### VoteItemIsNoOutcome
The vote item was expected to be an outcome, but is actually not an outcome.

---------
### WinnerVoteItemIsNoOutcome
The winner vote item is not an outcome.

---------