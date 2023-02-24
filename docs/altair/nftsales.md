
# NftSales

---------
## Calls

---------
### add
Add an NFT

Fails if
  - the NFT is not found in [T::NonFungibles]
  - `origin` is not the owner of the nft
  - the nft is already for sale
  - transferring ownership of the NFT to this pallet&\#x27;s account fails
#### Attributes
| Name | Type |
| -------- | -------- | 
| class_id | `T::CollectionId` | 
| instance_id | `T::ItemId` | 
| price | `Price<CurrencyOf<T>, BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'NftSales', 'add', {
    'class_id': 'u64',
    'instance_id': 'u128',
    'price': {
        'amount': 'u128',
        'currency': {
            'AUSD': None,
            'ForeignAsset': 'u32',
            'KSM': None,
            'Native': None,
            'Tranche': (
                'u64',
                '[u8; 16]',
            ),
        },
    },
}
)
```

---------
### buy
Buy the given nft

Buyers must propose a `max_offer` to save them from a scenario where they could end up
paying more than they desired for an NFT. That scenario could take place if the seller
increased the asking price right before the buyer submits this call to buy said NFT.

Buyers always pay the latest asking price as long as it does not exceed their max offer.

Fails if
  - the NFT is not for sale
  - `origin` is the seller of the NFT
  - `origin` does not have enough balance of the currency the nft is being sold in
  - transferring the asking price from the buyer to the seller fails
  - transferring the nft to the buyer fails
#### Attributes
| Name | Type |
| -------- | -------- | 
| class_id | `T::CollectionId` | 
| instance_id | `T::ItemId` | 
| max_offer | `Price<CurrencyOf<T>, BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'NftSales', 'buy', {
    'class_id': 'u64',
    'instance_id': 'u128',
    'max_offer': {
        'amount': 'u128',
        'currency': {
            'AUSD': None,
            'ForeignAsset': 'u32',
            'KSM': None,
            'Native': None,
            'Tranche': (
                'u64',
                '[u8; 16]',
            ),
        },
    },
}
)
```

---------
### remove
Remove an NFT

The seller of an NFT that is for sale can call this extrinsic to reclaim
ownership over their NFT and remove it from sale.

Fails if
  - the nft is not for sale
  - `origin` is not the seller of the NFT
  - transferring the ownership of the NFT back to the seller fails
#### Attributes
| Name | Type |
| -------- | -------- | 
| class_id | `T::CollectionId` | 
| instance_id | `T::ItemId` | 

#### Python
```python
call = substrate.compose_call(
    'NftSales', 'remove', {
    'class_id': 'u64',
    'instance_id': 'u128',
}
)
```

---------
## Events

---------
### ForSale
An NFT is now for sale
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| class_id | `T::CollectionId` | ```u64```
| instance_id | `T::ItemId` | ```u128```
| sale | `SaleOf<T>` | ```{'seller': 'AccountId', 'price': {'currency': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), 'KSM': None, 'AUSD': None, 'ForeignAsset': 'u32'}, 'amount': 'u128'}}```

---------
### Removed
An NFT was removed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| class_id | `T::CollectionId` | ```u64```
| instance_id | `T::ItemId` | ```u128```

---------
### Sold
An NFT has been sold
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| class_id | `T::CollectionId` | ```u64```
| instance_id | `T::ItemId` | ```u128```
| sale | `SaleOf<T>` | ```{'seller': 'AccountId', 'price': {'currency': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), 'KSM': None, 'AUSD': None, 'ForeignAsset': 'u32'}, 'amount': 'u128'}}```
| buyer | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### NftsBySeller
 Nft lookup by seller.

 We use this storage to efficiently look up the NFTs being sold by
 an account (seller).

#### Python
```python
result = substrate.query(
    'NftSales', 'NftsBySeller', ['AccountId', 'u64', 'u128']
)
```

#### Return value
```python
()
```
---------
### Sales
 The active sales.
 A sale is an entry identified by an NFT collection and item id.

#### Python
```python
result = substrate.query(
    'NftSales', 'Sales', ['u64', 'u128']
)
```

#### Return value
```python
{
    'price': {
        'amount': 'u128',
        'currency': {
            'AUSD': None,
            'ForeignAsset': 'u32',
            'KSM': None,
            'Native': None,
            'Tranche': ('u64', '[u8; 16]'),
        },
    },
    'seller': 'AccountId',
}
```
---------
## Constants

---------
### PalletId
 The Id of this pallet
#### Value
```python
'0x70616c2f6e667473'
```
#### Python
```python
constant = substrate.get_constant('NftSales', 'PalletId')
```
---------
## Errors

---------
### AlreadyForSale
A seller has attempted to add an NFT that is already for sale

---------
### InvalidOffer
A buyer&\#x27;s max offer is invalid, i.e., either the currency or amount did
not match the latest asking price for the targeted NFT.

---------
### NotForSale
An operation expected an NFT to be for sale when it is not

---------
### NotFound
A user tried to add an NFT that could not be found in T::NonFungibles

---------
### NotOwner
The origin is not the owner of an NFT

---------