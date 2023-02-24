
# AssetManager

---------
## Calls

---------
### add_asset_type
Add the xcm type mapping for a existing assetId, other assetType still exists if any.
TODO: Change add_asset_type with internal function wrapper
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| new_asset_type | `T::ForeignAssetType` | 

#### Python
```python
call = substrate.compose_call(
    'AssetManager', 'add_asset_type', {
    'asset_id': 'u128',
    'new_asset_type': {
        'ParachainReserve': {
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
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Treasury': None,
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
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X3': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X4': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X5': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X6': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X7': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X8': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
            },
            'parents': 'u8',
        },
        'SelfReserve': None,
    },
}
)
```

---------
### register_foreign_asset_type
Register new asset with the asset manager
TODO::Reserve native token multilocation through GenesisBuild/RuntimeUpgrade
TODO::Add Multilocation filter for register
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_type | `T::ForeignAssetType` | 
| metadata | `AssetMetadata<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'AssetManager', 'register_foreign_asset_type', {
    'asset_type': {
        'ParachainReserve': {
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
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Treasury': None,
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
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X3': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X4': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X5': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X6': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X7': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X8': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
            },
            'parents': 'u8',
        },
        'SelfReserve': None,
    },
    'metadata': {
        'decimals': 'u8',
        'is_frozen': 'bool',
        'minimal_balance': 'u128',
        'name': 'Bytes',
        'symbol': 'Bytes',
    },
}
)
```

---------
### remove_asset_type
We do not allow the destroy of asset id so far; So at least one AssetTpye should be
assigned to existing AssetId Both asset_type and potential new_default_asset_type must
be an existing relation with asset_id
TODO: Change remove_asset_type with internal function wrapper
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_type | `T::ForeignAssetType` | 
| new_default_asset_type | `Option<T::ForeignAssetType>` | 

#### Python
```python
call = substrate.compose_call(
    'AssetManager', 'remove_asset_type', {
    'asset_type': {
        'ParachainReserve': {
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
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Treasury': None,
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
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X3': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X4': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X5': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X6': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X7': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X8': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
            },
            'parents': 'u8',
        },
        'SelfReserve': None,
    },
    'new_default_asset_type': (
        None,
        {
            'ParachainReserve': {
                'interior': {
                    'Here': None,
                    'X1': {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
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
            'SelfReserve': None,
        },
    ),
}
)
```

---------
### set_asset_units_per_second
Change the amount of units we are charging per execution second
for a given ForeignAssetType
0 means not support
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| units_per_second | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'AssetManager', 'set_asset_units_per_second', {
    'asset_id': 'u128',
    'units_per_second': 'u128',
}
)
```

---------
### update_foreign_asset_metadata
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| metadata | `AssetMetadata<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'AssetManager', 'update_foreign_asset_metadata', {
    'asset_id': 'u128',
    'metadata': {
        'decimals': 'u8',
        'is_frozen': 'bool',
        'minimal_balance': 'u128',
        'name': 'Bytes',
        'symbol': 'Bytes',
    },
}
)
```

---------
## Events

---------
### ForeignAssetMetadataUpdated
The foreign asset updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| metadata | `AssetMetadata<BalanceOf<T>>` | ```{'name': 'Bytes', 'symbol': 'Bytes', 'decimals': 'u8', 'minimal_balance': 'u128', 'is_frozen': 'bool'}```

---------
### ForeignAssetTrackerUpdated
AssetTracker manipulated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_asset_tracker | `T::AssetId` | ```u128```
| new_asset_tracker | `T::AssetId` | ```u128```

---------
### ForeignAssetTypeRegistered
New asset with the asset manager is registered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| asset_type | `T::ForeignAssetType` | ```{'SelfReserve': None, 'ParachainReserve': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::74', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::74', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::74', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::78', 'part': 'scale_info::79'}}, 'X2': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X3': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X4': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X5': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X6': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X7': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X8': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'})}}}```

---------
### ForeignAssetTypeRemoved
New Event gives the info about involved asset_id, removed asset_type, and the new
default asset_id and asset_type mapping after removal
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| removed_asset_type | `T::ForeignAssetType` | ```{'SelfReserve': None, 'ParachainReserve': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::74', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::74', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::74', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::78', 'part': 'scale_info::79'}}, 'X2': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X3': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X4': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X5': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X6': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X7': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X8': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'})}}}```
| default_asset_type | `T::ForeignAssetType` | ```{'SelfReserve': None, 'ParachainReserve': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::74', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::74', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::74', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::78', 'part': 'scale_info::79'}}, 'X2': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X3': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X4': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X5': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X6': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X7': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X8': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'})}}}```

---------
### UnitsPerSecondChanged
Changed the amount of units we
are charging per execution second for a given asset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| units_per_second | `u128` | ```u128```

---------
## Storage functions

---------
### AssetIdMetadata
 The storages for AssetIdMetadata.
 AssetIdMetadata: map AssetId =&gt; Option&lt;AssetMetadata&gt;

#### Python
```python
result = substrate.query(
    'AssetManager', 'AssetIdMetadata', ['u128']
)
```

#### Return value
```python
{
    'decimals': 'u8',
    'is_frozen': 'bool',
    'minimal_balance': 'u128',
    'name': 'Bytes',
    'symbol': 'Bytes',
}
```
---------
### AssetIdType
 Mapping from an asset id to asset type.
 This is mostly used when receiving transaction specifying an asset directly,
 like transferring an asset from this chain to another.

#### Python
```python
result = substrate.query(
    'AssetManager', 'AssetIdType', ['u128']
)
```

#### Return value
```python
{
    'ParachainReserve': {
        'interior': {
            'Here': None,
            'X1': {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::74'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::74',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::74',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::78',
                    'part': 'scale_info::79',
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
    'SelfReserve': None,
}
```
---------
### AssetIdUnitsPerSecond
 Stores the units per second for local execution for a AssetType.
 This is used to know how to charge for XCM execution in a particular asset
 Not all assets might contain units per second, hence the different storage

#### Python
```python
result = substrate.query(
    'AssetManager', 'AssetIdUnitsPerSecond', ['u128']
)
```

#### Return value
```python
'u128'
```
---------
### AssetTypeId
 Reverse mapping of AssetIdType. Mapping from an asset type to an asset id.
 This is mostly used when receiving a multilocation XCM message to retrieve
 the corresponding asset in which tokens should me minted.

#### Python
```python
result = substrate.query(
    'AssetManager', 'AssetTypeId', [
    {
        'ParachainReserve': {
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
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Treasury': None,
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
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X3': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X4': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X5': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X6': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X7': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
                'X8': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::74',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::74',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::74',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::78',
                            'part': 'scale_info::79',
                        },
                    },
                ),
            },
            'parents': 'u8',
        },
        'SelfReserve': None,
    },
]
)
```

#### Return value
```python
'u128'
```
---------
### ForeignAssetTracker
 Stores the tracker of foreign assets id that have been
 created so far

#### Python
```python
result = substrate.query(
    'AssetManager', 'ForeignAssetTracker', []
)
```

#### Return value
```python
'u128'
```
---------
## Errors

---------
### AssetAlreadyExists

---------
### AssetIdDoesNotExist

---------
### AssetIdLimitReached

---------
### AssetTypeDoesNotExist

---------
### DefaultAssetTypeRemoved

---------