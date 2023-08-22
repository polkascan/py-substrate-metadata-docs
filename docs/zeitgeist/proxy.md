
# Proxy

---------
## Calls

---------
### add_proxy
Register a proxy account for the sender that is able to make calls on its behalf.

The dispatch origin for this call must be _Signed_.

Parameters:
- `proxy`: The account that the `caller` would like to make a proxy.
- `proxy_type`: The permissions allowed for this proxy account.
- `delay`: The announcement period required of the initial proxy. Will generally be
zero.
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
    'delay': 'u64',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'proxy_type': (
        'Any',
        'CancelProxy',
        'Governance',
        'Staking',
        'CreateEditMarket',
        'ReportOutcome',
        'Dispute',
        'ProvideLiquidity',
        'BuySellCompleteSets',
        'Trading',
        'HandleAssets',
    ),
}
)
```

---------
### announce
Publish the hash of a proxy-call that will be made in the future.

This must be called some number of blocks before the corresponding `proxy` is attempted
if the delay associated with the proxy relationship is greater than zero.

No more than `MaxPending` announcements may be made at any one time.

This will take a deposit of `AnnouncementDepositFactor` as well as
`AnnouncementDepositBase` if there are no other pending announcements.

The dispatch origin for this call must be _Signed_ and a proxy of `real`.

Parameters:
- `real`: The account that the proxy will make a call on behalf of.
- `call_hash`: The hash of the call to be made by the `real` account.
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
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### create_pure
Spawn a fresh new account that is guaranteed to be otherwise inaccessible, and
initialize it with a proxy of `proxy_type` for `origin` sender.

Requires a `Signed` origin.

- `proxy_type`: The type of the proxy that the sender will be registered as over the
new account. This will almost always be the most permissive `ProxyType` possible to
allow for maximum flexibility.
- `index`: A disambiguation index, in case this is called multiple times in the same
transaction (e.g. with `utility::batch`). Unless you&\#x27;re using `batch` you probably just
want to use `0`.
- `delay`: The announcement period required of the initial proxy. Will generally be
zero.

Fails with `Duplicate` if this has already been called in this transaction, from the
same sender, with the same parameters.

Fails if there are insufficient funds to pay for deposit.
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
    'delay': 'u64',
    'index': 'u16',
    'proxy_type': (
        'Any',
        'CancelProxy',
        'Governance',
        'Staking',
        'CreateEditMarket',
        'ReportOutcome',
        'Dispute',
        'ProvideLiquidity',
        'BuySellCompleteSets',
        'Trading',
        'HandleAssets',
    ),
}
)
```

---------
### kill_pure
Removes a previously spawned pure proxy.

WARNING: **All access to this account will be lost.** Any funds held in it will be
inaccessible.

Requires a `Signed` origin, and the sender account must have been created by a call to
`pure` with corresponding parameters.

- `spawner`: The account that originally called `pure` to create this account.
- `index`: The disambiguation index originally passed to `pure`. Probably `0`.
- `proxy_type`: The proxy type originally passed to `pure`.
- `height`: The height of the chain when the call to `pure` was processed.
- `ext_index`: The extrinsic index in which the call to `pure` was processed.

Fails with `NoPermission` in case the caller is not a previously created pure
account whose `pure` call has corresponding parameters.
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
    'height': 'u64',
    'index': 'u16',
    'proxy_type': (
        'Any',
        'CancelProxy',
        'Governance',
        'Staking',
        'CreateEditMarket',
        'ReportOutcome',
        'Dispute',
        'ProvideLiquidity',
        'BuySellCompleteSets',
        'Trading',
        'HandleAssets',
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
Dispatch the given `call` from an account that the sender is authorised for through
`add_proxy`.

Removes any corresponding announcement(s).

The dispatch origin for this call must be _Signed_.

Parameters:
- `real`: The account that the proxy will make a call on behalf of.
- `force_proxy_type`: Specify the exact proxy type to be used and checked for this call.
- `call`: The call to be made by the `real` account.
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
            'Staking',
            'CreateEditMarket',
            'ReportOutcome',
            'Dispute',
            'ProvideLiquidity',
            'BuySellCompleteSets',
            'Trading',
            'HandleAssets',
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
Dispatch the given `call` from an account that the sender is authorized for through
`add_proxy`.

Removes any corresponding announcement(s).

The dispatch origin for this call must be _Signed_.

Parameters:
- `real`: The account that the proxy will make a call on behalf of.
- `force_proxy_type`: Specify the exact proxy type to be used and checked for this call.
- `call`: The call to be made by the `real` account.
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
            'CancelProxy',
            'Governance',
            'Staking',
            'CreateEditMarket',
            'ReportOutcome',
            'Dispute',
            'ProvideLiquidity',
            'BuySellCompleteSets',
            'Trading',
            'HandleAssets',
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
Remove the given announcement of a delegate.

May be called by a target (proxied) account to remove a call that one of their delegates
(`delegate`) has announced they want to execute. The deposit is returned.

The dispatch origin for this call must be _Signed_.

Parameters:
- `delegate`: The account that previously announced the call.
- `call_hash`: The hash of the call to be made.
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
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### remove_announcement
Remove a given announcement.

May be called by a proxy account to remove a call they previously announced and return
the deposit.

The dispatch origin for this call must be _Signed_.

Parameters:
- `real`: The account that the proxy will make a call on behalf of.
- `call_hash`: The hash of the call to be made by the `real` account.
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
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### remove_proxies
Unregister all proxy accounts for the sender.

The dispatch origin for this call must be _Signed_.

WARNING: This may be called on accounts created by `pure`, however if done, then
the unreserved fees will be inaccessible. **All access to this account will be lost.**
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
Unregister a proxy account for the sender.

The dispatch origin for this call must be _Signed_.

Parameters:
- `proxy`: The account that the `caller` would like to remove as a proxy.
- `proxy_type`: The permissions currently enabled for the removed proxy account.
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
    'delay': 'u64',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'proxy_type': (
        'Any',
        'CancelProxy',
        'Governance',
        'Staking',
        'CreateEditMarket',
        'ReportOutcome',
        'Dispute',
        'ProvideLiquidity',
        'BuySellCompleteSets',
        'Trading',
        'HandleAssets',
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
| call_hash | `CallHashOf<T>` | ```[u8; 32]```

---------
### ProxyAdded
A proxy was added.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```AccountId```
| delegatee | `T::AccountId` | ```AccountId```
| proxy_type | `T::ProxyType` | ```('Any', 'CancelProxy', 'Governance', 'Staking', 'CreateEditMarket', 'ReportOutcome', 'Dispute', 'ProvideLiquidity', 'BuySellCompleteSets', 'Trading', 'HandleAssets')```
| delay | `T::BlockNumber` | ```u64```

---------
### ProxyExecuted
A proxy was executed correctly, with the given.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### ProxyRemoved
A proxy was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| delegator | `T::AccountId` | ```AccountId```
| delegatee | `T::AccountId` | ```AccountId```
| proxy_type | `T::ProxyType` | ```('Any', 'CancelProxy', 'Governance', 'Staking', 'CreateEditMarket', 'ReportOutcome', 'Dispute', 'ProvideLiquidity', 'BuySellCompleteSets', 'Trading', 'HandleAssets')```
| delay | `T::BlockNumber` | ```u64```

---------
### PureCreated
A pure account has been created by new proxy with given
disambiguation index and proxy type.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pure | `T::AccountId` | ```AccountId```
| who | `T::AccountId` | ```AccountId```
| proxy_type | `T::ProxyType` | ```('Any', 'CancelProxy', 'Governance', 'Staking', 'CreateEditMarket', 'ReportOutcome', 'Dispute', 'ProvideLiquidity', 'BuySellCompleteSets', 'Trading', 'HandleAssets')```
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
([{'call_hash': '[u8; 32]', 'height': 'u64', 'real': 'AccountId'}], 'u128')
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
            'delay': 'u64',
            'delegate': 'AccountId',
            'proxy_type': (
                'Any',
                'CancelProxy',
                'Governance',
                'Staking',
                'CreateEditMarket',
                'ReportOutcome',
                'Dispute',
                'ProvideLiquidity',
                'BuySellCompleteSets',
                'Trading',
                'HandleAssets',
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
15006000000
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
49500000
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
15006000000
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
24750000
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