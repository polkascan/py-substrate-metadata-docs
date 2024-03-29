
# Preimage

---------
## Calls

---------
### note_preimage
See [`Pallet::note_preimage`].
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
See [`Pallet::request_preimage`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Preimage', 'request_preimage', {'hash': 'scale_info::12'}
)
```

---------
### unnote_preimage
See [`Pallet::unnote_preimage`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Preimage', 'unnote_preimage', {'hash': 'scale_info::12'}
)
```

---------
### unrequest_preimage
See [`Pallet::unrequest_preimage`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Preimage', 'unrequest_preimage', {'hash': 'scale_info::12'}
)
```

---------
## Events

---------
### Cleared
A preimage has ben cleared.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```scale_info::12```

---------
### Noted
A preimage has been noted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```scale_info::12```

---------
### Requested
A preimage has been requested.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```scale_info::12```

---------
## Storage functions

---------
### PreimageFor

#### Python
```python
result = substrate.query(
    'Preimage', 'PreimageFor', [('scale_info::12', 'u32')]
)
```

#### Return value
```python
'Bytes'
```
---------
### StatusFor
 The request status of a given hash.

#### Python
```python
result = substrate.query(
    'Preimage', 'StatusFor', ['scale_info::12']
)
```

#### Return value
```python
{
    'Requested': {
        'count': 'u32',
        'deposit': (None, ('[u8; 20]', 'u128')),
        'len': (None, 'u32'),
    },
    'Unrequested': {'deposit': ('[u8; 20]', 'u128'), 'len': 'u32'},
}
```
---------
## Errors

---------
### AlreadyNoted
Preimage has already been noted on-chain.

---------
### NotAuthorized
The user is not authorized to perform this action.

---------
### NotNoted
The preimage cannot be removed since it has not yet been noted.

---------
### NotRequested
The preimage request cannot be removed since no outstanding requests exist.

---------
### Requested
A preimage may not be removed when there are outstanding requests.

---------
### TooBig
Preimage is too large to store on-chain.

---------