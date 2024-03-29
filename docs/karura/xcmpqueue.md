
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
## Events

---------
### XcmpMessageSent
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message_hash | `XcmHash` | ```[u8; 32]```

---------
## Storage functions

---------
### DeliveryFeeFactor

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

#### Python
```python
result = substrate.query(
    'XcmpQueue', 'InboundXcmpSuspended', []
)
```

#### Return value
```python
'scale_info::470'
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
## Constants

---------
### MaxInboundSuspended
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

---------
### AlreadySuspended

---------
### BadQueueConfig

---------