
# System

---------
## Calls

---------
### kill_prefix
See [`Pallet::kill_prefix`].
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
See [`Pallet::kill_storage`].
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
See [`Pallet::remark`].
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
See [`Pallet::remark_with_event`].
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
See [`Pallet::set_code`].
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
See [`Pallet::set_code_without_checks`].
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
See [`Pallet::set_heap_pages`].
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
See [`Pallet::set_storage`].
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
| dispatch_error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}```
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
| account | `T::AccountId` | ```[u8; 20]```

---------
### NewAccount
A new account was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```[u8; 20]```

---------
### Remarked
On on-chain remark happened.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```[u8; 20]```
| hash | `T::Hash` | ```scale_info::12```

---------
## Storage functions

---------
### Account
 The full account information for a particular account ID.

#### Python
```python
result = substrate.query(
    'System', 'Account', ['[u8; 20]']
)
```

#### Return value
```python
{
    'consumers': 'u32',
    'data': {
        'flags': 'u128',
        'free': 'u128',
        'frozen': 'u128',
        'reserved': 'u128',
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
'scale_info::12'
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

 The value has the type `(BlockNumberFor&lt;T&gt;, EventIndex)` because if we used only just
 the `EventIndex` then in case if the topic has the same contents on the next block
 no notification will be triggered thus the event might be lost.

#### Python
```python
result = substrate.query(
    'System', 'EventTopics', ['scale_info::12']
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
            None: None,
            'AssetManager': {
                'ForeignAssetDestroyed': {
                    'asset_id': 'u128',
                    'asset_type': 'scale_info::298',
                },
                'ForeignAssetRegistered': {
                    'asset': 'scale_info::298',
                    'asset_id': 'u128',
                    'metadata': 'scale_info::299',
                },
                'ForeignAssetRemoved': {
                    'asset_id': 'u128',
                    'asset_type': 'scale_info::298',
                },
                'ForeignAssetTypeChanged': {
                    'asset_id': 'u128',
                    'new_asset_type': 'scale_info::298',
                },
                'LocalAssetDestroyed': {'asset_id': 'u128'},
                'LocalAssetRegistered': {
                    'asset_id': 'u128',
                    'creator': '[u8; 20]',
                    'owner': '[u8; 20]',
                },
                'SupportedAssetRemoved': {'asset_type': 'scale_info::298'},
                'UnitsPerSecondChanged': {
                    'asset_type': 'scale_info::298',
                    'units_per_second': 'u128',
                },
            },
            'Assets': {
                'AccountsDestroyed': {
                    'accounts_destroyed': 'u32',
                    'accounts_remaining': 'u32',
                    'asset_id': 'u128',
                },
                'ApprovalCancelled': {
                    'asset_id': 'u128',
                    'delegate': '[u8; 20]',
                    'owner': '[u8; 20]',
                },
                'ApprovalsDestroyed': {
                    'approvals_destroyed': 'u32',
                    'approvals_remaining': 'u32',
                    'asset_id': 'u128',
                },
                'ApprovedTransfer': {
                    'amount': 'u128',
                    'asset_id': 'u128',
                    'delegate': '[u8; 20]',
                    'source': '[u8; 20]',
                },
                'AssetFrozen': {'asset_id': 'u128'},
                'AssetMinBalanceChanged': {
                    'asset_id': 'u128',
                    'new_min_balance': 'u128',
                },
                'AssetStatusChanged': {'asset_id': 'u128'},
                'AssetThawed': {'asset_id': 'u128'},
                'Blocked': {'asset_id': 'u128', 'who': '[u8; 20]'},
                'Burned': {
                    'asset_id': 'u128',
                    'balance': 'u128',
                    'owner': '[u8; 20]',
                },
                'Created': {
                    'asset_id': 'u128',
                    'creator': '[u8; 20]',
                    'owner': '[u8; 20]',
                },
                'Destroyed': {'asset_id': 'u128'},
                'DestructionStarted': {'asset_id': 'u128'},
                'ForceCreated': {'asset_id': 'u128', 'owner': '[u8; 20]'},
                'Frozen': {'asset_id': 'u128', 'who': '[u8; 20]'},
                'Issued': {
                    'amount': 'u128',
                    'asset_id': 'u128',
                    'owner': '[u8; 20]',
                },
                'MetadataCleared': {'asset_id': 'u128'},
                'MetadataSet': {
                    'asset_id': 'u128',
                    'decimals': 'u8',
                    'is_frozen': 'bool',
                    'name': 'Bytes',
                    'symbol': 'Bytes',
                },
                'OwnerChanged': {'asset_id': 'u128', 'owner': '[u8; 20]'},
                'TeamChanged': {
                    'admin': '[u8; 20]',
                    'asset_id': 'u128',
                    'freezer': '[u8; 20]',
                    'issuer': '[u8; 20]',
                },
                'Thawed': {'asset_id': 'u128', 'who': '[u8; 20]'},
                'Touched': {
                    'asset_id': 'u128',
                    'depositor': '[u8; 20]',
                    'who': '[u8; 20]',
                },
                'Transferred': {
                    'amount': 'u128',
                    'asset_id': 'u128',
                    'from': '[u8; 20]',
                    'to': '[u8; 20]',
                },
                'TransferredApproved': {
                    'amount': 'u128',
                    'asset_id': 'u128',
                    'delegate': '[u8; 20]',
                    'destination': '[u8; 20]',
                    'owner': '[u8; 20]',
                },
            },
            'AuthorFilter': {'EligibleUpdated': 'u32'},
            'AuthorMapping': {
                'KeysRegistered': {
                    'account_id': '[u8; 20]',
                    'keys': '[u8; 32]',
                    'nimbus_id': '[u8; 32]',
                },
                'KeysRemoved': {
                    'account_id': '[u8; 20]',
                    'keys': '[u8; 32]',
                    'nimbus_id': '[u8; 32]',
                },
                'KeysRotated': {
                    'account_id': '[u8; 20]',
                    'new_keys': '[u8; 32]',
                    'new_nimbus_id': '[u8; 32]',
                },
            },
            'Balances': {
                'BalanceSet': {'free': 'u128', 'who': '[u8; 20]'},
                'Burned': {'amount': 'u128', 'who': '[u8; 20]'},
                'Deposit': {'amount': 'u128', 'who': '[u8; 20]'},
                'DustLost': {'account': '[u8; 20]', 'amount': 'u128'},
                'Endowed': {'account': '[u8; 20]', 'free_balance': 'u128'},
                'Frozen': {'amount': 'u128', 'who': '[u8; 20]'},
                'Issued': {'amount': 'u128'},
                'Locked': {'amount': 'u128', 'who': '[u8; 20]'},
                'Minted': {'amount': 'u128', 'who': '[u8; 20]'},
                'Rescinded': {'amount': 'u128'},
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'destination_status': 'scale_info::34',
                    'from': '[u8; 20]',
                    'to': '[u8; 20]',
                },
                'Reserved': {'amount': 'u128', 'who': '[u8; 20]'},
                'Restored': {'amount': 'u128', 'who': '[u8; 20]'},
                'Slashed': {'amount': 'u128', 'who': '[u8; 20]'},
                'Suspended': {'amount': 'u128', 'who': '[u8; 20]'},
                'Thawed': {'amount': 'u128', 'who': '[u8; 20]'},
                'Transfer': {
                    'amount': 'u128',
                    'from': '[u8; 20]',
                    'to': '[u8; 20]',
                },
                'Unlocked': {'amount': 'u128', 'who': '[u8; 20]'},
                'Unreserved': {'amount': 'u128', 'who': '[u8; 20]'},
                'Upgraded': {'who': '[u8; 20]'},
                'Withdraw': {'amount': 'u128', 'who': '[u8; 20]'},
            },
            'ConvictionVoting': {'Delegated': ('[u8; 20]', '[u8; 20]'), 'Undelegated': '[u8; 20]'},
            'CrowdloanRewards': {
                'InitialPaymentMade': ('[u8; 20]', 'u128'),
                'InitializedAccountWithNotEnoughContribution': (
                    '[u8; 32]',
                    (None, '[u8; 20]'),
                    'u128',
                ),
                'InitializedAlreadyInitializedAccount': (
                    '[u8; 32]',
                    (None, '[u8; 20]'),
                    'u128',
                ),
                'NativeIdentityAssociated': ('[u8; 32]', '[u8; 20]', 'u128'),
                'RewardAddressUpdated': ('[u8; 20]', '[u8; 20]'),
                'RewardsPaid': ('[u8; 20]', 'u128'),
            },
            'CumulusXcm': {
                'ExecutedDownward': ('[u8; 32]', 'scale_info::338'),
                'InvalidFormat': '[u8; 32]',
                'UnsupportedVersion': '[u8; 32]',
            },
            'Democracy': {
                'Blacklisted': {'proposal_hash': 'scale_info::12'},
                'Cancelled': {'ref_index': 'u32'},
                'Delegated': {'target': '[u8; 20]', 'who': '[u8; 20]'},
                'ExternalTabled': None,
                'MetadataCleared': {
                    'hash': 'scale_info::12',
                    'owner': 'scale_info::81',
                },
                'MetadataSet': {
                    'hash': 'scale_info::12',
                    'owner': 'scale_info::81',
                },
                'MetadataTransferred': {
                    'hash': 'scale_info::12',
                    'owner': 'scale_info::81',
                    'prev_owner': 'scale_info::81',
                },
                'NotPassed': {'ref_index': 'u32'},
                'Passed': {'ref_index': 'u32'},
                'ProposalCanceled': {'prop_index': 'u32'},
                'Proposed': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Seconded': {'prop_index': 'u32', 'seconder': '[u8; 20]'},
                'Started': {'ref_index': 'u32', 'threshold': 'scale_info::78'},
                'Tabled': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Undelegated': {'account': '[u8; 20]'},
                'Vetoed': {
                    'proposal_hash': 'scale_info::12',
                    'until': 'u32',
                    'who': '[u8; 20]',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::79',
                    'voter': '[u8; 20]',
                },
            },
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_hash': '[u8; 32]',
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::338',
                },
                'InvalidFormat': {'message_hash': '[u8; 32]'},
                'MaxMessagesExhausted': {'message_hash': '[u8; 32]'},
                'OverweightEnqueued': {
                    'message_hash': '[u8; 32]',
                    'message_id': '[u8; 32]',
                    'overweight_index': 'u64',
                    'required_weight': 'scale_info::9',
                },
                'OverweightServiced': {
                    'overweight_index': 'u64',
                    'weight_used': 'scale_info::9',
                },
                'UnsupportedVersion': {'message_hash': '[u8; 32]'},
                'WeightExhausted': {
                    'message_hash': '[u8; 32]',
                    'message_id': '[u8; 32]',
                    'remaining_weight': 'scale_info::9',
                    'required_weight': 'scale_info::9',
                },
            },
            'EVM': {
                'Created': {'address': '[u8; 20]'},
                'CreatedFailed': {'address': '[u8; 20]'},
                'Executed': {'address': '[u8; 20]'},
                'ExecutedFailed': {'address': '[u8; 20]'},
                'Log': {'log': 'scale_info::63'},
            },
            'Ethereum': {
                'Executed': {
                    'exit_reason': 'scale_info::67',
                    'extra_data': 'Bytes',
                    'from': '[u8; 20]',
                    'to': '[u8; 20]',
                    'transaction_hash': 'scale_info::12',
                },
            },
            'Identity': {
                'IdentityCleared': {'deposit': 'u128', 'who': '[u8; 20]'},
                'IdentityKilled': {'deposit': 'u128', 'who': '[u8; 20]'},
                'IdentitySet': {'who': '[u8; 20]'},
                'JudgementGiven': {
                    'registrar_index': 'u32',
                    'target': '[u8; 20]',
                },
                'JudgementRequested': {
                    'registrar_index': 'u32',
                    'who': '[u8; 20]',
                },
                'JudgementUnrequested': {
                    'registrar_index': 'u32',
                    'who': '[u8; 20]',
                },
                'RegistrarAdded': {'registrar_index': 'u32'},
                'SubIdentityAdded': {
                    'deposit': 'u128',
                    'main': '[u8; 20]',
                    'sub': '[u8; 20]',
                },
                'SubIdentityRemoved': {
                    'deposit': 'u128',
                    'main': '[u8; 20]',
                    'sub': '[u8; 20]',
                },
                'SubIdentityRevoked': {
                    'deposit': 'u128',
                    'main': '[u8; 20]',
                    'sub': '[u8; 20]',
                },
            },
            'MaintenanceMode': {
                'EnteredMaintenanceMode': None,
                'FailedToResumeIdleXcmExecution': {'error': 'scale_info::26'},
                'FailedToSuspendIdleXcmExecution': {'error': 'scale_info::26'},
                'NormalOperationResumed': None,
            },
            'Migrations': {
                'FailedToResumeIdleXcmExecution': {'error': 'scale_info::26'},
                'FailedToSuspendIdleXcmExecution': {'error': 'scale_info::26'},
                'MigrationCompleted': {
                    'consumed_weight': 'scale_info::9',
                    'migration_name': 'Bytes',
                },
                'MigrationStarted': {'migration_name': 'Bytes'},
                'RuntimeUpgradeCompleted': {'weight': 'scale_info::9'},
                'RuntimeUpgradeStarted': None,
            },
            'MoonbeamOrbiters': {
                'OrbiterJoinCollatorPool': {
                    'collator': '[u8; 20]',
                    'orbiter': '[u8; 20]',
                },
                'OrbiterLeaveCollatorPool': {
                    'collator': '[u8; 20]',
                    'orbiter': '[u8; 20]',
                },
                'OrbiterRegistered': {
                    'account': '[u8; 20]',
                    'deposit': 'u128',
                },
                'OrbiterRewarded': {'account': '[u8; 20]', 'rewards': 'u128'},
                'OrbiterRotation': {
                    'collator': '[u8; 20]',
                    'new_orbiter': (None, '[u8; 20]'),
                    'old_orbiter': (None, '[u8; 20]'),
                },
                'OrbiterUnregistered': {'account': '[u8; 20]'},
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': '[u8; 20]',
                    'call_hash': '[u8; 32]',
                    'multisig': '[u8; 20]',
                    'timepoint': 'scale_info::61',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': '[u8; 20]',
                    'multisig': '[u8; 20]',
                    'timepoint': 'scale_info::61',
                },
                'MultisigExecuted': {
                    'approving': '[u8; 20]',
                    'call_hash': '[u8; 32]',
                    'multisig': '[u8; 20]',
                    'result': 'scale_info::52',
                    'timepoint': 'scale_info::61',
                },
                'NewMultisig': {
                    'approving': '[u8; 20]',
                    'call_hash': '[u8; 32]',
                    'multisig': '[u8; 20]',
                },
            },
            'OpenTechCommitteeCollective': {
                'Approved': {'proposal_hash': 'scale_info::12'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': 'scale_info::12',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': 'scale_info::12'},
                'Executed': {
                    'proposal_hash': 'scale_info::12',
                    'result': 'scale_info::52',
                },
                'MemberExecuted': {
                    'proposal_hash': 'scale_info::12',
                    'result': 'scale_info::52',
                },
                'Proposed': {
                    'account': '[u8; 20]',
                    'proposal_hash': 'scale_info::12',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'Voted': {
                    'account': '[u8; 20]',
                    'no': 'u32',
                    'proposal_hash': 'scale_info::12',
                    'voted': 'bool',
                    'yes': 'u32',
                },
            },
            'ParachainStaking': {
                'AutoCompoundSet': {
                    'candidate': '[u8; 20]',
                    'delegator': '[u8; 20]',
                    'value': 'u8',
                },
                'BlocksPerRoundSet': {
                    'current_round': 'u32',
                    'first_block': 'u32',
                    'new': 'u32',
                    'new_per_round_inflation_ideal': 'u32',
                    'new_per_round_inflation_max': 'u32',
                    'new_per_round_inflation_min': 'u32',
                    'old': 'u32',
                },
                'CancelledCandidateBondLess': {
                    'amount': 'u128',
                    'candidate': '[u8; 20]',
                    'execute_round': 'u32',
                },
                'CancelledCandidateExit': {'candidate': '[u8; 20]'},
                'CancelledDelegationRequest': {
                    'cancelled_request': 'scale_info::38',
                    'collator': '[u8; 20]',
                    'delegator': '[u8; 20]',
                },
                'CandidateBackOnline': {'candidate': '[u8; 20]'},
                'CandidateBondLessRequested': {
                    'amount_to_decrease': 'u128',
                    'candidate': '[u8; 20]',
                    'execute_round': 'u32',
                },
                'CandidateBondedLess': {
                    'amount': 'u128',
                    'candidate': '[u8; 20]',
                    'new_bond': 'u128',
                },
                'CandidateBondedMore': {
                    'amount': 'u128',
                    'candidate': '[u8; 20]',
                    'new_total_bond': 'u128',
                },
                'CandidateLeft': {
                    'ex_candidate': '[u8; 20]',
                    'new_total_amt_locked': 'u128',
                    'unlocked_amount': 'u128',
                },
                'CandidateScheduledExit': {
                    'candidate': '[u8; 20]',
                    'exit_allowed_round': 'u32',
                    'scheduled_exit': 'u32',
                },
                'CandidateWentOffline': {'candidate': '[u8; 20]'},
                'CollatorChosen': {
                    'collator_account': '[u8; 20]',
                    'round': 'u32',
                    'total_exposed_amount': 'u128',
                },
                'CollatorCommissionSet': {'new': 'u32', 'old': 'u32'},
                'Compounded': {
                    'amount': 'u128',
                    'candidate': '[u8; 20]',
                    'delegator': '[u8; 20]',
                },
                'Delegation': {
                    'auto_compound': 'u8',
                    'candidate': '[u8; 20]',
                    'delegator': '[u8; 20]',
                    'delegator_position': 'scale_info::40',
                    'locked_amount': 'u128',
                },
                'DelegationDecreaseScheduled': {
                    'amount_to_decrease': 'u128',
                    'candidate': '[u8; 20]',
                    'delegator': '[u8; 20]',
                    'execute_round': 'u32',
                },
                'DelegationDecreased': {
                    'amount': 'u128',
                    'candidate': '[u8; 20]',
                    'delegator': '[u8; 20]',
                    'in_top': 'bool',
                },
                'DelegationIncreased': {
                    'amount': 'u128',
                    'candidate': '[u8; 20]',
                    'delegator': '[u8; 20]',
                    'in_top': 'bool',
                },
                'DelegationKicked': {
                    'candidate': '[u8; 20]',
                    'delegator': '[u8; 20]',
                    'unstaked_amount': 'u128',
                },
                'DelegationRevocationScheduled': {
                    'candidate': '[u8; 20]',
                    'delegator': '[u8; 20]',
                    'round': 'u32',
                    'scheduled_exit': 'u32',
                },
                'DelegationRevoked': {
                    'candidate': '[u8; 20]',
                    'delegator': '[u8; 20]',
                    'unstaked_amount': 'u128',
                },
                'DelegatorExitCancelled': {'delegator': '[u8; 20]'},
                'DelegatorExitScheduled': {
                    'delegator': '[u8; 20]',
                    'round': 'u32',
                    'scheduled_exit': 'u32',
                },
                'DelegatorLeft': {
                    'delegator': '[u8; 20]',
                    'unstaked_amount': 'u128',
                },
                'DelegatorLeftCandidate': {
                    'candidate': '[u8; 20]',
                    'delegator': '[u8; 20]',
                    'total_candidate_staked': 'u128',
                    'unstaked_amount': 'u128',
                },
                'InflationSet': {
                    'annual_ideal': 'u32',
                    'annual_max': 'u32',
                    'annual_min': 'u32',
                    'round_ideal': 'u32',
                    'round_max': 'u32',
                    'round_min': 'u32',
                },
                'JoinedCollatorCandidates': {
                    'account': '[u8; 20]',
                    'amount_locked': 'u128',
                    'new_total_amt_locked': 'u128',
                },
                'NewRound': {
                    'round': 'u32',
                    'selected_collators_number': 'u32',
                    'starting_block': 'u32',
                    'total_balance': 'u128',
                },
                'ParachainBondAccountSet': {
                    'new': '[u8; 20]',
                    'old': '[u8; 20]',
                },
                'ParachainBondReservePercentSet': {'new': 'u8', 'old': 'u8'},
                'ReservedForParachainBond': {
                    'account': '[u8; 20]',
                    'value': 'u128',
                },
                'Rewarded': {'account': '[u8; 20]', 'rewards': 'u128'},
                'StakeExpectationsSet': {
                    'expect_ideal': 'u128',
                    'expect_max': 'u128',
                    'expect_min': 'u128',
                },
                'TotalSelectedSet': {'new': 'u32', 'old': 'u32'},
            },
            'ParachainSystem': {
                'DownwardMessagesProcessed': {
                    'dmq_head': 'scale_info::12',
                    'weight_used': 'scale_info::9',
                },
                'DownwardMessagesReceived': {'count': 'u32'},
                'UpgradeAuthorized': {'code_hash': 'scale_info::12'},
                'UpwardMessageSent': {'message_hash': (None, '[u8; 32]')},
                'ValidationFunctionApplied': {'relay_chain_block_num': 'u32'},
                'ValidationFunctionDiscarded': None,
                'ValidationFunctionStored': None,
            },
            'PolkadotXcm': {
                'AssetsClaimed': {
                    'assets': 'scale_info::287',
                    'hash': 'scale_info::12',
                    'origin': 'scale_info::127',
                },
                'AssetsTrapped': {
                    'assets': 'scale_info::287',
                    'hash': 'scale_info::12',
                    'origin': 'scale_info::127',
                },
                'Attempted': {'outcome': 'scale_info::338'},
                'FeesPaid': {'fees': ['scale_info::267'], 'paying': 'scale_info::127'},
                'InvalidQuerier': {
                    'expected_querier': 'scale_info::127',
                    'maybe_actual_querier': (None, 'scale_info::127'),
                    'origin': 'scale_info::127',
                    'query_id': 'u64',
                },
                'InvalidQuerierVersion': {
                    'origin': 'scale_info::127',
                    'query_id': 'u64',
                },
                'InvalidResponder': {
                    'expected_location': (None, 'scale_info::127'),
                    'origin': 'scale_info::127',
                    'query_id': 'u64',
                },
                'InvalidResponderVersion': {
                    'origin': 'scale_info::127',
                    'query_id': 'u64',
                },
                'Notified': {
                    'call_index': 'u8',
                    'pallet_index': 'u8',
                    'query_id': 'u64',
                },
                'NotifyDecodeFailed': {
                    'call_index': 'u8',
                    'pallet_index': 'u8',
                    'query_id': 'u64',
                },
                'NotifyDispatchError': {
                    'call_index': 'u8',
                    'pallet_index': 'u8',
                    'query_id': 'u64',
                },
                'NotifyOverweight': {
                    'actual_weight': 'scale_info::9',
                    'call_index': 'u8',
                    'max_budgeted_weight': 'scale_info::9',
                    'pallet_index': 'u8',
                    'query_id': 'u64',
                },
                'NotifyTargetMigrationFail': {
                    'location': 'scale_info::234',
                    'query_id': 'u64',
                },
                'NotifyTargetSendFail': {
                    'error': 'scale_info::274',
                    'location': 'scale_info::127',
                    'query_id': 'u64',
                },
                'ResponseReady': {
                    'query_id': 'u64',
                    'response': 'scale_info::271',
                },
                'ResponseTaken': {'query_id': 'u64'},
                'Sent': {
                    'destination': 'scale_info::127',
                    'message': ['scale_info::264'],
                    'message_id': '[u8; 32]',
                    'origin': 'scale_info::127',
                },
                'SupportedVersionChanged': {
                    'location': 'scale_info::127',
                    'version': 'u32',
                },
                'UnexpectedResponse': {
                    'origin': 'scale_info::127',
                    'query_id': 'u64',
                },
                'VersionChangeNotified': {
                    'cost': ['scale_info::267'],
                    'destination': 'scale_info::127',
                    'message_id': '[u8; 32]',
                    'result': 'u32',
                },
                'VersionNotifyRequested': {
                    'cost': ['scale_info::267'],
                    'destination': 'scale_info::127',
                    'message_id': '[u8; 32]',
                },
                'VersionNotifyStarted': {
                    'cost': ['scale_info::267'],
                    'destination': 'scale_info::127',
                    'message_id': '[u8; 32]',
                },
                'VersionNotifyUnrequested': {
                    'cost': ['scale_info::267'],
                    'destination': 'scale_info::127',
                    'message_id': '[u8; 32]',
                },
            },
            'Preimage': {
                'Cleared': {'hash': 'scale_info::12'},
                'Noted': {'hash': 'scale_info::12'},
                'Requested': {'hash': 'scale_info::12'},
            },
            'Proxy': {
                'Announced': {
                    'call_hash': 'scale_info::12',
                    'proxy': '[u8; 20]',
                    'real': '[u8; 20]',
                },
                'ProxyAdded': {
                    'delay': 'u32',
                    'delegatee': '[u8; 20]',
                    'delegator': '[u8; 20]',
                    'proxy_type': 'scale_info::55',
                },
                'ProxyExecuted': {'result': 'scale_info::52'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': '[u8; 20]',
                    'delegator': '[u8; 20]',
                    'proxy_type': 'scale_info::55',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::55',
                    'pure': '[u8; 20]',
                    'who': '[u8; 20]',
                },
            },
            'Randomness': {
                'RandomnessRequestedBabeEpoch': {
                    'contract_address': '[u8; 20]',
                    'earliest_epoch': 'u64',
                    'fee': 'u128',
                    'gas_limit': 'u64',
                    'id': 'u64',
                    'num_words': 'u8',
                    'refund_address': '[u8; 20]',
                    'salt': 'scale_info::12',
                },
                'RandomnessRequestedLocal': {
                    'contract_address': '[u8; 20]',
                    'earliest_block': 'u32',
                    'fee': 'u128',
                    'gas_limit': 'u64',
                    'id': 'u64',
                    'num_words': 'u8',
                    'refund_address': '[u8; 20]',
                    'salt': 'scale_info::12',
                },
                'RequestExpirationExecuted': {'id': 'u64'},
                'RequestFeeIncreased': {'id': 'u64', 'new_fee': 'u128'},
                'RequestFulfilled': {'id': 'u64'},
            },
            'Referenda': {
                'Approved': {'index': 'u32'},
                'Cancelled': {'index': 'u32', 'tally': 'scale_info::327'},
                'ConfirmAborted': {'index': 'u32'},
                'ConfirmStarted': {'index': 'u32'},
                'Confirmed': {'index': 'u32', 'tally': 'scale_info::327'},
                'DecisionDepositPlaced': {
                    'amount': 'u128',
                    'index': 'u32',
                    'who': '[u8; 20]',
                },
                'DecisionDepositRefunded': {
                    'amount': 'u128',
                    'index': 'u32',
                    'who': '[u8; 20]',
                },
                'DecisionStarted': {
                    'index': 'u32',
                    'proposal': 'scale_info::85',
                    'tally': 'scale_info::327',
                    'track': 'u16',
                },
                'DepositSlashed': {'amount': 'u128', 'who': '[u8; 20]'},
                'Killed': {'index': 'u32', 'tally': 'scale_info::327'},
                'MetadataCleared': {'hash': 'scale_info::12', 'index': 'u32'},
                'MetadataSet': {'hash': 'scale_info::12', 'index': 'u32'},
                'Rejected': {'index': 'u32', 'tally': 'scale_info::327'},
                'SubmissionDepositRefunded': {
                    'amount': 'u128',
                    'index': 'u32',
                    'who': '[u8; 20]',
                },
                'Submitted': {
                    'index': 'u32',
                    'proposal': 'scale_info::85',
                    'track': 'u16',
                },
                'TimedOut': {'index': 'u32', 'tally': 'scale_info::327'},
            },
            'Scheduler': {
                'CallUnavailable': {
                    'id': (None, '[u8; 32]'),
                    'task': ('u32', 'u32'),
                },
                'Canceled': {'index': 'u32', 'when': 'u32'},
                'Dispatched': {
                    'id': (None, '[u8; 32]'),
                    'result': 'scale_info::52',
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
            'System': {
                'CodeUpdated': None,
                'ExtrinsicFailed': {
                    'dispatch_error': 'scale_info::26',
                    'dispatch_info': 'scale_info::23',
                },
                'ExtrinsicSuccess': {'dispatch_info': 'scale_info::23'},
                'KilledAccount': {'account': '[u8; 20]'},
                'NewAccount': {'account': '[u8; 20]'},
                'Remarked': {'hash': 'scale_info::12', 'sender': '[u8; 20]'},
            },
            'TransactionPayment': {
                'TransactionFeePaid': {
                    'actual_fee': 'u128',
                    'tip': 'u128',
                    'who': '[u8; 20]',
                },
            },
            'Treasury': {
                'AssetSpendApproved': {
                    'amount': 'u128',
                    'asset_kind': (),
                    'beneficiary': '[u8; 20]',
                    'expire_at': 'u32',
                    'index': 'u32',
                    'valid_from': 'u32',
                },
                'AssetSpendVoided': {'index': 'u32'},
                'Awarded': {
                    'account': '[u8; 20]',
                    'award': 'u128',
                    'proposal_index': 'u32',
                },
                'Burnt': {'burnt_funds': 'u128'},
                'Deposit': {'value': 'u128'},
                'Paid': {'index': 'u32', 'payment_id': ()},
                'PaymentFailed': {'index': 'u32', 'payment_id': ()},
                'Proposed': {'proposal_index': 'u32'},
                'Rejected': {'proposal_index': 'u32', 'slashed': 'u128'},
                'Rollover': {'rollover_balance': 'u128'},
                'SpendApproved': {
                    'amount': 'u128',
                    'beneficiary': '[u8; 20]',
                    'proposal_index': 'u32',
                },
                'SpendProcessed': {'index': 'u32'},
                'Spending': {'budget_remaining': 'u128'},
                'UpdatedInactive': {
                    'deactivated': 'u128',
                    'reactivated': 'u128',
                },
            },
            'TreasuryCouncilCollective': {
                'Approved': {'proposal_hash': 'scale_info::12'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': 'scale_info::12',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': 'scale_info::12'},
                'Executed': {
                    'proposal_hash': 'scale_info::12',
                    'result': 'scale_info::52',
                },
                'MemberExecuted': {
                    'proposal_hash': 'scale_info::12',
                    'result': 'scale_info::52',
                },
                'Proposed': {
                    'account': '[u8; 20]',
                    'proposal_hash': 'scale_info::12',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'Voted': {
                    'account': '[u8; 20]',
                    'no': 'u32',
                    'proposal_hash': 'scale_info::12',
                    'voted': 'bool',
                    'yes': 'u32',
                },
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::26',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::52'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::26'},
            },
            'Whitelist': {
                'CallWhitelisted': {'call_hash': 'scale_info::12'},
                'WhitelistedCallDispatched': {
                    'call_hash': 'scale_info::12',
                    'result': 'scale_info::329',
                },
                'WhitelistedCallRemoved': {'call_hash': 'scale_info::12'},
            },
            'XTokens': {
                'TransferredMultiAssets': {
                    'assets': ['scale_info::267'],
                    'dest': 'scale_info::127',
                    'fee': 'scale_info::267',
                    'sender': '[u8; 20]',
                },
            },
            'XcmTransactor': {
                'DeRegisteredDerivative': {'index': 'u16'},
                'DestFeePerSecondChanged': {
                    'fee_per_second': 'u128',
                    'location': 'scale_info::127',
                },
                'DestFeePerSecondRemoved': {'location': 'scale_info::127'},
                'HrmpManagementSent': {'action': 'scale_info::313'},
                'RegisteredDerivative': {
                    'account_id': '[u8; 20]',
                    'index': 'u16',
                },
                'TransactFailed': {'error': 'scale_info::274'},
                'TransactInfoChanged': {
                    'location': 'scale_info::127',
                    'remote_info': 'scale_info::345',
                },
                'TransactInfoRemoved': {'location': 'scale_info::127'},
                'TransactedDerivative': {
                    'account_id': '[u8; 20]',
                    'call': 'Bytes',
                    'dest': 'scale_info::127',
                    'index': 'u16',
                },
                'TransactedSigned': {
                    'call': 'Bytes',
                    'dest': 'scale_info::127',
                    'fee_payer': '[u8; 20]',
                },
                'TransactedSovereign': {
                    'call': 'Bytes',
                    'dest': 'scale_info::127',
                    'fee_payer': '[u8; 20]',
                },
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': '[u8; 32]'},
                'BadVersion': {'message_hash': '[u8; 32]'},
                'Fail': {
                    'error': 'scale_info::274',
                    'message_hash': '[u8; 32]',
                    'message_id': '[u8; 32]',
                    'weight': 'scale_info::9',
                },
                'OverweightEnqueued': {
                    'index': 'u64',
                    'required': 'scale_info::9',
                    'sender': 'u32',
                    'sent_at': 'u32',
                },
                'OverweightServiced': {
                    'index': 'u64',
                    'used': 'scale_info::9',
                },
                'Success': {
                    'message_hash': '[u8; 32]',
                    'message_id': '[u8; 32]',
                    'weight': 'scale_info::9',
                },
                'XcmpMessageSent': {'message_hash': '[u8; 32]'},
            },
        },
        'phase': {
            'ApplyExtrinsic': 'u32',
            'Finalization': None,
            'Initialization': None,
        },
        'topics': ['scale_info::12'],
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
'scale_info::12'
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
256
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
{'max': {'mandatory': 5242880, 'normal': 3932160, 'operational': 5242880}}
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
    'base_block': {'proof_size': 0, 'ref_time': 390584000},
    'max_block': {'proof_size': 5242880, 'ref_time': 500000000000},
    'per_class': {
        'mandatory': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 124414000},
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 250000000},
            'max_extrinsic': {'proof_size': 3407872, 'ref_time': 324750000000},
            'max_total': {'proof_size': 3932160, 'ref_time': 375000000000},
            'reserved': {'proof_size': 0, 'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 124414000},
            'max_extrinsic': {'proof_size': 4718592, 'ref_time': 449875586000},
            'max_total': {'proof_size': 5242880, 'ref_time': 500000000000},
            'reserved': {'proof_size': 1310720, 'ref_time': 125000000000},
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
1285
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
        ('0xd2bc9897eed08f15', 3),
        ('0xd0399cd053adda2b', 1),
        ('0xdf6acb689907609b', 4),
        ('0x37e397fc7c91f5e4', 2),
        ('0x40fe3ad401f8959a', 6),
        ('0xf78b278be53f454c', 2),
        ('0xab3c0572291feb8b', 1),
        ('0xbc9d89904f5b923f', 1),
        ('0xbd78255d4feeea1f', 4),
        ('0xa33d43f58731ad84', 2),
        ('0x582211f65bb14b89', 5),
        ('0xe65b00e46cedd0aa', 2),
        ('0x37c8bb1350a9a2a8', 4),
        ('0x2aa62120049dd2d2', 1),
        ('0xea93e3f16f3d6962', 2),
        ('0xba8173bf23b2e6f8', 1),
    ],
    'authoring_version': 3,
    'impl_name': 'moonriver',
    'impl_version': 0,
    'spec_name': 'moonriver',
    'spec_version': 2801,
    'state_version': 0,
    'transaction_version': 2,
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