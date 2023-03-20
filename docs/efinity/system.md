
# System

---------
## Calls

---------
### fill_block
A dispatch that will fill the block weight up to the given ratio.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ratio | `Perbill` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'fill_block', {'ratio': 'u32'}
)
```

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

\# &lt;weight&gt;
- `O(1)`
\# &lt;/weight&gt;
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

\# &lt;weight&gt;
- `O(C + S)` where `C` length of `code` and `S` complexity of `can_set_code`
- 1 call to `can_set_code`: `O(S)` (calls `sp_io::misc::runtime_version` which is
  expensive).
- 1 storage write (codec `O(C)`).
- 1 digest item.
- 1 event.
The weight of this function is dependent on the runtime, but generally this is very
expensive. We will treat this as a full block.
\# &lt;/weight&gt;
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

\# &lt;weight&gt;
- `O(C)` where `C` length of `code`
- 1 storage write (codec `O(C)`).
- 1 digest item.
- 1 event.
The weight of this function is dependent on the runtime. We will treat this as a full
block. \# &lt;/weight&gt;
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
                    'destination_status': 'scale_info::40',
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
            'Bounties': {
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
            },
            'Claims': {
                'Claimed': {
                    'amount': 'u128',
                    'ethereum_address': '[u8; 20]',
                    'who': 'AccountId',
                },
            },
            'CollatorStaking': {
                'CandidateJoined': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'rewards_cut': 'u32',
                },
                'CandidateRemoved': {'account_id': 'AccountId'},
                'CollatorSelected': {'account_id': 'AccountId'},
                'NewInvulnerables': {'new': ['AccountId']},
                'Nominated': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'collator_id': 'AccountId',
                },
                'NominationRemoved': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'collator_id': 'AccountId',
                },
                'RoundFinalized': {'number': 'u32'},
            },
            'CommunityPool': {
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
                    'result': 'scale_info::31',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::31',
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
            'CumulusXcm': {
                'ExecutedDownward': ('[u8; 8]', 'scale_info::65'),
                'InvalidFormat': '[u8; 8]',
                'UnsupportedVersion': '[u8; 8]',
            },
            'Democracy': {
                'Blacklisted': {'proposal_hash': '[u8; 32]'},
                'Cancelled': {'ref_index': 'u32'},
                'Delegated': {'target': 'AccountId', 'who': 'AccountId'},
                'ExternalTabled': None,
                'NotPassed': {'ref_index': 'u32'},
                'Passed': {'ref_index': 'u32'},
                'ProposalCanceled': {'prop_index': 'u32'},
                'Proposed': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Seconded': {'prop_index': 'u32', 'seconder': 'AccountId'},
                'Started': {'ref_index': 'u32', 'threshold': 'scale_info::46'},
                'Tabled': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Undelegated': {'account': 'AccountId'},
                'Vetoed': {
                    'proposal_hash': '[u8; 32]',
                    'until': 'u32',
                    'who': 'AccountId',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::47',
                    'voter': 'AccountId',
                },
            },
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::65',
                },
                'InvalidFormat': {'message_id': '[u8; 32]'},
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
            'EfinityUtility': {
                'BatchDispatched': None,
                'BatchFailed': {'error': 'scale_info::24', 'index': 'u32'},
                'BatchPartiallyDispatched': [('u32', 'scale_info::24')],
            },
            'EfinityXcm': {
                'MinimumWeightUpdated': {
                    'fee': 'u128',
                    'minimum_weight': 'scale_info::8',
                },
            },
            'ExtrinsicPause': {
                'ExtrinsicPaused': {
                    'extrinsic_name': 'Bytes',
                    'pallet_name': 'Bytes',
                },
                'ExtrinsicResumed': {
                    'extrinsic_name': 'Bytes',
                    'pallet_name': 'Bytes',
                },
                'PalletPaused': {'pallet_name': 'Bytes'},
                'PalletResumed': {'pallet_name': 'Bytes'},
            },
            'FuelTanks': {
                'AccountAdded': {
                    'tank_deposit': 'u128',
                    'tank_id': 'AccountId',
                    'user_deposit': 'u128',
                    'user_id': 'AccountId',
                },
                'AccountRemoved': {
                    'tank_id': 'AccountId',
                    'user_id': 'AccountId',
                },
                'AccountRuleDataRemoved': {
                    'rule_kind': 'scale_info::204',
                    'rule_set_id': 'u32',
                    'tank_id': 'AccountId',
                    'user_id': 'AccountId',
                },
                'CallDispatched': {
                    'caller': 'AccountId',
                    'tank_id': 'AccountId',
                },
                'DispatchFailed': {
                    'caller': 'AccountId',
                    'error': 'scale_info::24',
                    'tank_id': 'AccountId',
                },
                'FreezeStateMutated': {
                    'is_frozen': 'bool',
                    'rule_set_id': (None, 'u32'),
                    'tank_id': 'AccountId',
                },
                'FuelTankCreated': {
                    'name': 'Bytes',
                    'owner': 'AccountId',
                    'tank_id': 'AccountId',
                },
                'FuelTankDestroyed': {'tank_id': 'AccountId'},
                'FuelTankMutated': {
                    'mutation': 'scale_info::189',
                    'tank_id': 'AccountId',
                },
                'MutateFreezeStateScheduled': {
                    'is_frozen': 'bool',
                    'rule_set_id': (None, 'u32'),
                    'tank_id': 'AccountId',
                },
                'RuleSetInserted': {
                    'rule_set_id': 'u32',
                    'tank_id': 'AccountId',
                },
                'RuleSetRemoved': {
                    'rule_set_id': 'u32',
                    'tank_id': 'AccountId',
                },
                'ScheduleMutateFreezeStateFailed': {
                    'error': 'scale_info::24',
                    'is_frozen': 'bool',
                    'rule_set_id': (None, 'u32'),
                    'tank_id': 'AccountId',
                },
            },
            'Marketplace': {
                'AuctionFinalized': {
                    'listing_id': '[u8; 32]',
                    'protocol_fee': 'u128',
                    'royalty': 'u128',
                    'winning_bid': (None, 'scale_info::214'),
                },
                'BidPlaced': {
                    'bid': 'scale_info::214',
                    'listing_id': '[u8; 32]',
                },
                'ListingCancelled': {'listing_id': '[u8; 32]'},
                'ListingCreated': {
                    'listing': 'scale_info::206',
                    'listing_id': '[u8; 32]',
                },
                'ListingFilled': {
                    'amount_filled': 'u128',
                    'amount_remaining': 'u128',
                    'buyer': 'AccountId',
                    'listing_id': '[u8; 32]',
                    'protocol_fee': 'u128',
                    'royalty': 'u128',
                },
                'ProtocolFeeSet': {'protocol_fee': 'u32'},
            },
            'MultiTokens': {
                'Approved': {
                    'amount': (None, 'u128'),
                    'collection_id': 'u128',
                    'expiration': (None, 'u32'),
                    'operator': 'AccountId',
                    'owner': 'AccountId',
                    'token_id': (None, 'u128'),
                },
                'AttributeRemoved': {
                    'collection_id': 'u128',
                    'key': 'Bytes',
                    'token_id': (None, 'u128'),
                },
                'AttributeSet': {
                    'collection_id': 'u128',
                    'key': 'Bytes',
                    'token_id': (None, 'u128'),
                    'value': 'Bytes',
                },
                'BalanceSet': {
                    'account_id': 'AccountId',
                    'balance': 'u128',
                    'collection_id': 'u128',
                    'reserved_balance': 'u128',
                    'token_id': 'u128',
                },
                'Burned': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'collection_id': 'u128',
                    'token_id': 'u128',
                },
                'CollectionAccountCreated': {
                    'account_id': 'AccountId',
                    'collection_id': 'u128',
                },
                'CollectionAccountDestroyed': {
                    'account_id': 'AccountId',
                    'collection_id': 'u128',
                },
                'CollectionAccountUpdated': {
                    'account_id': 'AccountId',
                    'collection_id': 'u128',
                    'value': (None, 'scale_info::159'),
                },
                'CollectionCreated': {
                    'collection_id': 'u128',
                    'owner': 'AccountId',
                },
                'CollectionDestroyed': {
                    'caller': 'AccountId',
                    'collection_id': 'u128',
                },
                'CollectionMutated': {
                    'collection_id': 'u128',
                    'mutation': 'scale_info::111',
                },
                'CollectionUpdated': {
                    'collection_id': 'u128',
                    'value': (None, 'scale_info::142'),
                },
                'Deposit': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'collection_id': 'u128',
                    'token_id': 'u128',
                },
                'Frozen': {
                    'collection_id': 'u128',
                    'freeze_type': 'scale_info::135',
                },
                'MigrationStatusUpdated': {'stage': 'scale_info::179'},
                'Minted': {
                    'amount': 'u128',
                    'collection_id': 'u128',
                    'issuer': 'scale_info::120',
                    'recipient': 'AccountId',
                    'token_id': 'u128',
                },
                'MovedReserves': {
                    'amount': 'u128',
                    'collection_id': 'u128',
                    'destination': 'AccountId',
                    'reserve_id': (None, '[u8; 8]'),
                    'source': 'AccountId',
                    'token_id': 'u128',
                },
                'NextCollectionIdUpdated': {'collection_id': 'u128'},
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'collection_id': 'u128',
                    'destination': 'AccountId',
                    'reserve_id': (None, '[u8; 8]'),
                    'source': 'AccountId',
                    'token_id': 'u128',
                },
                'Reserved': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'collection_id': 'u128',
                    'reserve_id': (None, '[u8; 8]'),
                    'token_id': 'u128',
                },
                'Slashed': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'collection_id': 'u128',
                    'token_id': 'u128',
                },
                'Thawed': {
                    'collection_id': 'u128',
                    'freeze_type': 'scale_info::135',
                },
                'TokenAccountCreated': {
                    'account_id': 'AccountId',
                    'balance': 'u128',
                    'collection_id': 'u128',
                    'token_id': 'u128',
                },
                'TokenAccountDestroyed': {
                    'account_id': 'AccountId',
                    'collection_id': 'u128',
                    'token_id': 'u128',
                },
                'TokenAccountUpdated': {
                    'account_id': 'AccountId',
                    'collection_id': 'u128',
                    'token_id': 'u128',
                    'value': (None, 'scale_info::166'),
                },
                'TokenCreated': {
                    'collection_id': 'u128',
                    'initial_supply': 'u128',
                    'issuer': 'scale_info::120',
                    'token_id': 'u128',
                },
                'TokenDestroyed': {
                    'caller': 'AccountId',
                    'collection_id': 'u128',
                    'token_id': 'u128',
                },
                'TokenMutated': {
                    'collection_id': 'u128',
                    'mutation': 'scale_info::121',
                    'token_id': 'u128',
                },
                'TokenUpdated': {
                    'collection_id': 'u128',
                    'token_id': 'u128',
                    'value': (None, 'scale_info::155'),
                },
                'Transferred': {
                    'amount': 'u128',
                    'collection_id': 'u128',
                    'from': 'AccountId',
                    'operator': 'AccountId',
                    'to': 'AccountId',
                    'token_id': 'u128',
                },
                'Unapproved': {
                    'collection_id': 'u128',
                    'operator': 'AccountId',
                    'owner': 'AccountId',
                    'token_id': (None, 'u128'),
                },
                'Unreserved': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'collection_id': 'u128',
                    'reserve_id': (None, '[u8; 8]'),
                    'token_id': 'u128',
                },
                'Withdraw': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'collection_id': 'u128',
                    'token_id': 'u128',
                },
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::55',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::55',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::31',
                    'timepoint': 'scale_info::55',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'OrmlXcm': {
                'Sent': {'message': ['scale_info::77'], 'to': 'scale_info::66'},
            },
            'ParachainSystem': {
                'DownwardMessagesProcessed': {
                    'dmq_head': '[u8; 32]',
                    'weight_used': 'scale_info::8',
                },
                'DownwardMessagesReceived': {'count': 'u32'},
                'UpgradeAuthorized': {'code_hash': '[u8; 32]'},
                'ValidationFunctionApplied': {'relay_chain_block_num': 'u32'},
                'ValidationFunctionDiscarded': None,
                'ValidationFunctionStored': None,
            },
            'PolkadotXcm': {
                'AssetsClaimed': (
                    '[u8; 32]',
                    'scale_info::66',
                    'scale_info::96',
                ),
                'AssetsTrapped': (
                    '[u8; 32]',
                    'scale_info::66',
                    'scale_info::96',
                ),
                'Attempted': {
                    'Complete': 'u64',
                    'Error': 'scale_info::62',
                    'Incomplete': ('u64', 'scale_info::62'),
                },
                'InvalidResponder': (
                    'scale_info::66',
                    'u64',
                    (None, 'scale_info::66'),
                ),
                'InvalidResponderVersion': ('scale_info::66', 'u64'),
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
                'NotifyTargetMigrationFail': ('scale_info::101', 'u64'),
                'NotifyTargetSendFail': (
                    'scale_info::66',
                    'u64',
                    'scale_info::62',
                ),
                'ResponseReady': ('u64', 'scale_info::86'),
                'ResponseTaken': 'u64',
                'Sent': (
                    'scale_info::66',
                    'scale_info::66',
                    ['scale_info::77'],
                ),
                'SupportedVersionChanged': ('scale_info::66', 'u32'),
                'UnexpectedResponse': ('scale_info::66', 'u64'),
                'VersionChangeNotified': ('scale_info::66', 'u32'),
            },
            'Preimage': {
                'Cleared': {'hash': '[u8; 32]'},
                'Noted': {'hash': '[u8; 32]'},
                'Requested': {'hash': '[u8; 32]'},
            },
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
                    'dispatch_error': 'scale_info::24',
                    'dispatch_info': 'scale_info::21',
                },
                'ExtrinsicSuccess': {'dispatch_info': 'scale_info::21'},
                'KilledAccount': {'account': 'AccountId'},
                'NewAccount': {'account': 'AccountId'},
                'Remarked': {'hash': '[u8; 32]', 'sender': 'AccountId'},
            },
            'XTokens': {
                'TransferredMultiAssets': {
                    'assets': ['scale_info::80'],
                    'dest': 'scale_info::66',
                    'fee': 'scale_info::80',
                    'sender': 'AccountId',
                },
            },
            None: None,
            'Pools': {
                'PoolsMutated': {
                    'collator': 'scale_info::184',
                    'community': 'scale_info::184',
                    'fuel_tanks': 'scale_info::184',
                    'price_discovery': 'scale_info::184',
                },
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
                    'result': 'scale_info::31',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::31',
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
                    'who': 'AccountId',
                },
            },
            'UnknownTokens': {
                'Deposited': {
                    'asset': 'scale_info::80',
                    'who': 'scale_info::66',
                },
                'Withdrawn': {
                    'asset': 'scale_info::80',
                    'who': 'scale_info::66',
                },
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::24',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::31'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::24'},
            },
            'Vesting': {
                'Claimed': {'amount': 'u128', 'who': 'AccountId'},
                'VestingScheduleAdded': {
                    'from': 'AccountId',
                    'to': 'AccountId',
                    'vesting_schedule': 'scale_info::43',
                },
                'VestingSchedulesUpdated': {'who': 'AccountId'},
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': (None, '[u8; 32]')},
                'BadVersion': {'message_hash': (None, '[u8; 32]')},
                'Fail': {
                    'error': 'scale_info::62',
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
                'UpwardMessageSent': {'message_hash': (None, '[u8; 32]')},
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
    'base_block': {'proof_size': 0, 'ref_time': 358523000},
    'max_block': {
        'proof_size': 18446744073709551615,
        'ref_time': 2000000000000,
    },
    'per_class': {
        'mandatory': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 98974000},
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 98974000},
            'max_extrinsic': {
                'proof_size': 11990383647911208550,
                'ref_time': 1299901026000,
            },
            'max_total': {
                'proof_size': 13835058055282163711,
                'ref_time': 1500000000000,
            },
            'reserved': {'proof_size': 0, 'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 98974000},
            'max_extrinsic': {
                'proof_size': 16602069666338596454,
                'ref_time': 1799901026000,
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
1110
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
        ('0x37e397fc7c91f5e4', 1),
        ('0x40fe3ad401f8959a', 6),
        ('0xd2bc9897eed08f15', 3),
        ('0xf78b278be53f454c', 2),
        ('0xab3c0572291feb8b', 1),
        ('0xdd718d5cc53262d4', 1),
        ('0xea93e3f16f3d6962', 2),
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 2),
        ('0xf3ff14d5ab527059', 2),
    ],
    'authoring_version': 0,
    'impl_name': 'efinity',
    'impl_version': 0,
    'spec_name': 'efinity',
    'spec_version': 3012,
    'state_version': 0,
    'transaction_version': 7,
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