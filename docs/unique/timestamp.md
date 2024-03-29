
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
 Whether the timestamp has been updated in this block.

 This value is updated to `true` upon successful submission of a timestamp by a node.
 It is then checked at the end of each block execution in the `on_finalize` hook.

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
 The current time for the current block.

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
 The minimum period between blocks.

 Be aware that this is different to the *expected* period that the block production
 apparatus provides. Your chosen consensus system will generally work with this to
 determine a sensible block time. For example, in the Aura pallet it will be double this
 period on default settings.
#### Value
```python
6000
```
#### Python
```python
constant = substrate.get_constant('Timestamp', 'MinimumPeriod')
```
---------