
# ParasShared

---------
## Storage functions

---------
### ActiveValidatorIndices
 All the validators actively participating in parachain consensus.
 Indices are into the broader validator set.

#### Python
```python
result = substrate.query(
    'ParasShared', 'ActiveValidatorIndices', []
)
```

#### Return value
```python
['u32']
```
---------
### ActiveValidatorKeys
 The parachain attestation keys of the validators actively participating in parachain consensus.
 This should be the same length as `ActiveValidatorIndices`.

#### Python
```python
result = substrate.query(
    'ParasShared', 'ActiveValidatorKeys', []
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### CurrentSessionIndex
 The current session index.

#### Python
```python
result = substrate.query(
    'ParasShared', 'CurrentSessionIndex', []
)
```

#### Return value
```python
'u32'
```
---------