
# Bridge

---------
## Calls

---------
### add_freeze_admin
Add a freeze admin.

\#\# Errors
- `BadAdmin` if `origin` is not `Self::admin()` account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| freeze_admin | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'add_freeze_admin', {'freeze_admin': 'AccountId'}
)
```

---------
### batch_propose_bridge_tx
Proposes a vector of bridge transactions. The vector is processed until the first
proposal which causes an error, in which case the error is returned and the rest of
proposals are not processed.

\#\# Errors
- `ControllerNotSet` if `Controllers` was not set.

\# Weight
`500_000_000 + 7_000_000 * bridge_txs.len()`
#### Attributes
| Name | Type |
| -------- | -------- | 
| bridge_txs | `Vec<BridgeTx<T::AccountId>>` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'batch_propose_bridge_tx', {
    'bridge_txs': [
        {
            'amount': 'u128',
            'nonce': 'u32',
            'recipient': 'AccountId',
            'tx_hash': 'scale_info::11',
        },
    ],
}
)
```

---------
### change_admin
Changes the bridge admin key.

\#\# Errors
- `BadAdmin` if `origin` is not `Self::admin()` account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| admin | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'change_admin', {'admin': 'AccountId'}
)
```

---------
### change_bridge_exempted
Changes the bridge limit exempted list.

\#\# Errors
- `BadAdmin` if `origin` is not `Self::admin()` account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| exempted | `Vec<(IdentityId, bool)>` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'change_bridge_exempted', {'exempted': [('[u8; 32]', 'bool')]}
)
```

---------
### change_bridge_limit
Changes the bridge limits.

\#\# Errors
- `BadAdmin` if `origin` is not `Self::admin()` account.
- `DivisionByZero` if `duration` is zero.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 
| duration | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'change_bridge_limit', {'amount': 'u128', 'duration': 'u32'}
)
```

---------
### change_controller
Changes the controller account as admin.

\#\# Errors
- `BadAdmin` if `origin` is not `Self::admin()` account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| controller | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'change_controller', {'controller': 'AccountId'}
)
```

---------
### change_timelock
Changes the timelock period.

\#\# Errors
- `BadAdmin` if `origin` is not `Self::admin()` account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| timelock | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'change_timelock', {'timelock': 'u32'}
)
```

---------
### force_handle_bridge_tx
Forces handling a transaction by bypassing the bridge limit and timelock.

\#\# Errors
- `BadAdmin` if `origin` is not `Self::admin()` account.
- `NoValidCdd` if `bridge_tx.recipient` does not have a valid CDD claim.
#### Attributes
| Name | Type |
| -------- | -------- | 
| bridge_tx | `BridgeTx<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'force_handle_bridge_tx', {
    'bridge_tx': {
        'amount': 'u128',
        'nonce': 'u32',
        'recipient': 'AccountId',
        'tx_hash': 'scale_info::11',
    },
}
)
```

---------
### freeze
Freezes transaction handling in the bridge module if it is not already frozen. When the
bridge is frozen, attempted transactions get postponed instead of getting handled.

\#\# Errors
- `BadAdmin` if `origin` is not `Self::admin()` account.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'freeze', {}
)
```

---------
### freeze_txs
Freezes given bridge transactions.
If any bridge txn is already handled then this function will just ignore it and process next one.

\#\# Errors
- `BadAdmin` if `origin` is not `Self::admin()` account.

\# Weight
`400_000_000 + 2_000_000 * bridge_txs.len()`
#### Attributes
| Name | Type |
| -------- | -------- | 
| bridge_txs | `Vec<BridgeTx<T::AccountId>>` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'freeze_txs', {
    'bridge_txs': [
        {
            'amount': 'u128',
            'nonce': 'u32',
            'recipient': 'AccountId',
            'tx_hash': 'scale_info::11',
        },
    ],
}
)
```

---------
### handle_bridge_tx
Handles an approved bridge transaction proposal.

\#\# Errors
- `BadCaller` if `origin` is not `Self::controller` or  `Self::admin`.
- `TimelockedTx` if the transaction status is `Timelocked`.
- `ProposalAlreadyHandled` if the transaction status is `Handled`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| bridge_tx | `BridgeTx<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'handle_bridge_tx', {
    'bridge_tx': {
        'amount': 'u128',
        'nonce': 'u32',
        'recipient': 'AccountId',
        'tx_hash': 'scale_info::11',
    },
}
)
```

---------
### handle_scheduled_bridge_tx
Root callable extrinsic, used as an internal call to handle a scheduled timelocked bridge transaction.

\# Errors
- `BadOrigin` if `origin` is not root.
- `ProposalAlreadyHandled` if transaction status is `Handled`.
- `FrozenTx` if transaction status is `Frozen`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| bridge_tx | `BridgeTx<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'handle_scheduled_bridge_tx', {
    'bridge_tx': {
        'amount': 'u128',
        'nonce': 'u32',
        'recipient': 'AccountId',
        'tx_hash': 'scale_info::11',
    },
}
)
```

---------
### propose_bridge_tx
Proposes a bridge transaction, which amounts to making a multisig proposal for the
bridge transaction if the transaction is new or approving an existing proposal if the
transaction has already been proposed.

\#\# Errors
- `ControllerNotSet` if `Controllers` was not set.
#### Attributes
| Name | Type |
| -------- | -------- | 
| bridge_tx | `BridgeTx<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'propose_bridge_tx', {
    'bridge_tx': {
        'amount': 'u128',
        'nonce': 'u32',
        'recipient': 'AccountId',
        'tx_hash': 'scale_info::11',
    },
}
)
```

---------
### remove_freeze_admin
Remove a freeze admin.

\#\# Errors
- `BadAdmin` if `origin` is not `Self::admin()` account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| freeze_admin | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'remove_freeze_admin', {'freeze_admin': 'AccountId'}
)
```

---------
### remove_txs
Remove given bridge transactions.

\#\# Errors
- `BadAdmin` if `origin` is not `Self::admin()` account.
- `NotFrozen` if a tx in `bridge_txs` is not frozen.
#### Attributes
| Name | Type |
| -------- | -------- | 
| bridge_txs | `Vec<BridgeTx<T::AccountId>>` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'remove_txs', {
    'bridge_txs': [
        {
            'amount': 'u128',
            'nonce': 'u32',
            'recipient': 'AccountId',
            'tx_hash': 'scale_info::11',
        },
    ],
}
)
```

---------
### unfreeze
Unfreezes transaction handling in the bridge module if it is frozen.

\#\# Errors
- `BadAdmin` if `origin` is not `Self::admin()` account.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'unfreeze', {}
)
```

---------
### unfreeze_txs
Unfreezes given bridge transactions.
If any bridge txn is already handled then this function will just ignore it and process next one.

\#\# Errors
- `BadAdmin` if `origin` is not `Self::admin()` account.

\# Weight
`400_000_000 + 7_000_000 * bridge_txs.len()`
#### Attributes
| Name | Type |
| -------- | -------- | 
| bridge_txs | `Vec<BridgeTx<T::AccountId>>` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'unfreeze_txs', {
    'bridge_txs': [
        {
            'amount': 'u128',
            'nonce': 'u32',
            'recipient': 'AccountId',
            'tx_hash': 'scale_info::11',
        },
    ],
}
)
```

---------
## Events

---------
### AdminChanged
Confirmation of Admin change.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```

---------
### BridgeLimitUpdated
Bridge limit has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Balance` | ```u128```
| None | `BlockNumber` | ```u32```

---------
### BridgeTxFailed
Bridge Tx failed.  Recipient missing CDD or limit reached.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `BridgeTx<AccountId>` | ```{'nonce': 'u32', 'recipient': 'AccountId', 'amount': 'u128', 'tx_hash': 'scale_info::11'}```
| None | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
### BridgeTxScheduleFailed
Failed to schedule Bridge Tx.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `BridgeTx<AccountId>` | ```{'nonce': 'u32', 'recipient': 'AccountId', 'amount': 'u128', 'tx_hash': 'scale_info::11'}```
| None | `Vec<u8>` | ```Bytes```

---------
### BridgeTxScheduled
Bridge Tx Scheduled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `BridgeTx<AccountId>` | ```{'nonce': 'u32', 'recipient': 'AccountId', 'amount': 'u128', 'tx_hash': 'scale_info::11'}```
| None | `BlockNumber` | ```u32```

---------
### Bridged
Confirmation of POLYX upgrade on Polymesh from POLY tokens on Ethereum.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `BridgeTx<AccountId>` | ```{'nonce': 'u32', 'recipient': 'AccountId', 'amount': 'u128', 'tx_hash': 'scale_info::11'}```

---------
### ControllerChanged
Confirmation of a signer set change.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```

---------
### ExemptedUpdated
Exemption status of an identity has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `IdentityId` | ```[u8; 32]```
| None | `bool` | ```bool```

---------
### FreezeAdminAdded
A new freeze admin has been added.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```

---------
### FreezeAdminRemoved
A freeze admin has been removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```

---------
### Frozen
Notification of freezing the bridge.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```

---------
### FrozenTx
Notification of freezing a transaction.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `BridgeTx<AccountId>` | ```{'nonce': 'u32', 'recipient': 'AccountId', 'amount': 'u128', 'tx_hash': 'scale_info::11'}```

---------
### TimelockChanged
Confirmation of default timelock change.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `BlockNumber` | ```u32```

---------
### TxRemoved
Notification of removing a transaction.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `BridgeTx<AccountId>` | ```{'nonce': 'u32', 'recipient': 'AccountId', 'amount': 'u128', 'tx_hash': 'scale_info::11'}```

---------
### TxsHandled
An event emitted after a vector of transactions is handled. The parameter is a vector of
tuples of recipient account, its nonce, and the status of the processed transaction.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<(AccountId, u32, HandledTxStatus)>` | ```[('AccountId', 'u32', {'Success': None, 'Error': 'Bytes'})]```

---------
### Unfrozen
Notification of unfreezing the bridge.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```

---------
### UnfrozenTx
Notification of unfreezing a transaction.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `BridgeTx<AccountId>` | ```{'nonce': 'u32', 'recipient': 'AccountId', 'amount': 'u128', 'tx_hash': 'scale_info::11'}```

---------
## Storage functions

---------
### Admin
 The admin key.

#### Python
```python
result = substrate.query(
    'Bridge', 'Admin', []
)
```

#### Return value
```python
'AccountId'
```
---------
### BridgeLimit
 The maximum number of bridged POLYX per identity within a set interval of
 blocks. Fields: POLYX amount and the block interval duration.

#### Python
```python
result = substrate.query(
    'Bridge', 'BridgeLimit', []
)
```

#### Return value
```python
('u128', 'u32')
```
---------
### BridgeLimitExempted
 Identities not constrained by the bridge limit.

#### Python
```python
result = substrate.query(
    'Bridge', 'BridgeLimitExempted', ['[u8; 32]']
)
```

#### Return value
```python
'bool'
```
---------
### BridgeTxDetails
 Details of bridge transactions identified with pairs of the recipient account and the
 bridge transaction nonce.

#### Python
```python
result = substrate.query(
    'Bridge', 'BridgeTxDetails', ['AccountId', 'u32']
)
```

#### Return value
```python
{
    'amount': 'u128',
    'execution_block': 'u32',
    'status': {
        'Absent': None,
        'Frozen': None,
        'Handled': None,
        'Pending': 'u8',
        'Timelocked': None,
    },
    'tx_hash': 'scale_info::11',
}
```
---------
### Controller
 The multisig account of the bridge controller. The genesis signers accept their
 authorizations and are able to get their proposals delivered. The bridge creator
 transfers some POLY to their identity.

#### Python
```python
result = substrate.query(
    'Bridge', 'Controller', []
)
```

#### Return value
```python
'AccountId'
```
---------
### FreezeAdmins
 Freeze bridge admins.  These accounts can only freeze the bridge.

#### Python
```python
result = substrate.query(
    'Bridge', 'FreezeAdmins', ['AccountId']
)
```

#### Return value
```python
'bool'
```
---------
### Frozen
 Whether or not the bridge operation is frozen.

#### Python
```python
result = substrate.query(
    'Bridge', 'Frozen', []
)
```

#### Return value
```python
'bool'
```
---------
### PolyxBridged
 Amount of POLYX bridged by the identity in last block interval. Fields: the bridged
 amount and the last interval number.

#### Python
```python
result = substrate.query(
    'Bridge', 'PolyxBridged', ['[u8; 32]']
)
```

#### Return value
```python
('u128', 'u32')
```
---------
### StorageVersion
 Storage version.

#### Python
```python
result = substrate.query(
    'Bridge', 'StorageVersion', []
)
```

#### Return value
```python
'u8'
```
---------
### Timelock
 The bridge transaction timelock period, in blocks, since the acceptance of the
 transaction proposal during which the admin key can freeze the transaction.

#### Python
```python
result = substrate.query(
    'Bridge', 'Timelock', []
)
```

#### Return value
```python
'u32'
```
---------
## Errors

---------
### BadAdmin
The origin is not the admin address.

---------
### BadCaller
The origin is not the controller or the admin address.

---------
### BridgeLimitReached
The identity&\#x27;s minted total has reached the bridge limit.

---------
### ControllerNotSet
The bridge controller address is not set.

---------
### DivisionByZero
The block interval duration is zero. Cannot divide.

---------
### Frozen
The bridge is already frozen.

---------
### FrozenTx
The transaction is frozen.

---------
### NoValidCdd
The recipient DID has no valid CDD.

---------
### NotFrozen
The bridge is not frozen.

---------
### Overflow
The identity&\#x27;s minted total has overflowed.

---------
### ProposalAlreadyHandled
The bridge transaction proposal has already been handled and the funds minted.

---------
### TimelockedTx
The transaction is timelocked.

---------
### Unauthorized
Unauthorized to perform an operation.

---------