
# CallFilter

---------
## Calls

---------
### disable
Disable a pallet function.

The dispatch origin for this call must be _Signed_ and the sender must be
`DisableOrigin`.

Possibly emits a `Disabled` event.
#### Attributes
| Name | Type |
| -------- | -------- | 
| entry | `CallFilterEntryOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CallFilter', 'disable', {
    'entry': {
        'function_name': 'Bytes',
        'pallet_name': 'Bytes',
    },
}
)
```

---------
### enable
Enable a previously disabled pallet function.

The dispatch origin for this call must be _Signed_ and the sender must be
`EnableOrigin`.

Possibly emits an `Enabled` event.
#### Attributes
| Name | Type |
| -------- | -------- | 
| entry | `CallFilterEntryOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CallFilter', 'enable', {
    'entry': {
        'function_name': 'Bytes',
        'pallet_name': 'Bytes',
    },
}
)
```

---------
## Events

---------
### Disabled
Paused transaction
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| entry | `CallFilterEntryOf<T>` | ```{'pallet_name': 'Bytes', 'function_name': 'Bytes'}```

---------
### Enabled
Unpaused transaction
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| entry | `CallFilterEntryOf<T>` | ```{'pallet_name': 'Bytes', 'function_name': 'Bytes'}```

---------
## Storage functions

---------
### DisabledCalls
 The list of disabled extrinsics.

#### Python
```python
result = substrate.query(
    'CallFilter', 'DisabledCalls', [
    {
        'function_name': 'Bytes',
        'pallet_name': 'Bytes',
    },
]
)
```

#### Return value
```python
()
```
---------
## Constants

---------
### MaxStringSize
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('CallFilter', 'MaxStringSize')
```
---------
## Errors

---------
### CannotDisable
We tried to disable an extrinsic that cannot be disabled.

---------
### InvalidString
The pallet name is not a valid UTF8 string.

---------