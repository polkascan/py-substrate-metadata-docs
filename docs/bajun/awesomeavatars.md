
# AwesomeAvatars

---------
## Calls

---------
### buy
See [`Pallet::buy`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| avatar_id | `AvatarIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'buy', {'avatar_id': 'scale_info::12'}
)
```

---------
### claim_treasury
See [`Pallet::claim_treasury`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| season_id | `SeasonId` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'claim_treasury', {'season_id': 'u16'}
)
```

---------
### forge
See [`Pallet::forge`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| leader | `AvatarIdOf<T>` | 
| sacrifices | `Vec<AvatarIdOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'forge', {
    'leader': 'scale_info::12',
    'sacrifices': ['scale_info::12'],
}
)
```

---------
### lock_avatar
See [`Pallet::lock_avatar`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| avatar_id | `AvatarIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'lock_avatar', {'avatar_id': 'scale_info::12'}
)
```

---------
### mint
See [`Pallet::mint`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| mint_option | `MintOption` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'mint', {
    'mint_option': {
        'pack_size': (
            'One',
            'Three',
            'Six',
        ),
        'pack_type': (
            'Material',
            'Equipment',
            'Special',
        ),
        'payment': ('Free', 'Normal'),
    },
}
)
```

---------
### prepare_avatar
See [`Pallet::prepare_avatar`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| avatar_id | `AvatarIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'prepare_avatar', {'avatar_id': 'scale_info::12'}
)
```

---------
### prepare_ipfs
See [`Pallet::prepare_ipfs`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| avatar_id | `AvatarIdOf<T>` | 
| url | `IpfsUrl` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'prepare_ipfs', {
    'avatar_id': 'scale_info::12',
    'url': 'Bytes',
}
)
```

---------
### remove_price
See [`Pallet::remove_price`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| avatar_id | `AvatarIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'remove_price', {'avatar_id': 'scale_info::12'}
)
```

---------
### set_collection_id
See [`Pallet::set_collection_id`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'set_collection_id', {'collection_id': 'u32'}
)
```

---------
### set_free_mints
See [`Pallet::set_free_mints`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `T::AccountId` | 
| how_many | `MintCount` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'set_free_mints', {
    'how_many': 'u16',
    'target': 'AccountId',
}
)
```

---------
### set_organizer
See [`Pallet::set_organizer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| organizer | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'set_organizer', {'organizer': 'AccountId'}
)
```

---------
### set_price
See [`Pallet::set_price`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| avatar_id | `AvatarIdOf<T>` | 
| price | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'set_price', {
    'avatar_id': 'scale_info::12',
    'price': 'u128',
}
)
```

---------
### set_season
See [`Pallet::set_season`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| season_id | `SeasonId` | 
| season | `SeasonOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'set_season', {
    'season': {
        'base_prob': 'u8',
        'batch_mint_probs': 'Bytes',
        'description': 'Bytes',
        'early_start': 'u32',
        'end': 'u32',
        'fee': {
            'buy_minimum': 'u128',
            'buy_percent': 'u8',
            'mint': {
                'one': 'u128',
                'six': 'u128',
                'three': 'u128',
            },
            'prepare_avatar': 'u128',
            'transfer_avatar': 'u128',
            'upgrade_storage': 'u128',
        },
        'forge_logic': (
            'First',
            'Second',
        ),
        'max_components': 'u8',
        'max_sacrifices': 'u8',
        'max_tier_forges': 'u32',
        'max_variations': 'u8',
        'min_sacrifices': 'u8',
        'mint_logic': (
            'First',
            'Second',
        ),
        'name': 'Bytes',
        'per_period': 'u32',
        'periods': 'u16',
        'single_mint_probs': 'Bytes',
        'start': 'u32',
        'tiers': [
            (
                'None',
                'Common',
                'Uncommon',
                'Rare',
                'Epic',
                'Legendary',
                'Mythical',
            ),
        ],
        'trade_filters': ['u32'],
    },
    'season_id': 'u16',
}
)
```

---------
### set_service_account
See [`Pallet::set_service_account`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| service_account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'set_service_account', {'service_account': 'AccountId'}
)
```

---------
### set_treasurer
See [`Pallet::set_treasurer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| season_id | `SeasonId` | 
| treasurer | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'set_treasurer', {
    'season_id': 'u16',
    'treasurer': 'AccountId',
}
)
```

---------
### transfer_avatar
See [`Pallet::transfer_avatar`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| avatar_id | `AvatarIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'transfer_avatar', {
    'avatar_id': 'scale_info::12',
    'to': 'AccountId',
}
)
```

---------
### transfer_free_mints
See [`Pallet::transfer_free_mints`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| how_many | `MintCount` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'transfer_free_mints', {'how_many': 'u16', 'to': 'AccountId'}
)
```

---------
### unlock_avatar
See [`Pallet::unlock_avatar`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| avatar_id | `AvatarIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'unlock_avatar', {'avatar_id': 'scale_info::12'}
)
```

---------
### unprepare_avatar
See [`Pallet::unprepare_avatar`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| avatar_id | `AvatarIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'unprepare_avatar', {'avatar_id': 'scale_info::12'}
)
```

---------
### update_global_config
See [`Pallet::update_global_config`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_global_config | `GlobalConfigOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'update_global_config', {
    'new_global_config': {
        'forge': {'open': 'bool'},
        'mint': {
            'cooldown': 'u32',
            'free_mint_fee_multiplier': 'u16',
            'open': 'bool',
        },
        'nft_transfer': {
            'open': 'bool',
        },
        'trade': {'open': 'bool'},
        'transfer': {
            'free_mint_transfer_fee': 'u16',
            'min_free_mint_transfer': 'u16',
            'open': 'bool',
        },
    },
}
)
```

---------
### upgrade_storage
See [`Pallet::upgrade_storage`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| beneficiary | `Option<AccountIdOf<T>>` | 
| in_season | `Option<SeasonId>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'upgrade_storage', {
    'beneficiary': (None, 'AccountId'),
    'in_season': (None, 'u16'),
}
)
```

---------
## Events

---------
### AvatarLocked
Avatar locked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| avatar_id | `AvatarIdOf<T>` | ```scale_info::12```

---------
### AvatarPriceSet
Avatar has price set for trade.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| avatar_id | `AvatarIdOf<T>` | ```scale_info::12```
| price | `BalanceOf<T>` | ```u128```

---------
### AvatarPriceUnset
Avatar has price removed for trade.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| avatar_id | `AvatarIdOf<T>` | ```scale_info::12```

---------
### AvatarTraded
Avatar has been traded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| avatar_id | `AvatarIdOf<T>` | ```scale_info::12```
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```

---------
### AvatarTransferred
Avatar transferred.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| avatar_id | `AvatarIdOf<T>` | ```scale_info::12```

---------
### AvatarUnlocked
Avatar unlocked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| avatar_id | `AvatarIdOf<T>` | ```scale_info::12```

---------
### AvatarsForged
Avatar forged.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| avatar_ids | `Vec<(AvatarIdOf<T>, UpgradedComponents)>` | ```[('scale_info::12', 'u8')]```

---------
### AvatarsMinted
Avatars minted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| avatar_ids | `Vec<AvatarIdOf<T>>` | ```['scale_info::12']```

---------
### CollectionIdSet
A collection ID has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `CollectionIdOf<T>` | ```u32```

---------
### FreeMintsSet
Free mints set for target account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| target | `T::AccountId` | ```AccountId```
| how_many | `MintCount` | ```u16```

---------
### FreeMintsTransferred
Free mints transferred between accounts.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| how_many | `MintCount` | ```u16```

---------
### OrganizerSet
An organizer has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| organizer | `T::AccountId` | ```AccountId```

---------
### PreparedAvatar
Avatar prepared.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| avatar_id | `AvatarIdOf<T>` | ```scale_info::12```

---------
### PreparedIpfsUrl
IPFS URL prepared.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| url | `IpfsUrl` | ```Bytes```

---------
### SeasonFinished
A season has finished.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SeasonId` | ```u16```

---------
### SeasonStarted
A season has started.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SeasonId` | ```u16```

---------
### ServiceAccountSet
A service account has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| service_account | `T::AccountId` | ```AccountId```

---------
### StorageTierUpgraded
Storage tier has been upgraded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| season_id | `SeasonId` | ```u16```

---------
### TreasurerSet
A treasurer has been set for a season.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| season_id | `SeasonId` | ```u16```
| treasurer | `T::AccountId` | ```AccountId```

---------
### TreasuryClaimed
A season&\#x27;s treasury has been claimed by a treasurer.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| season_id | `SeasonId` | ```u16```
| treasurer | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### UnpreparedAvatar
Avatar unprepared.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| avatar_id | `AvatarIdOf<T>` | ```scale_info::12```

---------
### UpdatedGlobalConfig
Global configuration updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `GlobalConfigOf<T>` | ```{'mint': {'open': 'bool', 'cooldown': 'u32', 'free_mint_fee_multiplier': 'u16'}, 'forge': {'open': 'bool'}, 'transfer': {'open': 'bool', 'free_mint_transfer_fee': 'u16', 'min_free_mint_transfer': 'u16'}, 'trade': {'open': 'bool'}, 'nft_transfer': {'open': 'bool'}}```

---------
### UpdatedSeason
The season configuration for {season_id} has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| season_id | `SeasonId` | ```u16```
| season | `SeasonOf<T>` | ```{'name': 'Bytes', 'description': 'Bytes', 'early_start': 'u32', 'start': 'u32', 'end': 'u32', 'max_tier_forges': 'u32', 'max_variations': 'u8', 'max_components': 'u8', 'min_sacrifices': 'u8', 'max_sacrifices': 'u8', 'tiers': [('None', 'Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythical')], 'single_mint_probs': 'Bytes', 'batch_mint_probs': 'Bytes', 'base_prob': 'u8', 'per_period': 'u32', 'periods': 'u16', 'trade_filters': ['u32'], 'fee': {'mint': {'one': 'u128', 'three': 'u128', 'six': 'u128'}, 'transfer_avatar': 'u128', 'buy_minimum': 'u128', 'buy_percent': 'u8', 'upgrade_storage': 'u128', 'prepare_avatar': 'u128'}, 'mint_logic': ('First', 'Second'), 'forge_logic': ('First', 'Second')}```

---------
## Storage functions

---------
### Avatars

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'Avatars', ['scale_info::12']
)
```

#### Return value
```python
(
    'AccountId',
    {'dna': 'Bytes', 'encoding': ('V1', 'V2'), 'season_id': 'u16', 'souls': 'u32'},
)
```
---------
### CollectionId

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'CollectionId', []
)
```

#### Return value
```python
'u32'
```
---------
### CurrentSeasonStatus

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'CurrentSeasonStatus', []
)
```

#### Return value
```python
{
    'active': 'bool',
    'early': 'bool',
    'early_ended': 'bool',
    'max_tier_avatars': 'u32',
    'season_id': 'u16',
}
```
---------
### GlobalConfigs

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'GlobalConfigs', []
)
```

#### Return value
```python
{
    'forge': {'open': 'bool'},
    'mint': {
        'cooldown': 'u32',
        'free_mint_fee_multiplier': 'u16',
        'open': 'bool',
    },
    'nft_transfer': {'open': 'bool'},
    'trade': {'open': 'bool'},
    'transfer': {
        'free_mint_transfer_fee': 'u16',
        'min_free_mint_transfer': 'u16',
        'open': 'bool',
    },
}
```
---------
### LockedAvatars

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'LockedAvatars', ['scale_info::12']
)
```

#### Return value
```python
()
```
---------
### Organizer

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'Organizer', []
)
```

#### Return value
```python
'AccountId'
```
---------
### Owners

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'Owners', ['AccountId', 'u16']
)
```

#### Return value
```python
['scale_info::12']
```
---------
### PlayerConfigs

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'PlayerConfigs', ['AccountId']
)
```

#### Return value
```python
{'free_mints': 'u16'}
```
---------
### PlayerSeasonConfigs

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'PlayerSeasonConfigs', ['AccountId', 'u16']
)
```

#### Return value
```python
{
    'stats': {
        'forge': {
            'first': 'u32',
            'last': 'u32',
            'seasons_participated': 'scale_info::520',
        },
        'mint': {
            'first': 'u32',
            'last': 'u32',
            'seasons_participated': 'scale_info::520',
        },
        'trade': {'bought': 'u32', 'sold': 'u32'},
    },
    'storage_tier': ('One', 'Two', 'Three', 'Four', 'Five', 'Max'),
}
```
---------
### Preparation

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'Preparation', ['scale_info::12']
)
```

#### Return value
```python
'Bytes'
```
---------
### SeasonStats

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'SeasonStats', ['u16', 'AccountId']
)
```

#### Return value
```python
{'forged': 'u32', 'minted': 'u32'}
```
---------
### Seasons
 Storage for the seasons.

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'Seasons', ['u16']
)
```

#### Return value
```python
{
    'base_prob': 'u8',
    'batch_mint_probs': 'Bytes',
    'description': 'Bytes',
    'early_start': 'u32',
    'end': 'u32',
    'fee': {
        'buy_minimum': 'u128',
        'buy_percent': 'u8',
        'mint': {'one': 'u128', 'six': 'u128', 'three': 'u128'},
        'prepare_avatar': 'u128',
        'transfer_avatar': 'u128',
        'upgrade_storage': 'u128',
    },
    'forge_logic': ('First', 'Second'),
    'max_components': 'u8',
    'max_sacrifices': 'u8',
    'max_tier_forges': 'u32',
    'max_variations': 'u8',
    'min_sacrifices': 'u8',
    'mint_logic': ('First', 'Second'),
    'name': 'Bytes',
    'per_period': 'u32',
    'periods': 'u16',
    'single_mint_probs': 'Bytes',
    'start': 'u32',
    'tiers': [
        (
            'None',
            'Common',
            'Uncommon',
            'Rare',
            'Epic',
            'Legendary',
            'Mythical',
        ),
    ],
    'trade_filters': ['u32'],
}
```
---------
### ServiceAccount

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'ServiceAccount', []
)
```

#### Return value
```python
'AccountId'
```
---------
### Trade

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'Trade', ['u16', 'scale_info::12']
)
```

#### Return value
```python
'u128'
```
---------
### Treasurer

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'Treasurer', ['u16']
)
```

#### Return value
```python
'AccountId'
```
---------
### Treasury

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'Treasury', ['u16']
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### KeyLimit
 The maximum length of an attribute key.
#### Value
```python
32
```
#### Python
```python
constant = substrate.get_constant('AwesomeAvatars', 'KeyLimit')
```
---------
### PalletId
#### Value
```python
'0x616a2f6161617472'
```
#### Python
```python
constant = substrate.get_constant('AwesomeAvatars', 'PalletId')
```
---------
### ValueLimit
 The maximum length of an attribute value.
#### Value
```python
64
```
#### Python
```python
constant = substrate.get_constant('AwesomeAvatars', 'ValueLimit')
```
---------
## Errors

---------
### AlreadyOwned
Attempt to buy his or her own avatar.

---------
### AlreadyPrepared
Tried to prepare an already prepared avatar.

---------
### AvatarCannotBeTraded
This avatar cannot be used in trades.

---------
### AvatarInTrade
An avatar listed for trade is used to forge.

---------
### AvatarLocked
The avatar is currently locked and cannot be used.

---------
### AvatarUnlocked
The avatar is currently unlocked and cannot be locked again.

---------
### BaseProbTooHigh
The given base probability is too high. It must be less than 100.

---------
### BatchMintProbsOverflow
The sum of the given batch mint probabilities overflows.

---------
### CannotClaimDuringSeason
Tried claiming treasury during a season.

---------
### CannotClaimZero
Tried claiming treasury which is zero.

---------
### CannotTransferFromInactiveAccount
Tried transferring while the account still hasn&\#x27;t minted and forged anything.

---------
### CannotTransferToSelf
Tried transferring to his or her own account.

---------
### CollectionIdNotSet
There is no collection ID set for NFT handler.

---------
### DuplicatedRarityTier
Some rarity tier are duplicated.

---------
### EarlyStartTooEarly
The season starts before the previous season has ended.

---------
### EarlyStartTooLate
The season season start later than its early access

---------
### EmptyIpfsUrl
Tried to prepare an IPFS URL for an avatar with an empty URL.

---------
### ExcessiveSacrifices
The amount of sacrifices is too much for forging.

---------
### ForgeClosed
Forging is not available at the moment.

---------
### IncompatibleAvatarVersions
Tried to forge avatars with different DNA versions.

---------
### IncompatibleForgeComponents
The components tried to forge were not compatible.

---------
### IncompatibleMintComponents
The components tried to mint were not compatible.

---------
### IncorrectAvatarId
Incorrect Avatar ID.

---------
### IncorrectAvatarSeason
Tried to forge avatars from different seasons.

---------
### IncorrectData
Incorrect data.

---------
### IncorrectDna
Incorrect DNA.

---------
### IncorrectRarityPercentages
Rarity percentages don&\#x27;t add up to 100

---------
### IncorrectSeasonId
Incorrect season ID.

---------
### InsufficientBalance
The player has not enough balance available.

---------
### InsufficientFreeMints
The player has not enough free mints available.

---------
### InsufficientSacrifices
The amount of sacrifices is not sufficient for forging.

---------
### InsufficientStorageForForging
There&\#x27;s not enough space to hold the forging results

---------
### LeaderSacrificed
Leader is being sacrificed.

---------
### MaxComponentsTooHigh
The season&\#x27;s max components value is more than the maximum allowed (random byte: 32).

---------
### MaxComponentsTooLow
The season&\#x27;s max components value is less than the minimum allowed (1).

---------
### MaxOwnershipReached
Max ownership reached.

---------
### MaxStorageTierReached
Max storage tier reached.

---------
### MaxVariationsTooHigh
The season&\#x27;s max variations value is more than the maximum allowed (15).

---------
### MaxVariationsTooLow
The season&\#x27;s max variations value is less than the minimum allowed (1).

---------
### MintClosed
Minting is not available at the moment.

---------
### MintCooldown
The player must wait cooldown period.

---------
### NftTransferClosed
NFT transfer is not available at the moment.

---------
### NoServiceAccount
No service account has been set.

---------
### NonSequentialSeasonId
The season ID of a season to create is not sequential.

---------
### NotPrepared
Tried to prepare an IPFS URL for an avatar, that is not yet prepared.

---------
### OrganizerNotSet
There is no account set as the organizer

---------
### Ownership
Avatar belongs to someone else.

---------
### PeriodConfigOverflow
The season&\#x27;s per period and periods configuration overflows.

---------
### PeriodsIndivisible
The season&\#x27;s periods configuration is indivisible by max variation.

---------
### PrematureSeasonEnd
Attempt to mint when the season has ended prematurely.

---------
### SeasonClosed
Attempt to mint or forge outside of an active season.

---------
### SeasonEndTooLate
The season ends after the new season has started.

---------
### SeasonStartTooLate
The season start date is newer than its end date.

---------
### SingleMintProbsOverflow
The sum of the given single mint probabilities overflows.

---------
### TooFewSacrifices
Less than minimum allowed sacrifices are used for forging.

---------
### TooLowFreeMints
Attempt to transfer, issue or withdraw free mints lower than the minimum allowed.

---------
### TooManyRarityPercentages
Max tier is achievable through forging only. Therefore the number of rarity percentages
must be less than that of tiers for a season.

---------
### TooManySacrifices
More than maximum allowed sacrifices are used for forging.

---------
### TradeClosed
Trading is not available at the moment.

---------
### TransferClosed
Transfer is not available at the moment.

---------
### UnknownAvatar
The avatar doesn&\#x27;t exist.

---------
### UnknownAvatarForSale
The avatar for sale doesn&\#x27;t exist.

---------
### UnknownPreparation
The preparation doesn&\#x27;t exist.

---------
### UnknownSeason
The season doesn&\#x27;t exist.

---------
### UnknownTier
The tier doesn&\#x27;t exist.

---------
### UnknownTreasurer
The treasurer doesn&\#x27;t exist.

---------