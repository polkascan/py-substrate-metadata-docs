
# NftFractionalization

---------
## Calls

---------
### fractionalize
See [`Pallet::fractionalize`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| nft_collection_id | `T::NftCollectionId` | 
| nft_id | `T::NftId` | 
| asset_id | `AssetIdOf<T>` | 
| beneficiary | `AccountIdLookupOf<T>` | 
| fractions | `AssetBalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'NftFractionalization', 'fractionalize', {
    'asset_id': 'u32',
    'beneficiary': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'fractions': 'u128',
    'nft_collection_id': 'u32',
    'nft_id': 'u32',
}
)
```

---------
### unify
See [`Pallet::unify`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| nft_collection_id | `T::NftCollectionId` | 
| nft_id | `T::NftId` | 
| asset_id | `AssetIdOf<T>` | 
| beneficiary | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'NftFractionalization', 'unify', {
    'asset_id': 'u32',
    'beneficiary': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'nft_collection_id': 'u32',
    'nft_id': 'u32',
}
)
```

---------
## Events

---------
### NftFractionalized
An NFT was successfully fractionalized.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| nft_collection | `T::NftCollectionId` | ```u32```
| nft | `T::NftId` | ```u32```
| fractions | `AssetBalanceOf<T>` | ```u128```
| asset | `AssetIdOf<T>` | ```u32```
| beneficiary | `T::AccountId` | ```AccountId```

---------
### NftUnified
An NFT was successfully returned back.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| nft_collection | `T::NftCollectionId` | ```u32```
| nft | `T::NftId` | ```u32```
| asset | `AssetIdOf<T>` | ```u32```
| beneficiary | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### NftToAsset
 Keeps track of the corresponding NFT ID, asset ID and amount minted.

#### Python
```python
result = substrate.query(
    'NftFractionalization', 'NftToAsset', [('u32', 'u32')]
)
```

#### Return value
```python
{
    'asset': 'u32',
    'asset_creator': 'AccountId',
    'deposit': 'u128',
    'fractions': 'u128',
}
```
---------
## Constants

---------
### Deposit
 The deposit paid by the user locking an NFT. The deposit is returned to the original NFT
 owner when the asset is unified and the NFT is unlocked.
#### Value
```python
100000000000
```
#### Python
```python
constant = substrate.get_constant('NftFractionalization', 'Deposit')
```
---------
### NewAssetName
 The newly created asset&#x27;s name.
#### Value
```python
'Frac'
```
#### Python
```python
constant = substrate.get_constant('NftFractionalization', 'NewAssetName')
```
---------
### NewAssetSymbol
 The newly created asset&#x27;s symbol.
#### Value
```python
'FRAC'
```
#### Python
```python
constant = substrate.get_constant('NftFractionalization', 'NewAssetSymbol')
```
---------
### PalletId
 The pallet&#x27;s id, used for deriving its sovereign account ID.
#### Value
```python
'0x6672616374696f6e'
```
#### Python
```python
constant = substrate.get_constant('NftFractionalization', 'PalletId')
```
---------
### StringLimit
 The maximum length of a name or symbol stored on-chain.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('NftFractionalization', 'StringLimit')
```
---------
## Errors

---------
### IncorrectAssetId
Asset ID does not correspond to locked NFT.

---------
### NftNotFound
NFT doesn&\#x27;t exist.

---------
### NftNotFractionalized
NFT has not yet been fractionalised.

---------
### NoPermission
The signing account has no permission to do the operation.

---------