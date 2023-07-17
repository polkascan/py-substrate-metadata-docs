
# Uniques

---------
## Calls

---------
### approve_transfer
Approve an item to be transferred by a delegated third-party account.

The origin must conform to `ForceOrigin` or must be `Signed` and the sender must be
either the owner of the `item` or the admin of the collection.

- `collection`: The collection of the item to be approved for delegated transfer.
- `item`: The item of the item to be approved for delegated transfer.
- `delegate`: The account to delegate permission to transfer the item.

Important NOTE: The `approved` account gets reset after each transfer.

Emits `ApprovedTransfer` on success.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| delegate | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'approve_transfer', {
    'collection': 'u64',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'item': 'u128',
}
)
```

---------
### burn
Destroy a single item.

Origin must be Signed and the signing account must be either:
- the Admin of the `collection`;
- the Owner of the `item`;

- `collection`: The collection of the item to be burned.
- `item`: The item of the item to be burned.
- `check_owner`: If `Some` then the operation will fail with `WrongOwner` unless the
  item is owned by this value.

Emits `Burned` with the actual amount burned.

Weight: `O(1)`
Modes: `check_owner.is_some()`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| check_owner | `Option<AccountIdLookupOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'burn', {
    'check_owner': (
        None,
        {
            'Address20': '[u8; 20]',
            'Address32': '[u8; 32]',
            'Id': 'AccountId',
            'Index': (),
            'Raw': 'Bytes',
        },
    ),
    'collection': 'u64',
    'item': 'u128',
}
)
```

---------
### buy_item
Allows to buy an item if it&\#x27;s up for sale.

Origin must be Signed and must not be the owner of the `item`.

- `collection`: The collection of the item.
- `item`: The item the sender wants to buy.
- `bid_price`: The price the sender is willing to pay.

Emits `ItemBought` on success.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| bid_price | `ItemPrice<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'buy_item', {
    'bid_price': 'u128',
    'collection': 'u64',
    'item': 'u128',
}
)
```

---------
### cancel_approval
Cancel the prior approval for the transfer of an item by a delegate.

Origin must be either:
- the `Force` origin;
- `Signed` with the signer being the Admin of the `collection`;
- `Signed` with the signer being the Owner of the `item`;

Arguments:
- `collection`: The collection of the item of whose approval will be cancelled.
- `item`: The item of the item of whose approval will be cancelled.
- `maybe_check_delegate`: If `Some` will ensure that the given account is the one to
  which permission of transfer is delegated.

Emits `ApprovalCancelled` on success.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| maybe_check_delegate | `Option<AccountIdLookupOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'cancel_approval', {
    'collection': 'u64',
    'item': 'u128',
    'maybe_check_delegate': (
        None,
        {
            'Address20': '[u8; 20]',
            'Address32': '[u8; 32]',
            'Id': 'AccountId',
            'Index': (),
            'Raw': 'Bytes',
        },
    ),
}
)
```

---------
### clear_attribute
Clear an attribute for a collection or item.

Origin must be either `ForceOrigin` or Signed and the sender should be the Owner of the
`collection`.

Any deposit is freed for the collection&\#x27;s owner.

- `collection`: The identifier of the collection whose item&\#x27;s metadata to clear.
- `maybe_item`: The identifier of the item whose metadata to clear.
- `key`: The key of the attribute.

Emits `AttributeCleared`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| maybe_item | `Option<T::ItemId>` | 
| key | `BoundedVec<u8, T::KeyLimit>` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'clear_attribute', {
    'collection': 'u64',
    'key': 'Bytes',
    'maybe_item': (None, 'u128'),
}
)
```

---------
### clear_collection_metadata
Clear the metadata for a collection.

Origin must be either `ForceOrigin` or `Signed` and the sender should be the Owner of
the `collection`.

Any deposit is freed for the collection&\#x27;s owner.

- `collection`: The identifier of the collection whose metadata to clear.

Emits `CollectionMetadataCleared`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'clear_collection_metadata', {'collection': 'u64'}
)
```

---------
### clear_metadata
Clear the metadata for an item.

Origin must be either `ForceOrigin` or Signed and the sender should be the Owner of the
`item`.

Any deposit is freed for the collection&\#x27;s owner.

- `collection`: The identifier of the collection whose item&\#x27;s metadata to clear.
- `item`: The identifier of the item whose metadata to clear.

Emits `MetadataCleared`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'clear_metadata', {'collection': 'u64', 'item': 'u128'}
)
```

---------
### create
Issue a new collection of non-fungible items from a public origin.

This new collection has no items initially and its owner is the origin.

The origin must conform to the configured `CreateOrigin` and have sufficient funds free.

`ItemDeposit` funds of sender are reserved.

Parameters:
- `collection`: The identifier of the new collection. This must not be currently in use.
- `admin`: The admin of this collection. The admin is the initial address of each
member of the collection&\#x27;s admin team.

Emits `Created` event when successful.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| admin | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'create', {
    'admin': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'collection': 'u64',
}
)
```

---------
### destroy
Destroy a collection of fungible items.

The origin must conform to `ForceOrigin` or must be `Signed` and the sender must be the
owner of the `collection`.

- `collection`: The identifier of the collection to be destroyed.
- `witness`: Information on the items minted in the collection. This must be
correct.

Emits `Destroyed` event when successful.

Weight: `O(n + m)` where:
- `n = witness.items`
- `m = witness.item_metadatas`
- `a = witness.attributes`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| witness | `DestroyWitness` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'destroy', {
    'collection': 'u64',
    'witness': {
        'attributes': 'u32',
        'item_metadatas': 'u32',
        'items': 'u32',
    },
}
)
```

---------
### force_create
Issue a new collection of non-fungible items from a privileged origin.

This new collection has no items initially.

The origin must conform to `ForceOrigin`.

Unlike `create`, no funds are reserved.

- `collection`: The identifier of the new item. This must not be currently in use.
- `owner`: The owner of this collection of items. The owner has full superuser
  permissions
over this item, but may later change and configure the permissions using
`transfer_ownership` and `set_team`.

Emits `ForceCreated` event when successful.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| owner | `AccountIdLookupOf<T>` | 
| free_holding | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'force_create', {
    'collection': 'u64',
    'free_holding': 'bool',
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
### force_item_status
Alter the attributes of a given item.

Origin must be `ForceOrigin`.

- `collection`: The identifier of the item.
- `owner`: The new Owner of this item.
- `issuer`: The new Issuer of this item.
- `admin`: The new Admin of this item.
- `freezer`: The new Freezer of this item.
- `free_holding`: Whether a deposit is taken for holding an item of this collection.
- `is_frozen`: Whether this collection is frozen except for permissioned/admin
instructions.

Emits `ItemStatusChanged` with the identity of the item.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| owner | `AccountIdLookupOf<T>` | 
| issuer | `AccountIdLookupOf<T>` | 
| admin | `AccountIdLookupOf<T>` | 
| freezer | `AccountIdLookupOf<T>` | 
| free_holding | `bool` | 
| is_frozen | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'force_item_status', {
    'admin': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'collection': 'u64',
    'free_holding': 'bool',
    'freezer': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'is_frozen': 'bool',
    'issuer': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
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
### freeze
Disallow further unprivileged transfer of an item.

Origin must be Signed and the sender should be the Freezer of the `collection`.

- `collection`: The collection of the item to be frozen.
- `item`: The item of the item to be frozen.

Emits `Frozen`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'freeze', {'collection': 'u64', 'item': 'u128'}
)
```

---------
### freeze_collection
Disallow further unprivileged transfers for a whole collection.

Origin must be Signed and the sender should be the Freezer of the `collection`.

- `collection`: The collection to be frozen.

Emits `CollectionFrozen`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'freeze_collection', {'collection': 'u64'}
)
```

---------
### mint
Mint an item of a particular collection.

The origin must be Signed and the sender must be the Issuer of the `collection`.

- `collection`: The collection of the item to be minted.
- `item`: The item value of the item to be minted.
- `beneficiary`: The initial owner of the minted item.

Emits `Issued` event when successful.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| owner | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'mint', {
    'collection': 'u64',
    'item': 'u128',
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
### redeposit
Reevaluate the deposits on some items.

Origin must be Signed and the sender should be the Owner of the `collection`.

- `collection`: The collection to be frozen.
- `items`: The items of the collection whose deposits will be reevaluated.

NOTE: This exists as a best-effort function. Any items which are unknown or
in the case that the owner account does not have reservable funds to pay for a
deposit increase are ignored. Generally the owner isn&\#x27;t going to call this on items
whose existing deposit is less than the refreshed deposit as it would only cost them,
so it&\#x27;s of little consequence.

It will still return an error in the case that the collection is unknown of the signer
is not permitted to call it.

Weight: `O(items.len())`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| items | `Vec<T::ItemId>` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'redeposit', {
    'collection': 'u64',
    'items': ['u128'],
}
)
```

---------
### set_accept_ownership
Set (or reset) the acceptance of ownership for a particular account.

Origin must be `Signed` and if `maybe_collection` is `Some`, then the signer must have a
provider reference.

- `maybe_collection`: The identifier of the collection whose ownership the signer is
  willing to accept, or if `None`, an indication that the signer is willing to accept no
  ownership transferal.

Emits `OwnershipAcceptanceChanged`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| maybe_collection | `Option<T::CollectionId>` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'set_accept_ownership', {'maybe_collection': (None, 'u64')}
)
```

---------
### set_attribute
Set an attribute for a collection or item.

Origin must be either `ForceOrigin` or Signed and the sender should be the Owner of the
`collection`.

If the origin is Signed, then funds of signer are reserved according to the formula:
`MetadataDepositBase + DepositPerByte * (key.len + value.len)` taking into
account any already reserved funds.

- `collection`: The identifier of the collection whose item&\#x27;s metadata to set.
- `maybe_item`: The identifier of the item whose metadata to set.
- `key`: The key of the attribute.
- `value`: The value to which to set the attribute.

Emits `AttributeSet`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| maybe_item | `Option<T::ItemId>` | 
| key | `BoundedVec<u8, T::KeyLimit>` | 
| value | `BoundedVec<u8, T::ValueLimit>` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'set_attribute', {
    'collection': 'u64',
    'key': 'Bytes',
    'maybe_item': (None, 'u128'),
    'value': 'Bytes',
}
)
```

---------
### set_collection_max_supply
Set the maximum amount of items a collection could have.

Origin must be either `ForceOrigin` or `Signed` and the sender should be the Owner of
the `collection`.

Note: This function can only succeed once per collection.

- `collection`: The identifier of the collection to change.
- `max_supply`: The maximum amount of items a collection could have.

Emits `CollectionMaxSupplySet` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| max_supply | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'set_collection_max_supply', {
    'collection': 'u64',
    'max_supply': 'u32',
}
)
```

---------
### set_collection_metadata
Set the metadata for a collection.

Origin must be either `ForceOrigin` or `Signed` and the sender should be the Owner of
the `collection`.

If the origin is `Signed`, then funds of signer are reserved according to the formula:
`MetadataDepositBase + DepositPerByte * data.len` taking into
account any already reserved funds.

- `collection`: The identifier of the item whose metadata to update.
- `data`: The general information of this item. Limited in length by `StringLimit`.
- `is_frozen`: Whether the metadata should be frozen against further changes.

Emits `CollectionMetadataSet`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| data | `BoundedVec<u8, T::StringLimit>` | 
| is_frozen | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'set_collection_metadata', {
    'collection': 'u64',
    'data': 'Bytes',
    'is_frozen': 'bool',
}
)
```

---------
### set_metadata
Set the metadata for an item.

Origin must be either `ForceOrigin` or Signed and the sender should be the Owner of the
`collection`.

If the origin is Signed, then funds of signer are reserved according to the formula:
`MetadataDepositBase + DepositPerByte * data.len` taking into
account any already reserved funds.

- `collection`: The identifier of the collection whose item&\#x27;s metadata to set.
- `item`: The identifier of the item whose metadata to set.
- `data`: The general information of this item. Limited in length by `StringLimit`.
- `is_frozen`: Whether the metadata should be frozen against further changes.

Emits `MetadataSet`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| data | `BoundedVec<u8, T::StringLimit>` | 
| is_frozen | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'set_metadata', {
    'collection': 'u64',
    'data': 'Bytes',
    'is_frozen': 'bool',
    'item': 'u128',
}
)
```

---------
### set_price
Set (or reset) the price for an item.

Origin must be Signed and must be the owner of the asset `item`.

- `collection`: The collection of the item.
- `item`: The item to set the price for.
- `price`: The price for the item. Pass `None`, to reset the price.
- `buyer`: Restricts the buy operation to a specific account.

Emits `ItemPriceSet` on success if the price is not `None`.
Emits `ItemPriceRemoved` on success if the price is `None`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| price | `Option<ItemPrice<T, I>>` | 
| whitelisted_buyer | `Option<AccountIdLookupOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'set_price', {
    'collection': 'u64',
    'item': 'u128',
    'price': (None, 'u128'),
    'whitelisted_buyer': (
        None,
        {
            'Address20': '[u8; 20]',
            'Address32': '[u8; 32]',
            'Id': 'AccountId',
            'Index': (),
            'Raw': 'Bytes',
        },
    ),
}
)
```

---------
### set_team
Change the Issuer, Admin and Freezer of a collection.

Origin must be Signed and the sender should be the Owner of the `collection`.

- `collection`: The collection whose team should be changed.
- `issuer`: The new Issuer of this collection.
- `admin`: The new Admin of this collection.
- `freezer`: The new Freezer of this collection.

Emits `TeamChanged`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| issuer | `AccountIdLookupOf<T>` | 
| admin | `AccountIdLookupOf<T>` | 
| freezer | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'set_team', {
    'admin': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'collection': 'u64',
    'freezer': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
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
Re-allow unprivileged transfer of an item.

Origin must be Signed and the sender should be the Freezer of the `collection`.

- `collection`: The collection of the item to be thawed.
- `item`: The item of the item to be thawed.

Emits `Thawed`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'thaw', {'collection': 'u64', 'item': 'u128'}
)
```

---------
### thaw_collection
Re-allow unprivileged transfers for a whole collection.

Origin must be Signed and the sender should be the Admin of the `collection`.

- `collection`: The collection to be thawed.

Emits `CollectionThawed`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'thaw_collection', {'collection': 'u64'}
)
```

---------
### transfer
Move an item from the sender account to another.

This resets the approved account of the item.

Origin must be Signed and the signing account must be either:
- the Admin of the `collection`;
- the Owner of the `item`;
- the approved delegate for the `item` (in this case, the approval is reset).

Arguments:
- `collection`: The collection of the item to be transferred.
- `item`: The item of the item to be transferred.
- `dest`: The account to receive ownership of the item.

Emits `Transferred`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| dest | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'transfer', {
    'collection': 'u64',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'item': 'u128',
}
)
```

---------
### transfer_ownership
Change the Owner of a collection.

Origin must be Signed and the sender should be the Owner of the `collection`.

- `collection`: The collection whose owner should be changed.
- `owner`: The new Owner of this collection. They must have called
  `set_accept_ownership` with `collection` in order for this operation to succeed.

Emits `OwnerChanged`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| owner | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'transfer_ownership', {
    'collection': 'u64',
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
An approval for a `delegate` account to transfer the `item` of an item
`collection` was cancelled by its `owner`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| item | `T::ItemId` | ```u128```
| owner | `T::AccountId` | ```AccountId```
| delegate | `T::AccountId` | ```AccountId```

---------
### ApprovedTransfer
An `item` of a `collection` has been approved by the `owner` for transfer by
a `delegate`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| item | `T::ItemId` | ```u128```
| owner | `T::AccountId` | ```AccountId```
| delegate | `T::AccountId` | ```AccountId```

---------
### AttributeCleared
Attribute metadata has been cleared for a `collection` or `item`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| maybe_item | `Option<T::ItemId>` | ```(None, 'u128')```
| key | `BoundedVec<u8, T::KeyLimit>` | ```Bytes```

---------
### AttributeSet
New attribute metadata has been set for a `collection` or `item`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| maybe_item | `Option<T::ItemId>` | ```(None, 'u128')```
| key | `BoundedVec<u8, T::KeyLimit>` | ```Bytes```
| value | `BoundedVec<u8, T::ValueLimit>` | ```Bytes```

---------
### Burned
An `item` was destroyed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| item | `T::ItemId` | ```u128```
| owner | `T::AccountId` | ```AccountId```

---------
### CollectionFrozen
Some `collection` was frozen.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```

---------
### CollectionMaxSupplySet
Max supply has been set for a collection.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| max_supply | `u32` | ```u32```

---------
### CollectionMetadataCleared
Metadata has been cleared for a `collection`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```

---------
### CollectionMetadataSet
New metadata has been set for a `collection`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| data | `BoundedVec<u8, T::StringLimit>` | ```Bytes```
| is_frozen | `bool` | ```bool```

---------
### CollectionThawed
Some `collection` was thawed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```

---------
### Created
A `collection` was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| creator | `T::AccountId` | ```AccountId```
| owner | `T::AccountId` | ```AccountId```

---------
### Destroyed
A `collection` was destroyed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```

---------
### ForceCreated
A `collection` was force-created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| owner | `T::AccountId` | ```AccountId```

---------
### Frozen
Some `item` was frozen.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| item | `T::ItemId` | ```u128```

---------
### Issued
An `item` was issued.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| item | `T::ItemId` | ```u128```
| owner | `T::AccountId` | ```AccountId```

---------
### ItemBought
An item was bought.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| item | `T::ItemId` | ```u128```
| price | `ItemPrice<T, I>` | ```u128```
| seller | `T::AccountId` | ```AccountId```
| buyer | `T::AccountId` | ```AccountId```

---------
### ItemPriceRemoved
The price for the instance was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| item | `T::ItemId` | ```u128```

---------
### ItemPriceSet
The price was set for the instance.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| item | `T::ItemId` | ```u128```
| price | `ItemPrice<T, I>` | ```u128```
| whitelisted_buyer | `Option<T::AccountId>` | ```(None, 'AccountId')```

---------
### ItemStatusChanged
A `collection` has had its attributes changed by the `Force` origin.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```

---------
### MetadataCleared
Metadata has been cleared for an item.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| item | `T::ItemId` | ```u128```

---------
### MetadataSet
New metadata has been set for an item.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| item | `T::ItemId` | ```u128```
| data | `BoundedVec<u8, T::StringLimit>` | ```Bytes```
| is_frozen | `bool` | ```bool```

---------
### OwnerChanged
The owner changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| new_owner | `T::AccountId` | ```AccountId```

---------
### OwnershipAcceptanceChanged
Ownership acceptance has changed for an account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| maybe_collection | `Option<T::CollectionId>` | ```(None, 'u64')```

---------
### Redeposited
Metadata has been cleared for an item.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| successful_items | `Vec<T::ItemId>` | ```['u128']```

---------
### TeamChanged
The management team changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| issuer | `T::AccountId` | ```AccountId```
| admin | `T::AccountId` | ```AccountId```
| freezer | `T::AccountId` | ```AccountId```

---------
### Thawed
Some `item` was thawed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| item | `T::ItemId` | ```u128```

---------
### Transferred
An `item` was transferred.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u64```
| item | `T::ItemId` | ```u128```
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### Account
 The items held by any given account; set out this way so that items owned by a single
 account can be enumerated.

#### Python
```python
result = substrate.query(
    'Uniques', 'Account', ['AccountId', 'u64', 'u128']
)
```

#### Return value
```python
()
```
---------
### Asset
 The items in existence and their ownership details.

#### Python
```python
result = substrate.query(
    'Uniques', 'Asset', ['u64', 'u128']
)
```

#### Return value
```python
{'approved': (None, 'AccountId'), 'deposit': 'u128', 'is_frozen': 'bool', 'owner': 'AccountId'}
```
---------
### Attribute
 Attributes of a collection.

#### Python
```python
result = substrate.query(
    'Uniques', 'Attribute', ['u64', (None, 'u128'), 'Bytes']
)
```

#### Return value
```python
('Bytes', 'u128')
```
---------
### Class
 Details of a collection.

#### Python
```python
result = substrate.query(
    'Uniques', 'Class', ['u64']
)
```

#### Return value
```python
{
    'admin': 'AccountId',
    'attributes': 'u32',
    'free_holding': 'bool',
    'freezer': 'AccountId',
    'is_frozen': 'bool',
    'issuer': 'AccountId',
    'item_metadatas': 'u32',
    'items': 'u32',
    'owner': 'AccountId',
    'total_deposit': 'u128',
}
```
---------
### ClassAccount
 The collections owned by any given account; set out this way so that collections owned by
 a single account can be enumerated.

#### Python
```python
result = substrate.query(
    'Uniques', 'ClassAccount', ['AccountId', 'u64']
)
```

#### Return value
```python
()
```
---------
### ClassMetadataOf
 Metadata of a collection.

#### Python
```python
result = substrate.query(
    'Uniques', 'ClassMetadataOf', ['u64']
)
```

#### Return value
```python
{'data': 'Bytes', 'deposit': 'u128', 'is_frozen': 'bool'}
```
---------
### CollectionMaxSupply
 Keeps track of the number of items a collection might have.

#### Python
```python
result = substrate.query(
    'Uniques', 'CollectionMaxSupply', ['u64']
)
```

#### Return value
```python
'u32'
```
---------
### InstanceMetadataOf
 Metadata of an item.

#### Python
```python
result = substrate.query(
    'Uniques', 'InstanceMetadataOf', ['u64', 'u128']
)
```

#### Return value
```python
{'data': 'Bytes', 'deposit': 'u128', 'is_frozen': 'bool'}
```
---------
### ItemPriceOf
 Price of an asset instance.

#### Python
```python
result = substrate.query(
    'Uniques', 'ItemPriceOf', ['u64', 'u128']
)
```

#### Return value
```python
('u128', (None, 'AccountId'))
```
---------
### OwnershipAcceptance
 The collection, if any, of which an account is willing to take ownership.

#### Python
```python
result = substrate.query(
    'Uniques', 'OwnershipAcceptance', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### AttributeDepositBase
 The basic amount of funds that must be reserved when adding an attribute to an item.
#### Value
```python
100000000000000000
```
#### Python
```python
constant = substrate.get_constant('Uniques', 'AttributeDepositBase')
```
---------
### CollectionDeposit
 The basic amount of funds that must be reserved for collection.
#### Value
```python
1000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Uniques', 'CollectionDeposit')
```
---------
### DepositPerByte
 The additional funds that must be reserved for the number of bytes store in metadata,
 either &quot;normal&quot; metadata or attribute metadata.
#### Value
```python
10000000000000000
```
#### Python
```python
constant = substrate.get_constant('Uniques', 'DepositPerByte')
```
---------
### ItemDeposit
 The basic amount of funds that must be reserved for an item.
#### Value
```python
100000000000000000
```
#### Python
```python
constant = substrate.get_constant('Uniques', 'ItemDeposit')
```
---------
### KeyLimit
 The maximum length of an attribute key.
#### Value
```python
256
```
#### Python
```python
constant = substrate.get_constant('Uniques', 'KeyLimit')
```
---------
### MetadataDepositBase
 The basic amount of funds that must be reserved when adding metadata to your item.
#### Value
```python
100000000000000000
```
#### Python
```python
constant = substrate.get_constant('Uniques', 'MetadataDepositBase')
```
---------
### StringLimit
 The maximum length of data stored on-chain.
#### Value
```python
256
```
#### Python
```python
constant = substrate.get_constant('Uniques', 'StringLimit')
```
---------
### ValueLimit
 The maximum length of an attribute value.
#### Value
```python
256
```
#### Python
```python
constant = substrate.get_constant('Uniques', 'ValueLimit')
```
---------
## Errors

---------
### AlreadyExists
The item ID has already been used for an item.

---------
### BadWitness
Invalid witness data given.

---------
### BidTooLow
The provided bid is too low.

---------
### Frozen
The item or collection is frozen.

---------
### InUse
The item ID is already taken.

---------
### Locked
The item is locked.

---------
### MaxSupplyAlreadySet
The max supply has already been set.

---------
### MaxSupplyReached
All items have been minted.

---------
### MaxSupplyTooSmall
The provided max supply is less to the amount of items a collection already has.

---------
### NoDelegate
There is no delegate approved.

---------
### NoPermission
The signing account has no permission to do the operation.

---------
### NotForSale
Item is not for sale.

---------
### Unaccepted
The named owner has not signed ownership of the collection is acceptable.

---------
### Unapproved
No approval exists that would allow the transfer.

---------
### UnknownCollection
The given item ID is unknown.

---------
### UnknownItem
The given item ID is unknown.

---------
### WrongDelegate
The delegate turned out to be different to what was expected.

---------
### WrongOwner
The owner turned out to be different to what was expected.

---------