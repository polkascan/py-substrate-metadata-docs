
# SubstrateBridgeInboundChannel

---------
## Calls

---------
### submit
#### Attributes
| Name | Type |
| -------- | -------- | 
| network_id | `SubNetworkId` | 
| commitment | `bridge_types::GenericCommitment<T::MaxMessagesPerCommit, T::
MaxMessagePayloadSize,>` | 
| proof | `<T::Verifier as Verifier>::Proof` | 

#### Python
```python
call = substrate.compose_call(
    'SubstrateBridgeInboundChannel', 'submit', {
    'commitment': {
        'EVM': {
            'messages': [
                {
                    'max_gas': 'scale_info::111',
                    'payload': 'Bytes',
                    'target': '[u8; 20]',
                },
            ],
            'nonce': 'u64',
            'total_max_gas': 'scale_info::111',
        },
        'Sub': {
            'messages': [
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
            ],
            'nonce': 'u64',
        },
    },
    'network_id': (
        'Mainnet',
        'Kusama',
        'Polkadot',
        'Rococo',
        'Alphanet',
        'Liberland',
    ),
    'proof': {
        'digest': {
            'logs': [
                {
                    'Commitment': (
                        {
                            'EVM': 'scale_info::111',
                            'EVMLegacy': 'u32',
                            'Sub': 'scale_info::105',
                        },
                        'scale_info::11',
                    ),
                },
            ],
        },
        'proof': ['[u8; 65]'],
    },
}
)
```

---------
## Storage functions

---------
### ChannelNonces

#### Python
```python
result = substrate.query(
    'SubstrateBridgeInboundChannel', 'ChannelNonces', [
    (
        'Mainnet',
        'Kusama',
        'Polkadot',
        'Rococo',
        'Alphanet',
        'Liberland',
    ),
]
)
```

#### Return value
```python
'u64'
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
constant = substrate.get_constant('SubstrateBridgeInboundChannel', 'ThisNetworkId')
```
---------
### UnsignedLongevity
 A configuration for longevity of unsigned transactions.
#### Value
```python
300
```
#### Python
```python
constant = substrate.get_constant('SubstrateBridgeInboundChannel', 'UnsignedLongevity')
```
---------
### UnsignedPriority
 A configuration for base priority of unsigned transactions.
#### Value
```python
1844674407370955161
```
#### Python
```python
constant = substrate.get_constant('SubstrateBridgeInboundChannel', 'UnsignedPriority')
```
---------
## Errors

---------
### CallEncodeFailed
Call encoding failed.

---------
### ContractExists
This contract already exists

---------
### InvalidCommitment
Submitted invalid commitment type.

---------
### InvalidNetwork
Message came from an invalid network.

---------
### InvalidNonce
Message has an unexpected nonce.

---------
### InvalidRewardFraction
Incorrect reward fraction

---------
### InvalidSourceChannel
Message came from an invalid outbound channel on the Ethereum side.

---------