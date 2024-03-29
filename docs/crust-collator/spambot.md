
# Spambot

---------
## Calls

---------
### ping
See [`Pallet::ping`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| seq | `u32` | 
| payload | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Spambot', 'ping', {'payload': 'Bytes', 'seq': 'u32'}
)
```

---------
### pong
See [`Pallet::pong`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| seq | `u32` | 
| payload | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Spambot', 'pong', {'payload': 'Bytes', 'seq': 'u32'}
)
```

---------
### start
See [`Pallet::start`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 
| payload | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Spambot', 'start', {'para': 'u32', 'payload': 'Bytes'}
)
```

---------
### start_many
See [`Pallet::start_many`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 
| count | `u32` | 
| payload | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Spambot', 'start_many', {
    'count': 'u32',
    'para': 'u32',
    'payload': 'Bytes',
}
)
```

---------
### stop
See [`Pallet::stop`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'Spambot', 'stop', {'para': 'u32'}
)
```

---------
### stop_all
See [`Pallet::stop_all`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| maybe_para | `Option<ParaId>` | 

#### Python
```python
call = substrate.compose_call(
    'Spambot', 'stop_all', {'maybe_para': (None, 'u32')}
)
```

---------
## Events

---------
### ErrorSendingPing
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SendError` | ```('NotApplicable', 'Transport', 'Unroutable', 'DestinationUnsupported', 'ExceedsMaxMessageSize', 'MissingArgument', 'Fees')```
| None | `ParaId` | ```u32```
| None | `u32` | ```u32```
| None | `Vec<u8>` | ```Bytes```

---------
### ErrorSendingPong
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SendError` | ```('NotApplicable', 'Transport', 'Unroutable', 'DestinationUnsupported', 'ExceedsMaxMessageSize', 'MissingArgument', 'Fees')```
| None | `ParaId` | ```u32```
| None | `u32` | ```u32```
| None | `Vec<u8>` | ```Bytes```

---------
### PingSent
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `u32` | ```u32```
| None | `Vec<u8>` | ```Bytes```
| None | `XcmHash` | ```[u8; 32]```
| None | `MultiAssets` | ```[{'id': {'Concrete': {'parents': 'u8', 'interior': 'scale_info::48'}, 'Abstract': '[u8; 32]'}, 'fun': {'Fungible': 'u128', 'NonFungible': {'Undefined': None, 'Index': 'u128', 'Array4': '[u8; 4]', 'Array8': '[u8; 8]', 'Array16': '[u8; 16]', 'Array32': '[u8; 32]'}}}]```

---------
### Pinged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `u32` | ```u32```
| None | `Vec<u8>` | ```Bytes```

---------
### PongSent
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `u32` | ```u32```
| None | `Vec<u8>` | ```Bytes```
| None | `XcmHash` | ```[u8; 32]```
| None | `MultiAssets` | ```[{'id': {'Concrete': {'parents': 'u8', 'interior': 'scale_info::48'}, 'Abstract': '[u8; 32]'}, 'fun': {'Fungible': 'u128', 'NonFungible': {'Undefined': None, 'Index': 'u128', 'Array4': '[u8; 4]', 'Array8': '[u8; 8]', 'Array16': '[u8; 16]', 'Array32': '[u8; 32]'}}}]```

---------
### Ponged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `u32` | ```u32```
| None | `Vec<u8>` | ```Bytes```
| None | `BlockNumberFor<T>` | ```u32```

---------
### UnknownPong
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `u32` | ```u32```
| None | `Vec<u8>` | ```Bytes```

---------
## Storage functions

---------
### PingCount
 The total number of pings sent.

#### Python
```python
result = substrate.query(
    'Spambot', 'PingCount', []
)
```

#### Return value
```python
'u32'
```
---------
### Pings
 The sent pings.

#### Python
```python
result = substrate.query(
    'Spambot', 'Pings', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### Targets
 The target parachains to ping.

#### Python
```python
result = substrate.query(
    'Spambot', 'Targets', []
)
```

#### Return value
```python
[('u32', 'Bytes')]
```
---------
## Errors

---------
### PayloadTooLarge
The payload provided is too large, limit is 1024 bytes.

---------
### TooManyTargets
Too many parachains have been added as a target.

---------