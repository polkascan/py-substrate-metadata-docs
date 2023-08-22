
# Babe

---------
## Calls

---------
### plan_config_change
Plan an epoch config change. The epoch config change is recorded and will be enacted on
the next call to `enact_epoch_change`. The config will be activated one epoch after.
Multiple calls to this method will replace any existing planned config change that had
not been enacted yet.
#### Attributes
| Name | Type |
| -------- | -------- | 
| config | `NextConfigDescriptor` | 

#### Python
```python
call = substrate.compose_call(
    'Babe', 'plan_config_change', {
    'config': {
        None: None,
        'V1': {
            'allowed_slots': (
                'PrimarySlots',
                'PrimaryAndSecondaryPlainSlots',
                'PrimaryAndSecondaryVRFSlots',
            ),
            'c': ('u64', 'u64'),
        },
    },
}
)
```

---------
### report_equivocation
Report authority equivocation/misbehavior. This method will verify
the equivocation proof and validate the given key ownership proof
against the extracted offender. If both are valid, the offence will
be reported.
#### Attributes
| Name | Type |
| -------- | -------- | 
| equivocation_proof | `Box<EquivocationProof<T::Header>>` | 
| key_owner_proof | `T::KeyOwnerProof` | 

#### Python
```python
call = substrate.compose_call(
    'Babe', 'report_equivocation', {
    'equivocation_proof': {
        'first_header': {
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
        'offender': '[u8; 32]',
        'second_header': {
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
        'slot': 'u64',
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
### report_equivocation_unsigned
Report authority equivocation/misbehavior. This method will verify
the equivocation proof and validate the given key ownership proof
against the extracted offender. If both are valid, the offence will
be reported.
This extrinsic must be called unsigned and it is expected that only
block authors will call it (validated in `ValidateUnsigned`), as such
if the block author is defined it will be defined as the equivocation
reporter.
#### Attributes
| Name | Type |
| -------- | -------- | 
| equivocation_proof | `Box<EquivocationProof<T::Header>>` | 
| key_owner_proof | `T::KeyOwnerProof` | 

#### Python
```python
call = substrate.compose_call(
    'Babe', 'report_equivocation_unsigned', {
    'equivocation_proof': {
        'first_header': {
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
        'offender': '[u8; 32]',
        'second_header': {
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
        'slot': 'u64',
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
### AuthorVrfRandomness
 This field should always be populated during block processing unless
 secondary plain slots are enabled (which don&#x27;t contain a VRF output).

 It is set in `on_finalize`, before it will contain the value from the last block.

#### Python
```python
result = substrate.query(
    'Babe', 'AuthorVrfRandomness', []
)
```

#### Return value
```python
(None, '[u8; 32]')
```
---------
### Authorities
 Current epoch authorities.

#### Python
```python
result = substrate.query(
    'Babe', 'Authorities', []
)
```

#### Return value
```python
[('[u8; 32]', 'u64')]
```
---------
### CurrentSlot
 Current slot number.

#### Python
```python
result = substrate.query(
    'Babe', 'CurrentSlot', []
)
```

#### Return value
```python
'u64'
```
---------
### EpochConfig
 The configuration for the current epoch. Should never be `None` as it is initialized in
 genesis.

#### Python
```python
result = substrate.query(
    'Babe', 'EpochConfig', []
)
```

#### Return value
```python
{
    'allowed_slots': (
        'PrimarySlots',
        'PrimaryAndSecondaryPlainSlots',
        'PrimaryAndSecondaryVRFSlots',
    ),
    'c': ('u64', 'u64'),
}
```
---------
### EpochIndex
 Current epoch index.

#### Python
```python
result = substrate.query(
    'Babe', 'EpochIndex', []
)
```

#### Return value
```python
'u64'
```
---------
### EpochStart
 The block numbers when the last and current epoch have started, respectively `N-1` and
 `N`.
 NOTE: We track this is in order to annotate the block number when a given pool of
 entropy was fixed (i.e. it was known to chain observers). Since epochs are defined in
 slots, which may be skipped, the block numbers may not line up with the slot numbers.

#### Python
```python
result = substrate.query(
    'Babe', 'EpochStart', []
)
```

#### Return value
```python
('u32', 'u32')
```
---------
### GenesisSlot
 The slot at which the first epoch actually started. This is 0
 until the first block of the chain.

#### Python
```python
result = substrate.query(
    'Babe', 'GenesisSlot', []
)
```

#### Return value
```python
'u64'
```
---------
### Initialized
 Temporary value (cleared at block finalization) which is `Some`
 if per-block initialization has already been called for current block.

#### Python
```python
result = substrate.query(
    'Babe', 'Initialized', []
)
```

#### Return value
```python
(
    None,
    {
        None: None,
        'Primary': {
            'authority_index': 'u32',
            'slot': 'u64',
            'vrf_output': '[u8; 32]',
            'vrf_proof': '[u8; 64]',
        },
        'SecondaryPlain': {'authority_index': 'u32', 'slot': 'u64'},
        'SecondaryVRF': {
            'authority_index': 'u32',
            'slot': 'u64',
            'vrf_output': '[u8; 32]',
            'vrf_proof': '[u8; 64]',
        },
    },
)
```
---------
### Lateness
 How late the current block is compared to its parent.

 This entry is populated as part of block execution and is cleaned up
 on block finalization. Querying this storage entry outside of block
 execution context should always yield zero.

#### Python
```python
result = substrate.query(
    'Babe', 'Lateness', []
)
```

#### Return value
```python
'u32'
```
---------
### NextAuthorities
 Next epoch authorities.

#### Python
```python
result = substrate.query(
    'Babe', 'NextAuthorities', []
)
```

#### Return value
```python
[('[u8; 32]', 'u64')]
```
---------
### NextEpochConfig
 The configuration for the next epoch, `None` if the config will not change
 (you can fallback to `EpochConfig` instead in that case).

#### Python
```python
result = substrate.query(
    'Babe', 'NextEpochConfig', []
)
```

#### Return value
```python
{
    'allowed_slots': (
        'PrimarySlots',
        'PrimaryAndSecondaryPlainSlots',
        'PrimaryAndSecondaryVRFSlots',
    ),
    'c': ('u64', 'u64'),
}
```
---------
### NextRandomness
 Next epoch randomness.

#### Python
```python
result = substrate.query(
    'Babe', 'NextRandomness', []
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### PendingEpochConfigChange
 Pending epoch configuration change that will be applied when the next epoch is enacted.

#### Python
```python
result = substrate.query(
    'Babe', 'PendingEpochConfigChange', []
)
```

#### Return value
```python
{
    None: None,
    'V1': {
        'allowed_slots': (
            'PrimarySlots',
            'PrimaryAndSecondaryPlainSlots',
            'PrimaryAndSecondaryVRFSlots',
        ),
        'c': ('u64', 'u64'),
    },
}
```
---------
### Randomness
 The epoch randomness for the *current* epoch.

 \# Security

 This MUST NOT be used for gambling, as it can be influenced by a
 malicious validator in the short term. It MAY be used in many
 cryptographic protocols, however, so long as one remembers that this
 (like everything else on-chain) it is public. For example, it can be
 used where a number is needed that cannot have been chosen by an
 adversary, for purposes such as public-coin zero-knowledge proofs.

#### Python
```python
result = substrate.query(
    'Babe', 'Randomness', []
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### SegmentIndex
 Randomness under construction.

 We make a trade-off between storage accesses and list length.
 We store the under-construction randomness in segments of up to
 `UNDER_CONSTRUCTION_SEGMENT_LENGTH`.

 Once a segment reaches this length, we begin the next one.
 We reset all segments and return to `0` at the beginning of every
 epoch.

#### Python
```python
result = substrate.query(
    'Babe', 'SegmentIndex', []
)
```

#### Return value
```python
'u32'
```
---------
### UnderConstruction
 TWOX-NOTE: `SegmentIndex` is an increasing integer, so this is okay.

#### Python
```python
result = substrate.query(
    'Babe', 'UnderConstruction', ['u32']
)
```

#### Return value
```python
['[u8; 32]']
```
---------
## Constants

---------
### EpochDuration
 The amount of time, in slots, that each epoch should last.
 NOTE: Currently it is not possible to change the epoch duration after
 the chain has started. Attempting to do so will brick block production.
#### Value
```python
2400
```
#### Python
```python
constant = substrate.get_constant('Babe', 'EpochDuration')
```
---------
### ExpectedBlockTime
 The expected average block time at which BABE should be creating
 blocks. Since BABE is probabilistic it is not trivial to figure out
 what the expected average block time should be based on the slot
 duration and the security parameter `c` (where `1 - c` represents
 the probability of a slot being empty).
#### Value
```python
6000
```
#### Python
```python
constant = substrate.get_constant('Babe', 'ExpectedBlockTime')
```
---------
### MaxAuthorities
 Max number of authorities allowed
#### Value
```python
100000
```
#### Python
```python
constant = substrate.get_constant('Babe', 'MaxAuthorities')
```
---------
## Errors

---------
### DuplicateOffenceReport
A given equivocation report is valid but already previously reported.

---------
### InvalidConfiguration
Submitted configuration is invalid.

---------
### InvalidEquivocationProof
An equivocation proof provided as part of an equivocation report is invalid.

---------
### InvalidKeyOwnershipProof
A key ownership proof provided as part of an equivocation report is invalid.

---------