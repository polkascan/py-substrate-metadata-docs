
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

 The value has the type `(T::BlockNumber, EventIndex)` because if we used only just
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
            'AssetsRegistry': {
                'AssetLocationRemoved': {'asset_id': 'u128'},
                'AssetLocationUpdated': {
                    'asset_id': 'u128',
                    'location': 'scale_info::137',
                },
                'AssetRegistered': {
                    'asset_id': 'u128',
                    'asset_info': 'scale_info::148',
                    'location': (None, 'scale_info::137'),
                },
                'AssetUpdated': {
                    'asset_id': 'u128',
                    'asset_info': 'scale_info::156',
                },
                'MinFeeUpdated': {
                    'amount': (None, 'u128'),
                    'foreign_asset_id': 'scale_info::137',
                    'target_parachain_id': 'u32',
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
                    'destination_status': 'scale_info::37',
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
            'CallFilter': {
                'Disabled': {'entry': 'scale_info::276'},
                'Enabled': {'entry': 'scale_info::276'},
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
            'ConvictionVoting': {'Delegated': ('AccountId', 'AccountId'), 'Undelegated': 'AccountId'},
            'Council': {
                'Approved': {'proposal_hash': 'scale_info::12'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': 'scale_info::12',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': 'scale_info::12'},
                'Executed': {
                    'proposal_hash': 'scale_info::12',
                    'result': 'scale_info::31',
                },
                'MemberExecuted': {
                    'proposal_hash': 'scale_info::12',
                    'result': 'scale_info::31',
                },
                'Proposed': {
                    'account': 'AccountId',
                    'proposal_hash': 'scale_info::12',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'Voted': {
                    'account': 'AccountId',
                    'no': 'u32',
                    'proposal_hash': 'scale_info::12',
                    'voted': 'bool',
                    'yes': 'u32',
                },
            },
            'CouncilMembership': (
                'MemberAdded',
                'MemberRemoved',
                'MembersSwapped',
                'MembersReset',
                'KeyChanged',
                'Dummy',
            ),
            'CrowdloanRewards': {
                'Associated': {
                    'remote_account': 'scale_info::130',
                    'reward_account': 'AccountId',
                },
                'Claimed': {
                    'amount': 'u128',
                    'remote_account': 'scale_info::130',
                    'reward_account': 'AccountId',
                },
                'Initialized': {'at': 'u64'},
                'OverFunded': {'excess_funds': 'u128'},
                'RewardsAdded': {
                    'additions': [('scale_info::130', 'u128', 'u64')],
                },
                'RewardsDeleted': {'deletions': ['scale_info::130']},
                'RewardsUnlocked': {'at': 'u64'},
            },
            'CumulusXcm': {
                'ExecutedDownward': ('[u8; 32]', 'scale_info::69'),
                'InvalidFormat': '[u8; 32]',
                'UnsupportedVersion': '[u8; 32]',
            },
            'Democracy': {
                'Blacklisted': {'proposal_hash': 'scale_info::12'},
                'Cancelled': {'ref_index': 'u32'},
                'Delegated': {'target': 'AccountId', 'who': 'AccountId'},
                'ExternalTabled': None,
                'MetadataCleared': {
                    'hash': 'scale_info::12',
                    'owner': 'scale_info::53',
                },
                'MetadataSet': {
                    'hash': 'scale_info::12',
                    'owner': 'scale_info::53',
                },
                'MetadataTransferred': {
                    'hash': 'scale_info::12',
                    'owner': 'scale_info::53',
                    'prev_owner': 'scale_info::53',
                },
                'NotPassed': {'ref_index': 'u32'},
                'Passed': {'ref_index': 'u32'},
                'ProposalCanceled': {'prop_index': 'u32'},
                'Proposed': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Seconded': {'prop_index': 'u32', 'seconder': 'AccountId'},
                'Started': {'ref_index': 'u32', 'threshold': 'scale_info::50'},
                'Tabled': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Undelegated': {'account': 'AccountId'},
                'Vetoed': {
                    'proposal_hash': 'scale_info::12',
                    'until': 'u32',
                    'who': 'AccountId',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::51',
                    'voter': 'AccountId',
                },
            },
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::69',
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
            'Ibc': {
                'AssetAdminUpdated': {'admin_account': 'AccountId'},
                'ChannelOpened': {'channel_id': 'Bytes', 'port_id': 'Bytes'},
                'ChargingFeeConfirmed': {'sequence': 'u64'},
                'ChargingFeeFailedAcknowledgement': {'sequence': 'u64'},
                'ChargingFeeOnTransferInitiated': {
                    'amount': 'u128',
                    'destination_channel': 'Bytes',
                    'from': 'Bytes',
                    'ibc_denom': 'Bytes',
                    'is_flat_fee': 'bool',
                    'local_asset_id': (None, 'u128'),
                    'sequence': 'u64',
                    'source_channel': 'Bytes',
                    'to': 'Bytes',
                },
                'ChargingFeeTimeout': {'sequence': 'u64'},
                'ChildStateUpdated': None,
                'ClientFrozen': {
                    'client_id': 'Bytes',
                    'height': 'u64',
                    'revision_number': 'u64',
                },
                'ClientStateSubstituted': {
                    'client_id': 'Str',
                    'height': 'scale_info::289',
                },
                'ClientUpgradeSet': None,
                'Events': {'events': ['scale_info::323']},
                'ExecuteMemoIbcTokenTransferFailed': {
                    'amount': 'u128',
                    'asset_id': 'u128',
                    'channel': 'u64',
                    'from': 'AccountId',
                    'next_memo': (None, 'Str'),
                    'to': 'Bytes',
                },
                'ExecuteMemoIbcTokenTransferFailedWithReason': {
                    'from': 'AccountId',
                    'memo': 'Str',
                    'reason': 'u8',
                },
                'ExecuteMemoIbcTokenTransferSuccess': {
                    'amount': 'u128',
                    'asset_id': 'u128',
                    'channel': 'u64',
                    'from': 'AccountId',
                    'next_memo': (None, 'Str'),
                    'to': 'Bytes',
                },
                'ExecuteMemoStarted': {
                    'account_id': 'AccountId',
                    'memo': (None, 'Str'),
                },
                'ExecuteMemoXcmFailed': {
                    'amount': 'u128',
                    'asset_id': 'u128',
                    'from': 'AccountId',
                    'para_id': (None, 'u32'),
                    'to': 'AccountId',
                },
                'ExecuteMemoXcmSuccess': {
                    'amount': 'u128',
                    'asset_id': 'u128',
                    'from': 'AccountId',
                    'para_id': (None, 'u32'),
                    'to': 'AccountId',
                },
                'FeeLessChannelIdsAdded': {
                    'destination_channel': 'u64',
                    'source_channel': 'u64',
                },
                'FeeLessChannelIdsRemoved': {
                    'destination_channel': 'u64',
                    'source_channel': 'u64',
                },
                'OnRecvPacketError': {'msg': 'Bytes'},
                'ParamsUpdated': {
                    'receive_enabled': 'bool',
                    'send_enabled': 'bool',
                },
                'TokenReceived': {
                    'amount': 'u128',
                    'destination_channel': 'Bytes',
                    'from': 'Str',
                    'ibc_denom': 'Bytes',
                    'is_receiver_source': 'bool',
                    'local_asset_id': (None, 'u128'),
                    'source_channel': 'Bytes',
                    'to': 'Str',
                },
                'TokenTransferCompleted': {
                    'amount': 'u128',
                    'destination_channel': 'Bytes',
                    'from': 'Str',
                    'ibc_denom': 'Bytes',
                    'is_sender_source': 'bool',
                    'local_asset_id': (None, 'u128'),
                    'source_channel': 'Bytes',
                    'to': 'Str',
                },
                'TokenTransferFailed': {
                    'amount': 'u128',
                    'destination_channel': 'Bytes',
                    'from': 'Str',
                    'ibc_denom': 'Bytes',
                    'is_sender_source': 'bool',
                    'local_asset_id': (None, 'u128'),
                    'source_channel': 'Bytes',
                    'to': 'Str',
                },
                'TokenTransferInitiated': {
                    'amount': 'u128',
                    'destination_channel': 'Bytes',
                    'from': 'Bytes',
                    'ibc_denom': 'Bytes',
                    'is_sender_source': 'bool',
                    'local_asset_id': (None, 'u128'),
                    'source_channel': 'Bytes',
                    'to': 'Bytes',
                },
                'TokenTransferTimeout': {
                    'amount': 'u128',
                    'destination_channel': 'Bytes',
                    'from': 'Str',
                    'ibc_denom': 'Bytes',
                    'is_sender_source': 'bool',
                    'local_asset_id': (None, 'u128'),
                    'source_channel': 'Bytes',
                    'to': 'Str',
                },
            },
            'Ics20Fee': {
                'FeeLessChannelIdsAdded': {
                    'destination_channel': 'u64',
                    'source_channel': 'u64',
                },
                'FeeLessChannelIdsRemoved': {
                    'destination_channel': 'u64',
                    'source_channel': 'u64',
                },
                'IbcTransferFeeCollected': {
                    'amount': 'u128',
                    'asset_id': 'u128',
                },
            },
            'Indices': {
                'IndexAssigned': {'index': 'u32', 'who': 'AccountId'},
                'IndexFreed': {'index': 'u32'},
                'IndexFrozen': {'index': 'u32', 'who': 'AccountId'},
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::39',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::39',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::31',
                    'timepoint': 'scale_info::39',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'OpenGovBalances': {
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
                    'destination_status': 'scale_info::37',
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
            'PalletLiquidStaking': {
                'Bonding': ('u16', 'AccountId', 'u128', 'scale_info::305'),
                'BondingExtra': ('u16', 'u128'),
                'ClaimedFor': ('AccountId', 'u128'),
                'CommissionRateUpdated': 'u128',
                'ExchangeRateUpdated': 'u128',
                'FastUnstakeMatched': ('AccountId', 'u128', 'u128', 'u128'),
                'IncentiveUpdated': 'u128',
                'Matching': ('u128', 'u128', 'u128'),
                'NewEra': 'u32',
                'Nominating': ('u16', ['AccountId']),
                'NonIdealStakingLedger': 'u16',
                'NotificationReceived': (
                    'scale_info::70',
                    'u64',
                    (None, ('u32', 'scale_info::66')),
                ),
                'OnInitializeHook': {
                    'era': 'u32',
                    'relay_block_number': 'u32',
                },
                'Rebonding': ('u16', 'u128'),
                'RelaychainStorageProofKey': ('u16', 'Bytes', 'AccountId'),
                'ReserveFactorUpdated': 'u32',
                'ReservesReduced': ('AccountId', 'u128'),
                'SetMembers': {'members': ['AccountId']},
                'SetStakingLedgerTry': {
                    'derivative_index': 'u16',
                    'origin': 'AccountId',
                    'proof': ['Bytes'],
                    'staking_ledger': 'scale_info::306',
                },
                'Staked': ('AccountId', 'u128'),
                'StakingLedgerCapUpdated': 'u128',
                'StakingLedgerUpdated': ('u16', 'scale_info::306'),
                'Unbonding': ('u16', 'u128'),
                'UnstakeCancelled': ('AccountId', 'u128', 'u128'),
                'Unstaked': ('AccountId', 'u128', 'u128'),
                'WithdrawingUnbonded': ('u16', 'u32'),
            },
            'PalletMultihopXcmIbc': {
                'FailedCallback': {
                    'origin_address': '[u8; 32]',
                    'reason': 'scale_info::331',
                    'route_id': 'u128',
                },
                'FailedMatchLocation': None,
                'FailedXcmToIbc': {
                    'amount': 'u128',
                    'asset_id': 'u128',
                    'memo': (None, 'Str'),
                    'origin_address': 'AccountId',
                    'to': '[u8; 32]',
                },
                'MultihopXcmMemo': {
                    'amount': 'u128',
                    'asset_id': 'u128',
                    'from': 'AccountId',
                    'is_error': 'bool',
                    'reason': 'scale_info::331',
                    'to': 'AccountId',
                },
                'SuccessXcmToIbc': {
                    'amount': 'u128',
                    'asset_id': 'u128',
                    'memo': (None, 'Str'),
                    'origin_address': 'AccountId',
                    'to': '[u8; 32]',
                },
            },
            'PalletXcmHelper': {
                'XcmWeightFeeUpdated': {
                    'fee': 'u128',
                    'weight': 'scale_info::9',
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
                'AssetsClaimed': (
                    'scale_info::12',
                    'scale_info::70',
                    'scale_info::108',
                ),
                'AssetsTrapped': (
                    'scale_info::12',
                    'scale_info::70',
                    'scale_info::108',
                ),
                'Attempted': {
                    'Complete': 'scale_info::9',
                    'Error': 'scale_info::66',
                    'Incomplete': ('scale_info::9', 'scale_info::66'),
                },
                'FeesPaid': ('scale_info::70', ['scale_info::85']),
                'InvalidQuerier': (
                    'scale_info::70',
                    'u64',
                    'scale_info::70',
                    (None, 'scale_info::70'),
                ),
                'InvalidQuerierVersion': ('scale_info::70', 'u64'),
                'InvalidResponder': (
                    'scale_info::70',
                    'u64',
                    (None, 'scale_info::70'),
                ),
                'InvalidResponderVersion': ('scale_info::70', 'u64'),
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
                'NotifyTargetMigrationFail': ('scale_info::122', 'u64'),
                'NotifyTargetSendFail': (
                    'scale_info::70',
                    'u64',
                    'scale_info::66',
                ),
                'ResponseReady': ('u64', 'scale_info::91'),
                'ResponseTaken': 'u64',
                'Sent': (
                    'scale_info::70',
                    'scale_info::70',
                    ['scale_info::82'],
                ),
                'SupportedVersionChanged': ('scale_info::70', 'u32'),
                'UnexpectedResponse': ('scale_info::70', 'u64'),
                'VersionChangeNotified': (
                    'scale_info::70',
                    'u32',
                    ['scale_info::85'],
                ),
                'VersionNotifyRequested': (
                    'scale_info::70',
                    ['scale_info::85'],
                ),
                'VersionNotifyStarted': ('scale_info::70', ['scale_info::85']),
                'VersionNotifyUnrequested': (
                    'scale_info::70',
                    ['scale_info::85'],
                ),
            },
            'Preimage': {
                'Cleared': {'hash': 'scale_info::12'},
                'Noted': {'hash': 'scale_info::12'},
                'Requested': {'hash': 'scale_info::12'},
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
                    'proxy_type': 'scale_info::63',
                },
                'ProxyExecuted': {'result': 'scale_info::31'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::63',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::63',
                    'pure': 'AccountId',
                    'who': 'AccountId',
                },
            },
            'Referenda': {
                'Approved': {'index': 'u32'},
                'Cancelled': {'index': 'u32', 'tally': 'scale_info::312'},
                'ConfirmAborted': {'index': 'u32'},
                'ConfirmStarted': {'index': 'u32'},
                'Confirmed': {'index': 'u32', 'tally': 'scale_info::312'},
                'DecisionDepositPlaced': {
                    'amount': 'u128',
                    'index': 'u32',
                    'who': 'AccountId',
                },
                'DecisionDepositRefunded': {
                    'amount': 'u128',
                    'index': 'u32',
                    'who': 'AccountId',
                },
                'DecisionStarted': {
                    'index': 'u32',
                    'proposal': 'scale_info::164',
                    'tally': 'scale_info::312',
                    'track': 'u16',
                },
                'DepositSlashed': {'amount': 'u128', 'who': 'AccountId'},
                'Killed': {'index': 'u32', 'tally': 'scale_info::312'},
                'MetadataCleared': {'hash': 'scale_info::12', 'index': 'u32'},
                'MetadataSet': {'hash': 'scale_info::12', 'index': 'u32'},
                'Rejected': {'index': 'u32', 'tally': 'scale_info::312'},
                'SubmissionDepositRefunded': {
                    'amount': 'u128',
                    'index': 'u32',
                    'who': 'AccountId',
                },
                'Submitted': {
                    'index': 'u32',
                    'proposal': 'scale_info::164',
                    'track': 'u16',
                },
                'TimedOut': {'index': 'u32', 'tally': 'scale_info::312'},
            },
            'ReleaseCommittee': {
                'Approved': {'proposal_hash': 'scale_info::12'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': 'scale_info::12',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': 'scale_info::12'},
                'Executed': {
                    'proposal_hash': 'scale_info::12',
                    'result': 'scale_info::31',
                },
                'MemberExecuted': {
                    'proposal_hash': 'scale_info::12',
                    'result': 'scale_info::31',
                },
                'Proposed': {
                    'account': 'AccountId',
                    'proposal_hash': 'scale_info::12',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'Voted': {
                    'account': 'AccountId',
                    'no': 'u32',
                    'proposal_hash': 'scale_info::12',
                    'voted': 'bool',
                    'yes': 'u32',
                },
            },
            'ReleaseMembership': (
                'MemberAdded',
                'MemberRemoved',
                'MembersSwapped',
                'MembersReset',
                'KeyChanged',
                'Dummy',
            ),
            'Scheduler': {
                'CallUnavailable': {
                    'id': (None, '[u8; 32]'),
                    'task': ('u32', 'u32'),
                },
                'Canceled': {'index': 'u32', 'when': 'u32'},
                'Dispatched': {
                    'id': (None, '[u8; 32]'),
                    'result': 'scale_info::31',
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
            'TechnicalCommittee': {
                'Approved': {'proposal_hash': 'scale_info::12'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': 'scale_info::12',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': 'scale_info::12'},
                'Executed': {
                    'proposal_hash': 'scale_info::12',
                    'result': 'scale_info::31',
                },
                'MemberExecuted': {
                    'proposal_hash': 'scale_info::12',
                    'result': 'scale_info::31',
                },
                'Proposed': {
                    'account': 'AccountId',
                    'proposal_hash': 'scale_info::12',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'Voted': {
                    'account': 'AccountId',
                    'no': 'u32',
                    'proposal_hash': 'scale_info::12',
                    'voted': 'bool',
                    'yes': 'u32',
                },
            },
            'TechnicalCommitteeMembership': (
                'MemberAdded',
                'MemberRemoved',
                'MembersSwapped',
                'MembersReset',
                'KeyChanged',
                'Dummy',
            ),
            'Tokens': {
                'BalanceSet': {
                    'currency_id': 'u128',
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Deposited': {
                    'amount': 'u128',
                    'currency_id': 'u128',
                    'who': 'AccountId',
                },
                'DustLost': {
                    'amount': 'u128',
                    'currency_id': 'u128',
                    'who': 'AccountId',
                },
                'Endowed': {
                    'amount': 'u128',
                    'currency_id': 'u128',
                    'who': 'AccountId',
                },
                'Issued': {'amount': 'u128', 'currency_id': 'u128'},
                'LockRemoved': {
                    'currency_id': 'u128',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'LockSet': {
                    'amount': 'u128',
                    'currency_id': 'u128',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'Locked': {
                    'amount': 'u128',
                    'currency_id': 'u128',
                    'who': 'AccountId',
                },
                'Rescinded': {'amount': 'u128', 'currency_id': 'u128'},
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'currency_id': 'u128',
                    'from': 'AccountId',
                    'status': 'scale_info::37',
                    'to': 'AccountId',
                },
                'Reserved': {
                    'amount': 'u128',
                    'currency_id': 'u128',
                    'who': 'AccountId',
                },
                'Slashed': {
                    'currency_id': 'u128',
                    'free_amount': 'u128',
                    'reserved_amount': 'u128',
                    'who': 'AccountId',
                },
                'TotalIssuanceSet': {'amount': 'u128', 'currency_id': 'u128'},
                'Transfer': {
                    'amount': 'u128',
                    'currency_id': 'u128',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unlocked': {
                    'amount': 'u128',
                    'currency_id': 'u128',
                    'who': 'AccountId',
                },
                'Unreserved': {
                    'amount': 'u128',
                    'currency_id': 'u128',
                    'who': 'AccountId',
                },
                'Withdrawn': {
                    'amount': 'u128',
                    'currency_id': 'u128',
                    'who': 'AccountId',
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
                'UpdatedInactive': {
                    'deactivated': 'u128',
                    'reactivated': 'u128',
                },
            },
            'UnknownTokens': {
                'Deposited': {
                    'asset': 'scale_info::85',
                    'who': 'scale_info::70',
                },
                'Withdrawn': {
                    'asset': 'scale_info::85',
                    'who': 'scale_info::70',
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
            'Whitelist': {
                'CallWhitelisted': {'call_hash': 'scale_info::12'},
                'WhitelistedCallDispatched': {
                    'call_hash': 'scale_info::12',
                    'result': 'scale_info::316',
                },
                'WhitelistedCallRemoved': {'call_hash': 'scale_info::12'},
            },
            'XTokens': {
                'TransferredMultiAssets': {
                    'assets': ['scale_info::85'],
                    'dest': 'scale_info::70',
                    'fee': 'scale_info::85',
                    'sender': 'AccountId',
                },
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': (None, '[u8; 32]')},
                'BadVersion': {'message_hash': (None, '[u8; 32]')},
                'Fail': {
                    'error': 'scale_info::66',
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
250
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
50
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
        ('0x9c53906fa888fe7c', 1),
        ('0x5c497be959ff24ab', 1),
        ('0xdf6acb689907609b', 4),
        ('0x37e397fc7c91f5e4', 2),
        ('0x40fe3ad401f8959a', 6),
        ('0xd2bc9897eed08f15', 3),
        ('0xf78b278be53f454c', 2),
        ('0xdd718d5cc53262d4', 1),
        ('0xab3c0572291feb8b', 1),
        ('0xea93e3f16f3d6962', 2),
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 1),
        ('0xa74824145d05c12a', 1),
    ],
    'authoring_version': 1,
    'impl_name': 'composable',
    'impl_version': 0,
    'spec_name': 'composable',
    'spec_version': 10044,
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