
# ClientsInfo

---------
## Calls

---------
### set_current_client_release
Sets the current client release version, in case of a bug fix or patch.
Clients include the vault, oracle, and faucet.

\# Arguments
* `client_name` - raw byte string representation of the client name (e.g. `b&quot;vault&quot;`, `b&quot;oracle&quot;`,
  `b&quot;faucet&quot;`)
* `release` - The release information for the given `client_name`
#### Attributes
| Name | Type |
| -------- | -------- | 
| client_name | `NameOf<T>` | 
| release | `ClientRelease<UriOf<T>, T::Hash>` | 

#### Python
```python
call = substrate.compose_call(
    'ClientsInfo', 'set_current_client_release', {
    'client_name': 'Bytes',
    'release': {
        'checksum': 'scale_info::12',
        'uri': 'Bytes',
    },
}
)
```

---------
### set_pending_client_release
Sets the pending client release version. To be batched alongside the
`parachainSystem.authorizeUpgrade` Cumulus call.
Clients include the vault, oracle, and faucet.

\# Arguments
* `client_name` - raw byte string representation of the client name (e.g. `b&quot;vault&quot;`, `b&quot;oracle&quot;`,
  `b&quot;faucet&quot;`)
* `release` - The release information for the given `client_name`
#### Attributes
| Name | Type |
| -------- | -------- | 
| client_name | `NameOf<T>` | 
| release | `ClientRelease<UriOf<T>, T::Hash>` | 

#### Python
```python
call = substrate.compose_call(
    'ClientsInfo', 'set_pending_client_release', {
    'client_name': 'Bytes',
    'release': {
        'checksum': 'scale_info::12',
        'uri': 'Bytes',
    },
}
)
```

---------
## Events

---------
### ApplyClientRelease
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| release | `ClientRelease<UriOf<T>, T::Hash>` | ```{'uri': 'Bytes', 'checksum': 'scale_info::12'}```

---------
### NotifyClientRelease
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| release | `ClientRelease<UriOf<T>, T::Hash>` | ```{'uri': 'Bytes', 'checksum': 'scale_info::12'}```

---------
## Storage functions

---------
### CurrentClientReleases
 Mapping of client name (string literal represented as bytes) to its release details.

#### Python
```python
result = substrate.query(
    'ClientsInfo', 'CurrentClientReleases', ['Bytes']
)
```

#### Return value
```python
{'checksum': 'scale_info::12', 'uri': 'Bytes'}
```
---------
### PendingClientReleases
 Mapping of client name (string literal represented as bytes) to its pending release details.

#### Python
```python
result = substrate.query(
    'ClientsInfo', 'PendingClientReleases', ['Bytes']
)
```

#### Return value
```python
{'checksum': 'scale_info::12', 'uri': 'Bytes'}
```
---------
## Constants

---------
### MaxNameLength
 The maximum length of a client name.
#### Value
```python
255
```
#### Python
```python
constant = substrate.get_constant('ClientsInfo', 'MaxNameLength')
```
---------
### MaxUriLength
 The maximum length of a client URI.
#### Value
```python
255
```
#### Python
```python
constant = substrate.get_constant('ClientsInfo', 'MaxUriLength')
```
---------