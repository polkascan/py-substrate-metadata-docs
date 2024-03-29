
# CollatorSelection

---------
## Calls

---------
### leave_intent
See [`Pallet::leave_intent`].
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
See [`Pallet::register_as_candidate`].
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
See [`Pallet::set_candidacy_bond`].
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
See [`Pallet::set_desired_candidates`].
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
See [`Pallet::set_invulnerables`].
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
### CandidateSlashed
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
### SlashDestination
 Destination account for slashed amount.

#### Python
```python
result = substrate.query(
    'CollatorSelection', 'SlashDestination', []
)
```

#### Return value
```python
'AccountId'
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
### NotAllowedCandidate
Account is now allowed to be a candidate due to an external reason (e.g. it might be participating in dApp staking)

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