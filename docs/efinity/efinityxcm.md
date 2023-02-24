
# EfinityXcm

---------
## Calls

---------
### force_set_minimum_weight
Update xcm fees amount to be used in xcm.Withdraw message
#### Attributes
| Name | Type |
| -------- | -------- | 
| xcm_call | `XcmOperation` | 
| xcm_weight_fee_misc | `MinimumWeightFeePair<Weight, T::Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'EfinityXcm', 'force_set_minimum_weight', {
    'xcm_call': {
        'ParachainFee': {
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
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                ),
                'X3': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                ),
                'X4': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                ),
                'X5': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                ),
                'X6': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                ),
                'X7': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                ),
                'X8': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                ),
            },
            'parents': 'u8',
        },
        'XTokensTransfer': None,
    },
    'xcm_weight_fee_misc': {
        'fee': 'u128',
        'minimum_weight': {
            'proof_size': 'u64',
            'ref_time': 'u64',
        },
    },
}
)
```

---------
### transfer_asset_to_parachain
`origin` transfers `amount` of `asset` to `beneficiary` on the `parachain`

Note: `asset` needs to be registered as foreign token in destination parachain

- `para_id`: destination parachain
- `beneficiary`: account to receive `asset` in destination parachain
- `asset`: asset to transfer
- `amount`: amount of `asset` to transfer
- `dest_weight`: optional weight to be paid in destination chain, unlimited in case it&\#x27;s
  `None`

\# Errors

- `InvalidAccountId`: `beneficiary` is invalid, i.e could not be converted to
#### Attributes
| Name | Type |
| -------- | -------- | 
| para_id | `ParachainId` | 
| beneficiary | `Account<T::AccountId>` | 
| asset_id | `T::AssetId` | 
| amount | `T::Balance` | 
| dest_weight | `Option<u64>` | 

#### Python
```python
call = substrate.compose_call(
    'EfinityXcm', 'transfer_asset_to_parachain', {
    'amount': 'u128',
    'asset_id': {
        'collection_id': 'u128',
        'token_id': 'u128',
    },
    'beneficiary': {
        'EVM': '[u8; 20]',
        'Substrate': 'AccountId',
    },
    'dest_weight': (None, 'u64'),
    'para_id': (
        'Acala',
        'Moonbeam',
        'Statemint',
    ),
}
)
```

---------
### transfer_to_parachain
`origin` transfers `amount` of EFI to `beneficiary` on the `parachain`

Note: EFI needs to be registered as foreign token in destination parachain

- `para_id`: destination parachain
- `beneficiary`: account to receive EFI in destination parachain
- `amount`: amount of EFI to transfer
- `dest_weight`: optional weight to be paid in destination chain, unlimited in case it&\#x27;s
  `None`

\# Errors

- `InvalidAccountId`: `beneficiary` is invalid, i.e could not be converted to
  `MultiLocation`
#### Attributes
| Name | Type |
| -------- | -------- | 
| para_id | `ParachainId` | 
| beneficiary | `Account<T::AccountId>` | 
| amount | `T::Balance` | 
| dest_weight | `Option<u64>` | 

#### Python
```python
call = substrate.compose_call(
    'EfinityXcm', 'transfer_to_parachain', {
    'amount': 'u128',
    'beneficiary': {
        'EVM': '[u8; 20]',
        'Substrate': 'AccountId',
    },
    'dest_weight': (None, 'u64'),
    'para_id': (
        'Acala',
        'Moonbeam',
        'Statemint',
    ),
}
)
```

---------
## Events

---------
### MinimumWeightUpdated
Xcm fee and weight updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MinimumWeightFeePair<Weight, T::Balance>` | ```{'minimum_weight': {'ref_time': 'u64', 'proof_size': 'u64'}, 'fee': 'u128'}```

---------
## Storage functions

---------
### MinimumWeights
 The `dest_weight` limit and fee for executing XCM msg sent by efinityXcm. Must be
 sufficient, otherwise the execution of XCM msg on relaychain will fail. For example it is
 used for setting the minimum fee (in DOT) for statemint.

 XcmWeightFee: map: XcmOperation =&gt; MinimumWeightFeePair

#### Python
```python
result = substrate.query(
    'EfinityXcm', 'MinimumWeights', [
    {
        'ParachainFee': {
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
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                ),
                'X3': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                ),
                'X4': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                ),
                'X5': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                ),
                'X6': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                ),
                'X7': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                ),
                'X8': (
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                    {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::70',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::70',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::70',
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
                ),
            },
            'parents': 'u8',
        },
        'XTokensTransfer': None,
    },
]
)
```

#### Return value
```python
{'fee': 'u128', 'minimum_weight': {'proof_size': 'u64', 'ref_time': 'u64'}}
```
---------
## Constants

---------
### BaseXcmWeight
 The actual weight for an XCM message is `T::BaseXcmWeight + T::Weigher::weight(&amp;msg)`.
#### Value
```python
100000000
```
#### Python
```python
constant = substrate.get_constant('EfinityXcm', 'BaseXcmWeight')
```
---------
### NativeCurrencyId
 ID of the native currency of the chain (EFI).
#### Value
```python
{'collection_id': 0, 'token_id': 0}
```
#### Python
```python
constant = substrate.get_constant('EfinityXcm', 'NativeCurrencyId')
```
---------
## Errors

---------
### InvalidBeneficiaryAddress
Invalid beneficiary

---------