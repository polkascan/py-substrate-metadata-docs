
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
    'BaseFee', 'set_base_fee_per_gas', {'fee': 'scale_info::55'}
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
### set_is_active
#### Attributes
| Name | Type |
| -------- | -------- | 
| is_active | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'BaseFee', 'set_is_active', {'is_active': 'bool'}
)
```

---------
## Events

---------
### BaseFeeOverflow
#### Attributes
No attributes

---------
### IsActive
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `bool` | ```bool```

---------
### NewBaseFeePerGas
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `U256` | ```scale_info::55```

---------
### NewElasticity
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Permill` | ```u32```

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
'scale_info::55'
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
### IsActive

#### Python
```python
result = substrate.query(
    'BaseFee', 'IsActive', []
)
```

#### Return value
```python
'bool'
```
---------