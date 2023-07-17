
# Honzon

---------
## Calls

---------
### adjust_loan
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| collateral_adjustment | `Amount` | 
| debit_adjustment | `Amount` | 

#### Python
```python
call = substrate.compose_call(
    'Honzon', 'adjust_loan', {
    'collateral_adjustment': 'i128',
    'currency_id': {
        'DexShare': (
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
        ),
        'Erc20': '[u8; 20]',
        'ForeignAsset': 'u16',
        'LiquidCrowdloan': 'u32',
        'StableAssetPoolToken': 'u32',
        'Token': (
            'ACA',
            'AUSD',
            'DOT',
            'LDOT',
            'TAP',
            'KAR',
            'KUSD',
            'KSM',
            'LKSM',
            'TAI',
            'BNC',
            'VSKSM',
            'PHA',
            'KINT',
            'KBTC',
        ),
    },
    'debit_adjustment': 'i128',
}
)
```

---------
### adjust_loan_by_debit_value
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| collateral_adjustment | `Amount` | 
| debit_value_adjustment | `Amount` | 

#### Python
```python
call = substrate.compose_call(
    'Honzon', 'adjust_loan_by_debit_value', {
    'collateral_adjustment': 'i128',
    'currency_id': {
        'DexShare': (
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
        ),
        'Erc20': '[u8; 20]',
        'ForeignAsset': 'u16',
        'LiquidCrowdloan': 'u32',
        'StableAssetPoolToken': 'u32',
        'Token': (
            'ACA',
            'AUSD',
            'DOT',
            'LDOT',
            'TAP',
            'KAR',
            'KUSD',
            'KSM',
            'LKSM',
            'TAI',
            'BNC',
            'VSKSM',
            'PHA',
            'KINT',
            'KBTC',
        ),
    },
    'debit_value_adjustment': 'i128',
}
)
```

---------
### authorize
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| to | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'Honzon', 'authorize', {
    'currency_id': {
        'DexShare': (
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
        ),
        'Erc20': '[u8; 20]',
        'ForeignAsset': 'u16',
        'LiquidCrowdloan': 'u32',
        'StableAssetPoolToken': 'u32',
        'Token': (
            'ACA',
            'AUSD',
            'DOT',
            'LDOT',
            'TAP',
            'KAR',
            'KUSD',
            'KSM',
            'LKSM',
            'TAI',
            'BNC',
            'VSKSM',
            'PHA',
            'KINT',
            'KBTC',
        ),
    },
    'to': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### close_loan_has_debit_by_dex
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| max_collateral_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Honzon', 'close_loan_has_debit_by_dex', {
    'currency_id': {
        'DexShare': (
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
        ),
        'Erc20': '[u8; 20]',
        'ForeignAsset': 'u16',
        'LiquidCrowdloan': 'u32',
        'StableAssetPoolToken': 'u32',
        'Token': (
            'ACA',
            'AUSD',
            'DOT',
            'LDOT',
            'TAP',
            'KAR',
            'KUSD',
            'KSM',
            'LKSM',
            'TAI',
            'BNC',
            'VSKSM',
            'PHA',
            'KINT',
            'KBTC',
        ),
    },
    'max_collateral_amount': 'u128',
}
)
```

---------
### expand_position_collateral
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| increase_debit_value | `Balance` | 
| min_increase_collateral | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Honzon', 'expand_position_collateral', {
    'currency_id': {
        'DexShare': (
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
        ),
        'Erc20': '[u8; 20]',
        'ForeignAsset': 'u16',
        'LiquidCrowdloan': 'u32',
        'StableAssetPoolToken': 'u32',
        'Token': (
            'ACA',
            'AUSD',
            'DOT',
            'LDOT',
            'TAP',
            'KAR',
            'KUSD',
            'KSM',
            'LKSM',
            'TAI',
            'BNC',
            'VSKSM',
            'PHA',
            'KINT',
            'KBTC',
        ),
    },
    'increase_debit_value': 'u128',
    'min_increase_collateral': 'u128',
}
)
```

---------
### shrink_position_debit
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| decrease_collateral | `Balance` | 
| min_decrease_debit_value | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Honzon', 'shrink_position_debit', {
    'currency_id': {
        'DexShare': (
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
        ),
        'Erc20': '[u8; 20]',
        'ForeignAsset': 'u16',
        'LiquidCrowdloan': 'u32',
        'StableAssetPoolToken': 'u32',
        'Token': (
            'ACA',
            'AUSD',
            'DOT',
            'LDOT',
            'TAP',
            'KAR',
            'KUSD',
            'KSM',
            'LKSM',
            'TAI',
            'BNC',
            'VSKSM',
            'PHA',
            'KINT',
            'KBTC',
        ),
    },
    'decrease_collateral': 'u128',
    'min_decrease_debit_value': 'u128',
}
)
```

---------
### transfer_debit
#### Attributes
| Name | Type |
| -------- | -------- | 
| from_currency | `CurrencyId` | 
| to_currency | `CurrencyId` | 
| debit_transfer | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Honzon', 'transfer_debit', {
    'debit_transfer': 'u128',
    'from_currency': {
        'DexShare': (
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
        ),
        'Erc20': '[u8; 20]',
        'ForeignAsset': 'u16',
        'LiquidCrowdloan': 'u32',
        'StableAssetPoolToken': 'u32',
        'Token': (
            'ACA',
            'AUSD',
            'DOT',
            'LDOT',
            'TAP',
            'KAR',
            'KUSD',
            'KSM',
            'LKSM',
            'TAI',
            'BNC',
            'VSKSM',
            'PHA',
            'KINT',
            'KBTC',
        ),
    },
    'to_currency': {
        'DexShare': (
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
        ),
        'Erc20': '[u8; 20]',
        'ForeignAsset': 'u16',
        'LiquidCrowdloan': 'u32',
        'StableAssetPoolToken': 'u32',
        'Token': (
            'ACA',
            'AUSD',
            'DOT',
            'LDOT',
            'TAP',
            'KAR',
            'KUSD',
            'KSM',
            'LKSM',
            'TAI',
            'BNC',
            'VSKSM',
            'PHA',
            'KINT',
            'KBTC',
        ),
    },
}
)
```

---------
### transfer_loan_from
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| from | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'Honzon', 'transfer_loan_from', {
    'currency_id': {
        'DexShare': (
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
        ),
        'Erc20': '[u8; 20]',
        'ForeignAsset': 'u16',
        'LiquidCrowdloan': 'u32',
        'StableAssetPoolToken': 'u32',
        'Token': (
            'ACA',
            'AUSD',
            'DOT',
            'LDOT',
            'TAP',
            'KAR',
            'KUSD',
            'KSM',
            'LKSM',
            'TAI',
            'BNC',
            'VSKSM',
            'PHA',
            'KINT',
            'KBTC',
        ),
    },
    'from': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### unauthorize
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| to | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'Honzon', 'unauthorize', {
    'currency_id': {
        'DexShare': (
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
        ),
        'Erc20': '[u8; 20]',
        'ForeignAsset': 'u16',
        'LiquidCrowdloan': 'u32',
        'StableAssetPoolToken': 'u32',
        'Token': (
            'ACA',
            'AUSD',
            'DOT',
            'LDOT',
            'TAP',
            'KAR',
            'KUSD',
            'KSM',
            'LKSM',
            'TAI',
            'BNC',
            'VSKSM',
            'PHA',
            'KINT',
            'KBTC',
        ),
    },
    'to': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### unauthorize_all
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Honzon', 'unauthorize_all', {}
)
```

---------
## Events

---------
### Authorization
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| authorizer | `T::AccountId` | ```AccountId```
| authorizee | `T::AccountId` | ```AccountId```
| collateral_type | `CurrencyId` | ```{'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'DexShare': ({'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}, {'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}), 'Erc20': '[u8; 20]', 'StableAssetPoolToken': 'u32', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16'}```

---------
### TransferDebit
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from_currency | `CurrencyId` | ```{'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'DexShare': ({'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}, {'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}), 'Erc20': '[u8; 20]', 'StableAssetPoolToken': 'u32', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16'}```
| to_currency | `CurrencyId` | ```{'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'DexShare': ({'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}, {'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}), 'Erc20': '[u8; 20]', 'StableAssetPoolToken': 'u32', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16'}```
| amount | `Balance` | ```u128```

---------
### UnAuthorization
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| authorizer | `T::AccountId` | ```AccountId```
| authorizee | `T::AccountId` | ```AccountId```
| collateral_type | `CurrencyId` | ```{'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'DexShare': ({'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}, {'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}), 'Erc20': '[u8; 20]', 'StableAssetPoolToken': 'u32', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16'}```

---------
### UnAuthorizationAll
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| authorizer | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### Authorization

#### Python
```python
result = substrate.query(
    'Honzon', 'Authorization', [
    'AccountId',
    (
        {
            'DexShare': (
                {
                    'Erc20': '[u8; 20]',
                    'ForeignAsset': 'u16',
                    'LiquidCrowdloan': 'u32',
                    'StableAssetPoolToken': 'u32',
                    'Token': (
                        'ACA',
                        'AUSD',
                        'DOT',
                        'LDOT',
                        'TAP',
                        'KAR',
                        'KUSD',
                        'KSM',
                        'LKSM',
                        'TAI',
                        'BNC',
                        'VSKSM',
                        'PHA',
                        'KINT',
                        'KBTC',
                    ),
                },
                {
                    'Erc20': '[u8; 20]',
                    'ForeignAsset': 'u16',
                    'LiquidCrowdloan': 'u32',
                    'StableAssetPoolToken': 'u32',
                    'Token': (
                        'ACA',
                        'AUSD',
                        'DOT',
                        'LDOT',
                        'TAP',
                        'KAR',
                        'KUSD',
                        'KSM',
                        'LKSM',
                        'TAI',
                        'BNC',
                        'VSKSM',
                        'PHA',
                        'KINT',
                        'KBTC',
                    ),
                },
            ),
            'Erc20': '[u8; 20]',
            'ForeignAsset': 'u16',
            'LiquidCrowdloan': 'u32',
            'StableAssetPoolToken': 'u32',
            'Token': (
                'ACA',
                'AUSD',
                'DOT',
                'LDOT',
                'TAP',
                'KAR',
                'KUSD',
                'KSM',
                'LKSM',
                'TAI',
                'BNC',
                'VSKSM',
                'PHA',
                'KINT',
                'KBTC',
            ),
        },
        'AccountId',
    ),
]
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### DepositPerAuthorization
#### Value
```python
4038400000000
```
#### Python
```python
constant = substrate.get_constant('Honzon', 'DepositPerAuthorization')
```
---------
## Errors

---------
### AlreadyAuthorized

---------
### AlreadyShutdown

---------
### AuthorizationNotExists

---------
### NoPermission

---------