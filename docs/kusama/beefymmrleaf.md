
# BeefyMmrLeaf

---------
## Storage functions

---------
### BeefyAuthorities
 Details of current BEEFY authority set.

#### Python
```python
result = substrate.query(
    'BeefyMmrLeaf', 'BeefyAuthorities', []
)
```

#### Return value
```python
{'id': 'u64', 'keyset_commitment': 'scale_info::12', 'len': 'u32'}
```
---------
### BeefyNextAuthorities
 Details of next BEEFY authority set.

 This storage entry is used as cache for calls to `update_beefy_next_authority_set`.

#### Python
```python
result = substrate.query(
    'BeefyMmrLeaf', 'BeefyNextAuthorities', []
)
```

#### Return value
```python
{'id': 'u64', 'keyset_commitment': 'scale_info::12', 'len': 'u32'}
```
---------