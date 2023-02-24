
# DaoCollective

---------
## Calls

---------
### close
Close a vote that is either approved, disapproved or whose voting period has ended.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| proposal_hash | `T::Hash` | 
| index | `ProposalIndex` | 

#### Python
```python
call = substrate.compose_call(
    'DaoCollective', 'close', {
    'dao_id': 'u64',
    'index': 'u32',
    'proposal_hash': '[u8; 32]',
}
)
```

---------
### disapprove_proposal
Disapprove a proposal, close, and remove it from the system, regardless of its current
state.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| proposal_hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'DaoCollective', 'disapprove_proposal', {
    'dao_id': 'u64',
    'proposal_hash': '[u8; 32]',
}
)
```

---------
### execute
Dispatch a proposal from a member using the `Member` origin.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| proposal | `Box<<T as Config<I>>::Proposal>` | 

#### Python
```python
call = substrate.compose_call(
    'DaoCollective', 'execute', {'dao_id': 'u64', 'proposal': 'Call'}
)
```

---------
### propose
Add a new proposal to either be voted on or executed directly.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| threshold | `MemberCount` | 
| proposal | `Box<<T as Config<I>>::Proposal>` | 

#### Python
```python
call = substrate.compose_call(
    'DaoCollective', 'propose', {
    'dao_id': 'u64',
    'proposal': 'Call',
    'threshold': 'u32',
}
)
```

---------
### set_ensure_origin_for_every_call
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| call | `Box<<T as dao::Config>::Call>` | 
| ensure | `DoAsEnsureOrigin<Proportion<MemberCount>, MemberCount>` | 

#### Python
```python
call = substrate.compose_call(
    'DaoCollective', 'set_ensure_origin_for_every_call', {
    'call': 'Call',
    'dao_id': 'u64',
    'ensure': {
        'Member': None,
        'Members': 'u32',
        'NoPermission': None,
        'Proportion': {
            'AtLeast': ('u32', 'u32'),
            'MoreThan': ('u32', 'u32'),
        },
        'Root': None,
    },
}
)
```

---------
### set_max_members
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| max | `MemberCount` | 

#### Python
```python
call = substrate.compose_call(
    'DaoCollective', 'set_max_members', {'dao_id': 'u64', 'max': 'u32'}
)
```

---------
### set_max_proposals
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| max | `ProposalIndex` | 

#### Python
```python
call = substrate.compose_call(
    'DaoCollective', 'set_max_proposals', {'dao_id': 'u64', 'max': 'u32'}
)
```

---------
### set_motion_duration
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| duration | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'DaoCollective', 'set_motion_duration', {'dao_id': 'u64', 'duration': 'u32'}
)
```

---------
### vote
Add an aye or nay vote for the sender to the given proposal.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| proposal | `T::Hash` | 
| index | `ProposalIndex` | 
| approve | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'DaoCollective', 'vote', {
    'approve': 'bool',
    'dao_id': 'u64',
    'index': 'u32',
    'proposal': '[u8; 32]',
}
)
```

---------
## Events

---------
### Approved
A motion was approved by the required threshold.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```

---------
### Closed
A proposal was closed because its threshold was reached or after its duration was up.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| yes | `MemberCount` | ```u32```
| no | `MemberCount` | ```u32```

---------
### Disapproved
A motion was not approved by the required threshold.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```

---------
### DoAsDone
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sudo_result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### Executed
A motion was executed; result will be `Ok` if it returned without error.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### MemberExecuted
A single member did some action; result will be `Ok` if it returned without error.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### Proposed
A motion (given hash) has been proposed (by given account) with a threshold (given
`MemberCount`).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| proposal_index | `ProposalIndex` | ```u32```
| proposal_hash | `T::Hash` | ```[u8; 32]```
| threshold | `MemberCount` | ```u32```

---------
### SetEnsure
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::DaoId` | ```u64```
| None | `T::CallId` | ```u32```
| None | `DoAsEnsureOrigin<Proportion<MemberCount>, MemberCount>` | ```{'Proportion': {'MoreThan': ('u32', 'u32'), 'AtLeast': ('u32', 'u32')}, 'Member': None, 'Members': 'u32', 'Root': None, 'NoPermission': None}```

---------
### SetMaxMembers
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dao_id | `T::DaoId` | ```u64```
| max | `MemberCount` | ```u32```

---------
### SetMaxProposals
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dao_id | `T::DaoId` | ```u64```
| max | `ProposalIndex` | ```u32```

---------
### SetMotionDuration
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dao_id | `T::DaoId` | ```u64```
| duration | `T::BlockNumber` | ```u32```

---------
### Voted
A motion (given hash) has been voted on by given account, leaving
a tally (yes votes and no votes given respectively as `MemberCount`).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| proposal_hash | `T::Hash` | ```[u8; 32]```
| voted | `bool` | ```bool```
| yes | `MemberCount` | ```u32```
| no | `MemberCount` | ```u32```

---------
## Storage functions

---------
### CollectiveMembers

#### Python
```python
result = substrate.query(
    'DaoCollective', 'CollectiveMembers', ['u64']
)
```

#### Return value
```python
['AccountId']
```
---------
### Ensures

#### Python
```python
result = substrate.query(
    'DaoCollective', 'Ensures', ['u64', 'u32']
)
```

#### Return value
```python
{
    'Member': None,
    'Members': 'u32',
    'NoPermission': None,
    'Proportion': {'AtLeast': ('u32', 'u32'), 'MoreThan': ('u32', 'u32')},
    'Root': None,
}
```
---------
### MaxMembers
 The maximum number of members supported by the pallet.

#### Python
```python
result = substrate.query(
    'DaoCollective', 'MaxMembers', ['u64']
)
```

#### Return value
```python
'u32'
```
---------
### MaxProposals
 Maximum number of proposals allowed to be active in parallel.

#### Python
```python
result = substrate.query(
    'DaoCollective', 'MaxProposals', ['u64']
)
```

#### Return value
```python
'u32'
```
---------
### MotionDuration
 The time-out for council motions.

#### Python
```python
result = substrate.query(
    'DaoCollective', 'MotionDuration', ['u64']
)
```

#### Return value
```python
'u32'
```
---------
### ProposalCount
 Proposals so far.

#### Python
```python
result = substrate.query(
    'DaoCollective', 'ProposalCount', ['u64']
)
```

#### Return value
```python
'u32'
```
---------
### ProposalOf
 Actual proposal for a given hash, if it&#x27;s current.

#### Python
```python
result = substrate.query(
    'DaoCollective', 'ProposalOf', ['u64', '[u8; 32]']
)
```

#### Return value
```python
'Call'
```
---------
### Proposals
 The hashes of the active proposals.

#### Python
```python
result = substrate.query(
    'DaoCollective', 'Proposals', ['u64']
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### Voting
 Votes on a given proposal, if it is ongoing.

#### Python
```python
result = substrate.query(
    'DaoCollective', 'Voting', ['u64', '[u8; 32]']
)
```

#### Return value
```python
{'ayes': ['AccountId'], 'end': 'u32', 'index': 'u32', 'nays': ['AccountId'], 'threshold': 'u32'}
```
---------
## Constants

---------
### MaxMembersForSystem
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('DaoCollective', 'MaxMembersForSystem')
```
---------
## Errors

---------
### AlreadyInitialized
Members are already initialized!

---------
### BadOrigin

---------
### DuplicateProposal
Duplicate proposals not allowed

---------
### DuplicateVote
Duplicate vote ignored

---------
### MembersNotExsits

---------
### NotDaoAccount

---------
### NotMember
Account is not a member

---------
### ProportionErr

---------
### ProposalMissing
Proposal must exist

---------
### ThresholdWrong

---------
### TooEarly
The close call was made too early, before the end of the voting.

---------
### TooManyProposals
There can only be a maximum of `MaxProposals` active proposals.

---------
### WrongIndex
Mismatched index

---------
### WrongProposalLength
The given length bound for the proposal was too low.

---------
### WrongProposalWeight
The given weight bound for the proposal was too low.

---------