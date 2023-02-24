
# Datalog

---------
## Calls

---------
### erase
Clear account datalog.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Datalog', 'erase', {}
)
```

---------
### record
Store new data into blockchain.
#### Attributes
| Name | Type |
| -------- | -------- | 
| record | `T::Record` | 

#### Python
```python
call = substrate.compose_call(
    'Datalog', 'record', {'record': 'Bytes'}
)
```

---------
## Events

---------
### Erased
Account datalog erased.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### NewRecord
New data added.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `<T::Time as Time>::Moment` | ```u64```
| None | `T::Record` | ```Bytes```

---------
## Storage functions

---------
### DatalogIndex
 Ringbuffer start/end pointers

#### Python
```python
result = substrate.query(
    'Datalog', 'DatalogIndex', ['AccountId']
)
```

#### Return value
```python
{'end': 'u64', 'start': 'u64'}
```
---------
### DatalogItem
 Ringbuffer items

#### Python
```python
result = substrate.query(
    'Datalog', 'DatalogItem', [('AccountId', 'u64')]
)
```

#### Return value
```python
('u64', 'Bytes')
```
---------
## Constants

---------
### WindowSize
 Data log window size
#### Value
```python
128
```
#### Python
```python
constant = substrate.get_constant('Datalog', 'WindowSize')
```
---------
## Errors

---------
### RecordTooBig
Data exceeds size limit

---------