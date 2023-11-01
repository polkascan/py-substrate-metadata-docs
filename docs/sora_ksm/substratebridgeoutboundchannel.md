
# SubstrateBridgeOutboundChannel

---------
## Events

---------
### MessageAccepted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| network_id | `SubNetworkId` | ```{'Mainnet': None, 'Kusama': None, 'Polkadot': None, 'Rococo': None, 'Custom': 'u32'}```
| batch_nonce | `u64` | ```u64```
| message_nonce | `MessageNonce` | ```u64```

---------
## Storage functions

---------
### ChannelNonces

#### Python
```python
result = substrate.query(
    'SubstrateBridgeOutboundChannel', 'ChannelNonces', [
    {
        'Custom': 'u32',
        'Kusama': None,
        'Mainnet': None,
        'Polkadot': None,
        'Rococo': None,
    },
]
)
```

#### Return value
```python
'u64'
```
---------
### Interval
 Interval between committing messages.

#### Python
```python
result = substrate.query(
    'SubstrateBridgeOutboundChannel', 'Interval', []
)
```

#### Return value
```python
'u32'
```
---------
### LatestCommitment

#### Python
```python
result = substrate.query(
    'SubstrateBridgeOutboundChannel', 'LatestCommitment', [
    {
        'Custom': 'u32',
        'Kusama': None,
        'Mainnet': None,
        'Polkadot': None,
        'Rococo': None,
    },
]
)
```

#### Return value
```python
{
    'block_number': 'u32',
    'commitment': {
        'EVM': {
            'messages': [
                {
                    'max_gas': '[u64; 4]',
                    'payload': 'Bytes',
                    'target': '[u8; 20]',
                },
            ],
            'nonce': 'u64',
            'total_max_gas': '[u64; 4]',
        },
        'Sub': {
            'messages': [{'payload': 'Bytes', 'timepoint': 'scale_info::287'}],
            'nonce': 'u64',
        },
    },
}
```
---------
### MessageQueues
 Messages waiting to be committed. To update the queue, use `append_message_queue` and `take_message_queue` methods
 (to keep correct value in [QueuesTotalGas]).

#### Python
```python
result = substrate.query(
    'SubstrateBridgeOutboundChannel', 'MessageQueues', [
    {
        'Custom': 'u32',
        'Kusama': None,
        'Mainnet': None,
        'Polkadot': None,
        'Rococo': None,
    },
]
)
```

#### Return value
```python
[
    {
        'payload': 'Bytes',
        'timepoint': {
            'EVM': 'u64',
            'Parachain': 'u32',
            'Pending': None,
            'Sora': 'u32',
            'Unknown': None,
        },
    },
]
```
---------
## Constants

---------
### ThisNetworkId
#### Value
```python
{'Sub': 'Kusama'}
```
#### Python
```python
constant = substrate.get_constant('SubstrateBridgeOutboundChannel', 'ThisNetworkId')
```
---------
## Errors

---------
### ChannelExists
This channel already exists

---------
### MaxGasTooBig
Maximum gas for queued batch exceeds limit.

---------
### NoFunds
Cannot pay the fee to submit a message.

---------
### Overflow
Cannot increment nonce

---------
### PayloadTooLarge
The message payload exceeds byte limit.

---------
### QueueSizeLimitReached
No more messages can be queued for the channel during this commit cycle.

---------