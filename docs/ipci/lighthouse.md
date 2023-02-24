
# Lighthouse

---------
## Calls

---------
### set
Inherent to set the lighthouse of a block.
#### Attributes
| Name | Type |
| -------- | -------- | 
| lighthouse | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Lighthouse', 'set', {'lighthouse': 'AccountId'}
)
```

---------
## Events

---------
### BlockReward
An account rewarded for block production. \[lighthouse, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### BlockReward
 Current block lighthouse reward.

#### Python
```python
result = substrate.query(
    'Lighthouse', 'BlockReward', []
)
```

#### Return value
```python
'u128'
```
---------
### Lighthouse
 Current block lighthouse account.

#### Python
```python
result = substrate.query(
    'Lighthouse', 'Lighthouse', []
)
```

#### Return value
```python
'AccountId'
```
---------
## Constants

---------
### BlockReward
 Reward amount for block proposer.
#### Value
```python
380520
```
#### Python
```python
constant = substrate.get_constant('Lighthouse', 'BlockReward')
```
---------
## Errors

---------
### LighthouseAlreadySet
Lighthouse already set in block.

---------