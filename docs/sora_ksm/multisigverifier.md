
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
        'EVM': 'scale_info::111',
        'EVMLegacy': 'u32',
        'Sub': (
            'Mainnet',
            'Kusama',
            'Polkadot',
            'Rococo',
            'Alphanet',
            'Liberland',
        ),
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
| None | `GenericNetworkId` | ```{'EVM': 'scale_info::111', 'Sub': ('Mainnet', 'Kusama', 'Polkadot', 'Rococo', 'Alphanet', 'Liberland'), 'EVMLegacy': 'u32'}```

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
| None | `GenericNetworkId` | ```{'EVM': 'scale_info::111', 'Sub': ('Mainnet', 'Kusama', 'Polkadot', 'Rococo', 'Alphanet', 'Liberland'), 'EVMLegacy': 'u32'}```

---------
## Storage functions

---------
### PeerKeys

#### Python
```python
result = substrate.query(
    'MultisigVerifier', 'PeerKeys', [
    {
        'EVM': 'scale_info::111',
        'EVMLegacy': 'u32',
        'Sub': (
            'Mainnet',
            'Kusama',
            'Polkadot',
            'Rococo',
            'Alphanet',
            'Liberland',
        ),
    },
]
)
```

#### Return value
```python
'scale_info::304'
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