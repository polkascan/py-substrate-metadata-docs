
# FeesSplit

---------
## Calls

---------
### set_treasury_cut_percent
#### Attributes
| Name | Type |
| -------- | -------- | 
| val | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'FeesSplit', 'set_treasury_cut_percent', {'val': 'u32'}
)
```

---------
## Storage functions

---------
### TreasuryCutPercent

#### Python
```python
result = substrate.query(
    'FeesSplit', 'TreasuryCutPercent', []
)
```

#### Return value
```python
'u32'
```
---------