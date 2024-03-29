
# PooledVaultRewards

---------
## Events

---------
### DepositStake
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}```
| stake_id | `T::StakeId` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| amount | `T::SignedFixedPoint` | ```i128```

---------
### DistributeReward
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::PoolRewardsCurrencyId` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}```
| amount | `T::SignedFixedPoint` | ```i128```

---------
### WithdrawReward
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}```
| stake_id | `T::StakeId` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| currency_id | `T::PoolRewardsCurrencyId` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}```
| amount | `T::SignedFixedPoint` | ```i128```

---------
### WithdrawStake
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}```
| stake_id | `T::StakeId` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| amount | `T::SignedFixedPoint` | ```i128```

---------
## Storage functions

---------
### RewardCurrencies
 Track the currencies used for rewards.

#### Python
```python
result = substrate.query(
    'PooledVaultRewards', 'RewardCurrencies', [
    {
        'Native': None,
        'Stellar': {
            'AlphaNum12': {
                'code': '[u8; 12]',
                'issuer': '[u8; 32]',
            },
            'AlphaNum4': {
                'code': '[u8; 4]',
                'issuer': '[u8; 32]',
            },
            'StellarNative': None,
        },
        'Token': 'u64',
        'XCM': 'u8',
        'ZenlinkLPToken': (
            'u8',
            'u8',
            'u8',
            'u8',
        ),
    },
]
)
```

#### Return value
```python
'scale_info::588'
```
---------
### RewardPerToken
 Used to compute the rewards for a participant&#x27;s stake.

#### Python
```python
result = substrate.query(
    'PooledVaultRewards', 'RewardPerToken', [
    {
        'Native': None,
        'Stellar': {
            'AlphaNum12': {
                'code': '[u8; 12]',
                'issuer': '[u8; 32]',
            },
            'AlphaNum4': {
                'code': '[u8; 4]',
                'issuer': '[u8; 32]',
            },
            'StellarNative': None,
        },
        'Token': 'u64',
        'XCM': 'u8',
        'ZenlinkLPToken': (
            'u8',
            'u8',
            'u8',
            'u8',
        ),
    },
    {
        'Native': None,
        'Stellar': {
            'AlphaNum12': {
                'code': '[u8; 12]',
                'issuer': '[u8; 32]',
            },
            'AlphaNum4': {
                'code': '[u8; 4]',
                'issuer': '[u8; 32]',
            },
            'StellarNative': None,
        },
        'Token': 'u64',
        'XCM': 'u8',
        'ZenlinkLPToken': (
            'u8',
            'u8',
            'u8',
            'u8',
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
### RewardTally
 Accounts for previous changes in stake size.

#### Python
```python
result = substrate.query(
    'PooledVaultRewards', 'RewardTally', [
    {
        'Native': None,
        'Stellar': {
            'AlphaNum12': {
                'code': '[u8; 12]',
                'issuer': '[u8; 32]',
            },
            'AlphaNum4': {
                'code': '[u8; 4]',
                'issuer': '[u8; 32]',
            },
            'StellarNative': None,
        },
        'Token': 'u64',
        'XCM': 'u8',
        'ZenlinkLPToken': (
            'u8',
            'u8',
            'u8',
            'u8',
        ),
    },
    (
        {
            'Native': None,
            'Stellar': {
                'AlphaNum12': {
                    'code': '[u8; 12]',
                    'issuer': '[u8; 32]',
                },
                'AlphaNum4': {
                    'code': '[u8; 4]',
                    'issuer': '[u8; 32]',
                },
                'StellarNative': None,
            },
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
        },
        {
            'account_id': 'AccountId',
            'currencies': {
                'collateral': {
                    'Native': None,
                    'Stellar': {
                        'AlphaNum12': {
                            'code': '[u8; 12]',
                            'issuer': '[u8; 32]',
                        },
                        'AlphaNum4': {
                            'code': '[u8; 4]',
                            'issuer': '[u8; 32]',
                        },
                        'StellarNative': None,
                    },
                    'Token': 'u64',
                    'XCM': 'u8',
                    'ZenlinkLPToken': (
                        'u8',
                        'u8',
                        'u8',
                        'u8',
                    ),
                },
                'wrapped': {
                    'Native': None,
                    'Stellar': {
                        'AlphaNum12': {
                            'code': '[u8; 12]',
                            'issuer': '[u8; 32]',
                        },
                        'AlphaNum4': {
                            'code': '[u8; 4]',
                            'issuer': '[u8; 32]',
                        },
                        'StellarNative': None,
                    },
                    'Token': 'u64',
                    'XCM': 'u8',
                    'ZenlinkLPToken': (
                        'u8',
                        'u8',
                        'u8',
                        'u8',
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
### Stake
 The stake of a participant in this reward pool.

#### Python
```python
result = substrate.query(
    'PooledVaultRewards', 'Stake', [
    (
        {
            'Native': None,
            'Stellar': {
                'AlphaNum12': {
                    'code': '[u8; 12]',
                    'issuer': '[u8; 32]',
                },
                'AlphaNum4': {
                    'code': '[u8; 4]',
                    'issuer': '[u8; 32]',
                },
                'StellarNative': None,
            },
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
        },
        {
            'account_id': 'AccountId',
            'currencies': {
                'collateral': {
                    'Native': None,
                    'Stellar': {
                        'AlphaNum12': {
                            'code': '[u8; 12]',
                            'issuer': '[u8; 32]',
                        },
                        'AlphaNum4': {
                            'code': '[u8; 4]',
                            'issuer': '[u8; 32]',
                        },
                        'StellarNative': None,
                    },
                    'Token': 'u64',
                    'XCM': 'u8',
                    'ZenlinkLPToken': (
                        'u8',
                        'u8',
                        'u8',
                        'u8',
                    ),
                },
                'wrapped': {
                    'Native': None,
                    'Stellar': {
                        'AlphaNum12': {
                            'code': '[u8; 12]',
                            'issuer': '[u8; 32]',
                        },
                        'AlphaNum4': {
                            'code': '[u8; 4]',
                            'issuer': '[u8; 32]',
                        },
                        'StellarNative': None,
                    },
                    'Token': 'u64',
                    'XCM': 'u8',
                    'ZenlinkLPToken': (
                        'u8',
                        'u8',
                        'u8',
                        'u8',
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
### TotalRewards
 The total unclaimed rewards distributed to this reward pool.
 NOTE: this is currently only used for integration tests.

#### Python
```python
result = substrate.query(
    'PooledVaultRewards', 'TotalRewards', [
    {
        'Native': None,
        'Stellar': {
            'AlphaNum12': {
                'code': '[u8; 12]',
                'issuer': '[u8; 32]',
            },
            'AlphaNum4': {
                'code': '[u8; 4]',
                'issuer': '[u8; 32]',
            },
            'StellarNative': None,
        },
        'Token': 'u64',
        'XCM': 'u8',
        'ZenlinkLPToken': (
            'u8',
            'u8',
            'u8',
            'u8',
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
    'PooledVaultRewards', 'TotalStake', [
    {
        'Native': None,
        'Stellar': {
            'AlphaNum12': {
                'code': '[u8; 12]',
                'issuer': '[u8; 32]',
            },
            'AlphaNum4': {
                'code': '[u8; 4]',
                'issuer': '[u8; 32]',
            },
            'StellarNative': None,
        },
        'Token': 'u64',
        'XCM': 'u8',
        'ZenlinkLPToken': (
            'u8',
            'u8',
            'u8',
            'u8',
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
## Constants

---------
### MaxRewardCurrencies
 The maximum number of reward currencies.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('PooledVaultRewards', 'MaxRewardCurrencies')
```
---------
## Errors

---------
### InsufficientFunds
Balance not sufficient to withdraw stake.

---------
### MaxRewardCurrencies
Maximum rewards currencies reached.

---------
### TryIntoIntError
Unable to convert value.

---------
### ZeroTotalStake
Cannot distribute rewards without stake.

---------