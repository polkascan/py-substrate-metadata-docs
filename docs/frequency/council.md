
# Council

---------
## Calls

---------
### close
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
    'Council', 'close', {
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
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'disapprove_proposal', {'proposal_hash': 'scale_info::12'}
)
```

---------
### execute
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `Box<<T as Config<I>>::Proposal>` | 
| length_bound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'execute', {
    'length_bound': 'u32',
    'proposal': 'Call',
}
)
```

---------
### propose
#### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `MemberCount` | 
| proposal | `Box<<T as Config<I>>::Proposal>` | 
| length_bound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'propose', {
    'length_bound': 'u32',
    'proposal': 'Call',
    'threshold': 'u32',
}
)
```

---------
### set_members
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_members | `Vec<T::AccountId>` | 
| prime | `Option<T::AccountId>` | 
| old_count | `MemberCount` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'set_members', {
    'new_members': ['AccountId'],
    'old_count': 'u32',
    'prime': (None, 'AccountId'),
}
)
```

---------
### vote
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `T::Hash` | 
| index | `ProposalIndex` | 
| approve | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'vote', {
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
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```scale_info::12```

---------
### Closed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```scale_info::12```
| yes | `MemberCount` | ```u32```
| no | `MemberCount` | ```u32```

---------
### Disapproved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```scale_info::12```

---------
### Executed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```scale_info::12```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}}```

---------
### MemberExecuted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```scale_info::12```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}}```

---------
### Proposed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| proposal_index | `ProposalIndex` | ```u32```
| proposal_hash | `T::Hash` | ```scale_info::12```
| threshold | `MemberCount` | ```u32```

---------
### Voted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| proposal_hash | `T::Hash` | ```scale_info::12```
| voted | `bool` | ```bool```
| yes | `MemberCount` | ```u32```
| no | `MemberCount` | ```u32```

---------
## Storage functions

---------
### Members

#### Python
```python
result = substrate.query(
    'Council', 'Members', []
)
```

#### Return value
```python
['AccountId']
```
---------
### Prime

#### Python
```python
result = substrate.query(
    'Council', 'Prime', []
)
```

#### Return value
```python
'AccountId'
```
---------
### ProposalCount

#### Python
```python
result = substrate.query(
    'Council', 'ProposalCount', []
)
```

#### Return value
```python
'u32'
```
---------
### ProposalOf

#### Python
```python
result = substrate.query(
    'Council', 'ProposalOf', ['scale_info::12']
)
```

#### Return value
```python
'Call'
```
---------
### Proposals

#### Python
```python
result = substrate.query(
    'Council', 'Proposals', []
)
```

#### Return value
```python
['scale_info::12']
```
---------
### Voting

#### Python
```python
result = substrate.query(
    'Council', 'Voting', ['scale_info::12']
)
```

#### Return value
```python
{'ayes': ['AccountId'], 'end': 'u32', 'index': 'u32', 'nays': ['AccountId'], 'threshold': 'u32'}
```
---------
## Constants

---------
### MaxProposalWeight
#### Value
```python
{'proof_size': 2621440, 'ref_time': 250000000000}
```
#### Python
```python
constant = substrate.get_constant('Council', 'MaxProposalWeight')
```
---------
## Errors

---------
### AlreadyInitialized

---------
### DuplicateProposal

---------
### DuplicateVote

---------
### NotMember

---------
### PrimeAccountNotMember

---------
### ProposalMissing

---------
### TooEarly

---------
### TooManyProposals

---------
### WrongIndex

---------
### WrongProposalLength

---------
### WrongProposalWeight

---------