
# VaultRewards

---------
## Events

---------
### DepositStake
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| reward_id | `T::RewardId` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```
| amount | `T::SignedFixedPoint` | ```i128```

---------
### DistributeReward
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}```
| amount | `T::SignedFixedPoint` | ```i128```

---------
### WithdrawReward
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| reward_id | `T::RewardId` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```
| currency_id | `T::CurrencyId` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}```
| amount | `T::SignedFixedPoint` | ```i128```

---------
### WithdrawStake
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| reward_id | `T::RewardId` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```
| amount | `T::SignedFixedPoint` | ```i128```

---------
## Storage functions

---------
### RewardPerToken
 Used to compute the rewards for a participant&#x27;s stake.

#### Python
```python
result = substrate.query(
    'VaultRewards', 'RewardPerToken', [
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
    'VaultRewards', 'RewardTally', [
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
                'XCM': 'u8',
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
### Stake
 The stake of a participant in this reward pool.

#### Python
```python
result = substrate.query(
    'VaultRewards', 'Stake', [
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
    'VaultRewards', 'TotalRewards', [
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
    'VaultRewards', 'TotalStake', []
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
constant = substrate.get_constant('VaultRewards', 'GetNativeCurrencyId')
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