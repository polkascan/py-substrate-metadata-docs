
# System

---------
## Calls

---------
### apply_authorized_upgrade
See [`Pallet::apply_authorized_upgrade`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| code | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'apply_authorized_upgrade', {'code': 'Bytes'}
)
```

---------
### authorize_upgrade
See [`Pallet::authorize_upgrade`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| code_hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'authorize_upgrade', {'code_hash': 'scale_info::12'}
)
```

---------
### authorize_upgrade_without_checks
See [`Pallet::authorize_upgrade_without_checks`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| code_hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'authorize_upgrade_without_checks', {'code_hash': 'scale_info::12'}
)
```

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
### UpgradeAuthorized
An upgrade was authorized.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| code_hash | `T::Hash` | ```scale_info::12```
| check_version | `bool` | ```bool```

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
### AuthorizedUpgrade
 `Some` if a code upgrade has been authorized.

#### Python
```python
result = substrate.query(
    'System', 'AuthorizedUpgrade', []
)
```

#### Return value
```python
{'check_version': 'bool', 'code_hash': 'scale_info::12'}
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
            None: None,
            'AwesomeAvatars': {
                'AvatarLocked': {'avatar_id': 'scale_info::12'},
                'AvatarPriceSet': {
                    'avatar_id': 'scale_info::12',
                    'price': 'u128',
                },
                'AvatarPriceUnset': {'avatar_id': 'scale_info::12'},
                'AvatarTraded': {
                    'avatar_id': 'scale_info::12',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'AvatarTransferred': {
                    'avatar_id': 'scale_info::12',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'AvatarUnlocked': {'avatar_id': 'scale_info::12'},
                'AvatarsForged': {'avatar_ids': [('scale_info::12', 'u8')]},
                'AvatarsMinted': {'avatar_ids': ['scale_info::12']},
                'CollectionIdSet': {'collection_id': 'u32'},
                'FreeMintsSet': {'how_many': 'u16', 'target': 'AccountId'},
                'FreeMintsTransferred': {
                    'from': 'AccountId',
                    'how_many': 'u16',
                    'to': 'AccountId',
                },
                'OrganizerSet': {'organizer': 'AccountId'},
                'PreparedAvatar': {'avatar_id': 'scale_info::12'},
                'PreparedIpfsUrl': {'url': 'Bytes'},
                'SeasonFinished': 'u16',
                'SeasonStarted': 'u16',
                'ServiceAccountSet': {'service_account': 'AccountId'},
                'StorageTierUpgraded': {
                    'account': 'AccountId',
                    'season_id': 'u16',
                },
                'TreasurerSet': {'season_id': 'u16', 'treasurer': 'AccountId'},
                'TreasuryClaimed': {
                    'amount': 'u128',
                    'season_id': 'u16',
                    'treasurer': 'AccountId',
                },
                'UnpreparedAvatar': {'avatar_id': 'scale_info::12'},
                'UpdatedGlobalConfig': {
                    'forge': 'scale_info::155',
                    'mint': 'scale_info::154',
                    'nft_transfer': 'scale_info::158',
                    'trade': 'scale_info::157',
                    'transfer': 'scale_info::156',
                },
                'UpdatedSeason': {
                    'season': 'scale_info::141',
                    'season_id': 'u16',
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
                    'destination_status': 'scale_info::47',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Reserved': {'amount': 'u128', 'who': 'AccountId'},
                'Restored': {'amount': 'u128', 'who': 'AccountId'},
                'Slashed': {'amount': 'u128', 'who': 'AccountId'},
                'Suspended': {'amount': 'u128', 'who': 'AccountId'},
                'Thawed': {'amount': 'u128', 'who': 'AccountId'},
                'TotalIssuanceForced': {'new': 'u128', 'old': 'u128'},
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
                'CandidateAdded': {
                    'account_id': 'AccountId',
                    'deposit': 'u128',
                },
                'CandidateBondUpdated': {
                    'account_id': 'AccountId',
                    'deposit': 'u128',
                },
                'CandidateRemoved': {'account_id': 'AccountId'},
                'CandidateReplaced': {
                    'deposit': 'u128',
                    'new': 'AccountId',
                    'old': 'AccountId',
                },
                'InvalidInvulnerableSkipped': {'account_id': 'AccountId'},
                'InvulnerableAdded': {'account_id': 'AccountId'},
                'InvulnerableRemoved': {'account_id': 'AccountId'},
                'NewCandidacyBond': {'bond_amount': 'u128'},
                'NewDesiredCandidates': {'desired_candidates': 'u32'},
                'NewInvulnerables': {'invulnerables': ['AccountId']},
            },
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
                    'result': 'scale_info::35',
                },
                'MemberExecuted': {
                    'proposal_hash': 'scale_info::12',
                    'result': 'scale_info::35',
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
            'CumulusXcm': {
                'ExecutedDownward': ('[u8; 32]', 'scale_info::57'),
                'InvalidFormat': '[u8; 32]',
                'UnsupportedVersion': '[u8; 32]',
            },
            'Identity': {
                'AuthorityAdded': {'authority': 'AccountId'},
                'AuthorityRemoved': {'authority': 'AccountId'},
                'DanglingUsernameRemoved': {
                    'username': 'Bytes',
                    'who': 'AccountId',
                },
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
                'PreapprovalExpired': {'whose': 'AccountId'},
                'PrimaryUsernameSet': {
                    'username': 'Bytes',
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
                'UsernameQueued': {
                    'expiration': 'u32',
                    'username': 'Bytes',
                    'who': 'AccountId',
                },
                'UsernameSet': {'username': 'Bytes', 'who': 'AccountId'},
            },
            'MessageQueue': {
                'OverweightEnqueued': {
                    'id': '[u8; 32]',
                    'message_index': 'u32',
                    'origin': 'scale_info::132',
                    'page_index': 'u32',
                },
                'PageReaped': {'index': 'u32', 'origin': 'scale_info::132'},
                'Processed': {
                    'id': 'scale_info::12',
                    'origin': 'scale_info::132',
                    'success': 'bool',
                    'weight_used': 'scale_info::9',
                },
                'ProcessingFailed': {
                    'error': 'scale_info::134',
                    'id': 'scale_info::12',
                    'origin': 'scale_info::132',
                },
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::34',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::34',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::35',
                    'timepoint': 'scale_info::34',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'Nft': {
                'AllApprovalsCancelled': {
                    'collection': 'u32',
                    'item': 'scale_info::12',
                    'owner': 'AccountId',
                },
                'ApprovalCancelled': {
                    'collection': 'u32',
                    'delegate': 'AccountId',
                    'item': 'scale_info::12',
                    'owner': 'AccountId',
                },
                'AttributeCleared': {
                    'collection': 'u32',
                    'key': 'Bytes',
                    'maybe_item': (None, 'scale_info::12'),
                    'namespace': 'scale_info::169',
                },
                'AttributeSet': {
                    'collection': 'u32',
                    'key': 'Bytes',
                    'maybe_item': (None, 'scale_info::12'),
                    'namespace': 'scale_info::169',
                    'value': 'Bytes',
                },
                'Burned': {
                    'collection': 'u32',
                    'item': 'scale_info::12',
                    'owner': 'AccountId',
                },
                'CollectionConfigChanged': {'collection': 'u32'},
                'CollectionLocked': {'collection': 'u32'},
                'CollectionMaxSupplySet': {
                    'collection': 'u32',
                    'max_supply': 'u32',
                },
                'CollectionMetadataCleared': {'collection': 'u32'},
                'CollectionMetadataSet': {
                    'collection': 'u32',
                    'data': 'Bytes',
                },
                'CollectionMintSettingsUpdated': {'collection': 'u32'},
                'Created': {
                    'collection': 'u32',
                    'creator': 'AccountId',
                    'owner': 'AccountId',
                },
                'Destroyed': {'collection': 'u32'},
                'ForceCreated': {'collection': 'u32', 'owner': 'AccountId'},
                'Issued': {
                    'collection': 'u32',
                    'item': 'scale_info::12',
                    'owner': 'AccountId',
                },
                'ItemAttributesApprovalAdded': {
                    'collection': 'u32',
                    'delegate': 'AccountId',
                    'item': 'scale_info::12',
                },
                'ItemAttributesApprovalRemoved': {
                    'collection': 'u32',
                    'delegate': 'AccountId',
                    'item': 'scale_info::12',
                },
                'ItemBought': {
                    'buyer': 'AccountId',
                    'collection': 'u32',
                    'item': 'scale_info::12',
                    'price': 'u128',
                    'seller': 'AccountId',
                },
                'ItemMetadataCleared': {
                    'collection': 'u32',
                    'item': 'scale_info::12',
                },
                'ItemMetadataSet': {
                    'collection': 'u32',
                    'data': 'Bytes',
                    'item': 'scale_info::12',
                },
                'ItemPriceRemoved': {
                    'collection': 'u32',
                    'item': 'scale_info::12',
                },
                'ItemPriceSet': {
                    'collection': 'u32',
                    'item': 'scale_info::12',
                    'price': 'u128',
                    'whitelisted_buyer': (None, 'AccountId'),
                },
                'ItemPropertiesLocked': {
                    'collection': 'u32',
                    'item': 'scale_info::12',
                    'lock_attributes': 'bool',
                    'lock_metadata': 'bool',
                },
                'ItemTransferLocked': {
                    'collection': 'u32',
                    'item': 'scale_info::12',
                },
                'ItemTransferUnlocked': {
                    'collection': 'u32',
                    'item': 'scale_info::12',
                },
                'NextCollectionIdIncremented': {'next_id': (None, 'u32')},
                'OwnerChanged': {
                    'collection': 'u32',
                    'new_owner': 'AccountId',
                },
                'OwnershipAcceptanceChanged': {
                    'maybe_collection': (None, 'u32'),
                    'who': 'AccountId',
                },
                'PalletAttributeSet': {
                    'attribute': 'scale_info::173',
                    'collection': 'u32',
                    'item': (None, 'scale_info::12'),
                    'value': 'Bytes',
                },
                'PreSignedAttributesSet': {
                    'collection': 'u32',
                    'item': 'scale_info::12',
                    'namespace': 'scale_info::169',
                },
                'Redeposited': {
                    'collection': 'u32',
                    'successful_items': ['scale_info::12'],
                },
                'SwapCancelled': {
                    'deadline': 'u32',
                    'desired_collection': 'u32',
                    'desired_item': (None, 'scale_info::12'),
                    'offered_collection': 'u32',
                    'offered_item': 'scale_info::12',
                    'price': (None, 'scale_info::171'),
                },
                'SwapClaimed': {
                    'deadline': 'u32',
                    'price': (None, 'scale_info::171'),
                    'received_collection': 'u32',
                    'received_item': 'scale_info::12',
                    'received_item_owner': 'AccountId',
                    'sent_collection': 'u32',
                    'sent_item': 'scale_info::12',
                    'sent_item_owner': 'AccountId',
                },
                'SwapCreated': {
                    'deadline': 'u32',
                    'desired_collection': 'u32',
                    'desired_item': (None, 'scale_info::12'),
                    'offered_collection': 'u32',
                    'offered_item': 'scale_info::12',
                    'price': (None, 'scale_info::171'),
                },
                'TeamChanged': {
                    'admin': (None, 'AccountId'),
                    'collection': 'u32',
                    'freezer': (None, 'AccountId'),
                    'issuer': (None, 'AccountId'),
                },
                'TipSent': {
                    'amount': 'u128',
                    'collection': 'u32',
                    'item': 'scale_info::12',
                    'receiver': 'AccountId',
                    'sender': 'AccountId',
                },
                'TransferApproved': {
                    'collection': 'u32',
                    'deadline': (None, 'u32'),
                    'delegate': 'AccountId',
                    'item': 'scale_info::12',
                    'owner': 'AccountId',
                },
                'Transferred': {
                    'collection': 'u32',
                    'from': 'AccountId',
                    'item': 'scale_info::12',
                    'to': 'AccountId',
                },
            },
            'NftTransfer': {
                'ItemRestored': {
                    'collection_id': 'u32',
                    'item_id': 'scale_info::12',
                    'owner': 'AccountId',
                },
                'ItemStored': {
                    'collection_id': 'u32',
                    'item_id': 'scale_info::12',
                    'owner': 'AccountId',
                },
            },
            'ParachainSystem': {
                'DownwardMessagesProcessed': {
                    'dmq_head': 'scale_info::12',
                    'weight_used': 'scale_info::9',
                },
                'DownwardMessagesReceived': {'count': 'u32'},
                'UpwardMessageSent': {'message_hash': (None, '[u8; 32]')},
                'ValidationFunctionApplied': {'relay_chain_block_num': 'u32'},
                'ValidationFunctionDiscarded': None,
                'ValidationFunctionStored': None,
            },
            'PolkadotXcm': {
                'AssetsClaimed': {
                    'assets': 'scale_info::104',
                    'hash': 'scale_info::12',
                    'origin': 'scale_info::59',
                },
                'AssetsTrapped': {
                    'assets': 'scale_info::104',
                    'hash': 'scale_info::12',
                    'origin': 'scale_info::59',
                },
                'Attempted': {'outcome': 'scale_info::57'},
                'FeesPaid': {'fees': ['scale_info::81'], 'paying': 'scale_info::59'},
                'InvalidQuerier': {
                    'expected_querier': 'scale_info::59',
                    'maybe_actual_querier': (None, 'scale_info::59'),
                    'origin': 'scale_info::59',
                    'query_id': 'u64',
                },
                'InvalidQuerierVersion': {
                    'origin': 'scale_info::59',
                    'query_id': 'u64',
                },
                'InvalidResponder': {
                    'expected_location': (None, 'scale_info::59'),
                    'origin': 'scale_info::59',
                    'query_id': 'u64',
                },
                'InvalidResponderVersion': {
                    'origin': 'scale_info::59',
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
                    'location': 'scale_info::129',
                    'query_id': 'u64',
                },
                'NotifyTargetSendFail': {
                    'error': 'scale_info::58',
                    'location': 'scale_info::59',
                    'query_id': 'u64',
                },
                'ResponseReady': {
                    'query_id': 'u64',
                    'response': 'scale_info::87',
                },
                'ResponseTaken': {'query_id': 'u64'},
                'Sent': {
                    'destination': 'scale_info::59',
                    'message': ['scale_info::78'],
                    'message_id': '[u8; 32]',
                    'origin': 'scale_info::59',
                },
                'SupportedVersionChanged': {
                    'location': 'scale_info::59',
                    'version': 'u32',
                },
                'UnexpectedResponse': {
                    'origin': 'scale_info::59',
                    'query_id': 'u64',
                },
                'VersionChangeNotified': {
                    'cost': ['scale_info::81'],
                    'destination': 'scale_info::59',
                    'message_id': '[u8; 32]',
                    'result': 'u32',
                },
                'VersionMigrationFinished': {'version': 'u32'},
                'VersionNotifyRequested': {
                    'cost': ['scale_info::81'],
                    'destination': 'scale_info::59',
                    'message_id': '[u8; 32]',
                },
                'VersionNotifyStarted': {
                    'cost': ['scale_info::81'],
                    'destination': 'scale_info::59',
                    'message_id': '[u8; 32]',
                },
                'VersionNotifyUnrequested': {
                    'cost': ['scale_info::81'],
                    'destination': 'scale_info::59',
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
                    'proxy': 'AccountId',
                    'real': 'AccountId',
                },
                'ProxyAdded': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::41',
                },
                'ProxyExecuted': {'result': 'scale_info::35'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::41',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::41',
                    'pure': 'AccountId',
                    'who': 'AccountId',
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
                    'result': 'scale_info::35',
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
                'KeyChanged': {'new': 'AccountId', 'old': (None, 'AccountId')},
                'KeyRemoved': None,
                'Sudid': {'sudo_result': 'scale_info::35'},
                'SudoAsDone': {'sudo_result': 'scale_info::35'},
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
                'UpgradeAuthorized': {
                    'check_version': 'bool',
                    'code_hash': 'scale_info::12',
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
                'AssetSpendApproved': {
                    'amount': 'u128',
                    'asset_kind': (),
                    'beneficiary': 'AccountId',
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
                'Paid': {'index': 'u32', 'payment_id': ()},
                'PaymentFailed': {'index': 'u32', 'payment_id': ()},
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
                'DispatchedAs': {'result': 'scale_info::35'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::25'},
            },
            'Vesting': {
                'Claimed': {'amount': 'u128', 'who': 'AccountId'},
                'VestingScheduleAdded': {
                    'from': 'AccountId',
                    'to': 'AccountId',
                    'vesting_schedule': 'scale_info::50',
                },
                'VestingSchedulesUpdated': {'who': 'AccountId'},
            },
            'XcmpQueue': {'XcmpMessageSent': {'message_hash': '[u8; 32]'}},
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
    'base_block': {'proof_size': 0, 'ref_time': 5000000000},
    'max_block': {'proof_size': 5242880, 'ref_time': 500000000000},
    'per_class': {
        'mandatory': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 125000000},
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 125000000},
            'max_extrinsic': {'proof_size': 3670016, 'ref_time': 349875000000},
            'max_total': {'proof_size': 3932160, 'ref_time': 375000000000},
            'reserved': {'proof_size': 0, 'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 125000000},
            'max_extrinsic': {'proof_size': 4980736, 'ref_time': 474875000000},
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
1337
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
        ('0xd7bdd8a272ca0d65', 1),
        ('0xdf6acb689907609b', 4),
        ('0x37e397fc7c91f5e4', 2),
        ('0x40fe3ad401f8959a', 6),
        ('0xd2bc9897eed08f15', 3),
        ('0xf78b278be53f454c', 2),
        ('0xab3c0572291feb8b', 1),
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 4),
        ('0xea93e3f16f3d6962', 2),
    ],
    'authoring_version': 1,
    'impl_name': 'bajun',
    'impl_version': 0,
    'spec_name': 'bajun',
    'spec_version': 201,
    'state_version': 1,
    'transaction_version': 1,
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
### NothingAuthorized
No upgrade authorized.

---------
### SpecVersionNeedsToIncrease
The specification version is not allowed to decrease between the current runtime
and the new runtime.

---------
### Unauthorized
The submitted code is not authorized.

---------