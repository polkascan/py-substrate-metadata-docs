
# Web3Names

---------
## Calls

---------
### ban
See [`Pallet::ban`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| name | `Web3NameInput<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Web3Names', 'ban', {'name': 'Bytes'}
)
```

---------
### change_deposit_owner
See [`Pallet::change_deposit_owner`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Web3Names', 'change_deposit_owner', {}
)
```

---------
### claim
See [`Pallet::claim`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| name | `Web3NameInput<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Web3Names', 'claim', {'name': 'Bytes'}
)
```

---------
### reclaim_deposit
See [`Pallet::reclaim_deposit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| name | `Web3NameInput<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Web3Names', 'reclaim_deposit', {'name': 'Bytes'}
)
```

---------
### release_by_owner
See [`Pallet::release_by_owner`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Web3Names', 'release_by_owner', {}
)
```

---------
### unban
See [`Pallet::unban`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| name | `Web3NameInput<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Web3Names', 'unban', {'name': 'Bytes'}
)
```

---------
### update_deposit
See [`Pallet::update_deposit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| name_input | `Web3NameInput<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Web3Names', 'update_deposit', {'name_input': 'Bytes'}
)
```

---------
## Events

---------
### Web3NameBanned
A name has been banned.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| name | `Web3NameOf<T>` | ```Bytes```

---------
### Web3NameClaimed
A new name has been claimed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `Web3NameOwnerOf<T>` | ```AccountId```
| name | `Web3NameOf<T>` | ```Bytes```

---------
### Web3NameReleased
A name has been released.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `Web3NameOwnerOf<T>` | ```AccountId```
| name | `Web3NameOf<T>` | ```Bytes```

---------
### Web3NameUnbanned
A name has been unbanned.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| name | `Web3NameOf<T>` | ```Bytes```

---------
## Storage functions

---------
### Banned
 Map of name -&gt; ().

 If a name key is present, the name is currently banned.

#### Python
```python
result = substrate.query(
    'Web3Names', 'Banned', ['Bytes']
)
```

#### Return value
```python
()
```
---------
### Names
 Map of owner -&gt; name.

#### Python
```python
result = substrate.query(
    'Web3Names', 'Names', ['AccountId']
)
```

#### Return value
```python
'Bytes'
```
---------
### Owner
 Map of name -&gt; ownership details.

#### Python
```python
result = substrate.query(
    'Web3Names', 'Owner', ['Bytes']
)
```

#### Return value
```python
{'claimed_at': 'u64', 'deposit': {'amount': 'u128', 'owner': 'AccountId'}, 'owner': 'AccountId'}
```
---------
## Constants

---------
### Deposit
 The amount of KILT to deposit to claim a name.
#### Value
```python
118050000000000
```
#### Python
```python
constant = substrate.get_constant('Web3Names', 'Deposit')
```
---------
### MaxNameLength
 The max encoded length of a name.
#### Value
```python
32
```
#### Python
```python
constant = substrate.get_constant('Web3Names', 'MaxNameLength')
```
---------
### MinNameLength
 The min encoded length of a name.
#### Value
```python
3
```
#### Python
```python
constant = substrate.get_constant('Web3Names', 'MinNameLength')
```
---------
## Errors

---------
### AlreadyBanned
The specified name has already been previously banned.

---------
### AlreadyExists
The specified name has already been previously claimed.

---------
### Banned
The specified name has been banned and cannot be interacted
with.

---------
### InsufficientFunds
The tx submitter does not have enough funds to pay for the deposit.

---------
### InvalidCharacter
A name that contains not allowed characters is being claimed.

---------
### NotAuthorized
The actor cannot performed the specified operation.

---------
### NotBanned
The specified name is not currently banned.

---------
### NotFound
The specified name does not exist.

---------
### OwnerAlreadyExists
The specified owner already owns a name.

---------
### OwnerNotFound
The specified owner does not own any names.

---------
### TooLong
A name that is too long is being claimed.

---------
### TooShort
A name that is too short is being claimed.

---------