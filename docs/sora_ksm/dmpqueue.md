
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
| weight_limit | `Weight` | 

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
\[ id, outcome \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MessageId` | ```[u8; 32]```
| None | `Outcome` | ```{'Complete': 'u64', 'Incomplete': ('u64', {'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'MultiLocationFull': None, 'MultiLocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'TooMuchWeightRequired': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'UnhandledXcmVersion': None, 'WeightLimitReached': 'u64', 'Barrier': None, 'WeightNotComputable': None}), 'Error': {'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'MultiLocationFull': None, 'MultiLocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'TooMuchWeightRequired': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'UnhandledXcmVersion': None, 'WeightLimitReached': 'u64', 'Barrier': None, 'WeightNotComputable': None}}```

---------
### InvalidFormat
Downward message is invalid XCM.
\[ id \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MessageId` | ```[u8; 32]```

---------
### OverweightEnqueued
Downward message is overweight and was placed in the overweight queue.
\[ id, index, required \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MessageId` | ```[u8; 32]```
| None | `OverweightIndex` | ```u64```
| None | `Weight` | ```u64```

---------
### OverweightServiced
Downward message from the overweight queue was executed.
\[ index, used \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `OverweightIndex` | ```u64```
| None | `Weight` | ```u64```

---------
### UnsupportedVersion
Downward message is unsupported version of XCM.
\[ id \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MessageId` | ```[u8; 32]```

---------
### WeightExhausted
The weight limit for handling downward messages was reached.
\[ id, remaining, required \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MessageId` | ```[u8; 32]```
| None | `Weight` | ```u64```
| None | `Weight` | ```u64```

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
{'max_individual': 'u64'}
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