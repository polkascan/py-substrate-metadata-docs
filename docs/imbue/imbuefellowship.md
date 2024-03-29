
# ImbueFellowship

---------
## Calls

---------
### add_candidate_to_shortlist
See [`Pallet::add_candidate_to_shortlist`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `AccountIdOf<T>` | 
| role | `Role` | 
| rank | `Rank` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueFellowship', 'add_candidate_to_shortlist', {
    'candidate': 'AccountId',
    'rank': 'u16',
    'role': ('Vetter', 'Freelancer'),
}
)
```

---------
### force_add_fellowship
See [`Pallet::force_add_fellowship`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdOf<T>` | 
| role | `Role` | 
| rank | `Rank` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueFellowship', 'force_add_fellowship', {
    'rank': 'u16',
    'role': ('Vetter', 'Freelancer'),
    'who': 'AccountId',
}
)
```

---------
### force_remove_and_slash_fellowship
See [`Pallet::force_remove_and_slash_fellowship`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueFellowship', 'force_remove_and_slash_fellowship', {'who': 'AccountId'}
)
```

---------
### leave_fellowship
See [`Pallet::leave_fellowship`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ImbueFellowship', 'leave_fellowship', {}
)
```

---------
### pay_deposit_to_remove_pending_status
See [`Pallet::pay_deposit_to_remove_pending_status`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ImbueFellowship', 'pay_deposit_to_remove_pending_status', {}
)
```

---------
### remove_candidate_from_shortlist
See [`Pallet::remove_candidate_from_shortlist`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueFellowship', 'remove_candidate_from_shortlist', {'candidate': 'AccountId'}
)
```

---------
## Events

---------
### CandidateAddedToShortlist
A candidate has been added to the shortlist.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```

---------
### CandidateRemovedFromShortlist
A candidate has been removed from the shortlist.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```

---------
### FellowshipAdded
A member has been added to the fellowship.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```
| role | `Role` | ```('Vetter', 'Freelancer')```

---------
### FellowshipRemoved
A member has been removed from the fellowship.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```

---------
### FellowshipSlashed
A member has been removed from the fellowship and their deposit slashes.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```

---------
### MemberAddedToPendingFellows
A member has been added to pending fellows awaiting deposit payment.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```

---------
## Storage functions

---------
### CandidateShortlist
 Contains the shortlist of candidates to be sent for approval.

#### Python
```python
result = substrate.query(
    'ImbueFellowship', 'CandidateShortlist', ['u32']
)
```

#### Return value
```python
'scale_info::531'
```
---------
### FellowToVetter
 Keeps track of the accounts a fellow has recruited.
 Can be used to pay out completion fees.

#### Python
```python
result = substrate.query(
    'ImbueFellowship', 'FellowToVetter', ['AccountId']
)
```

#### Return value
```python
'AccountId'
```
---------
### FellowshipReserves
 Keeps track of the deposits taken from a fellow.
 Needed incase the reserve amount will change.

#### Python
```python
result = substrate.query(
    'ImbueFellowship', 'FellowshipReserves', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### JuryPointer
 Jury pointer for setting the mark at which fellows have been selected for jury.

#### Python
```python
result = substrate.query(
    'ImbueFellowship', 'JuryPointer', []
)
```

#### Return value
```python
'u128'
```
---------
### PendingFellows
 Holds all the accounts that are able to become fellows that have not given their deposit for membership.

#### Python
```python
result = substrate.query(
    'ImbueFellowship', 'PendingFellows', ['AccountId']
)
```

#### Return value
```python
(('Vetter', 'Freelancer'), 'u16')
```
---------
### Roles
 Used to map who is a part of the fellowship.
 Returns the role of the account

#### Python
```python
result = substrate.query(
    'ImbueFellowship', 'Roles', ['AccountId']
)
```

#### Return value
```python
(('Vetter', 'Freelancer'), 'u16')
```
---------
### ShortlistRound
 Keeps track of the round the shortlist is in.

#### Python
```python
result = substrate.query(
    'ImbueFellowship', 'ShortlistRound', []
)
```

#### Return value
```python
'u32'
```
---------
## Errors

---------
### AlreadyAFellow
Already a fellow.

---------
### CandidateAlreadyOnShortlist
The candidate is already on the shortlist.

---------
### CandidateDepositRequired
The candidate must have the deposit amount to be put on the shortlst.

---------
### FellowshipReserveDisapeared
The fellowship deposit has could not be found, contact development.

---------
### NotAFellow
This account is not a fellow.

---------
### RoleLacksPermission
The role of the caller lacks the necessary permissions to run this.

---------
### RoleNotFound
This account does not have a role in the fellowship.

---------
### TooManyCandidates
The maximum number of candidates has been reached.

---------