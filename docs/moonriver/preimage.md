
# Preimage

---------
## Calls

---------
### ensure_updated
See [`Pallet::ensure_updated`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| hashes | `Vec<T::Hash>` | 

#### Python
```python
call = substrate.compose_call(
    'Preimage', 'ensure_updated', {'hashes': ['scale_info::12']}
)
```

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
### RequestStatusFor
 The request status of a given hash.

#### Python
```python
result = substrate.query(
    'Preimage', 'RequestStatusFor', ['scale_info::12']
)
```

#### Return value
```python
{
    'Requested': {
        'count': 'u32',
        'maybe_len': (None, 'u32'),
        'maybe_ticket': (None, ('[u8; 20]', 'u128')),
    },
    'Unrequested': {'len': 'u32', 'ticket': ('[u8; 20]', 'u128')},
}
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
### TooFew
Too few hashes were requested to be upgraded (i.e. zero).

---------
### TooMany
More than `MAX_HASH_UPGRADE_BULK_COUNT` hashes were requested to be upgraded at once.

---------