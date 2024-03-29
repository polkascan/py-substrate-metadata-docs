
# Scheduler

---------
## Calls

---------
### cancel
Cancel an anonymously scheduled task.
#### Attributes
| Name | Type |
| -------- | -------- | 
| when | `T::BlockNumber` | 
| index | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Scheduler', 'cancel', {'index': 'u32', 'when': 'u32'}
)
```

---------
### cancel_named
Cancel a named scheduled task.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `TaskName` | 

#### Python
```python
call = substrate.compose_call(
    'Scheduler', 'cancel_named', {'id': '[u8; 32]'}
)
```

---------
### schedule
Anonymously schedule a task.
#### Attributes
| Name | Type |
| -------- | -------- | 
| when | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule', {
    'call': {
        'Asset': 'Call',
        'Babe': {
            'plan_config_change': {
                'config': {
                    None: None,
                    'V1': {
                        'allowed_slots': (
                            'PrimarySlots',
                            'PrimaryAndSecondaryPlainSlots',
                            'PrimaryAndSecondaryVRFSlots',
                        ),
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
                        'digest': {
                            'logs': [
                                'scale_info::15',
                            ],
                        },
                        'extrinsics_root': 'scale_info::11',
                        'number': 'u32',
                        'parent_hash': 'scale_info::11',
                        'state_root': 'scale_info::11',
                    },
                    'offender': '[u8; 32]',
                    'second_header': {
                        'digest': {
                            'logs': [
                                'scale_info::15',
                            ],
                        },
                        'extrinsics_root': 'scale_info::11',
                        'number': 'u32',
                        'parent_hash': 'scale_info::11',
                        'state_root': 'scale_info::11',
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
                        'digest': {
                            'logs': [
                                'scale_info::15',
                            ],
                        },
                        'extrinsics_root': 'scale_info::11',
                        'number': 'u32',
                        'parent_hash': 'scale_info::11',
                        'state_root': 'scale_info::11',
                    },
                    'offender': '[u8; 32]',
                    'second_header': {
                        'digest': {
                            'logs': [
                                'scale_info::15',
                            ],
                        },
                        'extrinsics_root': 'scale_info::11',
                        'number': 'u32',
                        'parent_hash': 'scale_info::11',
                        'state_root': 'scale_info::11',
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
                    'pending': 'scale_info::173',
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
                'code_hash': 'scale_info::11',
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
                'code_hash': 'scale_info::11',
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
                'code_hash': 'scale_info::11',
            },
            'set_code': {
                'code_hash': 'scale_info::11',
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
                        {
                            'choices': [
                                'Bytes',
                            ],
                            'info_link': 'Bytes',
                            'title': 'Bytes',
                        },
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
                        {
                            'choices': [
                                'Bytes',
                            ],
                            'info_link': 'Bytes',
                            'title': 'Bytes',
                        },
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
                        'Precommit': {
                            'first': (
                                'scale_info::464',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::464',
                                '[u8; 64]',
                            ),
                        },
                        'Prevote': {
                            'first': (
                                'scale_info::459',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::459',
                                '[u8; 64]',
                            ),
                        },
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
                        'Precommit': {
                            'first': (
                                'scale_info::464',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::464',
                                '[u8; 64]',
                            ),
                        },
                        'Prevote': {
                            'first': (
                                'scale_info::459',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::459',
                                '[u8; 64]',
                            ),
                        },
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
            'claim': {'index': 'u32'},
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
            'free': {'index': 'u32'},
            'freeze': {'index': 'u32'},
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
                'hash': 'scale_info::11',
            },
            'unnote_preimage': {
                'hash': 'scale_info::11',
            },
            'unrequest_preimage': {
                'hash': 'scale_info::11',
            },
        },
        'ProtocolFee': 'Call',
        'Relayer': 'Call',
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
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    None: None,
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
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
                    'Asset': 'Call',
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
                    None: None,
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
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
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    None: None,
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
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
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
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
        'System': {
            'kill_prefix': {
                'prefix': 'Bytes',
                'subkeys': 'u32',
            },
            'kill_storage': {
                'keys': ['Bytes'],
            },
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
                    ('Bytes', 'Bytes'),
                ],
            },
        },
        'TechnicalCommittee': 'Call',
        'Timestamp': {
            'set': {'now': 'u64'},
        },
        'Treasury': 'Call',
        'UpgradeCommitteeMembership': 'Call',
        None: None,
        'TechnicalCommitteeMembership': 'Call',
        'UpgradeCommittee': 'Call',
        'Utility': {
            'as_derivative': {
                'call': {
                    'Asset': 'Call',
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
                        },
                    },
                    'MultiSig': 'Call',
                    'Nft': 'Call',
                    'Pips': 'Call',
                    'PolymeshCommittee': 'Call',
                    'PolymeshContracts': 'Call',
                    'ProtocolFee': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                    None: None,
                    'Portfolio': 'Call',
                    'Preimage': {
                        'note_preimage': {
                            'bytes': 'Bytes',
                        },
                        'request_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'TechnicalCommittee': 'Call',
                    'TechnicalCommitteeMembership': 'Call',
                    'Timestamp': {
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
                },
                'index': 'u16',
            },
            'batch': {
                'calls': [
                    {
                        'Asset': 'Call',
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                ],
            },
            'batch_all': {
                'calls': [
                    {
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
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Staking': 'Call',
                        None: None,
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                ],
            },
            'batch_atomic': {
                'calls': [
                    {
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                ],
            },
            'batch_old': {
                'calls': [
                    {
                        'Asset': 'Call',
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                ],
            },
            'batch_optimistic': {
                'calls': [
                    {
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                        None: None,
                    },
                ],
            },
            'dispatch_as': {
                'as_origin': {
                    'PolymeshCommittee': (
                        'Endorsed',
                    ),
                    'TechnicalCommittee': (
                        'Endorsed',
                    ),
                    'UpgradeCommittee': (
                        'Endorsed',
                    ),
                    'Void': (),
                    'system': {
                        'None': None,
                        'Root': None,
                        'Signed': 'AccountId',
                    },
                    None: None,
                },
                'call': {
                    None: None,
                    'Asset': 'Call',
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
                },
            },
            'force_batch': {
                'calls': [
                    {
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                        None: None,
                    },
                ],
            },
            'relay_tx': {
                'call': {
                    'call': {
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                    'nonce': 'u64',
                },
                'signature': {
                    'Ecdsa': '[u8; 65]',
                    'Ed25519': '[u8; 64]',
                    'Sr25519': '[u8; 64]',
                },
                'target': 'AccountId',
            },
            'with_weight': {
                'call': {
                    'Asset': 'Call',
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
                        },
                    },
                    'MultiSig': 'Call',
                    'Nft': 'Call',
                    'Pips': 'Call',
                    'PolymeshCommittee': 'Call',
                    'PolymeshContracts': 'Call',
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                    None: None,
                    'Portfolio': 'Call',
                    'Preimage': {
                        'note_preimage': {
                            'bytes': 'Bytes',
                        },
                        'request_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'TechnicalCommittee': 'Call',
                    'TechnicalCommitteeMembership': 'Call',
                    'Timestamp': {
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
                },
                'weight': {
                    'proof_size': 'u64',
                    'ref_time': 'u64',
                },
            },
        },
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
### schedule_after
Anonymously schedule a task after a delay.
#### Attributes
| Name | Type |
| -------- | -------- | 
| after | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule_after', {
    'after': 'u32',
    'call': {
        'Babe': {
            'plan_config_change': {
                'config': {
                    None: None,
                    'V1': {
                        'allowed_slots': (
                            'PrimarySlots',
                            'PrimaryAndSecondaryPlainSlots',
                            'PrimaryAndSecondaryVRFSlots',
                        ),
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
                        'digest': {
                            'logs': [
                                'scale_info::15',
                            ],
                        },
                        'extrinsics_root': 'scale_info::11',
                        'number': 'u32',
                        'parent_hash': 'scale_info::11',
                        'state_root': 'scale_info::11',
                    },
                    'offender': '[u8; 32]',
                    'second_header': {
                        'digest': {
                            'logs': [
                                'scale_info::15',
                            ],
                        },
                        'extrinsics_root': 'scale_info::11',
                        'number': 'u32',
                        'parent_hash': 'scale_info::11',
                        'state_root': 'scale_info::11',
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
                        'digest': {
                            'logs': [
                                'scale_info::15',
                            ],
                        },
                        'extrinsics_root': 'scale_info::11',
                        'number': 'u32',
                        'parent_hash': 'scale_info::11',
                        'state_root': 'scale_info::11',
                    },
                    'offender': '[u8; 32]',
                    'second_header': {
                        'digest': {
                            'logs': [
                                'scale_info::15',
                            ],
                        },
                        'extrinsics_root': 'scale_info::11',
                        'number': 'u32',
                        'parent_hash': 'scale_info::11',
                        'state_root': 'scale_info::11',
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
        'Indices': {
            'claim': {'index': 'u32'},
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
            'free': {'index': 'u32'},
            'freeze': {'index': 'u32'},
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
        None: None,
        'Asset': 'Call',
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
                    'pending': 'scale_info::173',
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
                'code_hash': 'scale_info::11',
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
                'code_hash': 'scale_info::11',
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
                'code_hash': 'scale_info::11',
            },
            'set_code': {
                'code_hash': 'scale_info::11',
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
                        {
                            'choices': [
                                'Bytes',
                            ],
                            'info_link': 'Bytes',
                            'title': 'Bytes',
                        },
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
                        {
                            'choices': [
                                'Bytes',
                            ],
                            'info_link': 'Bytes',
                            'title': 'Bytes',
                        },
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
                        'Precommit': {
                            'first': (
                                'scale_info::464',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::464',
                                '[u8; 64]',
                            ),
                        },
                        'Prevote': {
                            'first': (
                                'scale_info::459',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::459',
                                '[u8; 64]',
                            ),
                        },
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
                        'Precommit': {
                            'first': (
                                'scale_info::464',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::464',
                                '[u8; 64]',
                            ),
                        },
                        'Prevote': {
                            'first': (
                                'scale_info::459',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::459',
                                '[u8; 64]',
                            ),
                        },
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
        'Pips': 'Call',
        'PolymeshCommittee': 'Call',
        'PolymeshContracts': 'Call',
        'Portfolio': 'Call',
        'Preimage': {
            'note_preimage': {
                'bytes': 'Bytes',
            },
            'request_preimage': {
                'hash': 'scale_info::11',
            },
            'unnote_preimage': {
                'hash': 'scale_info::11',
            },
            'unrequest_preimage': {
                'hash': 'scale_info::11',
            },
        },
        'ProtocolFee': 'Call',
        'Relayer': 'Call',
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
                    None: None,
                    'Asset': 'Call',
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
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
                    'Asset': 'Call',
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'CddServiceProviders': 'Call',
                    'CommitteeMembership': 'Call',
                    'Contracts': {
                        'call': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'ExternalAgents': 'Call',
                    'Grandpa': {
                        'note_stalled': {
                            'best_finalized_block_number': 'u32',
                            'delay': 'u32',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'Indices': {
                        'claim': {
                            'index': 'u32',
                        },
                        'force_transfer': {
                            'freeze': 'bool',
                            'index': 'u32',
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
                        },
                    },
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                    None: None,
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                    'ComplianceManager': 'Call',
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
                            ],
                        },
                    },
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
                            'signature': '[u8; 64]',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'TechnicalCommittee': 'Call',
                    'TechnicalCommitteeMembership': 'Call',
                    'Timestamp': {
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
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
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    None: None,
                    'TechnicalCommitteeMembership': 'Call',
                    'UpgradeCommittee': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
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
                    None: None,
                    'Asset': 'Call',
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
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
        'System': {
            'kill_prefix': {
                'prefix': 'Bytes',
                'subkeys': 'u32',
            },
            'kill_storage': {
                'keys': ['Bytes'],
            },
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
                    ('Bytes', 'Bytes'),
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
        'Utility': {
            'as_derivative': {
                'call': {
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Indices': {
                        'claim': {
                            'index': 'u32',
                        },
                        'force_transfer': {
                            'freeze': 'bool',
                            'index': 'u32',
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
                        },
                    },
                    None: None,
                    'Asset': 'Call',
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
                            'signature': '[u8; 64]',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
                },
                'index': 'u16',
            },
            'batch': {
                'calls': [
                    {
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'UpgradeCommittee': 'Call',
                        None: None,
                        'Treasury': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                ],
            },
            'batch_all': {
                'calls': [
                    {
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
                        'Nft': 'Call',
                        'Pips': 'Call',
                        'PolymeshContracts': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'Relayer': 'Call',
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Staking': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        None: None,
                        'MultiSig': 'Call',
                        'PolymeshCommittee': 'Call',
                        'Portfolio': 'Call',
                        'ProtocolFee': 'Call',
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                ],
            },
            'batch_atomic': {
                'calls': [
                    {
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        None: None,
                        'Asset': 'Call',
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                ],
            },
            'batch_old': {
                'calls': [
                    {
                        'Asset': 'Call',
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                ],
            },
            'batch_optimistic': {
                'calls': [
                    {
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
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Staking': 'Call',
                        None: None,
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'ProtocolFee': 'Call',
                        'Relayer': 'Call',
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                ],
            },
            'dispatch_as': {
                'as_origin': {
                    None: None,
                    'PolymeshCommittee': (
                        'Endorsed',
                    ),
                    'TechnicalCommittee': (
                        'Endorsed',
                    ),
                    'UpgradeCommittee': (
                        'Endorsed',
                    ),
                    'Void': (),
                    'system': {
                        'None': None,
                        'Root': None,
                        'Signed': 'AccountId',
                    },
                },
                'call': {
                    'Asset': 'Call',
                    None: None,
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
                },
            },
            'force_batch': {
                'calls': [
                    {
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                        None: None,
                    },
                ],
            },
            'relay_tx': {
                'call': {
                    'call': {
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                    'nonce': 'u64',
                },
                'signature': {
                    'Ecdsa': '[u8; 65]',
                    'Ed25519': '[u8; 64]',
                    'Sr25519': '[u8; 64]',
                },
                'target': 'AccountId',
            },
            'with_weight': {
                'call': {
                    'Asset': 'Call',
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                    None: None,
                    'TechnicalCommittee': 'Call',
                    'Timestamp': {
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
                },
                'weight': {
                    'proof_size': 'u64',
                    'ref_time': 'u64',
                },
            },
        },
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
### schedule_named
Schedule a named task.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `TaskName` | 
| when | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule_named', {
    'call': {
        'Asset': 'Call',
        'Babe': {
            'plan_config_change': {
                'config': {
                    None: None,
                    'V1': {
                        'allowed_slots': (
                            'PrimarySlots',
                            'PrimaryAndSecondaryPlainSlots',
                            'PrimaryAndSecondaryVRFSlots',
                        ),
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
                        'digest': {
                            'logs': [
                                'scale_info::15',
                            ],
                        },
                        'extrinsics_root': 'scale_info::11',
                        'number': 'u32',
                        'parent_hash': 'scale_info::11',
                        'state_root': 'scale_info::11',
                    },
                    'offender': '[u8; 32]',
                    'second_header': {
                        'digest': {
                            'logs': [
                                'scale_info::15',
                            ],
                        },
                        'extrinsics_root': 'scale_info::11',
                        'number': 'u32',
                        'parent_hash': 'scale_info::11',
                        'state_root': 'scale_info::11',
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
                        'digest': {
                            'logs': [
                                'scale_info::15',
                            ],
                        },
                        'extrinsics_root': 'scale_info::11',
                        'number': 'u32',
                        'parent_hash': 'scale_info::11',
                        'state_root': 'scale_info::11',
                    },
                    'offender': '[u8; 32]',
                    'second_header': {
                        'digest': {
                            'logs': [
                                'scale_info::15',
                            ],
                        },
                        'extrinsics_root': 'scale_info::11',
                        'number': 'u32',
                        'parent_hash': 'scale_info::11',
                        'state_root': 'scale_info::11',
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
                    'pending': 'scale_info::173',
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
                'code_hash': 'scale_info::11',
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
                'code_hash': 'scale_info::11',
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
                'code_hash': 'scale_info::11',
            },
            'set_code': {
                'code_hash': 'scale_info::11',
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
                        {
                            'choices': [
                                'Bytes',
                            ],
                            'info_link': 'Bytes',
                            'title': 'Bytes',
                        },
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
                        {
                            'choices': [
                                'Bytes',
                            ],
                            'info_link': 'Bytes',
                            'title': 'Bytes',
                        },
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
                        'Precommit': {
                            'first': (
                                'scale_info::464',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::464',
                                '[u8; 64]',
                            ),
                        },
                        'Prevote': {
                            'first': (
                                'scale_info::459',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::459',
                                '[u8; 64]',
                            ),
                        },
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
                        'Precommit': {
                            'first': (
                                'scale_info::464',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::464',
                                '[u8; 64]',
                            ),
                        },
                        'Prevote': {
                            'first': (
                                'scale_info::459',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::459',
                                '[u8; 64]',
                            ),
                        },
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
            'claim': {'index': 'u32'},
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
            'free': {'index': 'u32'},
            'freeze': {'index': 'u32'},
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
                'hash': 'scale_info::11',
            },
            'unnote_preimage': {
                'hash': 'scale_info::11',
            },
            'unrequest_preimage': {
                'hash': 'scale_info::11',
            },
        },
        'ProtocolFee': 'Call',
        'Relayer': 'Call',
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
                    None: None,
                    'Asset': 'Call',
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
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
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
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
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    None: None,
                    'TechnicalCommitteeMembership': 'Call',
                    'UpgradeCommittee': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
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
                    None: None,
                    'Asset': 'Call',
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
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
        None: None,
        'Staking': 'Call',
        'Statistics': 'Call',
        'Sto': 'Call',
        'System': {
            'kill_prefix': {
                'prefix': 'Bytes',
                'subkeys': 'u32',
            },
            'kill_storage': {
                'keys': ['Bytes'],
            },
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
                    ('Bytes', 'Bytes'),
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
        'Utility': {
            'as_derivative': {
                'call': {
                    None: None,
                    'Asset': 'Call',
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
                },
                'index': 'u16',
            },
            'batch': {
                'calls': [
                    {
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                        None: None,
                    },
                ],
            },
            'batch_all': {
                'calls': [
                    {
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
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        None: None,
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'TechnicalCommitteeMembership': 'Call',
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                ],
            },
            'batch_atomic': {
                'calls': [
                    {
                        'Asset': 'Call',
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                ],
            },
            'batch_old': {
                'calls': [
                    {
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
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        None: None,
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'TechnicalCommitteeMembership': 'Call',
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                ],
            },
            'batch_optimistic': {
                'calls': [
                    {
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
                        'Nft': 'Call',
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
                        'ProtocolFee': 'Call',
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
                        None: None,
                        'MultiSig': 'Call',
                        'Pips': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'Relayer': 'Call',
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                ],
            },
            'dispatch_as': {
                'as_origin': {
                    'PolymeshCommittee': (
                        'Endorsed',
                    ),
                    'TechnicalCommittee': (
                        'Endorsed',
                    ),
                    None: None,
                    'UpgradeCommittee': (
                        'Endorsed',
                    ),
                    'Void': (),
                    'system': {
                        'None': None,
                        'Root': None,
                        'Signed': 'AccountId',
                    },
                },
                'call': {
                    'Asset': 'Call',
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    None: None,
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
                },
            },
            'force_batch': {
                'calls': [
                    {
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                ],
            },
            'relay_tx': {
                'call': {
                    'call': {
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                    'nonce': 'u64',
                },
                'signature': {
                    'Ecdsa': '[u8; 65]',
                    'Ed25519': '[u8; 64]',
                    'Sr25519': '[u8; 64]',
                },
                'target': 'AccountId',
            },
            'with_weight': {
                'call': {
                    'Asset': 'Call',
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    None: None,
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
                },
                'weight': {
                    'proof_size': 'u64',
                    'ref_time': 'u64',
                },
            },
        },
    },
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
### schedule_named_after
Schedule a named task after a delay.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `TaskName` | 
| after | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule_named_after', {
    'after': 'u32',
    'call': {
        'Asset': 'Call',
        'Babe': {
            'plan_config_change': {
                'config': {
                    None: None,
                    'V1': {
                        'allowed_slots': (
                            'PrimarySlots',
                            'PrimaryAndSecondaryPlainSlots',
                            'PrimaryAndSecondaryVRFSlots',
                        ),
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
                        'digest': {
                            'logs': [
                                'scale_info::15',
                            ],
                        },
                        'extrinsics_root': 'scale_info::11',
                        'number': 'u32',
                        'parent_hash': 'scale_info::11',
                        'state_root': 'scale_info::11',
                    },
                    'offender': '[u8; 32]',
                    'second_header': {
                        'digest': {
                            'logs': [
                                'scale_info::15',
                            ],
                        },
                        'extrinsics_root': 'scale_info::11',
                        'number': 'u32',
                        'parent_hash': 'scale_info::11',
                        'state_root': 'scale_info::11',
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
                        'digest': {
                            'logs': [
                                'scale_info::15',
                            ],
                        },
                        'extrinsics_root': 'scale_info::11',
                        'number': 'u32',
                        'parent_hash': 'scale_info::11',
                        'state_root': 'scale_info::11',
                    },
                    'offender': '[u8; 32]',
                    'second_header': {
                        'digest': {
                            'logs': [
                                'scale_info::15',
                            ],
                        },
                        'extrinsics_root': 'scale_info::11',
                        'number': 'u32',
                        'parent_hash': 'scale_info::11',
                        'state_root': 'scale_info::11',
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
                    'pending': 'scale_info::173',
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
                'code_hash': 'scale_info::11',
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
                'code_hash': 'scale_info::11',
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
                'code_hash': 'scale_info::11',
            },
            'set_code': {
                'code_hash': 'scale_info::11',
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
                        {
                            'choices': [
                                'Bytes',
                            ],
                            'info_link': 'Bytes',
                            'title': 'Bytes',
                        },
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
                        {
                            'choices': [
                                'Bytes',
                            ],
                            'info_link': 'Bytes',
                            'title': 'Bytes',
                        },
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
                        'Precommit': {
                            'first': (
                                'scale_info::464',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::464',
                                '[u8; 64]',
                            ),
                        },
                        'Prevote': {
                            'first': (
                                'scale_info::459',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::459',
                                '[u8; 64]',
                            ),
                        },
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
                        'Precommit': {
                            'first': (
                                'scale_info::464',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::464',
                                '[u8; 64]',
                            ),
                        },
                        'Prevote': {
                            'first': (
                                'scale_info::459',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::459',
                                '[u8; 64]',
                            ),
                        },
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
            'claim': {'index': 'u32'},
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
            'free': {'index': 'u32'},
            'freeze': {'index': 'u32'},
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
                'hash': 'scale_info::11',
            },
            'unnote_preimage': {
                'hash': 'scale_info::11',
            },
            'unrequest_preimage': {
                'hash': 'scale_info::11',
            },
        },
        'ProtocolFee': 'Call',
        'Relayer': 'Call',
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
                    None: None,
                    'Asset': 'Call',
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
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
                    'Asset': 'Call',
                    None: None,
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
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
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'CddServiceProviders': 'Call',
                    'CommitteeMembership': 'Call',
                    'Contracts': {
                        'call': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'ExternalAgents': 'Call',
                    'Grandpa': {
                        'note_stalled': {
                            'best_finalized_block_number': 'u32',
                            'delay': 'u32',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'Indices': {
                        'claim': {
                            'index': 'u32',
                        },
                        'force_transfer': {
                            'freeze': 'bool',
                            'index': 'u32',
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
                        },
                    },
                    'UpgradeCommitteeMembership': 'Call',
                    None: None,
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                    'ComplianceManager': 'Call',
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
                            ],
                        },
                    },
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
                            'signature': '[u8; 64]',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
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
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Indices': {
                        'claim': {
                            'index': 'u32',
                        },
                        'force_transfer': {
                            'freeze': 'bool',
                            'index': 'u32',
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
                        },
                    },
                    None: None,
                    'Asset': 'Call',
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
                            'signature': '[u8; 64]',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
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
        'System': {
            'kill_prefix': {
                'prefix': 'Bytes',
                'subkeys': 'u32',
            },
            'kill_storage': {
                'keys': ['Bytes'],
            },
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
                    ('Bytes', 'Bytes'),
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
        'Utility': {
            'as_derivative': {
                'call': {
                    None: None,
                    'Asset': 'Call',
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
                },
                'index': 'u16',
            },
            'batch': {
                'calls': [
                    {
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                        None: None,
                    },
                ],
            },
            'batch_all': {
                'calls': [
                    {
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                        None: None,
                    },
                ],
            },
            'batch_atomic': {
                'calls': [
                    {
                        'Asset': 'Call',
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                ],
            },
            'batch_old': {
                'calls': [
                    {
                        'Asset': 'Call',
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        None: None,
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                ],
            },
            'batch_optimistic': {
                'calls': [
                    {
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                ],
            },
            'dispatch_as': {
                'as_origin': {
                    'PolymeshCommittee': (
                        'Endorsed',
                    ),
                    'TechnicalCommittee': (
                        'Endorsed',
                    ),
                    'UpgradeCommittee': (
                        'Endorsed',
                    ),
                    'Void': (),
                    'system': {
                        'None': None,
                        'Root': None,
                        'Signed': 'AccountId',
                    },
                    None: None,
                },
                'call': {
                    'Asset': 'Call',
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
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
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    None: None,
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
                },
            },
            'force_batch': {
                'calls': [
                    {
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
                        'Scheduler': {
                            'cancel': 'InnerStruct',
                            'cancel_named': 'InnerStruct',
                            'schedule': 'InnerStruct',
                            'schedule_after': 'InnerStruct',
                            'schedule_named': 'InnerStruct',
                            'schedule_named_after': 'InnerStruct',
                        },
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
                            'remark': 'InnerStruct',
                            'remark_with_event': 'InnerStruct',
                            'set_code': 'InnerStruct',
                            'set_code_without_checks': 'InnerStruct',
                            'set_heap_pages': 'InnerStruct',
                            'set_storage': 'InnerStruct',
                        },
                        'TechnicalCommitteeMembership': 'Call',
                        'UpgradeCommittee': 'Call',
                        None: None,
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'TechnicalCommittee': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                ],
            },
            'relay_tx': {
                'call': {
                    'call': {
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
                        'System': {
                            'kill_prefix': 'InnerStruct',
                            'kill_storage': 'InnerStruct',
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
                        'Utility': {
                            'as_derivative': 'InnerStruct',
                            'batch': 'InnerStruct',
                            'batch_all': 'InnerStruct',
                            'batch_atomic': 'InnerStruct',
                            'batch_old': 'InnerStruct',
                            'batch_optimistic': 'InnerStruct',
                            'dispatch_as': 'InnerStruct',
                            'force_batch': 'InnerStruct',
                            'relay_tx': 'InnerStruct',
                            'with_weight': 'InnerStruct',
                        },
                    },
                    'nonce': 'u64',
                },
                'signature': {
                    'Ecdsa': '[u8; 65]',
                    'Ed25519': '[u8; 64]',
                    'Sr25519': '[u8; 64]',
                },
                'target': 'AccountId',
            },
            'with_weight': {
                'call': {
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::324',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::339',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Indices': {
                        'claim': {
                            'index': 'u32',
                        },
                        'force_transfer': {
                            'freeze': 'bool',
                            'index': 'u32',
                            'new': 'scale_info::347',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::347',
                        },
                    },
                    None: None,
                    'Asset': 'Call',
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::165',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::165',
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
                            'ca_id': 'scale_info::165',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::165',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::165',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::172',
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
                            'dest': 'scale_info::347',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::347',
                            'gas_limit': 'u64',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate': {
                            'code_hash': 'scale_info::11',
                            'data': 'Bytes',
                            'gas_limit': 'scale_info::8',
                            'salt': 'Bytes',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'instantiate_old_weight': {
                            'code_hash': 'scale_info::11',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': 'scale_info::11',
                        },
                        'set_code': {
                            'code_hash': 'scale_info::11',
                            'dest': 'scale_info::347',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::536',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::165',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::165',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::165',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::165',
                        },
                        'vote': {
                            'ca_id': 'scale_info::165',
                            'votes': [
                                'scale_info::212',
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
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::456',
                            'key_owner_proof': 'scale_info::342',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::467',
                            'signature': '[u8; 64]',
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
                            'hash': 'scale_info::11',
                        },
                        'unnote_preimage': {
                            'hash': 'scale_info::11',
                        },
                        'unrequest_preimage': {
                            'hash': 'scale_info::11',
                        },
                    },
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                        'schedule_named': {
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                            'when': 'u32',
                        },
                        'schedule_named_after': {
                            'after': 'u32',
                            'call': 'scale_info::379',
                            'id': '[u8; 32]',
                            'maybe_periodic': (
                                None,
                                (
                                    'u32',
                                    'u32',
                                ),
                            ),
                            'priority': 'u8',
                        },
                    },
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::453',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': {
                        'kill_prefix': {
                            'prefix': 'Bytes',
                            'subkeys': 'u32',
                        },
                        'kill_storage': {
                            'keys': [
                                'Bytes',
                            ],
                        },
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
                        'set': {
                            'now': 'u64',
                        },
                    },
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': {
                        'as_derivative': {
                            'call': 'scale_info::379',
                            'index': 'u16',
                        },
                        'batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::523',
                            'call': 'scale_info::379',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::379',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::522',
                            'signature': 'scale_info::501',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::379',
                            'weight': 'scale_info::8',
                        },
                    },
                },
                'weight': {
                    'proof_size': 'u64',
                    'ref_time': 'u64',
                },
            },
        },
        None: None,
    },
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
## Events

---------
### CallUnavailable
The call for the provided hash was not found so the task has been aborted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<TaskName>` | ```(None, '[u8; 32]')```

---------
### Canceled
Canceled some task.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| when | `T::BlockNumber` | ```u32```
| index | `u32` | ```u32```

---------
### Dispatched
Dispatched some task.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<TaskName>` | ```(None, '[u8; 32]')```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### PeriodicFailed
The given task was unable to be renewed since the agenda is full at that block.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<TaskName>` | ```(None, '[u8; 32]')```

---------
### PermanentlyOverweight
The given task can never be executed since it is overweight.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<TaskName>` | ```(None, '[u8; 32]')```

---------
### Scheduled
Scheduled some task.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| when | `T::BlockNumber` | ```u32```
| index | `u32` | ```u32```

---------
## Storage functions

---------
### Agenda
 Items to be executed, indexed by the block number that they should be executed on.

#### Python
```python
result = substrate.query(
    'Scheduler', 'Agenda', ['u32']
)
```

#### Return value
```python
[
    (
        None,
        {
            'call': {
                'Inline': 'Bytes',
                'Legacy': 'InnerStruct',
                'Lookup': 'InnerStruct',
            },
            'maybe_id': (None, '[u8; 32]'),
            'maybe_periodic': (None, ('u32', 'u32')),
            'origin': {
                None: None,
                'PolymeshCommittee': 'scale_info::525',
                'TechnicalCommittee': 'scale_info::526',
                'UpgradeCommittee': 'scale_info::527',
                'Void': 'scale_info::528',
                'system': 'scale_info::524',
            },
            'priority': 'u8',
        },
    ),
]
```
---------
### IncompleteSince

#### Python
```python
result = substrate.query(
    'Scheduler', 'IncompleteSince', []
)
```

#### Return value
```python
'u32'
```
---------
### Lookup
 Lookup from a name to the block number and index of the task.

 For v3 -&gt; v4 the previously unbounded identities are Blake2-256 hashed to form the v4
 identities.

#### Python
```python
result = substrate.query(
    'Scheduler', 'Lookup', ['[u8; 32]']
)
```

#### Return value
```python
('u32', 'u32')
```
---------
## Constants

---------
### MaxScheduledPerBlock
 The maximum number of scheduled calls in the queue for a single block.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('Scheduler', 'MaxScheduledPerBlock')
```
---------
### MaximumWeight
 The maximum weight that may be scheduled per block for any dispatchables.
#### Value
```python
{'proof_size': 14757395258967641292, 'ref_time': 1600000000000}
```
#### Python
```python
constant = substrate.get_constant('Scheduler', 'MaximumWeight')
```
---------
## Errors

---------
### FailedToSchedule
Failed to schedule a call

---------
### Named
Attempt to use a non-named function on a named task.

---------
### NotFound
Cannot find the scheduled call.

---------
### RescheduleNoChange
Reschedule failed because it does not change scheduled time.

---------
### TargetBlockNumberInPast
Given target block number is in the past.

---------