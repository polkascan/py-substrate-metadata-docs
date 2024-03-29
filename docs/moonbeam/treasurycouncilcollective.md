
# TreasuryCouncilCollective

---------
## Calls

---------
### close
See [`Pallet::close`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 
| index | `ProposalIndex` | 
| proposal_weight_bound | `Weight` | 
| length_bound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'TreasuryCouncilCollective', 'close', {
    'index': 'u32',
    'length_bound': 'u32',
    'proposal_hash': 'scale_info::12',
    'proposal_weight_bound': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
### disapprove_proposal
See [`Pallet::disapprove_proposal`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'TreasuryCouncilCollective', 'disapprove_proposal', {'proposal_hash': 'scale_info::12'}
)
```

---------
### execute
See [`Pallet::execute`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `Box<<T as Config<I>>::Proposal>` | 
| length_bound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'TreasuryCouncilCollective', 'execute', {
    'length_bound': 'u32',
    'proposal': 'Call',
}
)
```

---------
### propose
See [`Pallet::propose`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `MemberCount` | 
| proposal | `Box<<T as Config<I>>::Proposal>` | 
| length_bound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'TreasuryCouncilCollective', 'propose', {
    'length_bound': 'u32',
    'proposal': 'Call',
    'threshold': 'u32',
}
)
```

---------
### set_members
See [`Pallet::set_members`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_members | `Vec<T::AccountId>` | 
| prime | `Option<T::AccountId>` | 
| old_count | `MemberCount` | 

#### Python
```python
call = substrate.compose_call(
    'TreasuryCouncilCollective', 'set_members', {
    'new_members': ['[u8; 20]'],
    'old_count': 'u32',
    'prime': (None, '[u8; 20]'),
}
)
```

---------
### vote
See [`Pallet::vote`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `T::Hash` | 
| index | `ProposalIndex` | 
| approve | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'TreasuryCouncilCollective', 'vote', {
    'approve': 'bool',
    'index': 'u32',
    'proposal': 'scale_info::12',
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
| proposal_hash | `T::Hash` | ```scale_info::12```

---------
### Closed
A proposal was closed because its threshold was reached or after its duration was up.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```scale_info::12```
| yes | `MemberCount` | ```u32```
| no | `MemberCount` | ```u32```

---------
### Disapproved
A motion was not approved by the required threshold.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```scale_info::12```

---------
### Executed
A motion was executed; result will be `Ok` if it returned without error.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```scale_info::12```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}}```

---------
### MemberExecuted
A single member did some action; result will be `Ok` if it returned without error.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```scale_info::12```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}}```

---------
### Proposed
A motion (given hash) has been proposed (by given account) with a threshold (given
`MemberCount`).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```[u8; 20]```
| proposal_index | `ProposalIndex` | ```u32```
| proposal_hash | `T::Hash` | ```scale_info::12```
| threshold | `MemberCount` | ```u32```

---------
### Voted
A motion (given hash) has been voted on by given account, leaving
a tally (yes votes and no votes given respectively as `MemberCount`).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```[u8; 20]```
| proposal_hash | `T::Hash` | ```scale_info::12```
| voted | `bool` | ```bool```
| yes | `MemberCount` | ```u32```
| no | `MemberCount` | ```u32```

---------
## Storage functions

---------
### Members
 The current members of the collective. This is stored sorted (just by value).

#### Python
```python
result = substrate.query(
    'TreasuryCouncilCollective', 'Members', []
)
```

#### Return value
```python
['[u8; 20]']
```
---------
### Prime
 The prime member that helps determine the default vote behavior in case of absentations.

#### Python
```python
result = substrate.query(
    'TreasuryCouncilCollective', 'Prime', []
)
```

#### Return value
```python
'[u8; 20]'
```
---------
### ProposalCount
 Proposals so far.

#### Python
```python
result = substrate.query(
    'TreasuryCouncilCollective', 'ProposalCount', []
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
    'TreasuryCouncilCollective', 'ProposalOf', ['scale_info::12']
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
    'TreasuryCouncilCollective', 'Proposals', []
)
```

#### Return value
```python
['scale_info::12']
```
---------
### Voting
 Votes on a given proposal, if it is ongoing.

#### Python
```python
result = substrate.query(
    'TreasuryCouncilCollective', 'Voting', ['scale_info::12']
)
```

#### Return value
```python
{'ayes': ['[u8; 20]'], 'end': 'u32', 'index': 'u32', 'nays': ['[u8; 20]'], 'threshold': 'u32'}
```
---------
## Constants

---------
### MaxProposalWeight
 The maximum weight of a dispatch call that can be proposed and executed.
#### Value
```python
{'proof_size': 2621440, 'ref_time': 250000000000}
```
#### Python
```python
constant = substrate.get_constant('TreasuryCouncilCollective', 'MaxProposalWeight')
```
---------
## Errors

---------
### AlreadyInitialized
Members are already initialized!

---------
### DuplicateProposal
Duplicate proposals not allowed

---------
### DuplicateVote
Duplicate vote ignored

---------
### NotMember
Account is not a member

---------
### PrimeAccountNotMember
Prime account is not a member

---------
### ProposalMissing
Proposal must exist

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