
# Initializer

---------
## Calls

---------
### force_approve
See [`Pallet::force_approve`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| up_to | `BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Initializer', 'force_approve', {'up_to': 'u32'}
)
```

---------
## Storage functions

---------
### BufferedSessionChanges
 Buffered session changes along with the block number at which they should be applied.

 Typically this will be empty or one element long. Apart from that this item never hits
 the storage.

 However this is a `Vec` regardless to handle various edge cases that may occur at runtime
 upgrade boundaries or if governance intervenes.

#### Python
```python
result = substrate.query(
    'Initializer', 'BufferedSessionChanges', []
)
```

#### Return value
```python
[{'queued': ['[u8; 32]'], 'session_index': 'u32', 'validators': ['[u8; 32]']}]
```
---------
### HasInitialized
 Whether the parachains modules have been initialized within this block.

 Semantically a `bool`, but this guarantees it should never hit the trie,
 as this is cleared in `on_finalize` and Frame optimizes `None` values to be empty values.

 As a `bool`, `set(false)` and `remove()` both lead to the next `get()` being false, but one
 of them writes to the trie and one does not. This confusion makes `Option&lt;()&gt;` more suitable
 for the semantics of this variable.

#### Python
```python
result = substrate.query(
    'Initializer', 'HasInitialized', []
)
```

#### Return value
```python
()
```
---------