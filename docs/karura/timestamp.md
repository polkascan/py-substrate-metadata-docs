
# Timestamp

---------
## Calls

---------
### set
#### Attributes
| Name | Type |
| -------- | -------- | 
| now | `T::Moment` | 

#### Python
```python
call = substrate.compose_call(
    'Timestamp', 'set', {'now': 'u64'}
)
```

---------
## Storage functions

---------
### DidUpdate

#### Python
```python
result = substrate.query(
    'Timestamp', 'DidUpdate', []
)
```

#### Return value
```python
'bool'
```
---------
### Now

#### Python
```python
result = substrate.query(
    'Timestamp', 'Now', []
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### MinimumPeriod
#### Value
```python
6000
```
#### Python
```python
constant = substrate.get_constant('Timestamp', 'MinimumPeriod')
```
---------