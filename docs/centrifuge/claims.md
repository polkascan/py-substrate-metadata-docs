
# Claims

---------
## Calls

---------
### claim
Claims tokens awarded through Tinlake investments.

\# &lt;weight&gt;
- Based on hashes length
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 
| amount | `T::Balance` | 
| sorted_hashes | `Vec<T::Hash>` | 

#### Python
```python
call = substrate.compose_call(
    'Claims', 'claim', {
    'account_id': 'AccountId',
    'amount': 'u128',
    'sorted_hashes': ['[u8; 32]'],
}
)
```

---------
### set_upload_account
Admin function that sets the allowed upload account to add root hashes
Controlled by custom origin or root

\# &lt;weight&gt;
- Based on origin check and write op
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Claims', 'set_upload_account', {'account_id': 'AccountId'}
)
```

---------
### store_root_hash
Stores root hash for correspondent claim Merkle tree run

\# &lt;weight&gt;
- Based on origin check and write op
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| root_hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Claims', 'store_root_hash', {'root_hash': '[u8; 32]'}
)
```

---------
## Events

---------
### Claimed
Event triggered after a reward claim is successfully processed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| amount | `<T as pallet_balances::Config>::Balance` | ```u128```

---------
### RootHashStored
Event triggered when the root hash is stored
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| root_hash | `<T as frame_system::Config>::Hash` | ```[u8; 32]```

---------
## Storage functions

---------
### ClaimedAmounts
 Total claimed amounts for all accounts.

#### Python
```python
result = substrate.query(
    'Claims', 'ClaimedAmounts', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### RootHash
 Root hash that correspond to lists of reward claim amounts per account.

#### Python
```python
result = substrate.query(
    'Claims', 'RootHash', []
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### UploadAccount
 Account that is allowed to upload new root hashes.

#### Python
```python
result = substrate.query(
    'Claims', 'UploadAccount', []
)
```

#### Return value
```python
'AccountId'
```
---------
## Constants

---------
### MinimalPayoutAmount
 Minimal amount that can be claimed for a reward payout.

 This constant is set via [`parameter_types`](https://substrate.dev/docs/en/knowledgebase/runtime/macros\#parameter_types)
 macro when configuring a runtime.
#### Value
```python
5000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Claims', 'MinimalPayoutAmount')
```
---------
### PalletId
 Constant configuration parameter to store the module identifier for the pallet.

 The module identifier may be of the form ```PalletId(*b&quot;rd/claim&quot;)``` and set
 using the [`parameter_types`](https://substrate.dev/docs/en/knowledgebase/runtime/macros\#parameter_types)
#### Value
```python
'0x702f636c61696d73'
```
#### Python
```python
constant = substrate.get_constant('Claims', 'PalletId')
```
---------
## Errors

---------
### InsufficientBalance
Amount being claimed is less than the available amount in [`ClaimedAmounts`].

---------
### InvalidProofs
The combination of account id, amount, and proofs vector in a claim was invalid.

---------
### MustBeAdmin
Protected operation, must be performed by admin

---------
### UnderMinPayout
The payout amount attempting to be claimed is less than the minimum allowed by [`MinimalPayoutAmount`].

---------