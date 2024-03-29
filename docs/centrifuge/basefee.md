
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
    'BaseFee', 'set_base_fee_per_gas', {'fee': 'scale_info::131'}
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
| fee | `U256` | ```scale_info::131```

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
'scale_info::131'
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