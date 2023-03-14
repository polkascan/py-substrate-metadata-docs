
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
| asset_id | `T::AssetId` | 
| beneficiary | `T::AccountId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'AssetManager', 'mint_asset', {
    'amount': 'u128',
    'asset_id': 'u128',
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
| location | `T::Location` | 
| metadata | `<T::AssetConfig as AssetConfig<T>>::AssetRegistryMetadata` | 

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
        'is_sufficient': 'bool',
        'metadata': {
            'decimals': 'u8',
            'is_frozen': 'bool',
            'name': 'Bytes',
            'symbol': 'Bytes',
        },
        'min_balance': 'u128',
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
| reserve_chain | `T::Location` | 
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
| asset_id | `T::AssetId` | 
| units_per_second | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'AssetManager', 'set_units_per_second', {
    'asset_id': 'u128',
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
| asset_id | `T::AssetId` | 
| location | `T::Location` | 

#### Python
```python
call = substrate.compose_call(
    'AssetManager', 'update_asset_location', {
    'asset_id': 'u128',
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
| asset_id | `T::AssetId` | 
| metadata | `<T::AssetConfig as AssetConfig<T>>::AssetRegistryMetadata` | 

#### Python
```python
call = substrate.compose_call(
    'AssetManager', 'update_asset_metadata', {
    'asset_id': 'u128',
    'metadata': {
        'is_sufficient': 'bool',
        'metadata': {
            'decimals': 'u8',
            'is_frozen': 'bool',
            'name': 'Bytes',
            'symbol': 'Bytes',
        },
        'min_balance': 'u128',
    },
}
)
```

---------
## Events

---------
### AssetLocationUpdated
Updated the location of an asset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| location | `T::Location` | ```{'V0': {'Null': None, 'X1': {'Parent': None, 'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::68', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::68', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::68', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::73', 'part': 'scale_info::74'}}, 'X2': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X3': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X4': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X5': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X6': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X7': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X8': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'})}, 'V1': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::66', 'scale_info::66'), 'X3': ('scale_info::66', 'scale_info::66', 'scale_info::66'), 'X4': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X5': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X6': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X7': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X8': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66')}}}```

---------
### AssetMetadataUpdated
Updated the metadata of an asset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| metadata | `<T::AssetConfig as AssetConfig<T>>::AssetRegistryMetadata` | ```{'metadata': {'name': 'Bytes', 'symbol': 'Bytes', 'decimals': 'u8', 'is_frozen': 'bool'}, 'min_balance': 'u128', 'is_sufficient': 'bool'}```

---------
### AssetMinted
An asset was minted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| beneficiary | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### AssetRegistered
A new asset was registered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| location | `T::Location` | ```{'V0': {'Null': None, 'X1': {'Parent': None, 'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::68', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::68', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::68', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::73', 'part': 'scale_info::74'}}, 'X2': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X3': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X4': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X5': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X6': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X7': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X8': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'})}, 'V1': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::66', 'scale_info::66'), 'X3': ('scale_info::66', 'scale_info::66', 'scale_info::66'), 'X4': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X5': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X6': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X7': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X8': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66')}}}```
| metadata | `<T::AssetConfig as AssetConfig<T>>::AssetRegistryMetadata` | ```{'metadata': {'name': 'Bytes', 'symbol': 'Bytes', 'decimals': 'u8', 'is_frozen': 'bool'}, 'min_balance': 'u128', 'is_sufficient': 'bool'}```

---------
### MinXcmFeeUpdated
Updated the minimum XCM fee for an asset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| reserve_chain | `T::Location` | ```{'V0': {'Null': None, 'X1': {'Parent': None, 'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::68', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::68', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::68', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::73', 'part': 'scale_info::74'}}, 'X2': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X3': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X4': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X5': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X6': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X7': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}), 'X8': ({'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, {'Parent': None, 'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'})}, 'V1': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::66', 'scale_info::66'), 'X3': ('scale_info::66', 'scale_info::66', 'scale_info::66'), 'X4': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X5': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X6': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X7': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66'), 'X8': ('scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66', 'scale_info::66')}}}```
| min_xcm_fee | `u128` | ```u128```

---------
### UnitsPerSecondUpdated
Updated the units-per-second for an asset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
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
 [`AssetId`](AssetConfig::AssetId) to [`MultiLocation`] Map

 This is mostly useful when sending an asset to a foreign location.

#### Python
```python
result = substrate.query(
    'AssetManager', 'AssetIdLocation', ['u128']
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
 AssetId to AssetRegistry Map.

#### Python
```python
result = substrate.query(
    'AssetManager', 'AssetIdMetadata', ['u128']
)
```

#### Return value
```python
{
    'is_sufficient': 'bool',
    'metadata': {
        'decimals': 'u8',
        'is_frozen': 'bool',
        'name': 'Bytes',
        'symbol': 'Bytes',
    },
    'min_balance': 'u128',
}
```
---------
### LocationAssetId
 [`MultiLocation`] to [`AssetId`](AssetConfig::AssetId) Map

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
'u128'
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
 The Next Available [`AssetId`](AssetConfig::AssetId)

#### Python
```python
result = substrate.query(
    'AssetManager', 'NextAssetId', []
)
```

#### Return value
```python
'u128'
```
---------
### UnitsPerSecond
 XCM transfer cost for each [`AssetId`](AssetConfig::AssetId)

#### Python
```python
result = substrate.query(
    'AssetManager', 'UnitsPerSecond', ['u128']
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
Asset Already Registered

---------
### CannotUpdateNativeAssetMetadata
Cannot Update Native Asset Metadata

---------
### ErrorCreatingAsset
An error occured while creating a new asset at the [`AssetRegistry`].

---------
### LocationAlreadyExists
Location Already Exists

---------
### MintError
An error occurred while minting an asset.

---------
### UpdateNonExistentAsset
There was an attempt to update a non-existent asset.

---------
### UpdateParaIdError
An error occurred while updating the parachain id.

---------