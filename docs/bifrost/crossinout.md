
# CrossInOut

---------
## Calls

---------
### add_to_issue_whitelist
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| account | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CrossInOut', 'add_to_issue_whitelist', {
    'account': 'AccountId',
    'currency_id': {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
}
)
```

---------
### add_to_register_whitelist
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| account | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CrossInOut', 'add_to_register_whitelist', {
    'account': 'AccountId',
    'currency_id': {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
}
)
```

---------
### change_outer_linked_account
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| foreign_location | `Box<MultiLocation>` | 

#### Python
```python
call = substrate.compose_call(
    'CrossInOut', 'change_outer_linked_account', {
    'currency_id': {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
    'foreign_location': {
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
                        'AtLeastProportion': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Fraction': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Members': {
                            'count': 'u32',
                        },
                        'MoreThanProportion': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Voice': None,
                    },
                },
            },
            'X2': (
                {
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
                {
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
            ),
            'X3': (
                {
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
                {
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
                {
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
            ),
            'X4': (
                {
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
                {
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
                {
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
                {
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
            ),
            'X5': (
                {
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
                {
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
                {
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
                {
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
                {
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
            ),
            'X6': (
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
            ),
            'X7': (
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
            ),
            'X8': (
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
            ),
        },
        'parents': 'u8',
    },
}
)
```

---------
### cross_in
#### Attributes
| Name | Type |
| -------- | -------- | 
| location | `Box<MultiLocation>` | 
| currency_id | `CurrencyId` | 
| amount | `BalanceOf<T>` | 
| remark | `Option<Vec<u8>>` | 

#### Python
```python
call = substrate.compose_call(
    'CrossInOut', 'cross_in', {
    'amount': 'u128',
    'currency_id': {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
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
                        'AtLeastProportion': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Fraction': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Members': {
                            'count': 'u32',
                        },
                        'MoreThanProportion': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Voice': None,
                    },
                },
            },
            'X2': (
                {
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
                {
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
            ),
            'X3': (
                {
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
                {
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
                {
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
            ),
            'X4': (
                {
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
                {
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
                {
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
                {
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
            ),
            'X5': (
                {
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
                {
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
                {
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
                {
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
                {
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
            ),
            'X6': (
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
            ),
            'X7': (
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
            ),
            'X8': (
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
            ),
        },
        'parents': 'u8',
    },
    'remark': (None, 'Bytes'),
}
)
```

---------
### cross_out
Destroy some balance from an account and issue cross-out event.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CrossInOut', 'cross_out', {
    'amount': 'u128',
    'currency_id': {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
}
)
```

---------
### deregister_currency_for_cross_in_out
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'CrossInOut', 'deregister_currency_for_cross_in_out', {
    'currency_id': {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
}
)
```

---------
### register_currency_for_cross_in_out
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'CrossInOut', 'register_currency_for_cross_in_out', {
    'currency_id': {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
}
)
```

---------
### register_linked_account
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| who | `AccountIdOf<T>` | 
| foreign_location | `Box<MultiLocation>` | 

#### Python
```python
call = substrate.compose_call(
    'CrossInOut', 'register_linked_account', {
    'currency_id': {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
    'foreign_location': {
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
                        'AtLeastProportion': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Fraction': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Members': {
                            'count': 'u32',
                        },
                        'MoreThanProportion': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Voice': None,
                    },
                },
            },
            'X2': (
                {
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
                {
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
            ),
            'X3': (
                {
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
                {
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
                {
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
            ),
            'X4': (
                {
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
                {
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
                {
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
                {
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
            ),
            'X5': (
                {
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
                {
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
                {
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
                {
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
                {
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
            ),
            'X6': (
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
            ),
            'X7': (
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
            ),
            'X8': (
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
            ),
        },
        'parents': 'u8',
    },
    'who': 'AccountId',
}
)
```

---------
### remove_from_issue_whitelist
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| account | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CrossInOut', 'remove_from_issue_whitelist', {
    'account': 'AccountId',
    'currency_id': {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
}
)
```

---------
### remove_from_register_whitelist
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| account | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CrossInOut', 'remove_from_register_whitelist', {
    'account': 'AccountId',
    'currency_id': {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
}
)
```

---------
### set_crossing_minimum_amount
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| cross_in_minimum | `BalanceOf<T>` | 
| cross_out_minimum | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CrossInOut', 'set_crossing_minimum_amount', {
    'cross_in_minimum': 'u128',
    'cross_out_minimum': 'u128',
    'currency_id': {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
}
)
```

---------
## Events

---------
### AddedToIssueList
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `AccountIdOf<T>` | ```AccountId```
| currency_id | `CurrencyId` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```

---------
### AddedToRegisterList
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `AccountIdOf<T>` | ```AccountId```
| currency_id | `CurrencyId` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```

---------
### CrossedIn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `CurrencyId` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```
| dest | `AccountIdOf<T>` | ```AccountId```
| location | `MultiLocation` | ```{'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': {'Any': None, 'Named': 'Bytes', 'Polkadot': None, 'Kusama': None}, 'id': '[u8; 32]'}, 'AccountIndex64': {'network': {'Any': None, 'Named': 'Bytes', 'Polkadot': None, 'Kusama': None}, 'index': 'u64'}, 'AccountKey20': {'network': {'Any': None, 'Named': 'Bytes', 'Polkadot': None, 'Kusama': None}, 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': {'Unit': None, 'Named': 'Bytes', 'Index': 'u32', 'Executive': None, 'Technical': None, 'Legislative': None, 'Judicial': None}, 'part': {'Voice': None, 'Members': 'InnerStruct', 'Fraction': 'InnerStruct', 'AtLeastProportion': 'InnerStruct', 'MoreThanProportion': 'InnerStruct'}}}, 'X2': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}), 'X3': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}), 'X4': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}), 'X5': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}), 'X6': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}), 'X7': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}), 'X8': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}})}}```
| amount | `BalanceOf<T>` | ```u128```
| remark | `Option<Vec<u8>>` | ```(None, 'Bytes')```

---------
### CrossedOut
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `CurrencyId` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```
| crosser | `AccountIdOf<T>` | ```AccountId```
| location | `MultiLocation` | ```{'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': {'Any': None, 'Named': 'Bytes', 'Polkadot': None, 'Kusama': None}, 'id': '[u8; 32]'}, 'AccountIndex64': {'network': {'Any': None, 'Named': 'Bytes', 'Polkadot': None, 'Kusama': None}, 'index': 'u64'}, 'AccountKey20': {'network': {'Any': None, 'Named': 'Bytes', 'Polkadot': None, 'Kusama': None}, 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': {'Unit': None, 'Named': 'Bytes', 'Index': 'u32', 'Executive': None, 'Technical': None, 'Legislative': None, 'Judicial': None}, 'part': {'Voice': None, 'Members': 'InnerStruct', 'Fraction': 'InnerStruct', 'AtLeastProportion': 'InnerStruct', 'MoreThanProportion': 'InnerStruct'}}}, 'X2': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}), 'X3': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}), 'X4': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}), 'X5': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}), 'X6': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}), 'X7': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}), 'X8': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}})}}```
| amount | `BalanceOf<T>` | ```u128```

---------
### CrossingMinimumAmountSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `CurrencyId` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```
| cross_in_minimum | `BalanceOf<T>` | ```u128```
| cross_out_minimum | `BalanceOf<T>` | ```u128```

---------
### CurrencyDeregistered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `CurrencyId` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```

---------
### CurrencyRegistered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `CurrencyId` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```

---------
### LinkedAccountRegistered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `CurrencyId` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```
| who | `AccountIdOf<T>` | ```AccountId```
| foreign_location | `MultiLocation` | ```{'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': {'Any': None, 'Named': 'Bytes', 'Polkadot': None, 'Kusama': None}, 'id': '[u8; 32]'}, 'AccountIndex64': {'network': {'Any': None, 'Named': 'Bytes', 'Polkadot': None, 'Kusama': None}, 'index': 'u64'}, 'AccountKey20': {'network': {'Any': None, 'Named': 'Bytes', 'Polkadot': None, 'Kusama': None}, 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': {'Unit': None, 'Named': 'Bytes', 'Index': 'u32', 'Executive': None, 'Technical': None, 'Legislative': None, 'Judicial': None}, 'part': {'Voice': None, 'Members': 'InnerStruct', 'Fraction': 'InnerStruct', 'AtLeastProportion': 'InnerStruct', 'MoreThanProportion': 'InnerStruct'}}}, 'X2': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}), 'X3': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}), 'X4': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}), 'X5': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}), 'X6': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}), 'X7': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}), 'X8': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::65', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::65', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::65', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::69', 'part': 'scale_info::70'}})}}```

---------
### RemovedFromIssueList
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `AccountIdOf<T>` | ```AccountId```
| currency_id | `CurrencyId` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```

---------
### RemovedFromRegisterList
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `AccountIdOf<T>` | ```AccountId```
| currency_id | `CurrencyId` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```

---------
## Storage functions

---------
### AccountToOuterMultilocation
 Mapping a Bifrost account to a multilocation of a outer chain

#### Python
```python
result = substrate.query(
    'CrossInOut', 'AccountToOuterMultilocation', [
    {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
    'AccountId',
]
)
```

#### Return value
```python
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
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
        ),
        'X3': (
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
        ),
        'X4': (
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
        ),
        'X5': (
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
        ),
        'X6': (
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
        ),
        'X7': (
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
        ),
        'X8': (
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
            {
                'AccountId32': {'id': '[u8; 32]', 'network': 'scale_info::65'},
                'AccountIndex64': {
                    'index': 'u64',
                    'network': 'scale_info::65',
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': 'scale_info::65',
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': 'scale_info::69',
                    'part': 'scale_info::70',
                },
            },
        ),
    },
    'parents': 'u8',
}
```
---------
### CrossCurrencyRegistry
 To store currencies that support indirect cross-in and cross-out.

#### Python
```python
result = substrate.query(
    'CrossInOut', 'CrossCurrencyRegistry', [
    {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
]
)
```

#### Return value
```python
()
```
---------
### CrossingMinimumAmount
 minimum crossin and crossout amount【crossinMinimum, crossoutMinimum】

#### Python
```python
result = substrate.query(
    'CrossInOut', 'CrossingMinimumAmount', [
    {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
]
)
```

#### Return value
```python
('u128', 'u128')
```
---------
### IssueWhiteList
 Accounts in the whitelist can issue the corresponding Currency.

#### Python
```python
result = substrate.query(
    'CrossInOut', 'IssueWhiteList', [
    {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
]
)
```

#### Return value
```python
['AccountId']
```
---------
### OuterMultilocationToAccount
 Mapping a multilocation of a outer chain to a Bifrost account

#### Python
```python
result = substrate.query(
    'CrossInOut', 'OuterMultilocationToAccount', [
    {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
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
                        'AtLeastProportion': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Fraction': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Members': {
                            'count': 'u32',
                        },
                        'MoreThanProportion': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Voice': None,
                    },
                },
            },
            'X2': (
                {
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
                {
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
            ),
            'X3': (
                {
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
                {
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
                {
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
            ),
            'X4': (
                {
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
                {
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
                {
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
                {
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
            ),
            'X5': (
                {
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
                {
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
                {
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
                {
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
                {
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
            ),
            'X6': (
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
            ),
            'X7': (
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
            ),
            'X8': (
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
                {
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
            ),
        },
        'parents': 'u8',
    },
]
)
```

#### Return value
```python
'AccountId'
```
---------
### RegisterWhiteList
 Accounts in the whitelist can register the mapping between a multilocation and an accountId.

#### Python
```python
result = substrate.query(
    'CrossInOut', 'RegisterWhiteList', [
    {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
]
)
```

#### Return value
```python
['AccountId']
```
---------
## Errors

---------
### AlreadyExist

---------
### AmountLowerThanMinimum

---------
### CurrencyNotSupportCrossInAndOut

---------
### NoAccountIdMapping

---------
### NoCrossingMinimumSet

---------
### NoMultilocationMapping

---------
### NotAllowed

---------
### NotEnoughBalance

---------
### NotExist

---------