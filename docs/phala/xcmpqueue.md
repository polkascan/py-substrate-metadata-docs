
# XcmpQueue

---------
## Calls

---------
### resume_xcm_execution
Resumes all XCM executions for the XCMP queue.

Note that this function doesn&\#x27;t change the status of the in/out bound channels.

- `origin`: Must pass `ControllerOrigin`.
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
Services a single overweight XCM.

- `origin`: Must pass `ExecuteOverweightOrigin`.
- `index`: The index of the overweight XCM to service
- `weight_limit`: The amount of weight that XCM execution may take.

Errors:
- `BadOverweightIndex`: XCM under `index` is not found in the `Overweight` storage map.
- `BadXcm`: XCM under `index` cannot be properly decoded into a valid XCM format.
- `WeightOverLimit`: XCM execution may use greater `weight_limit`.

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
    'XcmpQueue', 'service_overweight', {
    'index': 'u64',
    'weight_limit': 'u64',
}
)
```

---------
### suspend_xcm_execution
Suspends all XCM executions for the XCMP queue, regardless of the sender&\#x27;s origin.

- `origin`: Must pass `ControllerOrigin`.
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
Overwrites the number of pages of messages which must be in the queue after which we drop any further
messages from the channel.

- `origin`: Must pass `Root`.
- `new`: Desired value for `QueueConfigData.drop_threshold`
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
Overwrites the number of pages of messages which the queue must be reduced to before it signals that
message sending may recommence after it has been suspended.

- `origin`: Must pass `Root`.
- `new`: Desired value for `QueueConfigData.resume_threshold`
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
Overwrites the number of pages of messages which must be in the queue for the other side to be told to
suspend their sending.

- `origin`: Must pass `Root`.
- `new`: Desired value for `QueueConfigData.suspend_value`
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
Overwrites the amount of remaining weight under which we stop processing messages.

- `origin`: Must pass `Root`.
- `new`: Desired value for `QueueConfigData.threshold_weight`
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'XcmpQueue', 'update_threshold_weight', {'new': 'u64'}
)
```

---------
### update_weight_restrict_decay
Overwrites the speed to which the available weight approaches the maximum weight.
A lower number results in a faster progression. A value of 1 makes the entire weight available initially.

- `origin`: Must pass `Root`.
- `new`: Desired value for `QueueConfigData.weight_restrict_decay`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'XcmpQueue', 'update_weight_restrict_decay', {'new': 'u64'}
)
```

---------
### update_xcmp_max_individual_weight
Overwrite the maximum amount of weight any individual message may consume.
Messages above this weight go into the overweight queue and may only be serviced explicitly.

- `origin`: Must pass `Root`.
- `new`: Desired value for `QueueConfigData.xcmp_max_individual_weight`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'XcmpQueue', 'update_xcmp_max_individual_weight', {'new': 'u64'}
)
```

---------
## Events

---------
### BadFormat
Bad XCM format used.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `Option<T::Hash>` | ```(None, '[u8; 32]')```

---------
### BadVersion
Bad XCM version used.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `Option<T::Hash>` | ```(None, '[u8; 32]')```

---------
### Fail
Some XCM failed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `Option<T::Hash>` | ```(None, '[u8; 32]')```
| error | `XcmError` | ```{'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'MultiLocationFull': None, 'MultiLocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'MaxWeightInvalid': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'UnhandledXcmVersion': None, 'WeightLimitReached': 'u64', 'Barrier': None, 'WeightNotComputable': None}```
| weight | `Weight` | ```u64```

---------
### OverweightEnqueued
An XCM exceeded the individual message weight budget.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `ParaId` | ```u32```
| sent_at | `RelayBlockNumber` | ```u32```
| index | `OverweightIndex` | ```u64```
| required | `Weight` | ```u64```

---------
### OverweightServiced
An XCM from the overweight queue was executed with the given actual weight used.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `OverweightIndex` | ```u64```
| used | `Weight` | ```u64```

---------
### Success
Some XCM was executed ok.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `Option<T::Hash>` | ```(None, '[u8; 32]')```
| weight | `Weight` | ```u64```

---------
### UpwardMessageSent
An upward message was sent to the relay chain.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `Option<T::Hash>` | ```(None, '[u8; 32]')```

---------
### XcmpMessageSent
An HRMP message was sent to a sibling parachain.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `Option<T::Hash>` | ```(None, '[u8; 32]')```

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
    'threshold_weight': 'u64',
    'weight_restrict_decay': 'u64',
    'xcmp_max_individual_weight': 'u64',
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