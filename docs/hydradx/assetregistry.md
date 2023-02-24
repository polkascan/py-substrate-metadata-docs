
# AssetRegistry

---------
## Calls

---------
### register
Register a new asset.

Asset is identified by `name` and the name must not be used to register another asset.

New asset is given `NextAssetId` - sequential asset id

Adds mapping between `name` and assigned `asset_id` so asset id can be retrieved by name too (Note: this approach is used in AMM implementation (xyk))

Emits &\#x27;Registered` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| name | `Vec<u8>` | 
| asset_type | `AssetType<T::AssetId>` | 
| existential_deposit | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'AssetRegistry', 'register', {
    'asset_type': {
        'PoolShare': ('u32', 'u32'),
        'Token': None,
    },
    'existential_deposit': 'u128',
    'name': 'Bytes',
}
)
```

---------
### set_location
Set asset native location.

Adds mapping between native location and local asset id and vice versa.

Mainly used in XCM.

Emits `LocationSet` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| location | `T::AssetNativeLocation` | 

#### Python
```python
call = substrate.compose_call(
    'AssetRegistry', 'set_location', {
    'asset_id': 'u32',
    'location': {
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
}
)
```

---------
### set_metadata
Set metadata for an asset.

- `asset_id`: Asset identifier.
- `symbol`: The exchange symbol for this asset. Limited in length by `StringLimit`.
- `decimals`: The number of decimals this asset uses to represent one unit.

Emits `MetadataSet` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| symbol | `Vec<u8>` | 
| decimals | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'AssetRegistry', 'set_metadata', {
    'asset_id': 'u32',
    'decimals': 'u8',
    'symbol': 'Bytes',
}
)
```

---------
### update
Update registered asset.

Updates also mapping between name and asset id if provided name is different than currently registered.

Emits `Updated` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| name | `Vec<u8>` | 
| asset_type | `AssetType<T::AssetId>` | 
| existential_deposit | `Option<T::Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'AssetRegistry', 'update', {
    'asset_id': 'u32',
    'asset_type': {
        'PoolShare': ('u32', 'u32'),
        'Token': None,
    },
    'existential_deposit': (
        None,
        'u128',
    ),
    'name': 'Bytes',
}
)
```

---------
## Events

---------
### LocationSet
Native location set for an asset.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| location | `T::AssetNativeLocation` | ```{'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::73', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::73', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::73', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::78', 'part': 'scale_info::79'}}, 'X2': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X3': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X4': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X5': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X6': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X7': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X8': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'})}}```

---------
### MetadataSet
Metadata set for an asset.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| symbol | `BoundedVec<u8, T::StringLimit>` | ```Bytes```
| decimals | `u8` | ```u8```

---------
### Registered
Asset was registered.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| asset_name | `BoundedVec<u8, T::StringLimit>` | ```Bytes```
| asset_type | `AssetType<T::AssetId>` | ```{'Token': None, 'PoolShare': ('u32', 'u32')}```

---------
### Updated
Asset was updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| asset_name | `BoundedVec<u8, T::StringLimit>` | ```Bytes```
| asset_type | `AssetType<T::AssetId>` | ```{'Token': None, 'PoolShare': ('u32', 'u32')}```

---------
## Storage functions

---------
### AssetIds
 Mapping between asset name and asset id.

#### Python
```python
result = substrate.query(
    'AssetRegistry', 'AssetIds', ['Bytes']
)
```

#### Return value
```python
'u32'
```
---------
### AssetLocations
 Native location of an asset.

#### Python
```python
result = substrate.query(
    'AssetRegistry', 'AssetLocations', ['u32']
)
```

#### Return value
```python
{
    'interior': {
        'Here': None,
        'X1': {
            'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::73'},
            'AccountIndex64': {'index': 'u64', 'network': 'scale_info::73'},
            'AccountKey20': {'key': '[u8; 20]', 'network': 'scale_info::73'},
            'GeneralIndex': 'u128',
            'GeneralKey': 'Bytes',
            'OnlyChild': None,
            'PalletInstance': 'u8',
            'Parachain': 'u32',
            'Plurality': {'id': 'scale_info::78', 'part': 'scale_info::79'},
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
}
```
---------
### AssetMetadataMap
 Metadata of an asset.

#### Python
```python
result = substrate.query(
    'AssetRegistry', 'AssetMetadataMap', ['u32']
)
```

#### Return value
```python
{'decimals': 'u8', 'symbol': 'Bytes'}
```
---------
### Assets
 Details of an asset.

#### Python
```python
result = substrate.query(
    'AssetRegistry', 'Assets', ['u32']
)
```

#### Return value
```python
{
    'asset_type': {'PoolShare': ('u32', 'u32'), 'Token': None},
    'existential_deposit': 'u128',
    'locked': 'bool',
    'name': 'Bytes',
}
```
---------
### LocationAssets
 Local asset for native location.

#### Python
```python
result = substrate.query(
    'AssetRegistry', 'LocationAssets', [
    {
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
                        'network': 'scale_info::73',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::73',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::73',
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
]
)
```

#### Return value
```python
'u32'
```
---------
### NextAssetId
 Next available asset id. This is sequential id assigned for each new registered asset.

#### Python
```python
result = substrate.query(
    'AssetRegistry', 'NextAssetId', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### NativeAssetId
 Native Asset Id
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('AssetRegistry', 'NativeAssetId')
```
---------
## Errors

---------
### AssetAlreadyRegistered
Asset is already registered.

---------
### AssetNotFound
Invalid asset name or symbol.

---------
### AssetNotRegistered
Asset ID is not registered in the asset-registry.

---------
### CannotUpdateLocation
Cannot update asset location

---------
### InvalidSharedAssetLen
Incorrect number of assets provided to create shared asset.

---------
### NoIdAvailable
Asset ID is not available. This only happens when it reaches the MAX value of given id type.

---------
### TooLong
Invalid asset name or symbol.

---------