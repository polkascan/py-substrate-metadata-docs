
# KylinMarket

---------
## Calls

---------
### accept_offer
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 
| offerer | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'KylinMarket', 'accept_offer', {
    'collection_id': 'u32',
    'nft_id': 'u32',
    'offerer': 'AccountId',
}
)
```

---------
### buy
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 
| amount | `Option<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinMarket', 'buy', {
    'amount': (None, 'u128'),
    'collection_id': 'u32',
    'nft_id': 'u32',
}
)
```

---------
### list
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 
| amount | `BalanceOf<T>` | 
| expires | `Option<T::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinMarket', 'list', {
    'amount': 'u128',
    'collection_id': 'u32',
    'expires': (None, 'u32'),
    'nft_id': 'u32',
}
)
```

---------
### make_offer
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 
| amount | `BalanceOf<T>` | 
| expires | `Option<T::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinMarket', 'make_offer', {
    'amount': 'u128',
    'collection_id': 'u32',
    'expires': (None, 'u32'),
    'nft_id': 'u32',
}
)
```

---------
### unlist
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 

#### Python
```python
call = substrate.compose_call(
    'KylinMarket', 'unlist', {
    'collection_id': 'u32',
    'nft_id': 'u32',
}
)
```

---------
### withdraw_offer
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 

#### Python
```python
call = substrate.compose_call(
    'KylinMarket', 'withdraw_offer', {
    'collection_id': 'u32',
    'nft_id': 'u32',
}
)
```

---------
## Events

---------
### OfferAccepted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| buyer | `T::AccountId` | ```AccountId```
| collection_id | `CollectionId` | ```u32```
| nft_id | `NftId` | ```u32```

---------
### OfferPlaced
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| offerer | `T::AccountId` | ```AccountId```
| collection_id | `CollectionId` | ```u32```
| nft_id | `NftId` | ```u32```
| price | `BalanceOf<T>` | ```u128```

---------
### OfferWithdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| collection_id | `CollectionId` | ```u32```
| nft_id | `NftId` | ```u32```

---------
### TokenListed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| collection_id | `CollectionId` | ```u32```
| nft_id | `NftId` | ```u32```
| price | `BalanceOf<T>` | ```u128```

---------
### TokenPriceUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| collection_id | `CollectionId` | ```u32```
| nft_id | `NftId` | ```u32```
| price | `Option<BalanceOf<T>>` | ```(None, 'u128')```

---------
### TokenSold
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| buyer | `T::AccountId` | ```AccountId```
| collection_id | `CollectionId` | ```u32```
| nft_id | `NftId` | ```u32```
| price | `BalanceOf<T>` | ```u128```

---------
### TokenUnlisted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| collection_id | `CollectionId` | ```u32```
| nft_id | `NftId` | ```u32```

---------
## Storage functions

---------
### ListedNfts

#### Python
```python
result = substrate.query(
    'KylinMarket', 'ListedNfts', ['u32', 'u32']
)
```

#### Return value
```python
{'amount': 'u128', 'expires': (None, 'u32'), 'listed_by': 'AccountId'}
```
---------
### Offers

#### Python
```python
result = substrate.query(
    'KylinMarket', 'Offers', [('u32', 'u32'), 'AccountId']
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
#### Value
```python
100000000000000
```
#### Python
```python
constant = substrate.get_constant('KylinMarket', 'MinimumOfferAmount')
```
---------
## Errors

---------
### AlreadyOffered

---------
### CannotBuyOwnToken

---------
### CannotListNftOwnedByNft

---------
### CannotOfferOnOwnToken

---------
### CannotUnlistToken

---------
### CannotWithdrawOffer

---------
### ListingHasExpired

---------
### NoPermission

---------
### NonTransferable

---------
### OfferHasExpired

---------
### OfferTooLow

---------
### PriceDiffersFromExpected

---------
### TokenDoesNotExist

---------
### TokenNotForSale

---------
### UnknownOffer

---------