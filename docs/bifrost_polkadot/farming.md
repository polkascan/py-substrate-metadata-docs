
# Farming

---------
## Calls

---------
### add_boost_pool_whitelist
#### Attributes
| Name | Type |
| -------- | -------- | 
| whitelist | `Vec<PoolId>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'add_boost_pool_whitelist', {'whitelist': ['u32']}
)
```

---------
### charge
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `PoolId` | 
| rewards | `Vec<(CurrencyIdOf<T>, BalanceOf<T>)>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'charge', {
    'pid': 'u32',
    'rewards': [
        (
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
            'u128',
        ),
    ],
}
)
```

---------
### charge_boost
#### Attributes
| Name | Type |
| -------- | -------- | 
| rewards | `Vec<(CurrencyIdOf<T>, BalanceOf<T>)>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'charge_boost', {
    'rewards': [
        (
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
            'u128',
        ),
    ],
}
)
```

---------
### claim
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'claim', {'pid': 'u32'}
)
```

---------
### close_pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'close_pool', {'pid': 'u32'}
)
```

---------
### create_farming_pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| tokens_proportion | `Vec<(CurrencyIdOf<T>, Perbill)>` | 
| basic_rewards | `Vec<(CurrencyIdOf<T>, BalanceOf<T>)>` | 
| gauge_init | `Option<
(CurrencyIdOf<T>, BlockNumberFor<T>, Vec<
(CurrencyIdOf<T>, BalanceOf<T>)>,)>` | 
| min_deposit_to_start | `BalanceOf<T>` | 
| after_block_to_start | `BlockNumberFor<T>` | 
| withdraw_limit_time | `BlockNumberFor<T>` | 
| claim_limit_time | `BlockNumberFor<T>` | 
| withdraw_limit_count | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'create_farming_pool', {
    'after_block_to_start': 'u32',
    'basic_rewards': [
        (
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
            'u128',
        ),
    ],
    'claim_limit_time': 'u32',
    'gauge_init': (
        None,
        (
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
            'u32',
            [
                (
                    {
                        'ForeignAsset': 'u32',
                        'LPToken': (
                            'scale_info::127',
                            'u8',
                            'scale_info::127',
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
                            'scale_info::127',
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
                    'u128',
                ),
            ],
        ),
    ),
    'min_deposit_to_start': 'u128',
    'tokens_proportion': [
        (
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
            'u32',
        ),
    ],
    'withdraw_limit_count': 'u8',
    'withdraw_limit_time': 'u32',
}
)
```

---------
### deposit
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `PoolId` | 
| add_value | `BalanceOf<T>` | 
| gauge_info | `Option<(BalanceOf<T>, BlockNumberFor<T>)>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'deposit', {
    'add_value': 'u128',
    'gauge_info': (
        None,
        ('u128', 'u32'),
    ),
    'pid': 'u32',
}
)
```

---------
### edit_pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `PoolId` | 
| basic_rewards | `Option<Vec<(CurrencyIdOf<T>, BalanceOf<T>)>>` | 
| withdraw_limit_time | `Option<BlockNumberFor<T>>` | 
| claim_limit_time | `Option<BlockNumberFor<T>>` | 
| gauge_basic_rewards | `Option<Vec<(CurrencyIdOf<T>, BalanceOf<T>)>>` | 
| withdraw_limit_count | `Option<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'edit_pool', {
    'basic_rewards': (
        None,
        [
            (
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
                'u128',
            ),
        ],
    ),
    'claim_limit_time': (None, 'u32'),
    'gauge_basic_rewards': (
        None,
        [
            (
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
                'u128',
            ),
        ],
    ),
    'pid': 'u32',
    'withdraw_limit_count': (
        None,
        'u8',
    ),
    'withdraw_limit_time': (
        None,
        'u32',
    ),
}
)
```

---------
### end_boost_round
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Farming', 'end_boost_round', {}
)
```

---------
### force_gauge_claim
#### Attributes
| Name | Type |
| -------- | -------- | 
| gid | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'force_gauge_claim', {'gid': 'u32'}
)
```

---------
### force_retire_pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'force_retire_pool', {'pid': 'u32'}
)
```

---------
### gauge_withdraw
#### Attributes
| Name | Type |
| -------- | -------- | 
| gid | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'gauge_withdraw', {'gid': 'u32'}
)
```

---------
### kill_pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'kill_pool', {'pid': 'u32'}
)
```

---------
### reset_pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `PoolId` | 
| basic_rewards | `Option<Vec<(CurrencyIdOf<T>, BalanceOf<T>)>>` | 
| min_deposit_to_start | `Option<BalanceOf<T>>` | 
| after_block_to_start | `Option<BlockNumberFor<T>>` | 
| withdraw_limit_time | `Option<BlockNumberFor<T>>` | 
| claim_limit_time | `Option<BlockNumberFor<T>>` | 
| withdraw_limit_count | `Option<u8>` | 
| gauge_init | `Option<
(CurrencyIdOf<T>, BlockNumberFor<T>, Vec<
(CurrencyIdOf<T>, BalanceOf<T>)>,)>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'reset_pool', {
    'after_block_to_start': (
        None,
        'u32',
    ),
    'basic_rewards': (
        None,
        [
            (
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
                'u128',
            ),
        ],
    ),
    'claim_limit_time': (None, 'u32'),
    'gauge_init': (
        None,
        (
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
            'u32',
            [
                (
                    {
                        'ForeignAsset': 'u32',
                        'LPToken': (
                            'scale_info::127',
                            'u8',
                            'scale_info::127',
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
                            'scale_info::127',
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
                    'u128',
                ),
            ],
        ),
    ),
    'min_deposit_to_start': (
        None,
        'u128',
    ),
    'pid': 'u32',
    'withdraw_limit_count': (
        None,
        'u8',
    ),
    'withdraw_limit_time': (
        None,
        'u32',
    ),
}
)
```

---------
### set_next_round_whitelist
#### Attributes
| Name | Type |
| -------- | -------- | 
| whitelist | `Vec<PoolId>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'set_next_round_whitelist', {'whitelist': ['u32']}
)
```

---------
### set_retire_limit
#### Attributes
| Name | Type |
| -------- | -------- | 
| limit | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'set_retire_limit', {'limit': 'u32'}
)
```

---------
### start_boost_round
#### Attributes
| Name | Type |
| -------- | -------- | 
| round_length | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'start_boost_round', {'round_length': 'u32'}
)
```

---------
### vote
#### Attributes
| Name | Type |
| -------- | -------- | 
| vote_list | `Vec<(PoolId, Percent)>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'vote', {'vote_list': [('u32', 'u8')]}
)
```

---------
### withdraw
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `PoolId` | 
| remove_value | `Option<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'withdraw', {
    'pid': 'u32',
    'remove_value': (None, 'u128'),
}
)
```

---------
### withdraw_claim
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'withdraw_claim', {'pid': 'u32'}
)
```

---------
## Events

---------
### AllForceGaugeClaimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| gid | `PoolId` | ```u32```

---------
### AllRetired
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `PoolId` | ```u32```

---------
### BoostCharged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```
| rewards | `Vec<(CurrencyIdOf<T>, BalanceOf<T>)>` | ```[({'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}, 'u128')]```

---------
### Charged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```
| pid | `PoolId` | ```u32```
| rewards | `Vec<(CurrencyIdOf<T>, BalanceOf<T>)>` | ```[({'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}, 'u128')]```

---------
### Claimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```
| pid | `PoolId` | ```u32```

---------
### Deposited
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```
| pid | `PoolId` | ```u32```
| add_value | `BalanceOf<T>` | ```u128```
| gauge_info | `Option<(BalanceOf<T>, BlockNumberFor<T>)>` | ```(None, ('u128', 'u32'))```

---------
### FarmingPoolClosed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `PoolId` | ```u32```

---------
### FarmingPoolCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `PoolId` | ```u32```

---------
### FarmingPoolEdited
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `PoolId` | ```u32```

---------
### FarmingPoolKilled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `PoolId` | ```u32```

---------
### FarmingPoolReset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `PoolId` | ```u32```

---------
### GaugeWithdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```
| gid | `PoolId` | ```u32```

---------
### PartiallyForceGaugeClaimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| gid | `PoolId` | ```u32```

---------
### PartiallyRetired
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `PoolId` | ```u32```

---------
### RetireLimitSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| limit | `u32` | ```u32```

---------
### RoundEnd
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| total_votes | `BalanceOf<T>` | ```u128```
| start_round | `BlockNumberFor<T>` | ```u32```
| end_round | `BlockNumberFor<T>` | ```u32```

---------
### RoundStart
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| round_length | `BlockNumberFor<T>` | ```u32```

---------
### RoundStartError
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| info | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
### Voted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```
| vote_list | `Vec<(PoolId, Percent)>` | ```[('u32', 'u8')]```

---------
### WithdrawClaimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```
| pid | `PoolId` | ```u32```

---------
### Withdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```
| pid | `PoolId` | ```u32```
| remove_value | `Option<BalanceOf<T>>` | ```(None, 'u128')```

---------
## Storage functions

---------
### BoostBasicRewards

#### Python
```python
result = substrate.query(
    'Farming', 'BoostBasicRewards', [
    'u32',
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
]
)
```

#### Return value
```python
'u128'
```
---------
### BoostNextRoundWhitelist

#### Python
```python
result = substrate.query(
    'Farming', 'BoostNextRoundWhitelist', ['u32']
)
```

#### Return value
```python
()
```
---------
### BoostPoolInfos

#### Python
```python
result = substrate.query(
    'Farming', 'BoostPoolInfos', []
)
```

#### Return value
```python
{
    'end_round': 'u32',
    'round_length': 'u32',
    'start_round': 'u32',
    'total_votes': 'u128',
}
```
---------
### BoostVotingPools

#### Python
```python
result = substrate.query(
    'Farming', 'BoostVotingPools', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### BoostWhitelist

#### Python
```python
result = substrate.query(
    'Farming', 'BoostWhitelist', ['u32']
)
```

#### Return value
```python
()
```
---------
### GaugeInfos

#### Python
```python
result = substrate.query(
    'Farming', 'GaugeInfos', ['u32', 'AccountId']
)
```

#### Return value
```python
{
    'claimed_time_factor': 'u128',
    'gauge_amount': 'u128',
    'gauge_last_block': 'u32',
    'gauge_start_block': 'u32',
    'gauge_stop_block': 'u32',
    'last_claim_block': 'u32',
    'latest_time_factor': 'u128',
    'total_time_factor': 'u128',
    'who': 'AccountId',
}
```
---------
### GaugePoolInfos
 Record gauge farming pool info.

 map PoolId =&gt; GaugePoolInfo

#### Python
```python
result = substrate.query(
    'Farming', 'GaugePoolInfos', ['u32']
)
```

#### Return value
```python
{
    'gauge_amount': 'u128',
    'gauge_basic_rewards': 'scale_info::629',
    'gauge_last_block': 'u32',
    'gauge_state': ('Unbond', 'Bonded'),
    'keeper': 'AccountId',
    'max_block': 'u32',
    'pid': 'u32',
    'reward_issuer': 'AccountId',
    'rewards': 'scale_info::635',
    'token': {
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
    'total_time_factor': 'u128',
}
```
---------
### GaugePoolNextId

#### Python
```python
result = substrate.query(
    'Farming', 'GaugePoolNextId', []
)
```

#### Return value
```python
'u32'
```
---------
### PoolInfos
 Record reward pool info.

 map PoolId =&gt; PoolInfo

#### Python
```python
result = substrate.query(
    'Farming', 'PoolInfos', ['u32']
)
```

#### Return value
```python
{
    'after_block_to_start': 'u32',
    'basic_rewards': 'scale_info::629',
    'basic_token': (
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
        'u32',
    ),
    'block_startup': (None, 'u32'),
    'claim_limit_time': 'u32',
    'gauge': (None, 'u32'),
    'keeper': 'AccountId',
    'min_deposit_to_start': 'u128',
    'reward_issuer': 'AccountId',
    'rewards': 'scale_info::630',
    'state': ('UnCharged', 'Charged', 'Ongoing', 'Dead', 'Retired'),
    'tokens_proportion': 'scale_info::628',
    'total_shares': 'u128',
    'withdraw_limit_count': 'u8',
    'withdraw_limit_time': 'u32',
}
```
---------
### PoolNextId

#### Python
```python
result = substrate.query(
    'Farming', 'PoolNextId', []
)
```

#### Return value
```python
'u32'
```
---------
### RetireLimit

#### Python
```python
result = substrate.query(
    'Farming', 'RetireLimit', []
)
```

#### Return value
```python
'u32'
```
---------
### SharesAndWithdrawnRewards
 Record share amount, reward currency and withdrawn reward amount for
 specific `AccountId` under `PoolId`.

 double_map (PoolId, AccountId) =&gt; ShareInfo

#### Python
```python
result = substrate.query(
    'Farming', 'SharesAndWithdrawnRewards', ['u32', 'AccountId']
)
```

#### Return value
```python
{
    'claim_last_block': 'u32',
    'share': 'u128',
    'who': 'AccountId',
    'withdraw_list': [('u32', 'u128')],
    'withdrawn_rewards': 'scale_info::629',
}
```
---------
### UserBoostInfos

#### Python
```python
result = substrate.query(
    'Farming', 'UserBoostInfos', ['AccountId']
)
```

#### Return value
```python
{'last_vote': 'u32', 'vote_amount': 'u128', 'vote_list': [('u32', 'u8')]}
```
---------
## Constants

---------
### FarmingBoost
#### Value
```python
'0x62662f666d627374'
```
#### Python
```python
constant = substrate.get_constant('Farming', 'FarmingBoost')
```
---------
### Keeper
 ModuleID for creating sub account
#### Value
```python
'0x62662f666d6b7072'
```
#### Python
```python
constant = substrate.get_constant('Farming', 'Keeper')
```
---------
### RewardIssuer
#### Value
```python
'0x62662f666d726972'
```
#### Python
```python
constant = substrate.get_constant('Farming', 'RewardIssuer')
```
---------
### TreasuryAccount
#### Value
```python
'eCSrvbA5gGNYdM3UjBNxcBNBqGxtz3SEEfydKragtL4pJ4F'
```
#### Python
```python
constant = substrate.get_constant('Farming', 'TreasuryAccount')
```
---------
### WhitelistMaximumLimit
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Farming', 'WhitelistMaximumLimit')
```
---------
## Errors

---------
### CanNotClaim
claim_limit_time exceeded

---------
### CanNotDeposit

---------
### GaugeInfoNotExist

---------
### GaugeMaxBlockOverflow
gauge pool max_block exceeded

---------
### GaugePoolNotExist

---------
### InvalidPoolState

---------
### LastGaugeNotClaim

---------
### NobodyVoting

---------
### NotInWhitelist

---------
### NotNullable

---------
### PercentOverflow

---------
### PoolDoesNotExist

---------
### RoundLengthNotSet

---------
### RoundNotOver

---------
### ShareInfoNotExists

---------
### WhitelistEmpty

---------
### WhitelistLimitExceeded

---------
### WithdrawLimitCountExceeded
withdraw_limit_time exceeded

---------