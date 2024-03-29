
# MessageQueue

---------
## Calls

---------
### execute_overweight
See [`Pallet::execute_overweight`].
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
See [`Pallet::reap_page`].
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
Message placed in overweight queue.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `[u8; 32]` | ```[u8; 32]```
| origin | `MessageOriginOf<T>` | ```{'Here': None, 'Parent': None, 'Sibling': 'u32'}```
| page_index | `PageIndex` | ```u32```
| message_index | `T::Size` | ```u32```

---------
### PageReaped
This page was reaped.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| origin | `MessageOriginOf<T>` | ```{'Here': None, 'Parent': None, 'Sibling': 'u32'}```
| index | `PageIndex` | ```u32```

---------
### Processed
Message is processed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `H256` | ```scale_info::12```
| origin | `MessageOriginOf<T>` | ```{'Here': None, 'Parent': None, 'Sibling': 'u32'}```
| weight_used | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```
| success | `bool` | ```bool```

---------
### ProcessingFailed
Message discarded due to an error in the `MessageProcessor` (usually a format error).
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
 The index of the first and last (non-empty) pages.

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
 The map of page indices to pages.

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
 The origin at which we should begin servicing.

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
 The size of the page; this implies the maximum message size which can be sent.

 A good value depends on the expected message sizes, their weights, the weight that is
 available for processing them and the maximal needed message size. The maximal message
 size is slightly lower than this as defined by [`MaxMessageLenOf`].
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
 The maximum number of stale pages (i.e. of overweight messages) allowed before culling
 can happen. Once there are more stale pages than this, then historical pages may be
 dropped, even if they contain unprocessed overweight messages.
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
 The amount of weight (if any) which should be provided to the message queue for
 servicing enqueued items.

 This may be legitimately `None` in the case that you will call
 `ServiceQueues::service_queues` manually.
#### Value
```python
{'proof_size': 1835008, 'ref_time': 175000000000}
```
#### Python
```python
constant = substrate.get_constant('MessageQueue', 'ServiceWeight')
```
---------
## Errors

---------
### AlreadyProcessed
The message was already processed and cannot be processed again.

---------
### InsufficientWeight
There is temporarily not enough weight to continue servicing messages.

---------
### NoMessage
The referenced message could not be found.

---------
### NoPage
Page to be reaped does not exist.

---------
### NotReapable
Page is not reapable because it has items remaining to be processed and is not old
enough.

---------
### QueuePaused
The queue is paused and no message can be executed from it.

This can change at any time and may resolve in the future by re-trying.

---------
### Queued
The message is queued for future execution.

---------
### RecursiveDisallowed
Another call is in progress and needs to finish before this call can happen.

---------
### TemporarilyUnprocessable
This message is temporarily unprocessable.

Such errors are expected, but not guaranteed, to resolve themselves eventually through
retrying.

---------