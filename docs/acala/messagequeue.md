
# MessageQueue

---------
## Calls

---------
### execute_overweight
#### Attributes
| Name | Type |
| -------- | -------- | 
| message_origin | `MessageOriginOf<T>` | 
| page | `PageIndex` | 
| index | `T::Size` | 
| weight_limit | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'MessageQueue', 'execute_overweight', {
    'index': 'u32',
    'message_origin': {
        'Here': None,
        'Parent': None,
        'Sibling': 'u32',
    },
    'page': 'u32',
    'weight_limit': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
### reap_page
#### Attributes
| Name | Type |
| -------- | -------- | 
| message_origin | `MessageOriginOf<T>` | 
| page_index | `PageIndex` | 

#### Python
```python
call = substrate.compose_call(
    'MessageQueue', 'reap_page', {
    'message_origin': {
        'Here': None,
        'Parent': None,
        'Sibling': 'u32',
    },
    'page_index': 'u32',
}
)
```

---------
## Events

---------
### OverweightEnqueued
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `[u8; 32]` | ```[u8; 32]```
| origin | `MessageOriginOf<T>` | ```{'Here': None, 'Parent': None, 'Sibling': 'u32'}```
| page_index | `PageIndex` | ```u32```
| message_index | `T::Size` | ```u32```

---------
### PageReaped
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| origin | `MessageOriginOf<T>` | ```{'Here': None, 'Parent': None, 'Sibling': 'u32'}```
| index | `PageIndex` | ```u32```

---------
### Processed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `H256` | ```scale_info::12```
| origin | `MessageOriginOf<T>` | ```{'Here': None, 'Parent': None, 'Sibling': 'u32'}```
| weight_used | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```
| success | `bool` | ```bool```

---------
### ProcessingFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `H256` | ```scale_info::12```
| origin | `MessageOriginOf<T>` | ```{'Here': None, 'Parent': None, 'Sibling': 'u32'}```
| error | `ProcessMessageError` | ```{'BadFormat': None, 'Corrupt': None, 'Unsupported': None, 'Overweight': {'ref_time': 'u64', 'proof_size': 'u64'}, 'Yield': None}```

---------
## Storage functions

---------
### BookStateFor

#### Python
```python
result = substrate.query(
    'MessageQueue', 'BookStateFor', [
    {
        'Here': None,
        'Parent': None,
        'Sibling': 'u32',
    },
]
)
```

#### Return value
```python
{
    'begin': 'u32',
    'count': 'u32',
    'end': 'u32',
    'message_count': 'u64',
    'ready_neighbours': (
        None,
        {
            'next': {'Here': None, 'Parent': None, 'Sibling': 'u32'},
            'prev': {'Here': None, 'Parent': None, 'Sibling': 'u32'},
        },
    ),
    'size': 'u64',
}
```
---------
### Pages

#### Python
```python
result = substrate.query(
    'MessageQueue', 'Pages', [
    {
        'Here': None,
        'Parent': None,
        'Sibling': 'u32',
    },
    'u32',
]
)
```

#### Return value
```python
{
    'first': 'u32',
    'first_index': 'u32',
    'heap': 'Bytes',
    'last': 'u32',
    'remaining': 'u32',
    'remaining_size': 'u32',
}
```
---------
### ServiceHead

#### Python
```python
result = substrate.query(
    'MessageQueue', 'ServiceHead', []
)
```

#### Return value
```python
{'Here': None, 'Parent': None, 'Sibling': 'u32'}
```
---------
## Constants

---------
### HeapSize
#### Value
```python
65536
```
#### Python
```python
constant = substrate.get_constant('MessageQueue', 'HeapSize')
```
---------
### MaxStale
#### Value
```python
8
```
#### Python
```python
constant = substrate.get_constant('MessageQueue', 'MaxStale')
```
---------
### ServiceWeight
#### Value
```python
{'proof_size': 18350080, 'ref_time': 175000000000}
```
#### Python
```python
constant = substrate.get_constant('MessageQueue', 'ServiceWeight')
```
---------
## Errors

---------
### AlreadyProcessed

---------
### InsufficientWeight

---------
### NoMessage

---------
### NoPage

---------
### NotReapable

---------
### QueuePaused

---------
### Queued

---------
### RecursiveDisallowed

---------
### TemporarilyUnprocessable

---------