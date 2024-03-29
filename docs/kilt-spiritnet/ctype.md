
# Ctype

---------
## Calls

---------
### add
See [`Pallet::add`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| ctype | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Ctype', 'add', {'ctype': 'Bytes'}
)
```

---------
### set_block_number
See [`Pallet::set_block_number`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| ctype_hash | `CtypeHashOf<T>` | 
| block_number | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Ctype', 'set_block_number', {
    'block_number': 'u64',
    'ctype_hash': 'scale_info::12',
}
)
```

---------
## Events

---------
### CTypeCreated
A new CType has been created.
\[creator identifier, CType hash\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CtypeCreatorOf<T>` | ```AccountId```
| None | `CtypeHashOf<T>` | ```scale_info::12```

---------
### CTypeUpdated
Information about a CType has been updated.
\[CType hash\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CtypeHashOf<T>` | ```scale_info::12```

---------
## Storage functions

---------
### Ctypes
 CTypes stored on chain.

 It maps from a CType hash to its creator and block number in which it
 was created.

#### Python
```python
result = substrate.query(
    'Ctype', 'Ctypes', ['scale_info::12']
)
```

#### Return value
```python
{'created_at': 'u64', 'creator': 'AccountId'}
```
---------
## Errors

---------
### AlreadyExists
The CType already exists.

---------
### NotFound
There is no CType with the given hash.

---------
### UnableToPayFees
The paying account was unable to pay the fees for creating a ctype.

---------