
# VaultStaking

---------
## Events

---------
### DepositStake
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}}}```
| nominator_id | `T::AccountId` | ```AccountId```
| amount | `T::SignedFixedPoint` | ```i128```

---------
### DistributeReward
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}```
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}}}```
| amount | `T::SignedFixedPoint` | ```i128```

---------
### ForceRefund
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}}}```

---------
### IncreaseNonce
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}}}```
| new_nonce | `T::Index` | ```u32```

---------
### WithdrawReward
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| nonce | `T::Index` | ```u32```
| currency_id | `T::CurrencyId` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}```
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}}}```
| nominator_id | `T::AccountId` | ```AccountId```
| amount | `T::SignedFixedPoint` | ```i128```

---------
### WithdrawStake
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}}}```
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
        'XCM': 'u8',
        'ZenlinkLPToken': (
            'u8',
            'u8',
            'u8',
            'u8',
        ),
    },
    (
        'u32',
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
### RewardTally
 Accounts for previous changes in stake size.

#### Python
```python
result = substrate.query(
    'VaultStaking', 'RewardTally', [
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
        'XCM': 'u8',
        'ZenlinkLPToken': (
            'u8',
            'u8',
            'u8',
            'u8',
        ),
    },
    (
        'u32',
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
        'XCM': 'u8',
        'ZenlinkLPToken': (
            'u8',
            'u8',
            'u8',
            'u8',
        ),
    },
    (
        'u32',
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
'Native'
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