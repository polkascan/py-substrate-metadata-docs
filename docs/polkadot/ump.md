
# Ump

---------
## Calls

---------
### service_overweight
Service a single overweight upward message.

- `origin`: Must pass `ExecuteOverweightOrigin`.
- `index`: The index of the overweight message to service.
- `weight_limit`: The amount of weight that message execution may take.

Errors:
- `UnknownMessageIndex`: Message of `index` is unknown.
- `WeightOverLimit`: Message execution may use greater than `weight_limit`.

Events:
- `OverweightServiced`: On success.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `OverweightIndex` | 
| weight_limit | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'Ump', 'service_overweight', {
    'index': 'u64',
    'weight_limit': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
## Events

---------
### ExecutedUpward
Upward message executed with the given outcome.
\[ id, outcome \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MessageId` | ```[u8; 32]```
| None | `Outcome` | ```{'Complete': 'u64', 'Incomplete': ('u64', {'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'MultiLocationFull': None, 'MultiLocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'MaxWeightInvalid': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'UnhandledXcmVersion': None, 'WeightLimitReached': 'u64', 'Barrier': None, 'WeightNotComputable': None}), 'Error': {'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'MultiLocationFull': None, 'MultiLocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'MaxWeightInvalid': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'UnhandledXcmVersion': None, 'WeightLimitReached': 'u64', 'Barrier': None, 'WeightNotComputable': None}}```

---------
### InvalidFormat
Upward message is invalid XCM.
\[ id \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MessageId` | ```[u8; 32]```

---------
### OverweightEnqueued
The weight budget was exceeded for an individual upward message.

This message can be later dispatched manually using `service_overweight` dispatchable
using the assigned `overweight_index`.

\[ para, id, overweight_index, required \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `MessageId` | ```[u8; 32]```
| None | `OverweightIndex` | ```u64```
| None | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### OverweightServiced
Upward message from the overweight queue was executed with the given actual weight
used.

\[ overweight_index, used \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `OverweightIndex` | ```u64```
| None | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### UnsupportedVersion
Upward message is unsupported version of XCM.
\[ id \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MessageId` | ```[u8; 32]```

---------
### UpwardMessagesReceived
Some upward messages have been received and will be processed.
\[ para, count, size \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `u32` | ```u32```
| None | `u32` | ```u32```

---------
### WeightExhausted
The weight limit for handling upward messages was reached.
\[ id, remaining, required \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MessageId` | ```[u8; 32]```
| None | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```
| None | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
## Storage functions

---------
### NeedsDispatch
 The ordered list of `ParaId`s that have a `RelayDispatchQueue` entry.

 Invariant:
 - The set of items from this vector should be exactly the set of the keys in
   `RelayDispatchQueues` and `RelayDispatchQueueSize`.

#### Python
```python
result = substrate.query(
    'Ump', 'NeedsDispatch', []
)
```

#### Return value
```python
['u32']
```
---------
### NextDispatchRoundStartWith
 This is the para that gets will get dispatched first during the next upward dispatchable queue
 execution round.

 Invariant:
 - If `Some(para)`, then `para` must be present in `NeedsDispatch`.

#### Python
```python
result = substrate.query(
    'Ump', 'NextDispatchRoundStartWith', []
)
```

#### Return value
```python
'u32'
```
---------
### Overweight
 The messages that exceeded max individual message weight budget.

 These messages stay there until manually dispatched.

#### Python
```python
result = substrate.query(
    'Ump', 'Overweight', ['u64']
)
```

#### Return value
```python
('u32', 'Bytes')
```
---------
### OverweightCount
 The number of overweight messages ever recorded in `Overweight` (and thus the lowest free
 index).

#### Python
```python
result = substrate.query(
    'Ump', 'OverweightCount', []
)
```

#### Return value
```python
'u64'
```
---------
### RelayDispatchQueueSize
 Size of the dispatch queues. Caches sizes of the queues in `RelayDispatchQueue`.

 First item in the tuple is the count of messages and second
 is the total length (in bytes) of the message payloads.

 Note that this is an auxiliary mapping: it&#x27;s possible to tell the byte size and the number of
 messages only looking at `RelayDispatchQueues`. This mapping is separate to avoid the cost of
 loading the whole message queue if only the total size and count are required.

 Invariant:
 - The set of keys should exactly match the set of keys of `RelayDispatchQueues`.

#### Python
```python
result = substrate.query(
    'Ump', 'RelayDispatchQueueSize', ['u32']
)
```

#### Return value
```python
('u32', 'u32')
```
---------
### RelayDispatchQueues
 The messages waiting to be handled by the relay-chain originating from a certain parachain.

 Note that some upward messages might have been already processed by the inclusion logic. E.g.
 channel management messages.

 The messages are processed in FIFO order.

#### Python
```python
result = substrate.query(
    'Ump', 'RelayDispatchQueues', ['u32']
)
```

#### Return value
```python
['Bytes']
```
---------
## Errors

---------
### UnknownMessageIndex
The message index given is unknown.

---------
### WeightOverLimit
The amount of weight given is possibly not enough for executing the message.

---------