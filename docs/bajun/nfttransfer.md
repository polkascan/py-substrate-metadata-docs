
# NftTransfer

---------
## Calls

---------
### set_locked_state
#### Attributes
| Name | Type |
| -------- | -------- | 
| locked_state | `PalletLockedState` | 

#### Python
```python
call = substrate.compose_call(
    'NftTransfer', 'set_locked_state', {
    'locked_state': (
        'Unlocked',
        'Locked',
    ),
}
)
```

---------
### set_organizer
#### Attributes
| Name | Type |
| -------- | -------- | 
| organizer | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'NftTransfer', 'set_organizer', {'organizer': 'AccountId'}
)
```

---------
## Events

---------
### AssetRestored
Asset has been restored back from its NFT representation [collection_id, asset_id,
owner]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u32```
| asset_id | `T::ItemId` | ```u128```
| owner | `T::AccountId` | ```AccountId```

---------
### AssetStored
Asset has been stored as an NFT [collection_id, asset_id, owner]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u32```
| asset_id | `T::ItemId` | ```u128```
| owner | `T::AccountId` | ```AccountId```

---------
### AssetTransferred
Asset has been transferred outside the chain [collection_id, asset_id, owner]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u32```
| asset_id | `T::ItemId` | ```u128```
| owner | `T::AccountId` | ```AccountId```

---------
### LockedStateSet
The pallet&\#x27;s lock status has been set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| locked_state | `PalletLockedState` | ```('Unlocked', 'Locked')```

---------
### OrganizerSet
An organizer has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| organizer | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### HoldingAccount

#### Python
```python
result = substrate.query(
    'NftTransfer', 'HoldingAccount', []
)
```

#### Return value
```python
'AccountId'
```
---------
### LockItemStatus

#### Python
```python
result = substrate.query(
    'NftTransfer', 'LockItemStatus', ['u32', 'u128']
)
```

#### Return value
```python
('Stored', 'Uploaded')
```
---------
### LockedState

#### Python
```python
result = substrate.query(
    'NftTransfer', 'LockedState', []
)
```

#### Return value
```python
('Unlocked', 'Locked')
```
---------
### NextItemId

#### Python
```python
result = substrate.query(
    'NftTransfer', 'NextItemId', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### NftClaimants

#### Python
```python
result = substrate.query(
    'NftTransfer', 'NftClaimants', ['u32', 'u128']
)
```

#### Return value
```python
'AccountId'
```
---------
### Organizer

#### Python
```python
result = substrate.query(
    'NftTransfer', 'Organizer', []
)
```

#### Return value
```python
'AccountId'
```
---------
## Constants

---------
### HoldingPalletId
 The holding&#x27;s pallet id, used for deriving its sovereign account identifier for the Nft
 holding account.
#### Value
```python
'0x616a2f6e66747472'
```
#### Python
```python
constant = substrate.get_constant('NftTransfer', 'HoldingPalletId')
```
---------
### MaxAssetEncodedSize
 Maximum amount of bytes that an asset may be encoded as.
#### Value
```python
200
```
#### Python
```python
constant = substrate.get_constant('NftTransfer', 'MaxAssetEncodedSize')
```
---------
## Errors

---------
### AssetRestoreFailure
The process of restoring an NFT into an Asset has failed.

---------
### AssetSizeAboveEncodingLimit
The given asset resulted in an encoded size larger that the defined encoding limit.

---------
### NftAttributeMissing
The given NFT id doesn&\#x27;t have the proper attribute set.

---------
### NftNotFound
The given NFT id didn&\#x27;t match any entries for the specified collection.

---------
### NftNotOwned
The given NFT is not owned by the requester.

---------
### NftOutsideOfChain
The given NFT is currently outside of the chain, transfer it back before attempting a
restore.

---------
### OrganizerNotSet
There is no account set as the organizer

---------
### PalletLocked
The pallet is currently locked and cannot be interacted with.

---------