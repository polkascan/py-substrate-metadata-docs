
# Nft

---------
## Calls

---------
### burn
Destroys NFT asset if the sender owns it

The dispatch origin for this call must be _Signed_.
- `asset_id`: the asset (class ID, token ID) that will be burned

Emits `CollectionLocked` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `(ClassIdOf<T>, TokenIdOf<T>)` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'burn', {'asset_id': ('u32', 'u64')}
)
```

---------
### create_class
Create new NFT class using provided NFT class data details

The dispatch origin for this call must be _Signed_.
- `metadata`: class metadata as NFT metadata
- `attributes`: class&\#x27; attributes
- `collection`: the class&\#x27; group collection ID
- `token_type`: the type of token which will be minted for this class
- `collection_type`: the type of collection the class will be
- `royalty_fee` - the fee (as a percent value) which will go to the class owner

Emits `NewNftClassCreated` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| metadata | `NftMetadata` | 
| attributes | `Attributes` | 
| collection_id | `GroupCollectionId` | 
| token_type | `TokenType` | 
| collection_type | `CollectionType` | 
| royalty_fee | `Perbill` | 
| mint_limit | `Option<u32>` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'create_class', {
    'attributes': 'scale_info::276',
    'collection_id': 'u64',
    'collection_type': {
        'Collectable': None,
        'Executable': 'Bytes',
        'Wearable': None,
    },
    'metadata': 'Bytes',
    'mint_limit': (None, 'u32'),
    'royalty_fee': 'u32',
    'token_type': (
        'Transferable',
        'BoundToAddress',
    ),
}
)
```

---------
### create_group
Create a new NFT group collection from provided name and properties
as NFT metadata

The dispatch origin for this call must be _Root_.
- `name`: name of the group collection as NFT metadata
- `properties`: properties of the group collection as NFT metadata

Emits `NewNftCollectionCreated` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| name | `NftMetadata` | 
| properties | `NftMetadata` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'create_group', {
    'name': 'Bytes',
    'properties': 'Bytes',
}
)
```

---------
### enable_promotion
Change NFT minting promotion status to the provided value

The dispatch origin for this call must be _Root_.
- `enable`: the promotion status (on or off)

Emits `PromotionEnabled` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| enable | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'enable_promotion', {'enable': 'bool'}
)
```

---------
### force_lock_collection
Lock the provided collection by governance if it is not already locked

The dispatch origin for this call must be _Root_.
- `class_id`: the class ID of the collection

Emits `CollectionLocked` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| class_id | `ClassIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'force_lock_collection', {'class_id': 'u32'}
)
```

---------
### force_transfer
Transfer a NFT asset triggered by governance

The dispatch origin for this call must be _Root_.
- `to`: account to transfer the NFT asset to
- `asset_id`: the asset (class ID, token ID) that will be transferred

Emits `ForceTransferredNft` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| from | `T::AccountId` | 
| to | `T::AccountId` | 
| asset_id | `(ClassIdOf<T>, TokenIdOf<T>)` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'force_transfer', {
    'asset_id': ('u32', 'u64'),
    'from': 'AccountId',
    'to': 'AccountId',
}
)
```

---------
### force_unlock_collection
Unlock the provided collection by governance if already locked

The dispatch origin for this call must be _Root_.
- `class_id`: the class ID of the collection

Emits `CollectionUnlocked` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| class_id | `ClassIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'force_unlock_collection', {'class_id': 'u32'}
)
```

---------
### force_unlock_nft
Unlock the provided NFT by governance if already locked

The dispatch origin for this call must be _Root_.
- `token_id`: the class ID nad token ID of the asset

Emits `NftUnlocked` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| token_id | `(ClassIdOf<T>, TokenIdOf<T>)` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'force_unlock_nft', {'token_id': ('u32', 'u64')}
)
```

---------
### force_update_royalty_fee
Force update royalty fee of a given class

The dispatch origin for this call must be _Root_.
- `class_id`: the class ID of the collection
- `new_royalty_fee: the new royalty fee of the collection

Emits `ClassRoyaltyFeeUpdated` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| class_id | `ClassIdOf<T>` | 
| new_royalty_fee | `Perbill` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'force_update_royalty_fee', {
    'class_id': 'u32',
    'new_royalty_fee': 'u32',
}
)
```

---------
### force_update_total_issuance
Force update the total issuance of a given class

The dispatch origin for this call must be _Root_.
- `class_id`: the class ID of the collection
- `current_total_issuance`: the current total issuance of the collection
- `new_total_issuance`: the new total issuance of the collection

Emits `ClassTotalIssuanceUpdated` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| class_id | `ClassIdOf<T>` | 
| current_total_issuance | `TokenIdOf<T>` | 
| new_total_issuance | `TokenIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'force_update_total_issuance', {
    'class_id': 'u32',
    'current_total_issuance': 'u64',
    'new_total_issuance': 'u64',
}
)
```

---------
### mint
Minting new NFTs using provided class ID, metadata,
attributes, and quantity

The dispatch origin for this call must be _Signed_.
- `class_id`: class ID of the collection the NFT will be part of
- `metadata`: NFT assets metadata as NFT metadata
- `attributes`: NFTs&\#x27; attributes
- `quantity`: the number of NFTs to be minted

Emits `NewNftMinted` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| class_id | `ClassIdOf<T>` | 
| metadata | `NftMetadata` | 
| attributes | `Attributes` | 
| quantity | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'mint', {
    'attributes': 'scale_info::276',
    'class_id': 'u32',
    'metadata': 'Bytes',
    'quantity': 'u32',
}
)
```

---------
### mint_stackable_nft
Minting new stackable NFTs using provided class ID, metadata,
attributes, and amount

The dispatch origin for this call must be _Signed_.
- `class_id`: class ID of the collection the NFT will be part of
- `metadata`: NFT assets metadata as NFT metadata
- `attributes`: NFTs&\#x27; attributes
- `amount`: the balance of the minted stackable NFTs

Emits `NewStackableNftMinted` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| class_id | `ClassIdOf<T>` | 
| metadata | `NftMetadata` | 
| attributes | `Attributes` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'mint_stackable_nft', {
    'amount': 'u128',
    'attributes': 'scale_info::276',
    'class_id': 'u32',
    'metadata': 'Bytes',
}
)
```

---------
### set_hard_limit
Set hard limit of minted tokens for a NFT class.

The dispatch origin for this call must be _Signed_.
Only class owner can make this call.
- `class_id`: the class ID of the collection

Emits `HardLimitSet` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| class_id | `ClassIdOf<T>` | 
| hard_limit | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'set_hard_limit', {
    'class_id': 'u32',
    'hard_limit': 'u32',
}
)
```

---------
### sign_asset
Support an NFT asset with provided contribution amount if not the asset owner

The dispatch origin for this call must be _Signed_.
- `asset_id`: the asset (class ID, token ID) that will be signed
- `contribution`: the amount the sender contributes to the Nft

Emits no event if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `(ClassIdOf<T>, TokenIdOf<T>)` | 
| contribution | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'sign_asset', {
    'asset_id': ('u32', 'u64'),
    'contribution': 'u128',
}
)
```

---------
### transfer
Transfer an existing NFT asset if it is not listed in an auction

The dispatch origin for this call must be _Signed_.
- `to`: account to transfer the NFT asset to
- `asset_id`: the asset (class ID, token ID) that will be transferred

Emits `TransferedNft` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| asset_id | `(ClassIdOf<T>, TokenIdOf<T>)` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'transfer', {'asset_id': ('u32', 'u64'), 'to': 'AccountId'}
)
```

---------
### transfer_batch
Transfer a batch of existing NFT assets if the batch size no more
than the max batch transfer size and the asset are owned by the sender

The dispatch origin for this call must be _Signed_.
- `to`: account to transfer the NFT asset to
- `tos`: list of assets (class ID, token ID) that will be transferred

Emits `TransferedNft` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| tos | `Vec<(T::AccountId, (ClassIdOf<T>, TokenIdOf<T>))>` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'transfer_batch', {'tos': [('AccountId', ('u32', 'u64'))]}
)
```

---------
### transfer_stackable_nft
Transfer an existing NFT asset if it is not listed in an auction

The dispatch origin for this call must be _Signed_.
- `to`: account to transfer the NFT asset to
- `asset_id`: the asset (class ID, token ID) that will be transferred

Emits `TransferedStakcableNft` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| asset_id | `(ClassIdOf<T>, TokenIdOf<T>)` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'transfer_stackable_nft', {
    'amount': 'u128',
    'asset_id': ('u32', 'u64'),
    'to': 'AccountId',
}
)
```

---------
### withdraw_funds_from_class_fund
Withdraws funds from class fund

The dispatch origin for this call must be _Signed_.
Only class owner can withdraw funds.
- `class_id`: the class ID of the class which funds will be withdrawn

Emits `ClassFundsWithdrawn` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| class_id | `ClassIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'withdraw_funds_from_class_fund', {'class_id': 'u32'}
)
```

---------
## Events

---------
### BurnedNft
Burn NFT
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `(ClassIdOf<T>, TokenIdOf<T>)` | ```('u32', 'u64')```

---------
### ClassFundsWithdrawn
Class funds are withdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ClassIdOf<T>` | ```u32```

---------
### ClassRoyaltyFeeUpdated
Successfully updated royalty fee
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ClassIdOf<T>` | ```u32```
| None | `Perbill` | ```u32```

---------
### ClassTotalIssuanceUpdated
Successfully updated class total issuance
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ClassIdOf<T>` | ```u32```
| None | `TokenIdOf<T>` | ```u64```

---------
### CollectionLocked
Collection is locked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ClassIdOf<T>` | ```u32```

---------
### CollectionUnlocked
Collection is unlocked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ClassIdOf<T>` | ```u32```

---------
### ExecutedNft
Executed NFT
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u64```

---------
### ForceTransferredNft
Successfully force transfer NFT
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `<T as frame_system::Config>::AccountId` | ```AccountId```
| None | `<T as frame_system::Config>::AccountId` | ```AccountId```
| None | `TokenIdOf<T>` | ```u64```
| None | `(ClassIdOf<T>, TokenIdOf<T>)` | ```('u32', 'u64')```

---------
### HardLimitSet
Hard limit is set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ClassIdOf<T>` | ```u32```

---------
### NewNftClassCreated
New NFT Collection/Class created
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `<T as frame_system::Config>::AccountId` | ```AccountId```
| None | `ClassIdOf<T>` | ```u32```

---------
### NewNftCollectionCreated
New NFT Group Collection created
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `GroupCollectionId` | ```u64```

---------
### NewNftMinted
Emit event when new nft minted - show the first and last asset mint
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `(ClassIdOf<T>, TokenIdOf<T>)` | ```('u32', 'u64')```
| None | `(ClassIdOf<T>, TokenIdOf<T>)` | ```('u32', 'u64')```
| None | `<T as frame_system::Config>::AccountId` | ```AccountId```
| None | `ClassIdOf<T>` | ```u32```
| None | `u32` | ```u32```
| None | `TokenIdOf<T>` | ```u64```

---------
### NewStackableNftMinted
Emit event when new nft minted - show the first and last asset mint
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `<T as frame_system::Config>::AccountId` | ```AccountId```
| None | `ClassIdOf<T>` | ```u32```
| None | `TokenIdOf<T>` | ```u64```
| None | `BalanceOf<T>` | ```u128```

---------
### NewTimeCapsuleMinted
Emit event when new time capsule minted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `(ClassIdOf<T>, TokenIdOf<T>)` | ```('u32', 'u64')```
| None | `<T as frame_system::Config>::AccountId` | ```AccountId```
| None | `ClassIdOf<T>` | ```u32```
| None | `TokenIdOf<T>` | ```u64```
| None | `T::BlockNumber` | ```u32```
| None | `Vec<u8>` | ```Bytes```

---------
### NftUnlocked
NFT is unlocked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ClassIdOf<T>` | ```u32```
| None | `TokenIdOf<T>` | ```u64```

---------
### PromotionEnabled
Promotion enabled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `bool` | ```bool```

---------
### ScheduledTimeCapsule
Scheduled time capsule
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u64```
| None | `Vec<u8>` | ```Bytes```
| None | `T::BlockNumber` | ```u32```

---------
### SignedNft
Signed on NFT
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TokenIdOf<T>` | ```u64```
| None | `<T as frame_system::Config>::AccountId` | ```AccountId```

---------
### TransferedNft
Successfully transfer NFT
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `<T as frame_system::Config>::AccountId` | ```AccountId```
| None | `<T as frame_system::Config>::AccountId` | ```AccountId```
| None | `TokenIdOf<T>` | ```u64```
| None | `(ClassIdOf<T>, TokenIdOf<T>)` | ```('u32', 'u64')```

---------
### TransferedStackableNft
Successfully transfer NFT
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `<T as frame_system::Config>::AccountId` | ```AccountId```
| None | `<T as frame_system::Config>::AccountId` | ```AccountId```
| None | `(ClassIdOf<T>, TokenIdOf<T>)` | ```('u32', 'u64')```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### AllNftGroupCollection
 Track the total NFT group collection IDs

#### Python
```python
result = substrate.query(
    'Nft', 'AllNftGroupCollection', []
)
```

#### Return value
```python
'u64'
```
---------
### AssetSupporters
 Stores list of supporter accounts for every NFT assets

#### Python
```python
result = substrate.query(
    'Nft', 'AssetSupporters', [('u32', 'u64')]
)
```

#### Return value
```python
['AccountId']
```
---------
### ClassDataCollection
 Stores group collection IDs for every class

#### Python
```python
result = substrate.query(
    'Nft', 'ClassDataCollection', ['u32']
)
```

#### Return value
```python
'u64'
```
---------
### GroupCollections
 Stores NFT group collection data

#### Python
```python
result = substrate.query(
    'Nft', 'GroupCollections', ['u64']
)
```

#### Return value
```python
{'name': 'Bytes', 'properties': 'Bytes'}
```
---------
### LockedCollection
 Index locked collections by class ID

#### Python
```python
result = substrate.query(
    'Nft', 'LockedCollection', ['u32']
)
```

#### Return value
```python
()
```
---------
### NextAssetId
 Track the next asset ID

#### Python
```python
result = substrate.query(
    'Nft', 'NextAssetId', []
)
```

#### Return value
```python
'u64'
```
---------
### NextGroupCollectionId
 Track the next group collection ID

#### Python
```python
result = substrate.query(
    'Nft', 'NextGroupCollectionId', []
)
```

#### Return value
```python
'u64'
```
---------
### PromotionEnabled
 Tracks if promotion is enabled

#### Python
```python
result = substrate.query(
    'Nft', 'PromotionEnabled', []
)
```

#### Return value
```python
'bool'
```
---------
## Constants

---------
### AssetMintingFee
 The data deposit per byte to calculate fee
 Default minting price per NFT token
#### Value
```python
1000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Nft', 'AssetMintingFee')
```
---------
### ClassMintingFee
 Default minting price per NFT token class
#### Value
```python
10000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Nft', 'ClassMintingFee')
```
---------
### MaxBatchMinting
 Max batch minting
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('Nft', 'MaxBatchMinting')
```
---------
### MaxBatchTransfer
 Max transfer batch
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Nft', 'MaxBatchTransfer')
```
---------
### MaxMetadata
 Max metadata length
#### Value
```python
1024
```
#### Python
```python
constant = substrate.get_constant('Nft', 'MaxMetadata')
```
---------
### MiningResourceId
 Fungible token id for promotion incentive
#### Value
```python
{'MiningResource': 0}
```
#### Python
```python
constant = substrate.get_constant('Nft', 'MiningResourceId')
```
---------
### PalletId
 NFT Module Id
#### Value
```python
'0x6269742f626e6674'
```
#### Python
```python
constant = substrate.get_constant('Nft', 'PalletId')
```
---------
### Treasury
 Treasury
#### Value
```python
'0x6269742f74727379'
```
#### Python
```python
constant = substrate.get_constant('Nft', 'Treasury')
```
---------
## Errors

---------
### AlreadyInitialized
Attempted to initialize the metaverse after it had already been initialized.

---------
### AssetAlreadyInAuction
Asset Id is currently in an auction

---------
### AssetIdAlreadyExist
Asset Id is already exist

---------
### AssetIdNotFound
Asset Id not found

---------
### AssetInfoNotFound
Asset Info not found

---------
### AssetIsLocked
NFT Asset is locked e.g on marketplace, or other locks

---------
### ClassIdNotFound
Class Id not found

---------
### CollectionAlreadyLocked
Collection already locked

---------
### CollectionDoesNotExist
Collection id does not exist

---------
### CollectionIsLocked
Collection is locked

---------
### CollectionIsNotLocked
Collection is not locked

---------
### EmptySupporters
Error when signing support

---------
### ErrorWhenScheduledTimeCapsule
Timecapsule scheduled error

---------
### ExceedMaximumBatchMinting
Exceed maximum batch minting

---------
### ExceedMaximumBatchTransfer
Exceed maximum batch transfer

---------
### ExceedMaximumMetadataLength
Exceed maximum length metadata

---------
### ExceededMintingLimit
NFT mint limit is exceeded

---------
### HardLimitIsAlreadySet
Hard limit is already set

---------
### InsufficientBalance
Insufficient Balance

---------
### InvalidAssetType
Extrisic is called using invalid NFT type

---------
### InvalidCurrentTotalIssuance
Invalid current total issuance
Invalid current total issuance

---------
### InvalidQuantity
Invalid quantity

---------
### InvalidStackableNftAmount
Invalid stackable NFT amount

---------
### InvalidStackableNftTransfer
Invalid stackable NFT transfer (stored value is equal to zero)

---------
### NoAvailableAssetId
No available asset id

---------
### NoAvailableCollectionId
No available collection id

---------
### NoPermission
No permission

---------
### NonTransferable
Non Transferable

---------
### OnlyForTimeCapsuleCollectionType
Only Time capsule collection

---------
### RoyaltyFeeExceedLimit
NFT Royalty fee exceed 50%

---------
### SignOwnAsset
Sign your own Asset

---------
### TimeCapsuleExecutionLogicIsInvalid
Timecapsule execution logic is invalid

---------
### TimecapsuleExecutedTooEarly
Time-capsule executed too early

---------
### TotalMintedAssetsForClassExceededProposedLimit
The total amount of minted NFTs is more than the proposed hard limit

---------