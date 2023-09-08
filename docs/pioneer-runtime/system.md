
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
            'AssetManager': {
                'AssetRegistered': {
                    'asset_id': 'scale_info::133',
                    'metadata': 'scale_info::132',
                },
                'AssetUpdated': {
                    'asset_id': 'scale_info::44',
                    'metadata': 'scale_info::132',
                },
                'ForeignAssetRegistered': {
                    'asset_address': 'scale_info::59',
                    'asset_id': 'u64',
                    'metadata': 'scale_info::132',
                },
                'ForeignAssetUpdated': {
                    'asset_address': 'scale_info::59',
                    'asset_id': 'u64',
                    'metadata': 'scale_info::132',
                },
            },
            'Auction': {
                'AuctionCancelled': 'u64',
                'AuctionExtended': ('u64', 'u32'),
                'AuctionFinalized': ('u64', 'AccountId', 'u128'),
                'AuctionFinalizedNoBid': 'u64',
                'Bid': ('u64', 'AccountId', 'u128'),
                'BuyNowFinalised': ('u64', 'AccountId', 'u128'),
                'CollectionAuthorizationRemoveInMetaverse': ('u32', 'u64'),
                'CollectionAuthorizedInMetaverse': ('u32', 'u64'),
                'NewAuctionItem': (
                    'u64',
                    'AccountId',
                    'scale_info::123',
                    'u128',
                    'u128',
                    'u32',
                ),
                'NftOfferAccepted': ('u32', 'u64', 'AccountId'),
                'NftOfferMade': ('u32', 'u64', 'AccountId', 'u128'),
                'NftOfferWithdrawn': ('u32', 'u64', 'AccountId'),
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
                    'destination_status': 'scale_info::39',
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
            'Continuum': {
                'ContinuumEmergencyShutdownEnabled': None,
                'ContinuumSpotTransferred': (
                    'AccountId',
                    'AccountId',
                    ('i32', 'i32'),
                ),
                'FinalizedVote': 'u64',
                'NewAuctionSlotRotated': 'u32',
                'NewContinuumNeighbourHoodProtocolStarted': ('u32', 'u64'),
                'NewContinuumReferendumStarted': ('u32', 'u64'),
                'NewExpressOfInterestAdded': ('AccountId', 'u64'),
                'NewMapSpotIssued': (('i32', 'i32'), 'AccountId'),
                'NewMaxAuctionSlotSet': 'u8',
                'NewMaxBoundSet': ('i32', 'i32'),
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
            'Crowdloan': {
                'AddedDistributorOrigin': 'AccountId',
                'RemovedDistributorOrigin': 'AccountId',
                'RemovedRewardVestingSchedule': ('AccountId', 'u32'),
                'TokenTransferred': ('AccountId', 'u128'),
                'VestedTokenTransferred': ('AccountId', 'scale_info::145'),
            },
            'CumulusXcm': {
                'ExecutedDownward': ('[u8; 8]', 'scale_info::58'),
                'InvalidFormat': '[u8; 8]',
                'UnsupportedVersion': '[u8; 8]',
            },
            'Currencies': {
                'BalanceUpdated': ('scale_info::44', 'AccountId', 'i128'),
                'Deposited': ('scale_info::44', 'AccountId', 'u128'),
                'Transferred': (
                    'scale_info::44',
                    'AccountId',
                    'AccountId',
                    'u128',
                ),
                'Withdrawn': ('scale_info::44', 'AccountId', 'u128'),
            },
            'Democracy': {
                'Blacklisted': {'proposal_hash': '[u8; 32]'},
                'Cancelled': {'ref_index': 'u32'},
                'Delegated': {'target': 'AccountId', 'who': 'AccountId'},
                'Executed': {'ref_index': 'u32', 'result': 'scale_info::31'},
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
                'Started': {
                    'ref_index': 'u32',
                    'threshold': 'scale_info::105',
                },
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
                    'vote': 'scale_info::106',
                    'voter': 'AccountId',
                },
            },
            'DmpQueue': {
                'ExecutedDownward': {
                    'message_id': '[u8; 32]',
                    'outcome': 'scale_info::58',
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
            'Economy': {
                'BitPowerExchangeRateUpdated': 'u128',
                'CancelPowerConversionRequest': (('u32', 'u64'), 'AccountId'),
                'EstateStakedToEconomy101': ('AccountId', 'u64', 'u128'),
                'EstateStakingRemovedFromEconomy101': (
                    'AccountId',
                    'u64',
                    'u128',
                ),
                'MiningResourceBurned': 'u128',
                'SelfStakedToEconomy101': ('AccountId', 'u128'),
                'SelfStakingRemovedFromEconomy101': ('AccountId', 'u128'),
                'SetPowerBalance': ('AccountId', 'u64'),
                'UnstakedAmountWithdrew': ('AccountId', 'u128'),
            },
            'Emergency': {
                'EmergencyStopped': {
                    'function_name_bytes': 'Bytes',
                    'pallet_name_bytes': 'Bytes',
                },
                'EmergencyUnStopped': {
                    'function_name_bytes': 'Bytes',
                    'pallet_name_bytes': 'Bytes',
                },
                'MaintenanceModeEnded': None,
                'MaintenanceModeStarted': None,
            },
            'Estate': {
                'EstateDestroyed': ('u64', 'scale_info::129'),
                'EstateLeaseContractCancelled': 'u64',
                'EstateLeaseContractEnded': 'u64',
                'EstateLeaseOfferAccepted': ('u64', 'AccountId', 'u32'),
                'EstateLeaseOfferCreated': ('AccountId', 'u64', 'u128'),
                'EstateLeaseOfferRemoved': ('AccountId', 'u64'),
                'EstateRentCollected': ('u64', 'u128'),
                'EstateUpdated': ('u64', 'scale_info::129', [('i32', 'i32')]),
                'LandBlockDeployed': (
                    'AccountId',
                    'u64',
                    'u128',
                    [('i32', 'i32')],
                ),
                'LandUnitAdded': ('u64', 'scale_info::129', [('i32', 'i32')]),
                'LandUnitsRemoved': ('u64', 'scale_info::129', [('i32', 'i32')]),
                'MaxBoundSet': ('u64', ('i32', 'i32')),
                'NewEstateMinted': (
                    'u64',
                    'scale_info::129',
                    'u64',
                    [('i32', 'i32')],
                ),
                'NewLandUnitMinted': ('scale_info::129', 'u64', ('i32', 'i32')),
                'NewLandsMinted': ('AccountId', 'u64', [('i32', 'i32')]),
                'NewRound': ('u32', 'u32', 'u64'),
                'TransferredEstate': ('u64', 'AccountId', 'AccountId'),
                'TransferredLandUnit': ('u64', ('i32', 'i32'), 'AccountId', 'AccountId'),
                'UndeployedLandBlockApproved': (
                    'AccountId',
                    'AccountId',
                    'u128',
                ),
                'UndeployedLandBlockBurnt': 'u128',
                'UndeployedLandBlockFreezed': 'u128',
                'UndeployedLandBlockIssued': ('AccountId', 'u128'),
                'UndeployedLandBlockTransferred': (
                    'AccountId',
                    'AccountId',
                    'u128',
                ),
                'UndeployedLandBlockUnapproved': 'u128',
                'UndeployedLandBlockUnfreezed': 'u128',
            },
            'Metaverse': {
                'MetaverseDestroyed': 'u64',
                'MetaverseFreezed': 'u64',
                'MetaverseListingFeeUpdated': ('u64', 'u32'),
                'MetaverseMintedNewCurrency': ('u64', 'scale_info::44'),
                'MetaverseStaked': ('AccountId', 'u64', 'u128'),
                'MetaverseStakingRewarded': (
                    'AccountId',
                    'u64',
                    'u32',
                    'u128',
                ),
                'MetaverseTreasuryFundsWithdrawn': 'u64',
                'MetaverseUnfreezed': 'u64',
                'MetaverseUnstaked': ('AccountId', 'u64', 'u128'),
                'NewMetaverseCreated': ('u64', 'AccountId'),
                'NewMetaverseRegisteredForStaking': ('u64', 'AccountId'),
                'TransferredMetaverse': ('u64', 'AccountId', 'AccountId'),
            },
            'Mining': {
                'AddNewMiningOrigin': 'AccountId',
                'DepositMiningResource': ('AccountId', 'u128'),
                'MiningConfigUpdated': ('u32', 'scale_info::113'),
                'MiningResourceBurnFrom': ('AccountId', 'u128'),
                'MiningResourceBurned': 'u128',
                'MiningResourceMinted': 'u128',
                'MiningResourceMintedTo': ('AccountId', 'u128'),
                'MiningRoundPaused': ('u32', 'u32'),
                'MiningRoundUnPaused': ('u32', 'u32'),
                'NewMiningRound': ('u32', 'scale_info::112'),
                'RemoveMiningOrigin': 'AccountId',
                'RoundLengthUpdated': 'u32',
                'WithdrawMiningResource': ('AccountId', 'u128'),
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::36',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::36',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::31',
                    'timepoint': 'scale_info::36',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'Nft': {
                'BurnedNft': ('u32', 'u64'),
                'ClassFundsWithdrawn': 'u32',
                'ClassRoyaltyFeeUpdated': ('u32', 'u32'),
                'ClassTotalIssuanceUpdated': ('u32', 'u64'),
                'CollectionLocked': 'u32',
                'CollectionUnlocked': 'u32',
                'ExecutedNft': 'u64',
                'ForceTransferredNft': (
                    'AccountId',
                    'AccountId',
                    'u64',
                    ('u32', 'u64'),
                ),
                'HardLimitSet': 'u32',
                'NewNftClassCreated': ('AccountId', 'u32'),
                'NewNftCollectionCreated': 'u64',
                'NewNftMinted': (('u32', 'u64'), ('u32', 'u64'), 'AccountId', 'u32', 'u32', 'u64'),
                'NewStackableNftMinted': ('AccountId', 'u32', 'u64', 'u128'),
                'NewTimeCapsuleMinted': (
                    ('u32', 'u64'),
                    'AccountId',
                    'u32',
                    'u64',
                    'u32',
                    'Bytes',
                ),
                'NftUnlocked': ('u32', 'u64'),
                'PromotionEnabled': 'bool',
                'ScheduledTimeCapsule': ('u64', 'Bytes', 'u32'),
                'SignedNft': ('u64', 'AccountId'),
                'TransferedNft': (
                    'AccountId',
                    'AccountId',
                    'u64',
                    ('u32', 'u64'),
                ),
                'TransferedStackableNft': (
                    'AccountId',
                    'AccountId',
                    ('u32', 'u64'),
                    'u128',
                ),
            },
            'OracleMembership': (
                'MemberAdded',
                'MemberRemoved',
                'MembersSwapped',
                'MembersReset',
                'KeyChanged',
                'Dummy',
            ),
            'OrmlXcm': {
                'Sent': {'message': ['scale_info::72'], 'to': 'scale_info::59'},
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
                    'scale_info::90',
                ),
                'Attempted': {
                    'Complete': 'u64',
                    'Error': 'scale_info::55',
                    'Incomplete': ('u64', 'scale_info::55'),
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
                'NotifyTargetMigrationFail': ('scale_info::95', 'u64'),
                'NotifyTargetSendFail': (
                    'scale_info::59',
                    'u64',
                    'scale_info::55',
                ),
                'ResponseReady': ('u64', 'scale_info::80'),
                'ResponseTaken': 'u64',
                'Sent': (
                    'scale_info::59',
                    'scale_info::59',
                    ['scale_info::72'],
                ),
                'SupportedVersionChanged': ('scale_info::59', 'u32'),
                'UnexpectedResponse': ('scale_info::59', 'u64'),
                'VersionChangeNotified': ('scale_info::59', 'u32'),
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
                'AnonymousCreated': {
                    'anonymous': 'AccountId',
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::136',
                    'who': 'AccountId',
                },
                'ProxyAdded': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::136',
                },
                'ProxyExecuted': {'result': 'scale_info::31'},
                'ProxyRemoved': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::136',
                },
            },
            'Reward': {
                'NewRewardCampaignCreated': ('u32', 'AccountId'),
                'NftRewardClaimed': ('u32', 'AccountId', [('u32', 'u64')]),
                'RewardCampaignCanceled': 'u32',
                'RewardCampaignClosed': 'u32',
                'RewardCampaignEnded': 'u32',
                'RewardCampaignRootClosed': 'u32',
                'RewardClaimed': ('u32', 'AccountId', 'u128'),
                'SetNftReward': ('u32', [('AccountId', [('u32', 'u64')])]),
                'SetNftRewardRoot': ('u32', '[u8; 32]'),
                'SetReward': ('u32', [('AccountId', 'u128')]),
                'SetRewardOriginAdded': 'AccountId',
                'SetRewardOriginRemoved': 'AccountId',
                'SetRewardRoot': ('u32', 'u128', '[u8; 32]'),
            },
            'RewardOracle': {
                'NewFeedData': {
                    'sender': 'AccountId',
                    'values': [('u32', 'Bytes')],
                },
            },
            'Scheduler': {
                'CallLookupFailed': {
                    'error': 'scale_info::33',
                    'id': (None, 'Bytes'),
                    'task': ('u32', 'u32'),
                },
                'Canceled': {'index': 'u32', 'when': 'u32'},
                'Dispatched': {
                    'id': (None, 'Bytes'),
                    'result': 'scale_info::31',
                    'task': ('u32', 'u32'),
                },
                'Scheduled': {'index': 'u32', 'when': 'u32'},
            },
            'Session': {'NewSession': {'session_index': 'u32'}},
            'Sudo': {
                'KeyChanged': {'old_sudoer': (None, 'AccountId')},
                'Sudid': {'sudo_result': 'scale_info::31'},
                'SudoAsDone': {'sudo_result': 'scale_info::31'},
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
            'Tokens': {
                'BalanceSet': {
                    'currency_id': 'scale_info::44',
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Deposited': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::44',
                    'who': 'AccountId',
                },
                'DustLost': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::44',
                    'who': 'AccountId',
                },
                'Endowed': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::44',
                    'who': 'AccountId',
                },
                'LockRemoved': {
                    'currency_id': 'scale_info::44',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'LockSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::44',
                    'lock_id': '[u8; 8]',
                    'who': 'AccountId',
                },
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::44',
                    'from': 'AccountId',
                    'status': 'scale_info::39',
                    'to': 'AccountId',
                },
                'Reserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::44',
                    'who': 'AccountId',
                },
                'Slashed': {
                    'currency_id': 'scale_info::44',
                    'free_amount': 'u128',
                    'reserved_amount': 'u128',
                    'who': 'AccountId',
                },
                'TotalIssuanceSet': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::44',
                },
                'Transfer': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::44',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unreserved': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::44',
                    'who': 'AccountId',
                },
                'Withdrawn': {
                    'amount': 'u128',
                    'currency_id': 'scale_info::44',
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
            'UnknownTokens': {
                'Deposited': {
                    'asset': 'scale_info::75',
                    'who': 'scale_info::59',
                },
                'Withdrawn': {
                    'asset': 'scale_info::75',
                    'who': 'scale_info::59',
                },
            },
            None: None,
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
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::22',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::31'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::22'},
            },
            'Vesting': {
                'VestingCompleted': {'account': 'AccountId'},
                'VestingUpdated': {'account': 'AccountId', 'unvested': 'u128'},
            },
            'XTokens': {
                'TransferredMultiAssets': {
                    'assets': ['scale_info::75'],
                    'dest': 'scale_info::59',
                    'fee': 'scale_info::75',
                    'sender': 'AccountId',
                },
            },
            'XcmpQueue': {
                'BadFormat': {'message_hash': (None, '[u8; 32]')},
                'BadVersion': {'message_hash': (None, '[u8; 32]')},
                'Fail': {
                    'error': 'scale_info::55',
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
            'max_extrinsic': 349913702000,
            'max_total': 375000000000,
            'reserved': 0,
        },
        'operational': {
            'base_extrinsic': 86298000,
            'max_extrinsic': 474913702000,
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
268
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
        ('0x37c8bb1350a9a2a8', 1),
        ('0xea93e3f16f3d6962', 2),
    ],
    'authoring_version': 1,
    'impl_name': 'pioneer-runtime',
    'impl_version': 0,
    'spec_name': 'pioneer-runtime',
    'spec_version': 19,
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