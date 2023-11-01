
# ImOnline

---------
## Calls

---------
### heartbeat
\#\# Complexity:
- `O(K + E)` where K is length of `Keys` (heartbeat.validators_len) and E is length of
  `heartbeat.network_state.external_address`
  - `O(K)`: decoding of length `K`
  - `O(E)`: decoding/encoding of length `E`
#### Attributes
| Name | Type |
| -------- | -------- | 
| heartbeat | `Heartbeat<T::BlockNumber>` | 
| signature | `<T::AuthorityId as RuntimeAppPublic>::Signature` | 

#### Python
```python
call = substrate.compose_call(
    'ImOnline', 'heartbeat', {
    'heartbeat': {
        'authority_index': 'u32',
        'block_number': 'u32',
        'network_state': {
            'external_addresses': [
                'Bytes',
            ],
            'peer_id': 'Bytes',
        },
        'session_index': 'u32',
        'validators_len': 'u32',
    },
    'signature': '[u8; 64]',
}
)
```

---------
## Events

---------
### AllGood
At the end of the session, no offence was committed.
#### Attributes
No attributes

---------
### HeartbeatReceived
A new heartbeat was received from `AuthorityId`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| authority_id | `T::AuthorityId` | ```[u8; 32]```

---------
### SomeOffline
At the end of the session, at least one validator was found to be offline.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| offline | `Vec<IdentificationTuple<T>>` | ```[('AccountId', {'total': 'u128', 'own': 'u128', 'others': [{'who': 'AccountId', 'value': 'u128'}]})]```

---------
## Storage functions

---------
### AuthoredBlocks
 For each session index, we keep a mapping of `ValidatorId&lt;T&gt;` to the
 number of blocks authored by the given authority.

#### Python
```python
result = substrate.query(
    'ImOnline', 'AuthoredBlocks', ['u32', 'AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### HeartbeatAfter
 The block number after which it&#x27;s ok to send heartbeats in the current
 session.

 At the beginning of each session we set this to a value that should fall
 roughly in the middle of the session duration. The idea is to first wait for
 the validators to produce a block in the current session, so that the
 heartbeat later on will not be necessary.

 This value will only be used as a fallback if we fail to get a proper session
 progress estimate from `NextSessionRotation`, as those estimates should be
 more accurate then the value we calculate for `HeartbeatAfter`.

#### Python
```python
result = substrate.query(
    'ImOnline', 'HeartbeatAfter', []
)
```

#### Return value
```python
'u32'
```
---------
### Keys
 The current set of keys that may issue a heartbeat.

#### Python
```python
result = substrate.query(
    'ImOnline', 'Keys', []
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### ReceivedHeartbeats
 For each session index, we keep a mapping of `SessionIndex` and `AuthIndex` to
 `WrapperOpaque&lt;BoundedOpaqueNetworkState&gt;`.

#### Python
```python
result = substrate.query(
    'ImOnline', 'ReceivedHeartbeats', ['u32', 'u32']
)
```

#### Return value
```python
('u32', {'external_addresses': ['Bytes'], 'peer_id': 'Bytes'})
```
---------
## Constants

---------
### UnsignedPriority
 A configuration for base priority of unsigned transactions.

 This is exposed so that it can be tuned for particular runtime, when
 multiple pallets send unsigned transactions.
#### Value
```python
18446744073709551615
```
#### Python
```python
constant = substrate.get_constant('ImOnline', 'UnsignedPriority')
```
---------
## Errors

---------
### DuplicatedHeartbeat
Duplicated heartbeat.

---------
### InvalidKey
Non existent public key.

---------