
# Preimage

---------
## Calls

---------
### note_preimage
Register a preimage on-chain.

If the preimage was previously requested, no fees or deposits are taken for providing
the preimage. Otherwise, a deposit is taken proportional to the size of the preimage.
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
Request a preimage be uploaded to the chain without paying any fees or deposits.

If the preimage requests has already been provided on-chain, we unreserve any deposit
a user may have paid, and take the control of the preimage out of their hands.
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Preimage', 'request_preimage', {'hash': 'scale_info::9'}
)
```

---------
### unnote_preimage
Clear an unrequested preimage from the runtime storage.
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Preimage', 'unnote_preimage', {'hash': 'scale_info::9'}
)
```

---------
### unrequest_preimage
Clear a previously made request for a preimage.

NOTE: THIS MUST NOT BE CALLED ON `hash` MORE TIMES THAN `request_preimage`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Preimage', 'unrequest_preimage', {'hash': 'scale_info::9'}
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
| hash | `T::Hash` | ```scale_info::9```

---------
### Noted
A preimage has been noted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```scale_info::9```

---------
### Requested
A preimage has been requested.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| hash | `T::Hash` | ```scale_info::9```

---------
## Storage functions

---------
### PreimageFor
 The preimages stored by this pallet.

#### Python
```python
result = substrate.query(
    'Preimage', 'PreimageFor', ['scale_info::9']
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
    'Preimage', 'StatusFor', ['scale_info::9']
)
```

#### Return value
```python
{'Requested': 'u32', 'Unrequested': (None, ('AccountId', 'u128'))}
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
### TooLarge
Preimage is too large to store on-chain.

---------