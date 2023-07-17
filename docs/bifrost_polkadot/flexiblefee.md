
# FlexibleFee

---------
## Calls

---------
### remove_from_user_fee_charge_order_list
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'FlexibleFee', 'remove_from_user_fee_charge_order_list', {}
)
```

---------
### set_universal_fee_currency_order_list
Set universal fee currency order list
#### Attributes
| Name | Type |
| -------- | -------- | 
| default_list | `BoundedVec<CurrencyIdOf<T>, T::MaxFeeCurrencyOrderListLen>` | 

#### Python
```python
call = substrate.compose_call(
    'FlexibleFee', 'set_universal_fee_currency_order_list', {
    'default_list': [
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
    ],
}
)
```

---------
### set_user_default_fee_currency
Set user default fee currency
#### Attributes
| Name | Type |
| -------- | -------- | 
| maybe_fee_currency | `Option<CurrencyIdOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'FlexibleFee', 'set_user_default_fee_currency', {
    'maybe_fee_currency': (
        None,
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
    ),
}
)
```

---------
## Events

---------
### ExtraFeeDeducted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ExtraFeeName` | ```('SalpContribute', 'StatemineTransfer', 'NoExtraFee')```
| None | `CurrencyIdOf<T>` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```
| None | `PalletBalanceOf<T>` | ```u128```

---------
### FixedRateFeeExchanged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyIdOf<T>` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```
| None | `PalletBalanceOf<T>` | ```u128```

---------
### FlexibleFeeExchanged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyIdOf<T>` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```
| None | `PalletBalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### UniversalFeeCurrencyOrderList
 Universal fee currency order list for all users

#### Python
```python
result = substrate.query(
    'FlexibleFee', 'UniversalFeeCurrencyOrderList', []
)
```

#### Return value
```python
[
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
        'VSBond2': ('u8', 'u32', 'u32', 'u32'),
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
```
---------
### UserDefaultFeeCurrency
 User default fee currency, if set, will be used as the first fee currency, and then use the
 universal fee currency order list

#### Python
```python
result = substrate.query(
    'FlexibleFee', 'UserDefaultFeeCurrency', ['AccountId']
)
```

#### Return value
```python
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
    'VSBond2': ('u8', 'u32', 'u32', 'u32'),
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
}
```
---------
### UserFeeChargeOrderList
 Deprecated. To-be removed after all data deleted.

#### Python
```python
result = substrate.query(
    'FlexibleFee', 'UserFeeChargeOrderList', ['AccountId']
)
```

#### Return value
```python
[
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
        'VSBond2': ('u8', 'u32', 'u32', 'u32'),
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
```
---------
## Constants

---------
### AltFeeCurrencyExchangeRate
 Alternative Fee currency exchange rate: ?x Fee currency: ?y Native currency
#### Value
```python
(1, 100)
```
#### Python
```python
constant = substrate.get_constant('FlexibleFee', 'AltFeeCurrencyExchangeRate')
```
---------
### AlternativeFeeCurrencyId
#### Value
```python
{'Token2': 0}
```
#### Python
```python
constant = substrate.get_constant('FlexibleFee', 'AlternativeFeeCurrencyId')
```
---------
### MaxFeeCurrencyOrderListLen
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('FlexibleFee', 'MaxFeeCurrencyOrderListLen')
```
---------
### NativeCurrencyId
#### Value
```python
{'Native': 'BNC'}
```
#### Python
```python
constant = substrate.get_constant('FlexibleFee', 'NativeCurrencyId')
```
---------
### TreasuryAccount
#### Value
```python
'eCSrvbA5gGNYdM3UjBNxcBNBqGxtz3SEEfydKragtL4pJ4F'
```
#### Python
```python
constant = substrate.get_constant('FlexibleFee', 'TreasuryAccount')
```
---------
## Errors

---------
### ConversionError

---------
### NotEnoughBalance

---------
### Overflow

---------
### WrongListLength

---------