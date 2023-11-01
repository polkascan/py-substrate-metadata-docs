
# MultisigVerifier

---------
## Calls

---------
### add_peer
#### Attributes
| Name | Type |
| -------- | -------- | 
| peer | `ecdsa::Public` | 

#### Python
```python
call = substrate.compose_call(
    'MultisigVerifier', 'add_peer', {'peer': '[u8; 33]'}
)
```

---------
### initialize
#### Attributes
| Name | Type |
| -------- | -------- | 
| network_id | `GenericNetworkId` | 
| peers | `BoundedVec<ecdsa::Public, T::MaxPeers>` | 

#### Python
```python
call = substrate.compose_call(
    'MultisigVerifier', 'initialize', {
    'network_id': {
        'EVM': '[u64; 4]',
        'EVMLegacy': 'u32',
        'Sub': {
            'Custom': 'u32',
            'Kusama': None,
            'Mainnet': None,
            'Polkadot': None,
            'Rococo': None,
        },
    },
    'peers': ['[u8; 33]'],
}
)
```

---------
### remove_peer
#### Attributes
| Name | Type |
| -------- | -------- | 
| peer | `ecdsa::Public` | 

#### Python
```python
call = substrate.compose_call(
    'MultisigVerifier', 'remove_peer', {'peer': '[u8; 33]'}
)
```

---------
## Events

---------
### NetworkInitialized
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `GenericNetworkId` | ```{'EVM': '[u64; 4]', 'Sub': {'Mainnet': None, 'Kusama': None, 'Polkadot': None, 'Rococo': None, 'Custom': 'u32'}, 'EVMLegacy': 'u32'}```

---------
### PeerAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ecdsa::Public` | ```[u8; 33]```

---------
### PeerRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ecdsa::Public` | ```[u8; 33]```

---------
### VerificationSuccessful
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `GenericNetworkId` | ```{'EVM': '[u64; 4]', 'Sub': {'Mainnet': None, 'Kusama': None, 'Polkadot': None, 'Rococo': None, 'Custom': 'u32'}, 'EVMLegacy': 'u32'}```

---------
## Storage functions

---------
### PeerKeys

#### Python
```python
result = substrate.query(
    'MultisigVerifier', 'PeerKeys', [
    {
        'EVM': '[u64; 4]',
        'EVMLegacy': 'u32',
        'Sub': {
            'Custom': 'u32',
            'Kusama': None,
            'Mainnet': None,
            'Polkadot': None,
            'Rococo': None,
        },
    },
]
)
```

#### Return value
```python
'scale_info::318'
```
---------
## Constants

---------
### MaxPeers
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('MultisigVerifier', 'MaxPeers')
```
---------
### ThisNetworkId
#### Value
```python
{'Sub': 'Kusama'}
```
#### Python
```python
constant = substrate.get_constant('MultisigVerifier', 'ThisNetworkId')
```
---------
## Errors

---------
### CommitmentNotFoundInDigest

---------
### DuplicatedPeer

---------
### InvalidInitParams

---------
### InvalidNetworkId

---------
### InvalidNumberOfSignatures

---------
### InvalidSignature

---------
### NetworkNotInitialized

---------
### NoSuchPeer

---------
### NotTrustedPeerSignature

---------
### PeerExists

---------
### TooMuchPeers

---------