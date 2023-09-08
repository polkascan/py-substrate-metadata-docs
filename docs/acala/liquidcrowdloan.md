
# LiquidCrowdloan

---------
## Calls

---------
### redeem
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidCrowdloan', 'redeem', {'amount': 'u128'}
)
```

---------
### set_redeem_currency_id
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidCrowdloan', 'set_redeem_currency_id', {
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
}
)
```

---------
### transfer_from_crowdloan_vault
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidCrowdloan', 'transfer_from_crowdloan_vault', {'amount': 'u128'}
)
```

---------
## Events

---------
### RedeemCurrencyIdUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `CurrencyId` | ```{'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'DexShare': ({'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}, {'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}), 'Erc20': '[u8; 20]', 'StableAssetPoolToken': 'u32', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16'}```

---------
### Redeemed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `CurrencyId` | ```{'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'DexShare': ({'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}, {'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}), 'Erc20': '[u8; 20]', 'StableAssetPoolToken': 'u32', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16'}```
| amount | `Balance` | ```u128```

---------
### TransferFromCrowdloanVaultRequested
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| amount | `Balance` | ```u128```

---------
## Storage functions

---------
### RedeemCurrencyId

#### Python
```python
result = substrate.query(
    'LiquidCrowdloan', 'RedeemCurrencyId', []
)
```

#### Return value
```python
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
}
```
---------
## Constants

---------
### CrowdloanVault
#### Value
```python
'22ubTemy7e7r37Hib4GRzsgrg6G5xR6GtsQeJFsV5pWUY1Rk'
```
#### Python
```python
constant = substrate.get_constant('LiquidCrowdloan', 'CrowdloanVault')
```
---------
### LiquidCrowdloanCurrencyId
#### Value
```python
{'LiquidCrowdloan': 13}
```
#### Python
```python
constant = substrate.get_constant('LiquidCrowdloan', 'LiquidCrowdloanCurrencyId')
```
---------
### PalletId
#### Value
```python
'0x6163612f6c71636c'
```
#### Python
```python
constant = substrate.get_constant('LiquidCrowdloan', 'PalletId')
```
---------
### RelayChainCurrencyId
#### Value
```python
{'Token': 'DOT'}
```
#### Python
```python
constant = substrate.get_constant('LiquidCrowdloan', 'RelayChainCurrencyId')
```
---------