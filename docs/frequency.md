# frequency
---------
| Properties |  |
| -------- | -------- |
| Spec name     | frequency     |
| Implementation name     | frequency     |
| Spec version     | 5     |
| SS58 Format     | 90     |
| Token symbol      | FRQCY     |
| Token decimals      | 8     |

## System
---------
### Calls
---------
#### fill_block
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
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispatch_info | `DispatchInfo` | ```{'weight': {'ref_time': 'u64'}, 'class': ('Normal', 'Operational', 'Mandatory'), 'pays_fee': ('Yes', 'No')}```

---------
#### ExtrinsicFailed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispatch_error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}```
| dispatch_info | `DispatchInfo` | ```{'weight': {'ref_time': 'u64'}, 'class': ('Normal', 'Operational', 'Mandatory'), 'pays_fee': ('Yes', 'No')}```

---------
#### CodeUpdated
##### Attributes
No attributes

---------
#### NewAccount
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
#### KilledAccount
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
#### Remarked
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| hash | `T::Hash` | ```[u8; 32]```

---------
### Storage functions
---------
#### Account

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
            None: None,
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
##### Value
```python
4096
```
##### Python
```python
constant = substrate.get_constant('System', 'BlockHashCount')
```
---------
#### DbWeight
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
    'spec_version': 5,
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

---------
#### SpecVersionNeedsToIncrease

---------
#### FailedToExtractRuntimeVersion

---------
#### NonDefaultComposite

---------
#### NonZeroRefCount

---------
#### CallFiltered

---------

## ParachainSystem
---------
### Calls
---------
#### set_validation_data
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
##### Attributes
No attributes

---------
#### ValidationFunctionApplied
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| relay_chain_block_num | `RelayChainBlockNumber` | ```u32```

---------
#### ValidationFunctionDiscarded
##### Attributes
No attributes

---------
#### UpgradeAuthorized
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| code_hash | `T::Hash` | ```[u8; 32]```

---------
#### DownwardMessagesReceived
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| count | `u32` | ```u32```

---------
#### DownwardMessagesProcessed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| weight_used | `Weight` | ```{'ref_time': 'u64'}```
| dmq_head | `relay_chain::Hash` | ```[u8; 32]```

---------
### Storage functions
---------
#### PendingValidationCode

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

---------
#### ProhibitedByPolkadot

---------
#### TooBig

---------
#### ValidationDataNotAvailable

---------
#### HostConfigurationNotAvailable

---------
#### NotScheduled

---------
#### NothingAuthorized

---------
#### Unauthorized

---------

## Timestamp
---------
### Calls
---------
#### set
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
    'weight': {'ref_time': 'u64'},
}
)
```

---------
#### set_key
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
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sudo_result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
#### KeyChanged
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_sudoer | `Option<T::AccountId>` | ```(None, 'AccountId')```

---------
#### SudoAsDone
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sudo_result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### Storage functions
---------
#### Key

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

---------

## Preimage
---------
### Calls
---------
#### note_preimage
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
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```[u8; 32]```

---------
#### Requested
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```[u8; 32]```

---------
#### Cleared
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```[u8; 32]```

---------
### Storage functions
---------
#### StatusFor

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

---------
#### AlreadyNoted

---------
#### NotAuthorized

---------
#### NotNoted

---------
#### Requested

---------
#### NotRequested

---------

## Democracy
---------
### Calls
---------
#### propose
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
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `PropIndex` | ```u32```
| deposit | `BalanceOf<T>` | ```u128```

---------
#### Tabled
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `PropIndex` | ```u32```
| deposit | `BalanceOf<T>` | ```u128```
| depositors | `Vec<T::AccountId>` | ```['AccountId']```

---------
#### ExternalTabled
##### Attributes
No attributes

---------
#### Started
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```
| threshold | `VoteThreshold` | ```('SuperMajorityApprove', 'SuperMajorityAgainst', 'SimpleMajority')```

---------
#### Passed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```

---------
#### NotPassed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```

---------
#### Cancelled
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```

---------
#### Executed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| ref_index | `ReferendumIndex` | ```u32```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
#### Delegated
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| target | `T::AccountId` | ```AccountId```

---------
#### Undelegated
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
#### Vetoed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| proposal_hash | `T::Hash` | ```[u8; 32]```
| until | `T::BlockNumber` | ```u32```

---------
#### PreimageNoted
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| who | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```

---------
#### PreimageUsed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| provider | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```

---------
#### PreimageInvalid
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| ref_index | `ReferendumIndex` | ```u32```

---------
#### PreimageMissing
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| ref_index | `ReferendumIndex` | ```u32```

---------
#### PreimageReaped
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| provider | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```
| reaper | `T::AccountId` | ```AccountId```

---------
#### Blacklisted
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```

---------
#### Voted
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| voter | `T::AccountId` | ```AccountId```
| ref_index | `ReferendumIndex` | ```u32```
| vote | `AccountVote<BalanceOf<T>>` | ```{'Standard': {'vote': {'aye': 'bool', 'conviction': ('None', 'Locked1x', 'Locked2x', 'Locked3x', 'Locked4x', 'Locked5x', 'Locked6x')}, 'balance': 'u128'}, 'Split': {'aye': 'u128', 'nay': 'u128'}}```

---------
#### Seconded
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| seconder | `T::AccountId` | ```AccountId```
| prop_index | `PropIndex` | ```u32```

---------
#### ProposalCanceled
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| prop_index | `PropIndex` | ```u32```

---------
### Storage functions
---------
#### PublicPropCount

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

---------
#### ProposalMissing

---------
#### AlreadyCanceled

---------
#### DuplicateProposal

---------
#### ProposalBlacklisted

---------
#### NotSimpleMajority

---------
#### InvalidHash

---------
#### NoProposal

---------
#### AlreadyVetoed

---------
#### DuplicatePreimage

---------
#### NotImminent

---------
#### TooEarly

---------
#### Imminent

---------
#### PreimageMissing

---------
#### ReferendumInvalid

---------
#### PreimageInvalid

---------
#### NoneWaiting

---------
#### NotVoter

---------
#### NoPermission

---------
#### AlreadyDelegating

---------
#### InsufficientFunds

---------
#### NotDelegating

---------
#### VotesExist

---------
#### InstantNotAllowed

---------
#### Nonsense

---------
#### WrongUpperBound

---------
#### MaxVotesReached

---------
#### TooManyProposals

---------
#### VotingPeriodLow

---------

## Scheduler
---------
### Calls
---------
#### schedule
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
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| when | `T::BlockNumber` | ```u32```
| index | `u32` | ```u32```

---------
#### Canceled
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| when | `T::BlockNumber` | ```u32```
| index | `u32` | ```u32```

---------
#### Dispatched
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<Vec<u8>>` | ```(None, 'Bytes')```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
#### CallLookupFailed
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
                'system': {'None': None, 'Root': None, 'Signed': 'AccountId'},
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
            'priority': 'u8',
        },
    ),
]
```
---------
#### Lookup

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

---------
#### NotFound

---------
#### TargetBlockNumberInPast

---------
#### RescheduleNoChange

---------

## Utility
---------
### Calls
---------
#### batch
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
### Events
---------
#### BatchInterrupted
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `u32` | ```u32```
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}```

---------
#### BatchCompleted
##### Attributes
No attributes

---------
#### BatchCompletedWithErrors
##### Attributes
No attributes

---------
#### ItemCompleted
##### Attributes
No attributes

---------
#### ItemFailed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}```

---------
#### DispatchedAs
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### Constants
---------
#### batched_calls_limit
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

---------

## Balances
---------
### Calls
---------
#### transfer
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
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| free_balance | `T::Balance` | ```u128```

---------
#### DustLost
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
#### Transfer
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
#### BalanceSet
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| free | `T::Balance` | ```u128```
| reserved | `T::Balance` | ```u128```

---------
#### Reserved
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
#### Unreserved
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
#### ReserveRepatriated
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```
| destination_status | `Status` | ```('Free', 'Reserved')```

---------
#### Deposit
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
#### Withdraw
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
#### Slashed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Storage functions
---------
#### TotalIssuance

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

---------
#### LiquidityRestrictions

---------
#### InsufficientBalance

---------
#### ExistentialDeposit

---------
#### KeepAlive

---------
#### ExistingVestingSchedule

---------
#### DeadAccount

---------
#### TooManyReserves

---------

## TransactionPayment
---------
### Events
---------
#### TransactionFeePaid
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
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| proposal_index | `ProposalIndex` | ```u32```
| proposal_hash | `T::Hash` | ```[u8; 32]```
| threshold | `MemberCount` | ```u32```

---------
#### Voted
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
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```

---------
#### Disapproved
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```

---------
#### Executed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
#### MemberExecuted
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
#### Closed
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

---------
#### DuplicateProposal

---------
#### ProposalMissing

---------
#### WrongIndex

---------
#### DuplicateVote

---------
#### AlreadyInitialized

---------
#### TooEarly

---------
#### TooManyProposals

---------
#### WrongProposalWeight

---------
#### WrongProposalLength

---------

## TechnicalCommittee
---------
### Calls
---------
#### set_members
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
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| proposal_index | `ProposalIndex` | ```u32```
| proposal_hash | `T::Hash` | ```[u8; 32]```
| threshold | `MemberCount` | ```u32```

---------
#### Voted
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
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```

---------
#### Disapproved
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```

---------
#### Executed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
#### MemberExecuted
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_hash | `T::Hash` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
#### Closed
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

---------
#### DuplicateProposal

---------
#### ProposalMissing

---------
#### WrongIndex

---------
#### DuplicateVote

---------
#### AlreadyInitialized

---------
#### TooEarly

---------
#### TooManyProposals

---------
#### WrongProposalWeight

---------
#### WrongProposalLength

---------

## Treasury
---------
### Calls
---------
#### propose_spend
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
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```

---------
#### Spending
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| budget_remaining | `BalanceOf<T, I>` | ```u128```

---------
#### Awarded
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```
| award | `BalanceOf<T, I>` | ```u128```
| account | `T::AccountId` | ```AccountId```

---------
#### Rejected
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| proposal_index | `ProposalIndex` | ```u32```
| slashed | `BalanceOf<T, I>` | ```u128```

---------
#### Burnt
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| burnt_funds | `BalanceOf<T, I>` | ```u128```

---------
#### Rollover
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| rollover_balance | `BalanceOf<T, I>` | ```u128```

---------
#### Deposit
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| value | `BalanceOf<T, I>` | ```u128```

---------
#### SpendApproved
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

---------
#### InvalidIndex

---------
#### TooManyApprovals

---------
#### InsufficientPermission

---------
#### ProposalNotApproved

---------

## Authorship
---------
### Calls
---------
#### set_uncles
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

---------
#### UnclesAlreadySet

---------
#### TooManyUncles

---------
#### GenesisUncle

---------
#### TooHighUncle

---------
#### UncleAlreadyIncluded

---------
#### OldUncle

---------

## CollatorSelection
---------
### Calls
---------
#### set_invulnerables
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

---------
#### TooFewCandidates

---------
#### Unknown

---------
#### Permission

---------
#### AlreadyCandidate

---------
#### NotCandidate

---------
#### TooManyInvulnerables

---------
#### AlreadyInvulnerable

---------
#### NoAssociatedValidatorId

---------
#### ValidatorNotRegistered

---------

## Session
---------
### Calls
---------
#### set_keys
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
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| session_index | `SessionIndex` | ```u32```

---------
### Storage functions
---------
#### Validators

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

---------
#### NoAssociatedValidatorId

---------
#### DuplicatedKey

---------
#### NoKeys

---------
#### NoAccount

---------

## Aura
---------
### Storage functions
---------
#### Authorities

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
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| vesting_schedule | `VestingScheduleOf<T>` | ```{'start': 'u32', 'period': 'u32', 'period_count': 'u32', 'per_period': 'u128'}```

---------
#### Claimed
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
#### VestingSchedulesUpdated
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

---------
### Storage functions
---------
#### VestingSchedules

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

---------
#### ZeroVestingPeriodCount

---------
#### InsufficientBalanceToLock

---------
#### TooManyVestingSchedules

---------
#### AmountLow

---------
#### MaxVestingSchedulesExceeded

---------

## Msa
---------
### Calls
---------
#### create
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
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```
| key | `T::AccountId` | ```AccountId```

---------
#### PublicKeyAdded
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```
| key | `T::AccountId` | ```AccountId```

---------
#### PublicKeyDeleted
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| key | `T::AccountId` | ```AccountId```

---------
#### DelegationGranted
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| provider_id | `ProviderId` | ```u64```
| delegator_id | `DelegatorId` | ```u64```

---------
#### ProviderCreated
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| provider_id | `ProviderId` | ```u64```

---------
#### DelegationRevoked
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| provider_id | `ProviderId` | ```u64```
| delegator_id | `DelegatorId` | ```u64```

---------
#### MsaRetired
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| msa_id | `MessageSourceId` | ```u64```

---------
#### DelegationUpdated
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| provider_id | `ProviderId` | ```u64```
| delegator_id | `DelegatorId` | ```u64```

---------
### Storage functions
---------
#### CurrentMsaIdentifierMaximum

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
#### PayloadSignatureBucketCount

##### Python
```python
result = substrate.query(
    'Msa', 'PayloadSignatureBucketCount', ['u32']
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
##### Value
```python
2
```
##### Python
```python
constant = substrate.get_constant('Msa', 'NumberOfBuckets')
```
---------
#### MaxSignaturesStored
##### Value
```python
100000
```
##### Python
```python
constant = substrate.get_constant('Msa', 'MaxSignaturesStored')
```
---------
### Errors
---------
#### KeyAlreadyRegistered

---------
#### MsaIdOverflow

---------
#### MsaOwnershipInvalidSignature

---------
#### NotMsaOwner

---------
#### InvalidSignature

---------
#### NotKeyOwner

---------
#### NoKeyExists

---------
#### KeyLimitExceeded

---------
#### InvalidSelfRemoval

---------
#### InvalidSelfProvider

---------
#### InvalidSchemaId

---------
#### DuplicateProvider

---------
#### AddProviderSignatureVerificationFailed

---------
#### UnauthorizedDelegator

---------
#### UnauthorizedProvider

---------
#### DelegationRevoked

---------
#### DelegationNotFound

---------
#### DuplicateProviderRegistryEntry

---------
#### ExceedsMaxProviderNameSize

---------
#### ExceedsMaxSchemaGrantsPerDelegation

---------
#### SchemaNotGranted

---------
#### ProviderNotRegistered

---------
#### ProofHasExpired

---------
#### ProofNotYetValid

---------
#### SignatureAlreadySubmitted

---------
#### NewKeyOwnershipInvalidSignature

---------
#### CannotPredictValidityPastCurrentBlock

---------
#### SignatureRegistryLimitExceeded

---------

## Messages
---------
### Calls
---------
#### add_ipfs_message
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
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| schema_id | `SchemaId` | ```u16```
| block_number | `T::BlockNumber` | ```u32```
| count | `u16` | ```u16```

---------
### Storage functions
---------
#### Messages

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
#### BlockMessageIndex

##### Python
```python
result = substrate.query(
    'Messages', 'BlockMessageIndex', []
)
```

##### Return value
```python
'u16'
```
---------
### Constants
---------
#### MaxMessagesPerBlock
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

---------
#### ExceedsMaxMessagePayloadSizeBytes

---------
#### TypeConversionOverflow

---------
#### InvalidMessageSourceAccount

---------
#### InvalidSchemaId

---------
#### UnAuthorizedDelegate

---------
#### InvalidPayloadLocation

---------

## Schemas
---------
### Calls
---------
#### create_schema
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
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `SchemaId` | ```u16```

---------
#### SchemaMaxSizeChanged
##### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### Storage functions
---------
#### GovernanceSchemaModelMaxBytes

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

---------
#### ExceedsMaxSchemaModelBytes

---------
#### LessThanMinSchemaModelBytes

---------
#### SchemaCountOverflow

---------