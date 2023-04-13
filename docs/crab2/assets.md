
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
| id | `T::AssetIdParameter` | 
| delegate | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'approve_transfer', {
    'amount': 'u128',
    'delegate': '[u8; 20]',
    'id': 'u64',
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
| id | `T::AssetIdParameter` | 
| who | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'burn', {
    'amount': 'u128',
    'id': 'u64',
    'who': '[u8; 20]',
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
| id | `T::AssetIdParameter` | 
| delegate | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'cancel_approval', {'delegate': '[u8; 20]', 'id': 'u64'}
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
| id | `T::AssetIdParameter` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'clear_metadata', {'id': 'u64'}
)
```

---------
### create
Issue a new class of fungible assets from a public origin.

This new asset class has no assets initially and its owner is the origin.

The origin must conform to the configured `CreateOrigin` and have sufficient funds free.

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
| id | `T::AssetIdParameter` | 
| admin | `AccountIdLookupOf<T>` | 
| min_balance | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'create', {
    'admin': '[u8; 20]',
    'id': 'u64',
    'min_balance': 'u128',
}
)
```

---------
### destroy_accounts
Destroy all accounts associated with a given asset.

`destroy_accounts` should only be called after `start_destroy` has been called, and the
asset is in a `Destroying` state.

Due to weight restrictions, this function may need to be called multiple times to fully
destroy all accounts. It will destroy `RemoveItemsLimit` accounts at a time.

- `id`: The identifier of the asset to be destroyed. This must identify an existing
  asset.

Each call emits the `Event::DestroyedAccounts` event.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'destroy_accounts', {'id': 'u64'}
)
```

---------
### destroy_approvals
Destroy all approvals associated with a given asset up to the max (T::RemoveItemsLimit).

`destroy_approvals` should only be called after `start_destroy` has been called, and the
asset is in a `Destroying` state.

Due to weight restrictions, this function may need to be called multiple times to fully
destroy all approvals. It will destroy `RemoveItemsLimit` approvals at a time.

- `id`: The identifier of the asset to be destroyed. This must identify an existing
  asset.

Each call emits the `Event::DestroyedApprovals` event.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'destroy_approvals', {'id': 'u64'}
)
```

---------
### finish_destroy
Complete destroying asset and unreserve currency.

`finish_destroy` should only be called after `start_destroy` has been called, and the
asset is in a `Destroying` state. All accounts or approvals should be destroyed before
hand.

- `id`: The identifier of the asset to be destroyed. This must identify an existing
  asset.

Each successful call emits the `Event::Destroyed` event.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'finish_destroy', {'id': 'u64'}
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
| id | `T::AssetIdParameter` | 
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
    'admin': '[u8; 20]',
    'freezer': '[u8; 20]',
    'id': 'u64',
    'is_frozen': 'bool',
    'is_sufficient': 'bool',
    'issuer': '[u8; 20]',
    'min_balance': 'u128',
    'owner': '[u8; 20]',
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
| id | `T::AssetIdParameter` | 
| owner | `AccountIdLookupOf<T>` | 
| delegate | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'force_cancel_approval', {
    'delegate': '[u8; 20]',
    'id': 'u64',
    'owner': '[u8; 20]',
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
| id | `T::AssetIdParameter` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'force_clear_metadata', {'id': 'u64'}
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
| id | `T::AssetIdParameter` | 
| owner | `AccountIdLookupOf<T>` | 
| is_sufficient | `bool` | 
| min_balance | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'force_create', {
    'id': 'u64',
    'is_sufficient': 'bool',
    'min_balance': 'u128',
    'owner': '[u8; 20]',
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
| id | `T::AssetIdParameter` | 
| name | `Vec<u8>` | 
| symbol | `Vec<u8>` | 
| decimals | `u8` | 
| is_frozen | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'force_set_metadata', {
    'decimals': 'u8',
    'id': 'u64',
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
| id | `T::AssetIdParameter` | 
| source | `AccountIdLookupOf<T>` | 
| dest | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'force_transfer', {
    'amount': 'u128',
    'dest': '[u8; 20]',
    'id': 'u64',
    'source': '[u8; 20]',
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
| id | `T::AssetIdParameter` | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'freeze', {'id': 'u64', 'who': '[u8; 20]'}
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
| id | `T::AssetIdParameter` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'freeze_asset', {'id': 'u64'}
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
| id | `T::AssetIdParameter` | 
| beneficiary | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'mint', {
    'amount': 'u128',
    'beneficiary': '[u8; 20]',
    'id': 'u64',
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
| id | `T::AssetIdParameter` | 
| allow_burn | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'refund', {'allow_burn': 'bool', 'id': 'u64'}
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
| id | `T::AssetIdParameter` | 
| name | `Vec<u8>` | 
| symbol | `Vec<u8>` | 
| decimals | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'set_metadata', {
    'decimals': 'u8',
    'id': 'u64',
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
| id | `T::AssetIdParameter` | 
| issuer | `AccountIdLookupOf<T>` | 
| admin | `AccountIdLookupOf<T>` | 
| freezer | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'set_team', {
    'admin': '[u8; 20]',
    'freezer': '[u8; 20]',
    'id': 'u64',
    'issuer': '[u8; 20]',
}
)
```

---------
### start_destroy
Start the process of destroying a fungible asset class.

`start_destroy` is the first in a series of extrinsics that should be called, to allow
destruction of an asset class.

The origin must conform to `ForceOrigin` or must be `Signed` by the asset&\#x27;s `owner`.

- `id`: The identifier of the asset to be destroyed. This must identify an existing
  asset.

The asset class must be frozen before calling `start_destroy`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'start_destroy', {'id': 'u64'}
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
| id | `T::AssetIdParameter` | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'thaw', {'id': 'u64', 'who': '[u8; 20]'}
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
| id | `T::AssetIdParameter` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'thaw_asset', {'id': 'u64'}
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
| id | `T::AssetIdParameter` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'touch', {'id': 'u64'}
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
| id | `T::AssetIdParameter` | 
| target | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'transfer', {
    'amount': 'u128',
    'id': 'u64',
    'target': '[u8; 20]',
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
| id | `T::AssetIdParameter` | 
| owner | `AccountIdLookupOf<T>` | 
| destination | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'transfer_approved', {
    'amount': 'u128',
    'destination': '[u8; 20]',
    'id': 'u64',
    'owner': '[u8; 20]',
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
| id | `T::AssetIdParameter` | 
| target | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'transfer_keep_alive', {
    'amount': 'u128',
    'id': 'u64',
    'target': '[u8; 20]',
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
| id | `T::AssetIdParameter` | 
| owner | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Assets', 'transfer_ownership', {'id': 'u64', 'owner': '[u8; 20]'}
)
```

---------
## Events

---------
### AccountsDestroyed
Accounts were destroyed for given asset.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```
| accounts_destroyed | `u32` | ```u32```
| accounts_remaining | `u32` | ```u32```

---------
### ApprovalCancelled
An approval for account `delegate` was cancelled by `owner`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```
| owner | `T::AccountId` | ```[u8; 20]```
| delegate | `T::AccountId` | ```[u8; 20]```

---------
### ApprovalsDestroyed
Approvals were destroyed for given asset.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```
| approvals_destroyed | `u32` | ```u32```
| approvals_remaining | `u32` | ```u32```

---------
### ApprovedTransfer
(Additional) funds have been approved for transfer to a destination account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```
| source | `T::AccountId` | ```[u8; 20]```
| delegate | `T::AccountId` | ```[u8; 20]```
| amount | `T::Balance` | ```u128```

---------
### AssetFrozen
Some asset `asset_id` was frozen.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```

---------
### AssetStatusChanged
An asset has had its attributes changed by the `Force` origin.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```

---------
### AssetThawed
Some asset `asset_id` was thawed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```

---------
### Burned
Some assets were destroyed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```
| owner | `T::AccountId` | ```[u8; 20]```
| balance | `T::Balance` | ```u128```

---------
### Created
Some asset class was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```
| creator | `T::AccountId` | ```[u8; 20]```
| owner | `T::AccountId` | ```[u8; 20]```

---------
### Destroyed
An asset class was destroyed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```

---------
### DestructionStarted
An asset class is in the process of being destroyed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```

---------
### ForceCreated
Some asset class was force-created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```
| owner | `T::AccountId` | ```[u8; 20]```

---------
### Frozen
Some account `who` was frozen.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```
| who | `T::AccountId` | ```[u8; 20]```

---------
### Issued
Some assets were issued.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```
| owner | `T::AccountId` | ```[u8; 20]```
| amount | `T::Balance` | ```u128```

---------
### MetadataCleared
Metadata has been cleared for an asset.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```

---------
### MetadataSet
New metadata has been set for an asset.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```
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
| asset_id | `T::AssetId` | ```u64```
| owner | `T::AccountId` | ```[u8; 20]```

---------
### TeamChanged
The management team changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```
| issuer | `T::AccountId` | ```[u8; 20]```
| admin | `T::AccountId` | ```[u8; 20]```
| freezer | `T::AccountId` | ```[u8; 20]```

---------
### Thawed
Some account `who` was thawed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```
| who | `T::AccountId` | ```[u8; 20]```

---------
### Transferred
Some assets were transferred.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```
| from | `T::AccountId` | ```[u8; 20]```
| to | `T::AccountId` | ```[u8; 20]```
| amount | `T::Balance` | ```u128```

---------
### TransferredApproved
An `amount` was transferred in its entirety from `owner` to `destination` by
the approved `delegate`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u64```
| owner | `T::AccountId` | ```[u8; 20]```
| delegate | `T::AccountId` | ```[u8; 20]```
| destination | `T::AccountId` | ```[u8; 20]```
| amount | `T::Balance` | ```u128```

---------
## Storage functions

---------
### Account
 The holdings of a specific account for a specific asset.

#### Python
```python
result = substrate.query(
    'Assets', 'Account', ['u64', '[u8; 20]']
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
    'Assets', 'Approvals', ['u64', '[u8; 20]', '[u8; 20]']
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
    'Assets', 'Asset', ['u64']
)
```

#### Return value
```python
{
    'accounts': 'u32',
    'admin': '[u8; 20]',
    'approvals': 'u32',
    'deposit': 'u128',
    'freezer': '[u8; 20]',
    'is_sufficient': 'bool',
    'issuer': '[u8; 20]',
    'min_balance': 'u128',
    'owner': '[u8; 20]',
    'status': ('Live', 'Frozen', 'Destroying'),
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
    'Assets', 'Metadata', ['u64']
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
0
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
0
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
0
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
0
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
0
```
#### Python
```python
constant = substrate.get_constant('Assets', 'MetadataDepositPerByte')
```
---------
### RemoveItemsLimit
 Max number of items to destroy per `destroy_accounts` and `destroy_approvals` call.

 Must be configured to result in a weight that makes each call fit in a block.
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('Assets', 'RemoveItemsLimit')
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
### AssetNotLive
The asset is not live, and likely being destroyed.

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
### IncorrectStatus
The asset status is not the expected status.

---------
### LiveAsset
The asset is a live asset and is actively being used. Usually emit for operations such
as `start_destroy` which require the asset to be in a destroying state.

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
### NotFrozen
The asset should be frozen before the given operation.

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