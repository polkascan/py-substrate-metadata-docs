
# HonzonBridge

---------
## Calls

---------
### from_bridged
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'HonzonBridge', 'from_bridged', {'amount': 'u128'}
)
```

---------
### set_bridged_stable_coin_address
#### Attributes
| Name | Type |
| -------- | -------- | 
| address | `EvmAddress` | 

#### Python
```python
call = substrate.compose_call(
    'HonzonBridge', 'set_bridged_stable_coin_address', {'address': '[u8; 20]'}
)
```

---------
### to_bridged
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'HonzonBridge', 'to_bridged', {'amount': 'u128'}
)
```

---------
## Events

---------
### BridgedStableCoinCurrencyIdSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| bridged_stable_coin_currency_id | `CurrencyId` | ```{'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'RENBTC', 'CASH', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'DexShare': ({'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'RENBTC', 'CASH', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}, {'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'RENBTC', 'CASH', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}), 'Erc20': '[u8; 20]', 'StableAssetPoolToken': 'u32', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16'}```

---------
### FromBridged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `Balance` | ```u128```

---------
### ToBridged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `Balance` | ```u128```

---------
## Storage functions

---------
### BridgedStableCoinCurrencyId

#### Python
```python
result = substrate.query(
    'HonzonBridge', 'BridgedStableCoinCurrencyId', []
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
                'RENBTC',
                'CASH',
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
                'RENBTC',
                'CASH',
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
        'RENBTC',
        'CASH',
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
### HonzonBridgeAccount
#### Value
```python
'qmmNufxeWaAUy6KGcxwC3u3EagHc9G9mbhHuxEaefbfXg3V'
```
#### Python
```python
constant = substrate.get_constant('HonzonBridge', 'HonzonBridgeAccount')
```
---------
### StableCoinCurrencyId
#### Value
```python
{'Token': 'KUSD'}
```
#### Python
```python
constant = substrate.get_constant('HonzonBridge', 'StableCoinCurrencyId')
```
---------
## Errors

---------
### BridgedStableCoinCurrencyIdNotSet

---------