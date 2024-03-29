
# AuthorMapping

---------
## Calls

---------
### add_association
See [`Pallet::add_association`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| nimbus_id | `NimbusId` | 

#### Python
```python
call = substrate.compose_call(
    'AuthorMapping', 'add_association', {'nimbus_id': '[u8; 32]'}
)
```

---------
### clear_association
See [`Pallet::clear_association`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| nimbus_id | `NimbusId` | 

#### Python
```python
call = substrate.compose_call(
    'AuthorMapping', 'clear_association', {'nimbus_id': '[u8; 32]'}
)
```

---------
### remove_keys
See [`Pallet::remove_keys`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'AuthorMapping', 'remove_keys', {}
)
```

---------
### set_keys
See [`Pallet::set_keys`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| keys | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'AuthorMapping', 'set_keys', {'keys': 'Bytes'}
)
```

---------
### update_association
See [`Pallet::update_association`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| old_nimbus_id | `NimbusId` | 
| new_nimbus_id | `NimbusId` | 

#### Python
```python
call = substrate.compose_call(
    'AuthorMapping', 'update_association', {
    'new_nimbus_id': '[u8; 32]',
    'old_nimbus_id': '[u8; 32]',
}
)
```

---------
## Events

---------
### KeysRegistered
A NimbusId has been registered and mapped to an AccountId.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| nimbus_id | `NimbusId` | ```[u8; 32]```
| account_id | `T::AccountId` | ```[u8; 20]```
| keys | `T::Keys` | ```[u8; 32]```

---------
### KeysRemoved
An NimbusId has been de-registered, and its AccountId mapping removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| nimbus_id | `NimbusId` | ```[u8; 32]```
| account_id | `T::AccountId` | ```[u8; 20]```
| keys | `T::Keys` | ```[u8; 32]```

---------
### KeysRotated
An NimbusId has been registered, replacing a previous registration and its mapping.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| new_nimbus_id | `NimbusId` | ```[u8; 32]```
| account_id | `T::AccountId` | ```[u8; 20]```
| new_keys | `T::Keys` | ```[u8; 32]```

---------
## Storage functions

---------
### MappingWithDeposit
 We maintain a mapping from the NimbusIds used in the consensus layer
 to the AccountIds runtime.

#### Python
```python
result = substrate.query(
    'AuthorMapping', 'MappingWithDeposit', ['[u8; 32]']
)
```

#### Return value
```python
{'account': '[u8; 20]', 'deposit': 'u128', 'keys': '[u8; 32]'}
```
---------
### NimbusLookup
 We maintain a reverse mapping from AccountIds to NimbusIDS

#### Python
```python
result = substrate.query(
    'AuthorMapping', 'NimbusLookup', ['[u8; 20]']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
## Errors

---------
### AlreadyAssociated
The NimbusId in question is already associated and cannot be overwritten

---------
### AssociationNotFound
The association can&\#x27;t be cleared because it is not found.

---------
### CannotAffordSecurityDeposit
This account cannot set an author because it cannon afford the security deposit

---------
### DecodeKeysFailed
Failed to decode T::Keys for `set_keys`

---------
### DecodeNimbusFailed
Failed to decode NimbusId for `set_keys`

---------
### NotYourAssociation
The association can&\#x27;t be cleared because it belongs to another account.

---------
### OldAuthorIdNotFound
No existing NimbusId can be found for the account

---------
### WrongKeySize
Keys have wrong size

---------