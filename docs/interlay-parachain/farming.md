
# Farming

---------
## Calls

---------
### claim
Withdraw any accrued rewards from the reward pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_currency_id | `CurrencyIdOf<T>` | 
| reward_currency_id | `CurrencyIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'claim', {
    'pool_currency_id': {
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
    'reward_currency_id': {
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
}
)
```

---------
### deposit
Stake all pool tokens in the reward pool

- `pool_currency_id`: LP token to deposit
- `length_rewards`: upper bound for number of reward currencies
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_currency_id | `CurrencyIdOf<T>` | 
| length_rewards | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'deposit', {
    'length_rewards': 'u32',
    'pool_currency_id': {
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
}
)
```

---------
### remove_reward_schedule
Explicitly remove a reward schedule and transfer any remaining
balance to the treasury
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_currency_id | `CurrencyIdOf<T>` | 
| reward_currency_id | `CurrencyIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'remove_reward_schedule', {
    'pool_currency_id': {
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
    'reward_currency_id': {
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
}
)
```

---------
### update_reward_schedule
Create or overwrite the reward schedule, if a reward schedule
already exists for the rewards currency the duration is added
to the existing duration and the rewards per period are modified
s.t. that the total (old remaining + new) rewards are distributed
over the new total duration
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_currency_id | `CurrencyIdOf<T>` | 
| reward_currency_id | `CurrencyIdOf<T>` | 
| period_count | `u32` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'update_reward_schedule', {
    'amount': 'u128',
    'period_count': 'u32',
    'pool_currency_id': {
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
    'reward_currency_id': {
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
}
)
```

---------
### withdraw
Unstake the pool tokens from the reward pool

- `pool_currency_id`: LP token to withdraw
- `amount`: of LP token to withdraw
- `length_rewards`: upper bound for number of reward currencies
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_currency_id | `CurrencyIdOf<T>` | 
| amount | `BalanceOf<T>` | 
| length_rewards | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'withdraw', {
    'amount': 'u128',
    'length_rewards': 'u32',
    'pool_currency_id': {
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
}
)
```

---------
## Events

---------
### RewardClaimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `AccountIdOf<T>` | ```AccountId```
| pool_currency_id | `CurrencyIdOf<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| reward_currency_id | `CurrencyIdOf<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| amount | `BalanceOf<T>` | ```u128```

---------
### RewardDistributed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_currency_id | `CurrencyIdOf<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| reward_currency_id | `CurrencyIdOf<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| amount | `BalanceOf<T>` | ```u128```

---------
### RewardScheduleUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_currency_id | `CurrencyIdOf<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| reward_currency_id | `CurrencyIdOf<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| period_count | `u32` | ```u32```
| per_period | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### RewardSchedules

#### Python
```python
result = substrate.query(
    'Farming', 'RewardSchedules', [
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
]
)
```

#### Return value
```python
{'per_period': 'u128', 'period_count': 'u32'}
```
---------
## Constants

---------
### FarmingPalletId
 The farming pallet id, used for deriving pool accounts.
#### Value
```python
'0x6d6f642f6661726d'
```
#### Python
```python
constant = substrate.get_constant('Farming', 'FarmingPalletId')
```
---------
### RewardPeriod
 The period to accrue rewards.
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Farming', 'RewardPeriod')
```
---------
### TreasuryAccountId
 The treasury account id for funding pools.
#### Value
```python
'wd9yNSwR5jsJWJoLHrMKt4K2T7R5392YmZoRdpqijnpLGzEcT'
```
#### Python
```python
constant = substrate.get_constant('Farming', 'TreasuryAccountId')
```
---------
## Errors

---------
### BadRewardLength

---------
### InsufficientStake

---------