
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
                'RegisteredAsset': {
                    'asset_id': 'u32',
                    'metadata': 'scale_info::61',
                },
                'UpdatedAsset': {
                    'asset_id': 'u32',
                    'metadata': 'scale_info::61',
                },
            },
            'BTCRelay': {
                'ChainReorg': {
                    'fork_depth': 'u32',
                    'new_chain_tip_hash': 'scale_info::95',
                    'new_chain_tip_height': 'u32',
                },
                'ForkAheadOfMainChain': {
                    'fork_height': 'u32',
                    'fork_id': 'u32',
                    'main_chain_height': 'u32',
                },
                'Initialized': {
                    'block_hash': 'scale_info::95',
                    'block_height': 'u32',
                    'relayer_id': 'AccountId',
                },
                'StoreForkHeader': {
                    'block_hash': 'scale_info::95',
                    'chain_id': 'u32',
                    'fork_height': 'u32',
                    'relayer_id': 'AccountId',
                },
                'StoreMainChainHeader': {
                    'block_hash': 'scale_info::95',
                    'block_height': 'u32',
                    'relayer_id': 'AccountId',
                },
            },
            'BaseFee': {
                'BaseFeeOverflow': None,
                'NewBaseFeePerGas': {'fee': '[u64; 4]'},
                'NewElasticity': {'elasticity': 'u32'},
            },
            'ClientsInfo': {
                'ApplyClientRelease': {'release': 'scale_info::119'},
                'NotifyClientRelease': {'release': 'scale_info::119'},
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
            'CumulusXcm': {
                'ExecutedDownward': ('[u8; 32]', 'scale_info::132'),
                'InvalidFormat': '[u8; 32]',
                'UnsupportedVersion': '[u8; 32]',
            },
            'Democracy': {
                'Cancelled': {'ref_index': 'u32'},
                'CancelledProposal': {'prop_index': 'u32'},
                'FastTrack': {'ref_index': 'u32'},
                'FastTrackReferendum': {'ref_index': 'u32'},
                'NotPassed': {'ref_index': 'u32'},
                'Passed': {'ref_index': 'u32'},
                'Proposed': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Started': {
                    'ref_index': 'u32',
                    'threshold': 'scale_info::121',
                },
                'Tabled': {'deposit': 'u128', 'proposal_index': 'u32'},
            },
            'DexGeneral': {
                'AssetSwap': {
                    'balances': ['u128'],
                    'owner': 'AccountId',
                    'recipient': 'AccountId',
                    'swap_path': ['scale_info::51'],
                },
                'BootstrapClaim': {
                    'asset_0': 'scale_info::51',
                    'asset_0_refund': 'u128',
                    'asset_1': 'scale_info::51',
                    'asset_1_refund': 'u128',
                    'bootstrap_pair_account': 'AccountId',
                    'claimer': 'AccountId',
                    'lp_amount': 'u128',
                    'receiver': 'AccountId',
                },
                'BootstrapContribute': {
                    'asset_0': 'scale_info::51',
                    'asset_0_contribute': 'u128',
                    'asset_1': 'scale_info::51',
                    'asset_1_contribute': 'u128',
                    'who': 'AccountId',
                },
                'BootstrapCreated': {
                    'asset_0': 'scale_info::51',
                    'asset_1': 'scale_info::51',
                    'bootstrap_pair_account': 'AccountId',
                    'capacity_supply_0': 'u128',
                    'capacity_supply_1': 'u128',
                    'end': 'u32',
                    'total_supply_0': 'u128',
                    'total_supply_1': 'u128',
                },
                'BootstrapEnd': {
                    'asset_0': 'scale_info::51',
                    'asset_0_amount': 'u128',
                    'asset_1': 'scale_info::51',
                    'asset_1_amount': 'u128',
                    'total_lp_supply': 'u128',
                },
                'BootstrapRefund': {
                    'asset_0': 'scale_info::51',
                    'asset_0_refund': 'u128',
                    'asset_1': 'scale_info::51',
                    'asset_1_refund': 'u128',
                    'bootstrap_pair_account': 'AccountId',
                    'caller': 'AccountId',
                },
                'BootstrapUpdate': {
                    'asset_0': 'scale_info::51',
                    'asset_1': 'scale_info::51',
                    'bootstrap_pair_account': 'AccountId',
                    'capacity_supply_0': 'u128',
                    'capacity_supply_1': 'u128',
                    'end': 'u32',
                    'total_supply_0': 'u128',
                    'total_supply_1': 'u128',
                },
                'ChargeReward': {
                    'asset_0': 'scale_info::51',
                    'asset_1': 'scale_info::51',
                    'charge_rewards': [('scale_info::51', 'u128')],
                    'who': 'AccountId',
                },
                'DistributeReward': {
                    'asset_0': 'scale_info::51',
                    'asset_1': 'scale_info::51',
                    'reward_holder': 'AccountId',
                    'rewards': [('scale_info::51', 'u128')],
                },
                'LiquidityAdded': {
                    'add_balance_0': 'u128',
                    'add_balance_1': 'u128',
                    'asset_0': 'scale_info::51',
                    'asset_1': 'scale_info::51',
                    'mint_balance_lp': 'u128',
                    'owner': 'AccountId',
                },
                'LiquidityRemoved': {
                    'asset_0': 'scale_info::51',
                    'asset_1': 'scale_info::51',
                    'burn_balance_lp': 'u128',
                    'owner': 'AccountId',
                    'recipient': 'AccountId',
                    'rm_balance_0': 'u128',
                    'rm_balance_1': 'u128',
                },
                'NewFeePoint': {'new_fee_point': 'u8'},
                'NewFeeRate': {
                    'asset_0': 'scale_info::51',
                    'asset_1': 'scale_info::51',
                    'new_fee_rate': 'u128',
                },
                'PairCreated': {
                    'asset_0': 'scale_info::51',
                    'asset_1': 'scale_info::51',
                    'fee_rate': 'u128',
                },
                'WithdrawReward': {
                    'asset_0': 'scale_info::51',
                    'asset_1': 'scale_info::51',
                    'recipient': 'AccountId',
                },
            },
            'DexStable': {
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
                    'currency_id': 'scale_info::51',
                    'fee_amount': 'u128',
                    'pool_id': 'u32',
                },
                'CreatePool': {
                    'a': 'u128',
                    'account': 'AccountId',
                    'admin_fee': 'u128',
                    'admin_fee_receiver': 'AccountId',
                    'currency_ids': ['scale_info::51'],
                    'lp_currency_id': 'scale_info::51',
                    'pool_id': 'u32',
                    'swap_fee': 'u128',
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
            'DexSwapRouter': (),
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::132',
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
            'EVM': {
                'Created': {'address': '[u8; 20]'},
                'CreatedFailed': {'address': '[u8; 20]'},
                'Executed': {'address': '[u8; 20]'},
                'ExecutedFailed': {'address': '[u8; 20]'},
                'Log': {'log': 'scale_info::198'},
            },
            'Escrow': {
                'Deposit': {
                    'amount': 'u128',
                    'unlock_height': 'u32',
                    'who': 'AccountId',
                },
                'Withdraw': {'amount': 'u128', 'who': 'AccountId'},
            },
            'EscrowAnnuity': {'BlockReward': 'u128'},
            'EscrowRewards': {
                'DepositStake': {
                    'amount': 'i128',
                    'pool_id': (),
                    'stake_id': 'AccountId',
                },
                'DistributeReward': {
                    'amount': 'i128',
                    'currency_id': 'scale_info::51',
                },
                'WithdrawReward': {
                    'amount': 'i128',
                    'currency_id': 'scale_info::51',
                    'pool_id': (),
                    'stake_id': 'AccountId',
                },
                'WithdrawStake': {
                    'amount': 'i128',
                    'pool_id': (),
                    'stake_id': 'AccountId',
                },
            },
            'Ethereum': {
                'Executed': {
                    'exit_reason': 'scale_info::189',
                    'extra_data': 'Bytes',
                    'from': '[u8; 20]',
                    'to': '[u8; 20]',
                    'transaction_hash': '[u8; 32]',
                },
            },
            'Farming': {
                'RewardClaimed': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'pool_currency_id': 'scale_info::51',
                    'reward_currency_id': 'scale_info::51',
                },
                'RewardDistributed': {
                    'amount': 'u128',
                    'pool_currency_id': 'scale_info::51',
                    'reward_currency_id': 'scale_info::51',
                },
                'RewardScheduleUpdated': {
                    'per_period': 'u128',
                    'period_count': 'u32',
                    'pool_currency_id': 'scale_info::51',
                    'reward_currency_id': 'scale_info::51',
                },
            },
            'FarmingRewards': {
                'DepositStake': {
                    'amount': 'i128',
                    'pool_id': 'scale_info::51',
                    'stake_id': 'AccountId',
                },
                'DistributeReward': {
                    'amount': 'i128',
                    'currency_id': 'scale_info::51',
                },
                'WithdrawReward': {
                    'amount': 'i128',
                    'currency_id': 'scale_info::51',
                    'pool_id': 'scale_info::51',
                    'stake_id': 'AccountId',
                },
                'WithdrawStake': {
                    'amount': 'i128',
                    'pool_id': 'scale_info::51',
                    'stake_id': 'AccountId',
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
                    'fee': 'u128',
                    'issue_id': '[u8; 32]',
                    'requester': 'AccountId',
                    'vault_id': 'scale_info::88',
                },
                'IssueAmountChange': {
                    'amount': 'u128',
                    'confiscated_griefing_collateral': 'u128',
                    'fee': 'u128',
                    'issue_id': '[u8; 32]',
                },
                'IssuePeriodChange': {'period': 'u32'},
                'RequestIssue': {
                    'amount': 'u128',
                    'fee': 'u128',
                    'griefing_collateral': 'u128',
                    'griefing_currency': 'scale_info::51',
                    'issue_id': '[u8; 32]',
                    'requester': 'AccountId',
                    'vault_address': 'scale_info::100',
                    'vault_id': 'scale_info::88',
                    'vault_public_key': '[u8; 33]',
                },
            },
            'Loans': {
                'ActivatedMarket': {
                    'underlying_currency_id': 'scale_info::51',
                },
                'Borrowed': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                },
                'DepositCollateral': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                },
                'Deposited': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                },
                'DistributedBorrowerReward': {
                    'borrow_reward_index': 'u128',
                    'borrower': 'AccountId',
                    'reward_delta': 'u128',
                    'underlying_currency_id': 'scale_info::51',
                },
                'DistributedSupplierReward': {
                    'reward_delta': 'u128',
                    'supplier': 'AccountId',
                    'supply_reward_index': 'u128',
                    'underlying_currency_id': 'scale_info::51',
                },
                'IncentiveReservesReduced': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                    'receiver': 'AccountId',
                },
                'InterestAccrued': {
                    'borrow_index': 'u128',
                    'borrow_rate': 'u128',
                    'exchange_rate': 'u128',
                    'supply_rate': 'u128',
                    'total_borrows': 'u128',
                    'total_reserves': 'u128',
                    'underlying_currency_id': 'scale_info::51',
                    'utilization_ratio': 'u32',
                },
                'LiquidatedBorrow': {
                    'borrower': 'AccountId',
                    'collateral_currency_id': 'scale_info::51',
                    'collateral_underlying_amount': 'u128',
                    'liquidation_currency_id': 'scale_info::51',
                    'liquidator': 'AccountId',
                    'repay_amount': 'u128',
                },
                'MarketRewardSpeedUpdated': {
                    'borrow_reward_per_block': 'u128',
                    'supply_reward_per_block': 'u128',
                    'underlying_currency_id': 'scale_info::51',
                },
                'NewMarket': {
                    'market': 'scale_info::172',
                    'underlying_currency_id': 'scale_info::51',
                },
                'Redeemed': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                },
                'RepaidBorrow': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                },
                'ReservesAdded': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                    'new_reserve_amount': 'u128',
                    'payer': 'AccountId',
                },
                'ReservesReduced': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                    'new_reserve_amount': 'u128',
                    'receiver': 'AccountId',
                },
                'RewardAdded': {'amount': 'u128', 'payer': 'AccountId'},
                'RewardPaid': {'amount': 'u128', 'receiver': 'AccountId'},
                'RewardWithdrawn': {'amount': 'u128', 'receiver': 'AccountId'},
                'UpdatedMarket': {
                    'market': 'scale_info::172',
                    'underlying_currency_id': 'scale_info::51',
                },
                'WithdrawCollateral': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                },
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::41',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::41',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::31',
                    'timepoint': 'scale_info::41',
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
                    'vault_id': 'scale_info::88',
                },
                'NominationOptIn': {'vault_id': 'scale_info::88'},
                'NominationOptOut': {'vault_id': 'scale_info::88'},
                'WithdrawCollateral': {
                    'amount': 'u128',
                    'nominator_id': 'AccountId',
                    'vault_id': 'scale_info::88',
                },
            },
            'Oracle': {
                'AggregateUpdated': {
                    'values': [('scale_info::109', (None, 'u128'))],
                },
                'FeedValues': {
                    'oracle_id': 'AccountId',
                    'values': [('scale_info::109', 'u128')],
                },
                'OracleAdded': {'name': 'Bytes', 'oracle_id': 'AccountId'},
                'OracleRemoved': {'oracle_id': 'AccountId'},
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
            'PolkadotXcm': {
                'AssetsClaimed': (
                    '[u8; 32]',
                    'scale_info::74',
                    'scale_info::160',
                ),
                'AssetsTrapped': (
                    '[u8; 32]',
                    'scale_info::74',
                    'scale_info::160',
                ),
                'Attempted': {
                    'Complete': 'scale_info::9',
                    'Error': 'scale_info::129',
                    'Incomplete': ('scale_info::9', 'scale_info::129'),
                },
                'FeesPaid': ('scale_info::74', ['scale_info::138']),
                'InvalidQuerier': (
                    'scale_info::74',
                    'u64',
                    'scale_info::74',
                    (None, 'scale_info::74'),
                ),
                'InvalidQuerierVersion': ('scale_info::74', 'u64'),
                'InvalidResponder': (
                    'scale_info::74',
                    'u64',
                    (None, 'scale_info::74'),
                ),
                'InvalidResponderVersion': ('scale_info::74', 'u64'),
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
                'NotifyTargetMigrationFail': ('scale_info::64', 'u64'),
                'NotifyTargetSendFail': (
                    'scale_info::74',
                    'u64',
                    'scale_info::129',
                ),
                'ResponseReady': ('u64', 'scale_info::143'),
                'ResponseTaken': 'u64',
                'Sent': (
                    'scale_info::74',
                    'scale_info::74',
                    ['scale_info::135'],
                ),
                'SupportedVersionChanged': ('scale_info::74', 'u32'),
                'UnexpectedResponse': ('scale_info::74', 'u64'),
                'VersionChangeNotified': (
                    'scale_info::74',
                    'u32',
                    ['scale_info::138'],
                ),
                'VersionNotifyRequested': (
                    'scale_info::74',
                    ['scale_info::138'],
                ),
                'VersionNotifyStarted': ('scale_info::74', ['scale_info::138']),
                'VersionNotifyUnrequested': (
                    'scale_info::74',
                    ['scale_info::138'],
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
                    'proxy_type': 'scale_info::44',
                },
                'ProxyExecuted': {'result': 'scale_info::31'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::44',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::44',
                    'pure': 'AccountId',
                    'who': 'AccountId',
                },
            },
            'Redeem': {
                'CancelRedeem': {
                    'redeem_id': '[u8; 32]',
                    'redeemer': 'AccountId',
                    'slashed_amount': 'u128',
                    'status': 'scale_info::115',
                    'vault_id': 'scale_info::88',
                },
                'ExecuteRedeem': {
                    'amount': 'u128',
                    'fee': 'u128',
                    'redeem_id': '[u8; 32]',
                    'redeemer': 'AccountId',
                    'transfer_fee': 'u128',
                    'vault_id': 'scale_info::88',
                },
                'LiquidationRedeem': {
                    'amount': 'u128',
                    'redeemer': 'AccountId',
                },
                'MintTokensForReimbursedRedeem': {
                    'amount': 'u128',
                    'redeem_id': '[u8; 32]',
                    'vault_id': 'scale_info::88',
                },
                'RedeemPeriodChange': {'period': 'u32'},
                'RequestRedeem': {
                    'amount': 'u128',
                    'btc_address': 'scale_info::100',
                    'fee': 'u128',
                    'premium': 'u128',
                    'redeem_id': '[u8; 32]',
                    'redeemer': 'AccountId',
                    'transfer_fee': 'u128',
                    'vault_id': 'scale_info::88',
                },
                'SelfRedeem': {
                    'amount': 'u128',
                    'fee': 'u128',
                    'vault_id': 'scale_info::88',
                },
            },
            'Replace': {
                'AcceptReplace': {
                    'amount': 'u128',
                    'btc_address': 'scale_info::100',
                    'collateral': 'u128',
                    'new_vault_id': 'scale_info::88',
                    'old_vault_id': 'scale_info::88',
                    'replace_id': '[u8; 32]',
                },
                'CancelReplace': {
                    'griefing_collateral': 'u128',
                    'new_vault_id': 'scale_info::88',
                    'old_vault_id': 'scale_info::88',
                    'replace_id': '[u8; 32]',
                },
                'ExecuteReplace': {
                    'new_vault_id': 'scale_info::88',
                    'old_vault_id': 'scale_info::88',
                    'replace_id': '[u8; 32]',
                },
                'ReplacePeriodChange': {'period': 'u32'},
                'RequestReplace': {
                    'amount': 'u128',
                    'griefing_collateral': 'u128',
                    'old_vault_id': 'scale_info::88',
                },
                'WithdrawReplace': {
                    'old_vault_id': 'scale_info::88',
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
                    'result': 'scale_info::31',
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
                'Activated': None,
                'Deactivated': None,
                'UpdateActiveBlock': {'block_number': 'u32'},
            },
            'Session': {'NewSession': {'session_index': 'u32'}},
            'Sudo': {
                'KeyChanged': {'old_sudoer': (None, 'AccountId')},
                'Sudid': {'sudo_result': 'scale_info::31'},
                'SudoAsDone': {'sudo_result': 'scale_info::31'},
            },
            'Supply': {'Inflation': {'total_inflation': 'u128'}},
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
                    'result': 'scale_info::31',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::31',
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
            'Tokens': {
                'BalanceSet': {
                    'currency_id': 'scale_info::51',
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Deposited': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                    'who': 'AccountId',
                },
                'DustLost': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                    'who': 'AccountId',
                },
                'Endowed': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                    'who': 'AccountId',
                },
                'LockRemoved': {
                    'currency_id': 'scale_info::51',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'LockSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'Locked': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                    'who': 'AccountId',
                },
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                    'from': 'AccountId',
                    'status': 'scale_info::54',
                    'to': 'AccountId',
                },
                'Reserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                    'who': 'AccountId',
                },
                'Slashed': {
                    'currency_id': 'scale_info::51',
                    'free_amount': 'u128',
                    'reserved_amount': 'u128',
                    'who': 'AccountId',
                },
                'TotalIssuanceSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                },
                'Transfer': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unlocked': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                    'who': 'AccountId',
                },
                'Unreserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
                    'who': 'AccountId',
                },
                'Withdrawn': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::51',
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
            'TxPause': {
                'SomethingPaused': {'full_name': ('Bytes', (None, 'Bytes'))},
                'SomethingUnpaused': {'full_name': ('Bytes', (None, 'Bytes'))},
            },
            'UnknownTokens': {
                'Deposited': {
                    'asset': 'scale_info::138',
                    'who': 'scale_info::74',
                },
                'Withdrawn': {
                    'asset': 'scale_info::138',
                    'who': 'scale_info::74',
                },
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::25',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::31'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::25'},
            },
            'VaultAnnuity': {'BlockReward': 'u128'},
            'VaultCapacity': {
                'DepositStake': {
                    'amount': 'i128',
                    'pool_id': (),
                    'stake_id': 'scale_info::51',
                },
                'DistributeReward': {
                    'amount': 'i128',
                    'currency_id': 'scale_info::51',
                },
                'WithdrawReward': {
                    'amount': 'i128',
                    'currency_id': 'scale_info::51',
                    'pool_id': (),
                    'stake_id': 'scale_info::51',
                },
                'WithdrawStake': {
                    'amount': 'i128',
                    'pool_id': (),
                    'stake_id': 'scale_info::51',
                },
            },
            'VaultRegistry': {
                'BanVault': {
                    'banned_until': 'u32',
                    'vault_id': 'scale_info::88',
                },
                'DecreaseLockedCollateral': {
                    'currency_pair': 'scale_info::89',
                    'delta': 'u128',
                    'total': 'u128',
                },
                'DecreaseToBeIssuedTokens': {
                    'decrease': 'u128',
                    'vault_id': 'scale_info::88',
                },
                'DecreaseToBeRedeemedTokens': {
                    'decrease': 'u128',
                    'vault_id': 'scale_info::88',
                },
                'DecreaseToBeReplacedTokens': {
                    'decrease': 'u128',
                    'vault_id': 'scale_info::88',
                },
                'DecreaseTokens': {
                    'decrease': 'u128',
                    'user_id': 'AccountId',
                    'vault_id': 'scale_info::88',
                },
                'IncreaseLockedCollateral': {
                    'currency_pair': 'scale_info::89',
                    'delta': 'u128',
                    'total': 'u128',
                },
                'IncreaseToBeIssuedTokens': {
                    'increase': 'u128',
                    'vault_id': 'scale_info::88',
                },
                'IncreaseToBeRedeemedTokens': {
                    'increase': 'u128',
                    'vault_id': 'scale_info::88',
                },
                'IncreaseToBeReplacedTokens': {
                    'increase': 'u128',
                    'vault_id': 'scale_info::88',
                },
                'IssueTokens': {
                    'increase': 'u128',
                    'vault_id': 'scale_info::88',
                },
                'LiquidateVault': {
                    'backing_collateral': 'u128',
                    'issued_tokens': 'u128',
                    'replace_collateral': 'u128',
                    'status': 'scale_info::102',
                    'to_be_issued_tokens': 'u128',
                    'to_be_redeemed_tokens': 'u128',
                    'to_be_replaced_tokens': 'u128',
                    'vault_id': 'scale_info::88',
                },
                'RedeemTokens': {
                    'redeemed_amount': 'u128',
                    'vault_id': 'scale_info::88',
                },
                'RedeemTokensLiquidatedVault': {
                    'collateral': 'u128',
                    'tokens': 'u128',
                    'vault_id': 'scale_info::88',
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
                    'vault_id': 'scale_info::88',
                },
                'RegisterAddress': {
                    'address': 'scale_info::100',
                    'vault_id': 'scale_info::88',
                },
                'RegisterVault': {
                    'collateral': 'u128',
                    'vault_id': 'scale_info::88',
                },
                'ReplaceTokens': {
                    'additional_collateral': 'u128',
                    'amount': 'u128',
                    'new_vault_id': 'scale_info::88',
                    'old_vault_id': 'scale_info::88',
                },
                'SetAcceptNewIssues': {
                    'accept_new_issues': 'bool',
                    'vault_id': 'scale_info::88',
                },
                'SetCustomSecureThreshold': {
                    'custom_threshold': (None, 'u128'),
                    'vault_id': 'scale_info::88',
                },
                'SetLiquidationCollateralThreshold': {
                    'currency_pair': 'scale_info::89',
                    'threshold': 'u128',
                },
                'SetPremiumRedeemThreshold': {
                    'currency_pair': 'scale_info::89',
                    'threshold': 'u128',
                },
                'SetSecureCollateralThreshold': {
                    'currency_pair': 'scale_info::89',
                    'threshold': 'u128',
                },
                'UpdatePublicKey': {
                    'account_id': 'AccountId',
                    'public_key': '[u8; 33]',
                },
            },
            'VaultRewards': {
                'DepositStake': {
                    'amount': 'i128',
                    'pool_id': 'scale_info::51',
                    'stake_id': 'scale_info::88',
                },
                'DistributeReward': {
                    'amount': 'i128',
                    'currency_id': 'scale_info::51',
                },
                'WithdrawReward': {
                    'amount': 'i128',
                    'currency_id': 'scale_info::51',
                    'pool_id': 'scale_info::51',
                    'stake_id': 'scale_info::88',
                },
                'WithdrawStake': {
                    'amount': 'i128',
                    'pool_id': 'scale_info::51',
                    'stake_id': 'scale_info::88',
                },
            },
            'VaultStaking': {
                'DepositStake': {
                    'amount': 'i128',
                    'nominator_id': 'AccountId',
                    'vault_id': 'scale_info::88',
                },
                'DistributeReward': {
                    'amount': 'i128',
                    'currency_id': 'scale_info::51',
                    'vault_id': 'scale_info::88',
                },
                'ForceRefund': {'vault_id': 'scale_info::88'},
                'IncreaseNonce': {
                    'new_nonce': 'u32',
                    'vault_id': 'scale_info::88',
                },
                'WithdrawReward': {
                    'amount': 'i128',
                    'currency_id': 'scale_info::51',
                    'nominator_id': 'AccountId',
                    'nonce': 'u32',
                    'vault_id': 'scale_info::88',
                },
                'WithdrawStake': {
                    'amount': 'i128',
                    'nominator_id': 'AccountId',
                    'vault_id': 'scale_info::88',
                },
            },
            'Vesting': {
                'Claimed': {'amount': 'u128', 'who': 'AccountId'},
                'VestingScheduleAdded': {
                    'from': 'AccountId',
                    'to': 'AccountId',
                    'vesting_schedule': 'scale_info::58',
                },
                'VestingSchedulesUpdated': {'who': 'AccountId'},
            },
            'XTokens': {
                'TransferredMultiAssets': {
                    'assets': ['scale_info::138'],
                    'dest': 'scale_info::74',
                    'fee': 'scale_info::138',
                    'sender': 'AccountId',
                },
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': (None, '[u8; 32]')},
                'BadVersion': {'message_hash': (None, '[u8; 32]')},
                'Fail': {
                    'error': 'scale_info::129',
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
    'base_block': {'proof_size': 0, 'ref_time': 6151485000},
    'max_block': {'proof_size': 5242880, 'ref_time': 500000000000},
    'per_class': {
        'mandatory': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 97286000},
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 97286000},
            'max_extrinsic': {'proof_size': 3407872, 'ref_time': 324902714000},
            'max_total': {'proof_size': 3932160, 'ref_time': 375000000000},
            'reserved': {'proof_size': 0, 'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 97286000},
            'max_extrinsic': {'proof_size': 4718592, 'ref_time': 449902714000},
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
2032
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
        ('0x22b97323b9e853da', 1),
        ('0x0dee8b30877eda0b', 1),
        ('0xd482d4d14bbbf88a', 1),
        ('0xc6b106fa1a388380', 1),
        ('0x6ef953004ba30e59', 1),
        ('0x16da96d36c6d5bb7', 1),
        ('0xcbfba9ca38dbdb1a', 1),
        ('0xc1e19f5c3385297a', 1),
        ('0xcaf39b979a6880bd', 1),
        ('0x69e2e1aa421f4fb0', 1),
        ('0x2be5cb02b0a56e73', 1),
        ('0x582211f65bb14b89', 5),
        ('0xe65b00e46cedd0aa', 2),
    ],
    'authoring_version': 1,
    'impl_name': 'interlay-parachain',
    'impl_version': 1,
    'spec_name': 'interlay-parachain',
    'spec_version': 1025003,
    'state_version': 0,
    'transaction_version': 4,
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