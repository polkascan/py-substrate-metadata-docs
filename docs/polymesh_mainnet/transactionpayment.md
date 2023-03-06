
# TransactionPayment

---------
## Storage functions

---------
### NextFeeMultiplier

#### Python
```python
result = substrate.query(
    'TransactionPayment', 'NextFeeMultiplier', []
)
```

#### Return value
```python
'u128'
```
---------
### StorageVersion

#### Python
```python
result = substrate.query(
    'TransactionPayment', 'StorageVersion', []
)
```

#### Return value
```python
('V1Ancient', 'V2')
```
---------
## Constants

---------
### TransactionByteFee
 The fee to be paid for making a transaction; the per-byte portion.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('TransactionPayment', 'TransactionByteFee')
```
---------
### WeightToFee
 The polynomial that is applied in order to derive fee from weight.
#### Value
```python
[{'coeff_frac': 46153, 'coeff_integer': 0, 'degree': 1, 'negative': False}]
```
#### Python
```python
constant = substrate.get_constant('TransactionPayment', 'WeightToFee')
```
---------