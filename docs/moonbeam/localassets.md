
# LocalAssets

---------
## Calls

---------
### approve_transfer
See [`Pallet::approve_transfer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 
| delegate | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'approve_transfer', {
    'amount': 'u128',
    'delegate': '[u8; 20]',
    'id': 'u128',
}
)
```

---------
### block
See [`Pallet::block`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'block', {'id': 'u128', 'who': '[u8; 20]'}
)
```

---------
### burn
See [`Pallet::burn`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 
| who | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'burn', {
    'amount': 'u128',
    'id': 'u128',
    'who': '[u8; 20]',
}
)
```

---------
### cancel_approval
See [`Pallet::cancel_approval`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 
| delegate | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'cancel_approval', {'delegate': '[u8; 20]', 'id': 'u128'}
)
```

---------
### clear_metadata
See [`Pallet::clear_metadata`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'clear_metadata', {'id': 'u128'}
)
```

---------
### create
See [`Pallet::create`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 
| admin | `AccountIdLookupOf<T>` | 
| min_balance | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'create', {
    'admin': '[u8; 20]',
    'id': 'u128',
    'min_balance': 'u128',
}
)
```

---------
### destroy_accounts
See [`Pallet::destroy_accounts`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'destroy_accounts', {'id': 'u128'}
)
```

---------
### destroy_approvals
See [`Pallet::destroy_approvals`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'destroy_approvals', {'id': 'u128'}
)
```

---------
### finish_destroy
See [`Pallet::finish_destroy`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'finish_destroy', {'id': 'u128'}
)
```

---------
### force_asset_status
See [`Pallet::force_asset_status`].
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
    'LocalAssets', 'force_asset_status', {
    'admin': '[u8; 20]',
    'freezer': '[u8; 20]',
    'id': 'u128',
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
See [`Pallet::force_cancel_approval`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 
| owner | `AccountIdLookupOf<T>` | 
| delegate | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'force_cancel_approval', {
    'delegate': '[u8; 20]',
    'id': 'u128',
    'owner': '[u8; 20]',
}
)
```

---------
### force_clear_metadata
See [`Pallet::force_clear_metadata`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'force_clear_metadata', {'id': 'u128'}
)
```

---------
### force_create
See [`Pallet::force_create`].
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
    'LocalAssets', 'force_create', {
    'id': 'u128',
    'is_sufficient': 'bool',
    'min_balance': 'u128',
    'owner': '[u8; 20]',
}
)
```

---------
### force_set_metadata
See [`Pallet::force_set_metadata`].
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
    'LocalAssets', 'force_set_metadata', {
    'decimals': 'u8',
    'id': 'u128',
    'is_frozen': 'bool',
    'name': 'Bytes',
    'symbol': 'Bytes',
}
)
```

---------
### force_transfer
See [`Pallet::force_transfer`].
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
    'LocalAssets', 'force_transfer', {
    'amount': 'u128',
    'dest': '[u8; 20]',
    'id': 'u128',
    'source': '[u8; 20]',
}
)
```

---------
### freeze
See [`Pallet::freeze`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'freeze', {'id': 'u128', 'who': '[u8; 20]'}
)
```

---------
### freeze_asset
See [`Pallet::freeze_asset`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'freeze_asset', {'id': 'u128'}
)
```

---------
### mint
See [`Pallet::mint`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 
| beneficiary | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'mint', {
    'amount': 'u128',
    'beneficiary': '[u8; 20]',
    'id': 'u128',
}
)
```

---------
### refund
See [`Pallet::refund`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 
| allow_burn | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'refund', {'allow_burn': 'bool', 'id': 'u128'}
)
```

---------
### refund_other
See [`Pallet::refund_other`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'refund_other', {'id': 'u128', 'who': '[u8; 20]'}
)
```

---------
### set_metadata
See [`Pallet::set_metadata`].
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
    'LocalAssets', 'set_metadata', {
    'decimals': 'u8',
    'id': 'u128',
    'name': 'Bytes',
    'symbol': 'Bytes',
}
)
```

---------
### set_min_balance
See [`Pallet::set_min_balance`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 
| min_balance | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'set_min_balance', {'id': 'u128', 'min_balance': 'u128'}
)
```

---------
### set_team
See [`Pallet::set_team`].
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
    'LocalAssets', 'set_team', {
    'admin': '[u8; 20]',
    'freezer': '[u8; 20]',
    'id': 'u128',
    'issuer': '[u8; 20]',
}
)
```

---------
### start_destroy
See [`Pallet::start_destroy`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'start_destroy', {'id': 'u128'}
)
```

---------
### thaw
See [`Pallet::thaw`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'thaw', {'id': 'u128', 'who': '[u8; 20]'}
)
```

---------
### thaw_asset
See [`Pallet::thaw_asset`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'thaw_asset', {'id': 'u128'}
)
```

---------
### touch
See [`Pallet::touch`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'touch', {'id': 'u128'}
)
```

---------
### touch_other
See [`Pallet::touch_other`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'touch_other', {'id': 'u128', 'who': '[u8; 20]'}
)
```

---------
### transfer
See [`Pallet::transfer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 
| target | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'transfer', {
    'amount': 'u128',
    'id': 'u128',
    'target': '[u8; 20]',
}
)
```

---------
### transfer_approved
See [`Pallet::transfer_approved`].
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
    'LocalAssets', 'transfer_approved', {
    'amount': 'u128',
    'destination': '[u8; 20]',
    'id': 'u128',
    'owner': '[u8; 20]',
}
)
```

---------
### transfer_keep_alive
See [`Pallet::transfer_keep_alive`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 
| target | `AccountIdLookupOf<T>` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'transfer_keep_alive', {
    'amount': 'u128',
    'id': 'u128',
    'target': '[u8; 20]',
}
)
```

---------
### transfer_ownership
See [`Pallet::transfer_ownership`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AssetIdParameter` | 
| owner | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LocalAssets', 'transfer_ownership', {'id': 'u128', 'owner': '[u8; 20]'}
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
| asset_id | `T::AssetId` | ```u128```
| accounts_destroyed | `u32` | ```u32```
| accounts_remaining | `u32` | ```u32```

---------
### ApprovalCancelled
An approval for account `delegate` was cancelled by `owner`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| owner | `T::AccountId` | ```[u8; 20]```
| delegate | `T::AccountId` | ```[u8; 20]```

---------
### ApprovalsDestroyed
Approvals were destroyed for given asset.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| approvals_destroyed | `u32` | ```u32```
| approvals_remaining | `u32` | ```u32```

---------
### ApprovedTransfer
(Additional) funds have been approved for transfer to a destination account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| source | `T::AccountId` | ```[u8; 20]```
| delegate | `T::AccountId` | ```[u8; 20]```
| amount | `T::Balance` | ```u128```

---------
### AssetFrozen
Some asset `asset_id` was frozen.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```

---------
### AssetMinBalanceChanged
The min_balance of an asset has been updated by the asset owner.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| new_min_balance | `T::Balance` | ```u128```

---------
### AssetStatusChanged
An asset has had its attributes changed by the `Force` origin.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```

---------
### AssetThawed
Some asset `asset_id` was thawed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```

---------
### Blocked
Some account `who` was blocked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| who | `T::AccountId` | ```[u8; 20]```

---------
### Burned
Some assets were destroyed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| owner | `T::AccountId` | ```[u8; 20]```
| balance | `T::Balance` | ```u128```

---------
### Created
Some asset class was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| creator | `T::AccountId` | ```[u8; 20]```
| owner | `T::AccountId` | ```[u8; 20]```

---------
### Destroyed
An asset class was destroyed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```

---------
### DestructionStarted
An asset class is in the process of being destroyed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```

---------
### ForceCreated
Some asset class was force-created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| owner | `T::AccountId` | ```[u8; 20]```

---------
### Frozen
Some account `who` was frozen.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| who | `T::AccountId` | ```[u8; 20]```

---------
### Issued
Some assets were issued.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| owner | `T::AccountId` | ```[u8; 20]```
| amount | `T::Balance` | ```u128```

---------
### MetadataCleared
Metadata has been cleared for an asset.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```

---------
### MetadataSet
New metadata has been set for an asset.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
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
| asset_id | `T::AssetId` | ```u128```
| owner | `T::AccountId` | ```[u8; 20]```

---------
### TeamChanged
The management team changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| issuer | `T::AccountId` | ```[u8; 20]```
| admin | `T::AccountId` | ```[u8; 20]```
| freezer | `T::AccountId` | ```[u8; 20]```

---------
### Thawed
Some account `who` was thawed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| who | `T::AccountId` | ```[u8; 20]```

---------
### Touched
Some account `who` was created with a deposit from `depositor`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
| who | `T::AccountId` | ```[u8; 20]```
| depositor | `T::AccountId` | ```[u8; 20]```

---------
### Transferred
Some assets were transferred.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u128```
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
| asset_id | `T::AssetId` | ```u128```
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
    'LocalAssets', 'Account', ['u128', '[u8; 20]']
)
```

#### Return value
```python
{
    'balance': 'u128',
    'extra': (),
    'reason': {
        'Consumer': None,
        'DepositFrom': ('[u8; 20]', 'u128'),
        'DepositHeld': 'u128',
        'DepositRefunded': None,
        'Sufficient': None,
    },
    'status': ('Liquid', 'Frozen', 'Blocked'),
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
    'LocalAssets', 'Approvals', ['u128', '[u8; 20]', '[u8; 20]']
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
    'LocalAssets', 'Asset', ['u128']
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
    'LocalAssets', 'Metadata', ['u128']
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
constant = substrate.get_constant('LocalAssets', 'ApprovalDeposit')
```
---------
### AssetAccountDeposit
 The amount of funds that must be reserved for a non-provider asset account to be
 maintained.
#### Value
```python
10180000000000000000
```
#### Python
```python
constant = substrate.get_constant('LocalAssets', 'AssetAccountDeposit')
```
---------
### AssetDeposit
 The basic amount of funds that must be reserved for an asset.
#### Value
```python
10000000000000000000000
```
#### Python
```python
constant = substrate.get_constant('LocalAssets', 'AssetDeposit')
```
---------
### MetadataDepositBase
 The basic amount of funds that must be reserved when adding metadata to your asset.
#### Value
```python
10680000000000000000
```
#### Python
```python
constant = substrate.get_constant('LocalAssets', 'MetadataDepositBase')
```
---------
### MetadataDepositPerByte
 The additional funds that must be reserved for the number of bytes you store in your
 metadata.
#### Value
```python
10000000000000000
```
#### Python
```python
constant = substrate.get_constant('LocalAssets', 'MetadataDepositPerByte')
```
---------
### RemoveItemsLimit
 Max number of items to destroy per `destroy_accounts` and `destroy_approvals` call.

 Must be configured to result in a weight that makes each call fit in a block.
#### Value
```python
656
```
#### Python
```python
constant = substrate.get_constant('LocalAssets', 'RemoveItemsLimit')
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
constant = substrate.get_constant('LocalAssets', 'StringLimit')
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
### CallbackFailed
Callback action resulted in error

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
### NotFrozen
The asset should be frozen before the given operation.

---------
### Unapproved
No approval exists that would allow the transfer.

---------
### UnavailableConsumer
Unable to increment the consumer reference counters on the account. Either no provider
reference exists to allow a non-zero balance of a non-self-sufficient asset, or one
fewer then the maximum number of consumers has been reached.

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