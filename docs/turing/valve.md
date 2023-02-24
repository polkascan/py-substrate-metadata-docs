
# Valve

---------
## Calls

---------
### close_pallet_gate
Close the pallet&\#x27;s gate.

Stop the pallet from receiving transactions.
If valve is closed you cannot close a pallet.
You cannot close this pallet, as then you could never open it.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pallet_name | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Valve', 'close_pallet_gate', {'pallet_name': 'Bytes'}
)
```

---------
### close_valve
Close the valve.

This will stop all the pallets defined in `ClosedCallFilter` from receiving transactions.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Valve', 'close_valve', {}
)
```

---------
### open_pallet_gate
Open the pallet.

This allows the pallet to receiving transactions.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pallet_name | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Valve', 'open_pallet_gate', {'pallet_name': 'Bytes'}
)
```

---------
### open_pallet_gates
Open the pallet gates.

In order to ensure this call is safe it will only open five gates at once.
It will send the PalletGatesClosed with a count of how many gates are still closed.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Valve', 'open_pallet_gates', {}
)
```

---------
### open_valve
Return the chain to normal operating mode.

This will open the valve but not any closed pallet gates.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Valve', 'open_valve', {}
)
```

---------
### start_price_automation_tasks
Allow scheduled tasks to run again.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Valve', 'start_price_automation_tasks', {}
)
```

---------
### start_scheduled_tasks
Allow scheduled tasks to run again.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Valve', 'start_scheduled_tasks', {}
)
```

---------
### stop_price_automation_tasks
Stop all scheduled tasks from running.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Valve', 'stop_price_automation_tasks', {}
)
```

---------
### stop_scheduled_tasks
Stop all scheduled tasks from running.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Valve', 'stop_scheduled_tasks', {}
)
```

---------
## Events

---------
### PalletGateClosed
The pallet gate has been closed. It can no longer recieve transactions.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pallet_name_bytes | `Vec<u8>` | ```Bytes```

---------
### PalletGateOpen
The pallet gate has been opened. It will now start receiving transactions.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pallet_name_bytes | `Vec<u8>` | ```Bytes```

---------
### PalletGatesClosed
The number of pallet gates still closed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| count | `u8` | ```u8```

---------
### ScheduledTasksResumed
Scheduled tasks will now start running.
#### Attributes
No attributes

---------
### ScheduledTasksStopped
Scheduled tasks are now longer being run.
#### Attributes
No attributes

---------
### ValveClosed
The valve has been closed. This has stopped transactions to non-critical pallets.
#### Attributes
No attributes

---------
### ValveOpen
The chain returned to its normal operating state.
#### Attributes
No attributes

---------
## Storage functions

---------
### ClosedPalletCount
 The closed pallet map. Each pallet in here will not receive transcations.

#### Python
```python
result = substrate.query(
    'Valve', 'ClosedPalletCount', []
)
```

#### Return value
```python
'u8'
```
---------
### ClosedPallets
 The closed pallet map. Each pallet in here will not receive transcations.

#### Python
```python
result = substrate.query(
    'Valve', 'ClosedPallets', ['Bytes']
)
```

#### Return value
```python
()
```
---------
### ValveClosed
 Whether the valve is closed.

#### Python
```python
result = substrate.query(
    'Valve', 'ValveClosed', []
)
```

#### Return value
```python
'bool'
```
---------
## Errors

---------
### CannotCloseGate
The valve pallet gate cannot be closed.

---------
### InvalidCharacter
Invalid character encoding.

---------
### NotAllowed
The user is not allowed to call the extrinsic.

---------
### ScheduledTasksAlreadyRunnung
Scheduled tasks are already running.

---------
### ScheduledTasksAlreadyStopped
Scheduled tasks have already been stopped.

---------
### ValveAlreadyClosed
The valve is already closed.

---------
### ValveAlreadyOpen
The valve is already open.

---------