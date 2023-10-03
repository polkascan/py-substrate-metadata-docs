
# Utility

---------
## Calls

---------
### batch
Dispatch multiple calls from the sender&\#x27;s origin.

This will execute until the first one fails and then stop.

May be called from root or a signed origin.

\# Parameters
- `calls`: The calls to be dispatched from the same origin.

\# Weight
- The sum of the weights of the `calls`.
- One event.

This will return `Ok` in all circumstances except an unsigned origin. To determine the success of the batch, an
event is deposited. If a call failed and the batch was interrupted, then the
`BatchInterrupted` event is deposited, along with the number of successful calls made
and the error of the failed call. If all were successful, then the `BatchCompleted`
event is deposited.
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'batch', {
    'calls': [
        {
            'Asset': 'Call',
            None: None,
            'Authorship': {
                'set_uncles': {
                    'new_uncles': [
                        {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                    ],
                },
            },
            'Babe': {
                'plan_config_change': {
                    'config': {
                        None: None,
                        'V1': {
                            'allowed_slots': 'scale_info::330',
                            'c': (
                                'u64',
                                'u64',
                            ),
                        },
                    },
                },
                'report_equivocation': {
                    'equivocation_proof': {
                        'first_header': {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                        'offender': '[u8; 32]',
                        'second_header': {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                        'slot': 'u64',
                    },
                    'key_owner_proof': {
                        'session': 'u32',
                        'trie_nodes': [
                            'Bytes',
                        ],
                        'validator_count': 'u32',
                    },
                },
                'report_equivocation_unsigned': {
                    'equivocation_proof': {
                        'first_header': {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                        'offender': '[u8; 32]',
                        'second_header': {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                        'slot': 'u64',
                    },
                    'key_owner_proof': {
                        'session': 'u32',
                        'trie_nodes': [
                            'Bytes',
                        ],
                        'validator_count': 'u32',
                    },
                },
            },
            'Balances': 'Call',
            'Base': 'Call',
            'Bridge': 'Call',
            'CapitalDistribution': {
                'claim': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                },
                'distribute': {
                    'amount': 'u128',
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'currency': '[u8; 12]',
                    'expires_at': (
                        None,
                        'u64',
                    ),
                    'payment_at': 'u64',
                    'per_share': 'u128',
                    'portfolio': (
                        None,
                        'u64',
                    ),
                },
                'push_benefit': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'holder': '[u8; 32]',
                },
                'reclaim': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                },
                'remove_distribution': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                },
            },
            'CddServiceProviders': 'Call',
            'Checkpoint': {
                'create_checkpoint': {
                    'ticker': '[u8; 12]',
                },
                'create_schedule': {
                    'schedule': {
                        'period': {
                            'amount': 'u64',
                            'unit': 'scale_info::173',
                        },
                        'remaining': 'u32',
                        'start': (
                            None,
                            'u64',
                        ),
                    },
                    'ticker': '[u8; 12]',
                },
                'remove_schedule': {
                    'id': 'u64',
                    'ticker': '[u8; 12]',
                },
                'set_schedules_max_complexity': {
                    'max_complexity': 'u64',
                },
            },
            'CommitteeMembership': 'Call',
            'ComplianceManager': 'Call',
            'Contracts': {
                'call': {
                    'data': 'Bytes',
                    'dest': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                    'gas_limit': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'call_old_weight': {
                    'data': 'Bytes',
                    'dest': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                    'gas_limit': 'u64',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'instantiate': {
                    'code_hash': '[u8; 32]',
                    'data': 'Bytes',
                    'gas_limit': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                    'salt': 'Bytes',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'instantiate_old_weight': {
                    'code_hash': '[u8; 32]',
                    'data': 'Bytes',
                    'gas_limit': 'u64',
                    'salt': 'Bytes',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'instantiate_with_code': {
                    'code': 'Bytes',
                    'data': 'Bytes',
                    'gas_limit': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                    'salt': 'Bytes',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'instantiate_with_code_old_weight': {
                    'code': 'Bytes',
                    'data': 'Bytes',
                    'gas_limit': 'u64',
                    'salt': 'Bytes',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'remove_code': {
                    'code_hash': '[u8; 32]',
                },
                'set_code': {
                    'code_hash': '[u8; 32]',
                    'dest': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                },
                'upload_code': {
                    'code': 'Bytes',
                    'determinism': (
                        'Deterministic',
                        'AllowIndeterminism',
                    ),
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                },
            },
            'CorporateAction': 'Call',
            'CorporateBallot': {
                'attach_ballot': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'meta': {
                        'motions': [
                            'scale_info::206',
                        ],
                        'title': 'Bytes',
                    },
                    'range': {
                        'end': 'u64',
                        'start': 'u64',
                    },
                    'rcv': 'bool',
                },
                'change_end': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'end': 'u64',
                },
                'change_meta': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'meta': {
                        'motions': [
                            'scale_info::206',
                        ],
                        'title': 'Bytes',
                    },
                },
                'change_rcv': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'rcv': 'bool',
                },
                'remove_ballot': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                },
                'vote': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'votes': [
                        {
                            'fallback': (
                                None,
                                'u16',
                            ),
                            'power': 'u128',
                        },
                    ],
                },
            },
            'ExternalAgents': 'Call',
            'Grandpa': {
                'note_stalled': {
                    'best_finalized_block_number': 'u32',
                    'delay': 'u32',
                },
                'report_equivocation': {
                    'equivocation_proof': {
                        'equivocation': {
                            'Precommit': 'scale_info::476',
                            'Prevote': 'scale_info::471',
                        },
                        'set_id': 'u64',
                    },
                    'key_owner_proof': {
                        'session': 'u32',
                        'trie_nodes': [
                            'Bytes',
                        ],
                        'validator_count': 'u32',
                    },
                },
                'report_equivocation_unsigned': {
                    'equivocation_proof': {
                        'equivocation': {
                            'Precommit': 'scale_info::476',
                            'Prevote': 'scale_info::471',
                        },
                        'set_id': 'u64',
                    },
                    'key_owner_proof': {
                        'session': 'u32',
                        'trie_nodes': [
                            'Bytes',
                        ],
                        'validator_count': 'u32',
                    },
                },
            },
            'Identity': 'Call',
            'ImOnline': {
                'heartbeat': {
                    'heartbeat': {
                        'authority_index': 'u32',
                        'block_number': 'u32',
                        'network_state': {
                            'external_addresses': [
                                'Bytes',
                            ],
                            'peer_id': 'Bytes',
                        },
                        'session_index': 'u32',
                        'validators_len': 'u32',
                    },
                    'signature': '[u8; 64]',
                },
            },
            'Indices': {
                'claim': {
                    'index': 'u32',
                },
                'force_transfer': {
                    'freeze': 'bool',
                    'index': 'u32',
                    'new': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                },
                'free': {
                    'index': 'u32',
                },
                'freeze': {
                    'index': 'u32',
                },
                'transfer': {
                    'index': 'u32',
                    'new': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                },
            },
            'MultiSig': 'Call',
            'Nft': 'Call',
            'Pips': 'Call',
            'PolymeshCommittee': 'Call',
            'PolymeshContracts': 'Call',
            'Portfolio': 'Call',
            'Preimage': {
                'note_preimage': {
                    'bytes': 'Bytes',
                },
                'request_preimage': {
                    'hash': '[u8; 32]',
                },
                'unnote_preimage': {
                    'hash': '[u8; 32]',
                },
                'unrequest_preimage': {
                    'hash': '[u8; 32]',
                },
            },
            'ProtocolFee': 'Call',
            'Relayer': 'Call',
            'Rewards': 'Call',
            'Scheduler': {
                'cancel': {
                    'index': 'u32',
                    'when': 'u32',
                },
                'cancel_named': {
                    'id': '[u8; 32]',
                },
                'schedule': {
                    'call': {
                        'Asset': 'Call',
                        'Authorship': {
                            'set_uncles': 'InnerStruct',
                        },
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Base': 'Call',
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'CddServiceProviders': 'Call',
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'CommitteeMembership': 'Call',
                        'ComplianceManager': 'Call',
                        'Contracts': {
                            'call': 'InnerStruct',
                            'call_old_weight': 'InnerStruct',
                            'instantiate': 'InnerStruct',
                            'instantiate_old_weight': 'InnerStruct',
                            'instantiate_with_code': 'InnerStruct',
                            'instantiate_with_code_old_weight': 'InnerStruct',
                            'remove_code': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'upload_code': 'InnerStruct',
                        },
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'ImOnline': {
                            'heartbeat': 'InnerStruct',
                        },
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'MultiSig': 'Call',
                        'Nft': 'Call',
                        'Pips': 'Call',
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'ProtocolFee': 'Call',
                        'Relayer': 'Call',
                        'Rewards': 'Call',
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'Sudo': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
                            'placeholder_fill_block': None,
                            'remark': 'InnerStruct',
                            'remark_with_event': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'set_code_without_checks': 'InnerStruct',
                            'set_heap_pages': 'InnerStruct',
                            'set_storage': 'InnerStruct',
                        },
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        None: None,
                        'Utility': 'Call',
                    },
                    'maybe_periodic': (
                        None,
                        ('u32', 'u32'),
                    ),
                    'priority': 'u8',
                    'when': 'u32',
                },
                'schedule_after': {
                    'after': 'u32',
                    'call': {
                        None: None,
                        'Asset': 'Call',
                        'Authorship': {
                            'set_uncles': 'InnerStruct',
                        },
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Base': 'Call',
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'CddServiceProviders': 'Call',
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'CommitteeMembership': 'Call',
                        'ComplianceManager': 'Call',
                        'Contracts': {
                            'call': 'InnerStruct',
                            'call_old_weight': 'InnerStruct',
                            'instantiate': 'InnerStruct',
                            'instantiate_old_weight': 'InnerStruct',
                            'instantiate_with_code': 'InnerStruct',
                            'instantiate_with_code_old_weight': 'InnerStruct',
                            'remove_code': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'upload_code': 'InnerStruct',
                        },
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'ImOnline': {
                            'heartbeat': 'InnerStruct',
                        },
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'MultiSig': 'Call',
                        'Nft': 'Call',
                        'Pips': 'Call',
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'ProtocolFee': 'Call',
                        'Relayer': 'Call',
                        'Rewards': 'Call',
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'Sudo': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
                            'placeholder_fill_block': None,
                            'remark': 'InnerStruct',
                            'remark_with_event': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'set_code_without_checks': 'InnerStruct',
                            'set_heap_pages': 'InnerStruct',
                            'set_storage': 'InnerStruct',
                        },
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': 'Call',
                    },
                    'maybe_periodic': (
                        None,
                        ('u32', 'u32'),
                    ),
                    'priority': 'u8',
                },
                'schedule_named': {
                    'call': {
                        'Authorship': {
                            'set_uncles': 'InnerStruct',
                        },
                        None: None,
                        'Asset': 'Call',
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Base': 'Call',
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'CddServiceProviders': 'Call',
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'CommitteeMembership': 'Call',
                        'ComplianceManager': 'Call',
                        'Contracts': {
                            'call': 'InnerStruct',
                            'call_old_weight': 'InnerStruct',
                            'instantiate': 'InnerStruct',
                            'instantiate_old_weight': 'InnerStruct',
                            'instantiate_with_code': 'InnerStruct',
                            'instantiate_with_code_old_weight': 'InnerStruct',
                            'remove_code': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'upload_code': 'InnerStruct',
                        },
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'ImOnline': {
                            'heartbeat': 'InnerStruct',
                        },
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'MultiSig': 'Call',
                        'Nft': 'Call',
                        'Pips': 'Call',
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'ProtocolFee': 'Call',
                        'Relayer': 'Call',
                        'Rewards': 'Call',
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'Sudo': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
                            'placeholder_fill_block': None,
                            'remark': 'InnerStruct',
                            'remark_with_event': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'set_code_without_checks': 'InnerStruct',
                            'set_heap_pages': 'InnerStruct',
                            'set_storage': 'InnerStruct',
                        },
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': 'Call',
                    },
                    'id': '[u8; 32]',
                    'maybe_periodic': (
                        None,
                        ('u32', 'u32'),
                    ),
                    'priority': 'u8',
                    'when': 'u32',
                },
                'schedule_named_after': {
                    'after': 'u32',
                    'call': {
                        'Asset': 'Call',
                        'Authorship': {
                            'set_uncles': 'InnerStruct',
                        },
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Base': 'Call',
                        'CommitteeMembership': 'Call',
                        None: None,
                        'Balances': 'Call',
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'CddServiceProviders': 'Call',
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'ComplianceManager': 'Call',
                        'Contracts': {
                            'call': 'InnerStruct',
                            'call_old_weight': 'InnerStruct',
                            'instantiate': 'InnerStruct',
                            'instantiate_old_weight': 'InnerStruct',
                            'instantiate_with_code': 'InnerStruct',
                            'instantiate_with_code_old_weight': 'InnerStruct',
                            'remove_code': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'upload_code': 'InnerStruct',
                        },
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'ImOnline': {
                            'heartbeat': 'InnerStruct',
                        },
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'MultiSig': 'Call',
                        'Nft': 'Call',
                        'Pips': 'Call',
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'ProtocolFee': 'Call',
                        'Relayer': 'Call',
                        'Rewards': 'Call',
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'Sudo': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
                            'placeholder_fill_block': None,
                            'remark': 'InnerStruct',
                            'remark_with_event': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'set_code_without_checks': 'InnerStruct',
                            'set_heap_pages': 'InnerStruct',
                            'set_storage': 'InnerStruct',
                        },
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': 'Call',
                    },
                    'id': '[u8; 32]',
                    'maybe_periodic': (
                        None,
                        ('u32', 'u32'),
                    ),
                    'priority': 'u8',
                },
            },
            'Session': {
                'purge_keys': None,
                'set_keys': {
                    'keys': {
                        'authority_discovery': '[u8; 32]',
                        'babe': '[u8; 32]',
                        'grandpa': '[u8; 32]',
                        'im_online': '[u8; 32]',
                    },
                    'proof': 'Bytes',
                },
            },
            'Settlement': 'Call',
            'Staking': 'Call',
            'Statistics': 'Call',
            'Sto': 'Call',
            'Sudo': 'Call',
            'System': {
                'kill_prefix': {
                    'prefix': 'Bytes',
                    'subkeys': 'u32',
                },
                'kill_storage': {
                    'keys': ['Bytes'],
                },
                'placeholder_fill_block': None,
                'remark': {
                    'remark': 'Bytes',
                },
                'remark_with_event': {
                    'remark': 'Bytes',
                },
                'set_code': {
                    'code': 'Bytes',
                },
                'set_code_without_checks': {
                    'code': 'Bytes',
                },
                'set_heap_pages': {
                    'pages': 'u64',
                },
                'set_storage': {
                    'items': [
                        (
                            'Bytes',
                            'Bytes',
                        ),
                    ],
                },
            },
            'TechnicalCommittee': 'Call',
            'TechnicalCommitteeMembership': 'Call',
            'Timestamp': {
                'set': {'now': 'u64'},
            },
            'Treasury': 'Call',
            'UpgradeCommittee': 'Call',
            'UpgradeCommitteeMembership': 'Call',
            'Utility': 'Call',
        },
    ],
}
)
```

---------
### batch_atomic
Dispatch multiple calls from the sender&\#x27;s origin.

This will execute all calls, in order, stopping at the first failure,
in which case the state changes are rolled back.
On failure, an event `BatchInterrupted(failure_idx, error)` is deposited.

May be called from root or a signed origin.

\# Parameters
- `calls`: The calls to be dispatched from the same origin.

\# Weight
- The sum of the weights of the `calls`.
- One event.

This will return `Ok` in all circumstances except an unsigned origin.
To determine the success of the batch, an event is deposited.
If any call failed, then `BatchInterrupted` is deposited.
If all were successful, then the `BatchCompleted` event is deposited.
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'batch_atomic', {
    'calls': [
        {
            'Asset': 'Call',
            'Authorship': {
                'set_uncles': {
                    'new_uncles': [
                        {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                    ],
                },
            },
            None: None,
            'Babe': {
                'plan_config_change': {
                    'config': {
                        None: None,
                        'V1': {
                            'allowed_slots': 'scale_info::330',
                            'c': (
                                'u64',
                                'u64',
                            ),
                        },
                    },
                },
                'report_equivocation': {
                    'equivocation_proof': {
                        'first_header': {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                        'offender': '[u8; 32]',
                        'second_header': {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                        'slot': 'u64',
                    },
                    'key_owner_proof': {
                        'session': 'u32',
                        'trie_nodes': [
                            'Bytes',
                        ],
                        'validator_count': 'u32',
                    },
                },
                'report_equivocation_unsigned': {
                    'equivocation_proof': {
                        'first_header': {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                        'offender': '[u8; 32]',
                        'second_header': {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                        'slot': 'u64',
                    },
                    'key_owner_proof': {
                        'session': 'u32',
                        'trie_nodes': [
                            'Bytes',
                        ],
                        'validator_count': 'u32',
                    },
                },
            },
            'Balances': 'Call',
            'Base': 'Call',
            'Bridge': 'Call',
            'CapitalDistribution': {
                'claim': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                },
                'distribute': {
                    'amount': 'u128',
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'currency': '[u8; 12]',
                    'expires_at': (
                        None,
                        'u64',
                    ),
                    'payment_at': 'u64',
                    'per_share': 'u128',
                    'portfolio': (
                        None,
                        'u64',
                    ),
                },
                'push_benefit': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'holder': '[u8; 32]',
                },
                'reclaim': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                },
                'remove_distribution': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                },
            },
            'CddServiceProviders': 'Call',
            'Checkpoint': {
                'create_checkpoint': {
                    'ticker': '[u8; 12]',
                },
                'create_schedule': {
                    'schedule': {
                        'period': {
                            'amount': 'u64',
                            'unit': 'scale_info::173',
                        },
                        'remaining': 'u32',
                        'start': (
                            None,
                            'u64',
                        ),
                    },
                    'ticker': '[u8; 12]',
                },
                'remove_schedule': {
                    'id': 'u64',
                    'ticker': '[u8; 12]',
                },
                'set_schedules_max_complexity': {
                    'max_complexity': 'u64',
                },
            },
            'CommitteeMembership': 'Call',
            'ComplianceManager': 'Call',
            'Contracts': {
                'call': {
                    'data': 'Bytes',
                    'dest': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                    'gas_limit': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'call_old_weight': {
                    'data': 'Bytes',
                    'dest': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                    'gas_limit': 'u64',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'instantiate': {
                    'code_hash': '[u8; 32]',
                    'data': 'Bytes',
                    'gas_limit': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                    'salt': 'Bytes',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'instantiate_old_weight': {
                    'code_hash': '[u8; 32]',
                    'data': 'Bytes',
                    'gas_limit': 'u64',
                    'salt': 'Bytes',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'instantiate_with_code': {
                    'code': 'Bytes',
                    'data': 'Bytes',
                    'gas_limit': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                    'salt': 'Bytes',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'instantiate_with_code_old_weight': {
                    'code': 'Bytes',
                    'data': 'Bytes',
                    'gas_limit': 'u64',
                    'salt': 'Bytes',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'remove_code': {
                    'code_hash': '[u8; 32]',
                },
                'set_code': {
                    'code_hash': '[u8; 32]',
                    'dest': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                },
                'upload_code': {
                    'code': 'Bytes',
                    'determinism': (
                        'Deterministic',
                        'AllowIndeterminism',
                    ),
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                },
            },
            'CorporateAction': 'Call',
            'CorporateBallot': {
                'attach_ballot': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'meta': {
                        'motions': [
                            'scale_info::206',
                        ],
                        'title': 'Bytes',
                    },
                    'range': {
                        'end': 'u64',
                        'start': 'u64',
                    },
                    'rcv': 'bool',
                },
                'change_end': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'end': 'u64',
                },
                'change_meta': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'meta': {
                        'motions': [
                            'scale_info::206',
                        ],
                        'title': 'Bytes',
                    },
                },
                'change_rcv': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'rcv': 'bool',
                },
                'remove_ballot': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                },
                'vote': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'votes': [
                        {
                            'fallback': (
                                None,
                                'u16',
                            ),
                            'power': 'u128',
                        },
                    ],
                },
            },
            'ExternalAgents': 'Call',
            'Grandpa': {
                'note_stalled': {
                    'best_finalized_block_number': 'u32',
                    'delay': 'u32',
                },
                'report_equivocation': {
                    'equivocation_proof': {
                        'equivocation': {
                            'Precommit': 'scale_info::476',
                            'Prevote': 'scale_info::471',
                        },
                        'set_id': 'u64',
                    },
                    'key_owner_proof': {
                        'session': 'u32',
                        'trie_nodes': [
                            'Bytes',
                        ],
                        'validator_count': 'u32',
                    },
                },
                'report_equivocation_unsigned': {
                    'equivocation_proof': {
                        'equivocation': {
                            'Precommit': 'scale_info::476',
                            'Prevote': 'scale_info::471',
                        },
                        'set_id': 'u64',
                    },
                    'key_owner_proof': {
                        'session': 'u32',
                        'trie_nodes': [
                            'Bytes',
                        ],
                        'validator_count': 'u32',
                    },
                },
            },
            'Identity': 'Call',
            'ImOnline': {
                'heartbeat': {
                    'heartbeat': {
                        'authority_index': 'u32',
                        'block_number': 'u32',
                        'network_state': {
                            'external_addresses': [
                                'Bytes',
                            ],
                            'peer_id': 'Bytes',
                        },
                        'session_index': 'u32',
                        'validators_len': 'u32',
                    },
                    'signature': '[u8; 64]',
                },
            },
            'Indices': {
                'claim': {
                    'index': 'u32',
                },
                'force_transfer': {
                    'freeze': 'bool',
                    'index': 'u32',
                    'new': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                },
                'free': {
                    'index': 'u32',
                },
                'freeze': {
                    'index': 'u32',
                },
                'transfer': {
                    'index': 'u32',
                    'new': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                },
            },
            'MultiSig': 'Call',
            'Nft': 'Call',
            'Pips': 'Call',
            'PolymeshCommittee': 'Call',
            'PolymeshContracts': 'Call',
            'Portfolio': 'Call',
            'Preimage': {
                'note_preimage': {
                    'bytes': 'Bytes',
                },
                'request_preimage': {
                    'hash': '[u8; 32]',
                },
                'unnote_preimage': {
                    'hash': '[u8; 32]',
                },
                'unrequest_preimage': {
                    'hash': '[u8; 32]',
                },
            },
            'ProtocolFee': 'Call',
            'Relayer': 'Call',
            'Rewards': 'Call',
            'Scheduler': {
                'cancel': {
                    'index': 'u32',
                    'when': 'u32',
                },
                'cancel_named': {
                    'id': '[u8; 32]',
                },
                'schedule': {
                    'call': {
                        'Asset': 'Call',
                        'Authorship': {
                            'set_uncles': 'InnerStruct',
                        },
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Base': 'Call',
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'CddServiceProviders': 'Call',
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'CommitteeMembership': 'Call',
                        'ComplianceManager': 'Call',
                        'Contracts': {
                            'call': 'InnerStruct',
                            'call_old_weight': 'InnerStruct',
                            'instantiate': 'InnerStruct',
                            'instantiate_old_weight': 'InnerStruct',
                            'instantiate_with_code': 'InnerStruct',
                            'instantiate_with_code_old_weight': 'InnerStruct',
                            'remove_code': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'upload_code': 'InnerStruct',
                        },
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'ImOnline': {
                            'heartbeat': 'InnerStruct',
                        },
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'MultiSig': 'Call',
                        'Nft': 'Call',
                        'Pips': 'Call',
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'ProtocolFee': 'Call',
                        'Relayer': 'Call',
                        'Rewards': 'Call',
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'Sudo': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
                            'placeholder_fill_block': None,
                            'remark': 'InnerStruct',
                            'remark_with_event': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'set_code_without_checks': 'InnerStruct',
                            'set_heap_pages': 'InnerStruct',
                            'set_storage': 'InnerStruct',
                        },
                        'TechnicalCommittee': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        None: None,
                        'TechnicalCommitteeMembership': 'Call',
                        'UpgradeCommittee': 'Call',
                        'Utility': 'Call',
                    },
                    'maybe_periodic': (
                        None,
                        ('u32', 'u32'),
                    ),
                    'priority': 'u8',
                    'when': 'u32',
                },
                'schedule_after': {
                    'after': 'u32',
                    'call': {
                        None: None,
                        'Asset': 'Call',
                        'Authorship': {
                            'set_uncles': 'InnerStruct',
                        },
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Base': 'Call',
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'CddServiceProviders': 'Call',
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'CommitteeMembership': 'Call',
                        'ComplianceManager': 'Call',
                        'Contracts': {
                            'call': 'InnerStruct',
                            'call_old_weight': 'InnerStruct',
                            'instantiate': 'InnerStruct',
                            'instantiate_old_weight': 'InnerStruct',
                            'instantiate_with_code': 'InnerStruct',
                            'instantiate_with_code_old_weight': 'InnerStruct',
                            'remove_code': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'upload_code': 'InnerStruct',
                        },
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'ImOnline': {
                            'heartbeat': 'InnerStruct',
                        },
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'MultiSig': 'Call',
                        'Nft': 'Call',
                        'Pips': 'Call',
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'ProtocolFee': 'Call',
                        'Relayer': 'Call',
                        'Rewards': 'Call',
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'Sudo': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
                            'placeholder_fill_block': None,
                            'remark': 'InnerStruct',
                            'remark_with_event': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'set_code_without_checks': 'InnerStruct',
                            'set_heap_pages': 'InnerStruct',
                            'set_storage': 'InnerStruct',
                        },
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': 'Call',
                    },
                    'maybe_periodic': (
                        None,
                        ('u32', 'u32'),
                    ),
                    'priority': 'u8',
                },
                'schedule_named': {
                    'call': {
                        'Asset': 'Call',
                        'Authorship': {
                            'set_uncles': 'InnerStruct',
                        },
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Base': 'Call',
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'CddServiceProviders': 'Call',
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'CommitteeMembership': 'Call',
                        'ComplianceManager': 'Call',
                        'Contracts': {
                            'call': 'InnerStruct',
                            'call_old_weight': 'InnerStruct',
                            'instantiate': 'InnerStruct',
                            'instantiate_old_weight': 'InnerStruct',
                            'instantiate_with_code': 'InnerStruct',
                            'instantiate_with_code_old_weight': 'InnerStruct',
                            'remove_code': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'upload_code': 'InnerStruct',
                        },
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'ImOnline': {
                            'heartbeat': 'InnerStruct',
                        },
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'MultiSig': 'Call',
                        'Nft': 'Call',
                        'Pips': 'Call',
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'ProtocolFee': 'Call',
                        'Relayer': 'Call',
                        'Rewards': 'Call',
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'Sudo': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
                            'placeholder_fill_block': None,
                            'remark': 'InnerStruct',
                            'remark_with_event': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'set_code_without_checks': 'InnerStruct',
                            'set_heap_pages': 'InnerStruct',
                            'set_storage': 'InnerStruct',
                        },
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        None: None,
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': 'Call',
                    },
                    'id': '[u8; 32]',
                    'maybe_periodic': (
                        None,
                        ('u32', 'u32'),
                    ),
                    'priority': 'u8',
                    'when': 'u32',
                },
                'schedule_named_after': {
                    'after': 'u32',
                    'call': {
                        'Asset': 'Call',
                        'Authorship': {
                            'set_uncles': 'InnerStruct',
                        },
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Base': 'Call',
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'CddServiceProviders': 'Call',
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'CommitteeMembership': 'Call',
                        'ComplianceManager': 'Call',
                        'Contracts': {
                            'call': 'InnerStruct',
                            'call_old_weight': 'InnerStruct',
                            'instantiate': 'InnerStruct',
                            'instantiate_old_weight': 'InnerStruct',
                            'instantiate_with_code': 'InnerStruct',
                            'instantiate_with_code_old_weight': 'InnerStruct',
                            'remove_code': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'upload_code': 'InnerStruct',
                        },
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'ImOnline': {
                            'heartbeat': 'InnerStruct',
                        },
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'MultiSig': 'Call',
                        'Nft': 'Call',
                        'Pips': 'Call',
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'ProtocolFee': 'Call',
                        'Relayer': 'Call',
                        'Rewards': 'Call',
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'Sudo': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
                            'placeholder_fill_block': None,
                            'remark': 'InnerStruct',
                            'remark_with_event': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'set_code_without_checks': 'InnerStruct',
                            'set_heap_pages': 'InnerStruct',
                            'set_storage': 'InnerStruct',
                        },
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': 'Call',
                        None: None,
                    },
                    'id': '[u8; 32]',
                    'maybe_periodic': (
                        None,
                        ('u32', 'u32'),
                    ),
                    'priority': 'u8',
                },
            },
            'Session': {
                'purge_keys': None,
                'set_keys': {
                    'keys': {
                        'authority_discovery': '[u8; 32]',
                        'babe': '[u8; 32]',
                        'grandpa': '[u8; 32]',
                        'im_online': '[u8; 32]',
                    },
                    'proof': 'Bytes',
                },
            },
            'Settlement': 'Call',
            'Staking': 'Call',
            'Statistics': 'Call',
            'Sto': 'Call',
            'Sudo': 'Call',
            'System': {
                'kill_prefix': {
                    'prefix': 'Bytes',
                    'subkeys': 'u32',
                },
                'kill_storage': {
                    'keys': ['Bytes'],
                },
                'placeholder_fill_block': None,
                'remark': {
                    'remark': 'Bytes',
                },
                'remark_with_event': {
                    'remark': 'Bytes',
                },
                'set_code': {
                    'code': 'Bytes',
                },
                'set_code_without_checks': {
                    'code': 'Bytes',
                },
                'set_heap_pages': {
                    'pages': 'u64',
                },
                'set_storage': {
                    'items': [
                        (
                            'Bytes',
                            'Bytes',
                        ),
                    ],
                },
            },
            'TechnicalCommittee': 'Call',
            'TechnicalCommitteeMembership': 'Call',
            'Timestamp': {
                'set': {'now': 'u64'},
            },
            'Treasury': 'Call',
            'UpgradeCommittee': 'Call',
            'UpgradeCommitteeMembership': 'Call',
            'Utility': 'Call',
        },
    ],
}
)
```

---------
### batch_optimistic
Dispatch multiple calls from the sender&\#x27;s origin.

This will execute all calls, in order, irrespective of failures.
Any failures will be available in a `BatchOptimisticFailed` event.

May be called from root or a signed origin.

\# Parameters
- `calls`: The calls to be dispatched from the same origin.


\# Weight
- The sum of the weights of the `calls`.
- One event.

This will return `Ok` in all circumstances except an unsigned origin.
To determine the success of the batch, an event is deposited.
If any call failed, then `BatchOptimisticFailed` is deposited,
with a vector of event counts for each call as well as a vector
of errors.
If all were successful, then the `BatchCompleted` event is deposited.
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'batch_optimistic', {
    'calls': [
        {
            'Asset': 'Call',
            'Authorship': {
                'set_uncles': {
                    'new_uncles': [
                        {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                    ],
                },
            },
            'Babe': {
                'plan_config_change': {
                    'config': {
                        None: None,
                        'V1': {
                            'allowed_slots': 'scale_info::330',
                            'c': (
                                'u64',
                                'u64',
                            ),
                        },
                    },
                },
                'report_equivocation': {
                    'equivocation_proof': {
                        'first_header': {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                        'offender': '[u8; 32]',
                        'second_header': {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                        'slot': 'u64',
                    },
                    'key_owner_proof': {
                        'session': 'u32',
                        'trie_nodes': [
                            'Bytes',
                        ],
                        'validator_count': 'u32',
                    },
                },
                'report_equivocation_unsigned': {
                    'equivocation_proof': {
                        'first_header': {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                        'offender': '[u8; 32]',
                        'second_header': {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                        'slot': 'u64',
                    },
                    'key_owner_proof': {
                        'session': 'u32',
                        'trie_nodes': [
                            'Bytes',
                        ],
                        'validator_count': 'u32',
                    },
                },
            },
            'Balances': 'Call',
            'Base': 'Call',
            'Bridge': 'Call',
            'CapitalDistribution': {
                'claim': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                },
                'distribute': {
                    'amount': 'u128',
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'currency': '[u8; 12]',
                    'expires_at': (
                        None,
                        'u64',
                    ),
                    'payment_at': 'u64',
                    'per_share': 'u128',
                    'portfolio': (
                        None,
                        'u64',
                    ),
                },
                'push_benefit': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'holder': '[u8; 32]',
                },
                'reclaim': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                },
                'remove_distribution': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                },
            },
            'CddServiceProviders': 'Call',
            'Checkpoint': {
                'create_checkpoint': {
                    'ticker': '[u8; 12]',
                },
                'create_schedule': {
                    'schedule': {
                        'period': {
                            'amount': 'u64',
                            'unit': 'scale_info::173',
                        },
                        'remaining': 'u32',
                        'start': (
                            None,
                            'u64',
                        ),
                    },
                    'ticker': '[u8; 12]',
                },
                'remove_schedule': {
                    'id': 'u64',
                    'ticker': '[u8; 12]',
                },
                'set_schedules_max_complexity': {
                    'max_complexity': 'u64',
                },
            },
            'CommitteeMembership': 'Call',
            'ComplianceManager': 'Call',
            'Contracts': {
                'call': {
                    'data': 'Bytes',
                    'dest': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                    'gas_limit': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'call_old_weight': {
                    'data': 'Bytes',
                    'dest': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                    'gas_limit': 'u64',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'instantiate': {
                    'code_hash': '[u8; 32]',
                    'data': 'Bytes',
                    'gas_limit': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                    'salt': 'Bytes',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'instantiate_old_weight': {
                    'code_hash': '[u8; 32]',
                    'data': 'Bytes',
                    'gas_limit': 'u64',
                    'salt': 'Bytes',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'instantiate_with_code': {
                    'code': 'Bytes',
                    'data': 'Bytes',
                    'gas_limit': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                    'salt': 'Bytes',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'instantiate_with_code_old_weight': {
                    'code': 'Bytes',
                    'data': 'Bytes',
                    'gas_limit': 'u64',
                    'salt': 'Bytes',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'remove_code': {
                    'code_hash': '[u8; 32]',
                },
                'set_code': {
                    'code_hash': '[u8; 32]',
                    'dest': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                },
                'upload_code': {
                    'code': 'Bytes',
                    'determinism': (
                        'Deterministic',
                        'AllowIndeterminism',
                    ),
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                },
            },
            'CorporateAction': 'Call',
            'CorporateBallot': {
                'attach_ballot': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'meta': {
                        'motions': [
                            'scale_info::206',
                        ],
                        'title': 'Bytes',
                    },
                    'range': {
                        'end': 'u64',
                        'start': 'u64',
                    },
                    'rcv': 'bool',
                },
                'change_end': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'end': 'u64',
                },
                'change_meta': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'meta': {
                        'motions': [
                            'scale_info::206',
                        ],
                        'title': 'Bytes',
                    },
                },
                'change_rcv': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'rcv': 'bool',
                },
                'remove_ballot': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                },
                'vote': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'votes': [
                        {
                            'fallback': (
                                None,
                                'u16',
                            ),
                            'power': 'u128',
                        },
                    ],
                },
            },
            'ExternalAgents': 'Call',
            'Grandpa': {
                'note_stalled': {
                    'best_finalized_block_number': 'u32',
                    'delay': 'u32',
                },
                'report_equivocation': {
                    'equivocation_proof': {
                        'equivocation': {
                            'Precommit': 'scale_info::476',
                            'Prevote': 'scale_info::471',
                        },
                        'set_id': 'u64',
                    },
                    'key_owner_proof': {
                        'session': 'u32',
                        'trie_nodes': [
                            'Bytes',
                        ],
                        'validator_count': 'u32',
                    },
                },
                'report_equivocation_unsigned': {
                    'equivocation_proof': {
                        'equivocation': {
                            'Precommit': 'scale_info::476',
                            'Prevote': 'scale_info::471',
                        },
                        'set_id': 'u64',
                    },
                    'key_owner_proof': {
                        'session': 'u32',
                        'trie_nodes': [
                            'Bytes',
                        ],
                        'validator_count': 'u32',
                    },
                },
            },
            'Identity': 'Call',
            'ImOnline': {
                'heartbeat': {
                    'heartbeat': {
                        'authority_index': 'u32',
                        'block_number': 'u32',
                        'network_state': {
                            'external_addresses': [
                                'Bytes',
                            ],
                            'peer_id': 'Bytes',
                        },
                        'session_index': 'u32',
                        'validators_len': 'u32',
                    },
                    'signature': '[u8; 64]',
                },
            },
            'Indices': {
                'claim': {
                    'index': 'u32',
                },
                'force_transfer': {
                    'freeze': 'bool',
                    'index': 'u32',
                    'new': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                },
                'free': {
                    'index': 'u32',
                },
                'freeze': {
                    'index': 'u32',
                },
                'transfer': {
                    'index': 'u32',
                    'new': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                },
            },
            'MultiSig': 'Call',
            'Nft': 'Call',
            'Pips': 'Call',
            'PolymeshCommittee': 'Call',
            'PolymeshContracts': 'Call',
            'Portfolio': 'Call',
            'Preimage': {
                'note_preimage': {
                    'bytes': 'Bytes',
                },
                'request_preimage': {
                    'hash': '[u8; 32]',
                },
                'unnote_preimage': {
                    'hash': '[u8; 32]',
                },
                'unrequest_preimage': {
                    'hash': '[u8; 32]',
                },
            },
            'ProtocolFee': 'Call',
            'Relayer': 'Call',
            'Rewards': 'Call',
            'Scheduler': {
                'cancel': {
                    'index': 'u32',
                    'when': 'u32',
                },
                'cancel_named': {
                    'id': '[u8; 32]',
                },
                'schedule': {
                    'call': {
                        'Asset': 'Call',
                        'Authorship': {
                            'set_uncles': 'InnerStruct',
                        },
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Base': 'Call',
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'CddServiceProviders': 'Call',
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'CommitteeMembership': 'Call',
                        'ComplianceManager': 'Call',
                        'Contracts': {
                            'call': 'InnerStruct',
                            'call_old_weight': 'InnerStruct',
                            'instantiate': 'InnerStruct',
                            'instantiate_old_weight': 'InnerStruct',
                            'instantiate_with_code': 'InnerStruct',
                            'instantiate_with_code_old_weight': 'InnerStruct',
                            'remove_code': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'upload_code': 'InnerStruct',
                        },
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'ImOnline': {
                            'heartbeat': 'InnerStruct',
                        },
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'MultiSig': 'Call',
                        'Nft': 'Call',
                        'Pips': 'Call',
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'ProtocolFee': 'Call',
                        'Relayer': 'Call',
                        'Rewards': 'Call',
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'Sudo': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
                            'placeholder_fill_block': None,
                            'remark': 'InnerStruct',
                            'remark_with_event': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'set_code_without_checks': 'InnerStruct',
                            'set_heap_pages': 'InnerStruct',
                            'set_storage': 'InnerStruct',
                        },
                        'TechnicalCommittee': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        None: None,
                        'TechnicalCommitteeMembership': 'Call',
                        'UpgradeCommittee': 'Call',
                        'Utility': 'Call',
                    },
                    'maybe_periodic': (
                        None,
                        ('u32', 'u32'),
                    ),
                    'priority': 'u8',
                    'when': 'u32',
                },
                'schedule_after': {
                    'after': 'u32',
                    'call': {
                        None: None,
                        'Asset': 'Call',
                        'Authorship': {
                            'set_uncles': 'InnerStruct',
                        },
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Base': 'Call',
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'CddServiceProviders': 'Call',
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'CommitteeMembership': 'Call',
                        'ComplianceManager': 'Call',
                        'Contracts': {
                            'call': 'InnerStruct',
                            'call_old_weight': 'InnerStruct',
                            'instantiate': 'InnerStruct',
                            'instantiate_old_weight': 'InnerStruct',
                            'instantiate_with_code': 'InnerStruct',
                            'instantiate_with_code_old_weight': 'InnerStruct',
                            'remove_code': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'upload_code': 'InnerStruct',
                        },
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'ImOnline': {
                            'heartbeat': 'InnerStruct',
                        },
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'MultiSig': 'Call',
                        'Nft': 'Call',
                        'Pips': 'Call',
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'ProtocolFee': 'Call',
                        'Relayer': 'Call',
                        'Rewards': 'Call',
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'Sudo': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
                            'placeholder_fill_block': None,
                            'remark': 'InnerStruct',
                            'remark_with_event': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'set_code_without_checks': 'InnerStruct',
                            'set_heap_pages': 'InnerStruct',
                            'set_storage': 'InnerStruct',
                        },
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': 'Call',
                    },
                    'maybe_periodic': (
                        None,
                        ('u32', 'u32'),
                    ),
                    'priority': 'u8',
                },
                'schedule_named': {
                    'call': {
                        'Asset': 'Call',
                        'Authorship': {
                            'set_uncles': 'InnerStruct',
                        },
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Base': 'Call',
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'CddServiceProviders': 'Call',
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'CommitteeMembership': 'Call',
                        'ComplianceManager': 'Call',
                        'Contracts': {
                            'call': 'InnerStruct',
                            'call_old_weight': 'InnerStruct',
                            'instantiate': 'InnerStruct',
                            'instantiate_old_weight': 'InnerStruct',
                            'instantiate_with_code': 'InnerStruct',
                            'instantiate_with_code_old_weight': 'InnerStruct',
                            'remove_code': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'upload_code': 'InnerStruct',
                        },
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'ImOnline': {
                            'heartbeat': 'InnerStruct',
                        },
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'MultiSig': 'Call',
                        'Nft': 'Call',
                        'Pips': 'Call',
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'ProtocolFee': 'Call',
                        'Relayer': 'Call',
                        'Rewards': 'Call',
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'Sudo': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
                            'placeholder_fill_block': None,
                            'remark': 'InnerStruct',
                            'remark_with_event': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'set_code_without_checks': 'InnerStruct',
                            'set_heap_pages': 'InnerStruct',
                            'set_storage': 'InnerStruct',
                        },
                        'TechnicalCommittee': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        None: None,
                        'TechnicalCommitteeMembership': 'Call',
                        'UpgradeCommittee': 'Call',
                        'Utility': 'Call',
                    },
                    'id': '[u8; 32]',
                    'maybe_periodic': (
                        None,
                        ('u32', 'u32'),
                    ),
                    'priority': 'u8',
                    'when': 'u32',
                },
                'schedule_named_after': {
                    'after': 'u32',
                    'call': {
                        'Asset': 'Call',
                        'Authorship': {
                            'set_uncles': 'InnerStruct',
                        },
                        None: None,
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Base': 'Call',
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'CddServiceProviders': 'Call',
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'CommitteeMembership': 'Call',
                        'ComplianceManager': 'Call',
                        'Contracts': {
                            'call': 'InnerStruct',
                            'call_old_weight': 'InnerStruct',
                            'instantiate': 'InnerStruct',
                            'instantiate_old_weight': 'InnerStruct',
                            'instantiate_with_code': 'InnerStruct',
                            'instantiate_with_code_old_weight': 'InnerStruct',
                            'remove_code': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'upload_code': 'InnerStruct',
                        },
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'ImOnline': {
                            'heartbeat': 'InnerStruct',
                        },
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'MultiSig': 'Call',
                        'Nft': 'Call',
                        'Pips': 'Call',
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'ProtocolFee': 'Call',
                        'Relayer': 'Call',
                        'Rewards': 'Call',
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'Sudo': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
                            'placeholder_fill_block': None,
                            'remark': 'InnerStruct',
                            'remark_with_event': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'set_code_without_checks': 'InnerStruct',
                            'set_heap_pages': 'InnerStruct',
                            'set_storage': 'InnerStruct',
                        },
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': 'Call',
                    },
                    'id': '[u8; 32]',
                    'maybe_periodic': (
                        None,
                        ('u32', 'u32'),
                    ),
                    'priority': 'u8',
                },
            },
            'Session': {
                'purge_keys': None,
                'set_keys': {
                    'keys': {
                        'authority_discovery': '[u8; 32]',
                        'babe': '[u8; 32]',
                        'grandpa': '[u8; 32]',
                        'im_online': '[u8; 32]',
                    },
                    'proof': 'Bytes',
                },
            },
            'Settlement': 'Call',
            'Staking': 'Call',
            'Statistics': 'Call',
            'Sto': 'Call',
            'Sudo': 'Call',
            'System': {
                'kill_prefix': {
                    'prefix': 'Bytes',
                    'subkeys': 'u32',
                },
                'kill_storage': {
                    'keys': ['Bytes'],
                },
                'placeholder_fill_block': None,
                'remark': {
                    'remark': 'Bytes',
                },
                'remark_with_event': {
                    'remark': 'Bytes',
                },
                'set_code': {
                    'code': 'Bytes',
                },
                'set_code_without_checks': {
                    'code': 'Bytes',
                },
                'set_heap_pages': {
                    'pages': 'u64',
                },
                'set_storage': {
                    'items': [
                        (
                            'Bytes',
                            'Bytes',
                        ),
                    ],
                },
            },
            'TechnicalCommitteeMembership': 'Call',
            'Timestamp': {
                'set': {'now': 'u64'},
            },
            'Treasury': 'Call',
            'UpgradeCommitteeMembership': 'Call',
            None: None,
            'TechnicalCommittee': 'Call',
            'UpgradeCommittee': 'Call',
            'Utility': 'Call',
        },
    ],
}
)
```

---------
### relay_tx
Relay a call for a target from an origin

Relaying in this context refers to the ability of origin to make a call on behalf of
target.

Fees are charged to origin

\# Parameters
- `target`: Account to be relayed
- `signature`: Signature from target authorizing the relay
- `call`: Call to be relayed on behalf of target

#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `T::AccountId` | 
| signature | `T::OffChainSignature` | 
| call | `UniqueCall<<T as Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'relay_tx', {
    'call': {
        'call': {
            'Asset': 'Call',
            'Authorship': {
                'set_uncles': {
                    'new_uncles': [
                        {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                    ],
                },
            },
            'Babe': {
                'plan_config_change': {
                    'config': {
                        None: None,
                        'V1': {
                            'allowed_slots': 'scale_info::330',
                            'c': (
                                'u64',
                                'u64',
                            ),
                        },
                    },
                },
                'report_equivocation': {
                    'equivocation_proof': {
                        'first_header': {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                        'offender': '[u8; 32]',
                        'second_header': {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                        'slot': 'u64',
                    },
                    'key_owner_proof': {
                        'session': 'u32',
                        'trie_nodes': [
                            'Bytes',
                        ],
                        'validator_count': 'u32',
                    },
                },
                'report_equivocation_unsigned': {
                    'equivocation_proof': {
                        'first_header': {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                        'offender': '[u8; 32]',
                        'second_header': {
                            'digest': 'scale_info::13',
                            'extrinsics_root': '[u8; 32]',
                            'number': 'u32',
                            'parent_hash': '[u8; 32]',
                            'state_root': '[u8; 32]',
                        },
                        'slot': 'u64',
                    },
                    'key_owner_proof': {
                        'session': 'u32',
                        'trie_nodes': [
                            'Bytes',
                        ],
                        'validator_count': 'u32',
                    },
                },
            },
            'Balances': 'Call',
            'Base': 'Call',
            'Bridge': 'Call',
            'CapitalDistribution': {
                'claim': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                },
                'distribute': {
                    'amount': 'u128',
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'currency': '[u8; 12]',
                    'expires_at': (
                        None,
                        'u64',
                    ),
                    'payment_at': 'u64',
                    'per_share': 'u128',
                    'portfolio': (
                        None,
                        'u64',
                    ),
                },
                'push_benefit': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'holder': '[u8; 32]',
                },
                'reclaim': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                },
                'remove_distribution': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                },
            },
            'CddServiceProviders': 'Call',
            'Checkpoint': {
                'create_checkpoint': {
                    'ticker': '[u8; 12]',
                },
                'create_schedule': {
                    'schedule': {
                        'period': {
                            'amount': 'u64',
                            'unit': 'scale_info::173',
                        },
                        'remaining': 'u32',
                        'start': (
                            None,
                            'u64',
                        ),
                    },
                    'ticker': '[u8; 12]',
                },
                'remove_schedule': {
                    'id': 'u64',
                    'ticker': '[u8; 12]',
                },
                'set_schedules_max_complexity': {
                    'max_complexity': 'u64',
                },
            },
            'CommitteeMembership': 'Call',
            'ComplianceManager': 'Call',
            'Contracts': {
                'call': {
                    'data': 'Bytes',
                    'dest': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                    'gas_limit': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'call_old_weight': {
                    'data': 'Bytes',
                    'dest': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                    'gas_limit': 'u64',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'instantiate': {
                    'code_hash': '[u8; 32]',
                    'data': 'Bytes',
                    'gas_limit': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                    'salt': 'Bytes',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'instantiate_old_weight': {
                    'code_hash': '[u8; 32]',
                    'data': 'Bytes',
                    'gas_limit': 'u64',
                    'salt': 'Bytes',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'instantiate_with_code': {
                    'code': 'Bytes',
                    'data': 'Bytes',
                    'gas_limit': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                    'salt': 'Bytes',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'instantiate_with_code_old_weight': {
                    'code': 'Bytes',
                    'data': 'Bytes',
                    'gas_limit': 'u64',
                    'salt': 'Bytes',
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                    'value': 'u128',
                },
                'remove_code': {
                    'code_hash': '[u8; 32]',
                },
                'set_code': {
                    'code_hash': '[u8; 32]',
                    'dest': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                },
                'upload_code': {
                    'code': 'Bytes',
                    'determinism': (
                        'Deterministic',
                        'AllowIndeterminism',
                    ),
                    'storage_deposit_limit': (
                        None,
                        'u128',
                    ),
                },
            },
            'CorporateAction': 'Call',
            'CorporateBallot': {
                'attach_ballot': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'meta': {
                        'motions': [
                            'scale_info::206',
                        ],
                        'title': 'Bytes',
                    },
                    'range': {
                        'end': 'u64',
                        'start': 'u64',
                    },
                    'rcv': 'bool',
                },
                'change_end': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'end': 'u64',
                },
                'change_meta': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'meta': {
                        'motions': [
                            'scale_info::206',
                        ],
                        'title': 'Bytes',
                    },
                },
                'change_rcv': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'rcv': 'bool',
                },
                'remove_ballot': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                },
                'vote': {
                    'ca_id': {
                        'local_id': 'u32',
                        'ticker': '[u8; 12]',
                    },
                    'votes': [
                        {
                            'fallback': (
                                None,
                                'u16',
                            ),
                            'power': 'u128',
                        },
                    ],
                },
            },
            'ExternalAgents': 'Call',
            'Grandpa': {
                'note_stalled': {
                    'best_finalized_block_number': 'u32',
                    'delay': 'u32',
                },
                'report_equivocation': {
                    'equivocation_proof': {
                        'equivocation': {
                            'Precommit': 'scale_info::476',
                            'Prevote': 'scale_info::471',
                        },
                        'set_id': 'u64',
                    },
                    'key_owner_proof': {
                        'session': 'u32',
                        'trie_nodes': [
                            'Bytes',
                        ],
                        'validator_count': 'u32',
                    },
                },
                'report_equivocation_unsigned': {
                    'equivocation_proof': {
                        'equivocation': {
                            'Precommit': 'scale_info::476',
                            'Prevote': 'scale_info::471',
                        },
                        'set_id': 'u64',
                    },
                    'key_owner_proof': {
                        'session': 'u32',
                        'trie_nodes': [
                            'Bytes',
                        ],
                        'validator_count': 'u32',
                    },
                },
            },
            'Identity': 'Call',
            'ImOnline': {
                'heartbeat': {
                    'heartbeat': {
                        'authority_index': 'u32',
                        'block_number': 'u32',
                        'network_state': {
                            'external_addresses': [
                                'Bytes',
                            ],
                            'peer_id': 'Bytes',
                        },
                        'session_index': 'u32',
                        'validators_len': 'u32',
                    },
                    'signature': '[u8; 64]',
                },
            },
            'MultiSig': 'Call',
            'Nft': 'Call',
            'PolymeshContracts': 'Call',
            'Preimage': {
                'note_preimage': {
                    'bytes': 'Bytes',
                },
                'request_preimage': {
                    'hash': '[u8; 32]',
                },
                'unnote_preimage': {
                    'hash': '[u8; 32]',
                },
                'unrequest_preimage': {
                    'hash': '[u8; 32]',
                },
            },
            'Relayer': 'Call',
            'Rewards': 'Call',
            'Session': {
                'purge_keys': None,
                'set_keys': {
                    'keys': {
                        'authority_discovery': '[u8; 32]',
                        'babe': '[u8; 32]',
                        'grandpa': '[u8; 32]',
                        'im_online': '[u8; 32]',
                    },
                    'proof': 'Bytes',
                },
            },
            'Staking': 'Call',
            'TechnicalCommitteeMembership': 'Call',
            'UpgradeCommitteeMembership': 'Call',
            None: None,
            'Indices': {
                'claim': {
                    'index': 'u32',
                },
                'force_transfer': {
                    'freeze': 'bool',
                    'index': 'u32',
                    'new': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                },
                'free': {
                    'index': 'u32',
                },
                'freeze': {
                    'index': 'u32',
                },
                'transfer': {
                    'index': 'u32',
                    'new': {
                        'Address20': '[u8; 20]',
                        'Address32': '[u8; 32]',
                        'Id': 'AccountId',
                        'Index': 'u32',
                        'Raw': 'Bytes',
                    },
                },
            },
            'Pips': 'Call',
            'PolymeshCommittee': 'Call',
            'Portfolio': 'Call',
            'ProtocolFee': 'Call',
            'Scheduler': {
                'cancel': {
                    'index': 'u32',
                    'when': 'u32',
                },
                'cancel_named': {
                    'id': '[u8; 32]',
                },
                'schedule': {
                    'call': {
                        'Authorship': {
                            'set_uncles': 'InnerStruct',
                        },
                        None: None,
                        'Asset': 'Call',
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Base': 'Call',
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'CddServiceProviders': 'Call',
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'CommitteeMembership': 'Call',
                        'ComplianceManager': 'Call',
                        'Contracts': {
                            'call': 'InnerStruct',
                            'call_old_weight': 'InnerStruct',
                            'instantiate': 'InnerStruct',
                            'instantiate_old_weight': 'InnerStruct',
                            'instantiate_with_code': 'InnerStruct',
                            'instantiate_with_code_old_weight': 'InnerStruct',
                            'remove_code': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'upload_code': 'InnerStruct',
                        },
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'ImOnline': {
                            'heartbeat': 'InnerStruct',
                        },
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'MultiSig': 'Call',
                        'Nft': 'Call',
                        'Pips': 'Call',
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'ProtocolFee': 'Call',
                        'Relayer': 'Call',
                        'Rewards': 'Call',
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'Sudo': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
                            'placeholder_fill_block': None,
                            'remark': 'InnerStruct',
                            'remark_with_event': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'set_code_without_checks': 'InnerStruct',
                            'set_heap_pages': 'InnerStruct',
                            'set_storage': 'InnerStruct',
                        },
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': 'Call',
                    },
                    'maybe_periodic': (
                        None,
                        ('u32', 'u32'),
                    ),
                    'priority': 'u8',
                    'when': 'u32',
                },
                'schedule_after': {
                    'after': 'u32',
                    'call': {
                        None: None,
                        'Asset': 'Call',
                        'Authorship': {
                            'set_uncles': 'InnerStruct',
                        },
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Base': 'Call',
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'CddServiceProviders': 'Call',
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'CommitteeMembership': 'Call',
                        'ComplianceManager': 'Call',
                        'Contracts': {
                            'call': 'InnerStruct',
                            'call_old_weight': 'InnerStruct',
                            'instantiate': 'InnerStruct',
                            'instantiate_old_weight': 'InnerStruct',
                            'instantiate_with_code': 'InnerStruct',
                            'instantiate_with_code_old_weight': 'InnerStruct',
                            'remove_code': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'upload_code': 'InnerStruct',
                        },
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'ImOnline': {
                            'heartbeat': 'InnerStruct',
                        },
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'MultiSig': 'Call',
                        'Nft': 'Call',
                        'Pips': 'Call',
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'ProtocolFee': 'Call',
                        'Relayer': 'Call',
                        'Rewards': 'Call',
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'Sudo': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
                            'placeholder_fill_block': None,
                            'remark': 'InnerStruct',
                            'remark_with_event': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'set_code_without_checks': 'InnerStruct',
                            'set_heap_pages': 'InnerStruct',
                            'set_storage': 'InnerStruct',
                        },
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': 'Call',
                    },
                    'maybe_periodic': (
                        None,
                        ('u32', 'u32'),
                    ),
                    'priority': 'u8',
                },
                'schedule_named': {
                    'call': {
                        'Asset': 'Call',
                        'Authorship': {
                            'set_uncles': 'InnerStruct',
                        },
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Bridge': 'Call',
                        None: None,
                        'Balances': 'Call',
                        'Base': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'CddServiceProviders': 'Call',
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'CommitteeMembership': 'Call',
                        'ComplianceManager': 'Call',
                        'Contracts': {
                            'call': 'InnerStruct',
                            'call_old_weight': 'InnerStruct',
                            'instantiate': 'InnerStruct',
                            'instantiate_old_weight': 'InnerStruct',
                            'instantiate_with_code': 'InnerStruct',
                            'instantiate_with_code_old_weight': 'InnerStruct',
                            'remove_code': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'upload_code': 'InnerStruct',
                        },
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'ImOnline': {
                            'heartbeat': 'InnerStruct',
                        },
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'MultiSig': 'Call',
                        'Nft': 'Call',
                        'Pips': 'Call',
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'ProtocolFee': 'Call',
                        'Relayer': 'Call',
                        'Rewards': 'Call',
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'Sudo': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
                            'placeholder_fill_block': None,
                            'remark': 'InnerStruct',
                            'remark_with_event': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'set_code_without_checks': 'InnerStruct',
                            'set_heap_pages': 'InnerStruct',
                            'set_storage': 'InnerStruct',
                        },
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': 'Call',
                    },
                    'id': '[u8; 32]',
                    'maybe_periodic': (
                        None,
                        ('u32', 'u32'),
                    ),
                    'priority': 'u8',
                    'when': 'u32',
                },
                'schedule_named_after': {
                    'after': 'u32',
                    'call': {
                        'Asset': 'Call',
                        None: None,
                        'Authorship': {
                            'set_uncles': 'InnerStruct',
                        },
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Base': 'Call',
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'CddServiceProviders': 'Call',
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'CommitteeMembership': 'Call',
                        'ComplianceManager': 'Call',
                        'Contracts': {
                            'call': 'InnerStruct',
                            'call_old_weight': 'InnerStruct',
                            'instantiate': 'InnerStruct',
                            'instantiate_old_weight': 'InnerStruct',
                            'instantiate_with_code': 'InnerStruct',
                            'instantiate_with_code_old_weight': 'InnerStruct',
                            'remove_code': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'upload_code': 'InnerStruct',
                        },
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'ImOnline': {
                            'heartbeat': 'InnerStruct',
                        },
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'MultiSig': 'Call',
                        'Nft': 'Call',
                        'Pips': 'Call',
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'ProtocolFee': 'Call',
                        'Relayer': 'Call',
                        'Rewards': 'Call',
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'Sudo': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
                            'placeholder_fill_block': None,
                            'remark': 'InnerStruct',
                            'remark_with_event': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'set_code_without_checks': 'InnerStruct',
                            'set_heap_pages': 'InnerStruct',
                            'set_storage': 'InnerStruct',
                        },
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': 'Call',
                    },
                    'id': '[u8; 32]',
                    'maybe_periodic': (
                        None,
                        ('u32', 'u32'),
                    ),
                    'priority': 'u8',
                },
            },
            'Settlement': 'Call',
            'Statistics': 'Call',
            'Sto': 'Call',
            'Sudo': 'Call',
            'System': {
                'kill_prefix': {
                    'prefix': 'Bytes',
                    'subkeys': 'u32',
                },
                'kill_storage': {
                    'keys': ['Bytes'],
                },
                'placeholder_fill_block': None,
                'remark': {
                    'remark': 'Bytes',
                },
                'remark_with_event': {
                    'remark': 'Bytes',
                },
                'set_code': {
                    'code': 'Bytes',
                },
                'set_code_without_checks': {
                    'code': 'Bytes',
                },
                'set_heap_pages': {
                    'pages': 'u64',
                },
                'set_storage': {
                    'items': [
                        (
                            'Bytes',
                            'Bytes',
                        ),
                    ],
                },
            },
            'TechnicalCommittee': 'Call',
            'Timestamp': {
                'set': {'now': 'u64'},
            },
            'Treasury': 'Call',
            'UpgradeCommittee': 'Call',
            'Utility': 'Call',
        },
        'nonce': 'u64',
    },
    'signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
    'target': 'AccountId',
}
)
```

---------
## Events

---------
### BatchCompleted
Batch of dispatches completed fully with no error.
Includes a vector of event counts for each dispatch.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventCounts` | ```['u32']```

---------
### BatchInterrupted
Batch of dispatches did not complete fully.
Includes a vector of event counts for each dispatch and
the index of the first failing dispatch as well as the error.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventCounts` | ```['u32']```
| None | `ErrorAt` | ```('u32', {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None})```

---------
### BatchOptimisticFailed
Batch of dispatches did not complete fully.
Includes a vector of event counts for each call and
a vector of any failed dispatches with their indices and associated error.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventCounts` | ```['u32']```
| None | `Vec<ErrorAt>` | ```[('u32', {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None})]```

---------
## Storage functions

---------
### Nonces

#### Python
```python
result = substrate.query(
    'Utility', 'Nonces', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
## Errors

---------
### InvalidNonce
Provided nonce was invalid
If the provided nonce &lt; current nonce, the call was already executed
If the provided nonce &gt; current nonce, the call(s) before the current failed to execute

---------
### InvalidSignature
Offchain signature is invalid

---------
### TargetCddMissing
Target does not have a valid CDD

---------