
# Continuum

---------
## Calls

---------
### bid_map_spot
Bid continuum slot with price
#### Attributes
| Name | Type |
| -------- | -------- | 
| auction_id | `AuctionId` | 
| value | `BalanceOf<T>` | 
| metaverse_id | `MetaverseId` | 

#### Python
```python
call = substrate.compose_call(
    'Continuum', 'bid_map_spot', {
    'auction_id': 'u64',
    'metaverse_id': 'u64',
    'value': 'u128',
}
)
```

---------
### buy_map_spot
Buy continuum slot with fixed price
#### Attributes
| Name | Type |
| -------- | -------- | 
| auction_id | `AuctionId` | 
| value | `BalanceOf<T>` | 
| metaverse_id | `MetaverseId` | 

#### Python
```python
call = substrate.compose_call(
    'Continuum', 'buy_map_spot', {
    'auction_id': 'u64',
    'metaverse_id': 'u64',
    'value': 'u128',
}
)
```

---------
### create_new_auction
Create new map auction
#### Attributes
| Name | Type |
| -------- | -------- | 
| spot_id | `MapSpotId` | 
| auction_type | `AuctionType` | 
| value | `BalanceOf<T>` | 
| end_time | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Continuum', 'create_new_auction', {
    'auction_type': (
        'Auction',
        'BuyNow',
    ),
    'end_time': 'u32',
    'spot_id': ('i32', 'i32'),
    'value': 'u128',
}
)
```

---------
### issue_map_slot
Issue new map slot
#### Attributes
| Name | Type |
| -------- | -------- | 
| coordinate | `(i32, i32)` | 
| slot_type | `TokenType` | 

#### Python
```python
call = substrate.compose_call(
    'Continuum', 'issue_map_slot', {
    'coordinate': ('i32', 'i32'),
    'slot_type': (
        'Transferable',
        'BoundToAddress',
    ),
}
)
```

---------
### set_allow_buy_now
Whether council enable buy now option
#### Attributes
| Name | Type |
| -------- | -------- | 
| enable | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Continuum', 'set_allow_buy_now', {'enable': 'bool'}
)
```

---------
### set_max_bounds
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_bound | `(i32, i32)` | 

#### Python
```python
call = substrate.compose_call(
    'Continuum', 'set_max_bounds', {'new_bound': ('i32', 'i32')}
)
```

---------
## Events

---------
### ContinuumEmergencyShutdownEnabled
Emergency shutdown is on
#### Attributes
No attributes

---------
### ContinuumSpotTransferred
Spot transferred
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `MapSpotId` | ```('i32', 'i32')```

---------
### FinalizedVote
Finalize vote
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SpotId` | ```u64```

---------
### NewAuctionSlotRotated
Rotated new auction slot
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```

---------
### NewContinuumNeighbourHoodProtocolStarted
Start new good neighbourhood protocol round
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```
| None | `SpotId` | ```u64```

---------
### NewContinuumReferendumStarted
Start new referendum
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```
| None | `SpotId` | ```u64```

---------
### NewExpressOfInterestAdded
New express of interest
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `SpotId` | ```u64```

---------
### NewMapSpotIssued
New Map Spot issued
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MapSpotId` | ```('i32', 'i32')```
| None | `T::AccountId` | ```AccountId```

---------
### NewMaxAuctionSlotSet
New max auction slot set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u8` | ```u8```

---------
### NewMaxBoundSet
New max bound set on continuum map
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `(i32, i32)` | ```('i32', 'i32')```

---------
## Storage functions

---------
### AllowBuyNow

#### Python
```python
result = substrate.query(
    'Continuum', 'AllowBuyNow', []
)
```

#### Return value
```python
'bool'
```
---------
### ContinuumCoordinates
 Continuum Spot Position

#### Python
```python
result = substrate.query(
    'Continuum', 'ContinuumCoordinates', [('i32', 'i32')]
)
```

#### Return value
```python
'u64'
```
---------
### ContinuumSpots
 Continuum Spot

#### Python
```python
result = substrate.query(
    'Continuum', 'ContinuumSpots', ['u64']
)
```

#### Return value
```python
{'metaverse_id': 'u64', 'x': 'i32', 'y': 'i32'}
```
---------
### MapSpotOwner

#### Python
```python
result = substrate.query(
    'Continuum', 'MapSpotOwner', [('i32', 'i32')]
)
```

#### Return value
```python
'AccountId'
```
---------
### MapSpots

#### Python
```python
result = substrate.query(
    'Continuum', 'MapSpots', [('i32', 'i32')]
)
```

#### Return value
```python
{
    'metaverse_id': (None, 'u64'),
    'owner': 'AccountId',
    'slot_type': ('Transferable', 'BoundToAddress'),
}
```
---------
### MaxBound
 Get max bound

#### Python
```python
result = substrate.query(
    'Continuum', 'MaxBound', []
)
```

#### Return value
```python
('i32', 'i32')
```
---------
### MetaverseLeadingBid

#### Python
```python
result = substrate.query(
    'Continuum', 'MetaverseLeadingBid', [('i32', 'i32'), 'u64']
)
```

#### Return value
```python
()
```
---------
### MetaverseMap

#### Python
```python
result = substrate.query(
    'Continuum', 'MetaverseMap', ['u64']
)
```

#### Return value
```python
('i32', 'i32')
```
---------
### NextContinuumSpotId

#### Python
```python
result = substrate.query(
    'Continuum', 'NextContinuumSpotId', []
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### AuctionDuration
 Auction duration
#### Value
```python
43200
```
#### Python
```python
constant = substrate.get_constant('Continuum', 'AuctionDuration')
```
---------
### ContinuumTreasury
 Continuum Treasury
#### Value
```python
'0x6269742f74727379'
```
#### Python
```python
constant = substrate.get_constant('Continuum', 'ContinuumTreasury')
```
---------
### SessionDuration
 New Slot Duration
 How long the new auction slot will be released. If set to zero, no new auctions are
 generated
#### Value
```python
43200
```
#### Python
```python
constant = substrate.get_constant('Continuum', 'SessionDuration')
```
---------
### SpotAuctionChillingDuration
 Auction Slot Chilling Duration
 How long the participates in the New Auction Slots will get confirmed by neighbours
#### Value
```python
43200
```
#### Python
```python
constant = substrate.get_constant('Continuum', 'SpotAuctionChillingDuration')
```
---------
## Errors

---------
### AlreadyShutdown
Already shutdown

---------
### ContinuumBuyNowIsDisabled
Continuum Buynow is disable

---------
### EOIAlreadyExists
Only send EOI once

---------
### FailedEOIToSlot
Can&\#x27;t add EOI to Slot

---------
### InsufficientFund
Insufficient fund to buy

---------
### InvalidSpotAuction
Auction is not for map spot or does not exists

---------
### MapSpotAlreadyExits
Map slot already exists

---------
### MapSpotNotFound
Map Spot is not found

---------
### MetaverseAlreadyGotSpot
Metaverse already secured the spot

---------
### MetaverseHasBidLeading
Metaverse already leading bid of a spot. One leading bid per metaverse.

---------
### MetaverseHasNotDeployedAnyLand
Metaverse has no deployed land.

---------
### NoActiveAuctionSlot
No Active Auction Slot

---------
### NoActiveGNP
No Active GNP List

---------
### NoActiveReferendum
No Active Referendum

---------
### NoActiveSession
No Active Session

---------
### NoPermission
No permission

---------
### NotMetaverseOwner
You are not the owner of the metaverse

---------
### ReferendumIsInValid
Referendum is invalid

---------
### SpotIsInAuction
Continuum Spot is in auction

---------
### SpotIsNotAvailable
Spot Owned

---------
### SpotIsOutOfBound
Spot is out of bound

---------
### SpotNotFound
Spot Not Found

---------
### TallyOverflow
Tally Overflow

---------