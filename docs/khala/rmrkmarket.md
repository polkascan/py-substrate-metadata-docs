
# RmrkMarket

---------
## Calls

---------
### accept_offer
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| nft_id | `T::ItemId` | 
| offerer | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkMarket', 'accept_offer', {
    'collection_id': 'u32',
    'nft_id': 'u32',
    'offerer': 'AccountId',
}
)
```

---------
### buy
Buy a listed NFT. Ensure that the NFT is available for purchase and has not recently
been purchased, sent, or burned.

Parameters:
	- `origin` - Account of the potential buyer
	- `collection_id` - Collection id of the RMRK NFT
	- `nft_id` - NFT id of the RMRK NFT
	- `amount` - Optional price at which buyer purchased at
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| nft_id | `T::ItemId` | 
| amount | `Option<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkMarket', 'buy', {
    'amount': (None, 'u128'),
    'collection_id': 'u32',
    'nft_id': 'u32',
}
)
```

---------
### list
List a RMRK NFT on the Marketplace for purchase. A listing can be cancelled, and is
automatically considered cancelled when a `buy` is executed on top of a given listing.
An NFT that has another NFT as its owner CANNOT be listed. An NFT owned by a NFT must
first be sent to an account before being listed.

Parameters:
	- `origin` - Account of owner of the RMRK NFT to be listed
	- `collection_id` - Collection id of the RMRK NFT
	- `nft_id` - NFT id of the RMRK NFT
	- `amount` - Price of the RMRK NFT
	- `expires` - Optional BlockNumber for when the listing expires
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| nft_id | `T::ItemId` | 
| amount | `BalanceOf<T>` | 
| expires | `Option<T::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkMarket', 'list', {
    'amount': 'u128',
    'collection_id': 'u32',
    'expires': (None, 'u32'),
    'nft_id': 'u32',
}
)
```

---------
### make_offer
Make an offer on a RMRK NFT for purchase. An offer can be set with an expiration where
the offer can no longer be accepted by the RMRK NFT owner

Parameters:
- `origin` - Account of the potential buyer
- `collection_id` - Collection id of the RMRK NFT
- `nft_id` - NFT id of the RMRK NFT
- `amount` - Price of the RMRK NFT
- `expiration` - Expiration of the offer
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| nft_id | `T::ItemId` | 
| amount | `BalanceOf<T>` | 
| expires | `Option<T::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkMarket', 'make_offer', {
    'amount': 'u128',
    'collection_id': 'u32',
    'expires': (None, 'u32'),
    'nft_id': 'u32',
}
)
```

---------
### unlist
Unlist a RMRK NFT on the Marketplace and remove from storage in `Listings`.

Parameters:
- `origin` - Account owner of the listed RMRK NFT
- `collection_id` - Collection id of the RMRK NFT
- `nft_id` - NFT id of the RMRK NFT
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| nft_id | `T::ItemId` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkMarket', 'unlist', {
    'collection_id': 'u32',
    'nft_id': 'u32',
}
)
```

---------
### withdraw_offer
Withdraw an offer on a RMRK NFT, such that it is no longer available to be accepted by
the NFT owner

Parameters:
- `origin` - Account that wants to withdraw their offer
- `collection_id` - Collection id of the RMRK NFT
- `nft_id` - NFT id of the RMRK NFT
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| nft_id | `T::ItemId` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkMarket', 'withdraw_offer', {
    'collection_id': 'u32',
    'nft_id': 'u32',
}
)
```

---------
## Events

---------
### OfferAccepted
Offer was accepted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| buyer | `T::AccountId` | ```AccountId```
| collection_id | `T::CollectionId` | ```u32```
| nft_id | `T::ItemId` | ```u32```

---------
### OfferPlaced
Offer was placed on a token
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| offerer | `T::AccountId` | ```AccountId```
| collection_id | `T::CollectionId` | ```u32```
| nft_id | `T::ItemId` | ```u32```
| price | `BalanceOf<T>` | ```u128```

---------
### OfferWithdrawn
Offer was withdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| collection_id | `T::CollectionId` | ```u32```
| nft_id | `T::ItemId` | ```u32```

---------
### TokenListed
Token listed on Marketplace
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| collection_id | `T::CollectionId` | ```u32```
| nft_id | `T::ItemId` | ```u32```
| price | `BalanceOf<T>` | ```u128```

---------
### TokenPriceUpdated
The price for a token was updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| collection_id | `T::CollectionId` | ```u32```
| nft_id | `T::ItemId` | ```u32```
| price | `Option<BalanceOf<T>>` | ```(None, 'u128')```

---------
### TokenSold
Token was sold to a new owner
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| buyer | `T::AccountId` | ```AccountId```
| collection_id | `T::CollectionId` | ```u32```
| nft_id | `T::ItemId` | ```u32```
| price | `BalanceOf<T>` | ```u128```

---------
### TokenUnlisted
Token unlisted on Marketplace
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| collection_id | `T::CollectionId` | ```u32```
| nft_id | `T::ItemId` | ```u32```

---------
## Storage functions

---------
### ListedNfts
 Stores listed NFT price info

#### Python
```python
result = substrate.query(
    'RmrkMarket', 'ListedNfts', ['u32', 'u32']
)
```

#### Return value
```python
{'amount': 'u128', 'expires': (None, 'u32'), 'listed_by': 'AccountId'}
```
---------
### Offers
 Stores offer on a NFT info

#### Python
```python
result = substrate.query(
    'RmrkMarket', 'Offers', [('u32', 'u32'), 'AccountId']
)
```

#### Return value
```python
{'amount': 'u128', 'expires': (None, 'u32'), 'maker': 'AccountId'}
```
---------
## Constants

---------
### MinimumOfferAmount
 Minimum offer amount as a valid offer
#### Value
```python
100000000
```
#### Python
```python
constant = substrate.get_constant('RmrkMarket', 'MinimumOfferAmount')
```
---------
## Errors

---------
### AlreadyOffered
Account cannot offer on a NFT again with an active offer

---------
### CannotBuyOwnToken
Cannot buy NFT that is already owned

---------
### CannotListNftOwnedByNft
Cannot list NFT owned by a NFT

---------
### CannotOfferOnOwnToken
Cannot make offer on NFT on own NFT

---------
### CannotUnlistToken
Cannot unlist NFT as it has already been unlisted or sold

---------
### CannotWithdrawOffer
Offer already accepted and cannot withdraw

---------
### ListingHasExpired
Listing has expired and cannot be bought

---------
### NoPermission
No permissions for account to interact with NFT

---------
### NonTransferable
Not possible to list non-transferable NFT

---------
### OfferHasExpired
Accepted offer has expired and cannot be accepted

---------
### OfferTooLow
Offer is below the OfferMinimumAmount threshold

---------
### PriceDiffersFromExpected
Price differs from when `buy` was executed

---------
### TokenDoesNotExist
Cannot list a non-existing NFT

---------
### TokenNotForSale
Token cannot be bought

---------
### UnknownOffer
Offer is unknown

---------