
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
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                ),
                'X3': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                ),
                'X4': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                ),
                'X5': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                ),
                'X6': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                ),
                'X7': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                ),
                'X8': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::113',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::113',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::113',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::116',
                            'part': 'scale_info::117',
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
                            'scale_info::122',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::122',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::122',
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
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                ),
                'X3': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                ),
                'X4': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                ),
                'X5': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                ),
                'X6': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                ),
                'X7': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                ),
                'X8': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
                        },
                    },
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::122',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::122',
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
                            'id': 'scale_info::123',
                            'part': 'scale_info::124',
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
                        'fun': 'scale_info::299',
                        'id': 'scale_info::298',
                    },
                    'weight_limit': {
                        'Limited': 'u64',
                        'Unlimited': None,
                    },
                },
                'ClaimAsset': {
                    'assets': [
                        'scale_info::297',
                    ],
                    'ticket': {
                        'interior': 'scale_info::110',
                        'parents': 'u8',
                    },
                },
                'ClearError': None,
                'ClearOrigin': None,
                'DepositAsset': {
                    'assets': {
                        'Definite': [
                            'scale_info::297',
                        ],
                        'Wild': 'scale_info::308',
                    },
                    'beneficiary': {
                        'interior': 'scale_info::110',
                        'parents': 'u8',
                    },
                    'max_assets': 'u32',
                },
                'DepositReserveAsset': {
                    'assets': {
                        'Definite': [
                            'scale_info::297',
                        ],
                        'Wild': 'scale_info::308',
                    },
                    'dest': {
                        'interior': 'scale_info::110',
                        'parents': 'u8',
                    },
                    'max_assets': 'u32',
                    'xcm': [
                        'scale_info::294',
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
                        'scale_info::111',
                        'scale_info::111',
                    ),
                    'X3': (
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                    ),
                    'X4': (
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                    ),
                    'X5': (
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                    ),
                    'X6': (
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                    ),
                    'X7': (
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                    ),
                    'X8': (
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                        'scale_info::111',
                    ),
                },
                'ExchangeAsset': {
                    'give': {
                        'Definite': [
                            'scale_info::297',
                        ],
                        'Wild': 'scale_info::308',
                    },
                    'receive': [
                        'scale_info::297',
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
                            'scale_info::297',
                        ],
                        'Wild': 'scale_info::308',
                    },
                    'reserve': {
                        'interior': 'scale_info::110',
                        'parents': 'u8',
                    },
                    'xcm': [
                        'scale_info::294',
                    ],
                },
                'InitiateTeleport': {
                    'assets': {
                        'Definite': [
                            'scale_info::297',
                        ],
                        'Wild': 'scale_info::308',
                    },
                    'dest': {
                        'interior': 'scale_info::110',
                        'parents': 'u8',
                    },
                    'xcm': [
                        'scale_info::294',
                    ],
                },
                'QueryHolding': {
                    'assets': {
                        'Definite': [
                            'scale_info::297',
                        ],
                        'Wild': 'scale_info::308',
                    },
                    'dest': {
                        'interior': 'scale_info::110',
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
                            'scale_info::297',
                        ],
                        'ExecutionResult': (
                            None,
                            (
                                'u32',
                                'scale_info::304',
                            ),
                        ),
                        'Null': None,
                        'Version': 'u32',
                    },
                },
                'ReceiveTeleportedAsset': [
                    'scale_info::297',
                ],
                'RefundSurplus': None,
                'ReportError': {
                    'dest': {
                        'interior': 'scale_info::110',
                        'parents': 'u8',
                    },
                    'max_response_weight': 'u64',
                    'query_id': 'u64',
                },
                'ReserveAssetDeposited': [
                    'scale_info::297',
                ],
                'SetAppendix': [
                    'scale_info::294',
                ],
                'SetErrorHandler': [
                    'scale_info::294',
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
                        'scale_info::297',
                    ],
                    'beneficiary': {
                        'interior': 'scale_info::110',
                        'parents': 'u8',
                    },
                },
                'TransferReserveAsset': {
                    'assets': [
                        'scale_info::297',
                    ],
                    'dest': {
                        'interior': 'scale_info::110',
                        'parents': 'u8',
                    },
                    'xcm': [
                        'scale_info::294',
                    ],
                },
                'Trap': 'u64',
                'UnsubscribeVersion': None,
                'WithdrawAsset': [
                    'scale_info::297',
                ],
            },
        ],
        'V3': [
            {
                'AliasOrigin': {
                    'interior': {
                        'Here': None,
                        'X1': 'scale_info::120',
                        'X2': (
                            'scale_info::120',
                            'scale_info::120',
                        ),
                        'X3': (
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                        ),
                        'X4': (
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                        ),
                        'X5': (
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                        ),
                        'X6': (
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                        ),
                        'X7': (
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                        ),
                        'X8': (
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                        ),
                    },
                    'parents': 'u8',
                },
                'BurnAsset': [
                    'scale_info::316',
                ],
                'BuyExecution': {
                    'fees': {
                        'fun': 'scale_info::318',
                        'id': 'scale_info::317',
                    },
                    'weight_limit': {
                        'Limited': 'scale_info::9',
                        'Unlimited': None,
                    },
                },
                'ClaimAsset': {
                    'assets': [
                        'scale_info::316',
                    ],
                    'ticket': {
                        'interior': 'scale_info::119',
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
                            'scale_info::316',
                        ],
                        'Wild': 'scale_info::333',
                    },
                    'beneficiary': {
                        'interior': 'scale_info::119',
                        'parents': 'u8',
                    },
                },
                'DepositReserveAsset': {
                    'assets': {
                        'Definite': [
                            'scale_info::316',
                        ],
                        'Wild': 'scale_info::333',
                    },
                    'dest': {
                        'interior': 'scale_info::119',
                        'parents': 'u8',
                    },
                    'xcm': [
                        'scale_info::313',
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
                        'GlobalConsensus': 'scale_info::122',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': 'InnerStruct',
                    },
                    'X2': (
                        'scale_info::120',
                        'scale_info::120',
                    ),
                    'X3': (
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                    ),
                    'X4': (
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                    ),
                    'X5': (
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                    ),
                    'X6': (
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                    ),
                    'X7': (
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                    ),
                    'X8': (
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                        'scale_info::120',
                    ),
                },
                'ExchangeAsset': {
                    'give': {
                        'Definite': [
                            'scale_info::316',
                        ],
                        'Wild': 'scale_info::333',
                    },
                    'maximal': 'bool',
                    'want': [
                        'scale_info::316',
                    ],
                },
                'ExpectAsset': [
                    'scale_info::316',
                ],
                'ExpectError': (
                    None,
                    (
                        'u32',
                        'scale_info::323',
                    ),
                ),
                'ExpectOrigin': (
                    None,
                    {
                        'interior': 'scale_info::119',
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
                        'X1': 'scale_info::120',
                        'X2': (
                            'scale_info::120',
                            'scale_info::120',
                        ),
                        'X3': (
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                        ),
                        'X4': (
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                        ),
                        'X5': (
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                        ),
                        'X6': (
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                        ),
                        'X7': (
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                        ),
                        'X8': (
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
                            'scale_info::120',
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
                        'scale_info::313',
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
                            'scale_info::316',
                        ],
                        'Wild': 'scale_info::333',
                    },
                    'reserve': {
                        'interior': 'scale_info::119',
                        'parents': 'u8',
                    },
                    'xcm': [
                        'scale_info::313',
                    ],
                },
                'InitiateTeleport': {
                    'assets': {
                        'Definite': [
                            'scale_info::316',
                        ],
                        'Wild': 'scale_info::333',
                    },
                    'dest': {
                        'interior': 'scale_info::119',
                        'parents': 'u8',
                    },
                    'xcm': [
                        'scale_info::313',
                    ],
                },
                'LockAsset': {
                    'asset': {
                        'fun': 'scale_info::318',
                        'id': 'scale_info::317',
                    },
                    'unlocker': {
                        'interior': 'scale_info::119',
                        'parents': 'u8',
                    },
                },
                'NoteUnlockable': {
                    'asset': {
                        'fun': 'scale_info::318',
                        'id': 'scale_info::317',
                    },
                    'owner': {
                        'interior': 'scale_info::119',
                        'parents': 'u8',
                    },
                },
                'QueryPallet': {
                    'module_name': 'Bytes',
                    'response_info': {
                        'destination': 'scale_info::118',
                        'max_weight': 'scale_info::9',
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
                        'scale_info::118',
                    ),
                    'query_id': 'u64',
                    'response': {
                        'Assets': [
                            'scale_info::316',
                        ],
                        'DispatchResult': 'scale_info::328',
                        'ExecutionResult': (
                            None,
                            (
                                'u32',
                                'scale_info::323',
                            ),
                        ),
                        'Null': None,
                        'PalletsInfo': [
                            'scale_info::325',
                        ],
                        'Version': 'u32',
                    },
                },
                'ReceiveTeleportedAsset': [
                    'scale_info::316',
                ],
                'RefundSurplus': None,
                'ReportError': {
                    'destination': {
                        'interior': 'scale_info::119',
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
                            'scale_info::316',
                        ],
                        'Wild': 'scale_info::333',
                    },
                    'response_info': {
                        'destination': 'scale_info::118',
                        'max_weight': 'scale_info::9',
                        'query_id': 'u64',
                    },
                },
                'ReportTransactStatus': {
                    'destination': {
                        'interior': 'scale_info::119',
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
                        'fun': 'scale_info::318',
                        'id': 'scale_info::317',
                    },
                    'locker': {
                        'interior': 'scale_info::119',
                        'parents': 'u8',
                    },
                },
                'ReserveAssetDeposited': [
                    'scale_info::316',
                ],
                'SetAppendix': [
                    'scale_info::313',
                ],
                'SetErrorHandler': [
                    'scale_info::313',
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
                        'scale_info::316',
                    ],
                    'beneficiary': {
                        'interior': 'scale_info::119',
                        'parents': 'u8',
                    },
                },
                'TransferReserveAsset': {
                    'assets': [
                        'scale_info::316',
                    ],
                    'dest': {
                        'interior': 'scale_info::119',
                        'parents': 'u8',
                    },
                    'xcm': [
                        'scale_info::313',
                    ],
                },
                'Trap': 'u64',
                'UniversalOrigin': {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::122',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::122',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::122',
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
                        'id': 'scale_info::123',
                        'part': 'scale_info::124',
                    },
                },
                'UnlockAsset': {
                    'asset': {
                        'fun': 'scale_info::318',
                        'id': 'scale_info::317',
                    },
                    'target': {
                        'interior': 'scale_info::119',
                        'parents': 'u8',
                    },
                },
                'UnpaidExecution': {
                    'check_origin': (
                        None,
                        'scale_info::118',
                    ),
                    'weight_limit': {
                        'Limited': 'scale_info::9',
                        'Unlimited': None,
                    },
                },
                'UnsubscribeVersion': None,
                'WithdrawAsset': [
                    'scale_info::316',
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
| to | `MultiLocation` | ```{'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': {'Unit': None, 'Moniker': '[u8; 4]', 'Index': 'u32', 'Executive': None, 'Technical': None, 'Legislative': None, 'Judicial': None, 'Defense': None, 'Administration': None, 'Treasury': None}, 'part': {'Voice': None, 'Members': 'InnerStruct', 'Fraction': 'InnerStruct', 'AtLeastProportion': 'InnerStruct', 'MoreThanProportion': 'InnerStruct'}}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': {'block_number': 'u64', 'block_hash': '[u8; 32]'}, 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': {'chain_id': 'u64'}, 'BitcoinCore': None, 'BitcoinCash': None}}, 'X2': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}), 'X3': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}), 'X4': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}), 'X5': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}), 'X6': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}), 'X7': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}), 'X8': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}})}}```
| message | `Xcm<()>` | ```[{'WithdrawAsset': ['scale_info::316'], 'ReserveAssetDeposited': ['scale_info::316'], 'ReceiveTeleportedAsset': ['scale_info::316'], 'QueryResponse': {'query_id': 'u64', 'response': {'Null': None, 'Assets': ['scale_info::316'], 'ExecutionResult': (None, ('u32', 'scale_info::323')), 'Version': 'u32', 'PalletsInfo': ['scale_info::325'], 'DispatchResult': 'scale_info::328'}, 'max_weight': {'ref_time': 'u64', 'proof_size': 'u64'}, 'querier': (None, 'scale_info::118')}, 'TransferAsset': {'assets': ['scale_info::316'], 'beneficiary': {'parents': 'u8', 'interior': 'scale_info::119'}}, 'TransferReserveAsset': {'assets': ['scale_info::316'], 'dest': {'parents': 'u8', 'interior': 'scale_info::119'}, 'xcm': ['scale_info::313']}, 'Transact': {'origin_kind': ('Native', 'SovereignAccount', 'Superuser', 'Xcm'), 'require_weight_at_most': {'ref_time': 'u64', 'proof_size': 'u64'}, 'call': {'encoded': 'Bytes'}}, 'HrmpNewChannelOpenRequest': {'sender': 'u32', 'max_message_size': 'u32', 'max_capacity': 'u32'}, 'HrmpChannelAccepted': {'recipient': 'u32'}, 'HrmpChannelClosing': {'initiator': 'u32', 'sender': 'u32', 'recipient': 'u32'}, 'ClearOrigin': None, 'DescendOrigin': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'InnerStruct', 'OnlyChild': None, 'Plurality': 'InnerStruct', 'GlobalConsensus': 'scale_info::122'}, 'X2': ('scale_info::120', 'scale_info::120'), 'X3': ('scale_info::120', 'scale_info::120', 'scale_info::120'), 'X4': ('scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120'), 'X5': ('scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120'), 'X6': ('scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120'), 'X7': ('scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120'), 'X8': ('scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120')}, 'ReportError': {'destination': {'parents': 'u8', 'interior': 'scale_info::119'}, 'query_id': 'u64', 'max_weight': {'ref_time': 'u64', 'proof_size': 'u64'}}, 'DepositAsset': {'assets': {'Definite': ['scale_info::316'], 'Wild': 'scale_info::333'}, 'beneficiary': {'parents': 'u8', 'interior': 'scale_info::119'}}, 'DepositReserveAsset': {'assets': {'Definite': ['scale_info::316'], 'Wild': 'scale_info::333'}, 'dest': {'parents': 'u8', 'interior': 'scale_info::119'}, 'xcm': ['scale_info::313']}, 'ExchangeAsset': {'give': {'Definite': ['scale_info::316'], 'Wild': 'scale_info::333'}, 'want': ['scale_info::316'], 'maximal': 'bool'}, 'InitiateReserveWithdraw': {'assets': {'Definite': ['scale_info::316'], 'Wild': 'scale_info::333'}, 'reserve': {'parents': 'u8', 'interior': 'scale_info::119'}, 'xcm': ['scale_info::313']}, 'InitiateTeleport': {'assets': {'Definite': ['scale_info::316'], 'Wild': 'scale_info::333'}, 'dest': {'parents': 'u8', 'interior': 'scale_info::119'}, 'xcm': ['scale_info::313']}, 'ReportHolding': {'response_info': {'destination': 'scale_info::118', 'query_id': 'u64', 'max_weight': 'scale_info::9'}, 'assets': {'Definite': ['scale_info::316'], 'Wild': 'scale_info::333'}}, 'BuyExecution': {'fees': {'id': 'scale_info::317', 'fun': 'scale_info::318'}, 'weight_limit': {'Unlimited': None, 'Limited': 'scale_info::9'}}, 'RefundSurplus': None, 'SetErrorHandler': ['scale_info::313'], 'SetAppendix': ['scale_info::313'], 'ClearError': None, 'ClaimAsset': {'assets': ['scale_info::316'], 'ticket': {'parents': 'u8', 'interior': 'scale_info::119'}}, 'Trap': 'u64', 'SubscribeVersion': {'query_id': 'u64', 'max_response_weight': {'ref_time': 'u64', 'proof_size': 'u64'}}, 'UnsubscribeVersion': None, 'BurnAsset': ['scale_info::316'], 'ExpectAsset': ['scale_info::316'], 'ExpectOrigin': (None, {'parents': 'u8', 'interior': 'scale_info::119'}), 'ExpectError': (None, ('u32', 'scale_info::323')), 'ExpectTransactStatus': {'Success': None, 'Error': 'Bytes', 'TruncatedError': 'Bytes'}, 'QueryPallet': {'module_name': 'Bytes', 'response_info': {'destination': 'scale_info::118', 'query_id': 'u64', 'max_weight': 'scale_info::9'}}, 'ExpectPallet': {'index': 'u32', 'name': 'Bytes', 'module_name': 'Bytes', 'crate_major': 'u32', 'min_crate_minor': 'u32'}, 'ReportTransactStatus': {'destination': {'parents': 'u8', 'interior': 'scale_info::119'}, 'query_id': 'u64', 'max_weight': {'ref_time': 'u64', 'proof_size': 'u64'}}, 'ClearTransactStatus': None, 'UniversalOrigin': {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::122'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::122'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::122'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::123', 'part': 'scale_info::124'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, 'ExportMessage': {'network': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}, 'destination': {'Here': None, 'X1': 'scale_info::120', 'X2': ('scale_info::120', 'scale_info::120'), 'X3': ('scale_info::120', 'scale_info::120', 'scale_info::120'), 'X4': ('scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120'), 'X5': ('scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120'), 'X6': ('scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120'), 'X7': ('scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120'), 'X8': ('scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120')}, 'xcm': ['scale_info::313']}, 'LockAsset': {'asset': {'id': 'scale_info::317', 'fun': 'scale_info::318'}, 'unlocker': {'parents': 'u8', 'interior': 'scale_info::119'}}, 'UnlockAsset': {'asset': {'id': 'scale_info::317', 'fun': 'scale_info::318'}, 'target': {'parents': 'u8', 'interior': 'scale_info::119'}}, 'NoteUnlockable': {'asset': {'id': 'scale_info::317', 'fun': 'scale_info::318'}, 'owner': {'parents': 'u8', 'interior': 'scale_info::119'}}, 'RequestUnlock': {'asset': {'id': 'scale_info::317', 'fun': 'scale_info::318'}, 'locker': {'parents': 'u8', 'interior': 'scale_info::119'}}, 'SetFeesMode': {'jit_withdraw': 'bool'}, 'SetTopic': '[u8; 32]', 'ClearTopic': None, 'AliasOrigin': {'parents': 'u8', 'interior': {'Here': None, 'X1': 'scale_info::120', 'X2': ('scale_info::120', 'scale_info::120'), 'X3': ('scale_info::120', 'scale_info::120', 'scale_info::120'), 'X4': ('scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120'), 'X5': ('scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120'), 'X6': ('scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120'), 'X7': ('scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120'), 'X8': ('scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120', 'scale_info::120')}}, 'UnpaidExecution': {'weight_limit': {'Unlimited': None, 'Limited': 'scale_info::9'}, 'check_origin': (None, 'scale_info::118')}}]```

---------
## Storage functions

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