
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
            None: None,
            'Assets': {
                'ApprovalCancelled': {
                    'asset_id': 'u32',
                    'delegate': 'AccountId',
                    'owner': 'AccountId',
                },
                'ApprovedTransfer': {
                    'amount': 'u128',
                    'asset_id': 'u32',
                    'delegate': 'AccountId',
                    'source': 'AccountId',
                },
                'AssetFrozen': {'asset_id': 'u32'},
                'AssetStatusChanged': {'asset_id': 'u32'},
                'AssetThawed': {'asset_id': 'u32'},
                'Burned': {
                    'asset_id': 'u32',
                    'balance': 'u128',
                    'owner': 'AccountId',
                },
                'Created': {
                    'asset_id': 'u32',
                    'creator': 'AccountId',
                    'owner': 'AccountId',
                },
                'Destroyed': {'asset_id': 'u32'},
                'ForceCreated': {'asset_id': 'u32', 'owner': 'AccountId'},
                'Frozen': {'asset_id': 'u32', 'who': 'AccountId'},
                'Issued': {
                    'asset_id': 'u32',
                    'owner': 'AccountId',
                    'total_supply': 'u128',
                },
                'MetadataCleared': {'asset_id': 'u32'},
                'MetadataSet': {
                    'asset_id': 'u32',
                    'decimals': 'u8',
                    'is_frozen': 'bool',
                    'name': 'Bytes',
                    'symbol': 'Bytes',
                },
                'OwnerChanged': {'asset_id': 'u32', 'owner': 'AccountId'},
                'TeamChanged': {
                    'admin': 'AccountId',
                    'asset_id': 'u32',
                    'freezer': 'AccountId',
                    'issuer': 'AccountId',
                },
                'Thawed': {'asset_id': 'u32', 'who': 'AccountId'},
                'Transferred': {
                    'amount': 'u128',
                    'asset_id': 'u32',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'TransferredApproved': {
                    'amount': 'u128',
                    'asset_id': 'u32',
                    'delegate': 'AccountId',
                    'destination': 'AccountId',
                    'owner': 'AccountId',
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
            'CarbonCredits': {
                'AuthorizedAccountAdded': {'account_id': 'AccountId'},
                'AuthorizedAccountRemoved': {'account_id': 'AccountId'},
                'BatchGroupAdded': {'group_id': 'u32', 'project_id': 'u32'},
                'CarbonCreditMinted': {
                    'amount': 'u128',
                    'group_id': 'u32',
                    'project_id': 'u32',
                    'recipient': 'AccountId',
                },
                'CarbonCreditRetired': {
                    'account': 'AccountId',
                    'amount': 'u128',
                    'asset_id': 'u32',
                    'group_id': 'u32',
                    'project_id': 'u32',
                    'retire_data': ['scale_info::101'],
                },
                'ProjectApproved': {'asset_ids': ['u32'], 'project_id': 'u32'},
                'ProjectCreated': {'project_id': 'u32'},
                'ProjectRejected': {'project_id': 'u32'},
                'ProjectResubmitted': {'project_id': 'u32'},
                'ProjectUpdated': {'project_id': 'u32'},
            },
            'CarbonCreditsPools': {
                'Deposit': {
                    'amount': 'u128',
                    'asset_id': 'u32',
                    'pool_id': 'u32',
                    'who': 'AccountId',
                },
                'PoolCreated': {
                    'admin': 'AccountId',
                    'config': 'scale_info::106',
                    'id': 'u32',
                },
                'Retired': {
                    'amount': 'u128',
                    'pool_id': 'u32',
                    'who': 'AccountId',
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
            'CumulusXcm': {
                'ExecutedDownward': ('[u8; 8]', 'scale_info::47'),
                'InvalidFormat': '[u8; 8]',
                'UnsupportedVersion': '[u8; 8]',
            },
            'Dex': {
                'BuyOrderCreated': {
                    'buyer': 'AccountId',
                    'fees_paid': 'u128',
                    'group_id': 'u32',
                    'order_id': 'u128',
                    'price_per_unit': 'u128',
                    'project_id': 'u32',
                    'sell_order_id': 'u128',
                    'seller': 'AccountId',
                    'total_amount': 'u128',
                    'units': 'u128',
                },
                'BuyOrderExpired': {
                    'buyer': 'AccountId',
                    'order_id': 'u128',
                    'sell_order_id': 'u128',
                    'units': 'u128',
                },
                'BuyOrderFilled': {
                    'buyer': 'AccountId',
                    'fees_paid': 'u128',
                    'group_id': 'u32',
                    'order_id': 'u128',
                    'price_per_unit': 'u128',
                    'project_id': 'u32',
                    'sell_order_id': 'u128',
                    'seller': 'AccountId',
                    'units': 'u128',
                },
                'BuyOrderPaymentValidated': {
                    'chain_id': 'u32',
                    'order_id': 'u128',
                    'validator': 'AccountId',
                },
                'SellOrderCancelled': {
                    'order_id': 'u128',
                    'seller': 'AccountId',
                },
                'SellOrderCreated': {
                    'asset_id': 'u32',
                    'group_id': 'u32',
                    'order_id': 'u128',
                    'owner': 'AccountId',
                    'price_per_unit': 'u128',
                    'project_id': 'u32',
                    'units': 'u128',
                },
                'SellerPayoutAuthoritySet': {'authority': 'AccountId'},
                'SellerPayoutExecuted': {
                    'payout': 'scale_info::123',
                    'seller': 'AccountId',
                },
                'SellerPayoutPreferenceSet': {
                    'preference': (None, 'scale_info::120'),
                    'seller': 'AccountId',
                },
                'UserOpenOrderUnitsLimitUpdated': {
                    'level': 'scale_info::129',
                    'limit': 'u128',
                },
                'ValidatorAccountAdded': {'account_id': 'AccountId'},
                'ValidatorAccountRemoved': {'account_id': 'AccountId'},
            },
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::47',
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
            'KYC': {
                'AuthorizedAccountAdded': {'account_id': 'AccountId'},
                'AuthorizedAccountRemoved': {'account_id': 'AccountId'},
                'Dummy': None,
                'KYCAirdrop': {'amount': 'u128', 'who': 'AccountId'},
                'KeyChanged': None,
                'MemberAdded': {'who': 'AccountId'},
                'MemberRemoved': {'who': 'AccountId'},
                'MembersReset': None,
                'MembersSwapped': None,
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::117',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::117',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::90',
                    'timepoint': 'scale_info::117',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'ParachainStaking': {
                'CandidateAdded': {
                    'account_id': 'AccountId',
                    'deposit': 'u128',
                },
                'CandidateRemoved': {'account_id': 'AccountId'},
                'CollatorRewardsTransferred': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                },
                'DelegatedMore': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'candidate': 'AccountId',
                },
                'DelegationRemoved': {
                    'account_id': 'AccountId',
                    'candidate': 'AccountId',
                },
                'DelegatorRewardsTransferred': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                },
                'InflationAmountSet': {'amount': 'u128'},
                'NewCandidacyBond': {'bond_amount': 'u128'},
                'NewDelegation': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'candidate': 'AccountId',
                },
                'NewDesiredCandidates': {'desired_candidates': 'u32'},
                'NewInvulnerables': {'invulnerables': ['scale_info::35']},
                'UnbondedWithdrawn': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                },
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
                    'scale_info::48',
                    'scale_info::79',
                ),
                'AssetsTrapped': (
                    '[u8; 32]',
                    'scale_info::48',
                    'scale_info::79',
                ),
                'Attempted': {
                    'Complete': 'u64',
                    'Error': 'scale_info::44',
                    'Incomplete': ('u64', 'scale_info::44'),
                },
                'InvalidResponder': (
                    'scale_info::48',
                    'u64',
                    (None, 'scale_info::48'),
                ),
                'InvalidResponderVersion': ('scale_info::48', 'u64'),
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
                'NotifyTargetMigrationFail': ('scale_info::84', 'u64'),
                'NotifyTargetSendFail': (
                    'scale_info::48',
                    'u64',
                    'scale_info::44',
                ),
                'ResponseReady': ('u64', 'scale_info::69'),
                'ResponseTaken': 'u64',
                'Sent': (
                    'scale_info::48',
                    'scale_info::48',
                    ['scale_info::60'],
                ),
                'SupportedVersionChanged': ('scale_info::48', 'u32'),
                'UnexpectedResponse': ('scale_info::48', 'u64'),
                'VersionChangeNotified': ('scale_info::48', 'u32'),
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
                    'proxy_type': 'scale_info::137',
                },
                'ProxyExecuted': {'result': 'scale_info::90'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::137',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::137',
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
                    'result': 'scale_info::90',
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
                'Sudid': {'sudo_result': 'scale_info::90'},
                'SudoAsDone': {'sudo_result': 'scale_info::90'},
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
            'Tokens': {
                'BalanceSet': {
                    'currency_id': 'scale_info::88',
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Deposited': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::88',
                    'who': 'AccountId',
                },
                'DustLost': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::88',
                    'who': 'AccountId',
                },
                'Endowed': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::88',
                    'who': 'AccountId',
                },
                'LockRemoved': {
                    'currency_id': 'scale_info::88',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'LockSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::88',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::88',
                    'from': 'AccountId',
                    'status': 'scale_info::31',
                    'to': 'AccountId',
                },
                'Reserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::88',
                    'who': 'AccountId',
                },
                'Slashed': {
                    'currency_id': 'scale_info::88',
                    'free_amount': 'u128',
                    'reserved_amount': 'u128',
                    'who': 'AccountId',
                },
                'TotalIssuanceSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::88',
                },
                'Transfer': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::88',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unreserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::88',
                    'who': 'AccountId',
                },
                'Withdrawn': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::88',
                    'who': 'AccountId',
                },
            },
            'TransactionPause': {
                'TransactionPaused': {
                    'function_name_bytes': 'Bytes',
                    'pallet_name_bytes': 'Bytes',
                },
                'TransactionUnpaused': {
                    'function_name_bytes': 'Bytes',
                    'pallet_name_bytes': 'Bytes',
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
            'Uniques': {
                'ApprovalCancelled': {
                    'collection': 'u32',
                    'delegate': 'AccountId',
                    'item': 'u32',
                    'owner': 'AccountId',
                },
                'ApprovedTransfer': {
                    'collection': 'u32',
                    'delegate': 'AccountId',
                    'item': 'u32',
                    'owner': 'AccountId',
                },
                'AttributeCleared': {
                    'collection': 'u32',
                    'key': 'Bytes',
                    'maybe_item': (None, 'u32'),
                },
                'AttributeSet': {
                    'collection': 'u32',
                    'key': 'Bytes',
                    'maybe_item': (None, 'u32'),
                    'value': 'Bytes',
                },
                'Burned': {
                    'collection': 'u32',
                    'item': 'u32',
                    'owner': 'AccountId',
                },
                'CollectionFrozen': {'collection': 'u32'},
                'CollectionMaxSupplySet': {
                    'collection': 'u32',
                    'max_supply': 'u32',
                },
                'CollectionMetadataCleared': {'collection': 'u32'},
                'CollectionMetadataSet': {
                    'collection': 'u32',
                    'data': 'Bytes',
                    'is_frozen': 'bool',
                },
                'CollectionThawed': {'collection': 'u32'},
                'Created': {
                    'collection': 'u32',
                    'creator': 'AccountId',
                    'owner': 'AccountId',
                },
                'Destroyed': {'collection': 'u32'},
                'ForceCreated': {'collection': 'u32', 'owner': 'AccountId'},
                'Frozen': {'collection': 'u32', 'item': 'u32'},
                'Issued': {
                    'collection': 'u32',
                    'item': 'u32',
                    'owner': 'AccountId',
                },
                'ItemBought': {
                    'buyer': 'AccountId',
                    'collection': 'u32',
                    'item': 'u32',
                    'price': 'u128',
                    'seller': 'AccountId',
                },
                'ItemPriceRemoved': {'collection': 'u32', 'item': 'u32'},
                'ItemPriceSet': {
                    'collection': 'u32',
                    'item': 'u32',
                    'price': 'u128',
                    'whitelisted_buyer': (None, 'AccountId'),
                },
                'ItemStatusChanged': {'collection': 'u32'},
                'MetadataCleared': {'collection': 'u32', 'item': 'u32'},
                'MetadataSet': {
                    'collection': 'u32',
                    'data': 'Bytes',
                    'is_frozen': 'bool',
                    'item': 'u32',
                },
                'OwnerChanged': {
                    'collection': 'u32',
                    'new_owner': 'AccountId',
                },
                'OwnershipAcceptanceChanged': {
                    'maybe_collection': (None, 'u32'),
                    'who': 'AccountId',
                },
                'Redeposited': {
                    'collection': 'u32',
                    'successful_items': ['u32'],
                },
                'TeamChanged': {
                    'admin': 'AccountId',
                    'collection': 'u32',
                    'freezer': 'AccountId',
                    'issuer': 'AccountId',
                },
                'Thawed': {'collection': 'u32', 'item': 'u32'},
                'Transferred': {
                    'collection': 'u32',
                    'from': 'AccountId',
                    'item': 'u32',
                    'to': 'AccountId',
                },
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::24',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::90'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::24'},
            },
            'VestingContract': {
                'AuthorizedAccountAdded': {'account_id': 'AccountId'},
                'AuthorizedAccountRemoved': {'account_id': 'AccountId'},
                'ContractAdded': {
                    'amount': 'u128',
                    'expiry': 'u32',
                    'recipient': 'AccountId',
                },
                'ContractRemoved': {'recipient': 'AccountId'},
                'ContractWithdrawn': {
                    'amount': 'u128',
                    'expiry': 'u32',
                    'recipient': 'AccountId',
                },
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': (None, '[u8; 32]')},
                'BadVersion': {'message_hash': (None, '[u8; 32]')},
                'Fail': {
                    'error': 'scale_info::44',
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
    ],
    'authoring_version': 1,
    'impl_name': 'bitgreen-parachain',
    'impl_version': 0,
    'spec_name': 'bitgreen-parachain',
    'spec_version': 1201,
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
### SpecVersionNeedsToIncrease
The specification version is not allowed to decrease between the current runtime
and the new runtime.

---------