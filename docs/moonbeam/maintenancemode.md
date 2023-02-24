
# MaintenanceMode

---------
## Calls

---------
### enter_maintenance_mode
Place the chain in maintenance mode

Weight cost is:
* One DB read to ensure we&\#x27;re not already in maintenance mode
* Three DB writes - 1 for the mode, 1 for suspending xcm execution, 1 for the event
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
Return the chain to normal operating mode

Weight cost is:
* One DB read to ensure we&\#x27;re in maintenance mode
* Three DB writes - 1 for the mode, 1 for resuming xcm execution, 1 for the event
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
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
### FailedToSuspendIdleXcmExecution
The call to suspend on_idle XCM execution failed with inner error
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

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