
# PWIncubation

---------
## Calls

---------
### feed_origin_of_shell
See [`Pallet::feed_origin_of_shell`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 

#### Python
```python
call = substrate.compose_call(
    'PWIncubation', 'feed_origin_of_shell', {
    'collection_id': 'u32',
    'nft_id': 'u32',
}
)
```

---------
### hatch_origin_of_shell
See [`Pallet::hatch_origin_of_shell`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 
| default_shell_metadata | `BoundedVec<u8, T::StringLimit>` | 

#### Python
```python
call = substrate.compose_call(
    'PWIncubation', 'hatch_origin_of_shell', {
    'collection_id': 'u32',
    'default_shell_metadata': 'Bytes',
    'nft_id': 'u32',
}
)
```

---------
### set_can_start_incubation_status
See [`Pallet::set_can_start_incubation_status`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| status | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'PWIncubation', 'set_can_start_incubation_status', {'status': 'bool'}
)
```

---------
### set_origin_of_shell_chosen_parts
See [`Pallet::set_origin_of_shell_chosen_parts`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 
| chosen_parts | `ShellPartsOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PWIncubation', 'set_origin_of_shell_chosen_parts', {
    'chosen_parts': {
        'parts': 'scale_info::183',
    },
    'collection_id': 'u32',
    'nft_id': 'u32',
}
)
```

---------
### set_shell_collection_id
See [`Pallet::set_shell_collection_id`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'PWIncubation', 'set_shell_collection_id', {'collection_id': 'u32'}
)
```

---------
### set_shell_parts_collection_id
See [`Pallet::set_shell_parts_collection_id`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'PWIncubation', 'set_shell_parts_collection_id', {'collection_id': 'u32'}
)
```

---------
### start_incubation
See [`Pallet::start_incubation`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 

#### Python
```python
call = substrate.compose_call(
    'PWIncubation', 'start_incubation', {
    'collection_id': 'u32',
    'nft_id': 'u32',
}
)
```

---------
## Events

---------
### CanStartIncubationStatusChanged
CanStartIncubation status changed and set official hatch time.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| status | `bool` | ```bool```
| start_time | `u64` | ```u64```
| official_hatch_time | `u64` | ```u64```

---------
### OriginOfShellChosenPartsUpdated
Origin of Shell updated chosen parts.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `CollectionId` | ```u32```
| nft_id | `NftId` | ```u32```
| old_chosen_parts | `Option<ShellPartsOf<T>>` | ```(None, {'parts': 'scale_info::183'})```
| new_chosen_parts | `ShellPartsOf<T>` | ```{'parts': 'scale_info::183'}```

---------
### OriginOfShellReceivedFood
Origin of Shell received food from an account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `CollectionId` | ```u32```
| nft_id | `NftId` | ```u32```
| sender | `T::AccountId` | ```AccountId```
| era | `EraId` | ```u64```

---------
### ShellAwakened
Shell has been awakened from an origin_of_shell being hatched and burned.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shell_collection_id | `CollectionId` | ```u32```
| shell_nft_id | `NftId` | ```u32```
| rarity | `RarityType` | ```('Prime', 'Magic', 'Legendary')```
| career | `CareerType` | ```('HackerWizard', 'HardwareDruid', 'RoboWarrior', 'TradeNegotiator', 'Web3Monk')```
| race | `RaceType` | ```('Cyborg', 'AISpectre', 'XGene', 'Pandroid')```
| generation_id | `GenerationId` | ```u32```
| origin_of_shell_collection_id | `CollectionId` | ```u32```
| origin_of_shell_nft_id | `NftId` | ```u32```
| owner | `T::AccountId` | ```AccountId```

---------
### ShellCollectionIdSet
Shell Collection ID is set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `CollectionId` | ```u32```

---------
### ShellPartMinted
Shell Part minted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shell_parts_collection_id | `CollectionId` | ```u32```
| shell_part_nft_id | `NftId` | ```u32```
| parent_shell_collection_id | `CollectionId` | ```u32```
| parent_shell_nft_id | `NftId` | ```u32```
| owner | `T::AccountId` | ```AccountId```

---------
### ShellPartsCollectionIdSet
Shell Parts Collection ID is set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `CollectionId` | ```u32```

---------
### StartedIncubation
Origin of Shell owner has initiated the incubation sequence.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `CollectionId` | ```u32```
| nft_id | `NftId` | ```u32```
| owner | `T::AccountId` | ```AccountId```
| start_time | `u64` | ```u64```
| hatch_time | `u64` | ```u64```

---------
## Storage functions

---------
### CanStartIncubation
 A bool value to determine if accounts can start incubation of Origin of Shells.

#### Python
```python
result = substrate.query(
    'PWIncubation', 'CanStartIncubation', []
)
```

#### Return value
```python
'bool'
```
---------
### FoodByOwners
 Info on Origin of Shells that the Owner has fed and the number of food left to feed other
 Origin of Shells.

#### Python
```python
result = substrate.query(
    'PWIncubation', 'FoodByOwners', ['AccountId']
)
```

#### Return value
```python
{'era': 'u64', 'food_left': 'u32', 'origin_of_shells_fed': 'scale_info::704'}
```
---------
### HasOriginOfShellStartedIncubation
 A bool value to determine if an Origin of Shell has started the incubation process.

#### Python
```python
result = substrate.query(
    'PWIncubation', 'HasOriginOfShellStartedIncubation', [('u32', 'u32')]
)
```

#### Return value
```python
'bool'
```
---------
### OfficialHatchTime
 Official hatch time for all Origin of Shells.

#### Python
```python
result = substrate.query(
    'PWIncubation', 'OfficialHatchTime', []
)
```

#### Return value
```python
'u64'
```
---------
### OriginOfShellFoodStats
 Total food fed to an Origin of Shell per Era.

#### Python
```python
result = substrate.query(
    'PWIncubation', 'OriginOfShellFoodStats', ['u64', ('u32', 'u32')]
)
```

#### Return value
```python
'u32'
```
---------
### OriginOfShellsChosenParts
 Storage of an account&#x27;s selected parts during the incubation process.

#### Python
```python
result = substrate.query(
    'PWIncubation', 'OriginOfShellsChosenParts', [('u32', 'u32')]
)
```

#### Return value
```python
{'parts': 'scale_info::183'}
```
---------
### ShellCollectionId
 Collection ID of the Shell NFT.

#### Python
```python
result = substrate.query(
    'PWIncubation', 'ShellCollectionId', []
)
```

#### Return value
```python
'u32'
```
---------
### ShellPartsCollectionId
 Collection ID of the Shell Parts NFTs.

#### Python
```python
result = substrate.query(
    'PWIncubation', 'ShellPartsCollectionId', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### FoodPerEra
 Amount of food per Era.
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('PWIncubation', 'FoodPerEra')
```
---------
### IncubationDurationSec
 Duration of incubation process.
#### Value
```python
691200
```
#### Python
```python
constant = substrate.get_constant('PWIncubation', 'IncubationDurationSec')
```
---------
### MaxFoodFeedSelf
 Max food to feed your own Origin of Shell.
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('PWIncubation', 'MaxFoodFeedSelf')
```
---------
## Errors

---------
### AlreadySentFoodTwice

---------
### CannotHatchOriginOfShell

---------
### CannotSendFoodToOriginOfShell

---------
### CannotSetOriginOfShellChosenParts

---------
### CareerNotDetected

---------
### ChosenPartsNotDetected

---------
### FoodInfoUpdateError

---------
### GenerationNotDetected

---------
### HatchingInProgress

---------
### MissingShellPartMetadata

---------
### NoFoodLeftToFeedOriginOfShell

---------
### NoPermission

---------
### NotOwner

---------
### RaceNotDetected

---------
### RarityTypeNotDetected

---------
### ShellCollectionIdAlreadySet

---------
### ShellCollectionIdNotSet

---------
### ShellPartsCollectionIdAlreadySet

---------
### ShellPartsCollectionIdNotSet

---------
### StartIncubationNotAvailable

---------
### WrongCollectionId

---------
### _Deprecated_MaxFoodFedLimitReached

---------
### _Deprecated_NoFoodAvailable

---------
### _Deprecated_NoHatchTimeDetected

---------