
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
| dispatch_error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}```
| dispatch_info | `DispatchInfo` | ```{'weight': 'u64', 'class': ('Normal', 'Operational', 'Mandatory'), 'pays_fee': ('Yes', 'No')}```

---------
### ExtrinsicSuccess
An extrinsic completed successfully.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispatch_info | `DispatchInfo` | ```{'weight': 'u64', 'class': ('Normal', 'Operational', 'Mandatory'), 'pays_fee': ('Yes', 'No')}```

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
{'mandatory': 'u64', 'normal': 'u64', 'operational': 'u64'}
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
            'AMM': {
                'LiquidityAdded': (
                    'AccountId',
                    'u32',
                    'u32',
                    'u32',
                    'u128',
                    'u128',
                ),
                'LiquidityRemoved': ('AccountId', 'u32', 'u32', 'u32', 'u128'),
                'Swapped': ('AccountId', ['u32'], 'u128', 'u128'),
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
            'Democracy': {
                'Blacklisted': {'proposal_hash': '[u8; 32]'},
                'Cancelled': {'ref_index': 'u32'},
                'Delegated': {'target': 'AccountId', 'who': 'AccountId'},
                'Executed': {'ref_index': 'u32', 'result': 'scale_info::29'},
                'ExternalTabled': None,
                'NotPassed': {'ref_index': 'u32'},
                'Passed': {'ref_index': 'u32'},
                'PreimageInvalid': {
                    'proposal_hash': '[u8; 32]',
                    'ref_index': 'u32',
                },
                'PreimageMissing': {
                    'proposal_hash': '[u8; 32]',
                    'ref_index': 'u32',
                },
                'PreimageNoted': {
                    'deposit': 'u128',
                    'proposal_hash': '[u8; 32]',
                    'who': 'AccountId',
                },
                'PreimageReaped': {
                    'deposit': 'u128',
                    'proposal_hash': '[u8; 32]',
                    'provider': 'AccountId',
                    'reaper': 'AccountId',
                },
                'PreimageUsed': {
                    'deposit': 'u128',
                    'proposal_hash': '[u8; 32]',
                    'provider': 'AccountId',
                },
                'ProposalCanceled': {'prop_index': 'u32'},
                'Proposed': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Seconded': {'prop_index': 'u32', 'seconder': 'AccountId'},
                'Started': {'ref_index': 'u32', 'threshold': 'scale_info::41'},
                'Tabled': {
                    'deposit': 'u128',
                    'depositors': ['AccountId'],
                    'proposal_index': 'u32',
                },
                'Undelegated': {'account': 'AccountId'},
                'Vetoed': {
                    'proposal_hash': '[u8; 32]',
                    'until': 'u32',
                    'who': 'AccountId',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::42',
                    'voter': 'AccountId',
                },
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::28',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::28',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::29',
                    'timepoint': 'scale_info::28',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            None: None,
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
                    'destination_status': 'scale_info::34',
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
                    'result': 'scale_info::29',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::29',
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
            'CreateDao': {
                'CreatedDao': ('AccountId', 'u64', 'scale_info::105'),
                'SomethingStored': ('u32', 'AccountId'),
            },
            'CumulusXcm': {
                'ExecutedDownward': ('[u8; 8]', 'scale_info::92'),
                'InvalidFormat': '[u8; 8]',
                'UnsupportedVersion': '[u8; 8]',
            },
            'Currencies': {
                'BalanceUpdated': ('u32', 'AccountId', 'i128'),
                'Burn': ('AccountId', 'u32', 'u128'),
                'CreateAsset': ('AccountId', 'u32', 'u128'),
                'Deposited': ('u32', 'AccountId', 'u128'),
                'ForceSetLocation': {
                    'currency_id': 'u32',
                    'location': 'scale_info::59',
                },
                'SetExistenialDepposit': {
                    'currency_id': 'u32',
                    'existenial_deposit': 'u128',
                },
                'SetLocation': {
                    'currency_id': 'u32',
                    'location': 'scale_info::59',
                },
                'SetMetadata': ('AccountId', 'u32', 'scale_info::273'),
                'SetWeightRateMultiple': {
                    'currency_id': 'u32',
                    'multiple': 'u128',
                },
                'Transferred': ('u32', 'AccountId', 'AccountId', 'u128'),
                'Withdrawn': ('u32', 'AccountId', 'u128'),
            },
            'Dao': {
                'Approved': '[u8; 32]',
                'Closed': ('[u8; 32]', 'u128', 'u128'),
                'Disapproved': '[u8; 32]',
                'Executed': ('[u8; 32]', 'scale_info::29'),
                'MemberExecuted': ('[u8; 32]', 'scale_info::29'),
                'Proposed': ('AccountId', 'u32', '[u8; 32]', 'u8'),
                'Voted': (
                    'AccountId',
                    '[u8; 32]',
                    'bool',
                    'u128',
                    'u128',
                    'u128',
                ),
            },
            'DaoCollective': {
                'Approved': {'proposal_hash': '[u8; 32]'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': '[u8; 32]'},
                'DoAsDone': {'sudo_result': 'scale_info::29'},
                'Executed': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::29',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::29',
                },
                'Proposed': {
                    'account': 'AccountId',
                    'proposal_hash': '[u8; 32]',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'SetEnsure': ('u64', 'u32', 'scale_info::108'),
                'SetMaxMembers': {'dao_id': 'u64', 'max': 'u32'},
                'SetMaxProposals': {'dao_id': 'u64', 'max': 'u32'},
                'SetMotionDuration': {'dao_id': 'u64', 'duration': 'u32'},
                'Voted': {
                    'account': 'AccountId',
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'voted': 'bool',
                    'yes': 'u32',
                },
            },
            'DaoDemocracy': {
                'CancelVote': ('u64', 'u32'),
                'EnactProposal': {
                    'dao_id': 'u64',
                    'index': 'u32',
                    'result': 'scale_info::29',
                },
                'Proposed': ('u64', '[u8; 32]'),
                'Second': ('u64', 'u128'),
                'SetEnactmentPeriod': {'dao_id': 'u64', 'period': 'u32'},
                'SetLaunchPeriod': {'dao_id': 'u64', 'period': 'u32'},
                'SetMaxPublicProps': {'dao_id': 'u64', 'max': 'u32'},
                'SetMinVoteWeight': ('u64', 'u32', 'u128'),
                'SetMinimumDeposit': {'dao_id': 'u64', 'min': 'u128'},
                'SetReservePeriod': {'dao_id': 'u64', 'period': 'u32'},
                'SetVotingPeriod': {'dao_id': 'u64', 'period': 'u32'},
                'StartTable': ('u64', 'u32'),
                'Unlock': ('AccountId', 'scale_info::105', 'scale_info::241'),
                'Unreserved': ('AccountId', 'u128'),
                'Vote': ('u64', 'u32', 'scale_info::241'),
            },
            'DaoSudo': {
                'CloseSudo': {'dao_id': 'u64', 'is_close': 'bool'},
                'SetSudoAccount': {
                    'dao_id': 'u64',
                    'sudo_account': 'AccountId',
                },
                'SudoDone': {
                    'sudo': 'AccountId',
                    'sudo_result': 'scale_info::29',
                },
            },
            'DicoOracle': {
                'NewFeedData': ('AccountId', [('u32', 'u128')], 'u64'),
                'NewLockedPrice': ('u32', 'u128'),
                'UnLockedPrice': 'u32',
            },
            'DicoTreasury': {
                'Approved': 'u32',
                'Awarded': ('u32', 'u128', 'AccountId'),
                'Burnt': 'u128',
                'Deposit': 'u128',
                'Proposed': 'u32',
                'Rejected': ('u32', 'u128'),
                'Rollover': 'u128',
                'SpendFund': None,
                'Spending': 'u128',
            },
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::92',
                },
                'InvalidFormat': {'message_id': '[u8; 32]'},
                'OverweightEnqueued': {
                    'message_id': '[u8; 32]',
                    'overweight_index': 'u64',
                    'required_weight': 'u64',
                },
                'OverweightServiced': {
                    'overweight_index': 'u64',
                    'weight_used': 'u64',
                },
                'UnsupportedVersion': {'message_id': '[u8; 32]'},
                'WeightExhausted': {
                    'message_id': '[u8; 32]',
                    'remaining_weight': 'u64',
                    'required_weight': 'u64',
                },
            },
            'DoAs': {
                'DoAsDone': {'sudo_result': 'scale_info::29'},
                'SetEnsure': ('u64', 'u32', 'scale_info::108'),
            },
            'Farm': {
                'DicoPerBlockIsSet': 'u128',
                'HalvingPeriodIsSet': 'u32',
                'LpDeposited': ('AccountId', 'u32', 'u128'),
                'LpWithdrawn': ('AccountId', 'u32', 'u128'),
                'PoolAllocPointUpdated': ('u32', 'u128'),
                'PoolCreated': 'u32',
                'StartBlockIsSet': 'u32',
            },
            'FarmExtend': {
                'AssetDeposited': ('AccountId', 'u32', 'u128'),
                'AssetWithdrawn': ('AccountId', 'u32', 'u128'),
                'PoolExtendCreated': (
                    'AccountId',
                    'u32',
                    'u32',
                    'u128',
                    'u32',
                ),
            },
            'Ico': {
                'CancelRequest': ('u32', 'u32'),
                'GetReward': ('u32', 'u32', 'AccountId', 'u128'),
                'InitiateIco': ('AccountId', 'u32', 'u128'),
                'InitiatorSetIcoAmountBound': ('u32', 'u32', 'u128', 'u128'),
                'Join': ('AccountId', 'u32', 'u32', 'u128', 'u128'),
                'PermitIco': ('AccountId', 'u32'),
                'PermitRelease': ('u32', 'u32', 'scale_info::281'),
                'RejectIco': ('AccountId', 'u32'),
                'RequestRelease': ('u32', 'u32', 'u8'),
                'SetAssetPowerMultiple': ('u32', 'scale_info::261'),
                'SetIcoMaxCount': ('u32', 'u32', 'u8'),
                'SetSystemIcoAmountBound': ('u128', 'u128'),
                'TerminateIco': ('u32', 'u32'),
                'TerminatedGiveBackAmount': (
                    'AccountId',
                    'u32',
                    'u32',
                    'u128',
                ),
                'Test': 'AccountId',
                'UnlockAsset': ('u32', 'AccountId', 'u128'),
                'UnreservedInitiatorRemainPledgeAmount': (
                    'u32',
                    'u32',
                    'u128',
                ),
                'UserReleaseIcoAmount': ('u32', 'u32', 'u128'),
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
            'Kyc': {
                'ApplyCertification': 'AccountId',
                'AuthenticationGiven': ('AccountId', 'u32'),
                'GetIAS': ('u32', '[u8; 32]'),
                'GetSwordHolder': ('u32', '[u8; 32]'),
                'IASAdded': 'u32',
                'IASJudgementRequested': ('AccountId', 'u32'),
                'IASKilled': 'AccountId',
                'IASRemoved': 'u32',
                'JudgementGiven': ('AccountId', 'u32'),
                'JudgementRequested': ('AccountId', 'u32'),
                'JudgementUnrequested': ('AccountId', 'u32'),
                'KYCCleared': 'AccountId',
                'KYCRemove': 'AccountId',
                'KYCSet': 'AccountId',
                'SetFee': 'u128',
                'SwordHolderAdded': 'u32',
                'SwordHolderKilled': 'AccountId',
                'SwordHolderRemoved': 'u32',
            },
            'LBP': {
                'FundraisingAssetAdded': ('u32', 'u128'),
                'FundraisingAssetRemoved': 'u32',
                'LbpCreated': (
                    'AccountId',
                    'u32',
                    'u32',
                    'u32',
                    'u128',
                    'u128',
                ),
                'LbpExited': ('AccountId', 'u32'),
                'Swapped': ('AccountId', 'u32', 'u32', 'u32', 'u128', 'u128'),
            },
            'Nft': {
                'Active': ('u32', 'u32'),
                'Burn': ('AccountId', 'u32', 'u32'),
                'BuyToken': ('AccountId', 'u32', 'u32', 'u128'),
                'Claim': ('AccountId', 'u32', 'u32'),
                'CreateClass': ('AccountId', 'u32'),
                'DestroyClass': ('AccountId', 'u32'),
                'Inactive': ('u32', 'u32'),
                'Mint': ('u32', 'u32'),
                'OfferTokenForSale': ('u32', 'u32', 'u128'),
                'Transfer': ('AccountId', 'AccountId', ('u32', 'u32')),
                'WithdrawSale': ('u32', 'u32'),
            },
            'OrmlXcm': {
                'Sent': {'message': ['scale_info::74'], 'to': 'scale_info::59'},
            },
            'ParachainSystem': {
                'DownwardMessagesProcessed': {
                    'dmq_head': '[u8; 32]',
                    'weight_used': 'u64',
                },
                'DownwardMessagesReceived': {'count': 'u32'},
                'UpgradeAuthorized': {'code_hash': '[u8; 32]'},
                'ValidationFunctionApplied': {'relay_chain_block_num': 'u32'},
                'ValidationFunctionDiscarded': None,
                'ValidationFunctionStored': None,
            },
            'PolkadotXcm': {
                'AssetsTrapped': (
                    '[u8; 32]',
                    'scale_info::59',
                    'scale_info::94',
                ),
                'Attempted': {
                    'Complete': 'u64',
                    'Error': 'scale_info::80',
                    'Incomplete': ('u64', 'scale_info::80'),
                },
                'InvalidResponder': (
                    'scale_info::59',
                    'u64',
                    (None, 'scale_info::59'),
                ),
                'InvalidResponderVersion': ('scale_info::59', 'u64'),
                'Notified': ('u64', 'u8', 'u8'),
                'NotifyDecodeFailed': ('u64', 'u8', 'u8'),
                'NotifyDispatchError': ('u64', 'u8', 'u8'),
                'NotifyOverweight': ('u64', 'u8', 'u8', 'u64', 'u64'),
                'NotifyTargetMigrationFail': ('scale_info::99', 'u64'),
                'NotifyTargetSendFail': (
                    'scale_info::59',
                    'u64',
                    'scale_info::80',
                ),
                'ResponseReady': ('u64', 'scale_info::77'),
                'ResponseTaken': 'u64',
                'Sent': (
                    'scale_info::59',
                    'scale_info::59',
                    ['scale_info::74'],
                ),
                'SupportedVersionChanged': ('scale_info::59', 'u32'),
                'UnexpectedResponse': ('scale_info::59', 'u64'),
                'VersionChangeNotified': ('scale_info::59', 'u32'),
            },
            'PriceDao': {
                'DepositAccounts': (['AccountId'], 'u128'),
                'GetOraclePrice': ('u32', 'u128'),
                'GetPrice': ('u32', 'u128'),
                'GetSwapPrice': ('u32', 'u128'),
                'LockPrice': ('u32', 'u128'),
                'SlashAccounts': ['AccountId'],
                'UnlockPrice': 'u32',
                'WhoLock': 'AccountId',
            },
            'Scheduler': {
                'CallLookupFailed': {
                    'error': 'scale_info::38',
                    'id': (None, 'Bytes'),
                    'task': ('u32', 'u32'),
                },
                'Canceled': {'index': 'u32', 'when': 'u32'},
                'Dispatched': {
                    'id': (None, 'Bytes'),
                    'result': 'scale_info::29',
                    'task': ('u32', 'u32'),
                },
                'Scheduled': {'index': 'u32', 'when': 'u32'},
            },
            'Session': {'NewSession': {'session_index': 'u32'}},
            'Sudo': {
                'KeyChanged': {'old_sudoer': (None, 'AccountId')},
                'Sudid': {'sudo_result': 'scale_info::29'},
                'SudoAsDone': {'sudo_result': 'scale_info::29'},
            },
            'System': {
                'CodeUpdated': None,
                'ExtrinsicFailed': {
                    'dispatch_error': 'scale_info::22',
                    'dispatch_info': 'scale_info::19',
                },
                'ExtrinsicSuccess': {'dispatch_info': 'scale_info::19'},
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
                    'result': 'scale_info::29',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::29',
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
                    'currency_id': 'u32',
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Deposited': {
                    'amount': 'u128',
                    'currency_id': 'u32',
                    'who': 'AccountId',
                },
                'DustLost': {
                    'amount': 'u128',
                    'currency_id': 'u32',
                    'who': 'AccountId',
                },
                'Endowed': {
                    'amount': 'u128',
                    'currency_id': 'u32',
                    'who': 'AccountId',
                },
                'LockRemoved': {
                    'currency_id': 'u32',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'LockSet': {
                    'amount': 'u128',
                    'currency_id': 'u32',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'currency_id': 'u32',
                    'from': 'AccountId',
                    'status': 'scale_info::34',
                    'to': 'AccountId',
                },
                'Reserved': {
                    'amount': 'u128',
                    'currency_id': 'u32',
                    'who': 'AccountId',
                },
                'Slashed': {
                    'currency_id': 'u32',
                    'free_amount': 'u128',
                    'reserved_amount': 'u128',
                    'who': 'AccountId',
                },
                'TotalIssuanceSet': {'amount': 'u128', 'currency_id': 'u32'},
                'Transfer': {
                    'amount': 'u128',
                    'currency_id': 'u32',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unreserved': {
                    'amount': 'u128',
                    'currency_id': 'u32',
                    'who': 'AccountId',
                },
                'Withdrawn': {
                    'amount': 'u128',
                    'currency_id': 'u32',
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
                    'asset': 'scale_info::57',
                    'who': 'scale_info::59',
                },
                'Withdrawn': {
                    'asset': 'scale_info::57',
                    'who': 'scale_info::59',
                },
            },
            'Vault': {
                'AddGuarder': ('u64', 'AccountId'),
                'BurnOperate': {
                    'call': 'Call',
                    'dao_id': 'u64',
                    'result': 'scale_info::29',
                },
                'IcoOperate': {
                    'call': 'Call',
                    'dao_id': 'u64',
                    'result': 'scale_info::29',
                },
                'OpenCexTransfer': ('u64', 'bool'),
                'RemoveGuard': ('u64', 'AccountId'),
                'SetFee': ('u64', 'scale_info::238'),
                'SetGuarders': 'u64',
                'SomethingStored': ('u32', 'AccountId'),
                'Unreserved': ('u64', 'u32', 'u128'),
            },
            'Vesting': {
                'Claimed': {'amount': 'u128', 'who': 'AccountId'},
                'VestingScheduleAdded': {
                    'from': 'AccountId',
                    'to': 'AccountId',
                    'vesting_schedule': 'scale_info::54',
                },
                'VestingSchedulesUpdated': {'who': 'AccountId'},
            },
            'XTokens': {
                'TransferredMultiAssets': {
                    'assets': ['scale_info::57'],
                    'dest': 'scale_info::59',
                    'fee': 'scale_info::57',
                    'sender': 'AccountId',
                },
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': (None, '[u8; 32]')},
                'BadVersion': {'message_hash': (None, '[u8; 32]')},
                'Fail': {
                    'error': 'scale_info::80',
                    'message_hash': (None, '[u8; 32]'),
                    'weight': 'u64',
                },
                'OverweightEnqueued': {
                    'index': 'u64',
                    'required': 'u64',
                    'sender': 'u32',
                    'sent_at': 'u32',
                },
                'OverweightServiced': {'index': 'u64', 'used': 'u64'},
                'Success': {'message_hash': (None, '[u8; 32]'), 'weight': 'u64'},
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
2400
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
    'base_block': 5346284000,
    'max_block': 500000000000,
    'per_class': {
        'mandatory': {
            'base_extrinsic': 86298000,
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': 86298000,
            'max_extrinsic': 324913702000,
            'max_total': 375000000000,
            'reserved': 0,
        },
        'operational': {
            'base_extrinsic': 86298000,
            'max_extrinsic': 449913702000,
            'max_total': 500000000000,
            'reserved': 125000000000,
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
 The designated SS85 prefix of this chain.

 This replaces the &quot;ss58Format&quot; property declared in the chain spec. Reason is
 that the runtime should know about the prefix in order to make use of it as
 an identifier of the chain.
#### Value
```python
42
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
        ('0x226fe6535864a43a', 1),
        ('0xd39b338cf9ae4c06', 1),
        ('0xdd718d5cc53262d4', 1),
        ('0xdf6acb689907609b', 4),
        ('0x37e397fc7c91f5e4', 1),
        ('0x40fe3ad401f8959a', 6),
        ('0xd2bc9897eed08f15', 3),
        ('0xf78b278be53f454c', 2),
        ('0xab3c0572291feb8b', 1),
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 1),
        ('0xea93e3f16f3d6962', 2),
    ],
    'authoring_version': 1,
    'impl_name': 'KICO',
    'impl_version': 0,
    'spec_name': 'KICO',
    'spec_version': 2022072701,
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