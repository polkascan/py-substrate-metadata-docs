
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
            'AppWorkingGroup': {
                'ApplicationWithdrawn': 'u64',
                'AppliedOnOpening': ('scale_info::218', 'u64'),
                'BudgetSet': 'u128',
                'BudgetSpending': ('AccountId', 'u128', (None, 'Bytes')),
                'LeadRemarked': 'Bytes',
                'LeaderSet': 'u64',
                'LeaderUnset': None,
                'NewMissedRewardLevelReached': ('u64', (None, 'u128')),
                'OpeningAdded': (
                    'u64',
                    'Bytes',
                    'scale_info::217',
                    'scale_info::210',
                    (None, 'u128'),
                ),
                'OpeningCanceled': 'u64',
                'OpeningFilled': ('u64', 'scale_info::214', 'scale_info::84'),
                'RewardPaid': ('u64', 'AccountId', 'u128', 'scale_info::221'),
                'StakeDecreased': ('u64', 'u128'),
                'StakeIncreased': ('u64', 'u128'),
                'StakeSlashed': ('u64', 'u128', 'u128', (None, 'Bytes')),
                'StatusTextChanged': ('[u8; 32]', (None, 'Bytes')),
                'TerminatedLeader': ('u64', (None, 'u128'), (None, 'Bytes')),
                'TerminatedWorker': ('u64', (None, 'u128'), (None, 'Bytes')),
                'WorkerExited': 'u64',
                'WorkerRemarked': ('u64', 'Bytes'),
                'WorkerRewardAccountUpdated': ('u64', 'AccountId'),
                'WorkerRewardAmountUpdated': ('u64', (None, 'u128')),
                'WorkerRoleAccountUpdated': ('u64', 'AccountId'),
                'WorkerStartedLeaving': ('u64', (None, 'Bytes')),
                'WorkingGroupBudgetFunded': ('u64', 'u128', 'Bytes'),
            },
            'BagsList': {
                'Rebagged': {'from': 'u64', 'to': 'u64', 'who': 'AccountId'},
                'ScoreUpdated': {'new_score': 'u64', 'who': 'AccountId'},
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
            'Bounty': {
                'BountyContributorRemarked': (
                    'scale_info::88',
                    'u64',
                    'Bytes',
                ),
                'BountyCreated': ('u64', 'scale_info::87', 'Bytes'),
                'BountyCreatorCherryWithdrawal': ('u64', 'scale_info::88'),
                'BountyCreatorOracleRewardWithdrawal': (
                    'u64',
                    'scale_info::88',
                ),
                'BountyCreatorRemarked': ('scale_info::88', 'u64', 'Bytes'),
                'BountyEntrantRemarked': ('u64', 'u64', 'u64', 'Bytes'),
                'BountyFunded': ('u64', 'scale_info::88', 'u128'),
                'BountyFundingWithdrawal': ('u64', 'scale_info::88'),
                'BountyMaxFundingReached': 'u64',
                'BountyOracleRemarked': ('scale_info::88', 'u64', 'Bytes'),
                'BountyOracleRewardWithdrawal': (
                    'u64',
                    'scale_info::88',
                    'u128',
                ),
                'BountyOracleSwitched': (
                    'u64',
                    'scale_info::88',
                    'scale_info::88',
                    'scale_info::88',
                ),
                'BountyRemoved': 'u64',
                'BountyTerminated': (
                    'u64',
                    'scale_info::88',
                    'scale_info::88',
                    'scale_info::88',
                ),
                'CreatorStateBloatBondWithdrawn': (
                    'u64',
                    'scale_info::88',
                    'u128',
                ),
                'FunderStateBloatBondWithdrawn': (
                    'u64',
                    'scale_info::88',
                    'u128',
                ),
                'OracleJudgmentSubmitted': (
                    'u64',
                    'scale_info::88',
                    'scale_info::91',
                    'Bytes',
                ),
                'WorkEntrantFundsWithdrawn': ('u64', 'u64', 'u64'),
                'WorkEntrantStakeSlashed': ('u64', 'u64', 'AccountId', 'u128'),
                'WorkEntrantStakeUnlocked': ('u64', 'u64', 'AccountId'),
                'WorkEntryAnnounced': (
                    'u64',
                    'u64',
                    'u64',
                    'AccountId',
                    'Bytes',
                ),
                'WorkSubmissionPeriodEnded': ('u64', 'scale_info::88'),
                'WorkSubmitted': ('u64', 'u64', 'u64', 'Bytes'),
            },
            'Constitution': {'ConstutionAmended': ('[u8; 32]', 'Bytes')},
            'Content': {
                'AuctionBidCanceled': ('u64', 'u64'),
                'AuctionBidMade': ('u64', 'u64', 'u128', (None, 'u64')),
                'AuctionCanceled': ('scale_info::99', 'u64'),
                'BidMadeCompletingAuction': ('u64', 'u64', (None, 'u64')),
                'BuyNowCanceled': ('u64', 'scale_info::99'),
                'BuyNowPriceUpdated': ('u64', 'scale_info::99', 'u128'),
                'CancelChannelTransfer': ('u64', 'scale_info::99'),
                'ChannelAgentRemarked': ('scale_info::99', 'u64', 'Bytes'),
                'ChannelAssetsDeletedByModerator': (
                    'scale_info::99',
                    'u64',
                    'scale_info::84',
                    'Bytes',
                ),
                'ChannelAssetsRemoved': (
                    'scale_info::99',
                    'u64',
                    'scale_info::84',
                    'scale_info::100',
                ),
                'ChannelCreated': (
                    'u64',
                    'scale_info::100',
                    'scale_info::127',
                    'AccountId',
                ),
                'ChannelDeleted': ('scale_info::99', 'u64'),
                'ChannelDeletedByModerator': (
                    'scale_info::99',
                    'u64',
                    'Bytes',
                ),
                'ChannelFundsWithdrawn': (
                    'scale_info::99',
                    'u64',
                    'u128',
                    'scale_info::155',
                ),
                'ChannelNftLimitUpdated': (
                    'scale_info::99',
                    'scale_info::156',
                    'u64',
                    'u64',
                ),
                'ChannelOwnerRemarked': ('u64', 'Bytes'),
                'ChannelPausedFeaturesUpdatedByModerator': (
                    'scale_info::99',
                    'u64',
                    'scale_info::112',
                    'Bytes',
                ),
                'ChannelPayoutsUpdated': ('scale_info::150', (None, 'u64'), 'AccountId'),
                'ChannelPrivilegeLevelUpdated': ('u64', 'u8'),
                'ChannelRewardClaimedAndWithdrawn': (
                    'scale_info::99',
                    'u64',
                    'u128',
                    'scale_info::155',
                ),
                'ChannelRewardUpdated': ('u128', 'u128', 'u64'),
                'ChannelStateBloatBondValueUpdated': 'u128',
                'ChannelTransferAccepted': ('u64', 'scale_info::149'),
                'ChannelUpdated': (
                    'scale_info::99',
                    'u64',
                    'scale_info::138',
                    'scale_info::84',
                ),
                'ChannelVisibilitySetByModerator': (
                    'scale_info::99',
                    'u64',
                    'bool',
                    'Bytes',
                ),
                'CreatorTokenIssued': ('scale_info::99', 'u64', 'u64'),
                'CuratorAdded': ('u64', 'u64', 'scale_info::105'),
                'CuratorGroupCreated': 'u64',
                'CuratorGroupPermissionsUpdated': ('u64', 'scale_info::143'),
                'CuratorGroupStatusSet': ('u64', 'bool'),
                'CuratorRemoved': ('u64', 'u64'),
                'EnglishAuctionSettled': ('u64', 'AccountId', 'u64'),
                'EnglishAuctionStarted': (
                    'scale_info::99',
                    'u64',
                    'scale_info::121',
                ),
                'GlobalNftLimitUpdated': ('scale_info::156', 'u64'),
                'InitializedChannelTransfer': (
                    'u64',
                    'scale_info::99',
                    'scale_info::117',
                ),
                'NftBought': ('u64', 'u64'),
                'NftDestroyed': ('scale_info::99', 'u64'),
                'NftIssued': ('scale_info::99', 'u64', 'scale_info::124'),
                'NftOwnerRemarked': ('scale_info::99', 'u64', 'Bytes'),
                'NftSellOrderMade': ('u64', 'scale_info::99', 'u128'),
                'NftSlingedBackToTheOriginalArtist': ('u64', 'scale_info::99'),
                'OfferAccepted': 'u64',
                'OfferCanceled': ('u64', 'scale_info::99'),
                'OfferStarted': (
                    'u64',
                    'scale_info::99',
                    'u64',
                    (None, 'u128'),
                ),
                'OpenAuctionBidAccepted': (
                    'scale_info::99',
                    'u64',
                    'u64',
                    'u128',
                ),
                'OpenAuctionStarted': (
                    'scale_info::99',
                    'u64',
                    'scale_info::123',
                    'u64',
                ),
                'ToggledNftLimits': 'bool',
                'VideoAssetsDeletedByModerator': (
                    'scale_info::99',
                    'u64',
                    'scale_info::84',
                    'bool',
                    'Bytes',
                ),
                'VideoCreated': (
                    'scale_info::99',
                    'u64',
                    'u64',
                    'scale_info::140',
                    'scale_info::84',
                ),
                'VideoDeleted': ('scale_info::99', 'u64'),
                'VideoDeletedByModerator': ('scale_info::99', 'u64', 'Bytes'),
                'VideoStateBloatBondValueUpdated': 'u128',
                'VideoUpdated': (
                    'scale_info::99',
                    'u64',
                    'scale_info::142',
                    'scale_info::84',
                ),
                'VideoVisibilitySetByModerator': (
                    'scale_info::99',
                    'u64',
                    'bool',
                    'Bytes',
                ),
            },
            'ContentWorkingGroup': {
                'ApplicationWithdrawn': 'u64',
                'AppliedOnOpening': ('scale_info::218', 'u64'),
                'BudgetSet': 'u128',
                'BudgetSpending': ('AccountId', 'u128', (None, 'Bytes')),
                'LeadRemarked': 'Bytes',
                'LeaderSet': 'u64',
                'LeaderUnset': None,
                'NewMissedRewardLevelReached': ('u64', (None, 'u128')),
                'OpeningAdded': (
                    'u64',
                    'Bytes',
                    'scale_info::217',
                    'scale_info::210',
                    (None, 'u128'),
                ),
                'OpeningCanceled': 'u64',
                'OpeningFilled': ('u64', 'scale_info::214', 'scale_info::84'),
                'RewardPaid': ('u64', 'AccountId', 'u128', 'scale_info::221'),
                'StakeDecreased': ('u64', 'u128'),
                'StakeIncreased': ('u64', 'u128'),
                'StakeSlashed': ('u64', 'u128', 'u128', (None, 'Bytes')),
                'StatusTextChanged': ('[u8; 32]', (None, 'Bytes')),
                'TerminatedLeader': ('u64', (None, 'u128'), (None, 'Bytes')),
                'TerminatedWorker': ('u64', (None, 'u128'), (None, 'Bytes')),
                'WorkerExited': 'u64',
                'WorkerRemarked': ('u64', 'Bytes'),
                'WorkerRewardAccountUpdated': ('u64', 'AccountId'),
                'WorkerRewardAmountUpdated': ('u64', (None, 'u128')),
                'WorkerRoleAccountUpdated': ('u64', 'AccountId'),
                'WorkerStartedLeaving': ('u64', (None, 'Bytes')),
                'WorkingGroupBudgetFunded': ('u64', 'u128', 'Bytes'),
            },
            'Council': {
                'AnnouncingPeriodStarted': 'u32',
                'BudgetBalanceSet': 'u128',
                'BudgetIncrementUpdated': 'u128',
                'BudgetRefill': 'u128',
                'BudgetRefillPlanned': 'u32',
                'CandidacyNoteSet': ('u64', 'Bytes'),
                'CandidacyStakeRelease': 'u64',
                'CandidacyWithdraw': 'u64',
                'CandidateRemarked': ('u64', 'Bytes'),
                'CouncilBudgetFunded': ('u64', 'u128', 'Bytes'),
                'CouncilorRemarked': ('u64', 'Bytes'),
                'CouncilorRewardUpdated': 'u128',
                'NewCandidate': ('u64', 'AccountId', 'AccountId', 'u128'),
                'NewCouncilElected': (['u64'], 'u32'),
                'NewCouncilNotElected': 'u32',
                'NotEnoughCandidates': 'u32',
                'RequestFunded': ('AccountId', 'u128'),
                'RewardPayment': ('u64', 'AccountId', 'u128', 'u128'),
                'VotingPeriodStarted': 'u32',
            },
            'DistributionWorkingGroup': {
                'ApplicationWithdrawn': 'u64',
                'AppliedOnOpening': ('scale_info::218', 'u64'),
                'BudgetSet': 'u128',
                'BudgetSpending': ('AccountId', 'u128', (None, 'Bytes')),
                'LeadRemarked': 'Bytes',
                'LeaderSet': 'u64',
                'LeaderUnset': None,
                'NewMissedRewardLevelReached': ('u64', (None, 'u128')),
                'OpeningAdded': (
                    'u64',
                    'Bytes',
                    'scale_info::217',
                    'scale_info::210',
                    (None, 'u128'),
                ),
                'OpeningCanceled': 'u64',
                'OpeningFilled': ('u64', 'scale_info::214', 'scale_info::84'),
                'RewardPaid': ('u64', 'AccountId', 'u128', 'scale_info::221'),
                'StakeDecreased': ('u64', 'u128'),
                'StakeIncreased': ('u64', 'u128'),
                'StakeSlashed': ('u64', 'u128', 'u128', (None, 'Bytes')),
                'StatusTextChanged': ('[u8; 32]', (None, 'Bytes')),
                'TerminatedLeader': ('u64', (None, 'u128'), (None, 'Bytes')),
                'TerminatedWorker': ('u64', (None, 'u128'), (None, 'Bytes')),
                'WorkerExited': 'u64',
                'WorkerRemarked': ('u64', 'Bytes'),
                'WorkerRewardAccountUpdated': ('u64', 'AccountId'),
                'WorkerRewardAmountUpdated': ('u64', (None, 'u128')),
                'WorkerRoleAccountUpdated': ('u64', 'AccountId'),
                'WorkerStartedLeaving': ('u64', (None, 'Bytes')),
                'WorkingGroupBudgetFunded': ('u64', 'u128', 'Bytes'),
            },
            'ElectionProviderMultiPhase': {
                'ElectionFinalized': {
                    'election_compute': (None, 'scale_info::33'),
                },
                'Rewarded': {'account': 'AccountId', 'value': 'u128'},
                'SignedPhaseStarted': {'round': 'u32'},
                'Slashed': {'account': 'AccountId', 'value': 'u128'},
                'SolutionStored': {
                    'election_compute': 'scale_info::33',
                    'prev_ejected': 'bool',
                },
                'UnsignedPhaseStarted': {'round': 'u32'},
            },
            'Forum': {
                'CategoryArchivalStatusUpdated': (
                    'u64',
                    'bool',
                    'scale_info::79',
                ),
                'CategoryCreated': ('u64', (None, 'u64'), 'Bytes', 'Bytes'),
                'CategoryDeleted': ('u64', 'scale_info::79'),
                'CategoryDescriptionUpdated': (
                    'u64',
                    '[u8; 32]',
                    'scale_info::79',
                ),
                'CategoryMembershipOfModeratorUpdated': ('u64', 'u64', 'bool'),
                'CategoryStickyThreadUpdate': (
                    'u64',
                    'scale_info::84',
                    'scale_info::79',
                ),
                'CategoryTitleUpdated': ('u64', '[u8; 32]', 'scale_info::79'),
                'PostAdded': ('u64', 'u64', 'u64', 'u64', 'Bytes', 'bool'),
                'PostDeleted': ('Bytes', 'u64', 'scale_info::81'),
                'PostModerated': (
                    'u64',
                    'Bytes',
                    'scale_info::79',
                    'u64',
                    'u64',
                ),
                'PostTextUpdated': ('u64', 'u64', 'u64', 'u64', 'Bytes'),
                'ThreadCreated': (
                    'u64',
                    'u64',
                    'u64',
                    'u64',
                    'Bytes',
                    'Bytes',
                ),
                'ThreadDeleted': ('u64', 'u64', 'u64', 'bool'),
                'ThreadMetadataUpdated': ('u64', 'u64', 'u64', 'Bytes'),
                'ThreadModerated': ('u64', 'Bytes', 'scale_info::79', 'u64'),
                'ThreadMoved': ('u64', 'u64', 'scale_info::79', 'u64'),
                'ThreadUpdated': ('u64', 'bool', 'scale_info::79', 'u64'),
            },
            'ForumWorkingGroup': {
                'ApplicationWithdrawn': 'u64',
                'AppliedOnOpening': ('scale_info::218', 'u64'),
                'BudgetSet': 'u128',
                'BudgetSpending': ('AccountId', 'u128', (None, 'Bytes')),
                'LeadRemarked': 'Bytes',
                'LeaderSet': 'u64',
                'LeaderUnset': None,
                'NewMissedRewardLevelReached': ('u64', (None, 'u128')),
                'OpeningAdded': (
                    'u64',
                    'Bytes',
                    'scale_info::217',
                    'scale_info::210',
                    (None, 'u128'),
                ),
                'OpeningCanceled': 'u64',
                'OpeningFilled': ('u64', 'scale_info::214', 'scale_info::84'),
                'RewardPaid': ('u64', 'AccountId', 'u128', 'scale_info::221'),
                'StakeDecreased': ('u64', 'u128'),
                'StakeIncreased': ('u64', 'u128'),
                'StakeSlashed': ('u64', 'u128', 'u128', (None, 'Bytes')),
                'StatusTextChanged': ('[u8; 32]', (None, 'Bytes')),
                'TerminatedLeader': ('u64', (None, 'u128'), (None, 'Bytes')),
                'TerminatedWorker': ('u64', (None, 'u128'), (None, 'Bytes')),
                'WorkerExited': 'u64',
                'WorkerRemarked': ('u64', 'Bytes'),
                'WorkerRewardAccountUpdated': ('u64', 'AccountId'),
                'WorkerRewardAmountUpdated': ('u64', (None, 'u128')),
                'WorkerRoleAccountUpdated': ('u64', 'AccountId'),
                'WorkerStartedLeaving': ('u64', (None, 'Bytes')),
                'WorkingGroupBudgetFunded': ('u64', 'u128', 'Bytes'),
            },
            'Grandpa': {
                'NewAuthorities': {'authority_set': [('[u8; 32]', 'u64')]},
                'Paused': None,
                'Resumed': None,
            },
            'ImOnline': {
                'AllGood': None,
                'HeartbeatReceived': {'authority_id': '[u8; 32]'},
                'SomeOffline': {'offline': [('AccountId', 'scale_info::51')]},
            },
            'JoystreamUtility': {
                'RuntimeUpgraded': 'Bytes',
                'Signaled': 'Bytes',
                'TokensBurned': ('AccountId', 'u128'),
                'UpdatedWorkingGroupBudget': (
                    'scale_info::96',
                    'u128',
                    'scale_info::97',
                ),
            },
            'Members': {
                'InitialInvitationBalanceUpdated': 'u128',
                'InitialInvitationCountUpdated': 'u32',
                'InvitesTransferred': ('u64', 'u64', 'u32'),
                'LeaderInvitationQuotaUpdated': 'u32',
                'MemberAccountsUpdated': (
                    'u64',
                    (None, 'AccountId'),
                    (None, 'AccountId'),
                ),
                'MemberCreated': ('u64', 'scale_info::72', 'u32'),
                'MemberInvited': ('u64', 'scale_info::71', 'u128'),
                'MemberProfileUpdated': (
                    'u64',
                    (None, 'Bytes'),
                    (None, 'Bytes'),
                ),
                'MemberRemarked': (
                    'u64',
                    'Bytes',
                    (None, ('AccountId', 'u128')),
                ),
                'MemberVerificationStatusUpdated': ('u64', 'bool', 'u64'),
                'MembershipBought': ('u64', 'scale_info::68', 'u32'),
                'MembershipGifted': ('u64', 'scale_info::73'),
                'MembershipPriceUpdated': 'u128',
                'ReferralCutUpdated': 'u8',
                'StakingAccountAdded': ('AccountId', 'u64'),
                'StakingAccountConfirmed': ('AccountId', 'u64'),
                'StakingAccountRemoved': ('AccountId', 'u64'),
            },
            'MembershipWorkingGroup': {
                'ApplicationWithdrawn': 'u64',
                'AppliedOnOpening': ('scale_info::218', 'u64'),
                'BudgetSet': 'u128',
                'BudgetSpending': ('AccountId', 'u128', (None, 'Bytes')),
                'LeadRemarked': 'Bytes',
                'LeaderSet': 'u64',
                'LeaderUnset': None,
                'NewMissedRewardLevelReached': ('u64', (None, 'u128')),
                'OpeningAdded': (
                    'u64',
                    'Bytes',
                    'scale_info::217',
                    'scale_info::210',
                    (None, 'u128'),
                ),
                'OpeningCanceled': 'u64',
                'OpeningFilled': ('u64', 'scale_info::214', 'scale_info::84'),
                'RewardPaid': ('u64', 'AccountId', 'u128', 'scale_info::221'),
                'StakeDecreased': ('u64', 'u128'),
                'StakeIncreased': ('u64', 'u128'),
                'StakeSlashed': ('u64', 'u128', 'u128', (None, 'Bytes')),
                'StatusTextChanged': ('[u8; 32]', (None, 'Bytes')),
                'TerminatedLeader': ('u64', (None, 'u128'), (None, 'Bytes')),
                'TerminatedWorker': ('u64', (None, 'u128'), (None, 'Bytes')),
                'WorkerExited': 'u64',
                'WorkerRemarked': ('u64', 'Bytes'),
                'WorkerRewardAccountUpdated': ('u64', 'AccountId'),
                'WorkerRewardAmountUpdated': ('u64', (None, 'u128')),
                'WorkerRoleAccountUpdated': ('u64', 'AccountId'),
                'WorkerStartedLeaving': ('u64', (None, 'Bytes')),
                'WorkingGroupBudgetFunded': ('u64', 'u128', 'Bytes'),
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::60',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::60',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::28',
                    'timepoint': 'scale_info::60',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'Offences': {'Offence': {'kind': '[u8; 16]', 'timeslot': 'Bytes'}},
            'OperationsWorkingGroupAlpha': {
                'ApplicationWithdrawn': 'u64',
                'AppliedOnOpening': ('scale_info::218', 'u64'),
                'BudgetSet': 'u128',
                'BudgetSpending': ('AccountId', 'u128', (None, 'Bytes')),
                'LeadRemarked': 'Bytes',
                'LeaderSet': 'u64',
                'LeaderUnset': None,
                'NewMissedRewardLevelReached': ('u64', (None, 'u128')),
                'OpeningAdded': (
                    'u64',
                    'Bytes',
                    'scale_info::217',
                    'scale_info::210',
                    (None, 'u128'),
                ),
                'OpeningCanceled': 'u64',
                'OpeningFilled': ('u64', 'scale_info::214', 'scale_info::84'),
                'RewardPaid': ('u64', 'AccountId', 'u128', 'scale_info::221'),
                'StakeDecreased': ('u64', 'u128'),
                'StakeIncreased': ('u64', 'u128'),
                'StakeSlashed': ('u64', 'u128', 'u128', (None, 'Bytes')),
                'StatusTextChanged': ('[u8; 32]', (None, 'Bytes')),
                'TerminatedLeader': ('u64', (None, 'u128'), (None, 'Bytes')),
                'TerminatedWorker': ('u64', (None, 'u128'), (None, 'Bytes')),
                'WorkerExited': 'u64',
                'WorkerRemarked': ('u64', 'Bytes'),
                'WorkerRewardAccountUpdated': ('u64', 'AccountId'),
                'WorkerRewardAmountUpdated': ('u64', (None, 'u128')),
                'WorkerRoleAccountUpdated': ('u64', 'AccountId'),
                'WorkerStartedLeaving': ('u64', (None, 'Bytes')),
                'WorkingGroupBudgetFunded': ('u64', 'u128', 'Bytes'),
            },
            'OperationsWorkingGroupBeta': {
                'ApplicationWithdrawn': 'u64',
                'AppliedOnOpening': ('scale_info::218', 'u64'),
                'BudgetSet': 'u128',
                'BudgetSpending': ('AccountId', 'u128', (None, 'Bytes')),
                'LeadRemarked': 'Bytes',
                'LeaderSet': 'u64',
                'LeaderUnset': None,
                'NewMissedRewardLevelReached': ('u64', (None, 'u128')),
                'OpeningAdded': (
                    'u64',
                    'Bytes',
                    'scale_info::217',
                    'scale_info::210',
                    (None, 'u128'),
                ),
                'OpeningCanceled': 'u64',
                'OpeningFilled': ('u64', 'scale_info::214', 'scale_info::84'),
                'RewardPaid': ('u64', 'AccountId', 'u128', 'scale_info::221'),
                'StakeDecreased': ('u64', 'u128'),
                'StakeIncreased': ('u64', 'u128'),
                'StakeSlashed': ('u64', 'u128', 'u128', (None, 'Bytes')),
                'StatusTextChanged': ('[u8; 32]', (None, 'Bytes')),
                'TerminatedLeader': ('u64', (None, 'u128'), (None, 'Bytes')),
                'TerminatedWorker': ('u64', (None, 'u128'), (None, 'Bytes')),
                'WorkerExited': 'u64',
                'WorkerRemarked': ('u64', 'Bytes'),
                'WorkerRewardAccountUpdated': ('u64', 'AccountId'),
                'WorkerRewardAmountUpdated': ('u64', (None, 'u128')),
                'WorkerRoleAccountUpdated': ('u64', 'AccountId'),
                'WorkerStartedLeaving': ('u64', (None, 'Bytes')),
                'WorkingGroupBudgetFunded': ('u64', 'u128', 'Bytes'),
            },
            'OperationsWorkingGroupGamma': {
                'ApplicationWithdrawn': 'u64',
                'AppliedOnOpening': ('scale_info::218', 'u64'),
                'BudgetSet': 'u128',
                'BudgetSpending': ('AccountId', 'u128', (None, 'Bytes')),
                'LeadRemarked': 'Bytes',
                'LeaderSet': 'u64',
                'LeaderUnset': None,
                'NewMissedRewardLevelReached': ('u64', (None, 'u128')),
                'OpeningAdded': (
                    'u64',
                    'Bytes',
                    'scale_info::217',
                    'scale_info::210',
                    (None, 'u128'),
                ),
                'OpeningCanceled': 'u64',
                'OpeningFilled': ('u64', 'scale_info::214', 'scale_info::84'),
                'RewardPaid': ('u64', 'AccountId', 'u128', 'scale_info::221'),
                'StakeDecreased': ('u64', 'u128'),
                'StakeIncreased': ('u64', 'u128'),
                'StakeSlashed': ('u64', 'u128', 'u128', (None, 'Bytes')),
                'StatusTextChanged': ('[u8; 32]', (None, 'Bytes')),
                'TerminatedLeader': ('u64', (None, 'u128'), (None, 'Bytes')),
                'TerminatedWorker': ('u64', (None, 'u128'), (None, 'Bytes')),
                'WorkerExited': 'u64',
                'WorkerRemarked': ('u64', 'Bytes'),
                'WorkerRewardAccountUpdated': ('u64', 'AccountId'),
                'WorkerRewardAmountUpdated': ('u64', (None, 'u128')),
                'WorkerRoleAccountUpdated': ('u64', 'AccountId'),
                'WorkerStartedLeaving': ('u64', (None, 'Bytes')),
                'WorkingGroupBudgetFunded': ('u64', 'u128', 'Bytes'),
            },
            'ProjectToken': {
                'AccountDustedBy': (
                    'u64',
                    'u64',
                    'AccountId',
                    'scale_info::171',
                ),
                'MemberJoinedWhitelist': ('u64', 'u64', 'scale_info::171'),
                'PatronageCreditClaimed': ('u64', 'u128', 'u64'),
                'PatronageRateDecreasedTo': ('u64', 'u64'),
                'RevenueSplitFinalized': ('u64', 'AccountId', 'u128'),
                'RevenueSplitIssued': ('u64', 'u32', 'u32', 'u128'),
                'RevenueSplitLeft': ('u64', 'u64', 'u128'),
                'TokenAmountTransferred': (
                    'u64',
                    'u64',
                    'scale_info::191',
                    'Bytes',
                ),
                'TokenAmountTransferredByIssuer': (
                    'u64',
                    'u64',
                    'scale_info::191',
                    'Bytes',
                ),
                'TokenDeissued': 'u64',
                'TokenIssued': ('u64', 'scale_info::172'),
                'TokenSaleFinalized': ('u64', 'u32', 'u128', 'u128'),
                'TokenSaleInitialized': (
                    'u64',
                    'u32',
                    'scale_info::194',
                    (None, 'Bytes'),
                ),
                'TokensBurned': ('u64', 'u64', 'u128'),
                'TokensPurchasedOnSale': ('u64', 'u32', 'u128', 'u64'),
                'TransferPolicyChangedToPermissionless': 'u64',
                'UpcomingTokenSaleUpdated': (
                    'u64',
                    'u32',
                    (None, 'u32'),
                    (None, 'u32'),
                ),
                'UserParticipatedInSplit': (
                    'u64',
                    'u64',
                    'u128',
                    'u128',
                    'u32',
                ),
            },
            'ProposalsCodex': {
                'ProposalCreated': (
                    'u32',
                    'scale_info::205',
                    'scale_info::206',
                    'u64',
                ),
            },
            'ProposalsDiscussion': {
                'PostCreated': ('u64', 'u64', 'u64', 'Bytes', 'bool'),
                'PostDeleted': ('u64', 'u64', 'u64', 'bool'),
                'PostUpdated': ('u64', 'u64', 'u64', 'Bytes'),
                'ThreadCreated': ('u64', 'u64'),
                'ThreadModeChanged': ('u64', 'scale_info::203', 'u64'),
            },
            'ProposalsEngine': {
                'ProposalCancelled': ('u64', 'u32'),
                'ProposalDecisionMade': ('u32', 'scale_info::198'),
                'ProposalExecuted': ('u32', 'scale_info::200'),
                'ProposalStatusUpdated': ('u32', 'scale_info::197'),
                'ProposerRemarked': ('u64', 'u32', 'Bytes'),
                'Voted': ('u64', 'u32', 'scale_info::201', 'Bytes'),
            },
            'Referendum': {
                'AccountOptedOutOfVoting': 'AccountId',
                'ReferendumFinished': ['scale_info::66'],
                'ReferendumStarted': ('u32', 'u32'),
                'ReferendumStartedForcefully': ('u32', 'u32'),
                'RevealingStageStarted': 'u32',
                'StakeReleased': 'AccountId',
                'VoteCast': ('AccountId', '[u8; 32]', 'u128'),
                'VoteRevealed': ('AccountId', 'u64', 'Bytes'),
            },
            'Session': {'NewSession': {'session_index': 'u32'}},
            'Staking': {
                'Bonded': ('AccountId', 'u128'),
                'Chilled': 'AccountId',
                'EraPaid': ('u32', 'u128', 'u128'),
                'Kicked': ('AccountId', 'AccountId'),
                'OldSlashingReportDiscarded': 'u32',
                'PayoutStarted': ('u32', 'AccountId'),
                'Rewarded': ('AccountId', 'u128'),
                'Slashed': ('AccountId', 'u128'),
                'StakersElected': None,
                'StakingElectionFailed': None,
                'Unbonded': ('AccountId', 'u128'),
                'ValidatorPrefsSet': ('AccountId', 'scale_info::37'),
                'Withdrawn': ('AccountId', 'u128'),
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
            'Utility': {
                'BatchCompleted': None,
                'BatchCompletedWithErrors': None,
                'BatchInterrupted': {
                    'error': 'scale_info::22',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::28'},
                'ItemCompleted': None,
                'ItemFailed': {'error': 'scale_info::22'},
            },
            None: None,
            'Storage': {
                'DataObjectPerMegabyteFeeUpdated': 'u128',
                'DataObjectStateBloatBondValueUpdated': 'u128',
                'DataObjectsDeleted': (
                    'AccountId',
                    'scale_info::159',
                    'scale_info::84',
                ),
                'DataObjectsMoved': (
                    'scale_info::159',
                    'scale_info::159',
                    'scale_info::84',
                ),
                'DataObjectsUpdated': (
                    'scale_info::158',
                    'scale_info::84',
                    'scale_info::84',
                ),
                'DataObjectsUploaded': (
                    'scale_info::84',
                    'scale_info::158',
                    'u128',
                ),
                'DistributionBucketCreated': (
                    'u64',
                    'bool',
                    'scale_info::131',
                ),
                'DistributionBucketDeleted': {
                    'distribution_bucket_family_id': 'u64',
                    'distribution_bucket_index': 'u64',
                },
                'DistributionBucketFamilyCreated': 'u64',
                'DistributionBucketFamilyDeleted': 'u64',
                'DistributionBucketFamilyMetadataSet': ('u64', 'Bytes'),
                'DistributionBucketInvitationAccepted': (
                    'u64',
                    'scale_info::131',
                ),
                'DistributionBucketInvitationCancelled': (
                    'scale_info::131',
                    'u64',
                ),
                'DistributionBucketMetadataSet': (
                    'u64',
                    'scale_info::131',
                    'Bytes',
                ),
                'DistributionBucketModeUpdated': ('scale_info::131', 'bool'),
                'DistributionBucketOperatorInvited': (
                    'scale_info::131',
                    'u64',
                ),
                'DistributionBucketOperatorRemoved': (
                    'scale_info::131',
                    'u64',
                ),
                'DistributionBucketStatusUpdated': ('scale_info::131', 'bool'),
                'DistributionBucketsPerBagLimitUpdated': 'u32',
                'DistributionBucketsUpdatedForBag': (
                    'scale_info::159',
                    'u64',
                    'scale_info::84',
                    'scale_info::84',
                ),
                'DistributionOperatorRemarked': (
                    'u64',
                    'scale_info::131',
                    'Bytes',
                ),
                'DynamicBagCreated': ('scale_info::162', 'scale_info::84'),
                'DynamicBagDeleted': {'Channel': 'u64', 'Member': 'u64'},
                'FamiliesInDynamicBagCreationPolicyUpdated': (
                    'scale_info::166',
                    'scale_info::167',
                ),
                'NumberOfStorageBucketsInDynamicBagCreationPolicyUpdated': (
                    'scale_info::166',
                    'u32',
                ),
                'PendingDataObjectsAccepted': (
                    'u64',
                    'u64',
                    'scale_info::159',
                    'scale_info::84',
                ),
                'StorageBucketCreated': ('u64', (None, 'u64'), 'bool', 'u64', 'u64'),
                'StorageBucketDeleted': 'u64',
                'StorageBucketInvitationAccepted': ('u64', 'u64', 'AccountId'),
                'StorageBucketInvitationCancelled': 'u64',
                'StorageBucketOperatorInvited': ('u64', 'u64'),
                'StorageBucketOperatorRemoved': 'u64',
                'StorageBucketStatusUpdated': ('u64', 'bool'),
                'StorageBucketVoucherLimitsSet': ('u64', 'u64', 'u64'),
                'StorageBucketsPerBagLimitUpdated': 'u32',
                'StorageBucketsUpdatedForBag': (
                    'scale_info::159',
                    'scale_info::84',
                    'scale_info::84',
                ),
                'StorageBucketsVoucherMaxLimitsUpdated': ('u64', 'u64'),
                'StorageOperatorMetadataSet': ('u64', 'u64', 'Bytes'),
                'StorageOperatorRemarked': ('u64', 'u64', 'Bytes'),
                'UpdateBlacklist': ('scale_info::163', 'scale_info::163'),
                'UploadingBlockStatusUpdated': 'bool',
                'VoucherChanged': ('u64', 'scale_info::165'),
            },
            'StorageWorkingGroup': {
                'ApplicationWithdrawn': 'u64',
                'AppliedOnOpening': ('scale_info::218', 'u64'),
                'BudgetSet': 'u128',
                'BudgetSpending': ('AccountId', 'u128', (None, 'Bytes')),
                'LeadRemarked': 'Bytes',
                'LeaderSet': 'u64',
                'LeaderUnset': None,
                'NewMissedRewardLevelReached': ('u64', (None, 'u128')),
                'OpeningAdded': (
                    'u64',
                    'Bytes',
                    'scale_info::217',
                    'scale_info::210',
                    (None, 'u128'),
                ),
                'OpeningCanceled': 'u64',
                'OpeningFilled': ('u64', 'scale_info::214', 'scale_info::84'),
                'RewardPaid': ('u64', 'AccountId', 'u128', 'scale_info::221'),
                'StakeDecreased': ('u64', 'u128'),
                'StakeIncreased': ('u64', 'u128'),
                'StakeSlashed': ('u64', 'u128', 'u128', (None, 'Bytes')),
                'StatusTextChanged': ('[u8; 32]', (None, 'Bytes')),
                'TerminatedLeader': ('u64', (None, 'u128'), (None, 'Bytes')),
                'TerminatedWorker': ('u64', (None, 'u128'), (None, 'Bytes')),
                'WorkerExited': 'u64',
                'WorkerRemarked': ('u64', 'Bytes'),
                'WorkerRewardAccountUpdated': ('u64', 'AccountId'),
                'WorkerRewardAmountUpdated': ('u64', (None, 'u128')),
                'WorkerRoleAccountUpdated': ('u64', 'AccountId'),
                'WorkerStartedLeaving': ('u64', (None, 'Bytes')),
                'WorkingGroupBudgetFunded': ('u64', 'u128', 'Bytes'),
            },
            'Vesting': {
                'VestingCompleted': {'account': 'AccountId'},
                'VestingUpdated': {'account': 'AccountId', 'unvested': 'u128'},
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
    'base_block': 5919668000,
    'max_block': 2000000000000,
    'per_class': {
        'mandatory': {
            'base_extrinsic': 106628000,
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': 106628000,
            'max_extrinsic': 1299893372000,
            'max_total': 1500000000000,
            'reserved': 0,
        },
        'operational': {
            'base_extrinsic': 106628000,
            'max_extrinsic': 1799893372000,
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
{'read': 8997000, 'write': 54966000}
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
126
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
        ('0xed99c5acb25eedf5', 3),
        ('0xcbca25e39f142387', 2),
        ('0x687ad44ad37f03c2', 1),
        ('0xbc9d89904f5b923f', 1),
        ('0x37c8bb1350a9a2a8', 1),
        ('0xab3c0572291feb8b', 1),
    ],
    'authoring_version': 12,
    'impl_name': 'joystream-node',
    'impl_version': 0,
    'spec_name': 'joystream-node',
    'spec_version': 2001,
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