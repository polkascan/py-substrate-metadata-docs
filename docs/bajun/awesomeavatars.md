
# AwesomeAvatars

---------
## Calls

---------
### buy
Buy the given avatar.

It consumes tokens for the trade operation. The avatar will be owned by the
player after the transaction.

Only allowed while trade period is open.

Emits `AvatarTraded` event when successful.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| avatar_id | `AvatarIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'buy', {'avatar_id': '[u8; 32]'}
)
```

---------
### claim_treasury
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
### fix_variation
#### Attributes
| Name | Type |
| -------- | -------- | 
| avatar_id | `AvatarIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'fix_variation', {'avatar_id': '[u8; 32]'}
)
```

---------
### forge
Forge an avatar.

This action can enhance the skills of an avatar by consuming a batch of avatars.
The minimum and maximum number of avatars that can be utilized for forging is
defined in the season configuration.

Emits `AvatarForged` event when successful.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| leader | `AvatarIdOf<T>` | 
| sacrifices | `Vec<AvatarIdOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'forge', {
    'leader': '[u8; 32]',
    'sacrifices': ['[u8; 32]'],
}
)
```

---------
### lock_avatar
#### Attributes
| Name | Type |
| -------- | -------- | 
| avatar_id | `AvatarIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'lock_avatar', {'avatar_id': '[u8; 32]'}
)
```

---------
### mint
Issue a new avatar.

Emits `AvatarsMinted` event when successful.

Weight: `O(n)` where:
- `n = max avatars per player`
#### Attributes
| Name | Type |
| -------- | -------- | 
| mint_option | `MintOption` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'mint', {
    'mint_option': {
        'count': (
            'One',
            'Three',
            'Six',
        ),
        'mint_type': (
            'Free',
            'Normal',
        ),
    },
}
)
```

---------
### prepare_avatar
#### Attributes
| Name | Type |
| -------- | -------- | 
| avatar_id | `AvatarIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'prepare_avatar', {'avatar_id': '[u8; 32]'}
)
```

---------
### prepare_ipfs
#### Attributes
| Name | Type |
| -------- | -------- | 
| avatar_id | `AvatarIdOf<T>` | 
| url | `IpfsUrl` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'prepare_ipfs', {
    'avatar_id': '[u8; 32]',
    'url': 'Bytes',
}
)
```

---------
### remove_price
Remove the price of a given avatar.

Only allowed while trade period is open.

Emits `AvatarPriceUnset` event when successful.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| avatar_id | `AvatarIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'remove_price', {'avatar_id': '[u8; 32]'}
)
```

---------
### set_collection_id
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
Set free mints.

It can only be called by an organizer account.

Emits `FreeMintSet` event when successful.

Weight: `O(1)`
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
Set game organizer.

The organizer account is like an admin, allowed to perform certain operations
related with the game configuration like `set_season`, `ensure_free_mint` and
`update_global_config`.

It can only be set by a root account.

Emits `OrganizerSet` event when successful.

Weight: `O(1)`
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
Set the price of a given avatar.

Only allowed while trade period is open.

Emits `AvatarPriceSet` event when successful.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| avatar_id | `AvatarIdOf<T>` | 
| price | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'set_price', {
    'avatar_id': '[u8; 32]',
    'price': 'u128',
}
)
```

---------
### set_season
Set season.

Creates a new season. The new season can overlap with the already existing.

It can only be set by an organizer account.

Emits `UpdatedSeason` event when successful.

Weight: `O(1)`
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
        'max_components': 'u8',
        'max_sacrifices': 'u8',
        'max_tier_forges': 'u32',
        'max_variations': 'u8',
        'min_sacrifices': 'u8',
        'name': 'Bytes',
        'per_period': 'u32',
        'periods': 'u16',
        'single_mint_probs': 'Bytes',
        'start': 'u32',
        'tiers': [
            (
                'Common',
                'Uncommon',
                'Rare',
                'Epic',
                'Legendary',
                'Mythical',
            ),
        ],
    },
    'season_id': 'u16',
}
)
```

---------
### set_service_account
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
Set treasurer.

This is an additional treasury.

It can only be set by a root account.

Emits `TreasurerSet` event when successful.

Weight: `O(1)`
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
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| avatar_id | `AvatarIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'transfer_avatar', {
    'avatar_id': '[u8; 32]',
    'to': 'AccountId',
}
)
```

---------
### transfer_free_mints
Transfer free mints to a given account.

Emits `FreeMintsTransferred` event when successful.

Weight: `O(1)`
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
#### Attributes
| Name | Type |
| -------- | -------- | 
| avatar_id | `AvatarIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'unlock_avatar', {'avatar_id': '[u8; 32]'}
)
```

---------
### unprepare_avatar
#### Attributes
| Name | Type |
| -------- | -------- | 
| avatar_id | `AvatarIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'unprepare_avatar', {'avatar_id': '[u8; 32]'}
)
```

---------
### update_global_config
Update global configuration.

It can only be called by an organizer account.

Emits `UpdatedGlobalConfig` event when successful.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_global_config | `GlobalConfigOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'update_global_config', {
    'new_global_config': {
        'account': {
            'storage_upgrade_fee': 'u128',
        },
        'forge': {'open': 'bool'},
        'mint': {
            'cooldown': 'u32',
            'fees': {
                'one': 'u128',
                'six': 'u128',
                'three': 'u128',
            },
            'free_mint_fee_multiplier': 'u16',
            'open': 'bool',
        },
        'nft_transfer': {
            'open': 'bool',
            'prepare_fee': 'u128',
        },
        'trade': {
            'min_fee': 'u128',
            'open': 'bool',
            'percent_fee': 'u8',
        },
        'transfer': {
            'avatar_transfer_fee': 'u128',
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
Upgrade storage.

Emits `StorageTierUpgraded` event when successful.

Weight: `O(1)`
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'AwesomeAvatars', 'upgrade_storage', {}
)
```

---------
## Events

---------
### AvatarForged
Avatar forged.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| avatar_id | `AvatarIdOf<T>` | ```[u8; 32]```
| upgraded_components | `u8` | ```u8```

---------
### AvatarLocked
Avatar locked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| avatar_id | `AvatarIdOf<T>` | ```[u8; 32]```

---------
### AvatarPriceSet
Avatar has price set for trade.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| avatar_id | `AvatarIdOf<T>` | ```[u8; 32]```
| price | `BalanceOf<T>` | ```u128```

---------
### AvatarPriceUnset
Avatar has price removed for trade.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| avatar_id | `AvatarIdOf<T>` | ```[u8; 32]```

---------
### AvatarTraded
Avatar has been traded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| avatar_id | `AvatarIdOf<T>` | ```[u8; 32]```
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
| avatar_id | `AvatarIdOf<T>` | ```[u8; 32]```

---------
### AvatarUnlocked
Avatar unlocked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| avatar_id | `AvatarIdOf<T>` | ```[u8; 32]```

---------
### AvatarsMinted
Avatars minted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| avatar_ids | `Vec<AvatarIdOf<T>>` | ```['[u8; 32]']```

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
| avatar_id | `AvatarIdOf<T>` | ```[u8; 32]```

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
No attributes

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
| avatar_id | `AvatarIdOf<T>` | ```[u8; 32]```

---------
### UpdatedGlobalConfig
Global configuration updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `GlobalConfigOf<T>` | ```{'mint': {'open': 'bool', 'fees': {'one': 'u128', 'three': 'u128', 'six': 'u128'}, 'cooldown': 'u32', 'free_mint_fee_multiplier': 'u16'}, 'forge': {'open': 'bool'}, 'transfer': {'open': 'bool', 'free_mint_transfer_fee': 'u16', 'min_free_mint_transfer': 'u16', 'avatar_transfer_fee': 'u128'}, 'trade': {'open': 'bool', 'min_fee': 'u128', 'percent_fee': 'u8'}, 'account': {'storage_upgrade_fee': 'u128'}, 'nft_transfer': {'open': 'bool', 'prepare_fee': 'u128'}}```

---------
### UpdatedSeason
The season configuration for {season_id} has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| season_id | `SeasonId` | ```u16```
| season | `SeasonOf<T>` | ```{'name': 'Bytes', 'description': 'Bytes', 'early_start': 'u32', 'start': 'u32', 'end': 'u32', 'max_tier_forges': 'u32', 'max_variations': 'u8', 'max_components': 'u8', 'min_sacrifices': 'u8', 'max_sacrifices': 'u8', 'tiers': [('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythical')], 'single_mint_probs': 'Bytes', 'batch_mint_probs': 'Bytes', 'base_prob': 'u8', 'per_period': 'u32', 'periods': 'u16'}```

---------
## Storage functions

---------
### Accounts

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'Accounts', ['AccountId']
)
```

#### Return value
```python
{
    'free_mints': 'u16',
    'stats': {
        'forge': {
            'first': 'u32',
            'last': 'u32',
            'seasons_participated': 'scale_info::413',
        },
        'mint': {
            'first': 'u32',
            'last': 'u32',
            'seasons_participated': 'scale_info::413',
        },
        'trade': {'bought': 'u32', 'sold': 'u32'},
    },
    'storage_tier': ('One', 'Two', 'Three', 'Four', 'Five', 'Max'),
}
```
---------
### Avatars

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'Avatars', ['[u8; 32]']
)
```

#### Return value
```python
('AccountId', {'dna': 'Bytes', 'season_id': 'u16', 'souls': 'u32'})
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
### CurrentSeasonId
 Contains the identifier of the current season.

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'CurrentSeasonId', []
)
```

#### Return value
```python
'u16'
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
    'account': {'storage_upgrade_fee': 'u128'},
    'forge': {'open': 'bool'},
    'mint': {
        'cooldown': 'u32',
        'fees': {'one': 'u128', 'six': 'u128', 'three': 'u128'},
        'free_mint_fee_multiplier': 'u16',
        'open': 'bool',
    },
    'nft_transfer': {'open': 'bool', 'prepare_fee': 'u128'},
    'trade': {'min_fee': 'u128', 'open': 'bool', 'percent_fee': 'u8'},
    'transfer': {
        'avatar_transfer_fee': 'u128',
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
    'AwesomeAvatars', 'LockedAvatars', ['[u8; 32]']
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
    'AwesomeAvatars', 'Owners', ['AccountId']
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### Preparation

#### Python
```python
result = substrate.query(
    'AwesomeAvatars', 'Preparation', ['[u8; 32]']
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
    'max_components': 'u8',
    'max_sacrifices': 'u8',
    'max_tier_forges': 'u32',
    'max_variations': 'u8',
    'min_sacrifices': 'u8',
    'name': 'Bytes',
    'per_period': 'u32',
    'periods': 'u16',
    'single_mint_probs': 'Bytes',
    'start': 'u32',
    'tiers': [('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythical')],
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
    'AwesomeAvatars', 'Trade', ['[u8; 32]']
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
## Errors

---------
### AlreadyOwned
Attempt to buy his or her own avatar.

---------
### AlreadyPrepared
Tried to prepare an already prepared avatar.

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
### CannotClaimDuringSeason
Tried claiming treasury during a season.

---------
### CannotClaimZero
Tried claiming treasury which is zero.

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
### ForgeClosed
Forging is not available at the moment.

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
### InsufficientFreeMints
The player has not enough free mints available.

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
### TooFewSacrifices
Less than minimum allowed sacrifices are used for forging.

---------
### TooLowFees
Attempt to set fees lower than the existential deposit amount.

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