
# RewardDistribution

---------
## Calls

---------
### collect_reward
Allow users who have staked to collect rewards for a given vault and rewraded currency
#### Attributes
| Name | Type |
| -------- | -------- | 
| vault_id | `DefaultVaultId<T>` | 
| reward_currency_id | `CurrencyId<T>` | 
| index | `Option<T::Index>` | 

#### Python
```python
call = substrate.compose_call(
    'RewardDistribution', 'collect_reward', {
    'index': (None, 'u32'),
    'reward_currency_id': {
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
    'vault_id': {
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
}
)
```

---------
### set_reward_per_block
Sets the reward per block.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_reward_per_block | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RewardDistribution', 'set_reward_per_block', {'new_reward_per_block': 'u128'}
)
```

---------
## Events

---------
### RewardPerBlockAdapted
A new RewardPerBlock value has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### NativeLiability
 Storage to keep track of the to-be-minted native rewards

#### Python
```python
result = substrate.query(
    'RewardDistribution', 'NativeLiability', []
)
```

#### Return value
```python
'u128'
```
---------
### RewardPerBlock
 Reward per block.

#### Python
```python
result = substrate.query(
    'RewardDistribution', 'RewardPerBlock', []
)
```

#### Return value
```python
'u128'
```
---------
### RewardsAdaptedAt
 Last Block were rewards per block were modified

#### Python
```python
result = substrate.query(
    'RewardDistribution', 'RewardsAdaptedAt', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### DecayInterval
 Defines the interval (in number of blocks) at which the reward per block decays.
#### Value
```python
216000
```
#### Python
```python
constant = substrate.get_constant('RewardDistribution', 'DecayInterval')
```
---------
### DecayRate
 Defines the rate at which the reward per block decays.
#### Value
```python
37567400000000000
```
#### Python
```python
constant = substrate.get_constant('RewardDistribution', 'DecayRate')
```
---------
## Errors

---------
### CollectAmountTooSmall
If the amount to collect is less than existential deposit

---------
### InconsistentRewardCurrencies
If distribution logic reaches an inconsistency with the amount of currencies in the
system

---------
### NoRewardsForAccount
Origin attempt to withdraw with 0 rewards

---------
### NotEnoughRewardsRegistered
Amount to be minted is more than total rewarded

---------
### Overflow
Overflow

---------
### Underflow
Underflow

---------