
# BaseFee

---------
## Calls

---------
### set_base_fee_per_gas
#### Attributes
| Name | Type |
| -------- | -------- | 
| fee | `U256` | 

#### Python
```python
call = substrate.compose_call(
    'BaseFee', 'set_base_fee_per_gas', {'fee': '[u64; 4]'}
)
```

---------
### set_elasticity
#### Attributes
| Name | Type |
| -------- | -------- | 
| elasticity | `Permill` | 

#### Python
```python
call = substrate.compose_call(
    'BaseFee', 'set_elasticity', {'elasticity': 'u32'}
)
```

---------
## Events

---------
### BaseFeeOverflow
#### Attributes
No attributes

---------
### NewBaseFeePerGas
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| fee | `U256` | ```[u64; 4]```

---------
### NewElasticity
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| elasticity | `Permill` | ```u32```

---------
## Storage functions

---------
### BaseFeePerGas

#### Python
```python
result = substrate.query(
    'BaseFee', 'BaseFeePerGas', []
)
```

#### Return value
```python
'[u64; 4]'
```
---------
### Elasticity

#### Python
```python
result = substrate.query(
    'BaseFee', 'Elasticity', []
)
```

#### Return value
```python
'u32'
```
---------