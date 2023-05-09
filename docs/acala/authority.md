
# Authority

---------
## Calls

---------
### authorize_call
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<CallOf<T>>` | 
| caller | `Option<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Authority', 'authorize_call', {
    'call': 'Call',
    'caller': (None, 'AccountId'),
}
)
```

---------
### cancel_scheduled_dispatch
#### Attributes
| Name | Type |
| -------- | -------- | 
| initial_origin | `Box<T::PalletsOrigin>` | 
| task_id | `ScheduleTaskIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Authority', 'cancel_scheduled_dispatch', {
    'initial_origin': {
        'system': {
            'None': None,
            'Root': None,
            'Signed': 'AccountId',
        },
        None: None,
        'Authority': {
            'delay': 'u32',
            'origin': {
                'Authority': {
                    'delay': 'u32',
                    'origin': {
                        'system': {
                            'None': None,
                            'Root': None,
                            'Signed': 'AccountId',
                        },
                        None: None,
                        'Authority': {
                            'delay': 'u32',
                            'origin': 'scale_info::114',
                        },
                        'CumulusXcm': {
                            'Relay': None,
                            'SiblingParachain': 'u32',
                        },
                        'FinancialCouncil': {
                            'Member': 'AccountId',
                            'Members': (
                                'u32',
                                'u32',
                            ),
                            '_Phantom': None,
                        },
                        'GeneralCouncil': {
                            'Member': 'AccountId',
                            'Members': (
                                'u32',
                                'u32',
                            ),
                            '_Phantom': None,
                        },
                        'HomaCouncil': {
                            'Member': 'AccountId',
                            'Members': (
                                'u32',
                                'u32',
                            ),
                            '_Phantom': None,
                        },
                        'PolkadotXcm': {
                            'Response': 'scale_info::74',
                            'Xcm': 'scale_info::74',
                        },
                        'TechnicalCommittee': {
                            'Member': 'AccountId',
                            'Members': (
                                'u32',
                                'u32',
                            ),
                            '_Phantom': None,
                        },
                        'Void': (),
                    },
                },
                'CumulusXcm': {
                    'Relay': None,
                    'SiblingParachain': 'u32',
                },
                'FinancialCouncil': {
                    'Member': 'AccountId',
                    'Members': (
                        'u32',
                        'u32',
                    ),
                    '_Phantom': None,
                },
                'GeneralCouncil': {
                    'Member': 'AccountId',
                    'Members': (
                        'u32',
                        'u32',
                    ),
                    '_Phantom': None,
                },
                'HomaCouncil': {
                    'Member': 'AccountId',
                    'Members': (
                        'u32',
                        'u32',
                    ),
                    '_Phantom': None,
                },
                'PolkadotXcm': {
                    'Response': {
                        'interior': {
                            'Here': None,
                            'X1': 'scale_info::76',
                            'X2': (
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X3': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X4': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X5': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X6': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X7': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X8': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                        },
                        'parents': 'u8',
                    },
                    'Xcm': {
                        'interior': {
                            'Here': None,
                            'X1': 'scale_info::76',
                            'X2': (
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X3': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X4': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X5': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X6': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X7': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X8': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                        },
                        'parents': 'u8',
                    },
                },
                'TechnicalCommittee': {
                    'Member': 'AccountId',
                    'Members': (
                        'u32',
                        'u32',
                    ),
                    '_Phantom': None,
                },
                'Void': (),
                'system': {
                    'None': None,
                    'Root': None,
                    'Signed': 'AccountId',
                },
                None: None,
            },
        },
        'CumulusXcm': {
            'Relay': None,
            'SiblingParachain': 'u32',
        },
        'FinancialCouncil': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'GeneralCouncil': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'HomaCouncil': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'PolkadotXcm': {
            'Response': {
                'interior': {
                    'Here': None,
                    'X1': {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::78',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::78',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::78',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::80',
                            'part': 'scale_info::81',
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
            'Xcm': {
                'interior': {
                    'Here': None,
                    'X1': {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::78',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::78',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::78',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::80',
                            'part': 'scale_info::81',
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
        'TechnicalCommittee': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'Void': (),
    },
    'task_id': 'u32',
}
)
```

---------
### delay_scheduled_dispatch
#### Attributes
| Name | Type |
| -------- | -------- | 
| initial_origin | `Box<T::PalletsOrigin>` | 
| task_id | `ScheduleTaskIndex` | 
| additional_delay | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Authority', 'delay_scheduled_dispatch', {
    'additional_delay': 'u32',
    'initial_origin': {
        'Authority': {
            'delay': 'u32',
            'origin': {
                None: None,
                'Authority': {
                    'delay': 'u32',
                    'origin': {
                        'Authority': {
                            'delay': 'u32',
                            'origin': 'scale_info::114',
                        },
                        'system': {
                            'None': None,
                            'Root': None,
                            'Signed': 'AccountId',
                        },
                        None: None,
                        'CumulusXcm': {
                            'Relay': None,
                            'SiblingParachain': 'u32',
                        },
                        'FinancialCouncil': {
                            'Member': 'AccountId',
                            'Members': (
                                'u32',
                                'u32',
                            ),
                            '_Phantom': None,
                        },
                        'GeneralCouncil': {
                            'Member': 'AccountId',
                            'Members': (
                                'u32',
                                'u32',
                            ),
                            '_Phantom': None,
                        },
                        'HomaCouncil': {
                            'Member': 'AccountId',
                            'Members': (
                                'u32',
                                'u32',
                            ),
                            '_Phantom': None,
                        },
                        'PolkadotXcm': {
                            'Response': 'scale_info::74',
                            'Xcm': 'scale_info::74',
                        },
                        'TechnicalCommittee': {
                            'Member': 'AccountId',
                            'Members': (
                                'u32',
                                'u32',
                            ),
                            '_Phantom': None,
                        },
                        'Void': (),
                    },
                },
                'CumulusXcm': {
                    'Relay': None,
                    'SiblingParachain': 'u32',
                },
                'FinancialCouncil': {
                    'Member': 'AccountId',
                    'Members': (
                        'u32',
                        'u32',
                    ),
                    '_Phantom': None,
                },
                'GeneralCouncil': {
                    'Member': 'AccountId',
                    'Members': (
                        'u32',
                        'u32',
                    ),
                    '_Phantom': None,
                },
                'HomaCouncil': {
                    'Member': 'AccountId',
                    'Members': (
                        'u32',
                        'u32',
                    ),
                    '_Phantom': None,
                },
                'PolkadotXcm': {
                    'Response': {
                        'interior': {
                            'Here': None,
                            'X1': 'scale_info::76',
                            'X2': (
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X3': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X4': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X5': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X6': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X7': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X8': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                        },
                        'parents': 'u8',
                    },
                    'Xcm': {
                        'interior': {
                            'Here': None,
                            'X1': 'scale_info::76',
                            'X2': (
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X3': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X4': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X5': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X6': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X7': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X8': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                        },
                        'parents': 'u8',
                    },
                },
                'TechnicalCommittee': {
                    'Member': 'AccountId',
                    'Members': (
                        'u32',
                        'u32',
                    ),
                    '_Phantom': None,
                },
                'Void': (),
                'system': {
                    'None': None,
                    'Root': None,
                    'Signed': 'AccountId',
                },
            },
        },
        'CumulusXcm': {
            'Relay': None,
            'SiblingParachain': 'u32',
        },
        None: None,
        'FinancialCouncil': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'GeneralCouncil': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'HomaCouncil': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'PolkadotXcm': {
            'Response': {
                'interior': {
                    'Here': None,
                    'X1': {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::78',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::78',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::78',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::80',
                            'part': 'scale_info::81',
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
            'Xcm': {
                'interior': {
                    'Here': None,
                    'X1': {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::78',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::78',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::78',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::80',
                            'part': 'scale_info::81',
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
        'TechnicalCommittee': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'Void': (),
        'system': {
            'None': None,
            'Root': None,
            'Signed': 'AccountId',
        },
    },
    'task_id': 'u32',
}
)
```

---------
### dispatch_as
#### Attributes
| Name | Type |
| -------- | -------- | 
| as_origin | `T::AsOriginId` | 
| call | `Box<CallOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Authority', 'dispatch_as', {
    'as_origin': (
        'Root',
        'Treasury',
        'HonzonTreasury',
        'HomaTreasury',
        'TreasuryReserve',
    ),
    'call': 'Call',
}
)
```

---------
### fast_track_scheduled_dispatch
#### Attributes
| Name | Type |
| -------- | -------- | 
| initial_origin | `Box<T::PalletsOrigin>` | 
| task_id | `ScheduleTaskIndex` | 
| when | `DispatchTime<T::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'Authority', 'fast_track_scheduled_dispatch', {
    'initial_origin': {
        'system': {
            'None': None,
            'Root': None,
            'Signed': 'AccountId',
        },
        None: None,
        'Authority': {
            'delay': 'u32',
            'origin': {
                'Authority': {
                    'delay': 'u32',
                    'origin': {
                        'Authority': {
                            'delay': 'u32',
                            'origin': 'scale_info::114',
                        },
                        'CumulusXcm': {
                            'Relay': None,
                            'SiblingParachain': 'u32',
                        },
                        'FinancialCouncil': {
                            'Member': 'AccountId',
                            'Members': (
                                'u32',
                                'u32',
                            ),
                            '_Phantom': None,
                        },
                        'GeneralCouncil': {
                            'Member': 'AccountId',
                            'Members': (
                                'u32',
                                'u32',
                            ),
                            '_Phantom': None,
                        },
                        'HomaCouncil': {
                            'Member': 'AccountId',
                            'Members': (
                                'u32',
                                'u32',
                            ),
                            '_Phantom': None,
                        },
                        'PolkadotXcm': {
                            'Response': 'scale_info::74',
                            'Xcm': 'scale_info::74',
                        },
                        'TechnicalCommittee': {
                            'Member': 'AccountId',
                            'Members': (
                                'u32',
                                'u32',
                            ),
                            '_Phantom': None,
                        },
                        'Void': (),
                        'system': {
                            'None': None,
                            'Root': None,
                            'Signed': 'AccountId',
                        },
                        None: None,
                    },
                },
                'CumulusXcm': {
                    'Relay': None,
                    'SiblingParachain': 'u32',
                },
                'FinancialCouncil': {
                    'Member': 'AccountId',
                    'Members': (
                        'u32',
                        'u32',
                    ),
                    '_Phantom': None,
                },
                'GeneralCouncil': {
                    'Member': 'AccountId',
                    'Members': (
                        'u32',
                        'u32',
                    ),
                    '_Phantom': None,
                },
                'HomaCouncil': {
                    'Member': 'AccountId',
                    'Members': (
                        'u32',
                        'u32',
                    ),
                    '_Phantom': None,
                },
                'PolkadotXcm': {
                    'Response': {
                        'interior': {
                            'Here': None,
                            'X1': 'scale_info::76',
                            'X2': (
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X3': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X4': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X5': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X6': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X7': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X8': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                        },
                        'parents': 'u8',
                    },
                    'Xcm': {
                        'interior': {
                            'Here': None,
                            'X1': 'scale_info::76',
                            'X2': (
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X3': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X4': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X5': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X6': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X7': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                            'X8': (
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                                'scale_info::76',
                            ),
                        },
                        'parents': 'u8',
                    },
                },
                'Void': (),
                None: None,
                'TechnicalCommittee': {
                    'Member': 'AccountId',
                    'Members': (
                        'u32',
                        'u32',
                    ),
                    '_Phantom': None,
                },
                'system': {
                    'None': None,
                    'Root': None,
                    'Signed': 'AccountId',
                },
            },
        },
        'CumulusXcm': {
            'Relay': None,
            'SiblingParachain': 'u32',
        },
        'FinancialCouncil': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'GeneralCouncil': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'HomaCouncil': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'PolkadotXcm': {
            'Response': {
                'interior': {
                    'Here': None,
                    'X1': {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::78',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::78',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::78',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::80',
                            'part': 'scale_info::81',
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
            'Xcm': {
                'interior': {
                    'Here': None,
                    'X1': {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::78',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::78',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::78',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::80',
                            'part': 'scale_info::81',
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
        'TechnicalCommittee': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'Void': (),
    },
    'task_id': 'u32',
    'when': {
        'After': 'u32',
        'At': 'u32',
    },
}
)
```

---------
### remove_authorized_call
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Authority', 'remove_authorized_call', {'hash': '[u8; 32]'}
)
```

---------
### schedule_dispatch
#### Attributes
| Name | Type |
| -------- | -------- | 
| when | `DispatchTime<T::BlockNumber>` | 
| priority | `Priority` | 
| with_delayed_origin | `bool` | 
| call | `Box<CallOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Authority', 'schedule_dispatch', {
    'call': 'Call',
    'priority': 'u8',
    'when': {
        'After': 'u32',
        'At': 'u32',
    },
    'with_delayed_origin': 'bool',
}
)
```

---------
### trigger_call
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 
| call_weight_bound | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'Authority', 'trigger_call', {
    'call_weight_bound': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
    'hash': '[u8; 32]',
}
)
```

---------
### trigger_old_call
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 
| call_weight_bound | `OldWeight` | 

#### Python
```python
call = substrate.compose_call(
    'Authority', 'trigger_old_call', {
    'call_weight_bound': 'u64',
    'hash': '[u8; 32]',
}
)
```

---------
## Events

---------
### AuthorizedCall
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```[u8; 32]```
| caller | `Option<T::AccountId>` | ```(None, 'AccountId')```

---------
### Cancelled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| origin | `T::PalletsOrigin` | ```{'system': {'Root': None, 'Signed': 'AccountId', 'None': None}, None: None, 'Void': (), 'PolkadotXcm': {'Xcm': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::76', 'scale_info::76'), 'X3': ('scale_info::76', 'scale_info::76', 'scale_info::76'), 'X4': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X5': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X6': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X7': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X8': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76')}}, 'Response': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::76', 'scale_info::76'), 'X3': ('scale_info::76', 'scale_info::76', 'scale_info::76'), 'X4': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X5': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X6': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X7': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X8': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76')}}}, 'CumulusXcm': {'Relay': None, 'SiblingParachain': 'u32'}, 'Authority': {'delay': 'u32', 'origin': {'system': {'Root': None, 'Signed': 'AccountId', 'None': None}, None: None, 'Void': (), 'PolkadotXcm': {'Xcm': {'parents': 'u8', 'interior': 'scale_info::75'}, 'Response': {'parents': 'u8', 'interior': 'scale_info::75'}}, 'CumulusXcm': {'Relay': None, 'SiblingParachain': 'u32'}, 'Authority': {'delay': 'u32', 'origin': {'system': 'scale_info::115', None: None, 'Void': 'scale_info::123', 'PolkadotXcm': 'scale_info::116', 'CumulusXcm': 'scale_info::117', 'Authority': 'scale_info::118', 'GeneralCouncil': 'scale_info::119', 'FinancialCouncil': 'scale_info::120', 'HomaCouncil': 'scale_info::121', 'TechnicalCommittee': 'scale_info::122'}}, 'GeneralCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'FinancialCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'HomaCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'TechnicalCommittee': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}}}, 'GeneralCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'FinancialCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'HomaCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'TechnicalCommittee': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}}```
| index | `ScheduleTaskIndex` | ```u32```

---------
### Delayed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| origin | `T::PalletsOrigin` | ```{'system': {'Root': None, 'Signed': 'AccountId', 'None': None}, None: None, 'Void': (), 'PolkadotXcm': {'Xcm': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::76', 'scale_info::76'), 'X3': ('scale_info::76', 'scale_info::76', 'scale_info::76'), 'X4': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X5': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X6': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X7': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X8': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76')}}, 'Response': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::76', 'scale_info::76'), 'X3': ('scale_info::76', 'scale_info::76', 'scale_info::76'), 'X4': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X5': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X6': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X7': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X8': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76')}}}, 'CumulusXcm': {'Relay': None, 'SiblingParachain': 'u32'}, 'Authority': {'delay': 'u32', 'origin': {'system': {'Root': None, 'Signed': 'AccountId', 'None': None}, None: None, 'Void': (), 'PolkadotXcm': {'Xcm': {'parents': 'u8', 'interior': 'scale_info::75'}, 'Response': {'parents': 'u8', 'interior': 'scale_info::75'}}, 'CumulusXcm': {'Relay': None, 'SiblingParachain': 'u32'}, 'Authority': {'delay': 'u32', 'origin': {'system': 'scale_info::115', None: None, 'Void': 'scale_info::123', 'PolkadotXcm': 'scale_info::116', 'CumulusXcm': 'scale_info::117', 'Authority': 'scale_info::118', 'GeneralCouncil': 'scale_info::119', 'FinancialCouncil': 'scale_info::120', 'HomaCouncil': 'scale_info::121', 'TechnicalCommittee': 'scale_info::122'}}, 'GeneralCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'FinancialCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'HomaCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'TechnicalCommittee': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}}}, 'GeneralCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'FinancialCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'HomaCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'TechnicalCommittee': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}}```
| index | `ScheduleTaskIndex` | ```u32```
| when | `T::BlockNumber` | ```u32```

---------
### Dispatched
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### FastTracked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| origin | `T::PalletsOrigin` | ```{'system': {'Root': None, 'Signed': 'AccountId', 'None': None}, None: None, 'Void': (), 'PolkadotXcm': {'Xcm': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::76', 'scale_info::76'), 'X3': ('scale_info::76', 'scale_info::76', 'scale_info::76'), 'X4': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X5': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X6': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X7': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X8': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76')}}, 'Response': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::76', 'scale_info::76'), 'X3': ('scale_info::76', 'scale_info::76', 'scale_info::76'), 'X4': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X5': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X6': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X7': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X8': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76')}}}, 'CumulusXcm': {'Relay': None, 'SiblingParachain': 'u32'}, 'Authority': {'delay': 'u32', 'origin': {'system': {'Root': None, 'Signed': 'AccountId', 'None': None}, None: None, 'Void': (), 'PolkadotXcm': {'Xcm': {'parents': 'u8', 'interior': 'scale_info::75'}, 'Response': {'parents': 'u8', 'interior': 'scale_info::75'}}, 'CumulusXcm': {'Relay': None, 'SiblingParachain': 'u32'}, 'Authority': {'delay': 'u32', 'origin': {'system': 'scale_info::115', None: None, 'Void': 'scale_info::123', 'PolkadotXcm': 'scale_info::116', 'CumulusXcm': 'scale_info::117', 'Authority': 'scale_info::118', 'GeneralCouncil': 'scale_info::119', 'FinancialCouncil': 'scale_info::120', 'HomaCouncil': 'scale_info::121', 'TechnicalCommittee': 'scale_info::122'}}, 'GeneralCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'FinancialCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'HomaCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'TechnicalCommittee': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}}}, 'GeneralCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'FinancialCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'HomaCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'TechnicalCommittee': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}}```
| index | `ScheduleTaskIndex` | ```u32```
| when | `T::BlockNumber` | ```u32```

---------
### RemovedAuthorizedCall
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```[u8; 32]```

---------
### Scheduled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| origin | `T::PalletsOrigin` | ```{'system': {'Root': None, 'Signed': 'AccountId', 'None': None}, None: None, 'Void': (), 'PolkadotXcm': {'Xcm': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::76', 'scale_info::76'), 'X3': ('scale_info::76', 'scale_info::76', 'scale_info::76'), 'X4': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X5': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X6': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X7': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X8': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76')}}, 'Response': {'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::76', 'scale_info::76'), 'X3': ('scale_info::76', 'scale_info::76', 'scale_info::76'), 'X4': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X5': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X6': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X7': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76'), 'X8': ('scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76', 'scale_info::76')}}}, 'CumulusXcm': {'Relay': None, 'SiblingParachain': 'u32'}, 'Authority': {'delay': 'u32', 'origin': {'system': {'Root': None, 'Signed': 'AccountId', 'None': None}, None: None, 'Void': (), 'PolkadotXcm': {'Xcm': {'parents': 'u8', 'interior': 'scale_info::75'}, 'Response': {'parents': 'u8', 'interior': 'scale_info::75'}}, 'CumulusXcm': {'Relay': None, 'SiblingParachain': 'u32'}, 'Authority': {'delay': 'u32', 'origin': {'system': 'scale_info::115', None: None, 'Void': 'scale_info::123', 'PolkadotXcm': 'scale_info::116', 'CumulusXcm': 'scale_info::117', 'Authority': 'scale_info::118', 'GeneralCouncil': 'scale_info::119', 'FinancialCouncil': 'scale_info::120', 'HomaCouncil': 'scale_info::121', 'TechnicalCommittee': 'scale_info::122'}}, 'GeneralCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'FinancialCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'HomaCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'TechnicalCommittee': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}}}, 'GeneralCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'FinancialCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'HomaCouncil': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}, 'TechnicalCommittee': {'Members': ('u32', 'u32'), 'Member': 'AccountId', '_Phantom': None}}```
| index | `ScheduleTaskIndex` | ```u32```

---------
### TriggeredCallBy
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```[u8; 32]```
| caller | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### NextTaskIndex

#### Python
```python
result = substrate.query(
    'Authority', 'NextTaskIndex', []
)
```

#### Return value
```python
'u32'
```
---------
### SavedCalls

#### Python
```python
result = substrate.query(
    'Authority', 'SavedCalls', ['[u8; 32]']
)
```

#### Return value
```python
('Call', (None, 'AccountId'))
```
---------
## Errors

---------
### CallNotAuthorized

---------
### FailedToCancel

---------
### FailedToDelay

---------
### FailedToFastTrack

---------
### FailedToSchedule

---------
### TriggerCallNotPermitted

---------
### WrongCallWeightBound

---------