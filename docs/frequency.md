# frequency
---------
| Properties |  |
| -------- | -------- |
| Spec name     | frequency     |
| Implementation name     | frequency     |
| Spec version     | 1     |
| SS58 Format     | 90     |
| Token symbol      | FRQCY     |
| Token decimals      | 8     |

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
| dispatch_info | `DispatchInfo` | ```{'weight': {'ref_time': 'u64'}, 'class': ('Normal', 'Operational', 'Mandatory'), 'pays_fee': ('Yes', 'No')}```

---------
#### ExtrinsicFailed
An extrinsic failed.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispatch_error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}```
| dispatch_info | `DispatchInfo` | ```{'weight': {'ref_time': 'u64'}, 'class': ('Normal', 'Operational', 'Mandatory'), 'pays_fee': ('Yes', 'No')}```

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
    'mandatory': {'ref_time': 'u64'},
    'normal': {'ref_time': 'u64'},
    'operational': {'ref_time': 'u64'},
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
            None: None,
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
                    'destination_status': 'scale_info::45',
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
            'CollatorSelection': {
                'CandidateAdded': {
                    'account_id': 'AccountId',
                    'deposit': 'u128',
                },
                'CandidateRemoved': {'account_id': 'AccountId'},
                'NewCandidacyBond': {'bond_amount': 'u128'},
                'NewDesiredCandidates': {'desired_candidates': 'u32'},
                'NewInvulnerables': {'invulnerables': ['AccountId']},
            },
            'Council': {
                'Approved': {'proposal_hash': '[u8; 32]'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': '[u8; 32]'},
                'Executed': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::30',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::30',
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
            'Democracy': {
                'Blacklisted': {'proposal_hash': '[u8; 32]'},
                'Cancelled': {'ref_index': 'u32'},
                'Delegated': {'target': 'AccountId', 'who': 'AccountId'},
                'Executed': {'ref_index': 'u32', 'result': 'scale_info::30'},
                'ExternalTabled': None,
                'NotPassed': {'ref_index': 'u32'},
                'Passed': {'ref_index': 'u32'},
                'PreimageInvalid': {
                    'proposal_hash': '[u8; 32]',
                    'ref_index': 'u32',
                },
                'PreimageMissing': {
                    'proposal_hash': '[u8; 32]',
                    'ref_index': 'u32',
                },
                'PreimageNoted': {
                    'deposit': 'u128',
                    'proposal_hash': '[u8; 32]',
                    'who': 'AccountId',
                },
                'PreimageReaped': {
                    'deposit': 'u128',
                    'proposal_hash': '[u8; 32]',
                    'provider': 'AccountId',
                    'reaper': 'AccountId',
                },
                'PreimageUsed': {
                    'deposit': 'u128',
                    'proposal_hash': '[u8; 32]',
                    'provider': 'AccountId',
                },
                'ProposalCanceled': {'prop_index': 'u32'},
                'Proposed': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Seconded': {'prop_index': 'u32', 'seconder': 'AccountId'},
                'Started': {'ref_index': 'u32', 'threshold': 'scale_info::36'},
                'Tabled': {
                    'deposit': 'u128',
                    'depositors': ['AccountId'],
                    'proposal_index': 'u32',
                },
                'Undelegated': {'account': 'AccountId'},
                'Vetoed': {
                    'proposal_hash': '[u8; 32]',
                    'until': 'u32',
                    'who': 'AccountId',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::37',
                    'voter': 'AccountId',
                },
            },
            'Messages': {
                'MessagesStored': {
                    'block_number': 'u32',
                    'count': 'u16',
                    'schema_id': 'u16',
                },
            },
            'Msa': {
                'DelegationGranted': {
                    'delegator_id': 'u64',
                    'provider_id': 'u64',
                },
                'DelegationRevoked': {
                    'delegator_id': 'u64',
                    'provider_id': 'u64',
                },
                'DelegationUpdated': {
                    'delegator_id': 'u64',
                    'provider_id': 'u64',
                },
                'MsaCreated': {'key': 'AccountId', 'msa_id': 'u64'},
                'MsaRetired': {'msa_id': 'u64'},
                'ProviderCreated': {'provider_id': 'u64'},
                'PublicKeyAdded': {'key': 'AccountId', 'msa_id': 'u64'},
                'PublicKeyDeleted': {'key': 'AccountId'},
            },
            'ParachainSystem': {
                'DownwardMessagesProcessed': {
                    'dmq_head': '[u8; 32]',
                    'weight_used': 'scale_info::8',
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
                    'error': 'scale_info::42',
                    'id': (None, 'Bytes'),
                    'task': ('u32', 'u32'),
                },
                'Canceled': {'index': 'u32', 'when': 'u32'},
                'Dispatched': {
                    'id': (None, 'Bytes'),
                    'result': 'scale_info::30',
                    'task': ('u32', 'u32'),
                },
                'Scheduled': {'index': 'u32', 'when': 'u32'},
            },
            'Schemas': {'SchemaCreated': ('AccountId', 'u16'), 'SchemaMaxSizeChanged': 'u32'},
            'Session': {'NewSession': {'session_index': 'u32'}},
            'Sudo': {
                'KeyChanged': {'old_sudoer': (None, 'AccountId')},
                'Sudid': {'sudo_result': 'scale_info::30'},
                'SudoAsDone': {'sudo_result': 'scale_info::30'},
            },
            'System': {
                'CodeUpdated': None,
                'ExtrinsicFailed': {
                    'dispatch_error': 'scale_info::23',
                    'dispatch_info': 'scale_info::20',
                },
                'ExtrinsicSuccess': {'dispatch_info': 'scale_info::20'},
                'KilledAccount': {'account': 'AccountId'},
                'NewAccount': {'account': 'AccountId'},
                'Remarked': {'hash': '[u8; 32]', 'sender': 'AccountId'},
            },
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
                    'result': 'scale_info::30',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::30',
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
            'TransactionPayment': {
                'TransactionFeePaid': {
                    'actual_fee': 'u128',
                    'tip': 'u128',
                    'who': 'AccountId',
                },
            },
            'Treasury': {
                'Awarded': {
                    'account': 'AccountId',
                    'award': 'u128',
                    'proposal_index': 'u32',
                },
                'Burnt': {'burnt_funds': 'u128'},
                'Deposit': {'value': 'u128'},
                'Proposed': {'proposal_index': 'u32'},
                'Rejected': {'proposal_index': 'u32', 'slashed': 'u128'},
                'Rollover': {'rollover_balance': 'u128'},
                'SpendApproved': {
                    'amount': 'u128',
                    'beneficiary': 'AccountId',
                    'proposal_index': 'u32',
                },
                'Spending': {'budget_remaining': 'u128'},
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::23',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::30'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::23'},
            },
            'Vesting': {
                'Claimed': {'amount': 'u128', 'who': 'AccountId'},
                'VestingScheduleAdded': {
                    'from': 'AccountId',
                    'to': 'AccountId',
                    'vesting_schedule': 'scale_info::54',
                },
                'VestingSchedulesUpdated': {'who': 'AccountId'},
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
    'base_block': {'ref_time': 5000000000},
    'max_block': {'ref_time': 500000000000},
    'per_class': {
        'mandatory': {
            'base_extrinsic': {'ref_time': 125000000},
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': {'ref_time': 125000000},
            'max_extrinsic': {'ref_time': 349875000000},
            'max_total': {'ref_time': 375000000000},
            'reserved': {'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'ref_time': 125000000},
            'max_extrinsic': {'ref_time': 474875000000},
            'max_total': {'ref_time': 500000000000},
            'reserved': {'ref_time': 125000000000},
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
        ('0xdf6acb689907609b', 4),
        ('0x37e397fc7c91f5e4', 1),
        ('0x40fe3ad401f8959a', 6),
        ('0xd2bc9897eed08f15', 3),
        ('0xf78b278be53f454c', 2),
        ('0xab3c0572291feb8b', 1),
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 1),
        ('0xea93e3f16f3d6962', 2),
        ('0x54bef602b989d121', 1),
        ('0x02fadd88517cc081', 1),
        ('0x24d062f93a859f6f', 1),
    ],
    'authoring_version': 1,
    'impl_name': 'frequency',
    'impl_version': 0,
    'spec_name': 'frequency',
    'spec_version': 1,
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
90
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
        'horizontal_messages': 'scale_info::109',
        'relay_chain_state': {
            'trie_nodes': 'scale_info::91',
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
| weight_used | `Weight` | ```{'ref_time': 'u64'}```
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
    'ParachainSystem', 'RelayStateProof', []
)
```

##### Return value
```python
{'trie_nodes': 'scale_info::91'}
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
    'ParachainSystem', 'LastHrmpMqcHeads', []
)
```

##### Return value
```python
'scale_info::100'
```
---------
#### ProcessedDownwardMessages
 Number of downward messages processed in a block.

 This will be cleared in `on_initialize` of each new block.

##### Python
```python
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
    'ParachainSystem', 'ReservedXcmpWeightOverride', []
)
```

##### Return value
```python
{'ref_time': 'u64'}
```
---------
#### ReservedDmpWeightOverride
 The weight we reserve at the beginning of the block for processing DMP messages. This
 overrides the amount set in the Config trait.

##### Python
```python
result = substrate.query(
    'ParachainSystem', 'ReservedDmpWeightOverride', []
)
```

##### Return value
```python
{'ref_time': 'u64'}
```
---------
#### AuthorizedUpgrade
 The next authorized upgrade, if there is one.

##### Python
```python
result = substrate.query(
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
result = substrate.query(
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
6000
```
##### Python
```python
constant = substrate.get_constant('Timestamp', 'MinimumPeriod')
```
---------

## ParachainInfo
---------
### Storage functions
---------
#### ParachainId

##### Python
```python
result = substrate.query(
    'ParachainInfo', 'ParachainId', []
)
```

##### Return value
```python
'u32'
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
| call | `Box<<T as Config>::Call>` | 

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
| call | `Box<<T as Config>::Call>` | 
| weight | `Weight` | 

##### Python
```python
call = substrate.compose_call(
    'Sudo', 'sudo_unchecked_weight', {
    'call': 'Call',
    'weight': {'ref_time': 'u64'},
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
| call | `Box<<T as Config>::Call>` | 

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
| sudo_result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

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
| sudo_result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

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
result = substrate.query(
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
result = substrate.query(
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

## Democracy
---------
### Calls
---------
#### propose
Propose a sensitive action to be taken.

The dispatch origin of this call must be _Signed_ and the sender must
have funds to cover the deposit.

- `proposal_hash`: The hash of the proposal preimage.
- `value`: The amount of deposit (must be at least `MinimumDeposit`).

Emits `Proposed`.

Weight: `O(p)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 
| value | `BalanceOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'propose', {
    'proposal_hash': '[u8; 32]',
    'value': 'u128',
}
)
```

---------
#### second
Signals agreement with a particular proposal.

The dispatch origin of this call must be _Signed_ and the sender
must have funds to cover the deposit, equal to the original deposit.

- `proposal`: The index of the proposal to second.
- `seconds_upper_bound`: an upper bound on the current number of seconds on this
  proposal. Extrinsic is weighted according to this value with no refund.

Weight: `O(S)` where S is the number of seconds a proposal already has.
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `PropIndex` | 
| seconds_upper_bound | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'second', {
    'proposal': 'u32',
    'seconds_upper_bound': 'u32',
}
)
```

---------
#### vote
Vote in a referendum. If `vote.is_aye()`, the vote is to enact the proposal;
otherwise it is a vote to keep the status quo.

The dispatch origin of this call must be _Signed_.

- `ref_index`: The index of the referendum to vote for.
- `vote`: The vote configuration.

Weight: `O(R)` where R is the number of referendums the voter has voted on.
##### Attributes
| Name | Type |
| -------- | -------- | 
| ref_index | `ReferendumIndex` | 
| vote | `AccountVote<BalanceOf<T>>` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'vote', {
    'ref_index': 'u32',
    'vote': {
        'Split': {
            'aye': 'u128',
            'nay': 'u128',
        },
        'Standard': {
            'balance': 'u128',
            'vote': {
                'aye': 'bool',
                'conviction': (
                    'None',
                    'Locked1x',
                    'Locked2x',
                    'Locked3x',
                    'Locked4x',
                    'Locked5x',
                    'Locked6x',
                ),
            },
        },
    },
}
)
```

---------
#### emergency_cancel
Schedule an emergency cancellation of a referendum. Cannot happen twice to the same
referendum.

The dispatch origin of this call must be `CancellationOrigin`.

-`ref_index`: The index of the referendum to cancel.

Weight: `O(1)`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| ref_index | `ReferendumIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'emergency_cancel', {'ref_index': 'u32'}
)
```

---------
#### external_propose
Schedule a referendum to be tabled once it is legal to schedule an external
referendum.

The dispatch origin of this call must be `ExternalOrigin`.

- `proposal_hash`: The preimage hash of the proposal.

Weight: `O(V)` with V number of vetoers in the blacklist of proposal.
  Decoding vec of length V. Charged as maximum
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'external_propose', {'proposal_hash': '[u8; 32]'}
)
```

---------
#### external_propose_majority
Schedule a majority-carries referendum to be tabled next once it is legal to schedule
an external referendum.

The dispatch of this call must be `ExternalMajorityOrigin`.

- `proposal_hash`: The preimage hash of the proposal.

Unlike `external_propose`, blacklisting has no effect on this and it may replace a
pre-scheduled `external_propose` call.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'external_propose_majority', {'proposal_hash': '[u8; 32]'}
)
```

---------
#### external_propose_default
Schedule a negative-turnout-bias referendum to be tabled next once it is legal to
schedule an external referendum.

The dispatch of this call must be `ExternalDefaultOrigin`.

- `proposal_hash`: The preimage hash of the proposal.

Unlike `external_propose`, blacklisting has no effect on this and it may replace a
pre-scheduled `external_propose` call.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'external_propose_default', {'proposal_hash': '[u8; 32]'}
)
```

---------
#### fast_track
Schedule the currently externally-proposed majority-carries referendum to be tabled
immediately. If there is no externally-proposed referendum currently, or if there is one
but it is not a majority-carries referendum then it fails.

The dispatch of this call must be `FastTrackOrigin`.

- `proposal_hash`: The hash of the current external proposal.
- `voting_period`: The period that is allowed for voting on this proposal.
	Must be always greater than zero.
	For `FastTrackOrigin` must be equal or greater than `FastTrackVotingPeriod`.
- `delay`: The number of block after voting has ended in approval and this should be
  enacted. This doesn&\#x27;t have a minimum amount.

Emits `Started`.

Weight: `O(1)`
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 
| voting_period | `T::BlockNumber` | 
| delay | `T::BlockNumber` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'fast_track', {
    'delay': 'u32',
    'proposal_hash': '[u8; 32]',
    'voting_period': 'u32',
}
)
```

---------
#### veto_external
Veto and blacklist the external proposal hash.

The dispatch origin of this call must be `VetoOrigin`.

- `proposal_hash`: The preimage hash of the proposal to veto and blacklist.

Emits `Vetoed`.

Weight: `O(V + log(V))` where V is number of `existing vetoers`
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'veto_external', {'proposal_hash': '[u8; 32]'}
)
```

---------
#### cancel_referendum
Remove a referendum.

The dispatch origin of this call must be _Root_.

- `ref_index`: The index of the referendum to cancel.

\# Weight: `O(1)`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| ref_index | `ReferendumIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'cancel_referendum', {'ref_index': 'u32'}
)
```

---------
#### cancel_queued
Cancel a proposal queued for enactment.

The dispatch origin of this call must be _Root_.

- `which`: The index of the referendum to cancel.

Weight: `O(D)` where `D` is the items in the dispatch queue. Weighted as `D = 10`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| which | `ReferendumIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'cancel_queued', {'which': 'u32'}
)
```

---------
#### delegate
Delegate the voting power (with some given conviction) of the sending account.

The balance delegated is locked for as long as it&\#x27;s delegated, and thereafter for the
time appropriate for the conviction&\#x27;s lock period.

The dispatch origin of this call must be _Signed_, and the signing account must either:
  - be delegating already; or
  - have no voting activity (if there is, then it will need to be removed/consolidated
    through `reap_vote` or `unvote`).

- `to`: The account whose voting the `target` account&\#x27;s voting power will follow.
- `conviction`: The conviction that will be attached to the delegated votes. When the
  account is undelegated, the funds will be locked for the corresponding period.
- `balance`: The amount of the account&\#x27;s balance to be used in delegating. This must not
  be more than the account&\#x27;s current balance.

Emits `Delegated`.

Weight: `O(R)` where R is the number of referendums the voter delegating to has
  voted on. Weight is charged as if maximum votes.
##### Attributes
| Name | Type |
| -------- | -------- | 
| to | `AccountIdLookupOf<T>` | 
| conviction | `Conviction` | 
| balance | `BalanceOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'delegate', {
    'balance': 'u128',
    'conviction': (
        'None',
        'Locked1x',
        'Locked2x',
        'Locked3x',
        'Locked4x',
        'Locked5x',
        'Locked6x',
    ),
    'to': {
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
#### undelegate
Undelegate the voting power of the sending account.

Tokens may be unlocked following once an amount of time consistent with the lock period
of the conviction with which the delegation was issued.

The dispatch origin of this call must be _Signed_ and the signing account must be
currently delegating.

Emits `Undelegated`.

Weight: `O(R)` where R is the number of referendums the voter delegating to has
  voted on. Weight is charged as if maximum votes.
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'undelegate', {}
)
```

---------
#### clear_public_proposals
Clears all public proposals.

The dispatch origin of this call must be _Root_.

Weight: `O(1)`.
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'clear_public_proposals', {}
)
```

---------
#### note_preimage
Register the preimage for an upcoming proposal. This doesn&\#x27;t require the proposal to be
in the dispatch queue but does require a deposit, returned once enacted.

The dispatch origin of this call must be _Signed_.

- `encoded_proposal`: The preimage of a proposal.

Emits `PreimageNoted`.

Weight: `O(E)` with E size of `encoded_proposal` (protected by a required deposit).
##### Attributes
| Name | Type |
| -------- | -------- | 
| encoded_proposal | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'note_preimage', {'encoded_proposal': 'Bytes'}
)
```

---------
#### note_preimage_operational
Same as `note_preimage` but origin is `OperationalPreimageOrigin`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| encoded_proposal | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'note_preimage_operational', {'encoded_proposal': 'Bytes'}
)
```

---------
#### note_imminent_preimage
Register the preimage for an upcoming proposal. This requires the proposal to be
in the dispatch queue. No deposit is needed. When this call is successful, i.e.
the preimage has not been uploaded before and matches some imminent proposal,
no fee is paid.

The dispatch origin of this call must be _Signed_.

- `encoded_proposal`: The preimage of a proposal.

Emits `PreimageNoted`.

Weight: `O(E)` with E size of `encoded_proposal` (protected by a required deposit).
##### Attributes
| Name | Type |
| -------- | -------- | 
| encoded_proposal | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'note_imminent_preimage', {'encoded_proposal': 'Bytes'}
)
```

---------
#### note_imminent_preimage_operational
Same as `note_imminent_preimage` but origin is `OperationalPreimageOrigin`.
##### Attributes
| Name | Type |
| -------- | -------- | 
| encoded_proposal | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'note_imminent_preimage_operational', {'encoded_proposal': 'Bytes'}
)
```

---------
#### reap_preimage
Remove an expired proposal preimage and collect the deposit.

The dispatch origin of this call must be _Signed_.

- `proposal_hash`: The preimage hash of a proposal.
- `proposal_length_upper_bound`: an upper bound on length of the proposal. Extrinsic is
  weighted according to this value with no refund.

This will only work after `VotingPeriod` blocks from the time that the preimage was
noted, if it&\#x27;s the same account doing it. If it&\#x27;s a different account, then it&\#x27;ll only
work an additional `EnactmentPeriod` later.

Emits `PreimageReaped`.

Weight: `O(D)` where D is length of proposal.
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 
| proposal_len_upper_bound | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'reap_preimage', {
    'proposal_hash': '[u8; 32]',
    'proposal_len_upper_bound': 'u32',
}
)
```

---------
#### unlock
Unlock tokens that have an expired lock.

The dispatch origin of this call must be _Signed_.

- `target`: The account to remove the lock on.

Weight: `O(R)` with R number of vote of target.
##### Attributes
| Name | Type |
| -------- | -------- | 
| target | `AccountIdLookupOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'unlock', {
    'target': {
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
#### remove_vote
Remove a vote for a referendum.

If:
- the referendum was cancelled, or
- the referendum is ongoing, or
- the referendum has ended such that
  - the vote of the account was in opposition to the result; or
  - there was no conviction to the account&\#x27;s vote; or
  - the account made a split vote
...then the vote is removed cleanly and a following call to `unlock` may result in more
funds being available.

If, however, the referendum has ended and:
- it finished corresponding to the vote of the account, and
- the account made a standard vote with conviction, and
- the lock period of the conviction is not over
...then the lock will be aggregated into the overall account&\#x27;s lock, which may involve
*overlocking* (where the two locks are combined into a single lock that is the maximum
of both the amount locked and the time is it locked for).

The dispatch origin of this call must be _Signed_, and the signer must have a vote
registered for referendum `index`.

- `index`: The index of referendum of the vote to be removed.

Weight: `O(R + log R)` where R is the number of referenda that `target` has voted on.
  Weight is calculated for the maximum number of vote.
##### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ReferendumIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'remove_vote', {'index': 'u32'}
)
```

---------
#### remove_other_vote
Remove a vote for a referendum.

If the `target` is equal to the signer, then this function is exactly equivalent to
`remove_vote`. If not equal to the signer, then the vote must have expired,
either because the referendum was cancelled, because the voter lost the referendum or
because the conviction period is over.

The dispatch origin of this call must be _Signed_.

- `target`: The account of the vote to be removed; this account must have voted for
  referendum `index`.
- `index`: The index of referendum of the vote to be removed.

Weight: `O(R + log R)` where R is the number of referenda that `target` has voted on.
  Weight is calculated for the maximum number of vote.
##### Attributes
| Name | Type |
| -------- | -------- | 
| target | `AccountIdLookupOf<T>` | 
| index | `ReferendumIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'remove_other_vote', {
    'index': 'u32',
    'target': {
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
#### enact_proposal
Enact a proposal from a referendum. For now we just make the weight be the maximum.
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 
| index | `ReferendumIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'enact_proposal', {
    'index': 'u32',
    'proposal_hash': '[u8; 32]',
}
)
```

---------
#### blacklist
Permanently place a proposal into the blacklist. This prevents it from ever being
proposed again.

If called on a queued public or external proposal, then this will result in it being
removed. If the `ref_index` supplied is an active referendum with the proposal hash,
then it will be cancelled.

The dispatch origin of this call must be `BlacklistOrigin`.

- `proposal_hash`: The proposal hash to blacklist permanently.
- `ref_index`: An ongoing referendum whose hash is `proposal_hash`, which will be
cancelled.

Weight: `O(p)` (though as this is an high-privilege dispatch, we assume it has a
  reasonable value).
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_hash | `T::Hash` | 
| maybe_ref_index | `Option<ReferendumIndex>` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'blacklist', {
    'maybe_ref_index': (None, 'u32'),
    'proposal_hash': '[u8; 32]',
}
)
```

---------
#### cancel_proposal
Remove a proposal.

The dispatch origin of this call must be `CancelProposalOrigin`.

- `prop_index`: The index of the proposal to cancel.

Weight: `O(p)` where `p = PublicProps::&lt;T&gt;::decode_len()`
##### Attributes
| Name | Type |
| -------- | -------- | 
| prop_index | `PropIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Democracy', 'cancel_proposal', {'prop_index': 'u32'}
)
```

---------
### Events
---------
#### Proposed
A motion has been proposed by a public account.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `PropIndex` | ```u32```
| deposit | `BalanceOf<T>` | ```u128```

---------
#### Tabled
A public proposal has been tabled for referendum vote.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `PropIndex` | ```u32```
| deposit | `BalanceOf<T>` | ```u128```
| depositors | `Vec<T::AccountId>` | ```['AccountId']```

---------
#### ExternalTabled
An external proposal has been tabled.
##### Attributes
No attributes

---------
#### Started
A referendum has begun.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```
| threshold | `VoteThreshold` | ```('SuperMajorityApprove', 'SuperMajorityAgainst', 'SimpleMajority')```

---------
#### Passed
A proposal has been approved by referendum.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```

---------
#### NotPassed
A proposal has been rejected by referendum.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```

---------
#### Cancelled
A referendum has been cancelled.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```

---------
#### Executed
A proposal has been enacted.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
#### Delegated
An account has delegated their vote to another account.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| target | `T::AccountId` | ```AccountId```

---------
#### Undelegated
An account has cancelled a previous delegation operation.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
#### Vetoed
An external proposal has been vetoed.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| proposal_hash | `T::Hash` | ```[u8; 32]```
| until | `T::BlockNumber` | ```u32```

---------
#### PreimageNoted
A proposal&\#x27;s preimage was noted, and the deposit taken.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| who | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```

---------
#### PreimageUsed
A proposal preimage was removed and used (the deposit was returned).
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| provider | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```

---------
#### PreimageInvalid
A proposal could not be executed because its preimage was invalid.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| ref_index | `ReferendumIndex` | ```u32```

---------
#### PreimageMissing
A proposal could not be executed because its preimage was missing.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| ref_index | `ReferendumIndex` | ```u32```

---------
#### PreimageReaped
A registered preimage was removed and the deposit collected by the reaper.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| provider | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```
| reaper | `T::AccountId` | ```AccountId```

---------
#### Blacklisted
A proposal_hash has been blacklisted permanently.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```

---------
#### Voted
An account has voted in a referendum
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| voter | `T::AccountId` | ```AccountId```
| ref_index | `ReferendumIndex` | ```u32```
| vote | `AccountVote<BalanceOf<T>>` | ```{'Standard': {'vote': {'aye': 'bool', 'conviction': ('None', 'Locked1x', 'Locked2x', 'Locked3x', 'Locked4x', 'Locked5x', 'Locked6x')}, 'balance': 'u128'}, 'Split': {'aye': 'u128', 'nay': 'u128'}}```

---------
#### Seconded
An account has secconded a proposal
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| seconder | `T::AccountId` | ```AccountId```
| prop_index | `PropIndex` | ```u32```

---------
#### ProposalCanceled
A proposal got canceled.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| prop_index | `PropIndex` | ```u32```

---------
### Storage functions
---------
#### PublicPropCount
 The number of (public) proposals that have been made so far.

##### Python
```python
result = substrate.query(
    'Democracy', 'PublicPropCount', []
)
```

##### Return value
```python
'u32'
```
---------
#### PublicProps
 The public proposals. Unsorted. The second item is the proposal&#x27;s hash.

##### Python
```python
result = substrate.query(
    'Democracy', 'PublicProps', []
)
```

##### Return value
```python
[('u32', '[u8; 32]', 'AccountId')]
```
---------
#### DepositOf
 Those who have locked a deposit.

 TWOX-NOTE: Safe, as increasing integer keys are safe.

##### Python
```python
result = substrate.query(
    'Democracy', 'DepositOf', ['u32']
)
```

##### Return value
```python
(['AccountId'], 'u128')
```
---------
#### Preimages
 Map of hashes to the proposal preimage, along with who registered it and their deposit.
 The block number is the block at which it was deposited.

##### Python
```python
result = substrate.query(
    'Democracy', 'Preimages', ['[u8; 32]']
)
```

##### Return value
```python
{
    'Available': {
        'data': 'Bytes',
        'deposit': 'u128',
        'expiry': (None, 'u32'),
        'provider': 'AccountId',
        'since': 'u32',
    },
    'Missing': 'u32',
}
```
---------
#### ReferendumCount
 The next free referendum index, aka the number of referenda started so far.

##### Python
```python
result = substrate.query(
    'Democracy', 'ReferendumCount', []
)
```

##### Return value
```python
'u32'
```
---------
#### LowestUnbaked
 The lowest referendum index representing an unbaked referendum. Equal to
 `ReferendumCount` if there isn&#x27;t a unbaked referendum.

##### Python
```python
result = substrate.query(
    'Democracy', 'LowestUnbaked', []
)
```

##### Return value
```python
'u32'
```
---------
#### ReferendumInfoOf
 Information concerning any given referendum.

 TWOX-NOTE: SAFE as indexes are not under an attacker’s control.

##### Python
```python
result = substrate.query(
    'Democracy', 'ReferendumInfoOf', ['u32']
)
```

##### Return value
```python
{
    'Finished': {'approved': 'bool', 'end': 'u32'},
    'Ongoing': {
        'delay': 'u32',
        'end': 'u32',
        'proposal_hash': '[u8; 32]',
        'tally': {'ayes': 'u128', 'nays': 'u128', 'turnout': 'u128'},
        'threshold': (
            'SuperMajorityApprove',
            'SuperMajorityAgainst',
            'SimpleMajority',
        ),
    },
}
```
---------
#### VotingOf
 All votes for a particular voter. We store the balance for the number of votes that we
 have recorded. The second item is the total amount of delegations, that will be added.

 TWOX-NOTE: SAFE as `AccountId`s are crypto hashes anyway.

##### Python
```python
result = substrate.query(
    'Democracy', 'VotingOf', ['AccountId']
)
```

##### Return value
```python
{
    'Delegating': {
        'balance': 'u128',
        'conviction': (
            'None',
            'Locked1x',
            'Locked2x',
            'Locked3x',
            'Locked4x',
            'Locked5x',
            'Locked6x',
        ),
        'delegations': {'capital': 'u128', 'votes': 'u128'},
        'prior': ('u32', 'u128'),
        'target': 'AccountId',
    },
    'Direct': {
        'delegations': {'capital': 'u128', 'votes': 'u128'},
        'prior': ('u32', 'u128'),
        'votes': [('u32', {'Split': 'InnerStruct', 'Standard': 'InnerStruct'})],
    },
}
```
---------
#### LastTabledWasExternal
 True if the last referendum tabled was submitted externally. False if it was a public
 proposal.

##### Python
```python
result = substrate.query(
    'Democracy', 'LastTabledWasExternal', []
)
```

##### Return value
```python
'bool'
```
---------
#### NextExternal
 The referendum to be tabled whenever it would be valid to table an external proposal.
 This happens when a referendum needs to be tabled and one of two conditions are met:
 - `LastTabledWasExternal` is `false`; or
 - `PublicProps` is empty.

##### Python
```python
result = substrate.query(
    'Democracy', 'NextExternal', []
)
```

##### Return value
```python
(
    '[u8; 32]',
    ('SuperMajorityApprove', 'SuperMajorityAgainst', 'SimpleMajority'),
)
```
---------
#### Blacklist
 A record of who vetoed what. Maps proposal hash to a possible existent block number
 (until when it may not be resubmitted) and who vetoed it.

##### Python
```python
result = substrate.query(
    'Democracy', 'Blacklist', ['[u8; 32]']
)
```

##### Return value
```python
('u32', ['AccountId'])
```
---------
#### Cancellations
 Record of all proposals that have been subject to emergency cancellation.

##### Python
```python
result = substrate.query(
    'Democracy', 'Cancellations', ['[u8; 32]']
)
```

##### Return value
```python
'bool'
```
---------
#### StorageVersion
 Storage version of the pallet.

 New networks start with last version.

##### Python
```python
result = substrate.query(
    'Democracy', 'StorageVersion', []
)
```

##### Return value
```python
('V1', )
```
---------
### Constants
---------
#### EnactmentPeriod
 The period between a proposal being approved and enacted.

 It should generally be a little more than the unstake period to ensure that
 voting stakers have an opportunity to remove themselves from the system in the case
 where they are on the losing side of a vote.
##### Value
```python
57600
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'EnactmentPeriod')
```
---------
#### LaunchPeriod
 How often (in blocks) new public referenda are launched.
##### Value
```python
50400
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'LaunchPeriod')
```
---------
#### VotingPeriod
 How often (in blocks) to check for new votes.
##### Value
```python
50400
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'VotingPeriod')
```
---------
#### VoteLockingPeriod
 The minimum period of vote locking.

 It should be no shorter than enactment period to ensure that in the case of an approval,
 those successful voters are locked into the consequences that their votes entail.
##### Value
```python
57600
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'VoteLockingPeriod')
```
---------
#### MinimumDeposit
 The minimum amount to be used as a deposit for a public referendum proposal.
##### Value
```python
10000000000
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'MinimumDeposit')
```
---------
#### InstantAllowed
 Indicator for whether an emergency origin is even allowed to happen. Some chains may
 want to set this permanently to `false`, others may want to condition it on things such
 as an upgrade having happened recently.
##### Value
```python
True
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'InstantAllowed')
```
---------
#### FastTrackVotingPeriod
 Minimum voting period allowed for a fast-track referendum.
##### Value
```python
900
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'FastTrackVotingPeriod')
```
---------
#### CooloffPeriod
 Period in blocks where an external proposal may not be re-submitted after being vetoed.
##### Value
```python
50400
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'CooloffPeriod')
```
---------
#### PreimageByteDeposit
 The amount of balance that must be deposited per byte of preimage stored.
##### Value
```python
100000
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'PreimageByteDeposit')
```
---------
#### MaxVotes
 The maximum number of votes for an account.

 Also used to compute weight, an overly big value can
 lead to extrinsic with very big weight: see `delegate` for instance.
##### Value
```python
100
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'MaxVotes')
```
---------
#### MaxProposals
 The maximum number of public proposals that can exist at any time.
##### Value
```python
100
```
##### Python
```python
constant = substrate.get_constant('Democracy', 'MaxProposals')
```
---------
### Errors
---------
#### ValueLow
Value too low

---------
#### ProposalMissing
Proposal does not exist

---------
#### AlreadyCanceled
Cannot cancel the same proposal twice

---------
#### DuplicateProposal
Proposal already made

---------
#### ProposalBlacklisted
Proposal still blacklisted

---------
#### NotSimpleMajority
Next external proposal not simple majority

---------
#### InvalidHash
Invalid hash

---------
#### NoProposal
No external proposal

---------
#### AlreadyVetoed
Identity may not veto a proposal twice

---------
#### DuplicatePreimage
Preimage already noted

---------
#### NotImminent
Not imminent

---------
#### TooEarly
Too early

---------
#### Imminent
Imminent

---------
#### PreimageMissing
Preimage not found

---------
#### ReferendumInvalid
Vote given for invalid referendum

---------
#### PreimageInvalid
Invalid preimage

---------
#### NoneWaiting
No proposals waiting

---------
#### NotVoter
The given account did not vote on the referendum.

---------
#### NoPermission
The actor has no permission to conduct the action.

---------
#### AlreadyDelegating
The account is already delegating.

---------
#### InsufficientFunds
Too high a balance was provided that the account cannot afford.

---------
#### NotDelegating
The account is not currently delegating.

---------
#### VotesExist
The account currently has votes attached to it and the operation cannot succeed until
these are removed, either through `unvote` or `reap_vote`.

---------
#### InstantNotAllowed
The instant referendum origin is currently disallowed.

---------
#### Nonsense
Delegation to oneself makes no sense.

---------
#### WrongUpperBound
Invalid upper bound.

---------
#### MaxVotesReached
Maximum number of votes reached.

---------
#### TooManyProposals
Maximum number of proposals reached.

---------
#### VotingPeriodLow
Voting period too low

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
            'call': {'Hash': '[u8; 32]', 'Value': 'Call'},
            'maybe_id': (None, 'Bytes'),
            'maybe_periodic': (None, ('u32', 'u32')),
            'origin': {
                None: None,
                'Council': {
                    'Member': 'AccountId',
                    'Members': ('u32', 'u32'),
                    '_Phantom': None,
                },
                'TechnicalCommittee': {
                    'Member': 'AccountId',
                    'Members': ('u32', 'u32'),
                    '_Phantom': None,
                },
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
 Lookup from identity to the block number and index of the task.

##### Python
```python
result = substrate.query(
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
{'ref_time': 50000000000}
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
        'Council': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
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
#### StorageVersion
 Storage version of the pallet.

 This is set to v2.0.0 for new networks.

##### Python
```python
result = substrate.query(
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
1000000
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
50
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

## Council
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
    'Council', 'set_members', {
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
    'Council', 'execute', {
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
    'Council', 'propose', {
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
    'Council', 'vote', {
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
    'Council', 'close', {
    'index': 'u32',
    'length_bound': 'u32',
    'proposal_hash': '[u8; 32]',
    'proposal_weight_bound': {
        'ref_time': 'u64',
    },
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
    'Council', 'disapprove_proposal', {'proposal_hash': '[u8; 32]'}
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
result = substrate.query(
    'Council', 'Proposals', []
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
result = substrate.query(
    'Council', 'ProposalOf', ['[u8; 32]']
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
result = substrate.query(
    'Council', 'Voting', ['[u8; 32]']
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
result = substrate.query(
    'Council', 'ProposalCount', []
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
result = substrate.query(
    'Council', 'Members', []
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
result = substrate.query(
    'Council', 'Prime', []
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
    'proposal_weight_bound': {
        'ref_time': 'u64',
    },
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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

## Treasury
---------
### Calls
---------
#### propose_spend
Put forward a suggestion for spending. A deposit proportional to the value
is reserved and slashed if the proposal is rejected. It is returned once the
proposal is awarded.

\# &lt;weight&gt;
- Complexity: O(1)
- DbReads: `ProposalCount`, `origin account`
- DbWrites: `ProposalCount`, `Proposals`, `origin account`
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| value | `BalanceOf<T, I>` | 
| beneficiary | `AccountIdLookupOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Treasury', 'propose_spend', {
    'beneficiary': {
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
#### reject_proposal
Reject a proposed spend. The original deposit will be slashed.

May only be called from `T::RejectOrigin`.

\# &lt;weight&gt;
- Complexity: O(1)
- DbReads: `Proposals`, `rejected proposer account`
- DbWrites: `Proposals`, `rejected proposer account`
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_id | `ProposalIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Treasury', 'reject_proposal', {'proposal_id': 'u32'}
)
```

---------
#### approve_proposal
Approve a proposal. At a later time, the proposal will be allocated to the beneficiary
and the original deposit will be returned.

May only be called from `T::ApproveOrigin`.

\# &lt;weight&gt;
- Complexity: O(1).
- DbReads: `Proposals`, `Approvals`
- DbWrite: `Approvals`
\# &lt;/weight&gt;
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_id | `ProposalIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Treasury', 'approve_proposal', {'proposal_id': 'u32'}
)
```

---------
#### spend
Propose and approve a spend of treasury funds.

- `origin`: Must be `SpendOrigin` with the `Success` value being at least `amount`.
- `amount`: The amount to be transferred from the treasury to the `beneficiary`.
- `beneficiary`: The destination account for the transfer.

NOTE: For record-keeping purposes, the proposer is deemed to be equivalent to the
beneficiary.
##### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T, I>` | 
| beneficiary | `AccountIdLookupOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Treasury', 'spend', {
    'amount': 'u128',
    'beneficiary': {
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
#### remove_approval
Force a previously approved proposal to be removed from the approval queue.
The original deposit will no longer be returned.

May only be called from `T::RejectOrigin`.
- `proposal_id`: The index of a proposal

\# &lt;weight&gt;
- Complexity: O(A) where `A` is the number of approvals
- Db reads and writes: `Approvals`
\# &lt;/weight&gt;

Errors:
- `ProposalNotApproved`: The `proposal_id` supplied was not found in the approval queue,
i.e., the proposal has not been approved. This could also mean the proposal does not
exist altogether, thus there is no way it would have been approved in the first place.
##### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_id | `ProposalIndex` | 

##### Python
```python
call = substrate.compose_call(
    'Treasury', 'remove_approval', {'proposal_id': 'u32'}
)
```

---------
### Events
---------
#### Proposed
New proposal.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```

---------
#### Spending
We have ended a spend period and will now allocate funds.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| budget_remaining | `BalanceOf<T, I>` | ```u128```

---------
#### Awarded
Some funds have been allocated.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```
| award | `BalanceOf<T, I>` | ```u128```
| account | `T::AccountId` | ```AccountId```

---------
#### Rejected
A proposal was rejected; funds were slashed.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```
| slashed | `BalanceOf<T, I>` | ```u128```

---------
#### Burnt
Some of our funds have been burnt.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| burnt_funds | `BalanceOf<T, I>` | ```u128```

---------
#### Rollover
Spending has finished; this is the amount that rolls over until next spend.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| rollover_balance | `BalanceOf<T, I>` | ```u128```

---------
#### Deposit
Some funds have been deposited.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| value | `BalanceOf<T, I>` | ```u128```

---------
#### SpendApproved
A new spend proposal has been approved.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```
| amount | `BalanceOf<T, I>` | ```u128```
| beneficiary | `T::AccountId` | ```AccountId```

---------
### Storage functions
---------
#### ProposalCount
 Number of proposals that have been made.

##### Python
```python
result = substrate.query(
    'Treasury', 'ProposalCount', []
)
```

##### Return value
```python
'u32'
```
---------
#### Proposals
 Proposals that have been made.

##### Python
```python
result = substrate.query(
    'Treasury', 'Proposals', ['u32']
)
```

##### Return value
```python
{
    'beneficiary': 'AccountId',
    'bond': 'u128',
    'proposer': 'AccountId',
    'value': 'u128',
}
```
---------
#### Approvals
 Proposal indices that have been approved but not yet awarded.

##### Python
```python
result = substrate.query(
    'Treasury', 'Approvals', []
)
```

##### Return value
```python
['u32']
```
---------
### Constants
---------
#### ProposalBond
 Fraction of a proposal&#x27;s value that should be bonded in order to place the proposal.
 An accepted proposal gets these back. A rejected proposal does not.
##### Value
```python
50000
```
##### Python
```python
constant = substrate.get_constant('Treasury', 'ProposalBond')
```
---------
#### ProposalBondMinimum
 Minimum amount of funds that should be placed in a deposit for making a proposal.
##### Value
```python
10000000000
```
##### Python
```python
constant = substrate.get_constant('Treasury', 'ProposalBondMinimum')
```
---------
#### ProposalBondMaximum
 Maximum amount of funds that should be placed in a deposit for making a proposal.
##### Value
```python
100000000000
```
##### Python
```python
constant = substrate.get_constant('Treasury', 'ProposalBondMaximum')
```
---------
#### SpendPeriod
 Period between successive spends.
##### Value
```python
50400
```
##### Python
```python
constant = substrate.get_constant('Treasury', 'SpendPeriod')
```
---------
#### Burn
 Percentage of spare funds (if any) that are burnt per spend period.
##### Value
```python
0
```
##### Python
```python
constant = substrate.get_constant('Treasury', 'Burn')
```
---------
#### PalletId
 The treasury&#x27;s pallet id, used for deriving its sovereign account ID.
##### Value
```python
'0x70792f7472737279'
```
##### Python
```python
constant = substrate.get_constant('Treasury', 'PalletId')
```
---------
#### MaxApprovals
 The maximum number of approvals that can wait in the spending queue.

 NOTE: This parameter is also used within the Bounties Pallet extension if enabled.
##### Value
```python
64
```
##### Python
```python
constant = substrate.get_constant('Treasury', 'MaxApprovals')
```
---------
### Errors
---------
#### InsufficientProposersBalance
Proposer&\#x27;s balance is too low.

---------
#### InvalidIndex
No proposal or bounty at that index.

---------
#### TooManyApprovals
Too many approvals in the queue.

---------
#### InsufficientPermission
The spend origin is valid but the amount it is allowed to spend is lower than the
amount to be spent.

---------
#### ProposalNotApproved
Proposal has not been approved.

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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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

## CollatorSelection
---------
### Calls
---------
#### set_invulnerables
Set the list of invulnerable (fixed) collators.
##### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Vec<T::AccountId>` | 

##### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'set_invulnerables', {'new': ['AccountId']}
)
```

---------
#### set_desired_candidates
Set the ideal number of collators (not including the invulnerables).
If lowering this number, then the number of running collators could be higher than this figure.
Aside from that edge case, there should be no other way to have more collators than the desired number.
##### Attributes
| Name | Type |
| -------- | -------- | 
| max | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'set_desired_candidates', {'max': 'u32'}
)
```

---------
#### set_candidacy_bond
Set the candidacy bond amount.
##### Attributes
| Name | Type |
| -------- | -------- | 
| bond | `BalanceOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'set_candidacy_bond', {'bond': 'u128'}
)
```

---------
#### register_as_candidate
Register this account as a collator candidate. The account must (a) already have
registered session keys and (b) be able to reserve the `CandidacyBond`.

This call is not available to `Invulnerable` collators.
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'register_as_candidate', {}
)
```

---------
#### leave_intent
Deregister `origin` as a collator candidate. Note that the collator can only leave on
session change. The `CandidacyBond` will be unreserved immediately.

This call will fail if the total number of candidates would drop below `MinCandidates`.

This call is not available to `Invulnerable` collators.
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'leave_intent', {}
)
```

---------
### Events
---------
#### NewInvulnerables
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| invulnerables | `Vec<T::AccountId>` | ```['AccountId']```

---------
#### NewDesiredCandidates
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| desired_candidates | `u32` | ```u32```

---------
#### NewCandidacyBond
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| bond_amount | `BalanceOf<T>` | ```u128```

---------
#### CandidateAdded
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```

---------
#### CandidateRemoved
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
### Storage functions
---------
#### Invulnerables
 The invulnerable, fixed collators.

##### Python
```python
result = substrate.query(
    'CollatorSelection', 'Invulnerables', []
)
```

##### Return value
```python
['AccountId']
```
---------
#### Candidates
 The (community, limited) collation candidates.

##### Python
```python
result = substrate.query(
    'CollatorSelection', 'Candidates', []
)
```

##### Return value
```python
[{'deposit': 'u128', 'who': 'AccountId'}]
```
---------
#### LastAuthoredBlock
 Last block authored by collator.

##### Python
```python
result = substrate.query(
    'CollatorSelection', 'LastAuthoredBlock', ['AccountId']
)
```

##### Return value
```python
'u32'
```
---------
#### DesiredCandidates
 Desired number of candidates.

 This should ideally always be less than [`Config::MaxCandidates`] for weights to be correct.

##### Python
```python
result = substrate.query(
    'CollatorSelection', 'DesiredCandidates', []
)
```

##### Return value
```python
'u32'
```
---------
#### CandidacyBond
 Fixed amount to deposit to become a collator.

 When a collator calls `leave_intent` they immediately receive the deposit back.

##### Python
```python
result = substrate.query(
    'CollatorSelection', 'CandidacyBond', []
)
```

##### Return value
```python
'u128'
```
---------
### Errors
---------
#### TooManyCandidates
Too many candidates

---------
#### TooFewCandidates
Too few candidates

---------
#### Unknown
Unknown error

---------
#### Permission
Permission issue

---------
#### AlreadyCandidate
User is already a candidate

---------
#### NotCandidate
User is not a candidate

---------
#### TooManyInvulnerables
Too many invulnerables

---------
#### AlreadyInvulnerable
User is already an Invulnerable

---------
#### NoAssociatedValidatorId
Account has no associated validator ID

---------
#### ValidatorNotRegistered
Validator ID is not yet registered

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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
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
result = substrate.query(
    'AuraExt', 'Authorities', []
)
```

##### Return value
```python
['[u8; 32]']
```
---------

## Vesting
---------
### Calls
---------
#### claim
##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'Vesting', 'claim', {}
)
```

---------
#### vested_transfer
##### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| schedule | `VestingScheduleOf<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Vesting', 'vested_transfer', {
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
#### update_vesting_schedules
##### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| vesting_schedules | `Vec<VestingScheduleOf<T>>` | 

##### Python
```python
call = substrate.compose_call(
    'Vesting', 'update_vesting_schedules', {
    'vesting_schedules': [
        {
            'per_period': 'u128',
            'period': 'u32',
            'period_count': 'u32',
            'start': 'u32',
        },
    ],
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
#### claim_for
##### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 

##### Python
```python
call = substrate.compose_call(
    'Vesting', 'claim_for', {
    'dest': {
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
Added new vesting schedule.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| vesting_schedule | `VestingScheduleOf<T>` | ```{'start': 'u32', 'period': 'u32', 'period_count': 'u32', 'per_period': 'u128'}```

---------
#### Claimed
Claimed vesting.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
#### VestingSchedulesUpdated
Updated vesting schedules.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

---------
### Storage functions
---------
#### VestingSchedules
 Vesting schedules of an account.

 VestingSchedules: map AccountId =&gt; Vec&lt;VestingSchedule&gt;

##### Python
```python
result = substrate.query(
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
### Constants
---------
#### MinVestedTransfer
 The minimum amount transferred to call `vested_transfer`.
##### Value
```python
0
```
##### Python
```python
constant = substrate.get_constant('Vesting', 'MinVestedTransfer')
```
---------
### Errors
---------
#### ZeroVestingPeriod
Vesting period is zero

---------
#### ZeroVestingPeriodCount
Number of vests is zero

---------
#### InsufficientBalanceToLock
Insufficient amount of balance to lock

---------
#### TooManyVestingSchedules
This account have too many vesting schedules

---------
#### AmountLow
The vested transfer amount is too low

---------
#### MaxVestingSchedulesExceeded
Failed because the maximum vesting schedules was exceeded

---------

## Msa
---------
### Calls
---------
#### create
Creates an MSA for the Origin (sender of the transaction).  Origin is assigned an MSA ID.

\# Events
* [`Event::MsaCreated`]

\# Errors

* [`Error::KeyAlreadyRegistered`] - MSA is already registered to the Origin.

##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'Msa', 'create', {}
)
```

---------
#### create_sponsored_account_with_delegation
`Origin` MSA creates an MSA on behalf of `delegator_key`, creates a Delegation with the `delegator_key`&\#x27;s MSA as the Delegator and `origin` as `Provider`. Deposits events [`MsaCreated`](Event::MsaCreated) and [`DelegationGranted`](Event::DelegationGranted).

\# Remarks
* Origin MUST be the provider
* Signatures should be over the [`AddProvider`] struct

\# Events
* [`Event::MsaCreated`]
* [`Event::DelegationGranted`]

\# Errors

* [`Error::UnauthorizedProvider`] - payload&\#x27;s MSA does not match given provider MSA.
* [`Error::InvalidSignature`] - `proof` verification fails; `delegator_key` must have signed `add_provider_payload`
* [`Error::NoKeyExists`] - there is no MSA for `origin`.
* [`Error::KeyAlreadyRegistered`] - there is already an MSA for `delegator_key`.
* [`Error::ProviderNotRegistered`] - the a non-provider MSA is used as the provider
* [`Error::ProofNotYetValid`] - `add_provider_payload` expiration is too far in the future
* [`Error::ProofHasExpired`] - `add_provider_payload` expiration is in the past
* [`Error::SignatureAlreadySubmitted`] - signature has already been used

##### Attributes
| Name | Type |
| -------- | -------- | 
| delegator_key | `T::AccountId` | 
| proof | `MultiSignature` | 
| add_provider_payload | `AddProvider` | 

##### Python
```python
call = substrate.compose_call(
    'Msa', 'create_sponsored_account_with_delegation', {
    'add_provider_payload': {
        'authorized_msa_id': 'u64',
        'expiration': 'u32',
        'schema_ids': ['u16'],
    },
    'delegator_key': 'AccountId',
    'proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
#### create_provider
Adds an association between MSA id and ProviderRegistryEntry. As of now, the
only piece of metadata we are recording is provider name.

\# Events
* [`Event::ProviderCreated`]

\# Errors
* [`Error::NoKeyExists`] - origin does not have an MSA
* [`Error::ExceedsMaxProviderNameSize`] - Too long of a provider name
* [`Error::DuplicateProviderRegistryEntry`] - a ProviderRegistryEntry associated with the given MSA id already exists.

##### Attributes
| Name | Type |
| -------- | -------- | 
| provider_name | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'Msa', 'create_provider', {'provider_name': 'Bytes'}
)
```

---------
#### grant_delegation
Creates a new Delegation for an existing MSA, with `origin` as the Provider and `delegator_key` is the delegator.
Since it is being sent on the Delegator&\#x27;s behalf, it requires the Delegator to authorize the new Delegation.

\# Remarks
* Origin MUST be the provider
* Signatures should be over the [`AddProvider`] struct

\# Events
* [`Event::DelegationGranted`]

\# Errors
* [`Error::AddProviderSignatureVerificationFailed`] - `origin`&\#x27;s MSA ID does not equal `add_provider_payload.authorized_msa_id`.
* [`Error::DuplicateProvider`] - there is already a Delegation for `origin` MSA and `delegator_key` MSA.
* [`Error::UnauthorizedProvider`] - `add_provider_payload.authorized_msa_id`  does not match MSA ID of `delegator_key`.
* [`Error::InvalidSelfProvider`] - Cannot delegate to the same MSA
* [`Error::InvalidSignature`] - `proof` verification fails; `delegator_key` must have signed `add_provider_payload`
* [`Error::NoKeyExists`] - there is no MSA for `origin` or `delegator_key`.
* [`Error::ProviderNotRegistered`] - the a non-provider MSA is used as the provider
* [`Error::UnauthorizedDelegator`] - Origin attempted to add a delegate for someone else&\#x27;s MSA

##### Attributes
| Name | Type |
| -------- | -------- | 
| delegator_key | `T::AccountId` | 
| proof | `MultiSignature` | 
| add_provider_payload | `AddProvider` | 

##### Python
```python
call = substrate.compose_call(
    'Msa', 'grant_delegation', {
    'add_provider_payload': {
        'authorized_msa_id': 'u64',
        'expiration': 'u32',
        'schema_ids': ['u16'],
    },
    'delegator_key': 'AccountId',
    'proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
#### revoke_delegation_by_delegator
Delegator (Origin) MSA terminates a delegation relationship with the `Provider` MSA. Deposits event[`DelegationRevoked`](Event::DelegationRevoked).

\# Events
* [`Event::DelegationRevoked`]

\# Errors

* [`Error::NoKeyExists`] - origin does not have an MSA
* [`Error::DelegationRevoked`] - the delegation has already been revoked.
* [`Error::DelegationNotFound`] - there is not delegation relationship between Origin and Delegator or Origin and Delegator are the same.

##### Attributes
| Name | Type |
| -------- | -------- | 
| provider_msa_id | `MessageSourceId` | 

##### Python
```python
call = substrate.compose_call(
    'Msa', 'revoke_delegation_by_delegator', {'provider_msa_id': 'u64'}
)
```

---------
#### add_public_key_to_msa
Adds a given `new_key` to `msa_id` of the account signing `msa_owner_proof`, which must match the MSA in `add_key_payload`.
The `new_key` must sign the `add_key_payload` to authorize the addition.

\# Remarks
* Origin can be same as msa owner.
* Signatures should be over the [`AddKeyData`] struct

\# Events
* [`Event::PublicKeyAdded`]

\# Errors

* [`Error::MsaOwnershipInvalidSignature`] - `key` is not a valid signer of the provided `add_key_payload`.
* [`Error::NewKeyOwnershipInvalidSignature`] - `key` is not a valid signer of the provided `add_key_payload`.
* [`Error::NoKeyExists`] - the MSA id for the account in `add_key_payload` does not exist.
* [`Error::NotMsaOwner`] - Origin&\#x27;s MSA is not the same as &\#x27;add_key_payload` MSA. Essentially you can only add a key to your own MSA.
* [`Error::ProofHasExpired`] - the current block is less than the `expired` bock number set in `AddKeyData`.
* [`Error::ProofNotYetValid`] - the `expired` block number set in `AddKeyData` is greater than the current block number plus mortality_block_limit().
* [`Error::SignatureAlreadySubmitted`] - signature has already been used.

##### Attributes
| Name | Type |
| -------- | -------- | 
| msa_owner_public_key | `T::AccountId` | 
| msa_owner_proof | `MultiSignature` | 
| new_key_owner_proof | `MultiSignature` | 
| add_key_payload | `AddKeyData<T>` | 

##### Python
```python
call = substrate.compose_call(
    'Msa', 'add_public_key_to_msa', {
    'add_key_payload': {
        'expiration': 'u32',
        'msa_id': 'u64',
        'new_public_key': 'AccountId',
    },
    'msa_owner_proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
    'msa_owner_public_key': 'AccountId',
    'new_key_owner_proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
#### delete_msa_public_key
Remove a key associated with an MSA by expiring it at the current block.

\# Remarks
* Removal of key deletes the association of the key with the MSA.
* The key can be re-added to same or another MSA if needed.

\# Events
* [`Event::PublicKeyDeleted`]

\# Errors
* [`Error::InvalidSelfRemoval`] - `origin` and `key` are the same.
* [`Error::NotKeyOwner`] - `origin` does not own the MSA ID associated with `key`.
* [`Error::NoKeyExists`] - `origin` or `key` are not associated with `origin`&\#x27;s MSA ID.

##### Attributes
| Name | Type |
| -------- | -------- | 
| public_key_to_delete | `T::AccountId` | 

##### Python
```python
call = substrate.compose_call(
    'Msa', 'delete_msa_public_key', {'public_key_to_delete': 'AccountId'}
)
```

---------
#### revoke_delegation_by_provider
Provider MSA terminates Delegation with a Delegator MSA by expiring the Delegation at the current block.

\# Events
* [`Event::DelegationRevoked`]

\# Errors

* [`Error::NoKeyExists`] - `provider_key` does not have an MSA key.
* [`Error::DelegationRevoked`] - delegation is already revoked
* [`Error::DelegationNotFound`] - no Delegation found between origin MSA and delegator MSA.

##### Attributes
| Name | Type |
| -------- | -------- | 
| delegator | `MessageSourceId` | 

##### Python
```python
call = substrate.compose_call(
    'Msa', 'revoke_delegation_by_provider', {'delegator': 'u64'}
)
```

---------
#### grant_schema_permissions
Grants a list of schema permissions to a provider. Schemas that have already
been granted are ignored. Schemas that are revoked are re-granted.

\# Events
* [`Event::DelegationUpdated`]

\# Errors
* [`Error::NoKeyExists`] no MSA for `origin`.
* [`Error::DelegationNotFound`] no delegation relationship between Origin and Delegator or Origin and Delegator are the same.
* [`Error::ExceedsMaxSchemaGrantsPerDelegation`] the limit of maximum allowed grants per delegation relationship has been exceeded.

##### Attributes
| Name | Type |
| -------- | -------- | 
| provider_msa_id | `MessageSourceId` | 
| schema_ids | `Vec<SchemaId>` | 

##### Python
```python
call = substrate.compose_call(
    'Msa', 'grant_schema_permissions', {
    'provider_msa_id': 'u64',
    'schema_ids': ['u16'],
}
)
```

---------
#### revoke_schema_permissions
Revokes a list of schema permissions to a provider. Attempting to revoke a Schemas that have already
been revoked are ignored.

\# Events
- [DelegationUpdated](Event::DelegationUpdated)

\# Errors
- [`NoKeyExists`](Error::NoKeyExists) - If there is not MSA for `origin`.
- [`DelegationNotFound`](Error::DelegationNotFound) - If there is not delegation relationship between Origin and Delegator or Origin and Delegator are the same.
- [`SchemaNotGranted`](Error::SchemaNotGranted) - If attempting to revoke a schema that has not previously been granted.

##### Attributes
| Name | Type |
| -------- | -------- | 
| provider_msa_id | `MessageSourceId` | 
| schema_ids | `Vec<SchemaId>` | 

##### Python
```python
call = substrate.compose_call(
    'Msa', 'revoke_schema_permissions', {
    'provider_msa_id': 'u64',
    'schema_ids': ['u16'],
}
)
```

---------
#### retire_msa
Retires an MSA

When a user wants to disassociate themselves from Frequency, they can retire their MSA for free provided that:
 (1) They own the MSA
 (2) There is only one account key
 (3) The MSA is not a registered provider.

This does not currently remove any messages related to the MSA.

\# Events
* [`Event::PublicKeyDeleted`]
* [`Event::MsaRetired`]

\# Errors
* [`Error::NoKeyExists`] - `delegator` does not have an MSA key.

##### Attributes
No attributes

##### Python
```python
call = substrate.compose_call(
    'Msa', 'retire_msa', {}
)
```

---------
### Events
---------
#### MsaCreated
A new Message Service Account was created with a new MessageSourceId
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```
| key | `T::AccountId` | ```AccountId```

---------
#### PublicKeyAdded
An AccountId has been associated with a MessageSourceId
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```
| key | `T::AccountId` | ```AccountId```

---------
#### PublicKeyDeleted
An AccountId had all permissions revoked from its MessageSourceId
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| key | `T::AccountId` | ```AccountId```

---------
#### DelegationGranted
A delegation relationship was added with the given provider and delegator
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| provider_id | `ProviderId` | ```u64```
| delegator_id | `DelegatorId` | ```u64```

---------
#### ProviderCreated
A Provider-MSA relationship was registered
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| provider_id | `ProviderId` | ```u64```

---------
#### DelegationRevoked
The Delegator revoked its delegation to the Provider
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| provider_id | `ProviderId` | ```u64```
| delegator_id | `DelegatorId` | ```u64```

---------
#### MsaRetired
The MSA has been retired.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```

---------
#### DelegationUpdated
A an update to the delegation occurred (ex. schema permissions where updated).
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| provider_id | `ProviderId` | ```u64```
| delegator_id | `DelegatorId` | ```u64```

---------
### Storage functions
---------
#### CurrentMsaIdentifierMaximum
 Storage type for the current MSA identifier maximum.
 We need to track this value because the identifier maximum
 is incremented each time a new identifier is created.
 - Value: The current maximum MSA Id

##### Python
```python
result = substrate.query(
    'Msa', 'CurrentMsaIdentifierMaximum', []
)
```

##### Return value
```python
'u64'
```
---------
#### DelegatorAndProviderToDelegation
 Storage type for mapping the relationship between a Delegator and its Provider.
 - Keys: Delegator MSA, Provider MSA
 - Value: [`Delegation`](common_primitives::msa::Delegation)

##### Python
```python
result = substrate.query(
    'Msa', 'DelegatorAndProviderToDelegation', ['u64', 'u64']
)
```

##### Return value
```python
{'revoked_at': 'u32', 'schema_permissions': 'scale_info::240'}
```
---------
#### ProviderToRegistryEntry
 Provider registration information
 - Key: Provider MSA Id
 - Value: [`ProviderRegistryEntry`](common_primitives::msa::ProviderRegistryEntry)

##### Python
```python
result = substrate.query(
    'Msa', 'ProviderToRegistryEntry', ['u64']
)
```

##### Return value
```python
{'provider_name': 'Bytes'}
```
---------
#### PublicKeyToMsaId
 Storage type for key to MSA information
 - Key: AccountId
 - Value: [`MessageSourceId`]

##### Python
```python
result = substrate.query(
    'Msa', 'PublicKeyToMsaId', ['AccountId']
)
```

##### Return value
```python
'u64'
```
---------
#### PublicKeyCountForMsaId
 Storage type for a reference counter of the number of keys associated to an MSA
 - Key: MSA Id
 - Value: [`u8`] Counter of Keys associated with the MSA

##### Python
```python
result = substrate.query(
    'Msa', 'PublicKeyCountForMsaId', ['u64']
)
```

##### Return value
```python
'u8'
```
---------
#### PayloadSignatureRegistry
 PayloadSignatureRegistry is used to prevent replay attacks for extrinsics
 that take an externally-signed payload.
 For this to work, the payload must include a mortality block number, which
 is used in lieu of a monotonically increasing nonce.

##### Python
```python
result = substrate.query(
    'Msa', 'PayloadSignatureRegistry', [
    'u32',
    {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
]
)
```

##### Return value
```python
'u32'
```
---------
### Constants
---------
#### MaxPublicKeysPerMsa
 Maximum count of keys allowed per MSA
##### Value
```python
25
```
##### Python
```python
constant = substrate.get_constant('Msa', 'MaxPublicKeysPerMsa')
```
---------
#### MaxSchemaGrantsPerDelegation
 Maximum count of schemas granted for publishing data per Provider
##### Value
```python
30
```
##### Python
```python
constant = substrate.get_constant('Msa', 'MaxSchemaGrantsPerDelegation')
```
---------
#### MaxProviderNameSize
 Maximum provider name size allowed per MSA association
##### Value
```python
16
```
##### Python
```python
constant = substrate.get_constant('Msa', 'MaxProviderNameSize')
```
---------
#### MortalityWindowSize
 The number of blocks per virtual &quot;bucket&quot; in the PayloadSignatureRegistry
 Virtual buckets are the first part of the double key in the PayloadSignatureRegistry
 StorageDoubleMap.  This permits a key grouping that enables mass removal
 of stale signatures which are no longer at risk of replay.
##### Value
```python
100
```
##### Python
```python
constant = substrate.get_constant('Msa', 'MortalityWindowSize')
```
---------
#### MaxSignaturesPerBucket
 The maximum number of signatures that can be assigned to a virtual bucket. In other
 words, no more than this many signatures can be assigned a specific first-key value.
##### Value
```python
50000
```
##### Python
```python
constant = substrate.get_constant('Msa', 'MaxSignaturesPerBucket')
```
---------
#### NumberOfBuckets
 The total number of virtual buckets
 There are exactly NumberOfBuckets first-key values in PayloadSignatureRegistry.
##### Value
```python
2
```
##### Python
```python
constant = substrate.get_constant('Msa', 'NumberOfBuckets')
```
---------
### Errors
---------
#### KeyAlreadyRegistered
Tried to add a key that was already registered to an MSA

---------
#### MsaIdOverflow
MsaId values have reached the maximum

---------
#### MsaOwnershipInvalidSignature
Cryptographic signature verification failed for adding a key to MSA

---------
#### NotMsaOwner
Ony the MSA Owner may perform the operation

---------
#### InvalidSignature
Cryptographic signature failed verification

---------
#### NotKeyOwner
Only the KeyOwner may perform the operation

---------
#### NoKeyExists
An operation was attempted with an unknown Key

---------
#### KeyLimitExceeded
The number of key values has reached its maximum

---------
#### InvalidSelfRemoval
A transaction&\#x27;s Origin (AccountId) may not remove itself

---------
#### InvalidSelfProvider
An MSA may not be its own delegate

---------
#### InvalidSchemaId
An invalid schema Id was provided

---------
#### DuplicateProvider
The delegation relationship already exists for the given MSA Ids

---------
#### AddProviderSignatureVerificationFailed
Cryptographic signature verification failed for adding the Provider as delegate

---------
#### UnauthorizedDelegator
Origin attempted to add a delegate for someone else&\#x27;s MSA

---------
#### UnauthorizedProvider
Origin attempted to add a different delegate than what was in the payload

---------
#### DelegationRevoked
The operation was attempted with a revoked delegation

---------
#### DelegationNotFound
The operation was attempted with an unknown delegation

---------
#### DuplicateProviderRegistryEntry
The MSA id submitted for provider creation has already been associated with a provider

---------
#### ExceedsMaxProviderNameSize
The maximum length for a provider name has been exceeded

---------
#### ExceedsMaxSchemaGrantsPerDelegation
The maximum number of schema grants has been exceeded

---------
#### SchemaNotGranted
Provider is not permitted to publish for given schema_id

---------
#### ProviderNotRegistered
The operation was attempted with a non-provider MSA

---------
#### ProofHasExpired
The submitted proof has expired; the current block is less the expiration block

---------
#### ProofNotYetValid
The submitted proof expiration block is too far in the future

---------
#### SignatureAlreadySubmitted
Attempted to add a signature when the signature is already in the registry

---------
#### NewKeyOwnershipInvalidSignature
Cryptographic signature verification failed for proving ownership of new public-key.

---------
#### CannotPredictValidityPastCurrentBlock
Attempted to request validity of schema permission or delegation in the future.

---------

## Messages
---------
### Calls
---------
#### add_ipfs_message
Adds a message for a resource hosted on IPFS. The payload storage will
contain both a
[CID](https://docs.ipfs.io/concepts/content-addressing/\#identifier-formats)
as well as a 32-bit payload length.
The actual payload will be on IPFS

\# Events
* [`Event::MessagesStored`] - In the next block

\# Errors
* [`Error::ExceedsMaxMessagePayloadSizeBytes`] - Payload is too large
* [`Error::InvalidSchemaId`] - Schema not found
* [`Error::InvalidPayloadLocation`] - The schema is not an IPFS payload location
* [`Error::InvalidMessageSourceAccount`] - Origin must be from an MSA
* [`Error::TooManyMessagesInBlock`] - Block is full of messages already
* [`Error::TypeConversionOverflow`] - Failed to add the message to storage as it is very full

##### Attributes
| Name | Type |
| -------- | -------- | 
| schema_id | `SchemaId` | 
| cid | `Vec<u8>` | 
| payload_length | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'Messages', 'add_ipfs_message', {
    'cid': 'Bytes',
    'payload_length': 'u32',
    'schema_id': 'u16',
}
)
```

---------
#### add_onchain_message
Add an on-chain message for a given schema id.

\# Events
* [`Event::MessagesStored`] - In the next block

\# Errors
* [`Error::ExceedsMaxMessagePayloadSizeBytes`] - Payload is too large
* [`Error::InvalidSchemaId`] - Schema not found
* [`Error::InvalidPayloadLocation`] - The schema is not an IPFS payload location
* [`Error::InvalidMessageSourceAccount`] - Origin must be from an MSA
* [`Error::UnAuthorizedDelegate`] - Trying to add a message without a proper delegation between the origin and the on_behalf_of MSA
* [`Error::TooManyMessagesInBlock`] - Block is full of messages already
* [`Error::TypeConversionOverflow`] - Failed to add the message to storage as it is very full

##### Attributes
| Name | Type |
| -------- | -------- | 
| on_behalf_of | `Option<MessageSourceId>` | 
| schema_id | `SchemaId` | 
| payload | `Vec<u8>` | 

##### Python
```python
call = substrate.compose_call(
    'Messages', 'add_onchain_message', {
    'on_behalf_of': (None, 'u64'),
    'payload': 'Bytes',
    'schema_id': 'u16',
}
)
```

---------
### Events
---------
#### MessagesStored
Messages are stored for a specified schema id and block number
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| schema_id | `SchemaId` | ```u16```
| block_number | `T::BlockNumber` | ```u32```
| count | `u16` | ```u16```

---------
### Storage functions
---------
#### BlockMessages
 A temporary storage of messages, given a schema id, for a duration of block period.
 At the start of the next block this storage is cleared and moved into Messages storage.
 - Value: List of Messages

##### Python
```python
result = substrate.query(
    'Messages', 'BlockMessages', []
)
```

##### Return value
```python
[
    (
        {
            'index': 'u16',
            'msa_id': (None, 'u64'),
            'payload': 'Bytes',
            'provider_msa_id': 'u64',
        },
        'u16',
    ),
]
```
---------
#### Messages
 A permanent storage for messages mapped by block number and schema id.
 - Keys: BlockNumber, Schema Id
 - Value: List of Messages

##### Python
```python
result = substrate.query(
    'Messages', 'Messages', ['u32', 'u16']
)
```

##### Return value
```python
[
    {
        'index': 'u16',
        'msa_id': (None, 'u64'),
        'payload': 'Bytes',
        'provider_msa_id': 'u64',
    },
]
```
---------
### Constants
---------
#### MaxMessagesPerBlock
 The maximum number of messages in a block.
##### Value
```python
7000
```
##### Python
```python
constant = substrate.get_constant('Messages', 'MaxMessagesPerBlock')
```
---------
#### MaxMessagePayloadSizeBytes
 The maximum size of a message payload bytes.
##### Value
```python
51200
```
##### Python
```python
constant = substrate.get_constant('Messages', 'MaxMessagePayloadSizeBytes')
```
---------
### Errors
---------
#### TooManyMessagesInBlock
Too many messages are added to existing block

---------
#### ExceedsMaxMessagePayloadSizeBytes
Message payload size is too large

---------
#### TypeConversionOverflow
Type Conversion Overflow

---------
#### InvalidMessageSourceAccount
Invalid Message Source Account

---------
#### InvalidSchemaId
Invalid SchemaId or Schema not found

---------
#### UnAuthorizedDelegate
UnAuthorizedDelegate

---------
#### InvalidPayloadLocation
Invalid payload location

---------

## Schemas
---------
### Calls
---------
#### create_schema
Adds a given schema to storage. The schema in question must be of length
between the min and max model size allowed for schemas (see pallet
constants above). If the pallet&\#x27;s maximum schema limit has been
fulfilled by the time this extrinsic is called, a SchemaCountOverflow error
will be thrown.

\# Events
* [`Event::SchemaCreated`]

\# Errors
* [`Error::LessThanMinSchemaModelBytes`] - The schema&\#x27;s length is less than the minimum schema length
* [`Error::ExceedsMaxSchemaModelBytes`] - The schema&\#x27;s length is greater than the maximum schema length
* [`Error::InvalidSchema`] - Schema is malformed in some way
* [`Error::SchemaCountOverflow`] - The schema count has exceeded its bounds

##### Attributes
| Name | Type |
| -------- | -------- | 
| model | `BoundedVec<u8, T::SchemaModelMaxBytesBoundedVecLimit>` | 
| model_type | `ModelType` | 
| payload_location | `PayloadLocation` | 

##### Python
```python
call = substrate.compose_call(
    'Schemas', 'create_schema', {
    'model': 'Bytes',
    'model_type': (
        'AvroBinary',
        'Parquet',
    ),
    'payload_location': (
        'OnChain',
        'IPFS',
    ),
}
)
```

---------
#### set_max_schema_model_bytes
Root and Governance can set a new max value for Schema bytes.
Must be &lt;= the limit of the Schema BoundedVec used for registration.

\# Requires
* Root Origin

\# Events
* [`Event::SchemaMaxSizeChanged`]

\# Errors
* [`Error::ExceedsMaxSchemaModelBytes`] - Cannot set to above the hard coded maximum [`Config::SchemaModelMaxBytesBoundedVecLimit`]

##### Attributes
| Name | Type |
| -------- | -------- | 
| max_size | `u32` | 

##### Python
```python
call = substrate.compose_call(
    'Schemas', 'set_max_schema_model_bytes', {'max_size': 'u32'}
)
```

---------
### Events
---------
#### SchemaCreated
Emitted when a schema is registered. [who, schemas id]
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `SchemaId` | ```u16```

---------
#### SchemaMaxSizeChanged
Emitted when maximum size for schema model is changed.
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### Storage functions
---------
#### GovernanceSchemaModelMaxBytes
 Storage for the Governance managed max bytes for schema model
 Allows for altering the max bytes without a full chain upgrade
 - Value: Max Bytes

##### Python
```python
result = substrate.query(
    'Schemas', 'GovernanceSchemaModelMaxBytes', []
)
```

##### Return value
```python
'u32'
```
---------
#### CurrentSchemaIdentifierMaximum
 Storage type for current number of schemas
 Useful for retrieving latest schema id
 - Value: Last Schema Id

##### Python
```python
result = substrate.query(
    'Schemas', 'CurrentSchemaIdentifierMaximum', []
)
```

##### Return value
```python
'u16'
```
---------
#### Schemas
 Storage for message schema struct data
 - Key: Schema Id
 - Value: [`Schema`](Schema)

##### Python
```python
result = substrate.query(
    'Schemas', 'Schemas', ['u16']
)
```

##### Return value
```python
{
    'model': 'Bytes',
    'model_type': ('AvroBinary', 'Parquet'),
    'payload_location': ('OnChain', 'IPFS'),
}
```
---------
### Constants
---------
#### MinSchemaModelSizeBytes
 Minimum length of Schema model size in bytes
##### Value
```python
8
```
##### Python
```python
constant = substrate.get_constant('Schemas', 'MinSchemaModelSizeBytes')
```
---------
#### SchemaModelMaxBytesBoundedVecLimit
 Maximum length of a Schema model Bounded Vec
##### Value
```python
65500
```
##### Python
```python
constant = substrate.get_constant('Schemas', 'SchemaModelMaxBytesBoundedVecLimit')
```
---------
#### MaxSchemaRegistrations
 Maximum number of schemas that can be registered
##### Value
```python
65000
```
##### Python
```python
constant = substrate.get_constant('Schemas', 'MaxSchemaRegistrations')
```
---------
### Errors
---------
#### InvalidSchema
Schema is malformed

---------
#### ExceedsMaxSchemaModelBytes
The schema model exceeds the maximum length allowed

---------
#### LessThanMinSchemaModelBytes
The schema is less than the minimum length allowed

---------
#### SchemaCountOverflow
CurrentSchemaIdentifierMaximum was attempted to overflow max, means MaxSchemaRegistrations is too big

---------