
# RemoteGovernance

---------
## Calls

---------
### emergency_safeguard
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `AnyCall<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RemoteGovernance', 'emergency_safeguard', {'call': 'Call'}
)
```

---------
### enact_remote_call
Handle relay message sent from the source backing pallet with relay message
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `AnyCall<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RemoteGovernance', 'enact_remote_call', {'call': 'Call'}
)
```

---------
## Events

---------
### Emergency
Bridge&\#x27;s GRANDPA finality has stalled for a long time, enter the emergency mode.
#### Attributes
No attributes

---------
### EmergencySafeguardDone
Emergency safeguard just took place. \[result\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### Recovery
Recover from the emergency mode.
#### Attributes
No attributes

---------
### RemoteCallEnacted
Remote call just enacted. \[result\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
## Storage functions

---------
### Emergency

#### Python
```python
result = substrate.query(
    'RemoteGovernance', 'Emergency', []
)
```

#### Return value
```python
'bool'
```
---------
### PreviousBridgeFinalized

#### Python
```python
result = substrate.query(
    'RemoteGovernance', 'PreviousBridgeFinalized', []
)
```

#### Return value
```python
'[u8; 32]'
```
---------
## Errors

---------
### EmergencyOnly
Only available on emergency mode.

---------
### RequireSourceRoot
Origin MUST be `SourceRoot`.

---------