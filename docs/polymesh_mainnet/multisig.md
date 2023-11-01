
# MultiSig

---------
## Calls

---------
### accept_multisig_signer_as_identity
Accepts a multisig signer authorization given to signer&\#x27;s identity.

\# Arguments
* `auth_id` - Auth id of the authorization.
#### Attributes
| Name | Type |
| -------- | -------- | 
| auth_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'accept_multisig_signer_as_identity', {'auth_id': 'u64'}
)
```

---------
### accept_multisig_signer_as_key
Accepts a multisig signer authorization given to signer&\#x27;s key (AccountId).

\# Arguments
* `auth_id` - Auth id of the authorization.
#### Attributes
| Name | Type |
| -------- | -------- | 
| auth_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'accept_multisig_signer_as_key', {'auth_id': 'u64'}
)
```

---------
### add_multisig_signer
Adds a signer to the multisig. This must be called by the multisig itself.

\# Arguments
* `signer` - Signatory to add.
#### Attributes
| Name | Type |
| -------- | -------- | 
| signer | `Signatory<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'add_multisig_signer', {
    'signer': {
        'Account': 'AccountId',
        'Identity': '[u8; 32]',
    },
}
)
```

---------
### add_multisig_signers_via_creator
Adds a signer to the multisig. This must be called by the creator identity of the
multisig.

\# Arguments
* `multisig` - Address of the multi sig
* `signers` - Signatories to add.

\# Weight
`900_000_000 + 3_000_000 * signers.len()`
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| signers | `Vec<Signatory<T::AccountId>>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'add_multisig_signers_via_creator', {
    'multisig': 'AccountId',
    'signers': [
        {
            'Account': 'AccountId',
            'Identity': '[u8; 32]',
        },
    ],
}
)
```

---------
### approve_as_identity
Approves a multisig proposal using the caller&\#x27;s identity.

\# Arguments
* `multisig` - MultiSig address.
* `proposal_id` - Proposal id to approve.
If quorum is reached, the proposal will be immediately executed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| proposal_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'approve_as_identity', {
    'multisig': 'AccountId',
    'proposal_id': 'u64',
}
)
```

---------
### approve_as_key
Approves a multisig proposal using the caller&\#x27;s secondary key (`AccountId`).

\# Arguments
* `multisig` - MultiSig address.
* `proposal_id` - Proposal id to approve.
If quorum is reached, the proposal will be immediately executed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| proposal_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'approve_as_key', {
    'multisig': 'AccountId',
    'proposal_id': 'u64',
}
)
```

---------
### change_sigs_required
Changes the number of signatures required by a multisig. This must be called by the
multisig itself.

\# Arguments
* `sigs_required` - New number of required signatures.
#### Attributes
| Name | Type |
| -------- | -------- | 
| sigs_required | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'change_sigs_required', {'sigs_required': 'u64'}
)
```

---------
### change_sigs_required_via_creator
Changes the number of signatures required by a multisig. This must be called by the creator of the multisig.

\# Arguments
* `multisig_account` - The account identifier ([`AccountId`]) for the multi signature account.
* `signatures_required` - The number of required signatures.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig_account | `T::AccountId` | 
| signatures_required | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'change_sigs_required_via_creator', {
    'multisig_account': 'AccountId',
    'signatures_required': 'u64',
}
)
```

---------
### create_multisig
Creates a multisig

\# Arguments
* `signers` - Signers of the multisig (They need to accept authorization before they are actually added).
* `sigs_required` - Number of sigs required to process a multi-sig tx.
#### Attributes
| Name | Type |
| -------- | -------- | 
| signers | `Vec<Signatory<T::AccountId>>` | 
| sigs_required | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'create_multisig', {
    'signers': [
        {
            'Account': 'AccountId',
            'Identity': '[u8; 32]',
        },
    ],
    'sigs_required': 'u64',
}
)
```

---------
### create_or_approve_proposal_as_identity
Creates a multisig proposal if it hasn&\#x27;t been created or approves it if it has.

\# Arguments
* `multisig` - MultiSig address.
* `proposal` - Proposal to be voted on.
* `expiry` - Optional proposal expiry time.
* `auto_close` - Close proposal on receiving enough reject votes.
If this is 1 out of `m` multisig, the proposal will be immediately executed.
\#[deprecated(since = &quot;6.0.0&quot;, note = &quot;Please use the `create_proposal_as_identity` and `approve_as_identity` instead&quot;)]
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| proposal | `Box<T::Proposal>` | 
| expiry | `Option<T::Moment>` | 
| auto_close | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'create_or_approve_proposal_as_identity', {
    'auto_close': 'bool',
    'expiry': (None, 'u64'),
    'multisig': 'AccountId',
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
        'UpgradeCommittee': 'Call',
        None: None,
        'Identity': 'Call',
        'Pips': 'Call',
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
                    None: None,
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
            },
        },
        'Settlement': 'Call',
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
        'UpgradeCommitteeMembership': 'Call',
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
                        'Babe': {
                            'plan_config_change': 'InnerStruct',
                            'report_equivocation': 'InnerStruct',
                            'report_equivocation_unsigned': 'InnerStruct',
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
                    None: None,
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
### create_or_approve_proposal_as_key
Creates a multisig proposal if it hasn&\#x27;t been created or approves it if it has.

\# Arguments
* `multisig` - MultiSig address.
* `proposal` - Proposal to be voted on.
* `expiry` - Optional proposal expiry time.
* `auto_close` - Close proposal on receiving enough reject votes.
If this is 1 out of `m` multisig, the proposal will be immediately executed.
\#[deprecated(since = &quot;6.0.0&quot;, note = &quot;Please use the `create_proposal_as_key` and `approve_as_key` instead&quot;)]
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| proposal | `Box<T::Proposal>` | 
| expiry | `Option<T::Moment>` | 
| auto_close | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'create_or_approve_proposal_as_key', {
    'auto_close': 'bool',
    'expiry': (None, 'u64'),
    'multisig': 'AccountId',
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
                    'Identity': 'Call',
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
                    None: None,
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
        None: None,
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
            'batch_atomic': {
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
                    'system': {
                        'None': None,
                        'Root': None,
                        'Signed': 'AccountId',
                    },
                    None: None,
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
                    None: None,
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
                        'TechnicalCommitteeMembership': 'Call',
                        None: None,
                        'TechnicalCommittee': 'Call',
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
### create_proposal_as_identity
Creates a multisig proposal

\# Arguments
* `multisig` - MultiSig address.
* `proposal` - Proposal to be voted on.
* `expiry` - Optional proposal expiry time.
* `auto_close` - Close proposal on receiving enough reject votes.
If this is 1 out of `m` multisig, the proposal will be immediately executed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| proposal | `Box<T::Proposal>` | 
| expiry | `Option<T::Moment>` | 
| auto_close | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'create_proposal_as_identity', {
    'auto_close': 'bool',
    'expiry': (None, 'u64'),
    'multisig': 'AccountId',
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
        'MultiSig': 'Call',
        'Nft': 'Call',
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
        'UpgradeCommittee': 'Call',
        None: None,
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
        'Pips': 'Call',
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
                    None: None,
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
                    'UpgradeCommittee': 'Call',
                    None: None,
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
            },
        },
        'Settlement': 'Call',
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
        'UpgradeCommitteeMembership': 'Call',
        'Utility': {
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
                        None: None,
                        'Relayer': 'Call',
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
                    'system': {
                        'None': None,
                        'Root': None,
                        'Signed': 'AccountId',
                    },
                    None: None,
                    'TechnicalCommittee': (
                        'Endorsed',
                    ),
                    'UpgradeCommittee': (
                        'Endorsed',
                    ),
                    'Void': (),
                },
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
                    None: None,
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
### create_proposal_as_key
Creates a multisig proposal

\# Arguments
* `multisig` - MultiSig address.
* `proposal` - Proposal to be voted on.
* `expiry` - Optional proposal expiry time.
* `auto_close` - Close proposal on receiving enough reject votes.
If this is 1 out of `m` multisig, the proposal will be immediately executed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| proposal | `Box<T::Proposal>` | 
| expiry | `Option<T::Moment>` | 
| auto_close | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'create_proposal_as_key', {
    'auto_close': 'bool',
    'expiry': (None, 'u64'),
    'multisig': 'AccountId',
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
                    None: None,
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
                    'Staking': 'Call',
                    None: None,
                    'Session': {
                        'purge_keys': None,
                        'set_keys': {
                            'keys': 'scale_info::450',
                            'proof': 'Bytes',
                        },
                    },
                    'Settlement': 'Call',
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
                    None: None,
                },
                'weight': {
                    'proof_size': 'u64',
                    'ref_time': 'u64',
                },
            },
        },
        None: None,
    },
}
)
```

---------
### execute_scheduled_proposal
Root callable extrinsic, used as an internal call for executing scheduled multisig proposal.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| proposal_id | `u64` | 
| multisig_did | `IdentityId` | 
| _proposal_weight | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'execute_scheduled_proposal', {
    '_proposal_weight': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
    'multisig': 'AccountId',
    'multisig_did': '[u8; 32]',
    'proposal_id': 'u64',
}
)
```

---------
### make_multisig_primary
Adds a multisig as the primary key of the current did if the current DID is the creator
of the multisig.

\# Arguments
* `multi_sig` - multi sig address
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| optional_cdd_auth_id | `Option<u64>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'make_multisig_primary', {
    'multisig': 'AccountId',
    'optional_cdd_auth_id': (
        None,
        'u64',
    ),
}
)
```

---------
### make_multisig_secondary
Adds a multisig as a secondary key of current did if the current did is the creator of the
multisig.

\# Arguments
* `multisig` - multi sig address
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'make_multisig_secondary', {'multisig': 'AccountId'}
)
```

---------
### reject_as_identity
Rejects a multisig proposal using the caller&\#x27;s identity.

\# Arguments
* `multisig` - MultiSig address.
* `proposal_id` - Proposal id to reject.
If quorum is reached, the proposal will be immediately executed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| proposal_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'reject_as_identity', {
    'multisig': 'AccountId',
    'proposal_id': 'u64',
}
)
```

---------
### reject_as_key
Rejects a multisig proposal using the caller&\#x27;s secondary key (`AccountId`).

\# Arguments
* `multisig` - MultiSig address.
* `proposal_id` - Proposal id to reject.
If quorum is reached, the proposal will be immediately executed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| proposal_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'reject_as_key', {
    'multisig': 'AccountId',
    'proposal_id': 'u64',
}
)
```

---------
### remove_creator_controls
Removes the creator ability to call `add_multisig_signers_via_creator`, `remove_multisig_signers_via_creator`
and `change_sigs_required_via_creator`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig_account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'remove_creator_controls', {'multisig_account': 'AccountId'}
)
```

---------
### remove_multisig_signer
Removes a signer from the multisig. This must be called by the multisig itself.

\# Arguments
* `signer` - Signatory to remove.
#### Attributes
| Name | Type |
| -------- | -------- | 
| signer | `Signatory<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'remove_multisig_signer', {
    'signer': {
        'Account': 'AccountId',
        'Identity': '[u8; 32]',
    },
}
)
```

---------
### remove_multisig_signers_via_creator
Removes a signer from the multisig.
This must be called by the creator identity of the multisig.

\# Arguments
* `multisig` - Address of the multisig.
* `signers` - Signatories to remove.

\# Weight
`900_000_000 + 3_000_000 * signers.len()`
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| signers | `Vec<Signatory<T::AccountId>>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'remove_multisig_signers_via_creator', {
    'multisig': 'AccountId',
    'signers': [
        {
            'Account': 'AccountId',
            'Identity': '[u8; 32]',
        },
    ],
}
)
```

---------
## Events

---------
### MultiSigCreated
Event emitted after creation of a multisig.
Arguments: caller DID, multisig address, signers (pending approval), signatures required.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `AccountId` | ```AccountId```
| None | `Vec<Signatory<AccountId>>` | ```[{'Identity': '[u8; 32]', 'Account': 'AccountId'}]```
| None | `u64` | ```u64```

---------
### MultiSigSignaturesRequiredChanged
Event emitted when the number of required signatures is changed.
Arguments: caller DID, multisig, new required signatures.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `u64` | ```u64```

---------
### MultiSigSignerAdded
Event emitted when a signatory is added.
Arguments: caller DID, multisig, added signer.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Signatory<AccountId>` | ```{'Identity': '[u8; 32]', 'Account': 'AccountId'}```

---------
### MultiSigSignerAuthorized
Event emitted when a multisig signatory is authorized to be added.
Arguments: caller DID, multisig, authorized signer.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Signatory<AccountId>` | ```{'Identity': '[u8; 32]', 'Account': 'AccountId'}```

---------
### MultiSigSignerRemoved
Event emitted when a multisig signatory is removed.
Arguments: caller DID, multisig, removed signer.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Signatory<AccountId>` | ```{'Identity': '[u8; 32]', 'Account': 'AccountId'}```

---------
### ProposalAdded
Event emitted after adding a proposal.
Arguments: caller DID, multisig, proposal ID.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `u64` | ```u64```

---------
### ProposalApproved
Event emitted when the proposal get approved.
Arguments: caller DID, multisig, authorized signer, proposal id.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Signatory<AccountId>` | ```{'Identity': '[u8; 32]', 'Account': 'AccountId'}```
| None | `u64` | ```u64```

---------
### ProposalExecuted
Event emitted when a proposal is executed.
Arguments: caller DID, multisig, proposal ID, result.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `u64` | ```u64```
| None | `bool` | ```bool```

---------
### ProposalExecutionFailed
Event emitted when there&\#x27;s an error in proposal execution
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
### ProposalRejected
Event emitted when a proposal is rejected.
Arguments: caller DID, multisig, proposal ID.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `u64` | ```u64```

---------
### ProposalRejectionVote
Event emitted when a vote is cast in favor of rejecting a proposal.
Arguments: caller DID, multisig, authorized signer, proposal id.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Signatory<AccountId>` | ```{'Identity': '[u8; 32]', 'Account': 'AccountId'}```
| None | `u64` | ```u64```

---------
### SchedulingFailed
Scheduling of proposal fails.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
## Storage functions

---------
### LostCreatorPrivileges
 Tracks creators who are no longer allowed to call via_creator extrinsics.

#### Python
```python
result = substrate.query(
    'MultiSig', 'LostCreatorPrivileges', ['[u8; 32]']
)
```

#### Return value
```python
'bool'
```
---------
### MultiSigNonce
 Nonce to ensure unique MultiSig addresses are generated; starts from 1.

#### Python
```python
result = substrate.query(
    'MultiSig', 'MultiSigNonce', []
)
```

#### Return value
```python
'u64'
```
---------
### MultiSigSigners
 Signers of a multisig. (multisig, signer) =&gt; bool.

#### Python
```python
result = substrate.query(
    'MultiSig', 'MultiSigSigners', [
    'AccountId',
    {
        'Account': 'AccountId',
        'Identity': '[u8; 32]',
    },
]
)
```

#### Return value
```python
'bool'
```
---------
### MultiSigSignsRequired
 Confirmations required before processing a multisig tx.

#### Python
```python
result = substrate.query(
    'MultiSig', 'MultiSigSignsRequired', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### MultiSigToIdentity
 Maps a multisig account to its identity.

#### Python
```python
result = substrate.query(
    'MultiSig', 'MultiSigToIdentity', ['AccountId']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### MultiSigTxDone
 Number of transactions proposed in a multisig. Used as tx id; starts from 0.

#### Python
```python
result = substrate.query(
    'MultiSig', 'MultiSigTxDone', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### NumberOfSigners
 Number of approved/accepted signers of a multisig.

#### Python
```python
result = substrate.query(
    'MultiSig', 'NumberOfSigners', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### ProposalDetail
 Details of a multisig proposal

 multisig -&gt; proposal id =&gt; ProposalDetails.

#### Python
```python
result = substrate.query(
    'MultiSig', 'ProposalDetail', ['AccountId', 'u64']
)
```

#### Return value
```python
{
    'approvals': 'u64',
    'auto_close': 'bool',
    'expiry': (None, 'u64'),
    'rejections': 'u64',
    'status': (
        'Invalid',
        'ActiveOrExpired',
        'ExecutionSuccessful',
        'ExecutionFailed',
        'Rejected',
    ),
}
```
---------
### ProposalIds
 A mapping of proposals to their IDs.

#### Python
```python
result = substrate.query(
    'MultiSig', 'ProposalIds', [
    'AccountId',
    {
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
        None: None,
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
                    None: None,
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
                    'UpgradeCommittee': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    None: None,
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
                    None: None,
                },
                'weight': {
                    'proof_size': 'u64',
                    'ref_time': 'u64',
                },
            },
        },
    },
]
)
```

#### Return value
```python
'u64'
```
---------
### Proposals
 Proposals presented for voting to a multisig.

 multisig -&gt; proposal id =&gt; Option&lt;T::Proposal&gt;.

#### Python
```python
result = substrate.query(
    'MultiSig', 'Proposals', ['AccountId', 'u64']
)
```

#### Return value
```python
{
    None: None,
    'Asset': 'Call',
    'Babe': {
        'plan_config_change': {
            'config': {
                None: None,
                'V1': {'allowed_slots': 'scale_info::323', 'c': ('u64', 'u64')},
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
                    'Precommit': 'scale_info::460',
                    'Prevote': 'scale_info::455',
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
                    'Precommit': 'scale_info::460',
                    'Prevote': 'scale_info::455',
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
    'Scheduler': {
        'cancel': {'index': 'u32', 'when': 'u32'},
        'cancel_named': {'id': '[u8; 32]'},
        'schedule': {
            'call': {
                'Babe': {
                    'plan_config_change': 'InnerStruct',
                    'report_equivocation': 'InnerStruct',
                    'report_equivocation_unsigned': 'InnerStruct',
                },
                'Balances': 'Call',
                None: None,
                'Asset': 'Call',
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
                'Timestamp': {'set': 'InnerStruct'},
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
            'maybe_periodic': (None, ('u32', 'u32')),
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
                'Timestamp': {'set': 'InnerStruct'},
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
            'maybe_periodic': (None, ('u32', 'u32')),
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
                'ImOnline': {'heartbeat': 'InnerStruct'},
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
                'Preimage': {
                    'note_preimage': 'InnerStruct',
                    'request_preimage': 'InnerStruct',
                    'unnote_preimage': 'InnerStruct',
                    'unrequest_preimage': 'InnerStruct',
                },
                'Relayer': 'Call',
                'Session': {'purge_keys': None, 'set_keys': 'InnerStruct'},
                'Staking': 'Call',
                'UpgradeCommittee': 'Call',
                None: None,
                'Identity': 'Call',
                'MultiSig': 'Call',
                'Pips': 'Call',
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
                'Timestamp': {'set': 'InnerStruct'},
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
            'maybe_periodic': (None, ('u32', 'u32')),
            'priority': 'u8',
            'when': 'u32',
        },
        'schedule_named_after': {
            'after': 'u32',
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
                'Timestamp': {'set': 'InnerStruct'},
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
                    'Utility': 'scale_info::517',
                    None: None,
                    'UpgradeCommitteeMembership': 'Call',
                },
            ],
        },
        'batch_old': {
            'calls': [
                {
                    'Babe': 'scale_info::335',
                    'Indices': 'scale_info::343',
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
                'PolymeshCommittee': ('Endorsed', ),
                'TechnicalCommittee': ('Endorsed', ),
                'UpgradeCommittee': ('Endorsed', ),
                'Void': (),
                None: None,
                'system': {'None': None, 'Root': None, 'Signed': 'AccountId'},
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
                'Session': {'purge_keys': None, 'set_keys': 'InnerStruct'},
                'Staking': 'Call',
                None: None,
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
                'Timestamp': {'set': 'InnerStruct'},
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
                    'Treasury': 'Call',
                    'UpgradeCommitteeMembership': 'Call',
                    None: None,
                    'Timestamp': 'scale_info::341',
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
                'Timestamp': {'set': 'InnerStruct'},
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
            'weight': {'proof_size': 'u64', 'ref_time': 'u64'},
        },
    },
}
```
---------
### StorageVersion
 Storage version.

#### Python
```python
result = substrate.query(
    'MultiSig', 'StorageVersion', []
)
```

#### Return value
```python
'u8'
```
---------
### TransactionVersion
 The last transaction version, used for `on_runtime_upgrade`.

#### Python
```python
result = substrate.query(
    'MultiSig', 'TransactionVersion', []
)
```

#### Return value
```python
'u32'
```
---------
### Votes
 Individual multisig signer votes.

 (multisig, proposal_id) -&gt; signer =&gt; vote.

#### Python
```python
result = substrate.query(
    'MultiSig', 'Votes', [
    ('AccountId', 'u64'),
    {
        'Account': 'AccountId',
        'Identity': '[u8; 32]',
    },
]
)
```

#### Return value
```python
'bool'
```
---------
## Errors

---------
### AlreadyASigner
Already a signer.

---------
### AlreadyVoted
Already voted.

---------
### CddMissing
The multisig is not attached to a CDD&\#x27;d identity.

---------
### ChangeNotAllowed
Changing multisig parameters not allowed since multisig is a primary key.

---------
### CreatorControlsHaveBeenRemoved
The creator is no longer allowed to call via creator extrinsics.

---------
### DecodingError
Multisig address.

---------
### FailedToChargeFee
Couldn&\#x27;t charge fee for the transaction.

---------
### FailedToSchedule
Scheduling of a proposal fails

---------
### IdentityNotCreator
Identity provided is not the multisig&\#x27;s creator.

---------
### MissingCurrentIdentity
Current DID is missing

---------
### MultisigMissingIdentity
Multisig is not attached to an identity

---------
### MultisigNotAllowedToLinkToItself
Multisig not allowed to add itself as a signer.

---------
### NoSigners
No signers.

---------
### NoSuchMultisig
No such multisig.

---------
### NonceOverflow
A nonce overflow.

---------
### NotASigner
Not a signer.

---------
### NotEnoughSigners
Not enough signers.

---------
### NotPrimaryKey
The function can only be called by the primary key of the did

---------
### ProposalAlreadyExecuted
Proposal was executed earlier

---------
### ProposalAlreadyRejected
Proposal was rejected earlier

---------
### ProposalExpired
Proposal has expired

---------
### ProposalMissing
The proposal does not exist.

---------
### RequiredSignaturesOutOfBounds
Too few or too many required signatures.

---------
### SignerAlreadyLinkedToIdentity
Signer is an account key that is already associated with an identity.

---------
### SignerAlreadyLinkedToMultisig
Signer is an account key that is already associated with a multisig.

---------
### TooManySigners
More signers than required.

---------