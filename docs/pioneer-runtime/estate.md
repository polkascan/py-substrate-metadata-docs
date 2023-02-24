
# Estate

---------
## Calls

---------
### accept_lease_offer
Accept lease offer for estate that is not leased

The dispatch origin for this call must be _Singed_.
Only the estate owner can make this call.
- `estate_id`: the ID of the estate that will be leased
- `recipient`: the account that made the lease offer

Emits `EstateLeaseOfferAccepted` if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| estate_id | `EstateId` | 
| recipient | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'accept_lease_offer', {
    'estate_id': 'u64',
    'recipient': 'AccountId',
}
)
```

---------
### add_land_unit_to_estate
Add more land units to existing estate that is not in auction

The dispatch origin for this call must be _Singed_.
Only the estate owner can make this call.
They must also own the land units.
- `estate_id`: the ID of the estate that the land units will be added to
- `land_units`: list of land unit coordinates that will be added to estate

Emits `LandUnitAdded` if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| estate_id | `EstateId` | 
| land_units | `Vec<(i32, i32)>` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'add_land_unit_to_estate', {
    'estate_id': 'u64',
    'land_units': [('i32', 'i32')],
}
)
```

---------
### approve_undeployed_land_blocks
Approve existing undeployed land block which is not frozen.

The dispatch origin for this call must be _Singed_.
Only the undeployed land block owner can make this call.
- `to`: the account for which the undeployed land block will be approved
- `undeployed_land_block_id`: the ID of the undeployed land block that will be burned

Emits `UndeployedLandBlockApproved` if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| undeployed_land_block_id | `UndeployedLandBlockId` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'approve_undeployed_land_blocks', {
    'to': 'AccountId',
    'undeployed_land_block_id': 'u128',
}
)
```

---------
### burn_undeployed_land_blocks
Burn raw land block that will reduce total supply

The dispatch origin for this call must be _Singed_.
Only the undeployed land block owner can make this call.
- `undeployed_land_block_id`: the ID of the undeployed land block that will be burned

Emits `UndeployedLandBlockBurnt` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| undeployed_land_block_id | `UndeployedLandBlockId` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'burn_undeployed_land_blocks', {'undeployed_land_block_id': 'u128'}
)
```

---------
### cancel_lease
Cancels existing lease

The dispatch origin for this call must be _Root_.
- `estate_id`: the ID of the estate that will be leased
- `leasor`: the account that is leasing the estate

Emits `EstateLeaseContractCancelled` if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| estate_owner | `T::AccountId` | 
| estate_id | `EstateId` | 
| leasor | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'cancel_lease', {
    'estate_id': 'u64',
    'estate_owner': 'AccountId',
    'leasor': 'AccountId',
}
)
```

---------
### collect_rent
Collect rent for a leased estate

The dispatch origin for this call must be _Singed_.
Only the estate owner can make this call.
- `estate_id`: the ID of the estate that will be leased

Emits `EstateRentCollected` if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| estate_id | `EstateId` | 
| leasor | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'collect_rent', {
    'estate_id': 'u64',
    'leasor': 'AccountId',
}
)
```

---------
### create_estate
Create new estate from existing land units

The dispatch origin for this call must be _Signed_.
- `metaverse_id`: the metaverse id that the land units will be minted on
- `coordinates`: list of land units coordinates

Emits `NewEstateMinted` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| metaverse_id | `MetaverseId` | 
| coordinates | `Vec<(i32, i32)>` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'create_estate', {
    'coordinates': [('i32', 'i32')],
    'metaverse_id': 'u64',
}
)
```

---------
### create_lease_offer
Create a lease offer for estate that is not leased

The dispatch origin for this call must be _Singed_.
Only  origin that is not the estate owner can make this call.
- `estate_id`: the ID of the estate that will be leased
- `price_per_block`: lease price per block
- `duration`: lease duration (in number of blocks)

Emits `EstateLeaseOfferCreated` if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| estate_id | `EstateId` | 
| price_per_block | `BalanceOf<T>` | 
| duration | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'create_lease_offer', {
    'duration': 'u32',
    'estate_id': 'u64',
    'price_per_block': 'u128',
}
)
```

---------
### deploy_land_block
Deploy raw land block to metaverse and turn raw land block to land unit with given
coordinates

The dispatch origin for this call must be _Signed_.
Only the undeployed land block owner can make this call.
- `undeployed_land_block_id`: the undeployed land block ID
- `metaverse_id`: the metaverse ID that the land block will be deployed on
- `land_block_coordinates`: the coordinates of the land block
- `coordinates`: list of land units coordinates

Emits `LandBlockDeployed` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| undeployed_land_block_id | `UndeployedLandBlockId` | 
| metaverse_id | `MetaverseId` | 
| land_block_coordinate | `(i32, i32)` | 
| coordinates | `Vec<(i32, i32)>` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'deploy_land_block', {
    'coordinates': [('i32', 'i32')],
    'land_block_coordinate': (
        'i32',
        'i32',
    ),
    'metaverse_id': 'u64',
    'undeployed_land_block_id': 'u128',
}
)
```

---------
### dissolve_estate
Dissolve estate to land units if it is not in auction.

The dispatch origin for this call must be _Singed_.
Only the estate owner can make this call.
- `estate_id`: the ID of the estate that will be dissolved

Emits `EstateDestroyed` if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| estate_id | `EstateId` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'dissolve_estate', {'estate_id': 'u64'}
)
```

---------
### freeze_undeployed_land_blocks
Freezes undeployed land block which is not already frozen

The dispatch origin for this call must be _Root_.
- `undeployed_land_block_id`: the ID of the undeployed land block that will be freezed

Emits `UndeployedLandBlockFreezed` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| undeployed_land_block_id | `UndeployedLandBlockId` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'freeze_undeployed_land_blocks', {'undeployed_land_block_id': 'u128'}
)
```

---------
### issue_undeployed_land_blocks
Issues new undeployed land block(s)

The dispatch origin for this call must be _Root_.
- `beneficiary`: the account which will be the owner of the undeployed land block(s)
- `number_of_land_block`: the number of undeployed land block(s) that will be created
- `number_land_units_per_land_block`: the number of land units in each undeployed land
  block
- `land_block_coordinates`: the coordinates of the undeployed land block

Emits `UndeployedLandBlockIssued` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| beneficiary | `T::AccountId` | 
| number_of_land_block | `u32` | 
| number_land_units_per_land_block | `u32` | 
| undeployed_land_block_type | `UndeployedLandBlockType` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'issue_undeployed_land_blocks', {
    'beneficiary': 'AccountId',
    'number_land_units_per_land_block': 'u32',
    'number_of_land_block': 'u32',
    'undeployed_land_block_type': (
        'Transferable',
        'BoundToAddress',
    ),
}
)
```

---------
### mint_estate
Mint new estate with no existing land units, only used for council to manually mint
estate for beneficiary

The dispatch origin for this call must be _Root_.
- `beneficiary`: the account which will be the owner of the land units
- `metaverse_id`: the metaverse id that the land units will be minted on
- `coordinates`: list of land units coordinates

Emits `NewEstateMinted` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| beneficiary | `T::AccountId` | 
| metaverse_id | `MetaverseId` | 
| coordinates | `Vec<(i32, i32)>` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'mint_estate', {
    'beneficiary': 'AccountId',
    'coordinates': [('i32', 'i32')],
    'metaverse_id': 'u64',
}
)
```

---------
### mint_land
Minting of a land unit, only used by council to manually mint single land for
beneficiary

The dispatch origin for this call must be _Root_.
- `beneficiary`: the account which will be the owner of the land unit
- `metaverse_id`: the metaverse id that the land united will be minted on
- `coordinate`: coordinate of the land unit

Emits `NewLandsMinted` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| beneficiary | `T::AccountId` | 
| metaverse_id | `MetaverseId` | 
| coordinate | `(i32, i32)` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'mint_land', {
    'beneficiary': 'AccountId',
    'coordinate': ('i32', 'i32'),
    'metaverse_id': 'u64',
}
)
```

---------
### mint_lands
Minting of a land units, only used by council to manually mint number of lands for
beneficiary

The dispatch origin for this call must be _Root_.
- `beneficiary`: the account which will be the owner of the land units
- `metaverse_id`: the metaverse id that the land units will be minted on
- `coordinates`: list of land units coordinates

Emits `NewLandsMinted` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| beneficiary | `T::AccountId` | 
| metaverse_id | `MetaverseId` | 
| coordinates | `Vec<(i32, i32)>` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'mint_lands', {
    'beneficiary': 'AccountId',
    'coordinates': [('i32', 'i32')],
    'metaverse_id': 'u64',
}
)
```

---------
### remove_expired_lease
Removes expired lease

The dispatch origin for this call must be _Singed_.
Only the estate owner can make this call.
- `estate_id`: the ID of the estate that will be leased
- `leasor`: the account that is leasing the estate

Emits `EstateLeaseContractEnded` if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| estate_id | `EstateId` | 
| leasor | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'remove_expired_lease', {
    'estate_id': 'u64',
    'leasor': 'AccountId',
}
)
```

---------
### remove_land_unit_from_estate
Remove land units from existing estate if it is not in auction.

The dispatch origin for this call must be _Singed_.
Only the estate owner can make this call.
- `estate_id`: the ID of the estate that the land units will be removed from
- `land_units`: list of land unit coordinates that will be added to estate

Emits `LandUnitsRemoved` if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| estate_id | `EstateId` | 
| land_units | `Vec<(i32, i32)>` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'remove_land_unit_from_estate', {
    'estate_id': 'u64',
    'land_units': [('i32', 'i32')],
}
)
```

---------
### remove_lease_offer
Removes lease offer

The dispatch origin for this call must be _Singed_.
Only the account made the lease offer can make this call.
- `estate_id`: the ID of the estate that will be leased

Emits `EstateLeaseOfferRemoved` if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| estate_id | `EstateId` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'remove_lease_offer', {'estate_id': 'u64'}
)
```

---------
### transfer_estate
Transfer estate ownership if it is not in auction.

The dispatch origin for this call must be _Signed_.
Only the owner of an estate can make this call.
- `to`: the account which will be the owner of the estate
- `estate_id`: the estate ID of the the estate that will be transferred

Emits `TransferredEstate` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| estate_id | `EstateId` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'transfer_estate', {
    'estate_id': 'u64',
    'to': 'AccountId',
}
)
```

---------
### transfer_land
Transferring a land unit if it is not already in auction

The dispatch origin for this call must be _Signed_.
Only the owner of a land can make this call.
- `to`: the account which will be the owner of the land units
- `metaverse_id`: the metaverse id of the land unit
- `coordinate`: the coordinate of the land unit

Emits `TransferredLandUnit` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| metaverse_id | `MetaverseId` | 
| coordinate | `(i32, i32)` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'transfer_land', {
    'coordinate': ('i32', 'i32'),
    'metaverse_id': 'u64',
    'to': 'AccountId',
}
)
```

---------
### transfer_undeployed_land_blocks
Transfer undeployed land block owner if it is not in auction.

The dispatch origin for this call must be _Singed_.
Only the undeployed land block owner can make this call.
- `to`: the account that will receive the undeployed land block
- `undeployed_land_block_id`: the ID of the land block that will be transferred

Emits `UndeployedLandBlockTransferred` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| undeployed_land_block_id | `UndeployedLandBlockId` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'transfer_undeployed_land_blocks', {
    'to': 'AccountId',
    'undeployed_land_block_id': 'u128',
}
)
```

---------
### unapprove_undeployed_land_blocks
Unapprove existing undeployed land block which is not frozen.

The dispatch origin for this call must be _Singed_.
Only the undeployed land block owner can make this call.
- `undeployed_land_block_id`: the ID of the undeployed land block that will be
  unapproved

Emits `UndeployedLandBlockUnapproved` if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| undeployed_land_block_id | `UndeployedLandBlockId` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'unapprove_undeployed_land_blocks', {'undeployed_land_block_id': 'u128'}
)
```

---------
### unfreeze_undeployed_land_blocks
Unfreezes undeployed land block which is frozen.

The dispatch origin for this call must be _Root_.
- `undeployed_land_block_id`: the ID of the undeployed land block that will be unfreezed

Emits `UndeployedLandBlockUnfreezed` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| undeployed_land_block_id | `UndeployedLandBlockId` | 

#### Python
```python
call = substrate.compose_call(
    'Estate', 'unfreeze_undeployed_land_blocks', {'undeployed_land_block_id': 'u128'}
)
```

---------
## Events

---------
### EstateDestroyed
Estate is destroyed [Estate Id, Owner Id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EstateId` | ```u64```
| None | `OwnerId<T::AccountId, ClassId, TokenId>` | ```{'Account': 'AccountId', 'Token': ('u32', 'u64')}```

---------
### EstateLeaseContractCancelled
Estate lease contract was cancelled [Estate Id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EstateId` | ```u64```

---------
### EstateLeaseContractEnded
Estate lease contract ended [Estate Id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EstateId` | ```u64```

---------
### EstateLeaseOfferAccepted
Estate lease offer is accepted [Estate Id, Leasor account Id, Lease End Block]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EstateId` | ```u64```
| None | `T::AccountId` | ```AccountId```
| None | `T::BlockNumber` | ```u32```

---------
### EstateLeaseOfferCreated
Estate lease offer is created [AccountId, Estate Id, Total rent]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `EstateId` | ```u64```
| None | `BalanceOf<T>` | ```u128```

---------
### EstateLeaseOfferRemoved
Estate lease offer is removed [AccountId, Estate Id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `EstateId` | ```u64```

---------
### EstateRentCollected
Estate rent collected [EstateId, Balance]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EstateId` | ```u64```
| None | `BalanceOf<T>` | ```u128```

---------
### EstateUpdated
Estate is updated [Estate Id, Owner Id, Coordinates]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EstateId` | ```u64```
| None | `OwnerId<T::AccountId, ClassId, TokenId>` | ```{'Account': 'AccountId', 'Token': ('u32', 'u64')}```
| None | `Vec<(i32, i32)>` | ```[('i32', 'i32')]```

---------
### LandBlockDeployed
Land block is deployed [From Account Id, Metaverse Id, Undeployed Land Block Id,
Coordinates]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `MetaverseId` | ```u64```
| None | `UndeployedLandBlockId` | ```u128```
| None | `Vec<(i32, i32)>` | ```[('i32', 'i32')]```

---------
### LandUnitAdded
Land unit is added to an estate [Estate Id, Owner Id, Coordinates]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EstateId` | ```u64```
| None | `OwnerId<T::AccountId, ClassId, TokenId>` | ```{'Account': 'AccountId', 'Token': ('u32', 'u64')}```
| None | `Vec<(i32, i32)>` | ```[('i32', 'i32')]```

---------
### LandUnitsRemoved
Land unit is removed from an estate [Estate Id, Owner Id, Coordinates]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EstateId` | ```u64```
| None | `OwnerId<T::AccountId, ClassId, TokenId>` | ```{'Account': 'AccountId', 'Token': ('u32', 'u64')}```
| None | `Vec<(i32, i32)>` | ```[('i32', 'i32')]```

---------
### MaxBoundSet
Max bound is set for a metaverse [Metaverse Id, Min and Max Coordinate]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MetaverseId` | ```u64```
| None | `(i32, i32)` | ```('i32', 'i32')```

---------
### NewEstateMinted
New estate is minted [Estate Id, OwnerId, Metaverse Id, Coordinates]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EstateId` | ```u64```
| None | `OwnerId<T::AccountId, ClassId, TokenId>` | ```{'Account': 'AccountId', 'Token': ('u32', 'u64')}```
| None | `MetaverseId` | ```u64```
| None | `Vec<(i32, i32)>` | ```[('i32', 'i32')]```

---------
### NewLandUnitMinted
New land is minted [Beneficial Account Id, Metaverse Id, Coordinates]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `OwnerId<T::AccountId, ClassId, TokenId>` | ```{'Account': 'AccountId', 'Token': ('u32', 'u64')}```
| None | `MetaverseId` | ```u64```
| None | `(i32, i32)` | ```('i32', 'i32')```

---------
### NewLandsMinted
New lands are minted [Beneficial Account Id, Metaverse Id, Coordinates]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `MetaverseId` | ```u64```
| None | `Vec<(i32, i32)>` | ```[('i32', 'i32')]```

---------
### NewRound
New staking round started [Starting Block, Round, Total Land Unit]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```
| None | `RoundIndex` | ```u32```
| None | `u64` | ```u64```

---------
### TransferredEstate
Estate unit is transferred [Estate Id, From Account Id, To Account Id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EstateId` | ```u64```
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```

---------
### TransferredLandUnit
Land unit is transferred [Metaverse Id, Coordinates, From Account Id, To Account Id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MetaverseId` | ```u64```
| None | `(i32, i32)` | ```('i32', 'i32')```
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```

---------
### UndeployedLandBlockApproved
Undeployed land block is approved [Owner Account Id, Approved Account Id, Undeployed
Land Block Id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `UndeployedLandBlockId` | ```u128```

---------
### UndeployedLandBlockBurnt
Undeployed land block is burnt [Undeployed Land Block Id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `UndeployedLandBlockId` | ```u128```

---------
### UndeployedLandBlockFreezed
Undeployed land block is freezed [Undeployed Land Block Id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `UndeployedLandBlockId` | ```u128```

---------
### UndeployedLandBlockIssued
Undeployed land block is issued [Beneficial Account Id, Undeployed Land
Block Id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `UndeployedLandBlockId` | ```u128```

---------
### UndeployedLandBlockTransferred
Undeployed land block is transferred [From Account Id, To Account Id, Undeployed
Land Block Id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `UndeployedLandBlockId` | ```u128```

---------
### UndeployedLandBlockUnapproved
Undeployed land block is unapproved [Undeployed Land Block Id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `UndeployedLandBlockId` | ```u128```

---------
### UndeployedLandBlockUnfreezed
Undeployed land block is unfreezed [Undeployed Land Block Id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `UndeployedLandBlockId` | ```u128```

---------
## Storage functions

---------
### AllEstatesCount
 Track the total of estates

#### Python
```python
result = substrate.query(
    'Estate', 'AllEstatesCount', []
)
```

#### Return value
```python
'u64'
```
---------
### AllLandUnitsCount
 Track the total number of land units

#### Python
```python
result = substrate.query(
    'Estate', 'AllLandUnitsCount', []
)
```

#### Return value
```python
'u64'
```
---------
### EstateLeaseOffers
 Current estate lease offers

#### Python
```python
result = substrate.query(
    'Estate', 'EstateLeaseOffers', ['u64', 'AccountId']
)
```

#### Return value
```python
{
    'duration': 'u32',
    'end_block': 'u32',
    'price_per_block': 'u128',
    'start_block': 'u32',
    'unclaimed_rent': 'u128',
}
```
---------
### EstateLeases
 Current active estate leases

#### Python
```python
result = substrate.query(
    'Estate', 'EstateLeases', ['u64']
)
```

#### Return value
```python
{
    'duration': 'u32',
    'end_block': 'u32',
    'price_per_block': 'u128',
    'start_block': 'u32',
    'unclaimed_rent': 'u128',
}
```
---------
### EstateLeasors
 Current estate leasors

#### Python
```python
result = substrate.query(
    'Estate', 'EstateLeasors', ['AccountId', 'u64']
)
```

#### Return value
```python
()
```
---------
### EstateOwner
 Track estate owners

#### Python
```python
result = substrate.query(
    'Estate', 'EstateOwner', ['u64']
)
```

#### Return value
```python
{'Account': 'AccountId', 'Token': ('u32', 'u64')}
```
---------
### Estates
 Store estate information

#### Python
```python
result = substrate.query(
    'Estate', 'Estates', ['u64']
)
```

#### Return value
```python
{'land_units': [('i32', 'i32')], 'metaverse_id': 'u64'}
```
---------
### LandUnits
 Index land owners by metaverse ID and coordinate

#### Python
```python
result = substrate.query(
    'Estate', 'LandUnits', ['u64', ('i32', 'i32')]
)
```

#### Return value
```python
{'Account': 'AccountId', 'Token': ('u32', 'u64')}
```
---------
### MintingRateConfig
 Minting rate configuration

#### Python
```python
result = substrate.query(
    'Estate', 'MintingRateConfig', []
)
```

#### Return value
```python
{'annual': 'u64', 'expect': {'ideal': 'u64', 'max': 'u64', 'min': 'u64'}, 'max': 'u64'}
```
---------
### NextEstateId
 Track the next estate ID

#### Python
```python
result = substrate.query(
    'Estate', 'NextEstateId', []
)
```

#### Return value
```python
'u64'
```
---------
### NextUndeployedLandBlockId
 Track the next undeployed land ID

#### Python
```python
result = substrate.query(
    'Estate', 'NextUndeployedLandBlockId', []
)
```

#### Return value
```python
'u128'
```
---------
### Round
 Current round index and next round scheduled transition

#### Python
```python
result = substrate.query(
    'Estate', 'Round', []
)
```

#### Return value
```python
{'current': 'u32', 'first': 'u32', 'length': 'u32'}
```
---------
### TotalUndeployedLandUnit
 Track the total of undeployed land units

#### Python
```python
result = substrate.query(
    'Estate', 'TotalUndeployedLandUnit', []
)
```

#### Return value
```python
'u64'
```
---------
### UndeployedLandBlocks
 Store undeployed land blocks

#### Python
```python
result = substrate.query(
    'Estate', 'UndeployedLandBlocks', ['u128']
)
```

#### Return value
```python
{
    'approved': (None, 'AccountId'),
    'id': 'u128',
    'is_locked': 'bool',
    'number_land_units': 'u32',
    'owner': 'AccountId',
    'undeployed_land_block_type': ('Transferable', 'BoundToAddress'),
}
```
---------
### UndeployedLandBlocksOwner
 Index undeployed land blocks by account ID

#### Python
```python
result = substrate.query(
    'Estate', 'UndeployedLandBlocksOwner', ['AccountId', 'u128']
)
```

#### Return value
```python
()
```
---------
## Constants

---------
### LandTreasury
 Land treasury source
#### Value
```python
'0x6269742f6c616e64'
```
#### Python
```python
constant = substrate.get_constant('Estate', 'LandTreasury')
```
---------
### LeaseOfferExpiryPeriod
 The period for each lease offer will be available for acceptance (in number of blocks)
#### Value
```python
10000
```
#### Python
```python
constant = substrate.get_constant('Estate', 'LeaseOfferExpiryPeriod')
```
---------
### MaxLeasePeriod
 Maximum lease period duration (in number of blocks)
#### Value
```python
1000000
```
#### Python
```python
constant = substrate.get_constant('Estate', 'MaxLeasePeriod')
```
---------
### MaxOffersPerEstate
 Maximum lease offers for an estate
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Estate', 'MaxOffersPerEstate')
```
---------
### MinBlocksPerRound
 Minimum number of blocks per round
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('Estate', 'MinBlocksPerRound')
```
---------
### MinLeasePricePerBlock
 Minimum lease price per block
#### Value
```python
10000000000000000
```
#### Python
```python
constant = substrate.get_constant('Estate', 'MinLeasePricePerBlock')
```
---------
### MinimumStake
 Minimum staking balance
#### Value
```python
100000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Estate', 'MinimumStake')
```
---------
### NetworkFee
 Network fee charged when deploying a land block or creating an estate
#### Value
```python
10000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Estate', 'NetworkFee')
```
---------
### RewardPaymentDelay
 Delay of staking reward payment (in number of rounds)
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('Estate', 'RewardPaymentDelay')
```
---------
## Errors

---------
### AccountHasNoStake
Account has not staked anything

---------
### AlreadyOwnTheEstate
Already owning the estate

---------
### AlreadyOwnTheLandUnit
Already owning the land unit

---------
### AlreadyOwnTheUndeployedLandBlock
Already own the undeployed land block

---------
### BelowMinimumStake
Below minimum staking amount

---------
### CoordinatesForEstateIsNotValid
Coordinate for estate is not valid

---------
### EstateAlreadyInAuction
Estate is already in auction

---------
### EstateDoesNotExist
Estate is does not exist

---------
### EstateIdAlreadyExist
Estate ID already exist

---------
### EstateIsAlreadyLeased
Estate is already leased

---------
### EstateLeaseOffersQueueLimitIsReached
Estate lease offer limit is reached

---------
### EstateNotInAuction
Estate is not in auction

---------
### EstateStakeAlreadyLeft
Estate stake is already left

---------
### InsufficientBalanceForDeployingLandOrCreatingEstate
Insufficient balance for deploying land blocks or creating estates

---------
### InsufficientFund
Insufficient fund

---------
### InvalidOwnerValue
Invalid owner value

---------
### LandUnitAlreadyInAuction
Land unit is already in auction

---------
### LandUnitAlreadyInEstate

---------
### LandUnitDoesNotExist
Land unit does not exist

---------
### LandUnitIsNotAvailable
Land unit is not available

---------
### LandUnitIsOutOfBound
Land unit is out of bound

---------
### LandUnitNotInAuction
Land unit is not in auction

---------
### LeaseDoesNotExist
Lease does not exist

---------
### LeaseIsExpired
Lease is expired

---------
### LeaseIsNotExpired
Lease is not expired

---------
### LeaseOfferAlreadyExists
Lease offer already exists

---------
### LeaseOfferDoesNotExist
Lease offer does not exist

---------
### LeaseOfferDurationAboveMaximum
Lease duration beyond max duration

---------
### LeaseOfferIsNotExpired
Lease offer is not expired

---------
### LeaseOfferPriceBelowMinimum
Lease offer price per block is below the minimum

---------
### NoAvailableEstateId
No available estate ID

---------
### NoPermission
No permission

---------
### NoUnclaimedRentLeft
No unclaimed rent balance

---------
### OnlyFrozenUndeployedLandBlockCanBeDestroyed
Only frozen undeployed land block can be destroyed

---------
### Overflow
Value overflow

---------
### UndeployedLandBlockAlreadyFreezed
Undeployed land block is already freezed

---------
### UndeployedLandBlockAlreadyInAuction
Undeployed land block is already in auction

---------
### UndeployedLandBlockDoesNotHaveEnoughLandUnits
Undeployed land block does not hae enough land units

---------
### UndeployedLandBlockFreezed
Undeployed land block is freezed

---------
### UndeployedLandBlockIsNotTransferable
Undeployed land block is not transferable

---------
### UndeployedLandBlockNotFound
Undeployed land block is not found

---------
### UndeployedLandBlockNotFrozen
Undeployed land block is not frozen

---------
### UndeployedLandBlockNotOwned
Account is not the owner of a given undeployed land block

---------
### UndeployedLandBlockUnitAndInputDoesNotMatch
Number of land block credit and land unit does not match

---------