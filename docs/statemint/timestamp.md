
# Timestamp

---------
## Calls

---------
### set
Set the current time.

This call should be invoked exactly once per block. It will panic at the finalization
phase, if this call hasn&\#x27;t been invoked by that time.

The timestamp should be greater than the previous one by the amount specified by
`MinimumPeriod`.

The dispatch origin for this call must be `Inherent`.

\#\# Complexity
- `O(1)` (Note that implementations of `OnTimestampSet` must also be `O(1)`)
- 1 storage read and 1 storage mutation (codec `O(1)`). (because of `DidUpdate::take` in
  `on_finalize`)
- 1 event handler `on_timestamp_set`. Must be `O(1)`.
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