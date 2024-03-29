
# Proxy

---------
## Calls

---------
### add_proxy
See [`Pallet::add_proxy`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegate | `AccountIdLookupOf<T>` | 
| proxy_type | `T::ProxyType` | 
| delay | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Proxy', 'add_proxy', {
    'delay': 'u32',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'proxy_type': (
        'Any',
        'NonTransfer',
        'Governance',
        'Staking',
        'IdentityJudgement',
        'CancelProxy',
        'Auction',
        'Society',
        'NominationPools',
    ),
}
)
```

---------
### announce
See [`Pallet::announce`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| real | `AccountIdLookupOf<T>` | 
| call_hash | `CallHashOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Proxy', 'announce', {
    'call_hash': 'scale_info::12',
    'real': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### create_pure
See [`Pallet::create_pure`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| proxy_type | `T::ProxyType` | 
| delay | `BlockNumberFor<T>` | 
| index | `u16` | 

#### Python
```python
call = substrate.compose_call(
    'Proxy', 'create_pure', {
    'delay': 'u32',
    'index': 'u16',
    'proxy_type': (
        'Any',
        'NonTransfer',
        'Governance',
        'Staking',
        'IdentityJudgement',
        'CancelProxy',
        'Auction',
        'Society',
        'NominationPools',
    ),
}
)
```

---------
### kill_pure
See [`Pallet::kill_pure`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| spawner | `AccountIdLookupOf<T>` | 
| proxy_type | `T::ProxyType` | 
| index | `u16` | 
| height | `BlockNumberFor<T>` | 
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
        'NonTransfer',
        'Governance',
        'Staking',
        'IdentityJudgement',
        'CancelProxy',
        'Auction',
        'Society',
        'NominationPools',
    ),
    'spawner': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### proxy
See [`Pallet::proxy`].
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
            'NonTransfer',
            'Governance',
            'Staking',
            'IdentityJudgement',
            'CancelProxy',
            'Auction',
            'Society',
            'NominationPools',
        ),
    ),
    'real': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### proxy_announced
See [`Pallet::proxy_announced`].
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
        'Index': (),
        'Raw': 'Bytes',
    },
    'force_proxy_type': (
        None,
        (
            'Any',
            'NonTransfer',
            'Governance',
            'Staking',
            'IdentityJudgement',
            'CancelProxy',
            'Auction',
            'Society',
            'NominationPools',
        ),
    ),
    'real': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### reject_announcement
See [`Pallet::reject_announcement`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegate | `AccountIdLookupOf<T>` | 
| call_hash | `CallHashOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Proxy', 'reject_announcement', {
    'call_hash': 'scale_info::12',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### remove_announcement
See [`Pallet::remove_announcement`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| real | `AccountIdLookupOf<T>` | 
| call_hash | `CallHashOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Proxy', 'remove_announcement', {
    'call_hash': 'scale_info::12',
    'real': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### remove_proxies
See [`Pallet::remove_proxies`].
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
See [`Pallet::remove_proxy`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegate | `AccountIdLookupOf<T>` | 
| proxy_type | `T::ProxyType` | 
| delay | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Proxy', 'remove_proxy', {
    'delay': 'u32',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'proxy_type': (
        'Any',
        'NonTransfer',
        'Governance',
        'Staking',
        'IdentityJudgement',
        'CancelProxy',
        'Auction',
        'Society',
        'NominationPools',
    ),
}
)
```

---------
## Events

---------
### Announced
An announcement was placed to make a call in the future.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| real | `T::AccountId` | ```AccountId```
| proxy | `T::AccountId` | ```AccountId```
| call_hash | `CallHashOf<T>` | ```scale_info::12```

---------
### ProxyAdded
A proxy was added.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```AccountId```
| delegatee | `T::AccountId` | ```AccountId```
| proxy_type | `T::ProxyType` | ```('Any', 'NonTransfer', 'Governance', 'Staking', 'IdentityJudgement', 'CancelProxy', 'Auction', 'Society', 'NominationPools')```
| delay | `BlockNumberFor<T>` | ```u32```

---------
### ProxyExecuted
A proxy was executed correctly, with the given.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}}```

---------
### ProxyRemoved
A proxy was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```AccountId```
| delegatee | `T::AccountId` | ```AccountId```
| proxy_type | `T::ProxyType` | ```('Any', 'NonTransfer', 'Governance', 'Staking', 'IdentityJudgement', 'CancelProxy', 'Auction', 'Society', 'NominationPools')```
| delay | `BlockNumberFor<T>` | ```u32```

---------
### PureCreated
A pure account has been created by new proxy with given
disambiguation index and proxy type.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pure | `T::AccountId` | ```AccountId```
| who | `T::AccountId` | ```AccountId```
| proxy_type | `T::ProxyType` | ```('Any', 'NonTransfer', 'Governance', 'Staking', 'IdentityJudgement', 'CancelProxy', 'Auction', 'Society', 'NominationPools')```
| disambiguation_index | `u16` | ```u16```

---------
## Storage functions

---------
### Announcements
 The announcements made by the proxy (key).

#### Python
```python
result = substrate.query(
    'Proxy', 'Announcements', ['AccountId']
)
```

#### Return value
```python
([{'call_hash': 'scale_info::12', 'height': 'u32', 'real': 'AccountId'}], 'u128')
```
---------
### Proxies
 The set of account proxies. Maps the account which has delegated to the accounts
 which are being delegated to, together with the amount held on deposit.

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
                'NonTransfer',
                'Governance',
                'Staking',
                'IdentityJudgement',
                'CancelProxy',
                'Auction',
                'Society',
                'NominationPools',
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
 The base amount of currency needed to reserve for creating an announcement.

 This is held when a new storage item holding a `Balance` is created (typically 16
 bytes).
#### Value
```python
666933332400
```
#### Python
```python
constant = substrate.get_constant('Proxy', 'AnnouncementDepositBase')
```
---------
### AnnouncementDepositFactor
 The amount of currency needed per announcement made.

 This is held for adding an `AccountId`, `Hash` and `BlockNumber` (typically 68 bytes)
 into a pre-existing storage value.
#### Value
```python
2199997800
```
#### Python
```python
constant = substrate.get_constant('Proxy', 'AnnouncementDepositFactor')
```
---------
### MaxPending
 The maximum amount of time-delayed announcements that are allowed to be pending.
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
 The maximum amount of proxies allowed for a single account.
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
 The base amount of currency needed to reserve for creating a proxy.

 This is held for an additional storage item whose value size is
 `sizeof(Balance)` bytes and whose key size is `sizeof(AccountId)` bytes.
#### Value
```python
666933332400
```
#### Python
```python
constant = substrate.get_constant('Proxy', 'ProxyDepositBase')
```
---------
### ProxyDepositFactor
 The amount of currency needed per proxy added.

 This is held for adding 32 bytes plus an instance of `ProxyType` more into a
 pre-existing storage value. Thus, when configuring `ProxyDepositFactor` one should take
 into account `32 + proxy_type.encode().len()` bytes of data.
#### Value
```python
1099998900
```
#### Python
```python
constant = substrate.get_constant('Proxy', 'ProxyDepositFactor')
```
---------
## Errors

---------
### Duplicate
Account is already a proxy.

---------
### NoPermission
Call may not be made by proxy because it may escalate its privileges.

---------
### NoSelfProxy
Cannot add self as proxy.

---------
### NotFound
Proxy registration not found.

---------
### NotProxy
Sender is not a proxy of the account to be proxied.

---------
### TooMany
There are too many proxies registered or too many announcements pending.

---------
### Unannounced
Announcement, if made at all, was made too recently.

---------
### Unproxyable
A call which is incompatible with the proxy type&\#x27;s filter was attempted.

---------