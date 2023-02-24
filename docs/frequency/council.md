
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
    'proposal_hash': '[u8; 32]',
    'proposal_weight_bound': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
### close_old_weight
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 
| index | `ProposalIndex` | 
| proposal_weight_bound | `OldWeight` | 
| length_bound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Council', 'close_old_weight', {
    'index': 'u32',
    'length_bound': 'u32',
    'proposal_hash': '[u8; 32]',
    'proposal_weight_bound': 'u64',
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
    'Council', 'disapprove_proposal', {'proposal_hash': '[u8; 32]'}
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
    'proposal': '[u8; 32]',
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
| proposal_hash | `T::Hash` | ```[u8; 32]```

---------
### Closed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| yes | `MemberCount` | ```u32```
| no | `MemberCount` | ```u32```

---------
### Disapproved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```

---------
### Executed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### MemberExecuted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### Proposed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| proposal_index | `ProposalIndex` | ```u32```
| proposal_hash | `T::Hash` | ```[u8; 32]```
| threshold | `MemberCount` | ```u32```

---------
### Voted
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
    'Council', 'ProposalOf', ['[u8; 32]']
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
['[u8; 32]']
```
---------
### Voting

#### Python
```python
result = substrate.query(
    'Council', 'Voting', ['[u8; 32]']
)
```

#### Return value
```python
{'ayes': ['AccountId'], 'end': 'u32', 'index': 'u32', 'nays': ['AccountId'], 'threshold': 'u32'}
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