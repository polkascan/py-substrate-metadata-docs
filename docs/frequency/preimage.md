
# Preimage

---------
## Calls

---------
### note_preimage
#### Attributes
| Name | Type |
| -------- | -------- | 
| bytes | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Preimage', 'note_preimage', {'bytes': 'Bytes'}
)
```

---------
### request_preimage
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Preimage', 'request_preimage', {'hash': '[u8; 32]'}
)
```

---------
### unnote_preimage
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Preimage', 'unnote_preimage', {'hash': '[u8; 32]'}
)
```

---------
### unrequest_preimage
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Preimage', 'unrequest_preimage', {'hash': '[u8; 32]'}
)
```

---------
## Events

---------
### Cleared
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```[u8; 32]```

---------
### Noted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```[u8; 32]```

---------
### Requested
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```[u8; 32]```

---------
## Storage functions

---------
### PreimageFor

#### Python
```python
result = substrate.query(
    'Preimage', 'PreimageFor', [('[u8; 32]', 'u32')]
)
```

#### Return value
```python
'Bytes'
```
---------
### StatusFor

#### Python
```python
result = substrate.query(
    'Preimage', 'StatusFor', ['[u8; 32]']
)
```

#### Return value
```python
{
    'Requested': {
        'count': 'u32',
        'deposit': (None, ('AccountId', 'u128')),
        'len': (None, 'u32'),
    },
    'Unrequested': {'deposit': ('AccountId', 'u128'), 'len': 'u32'},
}
```
---------
## Errors

---------
### AlreadyNoted

---------
### NotAuthorized

---------
### NotNoted

---------
### NotRequested

---------
### Requested

---------
### TooBig

---------