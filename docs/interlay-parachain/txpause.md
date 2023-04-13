
# TxPause

---------
## Calls

---------
### pause
Pause a call.

Can only be called by [`Config::PauseOrigin`].
Emits an [`Event::SomethingPaused`] event on success.
#### Attributes
| Name | Type |
| -------- | -------- | 
| full_name | `FullNameOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'TxPause', 'pause', {
    'full_name': (
        'Bytes',
        (None, 'Bytes'),
    ),
}
)
```

---------
### unpause
Un-pause a call.

Can only be called by [`Config::UnpauseOrigin`].
Emits an [`Event::SomethingUnpaused`] event on success.
#### Attributes
| Name | Type |
| -------- | -------- | 
| full_name | `FullNameOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'TxPause', 'unpause', {
    'full_name': (
        'Bytes',
        (None, 'Bytes'),
    ),
}
)
```

---------
## Events

---------
### SomethingPaused
This pallet, or a specific call is now paused. \[pallet_name, Option&lt;call_name&gt;\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| full_name | `FullNameOf<T>` | ```('Bytes', (None, 'Bytes'))```

---------
### SomethingUnpaused
This pallet, or a specific call is now unpaused. \[pallet_name, Option&lt;call_name&gt;\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| full_name | `FullNameOf<T>` | ```('Bytes', (None, 'Bytes'))```

---------
## Storage functions

---------
### PausedCalls
 The set of calls that are explicitly paused.

#### Python
```python
result = substrate.query(
    'TxPause', 'PausedCalls', [('Bytes', (None, 'Bytes'))]
)
```

#### Return value
```python
()
```
---------
## Constants

---------
### MaxNameLen
 Maximum length for pallet and call SCALE encoded string names.

 Too long names will not be truncated but handled like
 [`Self::PauseTooLongNames`] specifies.
#### Value
```python
128
```
#### Python
```python
constant = substrate.get_constant('TxPause', 'MaxNameLen')
```
---------
### PauseTooLongNames
 Specifies if functions and pallets with too long names should be treated as paused.

 Setting this to `true` ensures that all calls that
 are callable, are also pause-able.
 Otherwise there could be a situation where a call
 is callable but not pause-able, which would could be exploited.
#### Value
```python
False
```
#### Python
```python
constant = substrate.get_constant('TxPause', 'PauseTooLongNames')
```
---------
## Errors

---------
### IsPaused
The call is (already or still) paused.

---------
### IsUnpausable
The call is listed as safe and cannot be paused.

---------
### IsUnpaused
The call is (already or still) unpaused.

---------
### NotFound

---------