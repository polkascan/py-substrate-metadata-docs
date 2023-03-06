
# XAssetsRegistrar

---------
## Calls

---------
### deregister
Deregister an asset with given `id`.

This asset will be marked as invalid.

This is a root-only operation.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'XAssetsRegistrar', 'deregister', {'id': 'u32'}
)
```

---------
### recover
Recover a deregister asset to the valid state.

`RegistrarHandler::on_register()` will be triggered again during the recover process.

This is a root-only operation.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `AssetId` | 
| has_mining_rights | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'XAssetsRegistrar', 'recover', {
    'has_mining_rights': 'bool',
    'id': 'u32',
}
)
```

---------
### register
Register a new foreign asset.

This is a root-only operation.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetId` | 
| asset | `AssetInfo` | 
| is_online | `bool` | 
| has_mining_rights | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'XAssetsRegistrar', 'register', {
    'asset': {
        'chain': (
            'ChainX',
            'Bitcoin',
            'Ethereum',
            'Polkadot',
        ),
        'decimals': 'u8',
        'desc': 'Bytes',
        'token': 'Bytes',
        'token_name': 'Bytes',
    },
    'asset_id': 'u32',
    'has_mining_rights': 'bool',
    'is_online': 'bool',
}
)
```

---------
### update_asset_info
Update the asset info, all the new fields are optional.

This is a root-only operation.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `AssetId` | 
| token | `Option<Token>` | 
| token_name | `Option<Token>` | 
| desc | `Option<Desc>` | 

#### Python
```python
call = substrate.compose_call(
    'XAssetsRegistrar', 'update_asset_info', {
    'desc': (None, 'Bytes'),
    'id': 'u32',
    'token': (None, 'Bytes'),
    'token_name': (None, 'Bytes'),
}
)
```

---------
## Events

---------
### Deregistered
An asset was deregistered. [asset_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```

---------
### Recovered
A deregistered asset was recovered. [asset_id, has_mining_rights]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```
| None | `bool` | ```bool```

---------
### Registered
A new asset was registered. [asset_id, has_mining_rights]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```
| None | `bool` | ```bool```

---------
## Storage functions

---------
### AssetIdsOf
 Asset id list for each Chain.

#### Python
```python
result = substrate.query(
    'XAssetsRegistrar', 'AssetIdsOf', [
    (
        'ChainX',
        'Bitcoin',
        'Ethereum',
        'Polkadot',
    ),
]
)
```

#### Return value
```python
['u32']
```
---------
### AssetInfoOf
 Asset info of each asset.

#### Python
```python
result = substrate.query(
    'XAssetsRegistrar', 'AssetInfoOf', ['u32']
)
```

#### Return value
```python
{
    'chain': ('ChainX', 'Bitcoin', 'Ethereum', 'Polkadot'),
    'decimals': 'u8',
    'desc': 'Bytes',
    'token': 'Bytes',
    'token_name': 'Bytes',
}
```
---------
### AssetOnline
 The map of asset to the online state.

#### Python
```python
result = substrate.query(
    'XAssetsRegistrar', 'AssetOnline', ['u32']
)
```

#### Return value
```python
'bool'
```
---------
### RegisteredAt
 The map of asset to the block number at which the asset was registered.

#### Python
```python
result = substrate.query(
    'XAssetsRegistrar', 'RegisteredAt', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
## Errors

---------
### AssetAlreadyExists
The asset already exists.

---------
### AssetAlreadyValid
The asset is already valid (online), no need to recover.

---------
### AssetDoesNotExist
The asset does not exist.

---------
### AssetIsInvalid
The asset is invalid (not online).

---------
### InvalidAscii
Text is invalid ASCII, only allow ASCII visible character [0x20, 0x7E]

---------
### InvalidAssetDescLength
Desc length is zero or too long

---------
### InvalidAssetTokenNameLength
Token name length is zero or too long

---------
### InvalidAssetTokenSymbolChar
Token symbol char is invalid, only allow ASCII alphanumeric character or &\#x27;-&\#x27;, &\#x27;.&\#x27;, &\#x27;|&\#x27;, &\#x27;~&\#x27;

---------
### InvalidAssetTokenSymbolLength
Token symbol length is zero or too long

---------