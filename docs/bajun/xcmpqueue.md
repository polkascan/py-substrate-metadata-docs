
# XcmpQueue

---------
## Calls

---------
### resume_xcm_execution
See [`Pallet::resume_xcm_execution`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'XcmpQueue', 'resume_xcm_execution', {}
)
```

---------
### suspend_xcm_execution
See [`Pallet::suspend_xcm_execution`].
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
See [`Pallet::update_drop_threshold`].
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
See [`Pallet::update_resume_threshold`].
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
See [`Pallet::update_suspend_threshold`].
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
## Events

---------
### XcmpMessageSent
An HRMP message was sent to a sibling parachain.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `XcmHash` | ```[u8; 32]```

---------
## Storage functions

---------
### DeliveryFeeFactor
 The factor to multiply the base delivery fee by.

#### Python
```python
result = substrate.query(
    'XcmpQueue', 'DeliveryFeeFactor', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### InboundXcmpSuspended
 The suspended inbound XCMP channels. All others are not suspended.

 This is a `StorageValue` instead of a `StorageMap` since we expect multiple reads per block
 to different keys with a one byte payload. The access to `BoundedBTreeSet` will be cached
 within the block and therefore only included once in the proof size.

 NOTE: The PoV benchmarking cannot know this and will over-estimate, but the actual proof
 will be smaller.

#### Python
```python
result = substrate.query(
    'XcmpQueue', 'InboundXcmpSuspended', []
)
```

#### Return value
```python
'scale_info::458'
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
## Constants

---------
### MaxInboundSuspended
 The maximum number of inbound XCMP channels that can be suspended simultaneously.

 Any further channel suspensions will fail and messages may get dropped without further
 notice. Choosing a high value (1000) is okay; the trade-off that is described in
 [`InboundXcmpSuspended`] still applies at that scale.
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('XcmpQueue', 'MaxInboundSuspended')
```
---------
## Errors

---------
### AlreadyResumed
The execution is already resumed.

---------
### AlreadySuspended
The execution is already suspended.

---------
### BadQueueConfig
Setting the queue config failed since one of its values was invalid.

---------