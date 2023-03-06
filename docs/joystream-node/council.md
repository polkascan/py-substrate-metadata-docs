
# Council

---------
## Calls

---------
### announce_candidacy
Subscribe candidate

\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| membership_id | `T::MemberId` | 
| staking_account_id | `T::AccountId` | 
| reward_account_id | `T::AccountId` | 
| stake | `Balance<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'announce_candidacy', {
    'membership_id': 'u64',
    'reward_account_id': 'AccountId',
    'stake': 'u128',
    'staking_account_id': 'AccountId',
}
)
```

---------
### candidate_remark
Candidate makes a remark message

\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate_id | `T::MemberId` | 
| msg | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'candidate_remark', {
    'candidate_id': 'u64',
    'msg': 'Bytes',
}
)
```

---------
### councilor_remark
Councilor makes a remark message

\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| councilor_id | `T::MemberId` | 
| msg | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'councilor_remark', {
    'councilor_id': 'u64',
    'msg': 'Bytes',
}
)
```

---------
### fund_council_budget
Fund the council budget by a member.
&lt;weight&gt;

\#\# Weight
`O (1)` Doesn&\#x27;t depend on the state or parameters
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| member_id | `MemberId<T>` | 
| amount | `Balance<T>` | 
| rationale | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'fund_council_budget', {
    'amount': 'u128',
    'member_id': 'u64',
    'rationale': 'Bytes',
}
)
```

---------
### funding_request
Transfers funds from council budget to account

\# &lt;weight&gt;

\#\# weight
`O (F)` where:
`F` is the length of `funding_requests`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| funding_requests | `Vec<FundingRequestParameters<Balance<T>, T::AccountId>>` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'funding_request', {
    'funding_requests': [
        {
            'account': 'AccountId',
            'amount': 'u128',
        },
    ],
}
)
```

---------
### plan_budget_refill
Plan the next budget refill.

\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| next_refill | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'plan_budget_refill', {'next_refill': 'u32'}
)
```

---------
### release_candidacy_stake
Release candidacy stake that is no longer needed.

\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| membership_id | `T::MemberId` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'release_candidacy_stake', {'membership_id': 'u64'}
)
```

---------
### set_budget
Sets the budget balance.

\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| balance | `Balance<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'set_budget', {'balance': 'u128'}
)
```

---------
### set_budget_increment
Sets the budget refill amount

\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| budget_increment | `Balance<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'set_budget_increment', {'budget_increment': 'u128'}
)
```

---------
### set_candidacy_note
Set short description for the user&\#x27;s candidacy. Can be called anytime during user&\#x27;s candidacy.

\# &lt;weight&gt;

\#\# weight
`O (N)` where:
`N` is the size of `note` in kilobytes
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| membership_id | `T::MemberId` | 
| note | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'set_candidacy_note', {
    'membership_id': 'u64',
    'note': 'Bytes',
}
)
```

---------
### set_councilor_reward
Sets the councilor reward per block

\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| councilor_reward | `Balance<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'set_councilor_reward', {'councilor_reward': 'u128'}
)
```

---------
### withdraw_candidacy
Withdraw candidacy and release candidacy stake.

\# &lt;weight&gt;

\#\# weight
`O (1)`
- db:
   - `O(1)` doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| membership_id | `T::MemberId` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'withdraw_candidacy', {'membership_id': 'u64'}
)
```

---------
## Events

---------
### AnnouncingPeriodStarted
New council was elected
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BlockNumber` | ```u32```

---------
### BudgetBalanceSet
Budget balance was changed by the root.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
### BudgetIncrementUpdated
Budget increment has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
### BudgetRefill
Budget balance was increased by automatic refill.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
### BudgetRefillPlanned
The next budget refill was planned.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BlockNumber` | ```u32```

---------
### CandidacyNoteSet
The candidate has set a new note for their candidacy
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### CandidacyStakeRelease
Candidacy stake that was no longer needed was released
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```

---------
### CandidacyWithdraw
Candidate has withdrawn his candidacy
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```

---------
### CandidateRemarked
Candidate remark message
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### CouncilBudgetFunded
Fund the council budget.
Params:
- Member ID
- Amount of balance
- Rationale
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `Balance` | ```u128```
| None | `Vec<u8>` | ```Bytes```

---------
### CouncilorRemarked
Councilor remark message
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### CouncilorRewardUpdated
Councilor reward has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
### NewCandidate
New candidate announced
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `AccountId` | ```AccountId```
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### NewCouncilElected
New council was elected and appointed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<MemberId>` | ```['u64']```
| None | `BlockNumber` | ```u32```

---------
### NewCouncilNotElected
New council was not elected
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BlockNumber` | ```u32```

---------
### NotEnoughCandidates
Announcing period can&\#x27;t finish because of insufficient candidtate count
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BlockNumber` | ```u32```

---------
### RequestFunded
Request has been funded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### RewardPayment
The whole reward was paid to the council member.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### VotingPeriodStarted
Candidates are announced and voting starts
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
## Storage functions

---------
### AnnouncementPeriodNr
 Index of the current candidacy period. It is incremented everytime announcement period
 starts.

#### Python
```python
result = substrate.query(
    'Council', 'AnnouncementPeriodNr', []
)
```

#### Return value
```python
'u64'
```
---------
### Budget
 Budget for the council&#x27;s elected members rewards.

#### Python
```python
result = substrate.query(
    'Council', 'Budget', []
)
```

#### Return value
```python
'u128'
```
---------
### BudgetIncrement
 Amount of balance to be refilled every budget period

#### Python
```python
result = substrate.query(
    'Council', 'BudgetIncrement', []
)
```

#### Return value
```python
'u128'
```
---------
### Candidates
 Map of all candidates that ever candidated and haven&#x27;t unstake yet.

#### Python
```python
result = substrate.query(
    'Council', 'Candidates', ['u64']
)
```

#### Return value
```python
{
    'cycle_id': 'u64',
    'note_hash': (None, '[u8; 32]'),
    'reward_account_id': 'AccountId',
    'stake': 'u128',
    'staking_account_id': 'AccountId',
    'vote_power': 'u128',
}
```
---------
### CouncilMembers
 Current council members

#### Python
```python
result = substrate.query(
    'Council', 'CouncilMembers', []
)
```

#### Return value
```python
[
    {
        'last_payment_block': 'u32',
        'membership_id': 'u64',
        'reward_account_id': 'AccountId',
        'stake': 'u128',
        'staking_account_id': 'AccountId',
        'unpaid_reward': 'u128',
    },
]
```
---------
### CouncilorReward
 Councilor reward per block

#### Python
```python
result = substrate.query(
    'Council', 'CouncilorReward', []
)
```

#### Return value
```python
'u128'
```
---------
### NextBudgetRefill
 The next block in which the budget will be increased.

#### Python
```python
result = substrate.query(
    'Council', 'NextBudgetRefill', []
)
```

#### Return value
```python
'u32'
```
---------
### NextRewardPayments
 The next block in which the elected council member rewards will be payed.

#### Python
```python
result = substrate.query(
    'Council', 'NextRewardPayments', []
)
```

#### Return value
```python
'u32'
```
---------
### Stage
 Current council voting stage

#### Python
```python
result = substrate.query(
    'Council', 'Stage', []
)
```

#### Return value
```python
{
    'changed_at': 'u32',
    'stage': {
        'Announcing': {'candidates_count': 'u32', 'ends_at': 'u32'},
        'Election': {'candidates_count': 'u32'},
        'Idle': {'ends_at': 'u32'},
    },
}
```
---------
## Constants

---------
### AnnouncingPeriodDuration
 Duration of annoncing period
#### Value
```python
129600
```
#### Python
```python
constant = substrate.get_constant('Council', 'AnnouncingPeriodDuration')
```
---------
### BudgetRefillPeriod
 Interval between automatic budget refills.
#### Value
```python
14400
```
#### Python
```python
constant = substrate.get_constant('Council', 'BudgetRefillPeriod')
```
---------
### CandidacyLockId
 Exports const - candidacy lock id.
#### Value
```python
'0x63616e6469646163'
```
#### Python
```python
constant = substrate.get_constant('Council', 'CandidacyLockId')
```
---------
### CouncilSize
 Council member count
#### Value
```python
3
```
#### Python
```python
constant = substrate.get_constant('Council', 'CouncilSize')
```
---------
### CouncilorLockId
 Exports const - councilor lock id.
#### Value
```python
'0x636f756e63696c6f'
```
#### Python
```python
constant = substrate.get_constant('Council', 'CouncilorLockId')
```
---------
### ElectedMemberRewardPeriod
 Interval for automatic reward payments.
#### Value
```python
14400
```
#### Python
```python
constant = substrate.get_constant('Council', 'ElectedMemberRewardPeriod')
```
---------
### IdlePeriodDuration
 Duration of idle period
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Council', 'IdlePeriodDuration')
```
---------
### MinCandidateStake
 Minimum stake candidate has to lock
#### Value
```python
1666666666660000
```
#### Python
```python
constant = substrate.get_constant('Council', 'MinCandidateStake')
```
---------
### MinNumberOfExtraCandidates
 Minimum number of extra candidates needed for the valid election.
 Number of total candidates is equal to council size plus extra candidates.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Council', 'MinNumberOfExtraCandidates')
```
---------
## Errors

---------
### ArithmeticError
Unexpected arithmetic error (overflow / underflow)

---------
### BadOrigin
Origin is invalid.

---------
### CandidacyStakeTooLow
Candidate haven&\#x27;t provided sufficient stake.

---------
### CandidateDoesNotExist
Candidate id not found

---------
### CantCandidateNow
User tried to announce candidacy outside of the candidacy announcement period.

---------
### CantCandidateTwice
User tried to announce candidacy twice in the same elections.

---------
### CantReleaseStakeNow
User tried to release stake outside of the revealing period.

---------
### CantVoteForYourself
Candidate can&\#x27;t vote for himself.

---------
### CantWithdrawCandidacyNow
Can&\#x27;t withdraw candidacy outside of the candidacy announcement period.

---------
### ConflictingStake
User tried to announce candidacy with an account that has the conflicting type of stake
with candidacy stake and has not enough balance for staking for both purposes.

---------
### EmptyFundingRequests
Funding requests without recieving accounts

---------
### InsufficientBalanceForStaking
Insufficient balance for candidacy staking.

---------
### InsufficientBalanceForTransfer
Cannot withdraw: insufficient budget balance.

---------
### InsufficientFundsForFundingRequest
Insufficent funds in council for executing &\#x27;Funding Request&\#x27;

---------
### InsufficientTokensForFunding
Insufficient tokens for funding (on member controller account)

---------
### InvalidAccountToStakeReuse
The combination of membership id and account id is invalid for unstaking an existing
candidacy stake.

---------
### MemberIdNotMatchAccount
Invalid membership.

---------
### NoStake
User tried to release stake when no stake exists.

---------
### NotCandidatingNow
User tried to withdraw candidacy when not candidating.

---------
### NotCouncilor
The member is not a councilor.

---------
### RepeatedFundRequestAccount
The same account is recieving funds from the same request twice

---------
### StakeStillNeeded
Council member and candidates can&\#x27;t withdraw stake yet.

---------
### ZeroBalanceFundRequest
Fund request no balance

---------
### ZeroTokensFunding
Trying to fund with zero tokens

---------