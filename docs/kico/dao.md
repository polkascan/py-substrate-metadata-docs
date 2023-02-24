
# Dao

---------
## Calls

---------
### close
The user close the proposal.

Everyone can do it
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyIdOf<T>` | 
| ico_index | `u32` | 
| proposal_hash | `T::Hash` | 
| index | `ProposalIndex` | 
| proposal_weight_bound | `Weight` | 
| length_bound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Dao', 'close', {
    'currency_id': 'u32',
    'ico_index': 'u32',
    'index': 'u32',
    'length_bound': 'u32',
    'proposal_hash': '[u8; 32]',
    'proposal_weight_bound': 'u64',
}
)
```

---------
### disapprove_proposal
The root user disapprove the proposal.

Referendum
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyIdOf<T>` | 
| proposal_hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Dao', 'disapprove_proposal', {
    'currency_id': 'u32',
    'proposal_hash': '[u8; 32]',
}
)
```

---------
### propose
The user makes a proposal.

Must be a member of the project ICO.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyIdOf<T>` | 
| ico_index | `u32` | 
| threshold | `Percent` | 
| proposal | `Box<<T as Config>::Proposal>` | 
| reason | `Vec<u8>` | 
| length_bound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Dao', 'propose', {
    'currency_id': 'u32',
    'ico_index': 'u32',
    'length_bound': 'u32',
    'proposal': 'Call',
    'reason': 'Bytes',
    'threshold': 'u8',
}
)
```

---------
### vote
Users vote on proposals.

Must be a member of the project ICO
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyIdOf<T>` | 
| ico_index | `u32` | 
| proposal | `T::Hash` | 
| index | `ProposalIndex` | 
| approve | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Dao', 'vote', {
    'approve': 'bool',
    'currency_id': 'u32',
    'ico_index': 'u32',
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
\[proposal_hash\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Hash` | ```[u8; 32]```

---------
### Closed
A proposal was closed because its threshold was reached or after its duration was up.
\[proposal_hash, yes, no\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Hash` | ```[u8; 32]```
| None | `MultiBalanceOf<T>` | ```u128```
| None | `MultiBalanceOf<T>` | ```u128```

---------
### Disapproved
A motion was not approved by the required threshold.
\[proposal_hash\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Hash` | ```[u8; 32]```

---------
### Executed
A motion was executed; result will be `Ok` if it returned without error.
\[proposal_hash, result\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Hash` | ```[u8; 32]```
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### MemberExecuted
A single member did some action; result will be `Ok` if it returned without error.
\[proposal_hash, result\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Hash` | ```[u8; 32]```
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### Proposed
A motion (given hash) has been proposed (by given account) with a threshold (given
`MemberCount`).
\[account, proposal_index, proposal_hash, threshold\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `ProposalIndex` | ```u32```
| None | `T::Hash` | ```[u8; 32]```
| None | `Percent` | ```u8```

---------
### Voted
A motion (given hash) has been voted on by given account, leaving
a tally (yes votes and no votes given respectively as `MemberCount`).
\[account, proposal_hash, voted, yes, no\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::Hash` | ```[u8; 32]```
| None | `bool` | ```bool```
| None | `MultiBalanceOf<T>` | ```u128```
| None | `MultiBalanceOf<T>` | ```u128```
| None | `MultiBalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### ProposalCount

#### Python
```python
result = substrate.query(
    'Dao', 'ProposalCount', ['u32']
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
    'Dao', 'ProposalOf', ['u32', '[u8; 32]']
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
    'Dao', 'Proposals', ['u32']
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
    'Dao', 'Voting', ['u32', '[u8; 32]']
)
```

#### Return value
```python
{
    'ayes': [('AccountId', 'u128')],
    'end': 'u32',
    'index': 'u32',
    'nays': [('AccountId', 'u128')],
    'reason': 'Bytes',
    'threshold': 'u8',
}
```
---------
## Constants

---------
### MaxProposals
 Maximum number of proposals allowed to be active in parallel.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Dao', 'MaxProposals')
```
---------
### MotionDuration
 The time-out for council motions.
#### Value
```python
36000
```
#### Python
```python
constant = substrate.get_constant('Dao', 'MotionDuration')
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
### NotIcoMember

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
### VoteExpire

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