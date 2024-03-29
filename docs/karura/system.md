
# System

---------
## Calls

---------
### kill_prefix
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
#### Attributes
No attributes

---------
### ExtrinsicFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispatch_error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}```
| dispatch_info | `DispatchInfo` | ```{'weight': {'ref_time': 'u64', 'proof_size': 'u64'}, 'class': ('Normal', 'Operational', 'Mandatory'), 'pays_fee': ('Yes', 'No')}```

---------
### ExtrinsicSuccess
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispatch_info | `DispatchInfo` | ```{'weight': {'ref_time': 'u64', 'proof_size': 'u64'}, 'class': ('Normal', 'Operational', 'Mandatory'), 'pays_fee': ('Yes', 'No')}```

---------
### KilledAccount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
### NewAccount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
### Remarked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| hash | `T::Hash` | ```[u8; 32]```

---------
## Storage functions

---------
### Account

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
            'AcalaOracle': {
                'NewFeedData': {
                    'sender': 'AccountId',
                    'values': [('scale_info::52', 'u128')],
                },
            },
            'AssetRegistry': {
                'AssetRegistered': {
                    'asset_id': 'scale_info::193',
                    'metadata': 'scale_info::192',
                },
                'AssetUpdated': {
                    'asset_id': 'scale_info::193',
                    'metadata': 'scale_info::192',
                },
                'ForeignAssetRegistered': {
                    'asset_address': 'scale_info::74',
                    'asset_id': 'u16',
                    'metadata': 'scale_info::192',
                },
                'ForeignAssetUpdated': {
                    'asset_address': 'scale_info::74',
                    'asset_id': 'u16',
                    'metadata': 'scale_info::192',
                },
            },
            'Auction': {
                'Bid': {
                    'amount': 'u128',
                    'auction_id': 'u32',
                    'bidder': 'AccountId',
                },
            },
            'AuctionManager': {
                'CancelAuction': {'auction_id': 'u32'},
                'CollateralAuctionAborted': {
                    'auction_id': 'u32',
                    'collateral_amount': 'u128',
                    'collateral_type': 'scale_info::52',
                    'refund_recipient': 'AccountId',
                    'target_stable_amount': 'u128',
                },
                'CollateralAuctionDealt': {
                    'auction_id': 'u32',
                    'collateral_amount': 'u128',
                    'collateral_type': 'scale_info::52',
                    'payment_amount': 'u128',
                    'winner': 'AccountId',
                },
                'DEXTakeCollateralAuction': {
                    'auction_id': 'u32',
                    'collateral_amount': 'u128',
                    'collateral_type': 'scale_info::52',
                    'supply_collateral_amount': 'u128',
                    'target_stable_amount': 'u128',
                },
                'NewCollateralAuction': {
                    'auction_id': 'u32',
                    'collateral_amount': 'u128',
                    'collateral_type': 'scale_info::52',
                    'target_bid_price': 'u128',
                },
            },
            'Authority': {
                'AuthorizedCall': {'caller': (None, 'AccountId'), 'hash': '[u8; 32]'},
                'Cancelled': {'index': 'u32', 'origin': 'scale_info::131'},
                'Delayed': {
                    'index': 'u32',
                    'origin': 'scale_info::131',
                    'when': 'u32',
                },
                'Dispatched': {'result': 'scale_info::33'},
                'FastTracked': {
                    'index': 'u32',
                    'origin': 'scale_info::131',
                    'when': 'u32',
                },
                'RemovedAuthorizedCall': {'hash': '[u8; 32]'},
                'Scheduled': {'index': 'u32', 'origin': 'scale_info::131'},
                'TriggeredCallBy': {'caller': 'AccountId', 'hash': '[u8; 32]'},
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
                    'destination_status': 'scale_info::50',
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
            'CdpEngine': {
                'CloseCDPInDebitByDEX': {
                    'collateral_type': 'scale_info::52',
                    'debit_value': 'u128',
                    'owner': 'AccountId',
                    'refund_collateral_amount': 'u128',
                    'sold_collateral_amount': 'u128',
                },
                'InterestRatePerSecUpdated': {
                    'collateral_type': 'scale_info::52',
                    'new_interest_rate_per_sec': (None, 'u128'),
                },
                'LiquidateUnsafeCDP': {
                    'bad_debt_value': 'u128',
                    'collateral_amount': 'u128',
                    'collateral_type': 'scale_info::52',
                    'owner': 'AccountId',
                    'target_amount': 'u128',
                },
                'LiquidationContractDeregistered': {'address': '[u8; 20]'},
                'LiquidationContractRegistered': {'address': '[u8; 20]'},
                'LiquidationPenaltyUpdated': {
                    'collateral_type': 'scale_info::52',
                    'new_liquidation_penalty': (None, 'u128'),
                },
                'LiquidationRatioUpdated': {
                    'collateral_type': 'scale_info::52',
                    'new_liquidation_ratio': (None, 'u128'),
                },
                'MaximumTotalDebitValueUpdated': {
                    'collateral_type': 'scale_info::52',
                    'new_total_debit_value': 'u128',
                },
                'RequiredCollateralRatioUpdated': {
                    'collateral_type': 'scale_info::52',
                    'new_required_collateral_ratio': (None, 'u128'),
                },
                'SettleCDPInDebit': {
                    'collateral_type': 'scale_info::52',
                    'owner': 'AccountId',
                },
            },
            'CdpTreasury': {
                'DebitOffsetBufferUpdated': {'amount': 'u128'},
                'ExpectedCollateralAuctionSizeUpdated': {
                    'collateral_type': 'scale_info::52',
                    'new_size': 'u128',
                },
            },
            'CollatorSelection': {
                'CandidateAdded': {'bond': 'u128', 'who': 'AccountId'},
                'CandidateRemoved': {'who': 'AccountId'},
                'NewCandidacyBond': {'new_candidacy_bond': 'u128'},
                'NewDesiredCandidates': {'new_desired_candidates': 'u32'},
                'NewInvulnerables': {'new_invulnerables': ['AccountId']},
            },
            'CumulusXcm': {
                'ExecutedDownward': ('[u8; 32]', 'scale_info::73'),
                'InvalidFormat': '[u8; 32]',
                'UnsupportedVersion': '[u8; 32]',
            },
            'Currencies': {
                'Deposited': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::52',
                    'who': 'AccountId',
                },
                'DustSwept': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::52',
                    'who': 'AccountId',
                },
                'Transferred': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::52',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Withdrawn': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::52',
                    'who': 'AccountId',
                },
            },
            'Democracy': {
                'Blacklisted': {'proposal_hash': '[u8; 32]'},
                'Cancelled': {'ref_index': 'u32'},
                'Delegated': {'target': 'AccountId', 'who': 'AccountId'},
                'ExternalTabled': None,
                'MetadataCleared': {
                    'hash': '[u8; 32]',
                    'owner': 'scale_info::154',
                },
                'MetadataSet': {
                    'hash': '[u8; 32]',
                    'owner': 'scale_info::154',
                },
                'MetadataTransferred': {
                    'hash': '[u8; 32]',
                    'owner': 'scale_info::154',
                    'prev_owner': 'scale_info::154',
                },
                'NotPassed': {'ref_index': 'u32'},
                'Passed': {'ref_index': 'u32'},
                'ProposalCanceled': {'prop_index': 'u32'},
                'Proposed': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Seconded': {'prop_index': 'u32', 'seconder': 'AccountId'},
                'Started': {
                    'ref_index': 'u32',
                    'threshold': 'scale_info::151',
                },
                'Tabled': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Undelegated': {'account': 'AccountId'},
                'Vetoed': {
                    'proposal_hash': '[u8; 32]',
                    'until': 'u32',
                    'who': 'AccountId',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::152',
                    'voter': 'AccountId',
                },
            },
            'Dex': {
                'AddLiquidity': {
                    'currency_0': 'scale_info::52',
                    'currency_1': 'scale_info::52',
                    'pool_0': 'u128',
                    'pool_1': 'u128',
                    'share_increment': 'u128',
                    'who': 'AccountId',
                },
                'AddProvision': {
                    'contribution_0': 'u128',
                    'contribution_1': 'u128',
                    'currency_0': 'scale_info::52',
                    'currency_1': 'scale_info::52',
                    'who': 'AccountId',
                },
                'DisableTradingPair': {
                    'trading_pair': ('scale_info::52', 'scale_info::52'),
                },
                'EnableTradingPair': {
                    'trading_pair': ('scale_info::52', 'scale_info::52'),
                },
                'ListProvisioning': {
                    'trading_pair': ('scale_info::52', 'scale_info::52'),
                },
                'ProvisioningAborted': {
                    'accumulated_provision_0': 'u128',
                    'accumulated_provision_1': 'u128',
                    'trading_pair': ('scale_info::52', 'scale_info::52'),
                },
                'ProvisioningToEnabled': {
                    'pool_0': 'u128',
                    'pool_1': 'u128',
                    'share_amount': 'u128',
                    'trading_pair': ('scale_info::52', 'scale_info::52'),
                },
                'RefundProvision': {
                    'contribution_0': 'u128',
                    'contribution_1': 'u128',
                    'currency_0': 'scale_info::52',
                    'currency_1': 'scale_info::52',
                    'who': 'AccountId',
                },
                'RemoveLiquidity': {
                    'currency_0': 'scale_info::52',
                    'currency_1': 'scale_info::52',
                    'pool_0': 'u128',
                    'pool_1': 'u128',
                    'share_decrement': 'u128',
                    'who': 'AccountId',
                },
                'Swap': {
                    'liquidity_changes': ['u128'],
                    'path': ['scale_info::52'],
                    'trader': 'AccountId',
                },
            },
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_hash': '[u8; 32]',
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::73',
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
            'EVM': {
                'ContractDevelopmentDisabled': {'who': 'AccountId'},
                'ContractDevelopmentEnabled': {'who': 'AccountId'},
                'ContractPublished': {'contract': '[u8; 20]'},
                'ContractSelfdestructed': {'contract': '[u8; 20]'},
                'ContractSetCode': {'contract': '[u8; 20]'},
                'Created': {
                    'contract': '[u8; 20]',
                    'from': '[u8; 20]',
                    'logs': ['scale_info::196'],
                    'used_gas': 'u64',
                    'used_storage': 'i32',
                },
                'CreatedFailed': {
                    'contract': '[u8; 20]',
                    'exit_reason': 'scale_info::199',
                    'from': '[u8; 20]',
                    'logs': ['scale_info::196'],
                    'used_gas': 'u64',
                    'used_storage': 'i32',
                },
                'Executed': {
                    'contract': '[u8; 20]',
                    'from': '[u8; 20]',
                    'logs': ['scale_info::196'],
                    'used_gas': 'u64',
                    'used_storage': 'i32',
                },
                'ExecutedFailed': {
                    'contract': '[u8; 20]',
                    'exit_reason': 'scale_info::199',
                    'from': '[u8; 20]',
                    'logs': ['scale_info::196'],
                    'output': 'Bytes',
                    'used_gas': 'u64',
                    'used_storage': 'i32',
                },
                'TransferredMaintainer': {
                    'contract': '[u8; 20]',
                    'new_maintainer': '[u8; 20]',
                },
            },
            'Earning': {
                'Bonded': {'amount': 'u128', 'who': 'AccountId'},
                'InstantUnbonded': {
                    'amount': 'u128',
                    'fee': 'u128',
                    'who': 'AccountId',
                },
                'Rebonded': {'amount': 'u128', 'who': 'AccountId'},
                'Unbonded': {'amount': 'u128', 'who': 'AccountId'},
                'Withdrawn': {'amount': 'u128', 'who': 'AccountId'},
            },
            'EmergencyShutdown': {
                'OpenRefund': {'block_number': 'u32'},
                'Refund': {
                    'refund_list': [('scale_info::52', 'u128')],
                    'stable_coin_amount': 'u128',
                    'who': 'AccountId',
                },
                'Shutdown': {'block_number': 'u32'},
            },
            'EvmAccounts': {
                'ClaimAccount': {
                    'account_id': 'AccountId',
                    'evm_address': '[u8; 20]',
                },
            },
            'FinancialCouncil': {
                'Approved': {'proposal_hash': '[u8; 32]'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': '[u8; 32]'},
                'Executed': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::33',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::33',
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
            'FinancialCouncilMembership': (
                'MemberAdded',
                'MemberRemoved',
                'MembersSwapped',
                'MembersReset',
                'KeyChanged',
                'Dummy',
            ),
            'GeneralCouncil': {
                'Approved': {'proposal_hash': '[u8; 32]'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': '[u8; 32]'},
                'Executed': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::33',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::33',
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
            'GeneralCouncilMembership': (
                'MemberAdded',
                'MemberRemoved',
                'MembersSwapped',
                'MembersReset',
                'KeyChanged',
                'Dummy',
            ),
            'Homa': {
                'BumpEraFrequencyUpdated': {'frequency': 'u32'},
                'CommissionRateUpdated': {'commission_rate': 'u128'},
                'CurrentEraBumped': {'new_era_index': 'u32'},
                'CurrentEraReset': {'new_era_index': 'u32'},
                'EstimatedRewardRatePerEraUpdated': {'reward_rate': 'u128'},
                'FastMatchFeeRateUpdated': {'fast_match_fee_rate': 'u128'},
                'LastEraBumpedBlockUpdated': {'last_era_bumped_block': 'u32'},
                'LedgerBondedReset': {
                    'new_bonded_amount': 'u128',
                    'sub_account_index': 'u16',
                },
                'LedgerUnlockingReset': {
                    'new_unlocking': ['scale_info::185'],
                    'sub_account_index': 'u16',
                },
                'Minted': {
                    'liquid_amount_added_to_void': 'u128',
                    'liquid_amount_received': 'u128',
                    'minter': 'AccountId',
                    'staking_currency_amount': 'u128',
                },
                'RedeemRequestCancelled': {
                    'cancelled_liquid_amount': 'u128',
                    'redeemer': 'AccountId',
                },
                'RedeemedByFastMatch': {
                    'fee_in_liquid': 'u128',
                    'matched_liquid_amount': 'u128',
                    'redeemed_staking_amount': 'u128',
                    'redeemer': 'AccountId',
                },
                'RedeemedByUnbond': {
                    'era_index_when_unbond': 'u32',
                    'liquid_amount': 'u128',
                    'redeemer': 'AccountId',
                    'unbonding_staking_amount': 'u128',
                },
                'RequestedRedeem': {
                    'allow_fast_match': 'bool',
                    'liquid_amount': 'u128',
                    'redeemer': 'AccountId',
                },
                'SoftBondedCapPerSubAccountUpdated': {'cap_amount': 'u128'},
                'WithdrawRedemption': {
                    'redeemer': 'AccountId',
                    'redemption_amount': 'u128',
                },
            },
            'HomaCouncil': {
                'Approved': {'proposal_hash': '[u8; 32]'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': '[u8; 32]'},
                'Executed': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::33',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::33',
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
            'HomaCouncilMembership': (
                'MemberAdded',
                'MemberRemoved',
                'MembersSwapped',
                'MembersReset',
                'KeyChanged',
                'Dummy',
            ),
            'Honzon': {
                'Authorization': {
                    'authorizee': 'AccountId',
                    'authorizer': 'AccountId',
                    'collateral_type': 'scale_info::52',
                },
                'TransferDebit': {
                    'amount': 'u128',
                    'from_currency': 'scale_info::52',
                    'to_currency': 'scale_info::52',
                },
                'UnAuthorization': {
                    'authorizee': 'AccountId',
                    'authorizer': 'AccountId',
                    'collateral_type': 'scale_info::52',
                },
                'UnAuthorizationAll': {'authorizer': 'AccountId'},
            },
            'HonzonBridge': {
                'BridgedStableCoinCurrencyIdSet': {
                    'bridged_stable_coin_currency_id': 'scale_info::52',
                },
                'FromBridged': {'amount': 'u128', 'who': 'AccountId'},
                'ToBridged': {'amount': 'u128', 'who': 'AccountId'},
            },
            'IdleScheduler': {
                'TaskAdded': {'task': 'scale_info::45', 'task_id': 'u32'},
                'TaskDispatched': {
                    'result': 'scale_info::33',
                    'task_id': 'u32',
                },
            },
            'Incentives': {
                'ClaimRewardDeductionRateUpdated': {
                    'deduction_rate': 'u128',
                    'pool': 'scale_info::189',
                },
                'ClaimRewards': {
                    'actual_amount': 'u128',
                    'deduction_amount': 'u128',
                    'pool': 'scale_info::189',
                    'reward_currency_id': 'scale_info::52',
                    'who': 'AccountId',
                },
                'DepositDexShare': {
                    'deposit': 'u128',
                    'dex_share_type': 'scale_info::52',
                    'who': 'AccountId',
                },
                'IncentiveRewardAmountUpdated': {
                    'pool': 'scale_info::189',
                    'reward_amount_per_period': 'u128',
                    'reward_currency_id': 'scale_info::52',
                },
                'WithdrawDexShare': {
                    'dex_share_type': 'scale_info::52',
                    'who': 'AccountId',
                    'withdraw': 'u128',
                },
            },
            'Loans': {
                'ConfiscateCollateralAndDebit': {
                    'collateral_type': 'scale_info::52',
                    'confiscated_collateral_amount': 'u128',
                    'deduct_debit_amount': 'u128',
                    'owner': 'AccountId',
                },
                'PositionUpdated': {
                    'collateral_adjustment': 'i128',
                    'collateral_type': 'scale_info::52',
                    'debit_adjustment': 'i128',
                    'owner': 'AccountId',
                },
                'TransferLoan': {
                    'currency_id': 'scale_info::52',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
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
                    'result': 'scale_info::33',
                    'timepoint': 'scale_info::37',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'NFT': {
                'BurnedToken': {
                    'class_id': 'u32',
                    'owner': 'AccountId',
                    'token_id': 'u64',
                },
                'BurnedTokenWithRemark': {
                    'class_id': 'u32',
                    'owner': 'AccountId',
                    'remark_hash': '[u8; 32]',
                    'token_id': 'u64',
                },
                'CreatedClass': {'class_id': 'u32', 'owner': 'AccountId'},
                'DestroyedClass': {'class_id': 'u32', 'owner': 'AccountId'},
                'MintedToken': {
                    'class_id': 'u32',
                    'from': 'AccountId',
                    'quantity': 'u32',
                    'to': 'AccountId',
                },
                'TransferredToken': {
                    'class_id': 'u32',
                    'from': 'AccountId',
                    'to': 'AccountId',
                    'token_id': 'u64',
                },
            },
            'OperatorMembershipAcala': (
                'MemberAdded',
                'MemberRemoved',
                'MembersSwapped',
                'MembersReset',
                'KeyChanged',
                'Dummy',
            ),
            'OrmlXcm': {
                'Sent': {'message': ['scale_info::84'], 'to': 'scale_info::74'},
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
            'Parameters': {'Updated': {'key_value': 'scale_info::161'}},
            'PolkadotXcm': {
                'AssetsClaimed': {
                    'assets': 'scale_info::110',
                    'hash': '[u8; 32]',
                    'origin': 'scale_info::74',
                },
                'AssetsTrapped': {
                    'assets': 'scale_info::110',
                    'hash': '[u8; 32]',
                    'origin': 'scale_info::74',
                },
                'Attempted': {'outcome': 'scale_info::73'},
                'FeesPaid': {'fees': ['scale_info::87'], 'paying': 'scale_info::74'},
                'InvalidQuerier': {
                    'expected_querier': 'scale_info::74',
                    'maybe_actual_querier': (None, 'scale_info::74'),
                    'origin': 'scale_info::74',
                    'query_id': 'u64',
                },
                'InvalidQuerierVersion': {
                    'origin': 'scale_info::74',
                    'query_id': 'u64',
                },
                'InvalidResponder': {
                    'expected_location': (None, 'scale_info::74'),
                    'origin': 'scale_info::74',
                    'query_id': 'u64',
                },
                'InvalidResponderVersion': {
                    'origin': 'scale_info::74',
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
                    'location': 'scale_info::124',
                    'query_id': 'u64',
                },
                'NotifyTargetSendFail': {
                    'error': 'scale_info::70',
                    'location': 'scale_info::74',
                    'query_id': 'u64',
                },
                'ResponseReady': {
                    'query_id': 'u64',
                    'response': 'scale_info::92',
                },
                'ResponseTaken': {'query_id': 'u64'},
                'Sent': {
                    'destination': 'scale_info::74',
                    'message': ['scale_info::84'],
                    'message_id': '[u8; 32]',
                    'origin': 'scale_info::74',
                },
                'SupportedVersionChanged': {
                    'location': 'scale_info::74',
                    'version': 'u32',
                },
                'UnexpectedResponse': {
                    'origin': 'scale_info::74',
                    'query_id': 'u64',
                },
                'VersionChangeNotified': {
                    'cost': ['scale_info::87'],
                    'destination': 'scale_info::74',
                    'message_id': '[u8; 32]',
                    'result': 'u32',
                },
                'VersionNotifyRequested': {
                    'cost': ['scale_info::87'],
                    'destination': 'scale_info::74',
                    'message_id': '[u8; 32]',
                },
                'VersionNotifyStarted': {
                    'cost': ['scale_info::87'],
                    'destination': 'scale_info::74',
                    'message_id': '[u8; 32]',
                },
                'VersionNotifyUnrequested': {
                    'cost': ['scale_info::87'],
                    'destination': 'scale_info::74',
                    'message_id': '[u8; 32]',
                },
            },
            'Preimage': {
                'Cleared': {'hash': '[u8; 32]'},
                'Noted': {'hash': '[u8; 32]'},
                'Requested': {'hash': '[u8; 32]'},
            },
            'Prices': {
                'LockPrice': {
                    'currency_id': 'scale_info::52',
                    'locked_price': 'u128',
                },
                'UnlockPrice': {'currency_id': 'scale_info::52'},
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
                    'proxy_type': 'scale_info::39',
                },
                'ProxyExecuted': {'result': 'scale_info::33'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::39',
                },
                'PureCreated': {
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::39',
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
                    'result': 'scale_info::33',
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
            'SessionManager': {
                'ScheduledSessionDuration': {
                    'block_number': 'u32',
                    'session_duration': 'u32',
                    'session_index': 'u32',
                },
            },
            'StableAsset': {
                'AModified': {
                    'pool_id': 'u32',
                    'time': 'u32',
                    'value': 'u128',
                },
                'BalanceUpdated': {
                    'new_balances': ['u128'],
                    'old_balances': ['u128'],
                    'pool_id': 'u32',
                },
                'CreatePool': {
                    'a': 'u128',
                    'pallet_id': 'AccountId',
                    'pool_id': 'u32',
                    'swap_id': 'AccountId',
                },
                'FeeCollected': {
                    'a': 'u128',
                    'amount': 'u128',
                    'new_balances': ['u128'],
                    'new_total_supply': 'u128',
                    'old_balances': ['u128'],
                    'old_total_supply': 'u128',
                    'pool_id': 'u32',
                    'who': 'AccountId',
                },
                'FeeModified': {
                    'mint_fee': 'u128',
                    'pool_id': 'u32',
                    'redeem_fee': 'u128',
                    'swap_fee': 'u128',
                },
                'Minted': {
                    'a': 'u128',
                    'balances': ['u128'],
                    'fee_amount': 'u128',
                    'input_amounts': ['u128'],
                    'min_output_amount': 'u128',
                    'minter': 'AccountId',
                    'output_amount': 'u128',
                    'pool_id': 'u32',
                    'total_supply': 'u128',
                },
                'RecipientModified': {
                    'fee_recipient': 'AccountId',
                    'pool_id': 'u32',
                    'yield_recipient': 'AccountId',
                },
                'RedeemedMulti': {
                    'a': 'u128',
                    'balances': ['u128'],
                    'fee_amount': 'u128',
                    'input_amount': 'u128',
                    'max_input_amount': 'u128',
                    'output_amounts': ['u128'],
                    'pool_id': 'u32',
                    'redeemer': 'AccountId',
                    'total_supply': 'u128',
                },
                'RedeemedProportion': {
                    'a': 'u128',
                    'balances': ['u128'],
                    'fee_amount': 'u128',
                    'input_amount': 'u128',
                    'min_output_amounts': ['u128'],
                    'output_amounts': ['u128'],
                    'pool_id': 'u32',
                    'redeemer': 'AccountId',
                    'total_supply': 'u128',
                },
                'RedeemedSingle': {
                    'a': 'u128',
                    'balances': ['u128'],
                    'fee_amount': 'u128',
                    'input_amount': 'u128',
                    'min_output_amount': 'u128',
                    'output_amount': 'u128',
                    'output_asset': 'scale_info::52',
                    'pool_id': 'u32',
                    'redeemer': 'AccountId',
                    'total_supply': 'u128',
                },
                'TokenSwapped': {
                    'a': 'u128',
                    'balances': ['u128'],
                    'input_amount': 'u128',
                    'input_asset': 'scale_info::52',
                    'min_output_amount': 'u128',
                    'output_amount': 'u128',
                    'output_asset': 'scale_info::52',
                    'pool_id': 'u32',
                    'swapper': 'AccountId',
                    'total_supply': 'u128',
                },
                'YieldCollected': {
                    'a': 'u128',
                    'amount': 'u128',
                    'new_total_supply': 'u128',
                    'old_total_supply': 'u128',
                    'pool_id': 'u32',
                    'who': 'AccountId',
                },
            },
            'Sudo': {
                'KeyChanged': {'old_sudoer': (None, 'AccountId')},
                'Sudid': {'sudo_result': 'scale_info::33'},
                'SudoAsDone': {'sudo_result': 'scale_info::33'},
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
                    'result': 'scale_info::33',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::33',
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
            'TechnicalCommitteeMembership': (
                'MemberAdded',
                'MemberRemoved',
                'MembersSwapped',
                'MembersReset',
                'KeyChanged',
                'Dummy',
            ),
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
                    'currency_id': 'scale_info::52',
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Deposited': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::52',
                    'who': 'AccountId',
                },
                'DustLost': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::52',
                    'who': 'AccountId',
                },
                'Endowed': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::52',
                    'who': 'AccountId',
                },
                'Issued': {'amount': 'u128', 'currency_id': 'scale_info::52'},
                'LockRemoved': {
                    'currency_id': 'scale_info::52',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'LockSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::52',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'Locked': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::52',
                    'who': 'AccountId',
                },
                'Rescinded': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::52',
                },
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::52',
                    'from': 'AccountId',
                    'status': 'scale_info::50',
                    'to': 'AccountId',
                },
                'Reserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::52',
                    'who': 'AccountId',
                },
                'Slashed': {
                    'currency_id': 'scale_info::52',
                    'free_amount': 'u128',
                    'reserved_amount': 'u128',
                    'who': 'AccountId',
                },
                'TotalIssuanceSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::52',
                },
                'Transfer': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::52',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unlocked': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::52',
                    'who': 'AccountId',
                },
                'Unreserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::52',
                    'who': 'AccountId',
                },
                'Withdrawn': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::52',
                    'who': 'AccountId',
                },
            },
            'TransactionPause': {
                'EvmPrecompilePaused': {'address': '[u8; 20]'},
                'EvmPrecompileUnpaused': {'address': '[u8; 20]'},
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
                'ChargeFeePoolDisabled': {
                    'currency_id': 'scale_info::52',
                    'foreign_amount': 'u128',
                    'native_amount': 'u128',
                },
                'ChargeFeePoolEnabled': {
                    'currency_id': 'scale_info::52',
                    'exchange_rate': 'u128',
                    'pool_size': 'u128',
                    'sub_account': 'AccountId',
                    'swap_threshold': 'u128',
                },
                'ChargeFeePoolSwapped': {
                    'new_exchange_rate': 'u128',
                    'new_pool_size': 'u128',
                    'old_exchange_rate': 'u128',
                    'sub_account': 'AccountId',
                    'supply_currency_id': 'scale_info::52',
                    'swap_exchange_rate': 'u128',
                },
                'TransactionFeePaid': {
                    'actual_fee': 'u128',
                    'actual_surplus': 'u128',
                    'actual_tip': 'u128',
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
            'UnknownTokens': {
                'Deposited': {
                    'asset': 'scale_info::87',
                    'who': 'scale_info::74',
                },
                'Withdrawn': {
                    'asset': 'scale_info::87',
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
                'DispatchedAs': {'result': 'scale_info::33'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::25'},
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
                    'assets': ['scale_info::87'],
                    'dest': 'scale_info::74',
                    'fee': 'scale_info::87',
                    'sender': 'AccountId',
                },
            },
            'XcmInterface': {
                'XcmDestWeightUpdated': {
                    'new_xcm_dest_weight': 'scale_info::9',
                    'xcm_operation': 'scale_info::187',
                },
                'XcmFeeUpdated': {
                    'new_xcm_dest_weight': 'u128',
                    'xcm_operation': 'scale_info::187',
                },
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': '[u8; 32]'},
                'BadVersion': {'message_hash': '[u8; 32]'},
                'Fail': {
                    'error': 'scale_info::70',
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
                'XcmpMessageSent': {'message_hash': '[u8; 32]'},
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
#### Value
```python
1200
```
#### Python
```python
constant = substrate.get_constant('System', 'BlockHashCount')
```
---------
### BlockLength
#### Value
```python
{'max': {'mandatory': 5242880, 'normal': 3670016, 'operational': 5242880}}
```
#### Python
```python
constant = substrate.get_constant('System', 'BlockLength')
```
---------
### BlockWeights
#### Value
```python
{
    'base_block': {'proof_size': 0, 'ref_time': 390584000},
    'max_block': {'proof_size': 52428800, 'ref_time': 500000000000},
    'per_class': {
        'mandatory': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 124414000},
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 124414000},
            'max_extrinsic': {
                'proof_size': 31457280,
                'ref_time': 299875586000,
            },
            'max_total': {'proof_size': 36700160, 'ref_time': 350000000000},
            'reserved': {'proof_size': 0, 'ref_time': 0},
        },
        'operational': {
            'base_extrinsic': {'proof_size': 0, 'ref_time': 124414000},
            'max_extrinsic': {
                'proof_size': 47185920,
                'ref_time': 449875586000,
            },
            'max_total': {'proof_size': 52428800, 'ref_time': 500000000000},
            'reserved': {'proof_size': 15728640, 'ref_time': 150000000000},
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
#### Value
```python
8
```
#### Python
```python
constant = substrate.get_constant('System', 'SS58Prefix')
```
---------
### Version
#### Value
```python
{
    'apis': [
        ('0xdf6acb689907609b', 4),
        ('0x37e397fc7c91f5e4', 2),
        ('0x40fe3ad401f8959a', 6),
        ('0xd2bc9897eed08f15', 3),
        ('0xf78b278be53f454c', 2),
        ('0xdd718d5cc53262d4', 1),
        ('0xab3c0572291feb8b', 1),
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 4),
        ('0x6ef953004ba30e59', 1),
        ('0x955e168e0cfb3409', 1),
        ('0xe3df3f2aa8a5cc57', 2),
        ('0xea93e3f16f3d6962', 2),
    ],
    'authoring_version': 1,
    'impl_name': 'karura',
    'impl_version': 0,
    'spec_name': 'karura',
    'spec_version': 2210,
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

---------
### FailedToExtractRuntimeVersion

---------
### InvalidSpecName

---------
### NonDefaultComposite

---------
### NonZeroRefCount

---------
### SpecVersionNeedsToIncrease

---------