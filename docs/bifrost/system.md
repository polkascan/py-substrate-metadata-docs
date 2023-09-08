
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
| dispatch_error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```
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
            'ConvictionVoting': {'Delegated': ('AccountId', 'AccountId'), 'Undelegated': 'AccountId'},
            'System': {
                'CodeUpdated': None,
                'ExtrinsicFailed': {
                    'dispatch_error': 'scale_info::25',
                    'dispatch_info': 'scale_info::22',
                },
                'ExtrinsicSuccess': {'dispatch_info': 'scale_info::22'},
                'KilledAccount': {'account': 'AccountId'},
                'NewAccount': {'account': 'AccountId'},
                'Remarked': {'hash': '[u8; 32]', 'sender': 'AccountId'},
            },
            None: None,
            'AssetRegistry': {
                'AssetRegistered': {
                    'asset_id': 'scale_info::417',
                    'metadata': 'scale_info::292',
                },
                'AssetUpdated': {
                    'asset_id': 'scale_info::417',
                    'metadata': 'scale_info::292',
                },
                'CurrencyIdRegistered': {
                    'currency_id': 'scale_info::255',
                    'metadata': 'scale_info::292',
                },
                'MultiLocationSet': {
                    'currency_id': 'scale_info::255',
                    'location': 'scale_info::119',
                    'weight': 'scale_info::9',
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
                    'destination_status': 'scale_info::34',
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
                    'BLP': 'u32',
                    'ForeignAsset': 'u32',
                    'LPToken': (
                        'scale_info::256',
                        'u8',
                        'scale_info::256',
                        'u8',
                    ),
                    'Native': 'scale_info::256',
                    'Stable': 'scale_info::256',
                    'StableLpToken': 'u32',
                    'Token': 'scale_info::256',
                    'Token2': 'u8',
                    'VSBond': ('scale_info::256', 'u32', 'u32', 'u32'),
                    'VSBond2': ('u8', 'u32', 'u32', 'u32'),
                    'VSToken': 'scale_info::256',
                    'VSToken2': 'u8',
                    'VToken': 'scale_info::256',
                    'VToken2': 'u8',
                },
                'TransferAccountEnabled': {
                    'BLP': 'u32',
                    'ForeignAsset': 'u32',
                    'LPToken': (
                        'scale_info::256',
                        'u8',
                        'scale_info::256',
                        'u8',
                    ),
                    'Native': 'scale_info::256',
                    'Stable': 'scale_info::256',
                    'StableLpToken': 'u32',
                    'Token': 'scale_info::256',
                    'Token2': 'u8',
                    'VSBond': ('scale_info::256', 'u32', 'u32', 'u32'),
                    'VSBond2': ('u8', 'u32', 'u32', 'u32'),
                    'VSToken': 'scale_info::256',
                    'VSToken2': 'u8',
                    'VToken': 'scale_info::256',
                    'VToken2': 'u8',
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
                    'result': 'scale_info::50',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::50',
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
            'CrossInOut': {
                'AddedToIssueList': {
                    'account': 'AccountId',
                    'currency_id': 'scale_info::255',
                },
                'AddedToRegisterList': {
                    'account': 'AccountId',
                    'currency_id': 'scale_info::255',
                },
                'CrossedIn': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                    'dest': 'AccountId',
                    'location': 'scale_info::133',
                    'remark': (None, 'Bytes'),
                },
                'CrossedOut': {
                    'amount': 'u128',
                    'crosser': 'AccountId',
                    'currency_id': 'scale_info::255',
                    'location': 'scale_info::133',
                },
                'CrossingMinimumAmountSet': {
                    'cross_in_minimum': 'u128',
                    'cross_out_minimum': 'u128',
                    'currency_id': 'scale_info::255',
                },
                'CurrencyDeregistered': {'currency_id': 'scale_info::255'},
                'CurrencyRegistered': {'currency_id': 'scale_info::255'},
                'LinkedAccountRegistered': {
                    'currency_id': 'scale_info::255',
                    'foreign_location': 'scale_info::133',
                    'who': 'AccountId',
                },
                'RemovedFromIssueList': {
                    'account': 'AccountId',
                    'currency_id': 'scale_info::255',
                },
                'RemovedFromRegisterList': {
                    'account': 'AccountId',
                    'currency_id': 'scale_info::255',
                },
            },
            'CumulusXcm': {
                'ExecutedDownward': ('[u8; 32]', 'scale_info::389'),
                'InvalidFormat': '[u8; 32]',
                'UnsupportedVersion': '[u8; 32]',
            },
            'Democracy': {
                'Blacklisted': {'proposal_hash': '[u8; 32]'},
                'Cancelled': {'ref_index': 'u32'},
                'Delegated': {'target': 'AccountId', 'who': 'AccountId'},
                'ExternalTabled': None,
                'MetadataCleared': {
                    'hash': '[u8; 32]',
                    'owner': 'scale_info::48',
                },
                'MetadataSet': {'hash': '[u8; 32]', 'owner': 'scale_info::48'},
                'MetadataTransferred': {
                    'hash': '[u8; 32]',
                    'owner': 'scale_info::48',
                    'prev_owner': 'scale_info::48',
                },
                'NotPassed': {'ref_index': 'u32'},
                'Passed': {'ref_index': 'u32'},
                'ProposalCanceled': {'prop_index': 'u32'},
                'Proposed': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Seconded': {'prop_index': 'u32', 'seconder': 'AccountId'},
                'Started': {'ref_index': 'u32', 'threshold': 'scale_info::45'},
                'Tabled': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Undelegated': {'account': 'AccountId'},
                'Vetoed': {
                    'proposal_hash': '[u8; 32]',
                    'until': 'u32',
                    'who': 'AccountId',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::46',
                    'voter': 'AccountId',
                },
            },
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::389',
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
            'Farming': {
                'AllForceGaugeClaimed': {'gid': 'u32'},
                'AllRetired': {'pid': 'u32'},
                'BoostCharged': {'rewards': [('scale_info::255', 'u128')], 'who': 'AccountId'},
                'Charged': {
                    'pid': 'u32',
                    'rewards': [('scale_info::255', 'u128')],
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
                'RoundEnd': {
                    'end_round': 'u32',
                    'start_round': 'u32',
                    'total_votes': 'u128',
                },
                'RoundStart': {'round_length': 'u32'},
                'RoundStartError': {'info': 'scale_info::25'},
                'Voted': {'vote_list': [('u32', 'u8')], 'who': 'AccountId'},
                'WithdrawClaimed': {'pid': 'u32', 'who': 'AccountId'},
                'Withdrawn': {
                    'pid': 'u32',
                    'remove_value': (None, 'u128'),
                    'who': 'AccountId',
                },
            },
            'FeeShare': {
                'Created': {'info': 'scale_info::435'},
                'Deleted': {'distribution_id': 'u32'},
                'Edited': {'info': 'scale_info::435'},
                'EraLengthSet': {'era_length': 'u32', 'next_era': 'u32'},
                'ExecuteFailed': {
                    'distribution_id': 'u32',
                    'info': 'scale_info::435',
                    'next_era': 'u32',
                },
                'Executed': {'distribution_id': 'u32'},
            },
            'FellowshipCollective': {
                'MemberAdded': {'who': 'AccountId'},
                'MemberRemoved': {'rank': 'u16', 'who': 'AccountId'},
                'RankChanged': {'rank': 'u16', 'who': 'AccountId'},
                'Voted': {
                    'poll': 'u32',
                    'tally': 'scale_info::441',
                    'vote': 'scale_info::440',
                    'who': 'AccountId',
                },
            },
            'FellowshipReferenda': {
                'Approved': {'index': 'u32'},
                'Cancelled': {'index': 'u32', 'tally': 'scale_info::441'},
                'ConfirmAborted': {'index': 'u32'},
                'ConfirmStarted': {'index': 'u32'},
                'Confirmed': {'index': 'u32', 'tally': 'scale_info::441'},
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
                    'proposal': 'scale_info::61',
                    'tally': 'scale_info::441',
                    'track': 'u16',
                },
                'DepositSlashed': {'amount': 'u128', 'who': 'AccountId'},
                'Killed': {'index': 'u32', 'tally': 'scale_info::441'},
                'MetadataCleared': {'hash': '[u8; 32]', 'index': 'u32'},
                'MetadataSet': {'hash': '[u8; 32]', 'index': 'u32'},
                'Rejected': {'index': 'u32', 'tally': 'scale_info::441'},
                'SubmissionDepositRefunded': {
                    'amount': 'u128',
                    'index': 'u32',
                    'who': 'AccountId',
                },
                'Submitted': {
                    'index': 'u32',
                    'proposal': 'scale_info::61',
                    'track': 'u16',
                },
                'TimedOut': {'index': 'u32', 'tally': 'scale_info::441'},
            },
            'FlexibleFee': {
                'ExtraFeeDeducted': (
                    'scale_info::411',
                    'scale_info::255',
                    'u128',
                ),
                'FixedRateFeeExchanged': ('scale_info::255', 'u128'),
                'FlexibleFeeExchanged': ('scale_info::255', 'u128'),
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
                    'timepoint': 'scale_info::207',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::207',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::50',
                    'timepoint': 'scale_info::207',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'OrmlXcm': {
                'Sent': {'message': ['scale_info::164'], 'to': 'scale_info::119'},
            },
            'ParachainStaking': {
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
                    'candidate': 'AccountId',
                    'execute_round': 'u32',
                },
                'CancelledCandidateExit': {'candidate': 'AccountId'},
                'CancelledDelegationRequest': {
                    'cancelled_request': 'scale_info::39',
                    'collator': 'AccountId',
                    'delegator': 'AccountId',
                },
                'CandidateBackOnline': {'candidate': 'AccountId'},
                'CandidateBondLessRequested': {
                    'amount_to_decrease': 'u128',
                    'candidate': 'AccountId',
                    'execute_round': 'u32',
                },
                'CandidateBondedLess': {
                    'amount': 'u128',
                    'candidate': 'AccountId',
                    'new_bond': 'u128',
                },
                'CandidateBondedMore': {
                    'amount': 'u128',
                    'candidate': 'AccountId',
                    'new_total_bond': 'u128',
                },
                'CandidateLeft': {
                    'ex_candidate': 'AccountId',
                    'new_total_amt_locked': 'u128',
                    'unlocked_amount': 'u128',
                },
                'CandidateScheduledExit': {
                    'candidate': 'AccountId',
                    'exit_allowed_round': 'u32',
                    'scheduled_exit': 'u32',
                },
                'CandidateWentOffline': {'candidate': 'AccountId'},
                'CollatorChosen': {
                    'collator_account': 'AccountId',
                    'round': 'u32',
                    'total_exposed_amount': 'u128',
                },
                'CollatorCommissionSet': {'new': 'u32', 'old': 'u32'},
                'Delegation': {
                    'candidate': 'AccountId',
                    'delegator': 'AccountId',
                    'delegator_position': 'scale_info::41',
                    'locked_amount': 'u128',
                },
                'DelegationDecreaseScheduled': {
                    'amount_to_decrease': 'u128',
                    'candidate': 'AccountId',
                    'delegator': 'AccountId',
                    'execute_round': 'u32',
                },
                'DelegationDecreased': {
                    'amount': 'u128',
                    'candidate': 'AccountId',
                    'delegator': 'AccountId',
                    'in_top': 'bool',
                },
                'DelegationIncreased': {
                    'amount': 'u128',
                    'candidate': 'AccountId',
                    'delegator': 'AccountId',
                    'in_top': 'bool',
                },
                'DelegationKicked': {
                    'candidate': 'AccountId',
                    'delegator': 'AccountId',
                    'unstaked_amount': 'u128',
                },
                'DelegationRevocationScheduled': {
                    'candidate': 'AccountId',
                    'delegator': 'AccountId',
                    'round': 'u32',
                    'scheduled_exit': 'u32',
                },
                'DelegationRevoked': {
                    'candidate': 'AccountId',
                    'delegator': 'AccountId',
                    'unstaked_amount': 'u128',
                },
                'DelegatorExitCancelled': {'delegator': 'AccountId'},
                'DelegatorExitScheduled': {
                    'delegator': 'AccountId',
                    'round': 'u32',
                    'scheduled_exit': 'u32',
                },
                'DelegatorLeft': {
                    'delegator': 'AccountId',
                    'unstaked_amount': 'u128',
                },
                'DelegatorLeftCandidate': {
                    'candidate': 'AccountId',
                    'delegator': 'AccountId',
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
                    'account': 'AccountId',
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
                    'new': 'AccountId',
                    'old': 'AccountId',
                },
                'ParachainBondReservePercentSet': {'new': 'u8', 'old': 'u8'},
                'ReservedForParachainBond': {
                    'account': 'AccountId',
                    'value': 'u128',
                },
                'Rewarded': {'account': 'AccountId', 'rewards': 'u128'},
                'StakeExpectationsSet': {
                    'expect_ideal': 'u128',
                    'expect_max': 'u128',
                    'expect_min': 'u128',
                },
                'TotalSelectedSet': {'new': 'u32', 'old': 'u32'},
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
                    'scale_info::119',
                    'scale_info::187',
                ),
                'AssetsTrapped': (
                    '[u8; 32]',
                    'scale_info::119',
                    'scale_info::187',
                ),
                'Attempted': {
                    'Complete': 'scale_info::9',
                    'Error': 'scale_info::174',
                    'Incomplete': ('scale_info::9', 'scale_info::174'),
                },
                'FeesPaid': ('scale_info::119', ['scale_info::167']),
                'InvalidQuerier': (
                    'scale_info::119',
                    'u64',
                    'scale_info::119',
                    (None, 'scale_info::119'),
                ),
                'InvalidQuerierVersion': ('scale_info::119', 'u64'),
                'InvalidResponder': (
                    'scale_info::119',
                    'u64',
                    (None, 'scale_info::119'),
                ),
                'InvalidResponderVersion': ('scale_info::119', 'u64'),
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
                'NotifyTargetMigrationFail': ('scale_info::132', 'u64'),
                'NotifyTargetSendFail': (
                    'scale_info::119',
                    'u64',
                    'scale_info::174',
                ),
                'ResponseReady': ('u64', 'scale_info::171'),
                'ResponseTaken': 'u64',
                'Sent': (
                    'scale_info::119',
                    'scale_info::119',
                    ['scale_info::164'],
                ),
                'SupportedVersionChanged': ('scale_info::119', 'u32'),
                'UnexpectedResponse': ('scale_info::119', 'u64'),
                'VersionChangeNotified': (
                    'scale_info::119',
                    'u32',
                    ['scale_info::167'],
                ),
                'VersionNotifyRequested': (
                    'scale_info::119',
                    ['scale_info::167'],
                ),
                'VersionNotifyStarted': (
                    'scale_info::119',
                    ['scale_info::167'],
                ),
                'VersionNotifyUnrequested': (
                    'scale_info::119',
                    ['scale_info::167'],
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
                    'proxy_type': 'scale_info::204',
                },
                'ProxyExecuted': {'result': 'scale_info::50'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::204',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::204',
                    'pure': 'AccountId',
                    'who': 'AccountId',
                },
            },
            'Referenda': {
                'Approved': {'index': 'u32'},
                'Cancelled': {'index': 'u32', 'tally': 'scale_info::382'},
                'ConfirmAborted': {'index': 'u32'},
                'ConfirmStarted': {'index': 'u32'},
                'Confirmed': {'index': 'u32', 'tally': 'scale_info::382'},
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
                    'proposal': 'scale_info::61',
                    'tally': 'scale_info::382',
                    'track': 'u16',
                },
                'DepositSlashed': {'amount': 'u128', 'who': 'AccountId'},
                'Killed': {'index': 'u32', 'tally': 'scale_info::382'},
                'MetadataCleared': {'hash': '[u8; 32]', 'index': 'u32'},
                'MetadataSet': {'hash': '[u8; 32]', 'index': 'u32'},
                'Rejected': {'index': 'u32', 'tally': 'scale_info::382'},
                'SubmissionDepositRefunded': {
                    'amount': 'u128',
                    'index': 'u32',
                    'who': 'AccountId',
                },
                'Submitted': {
                    'index': 'u32',
                    'proposal': 'scale_info::61',
                    'track': 'u16',
                },
                'TimedOut': {'index': 'u32', 'tally': 'scale_info::382'},
            },
            'Salp': {
                'AllRefunded': 'u32',
                'AllUnlocked': 'u32',
                'Buyback': 'u128',
                'BuybackByStablePool': {
                    'currency_id_in': 'scale_info::255',
                    'pool_id': 'u32',
                    'value': 'u128',
                },
                'Continued': ('u32', 'u32', 'u32'),
                'ContributeFailed': ('AccountId', 'u32', 'u128'),
                'Contributed': ('AccountId', 'u32', 'u128'),
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
                    'result': 'scale_info::50',
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
                    'currency_id': 'scale_info::255',
                    'delegator_id': 'scale_info::119',
                    'query_id': 'u64',
                    'query_id_hash': '[u8; 32]',
                },
                'ConvertAsset': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                    'who': 'scale_info::119',
                },
                'CurrencyDelaysSet': {
                    'currency_id': 'scale_info::255',
                    'delays': (None, 'scale_info::331'),
                },
                'CurrencyTuneExchangeRateLimitSet': {
                    'currency_id': 'scale_info::255',
                    'tune_exchange_rate_limit': (None, ('u32', 'u32')),
                },
                'Delegated': {
                    'currency_id': 'scale_info::255',
                    'delegator_id': 'scale_info::119',
                    'query_id': 'u64',
                    'query_id_hash': '[u8; 32]',
                    'targets': (None, ['scale_info::119']),
                },
                'DelegatorAdded': {
                    'currency_id': 'scale_info::255',
                    'delegator_id': 'scale_info::119',
                    'index': 'u16',
                },
                'DelegatorBondExtra': {
                    'currency_id': 'scale_info::255',
                    'delegator_id': 'scale_info::119',
                    'extra_bonded_amount': 'u128',
                    'query_id': 'u64',
                    'query_id_hash': '[u8; 32]',
                    'validator': (None, 'scale_info::119'),
                },
                'DelegatorBonded': {
                    'bonded_amount': 'u128',
                    'currency_id': 'scale_info::255',
                    'delegator_id': 'scale_info::119',
                    'query_id': 'u64',
                    'query_id_hash': '[u8; 32]',
                    'validator': (None, 'scale_info::119'),
                },
                'DelegatorInitialized': {
                    'currency_id': 'scale_info::255',
                    'delegator_id': 'scale_info::119',
                },
                'DelegatorLedgerQueryResponseConfirmed': {
                    'entry': 'scale_info::420',
                    'query_id': 'u64',
                },
                'DelegatorLedgerQueryResponseFailed': {'query_id': 'u64'},
                'DelegatorLedgerSet': {
                    'currency_id': 'scale_info::255',
                    'delegator': 'scale_info::119',
                    'ledger': (None, 'scale_info::310'),
                },
                'DelegatorRebond': {
                    'currency_id': 'scale_info::255',
                    'delegator_id': 'scale_info::119',
                    'query_id': 'u64',
                    'query_id_hash': '[u8; 32]',
                    'rebond_amount': (None, 'u128'),
                    'validator': (None, 'scale_info::119'),
                },
                'DelegatorRemoved': {
                    'currency_id': 'scale_info::255',
                    'delegator_id': 'scale_info::119',
                },
                'DelegatorUnbond': {
                    'currency_id': 'scale_info::255',
                    'delegator_id': 'scale_info::119',
                    'query_id': 'u64',
                    'query_id_hash': '[u8; 32]',
                    'unbond_amount': 'u128',
                    'validator': (None, 'scale_info::119'),
                },
                'DelegatorUnbondAll': {
                    'currency_id': 'scale_info::255',
                    'delegator_id': 'scale_info::119',
                    'query_id': 'u64',
                    'query_id_hash': '[u8; 32]',
                },
                'FeeSourceSet': {
                    'currency_id': 'scale_info::255',
                    'who_and_fee': (None, ('scale_info::119', 'u128')),
                },
                'FeeSupplemented': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                    'from': 'scale_info::119',
                    'to': 'scale_info::119',
                },
                'FundMoveFromExitToEntrance': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                },
                'HostingFeeCharged': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                },
                'HostingFeesSet': {
                    'currency_id': 'scale_info::255',
                    'fees': (None, ('u32', 'scale_info::119')),
                },
                'Liquidize': {
                    'amount': (None, 'u128'),
                    'currency_id': 'scale_info::255',
                    'delegator_id': 'scale_info::119',
                    'query_id': 'u64',
                    'query_id_hash': '[u8; 32]',
                    'time_unit': (None, 'scale_info::295'),
                },
                'MinimumsMaximumsSet': {
                    'currency_id': 'scale_info::255',
                    'minimums_and_maximums': (None, 'scale_info::329'),
                },
                'OngoingTimeUnitUpdateIntervalSet': {
                    'currency_id': 'scale_info::255',
                    'interval': (None, 'u32'),
                },
                'OperateOriginSet': {
                    'currency_id': 'scale_info::255',
                    'operator': (None, 'AccountId'),
                },
                'Payout': {
                    'currency_id': 'scale_info::255',
                    'time_unit': (None, 'scale_info::295'),
                    'validator': 'scale_info::119',
                },
                'PoolTokenDecreased': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                },
                'PoolTokenIncreased': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                },
                'Refund': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                    'index': 'u32',
                    'time_unit': 'scale_info::295',
                },
                'RemovedFromBoostList': {
                    'currency_id': 'scale_info::255',
                    'who': 'scale_info::119',
                },
                'SupplementFeeAccountWhitelistAdded': {
                    'currency_id': 'scale_info::255',
                    'who': 'scale_info::119',
                },
                'SupplementFeeAccountWhitelistRemoved': {
                    'currency_id': 'scale_info::255',
                    'who': 'scale_info::119',
                },
                'TimeUnitUpdated': {
                    'currency_id': 'scale_info::255',
                    'new': 'scale_info::295',
                    'old': (None, 'scale_info::295'),
                },
                'TransferBack': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                    'from': 'scale_info::119',
                    'to': 'scale_info::119',
                },
                'TransferTo': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                    'from': 'scale_info::119',
                    'to': 'scale_info::119',
                },
                'Undelegated': {
                    'currency_id': 'scale_info::255',
                    'delegator_id': 'scale_info::119',
                    'query_id': 'u64',
                    'query_id_hash': '[u8; 32]',
                    'targets': ['scale_info::119'],
                },
                'ValidatorBoostListAdded': {
                    'currency_id': 'scale_info::255',
                    'due_block_number': 'u32',
                    'who': 'scale_info::119',
                },
                'ValidatorBoostListSet': {
                    'currency_id': 'scale_info::255',
                    'validator_boost_list': [('scale_info::119', 'u32')],
                },
                'ValidatorsAdded': {
                    'currency_id': 'scale_info::255',
                    'validator_id': 'scale_info::119',
                },
                'ValidatorsByDelegatorQueryResponseConfirmed': {
                    'entry': 'scale_info::425',
                    'query_id': 'u64',
                },
                'ValidatorsByDelegatorQueryResponseFailed': {
                    'query_id': 'u64',
                },
                'ValidatorsByDelegatorSet': {
                    'currency_id': 'scale_info::255',
                    'delegator_id': 'scale_info::119',
                    'validators_list': ['scale_info::119'],
                },
                'ValidatorsRemoved': {
                    'currency_id': 'scale_info::255',
                    'validator_id': 'scale_info::119',
                },
                'ValidatorsReset': {
                    'currency_id': 'scale_info::255',
                    'validator_list': ['scale_info::119'],
                },
                'XcmDestWeightAndFeeSet': {
                    'currency_id': 'scale_info::255',
                    'operation': 'scale_info::303',
                    'weight_and_fee': (None, ('scale_info::9', 'u128')),
                },
            },
            'Slpx': {
                'AddWhitelistAccountId': {
                    'evm_contract_account_id': 'AccountId',
                    'support_chain': 'scale_info::374',
                },
                'RemoveWhitelistAccountId': {
                    'evm_contract_account_id': 'AccountId',
                    'support_chain': 'scale_info::374',
                },
                'SetExecutionFee': {
                    'currency_id': 'scale_info::255',
                    'execution_fee': 'u128',
                },
                'SetTransferToFee': {
                    'support_chain': 'scale_info::374',
                    'transfer_to_fee': 'u128',
                },
                'XcmMint': {
                    'currency_id': 'scale_info::255',
                    'evm_caller': '[u8; 20]',
                    'target_chain': 'scale_info::373',
                    'token_amount': 'u128',
                },
                'XcmMintFailed': {
                    'currency_id': 'scale_info::255',
                    'evm_caller': '[u8; 20]',
                    'target_chain': 'scale_info::373',
                    'token_amount': 'u128',
                },
                'XcmRedeem': {
                    'evm_caller': '[u8; 20]',
                    'target_chain': 'scale_info::373',
                    'vtoken_amount': 'u128',
                    'vtoken_id': 'scale_info::255',
                },
                'XcmRedeemFailed': {
                    'evm_caller': '[u8; 20]',
                    'target_chain': 'scale_info::373',
                    'vtoken_amount': 'u128',
                    'vtoken_id': 'scale_info::255',
                },
                'XcmStablePoolSwap': {
                    'currency_id_out_amount': 'u128',
                    'evm_caller': '[u8; 20]',
                    'pool_token_index_in': 'u32',
                    'pool_token_index_out': 'u32',
                    'target_chain': 'scale_info::373',
                },
                'XcmStablePoolSwapFailed': {
                    'currency_id_in_amount': 'u128',
                    'evm_caller': '[u8; 20]',
                    'pool_token_index_in': 'u32',
                    'pool_token_index_out': 'u32',
                    'target_chain': 'scale_info::373',
                },
                'XcmZenlinkSwap': {
                    'currency_id_in': 'scale_info::255',
                    'currency_id_out': 'scale_info::255',
                    'currency_id_out_amount': 'u128',
                    'evm_caller': '[u8; 20]',
                    'target_chain': 'scale_info::373',
                },
                'XcmZenlinkSwapFailed': {
                    'currency_id_in': 'scale_info::255',
                    'currency_id_in_amount': 'u128',
                    'currency_id_out': 'scale_info::255',
                    'evm_caller': '[u8; 20]',
                    'target_chain': 'scale_info::373',
                },
            },
            'StableAsset': {
                'AModified': {
                    'pool_id': 'u32',
                    'time': 'u32',
                    'value': 'u128',
                },
                'BalanceUpdated': {
                    'new_balances': ['u128'],
                    'old_balances': ['u128'],
                    'pool_id': 'u32',
                },
                'CreatePool': {
                    'a': 'u128',
                    'pallet_id': 'AccountId',
                    'pool_id': 'u32',
                    'swap_id': 'AccountId',
                },
                'FeeCollected': {
                    'a': 'u128',
                    'amount': 'u128',
                    'new_balances': ['u128'],
                    'new_total_supply': 'u128',
                    'old_balances': ['u128'],
                    'old_total_supply': 'u128',
                    'pool_id': 'u32',
                    'who': 'AccountId',
                },
                'FeeModified': {
                    'mint_fee': 'u128',
                    'pool_id': 'u32',
                    'redeem_fee': 'u128',
                    'swap_fee': 'u128',
                },
                'LiquidityAdded': {
                    'a': 'u128',
                    'balances': ['u128'],
                    'fee_amount': 'u128',
                    'input_amounts': ['u128'],
                    'min_output_amount': 'u128',
                    'minter': 'AccountId',
                    'output_amount': 'u128',
                    'pool_id': 'u32',
                    'total_supply': 'u128',
                },
                'RecipientModified': {
                    'fee_recipient': 'AccountId',
                    'pool_id': 'u32',
                    'yield_recipient': 'AccountId',
                },
                'RedeemedMulti': {
                    'a': 'u128',
                    'balances': ['u128'],
                    'fee_amount': 'u128',
                    'input_amount': 'u128',
                    'max_input_amount': 'u128',
                    'output_amounts': ['u128'],
                    'pool_id': 'u32',
                    'redeemer': 'AccountId',
                    'total_supply': 'u128',
                },
                'RedeemedProportion': {
                    'a': 'u128',
                    'balances': ['u128'],
                    'fee_amount': 'u128',
                    'input_amount': 'u128',
                    'min_output_amounts': ['u128'],
                    'output_amounts': ['u128'],
                    'pool_id': 'u32',
                    'redeemer': 'AccountId',
                    'total_supply': 'u128',
                },
                'RedeemedSingle': {
                    'a': 'u128',
                    'balances': ['u128'],
                    'fee_amount': 'u128',
                    'input_amount': 'u128',
                    'min_output_amount': 'u128',
                    'output_amount': 'u128',
                    'output_asset': 'scale_info::255',
                    'pool_id': 'u32',
                    'redeemer': 'AccountId',
                    'total_supply': 'u128',
                },
                'TokenRateSet': {
                    'pool_id': 'u32',
                    'token_rate': [('scale_info::255', ('u128', 'u128'))],
                },
                'TokenSwapped': {
                    'a': 'u128',
                    'balances': ['u128'],
                    'input_amount': 'u128',
                    'input_asset': 'scale_info::255',
                    'min_output_amount': 'u128',
                    'output_amount': 'u128',
                    'output_asset': 'scale_info::255',
                    'pool_id': 'u32',
                    'swapper': 'AccountId',
                    'total_supply': 'u128',
                },
                'YieldCollected': {
                    'a': 'u128',
                    'amount': 'u128',
                    'new_total_supply': 'u128',
                    'old_total_supply': 'u128',
                    'pool_id': 'u32',
                    'who': 'AccountId',
                },
            },
            'SystemMaker': {
                'Charged': {
                    'currency_id': 'scale_info::255',
                    'value': 'u128',
                    'who': 'AccountId',
                },
                'Closed': {'currency_id': 'scale_info::255'},
                'ConfigSet': {
                    'currency_id': 'scale_info::255',
                    'info': 'scale_info::363',
                },
                'Paid': {'currency_id': 'scale_info::255', 'value': 'u128'},
                'RedeemFailed': {
                    'amount': 'u128',
                    'vcurrency_id': 'scale_info::255',
                },
            },
            'SystemStaking': {
                'DepositFailed': {
                    'amount': 'u128',
                    'farming_staking_amount': 'u128',
                    'pending_redeem_amount': 'u128',
                    'system_shadow_amount': 'u128',
                    'system_stakable_amount': 'u128',
                    'token': 'scale_info::255',
                },
                'MintFailed': {
                    'amount': 'u128',
                    'farming_staking_amount': 'u128',
                    'pending_redeem_amount': 'u128',
                    'system_shadow_amount': 'u128',
                    'system_stakable_amount': 'u128',
                    'token': 'scale_info::255',
                },
                'MintSuccess': {
                    'amount': 'u128',
                    'farming_staking_amount': 'u128',
                    'pending_redeem_amount': 'u128',
                    'system_shadow_amount': 'u128',
                    'system_stakable_amount': 'u128',
                    'token': 'scale_info::255',
                },
                'NewRound': {
                    'current': 'u32',
                    'first': 'u32',
                    'length': 'u32',
                },
                'Payout': {
                    'amount': 'u128',
                    'free': 'u128',
                    'from': 'AccountId',
                    'shadow': 'u128',
                    'to': 'AccountId',
                    'token': 'scale_info::255',
                    'vfree': 'u128',
                    'vtoken': 'scale_info::255',
                },
                'RedeemFailed': {
                    'amount': 'u128',
                    'farming_staking_amount': 'u128',
                    'pending_redeem_amount': 'u128',
                    'system_shadow_amount': 'u128',
                    'system_stakable_amount': 'u128',
                    'token': 'scale_info::255',
                },
                'Redeemed': {
                    'amount': 'u128',
                    'farming_staking_amount': 'u128',
                    'pending_redeem_amount': 'u128',
                    'system_shadow_amount': 'u128',
                    'system_stakable_amount': 'u128',
                    'token': 'scale_info::255',
                },
                'TokenConfigChanged': {
                    'add_or_sub': 'bool',
                    'exec_delay': 'u32',
                    'farming_poolids': ['u32'],
                    'lptoken_rates': ['u32'],
                    'system_stakable_base': 'u128',
                    'system_stakable_farming_rate': 'u32',
                    'token': 'scale_info::255',
                },
                'TokenInfoRefreshed': {'token': 'scale_info::255'},
                'VtokenNotFound': {'token': 'scale_info::255'},
                'WithdrawFailed': {
                    'amount': 'u128',
                    'farming_staking_amount': 'u128',
                    'pending_redeem_amount': 'u128',
                    'system_shadow_amount': 'u128',
                    'system_stakable_amount': 'u128',
                    'token': 'scale_info::255',
                },
                'WithdrawSuccess': {
                    'amount': 'u128',
                    'farming_staking_amount': 'u128',
                    'pending_redeem_amount': 'u128',
                    'system_shadow_amount': 'u128',
                    'system_stakable_amount': 'u128',
                    'token': 'scale_info::255',
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
                    'result': 'scale_info::50',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::50',
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
            'TokenIssuer': {
                'AddedToIssueList': ('AccountId', 'scale_info::255'),
                'AddedToTransferList': ('AccountId', 'scale_info::255'),
                'Issued': ('AccountId', 'scale_info::255', 'u128'),
                'RemovedFromIssueList': ('AccountId', 'scale_info::255'),
                'RemovedFromTransferList': ('AccountId', 'scale_info::255'),
                'Transferred': (
                    'AccountId',
                    'AccountId',
                    'scale_info::255',
                    'u128',
                ),
            },
            'Tokens': {
                'BalanceSet': {
                    'currency_id': 'scale_info::255',
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Deposited': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                    'who': 'AccountId',
                },
                'DustLost': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                    'who': 'AccountId',
                },
                'Endowed': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                    'who': 'AccountId',
                },
                'LockRemoved': {
                    'currency_id': 'scale_info::255',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'LockSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'Locked': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                    'who': 'AccountId',
                },
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                    'from': 'AccountId',
                    'status': 'scale_info::34',
                    'to': 'AccountId',
                },
                'Reserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                    'who': 'AccountId',
                },
                'Slashed': {
                    'currency_id': 'scale_info::255',
                    'free_amount': 'u128',
                    'reserved_amount': 'u128',
                    'who': 'AccountId',
                },
                'TotalIssuanceSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                },
                'Transfer': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unlocked': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                    'who': 'AccountId',
                },
                'Unreserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
                    'who': 'AccountId',
                },
                'Withdrawn': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::255',
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
                    'asset': 'scale_info::167',
                    'who': 'scale_info::119',
                },
                'Withdrawn': {
                    'asset': 'scale_info::167',
                    'who': 'scale_info::119',
                },
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::25',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::50'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::25'},
            },
            'VSBondAuction': {
                'OrderClinchd': (
                    'u64',
                    'scale_info::290',
                    'AccountId',
                    'AccountId',
                    'scale_info::255',
                    'u128',
                    'u128',
                    'u128',
                    'u128',
                ),
                'OrderCreated': (
                    'u64',
                    'scale_info::290',
                    'AccountId',
                    'scale_info::255',
                    'u128',
                    'u128',
                ),
                'OrderRevoked': (
                    'u64',
                    'scale_info::290',
                    'AccountId',
                    'scale_info::255',
                    'u128',
                    'u128',
                    'u128',
                ),
                'TransactionFeeRateSet': ('u32', 'u32'),
            },
            'Vesting': {
                'VestingCompleted': 'AccountId',
                'VestingUpdated': ('AccountId', 'u128'),
            },
            'VstokenConversion': {
                'ExchangeFeeSet': {'exchange_fee': 'scale_info::342'},
                'ExchangeRateSet': {
                    'exchange_rate': 'scale_info::344',
                    'lease': 'i32',
                },
                'RelaychainLeaseSet': {'lease': 'u32'},
                'VsbondConvertToVsdot': {
                    'address': 'AccountId',
                    'currency_id': 'scale_info::255',
                    'vsbond_amount': 'u128',
                    'vsdot_amount': 'u128',
                },
                'VsbondConvertToVsksm': {
                    'address': 'AccountId',
                    'currency_id': 'scale_info::255',
                    'vsbond_amount': 'u128',
                    'vsksm_amount': 'u128',
                },
                'VsbondConvertToVstoken': {
                    'address': 'AccountId',
                    'currency_id': 'scale_info::255',
                    'vsbond_amount': 'u128',
                    'vstoken_amount': 'u128',
                },
                'VsdotConvertToVsbond': {
                    'address': 'AccountId',
                    'currency_id': 'scale_info::255',
                    'vsbond_amount': 'u128',
                    'vsdot_amount': 'u128',
                },
                'VsksmConvertToVsbond': {
                    'address': 'AccountId',
                    'currency_id': 'scale_info::255',
                    'vsbond_amount': 'u128',
                    'vsksm_amount': 'u128',
                },
                'VstokenConvertToVsbond': {
                    'address': 'AccountId',
                    'currency_id': 'scale_info::255',
                    'vsbond_amount': 'u128',
                    'vstoken_amount': 'u128',
                },
            },
            'VtokenMinting': {
                'FastRedeemFailed': {'err': 'scale_info::25'},
                'FeeSet': {'mint_fee': 'u32', 'redeem_fee': 'u32'},
                'HookIterationLimitSet': {'limit': 'u32'},
                'MinTimeUnitSet': {
                    'time_unit': 'scale_info::295',
                    'token_id': 'scale_info::255',
                },
                'MinimumMintSet': {
                    'amount': 'u128',
                    'token_id': 'scale_info::255',
                },
                'MinimumRedeemSet': {
                    'amount': 'u128',
                    'token_id': 'scale_info::255',
                },
                'Minted': {
                    'address': 'AccountId',
                    'fee': 'u128',
                    'remark': 'Bytes',
                    'token_amount': 'u128',
                    'token_id': 'scale_info::255',
                    'vtoken_amount': 'u128',
                },
                'Rebonded': {
                    'address': 'AccountId',
                    'fee': 'u128',
                    'token_amount': 'u128',
                    'token_id': 'scale_info::255',
                    'vtoken_amount': 'u128',
                },
                'RebondedByUnlockId': {
                    'address': 'AccountId',
                    'fee': 'u128',
                    'token_amount': 'u128',
                    'token_id': 'scale_info::255',
                    'vtoken_amount': 'u128',
                },
                'RedeemSuccess': {
                    'to': 'AccountId',
                    'token_amount': 'u128',
                    'token_id': 'scale_info::255',
                    'unlock_id': 'u32',
                },
                'Redeemed': {
                    'address': 'AccountId',
                    'fee': 'u128',
                    'token_amount': 'u128',
                    'token_id': 'scale_info::255',
                    'vtoken_amount': 'u128',
                },
                'SupportRebondTokenAdded': {'token_id': 'scale_info::255'},
                'SupportRebondTokenRemoved': {'token_id': 'scale_info::255'},
                'UnlockDurationSet': {
                    'token_id': 'scale_info::255',
                    'unlock_duration': 'scale_info::295',
                },
                'UnlockingTotalSet': {
                    'amount': 'u128',
                    'token_id': 'scale_info::255',
                },
            },
            'Whitelist': {
                'CallWhitelisted': {'call_hash': '[u8; 32]'},
                'WhitelistedCallDispatched': {
                    'call_hash': '[u8; 32]',
                    'result': 'scale_info::384',
                },
                'WhitelistedCallRemoved': {'call_hash': '[u8; 32]'},
            },
            'XTokens': {
                'TransferredMultiAssets': {
                    'assets': ['scale_info::167'],
                    'dest': 'scale_info::119',
                    'fee': 'scale_info::167',
                    'sender': 'AccountId',
                },
            },
            'XcmInterface': {
                'TransferredStatemineMultiAsset': ('AccountId', 'u128'),
                'XcmDestWeightUpdated': ('scale_info::339', 'scale_info::9'),
                'XcmFeeUpdated': ('scale_info::339', 'u128'),
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': (None, '[u8; 32]')},
                'BadVersion': {'message_hash': (None, '[u8; 32]')},
                'Fail': {
                    'error': 'scale_info::174',
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
            'ZenlinkProtocol': {
                'AssetSwap': (
                    'AccountId',
                    'AccountId',
                    ['scale_info::266'],
                    ['u128'],
                ),
                'BootstrapClaim': (
                    'AccountId',
                    'AccountId',
                    'AccountId',
                    'scale_info::266',
                    'scale_info::266',
                    'u128',
                    'u128',
                    'u128',
                ),
                'BootstrapContribute': (
                    'AccountId',
                    'scale_info::266',
                    'u128',
                    'scale_info::266',
                    'u128',
                ),
                'BootstrapCreated': (
                    'AccountId',
                    'scale_info::266',
                    'scale_info::266',
                    'u128',
                    'u128',
                    'u128',
                    'u128',
                    'u32',
                ),
                'BootstrapEnd': (
                    'scale_info::266',
                    'scale_info::266',
                    'u128',
                    'u128',
                    'u128',
                ),
                'BootstrapRefund': (
                    'AccountId',
                    'AccountId',
                    'scale_info::266',
                    'scale_info::266',
                    'u128',
                    'u128',
                ),
                'BootstrapUpdate': (
                    'AccountId',
                    'scale_info::266',
                    'scale_info::266',
                    'u128',
                    'u128',
                    'u128',
                    'u128',
                    'u32',
                ),
                'Burned': ('scale_info::266', 'AccountId', 'u128'),
                'ChargeReward': (
                    'scale_info::266',
                    'scale_info::266',
                    'AccountId',
                    [('scale_info::266', 'u128')],
                ),
                'DistributeReward': (
                    'scale_info::266',
                    'scale_info::266',
                    'AccountId',
                    [('scale_info::266', 'u128')],
                ),
                'LiquidityAdded': (
                    'AccountId',
                    'scale_info::266',
                    'scale_info::266',
                    'u128',
                    'u128',
                    'u128',
                ),
                'LiquidityRemoved': (
                    'AccountId',
                    'AccountId',
                    'scale_info::266',
                    'scale_info::266',
                    'u128',
                    'u128',
                    'u128',
                ),
                'Minted': ('scale_info::266', 'AccountId', 'u128'),
                'PairCreated': ('scale_info::266', 'scale_info::266'),
                'Transferred': (
                    'scale_info::266',
                    'AccountId',
                    'AccountId',
                    'u128',
                ),
                'TransferredToParachain': (
                    'scale_info::266',
                    'AccountId',
                    'u32',
                    'AccountId',
                    'u128',
                    'u64',
                ),
                'WithdrawReward': (
                    'scale_info::266',
                    'scale_info::266',
                    'AccountId',
                ),
            },
            'ZenlinkStableAMM': {
                'AddLiquidity': {
                    'fees': ['u128'],
                    'mint_amount': 'u128',
                    'new_d': 'u128',
                    'pool_id': 'u32',
                    'supply_amounts': ['u128'],
                    'to': 'AccountId',
                    'who': 'AccountId',
                },
                'CollectProtocolFee': {
                    'currency_id': 'scale_info::255',
                    'fee_amount': 'u128',
                    'pool_id': 'u32',
                },
                'CreatePool': {
                    'a': 'u128',
                    'account': 'AccountId',
                    'admin_fee_receiver': 'AccountId',
                    'currency_ids': ['scale_info::255'],
                    'lp_currency_id': 'scale_info::255',
                    'pool_id': 'u32',
                },
                'CurrencyExchange': {
                    'in_amount': 'u128',
                    'in_index': 'u32',
                    'out_amount': 'u128',
                    'out_index': 'u32',
                    'pool_id': 'u32',
                    'to': 'AccountId',
                    'who': 'AccountId',
                },
                'CurrencyExchangeUnderlying': {
                    'account': 'AccountId',
                    'currency_index_from': 'u32',
                    'currency_index_to': 'u32',
                    'in_amount': 'u128',
                    'out_amount': 'u128',
                    'pool_id': 'u32',
                    'to': 'AccountId',
                },
                'NewAdminFee': {'new_admin_fee': 'u128', 'pool_id': 'u32'},
                'NewSwapFee': {'new_swap_fee': 'u128', 'pool_id': 'u32'},
                'RampA': {
                    'future_a_precise': 'u128',
                    'future_a_time': 'u128',
                    'initial_a_precise': 'u128',
                    'now': 'u128',
                    'pool_id': 'u32',
                },
                'RemoveLiquidity': {
                    'amounts': ['u128'],
                    'fees': ['u128'],
                    'new_total_supply': 'u128',
                    'pool_id': 'u32',
                    'to': 'AccountId',
                    'who': 'AccountId',
                },
                'RemoveLiquidityImbalance': {
                    'amounts': ['u128'],
                    'fees': ['u128'],
                    'new_d': 'u128',
                    'new_total_supply': 'u128',
                    'pool_id': 'u32',
                    'to': 'AccountId',
                    'who': 'AccountId',
                },
                'RemoveLiquidityOneCurrency': {
                    'burn_amount': 'u128',
                    'out_amount': 'u128',
                    'out_index': 'u32',
                    'pool_id': 'u32',
                    'to': 'AccountId',
                    'who': 'AccountId',
                },
                'StopRampA': {
                    'current_a': 'u128',
                    'now': 'u128',
                    'pool_id': 'u32',
                },
                'UpdateAdminFeeReceiver': {
                    'admin_fee_receiver': 'AccountId',
                    'pool_id': 'u32',
                },
            },
            'ZenlinkSwapRouter': (),
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
            'max_extrinsic': {'proof_size': 3407872, 'ref_time': 324886362000},
            'max_total': {'proof_size': 3932160, 'ref_time': 375000000000},
            'reserved': {'proof_size': 0, 'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 113638000},
            'max_extrinsic': {'proof_size': 4718592, 'ref_time': 449886362000},
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
        ('0x37c8bb1350a9a2a8', 4),
        ('0x37e397fc7c91f5e4', 2),
        ('0xf78b278be53f454c', 2),
        ('0xab3c0572291feb8b', 1),
        ('0xea93e3f16f3d6962', 2),
        ('0xdd718d5cc53262d4', 1),
        ('0xf877468f4ca0e826', 1),
        ('0x60aed43cb52456f1', 1),
        ('0x5179b539a332ab9a', 1),
        ('0xdc655468d8394120', 1),
        ('0x0d94b80c178630f0', 1),
        ('0x56efef6dbb213baf', 1),
    ],
    'authoring_version': 1,
    'impl_name': 'bifrost',
    'impl_version': 0,
    'spec_name': 'bifrost',
    'spec_version': 980,
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