
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
            'AssetRegistry': {
                'AssetRegistered': {
                    'asset_id': 'scale_info::129',
                    'metadata': 'scale_info::130',
                },
                'AssetUpdated': {
                    'asset_id': 'scale_info::129',
                    'metadata': 'scale_info::130',
                },
                'CurrencyIdRegistered': {
                    'currency_id': 'scale_info::113',
                    'metadata': 'scale_info::130',
                },
                'MultiLocationSet': {
                    'currency_id': 'scale_info::113',
                    'location': 'scale_info::57',
                    'weight': 'u128',
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
                    'destination_status': 'scale_info::32',
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
            'CallSwitchgear': {
                'TransactionSwitchedOn': ('Bytes', 'Bytes'),
                'TransactionSwitchedoff': ('Bytes', 'Bytes'),
                'TransferAccountDisabled': {
                    'ForeignAsset': 'u32',
                    'LPToken': (
                        'scale_info::114',
                        'u8',
                        'scale_info::114',
                        'u8',
                    ),
                    'Native': 'scale_info::114',
                    'Stable': 'scale_info::114',
                    'StableLpToken': 'u32',
                    'Token': 'scale_info::114',
                    'Token2': 'u8',
                    'VSBond': ('scale_info::114', 'u32', 'u32', 'u32'),
                    'VSBond2': ('u8', 'u32', 'u32', 'u32'),
                    'VSToken': 'scale_info::114',
                    'VSToken2': 'u8',
                    'VToken': 'scale_info::114',
                    'VToken2': 'u8',
                },
                'TransferAccountEnabled': {
                    'ForeignAsset': 'u32',
                    'LPToken': (
                        'scale_info::114',
                        'u8',
                        'scale_info::114',
                        'u8',
                    ),
                    'Native': 'scale_info::114',
                    'Stable': 'scale_info::114',
                    'StableLpToken': 'u32',
                    'Token': 'scale_info::114',
                    'Token2': 'u8',
                    'VSBond': ('scale_info::114', 'u32', 'u32', 'u32'),
                    'VSBond2': ('u8', 'u32', 'u32', 'u32'),
                    'VSToken': 'scale_info::114',
                    'VSToken2': 'u8',
                    'VToken': 'scale_info::114',
                    'VToken2': 'u8',
                },
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
                    'result': 'scale_info::43',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::43',
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
            'CumulusXcm': {
                'ExecutedDownward': ('[u8; 8]', 'scale_info::56'),
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
                'Started': {'ref_index': 'u32', 'threshold': 'scale_info::38'},
                'Tabled': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Undelegated': {'account': 'AccountId'},
                'Vetoed': {
                    'proposal_hash': '[u8; 32]',
                    'until': 'u32',
                    'who': 'AccountId',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::39',
                    'voter': 'AccountId',
                },
            },
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::56',
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
            'Farming': {
                'AllForceGaugeClaimed': {'gid': 'u32'},
                'AllRetired': {'pid': 'u32'},
                'Charged': {
                    'pid': 'u32',
                    'rewards': [('scale_info::113', 'u128')],
                    'who': 'AccountId',
                },
                'Claimed': {'pid': 'u32', 'who': 'AccountId'},
                'Deposited': {
                    'add_value': 'u128',
                    'gauge_info': (None, ('u128', 'u32')),
                    'pid': 'u32',
                    'who': 'AccountId',
                },
                'FarmingPoolClosed': {'pid': 'u32'},
                'FarmingPoolCreated': {'pid': 'u32'},
                'FarmingPoolEdited': {'pid': 'u32'},
                'FarmingPoolKilled': {'pid': 'u32'},
                'FarmingPoolReset': {'pid': 'u32'},
                'GaugeWithdrawn': {'gid': 'u32', 'who': 'AccountId'},
                'PartiallyForceGaugeClaimed': {'gid': 'u32'},
                'PartiallyRetired': {'pid': 'u32'},
                'RetireLimitSet': {'limit': 'u32'},
                'WithdrawClaimed': {'pid': 'u32', 'who': 'AccountId'},
                'Withdrawn': {
                    'pid': 'u32',
                    'remove_value': (None, 'u128'),
                    'who': 'AccountId',
                },
            },
            'FeeShare': {
                'Created': {'info': 'scale_info::196'},
                'Deleted': {'distribution_id': 'u32'},
                'Edited': {'info': 'scale_info::196'},
                'EraLengthSet': {'era_length': 'u32', 'next_era': 'u32'},
                'ExecuteFailed': {
                    'distribution_id': 'u32',
                    'info': 'scale_info::196',
                    'next_era': 'u32',
                },
                'Executed': {'distribution_id': 'u32'},
            },
            'FlexibleFee': {
                'ExtraFeeDeducted': (
                    'scale_info::125',
                    'scale_info::113',
                    'u128',
                ),
                'FixedRateFeeExchanged': ('scale_info::113', 'u128'),
                'FlexibleFeeExchanged': ('scale_info::113', 'u128'),
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
            'Indices': {
                'IndexAssigned': {'index': 'u32', 'who': 'AccountId'},
                'IndexFreed': {'index': 'u32'},
                'IndexFrozen': {'index': 'u32', 'who': 'AccountId'},
            },
            'MerkleDistributor': {
                'AddToWhiteList': 'AccountId',
                'Claim': ('u32', 'AccountId', 'u128'),
                'Create': ('u32', '[u8; 32]', 'u128'),
                'RemoveFromWhiteList': 'AccountId',
                'Withdraw': ('u32', 'AccountId', 'u128'),
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::104',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::104',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::43',
                    'timepoint': 'scale_info::104',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'OrmlXcm': {
                'Sent': {'message': ['scale_info::69'], 'to': 'scale_info::57'},
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
            'PhragmenElection': {
                'CandidateSlashed': {
                    'amount': 'u128',
                    'candidate': 'AccountId',
                },
                'ElectionError': None,
                'EmptyTerm': None,
                'MemberKicked': {'member': 'AccountId'},
                'NewTerm': {'new_members': [('AccountId', 'u128')]},
                'Renounced': {'candidate': 'AccountId'},
                'SeatHolderSlashed': {
                    'amount': 'u128',
                    'seat_holder': 'AccountId',
                },
            },
            'PolkadotXcm': {
                'AssetsClaimed': (
                    '[u8; 32]',
                    'scale_info::57',
                    'scale_info::88',
                ),
                'AssetsTrapped': (
                    '[u8; 32]',
                    'scale_info::57',
                    'scale_info::88',
                ),
                'Attempted': {
                    'Complete': 'u64',
                    'Error': 'scale_info::53',
                    'Incomplete': ('u64', 'scale_info::53'),
                },
                'InvalidResponder': (
                    'scale_info::57',
                    'u64',
                    (None, 'scale_info::57'),
                ),
                'InvalidResponderVersion': ('scale_info::57', 'u64'),
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
                'NotifyTargetMigrationFail': ('scale_info::93', 'u64'),
                'NotifyTargetSendFail': (
                    'scale_info::57',
                    'u64',
                    'scale_info::53',
                ),
                'ResponseReady': ('u64', 'scale_info::78'),
                'ResponseTaken': 'u64',
                'Sent': (
                    'scale_info::57',
                    'scale_info::57',
                    ['scale_info::69'],
                ),
                'SupportedVersionChanged': ('scale_info::57', 'u32'),
                'UnexpectedResponse': ('scale_info::57', 'u64'),
                'VersionChangeNotified': ('scale_info::57', 'u32'),
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
                    'proxy_type': 'scale_info::101',
                },
                'ProxyExecuted': {'result': 'scale_info::43'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::101',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::101',
                    'pure': 'AccountId',
                    'who': 'AccountId',
                },
            },
            'Salp': {
                'AllRefunded': 'u32',
                'AllUnlocked': 'u32',
                'Buyback': 'u128',
                'Continued': ('u32', 'u32', 'u32'),
                'ContributeFailed': ('AccountId', 'u32', 'u128', '[u8; 32]'),
                'Contributed': ('AccountId', 'u32', 'u128', '[u8; 32]'),
                'Contributing': ('AccountId', 'u32', 'u128', '[u8; 32]'),
                'Created': 'u32',
                'Dissolved': 'u32',
                'Edited': 'u32',
                'End': 'u32',
                'Failed': 'u32',
                'Redeemed': ('AccountId', 'u32', 'u32', 'u32', 'u128'),
                'Refunded': ('AccountId', 'u32', 'u32', 'u32', 'u128'),
                'RefundedDissolved': ('u32', 'u32', 'u32'),
                'Retired': 'u32',
                'Success': 'u32',
                'Unlocked': ('AccountId', 'u32', 'u128'),
                'VstokenUnlocked': 'AccountId',
                'Withdrew': ('u32', 'u128'),
            },
            'Scheduler': {
                'CallUnavailable': {
                    'id': (None, '[u8; 32]'),
                    'task': ('u32', 'u32'),
                },
                'Canceled': {'index': 'u32', 'when': 'u32'},
                'Dispatched': {
                    'id': (None, '[u8; 32]'),
                    'result': 'scale_info::43',
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
            'Slp': {
                'Chill': {
                    'currency_id': 'scale_info::113',
                    'delegator_id': 'scale_info::57',
                    'query_id': 'u64',
                    'query_id_hash': '[u8; 32]',
                },
                'CurrencyDelaysSet': {
                    'currency_id': 'scale_info::113',
                    'delays': (None, 'scale_info::175'),
                },
                'CurrencyTuneExchangeRateLimitSet': {
                    'currency_id': 'scale_info::113',
                    'tune_exchange_rate_limit': (None, ('u32', 'u32')),
                },
                'Delegated': {
                    'currency_id': 'scale_info::113',
                    'delegator_id': 'scale_info::57',
                    'query_id': 'u64',
                    'query_id_hash': '[u8; 32]',
                    'targets': (None, ['scale_info::57']),
                },
                'DelegatorAdded': {
                    'currency_id': 'scale_info::113',
                    'delegator_id': 'scale_info::57',
                    'index': 'u16',
                },
                'DelegatorBondExtra': {
                    'currency_id': 'scale_info::113',
                    'delegator_id': 'scale_info::57',
                    'extra_bonded_amount': 'u128',
                    'query_id': 'u64',
                    'query_id_hash': '[u8; 32]',
                    'validator': (None, 'scale_info::57'),
                },
                'DelegatorBonded': {
                    'bonded_amount': 'u128',
                    'currency_id': 'scale_info::113',
                    'delegator_id': 'scale_info::57',
                    'query_id': 'u64',
                    'query_id_hash': '[u8; 32]',
                    'validator': (None, 'scale_info::57'),
                },
                'DelegatorInitialized': {
                    'currency_id': 'scale_info::113',
                    'delegator_id': 'scale_info::57',
                },
                'DelegatorLedgerQueryResponseConfirmed': {
                    'entry': 'scale_info::165',
                    'query_id': 'u64',
                },
                'DelegatorLedgerQueryResponseFailSuccessfully': {
                    'query_id': 'u64',
                },
                'DelegatorLedgerSet': {
                    'currency_id': 'scale_info::113',
                    'delegator': 'scale_info::57',
                    'ledger': (None, 'scale_info::149'),
                },
                'DelegatorRebond': {
                    'currency_id': 'scale_info::113',
                    'delegator_id': 'scale_info::57',
                    'query_id': 'u64',
                    'query_id_hash': '[u8; 32]',
                    'rebond_amount': (None, 'u128'),
                    'validator': (None, 'scale_info::57'),
                },
                'DelegatorRemoved': {
                    'currency_id': 'scale_info::113',
                    'delegator_id': 'scale_info::57',
                },
                'DelegatorUnbond': {
                    'currency_id': 'scale_info::113',
                    'delegator_id': 'scale_info::57',
                    'query_id': 'u64',
                    'query_id_hash': '[u8; 32]',
                    'unbond_amount': 'u128',
                    'validator': (None, 'scale_info::57'),
                },
                'DelegatorUnbondAll': {
                    'currency_id': 'scale_info::113',
                    'delegator_id': 'scale_info::57',
                    'query_id': 'u64',
                    'query_id_hash': '[u8; 32]',
                },
                'FeeSourceSet': {
                    'currency_id': 'scale_info::113',
                    'who_and_fee': (None, ('scale_info::57', 'u128')),
                },
                'FeeSupplemented': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::113',
                    'from': 'scale_info::57',
                    'to': 'scale_info::57',
                },
                'FundMoveFromExitToEntrance': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::113',
                },
                'HostingFeeCharged': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::113',
                },
                'HostingFeesSet': {
                    'currency_id': 'scale_info::113',
                    'fees': (None, ('u32', 'scale_info::57')),
                },
                'Liquidize': {
                    'currency_id': 'scale_info::113',
                    'delegator_id': 'scale_info::57',
                    'query_id': 'u64',
                    'query_id_hash': '[u8; 32]',
                    'time_unit': (None, 'scale_info::132'),
                },
                'MinimumsMaximumsSet': {
                    'currency_id': 'scale_info::113',
                    'minimums_and_maximums': (None, 'scale_info::173'),
                },
                'OngoingTimeUnitUpdateIntervalSet': {
                    'currency_id': 'scale_info::113',
                    'interval': (None, 'u32'),
                },
                'OperateOriginSet': {
                    'currency_id': 'scale_info::113',
                    'operator': (None, 'AccountId'),
                },
                'Payout': {
                    'currency_id': 'scale_info::113',
                    'time_unit': (None, 'scale_info::132'),
                    'validator': 'scale_info::57',
                },
                'PoolTokenDecreased': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::113',
                },
                'PoolTokenIncreased': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::113',
                },
                'Refund': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::113',
                    'index': 'u32',
                    'time_unit': 'scale_info::132',
                },
                'SupplementFeeAccountWhitelistAdded': {
                    'currency_id': 'scale_info::113',
                    'who': 'scale_info::57',
                },
                'SupplementFeeAccountWhitelistRemoved': {
                    'currency_id': 'scale_info::113',
                    'who': 'scale_info::57',
                },
                'TimeUnitUpdated': {
                    'currency_id': 'scale_info::113',
                    'new': 'scale_info::132',
                    'old': (None, 'scale_info::132'),
                },
                'TransferBack': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::113',
                    'from': 'scale_info::57',
                    'to': 'scale_info::57',
                },
                'TransferTo': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::113',
                    'from': 'scale_info::57',
                    'to': 'scale_info::57',
                },
                'Undelegated': {
                    'currency_id': 'scale_info::113',
                    'delegator_id': 'scale_info::57',
                    'query_id': 'u64',
                    'query_id_hash': '[u8; 32]',
                    'targets': ['scale_info::57'],
                },
                'ValidatorsAdded': {
                    'currency_id': 'scale_info::113',
                    'validator_id': 'scale_info::57',
                },
                'ValidatorsByDelegatorQueryResponseConfirmed': {
                    'entry': 'scale_info::170',
                    'query_id': 'u64',
                },
                'ValidatorsByDelegatorQueryResponseFailSuccessfully': {
                    'query_id': 'u64',
                },
                'ValidatorsByDelegatorSet': {
                    'currency_id': 'scale_info::113',
                    'delegator_id': 'scale_info::57',
                    'validators_list': [('scale_info::57', '[u8; 32]')],
                },
                'ValidatorsRemoved': {
                    'currency_id': 'scale_info::113',
                    'validator_id': 'scale_info::57',
                },
                'XcmDestWeightAndFeeSet': {
                    'currency_id': 'scale_info::113',
                    'operation': 'scale_info::142',
                    'weight_and_fee': (None, ('u64', 'u128')),
                },
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
            'SystemMaker': {
                'Charged': {
                    'currency_id': 'scale_info::113',
                    'value': 'u128',
                    'who': 'AccountId',
                },
                'Closed': {'currency_id': 'scale_info::113'},
                'ConfigSet': {
                    'currency_id': 'scale_info::113',
                    'info': 'scale_info::194',
                },
                'Paid': {'currency_id': 'scale_info::113', 'value': 'u128'},
                'RedeemFailed': {
                    'amount': 'u128',
                    'vcurrency_id': 'scale_info::113',
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
                    'result': 'scale_info::43',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::43',
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
            'Tips': {
                'NewTip': {'tip_hash': '[u8; 32]'},
                'TipClosed': {
                    'payout': 'u128',
                    'tip_hash': '[u8; 32]',
                    'who': 'AccountId',
                },
                'TipClosing': {'tip_hash': '[u8; 32]'},
                'TipRetracted': {'tip_hash': '[u8; 32]'},
                'TipSlashed': {
                    'deposit': 'u128',
                    'finder': 'AccountId',
                    'tip_hash': '[u8; 32]',
                },
            },
            'TokenConversion': {
                'ExchangeFeeSet': {'exchange_fee': 'scale_info::184'},
                'ExchangeRateSet': {
                    'exchange_rate': 'scale_info::186',
                    'lease': 'i32',
                },
                'RelaychainLeaseSet': {'lease': 'u32'},
                'VsbondConvertToVsdot': {
                    'address': 'AccountId',
                    'currency_id': 'scale_info::113',
                    'vsbond_amount': 'u128',
                    'vsdot_amount': 'u128',
                },
                'VsbondConvertToVsksm': {
                    'address': 'AccountId',
                    'currency_id': 'scale_info::113',
                    'vsbond_amount': 'u128',
                    'vsksm_amount': 'u128',
                },
                'VsbondConvertToVstoken': {
                    'address': 'AccountId',
                    'currency_id': 'scale_info::113',
                    'vsbond_amount': 'u128',
                    'vstoken_amount': 'u128',
                },
                'VsdotConvertToVsbond': {
                    'address': 'AccountId',
                    'currency_id': 'scale_info::113',
                    'vsbond_amount': 'u128',
                    'vsdot_amount': 'u128',
                },
                'VsksmConvertToVsbond': {
                    'address': 'AccountId',
                    'currency_id': 'scale_info::113',
                    'vsbond_amount': 'u128',
                    'vsksm_amount': 'u128',
                },
                'VstokenConvertToVsbond': {
                    'address': 'AccountId',
                    'currency_id': 'scale_info::113',
                    'vsbond_amount': 'u128',
                    'vstoken_amount': 'u128',
                },
            },
            'Tokens': {
                'BalanceSet': {
                    'currency_id': 'scale_info::113',
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Deposited': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::113',
                    'who': 'AccountId',
                },
                'DustLost': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::113',
                    'who': 'AccountId',
                },
                'Endowed': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::113',
                    'who': 'AccountId',
                },
                'LockRemoved': {
                    'currency_id': 'scale_info::113',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'LockSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::113',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::113',
                    'from': 'AccountId',
                    'status': 'scale_info::32',
                    'to': 'AccountId',
                },
                'Reserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::113',
                    'who': 'AccountId',
                },
                'Slashed': {
                    'currency_id': 'scale_info::113',
                    'free_amount': 'u128',
                    'reserved_amount': 'u128',
                    'who': 'AccountId',
                },
                'TotalIssuanceSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::113',
                },
                'Transfer': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::113',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unreserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::113',
                    'who': 'AccountId',
                },
                'Withdrawn': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::113',
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
            },
            'UnknownTokens': {
                'Deposited': {
                    'asset': 'scale_info::72',
                    'who': 'scale_info::57',
                },
                'Withdrawn': {
                    'asset': 'scale_info::72',
                    'who': 'scale_info::57',
                },
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::24',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::43'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::24'},
            },
            'Vesting': {
                'VestingCompleted': 'AccountId',
                'VestingUpdated': ('AccountId', 'u128'),
            },
            'VtokenMinting': {
                'FeeSet': {'mint_fee': 'u32', 'redeem_fee': 'u32'},
                'HookIterationLimitSet': {'limit': 'u32'},
                'MinTimeUnitSet': {
                    'time_unit': 'scale_info::132',
                    'token_id': 'scale_info::113',
                },
                'MinimumMintSet': {
                    'amount': 'u128',
                    'token_id': 'scale_info::113',
                },
                'MinimumRedeemSet': {
                    'amount': 'u128',
                    'token_id': 'scale_info::113',
                },
                'Minted': {
                    'address': 'AccountId',
                    'fee': 'u128',
                    'token_amount': 'u128',
                    'token_id': 'scale_info::113',
                    'vtoken_amount': 'u128',
                },
                'Rebonded': {
                    'address': 'AccountId',
                    'fee': 'u128',
                    'token_amount': 'u128',
                    'token_id': 'scale_info::113',
                    'vtoken_amount': 'u128',
                },
                'RebondedByUnlockId': {
                    'address': 'AccountId',
                    'fee': 'u128',
                    'token_amount': 'u128',
                    'token_id': 'scale_info::113',
                    'vtoken_amount': 'u128',
                },
                'RedeemSuccess': {
                    'to': 'AccountId',
                    'token_amount': 'u128',
                    'token_id': 'scale_info::113',
                    'unlock_id': 'u32',
                },
                'Redeemed': {
                    'address': 'AccountId',
                    'fee': 'u128',
                    'token_amount': 'u128',
                    'token_id': 'scale_info::113',
                    'vtoken_amount': 'u128',
                },
                'SupportRebondTokenAdded': {'token_id': 'scale_info::113'},
                'SupportRebondTokenRemoved': {'token_id': 'scale_info::113'},
                'UnlockDurationSet': {
                    'token_id': 'scale_info::113',
                    'unlock_duration': 'scale_info::132',
                },
                'UnlockingTotalSet': {
                    'amount': 'u128',
                    'token_id': 'scale_info::113',
                },
            },
            'XTokens': {
                'TransferredMultiAssets': {
                    'assets': ['scale_info::72'],
                    'dest': 'scale_info::57',
                    'fee': 'scale_info::72',
                    'sender': 'AccountId',
                },
            },
            'XcmInterface': {
                'TransferredStatemineMultiAsset': ('AccountId', 'u128'),
                'XcmDestWeightUpdated': ('scale_info::182', 'u64'),
                'XcmFeeUpdated': ('scale_info::182', 'u128'),
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': (None, '[u8; 32]')},
                'BadVersion': {'message_hash': (None, '[u8; 32]')},
                'Fail': {
                    'error': 'scale_info::53',
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
            'ZenlinkProtocol': {
                'AssetSwap': (
                    'AccountId',
                    'AccountId',
                    ['scale_info::118'],
                    ['u128'],
                ),
                'BootstrapClaim': (
                    'AccountId',
                    'AccountId',
                    'AccountId',
                    'scale_info::118',
                    'scale_info::118',
                    'u128',
                    'u128',
                    'u128',
                ),
                'BootstrapContribute': (
                    'AccountId',
                    'scale_info::118',
                    'u128',
                    'scale_info::118',
                    'u128',
                ),
                'BootstrapCreated': (
                    'AccountId',
                    'scale_info::118',
                    'scale_info::118',
                    'u128',
                    'u128',
                    'u128',
                    'u128',
                    'u32',
                ),
                'BootstrapEnd': (
                    'scale_info::118',
                    'scale_info::118',
                    'u128',
                    'u128',
                    'u128',
                ),
                'BootstrapRefund': (
                    'AccountId',
                    'AccountId',
                    'scale_info::118',
                    'scale_info::118',
                    'u128',
                    'u128',
                ),
                'BootstrapUpdate': (
                    'AccountId',
                    'scale_info::118',
                    'scale_info::118',
                    'u128',
                    'u128',
                    'u128',
                    'u128',
                    'u32',
                ),
                'Burned': ('scale_info::118', 'AccountId', 'u128'),
                'ChargeReward': (
                    'scale_info::118',
                    'scale_info::118',
                    'AccountId',
                    [('scale_info::118', 'u128')],
                ),
                'DistributeReward': (
                    'scale_info::118',
                    'scale_info::118',
                    'AccountId',
                    [('scale_info::118', 'u128')],
                ),
                'LiquidityAdded': (
                    'AccountId',
                    'scale_info::118',
                    'scale_info::118',
                    'u128',
                    'u128',
                    'u128',
                ),
                'LiquidityRemoved': (
                    'AccountId',
                    'AccountId',
                    'scale_info::118',
                    'scale_info::118',
                    'u128',
                    'u128',
                    'u128',
                ),
                'Minted': ('scale_info::118', 'AccountId', 'u128'),
                'PairCreated': ('scale_info::118', 'scale_info::118'),
                'Transferred': (
                    'scale_info::118',
                    'AccountId',
                    'AccountId',
                    'u128',
                ),
                'TransferredToParachain': (
                    'scale_info::118',
                    'AccountId',
                    'u32',
                    'AccountId',
                    'u128',
                    'u64',
                ),
                'WithdrawReward': (
                    'scale_info::118',
                    'scale_info::118',
                    'AccountId',
                ),
            },
            None: None,
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
    'base_block': {'proof_size': 0, 'ref_time': 5346284000},
    'max_block': {'proof_size': 5242880, 'ref_time': 500000000000},
    'per_class': {
        'mandatory': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 86298000},
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 86298000},
            'max_extrinsic': {'proof_size': 3407872, 'ref_time': 324913702000},
            'max_total': {'proof_size': 3932160, 'ref_time': 375000000000},
            'reserved': {'proof_size': 0, 'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 86298000},
            'max_extrinsic': {'proof_size': 4718592, 'ref_time': 449913702000},
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
6
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
        ('0xdf6acb689907609b', 4),
        ('0x40fe3ad401f8959a', 6),
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 2),
        ('0x37e397fc7c91f5e4', 1),
        ('0xf78b278be53f454c', 2),
        ('0xab3c0572291feb8b', 1),
        ('0xea93e3f16f3d6962', 2),
        ('0xdd718d5cc53262d4', 1),
        ('0xf877468f4ca0e826', 1),
        ('0x60aed43cb52456f1', 1),
        ('0xdc655468d8394120', 1),
        ('0x0d94b80c178630f0', 1),
    ],
    'authoring_version': 0,
    'impl_name': 'bifrost_polkadot',
    'impl_version': 0,
    'spec_name': 'bifrost_polkadot',
    'spec_version': 969,
    'state_version': 0,
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
### SpecVersionNeedsToIncrease
The specification version is not allowed to decrease between the current runtime
and the new runtime.

---------