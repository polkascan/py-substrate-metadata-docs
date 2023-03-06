
# AuthorityDiscovery

---------
## Storage functions

---------
### Keys
 Keys of the current authority set.

#### Python
```python
result = substrate.query(
    'AuthorityDiscovery', 'Keys', []
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### NextKeys
 Keys of the next authority set.

#### Python
```python
result = substrate.query(
    'AuthorityDiscovery', 'NextKeys', []
)
```

#### Return value
```python
['[u8; 32]']
```
---------