
# TechnicalCommittee

---------
## Calls

---------
### set_expires_after
Changes the time after which a proposal expires.

\# Arguments
* `expiry` - The new expiry time.
#### Attributes
| Name | Type |
| -------- | -------- | 
| expiry | `MaybeBlock<T::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'TechnicalCommittee', 'set_expires_after', {
    'expiry': {
        'None': None,
        'Some': 'u32',
    },
}
)
```

---------
### set_release_coordinator
Changes the release coordinator.

\# Arguments
* `id` - The DID of the new release coordinator.

\# Errors
* `NotAMember`, If the new coordinator `id` is not part of the committee.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `IdentityId` | 

#### Python
```python
call = substrate.compose_call(
    'TechnicalCommittee', 'set_release_coordinator', {'id': '[u8; 32]'}
)
```

---------
### set_vote_threshold
Change the vote threshold the determines the winning proposal.
For e.g., for a simple majority use (1, 2) which represents the in-equation &quot;&gt;= 1/2&quot;.

\# Arguments
* `n` - Numerator of the fraction representing vote threshold.
* `d` - Denominator of the fraction representing vote threshold.
#### Attributes
| Name | Type |
| -------- | -------- | 
| n | `u32` | 
| d | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'TechnicalCommittee', 'set_vote_threshold', {'d': 'u32', 'n': 'u32'}
)
```

---------
### vote
Votes `approve`ingly (or not, if `false`)
on an existing `proposal` given by its hash, `index`.

\# Arguments
* `proposal` - A hash of the proposal to be voted on.
* `index` - The proposal index.
* `approve` - If `true` than this is a `for` vote, and `against` otherwise.

\# Errors
* `NotAMember`, if the `origin` is not a member of this committee.
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal | `T::Hash` | 
| index | `ProposalIndex` | 
| approve | `bool` | 

#### Python
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
### vote_or_propose
Proposes to the committee that `call` should be executed in its name.
Alternatively, if the hash of `call` has already been recorded, i.e., already proposed,
then this call counts as a vote, i.e., as if `vote_by_hash` was called.

\# Weight

The weight of this dispatchable is that of `call` as well as the complexity
for recording the vote itself.

\# Arguments
* `approve` - is this an approving vote?
  If the proposal doesn&\#x27;t exist, passing `false` will result in error `FirstVoteReject`.
* `call` - the call to propose for execution.

\# Errors
* `FirstVoteReject`, if `call` hasn&\#x27;t been proposed and `approve == false`.
* `NotAMember`, if the `origin` is not a member of this committee.
#### Attributes
| Name | Type |
| -------- | -------- | 
| approve | `bool` | 
| call | `Box<<T as Config<I>>::Proposal>` | 

#### Python
```python
call = substrate.compose_call(
    'TechnicalCommittee', 'vote_or_propose', {
    'approve': 'bool',
    'call': {
        'Asset': 'Call',
        'Authorship': {
            'set_uncles': {
                'new_uncles': [
                    {
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
                ],
            },
        },
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
                    'period': {
                        'amount': 'u64',
                        'unit': (
                            'Second',
                            'Minute',
                            'Hour',
                            'Day',
                            'Week',
                            'Month',
                            'Year',
                        ),
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
                                'scale_info::477',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::477',
                                '[u8; 64]',
                            ),
                        },
                        'Prevote': {
                            'first': (
                                'scale_info::472',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::472',
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
                                'scale_info::477',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::477',
                                '[u8; 64]',
                            ),
                        },
                        'Prevote': {
                            'first': (
                                'scale_info::472',
                                '[u8; 64]',
                            ),
                            'identity': '[u8; 32]',
                            'round_number': 'u64',
                            'second': (
                                'scale_info::472',
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
                        'set_uncles': {
                            'new_uncles': [
                                'scale_info::341',
                            ],
                        },
                    },
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::328',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::340',
                            'key_owner_proof': 'scale_info::343',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::340',
                            'key_owner_proof': 'scale_info::343',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::163',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::163',
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
                            'ca_id': 'scale_info::163',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::163',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::163',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::497',
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
                            'dest': 'scale_info::348',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::348',
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
                            'dest': 'scale_info::348',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::550',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::163',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::163',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::163',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::163',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::163',
                        },
                        'vote': {
                            'ca_id': 'scale_info::163',
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
                            'equivocation_proof': 'scale_info::469',
                            'key_owner_proof': 'scale_info::343',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::469',
                            'key_owner_proof': 'scale_info::343',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::480',
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
                            'new': 'scale_info::348',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::348',
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
                            'call': 'scale_info::392',
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
                            'call': 'scale_info::392',
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
                            'call': 'scale_info::392',
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
                            'call': 'scale_info::392',
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
                    'Sudo': 'Call',
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
                    'UpgradeCommittee': 'Call',
                    None: None,
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::466',
                            'proof': 'Bytes',
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
                    'Asset': 'Call',
                    'Authorship': {
                        'set_uncles': {
                            'new_uncles': [
                                'scale_info::341',
                            ],
                        },
                    },
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::328',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::340',
                            'key_owner_proof': 'scale_info::343',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::340',
                            'key_owner_proof': 'scale_info::343',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::163',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::163',
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
                            'ca_id': 'scale_info::163',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::163',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::163',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::497',
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
                            'dest': 'scale_info::348',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::348',
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
                            'dest': 'scale_info::348',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::550',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::163',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::163',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::163',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::163',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::163',
                        },
                        'vote': {
                            'ca_id': 'scale_info::163',
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
                            'equivocation_proof': 'scale_info::469',
                            'key_owner_proof': 'scale_info::343',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::469',
                            'key_owner_proof': 'scale_info::343',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::480',
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
                            'new': 'scale_info::348',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::348',
                        },
                    },
                    'MultiSig': 'Call',
                    'Nft': 'Call',
                    'Pips': 'Call',
                    'PolymeshContracts': 'Call',
                    'Rewards': 'Call',
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::466',
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
                    None: None,
                    'PolymeshCommittee': 'Call',
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
                            'call': 'scale_info::392',
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
                            'call': 'scale_info::392',
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
                            'call': 'scale_info::392',
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
                            'call': 'scale_info::392',
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
                    'Sudo': 'Call',
                    'TechnicalCommitteeMembership': 'Call',
                    'Timestamp': {
                        'set': {
                            'now': 'u64',
                        },
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
                        'set_uncles': {
                            'new_uncles': [
                                'scale_info::341',
                            ],
                        },
                    },
                    None: None,
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::328',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::340',
                            'key_owner_proof': 'scale_info::343',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::340',
                            'key_owner_proof': 'scale_info::343',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::163',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::163',
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
                            'ca_id': 'scale_info::163',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::163',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::163',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::497',
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
                            'dest': 'scale_info::348',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::348',
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
                            'dest': 'scale_info::348',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::550',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::163',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::163',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::163',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::163',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::163',
                        },
                        'vote': {
                            'ca_id': 'scale_info::163',
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
                            'equivocation_proof': 'scale_info::469',
                            'key_owner_proof': 'scale_info::343',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::469',
                            'key_owner_proof': 'scale_info::343',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::480',
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
                            'new': 'scale_info::348',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::348',
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
                            'call': 'scale_info::392',
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
                            'call': 'scale_info::392',
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
                            'call': 'scale_info::392',
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
                            'call': 'scale_info::392',
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
                            'keys': 'scale_info::466',
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
                            'keys': [
                                'Bytes',
                            ],
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
                        'set': {
                            'now': 'u64',
                        },
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
                    None: None,
                    'Asset': 'Call',
                    'Authorship': {
                        'set_uncles': {
                            'new_uncles': [
                                'scale_info::341',
                            ],
                        },
                    },
                    'Babe': {
                        'plan_config_change': {
                            'config': 'scale_info::328',
                        },
                        'report_equivocation': {
                            'equivocation_proof': 'scale_info::340',
                            'key_owner_proof': 'scale_info::343',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::340',
                            'key_owner_proof': 'scale_info::343',
                        },
                    },
                    'Balances': 'Call',
                    'Base': 'Call',
                    'Bridge': 'Call',
                    'CapitalDistribution': {
                        'claim': {
                            'ca_id': 'scale_info::163',
                        },
                        'distribute': {
                            'amount': 'u128',
                            'ca_id': 'scale_info::163',
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
                            'ca_id': 'scale_info::163',
                            'holder': '[u8; 32]',
                        },
                        'reclaim': {
                            'ca_id': 'scale_info::163',
                        },
                        'remove_distribution': {
                            'ca_id': 'scale_info::163',
                        },
                    },
                    'CddServiceProviders': 'Call',
                    'Checkpoint': {
                        'create_checkpoint': {
                            'ticker': '[u8; 12]',
                        },
                        'create_schedule': {
                            'schedule': 'scale_info::497',
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
                            'dest': 'scale_info::348',
                            'gas_limit': 'scale_info::8',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                            'value': 'u128',
                        },
                        'call_old_weight': {
                            'data': 'Bytes',
                            'dest': 'scale_info::348',
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
                            'dest': 'scale_info::348',
                        },
                        'upload_code': {
                            'code': 'Bytes',
                            'determinism': 'scale_info::550',
                            'storage_deposit_limit': (
                                None,
                                'u128',
                            ),
                        },
                    },
                    'CorporateAction': 'Call',
                    'CorporateBallot': {
                        'attach_ballot': {
                            'ca_id': 'scale_info::163',
                            'meta': 'scale_info::203',
                            'range': 'scale_info::202',
                            'rcv': 'bool',
                        },
                        'change_end': {
                            'ca_id': 'scale_info::163',
                            'end': 'u64',
                        },
                        'change_meta': {
                            'ca_id': 'scale_info::163',
                            'meta': 'scale_info::203',
                        },
                        'change_rcv': {
                            'ca_id': 'scale_info::163',
                            'rcv': 'bool',
                        },
                        'remove_ballot': {
                            'ca_id': 'scale_info::163',
                        },
                        'vote': {
                            'ca_id': 'scale_info::163',
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
                            'equivocation_proof': 'scale_info::469',
                            'key_owner_proof': 'scale_info::343',
                        },
                        'report_equivocation_unsigned': {
                            'equivocation_proof': 'scale_info::469',
                            'key_owner_proof': 'scale_info::343',
                        },
                    },
                    'Identity': 'Call',
                    'ImOnline': {
                        'heartbeat': {
                            'heartbeat': 'scale_info::480',
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
                            'new': 'scale_info::348',
                        },
                        'free': {
                            'index': 'u32',
                        },
                        'freeze': {
                            'index': 'u32',
                        },
                        'transfer': {
                            'index': 'u32',
                            'new': 'scale_info::348',
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
                            'call': 'scale_info::392',
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
                            'call': 'scale_info::392',
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
                            'call': 'scale_info::392',
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
                            'call': 'scale_info::392',
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
                            'keys': 'scale_info::466',
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
                            'keys': [
                                'Bytes',
                            ],
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
                        'set': {
                            'now': 'u64',
                        },
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
        'Utility': 'Call',
    },
}
)
```

---------
## Events

---------
### Approved
A motion was approved by the required threshold with the following
tally (yes votes, no votes and total seats given respectively as `MemberCount`).
Parameters: caller DID, proposal hash, yay vote count, nay vote count, total seats.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Hash` | ```[u8; 32]```
| None | `MemberCount` | ```u32```
| None | `MemberCount` | ```u32```
| None | `MemberCount` | ```u32```

---------
### Executed
A motion was executed; `DispatchResult` is `Ok(())` if returned without error.
Parameters: caller DID, proposal hash, result of proposal dispatch.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Hash` | ```[u8; 32]```
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### ExpiresAfterUpdated
Proposal expiry time has been updated.
Parameters: caller DID, new expiry time (if any).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `MaybeBlock<BlockNumber>` | ```{'Some': 'u32', 'None': None}```

---------
### FinalVotes
Final votes on a motion (given hash)
caller DID, ProposalIndex, Proposal hash, yes voters, no voter
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `ProposalIndex` | ```u32```
| None | `Hash` | ```[u8; 32]```
| None | `Vec<IdentityId>` | ```['[u8; 32]']```
| None | `Vec<IdentityId>` | ```['[u8; 32]']```

---------
### Proposed
A motion (given hash) has been proposed (by given account) with a threshold (given `MemberCount`).
Parameters: caller DID, proposal index, proposal hash.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `ProposalIndex` | ```u32```
| None | `Hash` | ```[u8; 32]```

---------
### Rejected
A motion was rejected by the required threshold with the following
tally (yes votes, no votes and total seats given respectively as `MemberCount`).
Parameters: caller DID, proposal hash, yay vote count, nay vote count, total seats.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Hash` | ```[u8; 32]```
| None | `MemberCount` | ```u32```
| None | `MemberCount` | ```u32```
| None | `MemberCount` | ```u32```

---------
### ReleaseCoordinatorUpdated
Release coordinator has been updated.
Parameters: caller DID, DID of the release coordinator.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Option<IdentityId>` | ```(None, '[u8; 32]')```

---------
### VoteRetracted
A vote on a motion (given hash) has been retracted.
caller DID, ProposalIndex, Proposal hash, vote that was retracted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `ProposalIndex` | ```u32```
| None | `Hash` | ```[u8; 32]```
| None | `bool` | ```bool```

---------
### VoteThresholdUpdated
Voting threshold has been updated
Parameters: caller DID, numerator, denominator
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `u32` | ```u32```
| None | `u32` | ```u32```

---------
### Voted
A motion (given hash) has been voted on by given account, leaving
a tally (yes votes, no votes and total seats given respectively as `MemberCount`).
caller DID, Proposal index, Proposal hash, current vote, yay vote count, nay vote count, total seats.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `ProposalIndex` | ```u32```
| None | `Hash` | ```[u8; 32]```
| None | `bool` | ```bool```
| None | `MemberCount` | ```u32```
| None | `MemberCount` | ```u32```
| None | `MemberCount` | ```u32```

---------
## Storage functions

---------
### ExpiresAfter
 Time after which a proposal will expire.

#### Python
```python
result = substrate.query(
    'TechnicalCommittee', 'ExpiresAfter', []
)
```

#### Return value
```python
{'None': None, 'Some': 'u32'}
```
---------
### Members
 The current members of the committee.

#### Python
```python
result = substrate.query(
    'TechnicalCommittee', 'Members', []
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### ProposalCount
 Proposals so far.

#### Python
```python
result = substrate.query(
    'TechnicalCommittee', 'ProposalCount', []
)
```

#### Return value
```python
'u32'
```
---------
### ProposalOf
 Actual proposal for a given hash.

#### Python
```python
result = substrate.query(
    'TechnicalCommittee', 'ProposalOf', ['[u8; 32]']
)
```

#### Return value
```python
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
                'V1': {'allowed_slots': 'scale_info::330', 'c': ('u64', 'u64')},
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
                'trie_nodes': ['Bytes'],
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
        'push_benefit': {'ca_id': {'local_id': 'u32', 'ticker': '[u8; 12]'}, 'holder': '[u8; 32]'},
        'reclaim': {'ca_id': {'local_id': 'u32', 'ticker': '[u8; 12]'}},
        'remove_distribution': {
            'ca_id': {'local_id': 'u32', 'ticker': '[u8; 12]'},
        },
    },
    'CddServiceProviders': 'Call',
    'Checkpoint': {
        'create_checkpoint': {'ticker': '[u8; 12]'},
        'create_schedule': {
            'schedule': {
                'period': {'amount': 'u64', 'unit': 'scale_info::173'},
                'remaining': 'u32',
                'start': (None, 'u64'),
            },
            'ticker': '[u8; 12]',
        },
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
            'code_hash': '[u8; 32]',
            'data': 'Bytes',
            'gas_limit': {'proof_size': 'u64', 'ref_time': 'u64'},
            'salt': 'Bytes',
            'storage_deposit_limit': (None, 'u128'),
            'value': 'u128',
        },
        'instantiate_old_weight': {
            'code_hash': '[u8; 32]',
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
        'remove_code': {'code_hash': '[u8; 32]'},
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
        'remove_ballot': {'ca_id': {'local_id': 'u32', 'ticker': '[u8; 12]'}},
        'vote': {
            'ca_id': {'local_id': 'u32', 'ticker': '[u8; 12]'},
            'votes': [{'fallback': (None, 'u16'), 'power': 'u128'}],
        },
    },
    'ExternalAgents': 'Call',
    'Grandpa': {
        'note_stalled': {'best_finalized_block_number': 'u32', 'delay': 'u32'},
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
                'trie_nodes': ['Bytes'],
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
                'network_state': {
                    'external_addresses': ['Bytes'],
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
        'note_preimage': {'bytes': 'Bytes'},
        'request_preimage': {'hash': '[u8; 32]'},
        'unnote_preimage': {'hash': '[u8; 32]'},
        'unrequest_preimage': {'hash': '[u8; 32]'},
    },
    'ProtocolFee': 'Call',
    'Relayer': 'Call',
    'Rewards': 'Call',
    'Scheduler': {
        'cancel': {'index': 'u32', 'when': 'u32'},
        'cancel_named': {'id': '[u8; 32]'},
        'schedule': {
            'call': {
                'Asset': 'Call',
                'Authorship': {'set_uncles': 'InnerStruct'},
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
                'ImOnline': {'heartbeat': 'InnerStruct'},
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
                'Session': {'purge_keys': None, 'set_keys': 'InnerStruct'},
                'Settlement': 'Call',
                'Statistics': 'Call',
                'Sto': 'Call',
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
                'TechnicalCommitteeMembership': 'Call',
                'Timestamp': {'set': 'InnerStruct'},
                None: None,
                'Staking': 'Call',
                'Sudo': 'Call',
                'TechnicalCommittee': 'Call',
                'Treasury': 'Call',
                'UpgradeCommittee': 'Call',
                'UpgradeCommitteeMembership': 'Call',
                'Utility': 'Call',
            },
            'maybe_periodic': (None, ('u32', 'u32')),
            'priority': 'u8',
            'when': 'u32',
        },
        'schedule_after': {
            'after': 'u32',
            'call': {
                'Asset': 'Call',
                'Authorship': {'set_uncles': 'InnerStruct'},
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
                'ImOnline': {'heartbeat': 'InnerStruct'},
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
                'Session': {'purge_keys': None, 'set_keys': 'InnerStruct'},
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
                'Timestamp': {'set': 'InnerStruct'},
                'Treasury': 'Call',
                'UpgradeCommittee': 'Call',
                'UpgradeCommitteeMembership': 'Call',
                'Utility': 'Call',
                None: None,
            },
            'maybe_periodic': (None, ('u32', 'u32')),
            'priority': 'u8',
        },
        'schedule_named': {
            'call': {
                'Asset': 'Call',
                'Authorship': {'set_uncles': 'InnerStruct'},
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
                'ImOnline': {'heartbeat': 'InnerStruct'},
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
                'Session': {'purge_keys': None, 'set_keys': 'InnerStruct'},
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
                'TechnicalCommitteeMembership': 'Call',
                'Timestamp': {'set': 'InnerStruct'},
                'Treasury': 'Call',
                None: None,
                'TechnicalCommittee': 'Call',
                'UpgradeCommittee': 'Call',
                'UpgradeCommitteeMembership': 'Call',
                'Utility': 'Call',
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
                'Authorship': {'set_uncles': 'InnerStruct'},
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
                'ExternalAgents': 'Call',
                'Grandpa': {
                    'note_stalled': 'InnerStruct',
                    'report_equivocation': 'InnerStruct',
                    'report_equivocation_unsigned': 'InnerStruct',
                },
                'Identity': 'Call',
                'ImOnline': {'heartbeat': 'InnerStruct'},
                'Indices': {
                    'claim': 'InnerStruct',
                    'force_transfer': 'InnerStruct',
                    'free': 'InnerStruct',
                    'freeze': 'InnerStruct',
                    'transfer': 'InnerStruct',
                },
                None: None,
                'Checkpoint': {
                    'create_checkpoint': 'InnerStruct',
                    'create_schedule': 'InnerStruct',
                    'remove_schedule': 'InnerStruct',
                    'set_schedules_max_complexity': 'InnerStruct',
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
                'Session': {'purge_keys': None, 'set_keys': 'InnerStruct'},
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
                'Timestamp': {'set': 'InnerStruct'},
                'Treasury': 'Call',
                'UpgradeCommittee': 'Call',
                'UpgradeCommitteeMembership': 'Call',
                'Utility': 'Call',
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
    'Sudo': 'Call',
    'System': {
        'kill_prefix': {'prefix': 'Bytes', 'subkeys': 'u32'},
        'kill_storage': {'keys': ['Bytes']},
        'placeholder_fill_block': None,
        'remark': {'remark': 'Bytes'},
        'remark_with_event': {'remark': 'Bytes'},
        'set_code': {'code': 'Bytes'},
        'set_code_without_checks': {'code': 'Bytes'},
        'set_heap_pages': {'pages': 'u64'},
        'set_storage': {'items': [('Bytes', 'Bytes')]},
    },
    'TechnicalCommittee': 'Call',
    'Timestamp': {'set': {'now': 'u64'}},
    'Treasury': 'Call',
    'UpgradeCommitteeMembership': 'Call',
    None: None,
    'TechnicalCommitteeMembership': 'Call',
    'UpgradeCommittee': 'Call',
    'Utility': 'Call',
}
```
---------
### Proposals
 The hashes of the active proposals.

#### Python
```python
result = substrate.query(
    'TechnicalCommittee', 'Proposals', []
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### ReleaseCoordinator
 Release coordinator.

#### Python
```python
result = substrate.query(
    'TechnicalCommittee', 'ReleaseCoordinator', []
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### StorageVersion
 Storage version.

#### Python
```python
result = substrate.query(
    'TechnicalCommittee', 'StorageVersion', []
)
```

#### Return value
```python
'u8'
```
---------
### VoteThreshold
 Vote threshold for an approval.

#### Python
```python
result = substrate.query(
    'TechnicalCommittee', 'VoteThreshold', []
)
```

#### Return value
```python
('u32', 'u32')
```
---------
### Voting
 PolymeshVotes on a given proposal, if it is ongoing.

#### Python
```python
result = substrate.query(
    'TechnicalCommittee', 'Voting', ['[u8; 32]']
)
```

#### Return value
```python
{
    'ayes': ['[u8; 32]'],
    'expiry': {'None': None, 'Some': 'u32'},
    'index': 'u32',
    'nays': ['[u8; 32]'],
}
```
---------
## Errors

---------
### DuplicateProposal
Duplicate proposal.

---------
### DuplicateVote
Duplicate votes are not allowed.

---------
### FirstVoteReject
First vote on a proposal creates it, so it must be an approval.
All proposals are motions to execute something as &quot;GC majority&quot;.
To reject e.g., a PIP, a motion to reject should be *approved*.

---------
### InvalidProportion
Proportion must be a rational number.

---------
### MismatchedVotingIndex
Mismatched voting index.

---------
### NoSuchProposal
No such proposal.

---------
### NotAMember
A DID isn&\#x27;t part of the committee.
The DID may either be a caller or some other context.

---------
### ProposalExpired
Proposal exists, but it has expired.

---------
### ProposalsLimitReached
Maximum number of proposals has been reached.

---------