
# ParasDisputes

---------
## Calls

---------
### force_unfreeze
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
| None | `CandidateHash` | ```[u8; 32]```
| None | `DisputeResult` | ```('Valid', 'Invalid')```

---------
### DisputeInitiated
A dispute has been initiated. \[candidate hash, dispute location\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CandidateHash` | ```[u8; 32]```
| None | `DisputeLocation` | ```('Local', 'Remote')```

---------
### DisputeTimedOut
A dispute has timed out due to insufficient participation.
`\[para id, candidate hash\]`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CandidateHash` | ```[u8; 32]```

---------
### Revert
A dispute has concluded with supermajority against a candidate.
Block authors should no longer build on top of this head and should
instead revert the block at the given height. This should be the
number of the child of the last known valid block in the chain.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```

---------
## Storage functions

---------
### Disputes
 All ongoing or concluded disputes for the last several sessions.

#### Python
```python
result = substrate.query(
    'ParasDisputes', 'Disputes', ['u32', '[u8; 32]']
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
    'ParasDisputes', 'Included', ['u32', '[u8; 32]']
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
### SpamSlots
 Maps session indices to a vector indicating the number of potentially-spam disputes
 each validator is participating in. Potentially-spam disputes are remote disputes which have
 fewer than `byzantine_threshold + 1` validators.

 The i&#x27;th entry of the vector corresponds to the i&#x27;th validator in the session.

#### Python
```python
result = substrate.query(
    'ParasDisputes', 'SpamSlots', ['u32']
)
```

#### Return value
```python
['u32']
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
### PotentialSpam
Too many spam slots used by some specific validator.

---------
### SingleSidedDispute
A dispute where there are only votes on one side.

---------
### ValidatorIndexOutOfBounds
Validator index on statement is out of bounds for session.

---------