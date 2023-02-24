
# EscrowAnnuity

---------
## Calls

---------
### set_reward_per_wrapped
#### Attributes
| Name | Type |
| -------- | -------- | 
| reward_per_wrapped | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'EscrowAnnuity', 'set_reward_per_wrapped', {'reward_per_wrapped': 'u128'}
)
```

---------
### update_rewards
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'EscrowAnnuity', 'update_rewards', {}
)
```

---------
### withdraw_rewards
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'EscrowAnnuity', 'withdraw_rewards', {}
)
```

---------
## Events

---------
### BlockReward
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T, I>` | ```u128```

---------
## Storage functions

---------
### RewardPerBlock

#### Python
```python
result = substrate.query(
    'EscrowAnnuity', 'RewardPerBlock', []
)
```

#### Return value
```python
'u128'
```
---------
### RewardPerWrapped

#### Python
```python
result = substrate.query(
    'EscrowAnnuity', 'RewardPerWrapped', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### AnnuityPalletId
 The annuity module id, used for deriving its sovereign account ID.
#### Value
```python
'0x6573632f616e6e75'
```
#### Python
```python
constant = substrate.get_constant('EscrowAnnuity', 'AnnuityPalletId')
```
---------
### EmissionPeriod
 The emission period for block rewards.
#### Value
```python
2628000
```
#### Python
```python
constant = substrate.get_constant('EscrowAnnuity', 'EmissionPeriod')
```
---------