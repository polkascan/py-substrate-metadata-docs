# bitgreen
---------
| Properties |  |
| -------- | -------- |
| Spec name     | bitgreen     |
| Implementation name     | bitgreen     |
| Spec version     | 1000     |
| SS58 Format     | 42     |
| Token symbol      | BBB     |
| Token decimals      | 18     |

## System
---------
### Calls
---------
#### remark
Make some on-chain remark.

\# &lt;weight&gt;
- `O(1)`
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| remark | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'System', 'remark', {'remark': 'Bytes'}
)
```

---------
#### set_heap_pages
Set the number of pages in the WebAssembly environment&\#x27;s heap.
##### Attributes
| Name | Type |
| -------- | -------- | 
| pages | `u64` | 

##### Python
```python
call = substrate.compose_call(
    'System', 'set_heap_pages', {'pages': 'u64'}
)
```

---------
#### set_code
Set the new runtime code.

\# &lt;weight&gt;
- `O(C + S)` where `C` length of `code` and `S` complexity of `can_set_code`
- 1 call to `can_set_code`: `O(S)` (calls `sp_io::misc::runtime_version` which is
  expensive).
- 1 storage write (codec `O(C)`).
- 1 digest item.
- 1 event.
The weight of this function is dependent on the runtime, but generally this is very
expensive. We will treat this as a full block.
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| code | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'System', 'set_code', {'code': 'Bytes'}
)
```

---------
#### set_code_without_checks
Set the new runtime code without doing any checks of the given `code`.

\# &lt;weight&gt;
- `O(C)` where `C` length of `code`
- 1 storage write (codec `O(C)`).
- 1 digest item.
- 1 event.
The weight of this function is dependent on the runtime. We will treat this as a full
block. \# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| code | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'System', 'set_code_without_checks', {'code': 'Bytes'}
)
```

---------
#### set_storage
Set some items of storage.
##### Attributes
| Name | Type |
| -------- | -------- | 
| items | `Vec<KeyValue>` | 

##### Python
```python
call = substrate.compose_call(
    'System', 'set_storage', {'items': [('Bytes', 'Bytes')]}
)
```

---------
#### kill_storage
Kill some items from storage.
##### Attributes
| Name | Type |
| -------- | -------- | 
| keys | `Vec<Key>` | 

##### Python
```python
call = substrate.compose_call(
    'System', 'kill_storage', {'keys': ['Bytes']}
)
```

---------
#### kill_prefix
Kill all storage items with a key that starts with the given prefix.

**NOTE:** We rely on the Root origin to provide us the number of subkeys under
the prefix we are removing to accurately calculate the weight of this function.
##### Attributes
| Name | Type |
| -------- | -------- | 
| prefix | `Key` | 
| subkeys | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'System', 'kill_prefix', {'prefix': 'Bytes', 'subkeys': 'u32'}
)
```

---------
#### remark_with_event
Make some on-chain remark and emit event.
##### Attributes
| Name | Type |
| -------- | -------- | 
| remark | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'System', 'remark_with_event', {'remark': 'Bytes'}
)
```

---------
### Events
---------
#### ExtrinsicSuccess
An extrinsic completed successfully.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispatch_info | `DispatchInfo` | ```{'weight': {'ref_time': 'u64', 'proof_size': 'u64'}, 'class': ('Normal', 'Operational', 'Mandatory'), 'pays_fee': ('Yes', 'No')}```

---------
#### ExtrinsicFailed
An extrinsic failed.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispatch_error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```
| dispatch_info | `DispatchInfo` | ```{'weight': {'ref_time': 'u64', 'proof_size': 'u64'}, 'class': ('Normal', 'Operational', 'Mandatory'), 'pays_fee': ('Yes', 'No')}```

---------
#### CodeUpdated
`:code` was updated.
##### Attributes
No attributes

---------
#### NewAccount
A new account was created.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
#### KilledAccount
An account was reaped.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
#### Remarked
On on-chain remark happened.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| hash | `T::Hash` | ```[u8; 32]```

---------
### Storage functions
---------
#### Account
 The full account information for a particular account ID.

##### Python
```python
result = substrate.query(
    'System', 'Account', ['AccountId']
)
```

##### Return value
```python
{
    'consumers': 'u32',
    'data': {
        'fee_frozen': 'u128',
        'free': 'u128',
        'misc_frozen': 'u128',
        'reserved': 'u128',
    },
    'nonce': 'u32',
    'providers': 'u32',
    'sufficients': 'u32',
}
```
---------
#### ExtrinsicCount
 Total extrinsics count for the current block.

##### Python
```python
result = substrate.query(
    'System', 'ExtrinsicCount', []
)
```

##### Return value
```python
'u32'
```
---------
#### BlockWeight
 The current weight for the block.

##### Python
```python
result = substrate.query(
    'System', 'BlockWeight', []
)
```

##### Return value
```python
{
    'mandatory': {'proof_size': 'u64', 'ref_time': 'u64'},
    'normal': {'proof_size': 'u64', 'ref_time': 'u64'},
    'operational': {'proof_size': 'u64', 'ref_time': 'u64'},
}
```
---------
#### AllExtrinsicsLen
 Total length (in bytes) for all extrinsics put together, for the current block.

##### Python
```python
result = substrate.query(
    'System', 'AllExtrinsicsLen', []
)
```

##### Return value
```python
'u32'
```
---------
#### BlockHash
 Map of block numbers to block hashes.

##### Python
```python
result = substrate.query(
    'System', 'BlockHash', ['u32']
)
```

##### Return value
```python
'[u8; 32]'
```
---------
#### ExtrinsicData
 Extrinsics data for the current block (maps an extrinsic&#x27;s index to its data).

##### Python
```python
result = substrate.query(
    'System', 'ExtrinsicData', ['u32']
)
```

##### Return value
```python
'Bytes'
```
---------
#### Number
 The current block number being processed. Set by `execute_block`.

##### Python
```python
result = substrate.query(
    'System', 'Number', []
)
```

##### Return value
```python
'u32'
```
---------
#### ParentHash
 Hash of the previous block.

##### Python
```python
result = substrate.query(
    'System', 'ParentHash', []
)
```

##### Return value
```python
'[u8; 32]'
```
---------
#### Digest
 Digest of the current block, also part of the block header.

##### Python
```python
result = substrate.query(
    'System', 'Digest', []
)
```

##### Return value
```python
{
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
}
```
---------
#### Events
 Events deposited for the current block.

 NOTE: The item is unbound and should therefore never be read on chain.
 It could otherwise inflate the PoV size of a block.

 Events have a large in-memory size. Box the events to not go out-of-memory
 just in case someone still reads them from within the runtime.

##### Python
```python
result = substrate.query(
    'System', 'Events', []
)
```

##### Return value
```python
[
    {
        'event': {
            'Balances': {
                'BalanceSet': {
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Deposit': {'amount': 'u128', 'who': 'AccountId'},
                'DustLost': {'account': 'AccountId', 'amount': 'u128'},
                'Endowed': {'account': 'AccountId', 'free_balance': 'u128'},
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'destination_status': 'scale_info::35',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Reserved': {'amount': 'u128', 'who': 'AccountId'},
                'Slashed': {'amount': 'u128', 'who': 'AccountId'},
                'Transfer': {
                    'amount': 'u128',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unreserved': {'amount': 'u128', 'who': 'AccountId'},
                'Withdraw': {'amount': 'u128', 'who': 'AccountId'},
            },
            'Grandpa': {
                'NewAuthorities': {'authority_set': [('[u8; 32]', 'u64')]},
                'Paused': None,
                'Resumed': None,
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::42',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::42',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::38',
                    'timepoint': 'scale_info::42',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'Preimage': {
                'Cleared': {'hash': '[u8; 32]'},
                'Noted': {'hash': '[u8; 32]'},
                'Requested': {'hash': '[u8; 32]'},
            },
            'Proxy': {
                'Announced': {
                    'call_hash': '[u8; 32]',
                    'proxy': 'AccountId',
                    'real': 'AccountId',
                },
                'ProxyAdded': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::49',
                },
                'ProxyExecuted': {'result': 'scale_info::38'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::49',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::49',
                    'pure': 'AccountId',
                    'who': 'AccountId',
                },
            },
            'Scheduler': {
                'CallUnavailable': {
                    'id': (None, '[u8; 32]'),
                    'task': ('u32', 'u32'),
                },
                'Canceled': {'index': 'u32', 'when': 'u32'},
                'Dispatched': {
                    'id': (None, '[u8; 32]'),
                    'result': 'scale_info::38',
                    'task': ('u32', 'u32'),
                },
                'PeriodicFailed': {
                    'id': (None, '[u8; 32]'),
                    'task': ('u32', 'u32'),
                },
                'PermanentlyOverweight': {
                    'id': (None, '[u8; 32]'),
                    'task': ('u32', 'u32'),
                },
                'Scheduled': {'index': 'u32', 'when': 'u32'},
            },
            'Sudo': {
                'KeyChanged': {'old_sudoer': (None, 'AccountId')},
                'Sudid': {'sudo_result': 'scale_info::38'},
                'SudoAsDone': {'sudo_result': 'scale_info::38'},
            },
            'System': {
                'CodeUpdated': None,
                'ExtrinsicFailed': {
                    'dispatch_error': 'scale_info::24',
                    'dispatch_info': 'scale_info::21',
                },
                'ExtrinsicSuccess': {'dispatch_info': 'scale_info::21'},
                'KilledAccount': {'account': 'AccountId'},
                'NewAccount': {'account': 'AccountId'},
                'Remarked': {'hash': '[u8; 32]', 'sender': 'AccountId'},
            },
            'TransactionPayment': {
                'TransactionFeePaid': {
                    'actual_fee': 'u128',
                    'tip': 'u128',
                    'who': 'AccountId',
                },
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::24',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::38'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::24'},
            },
            None: None,
        },
        'phase': {
            'ApplyExtrinsic': 'u32',
            'Finalization': None,
            'Initialization': None,
        },
        'topics': ['[u8; 32]'],
    },
]
```
---------
#### EventCount
 The number of events in the `Events&lt;T&gt;` list.

##### Python
```python
result = substrate.query(
    'System', 'EventCount', []
)
```

##### Return value
```python
'u32'
```
---------
#### EventTopics
 Mapping between a topic (represented by T::Hash) and a vector of indexes
 of events in the `&lt;Events&lt;T&gt;&gt;` list.

 All topic vectors have deterministic storage locations depending on the topic. This
 allows light-clients to leverage the changes trie storage tracking mechanism and
 in case of changes fetch the list of events of interest.

 The value has the type `(T::BlockNumber, EventIndex)` because if we used only just
 the `EventIndex` then in case if the topic has the same contents on the next block
 no notification will be triggered thus the event might be lost.

##### Python
```python
result = substrate.query(
    'System', 'EventTopics', ['[u8; 32]']
)
```

##### Return value
```python
[('u32', 'u32')]
```
---------
#### LastRuntimeUpgrade
 Stores the `spec_version` and `spec_name` of when the last runtime upgrade happened.

##### Python
```python
result = substrate.query(
    'System', 'LastRuntimeUpgrade', []
)
```

##### Return value
```python
{'spec_name': 'Str', 'spec_version': 'u32'}
```
---------
#### UpgradedToU32RefCount
 True if we have upgraded so that `type RefCount` is `u32`. False (default) if not.

##### Python
```python
result = substrate.query(
    'System', 'UpgradedToU32RefCount', []
)
```

##### Return value
```python
'bool'
```
---------
#### UpgradedToTripleRefCount
 True if we have upgraded so that AccountInfo contains three types of `RefCount`. False
 (default) if not.

##### Python
```python
result = substrate.query(
    'System', 'UpgradedToTripleRefCount', []
)
```

##### Return value
```python
'bool'
```
---------
#### ExecutionPhase
 The execution phase of the block.

##### Python
```python
result = substrate.query(
    'System', 'ExecutionPhase', []
)
```

##### Return value
```python
{'ApplyExtrinsic': 'u32', 'Finalization': None, 'Initialization': None}
```
---------
### Constants
---------
#### BlockWeights
 Block &amp; extrinsics weights: base values and limits.
##### Value
```python
{
    'base_block': {'proof_size': 0, 'ref_time': 358523000},
    'max_block': {
        'proof_size': 18446744073709551615,
        'ref_time': 2000000000000,
    },
    'per_class': {
        'mandatory': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 98974000},
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 98974000},
            'max_extrinsic': {
                'proof_size': 11990383647911208550,
                'ref_time': 1299901026000,
            },
            'max_total': {
                'proof_size': 13835058055282163711,
                'ref_time': 1500000000000,
            },
            'reserved': {'proof_size': 0, 'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 98974000},
            'max_extrinsic': {
                'proof_size': 16602069666338596454,
                'ref_time': 1799901026000,
            },
            'max_total': {
                'proof_size': 18446744073709551615,
                'ref_time': 2000000000000,
            },
            'reserved': {
                'proof_size': 4611686018427387904,
                'ref_time': 500000000000,
            },
        },
    },
}
```
##### Python
```python
constant = substrate.get_constant('System', 'BlockWeights')
```
---------
#### BlockLength
 The maximum length of a block (in bytes).
##### Value
```python
{'max': {'mandatory': 5242880, 'normal': 3932160, 'operational': 5242880}}
```
##### Python
```python
constant = substrate.get_constant('System', 'BlockLength')
```
---------
#### BlockHashCount
 Maximum number of block number to block hash mappings to keep (oldest pruned first).
##### Value
```python
2400
```
##### Python
```python
constant = substrate.get_constant('System', 'BlockHashCount')
```
---------
#### DbWeight
 The weight of runtime database operations the runtime can invoke.
##### Value
```python
{'read': 25000000, 'write': 100000000}
```
##### Python
```python
constant = substrate.get_constant('System', 'DbWeight')
```
---------
#### Version
 Get the chain&#x27;s current version.
##### Value
```python
{
    'apis': [
        ('0xdf6acb689907609b', 4),
        ('0x37e397fc7c91f5e4', 1),
        ('0x40fe3ad401f8959a', 6),
        ('0xd2bc9897eed08f15', 3),
        ('0xf78b278be53f454c', 2),
        ('0xdd718d5cc53262d4', 1),
        ('0xab3c0572291feb8b', 1),
        ('0xed99c5acb25eedf5', 3),
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 2),
        ('0xf3ff14d5ab527059', 2),
    ],
    'authoring_version': 1,
    'impl_name': 'bitgreen',
    'impl_version': 1,
    'spec_name': 'bitgreen',
    'spec_version': 1000,
    'state_version': 1,
    'transaction_version': 1,
}
```
##### Python
```python
constant = substrate.get_constant('System', 'Version')
```
---------
#### SS58Prefix
 The designated SS58 prefix of this chain.

 This replaces the &quot;ss58Format&quot; property declared in the chain spec. Reason is
 that the runtime should know about the prefix in order to make use of it as
 an identifier of the chain.
##### Value
```python
42
```
##### Python
```python
constant = substrate.get_constant('System', 'SS58Prefix')
```
---------
### Errors
---------
#### InvalidSpecName
The name of specification does not match between the current runtime
and the new runtime.

---------
#### SpecVersionNeedsToIncrease
The specification version is not allowed to decrease between the current runtime
and the new runtime.

---------
#### FailedToExtractRuntimeVersion
Failed to extract the runtime version from the new runtime.

Either calling `Core_version` or decoding `RuntimeVersion` failed.

---------
#### NonDefaultComposite
Suicide called when the account has non-default composite data.

---------
#### NonZeroRefCount
There is a non-zero reference count preventing the account from being purged.

---------
#### CallFiltered
The origin filter prevent the call to be dispatched.

---------

## RandomnessCollectiveFlip
---------
### Storage functions
---------
#### RandomMaterial
 Series of block headers from the last 81 blocks that acts as random seed material. This
 is arranged as a ring buffer with `block_number % 81` being the index into the `Vec` of
 the oldest hash.

##### Python
```python
result = substrate.query(
    'RandomnessCollectiveFlip', 'RandomMaterial', []
)
```

##### Return value
```python
['[u8; 32]']
```
---------

## Timestamp
---------
### Calls
---------
#### set
Set the current time.

This call should be invoked exactly once per block. It will panic at the finalization
phase, if this call hasn&\#x27;t been invoked by that time.

The timestamp should be greater than the previous one by the amount specified by
`MinimumPeriod`.

The dispatch origin for this call must be `Inherent`.

\# &lt;weight&gt;
- `O(1)` (Note that implementations of `OnTimestampSet` must also be `O(1)`)
- 1 storage read and 1 storage mutation (codec `O(1)`). (because of `DidUpdate::take` in
  `on_finalize`)
- 1 event handler `on_timestamp_set`. Must be `O(1)`.
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| now | `T::Moment` | 

##### Python
```python
call = substrate.compose_call(
    'Timestamp', 'set', {'now': 'u64'}
)
```

---------
### Storage functions
---------
#### Now
 Current time for the current block.

##### Python
```python
result = substrate.query(
    'Timestamp', 'Now', []
)
```

##### Return value
```python
'u64'
```
---------
#### DidUpdate
 Did the timestamp get updated in this block?

##### Python
```python
result = substrate.query(
    'Timestamp', 'DidUpdate', []
)
```

##### Return value
```python
'bool'
```
---------
### Constants
---------
#### MinimumPeriod
 The minimum period between blocks. Beware that this is different to the *expected*
 period that the block production apparatus provides. Your chosen consensus system will
 generally work with this to determine a sensible block time. e.g. For Aura, it will be
 double this period on default settings.
##### Value
```python
3000
```
##### Python
```python
constant = substrate.get_constant('Timestamp', 'MinimumPeriod')
```
---------

## Aura
---------
### Storage functions
---------
#### Authorities
 The current authority set.

##### Python
```python
result = substrate.query(
    'Aura', 'Authorities', []
)
```

##### Return value
```python
['[u8; 32]']
```
---------
#### CurrentSlot
 The current slot of this block.

 This will be set in `on_initialize`.

##### Python
```python
result = substrate.query(
    'Aura', 'CurrentSlot', []
)
```

##### Return value
```python
'u64'
```
---------

## Grandpa
---------
### Calls
---------
#### report_equivocation
Report voter equivocation/misbehavior. This method will verify the
equivocation proof and validate the given key ownership proof
against the extracted offender. If both are valid, the offence
will be reported.
##### Attributes
| Name | Type |
| -------- | -------- | 
| equivocation_proof | `Box<EquivocationProof<T::Hash, T::BlockNumber>>` | 
| key_owner_proof | `T::KeyOwnerProof` | 

##### Python
```python
call = substrate.compose_call(
    'Grandpa', 'report_equivocation', {
    'equivocation_proof': {
        'equivocation': {
            'Precommit': {
                'first': (
                    {
                        'target_hash': '[u8; 32]',
                        'target_number': 'u32',
                    },
                    '[u8; 64]',
                ),
                'identity': '[u8; 32]',
                'round_number': 'u64',
                'second': (
                    {
                        'target_hash': '[u8; 32]',
                        'target_number': 'u32',
                    },
                    '[u8; 64]',
                ),
            },
            'Prevote': {
                'first': (
                    {
                        'target_hash': '[u8; 32]',
                        'target_number': 'u32',
                    },
                    '[u8; 64]',
                ),
                'identity': '[u8; 32]',
                'round_number': 'u64',
                'second': (
                    {
                        'target_hash': '[u8; 32]',
                        'target_number': 'u32',
                    },
                    '[u8; 64]',
                ),
            },
        },
        'set_id': 'u64',
    },
    'key_owner_proof': (),
}
)
```

---------
#### report_equivocation_unsigned
Report voter equivocation/misbehavior. This method will verify the
equivocation proof and validate the given key ownership proof
against the extracted offender. If both are valid, the offence
will be reported.

This extrinsic must be called unsigned and it is expected that only
block authors will call it (validated in `ValidateUnsigned`), as such
if the block author is defined it will be defined as the equivocation
reporter.
##### Attributes
| Name | Type |
| -------- | -------- | 
| equivocation_proof | `Box<EquivocationProof<T::Hash, T::BlockNumber>>` | 
| key_owner_proof | `T::KeyOwnerProof` | 

##### Python
```python
call = substrate.compose_call(
    'Grandpa', 'report_equivocation_unsigned', {
    'equivocation_proof': {
        'equivocation': {
            'Precommit': {
                'first': (
                    {
                        'target_hash': '[u8; 32]',
                        'target_number': 'u32',
                    },
                    '[u8; 64]',
                ),
                'identity': '[u8; 32]',
                'round_number': 'u64',
                'second': (
                    {
                        'target_hash': '[u8; 32]',
                        'target_number': 'u32',
                    },
                    '[u8; 64]',
                ),
            },
            'Prevote': {
                'first': (
                    {
                        'target_hash': '[u8; 32]',
                        'target_number': 'u32',
                    },
                    '[u8; 64]',
                ),
                'identity': '[u8; 32]',
                'round_number': 'u64',
                'second': (
                    {
                        'target_hash': '[u8; 32]',
                        'target_number': 'u32',
                    },
                    '[u8; 64]',
                ),
            },
        },
        'set_id': 'u64',
    },
    'key_owner_proof': (),
}
)
```

---------
#### note_stalled
Note that the current authority set of the GRANDPA finality gadget has stalled.

This will trigger a forced authority set change at the beginning of the next session, to
be enacted `delay` blocks after that. The `delay` should be high enough to safely assume
that the block signalling the forced change will not be re-orged e.g. 1000 blocks.
The block production rate (which may be slowed down because of finality lagging) should
be taken into account when choosing the `delay`. The GRANDPA voters based on the new
authority will start voting on top of `best_finalized_block_number` for new finalized
blocks. `best_finalized_block_number` should be the highest of the latest finalized
block of all validators of the new authority set.

Only callable by root.
##### Attributes
| Name | Type |
| -------- | -------- | 
| delay | `T::BlockNumber` | 
| best_finalized_block_number | `T::BlockNumber` | 

##### Python
```python
call = substrate.compose_call(
    'Grandpa', 'note_stalled', {
    'best_finalized_block_number': 'u32',
    'delay': 'u32',
}
)
```

---------
### Events
---------
#### NewAuthorities
New authority set has been applied.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| authority_set | `AuthorityList` | ```[('[u8; 32]', 'u64')]```

---------
#### Paused
Current authority set has been paused.
##### Attributes
No attributes

---------
#### Resumed
Current authority set has been resumed.
##### Attributes
No attributes

---------
### Storage functions
---------
#### State
 State of the current authority set.

##### Python
```python
result = substrate.query(
    'Grandpa', 'State', []
)
```

##### Return value
```python
{
    'Live': None,
    'Paused': None,
    'PendingPause': {'delay': 'u32', 'scheduled_at': 'u32'},
    'PendingResume': {'delay': 'u32', 'scheduled_at': 'u32'},
}
```
---------
#### PendingChange
 Pending change: (signaled at, scheduled change).

##### Python
```python
result = substrate.query(
    'Grandpa', 'PendingChange', []
)
```

##### Return value
```python
{
    'delay': 'u32',
    'forced': (None, 'u32'),
    'next_authorities': [('[u8; 32]', 'u64')],
    'scheduled_at': 'u32',
}
```
---------
#### NextForced
 next block number where we can force a change.

##### Python
```python
result = substrate.query(
    'Grandpa', 'NextForced', []
)
```

##### Return value
```python
'u32'
```
---------
#### Stalled
 `true` if we are currently stalled.

##### Python
```python
result = substrate.query(
    'Grandpa', 'Stalled', []
)
```

##### Return value
```python
('u32', 'u32')
```
---------
#### CurrentSetId
 The number of changes (both in terms of keys and underlying economic responsibilities)
 in the &quot;set&quot; of Grandpa validators from genesis.

##### Python
```python
result = substrate.query(
    'Grandpa', 'CurrentSetId', []
)
```

##### Return value
```python
'u64'
```
---------
#### SetIdSession
 A mapping from grandpa set ID to the index of the *most recent* session for which its
 members were responsible.

 TWOX-NOTE: `SetId` is not under user control.

##### Python
```python
result = substrate.query(
    'Grandpa', 'SetIdSession', ['u64']
)
```

##### Return value
```python
'u32'
```
---------
### Constants
---------
#### MaxAuthorities
 Max Authorities in use
##### Value
```python
32
```
##### Python
```python
constant = substrate.get_constant('Grandpa', 'MaxAuthorities')
```
---------
### Errors
---------
#### PauseFailed
Attempt to signal GRANDPA pause when the authority set isn&\#x27;t live
(either paused or already pending pause).

---------
#### ResumeFailed
Attempt to signal GRANDPA resume when the authority set isn&\#x27;t paused
(either live or already pending resume).

---------
#### ChangePending
Attempt to signal GRANDPA change with one already pending.

---------
#### TooSoon
Cannot signal forced change so soon after last.

---------
#### InvalidKeyOwnershipProof
A key ownership proof provided as part of an equivocation report is invalid.

---------
#### InvalidEquivocationProof
An equivocation proof provided as part of an equivocation report is invalid.

---------
#### DuplicateOffenceReport
A given equivocation report is valid but already previously reported.

---------

## Balances
---------
### Calls
---------
#### transfer
Transfer some liquid free balance to another account.

`transfer` will set the `FreeBalance` of the sender and receiver.
If the sender&\#x27;s account is below the existential deposit as a result
of the transfer, the account will be reaped.

The dispatch origin for this call must be `Signed` by the transactor.

\# &lt;weight&gt;
- Dependent on arguments but not critical, given proper implementations for input config
  types. See related functions below.
- It contains a limited number of reads and writes internally and no complex
  computation.

Related functions:

  - `ensure_can_withdraw` is always called internally but has a bounded complexity.
  - Transferring balances to accounts that did not exist before will cause
    `T::OnNewAccount::on_new_account` to be called.
  - Removing enough funds from an account will trigger `T::DustRemoval::on_unbalanced`.
  - `transfer_keep_alive` works the same way as `transfer`, but has an additional check
    that the transfer will not kill the origin account.
---------------------------------
- Origin account is already in memory, so no DB operations for them.
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `AccountIdLookupOf<T>` | 
| value | `T::Balance` | 

##### Python
```python
call = substrate.compose_call(
    'Balances', 'transfer', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'value': 'u128',
}
)
```

---------
#### set_balance
Set the balances of a given account.

This will alter `FreeBalance` and `ReservedBalance` in storage. it will
also alter the total issuance of the system (`TotalIssuance`) appropriately.
If the new free or reserved balance is below the existential deposit,
it will reset the account nonce (`frame_system::AccountNonce`).

The dispatch origin for this call is `root`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 
| new_free | `T::Balance` | 
| new_reserved | `T::Balance` | 

##### Python
```python
call = substrate.compose_call(
    'Balances', 'set_balance', {
    'new_free': 'u128',
    'new_reserved': 'u128',
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
#### force_transfer
Exactly as `transfer`, except the origin must be root and the source account may be
specified.
\# &lt;weight&gt;
- Same as transfer, but additional read and write because the source account is not
  assumed to be in the overlay.
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| source | `AccountIdLookupOf<T>` | 
| dest | `AccountIdLookupOf<T>` | 
| value | `T::Balance` | 

##### Python
```python
call = substrate.compose_call(
    'Balances', 'force_transfer', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'source': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'value': 'u128',
}
)
```

---------
#### transfer_keep_alive
Same as the [`transfer`] call, but with a check that the transfer will not kill the
origin account.

99% of the time you want [`transfer`] instead.

[`transfer`]: struct.Pallet.html\#method.transfer
##### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `AccountIdLookupOf<T>` | 
| value | `T::Balance` | 

##### Python
```python
call = substrate.compose_call(
    'Balances', 'transfer_keep_alive', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'value': 'u128',
}
)
```

---------
#### transfer_all
Transfer the entire transferable balance from the caller account.

NOTE: This function only attempts to transfer _transferable_ balances. This means that
any locked, reserved, or existential deposits (when `keep_alive` is `true`), will not be
transferred by this function. To ensure that this function results in a killed account,
you might need to prepare the account by removing any reference counters, storage
deposits, etc...

The dispatch origin of this call must be Signed.

- `dest`: The recipient of the transfer.
- `keep_alive`: A boolean to determine if the `transfer_all` operation should send all
  of the funds the account has, causing the sender account to be killed (false), or
  transfer everything except at least the existential deposit, which will guarantee to
  keep the sender account alive (true). \# &lt;weight&gt;
- O(1). Just like transfer, but reading the user&\#x27;s transferable balance first.
  \#&lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `AccountIdLookupOf<T>` | 
| keep_alive | `bool` | 

##### Python
```python
call = substrate.compose_call(
    'Balances', 'transfer_all', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'keep_alive': 'bool',
}
)
```

---------
#### force_unreserve
Unreserve some balance from a user by force.

Can only be called by ROOT.
##### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

##### Python
```python
call = substrate.compose_call(
    'Balances', 'force_unreserve', {
    'amount': 'u128',
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### Events
---------
#### Endowed
An account was created with some free balance.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| free_balance | `T::Balance` | ```u128```

---------
#### DustLost
An account was removed whose balance was non-zero but below ExistentialDeposit,
resulting in an outright loss.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
#### Transfer
Transfer succeeded.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
#### BalanceSet
A balance was set by root.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| free | `T::Balance` | ```u128```
| reserved | `T::Balance` | ```u128```

---------
#### Reserved
Some balance was reserved (moved from free to reserved).
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
#### Unreserved
Some balance was unreserved (moved from reserved to free).
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
#### ReserveRepatriated
Some balance was moved from the reserve of the first account to the second account.
Final argument indicates the destination balance type.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```
| destination_status | `Status` | ```('Free', 'Reserved')```

---------
#### Deposit
Some amount was deposited (e.g. for transaction fees).
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
#### Withdraw
Some amount was withdrawn from the account (e.g. for transaction fees).
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
#### Slashed
Some amount was removed from the account (e.g. for misbehavior).
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Storage functions
---------
#### TotalIssuance
 The total units issued in the system.

##### Python
```python
result = substrate.query(
    'Balances', 'TotalIssuance', []
)
```

##### Return value
```python
'u128'
```
---------
#### InactiveIssuance
 The total units of outstanding deactivated balance in the system.

##### Python
```python
result = substrate.query(
    'Balances', 'InactiveIssuance', []
)
```

##### Return value
```python
'u128'
```
---------
#### Account
 The Balances pallet example of storing the balance of an account.

 \# Example

 ```nocompile
  impl pallet_balances::Config for Runtime {
    type AccountStore = StorageMapShim&lt;Self::Account&lt;Runtime&gt;, frame_system::Provider&lt;Runtime&gt;, AccountId, Self::AccountData&lt;Balance&gt;&gt;
  }
 ```

 You can also store the balance of an account in the `System` pallet.

 \# Example

 ```nocompile
  impl pallet_balances::Config for Runtime {
   type AccountStore = System
  }
 ```

 But this comes with tradeoffs, storing account balances in the system pallet stores
 `frame_system` data alongside the account data contrary to storing account balances in the
 `Balances` pallet, which uses a `StorageMap` to store balances data only.
 NOTE: This is only used in the case that this pallet is used to store balances.

##### Python
```python
result = substrate.query(
    'Balances', 'Account', ['AccountId']
)
```

##### Return value
```python
{
    'fee_frozen': 'u128',
    'free': 'u128',
    'misc_frozen': 'u128',
    'reserved': 'u128',
}
```
---------
#### Locks
 Any liquidity locks on some account balances.
 NOTE: Should only be accessed when setting, changing and freeing a lock.

##### Python
```python
result = substrate.query(
    'Balances', 'Locks', ['AccountId']
)
```

##### Return value
```python
[{'amount': 'u128', 'id': '[u8; 8]', 'reasons': ('Fee', 'Misc', 'All')}]
```
---------
#### Reserves
 Named reserves on some account balances.

##### Python
```python
result = substrate.query(
    'Balances', 'Reserves', ['AccountId']
)
```

##### Return value
```python
[{'amount': 'u128', 'id': '[u8; 8]'}]
```
---------
### Constants
---------
#### ExistentialDeposit
 The minimum amount required to keep an account open.
##### Value
```python
1000000000000000
```
##### Python
```python
constant = substrate.get_constant('Balances', 'ExistentialDeposit')
```
---------
#### MaxLocks
 The maximum number of locks that should exist on an account.
 Not strictly enforced, but used for weight estimation.
##### Value
```python
50
```
##### Python
```python
constant = substrate.get_constant('Balances', 'MaxLocks')
```
---------
#### MaxReserves
 The maximum number of named reserves that can exist on an account.
##### Value
```python
0
```
##### Python
```python
constant = substrate.get_constant('Balances', 'MaxReserves')
```
---------
### Errors
---------
#### VestingBalance
Vesting balance too high to send value

---------
#### LiquidityRestrictions
Account liquidity restrictions prevent withdrawal

---------
#### InsufficientBalance
Balance too low to send value.

---------
#### ExistentialDeposit
Value too low to create account due to existential deposit

---------
#### KeepAlive
Transfer/payment would kill account

---------
#### ExistingVestingSchedule
A vesting schedule already exists for this account

---------
#### DeadAccount
Beneficiary account must pre-exist

---------
#### TooManyReserves
Number of named reserves exceed MaxReserves

---------

## TransactionPayment
---------
### Events
---------
#### TransactionFeePaid
A transaction fee `actual_fee`, of which `tip` was added to the minimum inclusion fee,
has been paid by `who`.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| actual_fee | `BalanceOf<T>` | ```u128```
| tip | `BalanceOf<T>` | ```u128```

---------
### Storage functions
---------
#### NextFeeMultiplier

##### Python
```python
result = substrate.query(
    'TransactionPayment', 'NextFeeMultiplier', []
)
```

##### Return value
```python
'u128'
```
---------
#### StorageVersion

##### Python
```python
result = substrate.query(
    'TransactionPayment', 'StorageVersion', []
)
```

##### Return value
```python
('V1Ancient', 'V2')
```
---------
### Constants
---------
#### OperationalFeeMultiplier
 A fee mulitplier for `Operational` extrinsics to compute &quot;virtual tip&quot; to boost their
 `priority`

 This value is multipled by the `final_fee` to obtain a &quot;virtual tip&quot; that is later
 added to a tip component in regular `priority` calculations.
 It means that a `Normal` transaction can front-run a similarly-sized `Operational`
 extrinsic (with no tip), by including a tip value greater than the virtual tip.

 ```rust,ignore
 // For `Normal`
 let priority = priority_calc(tip);

 // For `Operational`
 let virtual_tip = (inclusion_fee + tip) * OperationalFeeMultiplier;
 let priority = priority_calc(tip + virtual_tip);
 ```

 Note that since we use `final_fee` the multiplier applies also to the regular `tip`
 sent with the transaction. So, not only does the transaction get a priority bump based
 on the `inclusion_fee`, but we also amplify the impact of tips applied to `Operational`
 transactions.
##### Value
```python
5
```
##### Python
```python
constant = substrate.get_constant('TransactionPayment', 'OperationalFeeMultiplier')
```
---------

## Sudo
---------
### Calls
---------
#### sudo
Authenticates the sudo key and dispatches a function call with `Root` origin.

The dispatch origin for this call must be _Signed_.

\# &lt;weight&gt;
- O(1).
- Limited storage reads.
- One DB write (event).
- Weight of derivative `call` execution + 10,000.
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Sudo', 'sudo', {'call': 'Call'}
)
```

---------
#### sudo_unchecked_weight
Authenticates the sudo key and dispatches a function call with `Root` origin.
This function does not check the weight of the call, and instead allows the
Sudo user to specify the weight of the call.

The dispatch origin for this call must be _Signed_.

\# &lt;weight&gt;
- O(1).
- The weight of this call is defined by the caller.
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::RuntimeCall>` | 
| weight | `Weight` | 

##### Python
```python
call = substrate.compose_call(
    'Sudo', 'sudo_unchecked_weight', {
    'call': 'Call',
    'weight': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
#### set_key
Authenticates the current sudo key and sets the given AccountId (`new`) as the new sudo
key.

The dispatch origin for this call must be _Signed_.

\# &lt;weight&gt;
- O(1).
- Limited storage reads.
- One DB change.
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| new | `AccountIdLookupOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Sudo', 'set_key', {
    'new': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
#### sudo_as
Authenticates the sudo key and dispatches a function call with `Signed` origin from
a given account.

The dispatch origin for this call must be _Signed_.

\# &lt;weight&gt;
- O(1).
- Limited storage reads.
- One DB write (event).
- Weight of derivative `call` execution + 10,000.
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Sudo', 'sudo_as', {
    'call': 'Call',
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### Events
---------
#### Sudid
A sudo just took place. \[result\]
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sudo_result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
#### KeyChanged
The \[sudoer\] just switched identity; the old key is supplied if one existed.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_sudoer | `Option<T::AccountId>` | ```(None, 'AccountId')```

---------
#### SudoAsDone
A sudo just took place. \[result\]
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sudo_result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### Storage functions
---------
#### Key
 The `AccountId` of the sudo key.

##### Python
```python
result = substrate.query(
    'Sudo', 'Key', []
)
```

##### Return value
```python
'AccountId'
```
---------
### Errors
---------
#### RequireSudo
Sender must be the Sudo account

---------

## Multisig
---------
### Calls
---------
#### as_multi_threshold_1
Immediately dispatch a multi-signature call using a single approval from the caller.

The dispatch origin for this call must be _Signed_.

- `other_signatories`: The accounts (other than the sender) who are part of the
multi-signature, but do not participate in the approval process.
- `call`: The call to be executed.

Result is equivalent to the dispatched result.

\# &lt;weight&gt;
O(Z + C) where Z is the length of the call and C its execution weight.
-------------------------------
- DB Weight: None
- Plus Call Weight
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| other_signatories | `Vec<T::AccountId>` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Multisig', 'as_multi_threshold_1', {
    'call': 'Call',
    'other_signatories': ['AccountId'],
}
)
```

---------
#### as_multi
Register approval for a dispatch to be made from a deterministic composite account if
approved by a total of `threshold - 1` of `other_signatories`.

If there are enough, then dispatch the call.

Payment: `DepositBase` will be reserved if this is the first approval, plus
`threshold` times `DepositFactor`. It is returned once this dispatch happens or
is cancelled.

The dispatch origin for this call must be _Signed_.

- `threshold`: The total number of approvals for this dispatch before it is executed.
- `other_signatories`: The accounts (other than the sender) who can approve this
dispatch. May not be empty.
- `maybe_timepoint`: If this is the first approval, then this must be `None`. If it is
not the first approval, then it must be `Some`, with the timepoint (block number and
transaction index) of the first approval transaction.
- `call`: The call to be executed.

NOTE: Unless this is the final approval, you will generally want to use
`approve_as_multi` instead, since it only requires a hash of the call.

Result is equivalent to the dispatched result if `threshold` is exactly `1`. Otherwise
on success, result is `Ok` and the result from the interior call, if it was executed,
may be found in the deposited `MultisigExecuted` event.

\# &lt;weight&gt;
- `O(S + Z + Call)`.
- Up to one balance-reserve or unreserve operation.
- One passthrough operation, one insert, both `O(S)` where `S` is the number of
  signatories. `S` is capped by `MaxSignatories`, with weight being proportional.
- One call encode &amp; hash, both of complexity `O(Z)` where `Z` is tx-len.
- One encode &amp; hash, both of complexity `O(S)`.
- Up to one binary search and insert (`O(logS + S)`).
- I/O: 1 read `O(S)`, up to 1 mutate `O(S)`. Up to one remove.
- One event.
- The weight of the `call`.
- Storage: inserts one item, value size bounded by `MaxSignatories`, with a deposit
  taken for its lifetime of `DepositBase + threshold * DepositFactor`.
-------------------------------
- DB Weight:
    - Reads: Multisig Storage, [Caller Account]
    - Writes: Multisig Storage, [Caller Account]
- Plus Call Weight
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `u16` | 
| other_signatories | `Vec<T::AccountId>` | 
| maybe_timepoint | `Option<Timepoint<T::BlockNumber>>` | 
| call | `Box<<T as Config>::RuntimeCall>` | 
| max_weight | `Weight` | 

##### Python
```python
call = substrate.compose_call(
    'Multisig', 'as_multi', {
    'call': 'Call',
    'max_weight': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
    'maybe_timepoint': (
        None,
        {
            'height': 'u32',
            'index': 'u32',
        },
    ),
    'other_signatories': ['AccountId'],
    'threshold': 'u16',
}
)
```

---------
#### approve_as_multi
Register approval for a dispatch to be made from a deterministic composite account if
approved by a total of `threshold - 1` of `other_signatories`.

Payment: `DepositBase` will be reserved if this is the first approval, plus
`threshold` times `DepositFactor`. It is returned once this dispatch happens or
is cancelled.

The dispatch origin for this call must be _Signed_.

- `threshold`: The total number of approvals for this dispatch before it is executed.
- `other_signatories`: The accounts (other than the sender) who can approve this
dispatch. May not be empty.
- `maybe_timepoint`: If this is the first approval, then this must be `None`. If it is
not the first approval, then it must be `Some`, with the timepoint (block number and
transaction index) of the first approval transaction.
- `call_hash`: The hash of the call to be executed.

NOTE: If this is the final approval, you will want to use `as_multi` instead.

\# &lt;weight&gt;
- `O(S)`.
- Up to one balance-reserve or unreserve operation.
- One passthrough operation, one insert, both `O(S)` where `S` is the number of
  signatories. `S` is capped by `MaxSignatories`, with weight being proportional.
- One encode &amp; hash, both of complexity `O(S)`.
- Up to one binary search and insert (`O(logS + S)`).
- I/O: 1 read `O(S)`, up to 1 mutate `O(S)`. Up to one remove.
- One event.
- Storage: inserts one item, value size bounded by `MaxSignatories`, with a deposit
  taken for its lifetime of `DepositBase + threshold * DepositFactor`.
----------------------------------
- DB Weight:
    - Read: Multisig Storage, [Caller Account]
    - Write: Multisig Storage, [Caller Account]
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `u16` | 
| other_signatories | `Vec<T::AccountId>` | 
| maybe_timepoint | `Option<Timepoint<T::BlockNumber>>` | 
| call_hash | `[u8; 32]` | 
| max_weight | `Weight` | 

##### Python
```python
call = substrate.compose_call(
    'Multisig', 'approve_as_multi', {
    'call_hash': '[u8; 32]',
    'max_weight': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
    'maybe_timepoint': (
        None,
        {
            'height': 'u32',
            'index': 'u32',
        },
    ),
    'other_signatories': ['AccountId'],
    'threshold': 'u16',
}
)
```

---------
#### cancel_as_multi
Cancel a pre-existing, on-going multisig transaction. Any deposit reserved previously
for this operation will be unreserved on success.

The dispatch origin for this call must be _Signed_.

- `threshold`: The total number of approvals for this dispatch before it is executed.
- `other_signatories`: The accounts (other than the sender) who can approve this
dispatch. May not be empty.
- `timepoint`: The timepoint (block number and transaction index) of the first approval
transaction for this dispatch.
- `call_hash`: The hash of the call to be executed.

\# &lt;weight&gt;
- `O(S)`.
- Up to one balance-reserve or unreserve operation.
- One passthrough operation, one insert, both `O(S)` where `S` is the number of
  signatories. `S` is capped by `MaxSignatories`, with weight being proportional.
- One encode &amp; hash, both of complexity `O(S)`.
- One event.
- I/O: 1 read `O(S)`, one remove.
- Storage: removes one item.
----------------------------------
- DB Weight:
    - Read: Multisig Storage, [Caller Account], Refund Account
    - Write: Multisig Storage, [Caller Account], Refund Account
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `u16` | 
| other_signatories | `Vec<T::AccountId>` | 
| timepoint | `Timepoint<T::BlockNumber>` | 
| call_hash | `[u8; 32]` | 

##### Python
```python
call = substrate.compose_call(
    'Multisig', 'cancel_as_multi', {
    'call_hash': '[u8; 32]',
    'other_signatories': ['AccountId'],
    'threshold': 'u16',
    'timepoint': {
        'height': 'u32',
        'index': 'u32',
    },
}
)
```

---------
### Events
---------
#### NewMultisig
A new multisig operation has begun.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| approving | `T::AccountId` | ```AccountId```
| multisig | `T::AccountId` | ```AccountId```
| call_hash | `CallHash` | ```[u8; 32]```

---------
#### MultisigApproval
A multisig operation has been approved by someone.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| approving | `T::AccountId` | ```AccountId```
| timepoint | `Timepoint<T::BlockNumber>` | ```{'height': 'u32', 'index': 'u32'}```
| multisig | `T::AccountId` | ```AccountId```
| call_hash | `CallHash` | ```[u8; 32]```

---------
#### MultisigExecuted
A multisig operation has been executed.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| approving | `T::AccountId` | ```AccountId```
| timepoint | `Timepoint<T::BlockNumber>` | ```{'height': 'u32', 'index': 'u32'}```
| multisig | `T::AccountId` | ```AccountId```
| call_hash | `CallHash` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
#### MultisigCancelled
A multisig operation has been cancelled.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| cancelling | `T::AccountId` | ```AccountId```
| timepoint | `Timepoint<T::BlockNumber>` | ```{'height': 'u32', 'index': 'u32'}```
| multisig | `T::AccountId` | ```AccountId```
| call_hash | `CallHash` | ```[u8; 32]```

---------
### Storage functions
---------
#### Multisigs
 The set of open multisig operations.

##### Python
```python
result = substrate.query(
    'Multisig', 'Multisigs', ['AccountId', '[u8; 32]']
)
```

##### Return value
```python
{
    'approvals': ['AccountId'],
    'deposit': 'u128',
    'depositor': 'AccountId',
    'when': {'height': 'u32', 'index': 'u32'},
}
```
---------
### Constants
---------
#### DepositBase
 The base amount of currency needed to reserve for creating a multisig execution or to
 store a dispatch call for later.

 This is held for an additional storage item whose value size is
 `4 + sizeof((BlockNumber, Balance, AccountId))` bytes and whose key size is
 `32 + sizeof(AccountId)` bytes.
##### Value
```python
2088000000000000000
```
##### Python
```python
constant = substrate.get_constant('Multisig', 'DepositBase')
```
---------
#### DepositFactor
 The amount of currency needed per unit threshold when creating a multisig execution.

 This is held for adding 32 bytes more into a pre-existing storage value.
##### Value
```python
32000000000000000
```
##### Python
```python
constant = substrate.get_constant('Multisig', 'DepositFactor')
```
---------
#### MaxSignatories
 The maximum amount of signatories allowed in the multisig.
##### Value
```python
100
```
##### Python
```python
constant = substrate.get_constant('Multisig', 'MaxSignatories')
```
---------
### Errors
---------
#### MinimumThreshold
Threshold must be 2 or greater.

---------
#### AlreadyApproved
Call is already approved by this signatory.

---------
#### NoApprovalsNeeded
Call doesn&\#x27;t need any (more) approvals.

---------
#### TooFewSignatories
There are too few signatories in the list.

---------
#### TooManySignatories
There are too many signatories in the list.

---------
#### SignatoriesOutOfOrder
The signatories were provided out of order; they should be ordered.

---------
#### SenderInSignatories
The sender was contained in the other signatories; it shouldn&\#x27;t be.

---------
#### NotFound
Multisig operation not found when attempting to cancel.

---------
#### NotOwner
Only the account that originally created the multisig is able to cancel it.

---------
#### NoTimepoint
No timepoint was given, yet the multisig operation is already underway.

---------
#### WrongTimepoint
A different timepoint was given to the multisig operation that is underway.

---------
#### UnexpectedTimepoint
A timepoint was given, yet no multisig operation is underway.

---------
#### MaxWeightTooLow
The maximum weight information provided was too low.

---------
#### AlreadyStored
The data to be stored is already stored.

---------

## Utility
---------
### Calls
---------
#### batch
Send a batch of dispatch calls.

May be called from any origin except `None`.

- `calls`: The calls to be dispatched from the same origin. The number of call must not
  exceed the constant: `batched_calls_limit` (available in constant metadata).

If origin is root then the calls are dispatched without checking origin filter. (This
includes bypassing `frame_system::Config::BaseCallFilter`).

\# &lt;weight&gt;
- Complexity: O(C) where C is the number of calls to be batched.
\# &lt;/weight&gt;

This will return `Ok` in all circumstances. To determine the success of the batch, an
event is deposited. If a call failed and the batch was interrupted, then the
`BatchInterrupted` event is deposited, along with the number of successful calls made
and the error of the failed call. If all were successful, then the `BatchCompleted`
event is deposited.
##### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Utility', 'batch', {'calls': ['Call']}
)
```

---------
#### as_derivative
Send a call through an indexed pseudonym of the sender.

Filter from origin are passed along. The call will be dispatched with an origin which
use the same filter as the origin of this call.

NOTE: If you need to ensure that any account-based filtering is not honored (i.e.
because you expect `proxy` to have been used prior in the call stack and you do not want
the call restrictions to apply to any sub-accounts), then use `as_multi_threshold_1`
in the Multisig pallet instead.

NOTE: Prior to version *12, this was called `as_limited_sub`.

The dispatch origin for this call must be _Signed_.
##### Attributes
| Name | Type |
| -------- | -------- | 
| index | `u16` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Utility', 'as_derivative', {'call': 'Call', 'index': 'u16'}
)
```

---------
#### batch_all
Send a batch of dispatch calls and atomically execute them.
The whole transaction will rollback and fail if any of the calls failed.

May be called from any origin except `None`.

- `calls`: The calls to be dispatched from the same origin. The number of call must not
  exceed the constant: `batched_calls_limit` (available in constant metadata).

If origin is root then the calls are dispatched without checking origin filter. (This
includes bypassing `frame_system::Config::BaseCallFilter`).

\# &lt;weight&gt;
- Complexity: O(C) where C is the number of calls to be batched.
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Utility', 'batch_all', {'calls': ['Call']}
)
```

---------
#### dispatch_as
Dispatches a function call with a provided origin.

The dispatch origin for this call must be _Root_.

\# &lt;weight&gt;
- O(1).
- Limited storage reads.
- One DB write (event).
- Weight of derivative `call` execution + T::WeightInfo::dispatch_as().
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| as_origin | `Box<T::PalletsOrigin>` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Utility', 'dispatch_as', {
    'as_origin': {
        'Void': (),
        'system': {
            'None': None,
            'Root': None,
            'Signed': 'AccountId',
        },
    },
    'call': 'Call',
}
)
```

---------
#### force_batch
Send a batch of dispatch calls.
Unlike `batch`, it allows errors and won&\#x27;t interrupt.

May be called from any origin except `None`.

- `calls`: The calls to be dispatched from the same origin. The number of call must not
  exceed the constant: `batched_calls_limit` (available in constant metadata).

If origin is root then the calls are dispatch without checking origin filter. (This
includes bypassing `frame_system::Config::BaseCallFilter`).

\# &lt;weight&gt;
- Complexity: O(C) where C is the number of calls to be batched.
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Utility', 'force_batch', {'calls': ['Call']}
)
```

---------
#### with_weight
Dispatch a function call with a specified weight.

This function does not check the weight of the call, and instead allows the
Root origin to specify the weight of the call.

The dispatch origin for this call must be _Root_.
##### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::RuntimeCall>` | 
| weight | `Weight` | 

##### Python
```python
call = substrate.compose_call(
    'Utility', 'with_weight', {
    'call': 'Call',
    'weight': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
### Events
---------
#### BatchInterrupted
Batch of dispatches did not complete fully. Index of first failing dispatch given, as
well as the error.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `u32` | ```u32```
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
#### BatchCompleted
Batch of dispatches completed fully with no error.
##### Attributes
No attributes

---------
#### BatchCompletedWithErrors
Batch of dispatches completed but has errors.
##### Attributes
No attributes

---------
#### ItemCompleted
A single item within a Batch of dispatches has completed with no error.
##### Attributes
No attributes

---------
#### ItemFailed
A single item within a Batch of dispatches has completed with error.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
#### DispatchedAs
A call was dispatched.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### Constants
---------
#### batched_calls_limit
 The limit on the number of batched calls.
##### Value
```python
10922
```
##### Python
```python
constant = substrate.get_constant('Utility', 'batched_calls_limit')
```
---------
### Errors
---------
#### TooManyCalls
Too many calls batched.

---------

## Scheduler
---------
### Calls
---------
#### schedule
Anonymously schedule a task.
##### Attributes
| Name | Type |
| -------- | -------- | 
| when | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule', {
    'call': 'Call',
    'maybe_periodic': (
        None,
        ('u32', 'u32'),
    ),
    'priority': 'u8',
    'when': 'u32',
}
)
```

---------
#### cancel
Cancel an anonymously scheduled task.
##### Attributes
| Name | Type |
| -------- | -------- | 
| when | `T::BlockNumber` | 
| index | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'Scheduler', 'cancel', {'index': 'u32', 'when': 'u32'}
)
```

---------
#### schedule_named
Schedule a named task.
##### Attributes
| Name | Type |
| -------- | -------- | 
| id | `TaskName` | 
| when | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule_named', {
    'call': 'Call',
    'id': '[u8; 32]',
    'maybe_periodic': (
        None,
        ('u32', 'u32'),
    ),
    'priority': 'u8',
    'when': 'u32',
}
)
```

---------
#### cancel_named
Cancel a named scheduled task.
##### Attributes
| Name | Type |
| -------- | -------- | 
| id | `TaskName` | 

##### Python
```python
call = substrate.compose_call(
    'Scheduler', 'cancel_named', {'id': '[u8; 32]'}
)
```

---------
#### schedule_after
Anonymously schedule a task after a delay.

\# &lt;weight&gt;
Same as [`schedule`].
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| after | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule_after', {
    'after': 'u32',
    'call': 'Call',
    'maybe_periodic': (
        None,
        ('u32', 'u32'),
    ),
    'priority': 'u8',
}
)
```

---------
#### schedule_named_after
Schedule a named task after a delay.

\# &lt;weight&gt;
Same as [`schedule_named`](Self::schedule_named).
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| id | `TaskName` | 
| after | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule_named_after', {
    'after': 'u32',
    'call': 'Call',
    'id': '[u8; 32]',
    'maybe_periodic': (
        None,
        ('u32', 'u32'),
    ),
    'priority': 'u8',
}
)
```

---------
### Events
---------
#### Scheduled
Scheduled some task.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| when | `T::BlockNumber` | ```u32```
| index | `u32` | ```u32```

---------
#### Canceled
Canceled some task.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| when | `T::BlockNumber` | ```u32```
| index | `u32` | ```u32```

---------
#### Dispatched
Dispatched some task.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<TaskName>` | ```(None, '[u8; 32]')```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
#### CallUnavailable
The call for the provided hash was not found so the task has been aborted.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<TaskName>` | ```(None, '[u8; 32]')```

---------
#### PeriodicFailed
The given task was unable to be renewed since the agenda is full at that block.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<TaskName>` | ```(None, '[u8; 32]')```

---------
#### PermanentlyOverweight
The given task can never be executed since it is overweight.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<TaskName>` | ```(None, '[u8; 32]')```

---------
### Storage functions
---------
#### IncompleteSince

##### Python
```python
result = substrate.query(
    'Scheduler', 'IncompleteSince', []
)
```

##### Return value
```python
'u32'
```
---------
#### Agenda
 Items to be executed, indexed by the block number that they should be executed on.

##### Python
```python
result = substrate.query(
    'Scheduler', 'Agenda', ['u32']
)
```

##### Return value
```python
[
    (
        None,
        {
            'call': {
                'Inline': 'Bytes',
                'Legacy': {'hash': '[u8; 32]'},
                'Lookup': {'hash': '[u8; 32]', 'len': 'u32'},
            },
            'maybe_id': (None, '[u8; 32]'),
            'maybe_periodic': (None, ('u32', 'u32')),
            'origin': {
                'Void': (),
                'system': {'None': None, 'Root': None, 'Signed': 'AccountId'},
            },
            'priority': 'u8',
        },
    ),
]
```
---------
#### Lookup
 Lookup from a name to the block number and index of the task.

 For v3 -&gt; v4 the previously unbounded identities are Blake2-256 hashed to form the v4
 identities.

##### Python
```python
result = substrate.query(
    'Scheduler', 'Lookup', ['[u8; 32]']
)
```

##### Return value
```python
('u32', 'u32')
```
---------
### Constants
---------
#### MaximumWeight
 The maximum weight that may be scheduled per block for any dispatchables.
##### Value
```python
{'proof_size': 14757395258967641292, 'ref_time': 1600000000000}
```
##### Python
```python
constant = substrate.get_constant('Scheduler', 'MaximumWeight')
```
---------
#### MaxScheduledPerBlock
 The maximum number of scheduled calls in the queue for a single block.
##### Value
```python
50
```
##### Python
```python
constant = substrate.get_constant('Scheduler', 'MaxScheduledPerBlock')
```
---------
### Errors
---------
#### FailedToSchedule
Failed to schedule a call

---------
#### NotFound
Cannot find the scheduled call.

---------
#### TargetBlockNumberInPast
Given target block number is in the past.

---------
#### RescheduleNoChange
Reschedule failed because it does not change scheduled time.

---------
#### Named
Attempt to use a non-named function on a named task.

---------

## Preimage
---------
### Calls
---------
#### note_preimage
Register a preimage on-chain.

If the preimage was previously requested, no fees or deposits are taken for providing
the preimage. Otherwise, a deposit is taken proportional to the size of the preimage.
##### Attributes
| Name | Type |
| -------- | -------- | 
| bytes | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'Preimage', 'note_preimage', {'bytes': 'Bytes'}
)
```

---------
#### unnote_preimage
Clear an unrequested preimage from the runtime storage.

If `len` is provided, then it will be a much cheaper operation.

- `hash`: The hash of the preimage to be removed from the store.
- `len`: The length of the preimage of `hash`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

##### Python
```python
call = substrate.compose_call(
    'Preimage', 'unnote_preimage', {'hash': '[u8; 32]'}
)
```

---------
#### request_preimage
Request a preimage be uploaded to the chain without paying any fees or deposits.

If the preimage requests has already been provided on-chain, we unreserve any deposit
a user may have paid, and take the control of the preimage out of their hands.
##### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

##### Python
```python
call = substrate.compose_call(
    'Preimage', 'request_preimage', {'hash': '[u8; 32]'}
)
```

---------
#### unrequest_preimage
Clear a previously made request for a preimage.

NOTE: THIS MUST NOT BE CALLED ON `hash` MORE TIMES THAN `request_preimage`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

##### Python
```python
call = substrate.compose_call(
    'Preimage', 'unrequest_preimage', {'hash': '[u8; 32]'}
)
```

---------
### Events
---------
#### Noted
A preimage has been noted.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```[u8; 32]```

---------
#### Requested
A preimage has been requested.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```[u8; 32]```

---------
#### Cleared
A preimage has ben cleared.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```[u8; 32]```

---------
### Storage functions
---------
#### StatusFor
 The request status of a given hash.

##### Python
```python
result = substrate.query(
    'Preimage', 'StatusFor', ['[u8; 32]']
)
```

##### Return value
```python
{
    'Requested': {
        'count': 'u32',
        'deposit': (None, ('AccountId', 'u128')),
        'len': (None, 'u32'),
    },
    'Unrequested': {'deposit': ('AccountId', 'u128'), 'len': 'u32'},
}
```
---------
#### PreimageFor

##### Python
```python
result = substrate.query(
    'Preimage', 'PreimageFor', [('[u8; 32]', 'u32')]
)
```

##### Return value
```python
'Bytes'
```
---------
### Errors
---------
#### TooBig
Preimage is too large to store on-chain.

---------
#### AlreadyNoted
Preimage has already been noted on-chain.

---------
#### NotAuthorized
The user is not authorized to perform this action.

---------
#### NotNoted
The preimage cannot be removed since it has not yet been noted.

---------
#### Requested
A preimage may not be removed when there are outstanding requests.

---------
#### NotRequested
The preimage request cannot be removed since no outstanding requests exist.

---------

## Proxy
---------
### Calls
---------
#### proxy
Dispatch the given `call` from an account that the sender is authorised for through
`add_proxy`.

Removes any corresponding announcement(s).

The dispatch origin for this call must be _Signed_.

Parameters:
- `real`: The account that the proxy will make a call on behalf of.
- `force_proxy_type`: Specify the exact proxy type to be used and checked for this call.
- `call`: The call to be made by the `real` account.
##### Attributes
| Name | Type |
| -------- | -------- | 
| real | `AccountIdLookupOf<T>` | 
| force_proxy_type | `Option<T::ProxyType>` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Proxy', 'proxy', {
    'call': 'Call',
    'force_proxy_type': (
        None,
        ('Any', ),
    ),
    'real': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
#### add_proxy
Register a proxy account for the sender that is able to make calls on its behalf.

The dispatch origin for this call must be _Signed_.

Parameters:
- `proxy`: The account that the `caller` would like to make a proxy.
- `proxy_type`: The permissions allowed for this proxy account.
- `delay`: The announcement period required of the initial proxy. Will generally be
zero.
##### Attributes
| Name | Type |
| -------- | -------- | 
| delegate | `AccountIdLookupOf<T>` | 
| proxy_type | `T::ProxyType` | 
| delay | `T::BlockNumber` | 

##### Python
```python
call = substrate.compose_call(
    'Proxy', 'add_proxy', {
    'delay': 'u32',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'proxy_type': ('Any', ),
}
)
```

---------
#### remove_proxy
Unregister a proxy account for the sender.

The dispatch origin for this call must be _Signed_.

Parameters:
- `proxy`: The account that the `caller` would like to remove as a proxy.
- `proxy_type`: The permissions currently enabled for the removed proxy account.
##### Attributes
| Name | Type |
| -------- | -------- | 
| delegate | `AccountIdLookupOf<T>` | 
| proxy_type | `T::ProxyType` | 
| delay | `T::BlockNumber` | 

##### Python
```python
call = substrate.compose_call(
    'Proxy', 'remove_proxy', {
    'delay': 'u32',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'proxy_type': ('Any', ),
}
)
```

---------
#### remove_proxies
Unregister all proxy accounts for the sender.

The dispatch origin for this call must be _Signed_.

WARNING: This may be called on accounts created by `pure`, however if done, then
the unreserved fees will be inaccessible. **All access to this account will be lost.**
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'Proxy', 'remove_proxies', {}
)
```

---------
#### create_pure
Spawn a fresh new account that is guaranteed to be otherwise inaccessible, and
initialize it with a proxy of `proxy_type` for `origin` sender.

Requires a `Signed` origin.

- `proxy_type`: The type of the proxy that the sender will be registered as over the
new account. This will almost always be the most permissive `ProxyType` possible to
allow for maximum flexibility.
- `index`: A disambiguation index, in case this is called multiple times in the same
transaction (e.g. with `utility::batch`). Unless you&\#x27;re using `batch` you probably just
want to use `0`.
- `delay`: The announcement period required of the initial proxy. Will generally be
zero.

Fails with `Duplicate` if this has already been called in this transaction, from the
same sender, with the same parameters.

Fails if there are insufficient funds to pay for deposit.
##### Attributes
| Name | Type |
| -------- | -------- | 
| proxy_type | `T::ProxyType` | 
| delay | `T::BlockNumber` | 
| index | `u16` | 

##### Python
```python
call = substrate.compose_call(
    'Proxy', 'create_pure', {
    'delay': 'u32',
    'index': 'u16',
    'proxy_type': ('Any', ),
}
)
```

---------
#### kill_pure
Removes a previously spawned pure proxy.

WARNING: **All access to this account will be lost.** Any funds held in it will be
inaccessible.

Requires a `Signed` origin, and the sender account must have been created by a call to
`pure` with corresponding parameters.

- `spawner`: The account that originally called `pure` to create this account.
- `index`: The disambiguation index originally passed to `pure`. Probably `0`.
- `proxy_type`: The proxy type originally passed to `pure`.
- `height`: The height of the chain when the call to `pure` was processed.
- `ext_index`: The extrinsic index in which the call to `pure` was processed.

Fails with `NoPermission` in case the caller is not a previously created pure
account whose `pure` call has corresponding parameters.
##### Attributes
| Name | Type |
| -------- | -------- | 
| spawner | `AccountIdLookupOf<T>` | 
| proxy_type | `T::ProxyType` | 
| index | `u16` | 
| height | `T::BlockNumber` | 
| ext_index | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'Proxy', 'kill_pure', {
    'ext_index': 'u32',
    'height': 'u32',
    'index': 'u16',
    'proxy_type': ('Any', ),
    'spawner': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
#### announce
Publish the hash of a proxy-call that will be made in the future.

This must be called some number of blocks before the corresponding `proxy` is attempted
if the delay associated with the proxy relationship is greater than zero.

No more than `MaxPending` announcements may be made at any one time.

This will take a deposit of `AnnouncementDepositFactor` as well as
`AnnouncementDepositBase` if there are no other pending announcements.

The dispatch origin for this call must be _Signed_ and a proxy of `real`.

Parameters:
- `real`: The account that the proxy will make a call on behalf of.
- `call_hash`: The hash of the call to be made by the `real` account.
##### Attributes
| Name | Type |
| -------- | -------- | 
| real | `AccountIdLookupOf<T>` | 
| call_hash | `CallHashOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Proxy', 'announce', {
    'call_hash': '[u8; 32]',
    'real': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
#### remove_announcement
Remove a given announcement.

May be called by a proxy account to remove a call they previously announced and return
the deposit.

The dispatch origin for this call must be _Signed_.

Parameters:
- `real`: The account that the proxy will make a call on behalf of.
- `call_hash`: The hash of the call to be made by the `real` account.
##### Attributes
| Name | Type |
| -------- | -------- | 
| real | `AccountIdLookupOf<T>` | 
| call_hash | `CallHashOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Proxy', 'remove_announcement', {
    'call_hash': '[u8; 32]',
    'real': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
#### reject_announcement
Remove the given announcement of a delegate.

May be called by a target (proxied) account to remove a call that one of their delegates
(`delegate`) has announced they want to execute. The deposit is returned.

The dispatch origin for this call must be _Signed_.

Parameters:
- `delegate`: The account that previously announced the call.
- `call_hash`: The hash of the call to be made.
##### Attributes
| Name | Type |
| -------- | -------- | 
| delegate | `AccountIdLookupOf<T>` | 
| call_hash | `CallHashOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Proxy', 'reject_announcement', {
    'call_hash': '[u8; 32]',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
#### proxy_announced
Dispatch the given `call` from an account that the sender is authorized for through
`add_proxy`.

Removes any corresponding announcement(s).

The dispatch origin for this call must be _Signed_.

Parameters:
- `real`: The account that the proxy will make a call on behalf of.
- `force_proxy_type`: Specify the exact proxy type to be used and checked for this call.
- `call`: The call to be made by the `real` account.
##### Attributes
| Name | Type |
| -------- | -------- | 
| delegate | `AccountIdLookupOf<T>` | 
| real | `AccountIdLookupOf<T>` | 
| force_proxy_type | `Option<T::ProxyType>` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

##### Python
```python
call = substrate.compose_call(
    'Proxy', 'proxy_announced', {
    'call': 'Call',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'force_proxy_type': (
        None,
        ('Any', ),
    ),
    'real': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### Events
---------
#### ProxyExecuted
A proxy was executed correctly, with the given.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
#### PureCreated
A pure account has been created by new proxy with given
disambiguation index and proxy type.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pure | `T::AccountId` | ```AccountId```
| who | `T::AccountId` | ```AccountId```
| proxy_type | `T::ProxyType` | ```('Any',)```
| disambiguation_index | `u16` | ```u16```

---------
#### Announced
An announcement was placed to make a call in the future.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| real | `T::AccountId` | ```AccountId```
| proxy | `T::AccountId` | ```AccountId```
| call_hash | `CallHashOf<T>` | ```[u8; 32]```

---------
#### ProxyAdded
A proxy was added.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```AccountId```
| delegatee | `T::AccountId` | ```AccountId```
| proxy_type | `T::ProxyType` | ```('Any',)```
| delay | `T::BlockNumber` | ```u32```

---------
#### ProxyRemoved
A proxy was removed.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```AccountId```
| delegatee | `T::AccountId` | ```AccountId```
| proxy_type | `T::ProxyType` | ```('Any',)```
| delay | `T::BlockNumber` | ```u32```

---------
### Storage functions
---------
#### Proxies
 The set of account proxies. Maps the account which has delegated to the accounts
 which are being delegated to, together with the amount held on deposit.

##### Python
```python
result = substrate.query(
    'Proxy', 'Proxies', ['AccountId']
)
```

##### Return value
```python
([{'delay': 'u32', 'delegate': 'AccountId', 'proxy_type': ('Any', )}], 'u128')
```
---------
#### Announcements
 The announcements made by the proxy (key).

##### Python
```python
result = substrate.query(
    'Proxy', 'Announcements', ['AccountId']
)
```

##### Return value
```python
([{'call_hash': '[u8; 32]', 'height': 'u32', 'real': 'AccountId'}], 'u128')
```
---------
### Constants
---------
#### ProxyDepositBase
 The base amount of currency needed to reserve for creating a proxy.

 This is held for an additional storage item whose value size is
 `sizeof(Balance)` bytes and whose key size is `sizeof(AccountId)` bytes.
##### Value
```python
2008000000000000000
```
##### Python
```python
constant = substrate.get_constant('Proxy', 'ProxyDepositBase')
```
---------
#### ProxyDepositFactor
 The amount of currency needed per proxy added.

 This is held for adding 32 bytes plus an instance of `ProxyType` more into a
 pre-existing storage value. Thus, when configuring `ProxyDepositFactor` one should take
 into account `32 + proxy_type.encode().len()` bytes of data.
##### Value
```python
33000000000000000
```
##### Python
```python
constant = substrate.get_constant('Proxy', 'ProxyDepositFactor')
```
---------
#### MaxProxies
 The maximum amount of proxies allowed for a single account.
##### Value
```python
32
```
##### Python
```python
constant = substrate.get_constant('Proxy', 'MaxProxies')
```
---------
#### MaxPending
 The maximum amount of time-delayed announcements that are allowed to be pending.
##### Value
```python
32
```
##### Python
```python
constant = substrate.get_constant('Proxy', 'MaxPending')
```
---------
#### AnnouncementDepositBase
 The base amount of currency needed to reserve for creating an announcement.

 This is held when a new storage item holding a `Balance` is created (typically 16
 bytes).
##### Value
```python
2008000000000000000
```
##### Python
```python
constant = substrate.get_constant('Proxy', 'AnnouncementDepositBase')
```
---------
#### AnnouncementDepositFactor
 The amount of currency needed per announcement made.

 This is held for adding an `AccountId`, `Hash` and `BlockNumber` (typically 68 bytes)
 into a pre-existing storage value.
##### Value
```python
66000000000000000
```
##### Python
```python
constant = substrate.get_constant('Proxy', 'AnnouncementDepositFactor')
```
---------
### Errors
---------
#### TooMany
There are too many proxies registered or too many announcements pending.

---------
#### NotFound
Proxy registration not found.

---------
#### NotProxy
Sender is not a proxy of the account to be proxied.

---------
#### Unproxyable
A call which is incompatible with the proxy type&\#x27;s filter was attempted.

---------
#### Duplicate
Account is already a proxy.

---------
#### NoPermission
Call may not be made by proxy because it may escalate its privileges.

---------
#### Unannounced
Announcement, if made at all, was made too recently.

---------
#### NoSelfProxy
Cannot add self as proxy.

---------