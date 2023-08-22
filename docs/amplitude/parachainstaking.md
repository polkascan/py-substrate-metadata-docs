
# ParachainStaking

---------
## Calls

---------
### cancel_leave_candidates
Revert the previously requested exit of the network of a collator
candidate. On success, adds back the candidate to the TopCandidates
and updates the collators.

Requires the candidate to previously have called
`init_leave_candidates`.

Emits `CollatorCanceledExit`.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'cancel_leave_candidates', {}
)
```

---------
### candidate_stake_less
Stake less funds for a collator candidate.

If the new amount of staked fund is not large enough, the account
could be removed from the set of collator candidates and not be
considered for authoring the next blocks.

This operation affects the pallet&\#x27;s total stake amount.

The unstaked funds are not released immediately to the account, but
they will be available after `StakeDuration` blocks.

The resulting total amount of funds staked must be within the
allowed range as set in the pallet&\#x27;s configuration.

Emits `CollatorStakedLess`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| less | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'candidate_stake_less', {'less': 'u128'}
)
```

---------
### candidate_stake_more
Stake more funds for a collator candidate.

If not in the set of candidates, staking enough funds allows the
account to be added to it. The larger amount of funds, the higher
chances to be selected as the author of the next block.

This operation affects the pallet&\#x27;s total stake amount.

The resulting total amount of funds staked must be within the
allowed range as set in the pallet&\#x27;s configuration.

Emits `CollatorStakedMore`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| more | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'candidate_stake_more', {'more': 'u128'}
)
```

---------
### claim_rewards
Claim block authoring rewards for the target address.

Requires `Rewards` to be set beforehand, which can by triggered by
any of the following options
* Calling increment_{collator, delegator}_rewards (active)
* Altering your stake (active)
* Leaving the network as a collator (active)
* Revoking a delegation as a delegator (active)
* Being a delegator whose collator left the network, altered their
  stake or incremented rewards (passive)

The dispatch origin can be any signed one, e.g., anyone can claim
for anyone.

Emits `Rewarded`.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'claim_rewards', {}
)
```

---------
### delegator_stake_less
Reduce the stake for delegating a collator candidate.

If the new amount of staked fund is not large enough, the collator
could be removed from the set of collator candidates and not be
considered for authoring the next blocks.

The unstaked funds are not release immediately to the account, but
they will be available after `StakeDuration` blocks.

The remaining staked funds must still be larger than the minimum
required by this pallet to maintain the status of delegator.

The resulting total amount of funds staked must be within the
allowed range as set in the pallet&\#x27;s configuration.

Emits `DelegatorStakedLess`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `<T::Lookup as StaticLookup>::Source` | 
| less | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'delegator_stake_less', {
    'candidate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'less': 'u128',
}
)
```

---------
### delegator_stake_more
Increase the stake for delegating a collator candidate.

If not in the set of candidates, staking enough funds allows the
collator candidate to be added to it.

Emits `DelegatorStakedMore`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `<T::Lookup as StaticLookup>::Source` | 
| more | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'delegator_stake_more', {
    'candidate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'more': 'u128',
}
)
```

---------
### execute_leave_candidates
Execute the network exit of a candidate who requested to leave at
least `ExitQueueDelay` rounds ago. Prepares unstaking of the
candidates and their delegators stake which can be unlocked via
`unlock_unstaked` after waiting at least `StakeDuration` many
blocks.

Requires the candidate to previously have called
`init_leave_candidates`.

The exit request can be reversed by calling
`cancel_leave_candidates`.

NOTE: Iterates over CandidatePool for each candidate over their
delegators to set rewards. Needs to be improved when scaling up
`MaxTopCandidates`.

Emits `CollatorLeft`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collator | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'execute_leave_candidates', {
    'collator': {
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
### execute_scheduled_reward_change
Executes the annual reduction of the reward rates for collators and
delegators. Moreover, sets rewards for all collators and delegators
before adjusting the inflation.

Emits `RoundInflationSet`.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'execute_scheduled_reward_change', {}
)
```

---------
### force_new_round
Forces the start of the new round in the next block.

The new round will be enforced via &lt;T as
ShouldEndSession&lt;_&gt;&gt;::should_end_session.

The dispatch origin must be Root.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'force_new_round', {}
)
```

---------
### force_remove_candidate
Forcedly removes a collator candidate from the TopCandidates and
clears all associated storage for the candidate and their
delegators.

Prepares unstaking of the candidates and their delegators stake
which can be unlocked via `unlock_unstaked` after waiting at
least `StakeDuration` many blocks. Also increments rewards for the
collator and their delegators.

Increments rewards of candidate and their delegators.

Emits `CandidateRemoved`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collator | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'force_remove_candidate', {
    'collator': {
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
### increment_collator_rewards
Actively increment the rewards of a collator and their delegators.

The same effect is triggered by changing the stake or leaving the
network.

The dispatch origin must be a collator.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'increment_collator_rewards', {}
)
```

---------
### increment_delegator_rewards
Actively increment the rewards of a delegator for all their
delegations.

The same effect is triggered by changing the stake or revoking
delegations.

The dispatch origin must be a delegator.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'increment_delegator_rewards', {}
)
```

---------
### init_leave_candidates
Request to leave the set of collator candidates.

On success, the account is immediately removed from the candidate
pool to prevent selection as a collator in future validation rounds,
but unstaking of the funds is executed with a delay of
`StakeDuration` blocks.

The exit request can be reversed by calling
`cancel_leave_candidates`.

This operation affects the pallet&\#x27;s total stake amount. It is
updated even though the funds of the candidate who signaled to leave
are still locked for `ExitDelay` + `StakeDuration` more blocks.

NOTE 1: Upon starting a new session_i in `new_session`, the current
top candidates are selected to be block authors for session_i+1. Any
changes to the top candidates afterwards do not effect the set of
authors for session_i+1.
Thus, we have to make sure none of these collators can
leave before session_i+1 ends by delaying their
exit for `ExitDelay` many blocks.

NOTE 2: We do not increment rewards in this extrinsic as the
candidate could still author blocks, and thus be eligible to receive
rewards, until the end of the next session.

Emits `CollatorScheduledExit`.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'init_leave_candidates', {}
)
```

---------
### join_candidates
Join the set of collator candidates.

In the next blocks, if the collator candidate has enough funds
staked to be included in any of the top `MaxSelectedCandidates`
positions, it will be included in the set of potential authors that
will be selected by the stake-weighted random selection function.

The staked funds of the new collator candidate are added to the
total stake of the system.

The total amount of funds staked must be within the allowed range as
set in the pallet&\#x27;s configuration.

The dispatch origin must not be already part of the collator
candidates nor of the delegators set.

Emits `JoinedCollatorCandidates`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| stake | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'join_candidates', {'stake': 'u128'}
)
```

---------
### join_delegators
Join the set of delegators by delegating to a collator candidate.

The account that wants to delegate cannot be part of the collator
candidates set as well.

The caller must _not_ have a delegation. If that is the case, they
are required to first remove the delegation.

The amount staked must be larger than the minimum required to become
a delegator as set in the pallet&\#x27;s configuration.

As only `MaxDelegatorsPerCollator` are allowed to delegate a given
collator, the amount staked must be larger than the lowest one in
the current set of delegator for the operation to be meaningful.

The collator&\#x27;s total stake as well as the pallet&\#x27;s total stake are
increased accordingly.

Emits `Delegation`.
Emits `DelegationReplaced` if the candidate has
`MaxDelegatorsPerCollator` many delegations but this delegator
staked more than one of the other delegators of this candidate.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collator | `<T::Lookup as StaticLookup>::Source` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'join_delegators', {
    'amount': 'u128',
    'collator': {
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
### leave_delegators
Leave the set of delegators and, by implication, revoke the ongoing
delegation.

All staked funds are not unlocked immediately, but they are added to
the queue of pending unstaking, and will effectively be released
after `StakeDuration` blocks from the moment the delegator leaves.

This operation reduces the total stake of the pallet as well as the
stakes of all collators that were delegated, potentially affecting
their chances to be included in the set of candidates in the next
rounds.

Automatically increments the accumulated rewards of the origin of
the current delegation.

Emits `DelegatorLeft`.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'leave_delegators', {}
)
```

---------
### set_blocks_per_round
Set the number of blocks each validation round lasts.

If the new value is less than the length of the current round, the
system will immediately move to the next round in the next block.

The new value must be higher than the minimum allowed as set in the
pallet&\#x27;s configuration.

The dispatch origin must be Root.

Emits `BlocksPerRoundSet`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'set_blocks_per_round', {'new': 'u32'}
)
```

---------
### set_inflation
Set the annual inflation rate to derive per-round inflation.

The inflation details are considered valid if the annual reward rate
is approximately the per-block reward rate multiplied by the
estimated* total number of blocks per year.

The estimated average block time is twelve seconds.

NOTE: Iterates over CandidatePool for each candidate over their
delegators to set rewards. Needs to be improved when scaling up
`MaxTopCandidates`.

The dispatch origin must be Root.

Emits `RoundInflationSet`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collator_max_rate_percentage | `Perquintill` | 
| collator_annual_reward_rate_percentage | `Perquintill` | 
| delegator_max_rate_percentage | `Perquintill` | 
| delegator_annual_reward_rate_percentage | `Perquintill` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'set_inflation', {
    'collator_annual_reward_rate_percentage': 'u64',
    'collator_max_rate_percentage': 'u64',
    'delegator_annual_reward_rate_percentage': 'u64',
    'delegator_max_rate_percentage': 'u64',
}
)
```

---------
### set_max_candidate_stake
Set the maximal amount a collator can stake. Existing stakes are not
changed.

The dispatch origin must be Root.

Emits `MaxCandidateStakeChanged`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'set_max_candidate_stake', {'new': 'u128'}
)
```

---------
### set_max_selected_candidates
Set the maximum number of collator candidates that can be selected
at the beginning of each validation round.

Changes are not applied until the start of the next round.

The new value must be higher than the minimum allowed as set in the
pallet&\#x27;s configuration.

The dispatch origin must be Root.

Emits `MaxSelectedCandidatesSet`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'set_max_selected_candidates', {'new': 'u32'}
)
```

---------
### unlock_unstaked
Unlock all previously staked funds that are now available for
unlocking by the origin account after `StakeDuration` blocks have
elapsed.

Weight: O(U) where U is the number of locked unstaking requests
bounded by `MaxUnstakeRequests`.
- Reads: [Origin Account], Unstaking, Locks
- Writes: Unstaking, Locks
- Kills: Unstaking &amp; Locks if no balance is locked anymore
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'unlock_unstaked', {
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
## Events

---------
### BlocksPerRoundSet
The length in blocks for future validation rounds has changed.
\[round number, first block in the current round, old value, new
value\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SessionIndex` | ```u32```
| None | `T::BlockNumber` | ```u32```
| None | `T::BlockNumber` | ```u32```
| None | `T::BlockNumber` | ```u32```

---------
### CandidateLeft
An account has left the set of collator candidates.
\[account, amount of funds un-staked\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### CollatorCanceledExit
A collator candidate has canceled the process to leave the set of
candidates and was added back to the candidate pool. \[collator&\#x27;s
account\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### CollatorRemoved
An account was forcedly removed from the  set of collator
candidates. \[account, amount of funds un-staked\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### CollatorScheduledExit
A collator candidate has started the process to leave the set of
candidates. \[round number, collator&\#x27;s account, round number when
the collator will be effectively removed from the set of
candidates\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SessionIndex` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `SessionIndex` | ```u32```

---------
### CollatorStakedLess
A collator candidate has decreased the amount of funds at stake.
\[collator&\#x27;s account, previous stake, new stake\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### CollatorStakedMore
A collator candidate has increased the amount of funds at stake.
\[collator&\#x27;s account, previous stake, new stake\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### Delegation
An account has delegated a new collator candidate.
\[account, amount of funds staked, total amount of delegators&\#x27; funds
staked for the collator candidate\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### DelegationReplaced
A new delegation has replaced an existing one in the set of ongoing
delegations for a collator candidate. \[new delegator&\#x27;s account,
amount of funds staked in the new delegation, replaced delegator&\#x27;s
account, amount of funds staked in the replace delegation, collator
candidate&\#x27;s account, new total amount of delegators&\#x27; funds staked
for the collator candidate\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### DelegatorLeft
An account has left the set of delegators.
\[account, amount of funds un-staked\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### DelegatorLeftCollator
An account has stopped delegating a collator candidate.
\[account, collator candidate&\#x27;s account, old amount of delegators&\#x27;
funds staked, new amount of delegators&\#x27; funds staked\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### DelegatorStakedLess
A delegator has decreased the amount of funds at stake for a
collator. \[delegator&\#x27;s account, collator&\#x27;s account, previous
delegation stake, new delegation stake\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### DelegatorStakedMore
A delegator has increased the amount of funds at stake for a
collator. \[delegator&\#x27;s account, collator&\#x27;s account, previous
delegation stake, new delegation stake\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### EnteredTopCandidates
A new account has joined the set of top candidates.
\[account\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### JoinedCollatorCandidates
A new account has joined the set of collator candidates.
\[account, amount staked by the new candidate\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### LeftTopCandidates
An account was removed from the set of top candidates.
\[account\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### MaxCandidateStakeChanged
The maximum candidate stake has been changed.
\[new max amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T>` | ```u128```

---------
### MaxSelectedCandidatesSet
The maximum number of collator candidates selected in future
validation rounds has changed. \[old value, new value\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```
| None | `u32` | ```u32```

---------
### NewRound
A new staking round has started.
\[block number, round number\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```
| None | `SessionIndex` | ```u32```

---------
### Rewarded
A collator or a delegator has received a reward.
\[account, amount of reward\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### RoundInflationSet
Inflation configuration for future validation rounds has changed.
\[maximum collator&\#x27;s staking rate, maximum collator&\#x27;s reward rate,
maximum delegator&\#x27;s staking rate, maximum delegator&\#x27;s reward rate\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Perquintill` | ```u64```
| None | `Perquintill` | ```u64```
| None | `Perquintill` | ```u64```
| None | `Perquintill` | ```u64```

---------
## Storage functions

---------
### CandidatePool
 The staking information for a candidate.

 It maps from an account to its information.
 Moreover, it counts the number of candidates.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'CandidatePool', ['AccountId']
)
```

#### Return value
```python
{
    'delegators': [{'amount': 'u128', 'owner': 'AccountId'}],
    'id': 'AccountId',
    'stake': 'u128',
    'status': {'Active': None, 'Leaving': 'u32'},
    'total': 'u128',
}
```
---------
### CounterForCandidatePool
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'CounterForCandidatePool', []
)
```

#### Return value
```python
'u32'
```
---------
### DelegatorState
 Delegation staking information.

 It maps from an account to its delegation details.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'DelegatorState', ['AccountId']
)
```

#### Return value
```python
{'amount': 'u128', 'owner': (None, 'AccountId')}
```
---------
### ForceNewRound

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'ForceNewRound', []
)
```

#### Return value
```python
'bool'
```
---------
### InflationConfig
 Inflation configuration.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'InflationConfig', []
)
```

#### Return value
```python
{
    'collator': {
        'max_rate': 'u64',
        'reward_rate': {'annual': 'u64', 'per_block': 'u64'},
    },
    'delegator': {
        'max_rate': 'u64',
        'reward_rate': {'annual': 'u64', 'per_block': 'u64'},
    },
}
```
---------
### LastDelegation
 Delegation information for the latest session in which a delegator
 delegated.

 It maps from an account to the number of delegations in the last
 session in which they (re-)delegated.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'LastDelegation', ['AccountId']
)
```

#### Return value
```python
{'counter': 'u32', 'round': 'u32'}
```
---------
### LastRewardReduction
 The year in which the last automatic reduction of the reward rates
 occurred.

 It starts at zero at genesis and increments by one every BLOCKS_PER_YEAR
 many blocks.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'LastRewardReduction', []
)
```

#### Return value
```python
'u32'
```
---------
### MaxCollatorCandidateStake
 The maximum amount a collator candidate can stake.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'MaxCollatorCandidateStake', []
)
```

#### Return value
```python
'u128'
```
---------
### MaxSelectedCandidates
 The maximum number of collator candidates selected at each round.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'MaxSelectedCandidates', []
)
```

#### Return value
```python
'u32'
```
---------
### RewardCount
 The counter of accumulated rewards for an account.

 For collators, it reflects the number of authored blocks since the last
 reward raise. Thus, everytime a collator authors a block, the
 counter is increased. It is reset, when the collator increments their
 rewards.

 For delegators, it is used to determine the difference between the
 delegator and corresponding collator when incrementing the delegator&#x27;s
 rewards. In this case, the counter is never incremented but reset to the
 collator one when the delegator reward increment happens.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'RewardCount', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### Rewards
 The accumulated rewards for collator candidates and delegators.

 It maps from accounts to their total rewards since the last payout.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'Rewards', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### Round
 Current round number and next round scheduled transition.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'Round', []
)
```

#### Return value
```python
{'current': 'u32', 'first': 'u32', 'length': 'u32'}
```
---------
### TopCandidates
 The collator candidates with the highest amount of stake.

 Each time the stake of a collator is increased, it is checked whether
 this pushes another candidate out of the list. When the stake is
 reduced however, it is not checked if another candidate has more stake,
 since this would require iterating over the entire [CandidatePool].

 There must always be more candidates than [MaxSelectedCandidates] so
 that a collator can drop out of the collator set by reducing their
 stake.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'TopCandidates', []
)
```

#### Return value
```python
[{'amount': 'u128', 'owner': 'AccountId'}]
```
---------
### TotalCollatorStake
 Total funds locked to back the currently selected collators.
 The sum of all collator and their delegator stakes.

 Note: There are more funds locked by this pallet, since the backing for
 non collating candidates is not included in [TotalCollatorStake].

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'TotalCollatorStake', []
)
```

#### Return value
```python
{'collators': 'u128', 'delegators': 'u128'}
```
---------
### Unstaking
 The funds waiting to be unstaked.

 It maps from accounts to all the funds addressed to them in the future
 blocks.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'Unstaking', ['AccountId']
)
```

#### Return value
```python
'scale_info::445'
```
---------
## Constants

---------
### CollatorRewardRateDecay
 The annual decay rate of the collator rewards
#### Value
```python
936879853200000000
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'CollatorRewardRateDecay')
```
---------
### DefaultBlocksPerRound
 Default number of blocks validation rounds last, as set in the
 genesis configuration.
#### Value
```python
600
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'DefaultBlocksPerRound')
```
---------
### ExitQueueDelay
 Number of rounds a collator has to stay active after submitting a
 request to leave the set of collator candidates.
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'ExitQueueDelay')
```
---------
### MaxDelegationsPerRound
 Maximum number of delegations which can be made within the same
 round.

 NOTE: To prevent re-delegation-reward attacks, we should keep this
 to be one.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MaxDelegationsPerRound')
```
---------
### MaxDelegatorsPerCollator
 Maximum number of delegators a single collator can have.
#### Value
```python
40
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MaxDelegatorsPerCollator')
```
---------
### MaxTopCandidates
 Maximum size of the top candidates set.
#### Value
```python
40
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MaxTopCandidates')
```
---------
### MaxUnstakeRequests
 Max number of concurrent active unstaking requests before
 unlocking.

 NOTE: To protect against irremovability of a candidate or delegator,
 we only allow for MaxUnstakeRequests - 1 many manual unstake
 requests. The last one serves as a placeholder for the cases of
 calling either `kick_delegator`, force_remove_candidate` or
 `execute_leave_candidates`. Otherwise, a user could max out their
 unstake requests and prevent themselves from being kicked from the
 set of candidates/delegators until they unlock their funds.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MaxUnstakeRequests')
```
---------
### MinBlocksPerRound
 Minimum number of blocks validation rounds can last.
#### Value
```python
300
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MinBlocksPerRound')
```
---------
### MinCollatorCandidateStake
 Minimum stake required for any account to be added to the set of
 candidates.
#### Value
```python
5000000000000000
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MinCollatorCandidateStake')
```
---------
### MinCollatorStake
 Minimum stake required for any account to be elected as validator
 for a round.
#### Value
```python
5000000000000000
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MinCollatorStake')
```
---------
### MinCollators
 Minimum number of collators selected from the set of candidates at
 every validation round.
#### Value
```python
8
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MinCollators')
```
---------
### MinDelegatorStake
 Minimum stake required for any account to become a delegator.
#### Value
```python
10000000000000
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MinDelegatorStake')
```
---------
### MinRequiredCollators
 Minimum number of collators which cannot leave the network if there
 are no others.
#### Value
```python
4
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MinRequiredCollators')
```
---------
### NetworkRewardRate
 The rate in percent for the network rewards which are based on the
 maximum number of collators and the maximum amount a collator can
 stake.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'NetworkRewardRate')
```
---------
### NetworkRewardStart
 The starting block number for the network rewards. Once the current
 block number exceeds this start, the beneficiary will receive the
 configured reward in each block.
#### Value
```python
4294967295
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'NetworkRewardStart')
```
---------
### StakeDuration
 Number of blocks for which unstaked balance will still be locked
 before it can be unlocked by actively calling the extrinsic
 `unlock_unstaked`.
#### Value
```python
50400
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'StakeDuration')
```
---------
## Errors

---------
### AlreadyDelegatedCollator
The delegator has already previously delegated the collator
candidate.

---------
### AlreadyDelegating
The account is already delegating the collator candidate.

---------
### AlreadyLeaving
The collator candidate has already trigger the process to leave the
set of collator candidates.

---------
### CandidateExists
The account is already part of the collator candidates set.

---------
### CandidateNotFound
The account is not part of the collator candidates set.

---------
### CannotDelegateIfLeaving
The collator candidate is in the process of leaving the set of
candidates and thus cannot be delegated to.

---------
### CannotJoinBeforeUnlocking
The account has a full list of unstaking requests and needs to
unlock at least one of these before being able to join (again).
NOTE: Can only happen if the account was a candidate or
delegator before and either got kicked or exited voluntarily.

---------
### CannotLeaveYet
The collator tried to leave before waiting at least for
`ExitQueueDelay` many rounds.

---------
### CannotSetAboveMax
The number of selected candidates per staking round is
above the maximum value allowed.

---------
### CannotSetBelowMin
The number of selected candidates per staking round is
below the minimum value allowed.

---------
### CannotStakeIfLeaving
The collator candidate is in the process of leaving the set of
candidates and cannot perform any other actions in the meantime.

---------
### DelegationBelowMin
The account has not staked enough funds to delegate a collator
candidate.

---------
### DelegationNotFound
The given delegation does not exist in the set of delegations.

---------
### DelegationsPerRoundExceeded
The delegator has exceeded the number of delegations per round which
is equal to MaxDelegatorsPerCollator.

This protects against attacks in which a delegator can re-delegate
from a collator who has already authored a block, to another one
which has not in this round.

---------
### DelegatorExists
The account is already part of the delegators set.

---------
### DelegatorNotFound
The account is not part of the delegators set.

---------
### InvalidSchedule
An invalid inflation configuration is trying to be set.

---------
### MaxCollatorsPerDelegatorExceeded
The delegator has already delegated the maximum number of candidates
allowed.

---------
### NoMoreUnstaking
The staking reward being unlocked does not exist.
Max unlocking requests reached.

---------
### NotLeaving
The collator candidate wanted to execute the exit but has not
requested to leave before by calling `init_leave_candidates`.

---------
### NotYetDelegating
The account has not delegated any collator candidate yet, hence it
is not in the set of delegators.

---------
### RewardsNotFound
Cannot claim rewards if empty.

---------
### StakeNotFound
Provided staked value is zero. Should never be thrown.

---------
### TooEarly
The reward rate cannot be adjusted yet as an entire year has not
passed.

---------
### TooFewCollatorCandidates
The set of collator candidates would fall below the required minimum
if the collator left.

---------
### TooManyDelegators
The collator candidate has already reached the maximum number of
delegators.

This error is generated in case a new delegation request does not
stake enough funds to replace some other existing delegation.

---------
### Underflow
The collator delegate or the delegator is trying to un-stake more
funds that are currently staked.

---------
### UnstakingIsEmpty
Cannot unlock when Unstaked is empty.

---------
### ValStakeAboveMax
The account has already staked the maximum amount of funds possible.

---------
### ValStakeBelowMin
The account has not staked enough funds to be added to the collator
candidates set.

---------
### ValStakeZero
The account tried to stake more or less with amount zero.

---------