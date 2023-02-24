
# CollatorSelection

---------
## Calls

---------
### leave_intent
Deregister `origin` as a collator candidate. Note that the collator can only leave on
session change. The `CandidacyBond` will be unreserved immediately.

This call will fail if the total number of candidates would drop below `MinCandidates`.

This call is not available to `Invulnerable` collators.
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
Register this account as a collator candidate. The account must (a) already have
registered session keys and (b) be able to reserve the `CandidacyBond`.

This call is not available to `Invulnerable` collators.
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
Set the candidacy bond amount.
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
Set the ideal number of collators (not including the invulnerables).
If lowering this number, then the number of running collators could be higher than this figure.
Aside from that edge case, there should be no other way to have more collators than the desired number.
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
Set the list of invulnerable (fixed) collators.
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
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### CandidateRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### NewCandidacyBond
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T>` | ```u128```

---------
### NewDesiredCandidates
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### NewInvulnerables
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<T::AccountId>` | ```['AccountId']```

---------
## Storage functions

---------
### CandidacyBond
 Fixed amount to deposit to become a collator.

 When a collator calls `leave_intent` they immediately receive the deposit back.

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
 The (community, limited) collation candidates.

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
 Desired number of candidates.

 This should ideally always be less than [`Config::MaxCandidates`] for weights to be correct.

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
 The invulnerable, fixed collators.

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
 Last block authored by collator.

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
User is already a candidate

---------
### AlreadyInvulnerable
User is already an Invulnerable

---------
### NoAssociatedValidatorId
Account has no associated validator ID

---------
### NotCandidate
User is not a candidate

---------
### Permission
Permission issue

---------
### TooFewCandidates
Too few candidates

---------
### TooManyCandidates
Too many candidates

---------
### Unknown
Unknown error

---------
### ValidatorNotRegistered
Validator ID is not yet registered

---------