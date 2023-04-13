
# EqStaking

---------
## Calls

---------
### add_manager
#### Attributes
| Name | Type |
| -------- | -------- | 
| manager | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'EqStaking', 'add_manager', {'manager': 'AccountId'}
)
```

---------
### custom_reward
#### Attributes
| Name | Type |
| -------- | -------- | 
| rewards | `Vec<(T::AccountId, StakePeriod, T::Balance)>` | 

#### Python
```python
call = substrate.compose_call(
    'EqStaking', 'custom_reward', {
    'rewards': [
        (
            'AccountId',
            (
                'One',
                'Two',
                'Three',
                'Six',
                'Twelve',
                'Sixteen',
                'Eighteen',
                'TwentyFour',
            ),
            'u128',
        ),
    ],
}
)
```

---------
### reward
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 
| amount | `T::Balance` | 
| external_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'EqStaking', 'reward', {
    'amount': 'u128',
    'external_id': 'u64',
    'who': 'AccountId',
}
)
```

---------
### stake
Stake the minimum value of `amount` and current free EQ balance for `period` if `MaxStakesCount` not reached
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `T::Balance` | 
| period | `StakePeriod` | 

#### Python
```python
call = substrate.compose_call(
    'EqStaking', 'stake', {
    'amount': 'u128',
    'period': (
        'One',
        'Two',
        'Three',
        'Six',
        'Twelve',
        'Sixteen',
        'Eighteen',
        'TwentyFour',
    ),
}
)
```

---------
### unlock
Unlock stake if mb_stake_index is some or unlock rewards otherwise.
Checks is lock period ended and throw error if not so.
#### Attributes
| Name | Type |
| -------- | -------- | 
| mb_stake_index | `Option<u32>` | 

#### Python
```python
call = substrate.compose_call(
    'EqStaking', 'unlock', {'mb_stake_index': (None, 'u32')}
)
```

---------
## Events

---------
### Distributed
\[accounts\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### Rewarded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```
| external_id | `u64` | ```u64```

---------
### Staked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```
| period | `StakePeriod` | ```('One', 'Two', 'Three', 'Six', 'Twelve', 'Sixteen', 'Eighteen', 'TwentyFour')```

---------
## Storage functions

---------
### PalletManager

#### Python
```python
result = substrate.query(
    'EqStaking', 'PalletManager', []
)
```

#### Return value
```python
'AccountId'
```
---------
### RewardExternalIds

#### Python
```python
result = substrate.query(
    'EqStaking', 'RewardExternalIds', []
)
```

#### Return value
```python
'scale_info::542'
```
---------
### Rewards

#### Python
```python
result = substrate.query(
    'EqStaking', 'Rewards', ['AccountId']
)
```

#### Return value
```python
{
    'amount': 'u128',
    'period': (
        'One',
        'Two',
        'Three',
        'Six',
        'Twelve',
        'Sixteen',
        'Eighteen',
        'TwentyFour',
    ),
    'start': 'u64',
}
```
---------
### Stakes

#### Python
```python
result = substrate.query(
    'EqStaking', 'Stakes', ['AccountId']
)
```

#### Return value
```python
[
    {
        'amount': 'u128',
        'period': (
            'One',
            'Two',
            'Three',
            'Six',
            'Twelve',
            'Sixteen',
            'Eighteen',
            'TwentyFour',
        ),
        'start': 'u64',
    },
]
```
---------
## Constants

---------
### MaxRewardExternalIdsCount
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('EqStaking', 'MaxRewardExternalIdsCount')
```
---------
### MaxStakesCount
 Max number of stakes for single account
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('EqStaking', 'MaxStakesCount')
```
---------
### RewardsLockPeriod
#### Value
```python
'Six'
```
#### Python
```python
constant = substrate.get_constant('EqStaking', 'RewardsLockPeriod')
```
---------
## Errors

---------
### CustomReward
Some error occurs in custom_reward

---------
### InsufficientFunds
No funds to stake

---------
### LockPeriodNotEnded
The funds blocking period has not ended yet

---------
### MaxStakesNumberReached
The account reached stakes max number

---------
### StakeNotFound
No stake with this arguments

---------
### UnableToAddRewardExternalId
Error while adding reward external ID

---------