
# Scheduler

---------
## Calls

---------
### cancel
Cancel an anonymously scheduled task.
#### Attributes
| Name | Type |
| -------- | -------- | 
| when | `T::BlockNumber` | 
| index | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Scheduler', 'cancel', {'index': 'u32', 'when': 'u32'}
)
```

---------
### cancel_named
Cancel a named scheduled task.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Scheduler', 'cancel_named', {'id': 'Bytes'}
)
```

---------
### schedule
Anonymously schedule a task.
#### Attributes
| Name | Type |
| -------- | -------- | 
| when | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<CallOrHashOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule', {
    'call': {
        'Hash': '[u8; 32]',
        'Value': 'Call',
    },
    'maybe_periodic': (
        None,
        ('u32', 'u32'),
    ),
    'priority': 'u8',
    'when': 'u32',
}
)
```

---------
### schedule_after
Anonymously schedule a task after a delay.

\# &lt;weight&gt;
Same as [`schedule`].
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| after | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<CallOrHashOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule_after', {
    'after': 'u32',
    'call': {
        'Hash': '[u8; 32]',
        'Value': 'Call',
    },
    'maybe_periodic': (
        None,
        ('u32', 'u32'),
    ),
    'priority': 'u8',
}
)
```

---------
### schedule_named
Schedule a named task.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `Vec<u8>` | 
| when | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<CallOrHashOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule_named', {
    'call': {
        'Hash': '[u8; 32]',
        'Value': 'Call',
    },
    'id': 'Bytes',
    'maybe_periodic': (
        None,
        ('u32', 'u32'),
    ),
    'priority': 'u8',
    'when': 'u32',
}
)
```

---------
### schedule_named_after
Schedule a named task after a delay.

\# &lt;weight&gt;
Same as [`schedule_named`](Self::schedule_named).
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `Vec<u8>` | 
| after | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<CallOrHashOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule_named_after', {
    'after': 'u32',
    'call': {
        'Hash': '[u8; 32]',
        'Value': 'Call',
    },
    'id': 'Bytes',
    'maybe_periodic': (
        None,
        ('u32', 'u32'),
    ),
    'priority': 'u8',
}
)
```

---------
## Events

---------
### CallLookupFailed
The call for the provided hash was not found so the task has been aborted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<Vec<u8>>` | ```(None, 'Bytes')```
| error | `LookupError` | ```('Unknown', 'BadFormat')```

---------
### Canceled
Canceled some task.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| when | `T::BlockNumber` | ```u32```
| index | `u32` | ```u32```

---------
### Dispatched
Dispatched some task.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<Vec<u8>>` | ```(None, 'Bytes')```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### Scheduled
Scheduled some task.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| when | `T::BlockNumber` | ```u32```
| index | `u32` | ```u32```

---------
## Storage functions

---------
### Agenda
 Items to be executed, indexed by the block number that they should be executed on.

#### Python
```python
result = substrate.query(
    'Scheduler', 'Agenda', ['u32']
)
```

#### Return value
```python
[
    (
        None,
        {
            'call': {'Hash': '[u8; 32]', 'Value': 'Call'},
            'maybe_id': (None, 'Bytes'),
            'maybe_periodic': (None, ('u32', 'u32')),
            'origin': {
                'CumulusXcm': {'Relay': None, 'SiblingParachain': 'u32'},
                'PolkadotXcm': {
                    'Response': 'scale_info::62',
                    'Xcm': 'scale_info::62',
                },
                'TechnicalCommittee': {
                    'Member': 'AccountId',
                    'Members': ('u32', 'u32'),
                    '_Phantom': None,
                },
                'Void': (),
                'system': {'None': None, 'Root': None, 'Signed': 'AccountId'},
                None: None,
            },
            'priority': 'u8',
        },
    ),
]
```
---------
### Lookup
 Lookup from identity to the block number and index of the task.

#### Python
```python
result = substrate.query(
    'Scheduler', 'Lookup', ['Bytes']
)
```

#### Return value
```python
('u32', 'u32')
```
---------
## Constants

---------
### MaxScheduledPerBlock
 The maximum number of scheduled calls in the queue for a single block.
 Not strictly enforced, but used for weight estimation.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('Scheduler', 'MaxScheduledPerBlock')
```
---------
### MaximumWeight
 The maximum weight that may be scheduled per block for any dispatchables of less
 priority than `schedule::HARD_DEADLINE`.
#### Value
```python
400000000000
```
#### Python
```python
constant = substrate.get_constant('Scheduler', 'MaximumWeight')
```
---------
## Errors

---------
### FailedToSchedule
Failed to schedule a call

---------
### NotFound
Cannot find the scheduled call.

---------
### RescheduleNoChange
Reschedule failed because it does not change scheduled time.

---------
### TargetBlockNumberInPast
Given target block number is in the past.

---------