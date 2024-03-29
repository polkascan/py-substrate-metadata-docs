
# TxPause

---------
## Calls

---------
### pause
See [`Pallet::pause`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| full_name | `RuntimeCallNameOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'TxPause', 'pause', {'full_name': ('Bytes', 'Bytes')}
)
```

---------
### unpause
See [`Pallet::unpause`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| ident | `RuntimeCallNameOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'TxPause', 'unpause', {'ident': ('Bytes', 'Bytes')}
)
```

---------
## Events

---------
### CallPaused
This pallet, or a specific call is now paused.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| full_name | `RuntimeCallNameOf<T>` | ```('Bytes', 'Bytes')```

---------
### CallUnpaused
This pallet, or a specific call is now unpaused.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| full_name | `RuntimeCallNameOf<T>` | ```('Bytes', 'Bytes')```

---------
## Storage functions

---------
### PausedCalls
 The set of calls that are explicitly paused.

#### Python
```python
result = substrate.query(
    'TxPause', 'PausedCalls', [('Bytes', 'Bytes')]
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
 Maximum length for pallet name and call name SCALE encoded string names.

 TOO LONG NAMES WILL BE TREATED AS PAUSED.
#### Value
```python
256
```
#### Python
```python
constant = substrate.get_constant('TxPause', 'MaxNameLen')
```
---------
## Errors

---------
### IsPaused
The call is paused.

---------
### IsUnpaused
The call is unpaused.

---------
### NotFound

---------
### Unpausable
The call is whitelisted and cannot be paused.

---------