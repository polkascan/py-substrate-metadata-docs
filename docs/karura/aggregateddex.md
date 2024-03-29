
# AggregatedDex

---------
## Calls

---------
### swap_with_exact_supply
#### Attributes
| Name | Type |
| -------- | -------- | 
| paths | `Vec<SwapPath>` | 
| supply_amount | `Balance` | 
| min_target_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'AggregatedDex', 'swap_with_exact_supply', {
    'min_target_amount': 'u128',
    'paths': [
        {
            'Dex': [
                {
                    'DexShare': (
                        {
                            'Erc20': '[u8; 20]',
                            'ForeignAsset': 'u16',
                            'LiquidCrowdloan': 'u32',
                            'StableAssetPoolToken': 'u32',
                            'Token': 'scale_info::54',
                        },
                        {
                            'Erc20': '[u8; 20]',
                            'ForeignAsset': 'u16',
                            'LiquidCrowdloan': 'u32',
                            'StableAssetPoolToken': 'u32',
                            'Token': 'scale_info::54',
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
            ],
            'Taiga': (
                'u32',
                'u32',
                'u32',
            ),
        },
    ],
    'supply_amount': 'u128',
}
)
```

---------
### swap_with_exact_target
#### Attributes
| Name | Type |
| -------- | -------- | 
| paths | `Vec<SwapPath>` | 
| target_amount | `Balance` | 
| max_supply_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'AggregatedDex', 'swap_with_exact_target', {
    'max_supply_amount': 'u128',
    'paths': [
        {
            'Dex': [
                {
                    'DexShare': (
                        {
                            'Erc20': '[u8; 20]',
                            'ForeignAsset': 'u16',
                            'LiquidCrowdloan': 'u32',
                            'StableAssetPoolToken': 'u32',
                            'Token': 'scale_info::54',
                        },
                        {
                            'Erc20': '[u8; 20]',
                            'ForeignAsset': 'u16',
                            'LiquidCrowdloan': 'u32',
                            'StableAssetPoolToken': 'u32',
                            'Token': 'scale_info::54',
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
            ],
            'Taiga': (
                'u32',
                'u32',
                'u32',
            ),
        },
    ],
    'target_amount': 'u128',
}
)
```

---------
### update_aggregated_swap_paths
#### Attributes
| Name | Type |
| -------- | -------- | 
| updates | `Vec<((CurrencyId, CurrencyId), Option<Vec<SwapPath>>)>` | 

#### Python
```python
call = substrate.compose_call(
    'AggregatedDex', 'update_aggregated_swap_paths', {
    'updates': [
        (
            (
                {
                    'DexShare': (
                        {
                            'Erc20': '[u8; 20]',
                            'ForeignAsset': 'u16',
                            'LiquidCrowdloan': 'u32',
                            'StableAssetPoolToken': 'u32',
                            'Token': 'scale_info::54',
                        },
                        {
                            'Erc20': '[u8; 20]',
                            'ForeignAsset': 'u16',
                            'LiquidCrowdloan': 'u32',
                            'StableAssetPoolToken': 'u32',
                            'Token': 'scale_info::54',
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
                {
                    'DexShare': (
                        {
                            'Erc20': '[u8; 20]',
                            'ForeignAsset': 'u16',
                            'LiquidCrowdloan': 'u32',
                            'StableAssetPoolToken': 'u32',
                            'Token': 'scale_info::54',
                        },
                        {
                            'Erc20': '[u8; 20]',
                            'ForeignAsset': 'u16',
                            'LiquidCrowdloan': 'u32',
                            'StableAssetPoolToken': 'u32',
                            'Token': 'scale_info::54',
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
            ),
            (
                None,
                [
                    {
                        'Dex': [
                            'scale_info::53',
                        ],
                        'Taiga': (
                            'u32',
                            'u32',
                            'u32',
                        ),
                    },
                ],
            ),
        ),
    ],
}
)
```

---------
## Storage functions

---------
### AggregatedSwapPaths

#### Python
```python
result = substrate.query(
    'AggregatedDex', 'AggregatedSwapPaths', [
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
    ),
]
)
```

#### Return value
```python
[
    {
        'Dex': [
            {
                'DexShare': ('scale_info::55', 'scale_info::55'),
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': 'scale_info::54',
            },
        ],
        'Taiga': ('u32', 'u32', 'u32'),
    },
]
```
---------
## Constants

---------
### DexSwapJointList
#### Value
```python
[[{'Token': 'KSM'}], [{'Token': 'LKSM'}], [{'Token': 'KUSD'}]]
```
#### Python
```python
constant = substrate.get_constant('AggregatedDex', 'DexSwapJointList')
```
---------
### SwapPathLimit
#### Value
```python
3
```
#### Python
```python
constant = substrate.get_constant('AggregatedDex', 'SwapPathLimit')
```
---------
## Errors

---------
### CannotSwap

---------
### InvalidPoolId

---------
### InvalidSwapPath

---------
### InvalidTokenIndex

---------