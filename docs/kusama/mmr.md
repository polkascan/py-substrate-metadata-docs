
# Mmr

---------
## Storage functions

---------
### Nodes
 Hashes of the nodes in the MMR.

 Note this collection only contains MMR peaks, the inner nodes (and leaves)
 are pruned and only stored in the Offchain DB.

#### Python
```python
result = substrate.query(
    'Mmr', 'Nodes', ['u64']
)
```

#### Return value
```python
'scale_info::12'
```
---------
### NumberOfLeaves
 Current size of the MMR (number of leaves).

#### Python
```python
result = substrate.query(
    'Mmr', 'NumberOfLeaves', []
)
```

#### Return value
```python
'u64'
```
---------
### RootHash
 Latest MMR Root hash.

#### Python
```python
result = substrate.query(
    'Mmr', 'RootHash', []
)
```

#### Return value
```python
'scale_info::12'
```
---------