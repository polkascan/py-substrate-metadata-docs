
# PWMarketplace

---------
## Calls

---------
### set_marketplace_owner
See [`Pallet::set_marketplace_owner`].
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
See [`Pallet::set_nfts_royalty_info`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| royalty_info | `RoyaltyInfo<T::AccountId, Permill>` | 
| collection_id | `CollectionIdOf<T>` | 
| nft_ids | `BoundedVec<ItemIdOf<T>, T::IterLimit>` | 

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
| collection_id | `CollectionIdOf<T>` | ```u32```
| nft_id | `ItemIdOf<T>` | ```u32```
| old_royalty_info | `Option<RoyaltyInfoOf<T>>` | ```(None, {'recipient': 'AccountId', 'amount': 'u32'})```
| new_royalty_info | `RoyaltyInfoOf<T>` | ```{'recipient': 'AccountId', 'amount': 'u32'}```

---------