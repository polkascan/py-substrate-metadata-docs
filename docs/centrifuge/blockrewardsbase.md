
# BlockRewardsBase

---------
## Events

---------
### CurrencyAttached
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| from | `Option<T::GroupId>` | ```(None, 'u32')```
| to | `T::GroupId` | ```u32```

---------
### GroupRewarded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| group_id | `T::GroupId` | ```u32```
| amount | `BalanceOf<T, I>` | ```u128```

---------
### RewardClaimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| group_id | `T::GroupId` | ```u32```
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| account_id | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T, I>` | ```u128```

---------
### StakeDeposited
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| group_id | `T::GroupId` | ```u32```
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| account_id | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T, I>` | ```u128```

---------
### StakeWithdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| group_id | `T::GroupId` | ```u32```
| currency_id | `T::CurrencyId` | ```{'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}```
| account_id | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T, I>` | ```u128```

---------
## Storage functions

---------
### Currency

#### Python
```python
result = substrate.query(
    'BlockRewardsBase', 'Currency', [
    {
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
    },
]
)
```

#### Return value
```python
((None, 'u32'), {'rpt_changes': ['i128'], 'total_stake': 'u128'})
```
---------
### Group

#### Python
```python
result = substrate.query(
    'BlockRewardsBase', 'Group', ['u32']
)
```

#### Return value
```python
{'rpt': 'i128', 'total_stake': 'u128'}
```
---------
### StakeAccount

#### Python
```python
result = substrate.query(
    'BlockRewardsBase', 'StakeAccount', [
    'AccountId',
    {
        'Native': None,
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'Staking': ('BlockRewards', ),
    },
]
)
```

#### Return value
```python
{'last_currency_movement': 'u16', 'reward_tally': 'i128', 'stake': 'u128'}
```
---------
## Constants

---------
### PalletId
 Identifier of this pallet used as an account where stores the reward
 that is not claimed. When you distribute reward, the amount
 distributed goes here.
#### Value
```python
'0x6366672f626c7277'
```
#### Python
```python
constant = substrate.get_constant('BlockRewardsBase', 'PalletId')
```
---------
## Errors

---------
### CurrencyInSameGroup

---------
### CurrencyMaxMovementsReached

---------
### CurrencyWithoutGroup

---------