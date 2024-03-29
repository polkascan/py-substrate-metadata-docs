
# ZenlinkSwapRouter

---------
## Calls

---------
### swap_exact_token_for_tokens_through_stable_pool
See [`Pallet::swap_exact_token_for_tokens_through_stable_pool`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount_in | `T::Balance` | 
| amount_out_min | `T::Balance` | 
| routes | `Vec<Route<T::StablePoolId, T::StableCurrencyId, T::NormalCurrencyId
>>` | 
| to | `T::AccountId` | 
| deadline | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkSwapRouter', 'swap_exact_token_for_tokens_through_stable_pool', {
    'amount_in': 'u128',
    'amount_out_min': 'u128',
    'deadline': 'u32',
    'routes': [
        {
            'Normal': [
                {
                    'asset_index': 'u64',
                    'asset_type': 'u8',
                    'chain_id': 'u32',
                },
            ],
            'Stable': {
                'base_pool_id': 'u32',
                'from_currency': {
                    'BLP': 'u32',
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
                    'Lend': 'u8',
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
                'mode': (
                    'Single',
                    'FromBase',
                    'ToBase',
                ),
                'pool_id': 'u32',
                'to_currency': {
                    'BLP': 'u32',
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
                    'Lend': 'u8',
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
            },
        },
    ],
    'to': 'AccountId',
}
)
```

---------
## Errors

---------
### AmountSlippage

---------
### ConvertCurrencyFailed

---------
### Deadline

---------
### InvalidPath

---------
### InvalidRoutes

---------
### MismatchPoolAndCurrencyId

---------