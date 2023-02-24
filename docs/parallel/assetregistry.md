
# AssetRegistry

---------
## Calls

---------
### deregister_asset
Remove a given assetId -&gt; assetType association
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'AssetRegistry', 'deregister_asset', {'asset_id': 'u32'}
)
```

---------
### register_asset
Register new asset with the asset registry
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| asset_type | `T::AssetType` | 

#### Python
```python
call = substrate.compose_call(
    'AssetRegistry', 'register_asset', {
    'asset_id': 'u32',
    'asset_type': {
        'Xcm': {
            'interior': {
                'Here': None,
                'X1': {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                'X2': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X3': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X4': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X5': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X6': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X7': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X8': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
            },
            'parents': 'u8',
        },
    },
}
)
```

---------
### remove_fee_payment_asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_type | `T::AssetType` | 

#### Python
```python
call = substrate.compose_call(
    'AssetRegistry', 'remove_fee_payment_asset', {
    'asset_type': {
        'Xcm': {
            'interior': {
                'Here': None,
                'X1': {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                'X2': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X3': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X4': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X5': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X6': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X7': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X8': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
            },
            'parents': 'u8',
        },
    },
}
)
```

---------
### update_asset_type
Change the xcm type mapping for a given assetId
We also change this if the previous units per second where pointing at the old
assetType
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| new_asset_type | `T::AssetType` | 

#### Python
```python
call = substrate.compose_call(
    'AssetRegistry', 'update_asset_type', {
    'asset_id': 'u32',
    'new_asset_type': {
        'Xcm': {
            'interior': {
                'Here': None,
                'X1': {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                'X2': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X3': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X4': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X5': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X6': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X7': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X8': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
            },
            'parents': 'u8',
        },
    },
}
)
```

---------
### update_asset_units_per_second
Change the amount of units we are charging per execution second for a given AssetType
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_type | `T::AssetType` | 
| units_per_second | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'AssetRegistry', 'update_asset_units_per_second', {
    'asset_type': {
        'Xcm': {
            'interior': {
                'Here': None,
                'X1': {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                'X2': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X3': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X4': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X5': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X6': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X7': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X8': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
            },
            'parents': 'u8',
        },
    },
    'units_per_second': 'u128',
}
)
```

---------
## Events

---------
### AssetDeregisteredd
Removed all information related to an assetId
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| asset_type | `T::AssetType` | ```{'Xcm': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, 'X2': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X3': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X4': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X5': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X6': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X7': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X8': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'})}}}```

---------
### AssetRegistered
New asset with the asset manager is registered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| asset_type | `T::AssetType` | ```{'Xcm': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, 'X2': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X3': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X4': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X5': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X6': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X7': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X8': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'})}}}```

---------
### AssetTypeUpdated
Changed the xcm type mapping for a given asset id
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| new_asset_type | `T::AssetType` | ```{'Xcm': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, 'X2': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X3': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X4': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X5': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X6': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X7': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X8': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'})}}}```

---------
### FeePaymentAssetRemoved
Supported asset type for fee payment removed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_type | `T::AssetType` | ```{'Xcm': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, 'X2': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X3': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X4': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X5': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X6': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X7': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X8': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'})}}}```

---------
### UnitsPerSecondUpdated
Changed the amount of units we are charging per execution second for a given asset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_type | `T::AssetType` | ```{'Xcm': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, 'X2': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X3': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X4': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X5': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X6': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X7': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X8': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'})}}}```
| units_per_second | `u128` | ```u128```

---------
## Storage functions

---------
### AssetIdType
 Mapping from an asset id to asset type.
 This is mostly used when receiving transaction specifying an asset directly,
 like transferring an asset from this chain to another.

#### Python
```python
result = substrate.query(
    'AssetRegistry', 'AssetIdType', ['u32']
)
```

#### Return value
```python
{
    'Xcm': {
        'interior': {
            'Here': None,
            'X1': {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            'X2': (
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
            ),
            'X3': (
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
            ),
            'X4': (
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
            ),
            'X5': (
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
            ),
            'X6': (
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
            ),
            'X7': (
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
            ),
            'X8': (
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
            ),
        },
        'parents': 'u8',
    },
}
```
---------
### AssetTypeId
 Reverse mapping of AssetIdType. Mapping from an asset type to an asset id.
 This is mostly used when receiving a multilocation XCM message to retrieve
 the corresponding asset in which tokens should me minted.

#### Python
```python
result = substrate.query(
    'AssetRegistry', 'AssetTypeId', [
    {
        'Xcm': {
            'interior': {
                'Here': None,
                'X1': {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                'X2': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X3': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X4': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X5': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X6': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X7': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X8': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
            },
            'parents': 'u8',
        },
    },
]
)
```

#### Return value
```python
'u32'
```
---------
### AssetTypeUnitsPerSecond
 Stores the units per second for local execution for a AssetType.
 This is used to know how to charge for XCM execution in a particular
 asset
 Not all assets might contain units per second, hence the different storage

#### Python
```python
result = substrate.query(
    'AssetRegistry', 'AssetTypeUnitsPerSecond', [
    {
        'Xcm': {
            'interior': {
                'Here': None,
                'X1': {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                'X2': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X3': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X4': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X5': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X6': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X7': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
                'X8': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::65',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::65',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::65',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::69',
                            'part': 'scale_info::70',
                        },
                    },
                ),
            },
            'parents': 'u8',
        },
    },
]
)
```

#### Return value
```python
'u128'
```
---------
### SupportedFeePaymentAssets

#### Python
```python
result = substrate.query(
    'AssetRegistry', 'SupportedFeePaymentAssets', []
)
```

#### Return value
```python
[
    {
        'Xcm': {
            'interior': {
                'Here': None,
                'X1': {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': 'InnerStruct',
                },
                'X2': ('scale_info::63', 'scale_info::63'),
                'X3': ('scale_info::63', 'scale_info::63', 'scale_info::63'),
                'X4': (
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                ),
                'X5': (
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                ),
                'X6': (
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                ),
                'X7': (
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                ),
                'X8': (
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                    'scale_info::63',
                ),
            },
            'parents': 'u8',
        },
    },
]
```
---------
## Errors

---------
### AssetAlreadyExists

---------
### AssetDoesNotExist

---------