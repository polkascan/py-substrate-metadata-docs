
# ParaInclusion

---------
## Events

---------
### CandidateBacked
A candidate was backed. `[candidate, head_data]`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CandidateReceipt<T::Hash>` | ```{'descriptor': {'para_id': 'u32', 'relay_parent': '[u8; 32]', 'collator': '[u8; 32]', 'persisted_validation_data_hash': '[u8; 32]', 'pov_hash': '[u8; 32]', 'erasure_root': '[u8; 32]', 'signature': '[u8; 64]', 'para_head': '[u8; 32]', 'validation_code_hash': '[u8; 32]'}, 'commitments_hash': '[u8; 32]'}```
| None | `HeadData` | ```Bytes```
| None | `CoreIndex` | ```u32```
| None | `GroupIndex` | ```u32```

---------
### CandidateIncluded
A candidate was included. `[candidate, head_data]`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CandidateReceipt<T::Hash>` | ```{'descriptor': {'para_id': 'u32', 'relay_parent': '[u8; 32]', 'collator': '[u8; 32]', 'persisted_validation_data_hash': '[u8; 32]', 'pov_hash': '[u8; 32]', 'erasure_root': '[u8; 32]', 'signature': '[u8; 64]', 'para_head': '[u8; 32]', 'validation_code_hash': '[u8; 32]'}, 'commitments_hash': '[u8; 32]'}```
| None | `HeadData` | ```Bytes```
| None | `CoreIndex` | ```u32```
| None | `GroupIndex` | ```u32```

---------
### CandidateTimedOut
A candidate timed out. `[candidate, head_data]`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CandidateReceipt<T::Hash>` | ```{'descriptor': {'para_id': 'u32', 'relay_parent': '[u8; 32]', 'collator': '[u8; 32]', 'persisted_validation_data_hash': '[u8; 32]', 'pov_hash': '[u8; 32]', 'erasure_root': '[u8; 32]', 'signature': '[u8; 64]', 'para_head': '[u8; 32]', 'validation_code_hash': '[u8; 32]'}, 'commitments_hash': '[u8; 32]'}```
| None | `HeadData` | ```Bytes```
| None | `CoreIndex` | ```u32```

---------
## Storage functions

---------
### AvailabilityBitfields
 The latest bitfield for each validator, referred to by their index in the validator set.

#### Python
```python
result = substrate.query(
    'ParaInclusion', 'AvailabilityBitfields', ['u32']
)
```

#### Return value
```python
{'bitfield': 'BitVec', 'submitted_at': 'u32'}
```
---------
### PendingAvailability
 Candidates pending availability by `ParaId`.

#### Python
```python
result = substrate.query(
    'ParaInclusion', 'PendingAvailability', ['u32']
)
```

#### Return value
```python
{
    'availability_votes': 'BitVec',
    'backed_in_number': 'u32',
    'backers': 'BitVec',
    'backing_group': 'u32',
    'core': 'u32',
    'descriptor': {
        'collator': '[u8; 32]',
        'erasure_root': '[u8; 32]',
        'para_head': '[u8; 32]',
        'para_id': 'u32',
        'persisted_validation_data_hash': '[u8; 32]',
        'pov_hash': '[u8; 32]',
        'relay_parent': '[u8; 32]',
        'signature': '[u8; 64]',
        'validation_code_hash': '[u8; 32]',
    },
    'hash': '[u8; 32]',
    'relay_parent_number': 'u32',
}
```
---------
### PendingAvailabilityCommitments
 The commitments of candidates pending availability, by `ParaId`.

#### Python
```python
result = substrate.query(
    'ParaInclusion', 'PendingAvailabilityCommitments', ['u32']
)
```

#### Return value
```python
{
    'head_data': 'Bytes',
    'horizontal_messages': [{'data': 'Bytes', 'recipient': 'u32'}],
    'hrmp_watermark': 'u32',
    'new_validation_code': (None, 'Bytes'),
    'processed_downward_messages': 'u32',
    'upward_messages': ['Bytes'],
}
```
---------
## Errors

---------
### BitfieldAllZeros
Bitfield consists of zeros only.

---------
### BitfieldDuplicateOrUnordered
Multiple bitfields submitted by same validator or validators out of order by index.

---------
### BitfieldReferencesFreedCore
A bitfield that references a freed core,
either intentionally or as part of a concluded
invalid dispute.

---------
### CandidateNotInParentContext
Candidate not in parent context.

---------
### CandidateScheduledBeforeParaFree
Candidate scheduled despite pending candidate already existing for the para.

---------
### HeadDataTooLarge
Head data exceeds the configured maximum.

---------
### HrmpWatermarkMishandling
The candidate didn&\#x27;t follow the rules of HRMP watermark advancement.

---------
### IncorrectDownwardMessageHandling
The downward message queue is not processed correctly.

---------
### InsufficientBacking
Insufficient (non-majority) backing.

---------
### InvalidBacking
Invalid (bad signature, unknown validator, etc.) backing.

---------
### InvalidBitfieldSignature
Invalid signature

---------
### InvalidGroupIndex
Invalid group index in core assignment.

---------
### InvalidOutboundHrmp
The HRMP messages sent by the candidate is not valid.

---------
### InvalidUpwardMessages
At least one upward message sent does not pass the acceptance criteria.

---------
### InvalidValidationCodeHash
The validation code hash of the candidate is not valid.

---------
### NewCodeTooLarge
Output code is too large

---------
### NotCollatorSigned
Collator did not sign PoV.

---------
### ParaHeadMismatch
The `para_head` hash in the candidate descriptor doesn&\#x27;t match the hash of the actual para head in the
commitments.

---------
### PrematureCodeUpgrade
Code upgrade prematurely.

---------
### ScheduledOutOfOrder
Scheduled cores out of order.

---------
### UnexpectedRelayParent
A different relay parent was provided compared to the on-chain stored one.

---------
### UnscheduledCandidate
Candidate submitted but para not scheduled.

---------
### UnsortedOrDuplicateBackedCandidates
Backed candidates are out of order (core index) or contain duplicates.

---------
### UnsortedOrDuplicateDisputeStatementSet
Dispute statement sets are out of order or contain duplicates.

---------
### UnsortedOrDuplicateValidatorIndices
Validator indices are out of order or contains duplicates.

---------
### ValidationDataHashMismatch
The validation data hash does not match expected.

---------
### ValidatorIndexOutOfBounds
Validator index out of bounds.

---------
### WrongBitfieldSize
Availability bitfield has unexpected size.

---------
### WrongCollator
Candidate included with the wrong collator.

---------