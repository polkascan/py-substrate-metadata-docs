# nodle-para
---------
| Properties |  |
| -------- | -------- |
| Spec name     | nodle-para     |
| Implementation name     | nodle-para     |
| Spec version     | 12     |
| SS58 Format     | 37     |
| Token symbol      | NODL     |
| Token decimals      | 11     |

## System
---------
### Calls
---------
#### fill_block
A dispatch that will fill the block weight up to the given ratio.
##### Attributes
| Name | Type |
| -------- | -------- | 
| ratio | `Perbill` | 

##### Python
```python
call = substrate.compose_call(
    'System', 'fill_block', {'ratio': 'u32'}
)
```

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
| dispatch_info | `DispatchInfo` | ```{'weight': 'u64', 'class': ('Normal', 'Operational', 'Mandatory'), 'pays_fee': ('Yes', 'No')}```

---------
#### ExtrinsicFailed
An extrinsic failed.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispatch_error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}```
| dispatch_info | `DispatchInfo` | ```{'weight': 'u64', 'class': ('Normal', 'Operational', 'Mandatory'), 'pays_fee': ('Yes', 'No')}```

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
call = substrate.query(
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
call = substrate.query(
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
call = substrate.query(
    'System', 'BlockWeight', []
)
```

##### Return value
```python
{'mandatory': 'u64', 'normal': 'u64', 'operational': 'u64'}
```
---------
#### AllExtrinsicsLen
 Total length (in bytes) for all extrinsics put together, for the current block.

##### Python
```python
call = substrate.query(
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
call = substrate.query(
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
call = substrate.query(
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
call = substrate.query(
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
call = substrate.query(
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
call = substrate.query(
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
call = substrate.query(
    'System', 'Events', []
)
```

##### Return value
```python
[
    {
        'event': {
            'System': {
                'CodeUpdated': None,
                'ExtrinsicFailed': {
                    'dispatch_error': 'scale_info::22',
                    'dispatch_info': 'scale_info::19',
                },
                'ExtrinsicSuccess': {'dispatch_info': 'scale_info::19'},
                'KilledAccount': {'account': 'AccountId'},
                'NewAccount': {'account': 'AccountId'},
                'Remarked': {'hash': '[u8; 32]', 'sender': 'AccountId'},
            },
            None: None,
            'AllocationsOracles': (
                'MemberAdded',
                'MemberRemoved',
                'MembersSwapped',
                'MembersReset',
                'KeyChanged',
                'Dummy',
            ),
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
                    'destination_status': 'scale_info::28',
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
            'CompanyReserve': {
                'Deposit': 'u128',
                'ReserveOp': {'Err': 'scale_info::22', 'Ok': ()},
                'SpentFunds': ('AccountId', 'u128'),
                'TipReceived': ('AccountId', 'u128'),
            },
            'CumulusXcm': {
                'ExecutedDownward': ('[u8; 8]', 'scale_info::50'),
                'InvalidFormat': '[u8; 8]',
                'UnsupportedVersion': '[u8; 8]',
            },
            'InternationalReserve': {
                'Deposit': 'u128',
                'ReserveOp': {'Err': 'scale_info::22', 'Ok': ()},
                'SpentFunds': ('AccountId', 'u128'),
                'TipReceived': ('AccountId', 'u128'),
            },
            'Mandate': {'RootOp': {'Err': 'scale_info::22', 'Ok': ()}},
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::54',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::54',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::33',
                    'timepoint': 'scale_info::54',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'ParachainSystem': {
                'DownwardMessagesProcessed': {
                    'dmq_head': '[u8; 32]',
                    'weight_used': 'u64',
                },
                'DownwardMessagesReceived': {'count': 'u32'},
                'UpgradeAuthorized': {'code_hash': '[u8; 32]'},
                'ValidationFunctionApplied': {'relay_chain_block_num': 'u32'},
                'ValidationFunctionDiscarded': None,
                'ValidationFunctionStored': None,
            },
            'Preimage': {
                'Cleared': {'hash': '[u8; 32]'},
                'Noted': {'hash': '[u8; 32]'},
                'Requested': {'hash': '[u8; 32]'},
            },
            'Scheduler': {
                'CallLookupFailed': {
                    'error': 'scale_info::35',
                    'id': (None, 'Bytes'),
                    'task': ('u32', 'u32'),
                },
                'Canceled': {'index': 'u32', 'when': 'u32'},
                'Dispatched': {
                    'id': (None, 'Bytes'),
                    'result': 'scale_info::33',
                    'task': ('u32', 'u32'),
                },
                'Scheduled': {'index': 'u32', 'when': 'u32'},
            },
            'Session': {'NewSession': {'session_index': 'u32'}},
            'TechnicalCommittee': {
                'Approved': {'proposal_hash': '[u8; 32]'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': '[u8; 32]'},
                'Executed': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::33',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::33',
                },
                'Proposed': {
                    'account': 'AccountId',
                    'proposal_hash': '[u8; 32]',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'Voted': {
                    'account': 'AccountId',
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'voted': 'bool',
                    'yes': 'u32',
                },
            },
            'TechnicalMembership': (
                'MemberAdded',
                'MemberRemoved',
                'MembersSwapped',
                'MembersReset',
                'KeyChanged',
                'Dummy',
            ),
            'TransactionPayment': {
                'TransactionFeePaid': {
                    'actual_fee': 'u128',
                    'tip': 'u128',
                    'who': 'AccountId',
                },
            },
            'Uniques': {
                'ApprovalCancelled': {
                    'collection': 'u32',
                    'delegate': 'AccountId',
                    'item': 'u32',
                    'owner': 'AccountId',
                },
                'ApprovedTransfer': {
                    'collection': 'u32',
                    'delegate': 'AccountId',
                    'item': 'u32',
                    'owner': 'AccountId',
                },
                'AttributeCleared': {
                    'collection': 'u32',
                    'key': 'Bytes',
                    'maybe_item': (None, 'u32'),
                },
                'AttributeSet': {
                    'collection': 'u32',
                    'key': 'Bytes',
                    'maybe_item': (None, 'u32'),
                    'value': 'Bytes',
                },
                'Burned': {
                    'collection': 'u32',
                    'item': 'u32',
                    'owner': 'AccountId',
                },
                'CollectionFrozen': {'collection': 'u32'},
                'CollectionMaxSupplySet': {
                    'collection': 'u32',
                    'max_supply': 'u32',
                },
                'CollectionMetadataCleared': {'collection': 'u32'},
                'CollectionMetadataSet': {
                    'collection': 'u32',
                    'data': 'Bytes',
                    'is_frozen': 'bool',
                },
                'CollectionThawed': {'collection': 'u32'},
                'Created': {
                    'collection': 'u32',
                    'creator': 'AccountId',
                    'owner': 'AccountId',
                },
                'Destroyed': {'collection': 'u32'},
                'ForceCreated': {'collection': 'u32', 'owner': 'AccountId'},
                'Frozen': {'collection': 'u32', 'item': 'u32'},
                'Issued': {
                    'collection': 'u32',
                    'item': 'u32',
                    'owner': 'AccountId',
                },
                'ItemStatusChanged': {'collection': 'u32'},
                'MetadataCleared': {'collection': 'u32', 'item': 'u32'},
                'MetadataSet': {
                    'collection': 'u32',
                    'data': 'Bytes',
                    'is_frozen': 'bool',
                    'item': 'u32',
                },
                'OwnerChanged': {
                    'collection': 'u32',
                    'new_owner': 'AccountId',
                },
                'OwnershipAcceptanceChanged': {
                    'maybe_collection': (None, 'u32'),
                    'who': 'AccountId',
                },
                'Redeposited': {
                    'collection': 'u32',
                    'successful_items': ['u32'],
                },
                'TeamChanged': {
                    'admin': 'AccountId',
                    'collection': 'u32',
                    'freezer': 'AccountId',
                    'issuer': 'AccountId',
                },
                'Thawed': {'collection': 'u32', 'item': 'u32'},
                'Transferred': {
                    'collection': 'u32',
                    'from': 'AccountId',
                    'item': 'u32',
                    'to': 'AccountId',
                },
            },
            'UsaReserve': {
                'Deposit': 'u128',
                'ReserveOp': {'Err': 'scale_info::22', 'Ok': ()},
                'SpentFunds': ('AccountId', 'u128'),
                'TipReceived': ('AccountId', 'u128'),
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::22',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::33'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::22'},
            },
            'ValidatorsSet': (
                'MemberAdded',
                'MemberRemoved',
                'MembersSwapped',
                'MembersReset',
                'KeyChanged',
                'Dummy',
            ),
            'Vesting': {
                'Claimed': ('AccountId', 'u128'),
                'VestingScheduleAdded': (
                    'AccountId',
                    'AccountId',
                    'scale_info::40',
                ),
                'VestingSchedulesCanceled': 'AccountId',
            },
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
call = substrate.query(
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
call = substrate.query(
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
call = substrate.query(
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
call = substrate.query(
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
call = substrate.query(
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
call = substrate.query(
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
    'base_block': 5346284000,
    'max_block': 500000000000,
    'per_class': {
        'mandatory': {
            'base_extrinsic': 86298000,
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': 86298000,
            'max_extrinsic': 324913702000,
            'max_total': 375000000000,
            'reserved': 0,
        },
        'operational': {
            'base_extrinsic': 86298000,
            'max_extrinsic': 449913702000,
            'max_total': 500000000000,
            'reserved': 125000000000,
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
        ('0xdd718d5cc53262d4', 1),
        ('0xab3c0572291feb8b', 1),
        ('0xdf6acb689907609b', 4),
        ('0x37e397fc7c91f5e4', 1),
        ('0x40fe3ad401f8959a', 6),
        ('0xd2bc9897eed08f15', 3),
        ('0xf78b278be53f454c', 2),
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 1),
        ('0xea93e3f16f3d6962', 2),
    ],
    'authoring_version': 1,
    'impl_name': 'nodle-para',
    'impl_version': 0,
    'spec_name': 'nodle-para',
    'spec_version': 12,
    'state_version': 0,
    'transaction_version': 4,
}
```
##### Python
```python
constant = substrate.get_constant('System', 'Version')
```
---------
#### SS58Prefix
 The designated SS85 prefix of this chain.

 This replaces the &quot;ss58Format&quot; property declared in the chain spec. Reason is
 that the runtime should know about the prefix in order to make use of it as
 an identifier of the chain.
##### Value
```python
37
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
call = substrate.query(
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
call = substrate.query(
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
6000
```
##### Python
```python
constant = substrate.get_constant('Timestamp', 'MinimumPeriod')
```
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
| dest | `<T::Lookup as StaticLookup>::Source` | 
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
| who | `<T::Lookup as StaticLookup>::Source` | 
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
| source | `<T::Lookup as StaticLookup>::Source` | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
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
| dest | `<T::Lookup as StaticLookup>::Source` | 
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
| dest | `<T::Lookup as StaticLookup>::Source` | 
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
| who | `<T::Lookup as StaticLookup>::Source` | 
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
call = substrate.query(
    'Balances', 'TotalIssuance', []
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
call = substrate.query(
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
call = substrate.query(
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
call = substrate.query(
    'Balances', 'Reserves', ['AccountId']
)
```

##### Return value
```python
[{'amount': 'u128', 'id': '[u8; 8]'}]
```
---------
#### StorageVersion
 Storage version of the pallet.

 This is set to v2.0.0 for new networks.

##### Python
```python
call = substrate.query(
    'Balances', 'StorageVersion', []
)
```

##### Return value
```python
('V1_0_0', 'V2_0_0')
```
---------
### Constants
---------
#### ExistentialDeposit
 The minimum amount required to keep an account open.
##### Value
```python
10000
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
Balance too low to send value

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
call = substrate.query(
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
call = substrate.query(
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
call = substrate.query(
    'RandomnessCollectiveFlip', 'RandomMaterial', []
)
```

##### Return value
```python
['[u8; 32]']
```
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
| call | `Box<CallOrHashOf<T>>` | 

##### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule', {
    'call': {
        'Hash': '[u8; 32]',
        'Value': 'Call',
    },
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
| id | `Vec<u8>` | 
| when | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<CallOrHashOf<T>>` | 

##### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule_named', {
    'call': {
        'Hash': '[u8; 32]',
        'Value': 'Call',
    },
    'id': 'Bytes',
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
| id | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'Scheduler', 'cancel_named', {'id': 'Bytes'}
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
| call | `Box<CallOrHashOf<T>>` | 

##### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule_after', {
    'after': 'u32',
    'call': {
        'Hash': '[u8; 32]',
        'Value': 'Call',
    },
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
| id | `Vec<u8>` | 
| after | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<CallOrHashOf<T>>` | 

##### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule_named_after', {
    'after': 'u32',
    'call': {
        'Hash': '[u8; 32]',
        'Value': 'Call',
    },
    'id': 'Bytes',
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
| id | `Option<Vec<u8>>` | ```(None, 'Bytes')```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
#### CallLookupFailed
The call for the provided hash was not found so the task has been aborted.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<Vec<u8>>` | ```(None, 'Bytes')```
| error | `LookupError` | ```('Unknown', 'BadFormat')```

---------
### Storage functions
---------
#### Agenda
 Items to be executed, indexed by the block number that they should be executed on.

##### Python
```python
call = substrate.query(
    'Scheduler', 'Agenda', ['u32']
)
```

##### Return value
```python
[
    (
        None,
        {
            'call': {'Hash': '[u8; 32]', 'Value': 'Call'},
            'maybe_id': (None, 'Bytes'),
            'maybe_periodic': (None, ('u32', 'u32')),
            'origin': {
                'CumulusXcm': {'Relay': None, 'SiblingParachain': 'u32'},
                'TechnicalCommittee': {
                    'Member': 'AccountId',
                    'Members': ('u32', 'u32'),
                    '_Phantom': None,
                },
                'Void': (),
                'system': {'None': None, 'Root': None, 'Signed': 'AccountId'},
                None: None,
            },
            'priority': 'u8',
        },
    ),
]
```
---------
#### Lookup
 Lookup from identity to the block number and index of the task.

##### Python
```python
call = substrate.query(
    'Scheduler', 'Lookup', ['Bytes']
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
 The maximum weight that may be scheduled per block for any dispatchables of less
 priority than `schedule::HARD_DEADLINE`.
##### Value
```python
400000000000
```
##### Python
```python
constant = substrate.get_constant('Scheduler', 'MaximumWeight')
```
---------
#### MaxScheduledPerBlock
 The maximum number of scheduled calls in the queue for a single block.
 Not strictly enforced, but used for weight estimation.
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

## CompanyReserve
---------
### Calls
---------
#### spend
Spend `amount` funds from the reserve account to `to`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| amount | `BalanceOf<T, I>` | 

##### Python
```python
call = substrate.compose_call(
    'CompanyReserve', 'spend', {'amount': 'u128', 'to': 'AccountId'}
)
```

---------
#### tip
Deposit `amount` tokens in the treasure account
##### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T, I>` | 

##### Python
```python
call = substrate.compose_call(
    'CompanyReserve', 'tip', {'amount': 'u128'}
)
```

---------
#### apply_as
Dispatch a call as coming from the reserve account
##### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config<I>>::Call>` | 

##### Python
```python
call = substrate.compose_call(
    'CompanyReserve', 'apply_as', {'call': 'Call'}
)
```

---------
### Events
---------
#### Deposit
Some amount was deposited (e.g. for transaction fees).
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T, I>` | ```u128```

---------
#### SpentFunds
Some funds were spent from the reserve.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T, I>` | ```u128```

---------
#### TipReceived
Someone tipped the company reserve
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T, I>` | ```u128```

---------
#### ReserveOp
We executed a call coming from the company reserve account
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------

## InternationalReserve
---------
### Calls
---------
#### spend
Spend `amount` funds from the reserve account to `to`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| amount | `BalanceOf<T, I>` | 

##### Python
```python
call = substrate.compose_call(
    'InternationalReserve', 'spend', {'amount': 'u128', 'to': 'AccountId'}
)
```

---------
#### tip
Deposit `amount` tokens in the treasure account
##### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T, I>` | 

##### Python
```python
call = substrate.compose_call(
    'InternationalReserve', 'tip', {'amount': 'u128'}
)
```

---------
#### apply_as
Dispatch a call as coming from the reserve account
##### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config<I>>::Call>` | 

##### Python
```python
call = substrate.compose_call(
    'InternationalReserve', 'apply_as', {'call': 'Call'}
)
```

---------
### Events
---------
#### Deposit
Some amount was deposited (e.g. for transaction fees).
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T, I>` | ```u128```

---------
#### SpentFunds
Some funds were spent from the reserve.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T, I>` | ```u128```

---------
#### TipReceived
Someone tipped the company reserve
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T, I>` | ```u128```

---------
#### ReserveOp
We executed a call coming from the company reserve account
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------

## UsaReserve
---------
### Calls
---------
#### spend
Spend `amount` funds from the reserve account to `to`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| amount | `BalanceOf<T, I>` | 

##### Python
```python
call = substrate.compose_call(
    'UsaReserve', 'spend', {'amount': 'u128', 'to': 'AccountId'}
)
```

---------
#### tip
Deposit `amount` tokens in the treasure account
##### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T, I>` | 

##### Python
```python
call = substrate.compose_call(
    'UsaReserve', 'tip', {'amount': 'u128'}
)
```

---------
#### apply_as
Dispatch a call as coming from the reserve account
##### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config<I>>::Call>` | 

##### Python
```python
call = substrate.compose_call(
    'UsaReserve', 'apply_as', {'call': 'Call'}
)
```

---------
### Events
---------
#### Deposit
Some amount was deposited (e.g. for transaction fees).
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T, I>` | ```u128```

---------
#### SpentFunds
Some funds were spent from the reserve.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T, I>` | ```u128```

---------
#### TipReceived
Someone tipped the company reserve
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T, I>` | ```u128```

---------
#### ReserveOp
We executed a call coming from the company reserve account
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------

## Vesting
---------
### Calls
---------
#### claim
Claim funds that have been vested so far
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'Vesting', 'claim', {}
)
```

---------
#### add_vesting_schedule
Wire funds to be vested by the receiver
##### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| schedule | `VestingScheduleOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Vesting', 'add_vesting_schedule', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'schedule': {
        'per_period': 'u128',
        'period': 'u32',
        'period_count': 'u32',
        'start': 'u32',
    },
}
)
```

---------
#### cancel_all_vesting_schedules
Cancel all vested schedules for the given user. If there are coins to be
claimed they will be auto claimed for the given user. If `limit_to_free_balance`
is set to true we will not error if the free balance of `who` has less coins
than what was granted and is being revoked (useful if the state was corrupted).
##### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| funds_collector | `<T::Lookup as StaticLookup>::Source` | 

##### Python
```python
call = substrate.compose_call(
    'Vesting', 'cancel_all_vesting_schedules', {
    'funds_collector': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
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
#### VestingScheduleAdded
Added new vesting schedule \[from, to, vesting_schedule\]
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `VestingScheduleOf<T>` | ```{'start': 'u32', 'period': 'u32', 'period_count': 'u32', 'per_period': 'u128'}```

---------
#### Claimed
Claimed vesting \[who, locked_amount\]
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
#### VestingSchedulesCanceled
Canceled all vesting schedules \[who\]
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### Storage functions
---------
#### VestingSchedules

##### Python
```python
call = substrate.query(
    'Vesting', 'VestingSchedules', ['AccountId']
)
```

##### Return value
```python
[
    {
        'per_period': 'u128',
        'period': 'u32',
        'period_count': 'u32',
        'start': 'u32',
    },
]
```
---------
#### CounterForVestingSchedules
Counter for the related counted storage map

##### Python
```python
call = substrate.query(
    'Vesting', 'CounterForVestingSchedules', []
)
```

##### Return value
```python
'u32'
```
---------
#### StorageVersion

##### Python
```python
call = substrate.query(
    'Vesting', 'StorageVersion', []
)
```

##### Return value
```python
('V0', 'V1')
```
---------
### Constants
---------
#### MaxSchedule
 The maximum number of vesting schedule.
##### Value
```python
100
```
##### Python
```python
constant = substrate.get_constant('Vesting', 'MaxSchedule')
```
---------
### Errors
---------
#### ZeroVestingPeriod

---------
#### ZeroVestingPeriodCount

---------
#### NumOverflow

---------
#### InsufficientBalanceToLock

---------
#### EmptySchedules

---------
#### VestingToSelf

---------
#### MaxScheduleOverflow

---------

## Mandate
---------
### Calls
---------
#### apply
Let the configured origin dispatch a call as root
##### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::Call>` | 

##### Python
```python
call = substrate.compose_call(
    'Mandate', 'apply', {'call': 'Call'}
)
```

---------
### Events
---------
#### RootOp
A root operation was executed, show result
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------

## TechnicalCommittee
---------
### Calls
---------
#### set_members
Set the collective&\#x27;s membership.

- `new_members`: The new member list. Be nice to the chain and provide it sorted.
- `prime`: The prime member whose vote sets the default.
- `old_count`: The upper bound for the previous number of members in storage. Used for
  weight estimation.

Requires root origin.

NOTE: Does not enforce the expected `MaxMembers` limit on the amount of members, but
      the weight estimations rely on it to estimate dispatchable weight.

\# WARNING:

The `pallet-collective` can also be managed by logic outside of the pallet through the
implementation of the trait [`ChangeMembers`].
Any call to `set_members` must be careful that the member set doesn&\#x27;t get out of sync
with other logic managing the member set.

\# &lt;weight&gt;
\#\# Weight
- `O(MP + N)` where:
  - `M` old-members-count (code- and governance-bounded)
  - `N` new-members-count (code- and governance-bounded)
  - `P` proposals-count (code-bounded)
- DB:
  - 1 storage mutation (codec `O(M)` read, `O(N)` write) for reading and writing the
    members
  - 1 storage read (codec `O(P)`) for reading the proposals
  - `P` storage mutations (codec `O(M)`) for updating the votes for each proposal
  - 1 storage write (codec `O(1)`) for deleting the old `prime` and setting the new one
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| new_members | `Vec<T::AccountId>` | 
| prime | `Option<T::AccountId>` | 
| old_count | `MemberCount` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalCommittee', 'set_members', {
    'new_members': ['AccountId'],
    'old_count': 'u32',
    'prime': (None, 'AccountId'),
}
)
```

---------
#### execute
Dispatch a proposal from a member using the `Member` origin.

Origin must be a member of the collective.

\# &lt;weight&gt;
\#\# Weight
- `O(M + P)` where `M` members-count (code-bounded) and `P` complexity of dispatching
  `proposal`
- DB: 1 read (codec `O(M)`) + DB access of `proposal`
- 1 event
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `Box<<T as Config<I>>::Proposal>` | 
| length_bound | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalCommittee', 'execute', {
    'length_bound': 'u32',
    'proposal': 'Call',
}
)
```

---------
#### propose
Add a new proposal to either be voted on or executed directly.

Requires the sender to be member.

`threshold` determines whether `proposal` is executed directly (`threshold &lt; 2`)
or put up for voting.

\# &lt;weight&gt;
\#\# Weight
- `O(B + M + P1)` or `O(B + M + P2)` where:
  - `B` is `proposal` size in bytes (length-fee-bounded)
  - `M` is members-count (code- and governance-bounded)
  - branching is influenced by `threshold` where:
    - `P1` is proposal execution complexity (`threshold &lt; 2`)
    - `P2` is proposals-count (code-bounded) (`threshold &gt;= 2`)
- DB:
  - 1 storage read `is_member` (codec `O(M)`)
  - 1 storage read `ProposalOf::contains_key` (codec `O(1)`)
  - DB accesses influenced by `threshold`:
    - EITHER storage accesses done by `proposal` (`threshold &lt; 2`)
    - OR proposal insertion (`threshold &lt;= 2`)
      - 1 storage mutation `Proposals` (codec `O(P2)`)
      - 1 storage mutation `ProposalCount` (codec `O(1)`)
      - 1 storage write `ProposalOf` (codec `O(B)`)
      - 1 storage write `Voting` (codec `O(M)`)
  - 1 event
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `MemberCount` | 
| proposal | `Box<<T as Config<I>>::Proposal>` | 
| length_bound | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalCommittee', 'propose', {
    'length_bound': 'u32',
    'proposal': 'Call',
    'threshold': 'u32',
}
)
```

---------
#### vote
Add an aye or nay vote for the sender to the given proposal.

Requires the sender to be a member.

Transaction fees will be waived if the member is voting on any particular proposal
for the first time and the call is successful. Subsequent vote changes will charge a
fee.
\# &lt;weight&gt;
\#\# Weight
- `O(M)` where `M` is members-count (code- and governance-bounded)
- DB:
  - 1 storage read `Members` (codec `O(M)`)
  - 1 storage mutation `Voting` (codec `O(M)`)
- 1 event
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `T::Hash` | 
| index | `ProposalIndex` | 
| approve | `bool` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalCommittee', 'vote', {
    'approve': 'bool',
    'index': 'u32',
    'proposal': '[u8; 32]',
}
)
```

---------
#### close
Close a vote that is either approved, disapproved or whose voting period has ended.

May be called by any signed account in order to finish voting and close the proposal.

If called before the end of the voting period it will only close the vote if it is
has enough votes to be approved or disapproved.

If called after the end of the voting period abstentions are counted as rejections
unless there is a prime member set and the prime member cast an approval.

If the close operation completes successfully with disapproval, the transaction fee will
be waived. Otherwise execution of the approved operation will be charged to the caller.

+ `proposal_weight_bound`: The maximum amount of weight consumed by executing the closed
proposal.
+ `length_bound`: The upper bound for the length of the proposal in storage. Checked via
`storage::read` so it is `size_of::&lt;u32&gt;() == 4` larger than the pure length.

\# &lt;weight&gt;
\#\# Weight
- `O(B + M + P1 + P2)` where:
  - `B` is `proposal` size in bytes (length-fee-bounded)
  - `M` is members-count (code- and governance-bounded)
  - `P1` is the complexity of `proposal` preimage.
  - `P2` is proposal-count (code-bounded)
- DB:
 - 2 storage reads (`Members`: codec `O(M)`, `Prime`: codec `O(1)`)
 - 3 mutations (`Voting`: codec `O(M)`, `ProposalOf`: codec `O(B)`, `Proposals`: codec
   `O(P2)`)
 - any mutations done while executing `proposal` (`P1`)
- up to 3 events
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 
| index | `ProposalIndex` | 
| proposal_weight_bound | `Weight` | 
| length_bound | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalCommittee', 'close', {
    'index': 'u32',
    'length_bound': 'u32',
    'proposal_hash': '[u8; 32]',
    'proposal_weight_bound': 'u64',
}
)
```

---------
#### disapprove_proposal
Disapprove a proposal, close, and remove it from the system, regardless of its current
state.

Must be called by the Root origin.

Parameters:
* `proposal_hash`: The hash of the proposal that should be disapproved.

\# &lt;weight&gt;
Complexity: O(P) where P is the number of max proposals
DB Weight:
* Reads: Proposals
* Writes: Voting, Proposals, ProposalOf
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalCommittee', 'disapprove_proposal', {'proposal_hash': '[u8; 32]'}
)
```

---------
### Events
---------
#### Proposed
A motion (given hash) has been proposed (by given account) with a threshold (given
`MemberCount`).
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| proposal_index | `ProposalIndex` | ```u32```
| proposal_hash | `T::Hash` | ```[u8; 32]```
| threshold | `MemberCount` | ```u32```

---------
#### Voted
A motion (given hash) has been voted on by given account, leaving
a tally (yes votes and no votes given respectively as `MemberCount`).
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| proposal_hash | `T::Hash` | ```[u8; 32]```
| voted | `bool` | ```bool```
| yes | `MemberCount` | ```u32```
| no | `MemberCount` | ```u32```

---------
#### Approved
A motion was approved by the required threshold.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```

---------
#### Disapproved
A motion was not approved by the required threshold.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```

---------
#### Executed
A motion was executed; result will be `Ok` if it returned without error.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
#### MemberExecuted
A single member did some action; result will be `Ok` if it returned without error.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
#### Closed
A proposal was closed because its threshold was reached or after its duration was up.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| yes | `MemberCount` | ```u32```
| no | `MemberCount` | ```u32```

---------
### Storage functions
---------
#### Proposals
 The hashes of the active proposals.

##### Python
```python
call = substrate.query(
    'TechnicalCommittee', 'Proposals', []
)
```

##### Return value
```python
['[u8; 32]']
```
---------
#### ProposalOf
 Actual proposal for a given hash, if it&#x27;s current.

##### Python
```python
call = substrate.query(
    'TechnicalCommittee', 'ProposalOf', ['[u8; 32]']
)
```

##### Return value
```python
'Call'
```
---------
#### Voting
 Votes on a given proposal, if it is ongoing.

##### Python
```python
call = substrate.query(
    'TechnicalCommittee', 'Voting', ['[u8; 32]']
)
```

##### Return value
```python
{'ayes': ['AccountId'], 'end': 'u32', 'index': 'u32', 'nays': ['AccountId'], 'threshold': 'u32'}
```
---------
#### ProposalCount
 Proposals so far.

##### Python
```python
call = substrate.query(
    'TechnicalCommittee', 'ProposalCount', []
)
```

##### Return value
```python
'u32'
```
---------
#### Members
 The current members of the collective. This is stored sorted (just by value).

##### Python
```python
call = substrate.query(
    'TechnicalCommittee', 'Members', []
)
```

##### Return value
```python
['AccountId']
```
---------
#### Prime
 The prime member that helps determine the default vote behavior in case of absentations.

##### Python
```python
call = substrate.query(
    'TechnicalCommittee', 'Prime', []
)
```

##### Return value
```python
'AccountId'
```
---------
### Errors
---------
#### NotMember
Account is not a member

---------
#### DuplicateProposal
Duplicate proposals not allowed

---------
#### ProposalMissing
Proposal must exist

---------
#### WrongIndex
Mismatched index

---------
#### DuplicateVote
Duplicate vote ignored

---------
#### AlreadyInitialized
Members are already initialized!

---------
#### TooEarly
The close call was made too early, before the end of the voting.

---------
#### TooManyProposals
There can only be a maximum of `MaxProposals` active proposals.

---------
#### WrongProposalWeight
The given weight bound for the proposal was too low.

---------
#### WrongProposalLength
The given length bound for the proposal was too low.

---------

## TechnicalMembership
---------
### Calls
---------
#### add_member
Add a member `who` to the set.

May only be called from `T::AddOrigin`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalMembership', 'add_member', {'who': 'AccountId'}
)
```

---------
#### remove_member
Remove a member `who` from the set.

May only be called from `T::RemoveOrigin`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalMembership', 'remove_member', {'who': 'AccountId'}
)
```

---------
#### swap_member
Swap out one member `remove` for another `add`.

May only be called from `T::SwapOrigin`.

Prime membership is *not* passed from `remove` to `add`, if extant.
##### Attributes
| Name | Type |
| -------- | -------- | 
| remove | `T::AccountId` | 
| add | `T::AccountId` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalMembership', 'swap_member', {
    'add': 'AccountId',
    'remove': 'AccountId',
}
)
```

---------
#### reset_members
Change the membership to a new set, disregarding the existing membership. Be nice and
pass `members` pre-sorted.

May only be called from `T::ResetOrigin`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| members | `Vec<T::AccountId>` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalMembership', 'reset_members', {'members': ['AccountId']}
)
```

---------
#### change_key
Swap out the sending member for some other key `new`.

May only be called from `Signed` origin of a current member.

Prime membership is passed from the origin account to `new`, if extant.
##### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::AccountId` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalMembership', 'change_key', {'new': 'AccountId'}
)
```

---------
#### set_prime
Set the prime member. Must be a current member.

May only be called from `T::PrimeOrigin`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

##### Python
```python
call = substrate.compose_call(
    'TechnicalMembership', 'set_prime', {'who': 'AccountId'}
)
```

---------
#### clear_prime
Remove the prime member if it exists.

May only be called from `T::PrimeOrigin`.
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'TechnicalMembership', 'clear_prime', {}
)
```

---------
### Events
---------
#### MemberAdded
The given member was added; see the transaction for who.
##### Attributes
No attributes

---------
#### MemberRemoved
The given member was removed; see the transaction for who.
##### Attributes
No attributes

---------
#### MembersSwapped
Two members were swapped; see the transaction for who.
##### Attributes
No attributes

---------
#### MembersReset
The membership was reset; see the transaction for who the new set is.
##### Attributes
No attributes

---------
#### KeyChanged
One of the members&\#x27; keys changed.
##### Attributes
No attributes

---------
#### Dummy
Phantom member, never used.
##### Attributes
No attributes

---------
### Storage functions
---------
#### Members
 The current membership, stored as an ordered Vec.

##### Python
```python
call = substrate.query(
    'TechnicalMembership', 'Members', []
)
```

##### Return value
```python
['AccountId']
```
---------
#### Prime
 The current prime member, if one exists.

##### Python
```python
call = substrate.query(
    'TechnicalMembership', 'Prime', []
)
```

##### Return value
```python
'AccountId'
```
---------
### Errors
---------
#### AlreadyMember
Already a member.

---------
#### NotMember
Not a member.

---------
#### TooManyMembers
Too many members.

---------

## Authorship
---------
### Calls
---------
#### set_uncles
Provide a set of uncles.
##### Attributes
| Name | Type |
| -------- | -------- | 
| new_uncles | `Vec<T::Header>` | 

##### Python
```python
call = substrate.compose_call(
    'Authorship', 'set_uncles', {
    'new_uncles': [
        {
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
    ],
}
)
```

---------
### Storage functions
---------
#### Uncles
 Uncles

##### Python
```python
call = substrate.query(
    'Authorship', 'Uncles', []
)
```

##### Return value
```python
[{'InclusionHeight': 'u32', 'Uncle': ('[u8; 32]', (None, 'AccountId'))}]
```
---------
#### Author
 Author of current block.

##### Python
```python
call = substrate.query(
    'Authorship', 'Author', []
)
```

##### Return value
```python
'AccountId'
```
---------
#### DidSetUncles
 Whether uncles were already set in this block.

##### Python
```python
call = substrate.query(
    'Authorship', 'DidSetUncles', []
)
```

##### Return value
```python
'bool'
```
---------
### Constants
---------
#### UncleGenerations
 The number of blocks back we should accept uncles.
 This means that we will deal with uncle-parents that are
 `UncleGenerations + 1` before `now`.
##### Value
```python
0
```
##### Python
```python
constant = substrate.get_constant('Authorship', 'UncleGenerations')
```
---------
### Errors
---------
#### InvalidUncleParent
The uncle parent not in the chain.

---------
#### UnclesAlreadySet
Uncles already set in the block.

---------
#### TooManyUncles
Too many uncles.

---------
#### GenesisUncle
The uncle is genesis.

---------
#### TooHighUncle
The uncle is too high in chain.

---------
#### UncleAlreadyIncluded
The uncle is already included.

---------
#### OldUncle
The uncle isn&\#x27;t recent enough to be included.

---------

## ValidatorsSet
---------
### Calls
---------
#### add_member
Add a member `who` to the set.

May only be called from `T::AddOrigin`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

##### Python
```python
call = substrate.compose_call(
    'ValidatorsSet', 'add_member', {'who': 'AccountId'}
)
```

---------
#### remove_member
Remove a member `who` from the set.

May only be called from `T::RemoveOrigin`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

##### Python
```python
call = substrate.compose_call(
    'ValidatorsSet', 'remove_member', {'who': 'AccountId'}
)
```

---------
#### swap_member
Swap out one member `remove` for another `add`.

May only be called from `T::SwapOrigin`.

Prime membership is *not* passed from `remove` to `add`, if extant.
##### Attributes
| Name | Type |
| -------- | -------- | 
| remove | `T::AccountId` | 
| add | `T::AccountId` | 

##### Python
```python
call = substrate.compose_call(
    'ValidatorsSet', 'swap_member', {
    'add': 'AccountId',
    'remove': 'AccountId',
}
)
```

---------
#### reset_members
Change the membership to a new set, disregarding the existing membership. Be nice and
pass `members` pre-sorted.

May only be called from `T::ResetOrigin`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| members | `Vec<T::AccountId>` | 

##### Python
```python
call = substrate.compose_call(
    'ValidatorsSet', 'reset_members', {'members': ['AccountId']}
)
```

---------
#### change_key
Swap out the sending member for some other key `new`.

May only be called from `Signed` origin of a current member.

Prime membership is passed from the origin account to `new`, if extant.
##### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::AccountId` | 

##### Python
```python
call = substrate.compose_call(
    'ValidatorsSet', 'change_key', {'new': 'AccountId'}
)
```

---------
#### set_prime
Set the prime member. Must be a current member.

May only be called from `T::PrimeOrigin`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

##### Python
```python
call = substrate.compose_call(
    'ValidatorsSet', 'set_prime', {'who': 'AccountId'}
)
```

---------
#### clear_prime
Remove the prime member if it exists.

May only be called from `T::PrimeOrigin`.
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'ValidatorsSet', 'clear_prime', {}
)
```

---------
### Events
---------
#### MemberAdded
The given member was added; see the transaction for who.
##### Attributes
No attributes

---------
#### MemberRemoved
The given member was removed; see the transaction for who.
##### Attributes
No attributes

---------
#### MembersSwapped
Two members were swapped; see the transaction for who.
##### Attributes
No attributes

---------
#### MembersReset
The membership was reset; see the transaction for who the new set is.
##### Attributes
No attributes

---------
#### KeyChanged
One of the members&\#x27; keys changed.
##### Attributes
No attributes

---------
#### Dummy
Phantom member, never used.
##### Attributes
No attributes

---------
### Storage functions
---------
#### Members
 The current membership, stored as an ordered Vec.

##### Python
```python
call = substrate.query(
    'ValidatorsSet', 'Members', []
)
```

##### Return value
```python
['AccountId']
```
---------
#### Prime
 The current prime member, if one exists.

##### Python
```python
call = substrate.query(
    'ValidatorsSet', 'Prime', []
)
```

##### Return value
```python
'AccountId'
```
---------
### Errors
---------
#### AlreadyMember
Already a member.

---------
#### NotMember
Not a member.

---------
#### TooManyMembers
Too many members.

---------

## Poa
---------
### Storage functions
---------
#### StorageVersion

##### Python
```python
call = substrate.query(
    'Poa', 'StorageVersion', []
)
```

##### Return value
```python
('V0', 'V1')
```
---------

## Session
---------
### Calls
---------
#### set_keys
Sets the session key(s) of the function caller to `keys`.
Allows an account to set its session key prior to becoming a validator.
This doesn&\#x27;t take effect until the next session.

The dispatch origin of this function must be signed.

\# &lt;weight&gt;
- Complexity: `O(1)`. Actual cost depends on the number of length of
  `T::Keys::key_ids()` which is fixed.
- DbReads: `origin account`, `T::ValidatorIdOf`, `NextKeys`
- DbWrites: `origin account`, `NextKeys`
- DbReads per key id: `KeyOwner`
- DbWrites per key id: `KeyOwner`
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| keys | `T::Keys` | 
| proof | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'Session', 'set_keys', {'keys': {'aura': '[u8; 32]'}, 'proof': 'Bytes'}
)
```

---------
#### purge_keys
Removes any session key(s) of the function caller.

This doesn&\#x27;t take effect until the next session.

The dispatch origin of this function must be Signed and the account must be either be
convertible to a validator ID using the chain&\#x27;s typical addressing system (this usually
means being a controller account) or directly convertible into a validator ID (which
usually means being a stash account).

\# &lt;weight&gt;
- Complexity: `O(1)` in number of key types. Actual cost depends on the number of length
  of `T::Keys::key_ids()` which is fixed.
- DbReads: `T::ValidatorIdOf`, `NextKeys`, `origin account`
- DbWrites: `NextKeys`, `origin account`
- DbWrites per key id: `KeyOwner`
\# &lt;/weight&gt;
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'Session', 'purge_keys', {}
)
```

---------
### Events
---------
#### NewSession
New session has happened. Note that the argument is the session index, not the
block number as the type might suggest.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| session_index | `SessionIndex` | ```u32```

---------
### Storage functions
---------
#### Validators
 The current set of validators.

##### Python
```python
call = substrate.query(
    'Session', 'Validators', []
)
```

##### Return value
```python
['AccountId']
```
---------
#### CurrentIndex
 Current index of the session.

##### Python
```python
call = substrate.query(
    'Session', 'CurrentIndex', []
)
```

##### Return value
```python
'u32'
```
---------
#### QueuedChanged
 True if the underlying economic identities or weighting behind the validators
 has changed in the queued validator set.

##### Python
```python
call = substrate.query(
    'Session', 'QueuedChanged', []
)
```

##### Return value
```python
'bool'
```
---------
#### QueuedKeys
 The queued keys for the next session. When the next session begins, these keys
 will be used to determine the validator&#x27;s session keys.

##### Python
```python
call = substrate.query(
    'Session', 'QueuedKeys', []
)
```

##### Return value
```python
[('AccountId', {'aura': '[u8; 32]'})]
```
---------
#### DisabledValidators
 Indices of disabled validators.

 The vec is always kept sorted so that we can find whether a given validator is
 disabled using binary search. It gets cleared when `on_session_ending` returns
 a new set of identities.

##### Python
```python
call = substrate.query(
    'Session', 'DisabledValidators', []
)
```

##### Return value
```python
['u32']
```
---------
#### NextKeys
 The next session keys for a validator.

##### Python
```python
call = substrate.query(
    'Session', 'NextKeys', ['AccountId']
)
```

##### Return value
```python
{'aura': '[u8; 32]'}
```
---------
#### KeyOwner
 The owner of a key. The key is the `KeyTypeId` + the encoded key.

##### Python
```python
call = substrate.query(
    'Session', 'KeyOwner', [('[u8; 4]', 'Bytes')]
)
```

##### Return value
```python
'AccountId'
```
---------
### Errors
---------
#### InvalidProof
Invalid ownership proof.

---------
#### NoAssociatedValidatorId
No associated validator ID for account.

---------
#### DuplicatedKey
Registered duplicate key.

---------
#### NoKeys
No keys are associated with this account.

---------
#### NoAccount
Key setting account is not live, so it&\#x27;s impossible to associate keys.

---------

## Aura
---------
### Storage functions
---------
#### Authorities
 The current authority set.

##### Python
```python
call = substrate.query(
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
call = substrate.query(
    'Aura', 'CurrentSlot', []
)
```

##### Return value
```python
'u64'
```
---------

## AuraExt
---------
### Storage functions
---------
#### Authorities
 Serves as cache for the authorities.

 The authorities in AuRa are overwritten in `on_initialize` when we switch to a new session,
 but we require the old authorities to verify the seal when validating a PoV. This will always
 be updated to the latest AuRa authorities in `on_finalize`.

##### Python
```python
call = substrate.query(
    'AuraExt', 'Authorities', []
)
```

##### Return value
```python
['[u8; 32]']
```
---------

## ParachainSystem
---------
### Calls
---------
#### set_validation_data
Set the current validation data.

This should be invoked exactly once per block. It will panic at the finalization
phase if the call was not invoked.

The dispatch origin for this call must be `Inherent`

As a side effect, this function upgrades the current validation function
if the appropriate time has come.
##### Attributes
| Name | Type |
| -------- | -------- | 
| data | `ParachainInherentData` | 

##### Python
```python
call = substrate.compose_call(
    'ParachainSystem', 'set_validation_data', {
    'data': {
        'downward_messages': [
            {
                'msg': 'Bytes',
                'sent_at': 'u32',
            },
        ],
        'horizontal_messages': 'scale_info::140',
        'relay_chain_state': {
            'trie_nodes': 'scale_info::137',
        },
        'validation_data': {
            'max_pov_size': 'u32',
            'parent_head': 'Bytes',
            'relay_parent_number': 'u32',
            'relay_parent_storage_root': '[u8; 32]',
        },
    },
}
)
```

---------
#### sudo_send_upward_message
##### Attributes
| Name | Type |
| -------- | -------- | 
| message | `UpwardMessage` | 

##### Python
```python
call = substrate.compose_call(
    'ParachainSystem', 'sudo_send_upward_message', {'message': 'Bytes'}
)
```

---------
#### authorize_upgrade
##### Attributes
| Name | Type |
| -------- | -------- | 
| code_hash | `T::Hash` | 

##### Python
```python
call = substrate.compose_call(
    'ParachainSystem', 'authorize_upgrade', {'code_hash': '[u8; 32]'}
)
```

---------
#### enact_authorized_upgrade
##### Attributes
| Name | Type |
| -------- | -------- | 
| code | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'ParachainSystem', 'enact_authorized_upgrade', {'code': 'Bytes'}
)
```

---------
### Events
---------
#### ValidationFunctionStored
The validation function has been scheduled to apply.
##### Attributes
No attributes

---------
#### ValidationFunctionApplied
The validation function was applied as of the contained relay chain block number.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| relay_chain_block_num | `RelayChainBlockNumber` | ```u32```

---------
#### ValidationFunctionDiscarded
The relay-chain aborted the upgrade process.
##### Attributes
No attributes

---------
#### UpgradeAuthorized
An upgrade has been authorized.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| code_hash | `T::Hash` | ```[u8; 32]```

---------
#### DownwardMessagesReceived
Some downward messages have been received and will be processed.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| count | `u32` | ```u32```

---------
#### DownwardMessagesProcessed
Downward messages were processed using the given weight.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| weight_used | `Weight` | ```u64```
| dmq_head | `relay_chain::Hash` | ```[u8; 32]```

---------
### Storage functions
---------
#### PendingValidationCode
 In case of a scheduled upgrade, this storage field contains the validation code to be applied.

 As soon as the relay chain gives us the go-ahead signal, we will overwrite the [`:code`][well_known_keys::CODE]
 which will result the next block process with the new validation code. This concludes the upgrade process.

 [well_known_keys::CODE]: sp_core::storage::well_known_keys::CODE

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'PendingValidationCode', []
)
```

##### Return value
```python
'Bytes'
```
---------
#### NewValidationCode
 Validation code that is set by the parachain and is to be communicated to collator and
 consequently the relay-chain.

 This will be cleared in `on_initialize` of each new block if no other pallet already set
 the value.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'NewValidationCode', []
)
```

##### Return value
```python
'Bytes'
```
---------
#### ValidationData
 The [`PersistedValidationData`] set for this block.
 This value is expected to be set only once per block and it&#x27;s never stored
 in the trie.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'ValidationData', []
)
```

##### Return value
```python
{
    'max_pov_size': 'u32',
    'parent_head': 'Bytes',
    'relay_parent_number': 'u32',
    'relay_parent_storage_root': '[u8; 32]',
}
```
---------
#### DidSetValidationCode
 Were the validation data set to notify the relay chain?

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'DidSetValidationCode', []
)
```

##### Return value
```python
'bool'
```
---------
#### LastRelayChainBlockNumber
 The relay chain block number associated with the last parachain block.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'LastRelayChainBlockNumber', []
)
```

##### Return value
```python
'u32'
```
---------
#### UpgradeRestrictionSignal
 An option which indicates if the relay-chain restricts signalling a validation code upgrade.
 In other words, if this is `Some` and [`NewValidationCode`] is `Some` then the produced
 candidate will be invalid.

 This storage item is a mirror of the corresponding value for the current parachain from the
 relay-chain. This value is ephemeral which means it doesn&#x27;t hit the storage. This value is
 set after the inherent.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'UpgradeRestrictionSignal', []
)
```

##### Return value
```python
(None, ('Present', ))
```
---------
#### RelayStateProof
 The state proof for the last relay parent block.

 This field is meant to be updated each block with the validation data inherent. Therefore,
 before processing of the inherent, e.g. in `on_initialize` this data may be stale.

 This data is also absent from the genesis.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'RelayStateProof', []
)
```

##### Return value
```python
{'trie_nodes': 'scale_info::137'}
```
---------
#### RelevantMessagingState
 The snapshot of some state related to messaging relevant to the current parachain as per
 the relay parent.

 This field is meant to be updated each block with the validation data inherent. Therefore,
 before processing of the inherent, e.g. in `on_initialize` this data may be stale.

 This data is also absent from the genesis.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'RelevantMessagingState', []
)
```

##### Return value
```python
{
    'dmq_mqc_head': '[u8; 32]',
    'egress_channels': [
        (
            'u32',
            {
                'max_capacity': 'u32',
                'max_message_size': 'u32',
                'max_total_size': 'u32',
                'mqc_head': (None, '[u8; 32]'),
                'msg_count': 'u32',
                'total_size': 'u32',
            },
        ),
    ],
    'ingress_channels': [
        (
            'u32',
            {
                'max_capacity': 'u32',
                'max_message_size': 'u32',
                'max_total_size': 'u32',
                'mqc_head': (None, '[u8; 32]'),
                'msg_count': 'u32',
                'total_size': 'u32',
            },
        ),
    ],
    'relay_dispatch_queue_size': ('u32', 'u32'),
}
```
---------
#### HostConfiguration
 The parachain host configuration that was obtained from the relay parent.

 This field is meant to be updated each block with the validation data inherent. Therefore,
 before processing of the inherent, e.g. in `on_initialize` this data may be stale.

 This data is also absent from the genesis.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'HostConfiguration', []
)
```

##### Return value
```python
{
    'hrmp_max_message_num_per_candidate': 'u32',
    'max_code_size': 'u32',
    'max_head_data_size': 'u32',
    'max_upward_message_num_per_candidate': 'u32',
    'max_upward_message_size': 'u32',
    'max_upward_queue_count': 'u32',
    'max_upward_queue_size': 'u32',
    'validation_upgrade_cooldown': 'u32',
    'validation_upgrade_delay': 'u32',
}
```
---------
#### LastDmqMqcHead
 The last downward message queue chain head we have observed.

 This value is loaded before and saved after processing inbound downward messages carried
 by the system inherent.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'LastDmqMqcHead', []
)
```

##### Return value
```python
'[u8; 32]'
```
---------
#### LastHrmpMqcHeads
 The message queue chain heads we have observed per each channel incoming channel.

 This value is loaded before and saved after processing inbound downward messages carried
 by the system inherent.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'LastHrmpMqcHeads', []
)
```

##### Return value
```python
'scale_info::201'
```
---------
#### ProcessedDownwardMessages
 Number of downward messages processed in a block.

 This will be cleared in `on_initialize` of each new block.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'ProcessedDownwardMessages', []
)
```

##### Return value
```python
'u32'
```
---------
#### HrmpWatermark
 HRMP watermark that was set in a block.

 This will be cleared in `on_initialize` of each new block.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'HrmpWatermark', []
)
```

##### Return value
```python
'u32'
```
---------
#### HrmpOutboundMessages
 HRMP messages that were sent in a block.

 This will be cleared in `on_initialize` of each new block.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'HrmpOutboundMessages', []
)
```

##### Return value
```python
[{'data': 'Bytes', 'recipient': 'u32'}]
```
---------
#### UpwardMessages
 Upward messages that were sent in a block.

 This will be cleared in `on_initialize` of each new block.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'UpwardMessages', []
)
```

##### Return value
```python
['Bytes']
```
---------
#### PendingUpwardMessages
 Upward messages that are still pending and not yet send to the relay chain.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'PendingUpwardMessages', []
)
```

##### Return value
```python
['Bytes']
```
---------
#### AnnouncedHrmpMessagesPerCandidate
 The number of HRMP messages we observed in `on_initialize` and thus used that number for
 announcing the weight of `on_initialize` and `on_finalize`.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'AnnouncedHrmpMessagesPerCandidate', []
)
```

##### Return value
```python
'u32'
```
---------
#### ReservedXcmpWeightOverride
 The weight we reserve at the beginning of the block for processing XCMP messages. This
 overrides the amount set in the Config trait.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'ReservedXcmpWeightOverride', []
)
```

##### Return value
```python
'u64'
```
---------
#### ReservedDmpWeightOverride
 The weight we reserve at the beginning of the block for processing DMP messages. This
 overrides the amount set in the Config trait.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'ReservedDmpWeightOverride', []
)
```

##### Return value
```python
'u64'
```
---------
#### AuthorizedUpgrade
 The next authorized upgrade, if there is one.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'AuthorizedUpgrade', []
)
```

##### Return value
```python
'[u8; 32]'
```
---------
#### CustomValidationHeadData
 A custom head data that should be returned as result of `validate_block`.

 See [`Pallet::set_custom_validation_head_data`] for more information.

##### Python
```python
call = substrate.query(
    'ParachainSystem', 'CustomValidationHeadData', []
)
```

##### Return value
```python
'Bytes'
```
---------
### Errors
---------
#### OverlappingUpgrades
Attempt to upgrade validation function while existing upgrade pending

---------
#### ProhibitedByPolkadot
Polkadot currently prohibits this parachain from upgrading its validation function

---------
#### TooBig
The supplied validation function has compiled into a blob larger than Polkadot is
willing to run

---------
#### ValidationDataNotAvailable
The inherent which supplies the validation data did not run this block

---------
#### HostConfigurationNotAvailable
The inherent which supplies the host configuration did not run this block

---------
#### NotScheduled
No validation function upgrade is currently scheduled.

---------
#### NothingAuthorized
No code upgrade has been authorized.

---------
#### Unauthorized
The given code upgrade has not been authorized.

---------

## ParachainInfo
---------
### Storage functions
---------
#### ParachainId

##### Python
```python
call = substrate.query(
    'ParachainInfo', 'ParachainId', []
)
```

##### Return value
```python
'u32'
```
---------

## CumulusXcm
---------
### Events
---------
#### InvalidFormat
Downward message is invalid XCM.
\[ id \]
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `[u8; 8]` | ```[u8; 8]```

---------
#### UnsupportedVersion
Downward message is unsupported version of XCM.
\[ id \]
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `[u8; 8]` | ```[u8; 8]```

---------
#### ExecutedDownward
Downward message executed with the given outcome.
\[ id, outcome \]
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `[u8; 8]` | ```[u8; 8]```
| None | `Outcome` | ```{'Complete': 'u64', 'Incomplete': ('u64', {'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'MultiLocationFull': None, 'MultiLocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'MaxWeightInvalid': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'UnhandledXcmVersion': None, 'WeightLimitReached': 'u64', 'Barrier': None, 'WeightNotComputable': None}), 'Error': {'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'MultiLocationFull': None, 'MultiLocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'MaxWeightInvalid': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'UnhandledXcmVersion': None, 'WeightLimitReached': 'u64', 'Barrier': None, 'WeightNotComputable': None}}```

---------

## Utility
---------
### Calls
---------
#### batch
Send a batch of dispatch calls.

May be called from any origin.

- `calls`: The calls to be dispatched from the same origin. The number of call must not
  exceed the constant: `batched_calls_limit` (available in constant metadata).

If origin is root then call are dispatch without checking origin filter. (This includes
bypassing `frame_system::Config::BaseCallFilter`).

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
| calls | `Vec<<T as Config>::Call>` | 

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
| call | `Box<<T as Config>::Call>` | 

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

May be called from any origin.

- `calls`: The calls to be dispatched from the same origin. The number of call must not
  exceed the constant: `batched_calls_limit` (available in constant metadata).

If origin is root then call are dispatch without checking origin filter. (This includes
bypassing `frame_system::Config::BaseCallFilter`).

\# &lt;weight&gt;
- Complexity: O(C) where C is the number of calls to be batched.
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::Call>` | 

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
| call | `Box<<T as Config>::Call>` | 

##### Python
```python
call = substrate.compose_call(
    'Utility', 'dispatch_as', {
    'as_origin': {
        'system': {
            'None': None,
            'Root': None,
            'Signed': 'AccountId',
        },
        None: None,
        'CumulusXcm': {
            'Relay': None,
            'SiblingParachain': 'u32',
        },
        'TechnicalCommittee': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'Void': (),
    },
    'call': 'Call',
}
)
```

---------
#### force_batch
Send a batch of dispatch calls.
Unlike `batch`, it allows errors and won&\#x27;t interrupt.

May be called from any origin.

- `calls`: The calls to be dispatched from the same origin. The number of call must not
  exceed the constant: `batched_calls_limit` (available in constant metadata).

If origin is root then call are dispatch without checking origin filter. (This includes
bypassing `frame_system::Config::BaseCallFilter`).

\# &lt;weight&gt;
- Complexity: O(C) where C is the number of calls to be batched.
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::Call>` | 

##### Python
```python
call = substrate.compose_call(
    'Utility', 'force_batch', {'calls': ['Call']}
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
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}```

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
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}```

---------
#### DispatchedAs
A call was dispatched.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

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
| call | `Box<<T as Config>::Call>` | 

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
    - Reads: Multisig Storage, [Caller Account], Calls (if `store_call`)
    - Writes: Multisig Storage, [Caller Account], Calls (if `store_call`)
- Plus Call Weight
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `u16` | 
| other_signatories | `Vec<T::AccountId>` | 
| maybe_timepoint | `Option<Timepoint<T::BlockNumber>>` | 
| call | `OpaqueCall<T>` | 
| store_call | `bool` | 
| max_weight | `Weight` | 

##### Python
```python
call = substrate.compose_call(
    'Multisig', 'as_multi', {
    'call': 'Call',
    'max_weight': 'u64',
    'maybe_timepoint': (
        None,
        {
            'height': 'u32',
            'index': 'u32',
        },
    ),
    'other_signatories': ['AccountId'],
    'store_call': 'bool',
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
    'max_weight': 'u64',
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
    - Read: Multisig Storage, [Caller Account], Refund Account, Calls
    - Write: Multisig Storage, [Caller Account], Refund Account, Calls
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
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

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
call = substrate.query(
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
#### Calls

##### Python
```python
call = substrate.query(
    'Multisig', 'Calls', ['[u8; 32]']
)
```

##### Return value
```python
('Call', 'AccountId', 'u128')
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
5430000000
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
1920000000
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

## Uniques
---------
### Calls
---------
#### create
Issue a new collection of non-fungible items from a public origin.

This new collection has no items initially and its owner is the origin.

The origin must be Signed and the sender must have sufficient funds free.

`ItemDeposit` funds of sender are reserved.

Parameters:
- `collection`: The identifier of the new collection. This must not be currently in use.
- `admin`: The admin of this collection. The admin is the initial address of each
member of the collection&\#x27;s admin team.

Emits `Created` event when successful.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| admin | `<T::Lookup as StaticLookup>::Source` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'create', {
    'admin': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'collection': 'u32',
}
)
```

---------
#### force_create
Issue a new collection of non-fungible items from a privileged origin.

This new collection has no items initially.

The origin must conform to `ForceOrigin`.

Unlike `create`, no funds are reserved.

- `collection`: The identifier of the new item. This must not be currently in use.
- `owner`: The owner of this collection of items. The owner has full superuser
  permissions
over this item, but may later change and configure the permissions using
`transfer_ownership` and `set_team`.

Emits `ForceCreated` event when successful.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| owner | `<T::Lookup as StaticLookup>::Source` | 
| free_holding | `bool` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'force_create', {
    'collection': 'u32',
    'free_holding': 'bool',
    'owner': {
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
#### destroy
Destroy a collection of fungible items.

The origin must conform to `ForceOrigin` or must be `Signed` and the sender must be the
owner of the `collection`.

- `collection`: The identifier of the collection to be destroyed.
- `witness`: Information on the items minted in the collection. This must be
correct.

Emits `Destroyed` event when successful.

Weight: `O(n + m)` where:
- `n = witness.items`
- `m = witness.item_metadatas`
- `a = witness.attributes`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| witness | `DestroyWitness` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'destroy', {
    'collection': 'u32',
    'witness': {
        'attributes': 'u32',
        'item_metadatas': 'u32',
        'items': 'u32',
    },
}
)
```

---------
#### mint
Mint an item of a particular collection.

The origin must be Signed and the sender must be the Issuer of the `collection`.

- `collection`: The collection of the item to be minted.
- `item`: The item value of the item to be minted.
- `beneficiary`: The initial owner of the minted item.

Emits `Issued` event when successful.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| owner | `<T::Lookup as StaticLookup>::Source` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'mint', {
    'collection': 'u32',
    'item': 'u32',
    'owner': {
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
#### burn
Destroy a single item.

Origin must be Signed and the sender should be the Admin of the `collection`.

- `collection`: The collection of the item to be burned.
- `item`: The item of the item to be burned.
- `check_owner`: If `Some` then the operation will fail with `WrongOwner` unless the
  item is owned by this value.

Emits `Burned` with the actual amount burned.

Weight: `O(1)`
Modes: `check_owner.is_some()`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| check_owner | `Option<<T::Lookup as StaticLookup>::Source>` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'burn', {
    'check_owner': (
        None,
        {
            'Address20': '[u8; 20]',
            'Address32': '[u8; 32]',
            'Id': 'AccountId',
            'Index': (),
            'Raw': 'Bytes',
        },
    ),
    'collection': 'u32',
    'item': 'u32',
}
)
```

---------
#### transfer
Move an item from the sender account to another.

Origin must be Signed and the signing account must be either:
- the Admin of the `collection`;
- the Owner of the `item`;
- the approved delegate for the `item` (in this case, the approval is reset).

Arguments:
- `collection`: The collection of the item to be transferred.
- `item`: The item of the item to be transferred.
- `dest`: The account to receive ownership of the item.

Emits `Transferred`.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| dest | `<T::Lookup as StaticLookup>::Source` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'transfer', {
    'collection': 'u32',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'item': 'u32',
}
)
```

---------
#### redeposit
Reevaluate the deposits on some items.

Origin must be Signed and the sender should be the Owner of the `collection`.

- `collection`: The collection to be frozen.
- `items`: The items of the collection whose deposits will be reevaluated.

NOTE: This exists as a best-effort function. Any items which are unknown or
in the case that the owner account does not have reservable funds to pay for a
deposit increase are ignored. Generally the owner isn&\#x27;t going to call this on items
whose existing deposit is less than the refreshed deposit as it would only cost them,
so it&\#x27;s of little consequence.

It will still return an error in the case that the collection is unknown of the signer
is not permitted to call it.

Weight: `O(items.len())`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| items | `Vec<T::ItemId>` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'redeposit', {'collection': 'u32', 'items': ['u32']}
)
```

---------
#### freeze
Disallow further unprivileged transfer of an item.

Origin must be Signed and the sender should be the Freezer of the `collection`.

- `collection`: The collection of the item to be frozen.
- `item`: The item of the item to be frozen.

Emits `Frozen`.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'freeze', {'collection': 'u32', 'item': 'u32'}
)
```

---------
#### thaw
Re-allow unprivileged transfer of an item.

Origin must be Signed and the sender should be the Freezer of the `collection`.

- `collection`: The collection of the item to be thawed.
- `item`: The item of the item to be thawed.

Emits `Thawed`.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'thaw', {'collection': 'u32', 'item': 'u32'}
)
```

---------
#### freeze_collection
Disallow further unprivileged transfers for a whole collection.

Origin must be Signed and the sender should be the Freezer of the `collection`.

- `collection`: The collection to be frozen.

Emits `CollectionFrozen`.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'freeze_collection', {'collection': 'u32'}
)
```

---------
#### thaw_collection
Re-allow unprivileged transfers for a whole collection.

Origin must be Signed and the sender should be the Admin of the `collection`.

- `collection`: The collection to be thawed.

Emits `CollectionThawed`.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'thaw_collection', {'collection': 'u32'}
)
```

---------
#### transfer_ownership
Change the Owner of a collection.

Origin must be Signed and the sender should be the Owner of the `collection`.

- `collection`: The collection whose owner should be changed.
- `owner`: The new Owner of this collection. They must have called
  `set_accept_ownership` with `collection` in order for this operation to succeed.

Emits `OwnerChanged`.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| owner | `<T::Lookup as StaticLookup>::Source` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'transfer_ownership', {
    'collection': 'u32',
    'owner': {
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
#### set_team
Change the Issuer, Admin and Freezer of a collection.

Origin must be Signed and the sender should be the Owner of the `collection`.

- `collection`: The collection whose team should be changed.
- `issuer`: The new Issuer of this collection.
- `admin`: The new Admin of this collection.
- `freezer`: The new Freezer of this collection.

Emits `TeamChanged`.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| issuer | `<T::Lookup as StaticLookup>::Source` | 
| admin | `<T::Lookup as StaticLookup>::Source` | 
| freezer | `<T::Lookup as StaticLookup>::Source` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'set_team', {
    'admin': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'collection': 'u32',
    'freezer': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'issuer': {
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
#### approve_transfer
Approve an item to be transferred by a delegated third-party account.

Origin must be Signed and must be the owner of the `item`.

- `collection`: The collection of the item to be approved for delegated transfer.
- `item`: The item of the item to be approved for delegated transfer.
- `delegate`: The account to delegate permission to transfer the item.

Emits `ApprovedTransfer` on success.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| delegate | `<T::Lookup as StaticLookup>::Source` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'approve_transfer', {
    'collection': 'u32',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'item': 'u32',
}
)
```

---------
#### cancel_approval
Cancel the prior approval for the transfer of an item by a delegate.

Origin must be either:
- the `Force` origin;
- `Signed` with the signer being the Admin of the `collection`;
- `Signed` with the signer being the Owner of the `item`;

Arguments:
- `collection`: The collection of the item of whose approval will be cancelled.
- `item`: The item of the item of whose approval will be cancelled.
- `maybe_check_delegate`: If `Some` will ensure that the given account is the one to
  which permission of transfer is delegated.

Emits `ApprovalCancelled` on success.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| maybe_check_delegate | `Option<<T::Lookup as StaticLookup>::Source>` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'cancel_approval', {
    'collection': 'u32',
    'item': 'u32',
    'maybe_check_delegate': (
        None,
        {
            'Address20': '[u8; 20]',
            'Address32': '[u8; 32]',
            'Id': 'AccountId',
            'Index': (),
            'Raw': 'Bytes',
        },
    ),
}
)
```

---------
#### force_item_status
Alter the attributes of a given item.

Origin must be `ForceOrigin`.

- `collection`: The identifier of the item.
- `owner`: The new Owner of this item.
- `issuer`: The new Issuer of this item.
- `admin`: The new Admin of this item.
- `freezer`: The new Freezer of this item.
- `free_holding`: Whether a deposit is taken for holding an item of this collection.
- `is_frozen`: Whether this collection is frozen except for permissioned/admin
instructions.

Emits `ItemStatusChanged` with the identity of the item.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| owner | `<T::Lookup as StaticLookup>::Source` | 
| issuer | `<T::Lookup as StaticLookup>::Source` | 
| admin | `<T::Lookup as StaticLookup>::Source` | 
| freezer | `<T::Lookup as StaticLookup>::Source` | 
| free_holding | `bool` | 
| is_frozen | `bool` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'force_item_status', {
    'admin': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'collection': 'u32',
    'free_holding': 'bool',
    'freezer': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'is_frozen': 'bool',
    'issuer': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'owner': {
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
#### set_attribute
Set an attribute for a collection or item.

Origin must be either `ForceOrigin` or Signed and the sender should be the Owner of the
`collection`.

If the origin is Signed, then funds of signer are reserved according to the formula:
`MetadataDepositBase + DepositPerByte * (key.len + value.len)` taking into
account any already reserved funds.

- `collection`: The identifier of the collection whose item&\#x27;s metadata to set.
- `maybe_item`: The identifier of the item whose metadata to set.
- `key`: The key of the attribute.
- `value`: The value to which to set the attribute.

Emits `AttributeSet`.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| maybe_item | `Option<T::ItemId>` | 
| key | `BoundedVec<u8, T::KeyLimit>` | 
| value | `BoundedVec<u8, T::ValueLimit>` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'set_attribute', {
    'collection': 'u32',
    'key': 'Bytes',
    'maybe_item': (None, 'u32'),
    'value': 'Bytes',
}
)
```

---------
#### clear_attribute
Clear an attribute for a collection or item.

Origin must be either `ForceOrigin` or Signed and the sender should be the Owner of the
`collection`.

Any deposit is freed for the collection&\#x27;s owner.

- `collection`: The identifier of the collection whose item&\#x27;s metadata to clear.
- `maybe_item`: The identifier of the item whose metadata to clear.
- `key`: The key of the attribute.

Emits `AttributeCleared`.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| maybe_item | `Option<T::ItemId>` | 
| key | `BoundedVec<u8, T::KeyLimit>` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'clear_attribute', {
    'collection': 'u32',
    'key': 'Bytes',
    'maybe_item': (None, 'u32'),
}
)
```

---------
#### set_metadata
Set the metadata for an item.

Origin must be either `ForceOrigin` or Signed and the sender should be the Owner of the
`collection`.

If the origin is Signed, then funds of signer are reserved according to the formula:
`MetadataDepositBase + DepositPerByte * data.len` taking into
account any already reserved funds.

- `collection`: The identifier of the collection whose item&\#x27;s metadata to set.
- `item`: The identifier of the item whose metadata to set.
- `data`: The general information of this item. Limited in length by `StringLimit`.
- `is_frozen`: Whether the metadata should be frozen against further changes.

Emits `MetadataSet`.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| data | `BoundedVec<u8, T::StringLimit>` | 
| is_frozen | `bool` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'set_metadata', {
    'collection': 'u32',
    'data': 'Bytes',
    'is_frozen': 'bool',
    'item': 'u32',
}
)
```

---------
#### clear_metadata
Clear the metadata for an item.

Origin must be either `ForceOrigin` or Signed and the sender should be the Owner of the
`item`.

Any deposit is freed for the collection&\#x27;s owner.

- `collection`: The identifier of the collection whose item&\#x27;s metadata to clear.
- `item`: The identifier of the item whose metadata to clear.

Emits `MetadataCleared`.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'clear_metadata', {'collection': 'u32', 'item': 'u32'}
)
```

---------
#### set_collection_metadata
Set the metadata for a collection.

Origin must be either `ForceOrigin` or `Signed` and the sender should be the Owner of
the `collection`.

If the origin is `Signed`, then funds of signer are reserved according to the formula:
`MetadataDepositBase + DepositPerByte * data.len` taking into
account any already reserved funds.

- `collection`: The identifier of the item whose metadata to update.
- `data`: The general information of this item. Limited in length by `StringLimit`.
- `is_frozen`: Whether the metadata should be frozen against further changes.

Emits `CollectionMetadataSet`.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| data | `BoundedVec<u8, T::StringLimit>` | 
| is_frozen | `bool` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'set_collection_metadata', {
    'collection': 'u32',
    'data': 'Bytes',
    'is_frozen': 'bool',
}
)
```

---------
#### clear_collection_metadata
Clear the metadata for a collection.

Origin must be either `ForceOrigin` or `Signed` and the sender should be the Owner of
the `collection`.

Any deposit is freed for the collection&\#x27;s owner.

- `collection`: The identifier of the collection whose metadata to clear.

Emits `CollectionMetadataCleared`.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'clear_collection_metadata', {'collection': 'u32'}
)
```

---------
#### set_accept_ownership
Set (or reset) the acceptance of ownership for a particular account.

Origin must be `Signed` and if `maybe_collection` is `Some`, then the signer must have a
provider reference.

- `maybe_collection`: The identifier of the collection whose ownership the signer is
  willing to accept, or if `None`, an indication that the signer is willing to accept no
  ownership transferal.

Emits `OwnershipAcceptanceChanged`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| maybe_collection | `Option<T::CollectionId>` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'set_accept_ownership', {'maybe_collection': (None, 'u32')}
)
```

---------
#### set_collection_max_supply
Set the maximum amount of items a collection could have.

Origin must be either `ForceOrigin` or `Signed` and the sender should be the Owner of
the `collection`.

Note: This function can only succeed once per collection.

- `collection`: The identifier of the collection to change.
- `max_supply`: The maximum amount of items a collection could have.

Emits `CollectionMaxSupplySet` event when successful.
##### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| max_supply | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'Uniques', 'set_collection_max_supply', {
    'collection': 'u32',
    'max_supply': 'u32',
}
)
```

---------
### Events
---------
#### Created
A `collection` was created.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| creator | `T::AccountId` | ```AccountId```
| owner | `T::AccountId` | ```AccountId```

---------
#### ForceCreated
A `collection` was force-created.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| owner | `T::AccountId` | ```AccountId```

---------
#### Destroyed
A `collection` was destroyed.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```

---------
#### Issued
An `item` was issued.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| owner | `T::AccountId` | ```AccountId```

---------
#### Transferred
An `item` was transferred.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```

---------
#### Burned
An `item` was destroyed.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| owner | `T::AccountId` | ```AccountId```

---------
#### Frozen
Some `item` was frozen.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```

---------
#### Thawed
Some `item` was thawed.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```

---------
#### CollectionFrozen
Some `collection` was frozen.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```

---------
#### CollectionThawed
Some `collection` was thawed.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```

---------
#### OwnerChanged
The owner changed.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| new_owner | `T::AccountId` | ```AccountId```

---------
#### TeamChanged
The management team changed.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| issuer | `T::AccountId` | ```AccountId```
| admin | `T::AccountId` | ```AccountId```
| freezer | `T::AccountId` | ```AccountId```

---------
#### ApprovedTransfer
An `item` of a `collection` has been approved by the `owner` for transfer by
a `delegate`.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| owner | `T::AccountId` | ```AccountId```
| delegate | `T::AccountId` | ```AccountId```

---------
#### ApprovalCancelled
An approval for a `delegate` account to transfer the `item` of an item
`collection` was cancelled by its `owner`.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| owner | `T::AccountId` | ```AccountId```
| delegate | `T::AccountId` | ```AccountId```

---------
#### ItemStatusChanged
A `collection` has had its attributes changed by the `Force` origin.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```

---------
#### CollectionMetadataSet
New metadata has been set for a `collection`.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| data | `BoundedVec<u8, T::StringLimit>` | ```Bytes```
| is_frozen | `bool` | ```bool```

---------
#### CollectionMetadataCleared
Metadata has been cleared for a `collection`.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```

---------
#### MetadataSet
New metadata has been set for an item.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| data | `BoundedVec<u8, T::StringLimit>` | ```Bytes```
| is_frozen | `bool` | ```bool```

---------
#### MetadataCleared
Metadata has been cleared for an item.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```

---------
#### Redeposited
Metadata has been cleared for an item.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| successful_items | `Vec<T::ItemId>` | ```['u32']```

---------
#### AttributeSet
New attribute metadata has been set for a `collection` or `item`.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| maybe_item | `Option<T::ItemId>` | ```(None, 'u32')```
| key | `BoundedVec<u8, T::KeyLimit>` | ```Bytes```
| value | `BoundedVec<u8, T::ValueLimit>` | ```Bytes```

---------
#### AttributeCleared
Attribute metadata has been cleared for a `collection` or `item`.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| maybe_item | `Option<T::ItemId>` | ```(None, 'u32')```
| key | `BoundedVec<u8, T::KeyLimit>` | ```Bytes```

---------
#### OwnershipAcceptanceChanged
Ownership acceptance has changed for an account.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| maybe_collection | `Option<T::CollectionId>` | ```(None, 'u32')```

---------
#### CollectionMaxSupplySet
Max supply has been set for a collection.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| max_supply | `u32` | ```u32```

---------
### Storage functions
---------
#### Class
 Details of a collection.

##### Python
```python
call = substrate.query(
    'Uniques', 'Class', ['u32']
)
```

##### Return value
```python
{
    'admin': 'AccountId',
    'attributes': 'u32',
    'free_holding': 'bool',
    'freezer': 'AccountId',
    'is_frozen': 'bool',
    'issuer': 'AccountId',
    'item_metadatas': 'u32',
    'items': 'u32',
    'owner': 'AccountId',
    'total_deposit': 'u128',
}
```
---------
#### OwnershipAcceptance
 The collection, if any, of which an account is willing to take ownership.

##### Python
```python
call = substrate.query(
    'Uniques', 'OwnershipAcceptance', ['AccountId']
)
```

##### Return value
```python
'u32'
```
---------
#### Account
 The items held by any given account; set out this way so that items owned by a single
 account can be enumerated.

##### Python
```python
call = substrate.query(
    'Uniques', 'Account', ['AccountId', 'u32', 'u32']
)
```

##### Return value
```python
()
```
---------
#### ClassAccount
 The collections owned by any given account; set out this way so that collections owned by
 a single account can be enumerated.

##### Python
```python
call = substrate.query(
    'Uniques', 'ClassAccount', ['AccountId', 'u32']
)
```

##### Return value
```python
()
```
---------
#### Asset
 The items in existence and their ownership details.

##### Python
```python
call = substrate.query(
    'Uniques', 'Asset', ['u32', 'u32']
)
```

##### Return value
```python
{'approved': (None, 'AccountId'), 'deposit': 'u128', 'is_frozen': 'bool', 'owner': 'AccountId'}
```
---------
#### ClassMetadataOf
 Metadata of a collection.

##### Python
```python
call = substrate.query(
    'Uniques', 'ClassMetadataOf', ['u32']
)
```

##### Return value
```python
{'data': 'Bytes', 'deposit': 'u128', 'is_frozen': 'bool'}
```
---------
#### InstanceMetadataOf
 Metadata of an item.

##### Python
```python
call = substrate.query(
    'Uniques', 'InstanceMetadataOf', ['u32', 'u32']
)
```

##### Return value
```python
{'data': 'Bytes', 'deposit': 'u128', 'is_frozen': 'bool'}
```
---------
#### Attribute
 Attributes of a collection.

##### Python
```python
call = substrate.query(
    'Uniques', 'Attribute', ['u32', (None, 'u32'), 'Bytes']
)
```

##### Return value
```python
('Bytes', 'u128')
```
---------
#### CollectionMaxSupply
 Keeps track of the number of items a collection might have.

##### Python
```python
call = substrate.query(
    'Uniques', 'CollectionMaxSupply', ['u32']
)
```

##### Return value
```python
'u32'
```
---------
### Constants
---------
#### CollectionDeposit
 The basic amount of funds that must be reserved for collection.
##### Value
```python
10000000000000
```
##### Python
```python
constant = substrate.get_constant('Uniques', 'CollectionDeposit')
```
---------
#### ItemDeposit
 The basic amount of funds that must be reserved for an item.
##### Value
```python
100000000000
```
##### Python
```python
constant = substrate.get_constant('Uniques', 'ItemDeposit')
```
---------
#### MetadataDepositBase
 The basic amount of funds that must be reserved when adding metadata to your item.
##### Value
```python
10000000000
```
##### Python
```python
constant = substrate.get_constant('Uniques', 'MetadataDepositBase')
```
---------
#### AttributeDepositBase
 The basic amount of funds that must be reserved when adding an attribute to an item.
##### Value
```python
10000000000
```
##### Python
```python
constant = substrate.get_constant('Uniques', 'AttributeDepositBase')
```
---------
#### DepositPerByte
 The additional funds that must be reserved for the number of bytes store in metadata,
 either &quot;normal&quot; metadata or attribute metadata.
##### Value
```python
1000000000
```
##### Python
```python
constant = substrate.get_constant('Uniques', 'DepositPerByte')
```
---------
#### StringLimit
 The maximum length of data stored on-chain.
##### Value
```python
50
```
##### Python
```python
constant = substrate.get_constant('Uniques', 'StringLimit')
```
---------
#### KeyLimit
 The maximum length of an attribute key.
##### Value
```python
32
```
##### Python
```python
constant = substrate.get_constant('Uniques', 'KeyLimit')
```
---------
#### ValueLimit
 The maximum length of an attribute value.
##### Value
```python
256
```
##### Python
```python
constant = substrate.get_constant('Uniques', 'ValueLimit')
```
---------
### Errors
---------
#### NoPermission
The signing account has no permission to do the operation.

---------
#### UnknownCollection
The given item ID is unknown.

---------
#### AlreadyExists
The item ID has already been used for an item.

---------
#### WrongOwner
The owner turned out to be different to what was expected.

---------
#### BadWitness
Invalid witness data given.

---------
#### InUse
The item ID is already taken.

---------
#### Frozen
The item or collection is frozen.

---------
#### WrongDelegate
The delegate turned out to be different to what was expected.

---------
#### NoDelegate
There is no delegate approved.

---------
#### Unapproved
No approval exists that would allow the transfer.

---------
#### Unaccepted
The named owner has not signed ownership of the collection is acceptable.

---------
#### Locked
The item is locked.

---------
#### MaxSupplyReached
All items have been minted.

---------
#### MaxSupplyAlreadySet
The max supply has already been set.

---------
#### MaxSupplyTooSmall
The provided max supply is less to the amount of items a collection already has.

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
call = substrate.query(
    'Preimage', 'StatusFor', ['[u8; 32]']
)
```

##### Return value
```python
{'Requested': 'u32', 'Unrequested': (None, ('AccountId', 'u128'))}
```
---------
#### PreimageFor
 The preimages stored by this pallet.

##### Python
```python
call = substrate.query(
    'Preimage', 'PreimageFor', ['[u8; 32]']
)
```

##### Return value
```python
'Bytes'
```
---------
### Errors
---------
#### TooLarge
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

## Allocations
---------
### Calls
---------
#### batch
Optimized allocation call, which will batch allocations of various amounts
and destinations and together. This allow us to be much more efficient and thus
increase our chain&\#x27;s capacity in handling these transactions.
##### Attributes
| Name | Type |
| -------- | -------- | 
| batch | `BoundedVec<(T::AccountId, BalanceOf<T>), T::MaxAllocs>` | 

##### Python
```python
call = substrate.compose_call(
    'Allocations', 'batch', {'batch': [('AccountId', 'u128')]}
)
```

---------
### Storage functions
---------
#### StorageVersion

##### Python
```python
call = substrate.query(
    'Allocations', 'StorageVersion', []
)
```

##### Return value
```python
('V0', 'V1')
```
---------
### Constants
---------
#### ProtocolFee
##### Value
```python
200000000
```
##### Python
```python
constant = substrate.get_constant('Allocations', 'ProtocolFee')
```
---------
#### MaximumSupply
##### Value
```python
2100000000000000000000
```
##### Python
```python
constant = substrate.get_constant('Allocations', 'MaximumSupply')
```
---------
#### ExistentialDeposit
 Runtime existential deposit
##### Value
```python
10000
```
##### Python
```python
constant = substrate.get_constant('Allocations', 'ExistentialDeposit')
```
---------
#### MaxAllocs
 How big a batch can be
##### Value
```python
500
```
##### Python
```python
constant = substrate.get_constant('Allocations', 'MaxAllocs')
```
---------
### Errors
---------
#### OracleAccessDenied
Function is restricted to oracles only

---------
#### TooManyCoinsToAllocate
We are trying to allocate more coins than we can

---------
#### DoesNotSatisfyExistentialDeposit
Amount is too low and will conflict with the ExistentialDeposit parameter

---------
#### BatchEmpty
Batch is empty or no issuance is necessary

---------

## AllocationsOracles
---------
### Calls
---------
#### add_member
Add a member `who` to the set.

May only be called from `T::AddOrigin`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

##### Python
```python
call = substrate.compose_call(
    'AllocationsOracles', 'add_member', {'who': 'AccountId'}
)
```

---------
#### remove_member
Remove a member `who` from the set.

May only be called from `T::RemoveOrigin`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

##### Python
```python
call = substrate.compose_call(
    'AllocationsOracles', 'remove_member', {'who': 'AccountId'}
)
```

---------
#### swap_member
Swap out one member `remove` for another `add`.

May only be called from `T::SwapOrigin`.

Prime membership is *not* passed from `remove` to `add`, if extant.
##### Attributes
| Name | Type |
| -------- | -------- | 
| remove | `T::AccountId` | 
| add | `T::AccountId` | 

##### Python
```python
call = substrate.compose_call(
    'AllocationsOracles', 'swap_member', {
    'add': 'AccountId',
    'remove': 'AccountId',
}
)
```

---------
#### reset_members
Change the membership to a new set, disregarding the existing membership. Be nice and
pass `members` pre-sorted.

May only be called from `T::ResetOrigin`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| members | `Vec<T::AccountId>` | 

##### Python
```python
call = substrate.compose_call(
    'AllocationsOracles', 'reset_members', {'members': ['AccountId']}
)
```

---------
#### change_key
Swap out the sending member for some other key `new`.

May only be called from `Signed` origin of a current member.

Prime membership is passed from the origin account to `new`, if extant.
##### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::AccountId` | 

##### Python
```python
call = substrate.compose_call(
    'AllocationsOracles', 'change_key', {'new': 'AccountId'}
)
```

---------
#### set_prime
Set the prime member. Must be a current member.

May only be called from `T::PrimeOrigin`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

##### Python
```python
call = substrate.compose_call(
    'AllocationsOracles', 'set_prime', {'who': 'AccountId'}
)
```

---------
#### clear_prime
Remove the prime member if it exists.

May only be called from `T::PrimeOrigin`.
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'AllocationsOracles', 'clear_prime', {}
)
```

---------
### Events
---------
#### MemberAdded
The given member was added; see the transaction for who.
##### Attributes
No attributes

---------
#### MemberRemoved
The given member was removed; see the transaction for who.
##### Attributes
No attributes

---------
#### MembersSwapped
Two members were swapped; see the transaction for who.
##### Attributes
No attributes

---------
#### MembersReset
The membership was reset; see the transaction for who the new set is.
##### Attributes
No attributes

---------
#### KeyChanged
One of the members&\#x27; keys changed.
##### Attributes
No attributes

---------
#### Dummy
Phantom member, never used.
##### Attributes
No attributes

---------
### Storage functions
---------
#### Members
 The current membership, stored as an ordered Vec.

##### Python
```python
call = substrate.query(
    'AllocationsOracles', 'Members', []
)
```

##### Return value
```python
['AccountId']
```
---------
#### Prime
 The current prime member, if one exists.

##### Python
```python
call = substrate.query(
    'AllocationsOracles', 'Prime', []
)
```

##### Return value
```python
'AccountId'
```
---------
### Errors
---------
#### AlreadyMember
Already a member.

---------
#### NotMember
Not a member.

---------
#### TooManyMembers
Too many members.

---------