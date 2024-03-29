
# ParaInherent

---------
## Calls

---------
### enter
See [`Pallet::enter`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| data | `ParachainsInherentData<HeaderFor<T>>` | 

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
                            'scale_info::326',
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
                        'erasure_root': 'scale_info::12',
                        'para_head': 'scale_info::12',
                        'para_id': 'u32',
                        'persisted_validation_data_hash': 'scale_info::12',
                        'pov_hash': 'scale_info::12',
                        'relay_parent': 'scale_info::12',
                        'signature': '[u8; 64]',
                        'validation_code_hash': 'scale_info::12',
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
                'candidate_hash': 'scale_info::12',
                'session': 'u32',
                'statements': [
                    (
                        {
                            'Invalid': 'scale_info::340',
                            'Valid': 'scale_info::339',
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
            'extrinsics_root': 'scale_info::12',
            'number': 'u32',
            'parent_hash': 'scale_info::12',
            'state_root': 'scale_info::12',
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
                'commitments_hash': 'scale_info::12',
                'descriptor': {
                    'collator': '[u8; 32]',
                    'erasure_root': 'scale_info::12',
                    'para_head': 'scale_info::12',
                    'para_id': 'u32',
                    'persisted_validation_data_hash': 'scale_info::12',
                    'pov_hash': 'scale_info::12',
                    'relay_parent': 'scale_info::12',
                    'signature': '[u8; 64]',
                    'validation_code_hash': 'scale_info::12',
                },
            },
            [('u32', 'scale_info::332')],
        ),
    ],
    'disputes': [
        {
            'candidate_hash': 'scale_info::12',
            'session': 'u32',
            'statements': [('scale_info::338', 'u32', '[u8; 64]')],
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