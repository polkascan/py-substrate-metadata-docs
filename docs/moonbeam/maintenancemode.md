
# MaintenanceMode

---------
## Calls

---------
### enter_maintenance_mode
See [`Pallet::enter_maintenance_mode`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'MaintenanceMode', 'enter_maintenance_mode', {}
)
```

---------
### resume_normal_operation
See [`Pallet::resume_normal_operation`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'MaintenanceMode', 'resume_normal_operation', {}
)
```

---------
## Events

---------
### EnteredMaintenanceMode
The chain was put into Maintenance Mode
#### Attributes
No attributes

---------
### FailedToResumeIdleXcmExecution
The call to resume on_idle XCM execution failed with inner error
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}```

---------
### FailedToSuspendIdleXcmExecution
The call to suspend on_idle XCM execution failed with inner error
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}```

---------
### NormalOperationResumed
The chain returned to its normal operating state
#### Attributes
No attributes

---------
## Storage functions

---------
### MaintenanceMode
 Whether the site is in maintenance mode

#### Python
```python
result = substrate.query(
    'MaintenanceMode', 'MaintenanceMode', []
)
```

#### Return value
```python
'bool'
```
---------
## Errors

---------
### AlreadyInMaintenanceMode
The chain cannot enter maintenance mode because it is already in maintenance mode

---------
### NotInMaintenanceMode
The chain cannot resume normal operation because it is not in maintenance mode

---------