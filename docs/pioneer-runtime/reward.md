
# Reward

---------
## Calls

---------
### add_set_reward_origin
Allow account to set rewards

The dispatch origin for this call must be _Signed_. This extrinsic only works if the
origin got admin privilege.
- `account`: the account which will be allowed to set rewards.

Emits `SetRewardOriginAdded` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Reward', 'add_set_reward_origin', {'account': 'AccountId'}
)
```

---------
### cancel_campaign
Cancel token-based campaign  

The dispatch origin for this call must be _Signed_. This extrinsic only works if the
origin got admin privilege.
- `campaign_id`: the ID of the campaign for which the rewards will be set.

Emits `RewardCampaignCanceled` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `CampaignId` | 

#### Python
```python
call = substrate.compose_call(
    'Reward', 'cancel_campaign', {'id': 'u32'}
)
```

---------
### cancel_nft_campaign
Cancel NFT-based campaign  

The dispatch origin for this call must be _Signed_. This extrinsic only works if the
origin got admin privilege.
- `campaign_id`: the ID of the campaign for which the rewards will be set.
- `left_nfts`: the size of the NFT reward pool.

Emits `RewardCampaignCanceled` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `CampaignId` | 
| left_nfts | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Reward', 'cancel_nft_campaign', {'id': 'u32', 'left_nfts': 'u64'}
)
```

---------
### claim_nft_reward
Claim reward set without merkle root for NFT-based campaign

The dispatch origin for this call must be _Signed_. This extrinsic only works if the
account is rewarded for the campaign.
- `campaign_id`: the ID of the campaign for which the account is claiming reward.
- `amount`: the amount of NFTs that the account is going to claim

Emits `RewardClaimed` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `CampaignId` | 
| amount | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Reward', 'claim_nft_reward', {'amount': 'u64', 'id': 'u32'}
)
```

---------
### claim_nft_reward_root
Claim reward set with merkle root for NFT-based campaign

The dispatch origin for this call must be _Signed_. This extrinsic only works if the
account is rewarded for the campaign.
- `campaign_id`: the ID of the campaign for which the account is claiming reward.
- `tokens`: the list of NFTs which the account will claim (required for  merkle-proof
  calculation).
- `leaf_nodes`: list of the merkle tree nodes required for  merkle-proof calculation.

Emits `RewardClaimed` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `CampaignId` | 
| reward_tokens | `Vec<(ClassId, TokenId)>` | 
| leaf_nodes | `Vec<Hash>` | 

#### Python
```python
call = substrate.compose_call(
    'Reward', 'claim_nft_reward_root', {
    'id': 'u32',
    'leaf_nodes': ['scale_info::9'],
    'reward_tokens': [('u32', 'u64')],
}
)
```

---------
### claim_reward
Claim reward set without merkle root for token-based campaign

The dispatch origin for this call must be _Signed_. This extrinsic only works if the
account is rewarded for the campaign.
- `campaign_id`: the ID of the campaign for which the account is claiming reward.

Emits `RewardClaimed` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `CampaignId` | 

#### Python
```python
call = substrate.compose_call(
    'Reward', 'claim_reward', {'id': 'u32'}
)
```

---------
### claim_reward_root
Claim reward set with merkle root for token-based campaign

The dispatch origin for this call must be _Signed_. This extrinsic only works if the
account is rewarded for the campaign.
- `campaign_id`: the ID of the campaign for which the account is claiming reward.
- `balance`: the amount of tokens which the account will claim (required for
  merkle-proof calculation).
- `leaf_nodes`: list of the merkle tree nodes required for merkle-proof calculation.

Emits `RewardClaimed` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `CampaignId` | 
| balance | `BalanceOf<T>` | 
| leaf_nodes | `Vec<Hash>` | 

#### Python
```python
call = substrate.compose_call(
    'Reward', 'claim_reward_root', {
    'balance': 'u128',
    'id': 'u32',
    'leaf_nodes': ['scale_info::9'],
}
)
```

---------
### close_campaign
Close token-based campaign  

The dispatch origin for this call must be _Signed_. This extrinsic only works for the
campign creator.
- `campaign_id`: the ID of the campaign for which the rewards will be set.
- `merkle_roots_quanity`: the amount of merkle roots that were used for setting rewards.

Emits `RewardCampaignClosed` and/or `RewardCampaignRootClosed`  if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `CampaignId` | 
| merkle_roots_quantity | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Reward', 'close_campaign', {
    'id': 'u32',
    'merkle_roots_quantity': 'u64',
}
)
```

---------
### close_nft_campaign
Close NFT-based campaign  

The dispatch origin for this call must be _Signed_. This extrinsic only works for the
campign creator.
- `campaign_id`: the ID of the campaign for which the rewards will be set.
- `left_nfts`: the amount of unclaimed NFTs in the reward pool.

Emits `RewardCampaignClosed` and/or `RewardCampaignRootClosed`  if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `CampaignId` | 
| left_nfts | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Reward', 'close_nft_campaign', {'id': 'u32', 'left_nfts': 'u64'}
)
```

---------
### create_campaign
Create a new token-based campaign from parameters

The dispatch origin for this call must be _Signed_.
- `creator`: the account for which the campaign is created.
- `reward`: the total balance of the currency provided as reward.
- `end`: the end block at which users can participate.
- `cooling_off_duration`: the duriation (in blocks) of the period during which accounts
  can claim rewards.
- `properties`: information relevant for the campaign.
- `currency_id`: specify the type of currency which for the reward pool.

Emits `NewRewardCampaignCreated` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| creator | `T::AccountId` | 
| reward | `BalanceOf<T>` | 
| end | `T::BlockNumber` | 
| cooling_off_duration | `T::BlockNumber` | 
| properties | `Vec<u8>` | 
| currency_id | `FungibleTokenId` | 

#### Python
```python
call = substrate.compose_call(
    'Reward', 'create_campaign', {
    'cooling_off_duration': 'u32',
    'creator': 'AccountId',
    'currency_id': {
        'DEXShare': ('u64', 'u64'),
        'FungibleToken': 'u64',
        'MiningResource': 'u64',
        'NativeToken': 'u64',
        'Stable': 'u64',
    },
    'end': 'u32',
    'properties': 'Bytes',
    'reward': 'u128',
}
)
```

---------
### create_nft_campaign
Create a new NFT-based campaign from parameters

The dispatch origin for this call must be _Signed_.
- `creator`: the account for which the campaign is created.
- `reward`: the pool of NFTs that will be provided as reward.
- `end`: the end block at which users can participate.
- `cooling_off_duration`: the duriation (in blocks) of the period during which accounts
  can claim rewards.
- `properties`: information relevant for the campaign.

Emits `NewRewardCampaignCreated` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| creator | `T::AccountId` | 
| reward | `Vec<(ClassId, TokenId)>` | 
| end | `T::BlockNumber` | 
| cooling_off_duration | `T::BlockNumber` | 
| properties | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Reward', 'create_nft_campaign', {
    'cooling_off_duration': 'u32',
    'creator': 'AccountId',
    'end': 'u32',
    'properties': 'Bytes',
    'reward': [('u32', 'u64')],
}
)
```

---------
### remove_set_reward_origin
Remove permission  to set rewards for a given account

The dispatch origin for this call must be _Signed_. This extrinsic only works if the
origin got admin privilege.
- `account`: the account which won&\#x27;;t be allowed to set rewards.

Emits `SetRewardOriginRemoved` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Reward', 'remove_set_reward_origin', {'account': 'AccountId'}
)
```

---------
### set_nft_reward
Set reward for NFT-based campaign without using merkle root

The dispatch origin for this call must be _Signed_. This extrinsic only works if the
origin got permission to set rewards.
- `campaign_id`: the ID of the campaign for which the rewards will be set.
- `rewards`: vector of account IDs and their number of tokens that they will receive
  pairs.
- `total_nfts_amount`: the total number of NFTs that will be rewrad.

Emits `SetReward` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `CampaignId` | 
| rewards | `Vec<(T::AccountId, u64)>` | 
| total_nfts_amount | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Reward', 'set_nft_reward', {
    'id': 'u32',
    'rewards': [('AccountId', 'u64')],
    'total_nfts_amount': 'u64',
}
)
```

---------
### set_nft_reward_root
Set reward for NFT-based campaign using merkle root

The dispatch origin for this call must be _Signed_. This extrinsic only works if the
origin got permission to set rewards.
- `campaign_id`: the ID of the campaign for which the rewards will be set.
- `merkle_root`: the merkle root that will be used when claiming rewards.

Emits `SetReward` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `CampaignId` | 
| merkle_root | `Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Reward', 'set_nft_reward_root', {
    'id': 'u32',
    'merkle_root': 'scale_info::9',
}
)
```

---------
### set_reward
Set reward for token-based campaign without using merkle root

The dispatch origin for this call must be _Signed_. This extrinsic only works if the
origin got permission to set rewards.
- `campaign_id`: the ID of the campaign for which the rewards will be set.
- `rewards`: vector of account IDs and their&\#x27;s reward balances pairs.

Emits `SetReward` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `CampaignId` | 
| rewards | `Vec<(T::AccountId, BalanceOf<T>)>` | 

#### Python
```python
call = substrate.compose_call(
    'Reward', 'set_reward', {
    'id': 'u32',
    'rewards': [('AccountId', 'u128')],
}
)
```

---------
### set_reward_root
Set reward for token-based campaign using merkle root

The dispatch origin for this call must be _Signed_. This extrinsic only works if the
origin got permission to set rewards.
- `campaign_id`: the ID of the campaign for which the rewards will be set.
- `total_amount`: the amount of tokens which will be rewarded.
- `merkle_root`: the merkle root that will be used when claiming rewards.

Emits `SetReward` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `CampaignId` | 
| total_amount | `BalanceOf<T>` | 
| merkle_root | `Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Reward', 'set_reward_root', {
    'id': 'u32',
    'merkle_root': 'scale_info::9',
    'total_amount': 'u128',
}
)
```

---------
## Events

---------
### NewRewardCampaignCreated
New campaign created [campaign_id, account]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CampaignId` | ```u32```
| None | `T::AccountId` | ```AccountId```

---------
### NftRewardClaimed
Reward claimed [campaign_id, account, assets]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CampaignId` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `Vec<(ClassId, TokenId)>` | ```[('u32', 'u64')]```

---------
### RewardCampaignCanceled
Reward campaign canceled [campaign_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CampaignId` | ```u32```

---------
### RewardCampaignClosed
Reward campaign closed [campaign_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CampaignId` | ```u32```

---------
### RewardCampaignEnded
Reward campaign ended [campaign_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CampaignId` | ```u32```

---------
### RewardCampaignRootClosed
Reward campaign  root closed [campaign_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CampaignId` | ```u32```

---------
### RewardClaimed
Reward claimed [campaign_id, account, balance]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CampaignId` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### SetNftReward
Set reward [campaign_id, rewards_list]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CampaignId` | ```u32```
| None | `Vec<(T::AccountId, Vec<(ClassId, TokenId)>)>` | ```[('AccountId', [('u32', 'u64')])]```

---------
### SetNftRewardRoot
Set NFT rewards using merkle root[campaign_id, hash]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CampaignId` | ```u32```
| None | `Hash` | ```scale_info::9```

---------
### SetReward
Set reward [campaign_id, rewards_list]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CampaignId` | ```u32```
| None | `Vec<(T::AccountId, BalanceOf<T>)>` | ```[('AccountId', 'u128')]```

---------
### SetRewardOriginAdded
Set reward origin added [account]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### SetRewardOriginRemoved
Set reward origin removed [account]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### SetRewardRoot
Set reward using merkle root [campaign_id, balance, hash]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CampaignId` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `Hash` | ```scale_info::9```

---------
## Storage functions

---------
### CampaignClaimedAccounts
 List of claimed account for each mekrle tree-based campaign

#### Python
```python
result = substrate.query(
    'Reward', 'CampaignClaimedAccounts', ['u32']
)
```

#### Return value
```python
['AccountId']
```
---------
### CampaignMerkleRoots
 List of merkle roots for each campaign

#### Python
```python
result = substrate.query(
    'Reward', 'CampaignMerkleRoots', ['u32']
)
```

#### Return value
```python
['scale_info::9']
```
---------
### Campaigns
 Info of campaign.

#### Python
```python
result = substrate.query(
    'Reward', 'Campaigns', ['u32']
)
```

#### Return value
```python
{
    'cap': {
        'FungibleTokens': (
            {
                'DEXShare': ('u64', 'u64'),
                'FungibleToken': 'u64',
                'MiningResource': 'u64',
                'NativeToken': 'u64',
                'Stable': 'u64',
            },
            'u128',
        ),
        'NftAssets': [('u32', 'u64')],
    },
    'claimed': {
        'FungibleTokens': (
            {
                'DEXShare': ('u64', 'u64'),
                'FungibleToken': 'u64',
                'MiningResource': 'u64',
                'NativeToken': 'u64',
                'Stable': 'u64',
            },
            'u128',
        ),
        'NftAssets': [('u32', 'u64')],
    },
    'cooling_off_duration': 'u32',
    'creator': 'AccountId',
    'end': 'u32',
    'properties': 'Bytes',
    'reward': {
        'FungibleTokens': (
            {
                'DEXShare': ('u64', 'u64'),
                'FungibleToken': 'u64',
                'MiningResource': 'u64',
                'NativeToken': 'u64',
                'Stable': 'u64',
            },
            'u128',
        ),
        'NftAssets': [('u32', 'u64')],
    },
    'trie_index': 'u32',
}
```
---------
### NextCampaignId
 Tracker for the next available campaign index

#### Python
```python
result = substrate.query(
    'Reward', 'NextCampaignId', []
)
```

#### Return value
```python
'u32'
```
---------
### NextTrieIndex
 Tracker for the next available trie index

#### Python
```python
result = substrate.query(
    'Reward', 'NextTrieIndex', []
)
```

#### Return value
```python
'u32'
```
---------
### SetRewardOrigins
 Set reward origins

#### Python
```python
result = substrate.query(
    'Reward', 'SetRewardOrigins', ['AccountId']
)
```

#### Return value
```python
()
```
---------
## Constants

---------
### CampaignDeposit
 The amount to be held on deposit by the creator when creating new campaign.
#### Value
```python
1000000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Reward', 'CampaignDeposit')
```
---------
### MaxLeafNodes
 The maximum amount of leaf nodes that could be passed when claiming reward
#### Value
```python
30
```
#### Python
```python
constant = substrate.get_constant('Reward', 'MaxLeafNodes')
```
---------
### MaxSetRewardsListLength
 The max number of accounts that could be rewarded per extrinsic
#### Value
```python
200
```
#### Python
```python
constant = substrate.get_constant('Reward', 'MaxSetRewardsListLength')
```
---------
### MinimumCampaignCoolingOffPeriod
 The minimum amount of blocks during which campaign rewards can be claimed.
#### Value
```python
50400
```
#### Python
```python
constant = substrate.get_constant('Reward', 'MinimumCampaignCoolingOffPeriod')
```
---------
### MinimumCampaignDuration
 The minimum amount of blocks during which campaign rewards can be claimed.
#### Value
```python
150
```
#### Python
```python
constant = substrate.get_constant('Reward', 'MinimumCampaignDuration')
```
---------
### MinimumRewardPool
 The minimum reward pool for a campaign
#### Value
```python
1000000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Reward', 'MinimumRewardPool')
```
---------
### MiningCurrencyId
 The currency id of BIT
#### Value
```python
{'MiningResource': 0}
```
#### Python
```python
constant = substrate.get_constant('Reward', 'MiningCurrencyId')
```
---------
### PalletId
 `PalletId` for the reward campaign pallet. An appropriate value could be
 `PalletId(*b&quot;b/reward&quot;)`
#### Value
```python
'0x6269742f74727379'
```
#### Python
```python
constant = substrate.get_constant('Reward', 'PalletId')
```
---------
## Errors

---------
### AccountAlreadyRewarded
The account is already rewarded for this campaign

---------
### ArithmeticOverflow
Arthimetic operation overflow

---------
### CampaignDurationBelowMinimum
Campaign duration is below minimum

---------
### CampaignEnded
Campaign period for setting rewards is over

---------
### CampaignExpired
Campaign already expired

---------
### CampaignIsNotFound
Campaign has ended or not valid

---------
### CampaignStillActive
Campaign is still active

---------
### CoolingOffPeriodBelowMinimum
Campaign cooling-off duration is below minimum

---------
### InvalidCampaignType
Invalid campaign type

---------
### InvalidMerkleRootsQuantity
Invalid merkle roots quantity

---------
### InvalidNftQuantity
Invalid left NFT quantity

---------
### InvalidRewardAccount
Invalid reward account

---------
### InvalidRewardLeafAmount
Reward leaf amount is larger then maximum

---------
### InvalidRewardType
Invalid reward type

---------
### InvalidSetRewardOrigin
Invalid set reward origin

---------
### InvalidTotalNftRewardAmountParameter
Invalid total NFT rewards amount parameter

---------
### MerkleRootNotRelatedToCampaign
Merkle root is not related to a campaign

---------
### NftTokenCannotBeRewarded
Nft token reward is already assigned

---------
### NoMerkleRootsFound
No merkle roots found

---------
### NoPermissionToUseNftInRewardPool
Cannot use an NFT token for a reward pool

---------
### NoRewardFound
No reward found in this account

---------
### NotCampaignCreator
Not campaign creator

---------
### RewardAlreadySet
Reward is already set

---------
### RewardExceedCap
Reward exceed the cap reward

---------
### RewardPoolBelowMinimum
Campaign reward pool is below the set minimum

---------
### RewardsListSizeAboveMaximum
Rewards list size is above maximum permited size

---------
### SetRewardOriginAlreadyAdded
Reward origin already added

---------
### SetRewardOriginDoesNotExist
Reward origin does not exist

---------