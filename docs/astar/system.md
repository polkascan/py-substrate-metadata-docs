
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
| hash | `T::Hash` | ```scale_info::12```

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
            'Assets': {
                'AccountsDestroyed': {
                    'accounts_destroyed': 'u32',
                    'accounts_remaining': 'u32',
                    'asset_id': 'u128',
                },
                'ApprovalCancelled': {
                    'asset_id': 'u128',
                    'delegate': 'AccountId',
                    'owner': 'AccountId',
                },
                'ApprovalsDestroyed': {
                    'approvals_destroyed': 'u32',
                    'approvals_remaining': 'u32',
                    'asset_id': 'u128',
                },
                'ApprovedTransfer': {
                    'amount': 'u128',
                    'asset_id': 'u128',
                    'delegate': 'AccountId',
                    'source': 'AccountId',
                },
                'AssetFrozen': {'asset_id': 'u128'},
                'AssetMinBalanceChanged': {
                    'asset_id': 'u128',
                    'new_min_balance': 'u128',
                },
                'AssetStatusChanged': {'asset_id': 'u128'},
                'AssetThawed': {'asset_id': 'u128'},
                'Blocked': {'asset_id': 'u128', 'who': 'AccountId'},
                'Burned': {
                    'asset_id': 'u128',
                    'balance': 'u128',
                    'owner': 'AccountId',
                },
                'Created': {
                    'asset_id': 'u128',
                    'creator': 'AccountId',
                    'owner': 'AccountId',
                },
                'Destroyed': {'asset_id': 'u128'},
                'DestructionStarted': {'asset_id': 'u128'},
                'ForceCreated': {'asset_id': 'u128', 'owner': 'AccountId'},
                'Frozen': {'asset_id': 'u128', 'who': 'AccountId'},
                'Issued': {
                    'amount': 'u128',
                    'asset_id': 'u128',
                    'owner': 'AccountId',
                },
                'MetadataCleared': {'asset_id': 'u128'},
                'MetadataSet': {
                    'asset_id': 'u128',
                    'decimals': 'u8',
                    'is_frozen': 'bool',
                    'name': 'Bytes',
                    'symbol': 'Bytes',
                },
                'OwnerChanged': {'asset_id': 'u128', 'owner': 'AccountId'},
                'TeamChanged': {
                    'admin': 'AccountId',
                    'asset_id': 'u128',
                    'freezer': 'AccountId',
                    'issuer': 'AccountId',
                },
                'Thawed': {'asset_id': 'u128', 'who': 'AccountId'},
                'Touched': {
                    'asset_id': 'u128',
                    'depositor': 'AccountId',
                    'who': 'AccountId',
                },
                'Transferred': {
                    'amount': 'u128',
                    'asset_id': 'u128',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'TransferredApproved': {
                    'amount': 'u128',
                    'asset_id': 'u128',
                    'delegate': 'AccountId',
                    'destination': 'AccountId',
                    'owner': 'AccountId',
                },
            },
            'Balances': {
                'BalanceSet': {'free': 'u128', 'who': 'AccountId'},
                'Burned': {'amount': 'u128', 'who': 'AccountId'},
                'Deposit': {'amount': 'u128', 'who': 'AccountId'},
                'DustLost': {'account': 'AccountId', 'amount': 'u128'},
                'Endowed': {'account': 'AccountId', 'free_balance': 'u128'},
                'Frozen': {'amount': 'u128', 'who': 'AccountId'},
                'Issued': {'amount': 'u128'},
                'Locked': {'amount': 'u128', 'who': 'AccountId'},
                'Minted': {'amount': 'u128', 'who': 'AccountId'},
                'Rescinded': {'amount': 'u128'},
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'destination_status': 'scale_info::43',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Reserved': {'amount': 'u128', 'who': 'AccountId'},
                'Restored': {'amount': 'u128', 'who': 'AccountId'},
                'Slashed': {'amount': 'u128', 'who': 'AccountId'},
                'Suspended': {'amount': 'u128', 'who': 'AccountId'},
                'Thawed': {'amount': 'u128', 'who': 'AccountId'},
                'Transfer': {
                    'amount': 'u128',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unlocked': {'amount': 'u128', 'who': 'AccountId'},
                'Unreserved': {'amount': 'u128', 'who': 'AccountId'},
                'Upgraded': {'who': 'AccountId'},
                'Withdraw': {'amount': 'u128', 'who': 'AccountId'},
            },
            'CollatorSelection': {
                'CandidateAdded': ('AccountId', 'u128'),
                'CandidateRemoved': 'AccountId',
                'CandidateSlashed': 'AccountId',
                'NewCandidacyBond': 'u128',
                'NewDesiredCandidates': 'u32',
                'NewInvulnerables': ['AccountId'],
            },
            'Contracts': {
                'Called': {
                    'caller': 'scale_info::138',
                    'contract': 'AccountId',
                },
                'CodeRemoved': {
                    'code_hash': 'scale_info::12',
                    'deposit_released': 'u128',
                    'remover': 'AccountId',
                },
                'CodeStored': {
                    'code_hash': 'scale_info::12',
                    'deposit_held': 'u128',
                    'uploader': 'AccountId',
                },
                'ContractCodeUpdated': {
                    'contract': 'AccountId',
                    'new_code_hash': 'scale_info::12',
                    'old_code_hash': 'scale_info::12',
                },
                'ContractEmitted': {'contract': 'AccountId', 'data': 'Bytes'},
                'DelegateCalled': {
                    'code_hash': 'scale_info::12',
                    'contract': 'AccountId',
                },
                'Instantiated': {
                    'contract': 'AccountId',
                    'deployer': 'AccountId',
                },
                'StorageDepositTransferredAndHeld': {
                    'amount': 'u128',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'StorageDepositTransferredAndReleased': {
                    'amount': 'u128',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Terminated': {
                    'beneficiary': 'AccountId',
                    'contract': 'AccountId',
                },
            },
            'CumulusXcm': {
                'ExecutedDownward': ('[u8; 32]', 'scale_info::67'),
                'InvalidFormat': '[u8; 32]',
                'UnsupportedVersion': '[u8; 32]',
            },
            'DappStaking': {
                'BonusReward': {
                    'account': 'AccountId',
                    'amount': 'u128',
                    'period': 'u32',
                    'smart_contract': 'scale_info::54',
                },
                'ClaimedUnlocked': {'account': 'AccountId', 'amount': 'u128'},
                'DAppOwnerChanged': {
                    'new_owner': 'AccountId',
                    'smart_contract': 'scale_info::54',
                },
                'DAppRegistered': {
                    'dapp_id': 'u16',
                    'owner': 'AccountId',
                    'smart_contract': 'scale_info::54',
                },
                'DAppReward': {
                    'amount': 'u128',
                    'beneficiary': 'AccountId',
                    'era': 'u32',
                    'smart_contract': 'scale_info::54',
                    'tier_id': 'u8',
                },
                'DAppRewardDestinationUpdated': {
                    'beneficiary': (None, 'AccountId'),
                    'smart_contract': 'scale_info::54',
                },
                'DAppUnregistered': {
                    'era': 'u32',
                    'smart_contract': 'scale_info::54',
                },
                'ExpiredEntriesRemoved': {
                    'account': 'AccountId',
                    'count': 'u16',
                },
                'Force': {'forcing_type': 'scale_info::58'},
                'Locked': {'account': 'AccountId', 'amount': 'u128'},
                'MaintenanceMode': {'enabled': 'bool'},
                'NewEra': {'era': 'u32'},
                'NewSubperiod': {
                    'number': 'u32',
                    'subperiod': 'scale_info::53',
                },
                'Relock': {'account': 'AccountId', 'amount': 'u128'},
                'Reward': {
                    'account': 'AccountId',
                    'amount': 'u128',
                    'era': 'u32',
                },
                'Stake': {
                    'account': 'AccountId',
                    'amount': 'u128',
                    'smart_contract': 'scale_info::54',
                },
                'Unlocking': {'account': 'AccountId', 'amount': 'u128'},
                'Unstake': {
                    'account': 'AccountId',
                    'amount': 'u128',
                    'smart_contract': 'scale_info::54',
                },
                'UnstakeFromUnregistered': {
                    'account': 'AccountId',
                    'amount': 'u128',
                    'smart_contract': 'scale_info::54',
                },
            },
            'DappStakingMigration': {'SingularStakingInfoTranslated': 'u32'},
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_hash': '[u8; 32]',
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::67',
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
            'DynamicEvmBaseFee': {
                'NewBaseFeePerGas': {'fee': 'scale_info::135'},
            },
            'EVM': {
                'Created': {'address': '[u8; 20]'},
                'CreatedFailed': {'address': '[u8; 20]'},
                'Executed': {'address': '[u8; 20]'},
                'ExecutedFailed': {'address': '[u8; 20]'},
                'Log': {'log': 'scale_info::123'},
            },
            'Ethereum': {
                'Executed': {
                    'exit_reason': 'scale_info::126',
                    'extra_data': 'Bytes',
                    'from': '[u8; 20]',
                    'to': '[u8; 20]',
                    'transaction_hash': 'scale_info::12',
                },
            },
            'Identity': {
                'IdentityCleared': {'deposit': 'u128', 'who': 'AccountId'},
                'IdentityKilled': {'deposit': 'u128', 'who': 'AccountId'},
                'IdentitySet': {'who': 'AccountId'},
                'JudgementGiven': {
                    'registrar_index': 'u32',
                    'target': 'AccountId',
                },
                'JudgementRequested': {
                    'registrar_index': 'u32',
                    'who': 'AccountId',
                },
                'JudgementUnrequested': {
                    'registrar_index': 'u32',
                    'who': 'AccountId',
                },
                'RegistrarAdded': {'registrar_index': 'u32'},
                'SubIdentityAdded': {
                    'deposit': 'u128',
                    'main': 'AccountId',
                    'sub': 'AccountId',
                },
                'SubIdentityRemoved': {
                    'deposit': 'u128',
                    'main': 'AccountId',
                    'sub': 'AccountId',
                },
                'SubIdentityRevoked': {
                    'deposit': 'u128',
                    'main': 'AccountId',
                    'sub': 'AccountId',
                },
            },
            'Inflation': {
                'ForcedInflationRecalculation': {'config': 'scale_info::46'},
                'InflationConfigurationForceChanged': {
                    'config': 'scale_info::46',
                },
                'InflationParametersForceChanged': None,
                'NewInflationConfiguration': {'config': 'scale_info::46'},
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::35',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::35',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::31',
                    'timepoint': 'scale_info::35',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
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
                    'assets': 'scale_info::103',
                    'hash': 'scale_info::12',
                    'origin': 'scale_info::68',
                },
                'AssetsTrapped': {
                    'assets': 'scale_info::103',
                    'hash': 'scale_info::12',
                    'origin': 'scale_info::68',
                },
                'Attempted': {'outcome': 'scale_info::67'},
                'FeesPaid': {'fees': ['scale_info::80'], 'paying': 'scale_info::68'},
                'InvalidQuerier': {
                    'expected_querier': 'scale_info::68',
                    'maybe_actual_querier': (None, 'scale_info::68'),
                    'origin': 'scale_info::68',
                    'query_id': 'u64',
                },
                'InvalidQuerierVersion': {
                    'origin': 'scale_info::68',
                    'query_id': 'u64',
                },
                'InvalidResponder': {
                    'expected_location': (None, 'scale_info::68'),
                    'origin': 'scale_info::68',
                    'query_id': 'u64',
                },
                'InvalidResponderVersion': {
                    'origin': 'scale_info::68',
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
                    'location': 'scale_info::117',
                    'query_id': 'u64',
                },
                'NotifyTargetSendFail': {
                    'error': 'scale_info::64',
                    'location': 'scale_info::68',
                    'query_id': 'u64',
                },
                'ResponseReady': {
                    'query_id': 'u64',
                    'response': 'scale_info::86',
                },
                'ResponseTaken': {'query_id': 'u64'},
                'Sent': {
                    'destination': 'scale_info::68',
                    'message': ['scale_info::77'],
                    'message_id': '[u8; 32]',
                    'origin': 'scale_info::68',
                },
                'SupportedVersionChanged': {
                    'location': 'scale_info::68',
                    'version': 'u32',
                },
                'UnexpectedResponse': {
                    'origin': 'scale_info::68',
                    'query_id': 'u64',
                },
                'VersionChangeNotified': {
                    'cost': ['scale_info::80'],
                    'destination': 'scale_info::68',
                    'message_id': '[u8; 32]',
                    'result': 'u32',
                },
                'VersionNotifyRequested': {
                    'cost': ['scale_info::80'],
                    'destination': 'scale_info::68',
                    'message_id': '[u8; 32]',
                },
                'VersionNotifyStarted': {
                    'cost': ['scale_info::80'],
                    'destination': 'scale_info::68',
                    'message_id': '[u8; 32]',
                },
                'VersionNotifyUnrequested': {
                    'cost': ['scale_info::80'],
                    'destination': 'scale_info::68',
                    'message_id': '[u8; 32]',
                },
            },
            'Proxy': {
                'Announced': {
                    'call_hash': 'scale_info::12',
                    'proxy': 'AccountId',
                    'real': 'AccountId',
                },
                'ProxyAdded': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::37',
                },
                'ProxyExecuted': {'result': 'scale_info::31'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::37',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::37',
                    'pure': 'AccountId',
                    'who': 'AccountId',
                },
            },
            'Session': {'NewSession': {'session_index': 'u32'}},
            'StaticPriceProvider': {'PriceSet': {'price': 'u64'}},
            'Sudo': {
                'KeyChanged': {'old_sudoer': (None, 'AccountId')},
                'Sudid': {'sudo_result': 'scale_info::31'},
                'SudoAsDone': {'sudo_result': 'scale_info::31'},
            },
            'System': {
                'CodeUpdated': None,
                'ExtrinsicFailed': {
                    'dispatch_error': 'scale_info::25',
                    'dispatch_info': 'scale_info::22',
                },
                'ExtrinsicSuccess': {'dispatch_info': 'scale_info::22'},
                'KilledAccount': {'account': 'AccountId'},
                'NewAccount': {'account': 'AccountId'},
                'Remarked': {'hash': 'scale_info::12', 'sender': 'AccountId'},
            },
            'TransactionPayment': {
                'TransactionFeePaid': {
                    'actual_fee': 'u128',
                    'tip': 'u128',
                    'who': 'AccountId',
                },
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::25',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::31'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::25'},
            },
            'Vesting': {
                'VestingCompleted': {'account': 'AccountId'},
                'VestingUpdated': {'account': 'AccountId', 'unvested': 'u128'},
            },
            'XTokens': {
                'TransferredMultiAssets': {
                    'assets': ['scale_info::80'],
                    'dest': 'scale_info::68',
                    'fee': 'scale_info::80',
                    'sender': 'AccountId',
                },
            },
            'XcAssetConfig': {
                'AssetLocationChanged': {
                    'asset_id': 'u128',
                    'new_asset_location': 'scale_info::117',
                    'previous_asset_location': 'scale_info::117',
                },
                'AssetRegistered': {
                    'asset_id': 'u128',
                    'asset_location': 'scale_info::117',
                },
                'AssetRemoved': {
                    'asset_id': 'u128',
                    'asset_location': 'scale_info::117',
                },
                'SupportedAssetRemoved': {'asset_location': 'scale_info::117'},
                'UnitsPerSecondChanged': {
                    'asset_location': 'scale_info::117',
                    'units_per_second': 'u128',
                },
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': '[u8; 32]'},
                'BadVersion': {'message_hash': '[u8; 32]'},
                'Fail': {
                    'error': 'scale_info::64',
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
4096
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
            'base_extrinsic': {'proof_size': 0, 'ref_time': 124414000},
            'max_extrinsic': {'proof_size': 3407872, 'ref_time': 324875586000},
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
5
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
        ('0x37e397fc7c91f5e4', 2),
        ('0xdd718d5cc53262d4', 1),
        ('0x40fe3ad401f8959a', 6),
        ('0xd2bc9897eed08f15', 3),
        ('0xf78b278be53f454c', 2),
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 4),
        ('0xf3ff14d5ab527059', 3),
        ('0xab3c0572291feb8b', 1),
        ('0xea93e3f16f3d6962', 2),
        ('0x582211f65bb14b89', 5),
        ('0xe65b00e46cedd0aa', 2),
        ('0x68b66ba122c93fa7', 2),
        ('0xe8accb82fb152951', 1),
    ],
    'authoring_version': 1,
    'impl_name': 'astar',
    'impl_version': 0,
    'spec_name': 'astar',
    'spec_version': 83,
    'state_version': 1,
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