
# EqAggregates

---------
## Storage functions

---------
### AccountUserGroups

#### Python
```python
result = substrate.query(
    'EqAggregates', 'AccountUserGroups', [('Balances', 'Bailsmen', 'Borrowers'), 'AccountId']
)
```

#### Return value
```python
'bool'
```
---------
### TotalUserGroups
 Pallet storage - stores aggregates for each user group

#### Python
```python
result = substrate.query(
    'EqAggregates', 'TotalUserGroups', [('Balances', 'Bailsmen', 'Borrowers'), 'u64']
)
```

#### Return value
```python
{'collateral': 'u128', 'debt': 'u128'}
```
---------