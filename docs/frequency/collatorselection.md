
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
## Events

---------
### CandidateAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```

---------
### CandidateRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
### NewCandidacyBond
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| bond_amount | `BalanceOf<T>` | ```u128```

---------
### NewDesiredCandidates
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| desired_candidates | `u32` | ```u32```

---------
### NewInvulnerables
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| invulnerables | `Vec<T::AccountId>` | ```['AccountId']```

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
[{'deposit': 'u128', 'who': 'AccountId'}]
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
### LastAuthoredBlock

#### Python
```python
result = substrate.query(
    'CollatorSelection', 'LastAuthoredBlock', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
## Errors

---------
### AlreadyCandidate

---------
### AlreadyInvulnerable

---------
### NoAssociatedValidatorId

---------
### NotCandidate

---------
### Permission

---------
### TooFewCandidates

---------
### TooManyCandidates

---------
### TooManyInvulnerables

---------
### Unknown

---------
### ValidatorNotRegistered

---------