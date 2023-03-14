
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
                    'destination_status': 'scale_info::31',
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
            'Contracts': {
                'Called': {'caller': 'AccountId', 'contract': 'AccountId'},
                'CodeRemoved': {'code_hash': '[u8; 32]'},
                'CodeStored': {'code_hash': '[u8; 32]'},
                'ContractCodeUpdated': {
                    'contract': 'AccountId',
                    'new_code_hash': '[u8; 32]',
                    'old_code_hash': '[u8; 32]',
                },
                'ContractEmitted': {'contract': 'AccountId', 'data': 'Bytes'},
                'DelegateCalled': {
                    'code_hash': '[u8; 32]',
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
                'Approved': {'proposal_hash': '[u8; 32]'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': '[u8; 32]'},
                'Executed': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::39',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::39',
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
                'ExecutedDownward': ('[u8; 8]', 'scale_info::59'),
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
                'Started': {'ref_index': 'u32', 'threshold': 'scale_info::34'},
                'Tabled': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Undelegated': {'account': 'AccountId'},
                'Vetoed': {
                    'proposal_hash': '[u8; 32]',
                    'until': 'u32',
                    'who': 'AccountId',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::35',
                    'voter': 'AccountId',
                },
            },
            'DiaOracleModule': {
                'AccountIdAuthorized': 'AccountId',
                'AccountIdDeauthorized': 'AccountId',
                'BatchingApiRouteSet': 'Bytes',
                'CurrencyAdded': ('Bytes', 'Bytes'),
                'CurrencyRemoved': ('Bytes', 'Bytes'),
                'UpdatedPrices': [(('Bytes', 'Bytes'), 'scale_info::112')],
            },
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::59',
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
                    'issue_id': '[u8; 32]',
                    'requester': 'AccountId',
                },
                'ExecuteIssue': {
                    'amount': 'u128',
                    'asset': 'scale_info::102',
                    'fee': 'u128',
                    'issue_id': '[u8; 32]',
                    'requester': 'AccountId',
                    'vault_id': 'scale_info::120',
                },
                'IssueAmountChange': {
                    'amount': 'u128',
                    'asset': 'scale_info::102',
                    'confiscated_griefing_collateral': 'u128',
                    'fee': 'u128',
                    'issue_id': '[u8; 32]',
                },
                'IssueMinimumTransferAmountUpdate': {
                    'new_minimum_amount': 'u128',
                },
                'IssuePeriodChange': {'period': 'u32'},
                'RateLimitUpdate': {
                    'interval_length': 'u32',
                    'limit_volume_amount': (None, 'u128'),
                    'limit_volume_currency_id': 'scale_info::102',
                },
                'RequestIssue': {
                    'amount': 'u128',
                    'asset': 'scale_info::102',
                    'fee': 'u128',
                    'griefing_collateral': 'u128',
                    'issue_id': '[u8; 32]',
                    'requester': 'AccountId',
                    'vault_id': 'scale_info::120',
                    'vault_stellar_public_key': '[u8; 32]',
                },
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::47',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::47',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::39',
                    'timepoint': 'scale_info::47',
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
                    'vault_id': 'scale_info::120',
                },
                'NominationOptIn': {'vault_id': 'scale_info::120'},
                'NominationOptOut': {'vault_id': 'scale_info::120'},
                'WithdrawCollateral': {
                    'amount': 'u128',
                    'nominator_id': 'AccountId',
                    'vault_id': 'scale_info::120',
                },
            },
            'Oracle': {
                'AggregateUpdated': {'values': [('scale_info::127', 'u128')]},
                'MaxDelayUpdated': {'max_delay': 'u64'},
                'OracleKeysUpdated': {'oracle_keys': ['scale_info::127']},
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
                    'scale_info::60',
                    'scale_info::91',
                ),
                'AssetsTrapped': (
                    '[u8; 32]',
                    'scale_info::60',
                    'scale_info::91',
                ),
                'Attempted': {
                    'Complete': 'u64',
                    'Error': 'scale_info::56',
                    'Incomplete': ('u64', 'scale_info::56'),
                },
                'InvalidResponder': (
                    'scale_info::60',
                    'u64',
                    (None, 'scale_info::60'),
                ),
                'InvalidResponderVersion': ('scale_info::60', 'u64'),
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
                'NotifyTargetMigrationFail': ('scale_info::96', 'u64'),
                'NotifyTargetSendFail': (
                    'scale_info::60',
                    'u64',
                    'scale_info::56',
                ),
                'ResponseReady': ('u64', 'scale_info::81'),
                'ResponseTaken': 'u64',
                'Sent': (
                    'scale_info::60',
                    'scale_info::60',
                    ['scale_info::72'],
                ),
                'SupportedVersionChanged': ('scale_info::60', 'u32'),
                'UnexpectedResponse': ('scale_info::60', 'u64'),
                'VersionChangeNotified': ('scale_info::60', 'u32'),
            },
            'Preimage': {
                'Cleared': {'hash': '[u8; 32]'},
                'Noted': {'hash': '[u8; 32]'},
                'Requested': {'hash': '[u8; 32]'},
            },
            'Redeem': {
                'CancelRedeem': {
                    'redeem_id': '[u8; 32]',
                    'redeemer': 'AccountId',
                    'slashed_amount': 'u128',
                    'status': 'scale_info::131',
                    'vault_id': 'scale_info::120',
                },
                'ExecuteRedeem': {
                    'amount': 'u128',
                    'asset': 'scale_info::102',
                    'fee': 'u128',
                    'redeem_id': '[u8; 32]',
                    'redeemer': 'AccountId',
                    'transfer_fee': 'u128',
                    'vault_id': 'scale_info::120',
                },
                'LiquidationRedeem': {
                    'amount': 'u128',
                    'asset': 'scale_info::102',
                    'redeemer': 'AccountId',
                },
                'MintTokensForReimbursedRedeem': {
                    'amount': 'u128',
                    'redeem_id': '[u8; 32]',
                    'vault_id': 'scale_info::120',
                },
                'RateLimitUpdate': {
                    'interval_length': 'u32',
                    'limit_volume_amount': (None, 'u128'),
                    'limit_volume_currency_id': 'scale_info::102',
                },
                'RedeemMinimumTransferAmountUpdate': {
                    'new_minimum_amount': 'u128',
                },
                'RedeemPeriodChange': {'period': 'u32'},
                'RequestRedeem': {
                    'amount': 'u128',
                    'asset': 'scale_info::102',
                    'fee': 'u128',
                    'premium': 'u128',
                    'redeem_id': '[u8; 32]',
                    'redeemer': 'AccountId',
                    'stellar_address': '[u8; 32]',
                    'transfer_fee': 'u128',
                    'vault_id': 'scale_info::120',
                },
                'SelfRedeem': {
                    'amount': 'u128',
                    'fee': 'u128',
                    'vault_id': 'scale_info::120',
                },
            },
            'Replace': {
                'AcceptReplace': {
                    'amount': 'u128',
                    'asset': 'scale_info::102',
                    'collateral': 'u128',
                    'new_vault_id': 'scale_info::120',
                    'old_vault_id': 'scale_info::120',
                    'replace_id': '[u8; 32]',
                    'stellar_address': '[u8; 32]',
                },
                'CancelReplace': {
                    'griefing_collateral': 'u128',
                    'new_vault_id': 'scale_info::120',
                    'old_vault_id': 'scale_info::120',
                    'replace_id': '[u8; 32]',
                },
                'ExecuteReplace': {
                    'new_vault_id': 'scale_info::120',
                    'old_vault_id': 'scale_info::120',
                    'replace_id': '[u8; 32]',
                },
                'ReplaceMinimumTransferAmountUpdate': {
                    'new_minimum_amount': 'u128',
                },
                'ReplacePeriodChange': {'period': 'u32'},
                'RequestReplace': {
                    'amount': 'u128',
                    'asset': 'scale_info::102',
                    'griefing_collateral': 'u128',
                    'old_vault_id': 'scale_info::120',
                },
                'WithdrawReplace': {
                    'asset': 'scale_info::102',
                    'old_vault_id': 'scale_info::120',
                    'withdrawn_griefing_collateral': 'u128',
                    'withdrawn_tokens': 'u128',
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
                    'result': 'scale_info::39',
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
                    'cleared_errors': ['scale_info::136'],
                    'new_status': 'scale_info::134',
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
                    'dispatch_error': 'scale_info::24',
                    'dispatch_info': 'scale_info::21',
                },
                'ExtrinsicSuccess': {'dispatch_info': 'scale_info::21'},
                'KilledAccount': {'account': 'AccountId'},
                'NewAccount': {'account': 'AccountId'},
                'Remarked': {'hash': '[u8; 32]', 'sender': 'AccountId'},
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
                    'result': 'scale_info::39',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::39',
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
            'Tokens': {
                'BalanceSet': {
                    'currency_id': 'scale_info::102',
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Deposited': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::102',
                    'who': 'AccountId',
                },
                'DustLost': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::102',
                    'who': 'AccountId',
                },
                'Endowed': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::102',
                    'who': 'AccountId',
                },
                'LockRemoved': {
                    'currency_id': 'scale_info::102',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'LockSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::102',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::102',
                    'from': 'AccountId',
                    'status': 'scale_info::31',
                    'to': 'AccountId',
                },
                'Reserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::102',
                    'who': 'AccountId',
                },
                'Slashed': {
                    'currency_id': 'scale_info::102',
                    'free_amount': 'u128',
                    'reserved_amount': 'u128',
                    'who': 'AccountId',
                },
                'TotalIssuanceSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::102',
                },
                'Transfer': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::102',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unreserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::102',
                    'who': 'AccountId',
                },
                'Withdrawn': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::102',
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
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::24',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::39'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::24'},
            },
            'VaultRegistry': {
                'BanVault': {
                    'banned_until': 'u32',
                    'vault_id': 'scale_info::120',
                },
                'DecreaseLockedCollateral': {
                    'currency_pair': 'scale_info::121',
                    'delta': 'u128',
                    'total': 'u128',
                },
                'DecreaseToBeIssuedTokens': {
                    'decrease': 'u128',
                    'vault_id': 'scale_info::120',
                },
                'DecreaseToBeRedeemedTokens': {
                    'decrease': 'u128',
                    'vault_id': 'scale_info::120',
                },
                'DecreaseToBeReplacedTokens': {
                    'decrease': 'u128',
                    'vault_id': 'scale_info::120',
                },
                'DecreaseTokens': {
                    'decrease': 'u128',
                    'user_id': 'AccountId',
                    'vault_id': 'scale_info::120',
                },
                'DepositCollateral': {
                    'free_collateral': 'u128',
                    'new_collateral': 'u128',
                    'total_collateral': 'u128',
                    'vault_id': 'scale_info::120',
                },
                'IncreaseLockedCollateral': {
                    'currency_pair': 'scale_info::121',
                    'delta': 'u128',
                    'total': 'u128',
                },
                'IncreaseToBeIssuedTokens': {
                    'increase': 'u128',
                    'vault_id': 'scale_info::120',
                },
                'IncreaseToBeRedeemedTokens': {
                    'increase': 'u128',
                    'vault_id': 'scale_info::120',
                },
                'IncreaseToBeReplacedTokens': {
                    'increase': 'u128',
                    'vault_id': 'scale_info::120',
                },
                'IssueTokens': {
                    'increase': 'u128',
                    'vault_id': 'scale_info::120',
                },
                'LiquidateVault': {
                    'backing_collateral': 'u128',
                    'issued_tokens': 'u128',
                    'replace_collateral': 'u128',
                    'status': 'scale_info::139',
                    'to_be_issued_tokens': 'u128',
                    'to_be_redeemed_tokens': 'u128',
                    'to_be_replaced_tokens': 'u128',
                    'vault_id': 'scale_info::120',
                },
                'RedeemTokens': {
                    'redeemed_amount': 'u128',
                    'vault_id': 'scale_info::120',
                },
                'RedeemTokensLiquidatedVault': {
                    'collateral': 'u128',
                    'tokens': 'u128',
                    'vault_id': 'scale_info::120',
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
                    'vault_id': 'scale_info::120',
                },
                'RegisterAddress': {
                    'address': '[u8; 32]',
                    'vault_id': 'scale_info::120',
                },
                'RegisterVault': {
                    'collateral': 'u128',
                    'vault_id': 'scale_info::120',
                },
                'ReplaceTokens': {
                    'additional_collateral': 'u128',
                    'amount': 'u128',
                    'new_vault_id': 'scale_info::120',
                    'old_vault_id': 'scale_info::120',
                },
                'UpdatePublicKey': {
                    'account_id': 'AccountId',
                    'public_key': '[u8; 32]',
                },
                'WithdrawCollateral': {
                    'total_collateral': 'u128',
                    'vault_id': 'scale_info::120',
                    'withdrawn_amount': 'u128',
                },
            },
            'VaultRewards': {
                'DepositStake': {
                    'amount': 'i128',
                    'reward_id': 'scale_info::120',
                },
                'DistributeReward': {
                    'amount': 'i128',
                    'currency_id': 'scale_info::102',
                },
                'WithdrawReward': {
                    'amount': 'i128',
                    'currency_id': 'scale_info::102',
                    'reward_id': 'scale_info::120',
                },
                'WithdrawStake': {
                    'amount': 'i128',
                    'reward_id': 'scale_info::120',
                },
            },
            'VaultStaking': {
                'DepositStake': {
                    'amount': 'i128',
                    'nominator_id': 'AccountId',
                    'vault_id': 'scale_info::120',
                },
                'DistributeReward': {
                    'amount': 'i128',
                    'currency_id': 'scale_info::102',
                    'vault_id': 'scale_info::120',
                },
                'ForceRefund': {'vault_id': 'scale_info::120'},
                'IncreaseNonce': {
                    'new_nonce': 'u32',
                    'vault_id': 'scale_info::120',
                },
                'WithdrawReward': {
                    'amount': 'i128',
                    'currency_id': 'scale_info::102',
                    'nominator_id': 'AccountId',
                    'nonce': 'u32',
                    'vault_id': 'scale_info::120',
                },
                'WithdrawStake': {
                    'amount': 'i128',
                    'nominator_id': 'AccountId',
                    'vault_id': 'scale_info::120',
                },
            },
            'Vesting': {
                'VestingCompleted': {'account': 'AccountId'},
                'VestingUpdated': {'account': 'AccountId', 'unvested': 'u128'},
            },
            'XTokens': {
                'TransferredMultiAssets': {
                    'assets': ['scale_info::75'],
                    'dest': 'scale_info::60',
                    'fee': 'scale_info::75',
                    'sender': 'AccountId',
                },
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': (None, '[u8; 32]')},
                'BadVersion': {'message_hash': (None, '[u8; 32]')},
                'Fail': {
                    'error': 'scale_info::56',
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
                    ['scale_info::114'],
                    ['u128'],
                ),
                'BootstrapClaim': (
                    'AccountId',
                    'AccountId',
                    'AccountId',
                    'scale_info::114',
                    'scale_info::114',
                    'u128',
                    'u128',
                    'u128',
                ),
                'BootstrapContribute': (
                    'AccountId',
                    'scale_info::114',
                    'u128',
                    'scale_info::114',
                    'u128',
                ),
                'BootstrapCreated': (
                    'AccountId',
                    'scale_info::114',
                    'scale_info::114',
                    'u128',
                    'u128',
                    'u128',
                    'u128',
                    'u32',
                ),
                'BootstrapEnd': (
                    'scale_info::114',
                    'scale_info::114',
                    'u128',
                    'u128',
                    'u128',
                ),
                'BootstrapRefund': (
                    'AccountId',
                    'AccountId',
                    'scale_info::114',
                    'scale_info::114',
                    'u128',
                    'u128',
                ),
                'BootstrapUpdate': (
                    'AccountId',
                    'scale_info::114',
                    'scale_info::114',
                    'u128',
                    'u128',
                    'u128',
                    'u128',
                    'u32',
                ),
                'Burned': ('scale_info::114', 'AccountId', 'u128'),
                'ChargeReward': (
                    'scale_info::114',
                    'scale_info::114',
                    'AccountId',
                    [('scale_info::114', 'u128')],
                ),
                'DistributeReward': (
                    'scale_info::114',
                    'scale_info::114',
                    'AccountId',
                    [('scale_info::114', 'u128')],
                ),
                'LiquidityAdded': (
                    'AccountId',
                    'scale_info::114',
                    'scale_info::114',
                    'u128',
                    'u128',
                    'u128',
                ),
                'LiquidityRemoved': (
                    'AccountId',
                    'AccountId',
                    'scale_info::114',
                    'scale_info::114',
                    'u128',
                    'u128',
                    'u128',
                ),
                'Minted': ('scale_info::114', 'AccountId', 'u128'),
                'PairCreated': ('scale_info::114', 'scale_info::114'),
                'Transferred': (
                    'scale_info::114',
                    'AccountId',
                    'AccountId',
                    'u128',
                ),
                'TransferredToParachain': (
                    'scale_info::114',
                    'AccountId',
                    'u32',
                    'AccountId',
                    'u128',
                    'u64',
                ),
                'WithdrawReward': (
                    'scale_info::114',
                    'scale_info::114',
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
        ('0x37e397fc7c91f5e4', 1),
        ('0x40fe3ad401f8959a', 6),
        ('0xd2bc9897eed08f15', 3),
        ('0xf78b278be53f454c', 2),
        ('0xab3c0572291feb8b', 1),
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 2),
        ('0xea93e3f16f3d6962', 2),
        ('0xfb74f0e21eea131a', 1),
        ('0x53699d721098ded3', 1),
        ('0x60aed43cb52456f1', 1),
        ('0xcaf39b979a6880bd', 1),
        ('0x16da96d36c6d5bb7', 1),
        ('0x69e2e1aa421f4fb0', 1),
        ('0x2be5cb02b0a56e73', 1),
    ],
    'authoring_version': 1,
    'impl_name': 'amplitude',
    'impl_version': 0,
    'spec_name': 'amplitude',
    'spec_version': 8,
    'state_version': 1,
    'transaction_version': 8,
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