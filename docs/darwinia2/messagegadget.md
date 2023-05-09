
# MessageGadget

---------
## Calls

---------
### set_commitment_contract
#### Attributes
| Name | Type |
| -------- | -------- | 
| commitment_contract | `H160` | 

#### Python
```python
call = substrate.compose_call(
    'MessageGadget', 'set_commitment_contract', {'commitment_contract': '[u8; 20]'}
)
```

---------
## Storage functions

---------
### CommitmentContract

#### Python
```python
result = substrate.query(
    'MessageGadget', 'CommitmentContract', []
)
```

#### Return value
```python
'[u8; 20]'
```
---------