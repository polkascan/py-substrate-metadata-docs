
# System

---------
## Calls

---------
### kill_prefix
Kill all storage items with a key that starts with the given prefix.

**NOTE:** We rely on the Root origin to provide us the number of subkeys under
the prefix we are removing to accurately calculate the weight of this function.
#### Attributes
| Name | Type |
| -------- | -------- | 
| prefix | `Key` | 
| subkeys | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'kill_prefix', {'prefix': 'Bytes', 'subkeys': 'u32'}
)
```

---------
### kill_storage
Kill some items from storage.
#### Attributes
| Name | Type |
| -------- | -------- | 
| keys | `Vec<Key>` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'kill_storage', {'keys': ['Bytes']}
)
```

---------
### remark
Make some on-chain remark.

\#\# Complexity
- `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| remark | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'remark', {'remark': 'Bytes'}
)
```

---------
### remark_with_event
Make some on-chain remark and emit event.
#### Attributes
| Name | Type |
| -------- | -------- | 
| remark | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'remark_with_event', {'remark': 'Bytes'}
)
```

---------
### set_code
Set the new runtime code.

\#\# Complexity
- `O(C + S)` where `C` length of `code` and `S` complexity of `can_set_code`
#### Attributes
| Name | Type |
| -------- | -------- | 
| code | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'set_code', {'code': 'Bytes'}
)
```

---------
### set_code_without_checks
Set the new runtime code without doing any checks of the given `code`.

\#\# Complexity
- `O(C)` where `C` length of `code`
#### Attributes
| Name | Type |
| -------- | -------- | 
| code | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'set_code_without_checks', {'code': 'Bytes'}
)
```

---------
### set_heap_pages
Set the number of pages in the WebAssembly environment&\#x27;s heap.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pages | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'set_heap_pages', {'pages': 'u64'}
)
```

---------
### set_storage
Set some items of storage.
#### Attributes
| Name | Type |
| -------- | -------- | 
| items | `Vec<KeyValue>` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'set_storage', {'items': [('Bytes', 'Bytes')]}
)
```

---------
## Events

---------
### CodeUpdated
`:code` was updated.
#### Attributes
No attributes

---------
### ExtrinsicFailed
An extrinsic failed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispatch_error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```
| dispatch_info | `DispatchInfo` | ```{'weight': {'ref_time': 'u64', 'proof_size': 'u64'}, 'class': ('Normal', 'Operational', 'Mandatory'), 'pays_fee': ('Yes', 'No')}```

---------
### ExtrinsicSuccess
An extrinsic completed successfully.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispatch_info | `DispatchInfo` | ```{'weight': {'ref_time': 'u64', 'proof_size': 'u64'}, 'class': ('Normal', 'Operational', 'Mandatory'), 'pays_fee': ('Yes', 'No')}```

---------
### KilledAccount
An account was reaped.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
### NewAccount
A new account was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
### Remarked
On on-chain remark happened.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| hash | `T::Hash` | ```scale_info::10```

---------
## Storage functions

---------
### Account
 The full account information for a particular account ID.

#### Python
```python
result = substrate.query(
    'System', 'Account', ['AccountId']
)
```

#### Return value
```python
{
    'consumers': 'u32',
    'data': {
        'fee_frozen': 'u64',
        'free': 'u64',
        'misc_frozen': 'u64',
        'reserved': 'u64',
    },
    'nonce': 'u32',
    'providers': 'u32',
    'sufficients': 'u32',
}
```
---------
### AllExtrinsicsLen
 Total length (in bytes) for all extrinsics put together, for the current block.

#### Python
```python
result = substrate.query(
    'System', 'AllExtrinsicsLen', []
)
```

#### Return value
```python
'u32'
```
---------
### BlockHash
 Map of block numbers to block hashes.

#### Python
```python
result = substrate.query(
    'System', 'BlockHash', ['u32']
)
```

#### Return value
```python
'scale_info::10'
```
---------
### BlockWeight
 The current weight for the block.

#### Python
```python
result = substrate.query(
    'System', 'BlockWeight', []
)
```

#### Return value
```python
{
    'mandatory': {'proof_size': 'u64', 'ref_time': 'u64'},
    'normal': {'proof_size': 'u64', 'ref_time': 'u64'},
    'operational': {'proof_size': 'u64', 'ref_time': 'u64'},
}
```
---------
### Digest
 Digest of the current block, also part of the block header.

#### Python
```python
result = substrate.query(
    'System', 'Digest', []
)
```

#### Return value
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
### EventCount
 The number of events in the `Events&lt;T&gt;` list.

#### Python
```python
result = substrate.query(
    'System', 'EventCount', []
)
```

#### Return value
```python
'u32'
```
---------
### EventTopics
 Mapping between a topic (represented by T::Hash) and a vector of indexes
 of events in the `&lt;Events&lt;T&gt;&gt;` list.

 All topic vectors have deterministic storage locations depending on the topic. This
 allows light-clients to leverage the changes trie storage tracking mechanism and
 in case of changes fetch the list of events of interest.

 The value has the type `(T::BlockNumber, EventIndex)` because if we used only just
 the `EventIndex` then in case if the topic has the same contents on the next block
 no notification will be triggered thus the event might be lost.

#### Python
```python
result = substrate.query(
    'System', 'EventTopics', ['scale_info::10']
)
```

#### Return value
```python
[('u32', 'u32')]
```
---------
### Events
 Events deposited for the current block.

 NOTE: The item is unbound and should therefore never be read on chain.
 It could otherwise inflate the PoV size of a block.

 Events have a large in-memory size. Box the events to not go out-of-memory
 just in case someone still reads them from within the runtime.

#### Python
```python
result = substrate.query(
    'System', 'Events', []
)
```

#### Return value
```python
[
    {
        'event': {
            'AdminUtils': (),
            'Balances': {
                'BalanceSet': {
                    'free': 'u64',
                    'reserved': 'u64',
                    'who': 'AccountId',
                },
                'Deposit': {'amount': 'u64', 'who': 'AccountId'},
                'DustLost': {'account': 'AccountId', 'amount': 'u64'},
                'Endowed': {'account': 'AccountId', 'free_balance': 'u64'},
                'ReserveRepatriated': {
                    'amount': 'u64',
                    'destination_status': 'scale_info::34',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Reserved': {'amount': 'u64', 'who': 'AccountId'},
                'Slashed': {'amount': 'u64', 'who': 'AccountId'},
                'Transfer': {
                    'amount': 'u64',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unreserved': {'amount': 'u64', 'who': 'AccountId'},
                'Withdraw': {'amount': 'u64', 'who': 'AccountId'},
            },
            'Commitments': {
                'Commitment': {'netuid': 'u16', 'who': 'AccountId'},
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::48',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::48',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::38',
                    'timepoint': 'scale_info::48',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'SenateMembers': (
                'MemberAdded',
                'MemberRemoved',
                'MembersSwapped',
                'MembersReset',
                'KeyChanged',
                'Dummy',
            ),
            'SubtensorModule': {
                'ActivityCutoffSet': ('u16', 'u16'),
                'AdjustmentAlphaSet': ('u16', 'u64'),
                'AdjustmentIntervalSet': ('u16', 'u16'),
                'AxonServed': ('u16', 'AccountId'),
                'BondsMovingAverageSet': ('u16', 'u64'),
                'BulkBalancesSet': ('u16', 'u16'),
                'BulkNeuronsRegistered': ('u16', 'u16'),
                'BurnSet': ('u16', 'u64'),
                'DefaultTakeSet': 'u16',
                'DelegateAdded': ('AccountId', 'AccountId', 'u16'),
                'DifficultySet': ('u16', 'u64'),
                'EmissionValuesSet': None,
                'Faucet': ('AccountId', 'u64'),
                'HotkeySwapped': {
                    'coldkey': 'AccountId',
                    'new_hotkey': 'AccountId',
                    'old_hotkey': 'AccountId',
                },
                'ImmunityPeriodSet': ('u16', 'u16'),
                'KappaSet': ('u16', 'u16'),
                'MaxAllowedUidsSet': ('u16', 'u16'),
                'MaxAllowedValidatorsSet': ('u16', 'u16'),
                'MaxBurnSet': ('u16', 'u64'),
                'MaxDifficultySet': ('u16', 'u64'),
                'MaxRegistrationsPerBlockSet': ('u16', 'u16'),
                'MaxWeightLimitSet': ('u16', 'u16'),
                'MinAllowedWeightSet': ('u16', 'u16'),
                'MinBurnSet': ('u16', 'u64'),
                'MinDifficultySet': ('u16', 'u64'),
                'NetworkAdded': ('u16', 'u16'),
                'NetworkImmunityPeriodSet': 'u64',
                'NetworkLockCostReductionIntervalSet': 'u64',
                'NetworkMinLockCostSet': 'u64',
                'NetworkRateLimitSet': 'u64',
                'NetworkRemoved': 'u16',
                'NeuronRegistered': ('u16', 'u16', 'AccountId'),
                'PowRegistrationAllowed': ('u16', 'bool'),
                'PrometheusServed': ('u16', 'AccountId'),
                'RAORecycledForRegistrationSet': ('u16', 'u64'),
                'RegistrationAllowed': ('u16', 'bool'),
                'RegistrationPerIntervalSet': ('u16', 'u16'),
                'RhoSet': ('u16', 'u16'),
                'ScalingLawPowerSet': ('u16', 'u16'),
                'SenateRequiredStakePercentSet': 'u64',
                'ServingRateLimitSet': ('u16', 'u64'),
                'StakeAdded': ('AccountId', 'u64'),
                'StakeRemoved': ('AccountId', 'u64'),
                'SubnetLimitSet': 'u16',
                'SubnetOwnerCutSet': 'u16',
                'Sudid': {'Err': 'scale_info::23', 'Ok': ()},
                'TempoSet': ('u16', 'u16'),
                'TxRateLimitSet': 'u64',
                'ValidatorPruneLenSet': ('u16', 'u64'),
                'WeightsMinStake': 'u64',
                'WeightsSet': ('u16', 'u16'),
                'WeightsSetRateLimitSet': ('u16', 'u64'),
                'WeightsVersionKeySet': ('u16', 'u64'),
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
                'Remarked': {'hash': 'scale_info::10', 'sender': 'AccountId'},
            },
            'TriumvirateMembers': (
                'MemberAdded',
                'MemberRemoved',
                'MembersSwapped',
                'MembersReset',
                'KeyChanged',
                'Dummy',
            ),
            None: None,
            'Grandpa': {
                'NewAuthorities': {'authority_set': [('[u8; 32]', 'u64')]},
                'Paused': None,
                'Resumed': None,
            },
            'Preimage': {
                'Cleared': {'hash': 'scale_info::10'},
                'Noted': {'hash': 'scale_info::10'},
                'Requested': {'hash': 'scale_info::10'},
            },
            'Registry': {
                'IdentityDissolved': {'who': 'AccountId'},
                'IdentitySet': {'who': 'AccountId'},
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
            'TransactionPayment': {
                'TransactionFeePaid': {
                    'actual_fee': 'u64',
                    'tip': 'u64',
                    'who': 'AccountId',
                },
            },
            'Triumvirate': {
                'Approved': {'proposal_hash': 'scale_info::10'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': 'scale_info::10',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': 'scale_info::10'},
                'Executed': {
                    'proposal_hash': 'scale_info::10',
                    'result': 'scale_info::38',
                },
                'MemberExecuted': {
                    'proposal_hash': 'scale_info::10',
                    'result': 'scale_info::38',
                },
                'Proposed': {
                    'account': 'AccountId',
                    'proposal_hash': 'scale_info::10',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'Voted': {
                    'account': 'AccountId',
                    'no': 'u32',
                    'proposal_hash': 'scale_info::10',
                    'voted': 'bool',
                    'yes': 'u32',
                },
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::23',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::38'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::23'},
            },
        },
        'phase': {
            'ApplyExtrinsic': 'u32',
            'Finalization': None,
            'Initialization': None,
        },
        'topics': ['scale_info::10'],
    },
]
```
---------
### ExecutionPhase
 The execution phase of the block.

#### Python
```python
result = substrate.query(
    'System', 'ExecutionPhase', []
)
```

#### Return value
```python
{'ApplyExtrinsic': 'u32', 'Finalization': None, 'Initialization': None}
```
---------
### ExtrinsicCount
 Total extrinsics count for the current block.

#### Python
```python
result = substrate.query(
    'System', 'ExtrinsicCount', []
)
```

#### Return value
```python
'u32'
```
---------
### ExtrinsicData
 Extrinsics data for the current block (maps an extrinsic&#x27;s index to its data).

#### Python
```python
result = substrate.query(
    'System', 'ExtrinsicData', ['u32']
)
```

#### Return value
```python
'Bytes'
```
---------
### LastRuntimeUpgrade
 Stores the `spec_version` and `spec_name` of when the last runtime upgrade happened.

#### Python
```python
result = substrate.query(
    'System', 'LastRuntimeUpgrade', []
)
```

#### Return value
```python
{'spec_name': 'Str', 'spec_version': 'u32'}
```
---------
### Number
 The current block number being processed. Set by `execute_block`.

#### Python
```python
result = substrate.query(
    'System', 'Number', []
)
```

#### Return value
```python
'u32'
```
---------
### ParentHash
 Hash of the previous block.

#### Python
```python
result = substrate.query(
    'System', 'ParentHash', []
)
```

#### Return value
```python
'scale_info::10'
```
---------
### UpgradedToTripleRefCount
 True if we have upgraded so that AccountInfo contains three types of `RefCount`. False
 (default) if not.

#### Python
```python
result = substrate.query(
    'System', 'UpgradedToTripleRefCount', []
)
```

#### Return value
```python
'bool'
```
---------
### UpgradedToU32RefCount
 True if we have upgraded so that `type RefCount` is `u32`. False (default) if not.

#### Python
```python
result = substrate.query(
    'System', 'UpgradedToU32RefCount', []
)
```

#### Return value
```python
'bool'
```
---------
## Constants

---------
### BlockHashCount
 Maximum number of block number to block hash mappings to keep (oldest pruned first).
#### Value
```python
2400
```
#### Python
```python
constant = substrate.get_constant('System', 'BlockHashCount')
```
---------
### BlockLength
 The maximum length of a block (in bytes).
#### Value
```python
{'max': {'mandatory': 10485760, 'normal': 7864320, 'operational': 10485760}}
```
#### Python
```python
constant = substrate.get_constant('System', 'BlockLength')
```
---------
### BlockWeights
 Block &amp; extrinsics weights: base values and limits.
#### Value
```python
{
    'base_block': {'proof_size': 0, 'ref_time': 381015000},
    'max_block': {
        'proof_size': 18446744073709551615,
        'ref_time': 4000000000000,
    },
    'per_class': {
        'mandatory': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 99840000},
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 99840000},
            'max_extrinsic': {
                'proof_size': 11990383647911208550,
                'ref_time': 2599900160000,
            },
            'max_total': {
                'proof_size': 13835058055282163711,
                'ref_time': 3000000000000,
            },
            'reserved': {'proof_size': 0, 'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 99840000},
            'max_extrinsic': {
                'proof_size': 16602069666338596454,
                'ref_time': 3599900160000,
            },
            'max_total': {
                'proof_size': 18446744073709551615,
                'ref_time': 4000000000000,
            },
            'reserved': {
                'proof_size': 4611686018427387904,
                'ref_time': 1000000000000,
            },
        },
    },
}
```
#### Python
```python
constant = substrate.get_constant('System', 'BlockWeights')
```
---------
### DbWeight
 The weight of runtime database operations the runtime can invoke.
#### Value
```python
{'read': 25000000, 'write': 100000000}
```
#### Python
```python
constant = substrate.get_constant('System', 'DbWeight')
```
---------
### SS58Prefix
 The designated SS58 prefix of this chain.

 This replaces the &quot;ss58Format&quot; property declared in the chain spec. Reason is
 that the runtime should know about the prefix in order to make use of it as
 an identifier of the chain.
#### Value
```python
42
```
#### Python
```python
constant = substrate.get_constant('System', 'SS58Prefix')
```
---------
### Version
 Get the chain&#x27;s current version.
#### Value
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
        ('0x37c8bb1350a9a2a8', 3),
        ('0xf3ff14d5ab527059', 3),
        ('0x42e62be4a39e5b60', 1),
        ('0x806df4ccaa9ed485', 1),
        ('0x8375104b299b74c5', 1),
        ('0x5d1fbfbe852f2807', 1),
        ('0xc6886e2f8e598b0a', 1),
    ],
    'authoring_version': 1,
    'impl_name': 'node-subtensor',
    'impl_version': 1,
    'spec_name': 'node-subtensor',
    'spec_version': 144,
    'state_version': 1,
    'transaction_version': 1,
}
```
#### Python
```python
constant = substrate.get_constant('System', 'Version')
```
---------
## Errors

---------
### CallFiltered
The origin filter prevent the call to be dispatched.

---------
### FailedToExtractRuntimeVersion
Failed to extract the runtime version from the new runtime.

Either calling `Core_version` or decoding `RuntimeVersion` failed.

---------
### InvalidSpecName
The name of specification does not match between the current runtime
and the new runtime.

---------
### NonDefaultComposite
Suicide called when the account has non-default composite data.

---------
### NonZeroRefCount
There is a non-zero reference count preventing the account from being purged.

---------
### SpecVersionNeedsToIncrease
The specification version is not allowed to decrease between the current runtime
and the new runtime.

---------