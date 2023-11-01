
# ParaInherent

---------
## Calls

---------
### enter
Enter the paras inherent. This will process bitfields and backed candidates.
#### Attributes
| Name | Type |
| -------- | -------- | 
| data | `ParachainsInherentData<T::Header>` | 

#### Python
```python
call = substrate.compose_call(
    'ParaInherent', 'enter', {
    'data': {
        'backed_candidates': [
            {
                'candidate': {
                    'commitments': {
                        'head_data': 'Bytes',
                        'horizontal_messages': [
                            'scale_info::336',
                        ],
                        'hrmp_watermark': 'u32',
                        'new_validation_code': (
                            None,
                            'Bytes',
                        ),
                        'processed_downward_messages': 'u32',
                        'upward_messages': [
                            'Bytes',
                        ],
                    },
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
                },
                'validator_indices': 'BitVec',
                'validity_votes': [
                    {
                        None: None,
                        'Explicit': '[u8; 64]',
                        'Implicit': '[u8; 64]',
                    },
                ],
            },
        ],
        'bitfields': [
            {
                'payload': 'BitVec',
                'signature': '[u8; 64]',
                'validator_index': 'u32',
            },
        ],
        'disputes': [
            {
                'candidate_hash': '[u8; 32]',
                'session': 'u32',
                'statements': [
                    (
                        {
                            'Invalid': 'scale_info::350',
                            'Valid': 'scale_info::349',
                        },
                        'u32',
                        '[u8; 64]',
                    ),
                ],
            },
        ],
        'parent_header': {
            'digest': {
                'logs': [
                    {
                        'Other': 'Bytes',
                        None: None,
                        'Consensus': (
                            '[u8; 4]',
                            'Bytes',
                        ),
                        'PreRuntime': (
                            '[u8; 4]',
                            'Bytes',
                        ),
                        'RuntimeEnvironmentUpdated': None,
                        'Seal': (
                            '[u8; 4]',
                            'Bytes',
                        ),
                    },
                ],
            },
            'extrinsics_root': '[u8; 32]',
            'number': 'u32',
            'parent_hash': '[u8; 32]',
            'state_root': '[u8; 32]',
        },
    },
}
)
```

---------
## Storage functions

---------
### Included
 Whether the paras inherent was included within this block.

 The `Option&lt;()&gt;` is effectively a `bool`, but it never hits storage in the `None` variant
 due to the guarantees of FRAME&#x27;s storage APIs.

 If this is `None` at the end of the block, we panic and render the block invalid.

#### Python
```python
result = substrate.query(
    'ParaInherent', 'Included', []
)
```

#### Return value
```python
()
```
---------
### OnChainVotes
 Scraped on chain data for extracting resolved disputes as well as backing votes.

#### Python
```python
result = substrate.query(
    'ParaInherent', 'OnChainVotes', []
)
```

#### Return value
```python
{
    'backing_validators_per_candidate': [
        (
            {
                'commitments_hash': '[u8; 32]',
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
            },
            [('u32', 'scale_info::342')],
        ),
    ],
    'disputes': [
        {
            'candidate_hash': '[u8; 32]',
            'session': 'u32',
            'statements': [('scale_info::348', 'u32', '[u8; 64]')],
        },
    ],
    'session': 'u32',
}
```
---------
## Errors

---------
### CandidateConcludedInvalid
Disputed candidate that was concluded invalid.

---------
### DisputeInvalid
A dispute statement was invalid.

---------
### DisputeStatementsUnsortedOrDuplicates
The ordering of dispute statements was invalid.

---------
### InherentOverweight
The data given to the inherent will result in an overweight block.

---------
### InvalidParentHeader
The hash of the submitted parent header doesn&\#x27;t correspond to the saved block hash of
the parent.

---------
### TooManyInclusionInherents
Inclusion inherent called more than once per block.

---------