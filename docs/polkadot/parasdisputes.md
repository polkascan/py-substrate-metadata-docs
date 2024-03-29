
# ParasDisputes

---------
## Calls

---------
### force_unfreeze
See [`Pallet::force_unfreeze`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParasDisputes', 'force_unfreeze', {}
)
```

---------
## Events

---------
### DisputeConcluded
A dispute has concluded for or against a candidate.
`\[para id, candidate hash, dispute result\]`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CandidateHash` | ```scale_info::12```
| None | `DisputeResult` | ```('Valid', 'Invalid')```

---------
### DisputeInitiated
A dispute has been initiated. \[candidate hash, dispute location\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CandidateHash` | ```scale_info::12```
| None | `DisputeLocation` | ```('Local', 'Remote')```

---------
### Revert
A dispute has concluded with supermajority against a candidate.
Block authors should no longer build on top of this head and should
instead revert the block at the given height. This should be the
number of the child of the last known valid block in the chain.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BlockNumberFor<T>` | ```u32```

---------
## Storage functions

---------
### BackersOnDisputes
 Backing votes stored for each dispute.
 This storage is used for slashing.

#### Python
```python
result = substrate.query(
    'ParasDisputes', 'BackersOnDisputes', ['u32', 'scale_info::12']
)
```

#### Return value
```python
'scale_info::748'
```
---------
### Disputes
 All ongoing or concluded disputes for the last several sessions.

#### Python
```python
result = substrate.query(
    'ParasDisputes', 'Disputes', ['u32', 'scale_info::12']
)
```

#### Return value
```python
{
    'concluded_at': (None, 'u32'),
    'start': 'u32',
    'validators_against': 'BitVec',
    'validators_for': 'BitVec',
}
```
---------
### Frozen
 Whether the chain is frozen. Starts as `None`. When this is `Some`,
 the chain will not accept any new parachain blocks for backing or inclusion,
 and its value indicates the last valid block number in the chain.
 It can only be set back to `None` by governance intervention.

#### Python
```python
result = substrate.query(
    'ParasDisputes', 'Frozen', []
)
```

#### Return value
```python
(None, 'u32')
```
---------
### Included
 All included blocks on the chain, as well as the block number in this chain that
 should be reverted back to if the candidate is disputed and determined to be invalid.

#### Python
```python
result = substrate.query(
    'ParasDisputes', 'Included', ['u32', 'scale_info::12']
)
```

#### Return value
```python
'u32'
```
---------
### LastPrunedSession
 The last pruned session, if any. All data stored by this module
 references sessions.

#### Python
```python
result = substrate.query(
    'ParasDisputes', 'LastPrunedSession', []
)
```

#### Return value
```python
'u32'
```
---------
## Errors

---------
### AncientDisputeStatement
Ancient dispute statement provided.

---------
### DuplicateDisputeStatementSets
Duplicate dispute statement sets provided.

---------
### DuplicateStatement
Validator vote submitted more than once to dispute.

---------
### InvalidSignature
Invalid signature on statement.

---------
### MaliciousBacker
A dispute vote from a malicious backer.

---------
### MissingBackingVotes
No backing votes were provides along dispute statements.

---------
### SingleSidedDispute
A dispute where there are only votes on one side.

---------
### UnconfirmedDispute
Unconfirmed dispute statement sets provided.

---------
### ValidatorIndexOutOfBounds
Validator index on statement is out of bounds for session.

---------