
# DmpQueue

---------
## Calls

---------
### service_overweight
See [`Pallet::service_overweight`].
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
### ExecutedDownward
Downward message executed with the given outcome.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `XcmHash` | ```[u8; 32]```
| message_id | `XcmHash` | ```[u8; 32]```
| outcome | `Outcome` | ```{'Complete': {'ref_time': 'u64', 'proof_size': 'u64'}, 'Incomplete': ({'ref_time': 'u64', 'proof_size': 'u64'}, {'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'LocationFull': None, 'LocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'MaxWeightInvalid': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'ExpectationFalse': None, 'PalletNotFound': None, 'NameMismatch': None, 'VersionIncompatible': None, 'HoldingWouldOverflow': None, 'ExportError': None, 'ReanchorFailed': None, 'NoDeal': None, 'FeesNotMet': None, 'LockError': None, 'NoPermission': None, 'Unanchored': None, 'NotDepositable': None, 'UnhandledXcmVersion': None, 'WeightLimitReached': {'ref_time': 'u64', 'proof_size': 'u64'}, 'Barrier': None, 'WeightNotComputable': None, 'ExceedsStackLimit': None}), 'Error': {'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'LocationFull': None, 'LocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'MaxWeightInvalid': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'ExpectationFalse': None, 'PalletNotFound': None, 'NameMismatch': None, 'VersionIncompatible': None, 'HoldingWouldOverflow': None, 'ExportError': None, 'ReanchorFailed': None, 'NoDeal': None, 'FeesNotMet': None, 'LockError': None, 'NoPermission': None, 'Unanchored': None, 'NotDepositable': None, 'UnhandledXcmVersion': None, 'WeightLimitReached': {'ref_time': 'u64', 'proof_size': 'u64'}, 'Barrier': None, 'WeightNotComputable': None, 'ExceedsStackLimit': None}}```

---------
### InvalidFormat
Downward message is invalid XCM.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `XcmHash` | ```[u8; 32]```

---------
### MaxMessagesExhausted
The maximum number of downward messages was reached.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `XcmHash` | ```[u8; 32]```

---------
### OverweightEnqueued
Downward message is overweight and was placed in the overweight queue.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `XcmHash` | ```[u8; 32]```
| message_id | `XcmHash` | ```[u8; 32]```
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
| message_hash | `XcmHash` | ```[u8; 32]```

---------
### WeightExhausted
The weight limit for handling downward messages was reached.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `XcmHash` | ```[u8; 32]```
| message_id | `XcmHash` | ```[u8; 32]```
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
### CounterForOverweight
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'DmpQueue', 'CounterForOverweight', []
)
```

#### Return value
```python
'u32'
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