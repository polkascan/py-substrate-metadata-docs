
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

\#\# Complexity
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

\#\# Complexity
- `O(C + S)` where `C` length of `code` and `S` complexity of `can_set_code`
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

\#\# Complexity
- `O(C)` where `C` length of `code`
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
| dispatch_error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```
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
| hash | `T::Hash` | ```[u8; 32]```

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
        'fee_frozen': 'u128',
        'free': 'u128',
        'misc_frozen': 'u128',
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
            'System': {
                'CodeUpdated': None,
                'ExtrinsicFailed': {
                    'dispatch_error': 'scale_info::24',
                    'dispatch_info': 'scale_info::21',
                },
                'ExtrinsicSuccess': {'dispatch_info': 'scale_info::21'},
                'KilledAccount': {'account': 'AccountId'},
                'NewAccount': {'account': 'AccountId'},
                'Remarked': {'hash': '[u8; 32]', 'sender': 'AccountId'},
            },
            None: None,
            'AssetsRegistry': {
                'AssetLocationRemoved': {'asset_id': 'u128'},
                'AssetLocationUpdated': {
                    'asset_id': 'u128',
                    'location': 'scale_info::138',
                },
                'AssetRegistered': {
                    'asset_id': 'u128',
                    'asset_info': 'scale_info::149',
                    'location': (None, 'scale_info::138'),
                },
                'AssetUpdated': {
                    'asset_id': 'u128',
                    'asset_info': 'scale_info::157',
                },
                'MinFeeUpdated': {
                    'amount': (None, 'u128'),
                    'foreign_asset_id': 'scale_info::138',
                    'target_parachain_id': 'u32',
                },
            },
            'Balances': {
                'BalanceSet': {
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Deposit': {'amount': 'u128', 'who': 'AccountId'},
                'DustLost': {'account': 'AccountId', 'amount': 'u128'},
                'Endowed': {'account': 'AccountId', 'free_balance': 'u128'},
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'destination_status': 'scale_info::36',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Reserved': {'amount': 'u128', 'who': 'AccountId'},
                'Slashed': {'amount': 'u128', 'who': 'AccountId'},
                'Transfer': {
                    'amount': 'u128',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unreserved': {'amount': 'u128', 'who': 'AccountId'},
                'Withdraw': {'amount': 'u128', 'who': 'AccountId'},
            },
            'CallFilter': {
                'Disabled': {'entry': 'scale_info::283'},
                'Enabled': {'entry': 'scale_info::283'},
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
                'Approved': {'proposal_hash': '[u8; 32]'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': '[u8; 32]'},
                'Executed': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::30',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::30',
                },
                'Proposed': {
                    'account': 'AccountId',
                    'proposal_hash': '[u8; 32]',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'Voted': {
                    'account': 'AccountId',
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
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
                    'remote_account': 'scale_info::131',
                    'reward_account': 'AccountId',
                },
                'Claimed': {
                    'amount': 'u128',
                    'remote_account': 'scale_info::131',
                    'reward_account': 'AccountId',
                },
                'Initialized': {'at': 'u64'},
                'OverFunded': {'excess_funds': 'u128'},
                'RewardsAdded': {
                    'additions': [('scale_info::131', 'u128', 'u64')],
                },
                'RewardsDeleted': {'deletions': ['scale_info::131']},
                'RewardsUnlocked': {'at': 'u64'},
            },
            'CumulusXcm': {
                'ExecutedDownward': ('[u8; 32]', 'scale_info::68'),
                'InvalidFormat': '[u8; 32]',
                'UnsupportedVersion': '[u8; 32]',
            },
            'CurrencyFactory': {'RangeCreated': {'range': 'scale_info::129'}},
            'Democracy': {
                'Blacklisted': {'proposal_hash': '[u8; 32]'},
                'Cancelled': {'ref_index': 'u32'},
                'Delegated': {'target': 'AccountId', 'who': 'AccountId'},
                'ExternalTabled': None,
                'MetadataCleared': {
                    'hash': '[u8; 32]',
                    'owner': 'scale_info::52',
                },
                'MetadataSet': {'hash': '[u8; 32]', 'owner': 'scale_info::52'},
                'MetadataTransferred': {
                    'hash': '[u8; 32]',
                    'owner': 'scale_info::52',
                    'prev_owner': 'scale_info::52',
                },
                'NotPassed': {'ref_index': 'u32'},
                'Passed': {'ref_index': 'u32'},
                'ProposalCanceled': {'prop_index': 'u32'},
                'Proposed': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Seconded': {'prop_index': 'u32', 'seconder': 'AccountId'},
                'Started': {'ref_index': 'u32', 'threshold': 'scale_info::49'},
                'Tabled': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Undelegated': {'account': 'AccountId'},
                'Vetoed': {
                    'proposal_hash': '[u8; 32]',
                    'until': 'u32',
                    'who': 'AccountId',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::50',
                    'voter': 'AccountId',
                },
            },
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::68',
                },
                'InvalidFormat': {'message_id': '[u8; 32]'},
                'MaxMessagesExhausted': {'message_id': '[u8; 32]'},
                'OverweightEnqueued': {
                    'message_id': '[u8; 32]',
                    'overweight_index': 'u64',
                    'required_weight': 'scale_info::8',
                },
                'OverweightServiced': {
                    'overweight_index': 'u64',
                    'weight_used': 'scale_info::8',
                },
                'UnsupportedVersion': {'message_id': '[u8; 32]'},
                'WeightExhausted': {
                    'message_id': '[u8; 32]',
                    'remaining_weight': 'scale_info::8',
                    'required_weight': 'scale_info::8',
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
                    'height': 'scale_info::296',
                },
                'ClientUpgradeSet': None,
                'Events': {'events': ['scale_info::318']},
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
                    'timepoint': 'scale_info::38',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::38',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::30',
                    'timepoint': 'scale_info::38',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'OpenGovBalances': {
                'BalanceSet': {
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Deposit': {'amount': 'u128', 'who': 'AccountId'},
                'DustLost': {'account': 'AccountId', 'amount': 'u128'},
                'Endowed': {'account': 'AccountId', 'free_balance': 'u128'},
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'destination_status': 'scale_info::36',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Reserved': {'amount': 'u128', 'who': 'AccountId'},
                'Slashed': {'amount': 'u128', 'who': 'AccountId'},
                'Transfer': {
                    'amount': 'u128',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unreserved': {'amount': 'u128', 'who': 'AccountId'},
                'Withdraw': {'amount': 'u128', 'who': 'AccountId'},
            },
            'PalletMultihopXcmIbc': {
                'FailedCallback': {
                    'origin_address': '[u8; 32]',
                    'reason': 'scale_info::326',
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
                    'reason': 'scale_info::326',
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
            'ParachainSystem': {
                'DownwardMessagesProcessed': {
                    'dmq_head': '[u8; 32]',
                    'weight_used': 'scale_info::8',
                },
                'DownwardMessagesReceived': {'count': 'u32'},
                'UpgradeAuthorized': {'code_hash': '[u8; 32]'},
                'UpwardMessageSent': {'message_hash': (None, '[u8; 32]')},
                'ValidationFunctionApplied': {'relay_chain_block_num': 'u32'},
                'ValidationFunctionDiscarded': None,
                'ValidationFunctionStored': None,
            },
            'PolkadotXcm': {
                'AssetsClaimed': (
                    '[u8; 32]',
                    'scale_info::69',
                    'scale_info::107',
                ),
                'AssetsTrapped': (
                    '[u8; 32]',
                    'scale_info::69',
                    'scale_info::107',
                ),
                'Attempted': {
                    'Complete': 'scale_info::8',
                    'Error': 'scale_info::65',
                    'Incomplete': ('scale_info::8', 'scale_info::65'),
                },
                'FeesPaid': ('scale_info::69', ['scale_info::84']),
                'InvalidQuerier': (
                    'scale_info::69',
                    'u64',
                    'scale_info::69',
                    (None, 'scale_info::69'),
                ),
                'InvalidQuerierVersion': ('scale_info::69', 'u64'),
                'InvalidResponder': (
                    'scale_info::69',
                    'u64',
                    (None, 'scale_info::69'),
                ),
                'InvalidResponderVersion': ('scale_info::69', 'u64'),
                'Notified': ('u64', 'u8', 'u8'),
                'NotifyDecodeFailed': ('u64', 'u8', 'u8'),
                'NotifyDispatchError': ('u64', 'u8', 'u8'),
                'NotifyOverweight': (
                    'u64',
                    'u8',
                    'u8',
                    'scale_info::8',
                    'scale_info::8',
                ),
                'NotifyTargetMigrationFail': ('scale_info::121', 'u64'),
                'NotifyTargetSendFail': (
                    'scale_info::69',
                    'u64',
                    'scale_info::65',
                ),
                'ResponseReady': ('u64', 'scale_info::90'),
                'ResponseTaken': 'u64',
                'Sent': (
                    'scale_info::69',
                    'scale_info::69',
                    ['scale_info::81'],
                ),
                'SupportedVersionChanged': ('scale_info::69', 'u32'),
                'UnexpectedResponse': ('scale_info::69', 'u64'),
                'VersionChangeNotified': (
                    'scale_info::69',
                    'u32',
                    ['scale_info::84'],
                ),
                'VersionNotifyRequested': (
                    'scale_info::69',
                    ['scale_info::84'],
                ),
                'VersionNotifyStarted': ('scale_info::69', ['scale_info::84']),
                'VersionNotifyUnrequested': (
                    'scale_info::69',
                    ['scale_info::84'],
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
                    'proxy': 'AccountId',
                    'real': 'AccountId',
                },
                'ProxyAdded': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::62',
                },
                'ProxyExecuted': {'result': 'scale_info::30'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::62',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::62',
                    'pure': 'AccountId',
                    'who': 'AccountId',
                },
            },
            'Referenda': {
                'Approved': {'index': 'u32'},
                'Cancelled': {'index': 'u32', 'tally': 'scale_info::307'},
                'ConfirmAborted': {'index': 'u32'},
                'ConfirmStarted': {'index': 'u32'},
                'Confirmed': {'index': 'u32', 'tally': 'scale_info::307'},
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
                    'proposal': 'scale_info::165',
                    'tally': 'scale_info::307',
                    'track': 'u16',
                },
                'DepositSlashed': {'amount': 'u128', 'who': 'AccountId'},
                'Killed': {'index': 'u32', 'tally': 'scale_info::307'},
                'MetadataCleared': {'hash': '[u8; 32]', 'index': 'u32'},
                'MetadataSet': {'hash': '[u8; 32]', 'index': 'u32'},
                'Rejected': {'index': 'u32', 'tally': 'scale_info::307'},
                'SubmissionDepositRefunded': {
                    'amount': 'u128',
                    'index': 'u32',
                    'who': 'AccountId',
                },
                'Submitted': {
                    'index': 'u32',
                    'proposal': 'scale_info::165',
                    'track': 'u16',
                },
                'TimedOut': {'index': 'u32', 'tally': 'scale_info::307'},
            },
            'ReleaseCommittee': {
                'Approved': {'proposal_hash': '[u8; 32]'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': '[u8; 32]'},
                'Executed': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::30',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::30',
                },
                'Proposed': {
                    'account': 'AccountId',
                    'proposal_hash': '[u8; 32]',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'Voted': {
                    'account': 'AccountId',
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
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
                    'result': 'scale_info::30',
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
                'Sudid': {'sudo_result': 'scale_info::30'},
                'SudoAsDone': {'sudo_result': 'scale_info::30'},
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
                    'result': 'scale_info::30',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::30',
                },
                'Proposed': {
                    'account': 'AccountId',
                    'proposal_hash': '[u8; 32]',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'Voted': {
                    'account': 'AccountId',
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
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
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'currency_id': 'u128',
                    'from': 'AccountId',
                    'status': 'scale_info::36',
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
                    'asset': 'scale_info::84',
                    'who': 'scale_info::69',
                },
                'Withdrawn': {
                    'asset': 'scale_info::84',
                    'who': 'scale_info::69',
                },
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::24',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::30'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::24'},
            },
            'Whitelist': {
                'CallWhitelisted': {'call_hash': '[u8; 32]'},
                'WhitelistedCallDispatched': {
                    'call_hash': '[u8; 32]',
                    'result': 'scale_info::311',
                },
                'WhitelistedCallRemoved': {'call_hash': '[u8; 32]'},
            },
            'XTokens': {
                'TransferredMultiAssets': {
                    'assets': ['scale_info::84'],
                    'dest': 'scale_info::69',
                    'fee': 'scale_info::84',
                    'sender': 'AccountId',
                },
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': (None, '[u8; 32]')},
                'BadVersion': {'message_hash': (None, '[u8; 32]')},
                'Fail': {
                    'error': 'scale_info::65',
                    'message_hash': (None, '[u8; 32]'),
                    'weight': 'scale_info::8',
                },
                'OverweightEnqueued': {
                    'index': 'u64',
                    'required': 'scale_info::8',
                    'sender': 'u32',
                    'sent_at': 'u32',
                },
                'OverweightServiced': {
                    'index': 'u64',
                    'used': 'scale_info::8',
                },
                'Success': {'message_hash': (None, '[u8; 32]'), 'weight': 'scale_info::8'},
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
    'base_block': {'proof_size': 0, 'ref_time': 381015000},
    'max_block': {'proof_size': 5242880, 'ref_time': 500000000000},
    'per_class': {
        'mandatory': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 99840000},
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 99840000},
            'max_extrinsic': {'proof_size': 3670016, 'ref_time': 349900160000},
            'max_total': {'proof_size': 3932160, 'ref_time': 375000000000},
            'reserved': {'proof_size': 0, 'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 99840000},
            'max_extrinsic': {'proof_size': 4980736, 'ref_time': 474900160000},
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
        ('0x37e397fc7c91f5e4', 1),
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
    'impl_version': 1,
    'spec_name': 'composable',
    'spec_version': 10039,
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