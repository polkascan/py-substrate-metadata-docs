
# CollatorSelection

---------
## Calls

---------
### leave_intent
Leave from collator set.
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
Register as candidate collator.
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
Register an specified candidate as collator.

- `new_candidate`: Who is going to be collator.
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
### remove_collator
Remove an specified collator.

- `collator`: Who is going to be remove from collators set.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collator | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'remove_collator', {'collator': 'AccountId'}
)
```

---------
### set_candidacy_bond
Set the amount held on reserved for candidate collator.

`bond`: The amount held on reserved.
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
Set how many candidate collator are allowed.

`max`: The max number of candidates.
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
### set_eviction_baseline
Set the collator performance percentile used as baseline for eviction

`percentile`: x-th percentile of collator performance to use as eviction baseline
#### Attributes
| Name | Type |
| -------- | -------- | 
| percentile | `Percent` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'set_eviction_baseline', {'percentile': 'u8'}
)
```

---------
### set_eviction_tolerance
Set the tolerated underperformance percentage before evicting

`percentage`: x% of missed blocks under eviction_baseline to tolerate
#### Attributes
| Name | Type |
| -------- | -------- | 
| percentage | `Percent` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'set_eviction_tolerance', {'percentage': 'u8'}
)
```

---------
### set_invulnerables
Set candidate collator as invulnerable.

`new`: candidate collator.
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
### NewEvictionBaseline
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Percent` | ```u8```

---------
### NewEvictionTolerance
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Percent` | ```u8```

---------
### NewInvulnerables
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<T::AccountId>` | ```['AccountId']```

---------
## Storage functions

---------
### BlocksPerCollatorThisSession

#### Python
```python
result = substrate.query(
    'CollatorSelection', 'BlocksPerCollatorThisSession', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### CandidacyBond
 Fixed deposit bond for each candidate.

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
### EvictionBaseline
 Performance percentile to use as baseline for collator eviction

#### Python
```python
result = substrate.query(
    'CollatorSelection', 'EvictionBaseline', []
)
```

#### Return value
```python
'u8'
```
---------
### EvictionTolerance
 Percentage of underperformance to _tolerate_ before evicting a collator

 i.e. A collator gets evicted if it produced _less_ than x% fewer blocks than the collator at EvictionBaseline

#### Python
```python
result = substrate.query(
    'CollatorSelection', 'EvictionTolerance', []
)
```

#### Return value
```python
'u8'
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
### NotAllowRemoveInvulnerable
Removing invulnerable collators is not allowed

---------
### NotCandidate
User is not a candidate

---------
### Permission
Permission issue

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