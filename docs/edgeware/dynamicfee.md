
# DynamicFee

---------
## Calls

---------
### note_min_gas_price_target
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `U256` | 

#### Python
```python
call = substrate.compose_call(
    'DynamicFee', 'note_min_gas_price_target', {'target': '[u64; 4]'}
)
```

---------
## Storage functions

---------
### MinGasPrice

#### Python
```python
result = substrate.query(
    'DynamicFee', 'MinGasPrice', []
)
```

#### Return value
```python
'[u64; 4]'
```
---------
### TargetMinGasPrice

#### Python
```python
result = substrate.query(
    'DynamicFee', 'TargetMinGasPrice', []
)
```

#### Return value
```python
'[u64; 4]'
```
---------