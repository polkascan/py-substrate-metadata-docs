
# XcmpQueue

---------
## Calls

---------
### resume_xcm_execution
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'XcmpQueue', 'resume_xcm_execution', {}
)
```

---------
### service_overweight
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `OverweightIndex` | 
| weight_limit | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'XcmpQueue', 'service_overweight', {
    'index': 'u64',
    'weight_limit': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
### suspend_xcm_execution
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'XcmpQueue', 'suspend_xcm_execution', {}
)
```

---------
### update_drop_threshold
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'XcmpQueue', 'update_drop_threshold', {'new': 'u32'}
)
```

---------
### update_resume_threshold
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'XcmpQueue', 'update_resume_threshold', {'new': 'u32'}
)
```

---------
### update_suspend_threshold
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'XcmpQueue', 'update_suspend_threshold', {'new': 'u32'}
)
```

---------
### update_threshold_weight
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'XcmpQueue', 'update_threshold_weight', {
    'new': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
### update_weight_restrict_decay
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'XcmpQueue', 'update_weight_restrict_decay', {
    'new': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
### update_xcmp_max_individual_weight
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'XcmpQueue', 'update_xcmp_max_individual_weight', {
    'new': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
## Events

---------
### BadFormat
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `XcmHash` | ```[u8; 32]```

---------
### BadVersion
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `XcmHash` | ```[u8; 32]```

---------
### Fail
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `XcmHash` | ```[u8; 32]```
| message_id | `XcmHash` | ```[u8; 32]```
| error | `XcmError` | ```{'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'LocationFull': None, 'LocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'MaxWeightInvalid': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'ExpectationFalse': None, 'PalletNotFound': None, 'NameMismatch': None, 'VersionIncompatible': None, 'HoldingWouldOverflow': None, 'ExportError': None, 'ReanchorFailed': None, 'NoDeal': None, 'FeesNotMet': None, 'LockError': None, 'NoPermission': None, 'Unanchored': None, 'NotDepositable': None, 'UnhandledXcmVersion': None, 'WeightLimitReached': {'ref_time': 'u64', 'proof_size': 'u64'}, 'Barrier': None, 'WeightNotComputable': None, 'ExceedsStackLimit': None}```
| weight | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### OverweightEnqueued
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `ParaId` | ```u32```
| sent_at | `RelayBlockNumber` | ```u32```
| index | `OverweightIndex` | ```u64```
| required | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### OverweightServiced
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `OverweightIndex` | ```u64```
| used | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### Success
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `XcmHash` | ```[u8; 32]```
| message_id | `XcmHash` | ```[u8; 32]```
| weight | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### XcmpMessageSent
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `XcmHash` | ```[u8; 32]```

---------
## Storage functions

---------
### CounterForOverweight

#### Python
```python
result = substrate.query(
    'XcmpQueue', 'CounterForOverweight', []
)
```

#### Return value
```python
'u32'
```
---------
### InboundXcmpMessages

#### Python
```python
result = substrate.query(
    'XcmpQueue', 'InboundXcmpMessages', ['u32', 'u32']
)
```

#### Return value
```python
'Bytes'
```
---------
### InboundXcmpStatus

#### Python
```python
result = substrate.query(
    'XcmpQueue', 'InboundXcmpStatus', []
)
```

#### Return value
```python
[
    {
        'message_metadata': [
            (
                'u32',
                (
                    'ConcatenatedVersionedXcm',
                    'ConcatenatedEncodedBlob',
                    'Signals',
                ),
            ),
        ],
        'sender': 'u32',
        'state': ('Ok', 'Suspended'),
    },
]
```
---------
### OutboundXcmpMessages

#### Python
```python
result = substrate.query(
    'XcmpQueue', 'OutboundXcmpMessages', ['u32', 'u16']
)
```

#### Return value
```python
'Bytes'
```
---------
### OutboundXcmpStatus

#### Python
```python
result = substrate.query(
    'XcmpQueue', 'OutboundXcmpStatus', []
)
```

#### Return value
```python
[
    {
        'first_index': 'u16',
        'last_index': 'u16',
        'recipient': 'u32',
        'signals_exist': 'bool',
        'state': ('Ok', 'Suspended'),
    },
]
```
---------
### Overweight

#### Python
```python
result = substrate.query(
    'XcmpQueue', 'Overweight', ['u64']
)
```

#### Return value
```python
('u32', 'u32', 'Bytes')
```
---------
### OverweightCount

#### Python
```python
result = substrate.query(
    'XcmpQueue', 'OverweightCount', []
)
```

#### Return value
```python
'u64'
```
---------
### QueueConfig

#### Python
```python
result = substrate.query(
    'XcmpQueue', 'QueueConfig', []
)
```

#### Return value
```python
{
    'drop_threshold': 'u32',
    'resume_threshold': 'u32',
    'suspend_threshold': 'u32',
    'threshold_weight': {'proof_size': 'u64', 'ref_time': 'u64'},
    'weight_restrict_decay': {'proof_size': 'u64', 'ref_time': 'u64'},
    'xcmp_max_individual_weight': {'proof_size': 'u64', 'ref_time': 'u64'},
}
```
---------
### QueueSuspended

#### Python
```python
result = substrate.query(
    'XcmpQueue', 'QueueSuspended', []
)
```

#### Return value
```python
'bool'
```
---------
### SignalMessages

#### Python
```python
result = substrate.query(
    'XcmpQueue', 'SignalMessages', ['u32']
)
```

#### Return value
```python
'Bytes'
```
---------
## Errors

---------
### BadOverweightIndex

---------
### BadXcm

---------
### BadXcmOrigin

---------
### FailedToSend

---------
### WeightOverLimit

---------