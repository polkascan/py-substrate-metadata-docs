
# CollatorSelection

---------
## Calls

---------
### add_invulnerable
See [`Pallet::add_invulnerable`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'add_invulnerable', {'new': 'AccountId'}
)
```

---------
### force_release_license
See [`Pallet::force_release_license`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'force_release_license', {'who': 'AccountId'}
)
```

---------
### get_license
See [`Pallet::get_license`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'get_license', {}
)
```

---------
### offboard
See [`Pallet::offboard`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'offboard', {}
)
```

---------
### onboard
See [`Pallet::onboard`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'onboard', {}
)
```

---------
### release_license
See [`Pallet::release_license`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'CollatorSelection', 'release_license', {}
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
## Events

---------
### CandidateAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
### CandidateRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
### InvulnerableAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| invulnerable | `T::AccountId` | ```AccountId```

---------
### InvulnerableRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| invulnerable | `T::AccountId` | ```AccountId```

---------
### LicenseObtained
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```

---------
### LicenseReleased
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| deposit_returned | `BalanceOf<T>` | ```u128```

---------
## Storage functions

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
['AccountId']
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
### LicenseDepositOf
 The (community) collation license holders.

#### Python
```python
result = substrate.query(
    'CollatorSelection', 'LicenseDepositOf', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
## Errors

---------
### AlreadyCandidate
User is already a candidate

---------
### AlreadyHoldingLicense
User already holds license to collate

---------
### AlreadyInvulnerable
User is already an Invulnerable

---------
### NoAssociatedValidatorId
Account has no associated validator ID

---------
### NoLicense
User does not hold a license to collate

---------
### NotCandidate
User is not a candidate

---------
### NotInvulnerable
User is not an Invulnerable

---------
### Permission
Permission issue

---------
### TooFewInvulnerables
Too few invulnerables

---------
### TooManyCandidates
Too many candidates

---------
### TooManyInvulnerables
Too many invulnerables

---------
### Unknown
Unknown error

---------
### ValidatorNotRegistered
Validator ID is not yet registered

---------