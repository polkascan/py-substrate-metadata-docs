
# Auction

---------
## Calls

---------
### accept_offer
Accept offer for an NFT asset

The dispatch origin for this call must be _Signed_.
Only NFT owner can make this call.
- `asset`: the NFT for which te offer will be accepted.
- `offeror`: the account whose offer will be accepted.

Emits `NftOfferAccepted` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `(ClassId, TokenId)` | 
| offeror | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Auction', 'accept_offer', {'asset': ('u32', 'u64'), 'offeror': 'AccountId'}
)
```

---------
### authorise_metaverse_collection
Metaverse owner can authorize collection that sell in their local marketplace

The dispatch origin for this call must be _Signed_. Only owner of metaverse can make
this call
- `class_id`: the nft collection that want to authorize
- `metaverse_id`: the metaverse id that user want to authorize

Emits `CollectionAuthorizedInMetaverse` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| class_id | `ClassId` | 
| metaverse_id | `MetaverseId` | 

#### Python
```python
call = substrate.compose_call(
    'Auction', 'authorise_metaverse_collection', {
    'class_id': 'u32',
    'metaverse_id': 'u64',
}
)
```

---------
### bid
User bid for any available auction.

The dispatch origin for this call must be _Signed_.
`id`: auction id that user wants to bid
`value`: the value of the bid
Fund will be reserved if bid accepted and release the fund of previous bidder at the
same time


Emits `Bid` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `AuctionId` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Auction', 'bid', {'id': 'u64', 'value': 'u128'}
)
```

---------
### buy_now
User buy for any available buy now listing.

The dispatch origin for this call must be _Signed_.
`auction_id`: the id of auction that user want to bid
`value`: the bid value
Fund will be transfer immediately if buy now price is accepted and asset will be
transferred to sender


Emits `BuyNowFinalised` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| auction_id | `AuctionId` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Auction', 'buy_now', {'auction_id': 'u64', 'value': 'u128'}
)
```

---------
### cancel_listing
Cancel listing that has no bid or buy now.

The dispatch origin for this call must be _Root_.
this call
- `auction_id`: the auction id that wish to cancel

Emits `AuctionCancelled` and  `AuctionFinalizedNoBid` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| auction_id | `AuctionId` | 

#### Python
```python
call = substrate.compose_call(
    'Auction', 'cancel_listing', {'auction_id': 'u64'}
)
```

---------
### create_new_auction
User create new auction listing if they are metaverse owner of their local marketplace
or NFT collection has authorized to list

The dispatch origin for this call must be _Signed_.
- `item_id`: he enum of what item type want to list
- `value`: value of the listing
- `listing_level`: if listing is on local or global marketplace
- `end_time`: the listing end time.

Emits `NewAuctionItem` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| item_id | `ItemId<BalanceOf<T>>` | 
| value | `BalanceOf<T>` | 
| end_time | `T::BlockNumber` | 
| listing_level | `ListingLevel<T::AccountId>` | 
| currency_id | `FungibleTokenId` | 

#### Python
```python
call = substrate.compose_call(
    'Auction', 'create_new_auction', {
    'currency_id': {
        'DEXShare': ('u64', 'u64'),
        'FungibleToken': 'u64',
        'MiningResource': 'u64',
        'NativeToken': 'u64',
        'Stable': 'u64',
    },
    'end_time': 'u32',
    'item_id': {
        'Block': 'u64',
        'Bundle': [
            ('u32', 'u64', 'u128'),
        ],
        'Estate': 'u64',
        'LandUnit': (('i32', 'i32'), 'u64'),
        'Metaverse': 'u64',
        'NFT': ('u32', 'u64'),
        'Spot': (('i32', 'i32'), 'u64'),
        'UndeployedLandBlock': 'u128',
    },
    'listing_level': {
        'Global': None,
        'Local': 'u64',
        'NetworkSpot': ['AccountId'],
    },
    'value': 'u128',
}
)
```

---------
### create_new_buy_now
User create new buy-now&\#x27;s listing if they are metaverse owner of their local marketplace
or NFT collection has authorized to list

The dispatch origin for this call must be _Signed_.
- `item_id`: the enum of what item type want to list
- `value`: value of the listing
- `listing_level`: if listing is on local or global marketplace
- `end_time`: the listing end time.

Emits `NewAuctionItem` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| item_id | `ItemId<BalanceOf<T>>` | 
| value | `BalanceOf<T>` | 
| end_time | `T::BlockNumber` | 
| listing_level | `ListingLevel<T::AccountId>` | 
| currency_id | `FungibleTokenId` | 

#### Python
```python
call = substrate.compose_call(
    'Auction', 'create_new_buy_now', {
    'currency_id': {
        'DEXShare': ('u64', 'u64'),
        'FungibleToken': 'u64',
        'MiningResource': 'u64',
        'NativeToken': 'u64',
        'Stable': 'u64',
    },
    'end_time': 'u32',
    'item_id': {
        'Block': 'u64',
        'Bundle': [
            ('u32', 'u64', 'u128'),
        ],
        'Estate': 'u64',
        'LandUnit': (('i32', 'i32'), 'u64'),
        'Metaverse': 'u64',
        'NFT': ('u32', 'u64'),
        'Spot': (('i32', 'i32'), 'u64'),
        'UndeployedLandBlock': 'u128',
    },
    'listing_level': {
        'Global': None,
        'Local': 'u64',
        'NetworkSpot': ['AccountId'],
    },
    'value': 'u128',
}
)
```

---------
### finalize_auction
Manually finalize ended auction.

The dispatch origin for this call must be _Signed_.
- `auction_id`: the ID of the auction that will be finalized.

Emits `AuctionFinalized` or `AuctionFinalizedNoBid` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| auction_id | `AuctionId` | 

#### Python
```python
call = substrate.compose_call(
    'Auction', 'finalize_auction', {'auction_id': 'u64'}
)
```

---------
### make_offer
Make offer for an NFT asset

The dispatch origin for this call must be _Signed_.
Only accounts that does not own the NFT asset can make this call
- `asset`: the NFT for which an offer will be made.
- `offer_amount`: the  amount of native tokens offered in exchange of the nft.

Emits `NftOfferMade` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `(ClassId, TokenId)` | 
| offer_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Auction', 'make_offer', {'asset': ('u32', 'u64'), 'offer_amount': 'u128'}
)
```

---------
### remove_authorise_metaverse_collection
Metaverse owner can remove authorized collection that sell in their local marketplace

The dispatch origin for this call must be _Signed_. Only owner of metaverse can make
this call
- `class_id`: the nft collection that want to authorize
- `metaverse_id`: the metaverse id that user want to authorize

Emits `CollectionAuthorizationRemoveInMetaverse` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| class_id | `ClassId` | 
| metaverse_id | `MetaverseId` | 

#### Python
```python
call = substrate.compose_call(
    'Auction', 'remove_authorise_metaverse_collection', {
    'class_id': 'u32',
    'metaverse_id': 'u64',
}
)
```

---------
### withdraw_offer
Withdraw offer for an NFT asset

The dispatch origin for this call must be _Signed_.
Only account which have already made an offer for the given NFT can make this call.
- `asset`: the NFT for which te offer will be withdrawn

Emits `NftOfferWithdrawn` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `(ClassId, TokenId)` | 

#### Python
```python
call = substrate.compose_call(
    'Auction', 'withdraw_offer', {'asset': ('u32', 'u64')}
)
```

---------
## Events

---------
### AuctionCancelled
Cancel listing with auction id. [class_id,
metaverse_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AuctionId` | ```u64```

---------
### AuctionExtended
Auction extended. [auction_id, end_block]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AuctionId` | ```u64```
| None | `T::BlockNumber` | ```u32```

---------
### AuctionFinalized
Auction finalized. [auction_id, bidder, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AuctionId` | ```u64```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### AuctionFinalizedNoBid
Listing finalized with no bid. [auction_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AuctionId` | ```u64```

---------
### Bid
A bid is placed. [auction_id, bidder, bidding_amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AuctionId` | ```u64```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### BuyNowFinalised
Buy finalized. [auction_id, bidder, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AuctionId` | ```u64```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### CollectionAuthorizationRemoveInMetaverse
NFT Collection authorization removed for listing in marketplace. [class_id,
metaverse_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ClassId` | ```u32```
| None | `MetaverseId` | ```u64```

---------
### CollectionAuthorizedInMetaverse
NFT Collection authorized for listing in marketplace. [class_id, metaverse_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ClassId` | ```u32```
| None | `MetaverseId` | ```u64```

---------
### NewAuctionItem
New auction item created. [auction_id, bidder, listing_level, initial_amount,
initial_amount, end_block]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AuctionId` | ```u64```
| None | `T::AccountId` | ```AccountId```
| None | `ListingLevel<T::AccountId>` | ```{'NetworkSpot': ['AccountId'], 'Global': None, 'Local': 'u64'}```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```
| None | `T::BlockNumber` | ```u32```

---------
### NftOfferAccepted
Nft offer is accepted [class_id, token_id, account_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ClassId` | ```u32```
| None | `TokenId` | ```u64```
| None | `T::AccountId` | ```AccountId```

---------
### NftOfferMade
Nft offer is made [class_id, token_id, account_id, offer amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ClassId` | ```u32```
| None | `TokenId` | ```u64```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### NftOfferWithdrawn
Nft offer is withdrawn [class_id, token_id, account_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ClassId` | ```u32```
| None | `TokenId` | ```u64```
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### AuctionEndTime
 Index auctions by end time.

#### Python
```python
result = substrate.query(
    'Auction', 'AuctionEndTime', ['u32', 'u64']
)
```

#### Return value
```python
()
```
---------
### AuctionItems
 Store asset with Auction

#### Python
```python
result = substrate.query(
    'Auction', 'AuctionItems', ['u64']
)
```

#### Return value
```python
{
    'amount': 'u128',
    'auction_type': ('Auction', 'BuyNow'),
    'currency_id': {
        'DEXShare': ('u64', 'u64'),
        'FungibleToken': 'u64',
        'MiningResource': 'u64',
        'NativeToken': 'u64',
        'Stable': 'u64',
    },
    'end_time': 'u32',
    'initial_amount': 'u128',
    'item_id': {
        'Block': 'u64',
        'Bundle': [('u32', 'u64', 'u128')],
        'Estate': 'u64',
        'LandUnit': (('i32', 'i32'), 'u64'),
        'Metaverse': 'u64',
        'NFT': ('u32', 'u64'),
        'Spot': (('i32', 'i32'), 'u64'),
        'UndeployedLandBlock': 'u128',
    },
    'listing_fee': 'u32',
    'listing_level': {
        'Global': None,
        'Local': 'u64',
        'NetworkSpot': ['AccountId'],
    },
    'recipient': 'AccountId',
    'start_time': 'u32',
}
```
---------
### Auctions
 Stores on-going and future auctions. Closed auction are removed.

#### Python
```python
result = substrate.query(
    'Auction', 'Auctions', ['u64']
)
```

#### Return value
```python
{'bid': (None, ('AccountId', 'u128')), 'end': (None, 'u32'), 'start': 'u32'}
```
---------
### AuctionsIndex
 Track the next auction ID.

#### Python
```python
result = substrate.query(
    'Auction', 'AuctionsIndex', []
)
```

#### Return value
```python
'u64'
```
---------
### ItemsInAuction
 Track which Assets are in auction

#### Python
```python
result = substrate.query(
    'Auction', 'ItemsInAuction', [
    {
        'Block': 'u64',
        'Bundle': [
            ('u32', 'u64', 'u128'),
        ],
        'Estate': 'u64',
        'LandUnit': (('i32', 'i32'), 'u64'),
        'Metaverse': 'u64',
        'NFT': ('u32', 'u64'),
        'Spot': (('i32', 'i32'), 'u64'),
        'UndeployedLandBlock': 'u128',
    },
]
)
```

#### Return value
```python
'bool'
```
---------
### MetaverseCollection
 Local marketplace collection authorisation

#### Python
```python
result = substrate.query(
    'Auction', 'MetaverseCollection', ['u64', 'u32']
)
```

#### Return value
```python
()
```
---------
### Offers
 Index NFT offers by token and oferror

#### Python
```python
result = substrate.query(
    'Auction', 'Offers', [('u32', 'u64'), 'AccountId']
)
```

#### Return value
```python
{'amount': 'u128', 'end_block': 'u32'}
```
---------
## Constants

---------
### AntiSnipeDuration
 Anti-snipe duration
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('Auction', 'AntiSnipeDuration')
```
---------
### AuctionTimeToClose
 Default auction close time if there is no end time specified
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Auction', 'AuctionTimeToClose')
```
---------
### MaxBundleItem
 Max number of items in bundle can be finalised in an auction
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Auction', 'MaxBundleItem')
```
---------
### MaxFinality
 Max number of listing can be finalised in a single block
#### Value
```python
200
```
#### Python
```python
constant = substrate.get_constant('Auction', 'MaxFinality')
```
---------
### MinimumAuctionDuration
 Minimum auction duration when new listing created.
#### Value
```python
300
```
#### Python
```python
constant = substrate.get_constant('Auction', 'MinimumAuctionDuration')
```
---------
### MinimumListingPrice
 Minimum listing price
#### Value
```python
1000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Auction', 'MinimumListingPrice')
```
---------
### NetworkFeeCommission
 Network fee that will be collected when auction or buy now is completed.
#### Value
```python
10000000
```
#### Python
```python
constant = substrate.get_constant('Auction', 'NetworkFeeCommission')
```
---------
### NetworkFeeReserve
 Network fee that will be reserved when an item is listed for auction or buy now.
 The fee will be unreserved after the auction or buy now is completed.
#### Value
```python
1000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Auction', 'NetworkFeeReserve')
```
---------
### OfferDuration
 Offer duration
#### Value
```python
100800
```
#### Python
```python
constant = substrate.get_constant('Auction', 'OfferDuration')
```
---------
## Errors

---------
### AssetDoesNotExist
Asset for listing does not exist

---------
### AuctionAlreadyStartedOrBid
Auction already started or got bid

---------
### AuctionDoesNotExist
Auction does not exist

---------
### AuctionEndIsLessThanMinimumDuration
Minimum Duration Is Too Low

---------
### AuctionHasNotStarted
Auction has not started

---------
### AuctionIsExpired
Auction is expired

---------
### AuctionIsNotExpired
Auction is  not expired

---------
### AuctionTypeIsNotSupported
Auction type is supported for listing

---------
### BidIsNotAccepted
Bid is not accepted e.g owner == bidder, listing stop accepting bid

---------
### CannotBidOnOwnAuction
Self bidding is not accepted

---------
### CollectionAlreadyAuthorised
Collection has already authorised

---------
### CollectionIsNotAuthorised
Collection is not authorised

---------
### EstateDoesNotExist
Estate does not exist, check if estate id is correct

---------
### ExceedBundleLimit
There is too many item inside the bundle.

---------
### ExceedFinalityLimit
There is too many auction ends at the same time.

---------
### FungibleTokenCurrencyNotFound
Social Token Currency is not exist

---------
### InsufficientFreeBalance
Insufficient free balance for bidding

---------
### InvalidAuctionType
Invalid auction type

---------
### InvalidBidPrice
Bid price is invalid

---------
### InvalidBuyNowPrice
Buy now input price is not valid

---------
### ItemAlreadyInAuction
Asset already in Auction

---------
### LandUnitDoesNotExist
Land unit does not exist, check if estate id is correct

---------
### ListingPriceIsBelowMinimum
Listing price is below the minimum.

---------
### MetaverseOwnerOnly
Only metaverse owner can participate

---------
### NoAvailableAuctionId
Auction is not found, either expired and not valid

---------
### NoPermissionToAcceptOffer
No permission to accept offer for a NFT.

---------
### NoPermissionToAuthoriseCollection
User has no permission to authorise collection

---------
### NoPermissionToCancelAuction
Has no permission to cancel auction.

---------
### NoPermissionToCreateAuction
Has no permission to create auction. Check listing authorization

---------
### NoPermissionToFinalizeAuction
No permission to finalize auction

---------
### NoPermissionToMakeOffer
No permission to make offer for a NFT.

---------
### OfferAlreadyExists
The account has already made offer for a given NFT

---------
### OfferDoesNotExist
The NFT offer does not exist

---------
### OfferIsExpired
The NFT offer is expired

---------
### UndeployedLandBlockDoesNotExistOrNotAvailable
Undeployed land block does not exist or is not available for auction

---------
### WrongListingLevel
Wrong Listing Level

---------