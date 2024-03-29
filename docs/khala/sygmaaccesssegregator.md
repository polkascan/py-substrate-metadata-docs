
# SygmaAccessSegregator

---------
## Calls

---------
### grant_access
See [`Pallet::grant_access`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pallet_index | `u8` | 
| extrinsic_name | `Vec<u8>` | 
| who | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'SygmaAccessSegregator', 'grant_access', {
    'extrinsic_name': 'Bytes',
    'pallet_index': 'u8',
    'who': 'AccountId',
}
)
```

---------
## Events

---------
### AccessGranted
Extrinsic access grant to someone
args: [pallet_index, extrinsic_name, who]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pallet_index | `u8` | ```u8```
| extrinsic_name | `Vec<u8>` | ```Bytes```
| who | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### ExtrinsicAccess
 Mapping signature of extrinsic to account has access
 (pallet_index, extrinsic_name) =&gt; account

#### Python
```python
result = substrate.query(
    'SygmaAccessSegregator', 'ExtrinsicAccess', [('u8', 'Bytes')]
)
```

#### Return value
```python
'AccountId'
```
---------
## Errors

---------
### GrantAccessFailed
Failed to grant extrinsic access permission to an account

---------
### Unimplemented
Function unimplemented

---------