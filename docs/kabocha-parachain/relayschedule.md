
# RelaySchedule

---------
## Calls

---------
### schedule
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'RelaySchedule', 'schedule', {'call': 'Call'}
)
```

---------
### set_at_block_number
#### Attributes
| Name | Type |
| -------- | -------- | 
| block | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'RelaySchedule', 'set_at_block_number', {'block': 'u32'}
)
```

---------
## Events

---------
### AddedCall
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `<T as Config>::Call` | ```Call```

---------
### AtBlockNumberUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### Dispatched
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `<T as Config>::Call` | ```Call```
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
## Storage functions

---------
### AtBlockNumber

#### Python
```python
result = substrate.query(
    'RelaySchedule', 'AtBlockNumber', []
)
```

#### Return value
```python
'u32'
```
---------
### Calls

#### Python
```python
result = substrate.query(
    'RelaySchedule', 'Calls', []
)
```

#### Return value
```python
['Call']
```
---------
### CurrentBlock

#### Python
```python
result = substrate.query(
    'RelaySchedule', 'CurrentBlock', []
)
```

#### Return value
```python
'u32'
```
---------