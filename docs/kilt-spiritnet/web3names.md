
# Web3Names

---------
## Calls

---------
### ban
Ban a name.

A banned name cannot be claimed by anyone. The name&\#x27;s deposit
is returned to the original payer.

The origin must be the ban origin.

Emits `Web3NameBanned` if the operation is carried out
successfully.

\# &lt;weight&gt;
Weight: O(1)
- Reads: Banned, Owner, Names storage entries + origin check
- Writes: Names, Owner, Banned storage entries + currency deposit
  release
\# &lt;/weight&gt;
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
Changes the deposit owner.

The balance that is reserved by the current deposit owner will be
freed and balance of the new deposit owner will get reserved.

The subject of the call must be the owner of the web3name.
The sender of the call will be the new deposit owner.
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
Assign the specified name to the owner as specified in the
origin.

The name must not have already been claimed by someone else and the
owner must not already own another name.

Emits `Web3NameClaimed` if the operation is carried out
successfully.

\# &lt;weight&gt;
Weight: O(1)
- Reads: Names, Owner, Banned storage entries + available currency
  check + origin check
- Writes: Names, Owner storage entries + currency deposit reserve
\# &lt;/weight&gt;
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
Release the provided name from its owner.

The origin must be the account that paid for the name&\#x27;s deposit.

Emits `Web3NameReleased` if the operation is carried out
successfully.

\# &lt;weight&gt;
Weight: O(1)
- Reads: Owner storage entry + origin check
- Writes: Names, Owner storage entries + currency deposit release
\# &lt;/weight&gt;
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
Release the provided name from its owner.

The origin must be the owner of the specified name.

Emits `Web3NameReleased` if the operation is carried out
successfully.

\# &lt;weight&gt;
Weight: O(1)
- Reads: Names storage entry + origin check
- Writes: Names, Owner storage entries + currency deposit release
\# &lt;/weight&gt;
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
Unban a name.

Make a name claimable again.

The origin must be the ban origin.

Emits `Web3NameUnbanned` if the operation is carried out
successfully.

\# &lt;weight&gt;
Weight: O(1)
- Reads: Banned storage entry + origin check
- Writes: Banned storage entry deposit release
\# &lt;/weight&gt;
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
Updates the deposit amount to the current deposit rate.

The sender must be the deposit owner.
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
### InsufficientFunds
The tx submitter does not have enough funds to pay for the deposit.

---------
### InvalidWeb3NameCharacter
A name that contains not allowed characters is being claimed.

---------
### NotAuthorized
The actor cannot performed the specified operation.

---------
### OwnerAlreadyExists
The specified owner already owns a name.

---------
### OwnerNotFound
The specified owner does not own any names.

---------
### Unauthorized
The origin was not authorized to perform that action

---------
### Web3NameAlreadyBanned
The specified name has already been previously banned.

---------
### Web3NameAlreadyClaimed
The specified name has already been previously claimed.

---------
### Web3NameBanned
The specified name has been banned and cannot be interacted
with.

---------
### Web3NameNotBanned
The specified name is not currently banned.

---------
### Web3NameNotFound
The specified name does not exist.

---------
### Web3NameTooLong
A name that is too long is being claimed.

---------
### Web3NameTooShort
A name that is too short is being claimed.

---------