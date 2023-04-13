
# DexSwapRouter

---------
## Calls

---------
### swap_exact_token_for_tokens_through_stable_pool
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
    'DexSwapRouter', 'swap_exact_token_for_tokens_through_stable_pool', {
    'amount_in': 'u128',
    'amount_out_min': 'u128',
    'deadline': 'u32',
    'routes': [
        {
            'Normal': [
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
## Constants

---------
### MaxSwaps
 The maximum number of swaps allowed in routes
#### Value
```python
4
```
#### Python
```python
constant = substrate.get_constant('DexSwapRouter', 'MaxSwaps')
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
### ExceededSwapLimit

---------
### InvalidPath

---------
### InvalidRoutes

---------
### MismatchPoolAndCurrencyId

---------