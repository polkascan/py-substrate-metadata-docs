
# BridgeDataSigner

---------
## Calls

---------
### add_peer
#### Attributes
| Name | Type |
| -------- | -------- | 
| network_id | `GenericNetworkId` | 
| peer | `ecdsa::Public` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeDataSigner', 'add_peer', {
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
    'peer': '[u8; 33]',
}
)
```

---------
### approve
#### Attributes
| Name | Type |
| -------- | -------- | 
| network_id | `GenericNetworkId` | 
| data | `H256` | 
| signature | `ecdsa::Signature` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeDataSigner', 'approve', {
    'data': 'scale_info::11',
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
    'signature': '[u8; 65]',
}
)
```

---------
### finish_add_peer
#### Attributes
| Name | Type |
| -------- | -------- | 
| peer | `ecdsa::Public` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeDataSigner', 'finish_add_peer', {'peer': '[u8; 33]'}
)
```

---------
### finish_remove_peer
#### Attributes
| Name | Type |
| -------- | -------- | 
| peer | `ecdsa::Public` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeDataSigner', 'finish_remove_peer', {'peer': '[u8; 33]'}
)
```

---------
### register_network
#### Attributes
| Name | Type |
| -------- | -------- | 
| network_id | `GenericNetworkId` | 
| peers | `BoundedVec<ecdsa::Public, T::MaxPeers>` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeDataSigner', 'register_network', {
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
| network_id | `GenericNetworkId` | 
| peer | `ecdsa::Public` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeDataSigner', 'remove_peer', {
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
    'peer': '[u8; 33]',
}
)
```

---------
## Events

---------
### AddedPeer
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| network_id | `GenericNetworkId` | ```{'EVM': 'scale_info::111', 'Sub': ('Mainnet', 'Kusama', 'Polkadot', 'Rococo', 'Alphanet', 'Liberland'), 'EVMLegacy': 'u32'}```
| peer | `ecdsa::Public` | ```[u8; 33]```

---------
### ApprovalAccepted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| network_id | `GenericNetworkId` | ```{'EVM': 'scale_info::111', 'Sub': ('Mainnet', 'Kusama', 'Polkadot', 'Rococo', 'Alphanet', 'Liberland'), 'EVMLegacy': 'u32'}```
| data | `H256` | ```scale_info::11```
| signature | `ecdsa::Signature` | ```[u8; 65]```

---------
### Approved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| network_id | `GenericNetworkId` | ```{'EVM': 'scale_info::111', 'Sub': ('Mainnet', 'Kusama', 'Polkadot', 'Rococo', 'Alphanet', 'Liberland'), 'EVMLegacy': 'u32'}```
| data | `H256` | ```scale_info::11```
| signatures | `BoundedVec<ecdsa::Signature, T::MaxPeers>` | ```['[u8; 65]']```

---------
### Initialized
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| network_id | `GenericNetworkId` | ```{'EVM': 'scale_info::111', 'Sub': ('Mainnet', 'Kusama', 'Polkadot', 'Rococo', 'Alphanet', 'Liberland'), 'EVMLegacy': 'u32'}```
| peers | `BoundedVec<ecdsa::Public, T::MaxPeers>` | ```['[u8; 33]']```

---------
### RemovedPeer
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| network_id | `GenericNetworkId` | ```{'EVM': 'scale_info::111', 'Sub': ('Mainnet', 'Kusama', 'Polkadot', 'Rococo', 'Alphanet', 'Liberland'), 'EVMLegacy': 'u32'}```
| peer | `ecdsa::Public` | ```[u8; 33]```

---------
## Storage functions

---------
### Approvals
 Approvals

#### Python
```python
result = substrate.query(
    'BridgeDataSigner', 'Approvals', [
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
    'scale_info::11',
]
)
```

#### Return value
```python
'scale_info::307'
```
---------
### Peers
 Peers

#### Python
```python
result = substrate.query(
    'BridgeDataSigner', 'Peers', [
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
### PendingPeerUpdate
 Pending peers

#### Python
```python
result = substrate.query(
    'BridgeDataSigner', 'PendingPeerUpdate', [
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
'bool'
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
constant = substrate.get_constant('BridgeDataSigner', 'MaxPeers')
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
constant = substrate.get_constant('BridgeDataSigner', 'UnsignedLongevity')
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
constant = substrate.get_constant('BridgeDataSigner', 'UnsignedPriority')
```
---------
## Errors

---------
### ApprovalsNotFound

---------
### DontHavePendingPeerUpdates

---------
### FailedToVerifySignature

---------
### HasPendingPeerUpdate

---------
### NetworkNotSupported

---------
### PalletInitialized

---------
### PalletNotInitialized

---------
### PeerExists

---------
### PeerNotExists

---------
### PeerNotFound

---------
### SignatureAlreadyExists

---------
### SignaturesNotFound

---------
### TooMuchApprovals

---------
### TooMuchPeers

---------