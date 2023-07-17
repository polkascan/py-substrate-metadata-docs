
# PWIncubation

---------
## Calls

---------
### feed_origin_of_shell
Sender tried to feed another Origin of Shell. This function will allocate a new daily
daily ration of food if the sender has not sent food to another Origin of Shell within
the current Era. If the sender has already sent food, the sender&\#x27;s FoodInfo will be
mutated to update the food left and the origin of shells the sender has fed during the
current Era.

Parameters:
- origin: The origin of the extrinsic feeding the target Origin of Shell.
- collection_id: The collection id of the Origin of Shell.
- nft_id: The NFT id of the Origin of Shell.
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
Hatch the origin_of_shell that is currently being hatched. This will trigger the end of
the incubation process and the origin_of_shell will be burned. After burning, the user
will receive the awakened Shell RMRK NFT and the nested NFT parts that renders the Shell
NFT.

Parameters:
- `origin`: Expected to be the `Overlord` account
- `collection_id`: The collection id of the Origin of Shell RMRK NFT
- `nft_id`: The NFT id of the Origin of Shell RMRK NFT
- `default_shell_metadata`: File resource URI in decentralized storage for Shell NFT
	parts that render the Shell NFT
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
Privileged function to enable incubation phase for accounts to start the incubation
process for their Origin of Shells.

Parameters:
`origin`: Expected to be the `Overlord` account
`status`: `bool` value to set for the status in storage
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
Privileged function to set the parts chosen by an account for a specific Origin of Shell.

Parameters:
- `origin` - Expected Overlord admin account to set the chosen part to the Origin of Shell
- `collection_id` - Collection ID of Origin of Shell
- `nft_id` - NFT ID of the Origin of Shell
- `chosen_parts` - Shell parts to be stored in Storage
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
        'parts': 'scale_info::182',
    },
    'collection_id': 'u32',
    'nft_id': 'u32',
}
)
```

---------
### set_shell_collection_id
Privileged function to set the collection id for the Awakened Shell collection.

Parameters:
- `origin` - Expected Overlord admin account to set the Shell Collection ID
- `collection_id` - Collection ID of the Shell Collection
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
Privileged function to set the collection id for the Shell Parts collection.

Parameters:
- `origin` - Expected Overlord admin account to set the Shell Parts Collection ID
- `collection_id` - Collection ID of the Shell Parts Collection
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
Once users have received their origin_of_shells and the start incubation event has been
triggered, they can start the incubation process and a timer will start for the
origin_of_shell to awaken at a designated time. Origin of Shells can reduce their time
by being in the top 10 of origin_of_shell&\#x27;s fed per era.

Parameters:
- origin: The origin of the extrinsic starting the incubation process
- collection_id: The collection id of the Origin of Shell RMRK NFT
- nft_id: The NFT id of the Origin of Shell RMRK NFT
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
| old_chosen_parts | `Option<ShellPartsOf<T>>` | ```(None, {'parts': 'scale_info::182'})```
| new_chosen_parts | `ShellPartsOf<T>` | ```{'parts': 'scale_info::182'}```

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
{'era': 'u64', 'food_left': 'u32', 'origin_of_shells_fed': 'scale_info::674'}
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
{'parts': 'scale_info::182'}
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