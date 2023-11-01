
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
            None: None,
            'AssetRegistry': {
                'LocationSet': {
                    'asset_id': 'u32',
                    'location': 'scale_info::65',
                },
                'MetadataSet': {
                    'asset_id': 'u32',
                    'decimals': 'u8',
                    'symbol': 'Bytes',
                },
                'Registered': {
                    'asset_id': 'u32',
                    'asset_name': 'Bytes',
                    'asset_type': 'scale_info::63',
                },
                'Updated': {
                    'asset_id': 'u32',
                    'asset_name': 'Bytes',
                    'asset_type': 'scale_info::63',
                    'existential_deposit': 'u128',
                    'xcm_rate_limit': (None, 'u128'),
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
                    'destination_status': 'scale_info::30',
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
            'Bonds': {
                'Issued': {
                    'amount': 'u128',
                    'bond_id': 'u32',
                    'fee': 'u128',
                    'issuer': 'AccountId',
                },
                'Redeemed': {
                    'amount': 'u128',
                    'bond_id': 'u32',
                    'who': 'AccountId',
                },
                'TokenCreated': {
                    'asset_id': 'u32',
                    'bond_id': 'u32',
                    'issuer': 'AccountId',
                    'maturity': 'u64',
                },
            },
            'CircuitBreaker': {
                'AddLiquidityLimitChanged': {
                    'asset_id': 'u32',
                    'liquidity_limit': (None, ('u32', 'u32')),
                },
                'RemoveLiquidityLimitChanged': {
                    'asset_id': 'u32',
                    'liquidity_limit': (None, ('u32', 'u32')),
                },
                'TradeVolumeLimitChanged': {
                    'asset_id': 'u32',
                    'trade_volume_limit': ('u32', 'u32'),
                },
            },
            'Claims': {'Claim': ('AccountId', '[u8; 20]', 'u128')},
            'CollatorRewards': {
                'CollatorRewarded': {
                    'amount': 'u128',
                    'currency': 'u32',
                    'who': 'AccountId',
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
                    'result': 'scale_info::34',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::34',
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
                'ExecutedDownward': ('[u8; 32]', 'scale_info::119'),
                'InvalidFormat': '[u8; 32]',
                'UnsupportedVersion': '[u8; 32]',
            },
            'Currencies': {
                'BalanceUpdated': {
                    'amount': 'i128',
                    'currency_id': 'u32',
                    'who': 'AccountId',
                },
                'Deposited': {
                    'amount': 'u128',
                    'currency_id': 'u32',
                    'who': 'AccountId',
                },
                'Transferred': {
                    'amount': 'u128',
                    'currency_id': 'u32',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Withdrawn': {
                    'amount': 'u128',
                    'currency_id': 'u32',
                    'who': 'AccountId',
                },
            },
            'DCA': {
                'Completed': {'id': 'u32', 'who': 'AccountId'},
                'ExecutionPlanned': {
                    'block': 'u32',
                    'id': 'u32',
                    'who': 'AccountId',
                },
                'ExecutionStarted': {'block': 'u32', 'id': 'u32'},
                'RandomnessGenerationFailed': {
                    'block': 'u32',
                    'error': 'scale_info::24',
                },
                'Scheduled': {'id': 'u32', 'who': 'AccountId'},
                'Terminated': {
                    'error': 'scale_info::24',
                    'id': 'u32',
                    'who': 'AccountId',
                },
                'TradeExecuted': {
                    'amount_in': 'u128',
                    'amount_out': 'u128',
                    'id': 'u32',
                    'who': 'AccountId',
                },
                'TradeFailed': {
                    'error': 'scale_info::24',
                    'id': 'u32',
                    'who': 'AccountId',
                },
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
                'Started': {'ref_index': 'u32', 'threshold': 'scale_info::39'},
                'Tabled': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Undelegated': {'account': 'AccountId'},
                'Vetoed': {
                    'proposal_hash': '[u8; 32]',
                    'until': 'u32',
                    'who': 'AccountId',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::40',
                    'voter': 'AccountId',
                },
            },
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::119',
                },
                'InvalidFormat': {'message_id': '[u8; 32]'},
                'MaxMessagesExhausted': {'message_id': '[u8; 32]'},
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
            'Duster': {
                'Added': {'who': 'AccountId'},
                'Dusted': {'amount': 'u128', 'who': 'AccountId'},
                'Removed': {'who': 'AccountId'},
            },
            'DynamicFees': (),
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
            'EmaOracle': (),
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
            'LBP': {
                'BuyExecuted': {
                    'amount': 'u128',
                    'asset_in': 'u32',
                    'asset_out': 'u32',
                    'buy_price': 'u128',
                    'fee_amount': 'u128',
                    'fee_asset': 'u32',
                    'who': 'AccountId',
                },
                'LiquidityAdded': {
                    'amount_a': 'u128',
                    'amount_b': 'u128',
                    'asset_a': 'u32',
                    'asset_b': 'u32',
                    'who': 'AccountId',
                },
                'LiquidityRemoved': {
                    'amount_a': 'u128',
                    'amount_b': 'u128',
                    'asset_a': 'u32',
                    'asset_b': 'u32',
                    'who': 'AccountId',
                },
                'PoolCreated': {
                    'data': 'scale_info::104',
                    'pool': 'AccountId',
                },
                'PoolUpdated': {
                    'data': 'scale_info::104',
                    'pool': 'AccountId',
                },
                'SellExecuted': {
                    'amount': 'u128',
                    'asset_in': 'u32',
                    'asset_out': 'u32',
                    'fee_amount': 'u128',
                    'fee_asset': 'u32',
                    'sale_price': 'u128',
                    'who': 'AccountId',
                },
            },
            'MultiTransactionPayment': {
                'CurrencyAdded': {'asset_id': 'u32'},
                'CurrencyRemoved': {'asset_id': 'u32'},
                'CurrencySet': {'account_id': 'AccountId', 'asset_id': 'u32'},
                'FeeWithdrawn': {
                    'account_id': 'AccountId',
                    'asset_id': 'u32',
                    'destination_account_id': 'AccountId',
                    'native_fee_amount': 'u128',
                    'non_native_fee_amount': 'u128',
                },
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::53',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::53',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::34',
                    'timepoint': 'scale_info::53',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'OTC': {
                'Cancelled': {'order_id': 'u32'},
                'Filled': {
                    'amount_in': 'u128',
                    'amount_out': 'u128',
                    'order_id': 'u32',
                    'who': 'AccountId',
                },
                'PartiallyFilled': {
                    'amount_in': 'u128',
                    'amount_out': 'u128',
                    'order_id': 'u32',
                    'who': 'AccountId',
                },
                'Placed': {
                    'amount_in': 'u128',
                    'amount_out': 'u128',
                    'asset_in': 'u32',
                    'asset_out': 'u32',
                    'order_id': 'u32',
                    'partially_fillable': 'bool',
                },
            },
            'Omnipool': {
                'AssetRefunded': {
                    'amount': 'u128',
                    'asset_id': 'u32',
                    'recipient': 'AccountId',
                },
                'AssetWeightCapUpdated': {'asset_id': 'u32', 'cap': 'u32'},
                'BuyExecuted': {
                    'amount_in': 'u128',
                    'amount_out': 'u128',
                    'asset_fee_amount': 'u128',
                    'asset_in': 'u32',
                    'asset_out': 'u32',
                    'protocol_fee_amount': 'u128',
                    'who': 'AccountId',
                },
                'LiquidityAdded': {
                    'amount': 'u128',
                    'asset_id': 'u32',
                    'position_id': 'u128',
                    'who': 'AccountId',
                },
                'LiquidityRemoved': {
                    'asset_id': 'u32',
                    'fee': 'u128',
                    'position_id': 'u128',
                    'shares_removed': 'u128',
                    'who': 'AccountId',
                },
                'PositionCreated': {
                    'amount': 'u128',
                    'asset': 'u32',
                    'owner': 'AccountId',
                    'position_id': 'u128',
                    'price': 'u128',
                    'shares': 'u128',
                },
                'PositionDestroyed': {
                    'owner': 'AccountId',
                    'position_id': 'u128',
                },
                'PositionUpdated': {
                    'amount': 'u128',
                    'asset': 'u32',
                    'owner': 'AccountId',
                    'position_id': 'u128',
                    'price': 'u128',
                    'shares': 'u128',
                },
                'SellExecuted': {
                    'amount_in': 'u128',
                    'amount_out': 'u128',
                    'asset_fee_amount': 'u128',
                    'asset_in': 'u32',
                    'asset_out': 'u32',
                    'protocol_fee_amount': 'u128',
                    'who': 'AccountId',
                },
                'TVLCapUpdated': {'cap': 'u128'},
                'TokenAdded': {
                    'asset_id': 'u32',
                    'initial_amount': 'u128',
                    'initial_price': 'u128',
                },
                'TradableStateUpdated': {
                    'asset_id': 'u32',
                    'state': 'scale_info::80',
                },
            },
            'OmnipoolLiquidityMining': {
                'DepositDestroyed': {'deposit_id': 'u128', 'who': 'AccountId'},
                'GlobalFarmCreated': {
                    'blocks_per_period': 'u32',
                    'id': 'u32',
                    'lrna_price_adjustment': 'u128',
                    'max_reward_per_period': 'u128',
                    'min_deposit': 'u128',
                    'owner': 'AccountId',
                    'planned_yielding_periods': 'u32',
                    'reward_currency': 'u32',
                    'total_rewards': 'u128',
                    'yield_per_period': 'u64',
                },
                'GlobalFarmTerminated': {
                    'global_farm_id': 'u32',
                    'reward_currency': 'u32',
                    'undistributed_rewards': 'u128',
                    'who': 'AccountId',
                },
                'RewardClaimed': {
                    'claimed': 'u128',
                    'deposit_id': 'u128',
                    'global_farm_id': 'u32',
                    'reward_currency': 'u32',
                    'who': 'AccountId',
                    'yield_farm_id': 'u32',
                },
                'SharesDeposited': {
                    'asset_id': 'u32',
                    'deposit_id': 'u128',
                    'global_farm_id': 'u32',
                    'position_id': 'u128',
                    'shares_amount': 'u128',
                    'who': 'AccountId',
                    'yield_farm_id': 'u32',
                },
                'SharesRedeposited': {
                    'asset_id': 'u32',
                    'deposit_id': 'u128',
                    'global_farm_id': 'u32',
                    'position_id': 'u128',
                    'shares_amount': 'u128',
                    'who': 'AccountId',
                    'yield_farm_id': 'u32',
                },
                'SharesWithdrawn': {
                    'amount': 'u128',
                    'deposit_id': 'u128',
                    'global_farm_id': 'u32',
                    'who': 'AccountId',
                    'yield_farm_id': 'u32',
                },
                'YieldFarmCreated': {
                    'asset_id': 'u32',
                    'global_farm_id': 'u32',
                    'loyalty_curve': (None, 'scale_info::88'),
                    'multiplier': 'u128',
                    'yield_farm_id': 'u32',
                },
                'YieldFarmResumed': {
                    'asset_id': 'u32',
                    'global_farm_id': 'u32',
                    'multiplier': 'u128',
                    'who': 'AccountId',
                    'yield_farm_id': 'u32',
                },
                'YieldFarmStopped': {
                    'asset_id': 'u32',
                    'global_farm_id': 'u32',
                    'who': 'AccountId',
                    'yield_farm_id': 'u32',
                },
                'YieldFarmTerminated': {
                    'asset_id': 'u32',
                    'global_farm_id': 'u32',
                    'who': 'AccountId',
                    'yield_farm_id': 'u32',
                },
                'YieldFarmUpdated': {
                    'asset_id': 'u32',
                    'global_farm_id': 'u32',
                    'multiplier': 'u128',
                    'who': 'AccountId',
                    'yield_farm_id': 'u32',
                },
            },
            'OmnipoolWarehouseLM': {
                'AllRewardsDistributed': {'global_farm_id': 'u32'},
                'GlobalFarmAccRPZUpdated': {
                    'accumulated_rpz': 'u128',
                    'global_farm_id': 'u32',
                    'total_shares_z': 'u128',
                },
                'YieldFarmAccRPVSUpdated': {
                    'accumulated_rpvs': 'u128',
                    'global_farm_id': 'u32',
                    'total_valued_shares': 'u128',
                    'yield_farm_id': 'u32',
                },
            },
            'OrmlXcm': {
                'Sent': {'message': ['scale_info::123'], 'to': 'scale_info::65'},
            },
            'ParachainSystem': {
                'DownwardMessagesProcessed': {
                    'dmq_head': '[u8; 32]',
                    'weight_used': 'scale_info::8',
                },
                'DownwardMessagesReceived': {'count': 'u32'},
                'UpgradeAuthorized': {'code_hash': '[u8; 32]'},
                'UpwardMessageSent': {'message_hash': (None, '[u8; 32]')},
                'ValidationFunctionApplied': {'relay_chain_block_num': 'u32'},
                'ValidationFunctionDiscarded': None,
                'ValidationFunctionStored': None,
            },
            'PolkadotXcm': {
                'AssetsClaimed': (
                    '[u8; 32]',
                    'scale_info::65',
                    'scale_info::146',
                ),
                'AssetsTrapped': (
                    '[u8; 32]',
                    'scale_info::65',
                    'scale_info::146',
                ),
                'Attempted': {
                    'Complete': 'scale_info::8',
                    'Error': 'scale_info::120',
                    'Incomplete': ('scale_info::8', 'scale_info::120'),
                },
                'FeesPaid': ('scale_info::65', ['scale_info::126']),
                'InvalidQuerier': (
                    'scale_info::65',
                    'u64',
                    'scale_info::65',
                    (None, 'scale_info::65'),
                ),
                'InvalidQuerierVersion': ('scale_info::65', 'u64'),
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
                    'scale_info::8',
                    'scale_info::8',
                ),
                'NotifyTargetMigrationFail': ('scale_info::160', 'u64'),
                'NotifyTargetSendFail': (
                    'scale_info::65',
                    'u64',
                    'scale_info::120',
                ),
                'ResponseReady': ('u64', 'scale_info::131'),
                'ResponseTaken': 'u64',
                'Sent': (
                    'scale_info::65',
                    'scale_info::65',
                    ['scale_info::123'],
                ),
                'SupportedVersionChanged': ('scale_info::65', 'u32'),
                'UnexpectedResponse': ('scale_info::65', 'u64'),
                'VersionChangeNotified': (
                    'scale_info::65',
                    'u32',
                    ['scale_info::126'],
                ),
                'VersionNotifyRequested': (
                    'scale_info::65',
                    ['scale_info::126'],
                ),
                'VersionNotifyStarted': ('scale_info::65', ['scale_info::126']),
                'VersionNotifyUnrequested': (
                    'scale_info::65',
                    ['scale_info::126'],
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
                    'proxy_type': 'scale_info::50',
                },
                'ProxyExecuted': {'result': 'scale_info::34'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::50',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::50',
                    'pure': 'AccountId',
                    'who': 'AccountId',
                },
            },
            'RelayChainInfo': {
                'CurrentBlockNumbers': {
                    'parachain_block_number': 'u32',
                    'relaychain_block_number': 'u32',
                },
            },
            'Router': {
                'RouteExecuted': {
                    'amount_in': 'u128',
                    'amount_out': 'u128',
                    'asset_in': 'u32',
                    'asset_out': 'u32',
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
                    'result': 'scale_info::34',
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
            'Stableswap': {
                'AmplificationChanging': {
                    'current_amplification': 'u16',
                    'end_block': 'u32',
                    'final_amplification': 'u16',
                    'pool_id': 'u32',
                    'start_block': 'u32',
                },
                'BuyExecuted': {
                    'amount_in': 'u128',
                    'amount_out': 'u128',
                    'asset_in': 'u32',
                    'asset_out': 'u32',
                    'fee': 'u128',
                    'pool_id': 'u32',
                    'who': 'AccountId',
                },
                'FeeUpdated': {'fee': 'u32', 'pool_id': 'u32'},
                'LiquidityAdded': {
                    'assets': ['scale_info::100'],
                    'pool_id': 'u32',
                    'shares': 'u128',
                    'who': 'AccountId',
                },
                'LiquidityRemoved': {
                    'amounts': ['scale_info::100'],
                    'fee': 'u128',
                    'pool_id': 'u32',
                    'shares': 'u128',
                    'who': 'AccountId',
                },
                'PoolCreated': {
                    'amplification': 'u16',
                    'assets': ['u32'],
                    'fee': 'u32',
                    'pool_id': 'u32',
                },
                'SellExecuted': {
                    'amount_in': 'u128',
                    'amount_out': 'u128',
                    'asset_in': 'u32',
                    'asset_out': 'u32',
                    'fee': 'u128',
                    'pool_id': 'u32',
                    'who': 'AccountId',
                },
                'TradableStateUpdated': {
                    'asset_id': 'u32',
                    'pool_id': 'u32',
                    'state': 'scale_info::101',
                },
            },
            'Staking': {
                'AccumulatedRpsUpdated': {
                    'accumulated_rps': 'u128',
                    'total_stake': 'u128',
                },
                'PositionCreated': {
                    'position_id': 'u128',
                    'stake': 'u128',
                    'who': 'AccountId',
                },
                'RewardsClaimed': {
                    'paid_rewards': 'u128',
                    'payable_percentage': 'u128',
                    'position_id': 'u128',
                    'slashed_points': 'u128',
                    'slashed_unpaid_rewards': 'u128',
                    'unlocked_rewards': 'u128',
                    'who': 'AccountId',
                },
                'StakeAdded': {
                    'locked_rewards': 'u128',
                    'payable_percentage': 'u128',
                    'position_id': 'u128',
                    'slashed_points': 'u128',
                    'stake': 'u128',
                    'total_stake': 'u128',
                    'who': 'AccountId',
                },
                'StakingInitialized': {'non_dustable_balance': 'u128'},
                'Unstaked': {
                    'position_id': 'u128',
                    'unlocked_stake': 'u128',
                    'who': 'AccountId',
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
                    'result': 'scale_info::34',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::34',
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
                'Locked': {
                    'amount': 'u128',
                    'currency_id': 'u32',
                    'who': 'AccountId',
                },
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'currency_id': 'u32',
                    'from': 'AccountId',
                    'status': 'scale_info::30',
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
                'Unlocked': {
                    'amount': 'u128',
                    'currency_id': 'u32',
                    'who': 'AccountId',
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
                'UpdatedInactive': {
                    'deactivated': 'u128',
                    'reactivated': 'u128',
                },
            },
            'Uniques': {
                'ApprovalCancelled': {
                    'collection': 'u128',
                    'delegate': 'AccountId',
                    'item': 'u128',
                    'owner': 'AccountId',
                },
                'ApprovedTransfer': {
                    'collection': 'u128',
                    'delegate': 'AccountId',
                    'item': 'u128',
                    'owner': 'AccountId',
                },
                'AttributeCleared': {
                    'collection': 'u128',
                    'key': 'Bytes',
                    'maybe_item': (None, 'u128'),
                },
                'AttributeSet': {
                    'collection': 'u128',
                    'key': 'Bytes',
                    'maybe_item': (None, 'u128'),
                    'value': 'Bytes',
                },
                'Burned': {
                    'collection': 'u128',
                    'item': 'u128',
                    'owner': 'AccountId',
                },
                'CollectionFrozen': {'collection': 'u128'},
                'CollectionMaxSupplySet': {
                    'collection': 'u128',
                    'max_supply': 'u32',
                },
                'CollectionMetadataCleared': {'collection': 'u128'},
                'CollectionMetadataSet': {
                    'collection': 'u128',
                    'data': 'Bytes',
                    'is_frozen': 'bool',
                },
                'CollectionThawed': {'collection': 'u128'},
                'Created': {
                    'collection': 'u128',
                    'creator': 'AccountId',
                    'owner': 'AccountId',
                },
                'Destroyed': {'collection': 'u128'},
                'ForceCreated': {'collection': 'u128', 'owner': 'AccountId'},
                'Frozen': {'collection': 'u128', 'item': 'u128'},
                'Issued': {
                    'collection': 'u128',
                    'item': 'u128',
                    'owner': 'AccountId',
                },
                'ItemBought': {
                    'buyer': 'AccountId',
                    'collection': 'u128',
                    'item': 'u128',
                    'price': 'u128',
                    'seller': 'AccountId',
                },
                'ItemPriceRemoved': {'collection': 'u128', 'item': 'u128'},
                'ItemPriceSet': {
                    'collection': 'u128',
                    'item': 'u128',
                    'price': 'u128',
                    'whitelisted_buyer': (None, 'AccountId'),
                },
                'ItemStatusChanged': {'collection': 'u128'},
                'MetadataCleared': {'collection': 'u128', 'item': 'u128'},
                'MetadataSet': {
                    'collection': 'u128',
                    'data': 'Bytes',
                    'is_frozen': 'bool',
                    'item': 'u128',
                },
                'OwnerChanged': {
                    'collection': 'u128',
                    'new_owner': 'AccountId',
                },
                'OwnershipAcceptanceChanged': {
                    'maybe_collection': (None, 'u128'),
                    'who': 'AccountId',
                },
                'Redeposited': {
                    'collection': 'u128',
                    'successful_items': ['u128'],
                },
                'TeamChanged': {
                    'admin': 'AccountId',
                    'collection': 'u128',
                    'freezer': 'AccountId',
                    'issuer': 'AccountId',
                },
                'Thawed': {'collection': 'u128', 'item': 'u128'},
                'Transferred': {
                    'collection': 'u128',
                    'from': 'AccountId',
                    'item': 'u128',
                    'to': 'AccountId',
                },
            },
            'UnknownTokens': {
                'Deposited': {
                    'asset': 'scale_info::126',
                    'who': 'scale_info::65',
                },
                'Withdrawn': {
                    'asset': 'scale_info::126',
                    'who': 'scale_info::65',
                },
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::24',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::34'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::24'},
            },
            'Vesting': {
                'Claimed': {'amount': 'u128', 'who': 'AccountId'},
                'VestingScheduleAdded': {
                    'from': 'AccountId',
                    'to': 'AccountId',
                    'vesting_schedule': 'scale_info::113',
                },
                'VestingSchedulesUpdated': {'who': 'AccountId'},
            },
            'XTokens': {
                'TransferredMultiAssets': {
                    'assets': ['scale_info::126'],
                    'dest': 'scale_info::65',
                    'fee': 'scale_info::126',
                    'sender': 'AccountId',
                },
            },
            'XYK': {
                'BuyExecuted': {
                    'amount': 'u128',
                    'asset_in': 'u32',
                    'asset_out': 'u32',
                    'buy_price': 'u128',
                    'fee_amount': 'u128',
                    'fee_asset': 'u32',
                    'pool': 'AccountId',
                    'who': 'AccountId',
                },
                'LiquidityAdded': {
                    'amount_a': 'u128',
                    'amount_b': 'u128',
                    'asset_a': 'u32',
                    'asset_b': 'u32',
                    'who': 'AccountId',
                },
                'LiquidityRemoved': {
                    'asset_a': 'u32',
                    'asset_b': 'u32',
                    'shares': 'u128',
                    'who': 'AccountId',
                },
                'PoolCreated': {
                    'asset_a': 'u32',
                    'asset_b': 'u32',
                    'initial_shares_amount': 'u128',
                    'pool': 'AccountId',
                    'share_token': 'u32',
                    'who': 'AccountId',
                },
                'PoolDestroyed': {
                    'asset_a': 'u32',
                    'asset_b': 'u32',
                    'pool': 'AccountId',
                    'share_token': 'u32',
                    'who': 'AccountId',
                },
                'SellExecuted': {
                    'amount': 'u128',
                    'asset_in': 'u32',
                    'asset_out': 'u32',
                    'fee_amount': 'u128',
                    'fee_asset': 'u32',
                    'pool': 'AccountId',
                    'sale_price': 'u128',
                    'who': 'AccountId',
                },
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': (None, '[u8; 32]')},
                'BadVersion': {'message_hash': (None, '[u8; 32]')},
                'Fail': {
                    'error': 'scale_info::120',
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
                'XcmDeferred': {
                    'deferred_to': 'u32',
                    'message_hash': (None, '[u8; 32]'),
                    'sender': 'u32',
                    'sent_at': 'u32',
                },
                'XcmDeferredQueueFull': None,
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
    'base_block': {'proof_size': 0, 'ref_time': 381015000},
    'max_block': {'proof_size': 5242880, 'ref_time': 500000000000},
    'per_class': {
        'mandatory': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 99840000},
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 99840000},
            'max_extrinsic': {'proof_size': 3801088, 'ref_time': 362400160000},
            'max_total': {'proof_size': 3932160, 'ref_time': 375000000000},
            'reserved': {'proof_size': 0, 'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 99840000},
            'max_extrinsic': {'proof_size': 5111808, 'ref_time': 487400160000},
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
63
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
        ('0x37c8bb1350a9a2a8', 3),
    ],
    'authoring_version': 1,
    'impl_name': 'hydradx',
    'impl_version': 0,
    'spec_name': 'hydradx',
    'spec_version': 183,
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