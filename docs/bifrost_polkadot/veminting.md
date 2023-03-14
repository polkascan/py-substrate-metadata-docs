
# VeMinting

---------
## Calls

---------
### create_lock
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `BalanceOf<T>` | 
| unlock_time | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'VeMinting', 'create_lock', {
    'unlock_time': 'u32',
    'value': 'u128',
}
)
```

---------
### get_rewards
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'VeMinting', 'get_rewards', {}
)
```

---------
### increase_amount
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VeMinting', 'increase_amount', {'value': 'u128'}
)
```

---------
### increase_unlock_time
#### Attributes
| Name | Type |
| -------- | -------- | 
| time | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'VeMinting', 'increase_unlock_time', {'time': 'u32'}
)
```

---------
### notify_rewards
#### Attributes
| Name | Type |
| -------- | -------- | 
| incentive_from | `AccountIdOf<T>` | 
| rewards_duration | `Option<T::BlockNumber>` | 
| rewards | `Vec<(CurrencyIdOf<T>, BalanceOf<T>)>` | 

#### Python
```python
call = substrate.compose_call(
    'VeMinting', 'notify_rewards', {
    'incentive_from': 'AccountId',
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
    'rewards_duration': (None, 'u32'),
}
)
```

---------
### set_config
#### Attributes
| Name | Type |
| -------- | -------- | 
| min_mint | `Option<BalanceOf<T>>` | 
| min_block | `Option<T::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'VeMinting', 'set_config', {
    'min_block': (None, 'u32'),
    'min_mint': (None, 'u128'),
}
)
```

---------
### withdraw
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'VeMinting', 'withdraw', {}
)
```

---------
## Events

---------
### AmountIncreased
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| addr | `AccountIdOf<T>` | ```AccountId```
| value | `BalanceOf<T>` | ```u128```

---------
### ConfigSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| config | `VeConfig<BalanceOf<T>, T::BlockNumber>` | ```{'amount': 'u128', 'min_mint': 'u128', 'min_block': 'u32'}```

---------
### IncentiveSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| rewards_duration | `T::BlockNumber` | ```u32```

---------
### LockCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| addr | `AccountIdOf<T>` | ```AccountId```
| value | `BalanceOf<T>` | ```u128```
| unlock_time | `T::BlockNumber` | ```u32```

---------
### Minted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| addr | `AccountIdOf<T>` | ```AccountId```
| value | `BalanceOf<T>` | ```u128```
| end | `T::BlockNumber` | ```u32```
| now | `T::BlockNumber` | ```u32```

---------
### RewardAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| rewards | `Vec<(CurrencyIdOf<T>, BalanceOf<T>)>` | ```[({'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}, 'u128')]```

---------
### Rewarded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| addr | `AccountIdOf<T>` | ```AccountId```
| rewards | `Vec<(CurrencyIdOf<T>, BalanceOf<T>)>` | ```[({'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}, 'u128')]```

---------
### Supply
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| supply_before | `BalanceOf<T>` | ```u128```
| supply | `BalanceOf<T>` | ```u128```

---------
### UnlockTimeIncreased
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| addr | `AccountIdOf<T>` | ```AccountId```
| unlock_time | `T::BlockNumber` | ```u32```

---------
### Withdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| addr | `AccountIdOf<T>` | ```AccountId```
| value | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### Epoch

#### Python
```python
result = substrate.query(
    'VeMinting', 'Epoch', []
)
```

#### Return value
```python
'[u64; 4]'
```
---------
### IncentiveConfigs

#### Python
```python
result = substrate.query(
    'VeMinting', 'IncentiveConfigs', []
)
```

#### Return value
```python
{
    'last_update_time': 'u32',
    'period_finish': 'u32',
    'reward_per_token_stored': 'scale_info::608',
    'reward_rate': 'scale_info::608',
    'rewards_duration': 'u32',
}
```
---------
### Locked

#### Python
```python
result = substrate.query(
    'VeMinting', 'Locked', ['AccountId']
)
```

#### Return value
```python
{'amount': 'u128', 'end': 'u32'}
```
---------
### PointHistory

#### Python
```python
result = substrate.query(
    'VeMinting', 'PointHistory', ['[u64; 4]']
)
```

#### Return value
```python
{'amount': 'u128', 'bias': 'i128', 'block': 'u32', 'slope': 'i128'}
```
---------
### Rewards

#### Python
```python
result = substrate.query(
    'VeMinting', 'Rewards', ['AccountId']
)
```

#### Return value
```python
'scale_info::608'
```
---------
### SlopeChanges

#### Python
```python
result = substrate.query(
    'VeMinting', 'SlopeChanges', ['u32']
)
```

#### Return value
```python
'i128'
```
---------
### Supply

#### Python
```python
result = substrate.query(
    'VeMinting', 'Supply', []
)
```

#### Return value
```python
'u128'
```
---------
### UserPointEpoch

#### Python
```python
result = substrate.query(
    'VeMinting', 'UserPointEpoch', ['AccountId']
)
```

#### Return value
```python
'[u64; 4]'
```
---------
### UserPointHistory

#### Python
```python
result = substrate.query(
    'VeMinting', 'UserPointHistory', ['AccountId', '[u64; 4]']
)
```

#### Return value
```python
{'amount': 'u128', 'bias': 'i128', 'block': 'u32', 'slope': 'i128'}
```
---------
### UserRewardPerTokenPaid

#### Python
```python
result = substrate.query(
    'VeMinting', 'UserRewardPerTokenPaid', ['AccountId']
)
```

#### Return value
```python
'scale_info::608'
```
---------
### VeConfigs

#### Python
```python
result = substrate.query(
    'VeMinting', 'VeConfigs', []
)
```

#### Return value
```python
{'amount': 'u128', 'min_block': 'u32', 'min_mint': 'u128'}
```
---------
## Constants

---------
### IncentivePalletId
#### Value
```python
'0x62662f7665696374'
```
#### Python
```python
constant = substrate.get_constant('VeMinting', 'IncentivePalletId')
```
---------
### MaxBlock
#### Value
```python
10512000
```
#### Python
```python
constant = substrate.get_constant('VeMinting', 'MaxBlock')
```
---------
### Multiplier
#### Value
```python
1000000000000
```
#### Python
```python
constant = substrate.get_constant('VeMinting', 'Multiplier')
```
---------
### TokenType
#### Value
```python
{'VToken': 'BNC'}
```
#### Python
```python
constant = substrate.get_constant('VeMinting', 'TokenType')
```
---------
### VeMintingPalletId
#### Value
```python
'0x62662f76656d6e74'
```
#### Python
```python
constant = substrate.get_constant('VeMinting', 'VeMintingPalletId')
```
---------
### VoteWeightMultiplier
#### Value
```python
3
```
#### Python
```python
constant = substrate.get_constant('VeMinting', 'VoteWeightMultiplier')
```
---------
### Week
#### Value
```python
50400
```
#### Python
```python
constant = substrate.get_constant('VeMinting', 'Week')
```
---------
## Errors

---------
### BelowMinimumMint

---------
### Expired

---------
### LockExist

---------
### LockNotExist

---------
### NoRewards

---------
### NotEnoughBalance

---------