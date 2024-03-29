
# CollatorSelection

---------
## Calls

---------
### add_invulnerable
See [`Pallet::add_invulnerable`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'add_invulnerable', {'who': 'AccountId'}
)
```

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
### remove_invulnerable
See [`Pallet::remove_invulnerable`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'remove_invulnerable', {'who': 'AccountId'}
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
### take_candidate_slot
See [`Pallet::take_candidate_slot`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| deposit | `BalanceOf<T>` | 
| target | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'take_candidate_slot', {
    'deposit': 'u128',
    'target': 'AccountId',
}
)
```

---------
### update_bond
See [`Pallet::update_bond`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_deposit | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'update_bond', {'new_deposit': 'u128'}
)
```

---------
## Events

---------
### CandidateAdded
A new candidate joined.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```

---------
### CandidateBondUpdated
Bond of a candidate updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```

---------
### CandidateRemoved
A candidate was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
### CandidateReplaced
An account was replaced in the candidate list by another one.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old | `T::AccountId` | ```AccountId```
| new | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```

---------
### InvalidInvulnerableSkipped
An account was unable to be added to the Invulnerables because they did not have keys
registered. Other Invulnerables may have been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
### InvulnerableAdded
A new Invulnerable was added.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
### InvulnerableRemoved
An Invulnerable was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
### NewCandidacyBond
The candidacy bond was set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| bond_amount | `BalanceOf<T>` | ```u128```

---------
### NewDesiredCandidates
The number of desired candidates was set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| desired_candidates | `u32` | ```u32```

---------
### NewInvulnerables
New Invulnerables were set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| invulnerables | `Vec<T::AccountId>` | ```['AccountId']```

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
### CandidateList
 The (community, limited) collation candidates. `Candidates` and `Invulnerables` should be
 mutually exclusive.

 This list is sorted in ascending order by deposit and when the deposits are equal, the least
 recently updated is considered greater.

#### Python
```python
result = substrate.query(
    'CollatorSelection', 'CandidateList', []
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
 The invulnerable, permissioned collators. This list must be sorted.

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
Account is already a candidate.

---------
### AlreadyInvulnerable
Account is already an Invulnerable.

---------
### DepositTooLow
New deposit amount would be below the minimum candidacy bond.

---------
### IdenticalDeposit
The updated deposit amount is equal to the amount already reserved.

---------
### InsertToCandidateListFailed
Could not insert in the candidate list.

---------
### InsufficientBond
Deposit amount is too low to take the target&\#x27;s slot in the candidate list.

---------
### InvalidUnreserve
Cannot lower candidacy bond while occupying a future collator slot in the list.

---------
### NoAssociatedValidatorId
Account has no associated validator ID.

---------
### NotCandidate
Account is not a candidate.

---------
### NotInvulnerable
Account is not an Invulnerable.

---------
### RemoveFromCandidateListFailed
Could not remove from the candidate list.

---------
### TargetIsNotCandidate
The target account to be replaced in the candidate list is not a candidate.

---------
### TooFewEligibleCollators
Leaving would result in too few candidates.

---------
### TooManyCandidates
The pallet has too many candidates.

---------
### TooManyInvulnerables
There are too many Invulnerables.

---------
### UpdateCandidateListFailed
Could not update the candidate list.

---------
### ValidatorNotRegistered
Validator ID is not yet registered.

---------