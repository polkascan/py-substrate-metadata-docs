
# Rewards

---------
## Storage functions

---------
### PoolInfos

#### Python
```python
result = substrate.query(
    'Rewards', 'PoolInfos', [
    {
        'Dex': {
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
        'Loans': {
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
    },
]
)
```

#### Return value
```python
{'rewards': 'scale_info::523', 'total_shares': 'u128'}
```
---------
### SharesAndWithdrawnRewards

#### Python
```python
result = substrate.query(
    'Rewards', 'SharesAndWithdrawnRewards', [
    {
        'Dex': {
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
        'Loans': {
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
    },
    'AccountId',
]
)
```

#### Return value
```python
('u128', 'scale_info::529')
```
---------
## Errors

---------
### CanSplitOnlyLessThanShare

---------
### PoolDoesNotExist

---------
### ShareDoesNotExist

---------