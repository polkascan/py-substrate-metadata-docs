
# OrmlXcm

---------
## Calls

---------
### send_as_sovereign
Send an XCM message as parachain sovereign.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `Box<VersionedMultiLocation>` | 
| message | `Box<VersionedXcm<()>>` | 

#### Python
```python
call = substrate.compose_call(
    'OrmlXcm', 'send_as_sovereign', {
    'dest': {
        None: None,
        'V2': {
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
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                ),
                'X3': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                ),
                'X4': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                ),
                'X5': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                ),
                'X6': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                ),
                'X7': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                ),
                'X8': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::111',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::111',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::111',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::114',
                            'part': 'scale_info::115',
                        },
                    },
                ),
            },
            'parents': 'u8',
        },
        'V3': {
            'interior': {
                'Here': None,
                'X1': {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::120',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::120',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::120',
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
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
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
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
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
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                ),
                'X3': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                ),
                'X4': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                ),
                'X5': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                ),
                'X6': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                ),
                'X7': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                ),
                'X8': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::120',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::120',
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
                            'id': 'scale_info::121',
                            'part': 'scale_info::122',
                        },
                    },
                ),
            },
            'parents': 'u8',
        },
    },
    'message': {
        None: None,
        'V2': [
            {
                'BuyExecution': {
                    'fees': {
                        'fun': 'scale_info::174',
                        'id': 'scale_info::173',
                    },
                    'weight_limit': {
                        'Limited': 'u64',
                        'Unlimited': None,
                    },
                },
                'ClaimAsset': {
                    'assets': [
                        'scale_info::172',
                    ],
                    'ticket': {
                        'interior': 'scale_info::108',
                        'parents': 'u8',
                    },
                },
                'ClearError': None,
                'ClearOrigin': None,
                'DepositAsset': {
                    'assets': {
                        'Definite': [
                            'scale_info::172',
                        ],
                        'Wild': 'scale_info::497',
                    },
                    'beneficiary': {
                        'interior': 'scale_info::108',
                        'parents': 'u8',
                    },
                    'max_assets': 'u32',
                },
                'DepositReserveAsset': {
                    'assets': {
                        'Definite': [
                            'scale_info::172',
                        ],
                        'Wild': 'scale_info::497',
                    },
                    'dest': {
                        'interior': 'scale_info::108',
                        'parents': 'u8',
                    },
                    'max_assets': 'u32',
                    'xcm': [
                        'scale_info::491',
                    ],
                },
                'DescendOrigin': {
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
                    'X2': (
                        'scale_info::109',
                        'scale_info::109',
                    ),
                    'X3': (
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                    ),
                    'X4': (
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                    ),
                    'X5': (
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                    ),
                    'X6': (
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                    ),
                    'X7': (
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                    ),
                    'X8': (
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                        'scale_info::109',
                    ),
                },
                'ExchangeAsset': {
                    'give': {
                        'Definite': [
                            'scale_info::172',
                        ],
                        'Wild': 'scale_info::497',
                    },
                    'receive': [
                        'scale_info::172',
                    ],
                },
                'HrmpChannelAccepted': {
                    'recipient': 'u32',
                },
                'HrmpChannelClosing': {
                    'initiator': 'u32',
                    'recipient': 'u32',
                    'sender': 'u32',
                },
                'HrmpNewChannelOpenRequest': {
                    'max_capacity': 'u32',
                    'max_message_size': 'u32',
                    'sender': 'u32',
                },
                'InitiateReserveWithdraw': {
                    'assets': {
                        'Definite': [
                            'scale_info::172',
                        ],
                        'Wild': 'scale_info::497',
                    },
                    'reserve': {
                        'interior': 'scale_info::108',
                        'parents': 'u8',
                    },
                    'xcm': [
                        'scale_info::491',
                    ],
                },
                'InitiateTeleport': {
                    'assets': {
                        'Definite': [
                            'scale_info::172',
                        ],
                        'Wild': 'scale_info::497',
                    },
                    'dest': {
                        'interior': 'scale_info::108',
                        'parents': 'u8',
                    },
                    'xcm': [
                        'scale_info::491',
                    ],
                },
                'QueryHolding': {
                    'assets': {
                        'Definite': [
                            'scale_info::172',
                        ],
                        'Wild': 'scale_info::497',
                    },
                    'dest': {
                        'interior': 'scale_info::108',
                        'parents': 'u8',
                    },
                    'max_response_weight': 'u64',
                    'query_id': 'u64',
                },
                'QueryResponse': {
                    'max_weight': 'u64',
                    'query_id': 'u64',
                    'response': {
                        'Assets': [
                            'scale_info::172',
                        ],
                        'ExecutionResult': (
                            None,
                            (
                                'u32',
                                'scale_info::495',
                            ),
                        ),
                        'Null': None,
                        'Version': 'u32',
                    },
                },
                'ReceiveTeleportedAsset': [
                    'scale_info::172',
                ],
                'RefundSurplus': None,
                'ReportError': {
                    'dest': {
                        'interior': 'scale_info::108',
                        'parents': 'u8',
                    },
                    'max_response_weight': 'u64',
                    'query_id': 'u64',
                },
                'ReserveAssetDeposited': [
                    'scale_info::172',
                ],
                'SetAppendix': [
                    'scale_info::491',
                ],
                'SetErrorHandler': [
                    'scale_info::491',
                ],
                'SubscribeVersion': {
                    'max_response_weight': 'u64',
                    'query_id': 'u64',
                },
                'Transact': {
                    'call': {
                        'encoded': 'Bytes',
                    },
                    'origin_type': (
                        'Native',
                        'SovereignAccount',
                        'Superuser',
                        'Xcm',
                    ),
                    'require_weight_at_most': 'u64',
                },
                'TransferAsset': {
                    'assets': [
                        'scale_info::172',
                    ],
                    'beneficiary': {
                        'interior': 'scale_info::108',
                        'parents': 'u8',
                    },
                },
                'TransferReserveAsset': {
                    'assets': [
                        'scale_info::172',
                    ],
                    'dest': {
                        'interior': 'scale_info::108',
                        'parents': 'u8',
                    },
                    'xcm': [
                        'scale_info::491',
                    ],
                },
                'Trap': 'u64',
                'UnsubscribeVersion': None,
                'WithdrawAsset': [
                    'scale_info::172',
                ],
            },
        ],
        'V3': [
            {
                'AliasOrigin': {
                    'interior': {
                        'Here': None,
                        'X1': 'scale_info::118',
                        'X2': (
                            'scale_info::118',
                            'scale_info::118',
                        ),
                        'X3': (
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                        ),
                        'X4': (
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                        ),
                        'X5': (
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                        ),
                        'X6': (
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                        ),
                        'X7': (
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                        ),
                        'X8': (
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                        ),
                    },
                    'parents': 'u8',
                },
                'BurnAsset': [
                    'scale_info::149',
                ],
                'BuyExecution': {
                    'fees': {
                        'fun': 'scale_info::151',
                        'id': 'scale_info::150',
                    },
                    'weight_limit': {
                        'Limited': 'scale_info::8',
                        'Unlimited': None,
                    },
                },
                'ClaimAsset': {
                    'assets': [
                        'scale_info::149',
                    ],
                    'ticket': {
                        'interior': 'scale_info::117',
                        'parents': 'u8',
                    },
                },
                'ClearError': None,
                'ClearOrigin': None,
                'ClearTopic': None,
                'ClearTransactStatus': None,
                'DepositAsset': {
                    'assets': {
                        'Definite': [
                            'scale_info::149',
                        ],
                        'Wild': 'scale_info::166',
                    },
                    'beneficiary': {
                        'interior': 'scale_info::117',
                        'parents': 'u8',
                    },
                },
                'DepositReserveAsset': {
                    'assets': {
                        'Definite': [
                            'scale_info::149',
                        ],
                        'Wild': 'scale_info::166',
                    },
                    'dest': {
                        'interior': 'scale_info::117',
                        'parents': 'u8',
                    },
                    'xcm': [
                        'scale_info::146',
                    ],
                },
                'DescendOrigin': {
                    'Here': None,
                    'X1': {
                        'AccountId32': 'InnerStruct',
                        'AccountIndex64': 'InnerStruct',
                        'AccountKey20': 'InnerStruct',
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'InnerStruct',
                        'GlobalConsensus': 'scale_info::120',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': 'InnerStruct',
                    },
                    'X2': (
                        'scale_info::118',
                        'scale_info::118',
                    ),
                    'X3': (
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                    ),
                    'X4': (
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                    ),
                    'X5': (
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                    ),
                    'X6': (
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                    ),
                    'X7': (
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                    ),
                    'X8': (
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                        'scale_info::118',
                    ),
                },
                'ExchangeAsset': {
                    'give': {
                        'Definite': [
                            'scale_info::149',
                        ],
                        'Wild': 'scale_info::166',
                    },
                    'maximal': 'bool',
                    'want': [
                        'scale_info::149',
                    ],
                },
                'ExpectAsset': [
                    'scale_info::149',
                ],
                'ExpectError': (
                    None,
                    (
                        'u32',
                        'scale_info::140',
                    ),
                ),
                'ExpectOrigin': (
                    None,
                    {
                        'interior': 'scale_info::117',
                        'parents': 'u8',
                    },
                ),
                'ExpectPallet': {
                    'crate_major': 'u32',
                    'index': 'u32',
                    'min_crate_minor': 'u32',
                    'module_name': 'Bytes',
                    'name': 'Bytes',
                },
                'ExpectTransactStatus': {
                    'Error': 'Bytes',
                    'Success': None,
                    'TruncatedError': 'Bytes',
                },
                'ExportMessage': {
                    'destination': {
                        'Here': None,
                        'X1': 'scale_info::118',
                        'X2': (
                            'scale_info::118',
                            'scale_info::118',
                        ),
                        'X3': (
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                        ),
                        'X4': (
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                        ),
                        'X5': (
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                        ),
                        'X6': (
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                        ),
                        'X7': (
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                        ),
                        'X8': (
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                            'scale_info::118',
                        ),
                    },
                    'network': {
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
                    'xcm': [
                        'scale_info::146',
                    ],
                },
                'HrmpChannelAccepted': {
                    'recipient': 'u32',
                },
                'HrmpChannelClosing': {
                    'initiator': 'u32',
                    'recipient': 'u32',
                    'sender': 'u32',
                },
                'HrmpNewChannelOpenRequest': {
                    'max_capacity': 'u32',
                    'max_message_size': 'u32',
                    'sender': 'u32',
                },
                'InitiateReserveWithdraw': {
                    'assets': {
                        'Definite': [
                            'scale_info::149',
                        ],
                        'Wild': 'scale_info::166',
                    },
                    'reserve': {
                        'interior': 'scale_info::117',
                        'parents': 'u8',
                    },
                    'xcm': [
                        'scale_info::146',
                    ],
                },
                'InitiateTeleport': {
                    'assets': {
                        'Definite': [
                            'scale_info::149',
                        ],
                        'Wild': 'scale_info::166',
                    },
                    'dest': {
                        'interior': 'scale_info::117',
                        'parents': 'u8',
                    },
                    'xcm': [
                        'scale_info::146',
                    ],
                },
                'LockAsset': {
                    'asset': {
                        'fun': 'scale_info::151',
                        'id': 'scale_info::150',
                    },
                    'unlocker': {
                        'interior': 'scale_info::117',
                        'parents': 'u8',
                    },
                },
                'NoteUnlockable': {
                    'asset': {
                        'fun': 'scale_info::151',
                        'id': 'scale_info::150',
                    },
                    'owner': {
                        'interior': 'scale_info::117',
                        'parents': 'u8',
                    },
                },
                'QueryPallet': {
                    'module_name': 'Bytes',
                    'response_info': {
                        'destination': 'scale_info::116',
                        'max_weight': 'scale_info::8',
                        'query_id': 'u64',
                    },
                },
                'QueryResponse': {
                    'max_weight': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                    'querier': (
                        None,
                        'scale_info::116',
                    ),
                    'query_id': 'u64',
                    'response': {
                        'Assets': [
                            'scale_info::149',
                        ],
                        'DispatchResult': 'scale_info::160',
                        'ExecutionResult': (
                            None,
                            (
                                'u32',
                                'scale_info::140',
                            ),
                        ),
                        'Null': None,
                        'PalletsInfo': [
                            'scale_info::159',
                        ],
                        'Version': 'u32',
                    },
                },
                'ReceiveTeleportedAsset': [
                    'scale_info::149',
                ],
                'RefundSurplus': None,
                'ReportError': {
                    'destination': {
                        'interior': 'scale_info::117',
                        'parents': 'u8',
                    },
                    'max_weight': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                    'query_id': 'u64',
                },
                'ReportHolding': {
                    'assets': {
                        'Definite': [
                            'scale_info::149',
                        ],
                        'Wild': 'scale_info::166',
                    },
                    'response_info': {
                        'destination': 'scale_info::116',
                        'max_weight': 'scale_info::8',
                        'query_id': 'u64',
                    },
                },
                'ReportTransactStatus': {
                    'destination': {
                        'interior': 'scale_info::117',
                        'parents': 'u8',
                    },
                    'max_weight': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                    'query_id': 'u64',
                },
                'RequestUnlock': {
                    'asset': {
                        'fun': 'scale_info::151',
                        'id': 'scale_info::150',
                    },
                    'locker': {
                        'interior': 'scale_info::117',
                        'parents': 'u8',
                    },
                },
                'ReserveAssetDeposited': [
                    'scale_info::149',
                ],
                'SetAppendix': [
                    'scale_info::146',
                ],
                'SetErrorHandler': [
                    'scale_info::146',
                ],
                'SetFeesMode': {
                    'jit_withdraw': 'bool',
                },
                'SetTopic': '[u8; 32]',
                'SubscribeVersion': {
                    'max_response_weight': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                    'query_id': 'u64',
                },
                'Transact': {
                    'call': {
                        'encoded': 'Bytes',
                    },
                    'origin_kind': (
                        'Native',
                        'SovereignAccount',
                        'Superuser',
                        'Xcm',
                    ),
                    'require_weight_at_most': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                },
                'TransferAsset': {
                    'assets': [
                        'scale_info::149',
                    ],
                    'beneficiary': {
                        'interior': 'scale_info::117',
                        'parents': 'u8',
                    },
                },
                'TransferReserveAsset': {
                    'assets': [
                        'scale_info::149',
                    ],
                    'dest': {
                        'interior': 'scale_info::117',
                        'parents': 'u8',
                    },
                    'xcm': [
                        'scale_info::146',
                    ],
                },
                'Trap': 'u64',
                'UniversalOrigin': {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::120',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::120',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::120',
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
                        'id': 'scale_info::121',
                        'part': 'scale_info::122',
                    },
                },
                'UnlockAsset': {
                    'asset': {
                        'fun': 'scale_info::151',
                        'id': 'scale_info::150',
                    },
                    'target': {
                        'interior': 'scale_info::117',
                        'parents': 'u8',
                    },
                },
                'UnpaidExecution': {
                    'check_origin': (
                        None,
                        'scale_info::116',
                    ),
                    'weight_limit': {
                        'Limited': 'scale_info::8',
                        'Unlimited': None,
                    },
                },
                'UnsubscribeVersion': None,
                'WithdrawAsset': [
                    'scale_info::149',
                ],
            },
        ],
    },
}
)
```

---------
## Events

---------
### Sent
XCM message sent. \[to, message\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| to | `MultiLocation` | ```{'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': {'Unit': None, 'Moniker': '[u8; 4]', 'Index': 'u32', 'Executive': None, 'Technical': None, 'Legislative': None, 'Judicial': None, 'Defense': None, 'Administration': None, 'Treasury': None}, 'part': {'Voice': None, 'Members': 'InnerStruct', 'Fraction': 'InnerStruct', 'AtLeastProportion': 'InnerStruct', 'MoreThanProportion': 'InnerStruct'}}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': {'block_number': 'u64', 'block_hash': '[u8; 32]'}, 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': {'chain_id': 'u64'}, 'BitcoinCore': None, 'BitcoinCash': None}}, 'X2': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}), 'X3': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}), 'X4': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}), 'X5': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}), 'X6': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}), 'X7': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}), 'X8': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}})}}```
| message | `Xcm<()>` | ```[{'WithdrawAsset': ['scale_info::149'], 'ReserveAssetDeposited': ['scale_info::149'], 'ReceiveTeleportedAsset': ['scale_info::149'], 'QueryResponse': {'query_id': 'u64', 'response': {'Null': None, 'Assets': ['scale_info::149'], 'ExecutionResult': (None, ('u32', 'scale_info::140')), 'Version': 'u32', 'PalletsInfo': ['scale_info::159'], 'DispatchResult': 'scale_info::160'}, 'max_weight': {'ref_time': 'u64', 'proof_size': 'u64'}, 'querier': (None, 'scale_info::116')}, 'TransferAsset': {'assets': ['scale_info::149'], 'beneficiary': {'parents': 'u8', 'interior': 'scale_info::117'}}, 'TransferReserveAsset': {'assets': ['scale_info::149'], 'dest': {'parents': 'u8', 'interior': 'scale_info::117'}, 'xcm': ['scale_info::146']}, 'Transact': {'origin_kind': ('Native', 'SovereignAccount', 'Superuser', 'Xcm'), 'require_weight_at_most': {'ref_time': 'u64', 'proof_size': 'u64'}, 'call': {'encoded': 'Bytes'}}, 'HrmpNewChannelOpenRequest': {'sender': 'u32', 'max_message_size': 'u32', 'max_capacity': 'u32'}, 'HrmpChannelAccepted': {'recipient': 'u32'}, 'HrmpChannelClosing': {'initiator': 'u32', 'sender': 'u32', 'recipient': 'u32'}, 'ClearOrigin': None, 'DescendOrigin': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'InnerStruct', 'OnlyChild': None, 'Plurality': 'InnerStruct', 'GlobalConsensus': 'scale_info::120'}, 'X2': ('scale_info::118', 'scale_info::118'), 'X3': ('scale_info::118', 'scale_info::118', 'scale_info::118'), 'X4': ('scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118'), 'X5': ('scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118'), 'X6': ('scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118'), 'X7': ('scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118'), 'X8': ('scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118')}, 'ReportError': {'destination': {'parents': 'u8', 'interior': 'scale_info::117'}, 'query_id': 'u64', 'max_weight': {'ref_time': 'u64', 'proof_size': 'u64'}}, 'DepositAsset': {'assets': {'Definite': ['scale_info::149'], 'Wild': 'scale_info::166'}, 'beneficiary': {'parents': 'u8', 'interior': 'scale_info::117'}}, 'DepositReserveAsset': {'assets': {'Definite': ['scale_info::149'], 'Wild': 'scale_info::166'}, 'dest': {'parents': 'u8', 'interior': 'scale_info::117'}, 'xcm': ['scale_info::146']}, 'ExchangeAsset': {'give': {'Definite': ['scale_info::149'], 'Wild': 'scale_info::166'}, 'want': ['scale_info::149'], 'maximal': 'bool'}, 'InitiateReserveWithdraw': {'assets': {'Definite': ['scale_info::149'], 'Wild': 'scale_info::166'}, 'reserve': {'parents': 'u8', 'interior': 'scale_info::117'}, 'xcm': ['scale_info::146']}, 'InitiateTeleport': {'assets': {'Definite': ['scale_info::149'], 'Wild': 'scale_info::166'}, 'dest': {'parents': 'u8', 'interior': 'scale_info::117'}, 'xcm': ['scale_info::146']}, 'ReportHolding': {'response_info': {'destination': 'scale_info::116', 'query_id': 'u64', 'max_weight': 'scale_info::8'}, 'assets': {'Definite': ['scale_info::149'], 'Wild': 'scale_info::166'}}, 'BuyExecution': {'fees': {'id': 'scale_info::150', 'fun': 'scale_info::151'}, 'weight_limit': {'Unlimited': None, 'Limited': 'scale_info::8'}}, 'RefundSurplus': None, 'SetErrorHandler': ['scale_info::146'], 'SetAppendix': ['scale_info::146'], 'ClearError': None, 'ClaimAsset': {'assets': ['scale_info::149'], 'ticket': {'parents': 'u8', 'interior': 'scale_info::117'}}, 'Trap': 'u64', 'SubscribeVersion': {'query_id': 'u64', 'max_response_weight': {'ref_time': 'u64', 'proof_size': 'u64'}}, 'UnsubscribeVersion': None, 'BurnAsset': ['scale_info::149'], 'ExpectAsset': ['scale_info::149'], 'ExpectOrigin': (None, {'parents': 'u8', 'interior': 'scale_info::117'}), 'ExpectError': (None, ('u32', 'scale_info::140')), 'ExpectTransactStatus': {'Success': None, 'Error': 'Bytes', 'TruncatedError': 'Bytes'}, 'QueryPallet': {'module_name': 'Bytes', 'response_info': {'destination': 'scale_info::116', 'query_id': 'u64', 'max_weight': 'scale_info::8'}}, 'ExpectPallet': {'index': 'u32', 'name': 'Bytes', 'module_name': 'Bytes', 'crate_major': 'u32', 'min_crate_minor': 'u32'}, 'ReportTransactStatus': {'destination': {'parents': 'u8', 'interior': 'scale_info::117'}, 'query_id': 'u64', 'max_weight': {'ref_time': 'u64', 'proof_size': 'u64'}}, 'ClearTransactStatus': None, 'UniversalOrigin': {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::120'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::120'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::120'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::121', 'part': 'scale_info::122'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, 'ExportMessage': {'network': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}, 'destination': {'Here': None, 'X1': 'scale_info::118', 'X2': ('scale_info::118', 'scale_info::118'), 'X3': ('scale_info::118', 'scale_info::118', 'scale_info::118'), 'X4': ('scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118'), 'X5': ('scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118'), 'X6': ('scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118'), 'X7': ('scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118'), 'X8': ('scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118')}, 'xcm': ['scale_info::146']}, 'LockAsset': {'asset': {'id': 'scale_info::150', 'fun': 'scale_info::151'}, 'unlocker': {'parents': 'u8', 'interior': 'scale_info::117'}}, 'UnlockAsset': {'asset': {'id': 'scale_info::150', 'fun': 'scale_info::151'}, 'target': {'parents': 'u8', 'interior': 'scale_info::117'}}, 'NoteUnlockable': {'asset': {'id': 'scale_info::150', 'fun': 'scale_info::151'}, 'owner': {'parents': 'u8', 'interior': 'scale_info::117'}}, 'RequestUnlock': {'asset': {'id': 'scale_info::150', 'fun': 'scale_info::151'}, 'locker': {'parents': 'u8', 'interior': 'scale_info::117'}}, 'SetFeesMode': {'jit_withdraw': 'bool'}, 'SetTopic': '[u8; 32]', 'ClearTopic': None, 'AliasOrigin': {'parents': 'u8', 'interior': {'Here': None, 'X1': 'scale_info::118', 'X2': ('scale_info::118', 'scale_info::118'), 'X3': ('scale_info::118', 'scale_info::118', 'scale_info::118'), 'X4': ('scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118'), 'X5': ('scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118'), 'X6': ('scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118'), 'X7': ('scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118'), 'X8': ('scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118', 'scale_info::118')}}, 'UnpaidExecution': {'weight_limit': {'Unlimited': None, 'Limited': 'scale_info::8'}, 'check_origin': (None, 'scale_info::116')}}]```

---------
## Errors

---------
### BadVersion
The version of the `Versioned` value used is not able to be
interpreted.

---------
### SendFailure
The message and destination was recognized as being reachable but
the operation could not be completed.

---------
### Unreachable
The message and destination combination was not recognized as being
reachable.

---------