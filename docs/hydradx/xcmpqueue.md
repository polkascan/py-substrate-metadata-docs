
# XcmpQueue

---------
## Events

---------
### BadFormat
Bad XCM format used.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `Option<XcmHash>` | ```(None, '[u8; 32]')```

---------
### BadVersion
Bad XCM version used.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `Option<XcmHash>` | ```(None, '[u8; 32]')```

---------
### Fail
Some XCM failed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `Option<XcmHash>` | ```(None, '[u8; 32]')```
| error | `XcmError` | ```{'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'LocationFull': None, 'LocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'MaxWeightInvalid': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'ExpectationFalse': None, 'PalletNotFound': None, 'NameMismatch': None, 'VersionIncompatible': None, 'HoldingWouldOverflow': None, 'ExportError': None, 'ReanchorFailed': None, 'NoDeal': None, 'FeesNotMet': None, 'LockError': None, 'NoPermission': None, 'Unanchored': None, 'NotDepositable': None, 'UnhandledXcmVersion': None, 'WeightLimitReached': {'ref_time': 'u64', 'proof_size': 'u64'}, 'Barrier': None, 'WeightNotComputable': None, 'ExceedsStackLimit': None}```
| weight | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### OverweightEnqueued
An XCM exceeded the individual message weight budget.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `ParaId` | ```u32```
| sent_at | `RelayBlockNumber` | ```u32```
| index | `OverweightIndex` | ```u64```
| required | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### OverweightServiced
An XCM from the overweight queue was executed with the given actual weight used.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `OverweightIndex` | ```u64```
| used | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### Success
Some XCM was executed ok.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `Option<XcmHash>` | ```(None, '[u8; 32]')```
| weight | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### XcmDeferred
Some XCM was deferred for later execution
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `ParaId` | ```u32```
| sent_at | `RelayBlockNumber` | ```u32```
| deferred_to | `RelayBlockNumber` | ```u32```
| message_hash | `Option<XcmHash>` | ```(None, '[u8; 32]')```

---------
### XcmDeferredQueueFull
#### Attributes
No attributes

---------
### XcmpMessageSent
An HRMP message was sent to a sibling parachain.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `Option<XcmHash>` | ```(None, '[u8; 32]')```

---------
## Storage functions

---------
### CounterForOverweight
Counter for the related counted storage map

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
### DeferredXcmMessages
 Inbound aggregate XCMP messages. It can only be one per ParaId.

#### Python
```python
result = substrate.query(
    'XcmpQueue', 'DeferredXcmMessages', ['u32']
)
```

#### Return value
```python
[
    {
        'deferred_to': 'u32',
        'sender': 'u32',
        'sent_at': 'u32',
        'xcm': {
            None: None,
            'V2': ['scale_info::322'],
            'V3': ['scale_info::326'],
        },
    },
]
```
---------
### InboundXcmpMessages
 Inbound aggregate XCMP messages. It can only be one per ParaId/block.

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
 Status of the inbound XCMP channels.

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
 The messages outbound in a given XCMP channel.

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
 The non-empty XCMP channels in order of becoming non-empty, and the index of the first
 and last outbound message. If the two indices are equal, then it indicates an empty
 queue and there must be a non-`Ok` `OutboundStatus`. We assume queues grow no greater
 than 65535 items. Queue indices for normal messages begin at one; zero is reserved in
 case of the need to send a high-priority signal message this block.
 The bool is true if there is a signal message waiting to be sent.

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
 The messages that exceeded max individual message weight budget.

 These message stay in this storage map until they are manually dispatched via
 `service_overweight`.

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
 The number of overweight messages ever recorded in `Overweight`. Also doubles as the next
 available free overweight index.

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
 The configuration which controls the dynamics of the outbound queue.

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
 Whether or not the XCMP queue is suspended from executing incoming XCMs or not.

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
 Any signal messages waiting to be sent.

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
Bad overweight index.

---------
### BadXcm
Bad XCM data.

---------
### BadXcmOrigin
Bad XCM origin.

---------
### FailedToSend
Failed to send XCM message.

---------
### WeightOverLimit
Provided weight is possibly not enough to execute the message.

---------