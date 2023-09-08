
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
            'BaseFee': {
                'BaseFeeOverflow': None,
                'NewBaseFeePerGas': {'fee': '[u64; 4]'},
                'NewElasticity': {'elasticity': 'u32'},
            },
            'BlockRewards': {
                'NewSession': {
                    'collator_reward': 'u128',
                    'last_changes': 'scale_info::77',
                    'total_reward': 'u128',
                },
                'SessionAdvancementFailed': {'error': 'scale_info::24'},
            },
            'BlockRewardsBase': {
                'CurrencyAttached': {
                    'currency_id': 'scale_info::70',
                    'from': (None, 'u32'),
                    'to': 'u32',
                },
                'GroupRewarded': {'amount': 'u128', 'group_id': 'u32'},
                'RewardClaimed': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'currency_id': 'scale_info::70',
                    'group_id': 'u32',
                },
                'StakeDeposited': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'currency_id': 'scale_info::70',
                    'group_id': 'u32',
                },
                'StakeWithdrawn': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'currency_id': 'scale_info::70',
                    'group_id': 'u32',
                },
            },
            'Bridge': {'Remark': ('[u8; 32]', '[u8; 32]')},
            'ChainBridge': {
                'ChainWhitelisted': 'u8',
                'FungibleTransfer': (
                    'u8',
                    'u64',
                    '[u8; 32]',
                    '[u64; 4]',
                    'Bytes',
                ),
                'GenericTransfer': ('u8', 'u64', '[u8; 32]', 'Bytes'),
                'NonFungibleTransfer': (
                    'u8',
                    'u64',
                    '[u8; 32]',
                    'Bytes',
                    'Bytes',
                    'Bytes',
                ),
                'ProposalApproved': ('u8', 'u64'),
                'ProposalFailed': ('u8', 'u64'),
                'ProposalRejected': ('u8', 'u64'),
                'ProposalSucceeded': ('u8', 'u64'),
                'RelayerAdded': 'AccountId',
                'RelayerRemoved': 'AccountId',
                'RelayerThresholdChanged': 'u32',
                'VoteAgainst': ('u8', 'u64', 'AccountId'),
                'VoteFor': ('u8', 'u64', 'AccountId'),
            },
            'Claims': {
                'Claimed': {'account_id': 'AccountId', 'amount': 'u128'},
                'RootHashStored': {'root_hash': '[u8; 32]'},
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
                'Approved': {'proposal_hash': '[u8; 32]'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': '[u8; 32]'},
                'Executed': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::38',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::38',
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
            'CrowdloanClaim': {
                'ClaimPalletInitialized': None,
                'ContributionsRootUpdated': '[u8; 32]',
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
                'ExecutedDownward': ('[u8; 8]', 'scale_info::86'),
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
                'Started': {'ref_index': 'u32', 'threshold': 'scale_info::53'},
                'Tabled': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Undelegated': {'account': 'AccountId'},
                'Vetoed': {
                    'proposal_hash': '[u8; 32]',
                    'until': 'u32',
                    'who': 'AccountId',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::54',
                    'voter': 'AccountId',
                },
            },
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::86',
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
            'EVM': {
                'Created': {'address': '[u8; 20]'},
                'CreatedFailed': {'address': '[u8; 20]'},
                'Executed': {'address': '[u8; 20]'},
                'ExecutedFailed': {'address': '[u8; 20]'},
                'Log': {'log': 'scale_info::137'},
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
                    'exit_reason': 'scale_info::143',
                    'from': '[u8; 20]',
                    'to': '[u8; 20]',
                    'transaction_hash': '[u8; 32]',
                },
            },
            'Fees': {
                'FeeChanged': {'fee': 'u128', 'key': 'scale_info::61'},
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
                    'investment_id': 'scale_info::169',
                    'who': 'AccountId',
                },
                'InvestCollectedWithoutActivePosition': {
                    'investment_id': 'scale_info::169',
                    'who': 'AccountId',
                },
                'InvestOrderUpdated': {
                    'amount': 'u128',
                    'investment_id': 'scale_info::169',
                    'submitted_at': 'u64',
                    'who': 'AccountId',
                },
                'InvestOrdersCleared': {
                    'fulfillment': 'scale_info::189',
                    'investment_id': 'scale_info::169',
                    'order_id': 'u64',
                },
                'InvestOrdersCollected': {
                    'collection': 'scale_info::186',
                    'investment_id': 'scale_info::169',
                    'outcome': 'scale_info::187',
                    'processed_orders': ['u64'],
                    'who': 'AccountId',
                },
                'InvestOrdersInProcessing': {
                    'investment_id': 'scale_info::169',
                    'order_id': 'u64',
                    'total_order': 'scale_info::190',
                },
                'RedeemCollectedForNonClearedOrderId': {
                    'investment_id': 'scale_info::169',
                    'who': 'AccountId',
                },
                'RedeemCollectedWithoutActivePosition': {
                    'investment_id': 'scale_info::169',
                    'who': 'AccountId',
                },
                'RedeemOrderUpdated': {
                    'amount': 'u128',
                    'investment_id': 'scale_info::169',
                    'submitted_at': 'u64',
                    'who': 'AccountId',
                },
                'RedeemOrdersCleared': {
                    'fulfillment': 'scale_info::189',
                    'investment_id': 'scale_info::169',
                    'order_id': 'u64',
                },
                'RedeemOrdersCollected': {
                    'collection': 'scale_info::188',
                    'investment_id': 'scale_info::169',
                    'outcome': 'scale_info::187',
                    'processed_orders': ['u64'],
                    'who': 'AccountId',
                },
                'RedeemOrdersInProcessing': {
                    'investment_id': 'scale_info::169',
                    'order_id': 'u64',
                    'total_order': 'scale_info::190',
                },
            },
            'Keystore': {
                'DepositSet': {'new_deposit': 'u128'},
                'KeyAdded': {
                    'key': '[u8; 32]',
                    'key_type': 'scale_info::201',
                    'owner': 'AccountId',
                    'purpose': 'scale_info::200',
                },
                'KeyRevoked': {
                    'block_number': 'u32',
                    'key': '[u8; 32]',
                    'owner': 'AccountId',
                },
            },
            'Loans': {
                'Borrowed': {
                    'amount': 'u128',
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
                    'loan_info': 'scale_info::203',
                    'pool_id': 'u64',
                },
                'PortfolioValuationUpdated': {
                    'pool_id': 'u64',
                    'update_type': 'scale_info::219',
                    'valuation': 'u128',
                },
                'Repaid': {
                    'amount': 'u128',
                    'loan_id': 'u64',
                    'pool_id': 'u64',
                    'unchecked_amount': 'u128',
                },
                'WriteOffPolicyUpdated': {'policy': ['scale_info::221'], 'pool_id': 'u64'},
                'WrittenOff': {
                    'loan_id': 'u64',
                    'pool_id': 'u64',
                    'status': 'scale_info::218',
                },
            },
            'Migration': {
                'FailedToMigrateProxyDataFor': 'AccountId',
                'FailedToMigrateVestingFor': 'AccountId',
                'MigratedProxyDataFor': ('AccountId', 'u128', 'u64'),
                'MigratedProxyProxies': 'u32',
                'MigratedSystemAccounts': 'u32',
                'MigratedTotalIssuance': ('u128', 'u128'),
                'MigratedVestingAccounts': 'u32',
                'MigratedVestingFor': ('AccountId', 'u128', 'u128', 'u32'),
                'MigrationFinished': None,
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::37',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::37',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::38',
                    'timepoint': 'scale_info::37',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'Nfts': {'DepositAsset': '[u8; 32]'},
            'OrmlAssetRegistry': {
                'RegisteredAsset': {
                    'asset_id': 'scale_info::70',
                    'metadata': 'scale_info::131',
                },
                'UpdatedAsset': {
                    'asset_id': 'scale_info::70',
                    'metadata': 'scale_info::131',
                },
            },
            'OrmlTokens': {
                'BalanceSet': {
                    'currency_id': 'scale_info::70',
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Deposited': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::70',
                    'who': 'AccountId',
                },
                'DustLost': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::70',
                    'who': 'AccountId',
                },
                'Endowed': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::70',
                    'who': 'AccountId',
                },
                'LockRemoved': {
                    'currency_id': 'scale_info::70',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'LockSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::70',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::70',
                    'from': 'AccountId',
                    'status': 'scale_info::31',
                    'to': 'AccountId',
                },
                'Reserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::70',
                    'who': 'AccountId',
                },
                'Slashed': {
                    'currency_id': 'scale_info::70',
                    'free_amount': 'u128',
                    'reserved_amount': 'u128',
                    'who': 'AccountId',
                },
                'TotalIssuanceSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::70',
                },
                'Transfer': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::70',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unreserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::70',
                    'who': 'AccountId',
                },
                'Withdrawn': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::70',
                    'who': 'AccountId',
                },
            },
            'OrmlXcm': {
                'Sent': {'message': ['scale_info::99'], 'to': 'scale_info::87'},
            },
            'Permissions': {
                'Added': {
                    'role': 'scale_info::181',
                    'scope': 'scale_info::180',
                    'to': 'AccountId',
                },
                'Purged': {'from': 'AccountId', 'scope': 'scale_info::180'},
                'Removed': {
                    'from': 'AccountId',
                    'role': 'scale_info::181',
                    'scope': 'scale_info::180',
                },
            },
            'PolkadotXcm': {
                'AssetsClaimed': (
                    '[u8; 32]',
                    'scale_info::87',
                    'scale_info::117',
                ),
                'AssetsTrapped': (
                    '[u8; 32]',
                    'scale_info::87',
                    'scale_info::117',
                ),
                'Attempted': {
                    'Complete': 'u64',
                    'Error': 'scale_info::83',
                    'Incomplete': ('u64', 'scale_info::83'),
                },
                'InvalidResponder': (
                    'scale_info::87',
                    'u64',
                    (None, 'scale_info::87'),
                ),
                'InvalidResponderVersion': ('scale_info::87', 'u64'),
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
                'NotifyTargetMigrationFail': ('scale_info::122', 'u64'),
                'NotifyTargetSendFail': (
                    'scale_info::87',
                    'u64',
                    'scale_info::83',
                ),
                'ResponseReady': ('u64', 'scale_info::107'),
                'ResponseTaken': 'u64',
                'Sent': (
                    'scale_info::87',
                    'scale_info::87',
                    ['scale_info::99'],
                ),
                'SupportedVersionChanged': ('scale_info::87', 'u32'),
                'UnexpectedResponse': ('scale_info::87', 'u64'),
                'VersionChangeNotified': ('scale_info::87', 'u32'),
            },
            'PoolSystem': {
                'Created': {
                    'admin': 'AccountId',
                    'depositor': 'AccountId',
                    'essence': 'scale_info::168',
                    'pool_id': 'u64',
                },
                'EpochClosed': {'epoch_id': 'u32', 'pool_id': 'u64'},
                'EpochExecuted': {'epoch_id': 'u32', 'pool_id': 'u64'},
                'MaxReserveSet': {'pool_id': 'u64'},
                'Rebalanced': {'pool_id': 'u64'},
                'SolutionSubmitted': {
                    'epoch_id': 'u32',
                    'pool_id': 'u64',
                    'solution': 'scale_info::154',
                },
                'Updated': {
                    'id': 'u64',
                    'new': 'scale_info::168',
                    'old': 'scale_info::168',
                },
            },
            None: None,
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
            'PoolRegistry': {
                'MetadataSet': {'metadata': 'Bytes', 'pool_id': 'u64'},
                'Registered': {'pool_id': 'u64'},
                'UpdateExecuted': {'pool_id': 'u64'},
                'UpdateRegistered': {'pool_id': 'u64'},
                'UpdateStored': {'pool_id': 'u64'},
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
                    'proxy_type': 'scale_info::41',
                },
                'ProxyExecuted': {'result': 'scale_info::38'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::41',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::41',
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
                    'result': 'scale_info::38',
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
                    'currency_id': 'scale_info::70',
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Transfer': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::70',
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
                    'error': 'scale_info::24',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::38'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::24'},
            },
            'Vesting': {
                'VestingCompleted': {'account': 'AccountId'},
                'VestingUpdated': {'account': 'AccountId', 'unvested': 'u128'},
            },
            'XTokens': {
                'TransferredMultiAssets': {
                    'assets': ['scale_info::102'],
                    'dest': 'scale_info::87',
                    'fee': 'scale_info::102',
                    'sender': 'AccountId',
                },
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': (None, '[u8; 32]')},
                'BadVersion': {'message_hash': (None, '[u8; 32]')},
                'Fail': {
                    'error': 'scale_info::83',
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
    'base_block': {'proof_size': 0, 'ref_time': 358523000},
    'max_block': {'proof_size': 5242880, 'ref_time': 500000000000},
    'per_class': {
        'mandatory': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 98974000},
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 98974000},
            'max_extrinsic': {'proof_size': 3670016, 'ref_time': 349901026000},
            'max_total': {'proof_size': 3932160, 'ref_time': 375000000000},
            'reserved': {'proof_size': 0, 'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 98974000},
            'max_extrinsic': {'proof_size': 4980736, 'ref_time': 474901026000},
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
36
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
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 2),
        ('0xea93e3f16f3d6962', 2),
        ('0xc937d79c92c4e872', 1),
        ('0x9ce8a204acbb1235', 1),
        ('0x8f5c2d0094ecd047', 1),
        ('0x582211f65bb14b89', 4),
        ('0xe65b00e46cedd0aa', 2),
    ],
    'authoring_version': 1,
    'impl_name': 'centrifuge',
    'impl_version': 1,
    'spec_name': 'centrifuge',
    'spec_version': 1019,
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