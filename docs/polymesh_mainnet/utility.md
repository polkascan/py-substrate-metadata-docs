
# Utility

---------
## Calls

---------
### batch
Send a batch of dispatch calls.

May be called from any origin except `None`.

- `calls`: The calls to be dispatched from the same origin. The number of call must not
  exceed the constant: `batched_calls_limit` (available in constant metadata).

If origin is root then the calls are dispatched without checking origin filter. (This
includes bypassing `frame_system::Config::BaseCallFilter`).

\#\# Complexity
- O(C) where C is the number of calls to be batched.

This will return `Ok` in all circumstances. To determine the success of the batch, an
event is deposited. If a call failed and the batch was interrupted, then the
`BatchInterrupted` event is deposited, along with the number of successful calls made
and the error of the failed call. If all were successful, then the `BatchCompleted`
event is deposited.
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'batch', {
    'calls': [
        {
            'Asset': 'Call',
            'Babe': {
                'plan_config_change': {
                    'config': {
                        None: None,
                        'V1': {
                            'allowed_slots': 'scale_info::323',
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
            None: None,
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
                            'Precommit': 'scale_info::460',
                            'Prevote': 'scale_info::455',
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
                            'Precommit': 'scale_info::460',
                            'Prevote': 'scale_info::455',
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
                        'Utility': {
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
                        'UpgradeCommitteeMembership': 'Call',
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
                        'TechnicalCommitteeMembership': 'Call',
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        None: None,
                        'TechnicalCommittee': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Utility': {
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
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'CorporateAction': 'Call',
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        None: None,
                        'Base': 'Call',
                        'CddServiceProviders': 'Call',
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
            'Utility': {
                'batch': {
                    'calls': [
                        {
                            None: None,
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_all': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'Utility': 'scale_info::517',
                            None: None,
                            'UpgradeCommitteeMembership': 'Call',
                        },
                    ],
                },
                'batch_atomic': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'Session': 'scale_info::449',
                            'Staking': 'Call',
                            'UpgradeCommittee': 'Call',
                            None: None,
                            'PolymeshCommittee': 'Call',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Settlement': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_old': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshContracts': 'Call',
                            'Preimage': 'scale_info::538',
                            'Relayer': 'Call',
                            'Session': 'scale_info::449',
                            'Staking': 'Call',
                            'System': 'scale_info::299',
                            None: None,
                            'MultiSig': 'Call',
                            'PolymeshCommittee': 'Call',
                            'Portfolio': 'Call',
                            'ProtocolFee': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Settlement': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_optimistic': {
                    'calls': [
                        {
                            None: None,
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
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
                        None: None,
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
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
                },
                'force_batch': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'Timestamp': 'scale_info::341',
                            None: None,
                            'TechnicalCommitteeMembership': 'Call',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'relay_tx': {
                    'call': {
                        'call': {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Staking': 'Call',
                            'System': 'scale_info::299',
                            None: None,
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
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
                        'TechnicalCommitteeMembership': 'Call',
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        None: None,
                        'TechnicalCommittee': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Utility': {
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
                    'weight': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                },
            },
        },
    ],
}
)
```

---------
### batch_all
Send a batch of dispatch calls and atomically execute them.
The whole transaction will rollback and fail if any of the calls failed.

May be called from any origin except `None`.

- `calls`: The calls to be dispatched from the same origin. The number of call must not
  exceed the constant: `batched_calls_limit` (available in constant metadata).

If origin is root then the calls are dispatched without checking origin filter. (This
includes bypassing `frame_system::Config::BaseCallFilter`).

\#\# Complexity
- O(C) where C is the number of calls to be batched.
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'batch_all', {
    'calls': [
        {
            'Babe': {
                'plan_config_change': {
                    'config': {
                        None: None,
                        'V1': {
                            'allowed_slots': 'scale_info::323',
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
                            'Precommit': 'scale_info::460',
                            'Prevote': 'scale_info::455',
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
                            'Precommit': 'scale_info::460',
                            'Prevote': 'scale_info::455',
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
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Base': 'Call',
                        'CddServiceProviders': 'Call',
                        'CommitteeMembership': 'Call',
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
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'PolymeshCommittee': 'Call',
                        None: None,
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'ComplianceManager': 'Call',
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'ImOnline': {
                            'heartbeat': 'InnerStruct',
                        },
                        'MultiSig': 'Call',
                        'Nft': 'Call',
                        'Pips': 'Call',
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
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Base': 'Call',
                        'CddServiceProviders': 'Call',
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
                        None: None,
                        'Utility': {
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
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
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
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
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
                        None: None,
                        'CddServiceProviders': 'Call',
                        'CommitteeMembership': 'Call',
                        'ComplianceManager': 'Call',
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'Identity': 'Call',
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
            'Utility': {
                'batch': {
                    'calls': [
                        {
                            None: None,
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_all': {
                    'calls': [
                        {
                            None: None,
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_atomic': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            None: None,
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_old': {
                    'calls': [
                        {
                            None: None,
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_optimistic': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            None: None,
                            'Utility': 'scale_info::517',
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
                },
                'force_batch': {
                    'calls': [
                        {
                            None: None,
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'relay_tx': {
                    'call': {
                        'call': {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Session': 'scale_info::449',
                            'System': 'scale_info::299',
                            None: None,
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
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
                    'weight': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                },
            },
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
On failure, an event `BatchInterruptedOld(failure_idx, error)` is deposited.

May be called from root or a signed origin.

\# Parameters
- `calls`: The calls to be dispatched from the same origin.

\# Weight
- The sum of the weights of the `calls`.
- One event.

This will return `Ok` in all circumstances except an unsigned origin.
To determine the success of the batch, an event is deposited.
If any call failed, then `BatchInterruptedOld` is deposited.
If all were successful, then the `BatchCompletedOld` event is deposited.

POLYMESH: deprecated.
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'batch_atomic', {
    'calls': [
        {
            'Asset': 'Call',
            None: None,
            'Babe': {
                'plan_config_change': {
                    'config': {
                        None: None,
                        'V1': {
                            'allowed_slots': 'scale_info::323',
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
                            'Precommit': 'scale_info::460',
                            'Prevote': 'scale_info::455',
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
                            'Precommit': 'scale_info::460',
                            'Prevote': 'scale_info::455',
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
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Staking': 'Call',
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
                        None: None,
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
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
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
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
                    'maybe_periodic': (
                        None,
                        ('u32', 'u32'),
                    ),
                    'priority': 'u8',
                },
                'schedule_named': {
                    'call': {
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
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        None: None,
                        'CddServiceProviders': 'Call',
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
            'Utility': {
                'batch': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                            None: None,
                        },
                    ],
                },
                'batch_all': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                            None: None,
                        },
                    ],
                },
                'batch_atomic': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            None: None,
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_old': {
                    'calls': [
                        {
                            None: None,
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_optimistic': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'CddServiceProviders': 'Call',
                            'CommitteeMembership': 'Call',
                            'Contracts': 'scale_info::529',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'Indices': 'scale_info::343',
                            'System': 'scale_info::299',
                            None: None,
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'Checkpoint': 'scale_info::475',
                            'ComplianceManager': 'Call',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ImOnline': 'scale_info::463',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'dispatch_as': {
                    'as_origin': {
                        'PolymeshCommittee': (
                            'Endorsed',
                        ),
                        None: None,
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
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'CddServiceProviders': 'Call',
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
                },
                'force_batch': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                            None: None,
                        },
                    ],
                },
                'relay_tx': {
                    'call': {
                        'call': {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'Nft': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Preimage': 'scale_info::538',
                            'Relayer': 'Call',
                            'Session': 'scale_info::449',
                            'Sto': 'Call',
                            'Utility': 'scale_info::517',
                            None: None,
                            'Grandpa': 'scale_info::452',
                            'MultiSig': 'Call',
                            'Pips': 'Call',
                            'Portfolio': 'Call',
                            'ProtocolFee': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
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
                        None: None,
                        'ProtocolFee': 'Call',
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
                    'weight': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                },
            },
        },
    ],
}
)
```

---------
### batch_old
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
`BatchInterruptedOld` event is deposited, along with the number of successful calls made
and the error of the failed call. If all were successful, then the `BatchCompletedOld`
event is deposited.

POLYMESH: Renamed from `batch` and deprecated.
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'batch_old', {
    'calls': [
        {
            'Asset': 'Call',
            'Babe': {
                'plan_config_change': {
                    'config': {
                        None: None,
                        'V1': {
                            'allowed_slots': 'scale_info::323',
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
                            'Precommit': 'scale_info::460',
                            'Prevote': 'scale_info::455',
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
                            'Precommit': 'scale_info::460',
                            'Prevote': 'scale_info::455',
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
            'Relayer': 'Call',
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
                        (
                            'Bytes',
                            'Bytes',
                        ),
                    ],
                },
            },
            None: None,
            'PolymeshCommittee': 'Call',
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
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Bridge': 'Call',
                        None: None,
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
            'TechnicalCommittee': 'Call',
            'TechnicalCommitteeMembership': 'Call',
            'Timestamp': {
                'set': {'now': 'u64'},
            },
            'Treasury': 'Call',
            'UpgradeCommittee': 'Call',
            'UpgradeCommitteeMembership': 'Call',
            'Utility': {
                'batch': {
                    'calls': [
                        {
                            None: None,
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_all': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'Preimage': 'scale_info::538',
                            'Session': 'scale_info::449',
                            'Staking': 'Call',
                            'System': 'scale_info::299',
                            None: None,
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Settlement': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_atomic': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                            None: None,
                        },
                    ],
                },
                'batch_old': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'CddServiceProviders': 'Call',
                            'CommitteeMembership': 'Call',
                            'Contracts': 'scale_info::529',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'Indices': 'scale_info::343',
                            'PolymeshCommittee': 'Call',
                            None: None,
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'Checkpoint': 'scale_info::475',
                            'ComplianceManager': 'Call',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ImOnline': 'scale_info::463',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_optimistic': {
                    'calls': [
                        {
                            None: None,
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
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
                        None: None,
                        'system': {
                            'None': None,
                            'Root': None,
                            'Signed': 'AccountId',
                        },
                    },
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
                },
                'force_batch': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Indices': 'scale_info::343',
                            None: None,
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'relay_tx': {
                    'call': {
                        'call': {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            None: None,
                            'PolymeshCommittee': 'Call',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
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
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Base': 'Call',
                        'CddServiceProviders': 'Call',
                        'CommitteeMembership': 'Call',
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
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
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
                        None: None,
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'ComplianceManager': 'Call',
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
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
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
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
                    'weight': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                },
            },
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
If all were successful, then the `BatchCompletedOld` event is deposited.

POLYMESH: deprecated.
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'batch_optimistic', {
    'calls': [
        {
            'Asset': 'Call',
            'Babe': {
                'plan_config_change': {
                    'config': {
                        None: None,
                        'V1': {
                            'allowed_slots': 'scale_info::323',
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
                            'Precommit': 'scale_info::460',
                            'Prevote': 'scale_info::455',
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
                            'Precommit': 'scale_info::460',
                            'Prevote': 'scale_info::455',
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
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Base': 'Call',
                        'CddServiceProviders': 'Call',
                        'CommitteeMembership': 'Call',
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
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
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
                        None: None,
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'ComplianceManager': 'Call',
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
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
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
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
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
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
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
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
                        None: None,
                        'CddServiceProviders': 'Call',
                        'CommitteeMembership': 'Call',
                        'ComplianceManager': 'Call',
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'Identity': 'Call',
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
            None: None,
            'Utility': {
                'batch': {
                    'calls': [
                        {
                            None: None,
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_all': {
                    'calls': [
                        {
                            None: None,
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_atomic': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            None: None,
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_old': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            None: None,
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_optimistic': {
                    'calls': [
                        {
                            None: None,
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
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
                },
                'force_batch': {
                    'calls': [
                        {
                            None: None,
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'relay_tx': {
                    'call': {
                        'call': {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                            None: None,
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
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Balances': 'Call',
                        'Base': 'Call',
                        'CddServiceProviders': 'Call',
                        'CommitteeMembership': 'Call',
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
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'PolymeshCommittee': 'Call',
                        None: None,
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'ComplianceManager': 'Call',
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'ImOnline': {
                            'heartbeat': 'InnerStruct',
                        },
                        'MultiSig': 'Call',
                        'Nft': 'Call',
                        'Pips': 'Call',
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
                    'weight': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                },
            },
        },
    ],
}
)
```

---------
### dispatch_as
Dispatches a function call with a provided origin.

The dispatch origin for this call must be _Root_.

\#\# Complexity
- O(1).
#### Attributes
| Name | Type |
| -------- | -------- | 
| as_origin | `Box<T::PalletsOrigin>` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
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
    },
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
                        'extrinsics_root': '[u8; 32]',
                        'number': 'u32',
                        'parent_hash': '[u8; 32]',
                        'state_root': '[u8; 32]',
                    },
                    'offender': '[u8; 32]',
                    'second_header': {
                        'digest': {
                            'logs': [
                                'scale_info::15',
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
                        'extrinsics_root': '[u8; 32]',
                        'number': 'u32',
                        'parent_hash': '[u8; 32]',
                        'state_root': '[u8; 32]',
                    },
                    'offender': '[u8; 32]',
                    'second_header': {
                        'digest': {
                            'logs': [
                                'scale_info::15',
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
                                'scale_info::461',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::461',
                                '[u8; 64]',
                            ),
                        },
                        'Prevote': {
                            'first': (
                                'scale_info::456',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::456',
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
                                'scale_info::461',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::461',
                                '[u8; 64]',
                            ),
                        },
                        'Prevote': {
                            'first': (
                                'scale_info::456',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::456',
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
                            'config': 'scale_info::321',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
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
                            'dest': 'scale_info::344',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::344',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': '[u8; 32]',
                        },
                        'set_code': {
                            'code_hash': '[u8; 32]',
                            'dest': 'scale_info::344',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::533',
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
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::464',
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
                            'new': 'scale_info::344',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::344',
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
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'keys': 'scale_info::450',
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
                    'Utility': {
                        'batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::520',
                            'call': 'scale_info::376',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::519',
                            'signature': 'scale_info::498',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::376',
                            'weight': 'scale_info::8',
                        },
                    },
                    None: None,
                    'TechnicalCommitteeMembership': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
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
                            'config': 'scale_info::321',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
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
                            'dest': 'scale_info::344',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::344',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': '[u8; 32]',
                        },
                        'set_code': {
                            'code_hash': '[u8; 32]',
                            'dest': 'scale_info::344',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::533',
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
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::464',
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
                            'new': 'scale_info::344',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::344',
                        },
                    },
                    'MultiSig': 'Call',
                    'Nft': 'Call',
                    'Pips': 'Call',
                    'PolymeshCommittee': 'Call',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::450',
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
                        'batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::520',
                            'call': 'scale_info::376',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::519',
                            'signature': 'scale_info::498',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::376',
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
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::321',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
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
                            'dest': 'scale_info::344',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::344',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': '[u8; 32]',
                        },
                        'set_code': {
                            'code_hash': '[u8; 32]',
                            'dest': 'scale_info::344',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::533',
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
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::464',
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
                            'new': 'scale_info::344',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::344',
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
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'keys': 'scale_info::450',
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
                        'batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::520',
                            'call': 'scale_info::376',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::519',
                            'signature': 'scale_info::498',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::376',
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
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::321',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'CddServiceProviders': 'Call',
                    'CommitteeMembership': 'Call',
                    'Contracts': {
                        'call': {
                            'data': 'Bytes',
                            'dest': 'scale_info::344',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::344',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': '[u8; 32]',
                        },
                        'set_code': {
                            'code_hash': '[u8; 32]',
                            'dest': 'scale_info::344',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::533',
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
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
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
                            'new': 'scale_info::344',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::344',
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
                            'heartbeat': 'scale_info::464',
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
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'keys': 'scale_info::450',
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
                        'batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::520',
                            'call': 'scale_info::376',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::519',
                            'signature': 'scale_info::498',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::376',
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
        None: None,
        'Utility': {
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
                        'ProtocolFee': 'Call',
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
                        None: None,
                        'Portfolio': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
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
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
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
                        'Utility': {
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
                        'UpgradeCommitteeMembership': 'Call',
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
                        'Treasury': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        None: None,
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'UpgradeCommittee': 'Call',
                        'Utility': {
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
                        'CddServiceProviders': 'Call',
                        'CommitteeMembership': 'Call',
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
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
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
                        None: None,
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'ComplianceManager': 'Call',
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
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
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
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
                    None: None,
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
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::321',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
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
                            'dest': 'scale_info::344',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::344',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': '[u8; 32]',
                        },
                        'set_code': {
                            'code_hash': '[u8; 32]',
                            'dest': 'scale_info::344',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::533',
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
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::464',
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
                            'new': 'scale_info::344',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::344',
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
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'keys': 'scale_info::450',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'Utility': {
                        'batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::520',
                            'call': 'scale_info::376',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::519',
                            'signature': 'scale_info::498',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::376',
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
                        'CddServiceProviders': 'Call',
                        'CommitteeMembership': 'Call',
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
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
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
                        None: None,
                        'Bridge': 'Call',
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'ComplianceManager': 'Call',
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
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
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
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
                            'config': 'scale_info::321',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
                        },
                    },
                    'Indices': {
                        'claim': {
                            'index': 'u32',
                        },
                        'force_transfer': {
                            'freeze': 'bool',
                            'index': 'u32',
                            'new': 'scale_info::344',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::344',
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
                            'dest': 'scale_info::344',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::344',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': '[u8; 32]',
                        },
                        'set_code': {
                            'code_hash': '[u8; 32]',
                            'dest': 'scale_info::344',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::533',
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
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::464',
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
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'keys': 'scale_info::450',
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
                        'batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::520',
                            'call': 'scale_info::376',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::519',
                            'signature': 'scale_info::498',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::376',
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
}
)
```

---------
### force_batch
Send a batch of dispatch calls.
Unlike `batch`, it allows errors and won&\#x27;t interrupt.

May be called from any origin except `None`.

- `calls`: The calls to be dispatched from the same origin. The number of call must not
  exceed the constant: `batched_calls_limit` (available in constant metadata).

If origin is root then the calls are dispatch without checking origin filter. (This
includes bypassing `frame_system::Config::BaseCallFilter`).

\#\# Complexity
- O(C) where C is the number of calls to be batched.
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'force_batch', {
    'calls': [
        {
            'Asset': 'Call',
            'Babe': {
                'plan_config_change': {
                    'config': {
                        None: None,
                        'V1': {
                            'allowed_slots': 'scale_info::323',
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
            None: None,
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
                            'Precommit': 'scale_info::460',
                            'Prevote': 'scale_info::455',
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
                            'Precommit': 'scale_info::460',
                            'Prevote': 'scale_info::455',
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
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
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
                        'ExternalAgents': 'Call',
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
                        'Identity': 'Call',
                        'MultiSig': 'Call',
                        None: None,
                        'CddServiceProviders': 'Call',
                        'CommitteeMembership': 'Call',
                        'ComplianceManager': 'Call',
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
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
                        'UpgradeCommittee': 'Call',
                        None: None,
                        'Sto': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
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
            'Utility': {
                'batch': {
                    'calls': [
                        {
                            None: None,
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_all': {
                    'calls': [
                        {
                            'Babe': 'scale_info::335',
                            'Identity': 'Call',
                            None: None,
                            'Asset': 'Call',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_atomic': {
                    'calls': [
                        {
                            None: None,
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_old': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            None: None,
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_optimistic': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'Utility': 'scale_info::517',
                            None: None,
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
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
                        'PolymeshCommittee': 'Call',
                        'Portfolio': 'Call',
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Staking': 'Call',
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
                        None: None,
                        'Pips': 'Call',
                        'PolymeshContracts': 'Call',
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
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
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
                },
                'force_batch': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Session': 'scale_info::449',
                            'Staking': 'Call',
                            None: None,
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Settlement': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'relay_tx': {
                    'call': {
                        'call': {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            None: None,
                            'Utility': 'scale_info::517',
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
                        None: None,
                        'Utility': {
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
                    'weight': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                },
            },
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

POLYMESH: added.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `T::AccountId` | 
| signature | `T::OffChainSignature` | 
| call | `UniqueCall<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'relay_tx', {
    'call': {
        'call': {
            None: None,
            'Asset': 'Call',
            'Babe': {
                'plan_config_change': {
                    'config': {
                        None: None,
                        'V1': {
                            'allowed_slots': 'scale_info::323',
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
                            'Precommit': 'scale_info::460',
                            'Prevote': 'scale_info::455',
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
                            'Precommit': 'scale_info::460',
                            'Prevote': 'scale_info::455',
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
                        'PolymeshContracts': 'Call',
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'Relayer': 'Call',
                        'Settlement': 'Call',
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
                        None: None,
                        'MultiSig': 'Call',
                        'Pips': 'Call',
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
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
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
                        'Staking': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
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
                        'Staking': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
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
            'Utility': {
                'batch': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            None: None,
                            'PolymeshCommittee': 'Call',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_all': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            None: None,
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_atomic': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'Portfolio': 'Call',
                            'Session': 'scale_info::449',
                            'Staking': 'Call',
                            'System': 'scale_info::299',
                            None: None,
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Settlement': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_old': {
                    'calls': [
                        {
                            None: None,
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'batch_optimistic': {
                    'calls': [
                        {
                            None: None,
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            'Utility': 'scale_info::517',
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
                        None: None,
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
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
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
                },
                'force_batch': {
                    'calls': [
                        {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'Identity': 'Call',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'PolymeshContracts': 'Call',
                            'Portfolio': 'Call',
                            'Preimage': 'scale_info::538',
                            'ProtocolFee': 'Call',
                            'Relayer': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Session': 'scale_info::449',
                            'Settlement': 'Call',
                            'Staking': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            None: None,
                            'TechnicalCommitteeMembership': 'Call',
                            'UpgradeCommittee': 'Call',
                            'Utility': 'scale_info::517',
                        },
                    ],
                },
                'relay_tx': {
                    'call': {
                        'call': {
                            'Asset': 'Call',
                            'Babe': 'scale_info::335',
                            'Balances': 'Call',
                            'Base': 'Call',
                            'Bridge': 'Call',
                            'CapitalDistribution': 'scale_info::473',
                            'CddServiceProviders': 'Call',
                            'Checkpoint': 'scale_info::475',
                            'CommitteeMembership': 'Call',
                            'ComplianceManager': 'Call',
                            'Contracts': 'scale_info::529',
                            'CorporateAction': 'Call',
                            'CorporateBallot': 'scale_info::483',
                            'ExternalAgents': 'Call',
                            'Grandpa': 'scale_info::452',
                            'ImOnline': 'scale_info::463',
                            'Indices': 'scale_info::343',
                            'MultiSig': 'Call',
                            'Nft': 'Call',
                            'PolymeshContracts': 'Call',
                            'Preimage': 'scale_info::538',
                            'Relayer': 'Call',
                            'Session': 'scale_info::449',
                            'Staking': 'Call',
                            'TechnicalCommitteeMembership': 'Call',
                            'UpgradeCommitteeMembership': 'Call',
                            None: None,
                            'Identity': 'Call',
                            'Pips': 'Call',
                            'PolymeshCommittee': 'Call',
                            'Portfolio': 'Call',
                            'ProtocolFee': 'Call',
                            'Scheduler': 'scale_info::493',
                            'Settlement': 'Call',
                            'Statistics': 'Call',
                            'Sto': 'Call',
                            'System': 'scale_info::299',
                            'TechnicalCommittee': 'Call',
                            'Timestamp': 'scale_info::341',
                            'Treasury': 'Call',
                            'UpgradeCommittee': 'Call',
                            'Utility': 'scale_info::517',
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
                    'weight': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                },
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
}
)
```

---------
### with_weight
Dispatch a function call with a specified weight.

This function does not check the weight of the call, and instead allows the
Root origin to specify the weight of the call.

The dispatch origin for this call must be _Root_.
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::RuntimeCall>` | 
| weight | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'Utility', 'with_weight', {
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
                        'extrinsics_root': '[u8; 32]',
                        'number': 'u32',
                        'parent_hash': '[u8; 32]',
                        'state_root': '[u8; 32]',
                    },
                    'offender': '[u8; 32]',
                    'second_header': {
                        'digest': {
                            'logs': [
                                'scale_info::15',
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
                        'extrinsics_root': '[u8; 32]',
                        'number': 'u32',
                        'parent_hash': '[u8; 32]',
                        'state_root': '[u8; 32]',
                    },
                    'offender': '[u8; 32]',
                    'second_header': {
                        'digest': {
                            'logs': [
                                'scale_info::15',
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
                                'scale_info::461',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::461',
                                '[u8; 64]',
                            ),
                        },
                        'Prevote': {
                            'first': (
                                'scale_info::456',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::456',
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
                                'scale_info::461',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::461',
                                '[u8; 64]',
                            ),
                        },
                        'Prevote': {
                            'first': (
                                'scale_info::456',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::456',
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
                            'config': 'scale_info::321',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
                        },
                    },
                    'Indices': {
                        'claim': {
                            'index': 'u32',
                        },
                        'force_transfer': {
                            'freeze': 'bool',
                            'index': 'u32',
                            'new': 'scale_info::344',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::344',
                        },
                    },
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
                            'dest': 'scale_info::344',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::344',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': '[u8; 32]',
                        },
                        'set_code': {
                            'code_hash': '[u8; 32]',
                            'dest': 'scale_info::344',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::533',
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
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::464',
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
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'keys': 'scale_info::450',
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
                        'batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::520',
                            'call': 'scale_info::376',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::519',
                            'signature': 'scale_info::498',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::376',
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
                            'config': 'scale_info::321',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
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
                            'dest': 'scale_info::344',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::344',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': '[u8; 32]',
                        },
                        'set_code': {
                            'code_hash': '[u8; 32]',
                            'dest': 'scale_info::344',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::533',
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
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::464',
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
                            'new': 'scale_info::344',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::344',
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
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'keys': 'scale_info::450',
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
                        'batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::520',
                            'call': 'scale_info::376',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::519',
                            'signature': 'scale_info::498',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::376',
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
                    None: None,
                    'Asset': 'Call',
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::321',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
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
                            'dest': 'scale_info::344',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::344',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': '[u8; 32]',
                        },
                        'set_code': {
                            'code_hash': '[u8; 32]',
                            'dest': 'scale_info::344',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::533',
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
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::464',
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
                            'new': 'scale_info::344',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::344',
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
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'keys': 'scale_info::450',
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
                        'batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::520',
                            'call': 'scale_info::376',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::519',
                            'signature': 'scale_info::498',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::376',
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
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::321',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
                        },
                    },
                    'Indices': {
                        'claim': {
                            'index': 'u32',
                        },
                        'force_transfer': {
                            'freeze': 'bool',
                            'index': 'u32',
                            'new': 'scale_info::344',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::344',
                        },
                    },
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
                            'dest': 'scale_info::344',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::344',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': '[u8; 32]',
                        },
                        'set_code': {
                            'code_hash': '[u8; 32]',
                            'dest': 'scale_info::344',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::533',
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
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::464',
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
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'keys': 'scale_info::450',
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
                        'batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::520',
                            'call': 'scale_info::376',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::519',
                            'signature': 'scale_info::498',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::376',
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
        'Utility': {
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
                        'CddServiceProviders': 'Call',
                        'CommitteeMembership': 'Call',
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
                        'ExternalAgents': 'Call',
                        'Identity': 'Call',
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
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
                        None: None,
                        'CapitalDistribution': {
                            'claim': 'InnerStruct',
                            'distribute': 'InnerStruct',
                            'push_benefit': 'InnerStruct',
                            'reclaim': 'InnerStruct',
                            'remove_distribution': 'InnerStruct',
                        },
                        'Checkpoint': {
                            'create_checkpoint': 'InnerStruct',
                            'create_schedule': 'InnerStruct',
                            'remove_schedule': 'InnerStruct',
                            'set_schedules_max_complexity': 'InnerStruct',
                        },
                        'ComplianceManager': 'Call',
                        'CorporateAction': 'Call',
                        'CorporateBallot': {
                            'attach_ballot': 'InnerStruct',
                            'change_end': 'InnerStruct',
                            'change_meta': 'InnerStruct',
                            'change_rcv': 'InnerStruct',
                            'remove_ballot': 'InnerStruct',
                            'vote': 'InnerStruct',
                        },
                        'Grandpa': {
                            'note_stalled': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
                        },
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
                        'Settlement': 'Call',
                        'Staking': 'Call',
                        'Statistics': 'Call',
                        'Sto': 'Call',
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
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
                        'Preimage': {
                            'note_preimage': 'InnerStruct',
                            'request_preimage': 'InnerStruct',
                            'unnote_preimage': 'InnerStruct',
                            'unrequest_preimage': 'InnerStruct',
                        },
                        'Session': {
                            'purge_keys': None,
                            'set_keys': 'InnerStruct',
                        },
                        'Staking': 'Call',
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
                        None: None,
                        'PolymeshCommittee': 'Call',
                        'PolymeshContracts': 'Call',
                        'Portfolio': 'Call',
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
                        'TechnicalCommittee': 'Call',
                        'TechnicalCommitteeMembership': 'Call',
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommittee': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        'Utility': {
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
                        'Timestamp': {
                            'set': 'InnerStruct',
                        },
                        'Treasury': 'Call',
                        'UpgradeCommitteeMembership': 'Call',
                        None: None,
                        'TechnicalCommitteeMembership': 'Call',
                        'UpgradeCommittee': 'Call',
                        'Utility': {
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
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::321',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
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
                            'dest': 'scale_info::344',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::344',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': '[u8; 32]',
                        },
                        'set_code': {
                            'code_hash': '[u8; 32]',
                            'dest': 'scale_info::344',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::533',
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
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::464',
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
                            'new': 'scale_info::344',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::344',
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
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'keys': 'scale_info::450',
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
                        'batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::520',
                            'call': 'scale_info::376',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::519',
                            'signature': 'scale_info::498',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::376',
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
                            'config': 'scale_info::321',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::336',
                            'key_owner_proof': 'scale_info::339',
                        },
                    },
                    'Indices': {
                        'claim': {
                            'index': 'u32',
                        },
                        'force_transfer': {
                            'freeze': 'bool',
                            'index': 'u32',
                            'new': 'scale_info::344',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::344',
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
                            'dest': 'scale_info::344',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::344',
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
                            'gas_limit': 'scale_info::8',
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
                            'code_hash': '[u8; 32]',
                        },
                        'set_code': {
                            'code_hash': '[u8; 32]',
                            'dest': 'scale_info::344',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::533',
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
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::453',
                            'key_owner_proof': 'scale_info::339',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::464',
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
                    'Scheduler': {
                        'cancel': {
                            'index': 'u32',
                            'when': 'u32',
                        },
                        'cancel_named': {
                            'id': '[u8; 32]',
                        },
                        'schedule': {
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'call': 'scale_info::376',
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
                            'keys': 'scale_info::450',
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
                        'batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_all': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_atomic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_old': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'batch_optimistic': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'dispatch_as': {
                            'as_origin': 'scale_info::520',
                            'call': 'scale_info::376',
                        },
                        'force_batch': {
                            'calls': [
                                'scale_info::376',
                            ],
                        },
                        'relay_tx': {
                            'call': 'scale_info::519',
                            'signature': 'scale_info::498',
                            'target': 'AccountId',
                        },
                        'with_weight': {
                            'call': 'scale_info::376',
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
    },
    'weight': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
## Events

---------
### BatchCompleted
Batch of dispatches completed fully with no error.
#### Attributes
No attributes

---------
### BatchCompletedOld
Batch of dispatches completed fully with no error.
Includes a vector of event counts for each dispatch.
POLYMESH: event deprecated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventCounts` | ```['u32']```

---------
### BatchCompletedWithErrors
Batch of dispatches completed but has errors.
#### Attributes
No attributes

---------
### BatchInterrupted
Batch of dispatches did not complete fully. Index of first failing dispatch given, as
well as the error.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `u32` | ```u32```
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
### BatchInterruptedOld
Batch of dispatches did not complete fully.
Includes a vector of event counts for each dispatch and
the index of the first failing dispatch as well as the error.
POLYMESH: event deprecated.
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
POLYMESH: event deprecated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventCounts` | ```['u32']```
| None | `Vec<ErrorAt>` | ```[('u32', {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None})]```

---------
### DispatchedAs
A call was dispatched.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### ItemCompleted
A single item within a Batch of dispatches has completed with no error.
#### Attributes
No attributes

---------
### ItemFailed
A single item within a Batch of dispatches has completed with error.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
### RelayedTx
Relayed transaction.
POLYMESH: event.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| caller_did | `IdentityId` | ```[u8; 32]```
| target | `T::AccountId` | ```AccountId```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
## Storage functions

---------
### Nonces
 Nonce for `relay_tx`.
 POLYMESH: added.

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
## Constants

---------
### batched_calls_limit
 The limit on the number of batched calls.
#### Value
```python
10922
```
#### Python
```python
constant = substrate.get_constant('Utility', 'batched_calls_limit')
```
---------
## Errors

---------
### InvalidNonce
Provided nonce was invalid
If the provided nonce &lt; current nonce, the call was already executed
If the provided nonce &gt; current nonce, the call(s) before the current failed to execute
POLYMESH error

---------
### InvalidSignature
Offchain signature is invalid
POLYMESH error

---------
### TargetCddMissing
Target does not have a valid CDD
POLYMESH error

---------
### TooManyCalls
Too many calls batched.

---------