
# Indices

---------
## Calls

---------
### claim
See [`Pallet::claim`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `T::AccountIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Indices', 'claim', {'index': 'u32'}
)
```

---------
### force_transfer
See [`Pallet::force_transfer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `AccountIdLookupOf<T>` | 
| index | `T::AccountIndex` | 
| freeze | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Indices', 'force_transfer', {
    'freeze': 'bool',
    'index': 'u32',
    'new': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### free
See [`Pallet::free`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `T::AccountIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Indices', 'free', {'index': 'u32'}
)
```

---------
### freeze
See [`Pallet::freeze`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `T::AccountIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Indices', 'freeze', {'index': 'u32'}
)
```

---------
### transfer
See [`Pallet::transfer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `AccountIdLookupOf<T>` | 
| index | `T::AccountIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Indices', 'transfer', {
    'index': 'u32',
    'new': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
## Events

---------
### IndexAssigned
A account index was assigned.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| index | `T::AccountIndex` | ```u32```

---------
### IndexFreed
A account index has been freed up (unassigned).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `T::AccountIndex` | ```u32```

---------
### IndexFrozen
A account index has been frozen to its current account ID.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `T::AccountIndex` | ```u32```
| who | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### Accounts
 The lookup from index to account.

#### Python
```python
result = substrate.query(
    'Indices', 'Accounts', ['u32']
)
```

#### Return value
```python
('AccountId', 'u128', 'bool')
```
---------
## Constants

---------
### Deposit
 The deposit needed for reserving an index.
#### Value
```python
33333333300
```
#### Python
```python
constant = substrate.get_constant('Indices', 'Deposit')
```
---------
## Errors

---------
### InUse
The index was not available.

---------
### NotAssigned
The index was not already assigned.

---------
### NotOwner
The index is assigned to another account.

---------
### NotTransfer
The source and destination accounts are identical.

---------
### Permanent
The index is permanent and may not be freed/changed.

---------