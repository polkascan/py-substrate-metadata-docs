
# XTokens

---------
## Calls

---------
### transfer
Transfer native currencies.

`dest_weight_limit` is the weight for XCM execution on the dest
chain, and it would be charged from the transferred assets. If set
below requirements, the execution may fail and assets wouldn&\#x27;t be
received.

It&\#x27;s a no-op if any error on local XCM execution or message sending.
Note sending assets out per se doesn&\#x27;t guarantee they would be
received. Receiving depends on if the XCM message could be delivered
by the network, and if the receiving chain would handle
messages correctly.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 
| amount | `T::Balance` | 
| dest | `Box<VersionedMultiLocation>` | 
| dest_weight_limit | `WeightLimit` | 

#### Python
```python
call = substrate.compose_call(
    'XTokens', 'transfer', {
    'amount': 'u128',
    'currency_id': 'u128',
    'dest': {
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                    {
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
                ),
                'X3': (
                    {
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
                    {
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
                    {
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
                ),
                'X4': (
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X5': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X6': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X7': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X8': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
            },
            'parents': 'u8',
        },
    },
    'dest_weight_limit': {
        'Limited': {
            'proof_size': 'u64',
            'ref_time': 'u64',
        },
        'Unlimited': None,
    },
}
)
```

---------
### transfer_multiasset
Transfer `MultiAsset`.

`dest_weight_limit` is the weight for XCM execution on the dest
chain, and it would be charged from the transferred assets. If set
below requirements, the execution may fail and assets wouldn&\#x27;t be
received.

It&\#x27;s a no-op if any error on local XCM execution or message sending.
Note sending assets out per se doesn&\#x27;t guarantee they would be
received. Receiving depends on if the XCM message could be delivered
by the network, and if the receiving chain would handle
messages correctly.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `Box<VersionedMultiAsset>` | 
| dest | `Box<VersionedMultiLocation>` | 
| dest_weight_limit | `WeightLimit` | 

#### Python
```python
call = substrate.compose_call(
    'XTokens', 'transfer_multiasset', {
    'asset': {
        'V2': {
            'fun': {
                'Fungible': 'u128',
                'NonFungible': {
                    'Array16': '[u8; 16]',
                    'Array32': '[u8; 32]',
                    'Array4': '[u8; 4]',
                    'Array8': '[u8; 8]',
                    'Blob': 'Bytes',
                    'Index': 'u128',
                    'Undefined': None,
                },
            },
            'id': {
                'Abstract': 'Bytes',
                'Concrete': {
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
                    'parents': 'u8',
                },
            },
        },
        'V3': {
            'fun': {
                'Fungible': 'u128',
                'NonFungible': {
                    'Array16': '[u8; 16]',
                    'Array32': '[u8; 32]',
                    'Array4': '[u8; 4]',
                    'Array8': '[u8; 8]',
                    'Index': 'u128',
                    'Undefined': None,
                },
            },
            'id': {
                'Abstract': '[u8; 32]',
                'Concrete': {
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
    },
    'dest': {
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                    {
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
                ),
                'X3': (
                    {
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
                    {
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
                    {
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
                ),
                'X4': (
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X5': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X6': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X7': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X8': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
            },
            'parents': 'u8',
        },
    },
    'dest_weight_limit': {
        'Limited': {
            'proof_size': 'u64',
            'ref_time': 'u64',
        },
        'Unlimited': None,
    },
}
)
```

---------
### transfer_multiasset_with_fee
Transfer `MultiAsset` specifying the fee and amount as separate.

`dest_weight_limit` is the weight for XCM execution on the dest
chain, and it would be charged from the transferred assets. If set
below requirements, the execution may fail and assets wouldn&\#x27;t be
received.

`fee` is the multiasset to be spent to pay for execution in
destination chain. Both fee and amount will be subtracted form the
callers balance For now we only accept fee and asset having the same
`MultiLocation` id.

If `fee` is not high enough to cover for the execution costs in the
destination chain, then the assets will be trapped in the
destination chain

It&\#x27;s a no-op if any error on local XCM execution or message sending.
Note sending assets out per se doesn&\#x27;t guarantee they would be
received. Receiving depends on if the XCM message could be delivered
by the network, and if the receiving chain would handle
messages correctly.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `Box<VersionedMultiAsset>` | 
| fee | `Box<VersionedMultiAsset>` | 
| dest | `Box<VersionedMultiLocation>` | 
| dest_weight_limit | `WeightLimit` | 

#### Python
```python
call = substrate.compose_call(
    'XTokens', 'transfer_multiasset_with_fee', {
    'asset': {
        'V2': {
            'fun': {
                'Fungible': 'u128',
                'NonFungible': {
                    'Array16': '[u8; 16]',
                    'Array32': '[u8; 32]',
                    'Array4': '[u8; 4]',
                    'Array8': '[u8; 8]',
                    'Blob': 'Bytes',
                    'Index': 'u128',
                    'Undefined': None,
                },
            },
            'id': {
                'Abstract': 'Bytes',
                'Concrete': {
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
                    'parents': 'u8',
                },
            },
        },
        'V3': {
            'fun': {
                'Fungible': 'u128',
                'NonFungible': {
                    'Array16': '[u8; 16]',
                    'Array32': '[u8; 32]',
                    'Array4': '[u8; 4]',
                    'Array8': '[u8; 8]',
                    'Index': 'u128',
                    'Undefined': None,
                },
            },
            'id': {
                'Abstract': '[u8; 32]',
                'Concrete': {
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
    },
    'dest': {
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                    {
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
                ),
                'X3': (
                    {
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
                    {
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
                    {
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
                ),
                'X4': (
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X5': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X6': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X7': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X8': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
            },
            'parents': 'u8',
        },
    },
    'dest_weight_limit': {
        'Limited': {
            'proof_size': 'u64',
            'ref_time': 'u64',
        },
        'Unlimited': None,
    },
    'fee': {
        'V2': {
            'fun': {
                'Fungible': 'u128',
                'NonFungible': {
                    'Array16': '[u8; 16]',
                    'Array32': '[u8; 32]',
                    'Array4': '[u8; 4]',
                    'Array8': '[u8; 8]',
                    'Blob': 'Bytes',
                    'Index': 'u128',
                    'Undefined': None,
                },
            },
            'id': {
                'Abstract': 'Bytes',
                'Concrete': {
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
                    'parents': 'u8',
                },
            },
        },
        'V3': {
            'fun': {
                'Fungible': 'u128',
                'NonFungible': {
                    'Array16': '[u8; 16]',
                    'Array32': '[u8; 32]',
                    'Array4': '[u8; 4]',
                    'Array8': '[u8; 8]',
                    'Index': 'u128',
                    'Undefined': None,
                },
            },
            'id': {
                'Abstract': '[u8; 32]',
                'Concrete': {
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
    },
}
)
```

---------
### transfer_multiassets
Transfer several `MultiAsset` specifying the item to be used as fee

`dest_weight_limit` is the weight for XCM execution on the dest
chain, and it would be charged from the transferred assets. If set
below requirements, the execution may fail and assets wouldn&\#x27;t be
received.

`fee_item` is index of the MultiAssets that we want to use for
payment

It&\#x27;s a no-op if any error on local XCM execution or message sending.
Note sending assets out per se doesn&\#x27;t guarantee they would be
received. Receiving depends on if the XCM message could be delivered
by the network, and if the receiving chain would handle
messages correctly.
#### Attributes
| Name | Type |
| -------- | -------- | 
| assets | `Box<VersionedMultiAssets>` | 
| fee_item | `u32` | 
| dest | `Box<VersionedMultiLocation>` | 
| dest_weight_limit | `WeightLimit` | 

#### Python
```python
call = substrate.compose_call(
    'XTokens', 'transfer_multiassets', {
    'assets': {
        'V2': [
            {
                'fun': {
                    'Fungible': 'u128',
                    'NonFungible': {
                        'Array16': '[u8; 16]',
                        'Array32': '[u8; 32]',
                        'Array4': '[u8; 4]',
                        'Array8': '[u8; 8]',
                        'Blob': 'Bytes',
                        'Index': 'u128',
                        'Undefined': None,
                    },
                },
                'id': {
                    'Abstract': 'Bytes',
                    'Concrete': {
                        'interior': 'scale_info::110',
                        'parents': 'u8',
                    },
                },
            },
        ],
        'V3': [
            {
                'fun': {
                    'Fungible': 'u128',
                    'NonFungible': {
                        'Array16': '[u8; 16]',
                        'Array32': '[u8; 32]',
                        'Array4': '[u8; 4]',
                        'Array8': '[u8; 8]',
                        'Index': 'u128',
                        'Undefined': None,
                    },
                },
                'id': {
                    'Abstract': '[u8; 32]',
                    'Concrete': {
                        'interior': 'scale_info::69',
                        'parents': 'u8',
                    },
                },
            },
        ],
    },
    'dest': {
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                    {
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
                ),
                'X3': (
                    {
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
                    {
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
                    {
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
                ),
                'X4': (
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X5': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X6': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X7': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X8': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
            },
            'parents': 'u8',
        },
    },
    'dest_weight_limit': {
        'Limited': {
            'proof_size': 'u64',
            'ref_time': 'u64',
        },
        'Unlimited': None,
    },
    'fee_item': 'u32',
}
)
```

---------
### transfer_multicurrencies
Transfer several currencies specifying the item to be used as fee

`dest_weight_limit` is the weight for XCM execution on the dest
chain, and it would be charged from the transferred assets. If set
below requirements, the execution may fail and assets wouldn&\#x27;t be
received.

`fee_item` is index of the currencies tuple that we want to use for
payment

It&\#x27;s a no-op if any error on local XCM execution or message sending.
Note sending assets out per se doesn&\#x27;t guarantee they would be
received. Receiving depends on if the XCM message could be delivered
by the network, and if the receiving chain would handle
messages correctly.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currencies | `Vec<(T::CurrencyId, T::Balance)>` | 
| fee_item | `u32` | 
| dest | `Box<VersionedMultiLocation>` | 
| dest_weight_limit | `WeightLimit` | 

#### Python
```python
call = substrate.compose_call(
    'XTokens', 'transfer_multicurrencies', {
    'currencies': [('u128', 'u128')],
    'dest': {
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                    {
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
                ),
                'X3': (
                    {
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
                    {
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
                    {
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
                ),
                'X4': (
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X5': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X6': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X7': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X8': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
            },
            'parents': 'u8',
        },
    },
    'dest_weight_limit': {
        'Limited': {
            'proof_size': 'u64',
            'ref_time': 'u64',
        },
        'Unlimited': None,
    },
    'fee_item': 'u32',
}
)
```

---------
### transfer_with_fee
Transfer native currencies specifying the fee and amount as
separate.

`dest_weight_limit` is the weight for XCM execution on the dest
chain, and it would be charged from the transferred assets. If set
below requirements, the execution may fail and assets wouldn&\#x27;t be
received.

`fee` is the amount to be spent to pay for execution in destination
chain. Both fee and amount will be subtracted form the callers
balance.

If `fee` is not high enough to cover for the execution costs in the
destination chain, then the assets will be trapped in the
destination chain

It&\#x27;s a no-op if any error on local XCM execution or message sending.
Note sending assets out per se doesn&\#x27;t guarantee they would be
received. Receiving depends on if the XCM message could be delivered
by the network, and if the receiving chain would handle
messages correctly.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 
| amount | `T::Balance` | 
| fee | `T::Balance` | 
| dest | `Box<VersionedMultiLocation>` | 
| dest_weight_limit | `WeightLimit` | 

#### Python
```python
call = substrate.compose_call(
    'XTokens', 'transfer_with_fee', {
    'amount': 'u128',
    'currency_id': 'u128',
    'dest': {
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                            'network': 'scale_info::112',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::112',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::112',
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
                    {
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
                ),
                'X3': (
                    {
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
                    {
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
                    {
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
                ),
                'X4': (
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X5': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X6': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X7': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
                'X8': (
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                ),
            },
            'parents': 'u8',
        },
    },
    'dest_weight_limit': {
        'Limited': {
            'proof_size': 'u64',
            'ref_time': 'u64',
        },
        'Unlimited': None,
    },
    'fee': 'u128',
}
)
```

---------
## Events

---------
### TransferredMultiAssets
Transferred `MultiAsset` with fee.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| assets | `MultiAssets` | ```[{'id': {'Concrete': {'parents': 'u8', 'interior': 'scale_info::69'}, 'Abstract': '[u8; 32]'}, 'fun': {'Fungible': 'u128', 'NonFungible': {'Undefined': None, 'Index': 'u128', 'Array4': '[u8; 4]', 'Array8': '[u8; 8]', 'Array16': '[u8; 16]', 'Array32': '[u8; 32]'}}}]```
| fee | `MultiAsset` | ```{'id': {'Concrete': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'InnerStruct', 'OnlyChild': None, 'Plurality': 'InnerStruct', 'GlobalConsensus': 'scale_info::73'}, 'X2': ('scale_info::70', 'scale_info::70'), 'X3': ('scale_info::70', 'scale_info::70', 'scale_info::70'), 'X4': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70'), 'X5': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70'), 'X6': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70'), 'X7': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70'), 'X8': ('scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70', 'scale_info::70')}}, 'Abstract': '[u8; 32]'}, 'fun': {'Fungible': 'u128', 'NonFungible': {'Undefined': None, 'Index': 'u128', 'Array4': '[u8; 4]', 'Array8': '[u8; 8]', 'Array16': '[u8; 16]', 'Array32': '[u8; 32]'}}}```
| dest | `MultiLocation` | ```{'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': {'Unit': None, 'Moniker': '[u8; 4]', 'Index': 'u32', 'Executive': None, 'Technical': None, 'Legislative': None, 'Judicial': None, 'Defense': None, 'Administration': None, 'Treasury': None}, 'part': {'Voice': None, 'Members': 'InnerStruct', 'Fraction': 'InnerStruct', 'AtLeastProportion': 'InnerStruct', 'MoreThanProportion': 'InnerStruct'}}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': {'block_number': 'u64', 'block_hash': '[u8; 32]'}, 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': {'chain_id': 'u64'}, 'BitcoinCore': None, 'BitcoinCash': None}}, 'X2': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}), 'X3': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}), 'X4': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}), 'X5': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}), 'X6': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}), 'X7': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}), 'X8': ({'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}}, {'Parachain': 'u32', 'AccountId32': {'network': (None, 'scale_info::73'), 'id': '[u8; 32]'}, 'AccountIndex64': {'network': (None, 'scale_info::73'), 'index': 'u64'}, 'AccountKey20': {'network': (None, 'scale_info::73'), 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': {'length': 'u8', 'data': '[u8; 32]'}, 'OnlyChild': None, 'Plurality': {'id': 'scale_info::76', 'part': 'scale_info::77'}, 'GlobalConsensus': {'ByGenesis': '[u8; 32]', 'ByFork': 'InnerStruct', 'Polkadot': None, 'Kusama': None, 'Westend': None, 'Rococo': None, 'Wococo': None, 'Ethereum': 'InnerStruct', 'BitcoinCore': None, 'BitcoinCash': None}})}}```

---------
## Constants

---------
### BaseXcmWeight
 Base XCM weight.

 The actually weight for an XCM message is `T::BaseXcmWeight +
 T::Weigher::weight(&amp;msg)`.
#### Value
```python
{'proof_size': 0, 'ref_time': 100000000}
```
#### Python
```python
constant = substrate.get_constant('XTokens', 'BaseXcmWeight')
```
---------
### SelfLocation
 Self chain location.
#### Value
```python
{'interior': 'Here', 'parents': 0}
```
#### Python
```python
constant = substrate.get_constant('XTokens', 'SelfLocation')
```
---------
## Errors

---------
### AssetHasNoReserve
Asset has no reserve location.

---------
### AssetIndexNonExistent
The specified index does not exist in a MultiAssets struct.

---------
### BadVersion
The version of the `Versioned` value used is not able to be
interpreted.

---------
### CannotReanchor
Could not re-anchor the assets to declare the fees for the
destination chain.

---------
### DestinationNotInvertible
The destination `MultiLocation` provided cannot be inverted.

---------
### DistinctReserveForAssetAndFee
We tried sending distinct asset and fee but they have different
reserve chains.

---------
### FeeNotEnough
Fee is not enough.

---------
### InvalidAncestry
Could not get ancestry of asset reserve location.

---------
### InvalidAsset
The MultiAsset is invalid.

---------
### InvalidDest
Invalid transfer destination.

---------
### MinXcmFeeNotDefined
MinXcmFee not registered for certain reserve location

---------
### NotCrossChainTransfer
Not cross-chain transfer.

---------
### NotCrossChainTransferableCurrency
Currency is not cross-chain transferable.

---------
### NotSupportedMultiLocation
Not supported MultiLocation

---------
### TooManyAssetsBeingSent
The number of assets to be sent is over the maximum.

---------
### UnweighableMessage
The message&\#x27;s weight could not be determined.

---------
### XcmExecutionFailed
XCM execution failed.

---------
### ZeroAmount
The transfering asset amount is zero.

---------
### ZeroFee
The fee is zero.

---------