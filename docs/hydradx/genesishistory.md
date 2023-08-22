
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
{'genesis_hash': '[u8; 32]', 'last_block_hash': '[u8; 32]'}
```
---------