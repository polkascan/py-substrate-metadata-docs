
# NFT

---------
## Calls

---------
### burn
See [`Pallet::burn`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::NftCollectionId` | 
| item_id | `T::NftItemId` | 

#### Python
```python
call = substrate.compose_call(
    'NFT', 'burn', {
    'collection_id': 'u128',
    'item_id': 'u128',
}
)
```

---------
### create_collection
See [`Pallet::create_collection`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::NftCollectionId` | 
| collection_type | `T::CollectionType` | 
| metadata | `BoundedVecOfUnq<T>` | 

#### Python
```python
call = substrate.compose_call(
    'NFT', 'create_collection', {
    'collection_id': 'u128',
    'collection_type': (
        'Marketplace',
        'LiquidityMining',
    ),
    'metadata': 'Bytes',
}
)
```

---------
### destroy_collection
See [`Pallet::destroy_collection`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::NftCollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'NFT', 'destroy_collection', {'collection_id': 'u128'}
)
```

---------
### mint
See [`Pallet::mint`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::NftCollectionId` | 
| item_id | `T::NftItemId` | 
| metadata | `BoundedVecOfUnq<T>` | 

#### Python
```python
call = substrate.compose_call(
    'NFT', 'mint', {
    'collection_id': 'u128',
    'item_id': 'u128',
    'metadata': 'Bytes',
}
)
```

---------
### transfer
See [`Pallet::transfer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::NftCollectionId` | 
| item_id | `T::NftItemId` | 
| dest | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'NFT', 'transfer', {
    'collection_id': 'u128',
    'dest': 'AccountId',
    'item_id': 'u128',
}
)
```

---------
## Events

---------
### CollectionCreated
A collection was created
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| collection_id | `T::NftCollectionId` | ```u128```
| collection_type | `T::CollectionType` | ```('Marketplace', 'LiquidityMining')```
| metadata | `BoundedVecOfUnq<T>` | ```Bytes```

---------
### CollectionDestroyed
A collection was destroyed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| collection_id | `T::NftCollectionId` | ```u128```

---------
### ItemBurned
An item was burned
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| collection_id | `T::NftCollectionId` | ```u128```
| item_id | `T::NftItemId` | ```u128```

---------
### ItemMinted
An item was minted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| collection_id | `T::NftCollectionId` | ```u128```
| item_id | `T::NftItemId` | ```u128```
| metadata | `BoundedVecOfUnq<T>` | ```Bytes```

---------
### ItemTransferred
An item was transferred
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| collection_id | `T::NftCollectionId` | ```u128```
| item_id | `T::NftItemId` | ```u128```

---------
## Storage functions

---------
### Collections
 Stores collection info

#### Python
```python
result = substrate.query(
    'NFT', 'Collections', ['u128']
)
```

#### Return value
```python
{'collection_type': ('Marketplace', 'LiquidityMining'), 'metadata': 'Bytes'}
```
---------
### Items
 Stores item info

#### Python
```python
result = substrate.query(
    'NFT', 'Items', ['u128', 'u128']
)
```

#### Return value
```python
{'metadata': 'Bytes'}
```
---------
## Constants

---------
### ReserveCollectionIdUpTo
 Collection IDs reserved for runtime up to the following constant
#### Value
```python
999999
```
#### Python
```python
constant = substrate.get_constant('NFT', 'ReserveCollectionIdUpTo')
```
---------
## Errors

---------
### CollectionUnknown
Collection does not exist

---------
### IdReserved
ID reserved for runtime

---------
### ItemUnknown
Item does not exist

---------
### NoAvailableCollectionId
Count of collections overflown

---------
### NoAvailableItemId
Count of items overflown

---------
### NotPermitted
Operation not permitted

---------
### TokenCollectionNotEmpty
Collection still contains minted tokens

---------