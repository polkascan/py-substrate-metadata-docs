
# Marketplace

---------
## Calls

---------
### accept_offer
See [`Pallet::accept_offer`].
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
See [`Pallet::add_royalty`].
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
See [`Pallet::buy`].
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
See [`Pallet::make_offer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::NftCollectionId` | 
| item_id | `T::NftItemId` | 
| amount | `BalanceOf<T>` | 
| expires | `BlockNumberFor<T>` | 

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
See [`Pallet::set_price`].
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
See [`Pallet::withdraw_offer`].
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
| expires | `BlockNumberFor<T>` | ```u32```

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