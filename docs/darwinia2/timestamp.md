
# Timestamp

---------
## Calls

---------
### set
See [`Pallet::set`].
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
 Did the timestamp get updated in this block?

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
 Current time for the current block.

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
 The minimum period between blocks. Beware that this is different to the *expected*
 period that the block production apparatus provides. Your chosen consensus system will
 generally work with this to determine a sensible block time. e.g. For Aura, it will be
 double this period on default settings.
#### Value
```python
6000
```
#### Python
```python
constant = substrate.get_constant('Timestamp', 'MinimumPeriod')
```
---------