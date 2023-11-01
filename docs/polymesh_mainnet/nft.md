
# Nft

---------
## Calls

---------
### create_nft_collection
Cretes a new `NFTCollection`.

\# Arguments
* `origin` - contains the secondary key of the caller (i.e. who signed the transaction to execute this function).
* `ticker` - the ticker associated to the new collection.
* `nft_type` - in case the asset hasn&\#x27;t been created yet, one will be created with the given type.
* `collection_keys` - all mandatory metadata keys that the tokens in the collection must have.

\#\# Errors
- `CollectionAlredyRegistered` - if the ticker is already associated to an NFT collection.
- `InvalidAssetType` - if the associated asset is not of type NFT.
- `MaxNumberOfKeysExceeded` - if the number of metadata keys for the collection is greater than the maximum allowed.
- `UnregisteredMetadataKey` - if any of the metadata keys needed for the collection has not been registered.
- `DuplicateMetadataKey` - if a duplicate metadata keys has been passed as input.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| nft_type | `Option<NonFungibleType>` | 
| collection_keys | `NFTCollectionKeys` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'create_nft_collection', {
    'collection_keys': [
        {
            'Global': 'u64',
            'Local': 'u64',
        },
    ],
    'nft_type': (
        None,
        {
            'Custom': 'u32',
            'Derivative': None,
            'FixedIncome': None,
            'Invoice': None,
        },
    ),
    'ticker': '[u8; 12]',
}
)
```

---------
### issue_nft
Issues an NFT to the caller.

\# Arguments
* `origin` - is a signer that has permissions to act as an agent of `ticker`.
* `ticker` - the ticker of the NFT collection.
* `nft_metadata_attributes` - all mandatory metadata keys and values for the NFT.
- `portfolio_kind` - the portfolio that will receive the minted nft.

\#\# Errors
- `CollectionNotFound` - if the collection associated to the given ticker has not been created.
- `InvalidMetadataAttribute` - if the number of attributes is not equal to the number set in the collection or attempting to set a value for a key not definied in the collection.
- `DuplicateMetadataKey` - if a duplicate metadata keys has been passed as input.


\# Permissions
* Asset
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| nft_metadata_attributes | `Vec<NFTMetadataAttribute>` | 
| portfolio_kind | `PortfolioKind` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'issue_nft', {
    'nft_metadata_attributes': [
        {
            'key': {
                'Global': 'u64',
                'Local': 'u64',
            },
            'value': 'Bytes',
        },
    ],
    'portfolio_kind': {
        'Default': None,
        'User': 'u64',
    },
    'ticker': '[u8; 12]',
}
)
```

---------
### redeem_nft
Redeems the given NFT from the caller&\#x27;s portfolio.

\# Arguments
* `origin` - is a signer that has permissions to act as an agent of `ticker`.
* `ticker` - the ticker of the NFT collection.
* `nft_id` - the id of the NFT to be burned.
* `portfolio_kind` - the portfolio that contains the nft.

\#\# Errors
- `CollectionNotFound` - if the collection associated to the given ticker has not been created.
- `NFTNotFound` - if the given NFT does not exist in the portfolio.

\# Permissions
* Asset
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| nft_id | `NFTId` | 
| portfolio_kind | `PortfolioKind` | 

#### Python
```python
call = substrate.compose_call(
    'Nft', 'redeem_nft', {
    'nft_id': 'u64',
    'portfolio_kind': {
        'Default': None,
        'User': 'u64',
    },
    'ticker': '[u8; 12]',
}
)
```

---------
## Events

---------
### NFTPortfolioUpdated
Emitted when NFTs were issued, redeemed or transferred.
Contains the [`IdentityId`] of the receiver/issuer/redeemer, the [`NFTs`], the [`PortfolioId`] of the source, the [`PortfolioId`]
of the destination and the [`PortfolioUpdateReason`].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `NFTs` | ```{'ticker': '[u8; 12]', 'ids': ['u64']}```
| None | `Option<PortfolioId>` | ```(None, {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}})```
| None | `Option<PortfolioId>` | ```(None, {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}})```
| None | `PortfolioUpdateReason` | ```{'Issued': {'funding_round_name': (None, 'Bytes')}, 'Redeemed': None, 'Transferred': {'instruction_id': (None, 'u64'), 'instruction_memo': (None, '[u8; 32]')}}```

---------
### NftCollectionCreated
Emitted when a new nft collection is created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `NFTCollectionId` | ```u64```

---------
## Storage functions

---------
### Collection
 All collection details for a given collection id.

#### Python
```python
result = substrate.query(
    'Nft', 'Collection', ['u64']
)
```

#### Return value
```python
{'id': 'u64', 'ticker': '[u8; 12]'}
```
---------
### CollectionKeys
 All mandatory metadata keys for a given collection.

#### Python
```python
result = substrate.query(
    'Nft', 'CollectionKeys', ['u64']
)
```

#### Return value
```python
'scale_info::725'
```
---------
### CollectionTicker
 The collection id corresponding to each ticker.

#### Python
```python
result = substrate.query(
    'Nft', 'CollectionTicker', ['[u8; 12]']
)
```

#### Return value
```python
'u64'
```
---------
### MetadataValue
 The metadata value of an nft given its collection id, token id and metadata key.

#### Python
```python
result = substrate.query(
    'Nft', 'MetadataValue', [
    ('u64', 'u64'),
    {'Global': 'u64', 'Local': 'u64'},
]
)
```

#### Return value
```python
'Bytes'
```
---------
### NextCollectionId
 The next available id for an NFT collection.

#### Python
```python
result = substrate.query(
    'Nft', 'NextCollectionId', []
)
```

#### Return value
```python
'u64'
```
---------
### NextNFTId
 The next available id for an NFT within a collection.

#### Python
```python
result = substrate.query(
    'Nft', 'NextNFTId', ['u64']
)
```

#### Return value
```python
'u64'
```
---------
### NumberOfNFTs
 The total number of NFTs per identity.

#### Python
```python
result = substrate.query(
    'Nft', 'NumberOfNFTs', ['[u8; 12]', '[u8; 32]']
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### MaxNumberOfCollectionKeys
#### Value
```python
255
```
#### Python
```python
constant = substrate.get_constant('Nft', 'MaxNumberOfCollectionKeys')
```
---------
### MaxNumberOfNFTsCount
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Nft', 'MaxNumberOfNFTsCount')
```
---------
## Errors

---------
### BalanceOverflow
An overflow while calculating the balance.

---------
### BalanceUnderflow
An underflow while calculating the balance.

---------
### CollectionAlredyRegistered
The ticker is already associated to an NFT collection.

---------
### CollectionNotFound
The NFT collection does not exist.

---------
### DuplicateMetadataKey
A duplicate metadata key has been passed as parameter.

---------
### DuplicatedNFTId
Duplicate ids are not allowed.

---------
### InvalidAssetType
The asset must be of type non-fungible.

---------
### InvalidMetadataAttribute
Either the number of keys or the key identifier does not match the keys defined for the collection.

---------
### InvalidNFTTransferCollectionNotFound
Failed to transfer an NFT - NFT collection not found.

---------
### InvalidNFTTransferComplianceFailure
Failed to transfer an NFT - compliance failed.

---------
### InvalidNFTTransferCountOverflow
Failed to transfer an NFT - identity count would overflow.

---------
### InvalidNFTTransferFrozenAsset
Failed to transfer an NFT - asset is frozen.

---------
### InvalidNFTTransferInsufficientCount
Failed to transfer an NFT - the number of nfts in the identity is insufficient.

---------
### InvalidNFTTransferNFTNotOwned
Failed to transfer an NFT - NFT not found in portfolio.

---------
### InvalidNFTTransferSamePortfolio
Failed to transfer an NFT - attempt to move to the same portfolio.

---------
### MaxNumberOfKeysExceeded
The maximum number of metadata keys was exceeded.

---------
### MaxNumberOfNFTsPerLegExceeded
The maximum number of nfts being transferred in one leg was exceeded.

---------
### NFTNotFound
The NFT does not exist.

---------
### UnregisteredMetadataKey
At least one of the metadata keys has not been registered.

---------
### ZeroCount
It is not possible to transferr zero nft.

---------