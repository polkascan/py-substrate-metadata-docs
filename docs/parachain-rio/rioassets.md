
# RioAssets

---------
## Calls

---------
### approve_transfer
Approve an amount of asset for transfer by a delegated third-party account.

Origin must be Signed.

Ensures that `ApprovalDeposit` worth of `Currency` is reserved from signing account
for the purpose of holding the approval. If some non-zero amount of assets is already
approved from signing account to `delegate`, then it is topped up or unreserved to
meet the right value.

NOTE: The signing account does not need to own `amount` of assets at the point of
making this call.

- `id`: The identifier of the asset.
- `delegate`: The account to delegate permission to transfer asset.
- `amount`: The amount of asset that may be transferred by `delegate`. If there is
already an approval in place, then this acts additively.

Emits `ApprovedTransfer` on success.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::CurrencyId` | 
| delegate | `T::AccountId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'RioAssets', 'approve_transfer', {
    'amount': 'u128',
    'delegate': 'AccountId',
    'id': 'u32',
}
)
```

---------
### cancel_approval
Cancel all of some asset approved for delegated transfer by a third-party account.

Origin must be Signed and there must be an approval in place between signer and
`delegate`.

Unreserves any deposit previously reserved by `approve_transfer` for the approval.

- `id`: The identifier of the asset.
- `delegate`: The account delegated permission to transfer asset.

Emits `ApprovalCancelled` on success.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::CurrencyId` | 
| delegate | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'RioAssets', 'cancel_approval', {'delegate': 'AccountId', 'id': 'u32'}
)
```

---------
### create
create a new asset with full permissions granted to whoever make the
call *sudo or proposal approved only*
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 
| asset_info | `AssetInfo<BoundedVec<u8, T::StringLimit>>` | 

#### Python
```python
call = substrate.compose_call(
    'RioAssets', 'create', {
    'asset_info': {
        'chain': (
            'Rio',
            'Bitcoin',
            'Litecoin',
            'Ethereum',
            'EOS',
            'Polkadot',
            'Kusama',
            'ChainX',
        ),
        'decimals': 'u8',
        'desc': 'Bytes',
        'name': 'Bytes',
        'symbol': 'Bytes',
    },
    'currency_id': 'u32',
}
)
```

---------
### force_transfer
Exactly as `transfer`, except the origin must be root and the source
account may be specified.

The dispatch origin for this call must be _Root_.

- `source`: The sender of the transfer.
- `dest`: The recipient of the transfer.
- `currency_id`: currency type.
- `amount`: free balance amount to tranfer.
#### Attributes
| Name | Type |
| -------- | -------- | 
| source | `<T::Lookup as StaticLookup>::Source` | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| currency_id | `T::CurrencyId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'RioAssets', 'force_transfer', {
    'amount': 'u128',
    'currency_id': 'u32',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'source': {
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
### offline_asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'RioAssets', 'offline_asset', {'currency_id': 'u32'}
)
```

---------
### online_asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'RioAssets', 'online_asset', {'currency_id': 'u32'}
)
```

---------
### transfer
Transfer some liquid free balance to another account.

`transfer` will set the `FreeBalance` of the sender and receiver.
It will decrease the total issuance of the system by the
`TransferFee`. If the sender&\#x27;s account is below the existential
deposit as a result of the transfer, the account will be reaped.

The dispatch origin for this call must be `Signed` by the
transactor.

- `dest`: The recipient of the transfer.
- `currency_id`: currency type.
- `amount`: free balance amount to tranfer.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| currency_id | `T::CurrencyId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'RioAssets', 'transfer', {
    'amount': 'u128',
    'currency_id': 'u32',
    'dest': {
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
### transfer_all
Transfer all remaining balance to the given account.

NOTE: This function only attempts to transfer _transferable_
balances. This means that any locked, reserved, or existential
deposits (when `keep_alive` is `true`), will not be transferred by
this function. To ensure that this function results in a killed
account, you might need to prepare the account by removing any
reference counters, storage deposits, etc...

The dispatch origin for this call must be `Signed` by the
transactor.

- `dest`: The recipient of the transfer.
- `currency_id`: currency type.
- `keep_alive`: A boolean to determine if the `transfer_all`
  operation should send all of the funds the account has, causing
  the sender account to be killed (false), or transfer everything
  except at least the existential deposit, which will guarantee to
  keep the sender account alive (true).
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| currency_id | `T::CurrencyId` | 
| keep_alive | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'RioAssets', 'transfer_all', {
    'currency_id': 'u32',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'keep_alive': 'bool',
}
)
```

---------
### transfer_approved
Transfer some asset balance from a previously delegated account to some third-party
account.

Origin must be Signed and there must be an approval in place by the `owner` to the
signer.

If the entire amount approved for transfer is transferred, then any deposit previously
reserved by `approve_transfer` is unreserved.

- `id`: The identifier of the asset.
- `owner`: The account which previously approved for a transfer of at least `amount` and
from which the asset balance will be withdrawn.
- `destination`: The account to which the asset balance of `amount` will be transferred.
- `amount`: The amount of assets to transfer.

Emits `TransferredApproved` on success.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::CurrencyId` | 
| owner | `T::AccountId` | 
| destination | `T::AccountId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'RioAssets', 'transfer_approved', {
    'amount': 'u128',
    'destination': 'AccountId',
    'id': 'u32',
    'owner': 'AccountId',
}
)
```

---------
### transfer_keep_alive
Same as the [`transfer`] call, but with a check that the transfer
will not kill the origin account.

99% of the time you want [`transfer`] instead.

The dispatch origin for this call must be `Signed` by the
transactor.

- `dest`: The recipient of the transfer.
- `currency_id`: currency type.
- `amount`: free balance amount to tranfer.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| currency_id | `T::CurrencyId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'RioAssets', 'transfer_keep_alive', {
    'amount': 'u128',
    'currency_id': 'u32',
    'dest': {
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
### update_asset_info
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 
| asset_info | `AssetInfo<BoundedVec<u8, T::StringLimit>>` | 

#### Python
```python
call = substrate.compose_call(
    'RioAssets', 'update_asset_info', {
    'asset_info': {
        'chain': (
            'Rio',
            'Bitcoin',
            'Litecoin',
            'Ethereum',
            'EOS',
            'Polkadot',
            'Kusama',
            'ChainX',
        ),
        'decimals': 'u8',
        'desc': 'Bytes',
        'name': 'Bytes',
        'symbol': 'Bytes',
    },
    'currency_id': 'u32',
}
)
```

---------
### update_restriction
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 
| restrictions | `Restrictions` | 

#### Python
```python
call = substrate.compose_call(
    'RioAssets', 'update_restriction', {
    'currency_id': 'u32',
    'restrictions': {'mask': 'u32'},
}
)
```

---------
## Events

---------
### ApprovalCancelled
An approval for account `delegate` was cancelled by `owner`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::CurrencyId` | ```u32```
| owner | `T::AccountId` | ```AccountId```
| delegate | `T::AccountId` | ```AccountId```

---------
### ApprovedTransfer
(Additional) funds have been approved for transfer to a destination account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::CurrencyId` | ```u32```
| source | `T::AccountId` | ```AccountId```
| delegate | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### BalanceSet
A balance was set by root.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| free | `T::Balance` | ```u128```
| reserved | `T::Balance` | ```u128```

---------
### Created
Asset created (currency_id, creator, asset_options).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```

---------
### Deposited
Deposited some balance into an account
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### DustLost
An account was removed whose balance was non-zero but below
ExistentialDeposit, resulting in an outright loss.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Endowed
An account was created with some free balance.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### LockRemoved
Some locked funds were unlocked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| lock_id | `LockIdentifier` | ```[u8; 8]```
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```

---------
### LockSet
Some funds are locked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| lock_id | `LockIdentifier` | ```[u8; 8]```
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### ReserveRepatriated
Some reserved balance was repatriated (moved from reserved to
another account).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```
| status | `BalanceStatus` | ```('Free', 'Reserved')```

---------
### Reserved
Some balance was reserved (moved from free to reserved).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Revoke
Asset is offline
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```

---------
### Slashed
Some balances were slashed (e.g. due to mis-behavior)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| free_amount | `T::Balance` | ```u128```
| reserved_amount | `T::Balance` | ```u128```

---------
### TotalIssuanceSet
The total issuance of an currency has been set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| amount | `T::Balance` | ```u128```

---------
### Transfer
Transfer succeeded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### TransferredApproved
An `amount` was transferred in its entirety from `owner` to `destination` by
the approved `delegate`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::CurrencyId` | ```u32```
| owner | `T::AccountId` | ```AccountId```
| delegate | `T::AccountId` | ```AccountId```
| destination | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### Unreserved
Some balance was unreserved (moved from reserved to free).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### UpdateAssetRestriction
Update asset restrictions
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| restrictions | `Restrictions` | ```{'mask': 'u32'}```

---------
### Withdrawn
Some balances were withdrawn (e.g. pay for transaction fee)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_id | `T::CurrencyId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
## Storage functions

---------
### Accounts
 The balance of a token type under an account.

 NOTE: If the total is ever zero, decrease account ref account.

 NOTE: This is only used in the case that this module is used to store
 balances.

#### Python
```python
result = substrate.query(
    'RioAssets', 'Accounts', ['AccountId', 'u32']
)
```

#### Return value
```python
{'free': 'u128', 'frozen': 'u128', 'reserved': 'u128'}
```
---------
### Approvals
 Approved balance transfers. First balance is the amount approved for transfer. Second
 is the amount of `T::Currency` reserved for storing this.
 First key is the asset ID, second key is the owner and third key is the delegate.

#### Python
```python
result = substrate.query(
    'RioAssets', 'Approvals', ['u32', 'AccountId', 'AccountId']
)
```

#### Return value
```python
{'amount': 'u128', 'deposit': 'u128'}
```
---------
### AssetInfos
 &quot;Symbols&quot; can only keep Vec&lt;u8&gt;, and utf8 safety is totally on the
 client side

#### Python
```python
result = substrate.query(
    'RioAssets', 'AssetInfos', ['u32']
)
```

#### Return value
```python
{
    'chain': (
        'Rio',
        'Bitcoin',
        'Litecoin',
        'Ethereum',
        'EOS',
        'Polkadot',
        'Kusama',
        'ChainX',
    ),
    'decimals': 'u8',
    'desc': 'Bytes',
    'name': 'Bytes',
    'symbol': 'Bytes',
}
```
---------
### AssetRestrictions
 Restrictions means this asset can&#x27;t do something

#### Python
```python
result = substrate.query(
    'RioAssets', 'AssetRestrictions', ['u32']
)
```

#### Return value
```python
{'mask': 'u32'}
```
---------
### Locks
 Any liquidity locks of a token type under an account.
 NOTE: Should only be accessed when setting, changing and freeing a lock.

#### Python
```python
result = substrate.query(
    'RioAssets', 'Locks', ['AccountId', 'u32']
)
```

#### Return value
```python
[{'amount': 'u128', 'id': '[u8; 8]'}]
```
---------
### Online

#### Python
```python
result = substrate.query(
    'RioAssets', 'Online', ['u32']
)
```

#### Return value
```python
'bool'
```
---------
### Reserves
 Named reserves on some account balances.

#### Python
```python
result = substrate.query(
    'RioAssets', 'Reserves', ['AccountId', 'u32']
)
```

#### Return value
```python
[{'amount': 'u128', 'id': '[u8; 8]'}]
```
---------
### TotalIssuance
 The total issuance of a token type.

#### Python
```python
result = substrate.query(
    'RioAssets', 'TotalIssuance', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### ApprovalDeposit
 The amount of funds that must be reserved when creating a new approval.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('RioAssets', 'ApprovalDeposit')
```
---------
### MaxLocks
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('RioAssets', 'MaxLocks')
```
---------
### MaxReserves
 The maximum number of named reserves that can exist on an account.
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('RioAssets', 'MaxReserves')
```
---------
### StringLimit
 The maximum length of a name or symbol stored on-chain.
#### Value
```python
128
```
#### Python
```python
constant = substrate.get_constant('RioAssets', 'StringLimit')
```
---------
## Errors

---------
### AmountIntoBalanceFailed
Cannot convert Amount into Balance type

---------
### BalanceTooLow
The balance is too low

---------
### DeadAccount
Beneficiary account must pre-exist

---------
### ExistedAsset
Asset already exist

---------
### ExistentialDeposit
Value too low to create account due to existential deposit

---------
### InvalidAsset
Invalid asset

---------
### InvalidAssetInfo
Invalid asset info when create asset

---------
### KeepAlive
Transfer/payment would kill account

---------
### LiquidityRestrictions
Failed because liquidity restrictions due to locking

---------
### MaxLocksExceeded
Failed because the maximum locks was exceeded

---------
### NotExistedAsset
Asset not exist

---------
### RestrictedAction
The asset is restricted by this action.

---------
### TextTooLong
Symbol, Name or Desc too long

---------
### TooManyReserves

---------
### Unapproved
No approval exists that would allow the transfer.

---------
### Unknown
Unknown error.

---------