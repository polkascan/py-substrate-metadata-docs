
# GenesisHistory

---------
## Storage functions

---------
### PreviousChain

#### Python
```python
result = substrate.query(
    'GenesisHistory', 'PreviousChain', []
)
```

#### Return value
```python
{'genesis_hash': 'Bytes', 'last_block_hash': 'Bytes'}
```
---------