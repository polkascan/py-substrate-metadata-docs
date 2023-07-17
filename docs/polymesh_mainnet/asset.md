
# Asset

---------
## Calls

---------
### accept_asset_ownership_transfer
This function is used to accept a token ownership transfer.
NB: To reject the transfer, call remove auth function in identity module.

\# Arguments
* `origin` It contains the secondary key of the caller (i.e. who signed the transaction to execute this function).
* `auth_id` Authorization ID of the token ownership transfer authorization.
#### Attributes
| Name | Type |
| -------- | -------- | 
| auth_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'accept_asset_ownership_transfer', {'auth_id': 'u64'}
)
```

---------
### accept_ticker_transfer
Accepts a ticker transfer.

Consumes the authorization `auth_id` (see `pallet_identity::consume_auth`).
NB: To reject the transfer, call remove auth function in identity module.

\# Arguments
* `origin` It contains the secondary key of the caller (i.e. who signed the transaction to execute this function).
* `auth_id` Authorization ID of ticker transfer authorization.

\#\# Errors
- `AuthorizationError::BadType` if `auth_id` is not a valid ticket transfer authorization.

#### Attributes
| Name | Type |
| -------- | -------- | 
| auth_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'accept_ticker_transfer', {'auth_id': 'u64'}
)
```

---------
### add_documents
Add documents for a given token.

\# Arguments
* `origin` is a signer that has permissions to act as an agent of `ticker`.
* `ticker` Ticker of the token.
* `docs` Documents to be attached to `ticker`.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| docs | `Vec<Document>` | 
| ticker | `Ticker` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'add_documents', {
    'docs': [
        {
            'content_hash': {
                'H128': '[u8; 16]',
                'H160': '[u8; 20]',
                'H192': '[u8; 24]',
                'H224': '[u8; 28]',
                'H256': '[u8; 32]',
                'H320': '[u8; 40]',
                'H384': '[u8; 48]',
                'H512': '[u8; 64]',
                'None': None,
            },
            'doc_type': (
                None,
                'Bytes',
            ),
            'filing_date': (
                None,
                'u64',
            ),
            'name': 'Bytes',
            'uri': 'Bytes',
        },
    ],
    'ticker': '[u8; 12]',
}
)
```

---------
### claim_classic_ticker
Claim a systematically reserved Polymath Classic (PMC) `ticker`
and transfer it to the `origin`&\#x27;s identity.

To verify that the `origin` is in control of the Ethereum account on the books,
an `ethereum_signature` containing the `origin`&\#x27;s DID as the message
must be provided by that Ethereum account.

\# Errors
- `NoSuchClassicTicker` if this is not a systematically reserved PMC ticker.
- `TickerAlreadyRegistered` if the ticker was already registered, e.g., by `origin`.
- `TickerRegistrationExpired` if the ticker&\#x27;s registration has expired.
- `BadOrigin` if not signed.
- `InvalidEthereumSignature` if the `ethereum_signature` is not valid.
- `NotAnOwner` if the ethereum account is not the owner of the PMC ticker.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| ethereum_signature | `EcdsaSignature` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'claim_classic_ticker', {
    'ethereum_signature': '[u8; 65]',
    'ticker': '[u8; 12]',
}
)
```

---------
### controller_transfer
Forces a transfer of token from `from_portfolio` to the caller&\#x27;s default portfolio.

\# Arguments
* `origin` Must be an external agent with appropriate permissions for a given ticker.
* `ticker` Ticker symbol of the asset.
* `value`  Amount of tokens need to force transfer.
* `from_portfolio` From whom portfolio tokens gets transferred.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| value | `Balance` | 
| from_portfolio | `PortfolioId` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'controller_transfer', {
    'from_portfolio': {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
    'ticker': '[u8; 12]',
    'value': 'u128',
}
)
```

---------
### create_asset
Initializes a new security token, with the initiating account as its owner.
The total supply will initially be zero. To mint tokens, use `issue`.

\# Arguments
* `origin` - contains the secondary key of the caller (i.e. who signed the transaction to execute this function).
* `name` - the name of the token.
* `ticker` - the ticker symbol of the token.
* `divisible` - a boolean to identify the divisibility status of the token.
* `asset_type` - the asset type.
* `identifiers` - a vector of asset identifiers.
* `funding_round` - name of the funding round.
* `disable_iu` - whether or not investor uniqueness enforcement should be disabled.
  This cannot be changed after creating the asset.

\#\# Errors
- `InvalidAssetIdentifier` if any of `identifiers` are invalid.
- `MaxLengthOfAssetNameExceeded` if `name`&\#x27;s length exceeds `T::AssetNameMaxLength`.
- `FundingRoundNameMaxLengthExceeded` if the name of the funding round is longer that
`T::FundingRoundNameMaxLength`.
- `AssetAlreadyCreated` if asset was already created.
- `TickerTooLong` if `ticker`&\#x27;s length is greater than `config.max_ticker_length` chain
parameter.
- `TickerNotAlphanumeric` if `ticker` is not yet registered, and contains non-alphanumeric characters or any character after first occurrence of `\0`.

\#\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| name | `AssetName` | 
| ticker | `Ticker` | 
| divisible | `bool` | 
| asset_type | `AssetType` | 
| identifiers | `Vec<AssetIdentifier>` | 
| funding_round | `Option<FundingRoundName>` | 
| disable_iu | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'create_asset', {
    'asset_type': {
        'Commodity': None,
        'Custom': 'u32',
        'Derivative': None,
        'EquityCommon': None,
        'EquityPreferred': None,
        'FixedIncome': None,
        'Fund': None,
        'NonFungible': {
            'Custom': 'u32',
            'Derivative': None,
            'FixedIncome': None,
            'Invoice': None,
        },
        'REIT': None,
        'RevenueShareAgreement': None,
        'StableCoin': None,
        'StructuredProduct': None,
    },
    'disable_iu': 'bool',
    'divisible': 'bool',
    'funding_round': (None, 'Bytes'),
    'identifiers': [
        {
            'CINS': '[u8; 9]',
            'CUSIP': '[u8; 9]',
            'FIGI': '[u8; 12]',
            'ISIN': '[u8; 12]',
            'LEI': '[u8; 20]',
        },
    ],
    'name': 'Bytes',
    'ticker': '[u8; 12]',
}
)
```

---------
### create_asset_with_custom_type
Utility extrinsic to batch `create_asset` and `register_custom_asset_type`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| name | `AssetName` | 
| ticker | `Ticker` | 
| divisible | `bool` | 
| custom_asset_type | `Vec<u8>` | 
| identifiers | `Vec<AssetIdentifier>` | 
| funding_round | `Option<FundingRoundName>` | 
| disable_iu | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'create_asset_with_custom_type', {
    'custom_asset_type': 'Bytes',
    'disable_iu': 'bool',
    'divisible': 'bool',
    'funding_round': (None, 'Bytes'),
    'identifiers': [
        {
            'CINS': '[u8; 9]',
            'CUSIP': '[u8; 9]',
            'FIGI': '[u8; 12]',
            'ISIN': '[u8; 12]',
            'LEI': '[u8; 20]',
        },
    ],
    'name': 'Bytes',
    'ticker': '[u8; 12]',
}
)
```

---------
### freeze
Freezes transfers and minting of a given token.

\# Arguments
* `origin` - the secondary key of the sender.
* `ticker` - the ticker of the token.

\#\# Errors
- `AlreadyFrozen` if `ticker` is already frozen.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'freeze', {'ticker': '[u8; 12]'}
)
```

---------
### issue
Issue, or mint, new tokens to the caller,
which must be an authorized external agent.

\# Arguments
* `origin` is a signer that has permissions to act as an agent of `ticker`.
* `ticker` of the token.
* `amount` of tokens that get issued.

\# Permissions
* Asset
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'issue', {
    'amount': 'u128',
    'ticker': '[u8; 12]',
}
)
```

---------
### make_divisible
Makes an indivisible token divisible.

\# Arguments
* `origin` is a signer that has permissions to act as an agent of `ticker`.
* `ticker` Ticker of the token.

\#\# Errors
- `AssetAlreadyDivisible` if `ticker` is already divisible.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'make_divisible', {'ticker': '[u8; 12]'}
)
```

---------
### redeem
Redeems existing tokens by reducing the balance of the caller&\#x27;s default portfolio and the total supply of the token

\# Arguments
* `origin` is a signer that has permissions to act as an agent of `ticker`.
* `ticker` Ticker of the token.
* `value` Amount of tokens to redeem.

\# Errors
- `Unauthorized` If called by someone without the appropriate external agent permissions
- `InvalidGranularity` If the amount is not divisible by 10^6 for non-divisible tokens
- `InsufficientPortfolioBalance` If the caller&\#x27;s default portfolio doesn&\#x27;t have enough free balance

\# Permissions
* Asset
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| value | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'redeem', {
    'ticker': '[u8; 12]',
    'value': 'u128',
}
)
```

---------
### redeem_from_portfolio
Redeems existing tokens by reducing the balance of the caller&\#x27;s portfolio and the total supply of the token

\# Arguments
* `origin` is a signer that has permissions to act as an agent of `ticker`.
* `ticker` Ticker of the token.
* `value` Amount of tokens to redeem.
* `portfolio` From whom portfolio tokens gets transferred.

\# Errors
- `Unauthorized` If called by someone without the appropriate external agent permissions
- `InvalidGranularity` If the amount is not divisible by 10^6 for non-divisible tokens
- `InsufficientPortfolioBalance` If the caller&\#x27;s `portfolio` doesn&\#x27;t have enough free balance
- `PortfolioDoesNotExist` If the portfolio doesn&\#x27;t exist.

\# Permissions
* Asset
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| value | `Balance` | 
| portfolio | `PortfolioKind` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'redeem_from_portfolio', {
    'portfolio': {
        'Default': None,
        'User': 'u64',
    },
    'ticker': '[u8; 12]',
    'value': 'u128',
}
)
```

---------
### register_and_set_local_asset_metadata
Registers and set local asset metadata.

\# Arguments
* `origin` is a signer that has permissions to act as an agent of `ticker`.
* `ticker` Ticker of the token.
* `name` Metadata name.
* `spec` Metadata type definition.
* `value` Metadata value.
* `details` Optional Metadata value details (expire, lock status).

\# Errors
* `AssetMetadataLocalKeyAlreadyExists` if a local metadata type with `name` already exists for `ticker`.
* `AssetMetadataNameMaxLengthExceeded` if the metadata `name` exceeds the maximum length.
* `AssetMetadataTypeDefMaxLengthExceeded` if the metadata `spec` type definition exceeds the maximum length.
* `AssetMetadataValueMaxLengthExceeded` if the metadata value exceeds the maximum length.

\# Permissions
* Agent
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| name | `AssetMetadataName` | 
| spec | `AssetMetadataSpec` | 
| value | `AssetMetadataValue` | 
| detail | `Option<AssetMetadataValueDetail<T::Moment>>` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'register_and_set_local_asset_metadata', {
    'detail': (
        None,
        {
            'expire': (None, 'u64'),
            'lock_status': {
                'Locked': None,
                'LockedUntil': 'u64',
                'Unlocked': None,
            },
        },
    ),
    'name': 'Bytes',
    'spec': {
        'description': (None, 'Bytes'),
        'type_def': (None, 'Bytes'),
        'url': (None, 'Bytes'),
    },
    'ticker': '[u8; 12]',
    'value': 'Bytes',
}
)
```

---------
### register_asset_metadata_global_type
Registers asset metadata global type.

\# Arguments
* `origin` is a signer that has permissions to act as an agent of `ticker`.
* `name` Metadata name.
* `spec` Metadata type definition.

\# Errors
* `AssetMetadataGlobalKeyAlreadyExists` if a globa metadata type with `name` already exists.
* `AssetMetadataNameMaxLengthExceeded` if the metadata `name` exceeds the maximum length.
* `AssetMetadataTypeDefMaxLengthExceeded` if the metadata `spec` type definition exceeds the maximum length.
#### Attributes
| Name | Type |
| -------- | -------- | 
| name | `AssetMetadataName` | 
| spec | `AssetMetadataSpec` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'register_asset_metadata_global_type', {
    'name': 'Bytes',
    'spec': {
        'description': (None, 'Bytes'),
        'type_def': (None, 'Bytes'),
        'url': (None, 'Bytes'),
    },
}
)
```

---------
### register_asset_metadata_local_type
Registers asset metadata local type.

\# Arguments
* `origin` is a signer that has permissions to act as an agent of `ticker`.
* `ticker` Ticker of the token.
* `name` Metadata name.
* `spec` Metadata type definition.

\# Errors
* `AssetMetadataLocalKeyAlreadyExists` if a local metadata type with `name` already exists for `ticker`.
* `AssetMetadataNameMaxLengthExceeded` if the metadata `name` exceeds the maximum length.
* `AssetMetadataTypeDefMaxLengthExceeded` if the metadata `spec` type definition exceeds the maximum length.

\# Permissions
* Agent
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| name | `AssetMetadataName` | 
| spec | `AssetMetadataSpec` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'register_asset_metadata_local_type', {
    'name': 'Bytes',
    'spec': {
        'description': (None, 'Bytes'),
        'type_def': (None, 'Bytes'),
        'url': (None, 'Bytes'),
    },
    'ticker': '[u8; 12]',
}
)
```

---------
### register_custom_asset_type
Registers a custom asset type.

The provided `ty` will be bound to an ID in storage.
The ID can then be used in `AssetType::Custom`.
Should the `ty` already exist in storage, no second ID is assigned to it.

\# Arguments
* `origin` who called the extrinsic.
* `ty` contains the string representation of the asset type.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ty | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'register_custom_asset_type', {'ty': 'Bytes'}
)
```

---------
### register_ticker
Registers a new ticker or extends validity of an existing ticker.
NB: Ticker validity does not get carry forward when renewing ticker.

\# Arguments
* `origin` It contains the secondary key of the caller (i.e. who signed the transaction to execute this function).
* `ticker` ticker to register.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'register_ticker', {'ticker': '[u8; 12]'}
)
```

---------
### remove_documents
Remove documents for a given token.

\# Arguments
* `origin` is a signer that has permissions to act as an agent of `ticker`.
* `ticker` Ticker of the token.
* `ids` Documents ids to be removed from `ticker`.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ids | `Vec<DocumentId>` | 
| ticker | `Ticker` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'remove_documents', {'ids': ['u32'], 'ticker': '[u8; 12]'}
)
```

---------
### remove_local_metadata_key
Removes the asset metadata key and value of a local key.

\# Arguments
* `origin` - the secondary key of the sender.
* `ticker` - the ticker of the local metadata key.
* `local_key` - the local metadata key.

\# Errors
 - `SecondaryKeyNotAuthorizedForAsset` - if called by someone without the appropriate external agent permissions.
 - `UnauthorizedAgent` - if called by someone without the appropriate external agent permissions.
 - `AssetMetadataKeyIsMissing` - if the key doens&\#x27;t exist.
 - `AssetMetadataValueIsLocked` - if the value of the key is locked.
 - AssetMetadataKeyBelongsToNFTCollection - if the key is a mandatory key in an NFT collection.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| local_key | `AssetMetadataLocalKey` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'remove_local_metadata_key', {
    'local_key': 'u64',
    'ticker': '[u8; 12]',
}
)
```

---------
### remove_metadata_value
Removes the asset metadata value of a metadata key.

\# Arguments
* `origin` - the secondary key of the sender.
* `ticker` - the ticker of the local metadata key.
* `metadata_key` - the metadata key that will have its value deleted.

\# Errors
 - `SecondaryKeyNotAuthorizedForAsset` - if called by someone without the appropriate external agent permissions.
 - `UnauthorizedAgent` - if called by someone without the appropriate external agent permissions.
 - `AssetMetadataKeyIsMissing` - if the key doens&\#x27;t exist.
 - `AssetMetadataValueIsLocked` - if the value of the key is locked.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| metadata_key | `AssetMetadataKey` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'remove_metadata_value', {
    'metadata_key': {
        'Global': 'u64',
        'Local': 'u64',
    },
    'ticker': '[u8; 12]',
}
)
```

---------
### rename_asset
Renames a given token.

\# Arguments
* `origin` - the secondary key of the sender.
* `ticker` - the ticker of the token.
* `name` - the new name of the token.

\#\# Errors
- `MaxLengthOfAssetNameExceeded` if length of `name` is greater than
`T::AssetNameMaxLength`.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| name | `AssetName` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'rename_asset', {
    'name': 'Bytes',
    'ticker': '[u8; 12]',
}
)
```

---------
### reserve_classic_ticker
Reserve a Polymath Classic (PMC) ticker.
Must be called by root, and assigns the ticker to a systematic DID.

\# Arguments
* `origin` which must be root.
* `classic_ticker_import` specification for the PMC ticker.
* `contract_did` to reserve the ticker to if `classic_ticker_import.is_contract` holds.
* `config` to use for expiry and ticker length.

\# Errors
* `AssetAlreadyCreated` if `classic_ticker_import.ticker` was created as an asset.
* `TickerTooLong` if the `config` considers the `classic_ticker_import.ticker` too long.
* `TickerAlreadyRegistered` if `classic_ticker_import.ticker` was already registered.
#### Attributes
| Name | Type |
| -------- | -------- | 
| classic_ticker_import | `ClassicTickerImport` | 
| contract_did | `IdentityId` | 
| config | `TickerRegistrationConfig<T::Moment>` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'reserve_classic_ticker', {
    'classic_ticker_import': {
        'eth_owner': '[u8; 20]',
        'is_contract': 'bool',
        'is_created': 'bool',
        'ticker': '[u8; 12]',
    },
    'config': {
        'max_ticker_length': 'u8',
        'registration_length': (
            None,
            'u64',
        ),
    },
    'contract_did': '[u8; 32]',
}
)
```

---------
### set_asset_metadata
Set asset metadata value.

\# Arguments
* `origin` is a signer that has permissions to act as an agent of `ticker`.
* `ticker` Ticker of the token.
* `key` Metadata key.
* `value` Metadata value.
* `details` Optional Metadata value details (expire, lock status).

\# Errors
* `AssetMetadataKeyIsMissing` if the metadata type key doesn&\#x27;t exist.
* `AssetMetadataValueIsLocked` if the metadata value for `key` is locked.
* `AssetMetadataValueMaxLengthExceeded` if the metadata value exceeds the maximum length.

\# Permissions
* Agent
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| key | `AssetMetadataKey` | 
| value | `AssetMetadataValue` | 
| detail | `Option<AssetMetadataValueDetail<T::Moment>>` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'set_asset_metadata', {
    'detail': (
        None,
        {
            'expire': (None, 'u64'),
            'lock_status': {
                'Locked': None,
                'LockedUntil': 'u64',
                'Unlocked': None,
            },
        },
    ),
    'key': {
        'Global': 'u64',
        'Local': 'u64',
    },
    'ticker': '[u8; 12]',
    'value': 'Bytes',
}
)
```

---------
### set_asset_metadata_details
Set asset metadata value details (expire, lock status).

\# Arguments
* `origin` is a signer that has permissions to act as an agent of `ticker`.
* `ticker` Ticker of the token.
* `key` Metadata key.
* `details` Metadata value details (expire, lock status).

\# Errors
* `AssetMetadataKeyIsMissing` if the metadata type key doesn&\#x27;t exist.
* `AssetMetadataValueIsLocked` if the metadata value for `key` is locked.

\# Permissions
* Agent
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| key | `AssetMetadataKey` | 
| detail | `AssetMetadataValueDetail<T::Moment>` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'set_asset_metadata_details', {
    'detail': {
        'expire': (None, 'u64'),
        'lock_status': {
            'Locked': None,
            'LockedUntil': 'u64',
            'Unlocked': None,
        },
    },
    'key': {
        'Global': 'u64',
        'Local': 'u64',
    },
    'ticker': '[u8; 12]',
}
)
```

---------
### set_funding_round
Sets the name of the current funding round.

\# Arguments
* `origin` - a signer that has permissions to act as an agent of `ticker`.
* `ticker` - the ticker of the token.
* `name` - the desired name of the current funding round.

\#\# Errors
- `FundingRoundNameMaxLengthExceeded` if length of `name` is greater than
`T::FundingRoundNameMaxLength`.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| name | `FundingRoundName` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'set_funding_round', {
    'name': 'Bytes',
    'ticker': '[u8; 12]',
}
)
```

---------
### unfreeze
Unfreezes transfers and minting of a given token.

\# Arguments
* `origin` - the secondary key of the sender.
* `ticker` - the ticker of the frozen token.

\#\# Errors
- `NotFrozen` if `ticker` is not frozen yet.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'unfreeze', {'ticker': '[u8; 12]'}
)
```

---------
### update_asset_type
Updates the type of an asset.

\# Arguments
* `origin` - the secondary key of the sender.
* `ticker` - the ticker of the token.
* `asset_type` - the new type of the token.

\#\# Errors
- `InvalidCustomAssetTypeId` if `asset_type` is of type custom and has an invalid type id.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| asset_type | `AssetType` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'update_asset_type', {
    'asset_type': {
        'Commodity': None,
        'Custom': 'u32',
        'Derivative': None,
        'EquityCommon': None,
        'EquityPreferred': None,
        'FixedIncome': None,
        'Fund': None,
        'NonFungible': {
            'Custom': 'u32',
            'Derivative': None,
            'FixedIncome': None,
            'Invoice': None,
        },
        'REIT': None,
        'RevenueShareAgreement': None,
        'StableCoin': None,
        'StructuredProduct': None,
    },
    'ticker': '[u8; 12]',
}
)
```

---------
### update_identifiers
Updates the asset identifiers.

\# Arguments
* `origin` - a signer that has permissions to act as an agent of `ticker`.
* `ticker` - the ticker of the token.
* `identifiers` - the asset identifiers to be updated in the form of a vector of pairs
   of `IdentifierType` and `AssetIdentifier` value.

\#\# Errors
- `InvalidAssetIdentifier` if `identifiers` contains any invalid identifier.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| identifiers | `Vec<AssetIdentifier>` | 

#### Python
```python
call = substrate.compose_call(
    'Asset', 'update_identifiers', {
    'identifiers': [
        {
            'CINS': '[u8; 9]',
            'CUSIP': '[u8; 9]',
            'FIGI': '[u8; 12]',
            'ISIN': '[u8; 12]',
            'LEI': '[u8; 20]',
        },
    ],
    'ticker': '[u8; 12]',
}
)
```

---------
## Events

---------
### AssetCreated
Event for creation of the asset.
caller DID/ owner DID, ticker, divisibility, asset type, beneficiary DID, disable investor uniqueness, asset name, identifiers, funding round
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `bool` | ```bool```
| None | `AssetType` | ```{'EquityCommon': None, 'EquityPreferred': None, 'Commodity': None, 'FixedIncome': None, 'REIT': None, 'Fund': None, 'RevenueShareAgreement': None, 'StructuredProduct': None, 'Derivative': None, 'Custom': 'u32', 'StableCoin': None, 'NonFungible': {'Derivative': None, 'FixedIncome': None, 'Invoice': None, 'Custom': 'u32'}}```
| None | `IdentityId` | ```[u8; 32]```
| None | `bool` | ```bool```
| None | `AssetName` | ```Bytes```
| None | `Vec<AssetIdentifier>` | ```[{'CUSIP': '[u8; 9]', 'CINS': '[u8; 9]', 'ISIN': '[u8; 12]', 'LEI': '[u8; 20]', 'FIGI': '[u8; 12]'}]```
| None | `Option<FundingRoundName>` | ```(None, 'Bytes')```

---------
### AssetFrozen
An event emitted when an asset is frozen.
Parameter: caller DID, ticker.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```

---------
### AssetOwnershipTransferred
Emit when token ownership is transferred.
caller DID / token ownership transferred to DID, ticker, from
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `IdentityId` | ```[u8; 32]```

---------
### AssetRenamed
An event emitted when a token is renamed.
Parameters: caller DID, ticker, new token name.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `AssetName` | ```Bytes```

---------
### AssetTypeChanged
An event emitted when the type of an asset changed.
Parameters: caller DID, ticker, new token type.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `AssetType` | ```{'EquityCommon': None, 'EquityPreferred': None, 'Commodity': None, 'FixedIncome': None, 'REIT': None, 'Fund': None, 'RevenueShareAgreement': None, 'StructuredProduct': None, 'Derivative': None, 'Custom': 'u32', 'StableCoin': None, 'NonFungible': {'Derivative': None, 'FixedIncome': None, 'Invoice': None, 'Custom': 'u32'}}```

---------
### AssetUnfrozen
An event emitted when an asset is unfrozen.
Parameter: caller DID, ticker.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```

---------
### ClassicTickerClaimed
A Polymath Classic token was claimed and transferred to a non-systematic DID.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `EthereumAddress` | ```[u8; 20]```

---------
### ControllerTransfer
Event for when a forced transfer takes place.
caller DID/ controller DID, ticker, Portfolio of token holder, value.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `PortfolioId` | ```{'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}```
| None | `Balance` | ```u128```

---------
### CustomAssetTypeExists
A custom asset type already exists on-chain.
caller DID, the ID of the custom asset type, the string contents registered.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `CustomAssetTypeId` | ```u32```
| None | `Vec<u8>` | ```Bytes```

---------
### CustomAssetTypeRegistered
A custom asset type was registered on-chain.
caller DID, the ID of the custom asset type, the string contents registered.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `CustomAssetTypeId` | ```u32```
| None | `Vec<u8>` | ```Bytes```

---------
### DivisibilityChanged
Event for change in divisibility.
caller DID, ticker, divisibility
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `bool` | ```bool```

---------
### DocumentAdded
A new document attached to an asset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `DocumentId` | ```u32```
| None | `Document` | ```{'uri': 'Bytes', 'content_hash': {'None': None, 'H512': '[u8; 64]', 'H384': '[u8; 48]', 'H320': '[u8; 40]', 'H256': '[u8; 32]', 'H224': '[u8; 28]', 'H192': '[u8; 24]', 'H160': '[u8; 20]', 'H128': '[u8; 16]'}, 'name': 'Bytes', 'doc_type': (None, 'Bytes'), 'filing_date': (None, 'u64')}```

---------
### DocumentRemoved
A document removed from an asset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `DocumentId` | ```u32```

---------
### ExtensionRemoved
A extension got removed.
caller DID, ticker, AccountId
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `AccountId` | ```AccountId```

---------
### FundingRoundSet
An event carrying the name of the current funding round of a ticker.
Parameters: caller DID, ticker, funding round name.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `FundingRoundName` | ```Bytes```

---------
### IdentifiersUpdated
Event emitted when any token identifiers are updated.
caller DID, ticker, a vector of (identifier type, identifier value)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `Vec<AssetIdentifier>` | ```[{'CUSIP': '[u8; 9]', 'CINS': '[u8; 9]', 'ISIN': '[u8; 12]', 'LEI': '[u8; 20]', 'FIGI': '[u8; 12]'}]```

---------
### IsIssuable
is_issuable() output
ticker, return value (true if issuable)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Ticker` | ```[u8; 12]```
| None | `bool` | ```bool```

---------
### Issued
Emit when tokens get issued.
caller DID, ticker, beneficiary DID, value, funding round, total issued in this funding round
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `IdentityId` | ```[u8; 32]```
| None | `Balance` | ```u128```
| None | `FundingRoundName` | ```Bytes```
| None | `Balance` | ```u128```

---------
### LocalMetadataKeyDeleted
An event emitted when a local metadata key has been removed.
Parameters: caller ticker, Local type name
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `AssetMetadataLocalKey` | ```u64```

---------
### MetadataValueDeleted
An event emitted when a local metadata value has been removed.
Parameters: caller ticker, Local type name
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `AssetMetadataKey` | ```{'Global': 'u64', 'Local': 'u64'}```

---------
### Redeemed
Emit when tokens get redeemed.
caller DID, ticker,  from DID, value
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `IdentityId` | ```[u8; 32]```
| None | `Balance` | ```u128```

---------
### RegisterAssetMetadataGlobalType
Register asset metadata global type.
(Global type name, Global type key, type specs)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetMetadataName` | ```Bytes```
| None | `AssetMetadataGlobalKey` | ```u64```
| None | `AssetMetadataSpec` | ```{'url': (None, 'Bytes'), 'description': (None, 'Bytes'), 'type_def': (None, 'Bytes')}```

---------
### RegisterAssetMetadataLocalType
Register asset metadata local type.
(Caller DID, ticker, Local type name, Local type key, type specs)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `AssetMetadataName` | ```Bytes```
| None | `AssetMetadataLocalKey` | ```u64```
| None | `AssetMetadataSpec` | ```{'url': (None, 'Bytes'), 'description': (None, 'Bytes'), 'type_def': (None, 'Bytes')}```

---------
### SetAssetMetadataValue
Set asset metadata value.
(Caller DID, ticker, metadata value, optional value details)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `AssetMetadataValue` | ```Bytes```
| None | `Option<AssetMetadataValueDetail<Moment>>` | ```(None, {'expire': (None, 'u64'), 'lock_status': {'Unlocked': None, 'Locked': None, 'LockedUntil': 'u64'}})```

---------
### SetAssetMetadataValueDetails
Set asset metadata value details (expire, lock status).
(Caller DID, ticker, value details)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `AssetMetadataValueDetail<Moment>` | ```{'expire': (None, 'u64'), 'lock_status': {'Unlocked': None, 'Locked': None, 'LockedUntil': 'u64'}}```

---------
### TickerRegistered
Emit when ticker is registered.
caller DID / ticker owner did, ticker, ticker owner, expiry
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `Option<Moment>` | ```(None, 'u64')```

---------
### TickerTransferred
Emit when ticker is transferred.
caller DID / ticker transferred to DID, ticker, from
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `IdentityId` | ```[u8; 32]```

---------
### Transfer
Event for transfer of tokens.
caller DID, ticker, from portfolio, to portfolio, value
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `PortfolioId` | ```{'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}```
| None | `PortfolioId` | ```{'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}```
| None | `Balance` | ```u128```

---------
### TransferWithData
An additional event to Transfer; emitted when `transfer_with_data` is called.
caller DID , ticker, from DID, to DID, value, data
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `IdentityId` | ```[u8; 32]```
| None | `IdentityId` | ```[u8; 32]```
| None | `Balance` | ```u128```
| None | `Vec<u8>` | ```Bytes```

---------
## Storage functions

---------
### AggregateBalance
 Store aggregate balance of those identities that has the same `ScopeId`.
 (Ticker, ScopeId) =&gt; Balance.

#### Python
```python
result = substrate.query(
    'Asset', 'AggregateBalance', ['[u8; 12]', '[u8; 32]']
)
```

#### Return value
```python
'u128'
```
---------
### AssetDocuments
 Documents attached to an Asset
 (ticker, doc_id) -&gt; document

#### Python
```python
result = substrate.query(
    'Asset', 'AssetDocuments', ['[u8; 12]', 'u32']
)
```

#### Return value
```python
{
    'content_hash': {
        'H128': '[u8; 16]',
        'H160': '[u8; 20]',
        'H192': '[u8; 24]',
        'H224': '[u8; 28]',
        'H256': '[u8; 32]',
        'H320': '[u8; 40]',
        'H384': '[u8; 48]',
        'H512': '[u8; 64]',
        'None': None,
    },
    'doc_type': (None, 'Bytes'),
    'filing_date': (None, 'u64'),
    'name': 'Bytes',
    'uri': 'Bytes',
}
```
---------
### AssetDocumentsIdSequence
 Per-ticker document ID counter.
 (ticker) -&gt; doc_id

#### Python
```python
result = substrate.query(
    'Asset', 'AssetDocumentsIdSequence', ['[u8; 12]']
)
```

#### Return value
```python
'u32'
```
---------
### AssetMetadataGlobalKeyToName
 Asset Metadata Global Key -&gt; Name.

#### Python
```python
result = substrate.query(
    'Asset', 'AssetMetadataGlobalKeyToName', ['u64']
)
```

#### Return value
```python
'Bytes'
```
---------
### AssetMetadataGlobalNameToKey
 Asset Metadata Global Name -&gt; Key.

#### Python
```python
result = substrate.query(
    'Asset', 'AssetMetadataGlobalNameToKey', ['Bytes']
)
```

#### Return value
```python
'u64'
```
---------
### AssetMetadataGlobalSpecs
 Asset Metadata Global Key specs.

#### Python
```python
result = substrate.query(
    'Asset', 'AssetMetadataGlobalSpecs', ['u64']
)
```

#### Return value
```python
{
    'description': (None, 'Bytes'),
    'type_def': (None, 'Bytes'),
    'url': (None, 'Bytes'),
}
```
---------
### AssetMetadataLocalKeyToName
 Asset Metadata Local Key -&gt; Name.

#### Python
```python
result = substrate.query(
    'Asset', 'AssetMetadataLocalKeyToName', ['[u8; 12]', 'u64']
)
```

#### Return value
```python
'Bytes'
```
---------
### AssetMetadataLocalNameToKey
 Asset Metadata Local Name -&gt; Key.

#### Python
```python
result = substrate.query(
    'Asset', 'AssetMetadataLocalNameToKey', ['[u8; 12]', 'Bytes']
)
```

#### Return value
```python
'u64'
```
---------
### AssetMetadataLocalSpecs
 Asset Metadata Local Key specs.

#### Python
```python
result = substrate.query(
    'Asset', 'AssetMetadataLocalSpecs', ['[u8; 12]', 'u64']
)
```

#### Return value
```python
{
    'description': (None, 'Bytes'),
    'type_def': (None, 'Bytes'),
    'url': (None, 'Bytes'),
}
```
---------
### AssetMetadataNextGlobalKey
 Next Asset Metadata Global Key.

#### Python
```python
result = substrate.query(
    'Asset', 'AssetMetadataNextGlobalKey', []
)
```

#### Return value
```python
'u64'
```
---------
### AssetMetadataNextLocalKey
 Next Asset Metadata Local Key.

#### Python
```python
result = substrate.query(
    'Asset', 'AssetMetadataNextLocalKey', ['[u8; 12]']
)
```

#### Return value
```python
'u64'
```
---------
### AssetMetadataValueDetails
 Details for an asset&#x27;s Metadata values.

#### Python
```python
result = substrate.query(
    'Asset', 'AssetMetadataValueDetails', [
    '[u8; 12]',
    {'Global': 'u64', 'Local': 'u64'},
]
)
```

#### Return value
```python
{
    'expire': (None, 'u64'),
    'lock_status': {'Locked': None, 'LockedUntil': 'u64', 'Unlocked': None},
}
```
---------
### AssetMetadataValues
 Metatdata values for an asset.

#### Python
```python
result = substrate.query(
    'Asset', 'AssetMetadataValues', [
    '[u8; 12]',
    {'Global': 'u64', 'Local': 'u64'},
]
)
```

#### Return value
```python
'Bytes'
```
---------
### AssetNames
 Asset name of the token corresponding to the token ticker.
 (ticker) -&gt; `AssetName`

#### Python
```python
result = substrate.query(
    'Asset', 'AssetNames', ['[u8; 12]']
)
```

#### Return value
```python
'Bytes'
```
---------
### AssetOwnershipRelations
 Tickers and token owned by a user
 (user, ticker) -&gt; AssetOwnership

#### Python
```python
result = substrate.query(
    'Asset', 'AssetOwnershipRelations', ['[u8; 32]', '[u8; 12]']
)
```

#### Return value
```python
('NotOwned', 'TickerOwned', 'AssetOwned')
```
---------
### BalanceOf
 The total asset ticker balance per identity.
 (ticker, DID) -&gt; Balance

#### Python
```python
result = substrate.query(
    'Asset', 'BalanceOf', ['[u8; 12]', '[u8; 32]']
)
```

#### Return value
```python
'u128'
```
---------
### BalanceOfAtScope
 Balances get stored on the basis of the `ScopeId`.
 Right now it is only helpful for the UI purposes but in future it can be used to do miracles on-chain.
 (ScopeId, IdentityId) =&gt; Balance.

#### Python
```python
result = substrate.query(
    'Asset', 'BalanceOfAtScope', ['[u8; 32]', '[u8; 32]']
)
```

#### Return value
```python
'u128'
```
---------
### ClassicTickers
 Ticker registration details on Polymath Classic / Ethereum.

#### Python
```python
result = substrate.query(
    'Asset', 'ClassicTickers', ['[u8; 12]']
)
```

#### Return value
```python
{'eth_owner': '[u8; 20]', 'is_created': 'bool'}
```
---------
### CustomTypeIdSequence
 The next `AssetType::Custom` ID in the sequence.

 Numbers in the sequence start from 1 rather than 0.

#### Python
```python
result = substrate.query(
    'Asset', 'CustomTypeIdSequence', []
)
```

#### Return value
```python
'u32'
```
---------
### CustomTypes
 Maps custom asset type ids to the registered string contents.

#### Python
```python
result = substrate.query(
    'Asset', 'CustomTypes', ['u32']
)
```

#### Return value
```python
'Bytes'
```
---------
### CustomTypesInverse
 Inverse map of `CustomTypes`, from registered string contents to custom asset type ids.

#### Python
```python
result = substrate.query(
    'Asset', 'CustomTypesInverse', ['Bytes']
)
```

#### Return value
```python
'u32'
```
---------
### DisableInvestorUniqueness
 Decides whether investor uniqueness requirement is enforced for this asset.
 `false` means that it is enforced.

 Ticker =&gt; bool.

#### Python
```python
result = substrate.query(
    'Asset', 'DisableInvestorUniqueness', ['[u8; 12]']
)
```

#### Return value
```python
'bool'
```
---------
### Frozen
 The set of frozen assets implemented as a membership map.
 ticker -&gt; bool

#### Python
```python
result = substrate.query(
    'Asset', 'Frozen', ['[u8; 12]']
)
```

#### Return value
```python
'bool'
```
---------
### FundingRound
 The name of the current funding round.
 ticker -&gt; funding round

#### Python
```python
result = substrate.query(
    'Asset', 'FundingRound', ['[u8; 12]']
)
```

#### Return value
```python
'Bytes'
```
---------
### Identifiers
 A map of a ticker name and asset identifiers.

#### Python
```python
result = substrate.query(
    'Asset', 'Identifiers', ['[u8; 12]']
)
```

#### Return value
```python
[
    {
        'CINS': '[u8; 9]',
        'CUSIP': '[u8; 9]',
        'FIGI': '[u8; 12]',
        'ISIN': '[u8; 12]',
        'LEI': '[u8; 20]',
    },
]
```
---------
### IssuedInFundingRound
 The total balances of tokens issued in all recorded funding rounds.
 (ticker, funding round) -&gt; balance

#### Python
```python
result = substrate.query(
    'Asset', 'IssuedInFundingRound', [('[u8; 12]', 'Bytes')]
)
```

#### Return value
```python
'u128'
```
---------
### ScopeIdOf
 Tracks the ScopeId of the identity for a given ticker.
 (Ticker, IdentityId) =&gt; ScopeId.

#### Python
```python
result = substrate.query(
    'Asset', 'ScopeIdOf', ['[u8; 12]', '[u8; 32]']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### StorageVersion
 Storage version.

#### Python
```python
result = substrate.query(
    'Asset', 'StorageVersion', []
)
```

#### Return value
```python
'u8'
```
---------
### TickerConfig
 Ticker registration config.
 (ticker) -&gt; TickerRegistrationConfig

#### Python
```python
result = substrate.query(
    'Asset', 'TickerConfig', []
)
```

#### Return value
```python
{'max_ticker_length': 'u8', 'registration_length': (None, 'u64')}
```
---------
### Tickers
 Ticker registration details.
 (ticker) -&gt; TickerRegistration

#### Python
```python
result = substrate.query(
    'Asset', 'Tickers', ['[u8; 12]']
)
```

#### Return value
```python
{'expiry': (None, 'u64'), 'owner': '[u8; 32]'}
```
---------
### Tokens
 Details of the token corresponding to the token ticker.
 (ticker) -&gt; SecurityToken details [returns SecurityToken struct]

#### Python
```python
result = substrate.query(
    'Asset', 'Tokens', ['[u8; 12]']
)
```

#### Return value
```python
{
    'asset_type': {
        'Commodity': None,
        'Custom': 'u32',
        'Derivative': None,
        'EquityCommon': None,
        'EquityPreferred': None,
        'FixedIncome': None,
        'Fund': None,
        'NonFungible': {
            'Custom': 'u32',
            'Derivative': None,
            'FixedIncome': None,
            'Invoice': None,
        },
        'REIT': None,
        'RevenueShareAgreement': None,
        'StableCoin': None,
        'StructuredProduct': None,
    },
    'divisible': 'bool',
    'owner_did': '[u8; 32]',
    'total_supply': 'u128',
}
```
---------
## Constants

---------
### AssetMetadataNameMaxLength
#### Value
```python
256
```
#### Python
```python
constant = substrate.get_constant('Asset', 'AssetMetadataNameMaxLength')
```
---------
### AssetMetadataTypeDefMaxLength
#### Value
```python
8192
```
#### Python
```python
constant = substrate.get_constant('Asset', 'AssetMetadataTypeDefMaxLength')
```
---------
### AssetMetadataValueMaxLength
#### Value
```python
8192
```
#### Python
```python
constant = substrate.get_constant('Asset', 'AssetMetadataValueMaxLength')
```
---------
### AssetNameMaxLength
#### Value
```python
128
```
#### Python
```python
constant = substrate.get_constant('Asset', 'AssetNameMaxLength')
```
---------
### FundingRoundNameMaxLength
#### Value
```python
128
```
#### Python
```python
constant = substrate.get_constant('Asset', 'FundingRoundNameMaxLength')
```
---------
## Errors

---------
### AlreadyFrozen
The token is already frozen.

---------
### AssetAlreadyCreated
The token has already been created.

---------
### AssetAlreadyDivisible
The token is already divisible.

---------
### AssetMetadataGlobalKeyAlreadyExists
Asset Metadata Global type already exists.

---------
### AssetMetadataKeyBelongsToNFTCollection
Attempt to delete a key that is needed for an NFT collection.

---------
### AssetMetadataKeyIsMissing
Asset Metadata key is missing.

---------
### AssetMetadataLocalKeyAlreadyExists
Asset Metadata Local type already exists for asset.

---------
### AssetMetadataNameMaxLengthExceeded
Maximum length of the asset metadata type name has been exceeded.

---------
### AssetMetadataTypeDefMaxLengthExceeded
Maximum length of the asset metadata type definition has been exceeded.

---------
### AssetMetadataValueIsEmpty
Attempt to lock a metadata value that is empty.

---------
### AssetMetadataValueIsLocked
Asset Metadata value is locked.

---------
### AssetMetadataValueMaxLengthExceeded
Maximum length of the asset metadata value has been exceeded.

---------
### BalanceOverflow
An overflow while calculating the balance.

---------
### FundingRoundNameMaxLengthExceeded
Maximum length of the funding round name has been exceeded.

---------
### IncompatibleAssetTypeUpdate
Attempt to update the type of a non fungible token to a fungible token or the other way around.

---------
### InsufficientBalance
The sender balance is not sufficient.

---------
### InvalidAssetIdentifier
Some `AssetIdentifier` was invalid.

---------
### InvalidCustomAssetTypeId
Invalid `CustomAssetTypeId`.

---------
### InvalidEthereumSignature
An invalid Ethereum `EcdsaSignature`.

---------
### InvalidGranularity
An invalid granularity.

---------
### InvalidTransfer
Transfer validation check failed.

---------
### InvestorUniquenessClaimNotAllowed
Investor Uniqueness claims are not allowed for this asset.

---------
### InvestorUniquenessNotAllowed
Investor Uniqueness not allowed.

---------
### MaxLengthOfAssetNameExceeded
Maximum length of asset name has been exceeded.

---------
### NoSuchAsset
No such token.

---------
### NoSuchClassicTicker
The given ticker is not a classic one.

---------
### NoSuchDoc
The given Document does not exist.

---------
### NotAnOwner
Not an owner of the token on Ethereum.

---------
### NotFrozen
The asset must be frozen.

---------
### SenderSameAsReceiver
Transfers to self are not allowed

---------
### TickerAlreadyRegistered
The ticker is already registered to someone else.

---------
### TickerFirstByteNotValid
Tickers should start with at least one valid byte.

---------
### TickerNotAlphanumeric
The ticker has non-alphanumeric parts.

---------
### TickerRegistrationExpired
Registration of ticker has expired.

---------
### TickerTooLong
The ticker length is over the limit.

---------
### TotalSupplyAboveLimit
The total supply is above the limit.

---------
### TotalSupplyOverflow
An overflow while calculating the total supply.

---------
### Unauthorized
The user is not authorized.

---------
### UnexpectedNonFungibleToken
Attempt to call an extrinsic that is only permitted for fungible tokens.

---------