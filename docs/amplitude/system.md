
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
            'AssetRegistry': {
                'RegisteredAsset': {
                    'asset_id': 'scale_info::122',
                    'metadata': 'scale_info::180',
                },
                'UpdatedAsset': {
                    'asset_id': 'scale_info::122',
                    'metadata': 'scale_info::180',
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
            None: None,
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
                    'destination_status': 'scale_info::33',
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
            'ClientsInfo': {
                'AccountIdAuthorized': 'AccountId',
                'AccountIdDeauthorized': 'AccountId',
                'ApplyClientRelease': {'release': 'scale_info::165'},
                'NotifyClientRelease': {'release': 'scale_info::165'},
            },
            'Contracts': {
                'Called': {'caller': 'AccountId', 'contract': 'AccountId'},
                'CodeRemoved': {'code_hash': 'scale_info::12'},
                'CodeStored': {'code_hash': 'scale_info::12'},
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
                'Terminated': {
                    'beneficiary': 'AccountId',
                    'contract': 'AccountId',
                },
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
                    'result': 'scale_info::42',
                },
                'MemberExecuted': {
                    'proposal_hash': 'scale_info::12',
                    'result': 'scale_info::42',
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
            'CumulusXcm': {
                'ExecutedDownward': ('[u8; 32]', 'scale_info::63'),
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
                    'owner': 'scale_info::39',
                },
                'MetadataSet': {
                    'hash': 'scale_info::12',
                    'owner': 'scale_info::39',
                },
                'MetadataTransferred': {
                    'hash': 'scale_info::12',
                    'owner': 'scale_info::39',
                    'prev_owner': 'scale_info::39',
                },
                'NotPassed': {'ref_index': 'u32'},
                'Passed': {'ref_index': 'u32'},
                'ProposalCanceled': {'prop_index': 'u32'},
                'Proposed': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Seconded': {'prop_index': 'u32', 'seconder': 'AccountId'},
                'Started': {'ref_index': 'u32', 'threshold': 'scale_info::36'},
                'Tabled': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Undelegated': {'account': 'AccountId'},
                'Vetoed': {
                    'proposal_hash': 'scale_info::12',
                    'until': 'u32',
                    'who': 'AccountId',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::37',
                    'voter': 'AccountId',
                },
            },
            'DiaOracleModule': {
                'AccountIdAuthorized': 'AccountId',
                'AccountIdDeauthorized': 'AccountId',
                'BatchingApiRouteSet': 'Bytes',
                'CurrencyAdded': ('Bytes', 'Bytes'),
                'CurrencyRemoved': ('Bytes', 'Bytes'),
                'UpdatedPrices': [(('Bytes', 'Bytes'), 'scale_info::132')],
            },
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::63',
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
                'BoostCharged': {'rewards': [('scale_info::122', 'u128')], 'who': 'AccountId'},
                'Charged': {
                    'pid': 'u32',
                    'rewards': [('scale_info::122', 'u128')],
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
            'Issue': {
                'CancelIssue': {
                    'griefing_collateral': 'u128',
                    'issue_id': 'scale_info::12',
                    'requester': 'AccountId',
                },
                'ExecuteIssue': {
                    'amount': 'u128',
                    'asset': 'scale_info::122',
                    'fee': 'u128',
                    'issue_id': 'scale_info::12',
                    'requester': 'AccountId',
                    'vault_id': 'scale_info::140',
                },
                'IssueAmountChange': {
                    'amount': 'u128',
                    'asset': 'scale_info::122',
                    'confiscated_griefing_collateral': 'u128',
                    'fee': 'u128',
                    'issue_id': 'scale_info::12',
                },
                'IssueMinimumTransferAmountUpdate': {
                    'new_minimum_amount': 'u128',
                },
                'IssuePeriodChange': {'period': 'u32'},
                'RateLimitUpdate': {
                    'interval_length': 'u32',
                    'limit_volume_amount': (None, 'u128'),
                    'limit_volume_currency_id': 'scale_info::122',
                },
                'RequestIssue': {
                    'amount': 'u128',
                    'asset': 'scale_info::122',
                    'fee': 'u128',
                    'griefing_collateral': 'u128',
                    'issue_id': 'scale_info::12',
                    'requester': 'AccountId',
                    'vault_id': 'scale_info::140',
                    'vault_stellar_public_key': '[u8; 32]',
                },
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::49',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::49',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::42',
                    'timepoint': 'scale_info::49',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'Nomination': {
                'DepositCollateral': {
                    'amount': 'u128',
                    'nominator_id': 'AccountId',
                    'vault_id': 'scale_info::140',
                },
                'NominationOptIn': {'vault_id': 'scale_info::140'},
                'NominationOptOut': {'vault_id': 'scale_info::140'},
                'WithdrawCollateral': {
                    'amount': 'u128',
                    'nominator_id': 'AccountId',
                    'vault_id': 'scale_info::140',
                },
            },
            'Oracle': {
                'AggregateUpdated': {'values': [('scale_info::147', 'u128')]},
                'MaxDelayUpdated': {'max_delay': 'u64'},
                'OracleKeysUpdated': {'oracle_keys': ['scale_info::147']},
            },
            'ParachainStaking': {
                'BlocksPerRoundSet': ('u32', 'u32', 'u32', 'u32'),
                'CandidateLeft': ('AccountId', 'u128'),
                'CollatorCanceledExit': 'AccountId',
                'CollatorRemoved': ('AccountId', 'u128'),
                'CollatorScheduledExit': ('u32', 'AccountId', 'u32'),
                'CollatorStakedLess': ('AccountId', 'u128', 'u128'),
                'CollatorStakedMore': ('AccountId', 'u128', 'u128'),
                'Delegation': ('AccountId', 'u128', 'AccountId', 'u128'),
                'DelegationReplaced': (
                    'AccountId',
                    'u128',
                    'AccountId',
                    'u128',
                    'AccountId',
                    'u128',
                ),
                'DelegatorLeft': ('AccountId', 'u128'),
                'DelegatorLeftCollator': (
                    'AccountId',
                    'AccountId',
                    'u128',
                    'u128',
                ),
                'DelegatorStakedLess': (
                    'AccountId',
                    'AccountId',
                    'u128',
                    'u128',
                ),
                'DelegatorStakedMore': (
                    'AccountId',
                    'AccountId',
                    'u128',
                    'u128',
                ),
                'EnteredTopCandidates': 'AccountId',
                'JoinedCollatorCandidates': ('AccountId', 'u128'),
                'LeftTopCandidates': 'AccountId',
                'MaxCandidateStakeChanged': 'u128',
                'MaxSelectedCandidatesSet': ('u32', 'u32'),
                'NewRound': ('u32', 'u32'),
                'Rewarded': ('AccountId', 'u128'),
                'RoundInflationSet': ('u64', 'u64', 'u64', 'u64'),
            },
            'PolkadotXcm': {
                'AssetsClaimed': (
                    'scale_info::12',
                    'scale_info::64',
                    'scale_info::102',
                ),
                'AssetsTrapped': (
                    'scale_info::12',
                    'scale_info::64',
                    'scale_info::102',
                ),
                'Attempted': {
                    'Complete': 'scale_info::9',
                    'Error': 'scale_info::60',
                    'Incomplete': ('scale_info::9', 'scale_info::60'),
                },
                'FeesPaid': ('scale_info::64', ['scale_info::79']),
                'InvalidQuerier': (
                    'scale_info::64',
                    'u64',
                    'scale_info::64',
                    (None, 'scale_info::64'),
                ),
                'InvalidQuerierVersion': ('scale_info::64', 'u64'),
                'InvalidResponder': (
                    'scale_info::64',
                    'u64',
                    (None, 'scale_info::64'),
                ),
                'InvalidResponderVersion': ('scale_info::64', 'u64'),
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
                'NotifyTargetMigrationFail': ('scale_info::116', 'u64'),
                'NotifyTargetSendFail': (
                    'scale_info::64',
                    'u64',
                    'scale_info::60',
                ),
                'ResponseReady': ('u64', 'scale_info::85'),
                'ResponseTaken': 'u64',
                'Sent': (
                    'scale_info::64',
                    'scale_info::64',
                    ['scale_info::76'],
                ),
                'SupportedVersionChanged': ('scale_info::64', 'u32'),
                'UnexpectedResponse': ('scale_info::64', 'u64'),
                'VersionChangeNotified': (
                    'scale_info::64',
                    'u32',
                    ['scale_info::79'],
                ),
                'VersionNotifyRequested': (
                    'scale_info::64',
                    ['scale_info::79'],
                ),
                'VersionNotifyStarted': ('scale_info::64', ['scale_info::79']),
                'VersionNotifyUnrequested': (
                    'scale_info::64',
                    ['scale_info::79'],
                ),
            },
            'PooledVaultRewards': {
                'DepositStake': {
                    'amount': 'i128',
                    'pool_id': 'scale_info::122',
                    'stake_id': 'scale_info::140',
                },
                'DistributeReward': {
                    'amount': 'i128',
                    'currency_id': 'scale_info::122',
                },
                'WithdrawReward': {
                    'amount': 'i128',
                    'currency_id': 'scale_info::122',
                    'pool_id': 'scale_info::122',
                    'stake_id': 'scale_info::140',
                },
                'WithdrawStake': {
                    'amount': 'i128',
                    'pool_id': 'scale_info::122',
                    'stake_id': 'scale_info::140',
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
                    'proxy_type': 'scale_info::54',
                },
                'ProxyExecuted': {'result': 'scale_info::42'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::54',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::54',
                    'pure': 'AccountId',
                    'who': 'AccountId',
                },
            },
            'Redeem': {
                'CancelRedeem': {
                    'redeem_id': 'scale_info::12',
                    'redeemer': 'AccountId',
                    'slashed_amount': 'u128',
                    'status': 'scale_info::151',
                    'vault_id': 'scale_info::140',
                },
                'ExecuteRedeem': {
                    'amount': 'u128',
                    'asset': 'scale_info::122',
                    'fee': 'u128',
                    'redeem_id': 'scale_info::12',
                    'redeemer': 'AccountId',
                    'transfer_fee': 'u128',
                    'vault_id': 'scale_info::140',
                },
                'LiquidationRedeem': {
                    'amount': 'u128',
                    'asset': 'scale_info::122',
                    'redeemer': 'AccountId',
                },
                'MintTokensForReimbursedRedeem': {
                    'amount': 'u128',
                    'redeem_id': 'scale_info::12',
                    'vault_id': 'scale_info::140',
                },
                'RateLimitUpdate': {
                    'interval_length': 'u32',
                    'limit_volume_amount': (None, 'u128'),
                    'limit_volume_currency_id': 'scale_info::122',
                },
                'RedeemMinimumTransferAmountUpdate': {
                    'new_minimum_amount': 'u128',
                },
                'RedeemPeriodChange': {'period': 'u32'},
                'RequestRedeem': {
                    'amount': 'u128',
                    'asset': 'scale_info::122',
                    'fee': 'u128',
                    'premium': 'u128',
                    'redeem_id': 'scale_info::12',
                    'redeemer': 'AccountId',
                    'stellar_address': '[u8; 32]',
                    'transfer_fee': 'u128',
                    'vault_id': 'scale_info::140',
                },
                'SelfRedeem': {
                    'amount': 'u128',
                    'fee': 'u128',
                    'vault_id': 'scale_info::140',
                },
            },
            'Replace': {
                'AcceptReplace': {
                    'amount': 'u128',
                    'asset': 'scale_info::122',
                    'collateral': 'u128',
                    'new_vault_id': 'scale_info::140',
                    'old_vault_id': 'scale_info::140',
                    'replace_id': 'scale_info::12',
                    'stellar_address': '[u8; 32]',
                },
                'CancelReplace': {
                    'griefing_collateral': 'u128',
                    'new_vault_id': 'scale_info::140',
                    'old_vault_id': 'scale_info::140',
                    'replace_id': 'scale_info::12',
                },
                'ExecuteReplace': {
                    'new_vault_id': 'scale_info::140',
                    'old_vault_id': 'scale_info::140',
                    'replace_id': 'scale_info::12',
                },
                'ReplaceMinimumTransferAmountUpdate': {
                    'new_minimum_amount': 'u128',
                },
                'ReplacePeriodChange': {'period': 'u32'},
                'RequestReplace': {
                    'amount': 'u128',
                    'asset': 'scale_info::122',
                    'griefing_collateral': 'u128',
                    'old_vault_id': 'scale_info::140',
                },
                'WithdrawReplace': {
                    'asset': 'scale_info::122',
                    'old_vault_id': 'scale_info::140',
                    'withdrawn_griefing_collateral': 'u128',
                    'withdrawn_tokens': 'u128',
                },
            },
            'RewardDistribution': {'RewardPerBlockAdapted': 'u128'},
            'Scheduler': {
                'CallUnavailable': {
                    'id': (None, '[u8; 32]'),
                    'task': ('u32', 'u32'),
                },
                'Canceled': {'index': 'u32', 'when': 'u32'},
                'Dispatched': {
                    'id': (None, '[u8; 32]'),
                    'result': 'scale_info::42',
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
            'Security': {
                'RecoverFromErrors': {
                    'cleared_errors': ['scale_info::156'],
                    'new_status': 'scale_info::154',
                },
                'UpdateActiveBlock': {'block_number': 'u32'},
            },
            'Session': {'NewSession': {'session_index': 'u32'}},
            'StellarRelay': {
                'UpdateTier1ValidatorSet': {
                    'new_validators_enactment_block_height': 'u32',
                },
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
                    'result': 'scale_info::42',
                },
                'MemberExecuted': {
                    'proposal_hash': 'scale_info::12',
                    'result': 'scale_info::42',
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
            'TokenAllowance': {
                'AllowedCurrenciesAdded': {'currencies': ['scale_info::122']},
                'AllowedCurrenciesDeleted': {'currencies': ['scale_info::122']},
                'TransferApproved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::122',
                    'delegate': 'AccountId',
                    'source': 'AccountId',
                },
            },
            'Tokens': {
                'BalanceSet': {
                    'currency_id': 'scale_info::122',
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Deposited': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::122',
                    'who': 'AccountId',
                },
                'DustLost': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::122',
                    'who': 'AccountId',
                },
                'Endowed': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::122',
                    'who': 'AccountId',
                },
                'LockRemoved': {
                    'currency_id': 'scale_info::122',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'LockSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::122',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'Locked': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::122',
                    'who': 'AccountId',
                },
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::122',
                    'from': 'AccountId',
                    'status': 'scale_info::33',
                    'to': 'AccountId',
                },
                'Reserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::122',
                    'who': 'AccountId',
                },
                'Slashed': {
                    'currency_id': 'scale_info::122',
                    'free_amount': 'u128',
                    'reserved_amount': 'u128',
                    'who': 'AccountId',
                },
                'TotalIssuanceSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::122',
                },
                'Transfer': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::122',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unlocked': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::122',
                    'who': 'AccountId',
                },
                'Unreserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::122',
                    'who': 'AccountId',
                },
                'Withdrawn': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::122',
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
            'TreasuryBuyoutExtension': {
                'AllowedAssetsForBuyoutUpdated': {
                    'allowed_assets': ['scale_info::122'],
                },
                'Buyout': {
                    'asset': 'scale_info::122',
                    'buyout_amount': 'u128',
                    'exchange_amount': 'u128',
                    'who': 'AccountId',
                },
                'BuyoutLimitUpdated': {'limit': (None, 'u128')},
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::25',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::42'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::25'},
            },
            'VaultRegistry': {
                'BanVault': {
                    'banned_until': 'u32',
                    'vault_id': 'scale_info::140',
                },
                'DecreaseLockedCollateral': {
                    'currency_pair': 'scale_info::141',
                    'delta': 'u128',
                    'total': 'u128',
                },
                'DecreaseToBeIssuedTokens': {
                    'decrease': 'u128',
                    'vault_id': 'scale_info::140',
                },
                'DecreaseToBeRedeemedTokens': {
                    'decrease': 'u128',
                    'vault_id': 'scale_info::140',
                },
                'DecreaseToBeReplacedTokens': {
                    'decrease': 'u128',
                    'vault_id': 'scale_info::140',
                },
                'DecreaseTokens': {
                    'decrease': 'u128',
                    'user_id': 'AccountId',
                    'vault_id': 'scale_info::140',
                },
                'DepositCollateral': {
                    'free_collateral': 'u128',
                    'new_collateral': 'u128',
                    'total_collateral': 'u128',
                    'vault_id': 'scale_info::140',
                },
                'IncreaseLockedCollateral': {
                    'currency_pair': 'scale_info::141',
                    'delta': 'u128',
                    'total': 'u128',
                },
                'IncreaseToBeIssuedTokens': {
                    'increase': 'u128',
                    'vault_id': 'scale_info::140',
                },
                'IncreaseToBeRedeemedTokens': {
                    'increase': 'u128',
                    'vault_id': 'scale_info::140',
                },
                'IncreaseToBeReplacedTokens': {
                    'increase': 'u128',
                    'vault_id': 'scale_info::140',
                },
                'IssueTokens': {
                    'increase': 'u128',
                    'vault_id': 'scale_info::140',
                },
                'LiquidateVault': {
                    'backing_collateral': 'u128',
                    'issued_tokens': 'u128',
                    'replace_collateral': 'u128',
                    'status': 'scale_info::159',
                    'to_be_issued_tokens': 'u128',
                    'to_be_redeemed_tokens': 'u128',
                    'to_be_replaced_tokens': 'u128',
                    'vault_id': 'scale_info::140',
                },
                'RedeemTokens': {
                    'redeemed_amount': 'u128',
                    'vault_id': 'scale_info::140',
                },
                'RedeemTokensLiquidatedVault': {
                    'collateral': 'u128',
                    'tokens': 'u128',
                    'vault_id': 'scale_info::140',
                },
                'RedeemTokensLiquidation': {
                    'burned_tokens': 'u128',
                    'redeemer_id': 'AccountId',
                    'transferred_collateral': 'u128',
                },
                'RedeemTokensPremium': {
                    'collateral': 'u128',
                    'redeemed_amount': 'u128',
                    'user_id': 'AccountId',
                    'vault_id': 'scale_info::140',
                },
                'RegisterAddress': {
                    'address': '[u8; 32]',
                    'vault_id': 'scale_info::140',
                },
                'RegisterVault': {
                    'collateral': 'u128',
                    'vault_id': 'scale_info::140',
                },
                'ReplaceTokens': {
                    'additional_collateral': 'u128',
                    'amount': 'u128',
                    'new_vault_id': 'scale_info::140',
                    'old_vault_id': 'scale_info::140',
                },
                'UpdatePublicKey': {
                    'account_id': 'AccountId',
                    'public_key': '[u8; 32]',
                },
                'WithdrawCollateral': {
                    'total_collateral': 'u128',
                    'vault_id': 'scale_info::140',
                    'withdrawn_amount': 'u128',
                },
            },
            'VaultStaking': {
                'DepositStake': {
                    'amount': 'i128',
                    'nominator_id': 'AccountId',
                    'vault_id': 'scale_info::140',
                },
                'DistributeReward': {
                    'amount': 'i128',
                    'currency_id': 'scale_info::122',
                    'vault_id': 'scale_info::140',
                },
                'ForceRefund': {'vault_id': 'scale_info::140'},
                'IncreaseNonce': {
                    'new_nonce': 'u32',
                    'vault_id': 'scale_info::140',
                },
                'WithdrawReward': {
                    'amount': 'i128',
                    'currency_id': 'scale_info::122',
                    'nominator_id': 'AccountId',
                    'nonce': 'u32',
                    'vault_id': 'scale_info::140',
                },
                'WithdrawStake': {
                    'amount': 'i128',
                    'nominator_id': 'AccountId',
                    'vault_id': 'scale_info::140',
                },
            },
            'Vesting': {
                'VestingCompleted': {'account': 'AccountId'},
                'VestingUpdated': {'account': 'AccountId', 'unvested': 'u128'},
            },
            'VestingManager': {
                'VestingScheduleRemoved': {
                    'schedule_index': 'u32',
                    'who': 'AccountId',
                },
            },
            'XTokens': {
                'TransferredMultiAssets': {
                    'assets': ['scale_info::79'],
                    'dest': 'scale_info::64',
                    'fee': 'scale_info::79',
                    'sender': 'AccountId',
                },
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': (None, '[u8; 32]')},
                'BadVersion': {'message_hash': (None, '[u8; 32]')},
                'Fail': {
                    'error': 'scale_info::60',
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
                    ['scale_info::134'],
                    ['u128'],
                ),
                'BootstrapClaim': (
                    'AccountId',
                    'AccountId',
                    'AccountId',
                    'scale_info::134',
                    'scale_info::134',
                    'u128',
                    'u128',
                    'u128',
                ),
                'BootstrapContribute': (
                    'AccountId',
                    'scale_info::134',
                    'u128',
                    'scale_info::134',
                    'u128',
                ),
                'BootstrapCreated': (
                    'AccountId',
                    'scale_info::134',
                    'scale_info::134',
                    'u128',
                    'u128',
                    'u128',
                    'u128',
                    'u32',
                ),
                'BootstrapEnd': (
                    'scale_info::134',
                    'scale_info::134',
                    'u128',
                    'u128',
                    'u128',
                ),
                'BootstrapRefund': (
                    'AccountId',
                    'AccountId',
                    'scale_info::134',
                    'scale_info::134',
                    'u128',
                    'u128',
                ),
                'BootstrapUpdate': (
                    'AccountId',
                    'scale_info::134',
                    'scale_info::134',
                    'u128',
                    'u128',
                    'u128',
                    'u128',
                    'u32',
                ),
                'Burned': ('scale_info::134', 'AccountId', 'u128'),
                'ChargeReward': (
                    'scale_info::134',
                    'scale_info::134',
                    'AccountId',
                    [('scale_info::134', 'u128')],
                ),
                'DistributeReward': (
                    'scale_info::134',
                    'scale_info::134',
                    'AccountId',
                    [('scale_info::134', 'u128')],
                ),
                'LiquidityAdded': (
                    'AccountId',
                    'scale_info::134',
                    'scale_info::134',
                    'u128',
                    'u128',
                    'u128',
                ),
                'LiquidityRemoved': (
                    'AccountId',
                    'AccountId',
                    'scale_info::134',
                    'scale_info::134',
                    'u128',
                    'u128',
                    'u128',
                ),
                'Minted': ('scale_info::134', 'AccountId', 'u128'),
                'PairCreated': ('scale_info::134', 'scale_info::134'),
                'Transferred': (
                    'scale_info::134',
                    'AccountId',
                    'AccountId',
                    'u128',
                ),
                'TransferredToParachain': (
                    'scale_info::134',
                    'AccountId',
                    'u32',
                    'AccountId',
                    'u128',
                    'u64',
                ),
                'WithdrawReward': (
                    'scale_info::134',
                    'scale_info::134',
                    'AccountId',
                ),
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
57
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
        ('0xea93e3f16f3d6962', 2),
        ('0xfb74f0e21eea131a', 1),
        ('0x53699d721098ded3', 1),
        ('0x60aed43cb52456f1', 1),
        ('0x0d94b80c178630f0', 1),
        ('0xcaf39b979a6880bd', 1),
        ('0x16da96d36c6d5bb7', 1),
        ('0x69e2e1aa421f4fb0', 1),
        ('0x2be5cb02b0a56e73', 1),
        ('0x68b66ba122c93fa7', 2),
        ('0x6ef953004ba30e59', 1),
    ],
    'authoring_version': 1,
    'impl_name': 'amplitude',
    'impl_version': 0,
    'spec_name': 'amplitude',
    'spec_version': 15,
    'state_version': 1,
    'transaction_version': 13,
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