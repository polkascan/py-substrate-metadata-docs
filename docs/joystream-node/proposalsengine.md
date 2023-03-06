
# ProposalsEngine

---------
## Calls

---------
### cancel_proposal
Cancel a proposal by its original proposer.

&lt;weight&gt;

\#\# Weight
`O (L)` where:
- `L` is the total number of locks in `Balances`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposer_id | `MemberId<T>` | 
| proposal_id | `T::ProposalId` | 

#### Python
```python
call = substrate.compose_call(
    'ProposalsEngine', 'cancel_proposal', {
    'proposal_id': 'u32',
    'proposer_id': 'u64',
}
)
```

---------
### proposer_remark
Proposer Remark

&lt;weight&gt;

\#\# Weight
`O (1)` doesn&\#x27;t depend on the state or parameters
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_id | `T::ProposalId` | 
| proposer_id | `MemberId<T>` | 
| msg | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'ProposalsEngine', 'proposer_remark', {
    'msg': 'Bytes',
    'proposal_id': 'u32',
    'proposer_id': 'u64',
}
)
```

---------
### veto_proposal
Veto a proposal. Must be root.

&lt;weight&gt;

\#\# Weight
`O (1)` doesn&\#x27;t depend on the state or parameters
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_id | `T::ProposalId` | 

#### Python
```python
call = substrate.compose_call(
    'ProposalsEngine', 'veto_proposal', {'proposal_id': 'u32'}
)
```

---------
### vote
Vote extrinsic. Conditions:  origin must allow votes.

&lt;weight&gt;

\#\# Weight
`O (R)` where:
- `R` is the size of `rationale` in kilobytes
- DB:
   - O(1) doesn&\#x27;t depend on the state or paraemters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| voter_id | `MemberId<T>` | 
| proposal_id | `T::ProposalId` | 
| vote | `VoteKind` | 
| rationale | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'ProposalsEngine', 'vote', {
    'proposal_id': 'u32',
    'rationale': 'Bytes',
    'vote': (
        'Approve',
        'Reject',
        'Slash',
        'Abstain',
    ),
    'voter_id': 'u64',
}
)
```

---------
## Events

---------
### ProposalCancelled
Emits on a proposal being cancelled
Params:
- Member Id of the proposer
- Id of the proposal
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `ProposalId` | ```u32```

---------
### ProposalDecisionMade
Emits on getting a proposal status decision.
Params:
- Id of a proposal.
- Proposal decision
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ProposalId` | ```u32```
| None | `ProposalDecision` | ```{'Canceled': None, 'CanceledByRuntime': None, 'Vetoed': None, 'Rejected': None, 'Slashed': None, 'Expired': None, 'Approved': ('PendingExecution', 'PendingConstitutionality')}```

---------
### ProposalExecuted
Emits on proposal execution.
Params:
- Id of a updated proposal.
- Proposal execution status.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ProposalId` | ```u32```
| None | `ExecutionStatus` | ```{'Executed': None, 'ExecutionFailed': {'error': 'Bytes'}}```

---------
### ProposalStatusUpdated
Emits on proposal creation.
Params:
- Id of a proposal.
- New proposal status.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ProposalId` | ```u32```
| None | `ProposalStatus<BlockNumber>` | ```{'Active': None, 'PendingExecution': 'u32', 'PendingConstitutionality': None}```

---------
### ProposerRemarked
Emits on proposer making a remark
- proposer id
- proposal id
- message
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `ProposalId` | ```u32```
| None | `Vec<u8>` | ```Bytes```

---------
### Voted
Emits on voting for the proposal
Params:
- Voter - member id of a voter.
- Id of a proposal.
- Kind of vote.
- Rationale.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MemberId` | ```u64```
| None | `ProposalId` | ```u32```
| None | `VoteKind` | ```('Approve', 'Reject', 'Slash', 'Abstain')```
| None | `Vec<u8>` | ```Bytes```

---------
## Storage functions

---------
### ActiveProposalCount
 Count of active proposals.

#### Python
```python
result = substrate.query(
    'ProposalsEngine', 'ActiveProposalCount', []
)
```

#### Return value
```python
'u32'
```
---------
### DispatchableCallCode
 Map proposal executable code by proposal id.

#### Python
```python
result = substrate.query(
    'ProposalsEngine', 'DispatchableCallCode', ['u32']
)
```

#### Return value
```python
'Bytes'
```
---------
### ProposalCount
 Count of all proposals that have been created.

#### Python
```python
result = substrate.query(
    'ProposalsEngine', 'ProposalCount', []
)
```

#### Return value
```python
'u32'
```
---------
### Proposals
 Map proposal by its id.

#### Python
```python
result = substrate.query(
    'ProposalsEngine', 'Proposals', ['u32']
)
```

#### Return value
```python
{
    'activated_at': 'u32',
    'exact_execution_block': (None, 'u32'),
    'nr_of_council_confirmations': 'u32',
    'parameters': {
        'approval_quorum_percentage': 'u32',
        'approval_threshold_percentage': 'u32',
        'constitutionality': 'u32',
        'grace_period': 'u32',
        'required_stake': (None, 'u128'),
        'slashing_quorum_percentage': 'u32',
        'slashing_threshold_percentage': 'u32',
        'voting_period': 'u32',
    },
    'proposer_id': 'u64',
    'staking_account_id': (None, 'AccountId'),
    'status': {
        'Active': None,
        'PendingConstitutionality': None,
        'PendingExecution': 'u32',
    },
    'voting_results': {
        'abstentions': 'u32',
        'approvals': 'u32',
        'rejections': 'u32',
        'slashes': 'u32',
    },
}
```
---------
### VoteExistsByProposalByVoter
 Double map for preventing duplicate votes. Should be cleaned after usage.

#### Python
```python
result = substrate.query(
    'ProposalsEngine', 'VoteExistsByProposalByVoter', ['u32', 'u64']
)
```

#### Return value
```python
('Approve', 'Reject', 'Slash', 'Abstain')
```
---------
## Constants

---------
### CancellationFee
 Exports const - the fee is applied when cancel the proposal. A fee would be slashed (burned).
#### Value
```python
166666666666
```
#### Python
```python
constant = substrate.get_constant('ProposalsEngine', 'CancellationFee')
```
---------
### DescriptionMaxLength
 Exports const -  max allowed proposal description length.
#### Value
```python
3000
```
#### Python
```python
constant = substrate.get_constant('ProposalsEngine', 'DescriptionMaxLength')
```
---------
### MaxActiveProposalLimit
 Exports const -  max simultaneous active proposals number.
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('ProposalsEngine', 'MaxActiveProposalLimit')
```
---------
### RejectionFee
 Exports const -  the fee is applied when the proposal gets rejected. A fee would
 be slashed (burned).
#### Value
```python
833333333330
```
#### Python
```python
constant = substrate.get_constant('ProposalsEngine', 'RejectionFee')
```
---------
### StakingHandlerLockId
 Exports const - staking handler lock id.
#### Value
```python
'0x70726f706f73616c'
```
#### Python
```python
constant = substrate.get_constant('ProposalsEngine', 'StakingHandlerLockId')
```
---------
### TitleMaxLength
 Exports const -  max allowed proposal title length.
#### Value
```python
40
```
#### Python
```python
constant = substrate.get_constant('ProposalsEngine', 'TitleMaxLength')
```
---------
## Errors

---------
### AlreadyVoted
The proposal have been already voted on

---------
### ArithmeticError
Unexpected arithmetic error (overflow / underflow)

---------
### ConflictingStakes
The conflicting stake discovered. Cannot stake.

---------
### DescriptionIsTooLong
Description is too long

---------
### EmptyDescriptionProvided
Proposal cannot have an empty body

---------
### EmptyStake
Stake cannot be empty with this proposal

---------
### EmptyTitleProvided
Proposal cannot have an empty title&quot;

---------
### InsufficientBalanceForStake
There is not enough balance for a stake.

---------
### InvalidExactExecutionBlock
Exact execution block cannot be less than current_block.

---------
### InvalidParameterApprovalThreshold
Approval threshold cannot be zero

---------
### InvalidParameterSlashingThreshold
Slashing threshold cannot be zero

---------
### InvalidStakingAccountForMember
Staking account doesn&\#x27;t belong to a member.

---------
### MaxActiveProposalNumberExceeded
Max active proposals number exceeded

---------
### MaxDispatchableCallCodeSizeExceeded
The size of encoded dispatchable call to be executed by the proposal is too big

---------
### NotAuthor
Not an author

---------
### ProposalFinalized
Proposal is finalized already

---------
### ProposalHasVotes
Disallow to cancel the proposal if there are any votes on it.

---------
### ProposalNotFound
The proposal does not exist

---------
### RequireRootOrigin
Require root origin in extrinsics

---------
### StakeDiffersFromRequired
Stake differs from the proposal requirements

---------
### StakeShouldBeEmpty
Stake should be empty for this proposal

---------
### TitleIsTooLong
Title is too long

---------
### ZeroExactExecutionBlock
Exact execution block cannot be zero.

---------