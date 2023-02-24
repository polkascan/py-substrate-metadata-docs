
# Marketplace

---------
## Calls

---------
### accept_offer
Accept an offer and process the trade

Parameters:
- `collection_id`: The identifier of a non-fungible token collection
- `item_id`: The item identifier of a collection
- `maker`: User who made the offer
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::NftCollectionId` | 
| item_id | `T::NftItemId` | 
| maker | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Marketplace', 'accept_offer', {
    'collection_id': 'u128',
    'item_id': 'u128',
    'maker': 'AccountId',
}
)
```

---------
### add_royalty
Add royalty feature where a cut for author is provided
There is non-refundable reserve held for creating a royalty

Parameters:
- `collection_id`: The collection of the asset to be minted.
- `item_id`: The item value of the asset to be minted.
- `author`: Receiver of the royalty
- `royalty`: Percentage reward from each trade for the author, represented in basis points
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::NftCollectionId` | 
| item_id | `T::NftItemId` | 
| author | `T::AccountId` | 
| royalty | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'Marketplace', 'add_royalty', {
    'author': 'AccountId',
    'collection_id': 'u128',
    'item_id': 'u128',
    'royalty': 'u16',
}
)
```

---------
### buy
Pays a price to the current owner
Transfers NFT ownership to the buyer
Disables automatic sell of the NFT

Parameters:
- `collection_id`: The identifier of a non-fungible token collection
- `item_id`: The item identifier of a collection
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::NftCollectionId` | 
| item_id | `T::NftItemId` | 

#### Python
```python
call = substrate.compose_call(
    'Marketplace', 'buy', {
    'collection_id': 'u128',
    'item_id': 'u128',
}
)
```

---------
### make_offer
Users can indicate what price they would be willing to pay for a token
Price can be lower than current listing price
Token doesn&\#x27;t have to be currently listed

Parameters:
- `collection_id`: The identifier of a non-fungible token collection
- `item_id`: The item identifier of a collection
- `amount`: The amount user is willing to pay
- `expires`: The block until the current owner can accept the offer
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::NftCollectionId` | 
| item_id | `T::NftItemId` | 
| amount | `BalanceOf<T>` | 
| expires | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Marketplace', 'make_offer', {
    'amount': 'u128',
    'collection_id': 'u128',
    'expires': 'u32',
    'item_id': 'u128',
}
)
```

---------
### set_price
Set trading price and allow sell
Setting price to None disables auto sell

Parameters:
- `collection_id`: The identifier of a non-fungible token collection
- `item_id`: The item identifier of a collection
- `new_price`: price the token will be listed for
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::NftCollectionId` | 
| item_id | `T::NftItemId` | 
| new_price | `Option<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Marketplace', 'set_price', {
    'collection_id': 'u128',
    'item_id': 'u128',
    'new_price': (None, 'u128'),
}
)
```

---------
### withdraw_offer
Reverse action to make_offer
Removes an offer and unreserves funds
Can be done by the offer maker or owner of the token

Parameters:
- `collection_id`: The identifier of a non-fungible token collection
- `item_id`: The item identifier of a collection
- `maker`: User who made the offer
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::NftCollectionId` | 
| item_id | `T::NftItemId` | 
| maker | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Marketplace', 'withdraw_offer', {
    'collection_id': 'u128',
    'item_id': 'u128',
    'maker': 'AccountId',
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
| who | `T::AccountId` | ```AccountId```
| collection | `T::NftCollectionId` | ```u128```
| item | `T::NftItemId` | ```u128```
| amount | `BalanceOf<T>` | ```u128```
| maker | `T::AccountId` | ```AccountId```

---------
### OfferPlaced
Offer was placed on a token
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| collection | `T::NftCollectionId` | ```u128```
| item | `T::NftItemId` | ```u128```
| amount | `BalanceOf<T>` | ```u128```
| expires | `T::BlockNumber` | ```u32```

---------
### OfferWithdrawn
Offer was withdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| collection | `T::NftCollectionId` | ```u128```
| item | `T::NftItemId` | ```u128```

---------
### RoyaltyAdded
Marketplace data has been added
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::NftCollectionId` | ```u128```
| item | `T::NftItemId` | ```u128```
| author | `T::AccountId` | ```AccountId```
| royalty | `u16` | ```u16```

---------
### RoyaltyPaid
Royalty hs been paid to the author
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::NftCollectionId` | ```u128```
| item | `T::NftItemId` | ```u128```
| author | `T::AccountId` | ```AccountId```
| royalty | `u16` | ```u16```
| royalty_amount | `BalanceOf<T>` | ```u128```

---------
### TokenPriceUpdated
The price for a token was updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| collection | `T::NftCollectionId` | ```u128```
| item | `T::NftItemId` | ```u128```
| price | `Option<BalanceOf<T>>` | ```(None, 'u128')```

---------
### TokenSold
Token was sold to a new owner
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| buyer | `T::AccountId` | ```AccountId```
| collection | `T::NftCollectionId` | ```u128```
| item | `T::NftItemId` | ```u128```
| price | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### MarketplaceItems
 Stores Marketplace info

#### Python
```python
result = substrate.query(
    'Marketplace', 'MarketplaceItems', ['u128', 'u128']
)
```

#### Return value
```python
{'author': 'AccountId', 'royalty': 'u16'}
```
---------
### Offers
 Stores offer info

#### Python
```python
result = substrate.query(
    'Marketplace', 'Offers', [('u128', 'u128'), 'AccountId']
)
```

#### Return value
```python
{'amount': 'u128', 'expires': 'u32', 'maker': 'AccountId'}
```
---------
### Prices
 Stores token info

#### Python
```python
result = substrate.query(
    'Marketplace', 'Prices', ['u128', 'u128']
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### MinimumOfferAmount
#### Value
```python
10000000000
```
#### Python
```python
constant = substrate.get_constant('Marketplace', 'MinimumOfferAmount')
```
---------
### RoyaltyBondAmount
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Marketplace', 'RoyaltyBondAmount')
```
---------
## Errors

---------
### AcceptNotAuthorized
User has to be the token owner to accept an offer

---------
### AlreadyOffered
User already made an offer for this token

---------
### BuyFromSelf
Cannot buy a token from yourself

---------
### CollectionOrItemUnknown
Collection or item does not exist

---------
### NotForSale
Token is currently not for sale

---------
### NotInRange
Royalty not in 0-9_999 range

---------
### NotTheTokenOwner
Account is not the owner of the token

---------
### OfferExpired
Offer is no longer valid

---------
### OfferTooLow
Offer is lower than the minimum threshold

---------
### RoyaltyAlreadySet
Royalty can be set only once

---------
### UnknownOffer
No offer for this token found from the user

---------
### WithdrawNotAuthorized
User has to be offer maker or token owner to withdraw an offer

---------