
# ParachainStaking

---------
## Calls

---------
### cancel_candidate_bond_less
See [`Pallet::cancel_candidate_bond_less`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'cancel_candidate_bond_less', {}
)
```

---------
### cancel_delegation_request
See [`Pallet::cancel_delegation_request`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'cancel_delegation_request', {'candidate': 'AccountId'}
)
```

---------
### cancel_leave_candidates
See [`Pallet::cancel_leave_candidates`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'cancel_leave_candidates', {'candidate_count': 'u32'}
)
```

---------
### cancel_leave_delegators
See [`Pallet::cancel_leave_delegators`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'cancel_leave_delegators', {}
)
```

---------
### candidate_bond_more
See [`Pallet::candidate_bond_more`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| more | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'candidate_bond_more', {'more': 'u128'}
)
```

---------
### delegate
See [`Pallet::delegate`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `AccountIdOf<T>` | 
| amount | `BalanceOf<T>` | 
| candidate_delegation_count | `u32` | 
| delegation_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'delegate', {
    'amount': 'u128',
    'candidate': 'AccountId',
    'candidate_delegation_count': 'u32',
    'delegation_count': 'u32',
}
)
```

---------
### delegator_bond_more
See [`Pallet::delegator_bond_more`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `AccountIdOf<T>` | 
| more | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'delegator_bond_more', {
    'candidate': 'AccountId',
    'more': 'u128',
}
)
```

---------
### execute_candidate_bond_less
See [`Pallet::execute_candidate_bond_less`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'execute_candidate_bond_less', {'candidate': 'AccountId'}
)
```

---------
### execute_delegation_request
See [`Pallet::execute_delegation_request`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegator | `AccountIdOf<T>` | 
| candidate | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'execute_delegation_request', {
    'candidate': 'AccountId',
    'delegator': 'AccountId',
}
)
```

---------
### execute_leave_candidates
See [`Pallet::execute_leave_candidates`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `AccountIdOf<T>` | 
| candidate_delegation_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'execute_leave_candidates', {
    'candidate': 'AccountId',
    'candidate_delegation_count': 'u32',
}
)
```

---------
### execute_leave_delegators
See [`Pallet::execute_leave_delegators`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegator | `AccountIdOf<T>` | 
| delegation_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'execute_leave_delegators', {
    'delegation_count': 'u32',
    'delegator': 'AccountId',
}
)
```

---------
### go_offline
See [`Pallet::go_offline`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'go_offline', {}
)
```

---------
### go_online
See [`Pallet::go_online`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'go_online', {}
)
```

---------
### hotfix_migrate_collators_from_reserve_to_locks
See [`Pallet::hotfix_migrate_collators_from_reserve_to_locks`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collators | `Vec<AccountIdOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'hotfix_migrate_collators_from_reserve_to_locks', {'collators': ['AccountId']}
)
```

---------
### hotfix_migrate_delegators_from_reserve_to_locks
See [`Pallet::hotfix_migrate_delegators_from_reserve_to_locks`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegators | `Vec<AccountIdOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'hotfix_migrate_delegators_from_reserve_to_locks', {'delegators': ['AccountId']}
)
```

---------
### hotfix_remove_delegation_requests_exited_candidates
See [`Pallet::hotfix_remove_delegation_requests_exited_candidates`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidates | `Vec<AccountIdOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'hotfix_remove_delegation_requests_exited_candidates', {'candidates': ['AccountId']}
)
```

---------
### join_candidates
See [`Pallet::join_candidates`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| bond | `BalanceOf<T>` | 
| candidate_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'join_candidates', {
    'bond': 'u128',
    'candidate_count': 'u32',
}
)
```

---------
### schedule_candidate_bond_less
See [`Pallet::schedule_candidate_bond_less`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| less | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'schedule_candidate_bond_less', {'less': 'u128'}
)
```

---------
### schedule_delegator_bond_less
See [`Pallet::schedule_delegator_bond_less`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `AccountIdOf<T>` | 
| less | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'schedule_delegator_bond_less', {
    'candidate': 'AccountId',
    'less': 'u128',
}
)
```

---------
### schedule_leave_candidates
See [`Pallet::schedule_leave_candidates`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'schedule_leave_candidates', {'candidate_count': 'u32'}
)
```

---------
### schedule_leave_delegators
See [`Pallet::schedule_leave_delegators`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'schedule_leave_delegators', {}
)
```

---------
### schedule_revoke_delegation
See [`Pallet::schedule_revoke_delegation`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collator | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'schedule_revoke_delegation', {'collator': 'AccountId'}
)
```

---------
### set_blocks_per_round
See [`Pallet::set_blocks_per_round`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'set_blocks_per_round', {'new': 'u32'}
)
```

---------
### set_collator_commission
See [`Pallet::set_collator_commission`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Perbill` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'set_collator_commission', {'new': 'u32'}
)
```

---------
### set_inflation
See [`Pallet::set_inflation`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| schedule | `Range<Perbill>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'set_inflation', {
    'schedule': {
        'ideal': 'u32',
        'max': 'u32',
        'min': 'u32',
    },
}
)
```

---------
### set_parachain_bond_account
See [`Pallet::set_parachain_bond_account`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'set_parachain_bond_account', {'new': 'AccountId'}
)
```

---------
### set_parachain_bond_reserve_percent
See [`Pallet::set_parachain_bond_reserve_percent`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Percent` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'set_parachain_bond_reserve_percent', {'new': 'u8'}
)
```

---------
### set_staking_expectations
See [`Pallet::set_staking_expectations`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| expectations | `Range<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'set_staking_expectations', {
    'expectations': {
        'ideal': 'u128',
        'max': 'u128',
        'min': 'u128',
    },
}
)
```

---------
### set_total_selected
See [`Pallet::set_total_selected`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'set_total_selected', {'new': 'u32'}
)
```

---------
## Events

---------
### BlocksPerRoundSet
Set blocks per round
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| current_round | `RoundIndex` | ```u32```
| first_block | `BlockNumberFor<T>` | ```u32```
| old | `u32` | ```u32```
| new | `u32` | ```u32```
| new_per_round_inflation_min | `Perbill` | ```u32```
| new_per_round_inflation_ideal | `Perbill` | ```u32```
| new_per_round_inflation_max | `Perbill` | ```u32```

---------
### CancelledCandidateBondLess
Cancelled request to decrease candidate&\#x27;s bond.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `AccountIdOf<T>` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```
| execute_round | `RoundIndex` | ```u32```

---------
### CancelledCandidateExit
Cancelled request to leave the set of candidates.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `AccountIdOf<T>` | ```AccountId```

---------
### CancelledDelegationRequest
Cancelled request to change an existing delegation.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `AccountIdOf<T>` | ```AccountId```
| cancelled_request | `CancelledScheduledRequest<BalanceOf<T>>` | ```{'when_executable': 'u32', 'action': {'Revoke': 'u128', 'Decrease': 'u128'}}```
| collator | `AccountIdOf<T>` | ```AccountId```

---------
### CandidateBackOnline
Candidate rejoins the set of collator candidates.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `AccountIdOf<T>` | ```AccountId```

---------
### CandidateBondLessRequested
Candidate requested to decrease a self bond.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `AccountIdOf<T>` | ```AccountId```
| amount_to_decrease | `BalanceOf<T>` | ```u128```
| execute_round | `RoundIndex` | ```u32```

---------
### CandidateBondedLess
Candidate has decreased a self bond.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `AccountIdOf<T>` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```
| new_bond | `BalanceOf<T>` | ```u128```

---------
### CandidateBondedMore
Candidate has increased a self bond.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `AccountIdOf<T>` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```
| new_total_bond | `BalanceOf<T>` | ```u128```

---------
### CandidateLeft
Candidate has left the set of candidates.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ex_candidate | `AccountIdOf<T>` | ```AccountId```
| unlocked_amount | `BalanceOf<T>` | ```u128```
| new_total_amt_locked | `BalanceOf<T>` | ```u128```

---------
### CandidateScheduledExit
Candidate has requested to leave the set of candidates.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| exit_allowed_round | `RoundIndex` | ```u32```
| candidate | `AccountIdOf<T>` | ```AccountId```
| scheduled_exit | `RoundIndex` | ```u32```

---------
### CandidateWentOffline
Candidate temporarily leave the set of collator candidates without unbonding.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `AccountIdOf<T>` | ```AccountId```

---------
### CollatorChosen
Candidate selected for collators. Total Exposed Amount includes all delegations.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| round | `RoundIndex` | ```u32```
| collator_account | `AccountIdOf<T>` | ```AccountId```
| total_exposed_amount | `BalanceOf<T>` | ```u128```

---------
### CollatorCommissionSet
Set collator commission to this value.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old | `Perbill` | ```u32```
| new | `Perbill` | ```u32```

---------
### Delegation
New delegation (increase of the existing one).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `AccountIdOf<T>` | ```AccountId```
| locked_amount | `BalanceOf<T>` | ```u128```
| candidate | `AccountIdOf<T>` | ```AccountId```
| delegator_position | `DelegatorAdded<BalanceOf<T>>` | ```{'AddedToTop': {'new_total': 'u128'}, 'AddedToBottom': None}```

---------
### DelegationDecreaseScheduled
Delegator requested to decrease a bond for the collator candidate.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `AccountIdOf<T>` | ```AccountId```
| candidate | `AccountIdOf<T>` | ```AccountId```
| amount_to_decrease | `BalanceOf<T>` | ```u128```
| execute_round | `RoundIndex` | ```u32```

---------
### DelegationDecreased
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `AccountIdOf<T>` | ```AccountId```
| candidate | `AccountIdOf<T>` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```
| in_top | `bool` | ```bool```

---------
### DelegationIncreased
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `AccountIdOf<T>` | ```AccountId```
| candidate | `AccountIdOf<T>` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```
| in_top | `bool` | ```bool```

---------
### DelegationKicked
Delegation kicked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `AccountIdOf<T>` | ```AccountId```
| candidate | `AccountIdOf<T>` | ```AccountId```
| unstaked_amount | `BalanceOf<T>` | ```u128```

---------
### DelegationRevocationScheduled
Delegator requested to revoke delegation.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| round | `RoundIndex` | ```u32```
| delegator | `AccountIdOf<T>` | ```AccountId```
| candidate | `AccountIdOf<T>` | ```AccountId```
| scheduled_exit | `RoundIndex` | ```u32```

---------
### DelegationRevoked
Delegation revoked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `AccountIdOf<T>` | ```AccountId```
| candidate | `AccountIdOf<T>` | ```AccountId```
| unstaked_amount | `BalanceOf<T>` | ```u128```

---------
### DelegatorExitCancelled
Cancelled a pending request to exit the set of delegators.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `AccountIdOf<T>` | ```AccountId```

---------
### DelegatorExitScheduled
Delegator requested to leave the set of delegators.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| round | `RoundIndex` | ```u32```
| delegator | `AccountIdOf<T>` | ```AccountId```
| scheduled_exit | `RoundIndex` | ```u32```

---------
### DelegatorLeft
Delegator has left the set of delegators.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `AccountIdOf<T>` | ```AccountId```
| unstaked_amount | `BalanceOf<T>` | ```u128```

---------
### DelegatorLeftCandidate
Delegation from candidate state has been remove.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `AccountIdOf<T>` | ```AccountId```
| candidate | `AccountIdOf<T>` | ```AccountId```
| unstaked_amount | `BalanceOf<T>` | ```u128```
| total_candidate_staked | `BalanceOf<T>` | ```u128```

---------
### InflationSet
Annual inflation input (first 3) was used to derive new per-round inflation (last 3)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| annual_min | `Perbill` | ```u32```
| annual_ideal | `Perbill` | ```u32```
| annual_max | `Perbill` | ```u32```
| round_min | `Perbill` | ```u32```
| round_ideal | `Perbill` | ```u32```
| round_max | `Perbill` | ```u32```

---------
### JoinedCollatorCandidates
Account joined the set of collator candidates.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `AccountIdOf<T>` | ```AccountId```
| amount_locked | `BalanceOf<T>` | ```u128```
| new_total_amt_locked | `BalanceOf<T>` | ```u128```

---------
### NewRound
Started new round.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| starting_block | `BlockNumberFor<T>` | ```u32```
| round | `RoundIndex` | ```u32```
| selected_collators_number | `u32` | ```u32```
| total_balance | `BalanceOf<T>` | ```u128```

---------
### ParachainBondAccountSet
Account (re)set for parachain bond treasury.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old | `AccountIdOf<T>` | ```AccountId```
| new | `AccountIdOf<T>` | ```AccountId```

---------
### ParachainBondReservePercentSet
Percent of inflation reserved for parachain bond (re)set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old | `Percent` | ```u8```
| new | `Percent` | ```u8```

---------
### ReservedForParachainBond
Transferred to account which holds funds reserved for parachain bond.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `AccountIdOf<T>` | ```AccountId```
| value | `BalanceOf<T>` | ```u128```

---------
### Rewarded
Paid the account (delegator or collator) the balance as liquid rewards.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `AccountIdOf<T>` | ```AccountId```
| rewards | `BalanceOf<T>` | ```u128```

---------
### StakeExpectationsSet
Staking expectations set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| expect_min | `BalanceOf<T>` | ```u128```
| expect_ideal | `BalanceOf<T>` | ```u128```
| expect_max | `BalanceOf<T>` | ```u128```

---------
### TotalSelectedSet
Set total selected candidates to this value.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old | `u32` | ```u32```
| new | `u32` | ```u32```

---------
## Storage functions

---------
### AtStake
 Snapshot of collator delegation stake at the start of the round

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'AtStake', ['u32', 'AccountId']
)
```

#### Return value
```python
{'bond': 'u128', 'delegations': [{'amount': 'u128', 'owner': 'AccountId'}], 'total': 'u128'}
```
---------
### AwardedPts
 Points for each collator per round

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'AwardedPts', ['u32', 'AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### BottomDelegations
 Bottom delegations for collator candidate

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'BottomDelegations', ['AccountId']
)
```

#### Return value
```python
{'delegations': [{'amount': 'u128', 'owner': 'AccountId'}], 'total': 'u128'}
```
---------
### CandidateInfo
 Get collator candidate info associated with an account if account is candidate else None

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'CandidateInfo', ['AccountId']
)
```

#### Return value
```python
{
    'bond': 'u128',
    'bottom_capacity': ('Full', 'Empty', 'Partial'),
    'delegation_count': 'u32',
    'highest_bottom_delegation_amount': 'u128',
    'lowest_bottom_delegation_amount': 'u128',
    'lowest_top_delegation_amount': 'u128',
    'request': (None, {'amount': 'u128', 'when_executable': 'u32'}),
    'status': {'Active': None, 'Idle': None, 'Leaving': 'u32'},
    'top_capacity': ('Full', 'Empty', 'Partial'),
    'total_counted': 'u128',
}
```
---------
### CandidatePool
 The pool of collator candidates, each with their total backing stake

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'CandidatePool', []
)
```

#### Return value
```python
[{'amount': 'u128', 'owner': 'AccountId'}]
```
---------
### CollatorCommission
 Commission percent taken off of rewards for all collators

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'CollatorCommission', []
)
```

#### Return value
```python
'u32'
```
---------
### CollatorReserveToLockMigrations
 Temporary storage item to track whether a given collator&#x27;s reserve has been migrated.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'CollatorReserveToLockMigrations', ['AccountId']
)
```

#### Return value
```python
'bool'
```
---------
### DelayedPayouts
 Delayed payouts

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'DelayedPayouts', ['u32']
)
```

#### Return value
```python
{
    'collator_commission': 'u32',
    'round_issuance': 'u128',
    'total_staking_reward': 'u128',
}
```
---------
### DelegationScheduledRequests
 Stores outstanding delegation requests per collator.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'DelegationScheduledRequests', ['AccountId']
)
```

#### Return value
```python
[
    {'action': {'Decrease': 'u128', 'Revoke': 'u128'}, 'delegator': 'AccountId', 'when_executable': 'u32'},
]
```
---------
### DelegatorReserveToLockMigrations
 Temporary storage item to track whether a given delegator&#x27;s reserve has been migrated.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'DelegatorReserveToLockMigrations', ['AccountId']
)
```

#### Return value
```python
'bool'
```
---------
### DelegatorState
 Get delegator state associated with an account if account is delegating else None

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'DelegatorState', ['AccountId']
)
```

#### Return value
```python
{
    'delegations': [{'amount': 'u128', 'owner': 'AccountId'}],
    'id': 'AccountId',
    'less_total': 'u128',
    'status': {'Active': None, 'Leaving': 'u32'},
    'total': 'u128',
}
```
---------
### InflationConfig
 Inflation configuration

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'InflationConfig', []
)
```

#### Return value
```python
{
    'annual': {'ideal': 'u32', 'max': 'u32', 'min': 'u32'},
    'expect': {'ideal': 'u128', 'max': 'u128', 'min': 'u128'},
    'round': {'ideal': 'u32', 'max': 'u32', 'min': 'u32'},
}
```
---------
### ParachainBondInfo
 Parachain bond config info { account, percent_of_inflation }

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'ParachainBondInfo', []
)
```

#### Return value
```python
{'account': 'AccountId', 'payment_in_round': 'u128', 'percent': 'u8'}
```
---------
### Points
 Total points awarded to collators for block production in the round

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'Points', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### Round
 Current round index and next round scheduled transition

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
### SelectedCandidates
 The collator candidates selected for the current round

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'SelectedCandidates', []
)
```

#### Return value
```python
['AccountId']
```
---------
### Staked
 Total counted stake for selected candidates in the round

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'Staked', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### TopDelegations
 Top delegations for collator candidate

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'TopDelegations', ['AccountId']
)
```

#### Return value
```python
{'delegations': [{'amount': 'u128', 'owner': 'AccountId'}], 'total': 'u128'}
```
---------
### Total
 Total capital locked by this staking pallet

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'Total', []
)
```

#### Return value
```python
'u128'
```
---------
### TotalSelected
 The total candidates selected every round

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'TotalSelected', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### AllowInflation
 Allow inflation or not
#### Value
```python
False
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'AllowInflation')
```
---------
### CandidateBondLessDelay
 Number of rounds candidate requests to decrease self-bond must wait to be executable
#### Value
```python
84
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'CandidateBondLessDelay')
```
---------
### DefaultBlocksPerRound
 Default number of blocks per round at genesis
#### Value
```python
600
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'DefaultBlocksPerRound')
```
---------
### DefaultCollatorCommission
 Default commission due to collators, is `CollatorCommission` storage value in genesis
#### Value
```python
100000000
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'DefaultCollatorCommission')
```
---------
### DefaultParachainBondReservePercent
 Default percent of inflation set aside for parachain bond account
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'DefaultParachainBondReservePercent')
```
---------
### DelegationBondLessDelay
 Number of rounds that delegation less requests must wait before executable
#### Value
```python
84
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'DelegationBondLessDelay')
```
---------
### InitSeedStk
 Invulnables init stake
#### Value
```python
5000000000000000
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'InitSeedStk')
```
---------
### LeaveCandidatesDelay
 Number of rounds that candidates remain bonded before exit request is executable
#### Value
```python
84
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'LeaveCandidatesDelay')
```
---------
### LeaveDelegatorsDelay
 Number of rounds that delegators remain bonded before exit request is executable
#### Value
```python
84
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'LeaveDelegatorsDelay')
```
---------
### MaxBottomDelegationsPerCandidate
 Maximum bottom delegations (not counted) per candidate
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MaxBottomDelegationsPerCandidate')
```
---------
### MaxDelegationsPerDelegator
 Maximum delegations per delegator
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MaxDelegationsPerDelegator')
```
---------
### MaxTopDelegationsPerCandidate
 Maximum top delegations counted per candidate
#### Value
```python
300
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MaxTopDelegationsPerCandidate')
```
---------
### MinBlocksPerRound
 Minimum number of blocks per round
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MinBlocksPerRound')
```
---------
### MinCandidateStk
 Minimum stake required for any account to be a collator candidate
#### Value
```python
5000000000000000
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MinCandidateStk')
```
---------
### MinCollatorStk
 Minimum stake required for any candidate to be in `SelectedCandidates` for the round
#### Value
```python
5000000000000000
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MinCollatorStk')
```
---------
### MinDelegation
 Minimum stake for any registered on-chain account to delegate
#### Value
```python
50000000000000
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MinDelegation')
```
---------
### MinDelegatorStk
 Minimum stake for any registered on-chain account to be a delegator
#### Value
```python
50000000000000
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MinDelegatorStk')
```
---------
### MinSelectedCandidates
 Minimum number of selected candidates every round
#### Value
```python
16
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MinSelectedCandidates')
```
---------
### PalletId
 PalletId
#### Value
```python
'0x62662f7374616b65'
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'PalletId')
```
---------
### PaymentInRound
 Fix payment in one round if no inflation
#### Value
```python
180000000000000
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'PaymentInRound')
```
---------
### RevokeDelegationDelay
 Number of rounds that delegations remain bonded before revocation request is executable
#### Value
```python
84
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'RevokeDelegationDelay')
```
---------
### RewardPaymentDelay
 Number of rounds after which block authors are rewarded
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'RewardPaymentDelay')
```
---------
### ToMigrateInvulnables
 Invulnables to migrate
#### Value
```python
[
    'eunwjK45qDugPXhnjxGUcMbifgdtgefzoW7PgMMpr39AXwh',
    'dBkoWVdQCccH1xNAeR1Y4vrETt3a4j4iU8Ct2ewY1FUjasL',
    'dwrEwfj2RFU4DS6EiTCfmxMpQ1sAsaHykftzwoptFe4a8aH',
    'fAjW6bwT4GKgW88sjZfNLRr5hWyMM9T9ZwqHYkFiSxw4Yhp',
]
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'ToMigrateInvulnables')
```
---------
## Errors

---------
### AlreadyActive

---------
### AlreadyDelegatedCandidate

---------
### AlreadyOffline

---------
### CandidateAlreadyLeaving

---------
### CandidateBondBelowMin

---------
### CandidateCannotLeaveYet

---------
### CandidateDNE

---------
### CandidateExists

---------
### CandidateNotLeaving

---------
### CannotDelegateIfLeaving

---------
### CannotDelegateLessThanOrEqualToLowestBottomWhenFull

---------
### CannotGoOnlineIfLeaving

---------
### CannotSetBelowMin

---------
### DelegationBelowMin

---------
### DelegationDNE

---------
### DelegatorAlreadyLeaving

---------
### DelegatorBondBelowMin

---------
### DelegatorCannotLeaveYet

---------
### DelegatorDNE

---------
### DelegatorDNEInDelegatorSet

---------
### DelegatorDNEinTopNorBottom

---------
### DelegatorExists

---------
### DelegatorNotLeaving

---------
### ExceedMaxDelegationsPerDelegator

---------
### InsufficientBalance

---------
### InvalidSchedule

---------
### NoWritingSameValue

---------
### PendingCandidateRequestAlreadyExists

---------
### PendingCandidateRequestNotDueYet

---------
### PendingCandidateRequestsDNE

---------
### PendingDelegationRequestAlreadyExists

---------
### PendingDelegationRequestDNE

---------
### PendingDelegationRequestNotDueYet

---------
### PendingDelegationRevoke

---------
### RoundLengthMustBeAtLeastTotalSelectedCollators

---------
### TooLowCandidateCountToLeaveCandidates

---------
### TooLowCandidateCountWeightHintCancelLeaveCandidates

---------
### TooLowCandidateCountWeightHintJoinCandidates

---------
### TooLowCandidateDelegationCountToDelegate

---------
### TooLowCandidateDelegationCountToLeaveCandidates

---------
### TooLowDelegationCountToDelegate

---------
### TooLowDelegationCountToLeaveDelegators

---------