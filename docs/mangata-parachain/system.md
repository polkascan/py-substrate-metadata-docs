
# System

---------
## Calls

---------
### enqueue_txs
Persists list of encoded txs into the storage queue. There is an dedicated
check in [Executive](https://storage.googleapis.com/mangata-docs-node/frame_executive/struct.Executive.html) that verifies that passed binary data can be
decoded into extrinsics.
#### Attributes
| Name | Type |
| -------- | -------- | 
| txs | `Vec<(Option<T::AccountId>, EncodedTx)>` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'enqueue_txs', {
    'txs': [
        ((None, 'AccountId'), 'Bytes'),
    ],
}
)
```

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
### TxsEnqueued
On stored txs
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| count | `u64` | ```u64```

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
    'data': (),
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
### BlockSeed
 Map of block numbers to block shuffling seeds

#### Python
```python
result = substrate.query(
    'System', 'BlockSeed', []
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
### DidStoreTxs
 Map of block numbers to block shuffling seeds

#### Python
```python
result = substrate.query(
    'System', 'DidStoreTxs', []
)
```

#### Return value
```python
'bool'
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
                'RegisteredAsset': {
                    'asset_id': 'u32',
                    'metadata': 'scale_info::107',
                },
                'UpdatedAsset': {
                    'asset_id': 'u32',
                    'metadata': 'scale_info::107',
                },
            },
            'Bootstrap': {
                'AccountsWhitelisted': None,
                'BootstrapFinalized': None,
                'BootstrapParitallyFinalized': None,
                'Provisioned': ('u32', 'u128'),
                'RewardsClaimed': ('u32', 'u128'),
                'RewardsLiquidityAcitvationFailed': (
                    'AccountId',
                    'u32',
                    'u128',
                ),
                'VestedProvisioned': ('u32', 'u128'),
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
                    'result': 'scale_info::116',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::116',
                },
                'MembersChanged': {'new_members': ['AccountId']},
                'PrimeSet': {'new_prime': (None, 'AccountId')},
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
            'Crowdloan': {
                'InitialPaymentMade': ('AccountId', 'u128'),
                'InitializedAccountWithNotEnoughContribution': (
                    'AccountId',
                    (None, 'AccountId'),
                    'u128',
                ),
                'InitializedAlreadyInitializedAccount': (
                    'AccountId',
                    (None, 'AccountId'),
                    'u128',
                ),
                'NativeIdentityAssociated': ('AccountId', 'AccountId', 'u128'),
                'RewardAddressUpdated': ('AccountId', 'AccountId'),
                'RewardsPaid': ('AccountId', 'u128'),
            },
            'CumulusXcm': {
                'ExecutedDownward': ('[u8; 8]', 'scale_info::64'),
                'InvalidFormat': '[u8; 8]',
                'UnsupportedVersion': '[u8; 8]',
            },
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::64',
                },
                'InvalidFormat': {'message_id': '[u8; 32]'},
                'OverweightEnqueued': {
                    'message_id': '[u8; 32]',
                    'overweight_index': 'u64',
                    'required_weight': 'scale_info::7',
                },
                'OverweightServiced': {
                    'overweight_index': 'u64',
                    'weight_used': 'scale_info::7',
                },
                'UnsupportedVersion': {'message_id': '[u8; 32]'},
                'WeightExhausted': {
                    'message_id': '[u8; 32]',
                    'remaining_weight': 'scale_info::7',
                    'required_weight': 'scale_info::7',
                },
            },
            'ParachainSystem': {
                'DownwardMessagesProcessed': {
                    'dmq_head': '[u8; 32]',
                    'weight_used': 'scale_info::7',
                },
                'DownwardMessagesReceived': {'count': 'u32'},
                'UpgradeAuthorized': {'code_hash': '[u8; 32]'},
                'ValidationFunctionApplied': {'relay_chain_block_num': 'u32'},
                'ValidationFunctionDiscarded': None,
                'ValidationFunctionStored': None,
            },
            'System': {
                'CodeUpdated': None,
                'ExtrinsicFailed': {
                    'dispatch_error': 'scale_info::31',
                    'dispatch_info': 'scale_info::28',
                },
                'ExtrinsicSuccess': {'dispatch_info': 'scale_info::28'},
                'KilledAccount': {'account': 'AccountId'},
                'NewAccount': {'account': 'AccountId'},
                'Remarked': {'hash': '[u8; 32]', 'sender': 'AccountId'},
                'TxsEnqueued': {'count': 'u64'},
            },
            'Xyk': {
                'AssetsSwapped': ('AccountId', 'u32', 'u128', 'u32', 'u128'),
                'BuyAssetFailedDueToSlippage': (
                    'AccountId',
                    'u32',
                    'u128',
                    'u32',
                    'u128',
                    'u128',
                ),
                'LiquidityActivated': ('AccountId', 'u32', 'u128'),
                'LiquidityBurned': (
                    'AccountId',
                    'u32',
                    'u128',
                    'u32',
                    'u128',
                    'u32',
                    'u128',
                ),
                'LiquidityDeactivated': ('AccountId', 'u32', 'u128'),
                'LiquidityMinted': (
                    'AccountId',
                    'u32',
                    'u128',
                    'u32',
                    'u128',
                    'u32',
                    'u128',
                ),
                'PoolCreated': ('AccountId', 'u32', 'u128', 'u32', 'u128'),
                'PoolPromotionUpdated': ('u32', (None, 'u8')),
                'RewardsClaimed': ('AccountId', 'u32', 'u128'),
                'SellAssetFailedDueToSlippage': (
                    'AccountId',
                    'u32',
                    'u128',
                    'u32',
                    'u128',
                    'u128',
                ),
            },
            None: None,
            'FeeLock': {
                'FeeLockMetadataUpdated': None,
                'FeeLockUnlocked': ('AccountId', 'u128'),
            },
            'Issuance': {
                'IssuanceConfigInitialized': {
                    'cap': 'u128',
                    'issuance_at_init': 'u128',
                    'linear_issuance_blocks': 'u32',
                    'liquidity_mining_split': 'u32',
                    'staking_split': 'u32',
                    'total_crowdloan_allocation': 'u128',
                },
                'SessionIssuanceIssued': ('u32', 'u128', 'u128'),
                'SessionIssuanceRecorded': ('u32', 'u128', 'u128'),
                'TGEFinalized': None,
                'TGEInstanceFailed': {'amount': 'u128', 'who': 'AccountId'},
                'TGEInstanceSucceeded': {'amount': 'u128', 'who': 'AccountId'},
            },
            'MultiPurposeLiquidity': {
                'TokensRelockedFromReserve': (
                    'AccountId',
                    'u32',
                    'u128',
                    'u128',
                ),
                'VestingTokensReserved': ('AccountId', 'u32', 'u128'),
            },
            'OrmlXcm': {
                'Sent': {'message': ['scale_info::77'], 'to': 'scale_info::65'},
            },
            'ParachainStaking': {
                'CancelledCandidateBondChange': (
                    'AccountId',
                    'scale_info::52',
                ),
                'CancelledCandidateExit': 'AccountId',
                'CancelledDelegationRequest': ('AccountId', 'scale_info::54'),
                'CandidateBackOnline': ('u32', 'AccountId'),
                'CandidateBondLessRequested': ('AccountId', 'u128', 'u32'),
                'CandidateBondMoreRequested': ('AccountId', 'u128', 'u32'),
                'CandidateBondedLess': ('AccountId', 'u128', 'u128'),
                'CandidateBondedMore': ('AccountId', 'u128', 'u128'),
                'CandidateLeft': ('AccountId', 'u128', 'u128'),
                'CandidateScheduledExit': ('u32', 'AccountId', 'u32'),
                'CandidateWentOffline': ('u32', 'AccountId'),
                'CollatorChosen': ('u32', 'AccountId', 'u128'),
                'CollatorCommissionSet': ('u32', 'u32'),
                'Delegation': (
                    'AccountId',
                    'u128',
                    'AccountId',
                    'scale_info::56',
                ),
                'DelegationDecreaseScheduled': (
                    'AccountId',
                    'AccountId',
                    'u128',
                    'u32',
                ),
                'DelegationDecreased': (
                    'AccountId',
                    'AccountId',
                    'u128',
                    'bool',
                ),
                'DelegationIncreaseScheduled': (
                    'AccountId',
                    'AccountId',
                    'u128',
                    'u32',
                ),
                'DelegationIncreased': (
                    'AccountId',
                    'AccountId',
                    'u128',
                    'bool',
                ),
                'DelegationRevocationScheduled': (
                    'u32',
                    'AccountId',
                    'AccountId',
                    'u32',
                ),
                'DelegationRevoked': ('AccountId', 'AccountId', 'u128'),
                'DelegatorDueReward': ('AccountId', 'AccountId', 'u128'),
                'DelegatorExitCancelled': 'AccountId',
                'DelegatorExitScheduled': ('u32', 'AccountId', 'u32'),
                'DelegatorLeft': ('AccountId', 'u128'),
                'DelegatorLeftCandidate': (
                    'AccountId',
                    'AccountId',
                    'u128',
                    'u128',
                ),
                'JoinedCollatorCandidates': ('AccountId', 'u128', 'u128'),
                'NewRound': ('u32', 'u32', 'u32', 'u128'),
                'Rewarded': ('AccountId', 'u128'),
                'StakeExpectationsSet': ('u128', 'u128', 'u128'),
                'TotalSelectedSet': ('u32', 'u32'),
            },
            'PolkadotXcm': {
                'AssetsClaimed': (
                    '[u8; 32]',
                    'scale_info::65',
                    'scale_info::95',
                ),
                'AssetsTrapped': (
                    '[u8; 32]',
                    'scale_info::65',
                    'scale_info::95',
                ),
                'Attempted': {
                    'Complete': 'u64',
                    'Error': 'scale_info::61',
                    'Incomplete': ('u64', 'scale_info::61'),
                },
                'InvalidResponder': (
                    'scale_info::65',
                    'u64',
                    (None, 'scale_info::65'),
                ),
                'InvalidResponderVersion': ('scale_info::65', 'u64'),
                'Notified': ('u64', 'u8', 'u8'),
                'NotifyDecodeFailed': ('u64', 'u8', 'u8'),
                'NotifyDispatchError': ('u64', 'u8', 'u8'),
                'NotifyOverweight': (
                    'u64',
                    'u8',
                    'u8',
                    'scale_info::7',
                    'scale_info::7',
                ),
                'NotifyTargetMigrationFail': ('scale_info::100', 'u64'),
                'NotifyTargetSendFail': (
                    'scale_info::65',
                    'u64',
                    'scale_info::61',
                ),
                'ResponseReady': ('u64', 'scale_info::85'),
                'ResponseTaken': 'u64',
                'Sent': (
                    'scale_info::65',
                    'scale_info::65',
                    ['scale_info::77'],
                ),
                'SupportedVersionChanged': ('scale_info::65', 'u32'),
                'UnexpectedResponse': ('scale_info::65', 'u64'),
                'VersionChangeNotified': ('scale_info::65', 'u32'),
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
                    'proxy_type': 'scale_info::123',
                },
                'ProxyExecuted': {'result': 'scale_info::116'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::123',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::123',
                    'pure': 'AccountId',
                    'who': 'AccountId',
                },
            },
            'Session': {'NewSession': {'session_index': 'u32'}},
            'Sudo': {
                'KeyChanged': {'old_sudoer': (None, 'AccountId')},
                'Sudid': {'sudo_result': 'scale_info::116'},
                'SudoAsDone': {'sudo_result': 'scale_info::116'},
            },
            'SudoOrigin': {
                'SuOriginDid': {'Err': 'scale_info::31', 'Ok': ()},
                'SuOriginDoAsDone': {'Err': 'scale_info::31', 'Ok': ()},
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
                'Issued': ('u32', 'AccountId', 'u128'),
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
                'Minted': ('u32', 'AccountId', 'u128'),
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'currency_id': 'u32',
                    'from': 'AccountId',
                    'status': 'scale_info::39',
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
                    'asset': 'scale_info::80',
                    'who': 'scale_info::65',
                },
                'Withdrawn': {
                    'asset': 'scale_info::80',
                    'who': 'scale_info::65',
                },
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::31',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::116'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::31'},
            },
            'Vesting': {
                'VestingCompleted': ('AccountId', 'u32'),
                'VestingUpdated': ('AccountId', 'u32', 'u128'),
            },
            'XTokens': {
                'TransferredMultiAssets': {
                    'assets': ['scale_info::80'],
                    'dest': 'scale_info::65',
                    'fee': 'scale_info::80',
                    'sender': 'AccountId',
                },
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': (None, '[u8; 32]')},
                'BadVersion': {'message_hash': (None, '[u8; 32]')},
                'Fail': {
                    'error': 'scale_info::61',
                    'message_hash': (None, '[u8; 32]'),
                    'weight': 'scale_info::7',
                },
                'OverweightEnqueued': {
                    'index': 'u64',
                    'required': 'scale_info::7',
                    'sender': 'u32',
                    'sent_at': 'u32',
                },
                'OverweightServiced': {
                    'index': 'u64',
                    'used': 'scale_info::7',
                },
                'Success': {'message_hash': (None, '[u8; 32]'), 'weight': 'scale_info::7'},
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
### StorageQueue
 Storage queue is used for storing transactions in blockchain itself.
 Main reason for that storage entry is fact that upon VER block `N` execution it is
 required to fetch &amp; executed transactions from previous block (`N-1`) but due to origin
 substrate design blocks &amp; extrinsics are stored in rocksDB database that is not accessible
 from runtime part of the node (see [Substrate architecture](https://storage.googleapis.com/mangata-docs-node/frame_executive/struct.Executive.html)) what makes it impossible to properly implement block
 execution logic. As an solution blockchain runtime storage was selected as buffer for txs
 waiting for execution. Main advantage of such approach is fact that storage state is public
 so its impossible to manipulate data stored in there. Storage queue is implemented as double
 buffered queue - to solve problem of rare occasions where due to different reasons some txs
 that were included in block `N` are not able to be executed in a following block `N+1` (good
 example is new session hook/event that by design consumes whole block capacity).


 \# Overhead
 Its worth to notice that storage queue adds only single storage write, as list of all txs
 is stored as single value (encoded list of txs) maped to single key (block number)

 \# Storage Qeueue interaction
 There are two ways to interact with storage queue:
 - enqueuing new txs using [`Pallet::enqueue_txs`] inherent
 - poping txs from the queue using [`Pallet::pop_txs`] that is exposed throught RuntimeApi
   call

#### Python
```python
result = substrate.query(
    'System', 'StorageQueue', []
)
```

#### Return value
```python
[('u32', (None, 'u32'), [((None, 'AccountId'), 'Bytes')])]
```
---------
### TxPrevalidation
 Map of block numbers to block shuffling seeds

#### Python
```python
result = substrate.query(
    'System', 'TxPrevalidation', []
)
```

#### Return value
```python
'bool'
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
    'base_block': {'proof_size': 0, 'ref_time': 8012576000},
    'max_block': {'proof_size': 9223372036854775807, 'ref_time': 250000000000},
    'per_class': {
        'mandatory': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 111477000},
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 111477000},
            'max_extrinsic': {
                'proof_size': 6456360425798343065,
                'ref_time': 174888523000,
            },
            'max_total': {
                'proof_size': 6917529027641081855,
                'ref_time': 187500000000,
            },
            'reserved': {'proof_size': 0, 'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 111477000},
            'max_extrinsic': {
                'proof_size': 8762203435012037017,
                'ref_time': 237388523000,
            },
            'max_total': {
                'proof_size': 9223372036854775807,
                'ref_time': 250000000000,
            },
            'reserved': {
                'proof_size': 2305843009213693952,
                'ref_time': 62500000000,
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
        ('0x5a84941cdf3b3c04', 1),
        ('0xbe7f39a70c12a34e', 1),
        ('0xb227f87c142c7334', 1),
        ('0xdd718d5cc53262d4', 1),
        ('0xc3fb9777d5cc63e1', 1),
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
    'authoring_version': 14,
    'impl_name': 'mangata-parachain',
    'impl_version': 0,
    'spec_name': 'mangata-parachain',
    'spec_version': 14,
    'state_version': 0,
    'transaction_version': 14,
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
### StorageQueueFull
the storage queue is empty and cannot accept any new txs

---------