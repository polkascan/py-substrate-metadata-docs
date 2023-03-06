
# EthereumChainId

---------
## Calls

---------
### set_chain_id
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_chain_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'EthereumChainId', 'set_chain_id', {'new_chain_id': 'u64'}
)
```

---------
## Storage functions

---------
### ChainId

#### Python
```python
result = substrate.query(
    'EthereumChainId', 'ChainId', []
)
```

#### Return value
```python
'u64'
```
---------