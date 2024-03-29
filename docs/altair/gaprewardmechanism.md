
# GapRewardMechanism

---------
## Storage functions

---------
### LastDistributionId

#### Python
```python
result = substrate.query(
    'GapRewardMechanism', 'LastDistributionId', []
)
```

#### Return value
```python
'u32'
```
---------
### RptHistory

#### Python
```python
result = substrate.query(
    'GapRewardMechanism', 'RptHistory', ['u32']
)
```

#### Return value
```python
'i128'
```
---------
## Errors

---------
### TryMovementAfterPendingState

---------