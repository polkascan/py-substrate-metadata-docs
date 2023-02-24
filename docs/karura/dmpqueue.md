
# DmpQueue

---------
## Calls

---------
### service_overweight
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
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_id | `MessageId` | ```[u8; 32]```
| outcome | `Outcome` | ```{'Complete': 'u64', 'Incomplete': ('u64', {'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'MultiLocationFull': None, 'MultiLocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'MaxWeightInvalid': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'UnhandledXcmVersion': None, 'WeightLimitReached': 'u64', 'Barrier': None, 'WeightNotComputable': None}), 'Error': {'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'MultiLocationFull': None, 'MultiLocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'MaxWeightInvalid': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'UnhandledXcmVersion': None, 'WeightLimitReached': 'u64', 'Barrier': None, 'WeightNotComputable': None}}```

---------
### InvalidFormat
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_id | `MessageId` | ```[u8; 32]```

---------
### OverweightEnqueued
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_id | `MessageId` | ```[u8; 32]```
| overweight_index | `OverweightIndex` | ```u64```
| required_weight | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### OverweightServiced
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| overweight_index | `OverweightIndex` | ```u64```
| weight_used | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### UnsupportedVersion
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_id | `MessageId` | ```[u8; 32]```

---------
### WeightExhausted
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

---------
### Unknown

---------