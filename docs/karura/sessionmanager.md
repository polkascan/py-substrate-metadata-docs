
# SessionManager

---------
## Calls

---------
### schedule_session_duration
#### Attributes
| Name | Type |
| -------- | -------- | 
| start_session | `SessionIndex` | 
| duration | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'SessionManager', 'schedule_session_duration', {
    'duration': 'u32',
    'start_session': 'u32',
}
)
```

---------
## Events

---------
### ScheduledSessionDuration
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| block_number | `BlockNumberFor<T>` | ```u32```
| session_index | `SessionIndex` | ```u32```
| session_duration | `BlockNumberFor<T>` | ```u32```

---------
## Storage functions

---------
### DurationOffset

#### Python
```python
result = substrate.query(
    'SessionManager', 'DurationOffset', []
)
```

#### Return value
```python
'u32'
```
---------
### SessionDuration

#### Python
```python
result = substrate.query(
    'SessionManager', 'SessionDuration', []
)
```

#### Return value
```python
'u32'
```
---------
### SessionDurationChanges

#### Python
```python
result = substrate.query(
    'SessionManager', 'SessionDurationChanges', ['u32']
)
```

#### Return value
```python
('u32', 'u32')
```
---------
## Errors

---------
### EstimateNextSessionFailed

---------
### InvalidDuration

---------
### InvalidSession

---------