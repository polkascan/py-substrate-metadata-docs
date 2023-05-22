
# Scheduler

---------
## Calls

---------
### cancel
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
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `TaskName` | 

#### Python
```python
call = substrate.compose_call(
    'Scheduler', 'cancel_named', {'id': '[u8; 32]'}
)
```

---------
### schedule
#### Attributes
| Name | Type |
| -------- | -------- | 
| when | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule', {
    'call': 'Call',
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
#### Attributes
| Name | Type |
| -------- | -------- | 
| after | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule_after', {
    'after': 'u32',
    'call': 'Call',
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
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `TaskName` | 
| when | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule_named', {
    'call': 'Call',
    'id': '[u8; 32]',
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
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `TaskName` | 
| after | `T::BlockNumber` | 
| maybe_periodic | `Option<schedule::Period<T::BlockNumber>>` | 
| priority | `schedule::Priority` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Scheduler', 'schedule_named_after', {
    'after': 'u32',
    'call': 'Call',
    'id': '[u8; 32]',
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
### CallUnavailable
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<TaskName>` | ```(None, '[u8; 32]')```

---------
### Canceled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| when | `T::BlockNumber` | ```u32```
| index | `u32` | ```u32```

---------
### Dispatched
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<TaskName>` | ```(None, '[u8; 32]')```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### PeriodicFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<TaskName>` | ```(None, '[u8; 32]')```

---------
### PermanentlyOverweight
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task | `TaskAddress<T::BlockNumber>` | ```('u32', 'u32')```
| id | `Option<TaskName>` | ```(None, '[u8; 32]')```

---------
### Scheduled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| when | `T::BlockNumber` | ```u32```
| index | `u32` | ```u32```

---------
## Storage functions

---------
### Agenda

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
            'call': {
                'Inline': 'Bytes',
                'Legacy': {'hash': '[u8; 32]'},
                'Lookup': {'hash': '[u8; 32]', 'len': 'u32'},
            },
            'maybe_id': (None, '[u8; 32]'),
            'maybe_periodic': (None, ('u32', 'u32')),
            'origin': {
                'Authority': {'delay': 'u32', 'origin': 'scale_info::114'},
                None: None,
                'CumulusXcm': {'Relay': None, 'SiblingParachain': 'u32'},
                'FinancialCouncil': {
                    'Member': 'AccountId',
                    'Members': ('u32', 'u32'),
                    '_Phantom': None,
                },
                'GeneralCouncil': {
                    'Member': 'AccountId',
                    'Members': ('u32', 'u32'),
                    '_Phantom': None,
                },
                'HomaCouncil': {
                    'Member': 'AccountId',
                    'Members': ('u32', 'u32'),
                    '_Phantom': None,
                },
                'PolkadotXcm': {
                    'Response': 'scale_info::74',
                    'Xcm': 'scale_info::74',
                },
                'TechnicalCommittee': {
                    'Member': 'AccountId',
                    'Members': ('u32', 'u32'),
                    '_Phantom': None,
                },
                'Void': (),
                'system': {'None': None, 'Root': None, 'Signed': 'AccountId'},
            },
            'priority': 'u8',
        },
    ),
]
```
---------
### IncompleteSince

#### Python
```python
result = substrate.query(
    'Scheduler', 'IncompleteSince', []
)
```

#### Return value
```python
'u32'
```
---------
### Lookup

#### Python
```python
result = substrate.query(
    'Scheduler', 'Lookup', ['[u8; 32]']
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
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Scheduler', 'MaxScheduledPerBlock')
```
---------
### MaximumWeight
#### Value
```python
{'proof_size': 4194304, 'ref_time': 400000000000}
```
#### Python
```python
constant = substrate.get_constant('Scheduler', 'MaximumWeight')
```
---------
## Errors

---------
### FailedToSchedule

---------
### Named

---------
### NotFound

---------
### RescheduleNoChange

---------
### TargetBlockNumberInPast

---------