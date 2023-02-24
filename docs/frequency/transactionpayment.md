
# TransactionPayment

---------
## Events

---------
### TransactionFeePaid
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| actual_fee | `BalanceOf<T>` | ```u128```
| tip | `BalanceOf<T>` | ```u128```

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
### OperationalFeeMultiplier
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('TransactionPayment', 'OperationalFeeMultiplier')
```
---------