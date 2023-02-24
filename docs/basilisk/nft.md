
# NFT

---------
## Calls

---------
### burn
Removes a token from existence.
Burning needs to be enabled in the permissions for the given collection type.

Parameters:
- `origin`: The NFT owner.
- `collection_id`: The collection of the asset to be burned.
- `item_id`: The instance of the asset to be burned.
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
Creates an NFT collection of the given collection type and sets its metadata.
The collection ID needs to be outside of the range of reserved IDs.
The creation of a collection needs to be enabled in the permissions
for the given collection type.

Parameters:
- `origin`: The owner of the newly created collection.
- `collection_id`: Identifier of a collection.
- `collection_type`: The collection type determines its purpose and usage.
- `metadata`: Arbitrary data about a collection, e.g. IPFS hash or name.

Emits CollectionCreated event
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
Removes a collection from existence.
Destroying of collections need to be enabled in the permissions
for the given collection type.
Fails if the collection is not empty.

Parameters:
- `origin`: The collection owner.
- `collection_id`: The identifier of the asset collection to be destroyed.
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
Mints an NFT in the specified collection and sets its metadata.
Minting of new items needs to be enabled in the permissions
for the given collection type.

Parameters:
- `origin`: The owner of the newly minted NFT.
- `collection_id`: The collection of the asset to be minted.
- `item_id`: The item of the asset to be minted.
- `metadata`: Arbitrary data about an item, e.g. IPFS hash or symbol.
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
Transfers NFT from account A to account B.
Transfers need to be enabled in the permissions for the given collection type.

Parameters:
- `origin`: The NFT owner
- `collection_id`: The collection of the asset to be transferred.
- `item_id`: The instance of the asset to be transferred.
- `dest`: The account to receive ownership of the asset.
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