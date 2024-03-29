
# System

---------
## Calls

---------
### kill_prefix
See [`Pallet::kill_prefix`].
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
See [`Pallet::kill_storage`].
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
See [`Pallet::remark`].
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
See [`Pallet::remark_with_event`].
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
See [`Pallet::set_code`].
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
See [`Pallet::set_code_without_checks`].
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
See [`Pallet::set_heap_pages`].
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
See [`Pallet::set_storage`].
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
| dispatch_error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}```
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
            'Consensus': ('[u8; 4]', 'Bytes'),
            'Other': 'Bytes',
            None: None,
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

 The value has the type `(BlockNumberFor&lt;T&gt;, EventIndex)` because if we used only just
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
            None: None,
            'AssetRegistry': {
                'AssetBanned': {'asset_id': 'u32'},
                'AssetUnbanned': {'asset_id': 'u32'},
                'ExistentialDepositPaid': {
                    'amount': 'u128',
                    'fee_asset': 'u32',
                    'who': 'AccountId',
                },
                'LocationSet': {
                    'asset_id': 'u32',
                    'location': 'scale_info::69',
                },
                'Registered': {
                    'asset_id': 'u32',
                    'asset_name': (None, 'Bytes'),
                    'asset_type': 'scale_info::66',
                    'decimals': (None, 'u8'),
                    'existential_deposit': 'u128',
                    'is_sufficient': 'bool',
                    'symbol': (None, 'Bytes'),
                    'xcm_rate_limit': (None, 'u128'),
                },
                'Updated': {
                    'asset_id': 'u32',
                    'asset_name': (None, 'Bytes'),
                    'asset_type': 'scale_info::66',
                    'decimals': (None, 'u8'),
                    'existential_deposit': 'u128',
                    'is_sufficient': 'bool',
                    'symbol': (None, 'Bytes'),
                    'xcm_rate_limit': (None, 'u128'),
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
                    'destination_status': 'scale_info::31',
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
                'InvalidInvulnerableSkipped': {'account_id': 'AccountId'},
                'InvulnerableAdded': {'account_id': 'AccountId'},
                'InvulnerableRemoved': {'account_id': 'AccountId'},
                'NewCandidacyBond': {'bond_amount': 'u128'},
                'NewDesiredCandidates': {'desired_candidates': 'u32'},
                'NewInvulnerables': {'invulnerables': ['AccountId']},
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
                    'result': 'scale_info::35',
                },
                'MemberExecuted': {
                    'proposal_hash': 'scale_info::12',
                    'result': 'scale_info::35',
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
                'ExecutedDownward': ('[u8; 32]', 'scale_info::148'),
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
                    'error': 'scale_info::25',
                },
                'Scheduled': {
                    'id': 'u32',
                    'order': 'scale_info::142',
                    'period': 'u32',
                    'total_amount': 'u128',
                    'who': 'AccountId',
                },
                'Terminated': {
                    'error': 'scale_info::25',
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
                    'error': 'scale_info::25',
                    'id': 'u32',
                    'who': 'AccountId',
                },
            },
            'Democracy': {
                'Blacklisted': {'proposal_hash': 'scale_info::12'},
                'Cancelled': {'ref_index': 'u32'},
                'Delegated': {'target': 'AccountId', 'who': 'AccountId'},
                'ExternalTabled': None,
                'MetadataCleared': {
                    'hash': 'scale_info::12',
                    'owner': 'scale_info::43',
                },
                'MetadataSet': {
                    'hash': 'scale_info::12',
                    'owner': 'scale_info::43',
                },
                'MetadataTransferred': {
                    'hash': 'scale_info::12',
                    'owner': 'scale_info::43',
                    'prev_owner': 'scale_info::43',
                },
                'NotPassed': {'ref_index': 'u32'},
                'Passed': {'ref_index': 'u32'},
                'ProposalCanceled': {'prop_index': 'u32'},
                'Proposed': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Seconded': {'prop_index': 'u32', 'seconder': 'AccountId'},
                'Started': {'ref_index': 'u32', 'threshold': 'scale_info::40'},
                'Tabled': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Undelegated': {'account': 'AccountId'},
                'Vetoed': {
                    'proposal_hash': 'scale_info::12',
                    'until': 'u32',
                    'who': 'AccountId',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::41',
                    'voter': 'AccountId',
                },
            },
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_hash': '[u8; 32]',
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::148',
                },
                'InvalidFormat': {'message_hash': '[u8; 32]'},
                'MaxMessagesExhausted': {'message_hash': '[u8; 32]'},
                'OverweightEnqueued': {
                    'message_hash': '[u8; 32]',
                    'message_id': '[u8; 32]',
                    'overweight_index': 'u64',
                    'required_weight': 'scale_info::9',
                },
                'OverweightServiced': {
                    'overweight_index': 'u64',
                    'weight_used': 'scale_info::9',
                },
                'UnsupportedVersion': {'message_hash': '[u8; 32]'},
                'WeightExhausted': {
                    'message_hash': '[u8; 32]',
                    'message_id': '[u8; 32]',
                    'remaining_weight': 'scale_info::9',
                    'required_weight': 'scale_info::9',
                },
            },
            'Duster': {
                'Added': {'who': 'AccountId'},
                'Dusted': {'amount': 'u128', 'who': 'AccountId'},
                'Removed': {'who': 'AccountId'},
            },
            'DynamicFees': (),
            'EVM': {
                'Created': {'address': '[u8; 20]'},
                'CreatedFailed': {'address': '[u8; 20]'},
                'Executed': {'address': '[u8; 20]'},
                'ExecutedFailed': {'address': '[u8; 20]'},
                'Log': {'log': 'scale_info::125'},
            },
            'EVMAccounts': {
                'Bound': {'account': 'AccountId', 'address': '[u8; 20]'},
                'DeployerAdded': {'who': '[u8; 20]'},
                'DeployerRemoved': {'who': '[u8; 20]'},
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
            'EmaOracle': (),
            'Ethereum': {
                'Executed': {
                    'exit_reason': 'scale_info::129',
                    'extra_data': 'Bytes',
                    'from': '[u8; 20]',
                    'to': '[u8; 20]',
                    'transaction_hash': 'scale_info::12',
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
                    'data': 'scale_info::108',
                    'pool': 'AccountId',
                },
                'PoolUpdated': {
                    'data': 'scale_info::108',
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
                    'result': 'scale_info::35',
                    'timepoint': 'scale_info::55',
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
                    'hub_amount_in': 'u128',
                    'hub_amount_out': 'u128',
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
                'ProtocolLiquidityRemoved': {
                    'amount': 'u128',
                    'asset_id': 'u32',
                    'hub_amount': 'u128',
                    'shares_removed': 'u128',
                    'who': 'AccountId',
                },
                'SellExecuted': {
                    'amount_in': 'u128',
                    'amount_out': 'u128',
                    'asset_fee_amount': 'u128',
                    'asset_in': 'u32',
                    'asset_out': 'u32',
                    'hub_amount_in': 'u128',
                    'hub_amount_out': 'u128',
                    'protocol_fee_amount': 'u128',
                    'who': 'AccountId',
                },
                'TokenAdded': {
                    'asset_id': 'u32',
                    'initial_amount': 'u128',
                    'initial_price': 'u128',
                },
                'TokenRemoved': {
                    'amount': 'u128',
                    'asset_id': 'u32',
                    'hub_withdrawn': 'u128',
                },
                'TradableStateUpdated': {
                    'asset_id': 'u32',
                    'state': 'scale_info::84',
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
                    'loyalty_curve': (None, 'scale_info::92'),
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
                'Sent': {'message': ['scale_info::152'], 'to': 'scale_info::69'},
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
            'PolkadotXcm': {
                'AssetsClaimed': {
                    'assets': 'scale_info::177',
                    'hash': 'scale_info::12',
                    'origin': 'scale_info::69',
                },
                'AssetsTrapped': {
                    'assets': 'scale_info::177',
                    'hash': 'scale_info::12',
                    'origin': 'scale_info::69',
                },
                'Attempted': {'outcome': 'scale_info::148'},
                'FeesPaid': {'fees': ['scale_info::155'], 'paying': 'scale_info::69'},
                'InvalidQuerier': {
                    'expected_querier': 'scale_info::69',
                    'maybe_actual_querier': (None, 'scale_info::69'),
                    'origin': 'scale_info::69',
                    'query_id': 'u64',
                },
                'InvalidQuerierVersion': {
                    'origin': 'scale_info::69',
                    'query_id': 'u64',
                },
                'InvalidResponder': {
                    'expected_location': (None, 'scale_info::69'),
                    'origin': 'scale_info::69',
                    'query_id': 'u64',
                },
                'InvalidResponderVersion': {
                    'origin': 'scale_info::69',
                    'query_id': 'u64',
                },
                'Notified': {
                    'call_index': 'u8',
                    'pallet_index': 'u8',
                    'query_id': 'u64',
                },
                'NotifyDecodeFailed': {
                    'call_index': 'u8',
                    'pallet_index': 'u8',
                    'query_id': 'u64',
                },
                'NotifyDispatchError': {
                    'call_index': 'u8',
                    'pallet_index': 'u8',
                    'query_id': 'u64',
                },
                'NotifyOverweight': {
                    'actual_weight': 'scale_info::9',
                    'call_index': 'u8',
                    'max_budgeted_weight': 'scale_info::9',
                    'pallet_index': 'u8',
                    'query_id': 'u64',
                },
                'NotifyTargetMigrationFail': {
                    'location': 'scale_info::191',
                    'query_id': 'u64',
                },
                'NotifyTargetSendFail': {
                    'error': 'scale_info::149',
                    'location': 'scale_info::69',
                    'query_id': 'u64',
                },
                'ResponseReady': {
                    'query_id': 'u64',
                    'response': 'scale_info::160',
                },
                'ResponseTaken': {'query_id': 'u64'},
                'Sent': {
                    'destination': 'scale_info::69',
                    'message': ['scale_info::152'],
                    'message_id': '[u8; 32]',
                    'origin': 'scale_info::69',
                },
                'SupportedVersionChanged': {
                    'location': 'scale_info::69',
                    'version': 'u32',
                },
                'UnexpectedResponse': {
                    'origin': 'scale_info::69',
                    'query_id': 'u64',
                },
                'VersionChangeNotified': {
                    'cost': ['scale_info::155'],
                    'destination': 'scale_info::69',
                    'message_id': '[u8; 32]',
                    'result': 'u32',
                },
                'VersionNotifyRequested': {
                    'cost': ['scale_info::155'],
                    'destination': 'scale_info::69',
                    'message_id': '[u8; 32]',
                },
                'VersionNotifyStarted': {
                    'cost': ['scale_info::155'],
                    'destination': 'scale_info::69',
                    'message_id': '[u8; 32]',
                },
                'VersionNotifyUnrequested': {
                    'cost': ['scale_info::155'],
                    'destination': 'scale_info::69',
                    'message_id': '[u8; 32]',
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
                    'proxy_type': 'scale_info::52',
                },
                'ProxyExecuted': {'result': 'scale_info::35'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::52',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::52',
                    'pure': 'AccountId',
                    'who': 'AccountId',
                },
            },
            'Referrals': {
                'AssetRewardsUpdated': {
                    'asset_id': 'u32',
                    'level': 'scale_info::115',
                    'rewards': 'scale_info::116',
                },
                'Claimed': {
                    'referrer_rewards': 'u128',
                    'trade_rewards': 'u128',
                    'who': 'AccountId',
                },
                'CodeLinked': {
                    'account': 'AccountId',
                    'code': 'Bytes',
                    'referral_account': 'AccountId',
                },
                'CodeRegistered': {'account': 'AccountId', 'code': 'Bytes'},
                'Converted': {
                    'from': 'scale_info::114',
                    'to': 'scale_info::114',
                },
                'LevelUp': {'level': 'scale_info::115', 'who': 'AccountId'},
            },
            'RelayChainInfo': {
                'CurrentBlockNumbers': {
                    'parachain_block_number': 'u32',
                    'relaychain_block_number': 'u32',
                },
            },
            'Router': {
                'Executed': {
                    'amount_in': 'u128',
                    'amount_out': 'u128',
                    'asset_in': 'u32',
                    'asset_out': 'u32',
                },
                'RouteUpdated': {'asset_ids': ['u32']},
            },
            'Scheduler': {
                'CallUnavailable': {
                    'id': (None, '[u8; 32]'),
                    'task': ('u32', 'u32'),
                },
                'Canceled': {'index': 'u32', 'when': 'u32'},
                'Dispatched': {
                    'id': (None, '[u8; 32]'),
                    'result': 'scale_info::35',
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
                    'assets': ['scale_info::104'],
                    'pool_id': 'u32',
                    'shares': 'u128',
                    'who': 'AccountId',
                },
                'LiquidityRemoved': {
                    'amounts': ['scale_info::104'],
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
                    'state': 'scale_info::105',
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
                    'result': 'scale_info::35',
                },
                'MemberExecuted': {
                    'proposal_hash': 'scale_info::12',
                    'result': 'scale_info::35',
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
            'Tips': {
                'NewTip': {'tip_hash': 'scale_info::12'},
                'TipClosed': {
                    'payout': 'u128',
                    'tip_hash': 'scale_info::12',
                    'who': 'AccountId',
                },
                'TipClosing': {'tip_hash': 'scale_info::12'},
                'TipRetracted': {'tip_hash': 'scale_info::12'},
                'TipSlashed': {
                    'deposit': 'u128',
                    'finder': 'AccountId',
                    'tip_hash': 'scale_info::12',
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
                'Issued': {'amount': 'u128', 'currency_id': 'u32'},
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
                'Rescinded': {'amount': 'u128', 'currency_id': 'u32'},
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'currency_id': 'u32',
                    'from': 'AccountId',
                    'status': 'scale_info::31',
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
                    'asset': 'scale_info::155',
                    'who': 'scale_info::69',
                },
                'Withdrawn': {
                    'asset': 'scale_info::155',
                    'who': 'scale_info::69',
                },
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::25',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::35'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::25'},
            },
            'Vesting': {
                'Claimed': {'amount': 'u128', 'who': 'AccountId'},
                'VestingScheduleAdded': {
                    'from': 'AccountId',
                    'to': 'AccountId',
                    'vesting_schedule': 'scale_info::123',
                },
                'VestingSchedulesUpdated': {'who': 'AccountId'},
            },
            'XTokens': {
                'TransferredMultiAssets': {
                    'assets': ['scale_info::155'],
                    'dest': 'scale_info::69',
                    'fee': 'scale_info::155',
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
            'XcmRateLimiter': (),
            'XcmpQueue': {
                'BadFormat': {'message_hash': '[u8; 32]'},
                'BadVersion': {'message_hash': '[u8; 32]'},
                'DeferredBucketDiscarded': {'index': ('u32', 'u16'), 'sender': 'u32'},
                'DeferredXcmDiscarded': {
                    'deferred_to': 'u32',
                    'index': ('u32', 'u16'),
                    'message_hash': (None, '[u8; 32]'),
                    'position': 'u32',
                    'sender': 'u32',
                    'sent_at': 'u32',
                },
                'Fail': {
                    'error': 'scale_info::149',
                    'message_hash': '[u8; 32]',
                    'message_id': '[u8; 32]',
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
                'Success': {
                    'message_hash': '[u8; 32]',
                    'message_id': '[u8; 32]',
                    'weight': 'scale_info::9',
                },
                'XcmDeferred': {
                    'deferred_to': 'u32',
                    'index': ('u32', 'u16'),
                    'message_hash': (None, '[u8; 32]'),
                    'position': 'u32',
                    'sender': 'u32',
                    'sent_at': 'u32',
                },
                'XcmDeferredQueueFull': {
                    'message_hash': (None, '[u8; 32]'),
                    'sender': 'u32',
                    'sent_at': 'u32',
                },
                'XcmpMessageSent': {'message_hash': '[u8; 32]'},
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
    'base_block': {'proof_size': 0, 'ref_time': 390584000},
    'max_block': {'proof_size': 5242880, 'ref_time': 500000000000},
    'per_class': {
        'mandatory': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 124414000},
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 124414000},
            'max_extrinsic': {'proof_size': 3801088, 'ref_time': 362375586000},
            'max_total': {'proof_size': 3932160, 'ref_time': 375000000000},
            'reserved': {'proof_size': 0, 'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 124414000},
            'max_extrinsic': {'proof_size': 5111808, 'ref_time': 487375586000},
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
        ('0x37e397fc7c91f5e4', 2),
        ('0x40fe3ad401f8959a', 6),
        ('0xd2bc9897eed08f15', 3),
        ('0xf78b278be53f454c', 2),
        ('0xab3c0572291feb8b', 1),
        ('0xdd718d5cc53262d4', 1),
        ('0xea93e3f16f3d6962', 2),
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 4),
        ('0x582211f65bb14b89', 5),
        ('0xe65b00e46cedd0aa', 2),
        ('0x0bb67a52fcd040ff', 1),
    ],
    'authoring_version': 1,
    'impl_name': 'hydradx',
    'impl_version': 0,
    'spec_name': 'hydradx',
    'spec_version': 224,
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