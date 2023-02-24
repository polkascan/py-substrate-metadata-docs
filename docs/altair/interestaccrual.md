
# InterestAccrual

---------
## Storage functions

---------
### LastUpdated

#### Python
```python
result = substrate.query(
    'InterestAccrual', 'LastUpdated', []
)
```

#### Return value
```python
'u64'
```
---------
### Rate

#### Python
```python
result = substrate.query(
    'InterestAccrual', 'Rate', ['u128']
)
```

#### Return value
```python
{'accumulated_rate': 'u128', 'reference_count': 'u32'}
```
---------
### RateCount

#### Python
```python
result = substrate.query(
    'InterestAccrual', 'RateCount', []
)
```

#### Return value
```python
'u32'
```
---------
### StorageVersion

#### Python
```python
result = substrate.query(
    'InterestAccrual', 'StorageVersion', []
)
```

#### Return value
```python
('V0', 'V1', 'V2')
```
---------
## Errors

---------
### DebtAdjustmentFailed
Emits when the debt adjustment failed

---------
### DebtCalculationFailed
Emits when the debt calculation failed

---------
### InvalidRate
Emits when a rate is not within the valid range

---------
### NoSuchRate
Emits when the interest rate was not used

---------
### NotInPast
Emits when a historic rate was asked for from the future

---------
### TooManyRates
Emits when adding a new rate would exceed the storage limits

---------