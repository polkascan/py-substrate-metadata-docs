
# RioAssetsExt

---------
## Calls

---------
### create
create a new asset with full permissions granted to whoever make the call
*sudo or proposal approved only*
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 
| asset_info | `AssetInfo<BoundedVec<u8, T::StringLimit>>` | 

#### Python
```python
call = substrate.compose_call(
    'RioAssetsExt', 'create', {
    'asset_info': {
        'chain': (
            'Rio',
            'Bitcoin',
            'Litecoin',
            'Ethereum',
            'EOS',
            'Polkadot',
            'Kusama',
            'ChainX',
        ),
        'decimals': 'u8',
        'desc': 'Bytes',
        'name': 'Bytes',
        'symbol': 'Bytes',
    },
    'currency_id': 'u32',
}
)
```

---------
### offline_asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'RioAssetsExt', 'offline_asset', {'currency_id': 'u32'}
)
```

---------
### online_asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'RioAssetsExt', 'online_asset', {'currency_id': 'u32'}
)
```

---------
### update_asset_info
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 
| asset_info | `AssetInfo<BoundedVec<u8, T::StringLimit>>` | 

#### Python
```python
call = substrate.compose_call(
    'RioAssetsExt', 'update_asset_info', {
    'asset_info': {
        'chain': (
            'Rio',
            'Bitcoin',
            'Litecoin',
            'Ethereum',
            'EOS',
            'Polkadot',
            'Kusama',
            'ChainX',
        ),
        'decimals': 'u8',
        'desc': 'Bytes',
        'name': 'Bytes',
        'symbol': 'Bytes',
    },
    'currency_id': 'u32',
}
)
```

---------
### update_restriction
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 
| restrictions | `Restrictions` | 

#### Python
```python
call = substrate.compose_call(
    'RioAssetsExt', 'update_restriction', {
    'currency_id': 'u32',
    'restrictions': {'mask': 'u32'},
}
)
```

---------