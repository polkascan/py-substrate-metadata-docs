
# QuadraticFunding

---------
## Calls

---------
### donate
An example dispatchable that takes a singles value as a parameter, writes the value to
storage and emits an event. This function must be dispatched by a signed extrinsic.
#### Attributes
| Name | Type |
| -------- | -------- | 
| round_id | `u32` | 
| amount | `BalanceOf<T>` | 
| currency_id | `CurrencyIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'QuadraticFunding', 'donate', {
    'amount': 'u128',
    'currency_id': ('KSM', 'DORA'),
    'round_id': 'u32',
}
)
```

---------
### end_round
End an `ongoing` round and distribute the funds in sponsor pool, any invalid index or round status will cause errors
#### Attributes
| Name | Type |
| -------- | -------- | 
| round_id | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'QuadraticFunding', 'end_round', {'round_id': 'u32'}
)
```

---------
### register_project
Register a project in an ongoing round, so that it can be voted
#### Attributes
| Name | Type |
| -------- | -------- | 
| round_id | `u32` | 
| hash | `T::Hash` | 
| name | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'QuadraticFunding', 'register_project', {
    'hash': '[u8; 32]',
    'name': 'Bytes',
    'round_id': 'u32',
}
)
```

---------
### start_round
#### Attributes
| Name | Type |
| -------- | -------- | 
| round_id | `u32` | 
| currency_id | `CurrencyIdOf<T>` | 
| name | `Vec<u8>` | 
| admin | `T::AccountId` | 
| round_reserve | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'QuadraticFunding', 'start_round', {
    'admin': 'AccountId',
    'currency_id': ('KSM', 'DORA'),
    'name': 'Bytes',
    'round_id': 'u32',
    'round_reserve': 'u128',
}
)
```

---------
### vote
Vote to a project, this function will transfer corresponding amount of token per your input ballot
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyIdOf<T>` | 
| round_id | `u32` | 
| hash | `T::Hash` | 
| ballot | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'QuadraticFunding', 'vote', {
    'ballot': 'u128',
    'currency_id': ('KSM', 'DORA'),
    'hash': '[u8; 32]',
    'round_id': 'u32',
}
)
```

---------
## Events

---------
### DonateSucceed
parameters. [round_id, who, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### ProjectRegistered
Event documentation should end with an array that provides descriptive names for event
parameters. [project_hash, who]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Hash` | ```[u8; 32]```
| None | `T::AccountId` | ```AccountId```

---------
### RoundEnded
parameters. [round_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### RoundStarted
parameters. [round_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### VoteCost
parameters. [project_hash, balance of cost]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Hash` | ```[u8; 32]```
| None | `u128` | ```u128```

---------
### VoteSucceed
parameters. [project_hash, who, number of ballots]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Hash` | ```[u8; 32]```
| None | `T::AccountId` | ```AccountId```
| None | `u128` | ```u128```

---------
## Storage functions

---------
### ProjectVotes

#### Python
```python
result = substrate.query(
    'QuadraticFunding', 'ProjectVotes', ['[u8; 32]', 'AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### Projects

#### Python
```python
result = substrate.query(
    'QuadraticFunding', 'Projects', ['u32', '[u8; 32]']
)
```

#### Return value
```python
{
    'grants': 'u128',
    'name': 'Bytes',
    'owner': 'AccountId',
    'support_area': 'u128',
    'support_fund': 'u128',
    'total_votes': 'u128',
}
```
---------
### RoundParticipants

#### Python
```python
result = substrate.query(
    'QuadraticFunding', 'RoundParticipants', ['u32', 'AccountId']
)
```

#### Return value
```python
'bool'
```
---------
### Rounds

#### Python
```python
result = substrate.query(
    'QuadraticFunding', 'Rounds', ['u32']
)
```

#### Return value
```python
{
    'admin': 'AccountId',
    'currency_id': ('KSM', 'DORA'),
    'name': 'Bytes',
    'ongoing': 'bool',
    'pre_tax_support_pool': 'u128',
    'round_reserve': 'u128',
    'support_pool': 'u128',
    'total_support_area': 'u128',
    'total_tax': 'u128',
}
```
---------
## Constants

---------
### PalletId
#### Value
```python
'0x70792f7175616664'
```
#### Python
```python
constant = substrate.get_constant('QuadraticFunding', 'PalletId')
```
---------
## Errors

---------
### BadMetadata

---------
### DonationTooSmall

---------
### DuplicateProject

---------
### DuplicateRound

---------
### InsufficientReserveDora

---------
### InvalidBallot

---------
### MismatchingCurencyId

---------
### NoneValue
Error names should be descriptive.

---------
### ProjectNameTooLong

---------
### ProjectNameTooShort

---------
### ProjectNotExist

---------
### RoundExisted

---------
### RoundHasEnded

---------
### RoundNameTooLong

---------
### RoundNameTooShort

---------
### RoundNotExist

---------
### StorageOverflow
Errors should have helpful documentation associated with them.

---------