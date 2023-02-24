
# AuthorFilter

---------
## Calls

---------
### set_eligible
Update the eligible count. Intended to be called by governance.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `EligibilityValue` | 

#### Python
```python
call = substrate.compose_call(
    'AuthorFilter', 'set_eligible', {'new': 'u32'}
)
```

---------
## Events

---------
### EligibleUpdated
The amount of eligible authors for the filter to select has been changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EligibilityValue` | ```u32```

---------
## Storage functions

---------
### EligibleCount
 The number of active authors that will be eligible at each height.

#### Python
```python
result = substrate.query(
    'AuthorFilter', 'EligibleCount', []
)
```

#### Return value
```python
'u32'
```
---------
### EligibleRatio

#### Python
```python
result = substrate.query(
    'AuthorFilter', 'EligibleRatio', []
)
```

#### Return value
```python
'u8'
```
---------