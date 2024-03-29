
# FellowshipCore

---------
## Calls

---------
### approve
See [`Pallet::approve`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 
| at_rank | `RankOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipCore', 'approve', {'at_rank': 'u16', 'who': 'AccountId'}
)
```

---------
### bump
See [`Pallet::bump`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipCore', 'bump', {'who': 'AccountId'}
)
```

---------
### import
See [`Pallet::import`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'FellowshipCore', 'import', {}
)
```

---------
### induct
See [`Pallet::induct`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipCore', 'induct', {'who': 'AccountId'}
)
```

---------
### offboard
See [`Pallet::offboard`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipCore', 'offboard', {'who': 'AccountId'}
)
```

---------
### promote
See [`Pallet::promote`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 
| to_rank | `RankOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipCore', 'promote', {'to_rank': 'u16', 'who': 'AccountId'}
)
```

---------
### set_active
See [`Pallet::set_active`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| is_active | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipCore', 'set_active', {'is_active': 'bool'}
)
```

---------
### set_params
See [`Pallet::set_params`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| params | `Box<ParamsOf<T, I>>` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipCore', 'set_params', {
    'params': {
        'active_salary': '[u128; 9]',
        'demotion_period': '[u32; 9]',
        'min_promotion_period': '[u32; 9]',
        'offboard_timeout': 'u32',
        'passive_salary': '[u128; 9]',
    },
}
)
```

---------
### submit_evidence
See [`Pallet::submit_evidence`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| wish | `Wish` | 
| evidence | `Evidence<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipCore', 'submit_evidence', {
    'evidence': 'Bytes',
    'wish': ('Retention', 'Promotion'),
}
)
```

---------
## Events

---------
### ActiveChanged
Member activity flag has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| is_active | `bool` | ```bool```

---------
### Demoted
Member has been demoted to the given (non-zero) rank.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| to_rank | `RankOf<T, I>` | ```u16```

---------
### EvidenceJudged
Some submitted evidence was judged and removed. There may or may not have been a change
to the rank, but in any case, `last_proof` is reset.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| wish | `Wish` | ```('Retention', 'Promotion')```
| evidence | `Evidence<T, I>` | ```Bytes```
| old_rank | `u16` | ```u16```
| new_rank | `Option<u16>` | ```(None, 'u16')```

---------
### Imported
Pre-ranked account has been inducted at their current rank.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| rank | `RankOf<T, I>` | ```u16```

---------
### Inducted
Member has begun being tracked in this pallet.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

---------
### Offboarded
Member has been removed from being tracked in this pallet (i.e. because rank is now
zero).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

---------
### ParamsChanged
Parameters for the pallet have changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| params | `ParamsOf<T, I>` | ```{'active_salary': '[u128; 9]', 'passive_salary': '[u128; 9]', 'demotion_period': '[u32; 9]', 'min_promotion_period': '[u32; 9]', 'offboard_timeout': 'u32'}```

---------
### Promoted
Member has been promoted to the given rank.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| to_rank | `RankOf<T, I>` | ```u16```

---------
### Proven
Member has been proven at their current rank, postponing auto-demotion.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| at_rank | `RankOf<T, I>` | ```u16```

---------
### Requested
Member has stated evidence of their efforts their request for rank.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| wish | `Wish` | ```('Retention', 'Promotion')```

---------
## Storage functions

---------
### Member
 The status of a claimant.

#### Python
```python
result = substrate.query(
    'FellowshipCore', 'Member', ['AccountId']
)
```

#### Return value
```python
{'is_active': 'bool', 'last_promotion': 'u32', 'last_proof': 'u32'}
```
---------
### MemberEvidence
 Some evidence together with the desired outcome for which it was presented.

#### Python
```python
result = substrate.query(
    'FellowshipCore', 'MemberEvidence', ['AccountId']
)
```

#### Return value
```python
(('Retention', 'Promotion'), 'Bytes')
```
---------
### Params
 The overall status of the system.

#### Python
```python
result = substrate.query(
    'FellowshipCore', 'Params', []
)
```

#### Return value
```python
{
    'active_salary': '[u128; 9]',
    'demotion_period': '[u32; 9]',
    'min_promotion_period': '[u32; 9]',
    'offboard_timeout': 'u32',
    'passive_salary': '[u128; 9]',
}
```
---------
## Constants

---------
### EvidenceSize
 The maximum size in bytes submitted evidence is allowed to be.
#### Value
```python
65536
```
#### Python
```python
constant = substrate.get_constant('FellowshipCore', 'EvidenceSize')
```
---------
## Errors

---------
### AlreadyInducted
The candidate has already been inducted. This should never happen since it would
require a candidate (rank 0) to already be tracked in the pallet.

---------
### InvalidRank
The given rank is invalid - this generally means it&\#x27;s not between 1 and `RANK_COUNT`.

---------
### NoPermission
The origin does not have enough permission to do this operation.

---------
### NotTracked
The candidate has not been inducted, so cannot be offboarded from this pallet.

---------
### NothingDoing
No work needs to be done at present for this member.

---------
### Ranked
Member&\#x27;s rank is not zero.

---------
### TooSoon
Operation cannot be done yet since not enough time has passed.

---------
### UnexpectedRank
Member&\#x27;s rank is not as expected - generally means that the rank provided to the call
does not agree with the state of the system.

---------
### Unranked
Member&\#x27;s rank is too low.

---------