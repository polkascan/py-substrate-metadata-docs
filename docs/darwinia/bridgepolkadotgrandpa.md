
# BridgePolkadotGrandpa

---------
## Calls

---------
### initialize
Bootstrap the bridge pallet with an initial header and authority set from which to sync.

The initial configuration provided does not need to be the genesis header of the bridged
chain, it can be any arbitrary header. You can also provide the next scheduled set
change if it is already know.

This function is only allowed to be called from a trusted origin and writes to storage
with practically no checks in terms of the validity of the data. It is important that
you ensure that valid data is being passed in.
#### Attributes
| Name | Type |
| -------- | -------- | 
| init_data | `super::InitializationData<BridgedHeader<T, I>>` | 

#### Python
```python
call = substrate.compose_call(
    'BridgePolkadotGrandpa', 'initialize', {
    'init_data': {
        'authority_list': [
            ('[u8; 32]', 'u64'),
        ],
        'header': {
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
        'is_halted': 'bool',
        'set_id': 'u64',
    },
}
)
```

---------
### set_operational
Halt or resume all pallet operations.

May only be called either by root, or by `PalletOwner`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| operational | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'BridgePolkadotGrandpa', 'set_operational', {'operational': 'bool'}
)
```

---------
### set_owner
Change `PalletOwner`.

May only be called either by root, or by `PalletOwner`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_owner | `Option<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'BridgePolkadotGrandpa', 'set_owner', {'new_owner': (None, 'AccountId')}
)
```

---------
### submit_finality_proof
Verify a target header is finalized according to the given finality proof.

It will use the underlying storage pallet to fetch information about the current
authorities and best finalized header in order to verify that the header is finalized.

If successful in verification, it will write the target header to the underlying storage
pallet.
#### Attributes
| Name | Type |
| -------- | -------- | 
| finality_target | `Box<BridgedHeader<T, I>>` | 
| justification | `GrandpaJustification<BridgedHeader<T, I>>` | 

#### Python
```python
call = substrate.compose_call(
    'BridgePolkadotGrandpa', 'submit_finality_proof', {
    'finality_target': {
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
    'justification': {
        'commit': {
            'precommits': [
                {
                    'id': '[u8; 32]',
                    'precommit': {
                        'target_hash': '[u8; 32]',
                        'target_number': 'u32',
                    },
                    'signature': '[u8; 64]',
                },
            ],
            'target_hash': '[u8; 32]',
            'target_number': 'u32',
        },
        'round': 'u64',
        'votes_ancestries': [
            {
                'digest': {
                    'logs': [
                        {
                            'Consensus': (
                                '[u8; 4]',
                                'Bytes',
                            ),
                            'Other': 'Bytes',
                            'PreRuntime': (
                                '[u8; 4]',
                                'Bytes',
                            ),
                            'RuntimeEnvironmentUpdated': None,
                            'Seal': (
                                '[u8; 4]',
                                'Bytes',
                            ),
                            None: None,
                        },
                    ],
                },
                'extrinsics_root': '[u8; 32]',
                'number': 'u32',
                'parent_hash': '[u8; 32]',
                'state_root': '[u8; 32]',
            },
        ],
    },
}
)
```

---------
## Storage functions

---------
### BestFinalized
 Hash of the best finalized header.

#### Python
```python
result = substrate.query(
    'BridgePolkadotGrandpa', 'BestFinalized', []
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### CurrentAuthoritySet
 The current GRANDPA Authority set.

#### Python
```python
result = substrate.query(
    'BridgePolkadotGrandpa', 'CurrentAuthoritySet', []
)
```

#### Return value
```python
{'authorities': [('[u8; 32]', 'u64')], 'set_id': 'u64'}
```
---------
### ImportedHashes
 A ring buffer of imported hashes. Ordered by the insertion time.

#### Python
```python
result = substrate.query(
    'BridgePolkadotGrandpa', 'ImportedHashes', ['u32']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### ImportedHashesPointer
 Current ring buffer position.

#### Python
```python
result = substrate.query(
    'BridgePolkadotGrandpa', 'ImportedHashesPointer', []
)
```

#### Return value
```python
'u32'
```
---------
### ImportedHeaders
 Headers which have been imported into the pallet.

#### Python
```python
result = substrate.query(
    'BridgePolkadotGrandpa', 'ImportedHeaders', ['[u8; 32]']
)
```

#### Return value
```python
{
    'digest': {
        'logs': [
            {
                'Other': 'Bytes',
                None: None,
                'Consensus': ('[u8; 4]', 'Bytes'),
                'PreRuntime': ('[u8; 4]', 'Bytes'),
                'RuntimeEnvironmentUpdated': None,
                'Seal': ('[u8; 4]', 'Bytes'),
            },
        ],
    },
    'extrinsics_root': '[u8; 32]',
    'number': 'u32',
    'parent_hash': '[u8; 32]',
    'state_root': '[u8; 32]',
}
```
---------
### InitialHash
 Hash of the header used to bootstrap the pallet.

#### Python
```python
result = substrate.query(
    'BridgePolkadotGrandpa', 'InitialHash', []
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### IsHalted
 If true, all pallet transactions are failed immediately.

#### Python
```python
result = substrate.query(
    'BridgePolkadotGrandpa', 'IsHalted', []
)
```

#### Return value
```python
'bool'
```
---------
### PalletOwner
 Optional pallet owner.

 Pallet owner has a right to halt all pallet operations and then resume it. If it is
 `None`, then there are no direct ways to halt/resume pallet operations, but other
 runtime methods may still be used to do that (i.e. democracy::referendum to update halt
 flag directly or call the `halt_operations`).

#### Python
```python
result = substrate.query(
    'BridgePolkadotGrandpa', 'PalletOwner', []
)
```

#### Return value
```python
'AccountId'
```
---------
### RequestCount
 The current number of requests which have written to storage.

 If the `RequestCount` hits `MaxRequests`, no more calls will be allowed to the pallet until
 the request capacity is increased.

 The `RequestCount` is decreased by one at the beginning of every block. This is to ensure
 that the pallet can always make progress.

#### Python
```python
result = substrate.query(
    'BridgePolkadotGrandpa', 'RequestCount', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### HeadersToKeep
 Maximal number of finalized headers to keep in the storage.

 The setting is there to prevent growing the on-chain state indefinitely. Note
 the setting does not relate to block numbers - we will simply keep as much items
 in the storage, so it doesn&#x27;t guarantee any fixed timeframe for finality headers.
#### Value
```python
500
```
#### Python
```python
constant = substrate.get_constant('BridgePolkadotGrandpa', 'HeadersToKeep')
```
---------
### MaxRequests
 The upper bound on the number of requests allowed by the pallet.

 A request refers to an action which writes a header to storage.

 Once this bound is reached the pallet will not allow any dispatchables to be called
 until the request count has decreased.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('BridgePolkadotGrandpa', 'MaxRequests')
```
---------
## Errors

---------
### AlreadyInitialized
The pallet has already been initialized.

---------
### Halted
All pallet operations are halted.

---------
### InvalidAuthoritySet
The authority set from the underlying header chain is invalid.

---------
### InvalidJustification
The given justification is invalid for the given header.

---------
### NotInitialized
The pallet is not yet initialized.

---------
### OldHeader
The header being imported is older than the best finalized header known to the pallet.

---------
### StorageRootMismatch
The storage proof doesn&\#x27;t contains storage root. So it is invalid for given header.

---------
### TooManyRequests
There are too many requests for the current window to handle.

---------
### UnknownHeader
The header is unknown to the pallet.

---------
### UnsupportedScheduledChange
The scheduled authority set change found in the header is unsupported by the pallet.

This is the case for non-standard (e.g forced) authority set changes.

---------