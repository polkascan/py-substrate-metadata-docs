
# Referrals

---------
## Calls

---------
### claim_rewards
See [`Pallet::claim_rewards`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Referrals', 'claim_rewards', {}
)
```

---------
### convert
See [`Pallet::convert`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'Referrals', 'convert', {'asset_id': 'u32'}
)
```

---------
### link_code
See [`Pallet::link_code`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| code | `ReferralCode<T::CodeLength>` | 

#### Python
```python
call = substrate.compose_call(
    'Referrals', 'link_code', {'code': 'Bytes'}
)
```

---------
### register_code
See [`Pallet::register_code`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| code | `ReferralCode<T::CodeLength>` | 

#### Python
```python
call = substrate.compose_call(
    'Referrals', 'register_code', {'code': 'Bytes'}
)
```

---------
### set_reward_percentage
See [`Pallet::set_reward_percentage`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| level | `Level` | 
| rewards | `FeeDistribution` | 

#### Python
```python
call = substrate.compose_call(
    'Referrals', 'set_reward_percentage', {
    'asset_id': 'u32',
    'level': (
        'None',
        'Tier0',
        'Tier1',
        'Tier2',
        'Tier3',
        'Tier4',
    ),
    'rewards': {
        'external': 'u32',
        'referrer': 'u32',
        'trader': 'u32',
    },
}
)
```

---------
## Events

---------
### AssetRewardsUpdated
New asset rewards has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| level | `Level` | ```('None', 'Tier0', 'Tier1', 'Tier2', 'Tier3', 'Tier4')```
| rewards | `FeeDistribution` | ```{'referrer': 'u32', 'trader': 'u32', 'external': 'u32'}```

---------
### Claimed
Rewards claimed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| referrer_rewards | `Balance` | ```u128```
| trade_rewards | `Balance` | ```u128```

---------
### CodeLinked
Referral code has been linked to an account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| code | `ReferralCode<T::CodeLength>` | ```Bytes```
| referral_account | `T::AccountId` | ```AccountId```

---------
### CodeRegistered
Referral code has been registered.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| code | `ReferralCode<T::CodeLength>` | ```Bytes```
| account | `T::AccountId` | ```AccountId```

---------
### Converted
Asset has been converted to RewardAsset.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `AssetAmount<T::AssetId>` | ```{'asset_id': 'u32', 'amount': 'u128'}```
| to | `AssetAmount<T::AssetId>` | ```{'asset_id': 'u32', 'amount': 'u128'}```

---------
### LevelUp
Referrer reached new level.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| level | `Level` | ```('None', 'Tier0', 'Tier1', 'Tier2', 'Tier3', 'Tier4')```

---------
## Storage functions

---------
### AssetRewards
 Asset fee distribution rewards information.
 Maps (asset_id, level) to asset reward percentages.

#### Python
```python
result = substrate.query(
    'Referrals', 'AssetRewards', [
    'u32',
    (
        'None',
        'Tier0',
        'Tier1',
        'Tier2',
        'Tier3',
        'Tier4',
    ),
]
)
```

#### Return value
```python
{'external': 'u32', 'referrer': 'u32', 'trader': 'u32'}
```
---------
### CounterForPendingConversions
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'Referrals', 'CounterForPendingConversions', []
)
```

#### Return value
```python
'u32'
```
---------
### LinkedAccounts
 Linked accounts.
 Maps an account to a referral account.

#### Python
```python
result = substrate.query(
    'Referrals', 'LinkedAccounts', ['AccountId']
)
```

#### Return value
```python
'AccountId'
```
---------
### PendingConversions
 Information about assets that are currently in the rewards pot.
 Used to easily determine list of assets that need to be converted.

#### Python
```python
result = substrate.query(
    'Referrals', 'PendingConversions', ['u32']
)
```

#### Return value
```python
()
```
---------
### ReferralAccounts
 Referral accounts
 Maps an account to a referral code.

#### Python
```python
result = substrate.query(
    'Referrals', 'ReferralAccounts', ['AccountId']
)
```

#### Return value
```python
'Bytes'
```
---------
### ReferralCodes
 Referral codes
 Maps a referral code to an account.

#### Python
```python
result = substrate.query(
    'Referrals', 'ReferralCodes', ['Bytes']
)
```

#### Return value
```python
'AccountId'
```
---------
### Referrer
 Referer level and total accumulated rewards over time.
 Maps referrer account to (Level, Balance). Level indicates current rewards and Balance is used to unlock next level.
 Dev note: we use OptionQuery here because this helps to easily determine that an account if referrer account.

#### Python
```python
result = substrate.query(
    'Referrals', 'Referrer', ['AccountId']
)
```

#### Return value
```python
(('None', 'Tier0', 'Tier1', 'Tier2', 'Tier3', 'Tier4'), 'u128')
```
---------
### ReferrerShares
 Shares of a referral account

#### Python
```python
result = substrate.query(
    'Referrals', 'ReferrerShares', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### TotalShares
 Total share issuance.

#### Python
```python
result = substrate.query(
    'Referrals', 'TotalShares', []
)
```

#### Return value
```python
'u128'
```
---------
### TraderShares
 Shares of a trader account

#### Python
```python
result = substrate.query(
    'Referrals', 'TraderShares', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### CodeLength
 Maximum referral code length.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Referrals', 'CodeLength')
```
---------
### MinCodeLength
 Minimum referral code length.
#### Value
```python
4
```
#### Python
```python
constant = substrate.get_constant('Referrals', 'MinCodeLength')
```
---------
### PalletId
 Pallet id. Determines account which holds accumulated rewards in various assets.
#### Value
```python
'0x726566657272616c'
```
#### Python
```python
constant = substrate.get_constant('Referrals', 'PalletId')
```
---------
### RegistrationFee
 Registration fee details.
 (ID of an asset which fee is to be paid in, Amount, Beneficiary account)
#### Value
```python
(0, 222000000000000, '7L53bUTBopuwFt3mKUfmkzgGLayYa1Yvn1hAg9v5UMrQzTfh')
```
#### Python
```python
constant = substrate.get_constant('Referrals', 'RegistrationFee')
```
---------
### RewardAsset
 ID of an asset that is used to distribute rewards in.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Referrals', 'RewardAsset')
```
---------
### SeedNativeAmount
 Seed amount that was sent to the reward pot.
#### Value
```python
10000000000000
```
#### Python
```python
constant = substrate.get_constant('Referrals', 'SeedNativeAmount')
```
---------
## Errors

---------
### AlreadyExists
Referral code already exists.

---------
### AlreadyLinked
Account is already linked to another referral account.

---------
### AlreadyRegistered
The account has already a code registered.

---------
### ConversionMinTradingAmountNotReached
Minimum trading amount for conversion has not been reached.

---------
### ConversionZeroAmountReceived
Zero amount received from conversion.

---------
### IncorrectRewardCalculation
Calculated rewards are more than the fee amount. This can happen if percentages are incorrectly set.

---------
### IncorrectRewardPercentage
Given referrer and trader percentages exceeds 100% percent.

---------
### InvalidCharacter
Referral code contains invalid character. Only alphanumeric characters are allowed.

---------
### InvalidCode
Provided referral code is invalid. Either does not exist or is too long.

---------
### LinkNotAllowed
Linking an account to the same referral account is not allowed.

---------
### PriceNotFound
Price for given asset pair not found.

---------
### TooLong
Referral code is too long.

---------
### TooShort
Referral code is too short.

---------
### ZeroAmount
Nothing in the referral pot account for the asset.

---------