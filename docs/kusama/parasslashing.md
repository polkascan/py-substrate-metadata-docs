
# ParasSlashing

---------
## Calls

---------
### report_dispute_lost_unsigned
#### Attributes
| Name | Type |
| -------- | -------- | 
| dispute_proof | `Box<DisputeProof>` | 
| key_owner_proof | `T::KeyOwnerProof` | 

#### Python
```python
call = substrate.compose_call(
    'ParasSlashing', 'report_dispute_lost_unsigned', {
    'dispute_proof': {
        'kind': (
            'ForInvalid',
            'AgainstValid',
        ),
        'time_slot': {
            'candidate_hash': '[u8; 32]',
            'session_index': 'u32',
        },
        'validator_id': '[u8; 32]',
        'validator_index': 'u32',
    },
    'key_owner_proof': {
        'session': 'u32',
        'trie_nodes': ['Bytes'],
        'validator_count': 'u32',
    },
}
)
```

---------
## Storage functions

---------
### UnappliedSlashes
 Validators pending dispute slashes.

#### Python
```python
result = substrate.query(
    'ParasSlashing', 'UnappliedSlashes', ['u32', '[u8; 32]']
)
```

#### Return value
```python
{'keys': 'scale_info::812', 'kind': ('ForInvalid', 'AgainstValid')}
```
---------
### ValidatorSetCounts
 `ValidatorSetCount` per session.

#### Python
```python
result = substrate.query(
    'ParasSlashing', 'ValidatorSetCounts', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
## Errors

---------
### DuplicateSlashingReport
The given slashing report is valid but already previously reported.

---------
### InvalidCandidateHash
The candidate hash is invalid.

---------
### InvalidKeyOwnershipProof
The key ownership proof is invalid.

---------
### InvalidSessionIndex
The session index is too old or invalid.

---------
### InvalidValidatorIndex
There is no pending slash for the given validator index and time
slot.

---------
### ValidatorIndexIdMismatch
The validator index does not match the validator id.

---------