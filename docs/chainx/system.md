
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
| dispatch_error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': 'u8'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero')}```
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
| hash | `T::Hash` | ```scale_info::9```

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
'scale_info::9'
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
    'System', 'EventTopics', ['scale_info::9']
)
```

#### Return value
```python
[('u32', 'u32')]
```
---------
### Events
 Events deposited for the current block.

 NOTE: This storage item is explicitly unbounded since it is never intended to be read
 from within the runtime.

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
            'BaseFee': {
                'BaseFeeOverflow': None,
                'IsActive': 'bool',
                'NewBaseFeePerGas': 'scale_info::111',
                'NewElasticity': 'u32',
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
            'Council': {
                'Approved': {'proposal_hash': 'scale_info::9'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': 'scale_info::9',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': 'scale_info::9'},
                'Executed': {
                    'proposal_hash': 'scale_info::9',
                    'result': 'scale_info::29',
                },
                'MemberExecuted': {
                    'proposal_hash': 'scale_info::9',
                    'result': 'scale_info::29',
                },
                'Proposed': {
                    'account': 'AccountId',
                    'proposal_hash': 'scale_info::9',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'Voted': {
                    'account': 'AccountId',
                    'no': 'u32',
                    'proposal_hash': 'scale_info::9',
                    'voted': 'bool',
                    'yes': 'u32',
                },
            },
            'Democracy': {
                'Blacklisted': {'proposal_hash': 'scale_info::9'},
                'Cancelled': {'ref_index': 'u32'},
                'Delegated': {'target': 'AccountId', 'who': 'AccountId'},
                'Executed': {'ref_index': 'u32', 'result': 'scale_info::29'},
                'ExternalTabled': None,
                'NotPassed': {'ref_index': 'u32'},
                'Passed': {'ref_index': 'u32'},
                'PreimageInvalid': {
                    'proposal_hash': 'scale_info::9',
                    'ref_index': 'u32',
                },
                'PreimageMissing': {
                    'proposal_hash': 'scale_info::9',
                    'ref_index': 'u32',
                },
                'PreimageNoted': {
                    'deposit': 'u128',
                    'proposal_hash': 'scale_info::9',
                    'who': 'AccountId',
                },
                'PreimageReaped': {
                    'deposit': 'u128',
                    'proposal_hash': 'scale_info::9',
                    'provider': 'AccountId',
                    'reaper': 'AccountId',
                },
                'PreimageUsed': {
                    'deposit': 'u128',
                    'proposal_hash': 'scale_info::9',
                    'provider': 'AccountId',
                },
                'Proposed': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Seconded': {'prop_index': 'u32', 'seconder': 'AccountId'},
                'Started': {'ref_index': 'u32', 'threshold': 'scale_info::50'},
                'Tabled': {
                    'deposit': 'u128',
                    'depositors': ['AccountId'],
                    'proposal_index': 'u32',
                },
                'Undelegated': {'account': 'AccountId'},
                'Vetoed': {
                    'proposal_hash': 'scale_info::9',
                    'until': 'u32',
                    'who': 'AccountId',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::51',
                    'voter': 'AccountId',
                },
            },
            'Elections': {
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
            'Ethereum': {
                'Executed': (
                    '[u8; 20]',
                    '[u8; 20]',
                    'scale_info::9',
                    'scale_info::114',
                ),
            },
            'Evm': {
                'BalanceDeposit': ('AccountId', '[u8; 20]', 'scale_info::111'),
                'BalanceWithdraw': (
                    'AccountId',
                    '[u8; 20]',
                    'scale_info::111',
                ),
                'Created': '[u8; 20]',
                'CreatedFailed': '[u8; 20]',
                'Executed': '[u8; 20]',
                'ExecutedFailed': '[u8; 20]',
                'Log': {
                    'address': '[u8; 20]',
                    'data': 'Bytes',
                    'topics': ['scale_info::9'],
                },
            },
            'Grandpa': {
                'NewAuthorities': {'authority_set': [('[u8; 32]', 'u64')]},
                'Paused': None,
                'Resumed': None,
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
                'SomeOffline': {'offline': [('AccountId', 'AccountId')]},
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
                    'timepoint': 'scale_info::64',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::64',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::29',
                    'timepoint': 'scale_info::64',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'Offences': {'Offence': {'kind': '[u8; 16]', 'timeslot': 'Bytes'}},
            'Proxy': {
                'Announced': {
                    'call_hash': 'scale_info::9',
                    'proxy': 'AccountId',
                    'real': 'AccountId',
                },
                'AnonymousCreated': {
                    'anonymous': 'AccountId',
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::105',
                    'who': 'AccountId',
                },
                'ProxyAdded': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::105',
                },
                'ProxyExecuted': {'result': 'scale_info::29'},
            },
            'Scheduler': {
                'CallLookupFailed': {
                    'error': 'scale_info::31',
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
            'System': {
                'CodeUpdated': None,
                'ExtrinsicFailed': {
                    'dispatch_error': 'scale_info::22',
                    'dispatch_info': 'scale_info::19',
                },
                'ExtrinsicSuccess': {'dispatch_info': 'scale_info::19'},
                'KilledAccount': {'account': 'AccountId'},
                'NewAccount': {'account': 'AccountId'},
                'Remarked': {'hash': 'scale_info::9', 'sender': 'AccountId'},
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
                'NewTip': {'tip_hash': 'scale_info::9'},
                'TipClosed': {
                    'payout': 'u128',
                    'tip_hash': 'scale_info::9',
                    'who': 'AccountId',
                },
                'TipClosing': {'tip_hash': 'scale_info::9'},
                'TipRetracted': {'tip_hash': 'scale_info::9'},
                'TipSlashed': {
                    'deposit': 'u128',
                    'finder': 'AccountId',
                    'tip_hash': 'scale_info::9',
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
                'Spending': {'budget_remaining': 'u128'},
            },
            'XAssets': {
                'BalanceSet': ('u32', 'AccountId', 'scale_info::68', 'u128'),
                'Destroyed': ('u32', 'AccountId', 'u128'),
                'Issued': ('u32', 'AccountId', 'u128'),
                'Moved': (
                    'u32',
                    'AccountId',
                    'scale_info::68',
                    'AccountId',
                    'scale_info::68',
                    'u128',
                ),
            },
            'XAssetsBridge': {
                'BackForeign': ('u32', 'bool'),
                'ClaimAccount': ('AccountId', '[u8; 20]'),
                'DepositExecuted': (
                    'u32',
                    'AccountId',
                    '[u8; 20]',
                    'u128',
                    '[u8; 20]',
                ),
                'Dissolve': 'AccountId',
                'ForceUnRegister': ('u32', '[u8; 20]'),
                'Paused': 'u32',
                'PausedAll': None,
                'Register': ('u32', '[u8; 20]'),
                'SetAdmin': 'AccountId',
                'Teleport': ('AccountId', 'u128', 'scale_info::124'),
                'UnPaused': 'u32',
                'UnPausedAll': None,
                'WithdrawExecuted': (
                    'u32',
                    'AccountId',
                    '[u8; 20]',
                    'u128',
                    '[u8; 20]',
                ),
            },
            'XAssetsRegistrar': {
                'Deregistered': 'u32',
                'Recovered': ('u32', 'bool'),
                'Registered': ('u32', 'bool'),
            },
            'XBtcLedger': {
                'BalanceSet': {'free': 'u128', 'who': 'AccountId'},
                'Deposit': {'amount': 'u128', 'who': 'AccountId'},
                'Endowed': {'account': 'AccountId', 'free_balance': 'u128'},
                'Transfer': {
                    'amount': 'u128',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Withdraw': {'amount': 'u128', 'who': 'AccountId'},
            },
            'XGatewayBitcoin': {
                'Deposited': ('scale_info::9', 'AccountId', 'u128'),
                'DepositedAptos': ('scale_info::9', 'scale_info::9', 'u128'),
                'DepositedEvm': ('scale_info::9', '[u8; 20]', 'u128'),
                'DepositedNamed': ('scale_info::9', 'Bytes', 'Bytes', 'u128'),
                'HeaderInserted': 'scale_info::9',
                'PendingDepositAptosRemoved': (
                    'scale_info::9',
                    'u128',
                    'scale_info::9',
                    'Bytes',
                ),
                'PendingDepositEvmRemoved': (
                    '[u8; 20]',
                    'u128',
                    'scale_info::9',
                    'Bytes',
                ),
                'PendingDepositNamedRemoved': (
                    'Bytes',
                    'Bytes',
                    'u128',
                    'scale_info::9',
                    'Bytes',
                ),
                'PendingDepositRemoved': (
                    'AccountId',
                    'u128',
                    'scale_info::9',
                    'Bytes',
                ),
                'TxProcessed': (
                    'scale_info::9',
                    'scale_info::9',
                    'scale_info::87',
                ),
                'UnclaimedDeposit': ('scale_info::9', 'Bytes'),
                'WithdrawalFatalErr': ('scale_info::9', 'scale_info::9'),
                'WithdrawalProposalCreated': ('AccountId', ['u32']),
                'WithdrawalProposalVoted': ('AccountId', 'bool'),
                'Withdrawn': ('scale_info::9', ['u32'], 'u128'),
            },
            'XGatewayCommon': {
                'AllocNativeReward': ('AccountId', 'u32', 'u128'),
                'AllocNotNativeReward': ('AccountId', 'u32', 'u32', 'u128'),
                'ReferralBinded': ('AccountId', 'scale_info::76', 'AccountId'),
                'SetTrusteeProps': (
                    'AccountId',
                    'scale_info::76',
                    'scale_info::78',
                ),
                'SetTrusteeProxy': (
                    'AccountId',
                    'scale_info::76',
                    'AccountId',
                ),
                'TransferAssetReward': ('AccountId', 'u32', 'u128'),
                'TransferTrusteeReward': (
                    'AccountId',
                    'AccountId',
                    'scale_info::76',
                    'u32',
                    'u128',
                ),
                'TrusteeSetChanged': (
                    'scale_info::76',
                    'u32',
                    'scale_info::81',
                    'u32',
                ),
            },
            'XGatewayRecords': {
                'Deposited': ('AccountId', 'u32', 'u128'),
                'WithdrawalCanceled': ('u32', 'scale_info::74'),
                'WithdrawalCreated': ('u32', 'scale_info::72'),
                'WithdrawalFinished': ('u32', 'scale_info::74'),
                'WithdrawalProcessed': 'u32',
                'WithdrawalRecovered': 'u32',
            },
            'XMiningAsset': {
                'Claimed': ('AccountId', 'u32', 'u128'),
                'Minted': ('AccountId', 'u128'),
            },
            'XSpot': {
                'CanceledOrderUpdated': {
                    'already_filled': 'u128',
                    'executed_indices': ['u64'],
                    'last_update_at': 'u32',
                    'props': 'scale_info::95',
                    'remaining': 'u128',
                    'status': 'scale_info::98',
                },
                'MakerOrderUpdated': {
                    'already_filled': 'u128',
                    'executed_indices': ['u64'],
                    'last_update_at': 'u32',
                    'props': 'scale_info::95',
                    'remaining': 'u128',
                    'status': 'scale_info::98',
                },
                'NewOrder': {
                    'already_filled': 'u128',
                    'executed_indices': ['u64'],
                    'last_update_at': 'u32',
                    'props': 'scale_info::95',
                    'remaining': 'u128',
                    'status': 'scale_info::98',
                },
                'OrderExecuted': {
                    'executed_at': 'u32',
                    'maker': 'AccountId',
                    'maker_order_id': 'u64',
                    'pair_id': 'u32',
                    'price': 'u128',
                    'taker': 'AccountId',
                    'taker_order_id': 'u64',
                    'trading_history_idx': 'u64',
                    'turnover': 'u128',
                },
                'PriceFluctuationUpdated': ('u32', 'u32'),
                'TakerOrderUpdated': {
                    'already_filled': 'u128',
                    'executed_indices': ['u64'],
                    'last_update_at': 'u32',
                    'props': 'scale_info::95',
                    'remaining': 'u128',
                    'status': 'scale_info::98',
                },
                'TradingPairAdded': {
                    'currency_pair': 'scale_info::102',
                    'id': 'u32',
                    'pip_decimals': 'u32',
                    'tick_decimals': 'u32',
                    'tradable': 'bool',
                },
                'TradingPairUpdated': {
                    'currency_pair': 'scale_info::102',
                    'id': 'u32',
                    'pip_decimals': 'u32',
                    'tick_decimals': 'u32',
                    'tradable': 'bool',
                },
            },
            'XStaking': {
                'Bonded': ('AccountId', 'AccountId', 'u128'),
                'Claimed': ('AccountId', 'AccountId', 'u128'),
                'ForceAllWithdrawn': 'AccountId',
                'ForceChilled': ('u32', ['AccountId']),
                'Minted': ('AccountId', 'u128'),
                'MintedForValidator': (
                    'AccountId',
                    'u128',
                    'AccountId',
                    'u128',
                ),
                'Rebonded': ('AccountId', 'AccountId', 'AccountId', 'u128'),
                'Slashed': ('AccountId', 'u128'),
                'Unbonded': ('AccountId', 'AccountId', 'u128'),
                'Withdrawn': ('AccountId', 'u128'),
            },
            'XSystem': {
                'Blacklisted': 'AccountId',
                'Unblacklisted': 'AccountId',
            },
            None: None,
            'Session': {'NewSession': {'session_index': 'u32'}},
            'TechnicalCommittee': {
                'Approved': {'proposal_hash': 'scale_info::9'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': 'scale_info::9',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': 'scale_info::9'},
                'Executed': {
                    'proposal_hash': 'scale_info::9',
                    'result': 'scale_info::29',
                },
                'MemberExecuted': {
                    'proposal_hash': 'scale_info::9',
                    'result': 'scale_info::29',
                },
                'Proposed': {
                    'account': 'AccountId',
                    'proposal_hash': 'scale_info::9',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'Voted': {
                    'account': 'AccountId',
                    'no': 'u32',
                    'proposal_hash': 'scale_info::9',
                    'voted': 'bool',
                    'yes': 'u32',
                },
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchInterrupted': {
                    'error': 'scale_info::22',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::29'},
                'ItemCompleted': None,
            },
            'XTransactionFee': {
                'BTCFeePaid': ('AccountId', 'u128'),
                'FeePaid': ('AccountId', 'u128', 'AccountId', 'u128'),
            },
        },
        'phase': {
            'ApplyExtrinsic': 'u32',
            'Finalization': None,
            'Initialization': None,
        },
        'topics': ['scale_info::9'],
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
'scale_info::9'
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
    'base_block': 5000000000,
    'max_block': 2000000000000,
    'per_class': {
        'mandatory': {
            'base_extrinsic': 125000000,
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': 125000000,
            'max_extrinsic': 1449875000000,
            'max_total': 1500000000000,
            'reserved': 0,
        },
        'operational': {
            'base_extrinsic': 125000000,
            'max_extrinsic': 1949875000000,
            'max_total': 2000000000000,
            'reserved': 500000000000,
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
44
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
        ('0x40fe3ad401f8959a', 5),
        ('0xd2bc9897eed08f15', 3),
        ('0xf78b278be53f454c', 2),
        ('0xcbca25e39f142387', 2),
        ('0xab3c0572291feb8b', 1),
        ('0xed99c5acb25eedf5', 3),
        ('0x687ad44ad37f03c2', 1),
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 1),
        ('0xbee05af7fa857707', 1),
        ('0x9ebc51b3f7417e21', 1),
        ('0xe2fb5589abd4cdd5', 1),
        ('0x1f9a726095b769ea', 1),
        ('0x81b5bdc101bdfcd3', 1),
        ('0xd29d497e8e7bb356', 1),
        ('0xf7caa15ca5ade450', 1),
        ('0x227ca46d3c40b0af', 1),
        ('0x8534d1a99d7a0f28', 1),
        ('0xe65b00e46cedd0aa', 2),
        ('0x582211f65bb14b89', 4),
    ],
    'authoring_version': 1,
    'impl_name': 'chainx-net',
    'impl_version': 1,
    'spec_name': 'chainx',
    'spec_version': 34,
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