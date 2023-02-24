
# Proxy

---------
## Calls

---------
### add_proxy
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegate | `AccountIdLookupOf<T>` | 
| proxy_type | `T::ProxyType` | 
| delay | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Proxy', 'add_proxy', {
    'delay': 'u32',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'proxy_type': (
        'Any',
        'CancelProxy',
        'Governance',
        'Auction',
        'Swap',
        'Loan',
        'DexLiquidity',
        'StableAssetSwap',
        'StableAssetLiquidity',
        'Homa',
    ),
}
)
```

---------
### announce
#### Attributes
| Name | Type |
| -------- | -------- | 
| real | `AccountIdLookupOf<T>` | 
| call_hash | `CallHashOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Proxy', 'announce', {
    'call_hash': '[u8; 32]',
    'real': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### create_pure
#### Attributes
| Name | Type |
| -------- | -------- | 
| proxy_type | `T::ProxyType` | 
| delay | `T::BlockNumber` | 
| index | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'Proxy', 'create_pure', {
    'delay': 'u32',
    'index': 'u16',
    'proxy_type': (
        'Any',
        'CancelProxy',
        'Governance',
        'Auction',
        'Swap',
        'Loan',
        'DexLiquidity',
        'StableAssetSwap',
        'StableAssetLiquidity',
        'Homa',
    ),
}
)
```

---------
### kill_pure
#### Attributes
| Name | Type |
| -------- | -------- | 
| spawner | `AccountIdLookupOf<T>` | 
| proxy_type | `T::ProxyType` | 
| index | `u16` | 
| height | `T::BlockNumber` | 
| ext_index | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Proxy', 'kill_pure', {
    'ext_index': 'u32',
    'height': 'u32',
    'index': 'u16',
    'proxy_type': (
        'Any',
        'CancelProxy',
        'Governance',
        'Auction',
        'Swap',
        'Loan',
        'DexLiquidity',
        'StableAssetSwap',
        'StableAssetLiquidity',
        'Homa',
    ),
    'spawner': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### proxy
#### Attributes
| Name | Type |
| -------- | -------- | 
| real | `AccountIdLookupOf<T>` | 
| force_proxy_type | `Option<T::ProxyType>` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Proxy', 'proxy', {
    'call': 'Call',
    'force_proxy_type': (
        None,
        (
            'Any',
            'CancelProxy',
            'Governance',
            'Auction',
            'Swap',
            'Loan',
            'DexLiquidity',
            'StableAssetSwap',
            'StableAssetLiquidity',
            'Homa',
        ),
    ),
    'real': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### proxy_announced
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegate | `AccountIdLookupOf<T>` | 
| real | `AccountIdLookupOf<T>` | 
| force_proxy_type | `Option<T::ProxyType>` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Proxy', 'proxy_announced', {
    'call': 'Call',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'force_proxy_type': (
        None,
        (
            'Any',
            'CancelProxy',
            'Governance',
            'Auction',
            'Swap',
            'Loan',
            'DexLiquidity',
            'StableAssetSwap',
            'StableAssetLiquidity',
            'Homa',
        ),
    ),
    'real': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### reject_announcement
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegate | `AccountIdLookupOf<T>` | 
| call_hash | `CallHashOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Proxy', 'reject_announcement', {
    'call_hash': '[u8; 32]',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### remove_announcement
#### Attributes
| Name | Type |
| -------- | -------- | 
| real | `AccountIdLookupOf<T>` | 
| call_hash | `CallHashOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Proxy', 'remove_announcement', {
    'call_hash': '[u8; 32]',
    'real': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### remove_proxies
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Proxy', 'remove_proxies', {}
)
```

---------
### remove_proxy
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegate | `AccountIdLookupOf<T>` | 
| proxy_type | `T::ProxyType` | 
| delay | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Proxy', 'remove_proxy', {
    'delay': 'u32',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'proxy_type': (
        'Any',
        'CancelProxy',
        'Governance',
        'Auction',
        'Swap',
        'Loan',
        'DexLiquidity',
        'StableAssetSwap',
        'StableAssetLiquidity',
        'Homa',
    ),
}
)
```

---------
## Events

---------
### Announced
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| real | `T::AccountId` | ```AccountId```
| proxy | `T::AccountId` | ```AccountId```
| call_hash | `CallHashOf<T>` | ```[u8; 32]```

---------
### ProxyAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```AccountId```
| delegatee | `T::AccountId` | ```AccountId```
| proxy_type | `T::ProxyType` | ```('Any', 'CancelProxy', 'Governance', 'Auction', 'Swap', 'Loan', 'DexLiquidity', 'StableAssetSwap', 'StableAssetLiquidity', 'Homa')```
| delay | `T::BlockNumber` | ```u32```

---------
### ProxyExecuted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### ProxyRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```AccountId```
| delegatee | `T::AccountId` | ```AccountId```
| proxy_type | `T::ProxyType` | ```('Any', 'CancelProxy', 'Governance', 'Auction', 'Swap', 'Loan', 'DexLiquidity', 'StableAssetSwap', 'StableAssetLiquidity', 'Homa')```
| delay | `T::BlockNumber` | ```u32```

---------
### PureCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pure | `T::AccountId` | ```AccountId```
| who | `T::AccountId` | ```AccountId```
| proxy_type | `T::ProxyType` | ```('Any', 'CancelProxy', 'Governance', 'Auction', 'Swap', 'Loan', 'DexLiquidity', 'StableAssetSwap', 'StableAssetLiquidity', 'Homa')```
| disambiguation_index | `u16` | ```u16```

---------
## Storage functions

---------
### Announcements

#### Python
```python
result = substrate.query(
    'Proxy', 'Announcements', ['AccountId']
)
```

#### Return value
```python
([{'call_hash': '[u8; 32]', 'height': 'u32', 'real': 'AccountId'}], 'u128')
```
---------
### Proxies

#### Python
```python
result = substrate.query(
    'Proxy', 'Proxies', ['AccountId']
)
```

#### Return value
```python
(
    [
        {
            'delay': 'u32',
            'delegate': 'AccountId',
            'proxy_type': (
                'Any',
                'CancelProxy',
                'Governance',
                'Auction',
                'Swap',
                'Loan',
                'DexLiquidity',
                'StableAssetSwap',
                'StableAssetLiquidity',
                'Homa',
            ),
        },
    ],
    'u128',
)
```
---------
## Constants

---------
### AnnouncementDepositBase
#### Value
```python
2002400000000
```
#### Python
```python
constant = substrate.get_constant('Proxy', 'AnnouncementDepositBase')
```
---------
### AnnouncementDepositFactor
#### Value
```python
19800000000
```
#### Python
```python
constant = substrate.get_constant('Proxy', 'AnnouncementDepositFactor')
```
---------
### MaxPending
#### Value
```python
32
```
#### Python
```python
constant = substrate.get_constant('Proxy', 'MaxPending')
```
---------
### MaxProxies
#### Value
```python
32
```
#### Python
```python
constant = substrate.get_constant('Proxy', 'MaxProxies')
```
---------
### ProxyDepositBase
#### Value
```python
2002400000000
```
#### Python
```python
constant = substrate.get_constant('Proxy', 'ProxyDepositBase')
```
---------
### ProxyDepositFactor
#### Value
```python
9900000000
```
#### Python
```python
constant = substrate.get_constant('Proxy', 'ProxyDepositFactor')
```
---------
## Errors

---------
### Duplicate

---------
### NoPermission

---------
### NoSelfProxy

---------
### NotFound

---------
### NotProxy

---------
### TooMany

---------
### Unannounced

---------
### Unproxyable

---------