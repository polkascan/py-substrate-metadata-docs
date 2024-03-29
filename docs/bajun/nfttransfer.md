
# NftTransfer

---------
## Events

---------
### ItemRestored
Item has been restored back from its NFT representation [collection_id, item_id, owner]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u32```
| item_id | `T::ItemId` | ```scale_info::12```
| owner | `T::AccountId` | ```AccountId```

---------
### ItemStored
Item has been stored as an NFT [collection_id, item_id, owner]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u32```
| item_id | `T::ItemId` | ```scale_info::12```
| owner | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### NftStatuses

#### Python
```python
result = substrate.query(
    'NftTransfer', 'NftStatuses', ['u32', 'scale_info::12']
)
```

#### Return value
```python
('Stored', 'Uploaded')
```
---------
## Constants

---------
### KeyLimit
 The maximum length of an attribute key.
#### Value
```python
32
```
#### Python
```python
constant = substrate.get_constant('NftTransfer', 'KeyLimit')
```
---------
### PalletId
 The NFT-transfer&#x27;s pallet id, used for deriving its sovereign account ID.
#### Value
```python
'0x616a2f6e66747472'
```
#### Python
```python
constant = substrate.get_constant('NftTransfer', 'PalletId')
```
---------
### ValueLimit
 The maximum length of an attribute value.
#### Value
```python
64
```
#### Python
```python
constant = substrate.get_constant('NftTransfer', 'ValueLimit')
```
---------
## Errors

---------
### DuplicateItemCode
Item code must be different to attribute codes.

---------
### EmptyIpfsUrl
IPFS URL must not be an empty string.

---------
### ItemRestoreFailure
The process of restoring an NFT into an item has failed.

---------
### NftNotOwned
The given NFT is not owned by the requester.

---------
### NftOutsideOfChain
The given NFT is currently outside of the chain, transfer it back before attempting a
restore.

---------
### UnknownClaim
The given claim doesn&\#x27;t exist.

---------
### UnknownItem
The given NFT item doesn&\#x27;t exist.

---------