
# ParachainStaking

---------
## Calls

---------
### cancel_candidate_bond_less
Cancel pending request to adjust the collator candidate self bond
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
Cancel request to change an existing delegation.
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'cancel_delegation_request', {'candidate': '[u8; 20]'}
)
```

---------
### cancel_leave_candidates
Cancel open request to leave candidates
- only callable by collator account
- result upon successful call is the candidate is active in the candidate pool
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
DEPRECATED use batch util with cancel_delegation_request for all delegations
Cancel a pending request to exit the set of delegators. Success clears the pending exit
request (thereby resetting the delay upon another `leave_delegators` call).
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
Increase collator candidate self bond by `more`
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
DEPRECATED use delegateWithAutoCompound
If caller is not a delegator and not a collator, then join the set of delegators
If caller is a delegator, then makes delegation to change their delegation state
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `T::AccountId` | 
| amount | `BalanceOf<T>` | 
| candidate_delegation_count | `u32` | 
| delegation_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'delegate', {
    'amount': 'u128',
    'candidate': '[u8; 20]',
    'candidate_delegation_count': 'u32',
    'delegation_count': 'u32',
}
)
```

---------
### delegate_with_auto_compound
If caller is not a delegator and not a collator, then join the set of delegators
If caller is a delegator, then makes delegation to change their delegation state
Sets the auto-compound config for the delegation
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `T::AccountId` | 
| amount | `BalanceOf<T>` | 
| auto_compound | `Percent` | 
| candidate_delegation_count | `u32` | 
| candidate_auto_compounding_delegation_count | `u32` | 
| delegation_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'delegate_with_auto_compound', {
    'amount': 'u128',
    'auto_compound': 'u8',
    'candidate': '[u8; 20]',
    'candidate_auto_compounding_delegation_count': 'u32',
    'candidate_delegation_count': 'u32',
    'delegation_count': 'u32',
}
)
```

---------
### delegator_bond_more
Bond more for delegators wrt a specific collator candidate.
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `T::AccountId` | 
| more | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'delegator_bond_more', {
    'candidate': '[u8; 20]',
    'more': 'u128',
}
)
```

---------
### execute_candidate_bond_less
Execute pending request to adjust the collator candidate self bond
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'execute_candidate_bond_less', {'candidate': '[u8; 20]'}
)
```

---------
### execute_delegation_request
Execute pending request to change an existing delegation
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegator | `T::AccountId` | 
| candidate | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'execute_delegation_request', {
    'candidate': '[u8; 20]',
    'delegator': '[u8; 20]',
}
)
```

---------
### execute_leave_candidates
Execute leave candidates request
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `T::AccountId` | 
| candidate_delegation_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'execute_leave_candidates', {
    'candidate': '[u8; 20]',
    'candidate_delegation_count': 'u32',
}
)
```

---------
### execute_leave_delegators
DEPRECATED use batch util with execute_delegation_request for all delegations
Execute the right to exit the set of delegators and revoke all ongoing delegations.
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegator | `T::AccountId` | 
| delegation_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'execute_leave_delegators', {
    'delegation_count': 'u32',
    'delegator': '[u8; 20]',
}
)
```

---------
### go_offline
Temporarily leave the set of collator candidates without unbonding
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
Rejoin the set of collator candidates if previously had called `go_offline`
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'go_online', {}
)
```

---------
### hotfix_remove_delegation_requests_exited_candidates
Hotfix to remove existing empty entries for candidates that have left.
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidates | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'hotfix_remove_delegation_requests_exited_candidates', {'candidates': ['[u8; 20]']}
)
```

---------
### join_candidates
Join the set of collator candidates
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
Request by collator candidate to decrease self bond by `less`
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
Request bond less for delegators wrt a specific collator candidate. The delegation&\#x27;s
rewards for rounds while the request is pending use the reduced bonded amount.
A bond less may not be performed if any other scheduled request is pending.
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `T::AccountId` | 
| less | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'schedule_delegator_bond_less', {
    'candidate': '[u8; 20]',
    'less': 'u128',
}
)
```

---------
### schedule_leave_candidates
Request to leave the set of candidates. If successful, the account is immediately
removed from the candidate pool to prevent selection as a collator.
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
DEPRECATED use batch util with schedule_revoke_delegation for all delegations
Request to leave the set of delegators. If successful, the caller is scheduled to be
allowed to exit via a [DelegationAction::Revoke] towards all existing delegations.
Success forbids future delegation requests until the request is invoked or cancelled.
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
Request to revoke an existing delegation. If successful, the delegation is scheduled
to be allowed to be revoked via the `execute_delegation_request` extrinsic.
The delegation receives no rewards for the rounds while a revoke is pending.
A revoke may not be performed if any other scheduled request is pending.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collator | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'schedule_revoke_delegation', {'collator': '[u8; 20]'}
)
```

---------
### set_auto_compound
Sets the auto-compounding reward percentage for a delegation.
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `T::AccountId` | 
| value | `Percent` | 
| candidate_auto_compounding_delegation_count_hint | `u32` | 
| delegation_count_hint | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'set_auto_compound', {
    'candidate': '[u8; 20]',
    'candidate_auto_compounding_delegation_count_hint': 'u32',
    'delegation_count_hint': 'u32',
    'value': 'u8',
}
)
```

---------
### set_blocks_per_round
Set blocks per round
- if called with `new` less than length of current round, will transition immediately
in the next block
- also updates per-round inflation config
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
Set the commission for all collators
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
Set the annual inflation rate to derive per-round inflation
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
Set the account that will hold funds set aside for parachain bond
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'set_parachain_bond_account', {'new': '[u8; 20]'}
)
```

---------
### set_parachain_bond_reserve_percent
Set the percent of inflation set aside for parachain bond
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
Set the expectations for total staked. These expectations determine the issuance for
the round according to logic in `fn compute_issuance`
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
Set the total number of collator candidates selected per round
- changes are not applied until the start of the next round
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
### AutoCompoundSet
Auto-compounding reward percent was set for a delegation.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `T::AccountId` | ```[u8; 20]```
| delegator | `T::AccountId` | ```[u8; 20]```
| value | `Percent` | ```u8```

---------
### BlocksPerRoundSet
Set blocks per round
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| current_round | `RoundIndex` | ```u32```
| first_block | `T::BlockNumber` | ```u32```
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
| candidate | `T::AccountId` | ```[u8; 20]```
| amount | `BalanceOf<T>` | ```u128```
| execute_round | `RoundIndex` | ```u32```

---------
### CancelledCandidateExit
Cancelled request to leave the set of candidates.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `T::AccountId` | ```[u8; 20]```

---------
### CancelledDelegationRequest
Cancelled request to change an existing delegation.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```[u8; 20]```
| cancelled_request | `CancelledScheduledRequest<BalanceOf<T>>` | ```{'when_executable': 'u32', 'action': {'Revoke': 'u128', 'Decrease': 'u128'}}```
| collator | `T::AccountId` | ```[u8; 20]```

---------
### CandidateBackOnline
Candidate rejoins the set of collator candidates.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `T::AccountId` | ```[u8; 20]```

---------
### CandidateBondLessRequested
Candidate requested to decrease a self bond.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `T::AccountId` | ```[u8; 20]```
| amount_to_decrease | `BalanceOf<T>` | ```u128```
| execute_round | `RoundIndex` | ```u32```

---------
### CandidateBondedLess
Candidate has decreased a self bond.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `T::AccountId` | ```[u8; 20]```
| amount | `BalanceOf<T>` | ```u128```
| new_bond | `BalanceOf<T>` | ```u128```

---------
### CandidateBondedMore
Candidate has increased a self bond.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `T::AccountId` | ```[u8; 20]```
| amount | `BalanceOf<T>` | ```u128```
| new_total_bond | `BalanceOf<T>` | ```u128```

---------
### CandidateLeft
Candidate has left the set of candidates.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ex_candidate | `T::AccountId` | ```[u8; 20]```
| unlocked_amount | `BalanceOf<T>` | ```u128```
| new_total_amt_locked | `BalanceOf<T>` | ```u128```

---------
### CandidateScheduledExit
Candidate has requested to leave the set of candidates.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| exit_allowed_round | `RoundIndex` | ```u32```
| candidate | `T::AccountId` | ```[u8; 20]```
| scheduled_exit | `RoundIndex` | ```u32```

---------
### CandidateWentOffline
Candidate temporarily leave the set of collator candidates without unbonding.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `T::AccountId` | ```[u8; 20]```

---------
### CollatorChosen
Candidate selected for collators. Total Exposed Amount includes all delegations.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| round | `RoundIndex` | ```u32```
| collator_account | `T::AccountId` | ```[u8; 20]```
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
### Compounded
Compounded a portion of rewards towards the delegation.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| candidate | `T::AccountId` | ```[u8; 20]```
| delegator | `T::AccountId` | ```[u8; 20]```
| amount | `BalanceOf<T>` | ```u128```

---------
### Delegation
New delegation (increase of the existing one).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```[u8; 20]```
| locked_amount | `BalanceOf<T>` | ```u128```
| candidate | `T::AccountId` | ```[u8; 20]```
| delegator_position | `DelegatorAdded<BalanceOf<T>>` | ```{'AddedToTop': {'new_total': 'u128'}, 'AddedToBottom': None}```
| auto_compound | `Percent` | ```u8```

---------
### DelegationDecreaseScheduled
Delegator requested to decrease a bond for the collator candidate.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```[u8; 20]```
| candidate | `T::AccountId` | ```[u8; 20]```
| amount_to_decrease | `BalanceOf<T>` | ```u128```
| execute_round | `RoundIndex` | ```u32```

---------
### DelegationDecreased
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```[u8; 20]```
| candidate | `T::AccountId` | ```[u8; 20]```
| amount | `BalanceOf<T>` | ```u128```
| in_top | `bool` | ```bool```

---------
### DelegationIncreased
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```[u8; 20]```
| candidate | `T::AccountId` | ```[u8; 20]```
| amount | `BalanceOf<T>` | ```u128```
| in_top | `bool` | ```bool```

---------
### DelegationKicked
Delegation kicked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```[u8; 20]```
| candidate | `T::AccountId` | ```[u8; 20]```
| unstaked_amount | `BalanceOf<T>` | ```u128```

---------
### DelegationRevocationScheduled
Delegator requested to revoke delegation.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| round | `RoundIndex` | ```u32```
| delegator | `T::AccountId` | ```[u8; 20]```
| candidate | `T::AccountId` | ```[u8; 20]```
| scheduled_exit | `RoundIndex` | ```u32```

---------
### DelegationRevoked
Delegation revoked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```[u8; 20]```
| candidate | `T::AccountId` | ```[u8; 20]```
| unstaked_amount | `BalanceOf<T>` | ```u128```

---------
### DelegatorExitCancelled
Cancelled a pending request to exit the set of delegators.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```[u8; 20]```

---------
### DelegatorExitScheduled
Delegator requested to leave the set of delegators.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| round | `RoundIndex` | ```u32```
| delegator | `T::AccountId` | ```[u8; 20]```
| scheduled_exit | `RoundIndex` | ```u32```

---------
### DelegatorLeft
Delegator has left the set of delegators.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```[u8; 20]```
| unstaked_amount | `BalanceOf<T>` | ```u128```

---------
### DelegatorLeftCandidate
Delegation from candidate state has been remove.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```[u8; 20]```
| candidate | `T::AccountId` | ```[u8; 20]```
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
| account | `T::AccountId` | ```[u8; 20]```
| amount_locked | `BalanceOf<T>` | ```u128```
| new_total_amt_locked | `BalanceOf<T>` | ```u128```

---------
### NewRound
Started new round.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| starting_block | `T::BlockNumber` | ```u32```
| round | `RoundIndex` | ```u32```
| selected_collators_number | `u32` | ```u32```
| total_balance | `BalanceOf<T>` | ```u128```

---------
### ParachainBondAccountSet
Account (re)set for parachain bond treasury.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old | `T::AccountId` | ```[u8; 20]```
| new | `T::AccountId` | ```[u8; 20]```

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
| account | `T::AccountId` | ```[u8; 20]```
| value | `BalanceOf<T>` | ```u128```

---------
### Rewarded
Paid the account (delegator or collator) the balance as liquid rewards.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```[u8; 20]```
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
    'ParachainStaking', 'AtStake', ['u32', '[u8; 20]']
)
```

#### Return value
```python
{
    'bond': 'u128',
    'delegations': [
        {'amount': 'u128', 'auto_compound': 'u8', 'owner': '[u8; 20]'},
    ],
    'total': 'u128',
}
```
---------
### AutoCompoundingDelegations
 Stores auto-compounding configuration per collator.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'AutoCompoundingDelegations', ['[u8; 20]']
)
```

#### Return value
```python
[{'delegator': '[u8; 20]', 'value': 'u8'}]
```
---------
### AwardedPts
 Points for each collator per round

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'AwardedPts', ['u32', '[u8; 20]']
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
    'ParachainStaking', 'BottomDelegations', ['[u8; 20]']
)
```

#### Return value
```python
{'delegations': [{'amount': 'u128', 'owner': '[u8; 20]'}], 'total': 'u128'}
```
---------
### CandidateInfo
 Get collator candidate info associated with an account if account is candidate else None

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'CandidateInfo', ['[u8; 20]']
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
[{'amount': 'u128', 'owner': '[u8; 20]'}]
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
    'ParachainStaking', 'DelegationScheduledRequests', ['[u8; 20]']
)
```

#### Return value
```python
[
    {'action': {'Decrease': 'u128', 'Revoke': 'u128'}, 'delegator': '[u8; 20]', 'when_executable': 'u32'},
]
```
---------
### DelegatorState
 Get delegator state associated with an account if account is delegating else None

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'DelegatorState', ['[u8; 20]']
)
```

#### Return value
```python
{
    'delegations': [{'amount': 'u128', 'owner': '[u8; 20]'}],
    'id': '[u8; 20]',
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
{'account': '[u8; 20]', 'percent': 'u8'}
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
['[u8; 20]']
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
    'ParachainStaking', 'TopDelegations', ['[u8; 20]']
)
```

#### Return value
```python
{'delegations': [{'amount': 'u128', 'owner': '[u8; 20]'}], 'total': 'u128'}
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
### CandidateBondLessDelay
 Number of rounds candidate requests to decrease self-bond must wait to be executable
#### Value
```python
28
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'CandidateBondLessDelay')
```
---------
### DelegationBondLessDelay
 Number of rounds that delegation less requests must wait before executable
#### Value
```python
28
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'DelegationBondLessDelay')
```
---------
### LeaveCandidatesDelay
 Number of rounds that candidates remain bonded before exit request is executable
#### Value
```python
28
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
28
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
2000000000000000000000000
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MinCandidateStk')
```
---------
### MinDelegation
 Minimum stake for any registered on-chain account to delegate
#### Value
```python
50000000000000000000
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
50000000000000000000
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
8
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MinSelectedCandidates')
```
---------
### RevokeDelegationDelay
 Number of rounds that delegations remain bonded before revocation request is executable
#### Value
```python
28
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
### RoundLengthMustBeGreaterThanTotalSelectedCollators

---------
### TooLowCandidateAutoCompoundingDelegationCountToAutoCompound

---------
### TooLowCandidateAutoCompoundingDelegationCountToDelegate

---------
### TooLowCandidateAutoCompoundingDelegationCountToLeaveCandidates

---------
### TooLowCandidateCountToLeaveCandidates

---------
### TooLowCandidateCountWeightHint

---------
### TooLowCandidateCountWeightHintCancelLeaveCandidates

---------
### TooLowCandidateCountWeightHintCandidateBondMore

---------
### TooLowCandidateCountWeightHintGoOffline

---------
### TooLowCandidateCountWeightHintGoOnline

---------
### TooLowCandidateCountWeightHintJoinCandidates

---------
### TooLowCandidateDelegationCountToDelegate

---------
### TooLowCandidateDelegationCountToLeaveCandidates

---------
### TooLowDelegationCountToAutoCompound

---------
### TooLowDelegationCountToDelegate

---------
### TooLowDelegationCountToLeaveDelegators

---------