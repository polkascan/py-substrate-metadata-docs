
# Earning

---------
## Calls

---------
### bond
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Earning', 'bond', {'amount': 'u128'}
)
```

---------
### rebond
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Earning', 'rebond', {'amount': 'u128'}
)
```

---------
### unbond
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Earning', 'unbond', {'amount': 'u128'}
)
```

---------
### unbond_instant
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Earning', 'unbond_instant', {'amount': 'u128'}
)
```

---------
### withdraw_unbonded
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Earning', 'withdraw_unbonded', {}
)
```

---------
## Events

---------
### Bonded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `Balance` | ```u128```

---------
### InstantUnbonded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `Balance` | ```u128```
| fee | `Balance` | ```u128```

---------
### Rebonded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `Balance` | ```u128```

---------
### Unbonded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `Balance` | ```u128```

---------
### Withdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `Balance` | ```u128```

---------
## Storage functions

---------
### Ledger

#### Python
```python
result = substrate.query(
    'Earning', 'Ledger', ['AccountId']
)
```

#### Return value
```python
{
    'active': 'u128',
    'total': 'u128',
    'unlocking': [{'unlock_at': 'u32', 'value': 'u128'}],
}
```
---------
## Constants

---------
### InstantUnstakeFee
#### Value
```python
None
```
#### Python
```python
constant = substrate.get_constant('Earning', 'InstantUnstakeFee')
```
---------
### LockIdentifier
#### Value
```python
'0x6163612f6561726e'
```
#### Python
```python
constant = substrate.get_constant('Earning', 'LockIdentifier')
```
---------
### MaxUnbondingChunks
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Earning', 'MaxUnbondingChunks')
```
---------
### MinBond
#### Value
```python
100000000000000
```
#### Python
```python
constant = substrate.get_constant('Earning', 'MinBond')
```
---------
### UnbondingPeriod
#### Value
```python
201600
```
#### Python
```python
constant = substrate.get_constant('Earning', 'UnbondingPeriod')
```
---------
## Errors

---------
### BelowMinBondThreshold

---------
### MaxUnlockChunksExceeded

---------
### NotAllowed

---------
### NotBonded

---------