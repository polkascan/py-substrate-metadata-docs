
# DexSwapRouter

---------
## Calls

---------
### swap_exact_tokens_for_tokens
Atomically execute a series of trades using `DexGeneral` and/or `DexStable`.
The whole transaction will rollback if any of the trades fail.

\#\# Complexity
- O(T) where T is the number of trades.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount_in | `T::Balance` | 
| amount_out_min | `T::Balance` | 
| routes | `Vec<Route<T::StablePoolId, T::CurrencyId>>` | 
| to | `T::AccountId` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'DexSwapRouter', 'swap_exact_tokens_for_tokens', {
    'amount_in': 'u128',
    'amount_out_min': 'u128',
    'deadline': 'u32',
    'routes': [
        {
            'General': [
                {
                    'ForeignAsset': 'u32',
                    'LendToken': 'u32',
                    'LpToken': (
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
                        },
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
                        },
                    ),
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ],
            'Stable': {
                'base_pool_id': 'u32',
                'from_currency': {
                    'ForeignAsset': 'u32',
                    'LendToken': 'u32',
                    'LpToken': (
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
                        },
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
                        },
                    ),
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                'mode': (
                    'Single',
                    'FromBase',
                    'ToBase',
                ),
                'pool_id': 'u32',
                'to_currency': {
                    'ForeignAsset': 'u32',
                    'LendToken': 'u32',
                    'LpToken': (
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
                        },
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
                        },
                    ),
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
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