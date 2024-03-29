
# PhalaMq

---------
## Calls

---------
### force_push_pallet_message
See [`Pallet::force_push_pallet_message`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| destination | `Vec<u8>` | 
| payload | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaMq', 'force_push_pallet_message', {
    'destination': 'Bytes',
    'payload': 'Bytes',
}
)
```

---------
### push_message
See [`Pallet::push_message`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| destination | `Vec<u8>` | 
| payload | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaMq', 'push_message', {
    'destination': 'Bytes',
    'payload': 'Bytes',
}
)
```

---------
### sync_offchain_message
See [`Pallet::sync_offchain_message`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| signed_message | `SignedMessage` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaMq', 'sync_offchain_message', {
    'signed_message': {
        'message': {
            'destination': 'Bytes',
            'payload': 'Bytes',
            'sender': {
                'AccountId': 'scale_info::12',
                'Cluster': 'scale_info::12',
                'Contract': 'scale_info::12',
                'Gatekeeper': None,
                'MultiLocation': 'Bytes',
                'Pallet': 'Bytes',
                'Reserved': None,
                'Worker': '[u8; 32]',
                None: None,
            },
        },
        'sequence': 'u64',
        'signature': 'Bytes',
    },
}
)
```

---------
## Storage functions

---------
### OffchainIngress
 The next expected sequence of a ingress message coming from a certain sender (origin)

#### Python
```python
result = substrate.query(
    'PhalaMq', 'OffchainIngress', [
    {
        'AccountId': 'scale_info::12',
        'Cluster': 'scale_info::12',
        'Contract': 'scale_info::12',
        'Gatekeeper': None,
        'MultiLocation': 'Bytes',
        'Pallet': 'Bytes',
        'Reserved': None,
        'Worker': '[u8; 32]',
        None: None,
    },
]
)
```

#### Return value
```python
'u64'
```
---------
### OutboundMessages
 Outbound messages at the current block.

 It will be cleared at the beginning of every block.

#### Python
```python
result = substrate.query(
    'PhalaMq', 'OutboundMessages', []
)
```

#### Return value
```python
[
    {
        'destination': 'Bytes',
        'payload': 'Bytes',
        'sender': {
            'AccountId': 'scale_info::12',
            'Cluster': 'scale_info::12',
            'Contract': 'scale_info::12',
            'Gatekeeper': None,
            'MultiLocation': 'Bytes',
            'Pallet': 'Bytes',
            'Reserved': None,
            'Worker': '[u8; 32]',
            None: None,
        },
    },
]
```
---------
### QueuedOutboundMessage

#### Python
```python
result = substrate.query(
    'PhalaMq', 'QueuedOutboundMessage', []
)
```

#### Return value
```python
[
    {
        'destination': 'Bytes',
        'payload': 'Bytes',
        'sender': {
            'AccountId': 'scale_info::12',
            'Cluster': 'scale_info::12',
            'Contract': 'scale_info::12',
            'Gatekeeper': None,
            'MultiLocation': 'Bytes',
            'Pallet': 'Bytes',
            'Reserved': None,
            'Worker': '[u8; 32]',
            None: None,
        },
    },
]
```
---------
## Errors

---------
### BadDestination

---------
### BadSender

---------
### BadSequence

---------