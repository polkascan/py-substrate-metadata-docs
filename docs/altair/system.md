
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
            None: None,
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
            'BaseFee': {
                'BaseFeeOverflow': None,
                'NewBaseFeePerGas': {'fee': 'scale_info::227'},
                'NewElasticity': {'elasticity': 'u32'},
            },
            'BlockRewards': {
                'NewSession': {
                    'collator_reward': 'u128',
                    'last_changes': 'scale_info::198',
                    'treasury_inflation_rate': 'u128',
                },
                'SessionAdvancementFailed': {'error': 'scale_info::25'},
            },
            'BlockRewardsBase': {
                'CurrencyAttached': {
                    'currency_id': 'scale_info::77',
                    'from': (None, 'u32'),
                    'to': 'u32',
                },
                'GroupRewarded': {'amount': 'u128', 'group_id': 'u32'},
                'RewardClaimed': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                    'group_id': 'u32',
                },
                'StakeDeposited': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                    'group_id': 'u32',
                },
                'StakeWithdrawn': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                    'group_id': 'u32',
                },
            },
            'CollatorAllowlist': {
                'CollatorAdded': {'collator_id': 'AccountId'},
                'CollatorRemoved': {'collator_id': 'AccountId'},
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
                'Approved': {'proposal_hash': 'scale_info::12'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': 'scale_info::12',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': 'scale_info::12'},
                'Executed': {
                    'proposal_hash': 'scale_info::12',
                    'result': 'scale_info::40',
                },
                'MemberExecuted': {
                    'proposal_hash': 'scale_info::12',
                    'result': 'scale_info::40',
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
            'CrowdloanClaim': {
                'ClaimPalletInitialized': None,
                'ContributionsRootUpdated': 'scale_info::12',
                'CrowdloanTrieIndexUpdated': 'u32',
                'LeasePeriodUpdated': 'u32',
                'LeaseStartUpdated': 'u32',
                'LockedAtUpdated': 'u32',
                'RewardClaimed': ('AccountId', 'AccountId', 'u128'),
            },
            'CrowdloanReward': {
                'DirectPayoutRatioUpdated': 'u32',
                'RewardClaimed': ('AccountId', 'u128', 'u128'),
                'RewardPalletInitialized': ('u32', 'u32', 'u32'),
                'VestingPeriodUpdated': 'u32',
                'VestingStartUpdated': 'u32',
            },
            'CumulusXcm': {
                'ExecutedDownward': ('[u8; 32]', 'scale_info::496'),
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
                    'owner': 'scale_info::57',
                },
                'MetadataSet': {
                    'hash': 'scale_info::12',
                    'owner': 'scale_info::57',
                },
                'MetadataTransferred': {
                    'hash': 'scale_info::12',
                    'owner': 'scale_info::57',
                    'prev_owner': 'scale_info::57',
                },
                'NotPassed': {'ref_index': 'u32'},
                'Passed': {'ref_index': 'u32'},
                'ProposalCanceled': {'prop_index': 'u32'},
                'Proposed': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Seconded': {'prop_index': 'u32', 'seconder': 'AccountId'},
                'Started': {'ref_index': 'u32', 'threshold': 'scale_info::54'},
                'Tabled': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Undelegated': {'account': 'AccountId'},
                'Vetoed': {
                    'proposal_hash': 'scale_info::12',
                    'until': 'u32',
                    'who': 'AccountId',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::55',
                    'voter': 'AccountId',
                },
            },
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::496',
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
                'Log': {'log': 'scale_info::506'},
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
                'Executed': {
                    'exit_reason': 'scale_info::509',
                    'extra_data': 'Bytes',
                    'from': '[u8; 20]',
                    'to': '[u8; 20]',
                    'transaction_hash': 'scale_info::12',
                },
            },
            'Fees': {
                'FeeChanged': {'fee': 'u128', 'key': 'scale_info::70'},
                'FeeToAuthor': {'balance': 'u128', 'from': 'AccountId'},
                'FeeToBurn': {'balance': 'u128', 'from': 'AccountId'},
                'FeeToTreasury': {'balance': 'u128', 'from': 'AccountId'},
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
            'InterestAccrual': (),
            'Investments': {
                'InvestCollectedForNonClearedOrderId': {
                    'investment_id': 'scale_info::102',
                    'who': 'AccountId',
                },
                'InvestCollectedWithoutActivePosition': {
                    'investment_id': 'scale_info::102',
                    'who': 'AccountId',
                },
                'InvestOrderUpdated': {
                    'amount': 'u128',
                    'investment_id': 'scale_info::102',
                    'submitted_at': 'u64',
                    'who': 'AccountId',
                },
                'InvestOrdersCleared': {
                    'fulfillment': 'scale_info::191',
                    'investment_id': 'scale_info::102',
                    'order_id': 'u64',
                },
                'InvestOrdersCollected': {
                    'collection': 'scale_info::188',
                    'investment_id': 'scale_info::102',
                    'outcome': 'scale_info::189',
                    'processed_orders': ['u64'],
                    'who': 'AccountId',
                },
                'InvestOrdersInProcessing': {
                    'investment_id': 'scale_info::102',
                    'order_id': 'u64',
                    'total_order': 'scale_info::192',
                },
                'RedeemCollectedForNonClearedOrderId': {
                    'investment_id': 'scale_info::102',
                    'who': 'AccountId',
                },
                'RedeemCollectedWithoutActivePosition': {
                    'investment_id': 'scale_info::102',
                    'who': 'AccountId',
                },
                'RedeemOrderUpdated': {
                    'amount': 'u128',
                    'investment_id': 'scale_info::102',
                    'submitted_at': 'u64',
                    'who': 'AccountId',
                },
                'RedeemOrdersCleared': {
                    'fulfillment': 'scale_info::191',
                    'investment_id': 'scale_info::102',
                    'order_id': 'u64',
                },
                'RedeemOrdersCollected': {
                    'collection': 'scale_info::190',
                    'investment_id': 'scale_info::102',
                    'outcome': 'scale_info::189',
                    'processed_orders': ['u64'],
                    'who': 'AccountId',
                },
                'RedeemOrdersInProcessing': {
                    'investment_id': 'scale_info::102',
                    'order_id': 'u64',
                    'total_order': 'scale_info::192',
                },
            },
            'LiquidityPools': {
                'IncomingMessage': {
                    'message': 'scale_info::206',
                    'sender': 'scale_info::145',
                },
            },
            'LiquidityPoolsAxelarGateway': {
                'ConverterSet': {
                    'converter': 'scale_info::492',
                    'id_hash': 'scale_info::12',
                },
                'GatewaySet': {'address': '[u8; 20]'},
            },
            None: None,
            'Keystore': {
                'DepositSet': {'new_deposit': 'u128'},
                'KeyAdded': {
                    'key': 'scale_info::12',
                    'key_type': 'scale_info::204',
                    'owner': 'AccountId',
                    'purpose': 'scale_info::203',
                },
                'KeyRevoked': {
                    'block_number': 'u32',
                    'key': 'scale_info::12',
                    'owner': 'AccountId',
                },
            },
            'LiquidityPoolsGateway': {
                'DomainRouterSet': {
                    'domain': 'scale_info::207',
                    'router': 'scale_info::210',
                },
                'InstanceAdded': {'instance': 'scale_info::145'},
                'InstanceRemoved': {'instance': 'scale_info::145'},
                'OutboundMessageExecutionFailure': {
                    'domain': 'scale_info::207',
                    'error': 'scale_info::25',
                    'message': 'scale_info::206',
                    'nonce': 'u64',
                    'sender': 'AccountId',
                },
                'OutboundMessageExecutionSuccess': {
                    'domain': 'scale_info::207',
                    'message': 'scale_info::206',
                    'nonce': 'u64',
                    'sender': 'AccountId',
                },
                'OutboundMessageSubmitted': {
                    'domain': 'scale_info::207',
                    'message': 'scale_info::206',
                    'sender': 'AccountId',
                },
                'RelayerAdded': {'relayer': 'scale_info::145'},
                'RelayerRemoved': {'relayer': 'scale_info::145'},
            },
            'LiquidityRewards': {
                'NewEpoch': {
                    'ends_on': 'u64',
                    'last_changes': 'scale_info::233',
                    'reward': 'u128',
                },
            },
            'LiquidityRewardsBase': {
                'CurrencyAttached': {
                    'currency_id': 'scale_info::77',
                    'from': (None, 'u32'),
                    'to': 'u32',
                },
                'GroupRewarded': {'amount': 'u128', 'group_id': 'u32'},
                'RewardClaimed': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                    'group_id': 'u32',
                },
                'StakeDeposited': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                    'group_id': 'u32',
                },
                'StakeWithdrawn': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                    'group_id': 'u32',
                },
            },
            'Loans': {
                'Borrowed': {
                    'amount': 'scale_info::134',
                    'loan_id': 'u64',
                    'pool_id': 'u64',
                },
                'Closed': {
                    'collateral': ('u64', 'u128'),
                    'loan_id': 'u64',
                    'pool_id': 'u64',
                },
                'Created': {
                    'loan_id': 'u64',
                    'loan_info': 'scale_info::171',
                    'pool_id': 'u64',
                },
                'DebtIncreased': {
                    'amount': 'scale_info::134',
                    'loan_id': 'u64',
                    'pool_id': 'u64',
                },
                'DebtTransferred': {
                    'borrow_amount': 'scale_info::134',
                    'from_loan_id': 'u64',
                    'pool_id': 'u64',
                    'repaid_amount': 'scale_info::133',
                    'to_loan_id': 'u64',
                },
                'Mutated': {
                    'loan_id': 'u64',
                    'mutation': 'scale_info::115',
                    'pool_id': 'u64',
                },
                'PortfolioValuationUpdated': {
                    'pool_id': 'u64',
                    'update_type': 'scale_info::184',
                    'valuation': 'u128',
                },
                'Repaid': {
                    'amount': 'scale_info::133',
                    'loan_id': 'u64',
                    'pool_id': 'u64',
                },
                'WriteOffPolicyUpdated': {'policy': ['scale_info::125'], 'pool_id': 'u64'},
                'WrittenOff': {
                    'loan_id': 'u64',
                    'pool_id': 'u64',
                    'status': 'scale_info::131',
                },
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::39',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::39',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::40',
                    'timepoint': 'scale_info::39',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'OraclePriceCollection': {
                'AddedKey': {'collection_id': 'u64', 'key': 'scale_info::178'},
                'RemovedKey': {
                    'collection_id': 'u64',
                    'key': 'scale_info::178',
                },
                'UpdatedCollection': {
                    'collection_id': 'u64',
                    'keys_updated': 'u32',
                },
                'UpdatedCollectionInfo': {
                    'collection_id': 'u64',
                    'collection_info': 'scale_info::138',
                },
            },
            'OraclePriceFeed': {
                'Fed': {
                    'feeder': 'scale_info::141',
                    'key': 'scale_info::178',
                    'value': 'u128',
                },
            },
            'OrderBook': {
                'FeederChanged': {'feeder_id': 'scale_info::141'},
                'OrderCancelled': {'account': 'AccountId', 'order_id': 'u64'},
                'OrderCreated': {
                    'amount_out': 'u128',
                    'creator_account': 'AccountId',
                    'currency_in': 'scale_info::77',
                    'currency_out': 'scale_info::77',
                    'min_fulfillment_amount_out': 'u128',
                    'order_id': 'u64',
                    'ratio': 'scale_info::243',
                },
                'OrderFulfillment': {
                    'currency_in': 'scale_info::77',
                    'currency_out': 'scale_info::77',
                    'fulfilling_account': 'AccountId',
                    'fulfillment_amount': 'u128',
                    'order_id': 'u64',
                    'partial_fulfillment': 'bool',
                    'placing_account': 'AccountId',
                    'ratio': 'u128',
                },
                'OrderUpdated': {
                    'account': 'AccountId',
                    'amount_out': 'u128',
                    'min_fulfillment_amount_out': 'u128',
                    'order_id': 'u64',
                    'ratio': 'scale_info::243',
                },
            },
            'OrmlAssetRegistry': {
                'RegisteredAsset': {
                    'asset_id': 'scale_info::77',
                    'metadata': 'scale_info::465',
                },
                'UpdatedAsset': {
                    'asset_id': 'scale_info::77',
                    'metadata': 'scale_info::465',
                },
            },
            'OrmlTokens': {
                'BalanceSet': {
                    'currency_id': 'scale_info::77',
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Deposited': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                    'who': 'AccountId',
                },
                'DustLost': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                    'who': 'AccountId',
                },
                'Endowed': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                    'who': 'AccountId',
                },
                'LockRemoved': {
                    'currency_id': 'scale_info::77',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'LockSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'Locked': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                    'who': 'AccountId',
                },
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                    'from': 'AccountId',
                    'status': 'scale_info::33',
                    'to': 'AccountId',
                },
                'Reserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                    'who': 'AccountId',
                },
                'Slashed': {
                    'currency_id': 'scale_info::77',
                    'free_amount': 'u128',
                    'reserved_amount': 'u128',
                    'who': 'AccountId',
                },
                'TotalIssuanceSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                },
                'Transfer': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unlocked': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                    'who': 'AccountId',
                },
                'Unreserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                    'who': 'AccountId',
                },
                'Withdrawn': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                    'who': 'AccountId',
                },
            },
            'OrmlXTokens': {
                'TransferredMultiAssets': {
                    'assets': ['scale_info::421'],
                    'dest': 'scale_info::148',
                    'fee': 'scale_info::421',
                    'sender': 'AccountId',
                },
            },
            'OrmlXcm': {
                'Sent': {'message': ['scale_info::418'], 'to': 'scale_info::148'},
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
            'Permissions': {
                'Added': {
                    'role': 'scale_info::81',
                    'scope': 'scale_info::76',
                    'to': 'AccountId',
                },
                'Purged': {'from': 'AccountId', 'scope': 'scale_info::76'},
                'Removed': {
                    'from': 'AccountId',
                    'role': 'scale_info::81',
                    'scope': 'scale_info::76',
                },
            },
            'PolkadotXcm': {
                'AssetsClaimed': (
                    'scale_info::12',
                    'scale_info::148',
                    'scale_info::441',
                ),
                'AssetsTrapped': (
                    'scale_info::12',
                    'scale_info::148',
                    'scale_info::441',
                ),
                'Attempted': {
                    'Complete': 'scale_info::9',
                    'Error': 'scale_info::428',
                    'Incomplete': ('scale_info::9', 'scale_info::428'),
                },
                'FeesPaid': ('scale_info::148', ['scale_info::421']),
                'InvalidQuerier': (
                    'scale_info::148',
                    'u64',
                    'scale_info::148',
                    (None, 'scale_info::148'),
                ),
                'InvalidQuerierVersion': ('scale_info::148', 'u64'),
                'InvalidResponder': (
                    'scale_info::148',
                    'u64',
                    (None, 'scale_info::148'),
                ),
                'InvalidResponderVersion': ('scale_info::148', 'u64'),
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
                'NotifyTargetMigrationFail': ('scale_info::214', 'u64'),
                'NotifyTargetSendFail': (
                    'scale_info::148',
                    'u64',
                    'scale_info::428',
                ),
                'ResponseReady': ('u64', 'scale_info::425'),
                'ResponseTaken': 'u64',
                'Sent': (
                    'scale_info::148',
                    'scale_info::148',
                    ['scale_info::418'],
                ),
                'SupportedVersionChanged': ('scale_info::148', 'u32'),
                'UnexpectedResponse': ('scale_info::148', 'u64'),
                'VersionChangeNotified': (
                    'scale_info::148',
                    'u32',
                    ['scale_info::421'],
                ),
                'VersionNotifyRequested': (
                    'scale_info::148',
                    ['scale_info::421'],
                ),
                'VersionNotifyStarted': (
                    'scale_info::148',
                    ['scale_info::421'],
                ),
                'VersionNotifyUnrequested': (
                    'scale_info::148',
                    ['scale_info::421'],
                ),
            },
            'PoolFees': {
                'Accrued': {
                    'disbursement': 'u128',
                    'fee_id': 'u64',
                    'pending': 'u128',
                    'pool_id': 'u64',
                },
                'Added': {
                    'bucket': 'scale_info::165',
                    'fee': 'scale_info::166',
                    'fee_id': 'u64',
                    'pool_id': 'u64',
                },
                'Charged': {
                    'amount': 'u128',
                    'fee_id': 'u64',
                    'pending': 'u128',
                    'pool_id': 'u64',
                },
                'Paid': {
                    'amount': 'u128',
                    'destination': 'AccountId',
                    'fee_id': 'u64',
                    'pool_id': 'u64',
                },
                'PortfolioValuationUpdated': {
                    'pool_id': 'u64',
                    'update_type': 'scale_info::184',
                    'valuation': 'u128',
                },
                'Proposed': {
                    'bucket': 'scale_info::165',
                    'fee': 'scale_info::166',
                    'fee_id': 'u64',
                    'pool_id': 'u64',
                },
                'Removed': {
                    'bucket': 'scale_info::165',
                    'fee_id': 'u64',
                    'pool_id': 'u64',
                },
                'Uncharged': {
                    'amount': 'u128',
                    'fee_id': 'u64',
                    'pending': 'u128',
                    'pool_id': 'u64',
                },
            },
            'PoolRegistry': {
                'MetadataSet': {'metadata': 'Bytes', 'pool_id': 'u64'},
                'Registered': {'pool_id': 'u64'},
                'UpdateExecuted': {'pool_id': 'u64'},
                'UpdateRegistered': {'pool_id': 'u64'},
                'UpdateStored': {'pool_id': 'u64'},
            },
            'PoolSystem': {
                'Created': {
                    'admin': 'AccountId',
                    'depositor': 'AccountId',
                    'essence': 'scale_info::101',
                    'pool_id': 'u64',
                },
                'EpochClosed': {'epoch_id': 'u32', 'pool_id': 'u64'},
                'EpochExecuted': {'epoch_id': 'u32', 'pool_id': 'u64'},
                'MaxReserveSet': {'pool_id': 'u64'},
                'NegativeBalanceSheet': {
                    'nav_aum': 'u128',
                    'nav_fees': 'u128',
                    'pool_id': 'u64',
                    'reserve': 'u128',
                },
                'ProposedChange': {
                    'change': 'scale_info::112',
                    'change_id': 'scale_info::12',
                    'pool_id': 'u64',
                },
                'Rebalanced': {'pool_id': 'u64'},
                'SolutionSubmitted': {
                    'epoch_id': 'u32',
                    'pool_id': 'u64',
                    'solution': 'scale_info::86',
                },
                'Updated': {
                    'id': 'u64',
                    'new': 'scale_info::101',
                    'old': 'scale_info::101',
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
                    'proxy_type': 'scale_info::43',
                },
                'ProxyExecuted': {'result': 'scale_info::40'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::43',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::43',
                    'pure': 'AccountId',
                    'who': 'AccountId',
                },
            },
            'Remarks': {
                'Remark': {'call': 'Call', 'remarks': ['scale_info::252']},
            },
            'Scheduler': {
                'CallUnavailable': {
                    'id': (None, '[u8; 32]'),
                    'task': ('u32', 'u32'),
                },
                'Canceled': {'index': 'u32', 'when': 'u32'},
                'Dispatched': {
                    'id': (None, '[u8; 32]'),
                    'result': 'scale_info::40',
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
            'TokenMux': {
                'Burned': {
                    'amount': 'u128',
                    'currency_in': 'scale_info::77',
                    'currency_out': 'scale_info::77',
                    'who': 'AccountId',
                },
                'Deposited': {
                    'amount': 'u128',
                    'currency_in': 'scale_info::77',
                    'currency_out': 'scale_info::77',
                    'who': 'AccountId',
                },
                'SwapMatched': {'amount': 'u128', 'id': 'u64'},
            },
            'Tokens': {
                'BalanceSet': {
                    'currency_id': 'scale_info::77',
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Transfer': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::77',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
            },
            'TransactionPayment': {
                'TransactionFeePaid': {
                    'actual_fee': 'u128',
                    'tip': 'u128',
                    'who': 'AccountId',
                },
            },
            'TransferAllowList': {
                'ToggleTransferAllowanceDelayFutureModifiable': {
                    'currency_id': 'scale_info::245',
                    'modifiable_once_after': (None, 'u32'),
                    'sender_account_id': 'AccountId',
                },
                'TransferAllowanceCreated': {
                    'allowed_at': 'u32',
                    'blocked_at': 'u32',
                    'currency_id': 'scale_info::245',
                    'receiver': 'scale_info::246',
                    'sender_account_id': 'AccountId',
                },
                'TransferAllowanceDelayAdd': {
                    'currency_id': 'scale_info::245',
                    'delay': 'u32',
                    'sender_account_id': 'AccountId',
                },
                'TransferAllowanceDelayPurge': {
                    'currency_id': 'scale_info::245',
                    'sender_account_id': 'AccountId',
                },
                'TransferAllowanceDelayUpdate': {
                    'currency_id': 'scale_info::245',
                    'delay': 'u32',
                    'sender_account_id': 'AccountId',
                },
                'TransferAllowancePurged': {
                    'currency_id': 'scale_info::245',
                    'receiver': 'scale_info::246',
                    'sender_account_id': 'AccountId',
                },
                'TransferAllowanceRemoved': {
                    'allowed_at': 'u32',
                    'blocked_at': 'u32',
                    'currency_id': 'scale_info::245',
                    'receiver': 'scale_info::246',
                    'sender_account_id': 'AccountId',
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
                    'collection': 'u64',
                    'delegate': 'AccountId',
                    'item': 'u128',
                    'owner': 'AccountId',
                },
                'ApprovedTransfer': {
                    'collection': 'u64',
                    'delegate': 'AccountId',
                    'item': 'u128',
                    'owner': 'AccountId',
                },
                'AttributeCleared': {
                    'collection': 'u64',
                    'key': 'Bytes',
                    'maybe_item': (None, 'u128'),
                },
                'AttributeSet': {
                    'collection': 'u64',
                    'key': 'Bytes',
                    'maybe_item': (None, 'u128'),
                    'value': 'Bytes',
                },
                'Burned': {
                    'collection': 'u64',
                    'item': 'u128',
                    'owner': 'AccountId',
                },
                'CollectionFrozen': {'collection': 'u64'},
                'CollectionMaxSupplySet': {
                    'collection': 'u64',
                    'max_supply': 'u32',
                },
                'CollectionMetadataCleared': {'collection': 'u64'},
                'CollectionMetadataSet': {
                    'collection': 'u64',
                    'data': 'Bytes',
                    'is_frozen': 'bool',
                },
                'CollectionThawed': {'collection': 'u64'},
                'Created': {
                    'collection': 'u64',
                    'creator': 'AccountId',
                    'owner': 'AccountId',
                },
                'Destroyed': {'collection': 'u64'},
                'ForceCreated': {'collection': 'u64', 'owner': 'AccountId'},
                'Frozen': {'collection': 'u64', 'item': 'u128'},
                'Issued': {
                    'collection': 'u64',
                    'item': 'u128',
                    'owner': 'AccountId',
                },
                'ItemBought': {
                    'buyer': 'AccountId',
                    'collection': 'u64',
                    'item': 'u128',
                    'price': 'u128',
                    'seller': 'AccountId',
                },
                'ItemPriceRemoved': {'collection': 'u64', 'item': 'u128'},
                'ItemPriceSet': {
                    'collection': 'u64',
                    'item': 'u128',
                    'price': 'u128',
                    'whitelisted_buyer': (None, 'AccountId'),
                },
                'ItemStatusChanged': {'collection': 'u64'},
                'MetadataCleared': {'collection': 'u64', 'item': 'u128'},
                'MetadataSet': {
                    'collection': 'u64',
                    'data': 'Bytes',
                    'is_frozen': 'bool',
                    'item': 'u128',
                },
                'OwnerChanged': {
                    'collection': 'u64',
                    'new_owner': 'AccountId',
                },
                'OwnershipAcceptanceChanged': {
                    'maybe_collection': (None, 'u64'),
                    'who': 'AccountId',
                },
                'Redeposited': {
                    'collection': 'u64',
                    'successful_items': ['u128'],
                },
                'TeamChanged': {
                    'admin': 'AccountId',
                    'collection': 'u64',
                    'freezer': 'AccountId',
                    'issuer': 'AccountId',
                },
                'Thawed': {'collection': 'u64', 'item': 'u128'},
                'Transferred': {
                    'collection': 'u64',
                    'from': 'AccountId',
                    'item': 'u128',
                    'to': 'AccountId',
                },
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::25',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::40'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::25'},
            },
            'Vesting': {
                'VestingCompleted': {'account': 'AccountId'},
                'VestingUpdated': {'account': 'AccountId', 'unvested': 'u128'},
            },
            'XcmTransactor': {
                'DeRegisteredDerivative': {'index': 'u16'},
                'DestFeePerSecondChanged': {
                    'fee_per_second': 'u128',
                    'location': 'scale_info::148',
                },
                'DestFeePerSecondRemoved': {'location': 'scale_info::148'},
                'HrmpManagementSent': {'action': 'scale_info::461'},
                'RegisteredDerivative': {
                    'account_id': 'AccountId',
                    'index': 'u16',
                },
                'TransactFailed': {'error': 'scale_info::428'},
                'TransactInfoChanged': {
                    'location': 'scale_info::148',
                    'remote_info': 'scale_info::500',
                },
                'TransactInfoRemoved': {'location': 'scale_info::148'},
                'TransactedDerivative': {
                    'account_id': 'AccountId',
                    'call': 'Bytes',
                    'dest': 'scale_info::148',
                    'index': 'u16',
                },
                'TransactedSigned': {
                    'call': 'Bytes',
                    'dest': 'scale_info::148',
                    'fee_payer': 'AccountId',
                },
                'TransactedSovereign': {
                    'call': 'Bytes',
                    'dest': 'scale_info::148',
                    'fee_payer': 'AccountId',
                },
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': (None, '[u8; 32]')},
                'BadVersion': {'message_hash': (None, '[u8; 32]')},
                'Fail': {
                    'error': 'scale_info::428',
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
            'max_extrinsic': {'proof_size': 3670016, 'ref_time': 349886362000},
            'max_total': {'proof_size': 3932160, 'ref_time': 375000000000},
            'reserved': {'proof_size': 0, 'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 113638000},
            'max_extrinsic': {'proof_size': 4980736, 'ref_time': 474886362000},
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
136
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
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 4),
        ('0xea93e3f16f3d6962', 2),
        ('0xc937d79c92c4e872', 1),
        ('0x9ce8a204acbb1235', 1),
        ('0x8f5c2d0094ecd047', 1),
        ('0x22b97323b9e853da', 2),
        ('0x639021f9c79c4897', 1),
        ('0x9c62715b4dcff733', 1),
        ('0x6575ae9c9f645c50', 1),
        ('0xa03b94ae2668f243', 1),
        ('0x582211f65bb14b89', 5),
        ('0xe65b00e46cedd0aa', 2),
    ],
    'authoring_version': 1,
    'impl_name': 'altair',
    'impl_version': 1,
    'spec_name': 'altair',
    'spec_version': 1034,
    'state_version': 0,
    'transaction_version': 2,
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