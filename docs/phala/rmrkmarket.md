
# RmrkMarket

---------
## Calls

---------
### accept_offer
See [`Pallet::accept_offer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| nft_id | `ItemIdOf<T>` | 
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
See [`Pallet::buy`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| nft_id | `ItemIdOf<T>` | 
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
See [`Pallet::list`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| nft_id | `ItemIdOf<T>` | 
| amount | `BalanceOf<T>` | 
| expires | `Option<BlockNumberFor<T>>` | 

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
See [`Pallet::make_offer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| nft_id | `ItemIdOf<T>` | 
| amount | `BalanceOf<T>` | 
| expires | `Option<BlockNumberFor<T>>` | 

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
See [`Pallet::unlist`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| nft_id | `ItemIdOf<T>` | 

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
See [`Pallet::withdraw_offer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| nft_id | `ItemIdOf<T>` | 

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
### MarketFeePaid
Market fee paid to marketplace owner
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| marketplace_owner | `T::AccountId` | ```AccountId```
| collection_id | `CollectionIdOf<T>` | ```u32```
| nft_id | `ItemIdOf<T>` | ```u32```
| amount | `BalanceOf<T>` | ```u128```

---------
### OfferAccepted
Offer was accepted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| buyer | `T::AccountId` | ```AccountId```
| collection_id | `CollectionIdOf<T>` | ```u32```
| nft_id | `ItemIdOf<T>` | ```u32```

---------
### OfferPlaced
Offer was placed on a token
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| offerer | `T::AccountId` | ```AccountId```
| collection_id | `CollectionIdOf<T>` | ```u32```
| nft_id | `ItemIdOf<T>` | ```u32```
| price | `BalanceOf<T>` | ```u128```

---------
### OfferWithdrawn
Offer was withdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| collection_id | `CollectionIdOf<T>` | ```u32```
| nft_id | `ItemIdOf<T>` | ```u32```

---------
### RoyaltyFeePaid
Royalty fee paid to royalty owner
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| royalty_owner | `T::AccountId` | ```AccountId```
| collection_id | `CollectionIdOf<T>` | ```u32```
| nft_id | `ItemIdOf<T>` | ```u32```
| amount | `BalanceOf<T>` | ```u128```

---------
### TokenListed
Token listed on Marketplace
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| collection_id | `CollectionIdOf<T>` | ```u32```
| nft_id | `ItemIdOf<T>` | ```u32```
| price | `BalanceOf<T>` | ```u128```

---------
### TokenPriceUpdated
The price for a token was updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| collection_id | `CollectionIdOf<T>` | ```u32```
| nft_id | `ItemIdOf<T>` | ```u32```
| price | `Option<BalanceOf<T>>` | ```(None, 'u128')```

---------
### TokenSold
Token was sold to a new owner
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| buyer | `T::AccountId` | ```AccountId```
| collection_id | `CollectionIdOf<T>` | ```u32```
| nft_id | `ItemIdOf<T>` | ```u32```
| price | `BalanceOf<T>` | ```u128```

---------
### TokenUnlisted
Token unlisted on Marketplace
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| collection_id | `CollectionIdOf<T>` | ```u32```
| nft_id | `ItemIdOf<T>` | ```u32```

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
### MarketplaceOwner
 Stores the marketplace owner account

#### Python
```python
result = substrate.query(
    'RmrkMarket', 'MarketplaceOwner', []
)
```

#### Return value
```python
'AccountId'
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
### MarketFee
 Market fee to be implemented downstream.
#### Value
```python
5000
```
#### Python
```python
constant = substrate.get_constant('RmrkMarket', 'MarketFee')
```
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
### CannotListNft
Cannot list NFT based on downstream logic implemented for MarketplaceHooks trait

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
### MarketplaceOwnerNotSet
Marketplace owner not configured

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