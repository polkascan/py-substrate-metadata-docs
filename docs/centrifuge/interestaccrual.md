
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
### Rates

#### Python
```python
result = substrate.query(
    'InterestAccrual', 'Rates', []
)
```

#### Return value
```python
[
    {
        'accumulated_rate': 'u128',
        'interest_rate_per_sec': 'u128',
        'reference_count': 'u32',
    },
]
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
### TooManyRates
Emits when adding a new rate would exceed the storage limits

---------