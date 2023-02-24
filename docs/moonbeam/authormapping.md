
# AuthorMapping

---------
## Calls

---------
### add_association
Register your NimbusId onchain so blocks you author are associated with your account.

Users who have been (or will soon be) elected active collators in staking,
should submit this extrinsic to have their blocks accepted and earn rewards.
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
Clear your Mapping.

This is useful when you are no longer an author and would like to re-claim your security
deposit.
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
Remove your Mapping.

This is useful when you are no longer an author and would like to re-claim your security
deposit.
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
Set association and session keys at once.

This is useful for key rotation to update Nimbus and VRF keys in one call.
No new security deposit is required. Will replace `update_association` which is kept
now for backwards compatibility reasons.
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
Change your Mapping.

This is useful for normal key rotation or for when switching from one physical collator
machine to another. No new security deposit is required.
This sets keys to new_nimbus_id.into() by default.
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