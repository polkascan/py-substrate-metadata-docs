
# Configuration

---------
## Calls

---------
### set_min_gas_price_override
#### Attributes
| Name | Type |
| -------- | -------- | 
| coeff | `Option<u64>` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_min_gas_price_override', {'coeff': (None, 'u64')}
)
```

---------
### set_weight_to_fee_coefficient_override
#### Attributes
| Name | Type |
| -------- | -------- | 
| coeff | `Option<u32>` | 

#### Python
```python
call = substrate.compose_call(
    'Configuration', 'set_weight_to_fee_coefficient_override', {'coeff': (None, 'u32')}
)
```

---------
## Storage functions

---------
### MinGasPriceOverride

#### Python
```python
result = substrate.query(
    'Configuration', 'MinGasPriceOverride', []
)
```

#### Return value
```python
'u64'
```
---------
### WeightToFeeCoefficientOverride

#### Python
```python
result = substrate.query(
    'Configuration', 'WeightToFeeCoefficientOverride', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### DefaultMinGasPrice
#### Value
```python
1019483274941
```
#### Python
```python
constant = substrate.get_constant('Configuration', 'DefaultMinGasPrice')
```
---------
### DefaultWeightToFeeCoefficient
#### Value
```python
207163598
```
#### Python
```python
constant = substrate.get_constant('Configuration', 'DefaultWeightToFeeCoefficient')
```
---------