
# CollatorSelection

---------
## Calls

---------
### leave_intent
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'leave_intent', {}
)
```

---------
### register_as_candidate
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'register_as_candidate', {}
)
```

---------
### register_candidate
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_candidate | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'register_candidate', {'new_candidate': 'AccountId'}
)
```

---------
### set_candidacy_bond
#### Attributes
| Name | Type |
| -------- | -------- | 
| bond | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'set_candidacy_bond', {'bond': 'u128'}
)
```

---------
### set_desired_candidates
#### Attributes
| Name | Type |
| -------- | -------- | 
| max | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'set_desired_candidates', {'max': 'u32'}
)
```

---------
### set_invulnerables
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'set_invulnerables', {'new': ['AccountId']}
)
```

---------
### withdraw_bond
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'withdraw_bond', {}
)
```

---------
## Events

---------
### CandidateAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| bond | `BalanceOf<T>` | ```u128```

---------
### CandidateRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

---------
### NewCandidacyBond
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| new_candidacy_bond | `BalanceOf<T>` | ```u128```

---------
### NewDesiredCandidates
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| new_desired_candidates | `u32` | ```u32```

---------
### NewInvulnerables
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| new_invulnerables | `Vec<T::AccountId>` | ```['AccountId']```

---------
## Storage functions

---------
### CandidacyBond

#### Python
```python
result = substrate.query(
    'CollatorSelection', 'CandidacyBond', []
)
```

#### Return value
```python
'u128'
```
---------
### Candidates

#### Python
```python
result = substrate.query(
    'CollatorSelection', 'Candidates', []
)
```

#### Return value
```python
'scale_info::428'
```
---------
### DesiredCandidates

#### Python
```python
result = substrate.query(
    'CollatorSelection', 'DesiredCandidates', []
)
```

#### Return value
```python
'u32'
```
---------
### Invulnerables

#### Python
```python
result = substrate.query(
    'CollatorSelection', 'Invulnerables', []
)
```

#### Return value
```python
['AccountId']
```
---------
### NonCandidates

#### Python
```python
result = substrate.query(
    'CollatorSelection', 'NonCandidates', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### SessionPoints

#### Python
```python
result = substrate.query(
    'CollatorSelection', 'SessionPoints', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### CollatorKickThreshold
#### Value
```python
650000
```
#### Python
```python
constant = substrate.get_constant('CollatorSelection', 'CollatorKickThreshold')
```
---------
### KickPenaltySessionLength
#### Value
```python
8
```
#### Python
```python
constant = substrate.get_constant('CollatorSelection', 'KickPenaltySessionLength')
```
---------
### MaxCandidates
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('CollatorSelection', 'MaxCandidates')
```
---------
### MaxInvulnerables
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('CollatorSelection', 'MaxInvulnerables')
```
---------
### MinCandidates
#### Value
```python
4
```
#### Python
```python
constant = substrate.get_constant('CollatorSelection', 'MinCandidates')
```
---------
### MinRewardDistributeAmount
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('CollatorSelection', 'MinRewardDistributeAmount')
```
---------
### PotId
#### Value
```python
'0x6163612f63706f74'
```
#### Python
```python
constant = substrate.get_constant('CollatorSelection', 'PotId')
```
---------
## Errors

---------
### AlreadyCandidate

---------
### AlreadyInvulnerable

---------
### BelowCandidatesMin

---------
### InvalidProof

---------
### MaxCandidatesExceeded

---------
### MaxInvulnerablesExceeded

---------
### NotCandidate

---------
### NotNonCandidate

---------
### NothingToWithdraw

---------
### Permission

---------
### RequireSessionKey

---------
### StillLocked

---------
### Unknown

---------