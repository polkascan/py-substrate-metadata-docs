
# ParachainStaking

---------
## Calls

---------
### add_staking_liquidity_token
#### Attributes
| Name | Type |
| -------- | -------- | 
| paired_or_liquidity_token | `PairedOrLiquidityToken` | 
| current_liquidity_tokens | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'add_staking_liquidity_token', {
    'current_liquidity_tokens': 'u32',
    'paired_or_liquidity_token': {
        'Liquidity': 'u32',
        'Paired': 'u32',
    },
}
)
```

---------
### cancel_candidate_bond_request
Cancel pending request to adjust the collator candidate self bond
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'cancel_candidate_bond_request', {}
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
    'ParachainStaking', 'cancel_delegation_request', {'candidate': 'AccountId'}
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
### delegate
If caller is not a delegator and not a collator, then join the set of delegators
If caller is a delegator, then makes delegation to change their delegation state
#### Attributes
| Name | Type |
| -------- | -------- | 
| collator | `T::AccountId` | 
| amount | `Balance` | 
| use_balance_from | `Option<BondKind>` | 
| candidate_delegation_count | `u32` | 
| delegation_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'delegate', {
    'amount': 'u128',
    'candidate_delegation_count': 'u32',
    'collator': 'AccountId',
    'delegation_count': 'u32',
    'use_balance_from': (
        None,
        (
            'AvailableBalance',
            'ActivatedUnstakedReserves',
            'UnspentReserves',
        ),
    ),
}
)
```

---------
### execute_candidate_bond_request
Execute pending request to adjust the collator candidate self bond
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `T::AccountId` | 
| use_balance_from | `Option<BondKind>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'execute_candidate_bond_request', {
    'candidate': 'AccountId',
    'use_balance_from': (
        None,
        (
            'AvailableBalance',
            'ActivatedUnstakedReserves',
            'UnspentReserves',
        ),
    ),
}
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
| use_balance_from | `Option<BondKind>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'execute_delegation_request', {
    'candidate': 'AccountId',
    'delegator': 'AccountId',
    'use_balance_from': (
        None,
        (
            'AvailableBalance',
            'ActivatedUnstakedReserves',
            'UnspentReserves',
        ),
    ),
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
    'candidate': 'AccountId',
    'candidate_delegation_count': 'u32',
}
)
```

---------
### execute_leave_delegators
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
    'delegator': 'AccountId',
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
### join_candidates
Join the set of collator candidates
#### Attributes
| Name | Type |
| -------- | -------- | 
| bond | `Balance` | 
| liquidity_token | `TokenId` | 
| use_balance_from | `Option<BondKind>` | 
| candidate_count | `u32` | 
| liquidity_token_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'join_candidates', {
    'bond': 'u128',
    'candidate_count': 'u32',
    'liquidity_token': 'u32',
    'liquidity_token_count': 'u32',
    'use_balance_from': (
        None,
        (
            'AvailableBalance',
            'ActivatedUnstakedReserves',
            'UnspentReserves',
        ),
    ),
}
)
```

---------
### remove_staking_liquidity_token
#### Attributes
| Name | Type |
| -------- | -------- | 
| paired_or_liquidity_token | `PairedOrLiquidityToken` | 
| current_liquidity_tokens | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'remove_staking_liquidity_token', {
    'current_liquidity_tokens': 'u32',
    'paired_or_liquidity_token': {
        'Liquidity': 'u32',
        'Paired': 'u32',
    },
}
)
```

---------
### schedule_candidate_bond_less
Request by collator candidate to decrease self bond by `less`
#### Attributes
| Name | Type |
| -------- | -------- | 
| less | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'schedule_candidate_bond_less', {'less': 'u128'}
)
```

---------
### schedule_candidate_bond_more
Request by collator candidate to increase self bond by `more`
#### Attributes
| Name | Type |
| -------- | -------- | 
| more | `Balance` | 
| use_balance_from | `Option<BondKind>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'schedule_candidate_bond_more', {
    'more': 'u128',
    'use_balance_from': (
        None,
        (
            'AvailableBalance',
            'ActivatedUnstakedReserves',
            'UnspentReserves',
        ),
    ),
}
)
```

---------
### schedule_delegator_bond_less
Request bond less for delegators wrt a specific collator candidate.
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `T::AccountId` | 
| less | `Balance` | 

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
### schedule_delegator_bond_more
Request to bond more for delegators wrt a specific collator candidate.
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `T::AccountId` | 
| more | `Balance` | 
| use_balance_from | `Option<BondKind>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'schedule_delegator_bond_more', {
    'candidate': 'AccountId',
    'more': 'u128',
    'use_balance_from': (
        None,
        (
            'AvailableBalance',
            'ActivatedUnstakedReserves',
            'UnspentReserves',
        ),
    ),
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
Request to leave the set of delegators. If successful, the caller is scheduled
to be allowed to exit. Success forbids future delegator actions until the request is
invoked or cancelled.
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
#### Attributes
| Name | Type |
| -------- | -------- | 
| collator | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'schedule_revoke_delegation', {'collator': 'AccountId'}
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
### CancelledCandidateBondChange
Candidate, Cancelled Request
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `CandidateBondRequest` | ```{'amount': 'u128', 'change': ('Increase', 'Decrease'), 'when_executable': 'u32'}```

---------
### CancelledCandidateExit
Candidate
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### CancelledDelegationRequest
Delegator, Cancelled Request
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `DelegationRequest<T::AccountId>` | ```{'collator': 'AccountId', 'amount': 'u128', 'when_executable': 'u32', 'action': ('Revoke', 'Increase', 'Decrease')}```

---------
### CandidateBackOnline
Round Online, Candidate
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `RoundIndex` | ```u32```
| None | `T::AccountId` | ```AccountId```

---------
### CandidateBondLessRequested
Candidate, Amount To Decrease, Round at which request can be executed by caller
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `RoundIndex` | ```u32```

---------
### CandidateBondMoreRequested
Candidate, Amount To Increase, Round at which request can be executed by caller
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `RoundIndex` | ```u32```

---------
### CandidateBondedLess
Candidate, Amount, New Bond
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### CandidateBondedMore
Candidate, Amount, New Bond Total
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### CandidateLeft
Ex-Candidate, Amount Unlocked, New Total Amt Locked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### CandidateScheduledExit
Round At Which Exit Is Allowed, Candidate, Scheduled Exit
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `RoundIndex` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `RoundIndex` | ```u32```

---------
### CandidateWentOffline
Round Offline, Candidate
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `RoundIndex` | ```u32```
| None | `T::AccountId` | ```AccountId```

---------
### CollatorChosen
Round, Collator Account, Total Exposed Amount (includes all delegations)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `RoundIndex` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### CollatorCommissionSet
Set collator commission to this value [old, new]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Perbill` | ```u32```
| None | `Perbill` | ```u32```

---------
### Delegation
Delegator, Amount Locked, Candidate, Delegator Position with New Total Counted if in Top
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `T::AccountId` | ```AccountId```
| None | `DelegatorAdded` | ```{'AddedToTop': {'new_total': 'u128'}, 'AddedToBottom': None}```

---------
### DelegationDecreaseScheduled
Delegator, Candidate, Amount to be decreased, Round at which can be executed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `RoundIndex` | ```u32```

---------
### DelegationDecreased
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `bool` | ```bool```

---------
### DelegationIncreaseScheduled
Delegator, Candidate, Amount to be increased, Round at which can be executed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `RoundIndex` | ```u32```

---------
### DelegationIncreased
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `bool` | ```bool```

---------
### DelegationRevocationScheduled
Round, Delegator, Candidate, Scheduled Exit
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `RoundIndex` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `RoundIndex` | ```u32```

---------
### DelegationRevoked
Delegator, Candidate, Amount Unstaked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### DelegatorDueReward
Delegator, Collator, Due reward (as per counted delegation for collator)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### DelegatorExitCancelled
Delegator
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### DelegatorExitScheduled
Round, Delegator, Scheduled Exit
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `RoundIndex` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `RoundIndex` | ```u32```

---------
### DelegatorLeft
Delegator, Amount Unstaked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### DelegatorLeftCandidate
Delegator, Candidate, Amount Unstaked, New Total Amt Staked for Candidate
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### JoinedCollatorCandidates
Account, Amount Locked, New Total Amt Locked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### NewRound
Starting Block, Round, Number of Collators Selected, Total Balance
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```
| None | `RoundIndex` | ```u32```
| None | `u32` | ```u32```
| None | `Balance` | ```u128```

---------
### Rewarded
Paid the account (delegator or collator) the balance as liquid rewards
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### StakeExpectationsSet
Staking expectations set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### TotalSelectedSet
Set total selected candidates to this value [old, new]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```
| None | `u32` | ```u32```

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
{
    'bond': 'u128',
    'delegations': [
        {'amount': 'u128', 'liquidity_token': 'u32', 'owner': 'AccountId'},
    ],
    'liquidity_token': 'u32',
    'total': 'u128',
}
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
[{'amount': 'u128', 'liquidity_token': 'u32', 'owner': 'AccountId'}]
```
---------
### CandidateState
 Get collator candidate state associated with an account if account is a candidate else None

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'CandidateState', ['AccountId']
)
```

#### Return value
```python
{
    'bond': 'u128',
    'bottom_delegations': [
        {'amount': 'u128', 'liquidity_token': 'u32', 'owner': 'AccountId'},
    ],
    'delegators': ['AccountId'],
    'id': 'AccountId',
    'liquidity_token': 'u32',
    'request': (
        None,
        {'amount': 'u128', 'change': ('Increase', 'Decrease'), 'when_executable': 'u32'},
    ),
    'state': {'Active': None, 'Idle': None, 'Leaving': 'u32'},
    'top_delegations': [
        {'amount': 'u128', 'liquidity_token': 'u32', 'owner': 'AccountId'},
    ],
    'total_backing': 'u128',
    'total_counted': 'u128',
}
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
    'delegations': [
        {'amount': 'u128', 'liquidity_token': 'u32', 'owner': 'AccountId'},
    ],
    'id': 'AccountId',
    'requests': {'requests': 'scale_info::384'},
    'status': {'Active': None, 'Leaving': 'u32'},
}
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
### StakingLiquidityTokens
 Points for each collator per round

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'StakingLiquidityTokens', []
)
```

#### Return value
```python
'scale_info::394'
```
---------
### Total
 Total capital locked by this staking pallet

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'Total', ['u32']
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
### BlocksPerRound
 Default number of blocks per round at genesis
#### Value
```python
1200
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'BlocksPerRound')
```
---------
### CandidateBondDelay
 Number of rounds that candidate requests to adjust self-bond must wait to be executable
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'CandidateBondDelay')
```
---------
### DefaultCollatorCommission
 Default commission due to collators, is `CollatorCommission` storage value in genesis
#### Value
```python
200000000
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'DefaultCollatorCommission')
```
---------
### DelegationBondDelay
 Number of rounds that delegation {more, less} requests must wait before executable
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'DelegationBondDelay')
```
---------
### LeaveCandidatesDelay
 Number of rounds that candidates remain bonded before exit request is executable
#### Value
```python
2
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
2
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'LeaveDelegatorsDelay')
```
---------
### MaxCollatorCandidates
 Maximum collator candidates allowed
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MaxCollatorCandidates')
```
---------
### MaxDelegationsPerDelegator
 Maximum delegations per delegator
#### Value
```python
30
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MaxDelegationsPerDelegator')
```
---------
### MaxDelegatorsPerCandidate
 Maximum delegators counted per candidate
#### Value
```python
12
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MaxDelegatorsPerCandidate')
```
---------
### MaxTotalDelegatorsPerCandidate
 Maximum delegators allowed per candidate
#### Value
```python
25
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MaxTotalDelegatorsPerCandidate')
```
---------
### MinCandidateStk
 Minimum stake required for any account to be a collator candidate
#### Value
```python
1500000000000000000000000
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
10000000000000000000
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
10000000000000000
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MinDelegation')
```
---------
### MinSelectedCandidates
 Minimum number of selected candidates every round
#### Value
```python
25
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'MinSelectedCandidates')
```
---------
### NativeTokenId
 The native token used for payouts
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'NativeTokenId')
```
---------
### RevokeDelegationDelay
 Number of rounds that delegations remain bonded before revocation request is executable
#### Value
```python
2
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
### StakingIssuanceVault
 The account id that holds the liquidity mining issuance
#### Value
```python
'5EYCAe5ijiYfqsPVaS1Spou5yMsPSGJDSoCZr6iYazvbVgUy'
```
#### Python
```python
constant = substrate.get_constant('ParachainStaking', 'StakingIssuanceVault')
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
### ExceedMaxCollatorCandidates

---------
### ExceedMaxDelegationsPerDelegator

---------
### ExceedMaxTotalDelegatorsPerCandidate

---------
### InsufficientBalance

---------
### InvalidSchedule

---------
### MathError

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
### StakingLiquidityTokenAlreadyListed

---------
### StakingLiquidityTokenNotListed

---------
### TooLowCandidateCountToLeaveCandidates

---------
### TooLowCandidateCountWeightHintCancelLeaveCandidates

---------
### TooLowCandidateCountWeightHintJoinCandidates

---------
### TooLowCandidateDelegationCountToDelegate

---------
### TooLowCurrentStakingLiquidityTokensCount

---------
### TooLowDelegationCountToDelegate

---------
### TooLowDelegationCountToLeaveDelegators

---------