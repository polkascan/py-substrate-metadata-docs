
# AssetsRegistry

---------
## Calls

---------
### register_asset
Creates an asset.

\# Parameters:

* `local_or_foreign` - Foreign asset location or unused local asset ID

* `asset_info` - Information to register the asset with, see [`AssetInfo`]

\# Emits
* `AssetRegistered`
#### Attributes
| Name | Type |
| -------- | -------- | 
| protocol_id | `[u8; 4]` | 
| nonce | `u64` | 
| location | `Option<T::ForeignAssetId>` | 
| asset_info | `AssetInfo<T::Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'AssetsRegistry', 'register_asset', {
    'asset_info': {
        'decimals': (None, 'u8'),
        'existential_deposit': 'u128',
        'name': (
            None,
            {'inner': 'Bytes'},
        ),
        'ratio': (
            None,
            {'d': 'u64', 'n': 'u64'},
        ),
        'symbol': (
            None,
            {'inner': 'Bytes'},
        ),
    },
    'location': (
        None,
        {
            'IbcIcs20': {
                'base_denom': 'Str',
                'trace_path': [
                    'scale_info::151',
                ],
            },
            'Xcm': {
                None: None,
                'V3': {
                    'interior': {
                        'Here': None,
                        'X1': {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        'X2': (
                            'scale_info::70',
                            'scale_info::70',
                        ),
                        'X3': (
                            'scale_info::70',
                            'scale_info::70',
                            'scale_info::70',
                        ),
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
            },
        },
    ),
    'nonce': 'u64',
    'protocol_id': '[u8; 4]',
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
| target_parachain_id | `u32` | 
| foreign_asset_id | `T::ForeignAssetId` | 
| amount | `Option<T::Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'AssetsRegistry', 'set_min_fee', {
    'amount': (None, 'u128'),
    'foreign_asset_id': {
        'IbcIcs20': {
            'base_denom': 'Str',
            'trace_path': [
                {
                    'channel_id': 'Str',
                    'port_id': 'Str',
                },
            ],
        },
        'Xcm': {
            None: None,
            'V3': {
                'interior': {
                    'Here': None,
                    'X1': {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::73',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::73',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::73',
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
                            'id': 'scale_info::76',
                            'part': 'scale_info::77',
                        },
                    },
                    'X2': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
    },
    'target_parachain_id': 'u32',
}
)
```

---------
### update_asset
Update stored asset information.

Emits:
* `AssetUpdated`
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::LocalAssetId` | 
| asset_info | `AssetInfoUpdate<T::Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'AssetsRegistry', 'update_asset', {
    'asset_id': 'u128',
    'asset_info': {
        'decimals': {
            'Ignore': None,
            'Set': (None, 'u8'),
        },
        'existential_deposit': {
            'Ignore': None,
            'Set': 'u128',
        },
        'name': {
            'Ignore': None,
            'Set': (
                None,
                {'inner': 'Bytes'},
            ),
        },
        'ratio': {
            'Ignore': None,
            'Set': (
                None,
                {
                    'd': 'u64',
                    'n': 'u64',
                },
            ),
        },
        'symbol': {
            'Ignore': None,
            'Set': (
                None,
                {'inner': 'Bytes'},
            ),
        },
    },
}
)
```

---------
### update_asset_location
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::LocalAssetId` | 
| location | `Option<T::ForeignAssetId>` | 

#### Python
```python
call = substrate.compose_call(
    'AssetsRegistry', 'update_asset_location', {
    'asset_id': 'u128',
    'location': (
        None,
        {
            'IbcIcs20': {
                'base_denom': 'Str',
                'trace_path': [
                    'scale_info::151',
                ],
            },
            'Xcm': {
                None: None,
                'V3': {
                    'interior': {
                        'Here': None,
                        'X1': {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        'X2': (
                            'scale_info::70',
                            'scale_info::70',
                        ),
                        'X3': (
                            'scale_info::70',
                            'scale_info::70',
                            'scale_info::70',
                        ),
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
            },
        },
    ),
}
)
```

---------
## Events

---------
### AssetLocationRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::LocalAssetId` | ```u128```

---------
### AssetLocationUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::LocalAssetId` | ```u128```
| location | `T::ForeignAssetId` | ```{'Xcm': {None: None, 'V3': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'InnerStruct', 'OnlyChild': None, 'Plurality': 'InnerStruct', 'GlobalConsensus': 'scale_info::73'}, 'X2': ('scale_info::70', 'scale_info::70'), 'X3': ('scale_info::70', 'scale_info::70', 'scale_info::70'), 'X4': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70'), 'X5': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70'), 'X6': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70'), 'X7': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70'), 'X8': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70')}}}, 'IbcIcs20': {'trace_path': ['scale_info::151'], 'base_denom': 'Str'}}```

---------
### AssetRegistered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::LocalAssetId` | ```u128```
| location | `Option<T::ForeignAssetId>` | ```(None, {'Xcm': {None: None, 'V3': {'parents': 'u8', 'interior': {'Here': None, 'X1': 'scale_info::70', 'X2': ('scale_info::70', 'scale_info::70'), 'X3': ('scale_info::70', 'scale_info::70', 'scale_info::70'), 'X4': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70'), 'X5': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70'), 'X6': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70'), 'X7': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70'), 'X8': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70')}}}, 'IbcIcs20': {'trace_path': ['scale_info::151'], 'base_denom': 'Str'}})```
| asset_info | `AssetInfo<T::Balance>` | ```{'name': (None, {'inner': 'Bytes'}), 'symbol': (None, {'inner': 'Bytes'}), 'decimals': (None, 'u8'), 'existential_deposit': 'u128', 'ratio': (None, {'n': 'u64', 'd': 'u64'})}```

---------
### AssetUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::LocalAssetId` | ```u128```
| asset_info | `AssetInfoUpdate<T::Balance>` | ```{'name': {'Ignore': None, 'Set': (None, {'inner': 'Bytes'})}, 'symbol': {'Ignore': None, 'Set': (None, {'inner': 'Bytes'})}, 'decimals': {'Ignore': None, 'Set': (None, 'u8')}, 'existential_deposit': {'Ignore': None, 'Set': 'u128'}, 'ratio': {'Ignore': None, 'Set': (None, {'n': 'u64', 'd': 'u64'})}}```

---------
### MinFeeUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| target_parachain_id | `u32` | ```u32```
| foreign_asset_id | `T::ForeignAssetId` | ```{'Xcm': {None: None, 'V3': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'InnerStruct', 'OnlyChild': None, 'Plurality': 'InnerStruct', 'GlobalConsensus': 'scale_info::73'}, 'X2': ('scale_info::70', 'scale_info::70'), 'X3': ('scale_info::70', 'scale_info::70', 'scale_info::70'), 'X4': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70'), 'X5': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70'), 'X6': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70'), 'X7': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70'), 'X8': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70')}}}, 'IbcIcs20': {'trace_path': ['scale_info::151'], 'base_denom': 'Str'}}```
| amount | `Option<T::Balance>` | ```(None, 'u128')```

---------
## Storage functions

---------
### AssetDecimals
 Decimals of an asset

#### Python
```python
result = substrate.query(
    'AssetsRegistry', 'AssetDecimals', ['u128']
)
```

#### Return value
```python
'u8'
```
---------
### AssetName
 Name of an asset

#### Python
```python
result = substrate.query(
    'AssetsRegistry', 'AssetName', ['u128']
)
```

#### Return value
```python
{'inner': 'Bytes'}
```
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
### AssetSymbol
 Symbol of an asset

#### Python
```python
result = substrate.query(
    'AssetsRegistry', 'AssetSymbol', ['u128']
)
```

#### Return value
```python
{'inner': 'Bytes'}
```
---------
### ExistentialDeposit
 The minimum balance of an asset required for the balance to be stored on chain

#### Python
```python
result = substrate.query(
    'AssetsRegistry', 'ExistentialDeposit', ['u128']
)
```

#### Return value
```python
'u128'
```
---------
### ForeignToLocal
 Mapping foreign asset to local asset.

#### Python
```python
result = substrate.query(
    'AssetsRegistry', 'ForeignToLocal', [
    {
        'IbcIcs20': {
            'base_denom': 'Str',
            'trace_path': [
                {
                    'channel_id': 'Str',
                    'port_id': 'Str',
                },
            ],
        },
        'Xcm': {
            None: None,
            'V3': {
                'interior': {
                    'Here': None,
                    'X1': {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::73',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::73',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::73',
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
                            'id': 'scale_info::76',
                            'part': 'scale_info::77',
                        },
                    },
                    'X2': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
    'IbcIcs20': {'base_denom': 'Str', 'trace_path': ['scale_info::151']},
    'Xcm': {
        None: None,
        'V3': {
            'interior': {
                'Here': None,
                'X1': {
                    'AccountId32': 'InnerStruct',
                    'AccountIndex64': 'InnerStruct',
                    'AccountKey20': 'InnerStruct',
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'InnerStruct',
                    'GlobalConsensus': 'scale_info::73',
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
        'IbcIcs20': {
            'base_denom': 'Str',
            'trace_path': [
                {
                    'channel_id': 'Str',
                    'port_id': 'Str',
                },
            ],
        },
        'Xcm': {
            None: None,
            'V3': {
                'interior': {
                    'Here': None,
                    'X1': {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::73',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::73',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::73',
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
                            'id': 'scale_info::76',
                            'part': 'scale_info::77',
                        },
                    },
                    'X2': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
                            'OnlyChild': None,
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
                            'GlobalConsensus': 'scale_info::73',
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
    },
]
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### NetworkId
 Network id, unique per chain
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('AssetsRegistry', 'NetworkId')
```
---------
## Errors

---------
### AssetAlreadyRegistered

---------
### AssetLocationIsNone

---------
### AssetNotFound

---------
### LocationIsUsed

---------
### StringExceedsMaxLength

---------