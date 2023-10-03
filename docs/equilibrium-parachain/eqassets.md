
# EqAssets

---------
## Calls

---------
### add_asset
Constructs and adds an asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_name | `AssetName` | 
| lot | `u128` | 
| price_step | `i64` | 
| maker_fee | `Permill` | 
| taker_fee | `Permill` | 
| asset_xcm_data | `AssetXcmData` | 
| debt_weight | `Permill` | 
| buyout_priority | `u64` | 
| asset_type | `AssetType` | 
| is_dex_enabled | `bool` | 
| collateral_discount | `Percent` | 
| lending_debt_weight | `Permill` | 
| prices | `Vec<FixedI64>` | 

#### Python
```python
call = substrate.compose_call(
    'EqAssets', 'add_asset', {
    'asset_name': 'Bytes',
    'asset_type': {
        'Lp': {
            'Curve': 'u32',
            'Yield': 'u32',
        },
        'Native': None,
        'Physical': None,
        'Synthetic': None,
    },
    'asset_xcm_data': {
        'None': None,
        'OtherReserved': {
            'decimals': 'u8',
            'multi_location': {
                'interior': {
                    'Here': None,
                    'X1': {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::55',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::55',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::55',
                            ),
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': {
                            'data': '[u8; 32]',
                            'length': 'u8',
                        },
                        'GlobalConsensus': {
                            'BitcoinCash': None,
                            'BitcoinCore': None,
                            'ByFork': 'InnerStruct',
                            'ByGenesis': '[u8; 32]',
                            'Ethereum': 'InnerStruct',
                            'Kusama': None,
                            'Polkadot': None,
                            'Rococo': None,
                            'Westend': None,
                            'Wococo': None,
                        },
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::58',
                            'part': 'scale_info::59',
                        },
                    },
                    'X2': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
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
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
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
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
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
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
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
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
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
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
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
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
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
        'SelfReserved': None,
    },
    'buyout_priority': 'u64',
    'collateral_discount': 'u8',
    'debt_weight': 'u32',
    'is_dex_enabled': 'bool',
    'lending_debt_weight': 'u32',
    'lot': 'u128',
    'maker_fee': 'u32',
    'price_step': 'i64',
    'prices': ['i64'],
    'taker_fee': 'u32',
}
)
```

---------
### remove_asset
Call to remove asset from eq_assets::Assets, eq_oracle, eq_lenders and financial_pallet storages
Doesn&\#x27;t affect mm, xdot and curve pools
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `Asset` | 

#### Python
```python
call = substrate.compose_call(
    'EqAssets', 'remove_asset', {'asset_id': 'u64'}
)
```

---------
### update_asset
Updates an asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `Asset` | 
| lot | `Option<u128>` | 
| price_step | `Option<i64>` | 
| maker_fee | `Option<Permill>` | 
| taker_fee | `Option<Permill>` | 
| asset_xcm_data | `Option<AssetXcmData>` | 
| debt_weight | `Option<Permill>` | 
| buyout_priority | `Option<u64>` | 
| asset_type | `Option<AssetType>` | 
| is_dex_enabled | `Option<bool>` | 
| collateral_discount | `Option<Percent>` | 
| lending_debt_weight | `Option<Permill>` | 

#### Python
```python
call = substrate.compose_call(
    'EqAssets', 'update_asset', {
    'asset_id': 'u64',
    'asset_type': (
        None,
        {
            'Lp': {
                'Curve': 'u32',
                'Yield': 'u32',
            },
            'Native': None,
            'Physical': None,
            'Synthetic': None,
        },
    ),
    'asset_xcm_data': (
        None,
        {
            'None': None,
            'OtherReserved': {
                'decimals': 'u8',
                'multi_location': {
                    'interior': {
                        'Here': None,
                        'X1': {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::55',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        'X2': (
                            'scale_info::52',
                            'scale_info::52',
                        ),
                        'X3': (
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                        ),
                        'X4': (
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                        ),
                        'X5': (
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                        ),
                        'X6': (
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                        ),
                        'X7': (
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                        ),
                        'X8': (
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                            'scale_info::52',
                        ),
                    },
                    'parents': 'u8',
                },
            },
            'SelfReserved': None,
        },
    ),
    'buyout_priority': (None, 'u64'),
    'collateral_discount': (
        None,
        'u8',
    ),
    'debt_weight': (None, 'u32'),
    'is_dex_enabled': (None, 'bool'),
    'lending_debt_weight': (
        None,
        'u32',
    ),
    'lot': (None, 'u128'),
    'maker_fee': (None, 'u32'),
    'price_step': (None, 'i64'),
    'taker_fee': (None, 'u32'),
}
)
```

---------
## Events

---------
### DeleteAsset
Asset removed from store \[asset, asset_name\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `eq_primitives::asset::AssetIdInnerType` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### NewAsset
New asset added to store  \[asset, asset_name\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `eq_primitives::asset::AssetIdInnerType` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### UpdateAsset
Asset updated in the store \[asset, asset_name\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `eq_primitives::asset::AssetIdInnerType` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
## Storage functions

---------
### Assets

#### Python
```python
result = substrate.query(
    'EqAssets', 'Assets', []
)
```

#### Return value
```python
[
    {
        'asset_type': {
            'Lp': {'Curve': 'u32', 'Yield': 'u32'},
            'Native': None,
            'Physical': None,
            'Synthetic': None,
        },
        'asset_xcm_data': {
            'None': None,
            'OtherReserved': {
                'decimals': 'u8',
                'multi_location': {
                    'interior': 'scale_info::51',
                    'parents': 'u8',
                },
            },
            'SelfReserved': None,
        },
        'buyout_priority': 'u64',
        'collateral_discount': 'u8',
        'debt_weight': 'u32',
        'id': 'u64',
        'is_dex_enabled': 'bool',
        'lending_debt_weight': 'u32',
        'lot': 'u128',
        'maker_fee': 'u32',
        'price_step': 'i64',
        'taker_fee': 'u32',
    },
]
```
---------
### AssetsToRemove

#### Python
```python
result = substrate.query(
    'EqAssets', 'AssetsToRemove', []
)
```

#### Return value
```python
['u64']
```
---------
## Constants

---------
### MainAsset
 Network native asset
 Commissions are paid in this asset
#### Value
```python
25969
```
#### Python
```python
constant = substrate.get_constant('EqAssets', 'MainAsset')
```
---------
## Errors

---------
### AssetAlreadyExists
Asset with the same AssetId already exists

---------
### AssetAlreadyToBeRemoved
Asset was already requested to be removed

---------
### AssetNameWrongLength
Asset name is too long

---------
### AssetNameWrongSymbols
Asset name contains a wrong symbol.
Only standard latin letters and digits are allowed.

---------
### AssetNotExists
Cannot delete an asset that does not exist

---------
### CollateralDiscountNegative
Collateral discount is negative

---------
### CollateralMustBeDisabledWithoutPrices
New asset without prices cannot be collateral.

---------
### DebtWeightMoreThanOne
Debt weight cannot be over 100%

---------
### DebtWeightNegative
Debt weight cannot be negative

---------
### Native
Operation not allowed for native asset

---------
### PriceStepNegative
Price step cannot be negative

---------