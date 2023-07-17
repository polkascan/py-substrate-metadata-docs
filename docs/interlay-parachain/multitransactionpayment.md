
# MultiTransactionPayment

---------
## Calls

---------
### with_fee_swap_path
#### Attributes
| Name | Type |
| -------- | -------- | 
| path | `Vec<T::CurrencyId>` | 
| amount_in_max | `<T as currency::Config>::Balance` | 
| call | `Box<CallOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTransactionPayment', 'with_fee_swap_path', {
    'amount_in_max': 'u128',
    'call': 'Call',
    'path': [
        {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
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
                {
                    'ForeignAsset': 'u32',
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
}
)
```

---------