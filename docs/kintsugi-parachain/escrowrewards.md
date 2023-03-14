
# EscrowRewards

---------
## Events

---------
### DepositStake
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```()```
| stake_id | `T::StakeId` | ```AccountId```
| amount | `T::SignedFixedPoint` | ```i128```

---------
### DistributeReward
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| amount | `T::SignedFixedPoint` | ```i128```

---------
### WithdrawReward
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```()```
| stake_id | `T::StakeId` | ```AccountId```
| currency_id | `T::CurrencyId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| amount | `T::SignedFixedPoint` | ```i128```

---------
### WithdrawStake
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```()```
| stake_id | `T::StakeId` | ```AccountId```
| amount | `T::SignedFixedPoint` | ```i128```

---------
## Storage functions

---------
### RewardCurrencies
 Track the currencies used for rewards.

#### Python
```python
result = substrate.query(
    'EscrowRewards', 'RewardCurrencies', [()]
)
```

#### Return value
```python
'scale_info::387'
```
---------
### RewardPerToken
 Used to compute the rewards for a participant&#x27;s stake.

#### Python
```python
result = substrate.query(
    'EscrowRewards', 'RewardPerToken', [
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
    (),
]
)
```

#### Return value
```python
'i128'
```
---------
### RewardTally
 Accounts for previous changes in stake size.

#### Python
```python
result = substrate.query(
    'EscrowRewards', 'RewardTally', [
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
    ((), 'AccountId'),
]
)
```

#### Return value
```python
'i128'
```
---------
### Stake
 The stake of a participant in this reward pool.

#### Python
```python
result = substrate.query(
    'EscrowRewards', 'Stake', [((), 'AccountId')]
)
```

#### Return value
```python
'i128'
```
---------
### TotalRewards
 The total unclaimed rewards distributed to this reward pool.
 NOTE: this is currently only used for integration tests.

#### Python
```python
result = substrate.query(
    'EscrowRewards', 'TotalRewards', [
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
'i128'
```
---------
### TotalStake
 The total stake deposited to this reward pool.

#### Python
```python
result = substrate.query(
    'EscrowRewards', 'TotalStake', [()]
)
```

#### Return value
```python
'i128'
```
---------
## Constants

---------
### GetNativeCurrencyId
#### Value
```python
{'Token': 'KINT'}
```
#### Python
```python
constant = substrate.get_constant('EscrowRewards', 'GetNativeCurrencyId')
```
---------
### GetWrappedCurrencyId
#### Value
```python
{'Token': 'KBTC'}
```
#### Python
```python
constant = substrate.get_constant('EscrowRewards', 'GetWrappedCurrencyId')
```
---------
## Errors

---------
### InsufficientFunds
Balance not sufficient to withdraw stake.

---------
### TryIntoIntError
Unable to convert value.

---------
### ZeroTotalStake
Cannot distribute rewards without stake.

---------