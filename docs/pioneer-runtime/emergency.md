
# Emergency

---------
## Calls

---------
### emergency_stop
#### Attributes
| Name | Type |
| -------- | -------- | 
| pallet_name | `Vec<u8>` | 
| function_name | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Emergency', 'emergency_stop', {
    'function_name': 'Bytes',
    'pallet_name': 'Bytes',
}
)
```

---------
### emergency_unstop
#### Attributes
| Name | Type |
| -------- | -------- | 
| pallet_name | `Vec<u8>` | 
| function_name | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Emergency', 'emergency_unstop', {
    'function_name': 'Bytes',
    'pallet_name': 'Bytes',
}
)
```

---------
### exit_maintenance_mode
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Emergency', 'exit_maintenance_mode', {}
)
```

---------
### start_maintenance_mode
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Emergency', 'start_maintenance_mode', {}
)
```

---------
## Events

---------
### EmergencyStopped
Stopped transaction
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pallet_name_bytes | `Vec<u8>` | ```Bytes```
| function_name_bytes | `Vec<u8>` | ```Bytes```

---------
### EmergencyUnStopped
Unstopped transaction
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pallet_name_bytes | `Vec<u8>` | ```Bytes```
| function_name_bytes | `Vec<u8>` | ```Bytes```

---------
### MaintenanceModeEnded
Chain is exit maintenance mode and enter normal operation
#### Attributes
No attributes

---------
### MaintenanceModeStarted
Chain is enter maintenance mode
#### Attributes
No attributes

---------
## Storage functions

---------
### EmergencyStoppedPallets
 The paused transaction map

 map (PalletNameBytes, FunctionNameBytes) =&gt; Option&lt;()&gt;

#### Python
```python
result = substrate.query(
    'Emergency', 'EmergencyStoppedPallets', [('Bytes', 'Bytes')]
)
```

#### Return value
```python
()
```
---------
### MaintenanceMode
 If the chain is in maintenance mode

#### Python
```python
result = substrate.query(
    'Emergency', 'MaintenanceMode', []
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
### CannotStopEmergencyCall
Can not stop emergency call

---------
### InvalidPalletAndFunction
invalid character encoding

---------
### NotInMaintenanceMode
The chain cannot resume normal operation because it is not in maintenance mode

---------