
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
            None: None,
            'Consensus': ('[u8; 4]', 'Bytes'),
            'Other': 'Bytes',
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
            None: None,
            'AssetRate': {
                'AssetRateCreated': {
                    'asset_kind': 'scale_info::59',
                    'rate': 'u128',
                },
                'AssetRateRemoved': {'asset_kind': 'scale_info::59'},
                'AssetRateUpdated': {
                    'asset_kind': 'scale_info::59',
                    'new': 'u128',
                    'old': 'u128',
                },
            },
            'Auctions': {
                'AuctionClosed': {'auction_index': 'u32'},
                'AuctionStarted': {
                    'auction_index': 'u32',
                    'ending': 'u32',
                    'lease_period': 'u32',
                },
                'BidAccepted': {
                    'amount': 'u128',
                    'bidder': 'AccountId',
                    'first_slot': 'u32',
                    'last_slot': 'u32',
                    'para_id': 'u32',
                },
                'ReserveConfiscated': {
                    'amount': 'u128',
                    'leaser': 'AccountId',
                    'para_id': 'u32',
                },
                'Reserved': {
                    'bidder': 'AccountId',
                    'extra_reserved': 'u128',
                    'total_amount': 'u128',
                },
                'Unreserved': {'amount': 'u128', 'bidder': 'AccountId'},
                'WinningOffset': {
                    'auction_index': 'u32',
                    'block_number': 'u32',
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
                    'destination_status': 'scale_info::32',
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
            'Bounties': {
                'BountyApproved': {'index': 'u32'},
                'BountyAwarded': {'beneficiary': 'AccountId', 'index': 'u32'},
                'BountyBecameActive': {'index': 'u32'},
                'BountyCanceled': {'index': 'u32'},
                'BountyClaimed': {
                    'beneficiary': 'AccountId',
                    'index': 'u32',
                    'payout': 'u128',
                },
                'BountyExtended': {'index': 'u32'},
                'BountyProposed': {'index': 'u32'},
                'BountyRejected': {'bond': 'u128', 'index': 'u32'},
                'CuratorAccepted': {
                    'bounty_id': 'u32',
                    'curator': 'AccountId',
                },
                'CuratorProposed': {
                    'bounty_id': 'u32',
                    'curator': 'AccountId',
                },
                'CuratorUnassigned': {'bounty_id': 'u32'},
            },
            'ChildBounties': {
                'Added': {'child_index': 'u32', 'index': 'u32'},
                'Awarded': {
                    'beneficiary': 'AccountId',
                    'child_index': 'u32',
                    'index': 'u32',
                },
                'Canceled': {'child_index': 'u32', 'index': 'u32'},
                'Claimed': {
                    'beneficiary': 'AccountId',
                    'child_index': 'u32',
                    'index': 'u32',
                    'payout': 'u128',
                },
            },
            'Claims': {
                'Claimed': {
                    'amount': 'u128',
                    'ethereum_address': '[u8; 20]',
                    'who': 'AccountId',
                },
            },
            'ConvictionVoting': {'Delegated': ('AccountId', 'AccountId'), 'Undelegated': 'AccountId'},
            'Crowdloan': {
                'AddedToNewRaise': {'para_id': 'u32'},
                'AllRefunded': {'para_id': 'u32'},
                'Contributed': {
                    'amount': 'u128',
                    'fund_index': 'u32',
                    'who': 'AccountId',
                },
                'Created': {'para_id': 'u32'},
                'Dissolved': {'para_id': 'u32'},
                'Edited': {'para_id': 'u32'},
                'HandleBidResult': {
                    'para_id': 'u32',
                    'result': 'scale_info::476',
                },
                'MemoUpdated': {
                    'memo': 'Bytes',
                    'para_id': 'u32',
                    'who': 'AccountId',
                },
                'PartiallyRefunded': {'para_id': 'u32'},
                'Withdrew': {
                    'amount': 'u128',
                    'fund_index': 'u32',
                    'who': 'AccountId',
                },
            },
            'ElectionProviderMultiPhase': {
                'ElectionFailed': None,
                'ElectionFinalized': {
                    'compute': 'scale_info::490',
                    'score': 'scale_info::301',
                },
                'PhaseTransitioned': {
                    'from': 'scale_info::491',
                    'round': 'u32',
                    'to': 'scale_info::491',
                },
                'Rewarded': {'account': 'AccountId', 'value': 'u128'},
                'Slashed': {'account': 'AccountId', 'value': 'u128'},
                'SolutionStored': {
                    'compute': 'scale_info::490',
                    'origin': (None, 'AccountId'),
                    'prev_ejected': 'bool',
                },
            },
            'FastUnstake': {
                'BatchChecked': {'eras': ['u32']},
                'BatchFinished': {'size': 'u32'},
                'InternalError': None,
                'Slashed': {'amount': 'u128', 'stash': 'AccountId'},
                'Unstaked': {
                    'result': 'scale_info::476',
                    'stash': 'AccountId',
                },
            },
            'FellowshipCollective': {
                'MemberAdded': {'who': 'AccountId'},
                'MemberRemoved': {'rank': 'u16', 'who': 'AccountId'},
                'RankChanged': {'rank': 'u16', 'who': 'AccountId'},
                'Voted': {
                    'poll': 'u32',
                    'tally': 'scale_info::467',
                    'vote': 'scale_info::466',
                    'who': 'AccountId',
                },
            },
            'FellowshipReferenda': {
                'Approved': {'index': 'u32'},
                'Cancelled': {'index': 'u32', 'tally': 'scale_info::467'},
                'ConfirmAborted': {'index': 'u32'},
                'ConfirmStarted': {'index': 'u32'},
                'Confirmed': {'index': 'u32', 'tally': 'scale_info::467'},
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
                    'proposal': 'scale_info::81',
                    'tally': 'scale_info::467',
                    'track': 'u16',
                },
                'DepositSlashed': {'amount': 'u128', 'who': 'AccountId'},
                'Killed': {'index': 'u32', 'tally': 'scale_info::467'},
                'MetadataCleared': {'hash': 'scale_info::12', 'index': 'u32'},
                'MetadataSet': {'hash': 'scale_info::12', 'index': 'u32'},
                'Rejected': {'index': 'u32', 'tally': 'scale_info::467'},
                'SubmissionDepositRefunded': {
                    'amount': 'u128',
                    'index': 'u32',
                    'who': 'AccountId',
                },
                'Submitted': {
                    'index': 'u32',
                    'proposal': 'scale_info::81',
                    'track': 'u16',
                },
                'TimedOut': {'index': 'u32', 'tally': 'scale_info::467'},
            },
            'Grandpa': {
                'NewAuthorities': {'authority_set': [('[u8; 32]', 'u64')]},
                'Paused': None,
                'Resumed': None,
            },
            'Hrmp': {
                'ChannelClosed': {
                    'by_parachain': 'u32',
                    'channel_id': 'scale_info::373',
                },
                'HrmpChannelForceOpened': {
                    'proposed_max_capacity': 'u32',
                    'proposed_max_message_size': 'u32',
                    'recipient': 'u32',
                    'sender': 'u32',
                },
                'HrmpSystemChannelOpened': {
                    'proposed_max_capacity': 'u32',
                    'proposed_max_message_size': 'u32',
                    'recipient': 'u32',
                    'sender': 'u32',
                },
                'OpenChannelAccepted': {'recipient': 'u32', 'sender': 'u32'},
                'OpenChannelCanceled': {
                    'by_parachain': 'u32',
                    'channel_id': 'scale_info::373',
                },
                'OpenChannelDepositsUpdated': {
                    'recipient': 'u32',
                    'sender': 'u32',
                },
                'OpenChannelRequested': {
                    'proposed_max_capacity': 'u32',
                    'proposed_max_message_size': 'u32',
                    'recipient': 'u32',
                    'sender': 'u32',
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
            'ImOnline': {
                'AllGood': None,
                'HeartbeatReceived': {'authority_id': '[u8; 32]'},
                'SomeOffline': {'offline': [('AccountId', 'scale_info::54')]},
            },
            'Indices': {
                'IndexAssigned': {'index': 'u32', 'who': 'AccountId'},
                'IndexFreed': {'index': 'u32'},
                'IndexFrozen': {'index': 'u32', 'who': 'AccountId'},
            },
            'MessageQueue': {
                'OverweightEnqueued': {
                    'id': '[u8; 32]',
                    'message_index': 'u32',
                    'origin': 'scale_info::450',
                    'page_index': 'u32',
                },
                'PageReaped': {'index': 'u32', 'origin': 'scale_info::450'},
                'Processed': {
                    'id': '[u8; 32]',
                    'origin': 'scale_info::450',
                    'success': 'bool',
                    'weight_used': 'scale_info::9',
                },
                'ProcessingFailed': {
                    'error': 'scale_info::517',
                    'id': '[u8; 32]',
                    'origin': 'scale_info::450',
                },
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::219',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::219',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::476',
                    'timepoint': 'scale_info::219',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'Nis': {
                'BidDropped': {
                    'amount': 'u128',
                    'duration': 'u32',
                    'who': 'AccountId',
                },
                'BidPlaced': {
                    'amount': 'u128',
                    'duration': 'u32',
                    'who': 'AccountId',
                },
                'BidRetracted': {
                    'amount': 'u128',
                    'duration': 'u32',
                    'who': 'AccountId',
                },
                'Funded': {'deficit': 'u128'},
                'Issued': {
                    'amount': 'u128',
                    'expiry': 'u32',
                    'index': 'u32',
                    'proportion': 'u64',
                    'who': 'AccountId',
                },
                'Thawed': {
                    'amount': 'u128',
                    'dropped': 'bool',
                    'index': 'u32',
                    'proportion': 'u64',
                    'who': 'AccountId',
                },
                'Transferred': {
                    'from': 'AccountId',
                    'index': 'u32',
                    'to': 'AccountId',
                },
            },
            'NisCounterpartBalances': {
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
                    'destination_status': 'scale_info::32',
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
            'NominationPools': {
                'Bonded': {
                    'bonded': 'u128',
                    'joined': 'bool',
                    'member': 'AccountId',
                    'pool_id': 'u32',
                },
                'Created': {'depositor': 'AccountId', 'pool_id': 'u32'},
                'Destroyed': {'pool_id': 'u32'},
                'MemberRemoved': {'member': 'AccountId', 'pool_id': 'u32'},
                'MinBalanceDeficitAdjusted': {
                    'amount': 'u128',
                    'pool_id': 'u32',
                },
                'MinBalanceExcessAdjusted': {
                    'amount': 'u128',
                    'pool_id': 'u32',
                },
                'PaidOut': {
                    'member': 'AccountId',
                    'payout': 'u128',
                    'pool_id': 'u32',
                },
                'PoolCommissionChangeRateUpdated': {
                    'change_rate': 'scale_info::324',
                    'pool_id': 'u32',
                },
                'PoolCommissionClaimed': {
                    'commission': 'u128',
                    'pool_id': 'u32',
                },
                'PoolCommissionUpdated': {
                    'current': (None, ('u32', 'AccountId')),
                    'pool_id': 'u32',
                },
                'PoolMaxCommissionUpdated': {
                    'max_commission': 'u32',
                    'pool_id': 'u32',
                },
                'PoolSlashed': {'balance': 'u128', 'pool_id': 'u32'},
                'RolesUpdated': {
                    'bouncer': (None, 'AccountId'),
                    'nominator': (None, 'AccountId'),
                    'root': (None, 'AccountId'),
                },
                'StateChanged': {
                    'new_state': 'scale_info::316',
                    'pool_id': 'u32',
                },
                'Unbonded': {
                    'balance': 'u128',
                    'era': 'u32',
                    'member': 'AccountId',
                    'points': 'u128',
                    'pool_id': 'u32',
                },
                'UnbondingPoolSlashed': {
                    'balance': 'u128',
                    'era': 'u32',
                    'pool_id': 'u32',
                },
                'Withdrawn': {
                    'balance': 'u128',
                    'member': 'AccountId',
                    'points': 'u128',
                    'pool_id': 'u32',
                },
            },
            'Offences': {'Offence': {'kind': '[u8; 16]', 'timeslot': 'Bytes'}},
            'ParaInclusion': {
                'CandidateBacked': ('scale_info::499', 'Bytes', 'u32', 'u32'),
                'CandidateIncluded': (
                    'scale_info::499',
                    'Bytes',
                    'u32',
                    'u32',
                ),
                'CandidateTimedOut': ('scale_info::499', 'Bytes', 'u32'),
                'UpwardMessagesReceived': {'count': 'u32', 'from': 'u32'},
            },
            'Paras': {
                'ActionQueued': ('u32', 'u32'),
                'CodeUpgradeScheduled': 'u32',
                'CurrentCodeUpdated': 'u32',
                'CurrentHeadUpdated': 'u32',
                'NewHeadNoted': 'u32',
                'PvfCheckAccepted': ('scale_info::12', 'u32'),
                'PvfCheckRejected': ('scale_info::12', 'u32'),
                'PvfCheckStarted': ('scale_info::12', 'u32'),
            },
            'ParasDisputes': {
                'DisputeConcluded': ('scale_info::12', 'scale_info::506'),
                'DisputeInitiated': ('scale_info::12', 'scale_info::505'),
                'Revert': 'u32',
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
                    'proxy_type': 'scale_info::216',
                },
                'ProxyExecuted': {'result': 'scale_info::476'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::216',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::216',
                    'pure': 'AccountId',
                    'who': 'AccountId',
                },
            },
            'Recovery': {
                'AccountRecovered': {
                    'lost_account': 'AccountId',
                    'rescuer_account': 'AccountId',
                },
                'RecoveryClosed': {
                    'lost_account': 'AccountId',
                    'rescuer_account': 'AccountId',
                },
                'RecoveryCreated': {'account': 'AccountId'},
                'RecoveryInitiated': {
                    'lost_account': 'AccountId',
                    'rescuer_account': 'AccountId',
                },
                'RecoveryRemoved': {'lost_account': 'AccountId'},
                'RecoveryVouched': {
                    'lost_account': 'AccountId',
                    'rescuer_account': 'AccountId',
                    'sender': 'AccountId',
                },
            },
            'Referenda': {
                'Approved': {'index': 'u32'},
                'Cancelled': {'index': 'u32', 'tally': 'scale_info::464'},
                'ConfirmAborted': {'index': 'u32'},
                'ConfirmStarted': {'index': 'u32'},
                'Confirmed': {'index': 'u32', 'tally': 'scale_info::464'},
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
                    'proposal': 'scale_info::81',
                    'tally': 'scale_info::464',
                    'track': 'u16',
                },
                'DepositSlashed': {'amount': 'u128', 'who': 'AccountId'},
                'Killed': {'index': 'u32', 'tally': 'scale_info::464'},
                'MetadataCleared': {'hash': 'scale_info::12', 'index': 'u32'},
                'MetadataSet': {'hash': 'scale_info::12', 'index': 'u32'},
                'Rejected': {'index': 'u32', 'tally': 'scale_info::464'},
                'SubmissionDepositRefunded': {
                    'amount': 'u128',
                    'index': 'u32',
                    'who': 'AccountId',
                },
                'Submitted': {
                    'index': 'u32',
                    'proposal': 'scale_info::81',
                    'track': 'u16',
                },
                'TimedOut': {'index': 'u32', 'tally': 'scale_info::464'},
            },
            'Registrar': {
                'Deregistered': {'para_id': 'u32'},
                'Registered': {'manager': 'AccountId', 'para_id': 'u32'},
                'Reserved': {'para_id': 'u32', 'who': 'AccountId'},
                'Swapped': {'other_id': 'u32', 'para_id': 'u32'},
            },
            'Scheduler': {
                'CallUnavailable': {
                    'id': (None, '[u8; 32]'),
                    'task': ('u32', 'u32'),
                },
                'Canceled': {'index': 'u32', 'when': 'u32'},
                'Dispatched': {
                    'id': (None, '[u8; 32]'),
                    'result': 'scale_info::476',
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
            'Slots': {
                'Leased': {
                    'extra_reserved': 'u128',
                    'leaser': 'AccountId',
                    'para_id': 'u32',
                    'period_begin': 'u32',
                    'period_count': 'u32',
                    'total_amount': 'u128',
                },
                'NewLeasePeriod': {'lease_period': 'u32'},
            },
            'Society': {
                'AutoUnbid': {'candidate': 'AccountId'},
                'Bid': {'candidate_id': 'AccountId', 'offer': 'u128'},
                'CandidateSuspended': {'candidate': 'AccountId'},
                'Challenged': {'member': 'AccountId'},
                'DefenderVote': {'vote': 'bool', 'voter': 'AccountId'},
                'Deposit': {'value': 'u128'},
                'Elevated': {'member': 'AccountId', 'rank': 'u32'},
                'Founded': {'founder': 'AccountId'},
                'Inducted': {'candidates': ['AccountId'], 'primary': 'AccountId'},
                'MemberSuspended': {'member': 'AccountId'},
                'NewParams': {'params': 'scale_info::479'},
                'SuspendedMemberJudgement': {
                    'judged': 'bool',
                    'who': 'AccountId',
                },
                'Unbid': {'candidate': 'AccountId'},
                'Unfounded': {'founder': 'AccountId'},
                'Unvouch': {'candidate': 'AccountId'},
                'Vote': {
                    'candidate': 'AccountId',
                    'vote': 'bool',
                    'voter': 'AccountId',
                },
                'Vouch': {
                    'candidate_id': 'AccountId',
                    'offer': 'u128',
                    'vouching': 'AccountId',
                },
            },
            'Staking': {
                'Bonded': {'amount': 'u128', 'stash': 'AccountId'},
                'Chilled': {'stash': 'AccountId'},
                'EraPaid': {
                    'era_index': 'u32',
                    'remainder': 'u128',
                    'validator_payout': 'u128',
                },
                'ForceEra': {'mode': 'scale_info::40'},
                'Kicked': {'nominator': 'AccountId', 'stash': 'AccountId'},
                'OldSlashingReportDiscarded': {'session_index': 'u32'},
                'PayoutStarted': {
                    'era_index': 'u32',
                    'validator_stash': 'AccountId',
                },
                'Rewarded': {
                    'amount': 'u128',
                    'dest': 'scale_info::35',
                    'stash': 'AccountId',
                },
                'SlashReported': {
                    'fraction': 'u32',
                    'slash_era': 'u32',
                    'validator': 'AccountId',
                },
                'Slashed': {'amount': 'u128', 'staker': 'AccountId'},
                'SnapshotTargetsSizeExceeded': {'size': 'u32'},
                'SnapshotVotersSizeExceeded': {'size': 'u32'},
                'StakersElected': None,
                'StakingElectionFailed': None,
                'Unbonded': {'amount': 'u128', 'stash': 'AccountId'},
                'ValidatorPrefsSet': {
                    'prefs': 'scale_info::37',
                    'stash': 'AccountId',
                },
                'Withdrawn': {'amount': 'u128', 'stash': 'AccountId'},
            },
            'StateTrieMigration': {
                'AutoMigrationFinished': None,
                'Halted': {'error': 'scale_info::513'},
                'Migrated': {
                    'child': 'u32',
                    'compute': 'scale_info::512',
                    'top': 'u32',
                },
                'Slashed': {'amount': 'u128', 'who': 'AccountId'},
            },
            'TransactionPayment': {
                'TransactionFeePaid': {
                    'actual_fee': 'u128',
                    'tip': 'u128',
                    'who': 'AccountId',
                },
            },
            'Treasury': {
                'AssetSpendApproved': {
                    'amount': 'u128',
                    'asset_kind': 'scale_info::59',
                    'beneficiary': 'scale_info::70',
                    'expire_at': 'u32',
                    'index': 'u32',
                    'valid_from': 'u32',
                },
                'AssetSpendVoided': {'index': 'u32'},
                'Awarded': {
                    'account': 'AccountId',
                    'award': 'u128',
                    'proposal_index': 'u32',
                },
                'Burnt': {'burnt_funds': 'u128'},
                'Deposit': {'value': 'u128'},
                'Paid': {'index': 'u32', 'payment_id': 'u64'},
                'PaymentFailed': {'index': 'u32', 'payment_id': 'u64'},
                'Proposed': {'proposal_index': 'u32'},
                'Rejected': {'proposal_index': 'u32', 'slashed': 'u128'},
                'Rollover': {'rollover_balance': 'u128'},
                'SpendApproved': {
                    'amount': 'u128',
                    'beneficiary': 'AccountId',
                    'proposal_index': 'u32',
                },
                'SpendProcessed': {'index': 'u32'},
                'Spending': {'budget_remaining': 'u128'},
                'UpdatedInactive': {
                    'deactivated': 'u128',
                    'reactivated': 'u128',
                },
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::25',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::476'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::25'},
            },
            'Vesting': {
                'VestingCompleted': {'account': 'AccountId'},
                'VestingUpdated': {'account': 'AccountId', 'unvested': 'u128'},
            },
            'VoterList': {
                'Rebagged': {'from': 'u64', 'to': 'u64', 'who': 'AccountId'},
                'ScoreUpdated': {'new_score': 'u64', 'who': 'AccountId'},
            },
            'Whitelist': {
                'CallWhitelisted': {'call_hash': 'scale_info::12'},
                'WhitelistedCallDispatched': {
                    'call_hash': 'scale_info::12',
                    'result': 'scale_info::470',
                },
                'WhitelistedCallRemoved': {'call_hash': 'scale_info::12'},
            },
            'XcmPallet': {
                'AssetsClaimed': {
                    'assets': 'scale_info::440',
                    'hash': 'scale_info::12',
                    'origin': 'scale_info::60',
                },
                'AssetsTrapped': {
                    'assets': 'scale_info::440',
                    'hash': 'scale_info::12',
                    'origin': 'scale_info::60',
                },
                'Attempted': {'outcome': 'scale_info::515'},
                'FeesPaid': {'fees': ['scale_info::421'], 'paying': 'scale_info::60'},
                'InvalidQuerier': {
                    'expected_querier': 'scale_info::60',
                    'maybe_actual_querier': (None, 'scale_info::60'),
                    'origin': 'scale_info::60',
                    'query_id': 'u64',
                },
                'InvalidQuerierVersion': {
                    'origin': 'scale_info::60',
                    'query_id': 'u64',
                },
                'InvalidResponder': {
                    'expected_location': (None, 'scale_info::60'),
                    'origin': 'scale_info::60',
                    'query_id': 'u64',
                },
                'InvalidResponderVersion': {
                    'origin': 'scale_info::60',
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
                    'location': 'scale_info::70',
                    'query_id': 'u64',
                },
                'NotifyTargetSendFail': {
                    'error': 'scale_info::427',
                    'location': 'scale_info::60',
                    'query_id': 'u64',
                },
                'ResponseReady': {
                    'query_id': 'u64',
                    'response': 'scale_info::424',
                },
                'ResponseTaken': {'query_id': 'u64'},
                'Sent': {
                    'destination': 'scale_info::60',
                    'message': ['scale_info::418'],
                    'message_id': '[u8; 32]',
                    'origin': 'scale_info::60',
                },
                'SupportedVersionChanged': {
                    'location': 'scale_info::60',
                    'version': 'u32',
                },
                'UnexpectedResponse': {
                    'origin': 'scale_info::60',
                    'query_id': 'u64',
                },
                'VersionChangeNotified': {
                    'cost': ['scale_info::421'],
                    'destination': 'scale_info::60',
                    'message_id': '[u8; 32]',
                    'result': 'u32',
                },
                'VersionNotifyRequested': {
                    'cost': ['scale_info::421'],
                    'destination': 'scale_info::60',
                    'message_id': '[u8; 32]',
                },
                'VersionNotifyStarted': {
                    'cost': ['scale_info::421'],
                    'destination': 'scale_info::60',
                    'message_id': '[u8; 32]',
                },
                'VersionNotifyUnrequested': {
                    'cost': ['scale_info::421'],
                    'destination': 'scale_info::60',
                    'message_id': '[u8; 32]',
                },
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
    'base_block': {'proof_size': 0, 'ref_time': 14278073000},
    'max_block': {
        'proof_size': 18446744073709551615,
        'ref_time': 2000000000000,
    },
    'per_class': {
        'mandatory': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 124706000},
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 124706000},
            'max_extrinsic': {
                'proof_size': 13650590614545068195,
                'ref_time': 1479875294000,
            },
            'max_total': {
                'proof_size': 13835058055282163711,
                'ref_time': 1500000000000,
            },
            'reserved': {'proof_size': 0, 'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 124706000},
            'max_extrinsic': {
                'proof_size': 18262276632972456099,
                'ref_time': 1979875294000,
            },
            'max_total': {
                'proof_size': 18446744073709551615,
                'ref_time': 2000000000000,
            },
            'reserved': {
                'proof_size': 4611686018427387904,
                'ref_time': 500000000000,
            },
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
2
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
        ('0x40fe3ad401f8959a', 6),
        ('0xd2bc9897eed08f15', 3),
        ('0xf78b278be53f454c', 2),
        ('0xaf2c0297a23e6d3d', 7),
        ('0x49eaaf1b548a0cb0', 3),
        ('0x91d5df18b0d2cf58', 2),
        ('0x2a5e924655399e60', 1),
        ('0xed99c5acb25eedf5', 3),
        ('0xcbca25e39f142387', 2),
        ('0x687ad44ad37f03c2', 1),
        ('0xab3c0572291feb8b', 1),
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 4),
        ('0xf3ff14d5ab527059', 3),
        ('0x17a6bc0d0062aeb3', 1),
        ('0x18ef58a3b67ba770', 1),
        ('0xfbc577b9d747efd6', 1),
    ],
    'authoring_version': 2,
    'impl_name': 'parity-kusama',
    'impl_version': 0,
    'spec_name': 'kusama',
    'spec_version': 1001002,
    'state_version': 1,
    'transaction_version': 25,
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