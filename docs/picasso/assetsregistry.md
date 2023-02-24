
# AssetsRegistry

---------
## Calls

---------
### register_asset
Creates asset using `CurrencyFactory`.
Raises `AssetRegistered` event

Sets only required fields by `CurrencyFactory`, to upsert metadata use referenced
pallet.

\# Parameters:

`ratio` -  
Allows `bring you own gas` fees.
Set to `None` to prevent payment in this asset, only transferring.
Setting to some will NOT start minting tokens with specified ratio.

```python
 ratio = foreign_token / native_token
 amount_of_foreign_asset = amount_of_native_asset * ratio
```

`decimals` - `human` number of decimals

`ed` - same meaning as in for foreign asset account (if None, then asset is not
sufficient)
#### Attributes
| Name | Type |
| -------- | -------- | 
| location | `T::ForeignAssetId` | 
| ratio | `Rational` | 
| decimals | `Option<Exponent>` | 

#### Python
```python
call = substrate.compose_call(
    'AssetsRegistry', 'register_asset', {
    'decimals': (None, 'u8'),
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
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X3': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X4': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X5': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X6': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X7': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X8': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
        },
        'parents': 'u8',
    },
    'ratio': {'d': 'u64', 'n': 'u64'},
}
)
```

---------
### set_min_fee
Minimal amount of `foreign_asset_id` required to send message to other network.
Target network may or may not accept payment `amount`.
Assumed this is maintained up to date by technical team.
Mostly UI hint and fail fast solution.
Messages sending smaller fee will not be sent.
In theory can be updated by parachain sovereign account too.
If None, than it is well known cannot pay with that asset on target_parachain_id.
If Some(0), than price can be anything greater or equal to zero.
If Some(MAX), than actually it forbids transfers.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target_parachain_id | `ParaId` | 
| foreign_asset_id | `T::ForeignAssetId` | 
| amount | `Option<T::Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'AssetsRegistry', 'set_min_fee', {
    'amount': (None, 'u128'),
    'foreign_asset_id': {
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
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X3': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X4': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X5': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X6': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X7': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X8': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
        },
        'parents': 'u8',
    },
    'target_parachain_id': 'u32',
}
)
```

---------
### update_asset
Given well existing asset, update its remote information.
Use with caution as it allow reroute assets location.
See `register_asset` for parameters meaning.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::LocalAssetId` | 
| location | `T::ForeignAssetId` | 
| ratio | `Rational` | 
| decimals | `Option<Exponent>` | 

#### Python
```python
call = substrate.compose_call(
    'AssetsRegistry', 'update_asset', {
    'asset_id': 'u128',
    'decimals': (None, 'u8'),
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
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X3': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X4': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X5': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X6': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X7': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X8': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
        },
        'parents': 'u8',
    },
    'ratio': {'d': 'u64', 'n': 'u64'},
}
)
```

---------
## Events

---------
### AssetRegistered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::LocalAssetId` | ```u128```
| location | `T::ForeignAssetId` | ```{'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::72', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::72', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::72', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}}, 'X2': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X3': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X4': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X5': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X6': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X7': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X8': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'})}}```
| decimals | `Option<Exponent>` | ```(None, 'u8')```

---------
### AssetUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::LocalAssetId` | ```u128```
| location | `T::ForeignAssetId` | ```{'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::72', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::72', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::72', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}}, 'X2': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X3': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X4': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X5': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X6': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X7': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X8': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'})}}```
| decimals | `Option<Exponent>` | ```(None, 'u8')```

---------
### MinFeeUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| target_parachain_id | `ParaId` | ```u32```
| foreign_asset_id | `T::ForeignAssetId` | ```{'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::72', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::72', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::72', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}}, 'X2': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X3': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X4': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X5': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X6': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X7': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X8': ({'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'})}}```
| amount | `Option<T::Balance>` | ```(None, 'u128')```

---------
## Storage functions

---------
### AssetRatio
 How much of asset amount is needed to pay for one unit of native token.

#### Python
```python
result = substrate.query(
    'AssetsRegistry', 'AssetRatio', ['u128']
)
```

#### Return value
```python
{'d': 'u64', 'n': 'u64'}
```
---------
### ForeignToLocal
 Mapping foreign asset to local asset.

#### Python
```python
result = substrate.query(
    'AssetsRegistry', 'ForeignToLocal', [
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
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X3': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X4': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X5': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X6': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X7': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X8': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
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
'u128'
```
---------
### LocalToForeign
 Mapping local asset to foreign asset.

#### Python
```python
result = substrate.query(
    'AssetsRegistry', 'LocalToForeign', ['u128']
)
```

#### Return value
```python
{
    'decimals': (None, 'u8'),
    'location': {
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
            'X2': ('scale_info::70', 'scale_info::70'),
            'X3': ('scale_info::70', 'scale_info::70', 'scale_info::70'),
            'X4': (
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
            ),
            'X5': (
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
            ),
            'X6': (
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
            ),
            'X7': (
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
            ),
            'X8': (
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
                'scale_info::70',
            ),
        },
        'parents': 'u8',
    },
}
```
---------
### MinFeeAmounts

#### Python
```python
result = substrate.query(
    'AssetsRegistry', 'MinFeeAmounts', [
    'u32',
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
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X3': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X4': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X5': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X6': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X7': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
            ),
            'X8': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::72',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::72',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::72',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::76',
                        'part': 'scale_info::77',
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
'u128'
```
---------
## Errors

---------
### AssetNotFound

---------
### ForeignAssetAlreadyRegistered

---------