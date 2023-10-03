
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
| hash | `T::Hash` | ```[u8; 32]```

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
'[u8; 32]'
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
    'System', 'EventTopics', ['[u8; 32]']
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
            'AccountMigration': {
                'Migrated': {'from': 'AccountId', 'to': '[u8; 20]'},
                'MultisigMigrated': {
                    'detail': 'scale_info::45',
                    'from': 'AccountId',
                },
                'NewMultisigParamsNoted': {
                    'from': 'AccountId',
                    'to': 'scale_info::43',
                },
            },
            'Assets': {
                'AccountsDestroyed': {
                    'accounts_destroyed': 'u32',
                    'accounts_remaining': 'u32',
                    'asset_id': 'u64',
                },
                'ApprovalCancelled': {
                    'asset_id': 'u64',
                    'delegate': '[u8; 20]',
                    'owner': '[u8; 20]',
                },
                'ApprovalsDestroyed': {
                    'approvals_destroyed': 'u32',
                    'approvals_remaining': 'u32',
                    'asset_id': 'u64',
                },
                'ApprovedTransfer': {
                    'amount': 'u128',
                    'asset_id': 'u64',
                    'delegate': '[u8; 20]',
                    'source': '[u8; 20]',
                },
                'AssetFrozen': {'asset_id': 'u64'},
                'AssetMinBalanceChanged': {
                    'asset_id': 'u64',
                    'new_min_balance': 'u128',
                },
                'AssetStatusChanged': {'asset_id': 'u64'},
                'AssetThawed': {'asset_id': 'u64'},
                'Blocked': {'asset_id': 'u64', 'who': '[u8; 20]'},
                'Burned': {
                    'asset_id': 'u64',
                    'balance': 'u128',
                    'owner': '[u8; 20]',
                },
                'Created': {
                    'asset_id': 'u64',
                    'creator': '[u8; 20]',
                    'owner': '[u8; 20]',
                },
                'Destroyed': {'asset_id': 'u64'},
                'DestructionStarted': {'asset_id': 'u64'},
                'ForceCreated': {'asset_id': 'u64', 'owner': '[u8; 20]'},
                'Frozen': {'asset_id': 'u64', 'who': '[u8; 20]'},
                'Issued': {
                    'amount': 'u128',
                    'asset_id': 'u64',
                    'owner': '[u8; 20]',
                },
                'MetadataCleared': {'asset_id': 'u64'},
                'MetadataSet': {
                    'asset_id': 'u64',
                    'decimals': 'u8',
                    'is_frozen': 'bool',
                    'name': 'Bytes',
                    'symbol': 'Bytes',
                },
                'OwnerChanged': {'asset_id': 'u64', 'owner': '[u8; 20]'},
                'TeamChanged': {
                    'admin': '[u8; 20]',
                    'asset_id': 'u64',
                    'freezer': '[u8; 20]',
                    'issuer': '[u8; 20]',
                },
                'Thawed': {'asset_id': 'u64', 'who': '[u8; 20]'},
                'Touched': {
                    'asset_id': 'u64',
                    'depositor': '[u8; 20]',
                    'who': '[u8; 20]',
                },
                'Transferred': {
                    'amount': 'u128',
                    'asset_id': 'u64',
                    'from': '[u8; 20]',
                    'to': '[u8; 20]',
                },
                'TransferredApproved': {
                    'amount': 'u128',
                    'asset_id': 'u64',
                    'delegate': '[u8; 20]',
                    'destination': '[u8; 20]',
                    'owner': '[u8; 20]',
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
            'BridgeDarwiniaDispatch': {
                'MessageCallDecodeFailed': ('[u8; 4]', ('[u8; 4]', 'u64')),
                'MessageCallValidateFailed': (
                    '[u8; 4]',
                    ('[u8; 4]', 'u64'),
                    'scale_info::168',
                ),
                'MessageDispatchPaymentFailed': (
                    '[u8; 4]',
                    ('[u8; 4]', 'u64'),
                    '[u8; 20]',
                    'scale_info::9',
                ),
                'MessageDispatched': ('[u8; 4]', ('[u8; 4]', 'u64'), 'scale_info::66'),
                'MessageRejected': ('[u8; 4]', ('[u8; 4]', 'u64')),
                'MessageSignatureMismatch': ('[u8; 4]', ('[u8; 4]', 'u64')),
                'MessageVersionSpecMismatch': ('[u8; 4]', ('[u8; 4]', 'u64'), 'u32', 'u32'),
                'MessageWeightMismatch': (
                    '[u8; 4]',
                    ('[u8; 4]', 'u64'),
                    'scale_info::9',
                    'scale_info::9',
                ),
                '_Dummy': None,
            },
            'BridgeDarwiniaMessages': {
                'MessageAccepted': {'lane_id': '[u8; 4]', 'nonce': 'u64'},
                'MessagesDelivered': {
                    'lane_id': '[u8; 4]',
                    'messages': 'scale_info::163',
                },
                'MessagesReceived': ['scale_info::157'],
                'ParameterUpdated': {'parameter': ()},
            },
            'BridgePolkadotParachain': {
                'IncorrectParachainHeadHash': {
                    'actual_parachain_head_hash': '[u8; 32]',
                    'parachain': 'u32',
                    'parachain_head_hash': '[u8; 32]',
                },
                'MissingParachainHead': {'parachain': 'u32'},
                'RejectedLargeParachainHead': {
                    'parachain': 'u32',
                    'parachain_head_hash': '[u8; 32]',
                    'parachain_head_size': 'u32',
                },
                'RejectedObsoleteParachainHead': {
                    'parachain': 'u32',
                    'parachain_head_hash': '[u8; 32]',
                },
                'UntrackedParachainRejected': {'parachain': 'u32'},
                'UpdatedParachainHead': {
                    'parachain': 'u32',
                    'parachain_head_hash': '[u8; 32]',
                },
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
                    'result': 'scale_info::66',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::66',
                },
                'Proposed': {
                    'account': '[u8; 20]',
                    'proposal_hash': '[u8; 32]',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'Voted': {
                    'account': '[u8; 20]',
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'voted': 'bool',
                    'yes': 'u32',
                },
            },
            'CumulusXcm': {
                'ExecutedDownward': ('[u8; 32]', 'scale_info::85'),
                'InvalidFormat': '[u8; 32]',
                'UnsupportedVersion': '[u8; 32]',
            },
            'DarwiniaFeeMarket': {
                'CancelEnrollment': '[u8; 20]',
                'Enroll': ('[u8; 20]', 'u128', 'u128'),
                'FeeMarketSlash': {
                    'account_id': '[u8; 20]',
                    'amount': 'u128',
                    'confirm_time': (None, 'u32'),
                    'delay_time': (None, 'u32'),
                    'lane': '[u8; 4]',
                    'message': 'u64',
                    'sent_time': 'u32',
                },
                'OrderCreated': (
                    '[u8; 4]',
                    'u64',
                    'u128',
                    ['[u8; 20]'],
                    (None, 'u32'),
                ),
                'OrderReward': ('[u8; 4]', 'u64', 'scale_info::173'),
                'UpdateAssignedRelayersNumber': 'u32',
                'UpdateCollateralSlashProtect': 'u128',
                'UpdateLockedCollateral': ('[u8; 20]', 'u128'),
                'UpdateRelayFee': ('[u8; 20]', 'u128'),
            },
            'DarwiniaStaking': {
                'CommissionUpdated': {'commission': 'u32', 'who': '[u8; 20]'},
                'Elected': {'collators': ['[u8; 20]']},
                'Payout': {'ring_amount': 'u128', 'staker': '[u8; 20]'},
                'Staked': {
                    'deposits': ['u16'],
                    'kton_amount': 'u128',
                    'ring_amount': 'u128',
                    'staker': '[u8; 20]',
                },
                'Unstaked': {
                    'deposits': ['u16'],
                    'kton_amount': 'u128',
                    'ring_amount': 'u128',
                    'staker': '[u8; 20]',
                },
            },
            'Democracy': {
                'Blacklisted': {'proposal_hash': '[u8; 32]'},
                'Cancelled': {'ref_index': 'u32'},
                'Delegated': {'target': '[u8; 20]', 'who': '[u8; 20]'},
                'ExternalTabled': None,
                'MetadataCleared': {
                    'hash': '[u8; 32]',
                    'owner': 'scale_info::64',
                },
                'MetadataSet': {'hash': '[u8; 32]', 'owner': 'scale_info::64'},
                'MetadataTransferred': {
                    'hash': '[u8; 32]',
                    'owner': 'scale_info::64',
                    'prev_owner': 'scale_info::64',
                },
                'NotPassed': {'ref_index': 'u32'},
                'Passed': {'ref_index': 'u32'},
                'ProposalCanceled': {'prop_index': 'u32'},
                'Proposed': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Seconded': {'prop_index': 'u32', 'seconder': '[u8; 20]'},
                'Started': {'ref_index': 'u32', 'threshold': 'scale_info::61'},
                'Tabled': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Undelegated': {'account': '[u8; 20]'},
                'Vetoed': {
                    'proposal_hash': '[u8; 32]',
                    'until': 'u32',
                    'who': '[u8; 20]',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::62',
                    'voter': '[u8; 20]',
                },
            },
            'Deposit': {
                'DepositClaimed': {'deposit_id': 'u16', 'owner': '[u8; 20]'},
                'DepositClaimedWithPenalty': {
                    'deposit_id': 'u16',
                    'kton_penalty': 'u128',
                    'owner': '[u8; 20]',
                },
                'DepositCreated': {
                    'deposit_id': 'u16',
                    'expired_time': 'u128',
                    'kton_reward': 'u128',
                    'owner': '[u8; 20]',
                    'start_time': 'u128',
                    'value': 'u128',
                },
            },
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::85',
                },
                'InvalidFormat': {'message_id': '[u8; 32]'},
                'MaxMessagesExhausted': {'message_id': '[u8; 32]'},
                'OverweightEnqueued': {
                    'message_id': '[u8; 32]',
                    'overweight_index': 'u64',
                    'required_weight': 'scale_info::9',
                },
                'OverweightServiced': {
                    'overweight_index': 'u64',
                    'weight_used': 'scale_info::9',
                },
                'UnsupportedVersion': {'message_id': '[u8; 32]'},
                'WeightExhausted': {
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
                'Log': {'log': 'scale_info::151'},
            },
            'EcdsaAuthority': {
                'CollectedEnoughAuthoritiesChangeSignatures': {
                    'message': '[u8; 32]',
                    'operation': 'scale_info::53',
                    'signatures': [('[u8; 20]', '[u8; 65]')],
                    'threshold': (None, 'u32'),
                },
                'CollectedEnoughNewMessageRootSignatures': {
                    'commitment': 'scale_info::59',
                    'message': '[u8; 32]',
                    'signatures': [('[u8; 20]', '[u8; 65]')],
                },
                'CollectingAuthoritiesChangeSignatures': {
                    'message': '[u8; 32]',
                },
                'CollectingNewMessageRootSignatures': {'message': '[u8; 32]'},
            },
            'Ethereum': {
                'Executed': {
                    'exit_reason': 'scale_info::142',
                    'extra_data': 'Bytes',
                    'from': '[u8; 20]',
                    'to': '[u8; 20]',
                    'transaction_hash': '[u8; 32]',
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
            'ParachainSystem': {
                'DownwardMessagesProcessed': {
                    'dmq_head': '[u8; 32]',
                    'weight_used': 'scale_info::9',
                },
                'DownwardMessagesReceived': {'count': 'u32'},
                'UpgradeAuthorized': {'code_hash': '[u8; 32]'},
                'UpwardMessageSent': {'message_hash': (None, '[u8; 32]')},
                'ValidationFunctionApplied': {'relay_chain_block_num': 'u32'},
                'ValidationFunctionDiscarded': None,
                'ValidationFunctionStored': None,
            },
            'PhragmenElection': {
                'CandidateSlashed': {
                    'amount': 'u128',
                    'candidate': '[u8; 20]',
                },
                'ElectionError': None,
                'EmptyTerm': None,
                'MemberKicked': {'member': '[u8; 20]'},
                'NewTerm': {'new_members': [('[u8; 20]', 'u128')]},
                'Renounced': {'candidate': '[u8; 20]'},
                'SeatHolderSlashed': {
                    'amount': 'u128',
                    'seat_holder': '[u8; 20]',
                },
            },
            'PolkadotXcm': {
                'AssetsClaimed': (
                    '[u8; 32]',
                    'scale_info::86',
                    'scale_info::123',
                ),
                'AssetsTrapped': (
                    '[u8; 32]',
                    'scale_info::86',
                    'scale_info::123',
                ),
                'Attempted': {
                    'Complete': 'scale_info::9',
                    'Error': 'scale_info::82',
                    'Incomplete': ('scale_info::9', 'scale_info::82'),
                },
                'FeesPaid': ('scale_info::86', ['scale_info::100']),
                'InvalidQuerier': (
                    'scale_info::86',
                    'u64',
                    'scale_info::86',
                    (None, 'scale_info::86'),
                ),
                'InvalidQuerierVersion': ('scale_info::86', 'u64'),
                'InvalidResponder': (
                    'scale_info::86',
                    'u64',
                    (None, 'scale_info::86'),
                ),
                'InvalidResponderVersion': ('scale_info::86', 'u64'),
                'Notified': ('u64', 'u8', 'u8'),
                'NotifyDecodeFailed': ('u64', 'u8', 'u8'),
                'NotifyDispatchError': ('u64', 'u8', 'u8'),
                'NotifyOverweight': (
                    'u64',
                    'u8',
                    'u8',
                    'scale_info::9',
                    'scale_info::9',
                ),
                'NotifyTargetMigrationFail': ('scale_info::137', 'u64'),
                'NotifyTargetSendFail': (
                    'scale_info::86',
                    'u64',
                    'scale_info::82',
                ),
                'ResponseReady': ('u64', 'scale_info::106'),
                'ResponseTaken': 'u64',
                'Sent': (
                    'scale_info::86',
                    'scale_info::86',
                    ['scale_info::97'],
                ),
                'SupportedVersionChanged': ('scale_info::86', 'u32'),
                'UnexpectedResponse': ('scale_info::86', 'u64'),
                'VersionChangeNotified': (
                    'scale_info::86',
                    'u32',
                    ['scale_info::100'],
                ),
                'VersionNotifyRequested': (
                    'scale_info::86',
                    ['scale_info::100'],
                ),
                'VersionNotifyStarted': ('scale_info::86', ['scale_info::100']),
                'VersionNotifyUnrequested': (
                    'scale_info::86',
                    ['scale_info::100'],
                ),
            },
            'Preimage': {
                'Cleared': {'hash': '[u8; 32]'},
                'Noted': {'hash': '[u8; 32]'},
                'Requested': {'hash': '[u8; 32]'},
            },
            'Proxy': {
                'Announced': {
                    'call_hash': '[u8; 32]',
                    'proxy': '[u8; 20]',
                    'real': '[u8; 20]',
                },
                'ProxyAdded': {
                    'delay': 'u32',
                    'delegatee': '[u8; 20]',
                    'delegator': '[u8; 20]',
                    'proxy_type': 'scale_info::80',
                },
                'ProxyExecuted': {'result': 'scale_info::66'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': '[u8; 20]',
                    'delegator': '[u8; 20]',
                    'proxy_type': 'scale_info::80',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::80',
                    'pure': '[u8; 20]',
                    'who': '[u8; 20]',
                },
            },
            'Scheduler': {
                'CallUnavailable': {
                    'id': (None, '[u8; 32]'),
                    'task': ('u32', 'u32'),
                },
                'Canceled': {'index': 'u32', 'when': 'u32'},
                'Dispatched': {
                    'id': (None, '[u8; 32]'),
                    'result': 'scale_info::66',
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
            'Session': {'NewSession': {'session_index': 'u32'}},
            'System': {
                'CodeUpdated': None,
                'ExtrinsicFailed': {
                    'dispatch_error': 'scale_info::26',
                    'dispatch_info': 'scale_info::23',
                },
                'ExtrinsicSuccess': {'dispatch_info': 'scale_info::23'},
                'KilledAccount': {'account': '[u8; 20]'},
                'NewAccount': {'account': '[u8; 20]'},
                'Remarked': {'hash': '[u8; 32]', 'sender': '[u8; 20]'},
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
                    'result': 'scale_info::66',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::66',
                },
                'Proposed': {
                    'account': '[u8; 20]',
                    'proposal_hash': '[u8; 32]',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'Voted': {
                    'account': '[u8; 20]',
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'voted': 'bool',
                    'yes': 'u32',
                },
            },
            'TechnicalMembership': (
                'MemberAdded',
                'MemberRemoved',
                'MembersSwapped',
                'MembersReset',
                'KeyChanged',
                'Dummy',
            ),
            'TransactionPayment': {
                'TransactionFeePaid': {
                    'actual_fee': 'u128',
                    'tip': 'u128',
                    'who': '[u8; 20]',
                },
            },
            'Treasury': {
                'Awarded': {
                    'account': '[u8; 20]',
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
                    'beneficiary': '[u8; 20]',
                    'proposal_index': 'u32',
                },
                'Spending': {'budget_remaining': 'u128'},
                'UpdatedInactive': {
                    'deactivated': 'u128',
                    'reactivated': 'u128',
                },
            },
            None: None,
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::26',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::66'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::26'},
            },
            'Vesting': {
                'VestingCompleted': {'account': '[u8; 20]'},
                'VestingUpdated': {'account': '[u8; 20]', 'unvested': 'u128'},
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': (None, '[u8; 32]')},
                'BadVersion': {'message_hash': (None, '[u8; 32]')},
                'Fail': {
                    'error': 'scale_info::82',
                    'message_hash': (None, '[u8; 32]'),
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
                'Success': {'message_hash': (None, '[u8; 32]'), 'weight': 'scale_info::9'},
                'XcmpMessageSent': {'message_hash': (None, '[u8; 32]')},
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
'[u8; 32]'
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
    'base_block': {'proof_size': 0, 'ref_time': 392184000},
    'max_block': {'proof_size': 5242880, 'ref_time': 500000000000},
    'per_class': {
        'mandatory': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 113638000},
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 113638000},
            'max_extrinsic': {'proof_size': 3670016, 'ref_time': 349886362000},
            'max_total': {'proof_size': 3932160, 'ref_time': 375000000000},
            'reserved': {'proof_size': 0, 'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 113638000},
            'max_extrinsic': {'proof_size': 4980736, 'ref_time': 474886362000},
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
        ('0xdd718d5cc53262d4', 1),
        ('0xdf6acb689907609b', 4),
        ('0x37e397fc7c91f5e4', 2),
        ('0x40fe3ad401f8959a', 6),
        ('0xd2bc9897eed08f15', 3),
        ('0xf78b278be53f454c', 2),
        ('0xab3c0572291feb8b', 1),
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 4),
        ('0xf3ff14d5ab527059', 3),
        ('0xea93e3f16f3d6962', 2),
        ('0x582211f65bb14b89', 5),
        ('0xe65b00e46cedd0aa', 2),
        ('0xbd78255d4feeea1f', 4),
    ],
    'authoring_version': 0,
    'impl_name': 'DarwiniaOfficialRust',
    'impl_version': 0,
    'spec_name': 'Crab2',
    'spec_version': 6402,
    'state_version': 0,
    'transaction_version': 0,
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