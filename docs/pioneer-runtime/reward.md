
# Reward

---------
## Calls

---------
### add_set_reward_origin
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
### claim_reward
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
### close_campaign
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `CampaignId` | 

#### Python
```python
call = substrate.compose_call(
    'Reward', 'close_campaign', {'id': 'u32'}
)
```

---------
### close_nft_campaign
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
### set_reward
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
Reward claimed [campaign_id, account, asset]
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
## Storage functions

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
100000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Reward', 'CampaignDeposit')
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
Artimetic operation overflow

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
### InvalidNftQuantity
Invalid left NFT quantity

---------
### InvalidRewardAccount
Invalid reward account

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
### NftTokenCannotBeRewarded
Nft token reward is already assigned

---------
### NoPermissionToUseNftInRewardPool
No permission to create nft campaign

---------
### NoRewardFound
No reward found in this account

---------
### NotCampaignCreator
Not campaign creator

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