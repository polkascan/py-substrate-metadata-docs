
# Assets

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
| id | `T::AssetId` | 
| delegate | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'approve_transfer', {
    'amount': 'u128',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'id': 'u32',
}
)
```

---------
### burn
Reduce the balance of `who` by as much as possible up to `amount` assets of `id`.

Origin must be Signed and the sender should be the Manager of the asset `id`.

Bails with `NoAccount` if the `who` is already dead.

- `id`: The identifier of the asset to have some amount burned.
- `who`: The account to be debited from.
- `amount`: The maximum amount by which `who`&\#x27;s balance should be reduced.

Emits `Burned` with the actual amount burned. If this takes the balance to below the
minimum for the asset, then the amount burned is increased to take it to zero.

Weight: `O(1)`
Modes: Post-existence of `who`; Pre &amp; post Zombie-status of `who`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 
| who | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'burn', {
    'amount': 'u128',
    'id': 'u32',
    'who': {
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
| id | `T::AssetId` | 
| delegate | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'cancel_approval', {
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'id': 'u32',
}
)
```

---------
### clear_metadata
Clear the metadata for an asset.

Origin must be Signed and the sender should be the Owner of the asset `id`.

Any deposit is freed for the asset owner.

- `id`: The identifier of the asset to clear.

Emits `MetadataCleared`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'clear_metadata', {'id': 'u32'}
)
```

---------
### create
Issue a new class of fungible assets from a public origin.

This new asset class has no assets initially and its owner is the origin.

The origin must be Signed and the sender must have sufficient funds free.

Funds of sender are reserved by `AssetDeposit`.

Parameters:
- `id`: The identifier of the new asset. This must not be currently in use to identify
an existing asset.
- `admin`: The admin of this class of assets. The admin is the initial address of each
member of the asset class&\#x27;s admin team.
- `min_balance`: The minimum balance of this new asset that any single account must
have. If an account&\#x27;s balance is reduced below this, then it collapses to zero.

Emits `Created` event when successful.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 
| admin | `AccountIdLookupOf<T>` | 
| min_balance | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'create', {
    'admin': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'id': 'u32',
    'min_balance': 'u128',
}
)
```

---------
### destroy
Destroy a class of fungible assets.

The origin must conform to `ForceOrigin` or must be Signed and the sender must be the
owner of the asset `id`.

- `id`: The identifier of the asset to be destroyed. This must identify an existing
asset.

Emits `Destroyed` event when successful.

NOTE: It can be helpful to first freeze an asset before destroying it so that you
can provide accurate witness information and prevent users from manipulating state
in a way that can make it harder to destroy.

Weight: `O(c + p + a)` where:
- `c = (witness.accounts - witness.sufficients)`
- `s = witness.sufficients`
- `a = witness.approvals`
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 
| witness | `DestroyWitness` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'destroy', {
    'id': 'u32',
    'witness': {
        'accounts': 'u32',
        'approvals': 'u32',
        'sufficients': 'u32',
    },
}
)
```

---------
### force_asset_status
Alter the attributes of a given asset.

Origin must be `ForceOrigin`.

- `id`: The identifier of the asset.
- `owner`: The new Owner of this asset.
- `issuer`: The new Issuer of this asset.
- `admin`: The new Admin of this asset.
- `freezer`: The new Freezer of this asset.
- `min_balance`: The minimum balance of this new asset that any single account must
have. If an account&\#x27;s balance is reduced below this, then it collapses to zero.
- `is_sufficient`: Whether a non-zero balance of this asset is deposit of sufficient
value to account for the state bloat associated with its balance storage. If set to
`true`, then non-zero balances may be stored without a `consumer` reference (and thus
an ED in the Balances pallet or whatever else is used to control user-account state
growth).
- `is_frozen`: Whether this asset class is frozen except for permissioned/admin
instructions.

Emits `AssetStatusChanged` with the identity of the asset.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 
| owner | `AccountIdLookupOf<T>` | 
| issuer | `AccountIdLookupOf<T>` | 
| admin | `AccountIdLookupOf<T>` | 
| freezer | `AccountIdLookupOf<T>` | 
| min_balance | `T::Balance` | 
| is_sufficient | `bool` | 
| is_frozen | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'force_asset_status', {
    'admin': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'freezer': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'id': 'u32',
    'is_frozen': 'bool',
    'is_sufficient': 'bool',
    'issuer': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'min_balance': 'u128',
    'owner': {
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
### force_cancel_approval
Cancel all of some asset approved for delegated transfer by a third-party account.

Origin must be either ForceOrigin or Signed origin with the signer being the Admin
account of the asset `id`.

Unreserves any deposit previously reserved by `approve_transfer` for the approval.

- `id`: The identifier of the asset.
- `delegate`: The account delegated permission to transfer asset.

Emits `ApprovalCancelled` on success.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 
| owner | `AccountIdLookupOf<T>` | 
| delegate | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'force_cancel_approval', {
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'id': 'u32',
    'owner': {
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
### force_clear_metadata
Clear the metadata for an asset.

Origin must be ForceOrigin.

Any deposit is returned.

- `id`: The identifier of the asset to clear.

Emits `MetadataCleared`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'force_clear_metadata', {'id': 'u32'}
)
```

---------
### force_create
Issue a new class of fungible assets from a privileged origin.

This new asset class has no assets initially.

The origin must conform to `ForceOrigin`.

Unlike `create`, no funds are reserved.

- `id`: The identifier of the new asset. This must not be currently in use to identify
an existing asset.
- `owner`: The owner of this class of assets. The owner has full superuser permissions
over this asset, but may later change and configure the permissions using
`transfer_ownership` and `set_team`.
- `min_balance`: The minimum balance of this new asset that any single account must
have. If an account&\#x27;s balance is reduced below this, then it collapses to zero.

Emits `ForceCreated` event when successful.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 
| owner | `AccountIdLookupOf<T>` | 
| is_sufficient | `bool` | 
| min_balance | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'force_create', {
    'id': 'u32',
    'is_sufficient': 'bool',
    'min_balance': 'u128',
    'owner': {
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
### force_set_metadata
Force the metadata for an asset to some value.

Origin must be ForceOrigin.

Any deposit is left alone.

- `id`: The identifier of the asset to update.
- `name`: The user friendly name of this asset. Limited in length by `StringLimit`.
- `symbol`: The exchange symbol for this asset. Limited in length by `StringLimit`.
- `decimals`: The number of decimals this asset uses to represent one unit.

Emits `MetadataSet`.

Weight: `O(N + S)` where N and S are the length of the name and symbol respectively.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 
| name | `Vec<u8>` | 
| symbol | `Vec<u8>` | 
| decimals | `u8` | 
| is_frozen | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'force_set_metadata', {
    'decimals': 'u8',
    'id': 'u32',
    'is_frozen': 'bool',
    'name': 'Bytes',
    'symbol': 'Bytes',
}
)
```

---------
### force_transfer
Move some assets from one account to another.

Origin must be Signed and the sender should be the Admin of the asset `id`.

- `id`: The identifier of the asset to have some amount transferred.
- `source`: The account to be debited.
- `dest`: The account to be credited.
- `amount`: The amount by which the `source`&\#x27;s balance of assets should be reduced and
`dest`&\#x27;s balance increased. The amount actually transferred may be slightly greater in
the case that the transfer would otherwise take the `source` balance above zero but
below the minimum balance. Must be greater than zero.

Emits `Transferred` with the actual amount transferred. If this takes the source balance
to below the minimum for the asset, then the amount transferred is increased to take it
to zero.

Weight: `O(1)`
Modes: Pre-existence of `dest`; Post-existence of `source`; Account pre-existence of
`dest`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 
| source | `AccountIdLookupOf<T>` | 
| dest | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'force_transfer', {
    'amount': 'u128',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'id': 'u32',
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
### freeze
Disallow further unprivileged transfers from an account.

Origin must be Signed and the sender should be the Freezer of the asset `id`.

- `id`: The identifier of the asset to be frozen.
- `who`: The account to be frozen.

Emits `Frozen`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'freeze', {
    'id': 'u32',
    'who': {
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
### freeze_asset
Disallow further unprivileged transfers for the asset class.

Origin must be Signed and the sender should be the Freezer of the asset `id`.

- `id`: The identifier of the asset to be frozen.

Emits `Frozen`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'freeze_asset', {'id': 'u32'}
)
```

---------
### mint
Mint assets of a particular class.

The origin must be Signed and the sender must be the Issuer of the asset `id`.

- `id`: The identifier of the asset to have some amount minted.
- `beneficiary`: The account to be credited with the minted assets.
- `amount`: The amount of the asset to be minted.

Emits `Issued` event when successful.

Weight: `O(1)`
Modes: Pre-existing balance of `beneficiary`; Account pre-existence of `beneficiary`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 
| beneficiary | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'mint', {
    'amount': 'u128',
    'beneficiary': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'id': 'u32',
}
)
```

---------
### refund
Return the deposit (if any) of an asset account.

The origin must be Signed.

- `id`: The identifier of the asset for the account to be created.
- `allow_burn`: If `true` then assets may be destroyed in order to complete the refund.

Emits `Refunded` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 
| allow_burn | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'refund', {'allow_burn': 'bool', 'id': 'u32'}
)
```

---------
### set_metadata
Set the metadata for an asset.

Origin must be Signed and the sender should be the Owner of the asset `id`.

Funds of sender are reserved according to the formula:
`MetadataDepositBase + MetadataDepositPerByte * (name.len + symbol.len)` taking into
account any already reserved funds.

- `id`: The identifier of the asset to update.
- `name`: The user friendly name of this asset. Limited in length by `StringLimit`.
- `symbol`: The exchange symbol for this asset. Limited in length by `StringLimit`.
- `decimals`: The number of decimals this asset uses to represent one unit.

Emits `MetadataSet`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 
| name | `Vec<u8>` | 
| symbol | `Vec<u8>` | 
| decimals | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'set_metadata', {
    'decimals': 'u8',
    'id': 'u32',
    'name': 'Bytes',
    'symbol': 'Bytes',
}
)
```

---------
### set_team
Change the Issuer, Admin and Freezer of an asset.

Origin must be Signed and the sender should be the Owner of the asset `id`.

- `id`: The identifier of the asset to be frozen.
- `issuer`: The new Issuer of this asset.
- `admin`: The new Admin of this asset.
- `freezer`: The new Freezer of this asset.

Emits `TeamChanged`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 
| issuer | `AccountIdLookupOf<T>` | 
| admin | `AccountIdLookupOf<T>` | 
| freezer | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'set_team', {
    'admin': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'freezer': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'id': 'u32',
    'issuer': {
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
### thaw
Allow unprivileged transfers from an account again.

Origin must be Signed and the sender should be the Admin of the asset `id`.

- `id`: The identifier of the asset to be frozen.
- `who`: The account to be unfrozen.

Emits `Thawed`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'thaw', {
    'id': 'u32',
    'who': {
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
### thaw_asset
Allow unprivileged transfers for the asset again.

Origin must be Signed and the sender should be the Admin of the asset `id`.

- `id`: The identifier of the asset to be thawed.

Emits `Thawed`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'thaw_asset', {'id': 'u32'}
)
```

---------
### touch
Create an asset account for non-provider assets.

A deposit will be taken from the signer account.

- `origin`: Must be Signed; the signer account must have sufficient funds for a deposit
  to be taken.
- `id`: The identifier of the asset for the account to be created.

Emits `Touched` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'touch', {'id': 'u32'}
)
```

---------
### transfer
Move some assets from the sender account to another.

Origin must be Signed.

- `id`: The identifier of the asset to have some amount transferred.
- `target`: The account to be credited.
- `amount`: The amount by which the sender&\#x27;s balance of assets should be reduced and
`target`&\#x27;s balance increased. The amount actually transferred may be slightly greater in
the case that the transfer would otherwise take the sender balance above zero but below
the minimum balance. Must be greater than zero.

Emits `Transferred` with the actual amount transferred. If this takes the source balance
to below the minimum for the asset, then the amount transferred is increased to take it
to zero.

Weight: `O(1)`
Modes: Pre-existence of `target`; Post-existence of sender; Account pre-existence of
`target`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 
| target | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'transfer', {
    'amount': 'u128',
    'id': 'u32',
    'target': {
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
| id | `T::AssetId` | 
| owner | `AccountIdLookupOf<T>` | 
| destination | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'transfer_approved', {
    'amount': 'u128',
    'destination': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'id': 'u32',
    'owner': {
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
### transfer_keep_alive
Move some assets from the sender account to another, keeping the sender account alive.

Origin must be Signed.

- `id`: The identifier of the asset to have some amount transferred.
- `target`: The account to be credited.
- `amount`: The amount by which the sender&\#x27;s balance of assets should be reduced and
`target`&\#x27;s balance increased. The amount actually transferred may be slightly greater in
the case that the transfer would otherwise take the sender balance above zero but below
the minimum balance. Must be greater than zero.

Emits `Transferred` with the actual amount transferred. If this takes the source balance
to below the minimum for the asset, then the amount transferred is increased to take it
to zero.

Weight: `O(1)`
Modes: Pre-existence of `target`; Post-existence of sender; Account pre-existence of
`target`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 
| target | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'transfer_keep_alive', {
    'amount': 'u128',
    'id': 'u32',
    'target': {
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
### transfer_ownership
Change the Owner of an asset.

Origin must be Signed and the sender should be the Owner of the asset `id`.

- `id`: The identifier of the asset.
- `owner`: The new Owner of this asset.

Emits `OwnerChanged`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetId` | 
| owner | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'transfer_ownership', {
    'id': 'u32',
    'owner': {
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
## Events

---------
### ApprovalCancelled
An approval for account `delegate` was cancelled by `owner`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| owner | `T::AccountId` | ```AccountId```
| delegate | `T::AccountId` | ```AccountId```

---------
### ApprovedTransfer
(Additional) funds have been approved for transfer to a destination account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| source | `T::AccountId` | ```AccountId```
| delegate | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### AssetFrozen
Some asset `asset_id` was frozen.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```

---------
### AssetStatusChanged
An asset has had its attributes changed by the `Force` origin.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```

---------
### AssetThawed
Some asset `asset_id` was thawed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```

---------
### Burned
Some assets were destroyed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| owner | `T::AccountId` | ```AccountId```
| balance | `T::Balance` | ```u128```

---------
### Created
Some asset class was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| creator | `T::AccountId` | ```AccountId```
| owner | `T::AccountId` | ```AccountId```

---------
### Destroyed
An asset class was destroyed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```

---------
### ForceCreated
Some asset class was force-created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| owner | `T::AccountId` | ```AccountId```

---------
### Frozen
Some account `who` was frozen.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| who | `T::AccountId` | ```AccountId```

---------
### Issued
Some assets were issued.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| owner | `T::AccountId` | ```AccountId```
| total_supply | `T::Balance` | ```u128```

---------
### MetadataCleared
Metadata has been cleared for an asset.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```

---------
### MetadataSet
New metadata has been set for an asset.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| name | `Vec<u8>` | ```Bytes```
| symbol | `Vec<u8>` | ```Bytes```
| decimals | `u8` | ```u8```
| is_frozen | `bool` | ```bool```

---------
### OwnerChanged
The owner changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| owner | `T::AccountId` | ```AccountId```

---------
### TeamChanged
The management team changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| issuer | `T::AccountId` | ```AccountId```
| admin | `T::AccountId` | ```AccountId```
| freezer | `T::AccountId` | ```AccountId```

---------
### Thawed
Some account `who` was thawed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| who | `T::AccountId` | ```AccountId```

---------
### Transferred
Some assets were transferred.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
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
| asset_id | `T::AssetId` | ```u32```
| owner | `T::AccountId` | ```AccountId```
| delegate | `T::AccountId` | ```AccountId```
| destination | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
## Storage functions

---------
### Account
 The holdings of a specific account for a specific asset.

#### Python
```python
result = substrate.query(
    'Assets', 'Account', ['u32', 'AccountId']
)
```

#### Return value
```python
{
    'balance': 'u128',
    'extra': (),
    'is_frozen': 'bool',
    'reason': {
        'Consumer': None,
        'DepositHeld': 'u128',
        'DepositRefunded': None,
        'Sufficient': None,
    },
}
```
---------
### Approvals
 Approved balance transfers. First balance is the amount approved for transfer. Second
 is the amount of `T::Currency` reserved for storing this.
 First key is the asset ID, second key is the owner and third key is the delegate.

#### Python
```python
result = substrate.query(
    'Assets', 'Approvals', ['u32', 'AccountId', 'AccountId']
)
```

#### Return value
```python
{'amount': 'u128', 'deposit': 'u128'}
```
---------
### Asset
 Details of an asset.

#### Python
```python
result = substrate.query(
    'Assets', 'Asset', ['u32']
)
```

#### Return value
```python
{
    'accounts': 'u32',
    'admin': 'AccountId',
    'approvals': 'u32',
    'deposit': 'u128',
    'freezer': 'AccountId',
    'is_frozen': 'bool',
    'is_sufficient': 'bool',
    'issuer': 'AccountId',
    'min_balance': 'u128',
    'owner': 'AccountId',
    'sufficients': 'u32',
    'supply': 'u128',
}
```
---------
### Metadata
 Metadata of an asset.

#### Python
```python
result = substrate.query(
    'Assets', 'Metadata', ['u32']
)
```

#### Return value
```python
{
    'decimals': 'u8',
    'deposit': 'u128',
    'is_frozen': 'bool',
    'name': 'Bytes',
    'symbol': 'Bytes',
}
```
---------
## Constants

---------
### ApprovalDeposit
 The amount of funds that must be reserved when creating a new approval.
#### Value
```python
100000000000
```
#### Python
```python
constant = substrate.get_constant('Assets', 'ApprovalDeposit')
```
---------
### AssetAccountDeposit
 The amount of funds that must be reserved for a non-provider asset account to be
 maintained.
#### Value
```python
1110000000000
```
#### Python
```python
constant = substrate.get_constant('Assets', 'AssetAccountDeposit')
```
---------
### AssetDeposit
 The basic amount of funds that must be reserved for an asset.
#### Value
```python
1000000000000
```
#### Python
```python
constant = substrate.get_constant('Assets', 'AssetDeposit')
```
---------
### MetadataDepositBase
 The basic amount of funds that must be reserved when adding metadata to your asset.
#### Value
```python
4230000000000
```
#### Python
```python
constant = substrate.get_constant('Assets', 'MetadataDepositBase')
```
---------
### MetadataDepositPerByte
 The additional funds that must be reserved for the number of bytes you store in your
 metadata.
#### Value
```python
60000000000
```
#### Python
```python
constant = substrate.get_constant('Assets', 'MetadataDepositPerByte')
```
---------
### StringLimit
 The maximum length of a name or symbol stored on-chain.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('Assets', 'StringLimit')
```
---------
## Errors

---------
### AlreadyExists
The asset-account already exists.

---------
### BadMetadata
Invalid metadata given.

---------
### BadWitness
Invalid witness data given.

---------
### BalanceLow
Account balance must be greater than or equal to the transfer amount.

---------
### Frozen
The origin account is frozen.

---------
### InUse
The asset ID is already taken.

---------
### MinBalanceZero
Minimum balance should be non-zero.

---------
### NoAccount
The account to alter does not exist.

---------
### NoDeposit
The asset-account doesn&\#x27;t have an associated deposit.

---------
### NoPermission
The signing account has no permission to do the operation.

---------
### NoProvider
Unable to increment the consumer reference counters on the account. Either no provider
reference exists to allow a non-zero balance of a non-self-sufficient asset, or the
maximum number of consumers has been reached.

---------
### Unapproved
No approval exists that would allow the transfer.

---------
### Unknown
The given asset ID is unknown.

---------
### WouldBurn
The operation would result in funds being burned.

---------
### WouldDie
The source account would not survive the transfer and it needs to stay alive.

---------