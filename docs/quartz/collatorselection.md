
# CollatorSelection

---------
## Calls

---------
### add_invulnerable
Add a collator to the list of invulnerable (fixed) collators.
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
Force deregister `origin` as a collator candidate as a governing authority, and revoke its license.
Note that the collator can only leave on session change.
The `LicenseBond` will be unreserved and returned immediately.

This call is, of course, not applicable to `Invulnerable` collators.
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
Purchase a license on block collation for this account.
It does not make it a collator candidate, use `onboard` afterward. The account must
(a) already have registered session keys and (b) be able to reserve the `LicenseBond`.

This call is not available to `Invulnerable` collators.
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
Deregister `origin` as a collator candidate. Note that the collator can only leave on
session change. The license to `onboard` later at any other time will remain.
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
Register this account as a candidate for collators for next sessions.
The account must already hold a license, and cannot offboard immediately during a session.

This call is not available to `Invulnerable` collators.
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
Forfeit `origin`&\#x27;s own license. The `LicenseBond` will be unreserved immediately.

This call is not available to `Invulnerable` collators.
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
Remove a collator from the list of invulnerable (fixed) collators.
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
## Constants

---------
### LicenceBondIdentifier
#### Value
```python
'0x6c6963656e63656964656e7469666965'
```
#### Python
```python
constant = substrate.get_constant('CollatorSelection', 'LicenceBondIdentifier')
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