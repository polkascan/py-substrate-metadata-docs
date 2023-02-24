
# SimpleInflation

---------
## Calls

---------
### set_issuing_amount
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'SimpleInflation', 'set_issuing_amount', {'new': 'u128'}
)
```

---------
## Storage functions

---------
### IssuingAmount

#### Python
```python
result = substrate.query(
    'SimpleInflation', 'IssuingAmount', []
)
```

#### Return value
```python
'u128'
```
---------