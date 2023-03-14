
# VaultStaking

---------
## Events

---------
### DepositStake
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}}}```
| nominator_id | `T::AccountId` | ```AccountId```
| amount | `T::SignedFixedPoint` | ```i128```

---------
### DistributeReward
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}}}```
| amount | `T::SignedFixedPoint` | ```i128```

---------
### ForceRefund
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}}}```

---------
### IncreaseNonce
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}}}```
| new_nonce | `T::Index` | ```u32```

---------
### WithdrawReward
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| nonce | `T::Index` | ```u32```
| currency_id | `T::CurrencyId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}}}```
| nominator_id | `T::AccountId` | ```AccountId```
| amount | `T::SignedFixedPoint` | ```i128```

---------
### WithdrawStake
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}}}```
| nominator_id | `T::AccountId` | ```AccountId```
| amount | `T::SignedFixedPoint` | ```i128```

---------
## Storage functions

---------
### Nonce
 The nonce of the current staking pool, used in force refunds.
 This is a strictly increasing value.

#### Python
```python
result = substrate.query(
    'VaultStaking', 'Nonce', [
    {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
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
            'wrapped': {
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
        },
    },
]
)
```

#### Return value
```python
'u32'
```
---------
### RewardPerToken
 Used to compute the rewards for a participant&#x27;s stake.

#### Python
```python
result = substrate.query(
    'VaultStaking', 'RewardPerToken', [
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
    (
        'u32',
        {
            'account_id': 'AccountId',
            'currencies': {
                'collateral': {
                    'ForeignAsset': 'u32',
                    'LendToken': 'u32',
                    'LpToken': (
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
                        },
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
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
                'wrapped': {
                    'ForeignAsset': 'u32',
                    'LendToken': 'u32',
                    'LpToken': (
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
                        },
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
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
            },
        },
    ),
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
    'VaultStaking', 'RewardTally', [
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
    (
        'u32',
        {
            'account_id': 'AccountId',
            'currencies': {
                'collateral': {
                    'ForeignAsset': 'u32',
                    'LendToken': 'u32',
                    'LpToken': (
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
                        },
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
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
                'wrapped': {
                    'ForeignAsset': 'u32',
                    'LendToken': 'u32',
                    'LpToken': (
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
                        },
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
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
            },
        },
        'AccountId',
    ),
]
)
```

#### Return value
```python
'i128'
```
---------
### SlashPerToken
 Used to compute the amount to slash from a participant&#x27;s stake.

#### Python
```python
result = substrate.query(
    'VaultStaking', 'SlashPerToken', [
    'u32',
    {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
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
            'wrapped': {
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
        },
    },
]
)
```

#### Return value
```python
'i128'
```
---------
### SlashTally
 Accounts for previous changes in stake size.

#### Python
```python
result = substrate.query(
    'VaultStaking', 'SlashTally', [
    'u32',
    (
        {
            'account_id': 'AccountId',
            'currencies': {
                'collateral': {
                    'ForeignAsset': 'u32',
                    'LendToken': 'u32',
                    'LpToken': (
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
                        },
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
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
                'wrapped': {
                    'ForeignAsset': 'u32',
                    'LendToken': 'u32',
                    'LpToken': (
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
                        },
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
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
            },
        },
        'AccountId',
    ),
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
    'VaultStaking', 'Stake', [
    'u32',
    (
        {
            'account_id': 'AccountId',
            'currencies': {
                'collateral': {
                    'ForeignAsset': 'u32',
                    'LendToken': 'u32',
                    'LpToken': (
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
                        },
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
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
                'wrapped': {
                    'ForeignAsset': 'u32',
                    'LendToken': 'u32',
                    'LpToken': (
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
                        },
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
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
            },
        },
        'AccountId',
    ),
]
)
```

#### Return value
```python
'i128'
```
---------
### TotalCurrentStake
 The total stake - this will increase on deposit and decrease on withdrawal or slashing.

#### Python
```python
result = substrate.query(
    'VaultStaking', 'TotalCurrentStake', [
    'u32',
    {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
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
            'wrapped': {
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
        },
    },
]
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
    'VaultStaking', 'TotalRewards', [
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
    (
        'u32',
        {
            'account_id': 'AccountId',
            'currencies': {
                'collateral': {
                    'ForeignAsset': 'u32',
                    'LendToken': 'u32',
                    'LpToken': (
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
                        },
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
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
                'wrapped': {
                    'ForeignAsset': 'u32',
                    'LendToken': 'u32',
                    'LpToken': (
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
                        },
                        {
                            'ForeignAsset': 'u32',
                            'StableLpToken': 'u32',
                            'Token': 'scale_info::51',
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
            },
        },
    ),
]
)
```

#### Return value
```python
'i128'
```
---------
### TotalStake
 The total stake - this will increase on deposit and decrease on withdrawal.

#### Python
```python
result = substrate.query(
    'VaultStaking', 'TotalStake', [
    'u32',
    {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
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
            'wrapped': {
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
        },
    },
]
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
constant = substrate.get_constant('VaultStaking', 'GetNativeCurrencyId')
```
---------
## Errors

---------
### InsufficientFunds
Balance not sufficient to withdraw stake.

---------
### SlashZeroTotalStake
Cannot slash zero total stake.

---------
### TryIntoIntError
Unable to convert value.

---------