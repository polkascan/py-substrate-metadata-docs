
# AssetManager

---------
## Calls

---------
### mint_asset
Mint asset by its asset id to a beneficiary.

* `origin`: Caller of this extrinsic, the access control is specified by `ForceOrigin`.
* `asset_id`: AssetId to be updated.
* `beneficiary`: Account to mint the asset.
* `amount`: Amount of asset being minted.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetId` | 
| beneficiary | `T::AccountId` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'AssetManager', 'mint_asset', {
    'amount': 'u128',
    'asset_id': 'u32',
    'beneficiary': 'AccountId',
}
)
```

---------
### register_asset
Register a new asset in the asset manager.

* `origin`: Caller of this extrinsic, the access control is specified by `ForceOrigin`.
* `location`: Location of the asset.
* `metadata`: Asset metadata.
* `min_balance`: Minimum balance to keep an account alive, used in conjunction with `is_sufficient`.
* `is_sufficient`: Whether this asset needs users to have an existential deposit to hold
 this asset.
#### Attributes
| Name | Type |
| -------- | -------- | 
| location | `<T::AssetConfig as AssetConfig<T>>::AssetLocation` | 
| metadata | `<T::AssetConfig as AssetConfig<T>>::AssetRegistrarMetadata` | 

#### Python
```python
call = substrate.compose_call(
    'AssetManager', 'register_asset', {
    'location': {
        'V0': {
            'Null': None,
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
                'Parent': None,
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
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X3': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X4': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X5': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X6': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X7': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X8': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
        },
        'V1': {
            'interior': {
                'Here': None,
                'X1': {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
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
    },
    'metadata': {
        'decimals': 'u8',
        'evm_address': (
            None,
            '[u8; 20]',
        ),
        'is_frozen': 'bool',
        'is_sufficient': 'bool',
        'min_balance': 'u128',
        'name': 'Bytes',
        'symbol': 'Bytes',
    },
}
)
```

---------
### set_min_xcm_fee
Set min xcm fee for asset/s on their reserve chain.

* `origin`: Caller of this extrinsic, the access control is specified by `ForceOrigin`.
* `reserve_chain`: Multilocation to be haven min xcm fee.
* `min_xcm_fee`: Amount of min_xcm_fee.
#### Attributes
| Name | Type |
| -------- | -------- | 
| reserve_chain | `<T::AssetConfig as AssetConfig<T>>::AssetLocation` | 
| min_xcm_fee | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'AssetManager', 'set_min_xcm_fee', {
    'min_xcm_fee': 'u128',
    'reserve_chain': {
        'V0': {
            'Null': None,
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
                'Parent': None,
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
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X3': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X4': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X5': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X6': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X7': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X8': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
        },
        'V1': {
            'interior': {
                'Here': None,
                'X1': {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
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
    },
}
)
```

---------
### set_units_per_second
Update an asset by its asset id in the asset manager.

* `origin`: Caller of this extrinsic, the access control is specified by `ForceOrigin`.
* `asset_id`: AssetId to be updated.
* `units_per_second`: units per second for `asset_id`
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetId` | 
| units_per_second | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'AssetManager', 'set_units_per_second', {
    'asset_id': 'u32',
    'units_per_second': 'u128',
}
)
```

---------
### update_asset_location
Update an asset by its asset id in the asset manager.

* `origin`: Caller of this extrinsic, the access control is specified by `ForceOrigin`.
* `asset_id`: AssetId to be updated.
* `location`: `location` to update the asset location.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetId` | 
| location | `<T::AssetConfig as AssetConfig<T>>::AssetLocation` | 

#### Python
```python
call = substrate.compose_call(
    'AssetManager', 'update_asset_location', {
    'asset_id': 'u32',
    'location': {
        'V0': {
            'Null': None,
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
                'Parent': None,
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
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X3': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X4': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X5': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X6': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X7': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X8': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
        },
        'V1': {
            'interior': {
                'Here': None,
                'X1': {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
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
    },
}
)
```

---------
### update_asset_metadata
Update an asset&\#x27;s metadata by its `asset_id`

* `origin`: Caller of this extrinsic, the access control is specified by `ForceOrigin`.
* `asset_id`: AssetId to be updated.
* `metadata`: new `metadata` to be associated with `asset_id`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetId` | 
| metadata | `<T::AssetConfig as AssetConfig<T>>::AssetRegistrarMetadata` | 

#### Python
```python
call = substrate.compose_call(
    'AssetManager', 'update_asset_metadata', {
    'asset_id': 'u32',
    'metadata': {
        'decimals': 'u8',
        'evm_address': (
            None,
            '[u8; 20]',
        ),
        'is_frozen': 'bool',
        'is_sufficient': 'bool',
        'min_balance': 'u128',
        'name': 'Bytes',
        'symbol': 'Bytes',
    },
}
)
```

---------
## Events

---------
### AssetLocationUpdated
An asset&\#x27;s location has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `AssetId` | ```u32```
| location | `<T::AssetConfig as AssetConfig<T>>::AssetLocation` | ```{'V0': {'Null': None, 'X1': {'Parent': None, 'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::68', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::68', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::68', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::73', 'part': 'scale_info::74'}}, 'X2': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X3': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X4': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X5': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X6': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X7': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X8': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'})}, 'V1': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::66', 'scale_info::66'), 'X3': ('scale_info::66', 'scale_info::66', 'scale_info::66'), 'X4': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X5': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X6': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X7': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X8': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66')}}}```

---------
### AssetMetadataUpdated
An asset;s metadata has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `AssetId` | ```u32```
| metadata | `<T::AssetConfig as AssetConfig<T>>::AssetRegistrarMetadata` | ```{'name': 'Bytes', 'symbol': 'Bytes', 'decimals': 'u8', 'evm_address': (None, '[u8; 20]'), 'is_frozen': 'bool', 'min_balance': 'u128', 'is_sufficient': 'bool'}```

---------
### AssetMinted
Asset minted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `AssetId` | ```u32```
| beneficiary | `T::AccountId` | ```AccountId```
| amount | `Balance` | ```u128```

---------
### AssetRegistered
A new asset registered.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `AssetId` | ```u32```
| asset_address | `<T::AssetConfig as AssetConfig<T>>::AssetLocation` | ```{'V0': {'Null': None, 'X1': {'Parent': None, 'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::68', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::68', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::68', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::73', 'part': 'scale_info::74'}}, 'X2': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X3': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X4': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X5': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X6': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X7': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X8': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'})}, 'V1': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::66', 'scale_info::66'), 'X3': ('scale_info::66', 'scale_info::66', 'scale_info::66'), 'X4': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X5': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X6': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X7': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X8': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66')}}}```
| metadata | `<T::AssetConfig as AssetConfig<T>>::AssetRegistrarMetadata` | ```{'name': 'Bytes', 'symbol': 'Bytes', 'decimals': 'u8', 'evm_address': (None, '[u8; 20]'), 'is_frozen': 'bool', 'min_balance': 'u128', 'is_sufficient': 'bool'}```

---------
### MinXcmFeeUpdated
Update min xcm fee of an asset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| reserve_chain | `<T::AssetConfig as AssetConfig<T>>::AssetLocation` | ```{'V0': {'Null': None, 'X1': {'Parent': None, 'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::68', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::68', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::68', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::73', 'part': 'scale_info::74'}}, 'X2': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X3': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X4': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X5': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X6': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X7': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X8': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'})}, 'V1': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::66', 'scale_info::66'), 'X3': ('scale_info::66', 'scale_info::66', 'scale_info::66'), 'X4': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X5': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X6': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X7': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X8': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66')}}}```
| min_xcm_fee | `u128` | ```u128```

---------
### UnitsPerSecondUpdated
Update units per second of an asset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `AssetId` | ```u32```
| units_per_second | `u128` | ```u128```

---------
## Storage functions

---------
### AllowedDestParaIds
 The count of associated assets for each para id except relaychain.

#### Python
```python
result = substrate.query(
    'AssetManager', 'AllowedDestParaIds', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### AssetIdLocation
 AssetId to MultiLocation Map.
 This is mostly useful when sending an asset to a foreign location.

#### Python
```python
result = substrate.query(
    'AssetManager', 'AssetIdLocation', ['u32']
)
```

#### Return value
```python
{
    'V0': {
        'Null': None,
        'X1': {
            'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::68'},
            'AccountIndex64': {'index': 'u64', 'network': 'scale_info::68'},
            'AccountKey20': {'key': '[u8; 20]', 'network': 'scale_info::68'},
            'GeneralIndex': 'u128',
            'GeneralKey': 'Bytes',
            'OnlyChild': None,
            'PalletInstance': 'u8',
            'Parachain': 'u32',
            'Parent': None,
            'Plurality': {'id': 'scale_info::73', 'part': 'scale_info::74'},
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
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
                'Parent': None,
                'Plurality': 'InnerStruct',
            },
        ),
    },
    'V1': {
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
            'X2': ('scale_info::66', 'scale_info::66'),
            'X3': ('scale_info::66', 'scale_info::66', 'scale_info::66'),
            'X4': (
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
            ),
            'X5': (
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
            ),
            'X6': (
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
            ),
            'X7': (
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
            ),
            'X8': (
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
                'scale_info::66',
            ),
        },
        'parents': 'u8',
    },
}
```
---------
### AssetIdMetadata
 AssetId to AssetRegistrar Map.

#### Python
```python
result = substrate.query(
    'AssetManager', 'AssetIdMetadata', ['u32']
)
```

#### Return value
```python
{
    'decimals': 'u8',
    'evm_address': (None, '[u8; 20]'),
    'is_frozen': 'bool',
    'is_sufficient': 'bool',
    'min_balance': 'u128',
    'name': 'Bytes',
    'symbol': 'Bytes',
}
```
---------
### LocationAssetId
 MultiLocation to AssetId Map.
 This is mostly useful when receiving an asset from a foreign location.

#### Python
```python
result = substrate.query(
    'AssetManager', 'LocationAssetId', [
    {
        'V0': {
            'Null': None,
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
                'Parent': None,
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
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X3': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X4': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X5': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X6': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X7': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X8': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
        },
        'V1': {
            'interior': {
                'Here': None,
                'X1': {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
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
    },
]
)
```

#### Return value
```python
'u32'
```
---------
### MinXcmFee
 Minimum xcm execution fee paid on destination chain.

#### Python
```python
result = substrate.query(
    'AssetManager', 'MinXcmFee', [
    {
        'V0': {
            'Null': None,
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
                'Parent': None,
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
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X3': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X4': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X5': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X6': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X7': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
            'X8': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Parent': None,
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
                    },
                },
            ),
        },
        'V1': {
            'interior': {
                'Here': None,
                'X1': {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': 'scale_info::68',
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': 'scale_info::68',
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': 'scale_info::68',
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': 'scale_info::73',
                        'part': 'scale_info::74',
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
    },
]
)
```

#### Return value
```python
'u128'
```
---------
### NextAssetId
 Get the next available AssetId.

#### Python
```python
result = substrate.query(
    'AssetManager', 'NextAssetId', []
)
```

#### Return value
```python
'u32'
```
---------
### UnitsPerSecond
 XCM transfer cost for different asset.

#### Python
```python
result = substrate.query(
    'AssetManager', 'UnitsPerSecond', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
## Errors

---------
### AssetAlreadyRegistered
Asset already registered.

---------
### CannotUpdateNativeAssetMetadata
Cannot update reserved assets metadata (0 and 1)

---------
### ErrorCreatingAsset
Error creating asset, e.g. error returned from the implementation layer.

---------
### LocationAlreadyExists
Location already exists.

---------
### MintError
Error on minting asset.

---------
### UpdateNonExistAsset
Update a non-exist asset.

---------
### UpdateParaIdError
Fail to update para id.

---------