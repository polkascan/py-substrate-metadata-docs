
# Crowdloan

---------
## Calls

---------
### send_reward
Reward crowdloan participant.
#### Attributes
| Name | Type |
| -------- | -------- | 
| recipient | `T::AccountId` | 
| reward_value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Crowdloan', 'send_reward', {
    'recipient': 'AccountId',
    'reward_value': 'u128',
}
)
```

---------
## Events

---------
### RewardPaid
Crowdloan reward paid
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------