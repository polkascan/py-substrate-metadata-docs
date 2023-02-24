
# Session

---------
## Calls

---------
### purge_keys
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Session', 'purge_keys', {}
)
```

---------
### set_keys
#### Attributes
| Name | Type |
| -------- | -------- | 
| keys | `T::Keys` | 
| proof | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Session', 'set_keys', {'keys': {'aura': '[u8; 32]'}, 'proof': 'Bytes'}
)
```

---------
## Events

---------
### NewSession
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| session_index | `SessionIndex` | ```u32```

---------
## Storage functions

---------
### CurrentIndex

#### Python
```python
result = substrate.query(
    'Session', 'CurrentIndex', []
)
```

#### Return value
```python
'u32'
```
---------
### DisabledValidators

#### Python
```python
result = substrate.query(
    'Session', 'DisabledValidators', []
)
```

#### Return value
```python
['u32']
```
---------
### KeyOwner

#### Python
```python
result = substrate.query(
    'Session', 'KeyOwner', [('[u8; 4]', 'Bytes')]
)
```

#### Return value
```python
'AccountId'
```
---------
### NextKeys

#### Python
```python
result = substrate.query(
    'Session', 'NextKeys', ['AccountId']
)
```

#### Return value
```python
{'aura': '[u8; 32]'}
```
---------
### QueuedChanged

#### Python
```python
result = substrate.query(
    'Session', 'QueuedChanged', []
)
```

#### Return value
```python
'bool'
```
---------
### QueuedKeys

#### Python
```python
result = substrate.query(
    'Session', 'QueuedKeys', []
)
```

#### Return value
```python
[('AccountId', {'aura': '[u8; 32]'})]
```
---------
### Validators

#### Python
```python
result = substrate.query(
    'Session', 'Validators', []
)
```

#### Return value
```python
['AccountId']
```
---------
## Errors

---------
### DuplicatedKey

---------
### InvalidProof

---------
### NoAccount

---------
### NoAssociatedValidatorId

---------
### NoKeys

---------