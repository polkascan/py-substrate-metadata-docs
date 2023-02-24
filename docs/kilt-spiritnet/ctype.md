
# Ctype

---------
## Calls

---------
### add
Create a new CType from the given unique CType hash and associates
it with its creator.

A CType with the same hash must not be stored on chain.

Emits `CTypeCreated`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: Ctypes, Balance
- Writes: Ctypes, Balance
\# &lt;/weight&gt;
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
Set the creation block number for a given CType, if found.

Emits `CTypeUpdated`.
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
    'ctype_hash': '[u8; 32]',
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
| None | `CtypeHashOf<T>` | ```[u8; 32]```

---------
### CTypeUpdated
Information about a CType has been updated.
\[CType hash\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CtypeHashOf<T>` | ```[u8; 32]```

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
    'Ctype', 'Ctypes', ['[u8; 32]']
)
```

#### Return value
```python
{'created_at': 'u64', 'creator': 'AccountId'}
```
---------
## Errors

---------
### CTypeAlreadyExists
The CType already exists.

---------
### CTypeNotFound
There is no CType with the given hash.

---------
### UnableToPayFees
The paying account was unable to pay the fees for creating a ctype.

---------