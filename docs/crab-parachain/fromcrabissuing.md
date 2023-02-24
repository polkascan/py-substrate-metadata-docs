
# FromCrabIssuing

---------
## Calls

---------
### burn_and_remote_unlock
#### Attributes
| Name | Type |
| -------- | -------- | 
| spec_version | `u32` | 
| weight | `u64` | 
| gas_limit | `u128` | 
| value | `RingBalance<T>` | 
| fee | `RingBalance<T>` | 
| recipient | `H160` | 

#### Python
```python
call = substrate.compose_call(
    'FromCrabIssuing', 'burn_and_remote_unlock', {
    'fee': 'u128',
    'gas_limit': 'u128',
    'recipient': '[u8; 20]',
    'spec_version': 'u32',
    'value': 'u128',
    'weight': 'u64',
}
)
```

---------
### handle_issuing_failure_from_remote
#### Attributes
| Name | Type |
| -------- | -------- | 
| failure_nonce | `MessageNonce` | 
| burn_pruned_messages | `Vec<MessageNonce>` | 
| min_retain_received_nonce | `MessageNonce` | 

#### Python
```python
call = substrate.compose_call(
    'FromCrabIssuing', 'handle_issuing_failure_from_remote', {
    'burn_pruned_messages': ['u64'],
    'failure_nonce': 'u64',
    'min_retain_received_nonce': 'u64',
}
)
```

---------
### handle_issuing_failure_local
#### Attributes
| Name | Type |
| -------- | -------- | 
| failure_nonce | `MessageNonce` | 

#### Python
```python
call = substrate.compose_call(
    'FromCrabIssuing', 'handle_issuing_failure_local', {'failure_nonce': 'u64'}
)
```

---------
### issue_from_remote
Handle relay message sent from the source backing pallet with relay message
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `RingBalance<T>` | 
| recipient | `AccountId<T>` | 
| burn_pruned_messages | `Vec<MessageNonce>` | 
| min_retain_received_nonce | `MessageNonce` | 

#### Python
```python
call = substrate.compose_call(
    'FromCrabIssuing', 'issue_from_remote', {
    'burn_pruned_messages': ['u64'],
    'min_retain_received_nonce': 'u64',
    'recipient': 'AccountId',
    'value': 'u128',
}
)
```

---------
### remote_unlock_failure
#### Attributes
| Name | Type |
| -------- | -------- | 
| spec_version | `u32` | 
| weight | `u64` | 
| gas_limit | `u128` | 
| failure_nonce | `MessageNonce` | 
| fee | `RingBalance<T>` | 

#### Python
```python
call = substrate.compose_call(
    'FromCrabIssuing', 'remote_unlock_failure', {
    'failure_nonce': 'u64',
    'fee': 'u128',
    'gas_limit': 'u128',
    'spec_version': 'u32',
    'weight': 'u64',
}
)
```

---------
### set_remote_backing_account
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `AccountId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'FromCrabIssuing', 'set_remote_backing_account', {'account': 'AccountId'}
)
```

---------
### set_secure_limited_period
#### Attributes
| Name | Type |
| -------- | -------- | 
| period | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'FromCrabIssuing', 'set_secure_limited_period', {'period': 'u32'}
)
```

---------
### set_security_limitation_ring_amount
#### Attributes
| Name | Type |
| -------- | -------- | 
| limitation | `RingBalance<T>` | 

#### Python
```python
call = substrate.compose_call(
    'FromCrabIssuing', 'set_security_limitation_ring_amount', {'limitation': 'u128'}
)
```

---------
## Events

---------
### RemoteBackingAccountUpdated
Update remote backing address \[account\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId<T>` | ```AccountId```

---------
### RemoteUnlockForFailure
request remote unlock for failure issue [request_nonce, failure_nonce]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MessageNonce` | ```u64```
| None | `MessageNonce` | ```u64```

---------
### TokenBurnAndRemoteUnlocked
TokenBurnAndRemoteUnlocked \[lane_id, message_nonce, sender, recipient, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `LaneId` | ```[u8; 4]```
| None | `MessageNonce` | ```u64```
| None | `AccountId<T>` | ```AccountId```
| None | `H160` | ```[u8; 20]```
| None | `RingBalance<T>` | ```u128```

---------
### TokenIssued
[recipient, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId<T>` | ```AccountId```
| None | `RingBalance<T>` | ```u128```

---------
### TokenIssuedForFailure
issue for failure unlock [lane_id, failure_nonce, recipient, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `LaneId` | ```[u8; 4]```
| None | `MessageNonce` | ```u64```
| None | `AccountId<T>` | ```AccountId```
| None | `RingBalance<T>` | ```u128```

---------
## Storage functions

---------
### MinReservedBurnNonce

#### Python
```python
result = substrate.query(
    'FromCrabIssuing', 'MinReservedBurnNonce', []
)
```

#### Return value
```python
'u64'
```
---------
### ReceivedNonces

#### Python
```python
result = substrate.query(
    'FromCrabIssuing', 'ReceivedNonces', []
)
```

#### Return value
```python
['u64']
```
---------
### RemoteBackingAccount
 Remote Backing Address, this used to verify the remote caller

#### Python
```python
result = substrate.query(
    'FromCrabIssuing', 'RemoteBackingAccount', []
)
```

#### Return value
```python
'AccountId'
```
---------
### SecureLimitedPeriod
 Period between security limitation. Zero means there is no period limitation.

#### Python
```python
result = substrate.query(
    'FromCrabIssuing', 'SecureLimitedPeriod', []
)
```

#### Return value
```python
'u32'
```
---------
### SecureLimitedRingAmount

#### Python
```python
result = substrate.query(
    'FromCrabIssuing', 'SecureLimitedRingAmount', []
)
```

#### Return value
```python
('u128', 'u128')
```
---------
### TransactionInfos
 `(sender, amount)` the user *sender* lock and remote issuing amount of asset

#### Python
```python
result = substrate.query(
    'FromCrabIssuing', 'TransactionInfos', [('[u8; 4]', 'u64')]
)
```

#### Return value
```python
('AccountId', 'u128')
```
---------
## Constants

---------
### MaxReserves
 The maximum number of named reserves that can exist on an account.
#### Value
```python
4096
```
#### Python
```python
constant = substrate.get_constant('FromCrabIssuing', 'MaxReserves')
```
---------
### PalletId
 The pallet id of this pallet
#### Value
```python
'0x64612f7061616973'
```
#### Python
```python
constant = substrate.get_constant('FromCrabIssuing', 'PalletId')
```
---------
## Errors

---------
### BackingAccountNone
Backing not configured

---------
### EvmEncodeFailed
encode evm method failed

---------
### FailureInfoNE
Failure message not exist

---------
### FailureNonceInvalid
Failure message verify failed

---------
### InsufficientBalance
Insufficient balance.

---------
### MessageAlreadyIssued
Message has already issued

---------
### MessageNotDelived
the message has not delived

---------
### NonceDuplicated
Message nonce duplicated.

---------
### RingDailyLimited
Redeem Daily Limited

---------
### TooManyNonces
too many nonces received

---------