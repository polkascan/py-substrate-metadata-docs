
# VstokenConversion

---------
## Calls

---------
### set_exchange_fee
#### Attributes
| Name | Type |
| -------- | -------- | 
| exchange_fee | `VstokenConversionExchangeFee<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'VstokenConversion', 'set_exchange_fee', {
    'exchange_fee': {
        'vsbond_exchange_fee_of_vstoken': 'u128',
        'vstoken_exchange_fee': 'u128',
    },
}
)
```

---------
### set_exchange_rate
#### Attributes
| Name | Type |
| -------- | -------- | 
| lease | `i32` | 
| exchange_rate | `VstokenConversionExchangeRate` | 

#### Python
```python
call = substrate.compose_call(
    'VstokenConversion', 'set_exchange_rate', {
    'exchange_rate': {
        'vsbond_convert_to_vstoken': 'u8',
        'vstoken_convert_to_vsbond': 'u8',
    },
    'lease': 'i32',
}
)
```

---------
### set_relaychain_lease
#### Attributes
| Name | Type |
| -------- | -------- | 
| lease | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'VstokenConversion', 'set_relaychain_lease', {'lease': 'u32'}
)
```

---------
### vsbond_convert_to_vstoken
#### Attributes
| Name | Type |
| -------- | -------- | 
| vs_bond_currency_id | `CurrencyIdOf<T>` | 
| vsbond_amount | `BalanceOf<T>` | 
| minimum_vstoken | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VstokenConversion', 'vsbond_convert_to_vstoken', {
    'minimum_vstoken': 'u128',
    'vs_bond_currency_id': {
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
    'vsbond_amount': 'u128',
}
)
```

---------
### vstoken_convert_to_vsbond
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyIdOf<T>` | 
| vstoken_amount | `BalanceOf<T>` | 
| minimum_vsbond | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VstokenConversion', 'vstoken_convert_to_vsbond', {
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
    'minimum_vsbond': 'u128',
    'vstoken_amount': 'u128',
}
)
```

---------
## Events

---------
### ExchangeFeeSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| exchange_fee | `VstokenConversionExchangeFee<BalanceOf<T>>` | ```{'vstoken_exchange_fee': 'u128', 'vsbond_exchange_fee_of_vstoken': 'u128'}```

---------
### ExchangeRateSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| lease | `i32` | ```i32```
| exchange_rate | `VstokenConversionExchangeRate` | ```{'vsbond_convert_to_vstoken': 'u8', 'vstoken_convert_to_vsbond': 'u8'}```

---------
### RelaychainLeaseSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| lease | `u32` | ```u32```

---------
### VsbondConvertToVsdot
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| address | `AccountIdOf<T>` | ```AccountId```
| currency_id | `CurrencyIdOf<T>` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```
| vsbond_amount | `BalanceOf<T>` | ```u128```
| vsdot_amount | `BalanceOf<T>` | ```u128```

---------
### VsbondConvertToVsksm
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| address | `AccountIdOf<T>` | ```AccountId```
| currency_id | `CurrencyIdOf<T>` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```
| vsbond_amount | `BalanceOf<T>` | ```u128```
| vsksm_amount | `BalanceOf<T>` | ```u128```

---------
### VsbondConvertToVstoken
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| address | `AccountIdOf<T>` | ```AccountId```
| currency_id | `CurrencyIdOf<T>` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```
| vsbond_amount | `BalanceOf<T>` | ```u128```
| vstoken_amount | `BalanceOf<T>` | ```u128```

---------
### VsdotConvertToVsbond
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| address | `AccountIdOf<T>` | ```AccountId```
| currency_id | `CurrencyIdOf<T>` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```
| vsbond_amount | `BalanceOf<T>` | ```u128```
| vsdot_amount | `BalanceOf<T>` | ```u128```

---------
### VsksmConvertToVsbond
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| address | `AccountIdOf<T>` | ```AccountId```
| currency_id | `CurrencyIdOf<T>` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```
| vsbond_amount | `BalanceOf<T>` | ```u128```
| vsksm_amount | `BalanceOf<T>` | ```u128```

---------
### VstokenConvertToVsbond
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| address | `AccountIdOf<T>` | ```AccountId```
| currency_id | `CurrencyIdOf<T>` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```
| vsbond_amount | `BalanceOf<T>` | ```u128```
| vstoken_amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### ExchangeFee
 exchange fee

#### Python
```python
result = substrate.query(
    'VstokenConversion', 'ExchangeFee', []
)
```

#### Return value
```python
{'vsbond_exchange_fee_of_vstoken': 'u128', 'vstoken_exchange_fee': 'u128'}
```
---------
### ExchangeRate

#### Python
```python
result = substrate.query(
    'VstokenConversion', 'ExchangeRate', ['i32']
)
```

#### Return value
```python
{'vsbond_convert_to_vstoken': 'u8', 'vstoken_convert_to_vsbond': 'u8'}
```
---------
### RelaychainLease

#### Python
```python
result = substrate.query(
    'VstokenConversion', 'RelaychainLease', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### RelayCurrencyId
#### Value
```python
{'Token': 'KSM'}
```
#### Python
```python
constant = substrate.get_constant('VstokenConversion', 'RelayCurrencyId')
```
---------
### TreasuryAccount
#### Value
```python
'eCSrvbA5gGNYdM3UjBNxcBNBqGxtz3SEEfydKragtL4pJ4F'
```
#### Python
```python
constant = substrate.get_constant('VstokenConversion', 'TreasuryAccount')
```
---------
### VsbondAccount
#### Value
```python
'0x62662f73616c7062'
```
#### Python
```python
constant = substrate.get_constant('VstokenConversion', 'VsbondAccount')
```
---------
## Errors

---------
### CalculationOverflow

---------
### NotEnoughBalance

---------
### NotSupportTokenType

---------