
# Pips

---------
## Calls

---------
### approve_committee_proposal
Approves the pending committee PIP given by the `id`.

\# Errors
* `BadOrigin` unless a GC voting majority executes this function.
* `NoSuchProposal` if the PIP with `id` doesn&\#x27;t exist.
* `IncorrectProposalState` if the proposal isn&\#x27;t pending.
* `NotByCommittee` if the proposal isn&\#x27;t by a committee.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `PipId` | 

#### Python
```python
call = substrate.compose_call(
    'Pips', 'approve_committee_proposal', {'id': 'u32'}
)
```

---------
### clear_snapshot
Clears the snapshot and emits the event `SnapshotCleared`.

\# Errors
* `NotACommitteeMember` - triggered when a non-GC-member executes the function.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Pips', 'clear_snapshot', {}
)
```

---------
### enact_snapshot_results
Enacts `results` for the PIPs in the snapshot queue.
The snapshot will be available for further enactments until it is cleared.

The `results` are encoded a list of `(id, result)` where `result` is applied to `id`.
Note that the snapshot priority queue is encoded with the *lowest priority first*.
so `results = [(id, Approve)]` will approve `SnapshotQueue[SnapshotQueue.len() - 1]`.

\# Errors
* `BadOrigin` - unless a GC voting majority executes this function.
* `CannotSkipPip` - a given PIP has already been skipped too many times.
* `SnapshotResultTooLarge` - on len(results) &gt; len(snapshot_queue).
* `SnapshotIdMismatch` - if:
  ```text
   ∃ (i ∈ 0..SnapshotQueue.len()).
     results[i].0 ≠ SnapshotQueue[SnapshotQueue.len() - i].id
  ```
   This is protects against clearing queue while GC is voting.
#### Attributes
| Name | Type |
| -------- | -------- | 
| results | `Vec<(PipId, SnapshotResult)>` | 

#### Python
```python
call = substrate.compose_call(
    'Pips', 'enact_snapshot_results', {
    'results': [
        (
            'u32',
            (
                'Approve',
                'Reject',
                'Skip',
            ),
        ),
    ],
}
)
```

---------
### execute_scheduled_pip
Internal dispatchable that handles execution of a PIP.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `PipId` | 

#### Python
```python
call = substrate.compose_call(
    'Pips', 'execute_scheduled_pip', {'id': 'u32'}
)
```

---------
### expire_scheduled_pip
Internal dispatchable that handles expiration of a PIP.
#### Attributes
| Name | Type |
| -------- | -------- | 
| did | `IdentityId` | 
| id | `PipId` | 

#### Python
```python
call = substrate.compose_call(
    'Pips', 'expire_scheduled_pip', {'did': '[u8; 32]', 'id': 'u32'}
)
```

---------
### propose
A network member creates a PIP by submitting a dispatchable which
changes the network in someway. A minimum deposit is required to open a new proposal.

\# Arguments
* `proposer` is either a signing key or committee.
   Used to understand whether this is a committee proposal and verified against `origin`.
* `proposal` a dispatchable call
* `deposit` minimum deposit value, which is ignored if `proposer` is a committee.
* `url` a link to a website for proposal discussion
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `Box<T::Proposal>` | 
| deposit | `Balance` | 
| url | `Option<Url>` | 
| description | `Option<PipDescription>` | 

#### Python
```python
call = substrate.compose_call(
    'Pips', 'propose', {
    'deposit': 'u128',
    'description': (None, 'Bytes'),
    'proposal': {
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
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    None: None,
                    'TechnicalCommitteeMembership': 'Call',
                    'Timestamp': {
                        'set': {
                            'now': 'u64',
                        },
                    },
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
                    'Treasury': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    None: None,
                    'Timestamp': {
                        'set': {
                            'now': 'u64',
                        },
                    },
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
                        'Indices': {
                            'claim': 'InnerStruct',
                            'force_transfer': 'InnerStruct',
                            'free': 'InnerStruct',
                            'freeze': 'InnerStruct',
                            'transfer': 'InnerStruct',
                        },
                        'PolymeshCommittee': 'Call',
                        'UpgradeCommittee': 'Call',
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
                        'Identity': 'Call',
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
                    'Treasury': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    None: None,
                    'Timestamp': {
                        'set': {
                            'now': 'u64',
                        },
                    },
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
                'weight': {
                    'proof_size': 'u64',
                    'ref_time': 'u64',
                },
            },
        },
        None: None,
    },
    'url': (None, 'Bytes'),
}
)
```

---------
### prune_proposal
Prune the PIP given by the `id`, refunding any funds not already refunded.
The PIP may not be active

This function is intended for storage garbage collection purposes.

\# Errors
* `BadOrigin` unless a GC voting majority executes this function.
* `NoSuchProposal` if the PIP with `id` doesn&\#x27;t exist.
* `IncorrectProposalState` if the proposal is active.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `PipId` | 

#### Python
```python
call = substrate.compose_call(
    'Pips', 'prune_proposal', {'id': 'u32'}
)
```

---------
### reject_proposal
Rejects the PIP given by the `id`, refunding any bonded funds,
assuming it hasn&\#x27;t been cancelled or executed.
Note that proposals scheduled-for-execution can also be rejected.

\# Errors
* `BadOrigin` unless a GC voting majority executes this function.
* `NoSuchProposal` if the PIP with `id` doesn&\#x27;t exist.
* `IncorrectProposalState` if the proposal was cancelled or executed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `PipId` | 

#### Python
```python
call = substrate.compose_call(
    'Pips', 'reject_proposal', {'id': 'u32'}
)
```

---------
### reschedule_execution
Updates the execution schedule of the PIP given by `id`.

\# Arguments
* `until` defines the future block where the enactment period will finished.
   `None` value means that enactment period is going to finish in the next block.

\# Errors
* `RescheduleNotByReleaseCoordinator` unless triggered by release coordinator.
* `IncorrectProposalState` unless the proposal was in a scheduled state.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `PipId` | 
| until | `Option<T::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'Pips', 'reschedule_execution', {'id': 'u32', 'until': (None, 'u32')}
)
```

---------
### set_active_pip_limit
Change the maximum number of active PIPs before community members cannot propose anything.
Can only be called by root.

\# Arguments
* `limit` of concurrent active PIPs.
#### Attributes
| Name | Type |
| -------- | -------- | 
| limit | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Pips', 'set_active_pip_limit', {'limit': 'u32'}
)
```

---------
### set_default_enactment_period
Change the default enactment period.
Can only be called by root.

\# Arguments
* `duration` the new default enactment period it takes for a scheduled PIP to be executed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| duration | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Pips', 'set_default_enactment_period', {'duration': 'u32'}
)
```

---------
### set_max_pip_skip_count
Change the maximum skip count (`max_pip_skip_count`).
Can only be called by root.

\# Arguments
* `max` skips before a PIP cannot be skipped by GC anymore.
#### Attributes
| Name | Type |
| -------- | -------- | 
| max | `SkippedCount` | 

#### Python
```python
call = substrate.compose_call(
    'Pips', 'set_max_pip_skip_count', {'max': 'u8'}
)
```

---------
### set_min_proposal_deposit
Change the minimum proposal deposit amount required to start a proposal.
Can only be called by root.

\# Arguments
* `deposit` the new min deposit required to start a proposal
#### Attributes
| Name | Type |
| -------- | -------- | 
| deposit | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Pips', 'set_min_proposal_deposit', {'deposit': 'u128'}
)
```

---------
### set_pending_pip_expiry
Change the amount of blocks after which a pending PIP is expired.
If `expiry` is `None` then PIPs never expire.
Can only be called by root.

\# Arguments
* `expiry` the block-time it takes for a still-`Pending` PIP to expire.
#### Attributes
| Name | Type |
| -------- | -------- | 
| expiry | `MaybeBlock<T::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'Pips', 'set_pending_pip_expiry', {
    'expiry': {
        'None': None,
        'Some': 'u32',
    },
}
)
```

---------
### set_prune_historical_pips
Change whether completed PIPs are pruned.
Can only be called by root.

\# Arguments
* `prune` specifies whether completed PIPs should be pruned.
#### Attributes
| Name | Type |
| -------- | -------- | 
| prune | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Pips', 'set_prune_historical_pips', {'prune': 'bool'}
)
```

---------
### snapshot
Takes a new snapshot of the current list of active &amp;&amp; pending PIPs.
The PIPs are then sorted into a priority queue based on each PIP&\#x27;s weight.

\# Errors
* `NotACommitteeMember` - triggered when a non-GC-member executes the function.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Pips', 'snapshot', {}
)
```

---------
### vote
Vote either in favor (`aye_or_nay` == true) or against a PIP with `id`.
The &quot;convinction&quot; or strength of the vote is given by `deposit`, which is reserved.

Note that `vote` is *not* additive.
That is, `vote(id, true, 50)` followed by `vote(id, true, 40)`
will first reserve `50` and then refund `50 - 10`, ending up with `40` in deposit.
To add atop of existing votes, you&\#x27;ll need `existing_deposit + addition`.

\# Arguments
* `id`, proposal id
* `aye_or_nay`, a bool representing for or against vote
* `deposit`, the &quot;conviction&quot; with which the vote is made.

\# Errors
* `NoSuchProposal` if `id` doesn&\#x27;t reference a valid PIP.
* `NotFromCommunity` if proposal was made by a committee.
* `IncorrectProposalState` if PIP isn&\#x27;t pending.
* `InsufficientDeposit` if `origin` cannot reserve `deposit - old_deposit`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `PipId` | 
| aye_or_nay | `bool` | 
| deposit | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Pips', 'vote', {
    'aye_or_nay': 'bool',
    'deposit': 'u128',
    'id': 'u32',
}
)
```

---------
## Events

---------
### ActivePipLimitChanged
The maximum number of active PIPs was changed.
(caller DID, old value, new value)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `u32` | ```u32```
| None | `u32` | ```u32```

---------
### DefaultEnactmentPeriodChanged
Default enactment period (in blocks) has been changed.
(caller DID, old period, new period)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `BlockNumber` | ```u32```
| None | `BlockNumber` | ```u32```

---------
### ExecutionCancellingFailed
Cancelling the PIP execution failed in the scheduler pallet.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PipId` | ```u32```

---------
### ExecutionScheduled
Execution of a PIP has been scheduled at specific block.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `PipId` | ```u32```
| None | `BlockNumber` | ```u32```

---------
### ExecutionSchedulingFailed
Scheduling of the PIP for execution failed in the scheduler pallet.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `PipId` | ```u32```
| None | `BlockNumber` | ```u32```

---------
### ExpiryScheduled
The PIP has been scheduled for expiry.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `PipId` | ```u32```
| None | `BlockNumber` | ```u32```

---------
### ExpirySchedulingFailed
Scheduling of the PIP for expiry failed in the scheduler pallet.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `PipId` | ```u32```
| None | `BlockNumber` | ```u32```

---------
### HistoricalPipsPruned
Pruning Historical PIPs is enabled or disabled (caller DID, old value, new value)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `bool` | ```bool```
| None | `bool` | ```bool```

---------
### MaxPipSkipCountChanged
The maximum times a PIP can be skipped was changed.
(caller DID, old value, new value)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `SkippedCount` | ```u8```
| None | `SkippedCount` | ```u8```

---------
### MinimumProposalDepositChanged
Minimum deposit amount modified
(caller DID, old amount, new amount)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### PendingPipExpiryChanged
Amount of blocks after which a pending PIP expires.
(caller DID, old expiry, new expiry)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `MaybeBlock<BlockNumber>` | ```{'Some': 'u32', 'None': None}```
| None | `MaybeBlock<BlockNumber>` | ```{'Some': 'u32', 'None': None}```

---------
### PipClosed
Pip has been closed, bool indicates whether data is pruned
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `PipId` | ```u32```
| None | `bool` | ```bool```

---------
### PipSkipped
A PIP in the snapshot queue was skipped.
(gc_did, pip_id, new_skip_count)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `PipId` | ```u32```
| None | `SkippedCount` | ```u8```

---------
### ProposalCreated
A PIP was made with a `Balance` stake.

\# Parameters:

Caller DID, Proposer, PIP ID, deposit, URL, description, expiry time, proposal data.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Proposer<AccountId>` | ```{'Community': 'AccountId', 'Committee': ('Technical', 'Upgrade')}```
| None | `PipId` | ```u32```
| None | `Balance` | ```u128```
| None | `Option<Url>` | ```(None, 'Bytes')```
| None | `Option<PipDescription>` | ```(None, 'Bytes')```
| None | `MaybeBlock<BlockNumber>` | ```{'Some': 'u32', 'None': None}```
| None | `ProposalData` | ```{'Hash': 'scale_info::11', 'Proposal': 'Bytes'}```

---------
### ProposalRefund
Refund proposal
(id, total amount)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `PipId` | ```u32```
| None | `Balance` | ```u128```

---------
### ProposalStateUpdated
Triggered each time the state of a proposal is amended
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `PipId` | ```u32```
| None | `ProposalState` | ```('Pending', 'Rejected', 'Scheduled', 'Failed', 'Executed', 'Expired')```

---------
### SnapshotCleared
The snapshot was cleared.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `SnapshotId` | ```u32```

---------
### SnapshotResultsEnacted
Results (e.g., approved, rejected, and skipped), were enacted for some PIPs.
(gc_did, snapshot_id_opt, skipped_pips_with_new_count, rejected_pips, approved_pips)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Option<SnapshotId>` | ```(None, 'u32')```
| None | `Vec<(PipId, SkippedCount)>` | ```[('u32', 'u8')]```
| None | `Vec<PipId>` | ```['u32']```
| None | `Vec<PipId>` | ```['u32']```

---------
### SnapshotTaken
A new snapshot was taken.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `SnapshotId` | ```u32```
| None | `Vec<SnapshottedPip>` | ```[{'id': 'u32', 'weight': ('bool', 'u128')}]```

---------
### Voted
`AccountId` voted `bool` on the proposal referenced by `PipId`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `PipId` | ```u32```
| None | `bool` | ```bool```
| None | `Balance` | ```u128```

---------
## Storage functions

---------
### ActivePipCount
 Total count of current pending or scheduled PIPs.

#### Python
```python
result = substrate.query(
    'Pips', 'ActivePipCount', []
)
```

#### Return value
```python
'u32'
```
---------
### ActivePipLimit
 The maximum allowed number for `ActivePipCount`.
 Once reached, new PIPs cannot be proposed by community members.

#### Python
```python
result = substrate.query(
    'Pips', 'ActivePipLimit', []
)
```

#### Return value
```python
'u32'
```
---------
### CommitteePips
 All existing PIPs where the proposer is a committee.
 This list is a cache of all ids in `Proposals` with `Proposer::Committee(_)`.

#### Python
```python
result = substrate.query(
    'Pips', 'CommitteePips', []
)
```

#### Return value
```python
['u32']
```
---------
### DefaultEnactmentPeriod
 Default enactment period that will be use after a proposal is accepted by GC.

#### Python
```python
result = substrate.query(
    'Pips', 'DefaultEnactmentPeriod', []
)
```

#### Return value
```python
'u32'
```
---------
### Deposits
 Those who have locked a deposit.
 proposal (id, proposer) -&gt; deposit

#### Python
```python
result = substrate.query(
    'Pips', 'Deposits', ['u32', 'AccountId']
)
```

#### Return value
```python
{'amount': 'u128', 'owner': 'AccountId'}
```
---------
### LiveQueue
 A live priority queue (lowest priority at index 0)
 of pending PIPs up to the active limit.
 Priority is defined by the `weight` in the `SnapshottedPip`.

 Unlike `SnapshotQueue`, this queue is live, getting updated with each vote cast.
 The snapshot is therefore essentially a point-in-time clone of this queue.

#### Python
```python
result = substrate.query(
    'Pips', 'LiveQueue', []
)
```

#### Return value
```python
[{'id': 'u32', 'weight': ('bool', 'u128')}]
```
---------
### MaxPipSkipCount
 Maximum times a PIP can be skipped before triggering `CannotSkipPip` in `enact_snapshot_results`.

#### Python
```python
result = substrate.query(
    'Pips', 'MaxPipSkipCount', []
)
```

#### Return value
```python
'u8'
```
---------
### MinimumProposalDeposit
 The minimum amount to be used as a deposit for community PIP creation.

#### Python
```python
result = substrate.query(
    'Pips', 'MinimumProposalDeposit', []
)
```

#### Return value
```python
'u128'
```
---------
### PendingPipExpiry
 How many blocks will it take, after a `Pending` PIP expires,
 assuming it has not transitioned to another `ProposalState`?

#### Python
```python
result = substrate.query(
    'Pips', 'PendingPipExpiry', []
)
```

#### Return value
```python
{'None': None, 'Some': 'u32'}
```
---------
### PipIdSequence
 Proposals so far. id can be used to keep track of PIPs off-chain.

#### Python
```python
result = substrate.query(
    'Pips', 'PipIdSequence', []
)
```

#### Return value
```python
'u32'
```
---------
### PipSkipCount
 The number of times a certain PIP has been skipped.
 Once a (configurable) threshhold is exceeded, a PIP cannot be skipped again.

#### Python
```python
result = substrate.query(
    'Pips', 'PipSkipCount', ['u32']
)
```

#### Return value
```python
'u8'
```
---------
### PipToSchedule
 Maps PIPs to the block at which they will be executed, if any.

#### Python
```python
result = substrate.query(
    'Pips', 'PipToSchedule', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### ProposalMetadata
 The metadata of the active proposals.

#### Python
```python
result = substrate.query(
    'Pips', 'ProposalMetadata', ['u32']
)
```

#### Return value
```python
{
    'created_at': 'u32',
    'description': (None, 'Bytes'),
    'expiry': {'None': None, 'Some': 'u32'},
    'id': 'u32',
    'transaction_version': 'u32',
    'url': (None, 'Bytes'),
}
```
---------
### ProposalResult
 PolymeshVotes on a given proposal, if it is ongoing.
 proposal id -&gt; vote count

#### Python
```python
result = substrate.query(
    'Pips', 'ProposalResult', ['u32']
)
```

#### Return value
```python
{
    'ayes_count': 'u32',
    'ayes_stake': 'u128',
    'nays_count': 'u32',
    'nays_stake': 'u128',
}
```
---------
### ProposalStates
 Proposal state for a given id.
 proposal id -&gt; proposalState

#### Python
```python
result = substrate.query(
    'Pips', 'ProposalStates', ['u32']
)
```

#### Return value
```python
('Pending', 'Rejected', 'Scheduled', 'Failed', 'Executed', 'Expired')
```
---------
### ProposalVotes
 Votes per Proposal and account. Used to avoid double vote issue.
 (proposal id, account) -&gt; Vote

#### Python
```python
result = substrate.query(
    'Pips', 'ProposalVotes', ['u32', 'AccountId']
)
```

#### Return value
```python
('bool', 'u128')
```
---------
### Proposals
 Actual proposal for a given id, if it&#x27;s current.
 proposal id -&gt; proposal

#### Python
```python
result = substrate.query(
    'Pips', 'Proposals', ['u32']
)
```

#### Return value
```python
{
    'id': 'u32',
    'proposal': {
        None: None,
        'Asset': 'Call',
        'Babe': {
            'plan_config_change': {'config': {None: None, 'V1': 'InnerStruct'}},
            'report_equivocation': {
                'equivocation_proof': {
                    'first_header': 'scale_info::340',
                    'offender': '[u8; 32]',
                    'second_header': 'scale_info::340',
                    'slot': 'u64',
                },
                'key_owner_proof': {
                    'session': 'u32',
                    'trie_nodes': ['Bytes'],
                    'validator_count': 'u32',
                },
            },
            'report_equivocation_unsigned': {
                'equivocation_proof': {
                    'first_header': 'scale_info::340',
                    'offender': '[u8; 32]',
                    'second_header': 'scale_info::340',
                    'slot': 'u64',
                },
                'key_owner_proof': {
                    'session': 'u32',
                    'trie_nodes': ['Bytes'],
                    'validator_count': 'u32',
                },
            },
        },
        'Balances': 'Call',
        'Base': 'Call',
        'Bridge': 'Call',
        'CapitalDistribution': {
            'claim': {'ca_id': {'local_id': 'u32', 'ticker': '[u8; 12]'}},
            'distribute': {
                'amount': 'u128',
                'ca_id': {'local_id': 'u32', 'ticker': '[u8; 12]'},
                'currency': '[u8; 12]',
                'expires_at': (None, 'u64'),
                'payment_at': 'u64',
                'per_share': 'u128',
                'portfolio': (None, 'u64'),
            },
            'push_benefit': {
                'ca_id': {'local_id': 'u32', 'ticker': '[u8; 12]'},
                'holder': '[u8; 32]',
            },
            'reclaim': {'ca_id': {'local_id': 'u32', 'ticker': '[u8; 12]'}},
            'remove_distribution': {
                'ca_id': {'local_id': 'u32', 'ticker': '[u8; 12]'},
            },
        },
        'CddServiceProviders': 'Call',
        'Checkpoint': {
            'create_checkpoint': {'ticker': '[u8; 12]'},
            'create_schedule': {'schedule': {'pending': 'scale_info::173'}, 'ticker': '[u8; 12]'},
            'remove_schedule': {'id': 'u64', 'ticker': '[u8; 12]'},
            'set_schedules_max_complexity': {'max_complexity': 'u64'},
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
                'gas_limit': {'proof_size': 'u64', 'ref_time': 'u64'},
                'storage_deposit_limit': (None, 'u128'),
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
                'storage_deposit_limit': (None, 'u128'),
                'value': 'u128',
            },
            'instantiate': {
                'code_hash': 'scale_info::11',
                'data': 'Bytes',
                'gas_limit': {'proof_size': 'u64', 'ref_time': 'u64'},
                'salt': 'Bytes',
                'storage_deposit_limit': (None, 'u128'),
                'value': 'u128',
            },
            'instantiate_old_weight': {
                'code_hash': 'scale_info::11',
                'data': 'Bytes',
                'gas_limit': 'u64',
                'salt': 'Bytes',
                'storage_deposit_limit': (None, 'u128'),
                'value': 'u128',
            },
            'instantiate_with_code': {
                'code': 'Bytes',
                'data': 'Bytes',
                'gas_limit': {'proof_size': 'u64', 'ref_time': 'u64'},
                'salt': 'Bytes',
                'storage_deposit_limit': (None, 'u128'),
                'value': 'u128',
            },
            'instantiate_with_code_old_weight': {
                'code': 'Bytes',
                'data': 'Bytes',
                'gas_limit': 'u64',
                'salt': 'Bytes',
                'storage_deposit_limit': (None, 'u128'),
                'value': 'u128',
            },
            'remove_code': {'code_hash': 'scale_info::11'},
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
                'determinism': ('Deterministic', 'AllowIndeterminism'),
                'storage_deposit_limit': (None, 'u128'),
            },
        },
        'CorporateAction': 'Call',
        'CorporateBallot': {
            'attach_ballot': {
                'ca_id': {'local_id': 'u32', 'ticker': '[u8; 12]'},
                'meta': {'motions': ['scale_info::206'], 'title': 'Bytes'},
                'range': {'end': 'u64', 'start': 'u64'},
                'rcv': 'bool',
            },
            'change_end': {'ca_id': {'local_id': 'u32', 'ticker': '[u8; 12]'}, 'end': 'u64'},
            'change_meta': {
                'ca_id': {'local_id': 'u32', 'ticker': '[u8; 12]'},
                'meta': {'motions': ['scale_info::206'], 'title': 'Bytes'},
            },
            'change_rcv': {'ca_id': {'local_id': 'u32', 'ticker': '[u8; 12]'}, 'rcv': 'bool'},
            'remove_ballot': {
                'ca_id': {'local_id': 'u32', 'ticker': '[u8; 12]'},
            },
            'vote': {
                'ca_id': {'local_id': 'u32', 'ticker': '[u8; 12]'},
                'votes': ['scale_info::212'],
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
                    'equivocation': 'scale_info::457',
                    'set_id': 'u64',
                },
                'key_owner_proof': {
                    'session': 'u32',
                    'trie_nodes': ['Bytes'],
                    'validator_count': 'u32',
                },
            },
            'report_equivocation_unsigned': {
                'equivocation_proof': {
                    'equivocation': 'scale_info::457',
                    'set_id': 'u64',
                },
                'key_owner_proof': {
                    'session': 'u32',
                    'trie_nodes': ['Bytes'],
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
                    'network_state': 'scale_info::468',
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
            'note_preimage': {'bytes': 'Bytes'},
            'request_preimage': {'hash': 'scale_info::11'},
            'unnote_preimage': {'hash': 'scale_info::11'},
            'unrequest_preimage': {'hash': 'scale_info::11'},
        },
        'ProtocolFee': 'Call',
        'Relayer': 'Call',
        'Scheduler': {
            'cancel': {'index': 'u32', 'when': 'u32'},
            'cancel_named': {'id': '[u8; 32]'},
            'schedule': {
                'call': {
                    'Asset': 'Call',
                    'Babe': 'scale_info::338',
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': 'scale_info::476',
                    'CddServiceProviders': 'Call',
                    'Checkpoint': 'scale_info::478',
                    'CommitteeMembership': 'Call',
                    'ComplianceManager': 'Call',
                    'Contracts': 'scale_info::532',
                    'CorporateAction': 'Call',
                    'CorporateBallot': 'scale_info::486',
                    'ExternalAgents': 'Call',
                    'Grandpa': 'scale_info::455',
                    'Identity': 'Call',
                    'ImOnline': 'scale_info::466',
                    'Indices': 'scale_info::346',
                    'MultiSig': 'Call',
                    'Nft': 'Call',
                    'Pips': 'Call',
                    'PolymeshCommittee': 'Call',
                    'PolymeshContracts': 'Call',
                    'Portfolio': 'Call',
                    'Preimage': 'scale_info::542',
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': 'scale_info::496',
                    'Session': 'scale_info::452',
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': 'scale_info::302',
                    'TechnicalCommittee': 'Call',
                    'TechnicalCommitteeMembership': 'Call',
                    'Timestamp': 'scale_info::344',
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': 'scale_info::520',
                    None: None,
                },
                'maybe_periodic': (None, ('u32', 'u32')),
                'priority': 'u8',
                'when': 'u32',
            },
            'schedule_after': {
                'after': 'u32',
                'call': {
                    'Asset': 'Call',
                    'Babe': 'scale_info::338',
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': 'scale_info::476',
                    'CddServiceProviders': 'Call',
                    'Checkpoint': 'scale_info::478',
                    'CommitteeMembership': 'Call',
                    'ComplianceManager': 'Call',
                    'Contracts': 'scale_info::532',
                    'CorporateAction': 'Call',
                    'CorporateBallot': 'scale_info::486',
                    'ExternalAgents': 'Call',
                    'Grandpa': 'scale_info::455',
                    'Identity': 'Call',
                    'ImOnline': 'scale_info::466',
                    'Indices': 'scale_info::346',
                    'MultiSig': 'Call',
                    'Nft': 'Call',
                    'Pips': 'Call',
                    'PolymeshCommittee': 'Call',
                    'PolymeshContracts': 'Call',
                    'Portfolio': 'Call',
                    'Preimage': 'scale_info::542',
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': 'scale_info::496',
                    'Session': 'scale_info::452',
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': 'scale_info::302',
                    'TechnicalCommittee': 'Call',
                    'TechnicalCommitteeMembership': 'Call',
                    'Timestamp': 'scale_info::344',
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'Utility': 'scale_info::520',
                    None: None,
                    'UpgradeCommitteeMembership': 'Call',
                },
                'maybe_periodic': (None, ('u32', 'u32')),
                'priority': 'u8',
            },
            'schedule_named': {
                'call': {
                    'Asset': 'Call',
                    'Babe': 'scale_info::338',
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': 'scale_info::476',
                    'CddServiceProviders': 'Call',
                    'Checkpoint': 'scale_info::478',
                    'CommitteeMembership': 'Call',
                    'ComplianceManager': 'Call',
                    'Contracts': 'scale_info::532',
                    'CorporateAction': 'Call',
                    'CorporateBallot': 'scale_info::486',
                    'ExternalAgents': 'Call',
                    'Grandpa': 'scale_info::455',
                    'Identity': 'Call',
                    'ImOnline': 'scale_info::466',
                    'Indices': 'scale_info::346',
                    'MultiSig': 'Call',
                    'Nft': 'Call',
                    'Pips': 'Call',
                    'PolymeshCommittee': 'Call',
                    'PolymeshContracts': 'Call',
                    'Portfolio': 'Call',
                    'Preimage': 'scale_info::542',
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': 'scale_info::496',
                    'Session': 'scale_info::452',
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': 'scale_info::302',
                    'TechnicalCommittee': 'Call',
                    'TechnicalCommitteeMembership': 'Call',
                    'Timestamp': 'scale_info::344',
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': 'scale_info::520',
                    None: None,
                },
                'id': '[u8; 32]',
                'maybe_periodic': (None, ('u32', 'u32')),
                'priority': 'u8',
                'when': 'u32',
            },
            'schedule_named_after': {
                'after': 'u32',
                'call': {
                    'Asset': 'Call',
                    'Babe': 'scale_info::338',
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': 'scale_info::476',
                    'CddServiceProviders': 'Call',
                    'Checkpoint': 'scale_info::478',
                    'CommitteeMembership': 'Call',
                    'ComplianceManager': 'Call',
                    'Contracts': 'scale_info::532',
                    'CorporateAction': 'Call',
                    'CorporateBallot': 'scale_info::486',
                    'ExternalAgents': 'Call',
                    'Grandpa': 'scale_info::455',
                    'Identity': 'Call',
                    'ImOnline': 'scale_info::466',
                    'Indices': 'scale_info::346',
                    'MultiSig': 'Call',
                    'Nft': 'Call',
                    'Pips': 'Call',
                    'PolymeshCommittee': 'Call',
                    'PolymeshContracts': 'Call',
                    'Portfolio': 'Call',
                    'Preimage': 'scale_info::542',
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': 'scale_info::496',
                    'Session': 'scale_info::452',
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': 'scale_info::302',
                    'TechnicalCommittee': 'Call',
                    'TechnicalCommitteeMembership': 'Call',
                    'Timestamp': 'scale_info::344',
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    None: None,
                    'Utility': 'scale_info::520',
                },
                'id': '[u8; 32]',
                'maybe_periodic': (None, ('u32', 'u32')),
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
            'kill_prefix': {'prefix': 'Bytes', 'subkeys': 'u32'},
            'kill_storage': {'keys': ['Bytes']},
            'remark': {'remark': 'Bytes'},
            'remark_with_event': {'remark': 'Bytes'},
            'set_code': {'code': 'Bytes'},
            'set_code_without_checks': {'code': 'Bytes'},
            'set_heap_pages': {'pages': 'u64'},
            'set_storage': {'items': [('Bytes', 'Bytes')]},
        },
        'TechnicalCommittee': 'Call',
        'TechnicalCommitteeMembership': 'Call',
        'Timestamp': {'set': {'now': 'u64'}},
        'Treasury': 'Call',
        'UpgradeCommittee': 'Call',
        'UpgradeCommitteeMembership': 'Call',
        'Utility': {
            'as_derivative': {
                'call': {
                    'Asset': 'Call',
                    'Babe': 'scale_info::338',
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': 'scale_info::476',
                    'CddServiceProviders': 'Call',
                    'Checkpoint': 'scale_info::478',
                    'CommitteeMembership': 'Call',
                    'ComplianceManager': 'Call',
                    'Contracts': 'scale_info::532',
                    'CorporateAction': 'Call',
                    'CorporateBallot': 'scale_info::486',
                    'ExternalAgents': 'Call',
                    'Grandpa': 'scale_info::455',
                    'Identity': 'Call',
                    'ImOnline': 'scale_info::466',
                    'Indices': 'scale_info::346',
                    'MultiSig': 'Call',
                    'Nft': 'Call',
                    'Pips': 'Call',
                    'PolymeshCommittee': 'Call',
                    'PolymeshContracts': 'Call',
                    'Portfolio': 'Call',
                    'Preimage': 'scale_info::542',
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': 'scale_info::496',
                    'Session': 'scale_info::452',
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': 'scale_info::302',
                    'TechnicalCommittee': 'Call',
                    'TechnicalCommitteeMembership': 'Call',
                    'Timestamp': 'scale_info::344',
                    'Treasury': 'Call',
                    None: None,
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': 'scale_info::520',
                },
                'index': 'u16',
            },
            'batch': {'calls': ['scale_info::379']},
            'batch_all': {'calls': ['scale_info::379']},
            'batch_atomic': {'calls': ['scale_info::379']},
            'batch_old': {'calls': ['scale_info::379']},
            'batch_optimistic': {'calls': ['scale_info::379']},
            'dispatch_as': {
                'as_origin': {
                    'PolymeshCommittee': 'scale_info::525',
                    None: None,
                    'TechnicalCommittee': 'scale_info::526',
                    'UpgradeCommittee': 'scale_info::527',
                    'Void': 'scale_info::528',
                    'system': 'scale_info::524',
                },
                'call': {
                    'Asset': 'Call',
                    'Babe': 'scale_info::338',
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': 'scale_info::476',
                    'CddServiceProviders': 'Call',
                    'Checkpoint': 'scale_info::478',
                    'CommitteeMembership': 'Call',
                    'ComplianceManager': 'Call',
                    'Contracts': 'scale_info::532',
                    'CorporateAction': 'Call',
                    'CorporateBallot': 'scale_info::486',
                    'ExternalAgents': 'Call',
                    'Grandpa': 'scale_info::455',
                    'Identity': 'Call',
                    'ImOnline': 'scale_info::466',
                    'Indices': 'scale_info::346',
                    'MultiSig': 'Call',
                    'Nft': 'Call',
                    'Pips': 'Call',
                    'PolymeshCommittee': 'Call',
                    'PolymeshContracts': 'Call',
                    'Portfolio': 'Call',
                    'Preimage': 'scale_info::542',
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': 'scale_info::496',
                    'Session': 'scale_info::452',
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': 'scale_info::302',
                    'TechnicalCommittee': 'Call',
                    'TechnicalCommitteeMembership': 'Call',
                    'Timestamp': 'scale_info::344',
                    None: None,
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': 'scale_info::520',
                },
            },
            'force_batch': {'calls': ['scale_info::379']},
            'relay_tx': {
                'call': {'call': 'scale_info::379', 'nonce': 'u64'},
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
                    'Babe': 'scale_info::338',
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': 'scale_info::476',
                    'CddServiceProviders': 'Call',
                    'Checkpoint': 'scale_info::478',
                    'CommitteeMembership': 'Call',
                    'ComplianceManager': 'Call',
                    'Contracts': 'scale_info::532',
                    'CorporateAction': 'Call',
                    'CorporateBallot': 'scale_info::486',
                    'ExternalAgents': 'Call',
                    'Grandpa': 'scale_info::455',
                    'Identity': 'Call',
                    'ImOnline': 'scale_info::466',
                    'Indices': 'scale_info::346',
                    'MultiSig': 'Call',
                    'Nft': 'Call',
                    'Pips': 'Call',
                    'PolymeshCommittee': 'Call',
                    'PolymeshContracts': 'Call',
                    'Portfolio': 'Call',
                    'Preimage': 'scale_info::542',
                    'ProtocolFee': 'Call',
                    'Relayer': 'Call',
                    'Scheduler': 'scale_info::496',
                    'Session': 'scale_info::452',
                    'Settlement': 'Call',
                    'Staking': 'Call',
                    'Statistics': 'Call',
                    'Sto': 'Call',
                    'System': 'scale_info::302',
                    'TechnicalCommittee': 'Call',
                    'TechnicalCommitteeMembership': 'Call',
                    'Timestamp': 'scale_info::344',
                    'Treasury': 'Call',
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    'Utility': 'scale_info::520',
                    None: None,
                },
                'weight': {'proof_size': 'u64', 'ref_time': 'u64'},
            },
        },
    },
    'proposer': {'Committee': ('Technical', 'Upgrade'), 'Community': 'AccountId'},
}
```
---------
### PruneHistoricalPips
 Determines whether historical PIP data is persisted or removed

#### Python
```python
result = substrate.query(
    'Pips', 'PruneHistoricalPips', []
)
```

#### Return value
```python
'bool'
```
---------
### SnapshotIdSequence
 Snapshots so far. id can be used to keep track of snapshots off-chain.

#### Python
```python
result = substrate.query(
    'Pips', 'SnapshotIdSequence', []
)
```

#### Return value
```python
'u32'
```
---------
### SnapshotMeta
 The metadata of the snapshot, if there is one.

#### Python
```python
result = substrate.query(
    'Pips', 'SnapshotMeta', []
)
```

#### Return value
```python
{'created_at': 'u32', 'id': 'u32', 'made_by': 'AccountId'}
```
---------
### SnapshotQueue
 The priority queue (lowest priority at index 0) of PIPs at the point of snapshotting.
 Priority is defined by the `weight` in the `SnapshottedPip`.

 A queued PIP can be skipped. Doing so bumps the `pip_skip_count`.
 Once a (configurable) threshhold is exceeded, a PIP cannot be skipped again.

#### Python
```python
result = substrate.query(
    'Pips', 'SnapshotQueue', []
)
```

#### Return value
```python
[{'id': 'u32', 'weight': ('bool', 'u128')}]
```
---------
### StorageVersion

#### Python
```python
result = substrate.query(
    'Pips', 'StorageVersion', []
)
```

#### Return value
```python
'u8'
```
---------
## Errors

---------
### CannotSkipPip
When enacting snapshot results, an unskippable PIP was skipped.

---------
### IncorrectDeposit
Proposer specifies an incorrect deposit

---------
### IncorrectProposalState
Proposal is not in the correct state

---------
### InsufficientDeposit
Proposer can&\#x27;t afford to lock minimum deposit

---------
### InvalidFutureBlockNumber
When a block number is less than current block number.

---------
### MissingCurrentIdentity
Missing current DID

---------
### NoSuchProposal
The proposal does not exist.

---------
### NotACommitteeMember
Not part of governance committee.

---------
### NotByCommittee
The given dispatchable call is not valid for this proposal.
The proposal must be by community, but isn&\#x27;t.

---------
### NotFromCommunity
The given dispatchable call is not valid for this proposal.
The proposal must be from the community, but isn&\#x27;t.

---------
### NumberOfVotesExceeded
When number of votes overflows.

---------
### ProposalNotInScheduledState
A proposal that is not in a scheduled state cannot be executed.

---------
### RescheduleNotByReleaseCoordinator
Only the GC release coordinator is allowed to reschedule proposal execution.

---------
### ScheduledProposalDoesntExist
Execution of a scheduled proposal failed because it is missing.

---------
### SnapshotIdMismatch
Tried to enact result for PIP with id different from that at the position in the queue.

---------
### SnapshotResultTooLarge
Tried to enact results for the snapshot queue overflowing its length.

---------
### StakeAmountOfVotesExceeded
When stake amount of a vote overflows.

---------
### TooManyActivePips
The current number of active (pending | scheduled) PIPs exceed the maximum
and the proposal is not by a committee.

---------