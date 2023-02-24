
# XcmpQueue

---------
## Events

---------
### BadFormat
Bad XCM format used.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Option<T::Hash>` | ```(None, '[u8; 32]')```

---------
### BadVersion
Bad XCM version used.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Option<T::Hash>` | ```(None, '[u8; 32]')```

---------
### Fail
Some XCM failed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Option<T::Hash>` | ```(None, '[u8; 32]')```
| None | `XcmError` | ```{'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'MultiLocationFull': None, 'MultiLocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'TooMuchWeightRequired': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'UnhandledXcmVersion': None, 'WeightLimitReached': 'u64', 'Barrier': None, 'WeightNotComputable': None}```

---------
### Success
Some XCM was executed ok.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Option<T::Hash>` | ```(None, '[u8; 32]')```

---------
### UpwardMessageSent
An upward message was sent to the relay chain.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Option<T::Hash>` | ```(None, '[u8; 32]')```

---------
### XcmpMessageSent
An HRMP message was sent to a sibling parachain.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Option<T::Hash>` | ```(None, '[u8; 32]')```

---------
## Storage functions

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
    (
        'u32',
        ('Ok', 'Suspended'),
        [
            (
                'u32',
                (
                    'ConcatenatedVersionedXcm',
                    'ConcatenatedEncodedBlob',
                    'Signals',
                ),
            ),
        ],
    ),
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
[('u32', ('Ok', 'Suspended'), 'bool', 'u16', 'u16')]
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
    'threshold_weight': 'u64',
    'weight_restrict_decay': 'u64',
}
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
### BadXcm
Bad XCM data.

---------
### BadXcmOrigin
Bad XCM origin.

---------
### FailedToSend
Failed to send XCM message.

---------