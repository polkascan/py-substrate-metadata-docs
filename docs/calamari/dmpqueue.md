
# DmpQueue

---------
## Calls

---------
### service_overweight
Service a single overweight message.

- `origin`: Must pass `ExecuteOverweightOrigin`.
- `index`: The index of the overweight message to service.
- `weight_limit`: The amount of weight that message execution may take.

Errors:
- `Unknown`: Message of `index` is unknown.
- `OverLimit`: Message execution may use greater than `weight_limit`.

Events:
- `OverweightServiced`: On success.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `OverweightIndex` | 
| weight_limit | `XcmWeight` | 

#### Python
```python
call = substrate.compose_call(
    'DmpQueue', 'service_overweight', {
    'index': 'u64',
    'weight_limit': 'u64',
}
)
```

---------
## Events

---------
### ExecutedDownward
Downward message executed with the given outcome.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_id | `MessageId` | ```[u8; 32]```
| outcome | `Outcome` | ```{'Complete': 'u64', 'Incomplete': ('u64', {'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'MultiLocationFull': None, 'MultiLocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'MaxWeightInvalid': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'UnhandledXcmVersion': None, 'WeightLimitReached': 'u64', 'Barrier': None, 'WeightNotComputable': None}), 'Error': {'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'MultiLocationFull': None, 'MultiLocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'MaxWeightInvalid': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'UnhandledXcmVersion': None, 'WeightLimitReached': 'u64', 'Barrier': None, 'WeightNotComputable': None}}```

---------
### InvalidFormat
Downward message is invalid XCM.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_id | `MessageId` | ```[u8; 32]```

---------
### OverweightEnqueued
Downward message is overweight and was placed in the overweight queue.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_id | `MessageId` | ```[u8; 32]```
| overweight_index | `OverweightIndex` | ```u64```
| required_weight | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### OverweightServiced
Downward message from the overweight queue was executed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| overweight_index | `OverweightIndex` | ```u64```
| weight_used | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### UnsupportedVersion
Downward message is unsupported version of XCM.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_id | `MessageId` | ```[u8; 32]```

---------
### WeightExhausted
The weight limit for handling downward messages was reached.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_id | `MessageId` | ```[u8; 32]```
| remaining_weight | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```
| required_weight | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
## Storage functions

---------
### Configuration
 The configuration.

#### Python
```python
result = substrate.query(
    'DmpQueue', 'Configuration', []
)
```

#### Return value
```python
{'max_individual': {'proof_size': 'u64', 'ref_time': 'u64'}}
```
---------
### Overweight
 The overweight messages.

#### Python
```python
result = substrate.query(
    'DmpQueue', 'Overweight', ['u64']
)
```

#### Return value
```python
('u32', 'Bytes')
```
---------
### PageIndex
 The page index.

#### Python
```python
result = substrate.query(
    'DmpQueue', 'PageIndex', []
)
```

#### Return value
```python
{'begin_used': 'u32', 'end_used': 'u32', 'overweight_count': 'u64'}
```
---------
### Pages
 The queue pages.

#### Python
```python
result = substrate.query(
    'DmpQueue', 'Pages', ['u32']
)
```

#### Return value
```python
[('u32', 'Bytes')]
```
---------
## Errors

---------
### OverLimit
The amount of weight given is possibly not enough for executing the message.

---------
### Unknown
The message index given is unknown.

---------