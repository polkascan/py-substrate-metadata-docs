
# PWMarketplace

---------
## Calls

---------
### set_marketplace_owner
Privileged function that can be called by the `Overlord` account to set the
`MarketplaceOwner` in the `pallet_rmrk_market` Storage.

Parameters:
- `origin`: Expected to be called by Overlord admin account.
- `new_marketplace_owner`: New `T::AccountId` of the new martketplace owner.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_marketplace_owner | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'PWMarketplace', 'set_marketplace_owner', {'new_marketplace_owner': 'AccountId'}
)
```

---------
### set_nfts_royalty_info
Privileged function to update the RoyaltyInfo for PhalaWorld NFTs that will be sold in
the marketplace.

Parameters:
- `origin`: Expected to be called by Overlord admin account.
- `royalty_info`: `RoyaltyInfo` to set the NFTs to.
- `collection_id`: `T::CollectionId` of the PhalaWorld NFT collection.
- `nft_ids`: `BoundedVec` NFT IDs to update in a collection bounded by T::IterLimit.
#### Attributes
| Name | Type |
| -------- | -------- | 
| royalty_info | `RoyaltyInfo<T::AccountId, Permill>` | 
| collection_id | `T::CollectionId` | 
| nft_ids | `BoundedVec<T::ItemId, T::IterLimit>` | 

#### Python
```python
call = substrate.compose_call(
    'PWMarketplace', 'set_nfts_royalty_info', {
    'collection_id': 'u32',
    'nft_ids': ['u32'],
    'royalty_info': {
        'amount': 'u32',
        'recipient': 'AccountId',
    },
}
)
```

---------
## Events

---------
### MarketplaceOwnerSet
Marketplace owner is set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_marketplace_owner | `Option<T::AccountId>` | ```(None, 'AccountId')```
| new_marketplace_owner | `T::AccountId` | ```AccountId```

---------
### RoyaltyInfoUpdated
RoyaltyInfo updated for a NFT.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u32```
| nft_id | `T::ItemId` | ```u32```
| old_royalty_info | `Option<RoyaltyInfoOf<T>>` | ```(None, {'recipient': 'AccountId', 'amount': 'u32'})```
| new_royalty_info | `RoyaltyInfoOf<T>` | ```{'recipient': 'AccountId', 'amount': 'u32'}```

---------