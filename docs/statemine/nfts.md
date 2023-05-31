
# Nfts

---------
## Calls

---------
### approve_item_attributes
Approve item&\#x27;s attributes to be changed by a delegated third-party account.

Origin must be Signed and must be an owner of the `item`.

- `collection`: A collection of the item.
- `item`: The item that holds attributes.
- `delegate`: The account to delegate permission to change attributes of the item.

Emits `ItemAttributesApprovalAdded` on success.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| delegate | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'approve_item_attributes', {
    'collection': 'u32',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'item': 'u32',
}
)
```

---------
### approve_transfer
Approve an item to be transferred by a delegated third-party account.

Origin must be either `ForceOrigin` or Signed and the sender should be the Owner of the
`item`.

- `collection`: The collection of the item to be approved for delegated transfer.
- `item`: The item to be approved for delegated transfer.
- `delegate`: The account to delegate permission to transfer the item.
- `maybe_deadline`: Optional deadline for the approval. Specified by providing the
	number of blocks after which the approval will expire

Emits `TransferApproved` on success.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| delegate | `AccountIdLookupOf<T>` | 
| maybe_deadline | `Option<<T as SystemConfig>::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'approve_transfer', {
    'collection': 'u32',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'item': 'u32',
    'maybe_deadline': (None, 'u32'),
}
)
```

---------
### burn
Destroy a single item.

The origin must conform to `ForceOrigin` or must be Signed and the signing account must
be the owner of the `item`.

- `collection`: The collection of the item to be burned.
- `item`: The item to be burned.

Emits `Burned`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'burn', {'collection': 'u32', 'item': 'u32'}
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
    'Nfts', 'buy_item', {
    'bid_price': 'u128',
    'collection': 'u32',
    'item': 'u32',
}
)
```

---------
### cancel_approval
Cancel one of the transfer approvals for a specific item.

Origin must be either:
- the `Force` origin;
- `Signed` with the signer being the Owner of the `item`;

Arguments:
- `collection`: The collection of the item of whose approval will be cancelled.
- `item`: The item of the collection of whose approval will be cancelled.
- `delegate`: The account that is going to loose their approval.

Emits `ApprovalCancelled` on success.

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
    'Nfts', 'cancel_approval', {
    'collection': 'u32',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'item': 'u32',
}
)
```

---------
### cancel_item_attributes_approval
Cancel the previously provided approval to change item&\#x27;s attributes.
All the previously set attributes by the `delegate` will be removed.

Origin must be Signed and must be an owner of the `item`.

- `collection`: Collection that the item is contained within.
- `item`: The item that holds attributes.
- `delegate`: The previously approved account to remove.

Emits `ItemAttributesApprovalRemoved` on success.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| delegate | `AccountIdLookupOf<T>` | 
| witness | `CancelAttributesApprovalWitness` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'cancel_item_attributes_approval', {
    'collection': 'u32',
    'delegate': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'item': 'u32',
    'witness': {
        'account_attributes': 'u32',
    },
}
)
```

---------
### cancel_swap
Cancel an atomic swap.

Origin must be Signed.
Origin must be an owner of the `item` if the deadline hasn&\#x27;t expired.

- `collection`: The collection of the item.
- `item`: The item an owner wants to give.

Emits `SwapCancelled` on success.
#### Attributes
| Name | Type |
| -------- | -------- | 
| offered_collection | `T::CollectionId` | 
| offered_item | `T::ItemId` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'cancel_swap', {
    'offered_collection': 'u32',
    'offered_item': 'u32',
}
)
```

---------
### claim_swap
Claim an atomic swap.
This method executes a pending swap, that was created by a counterpart before.

Origin must be Signed and must be an owner of the `item`.

- `send_collection`: The collection of the item to be sent.
- `send_item`: The item to be sent.
- `receive_collection`: The collection of the item to be received.
- `receive_item`: The item to be received.
- `witness_price`: A price that was previously agreed on.

Emits `SwapClaimed` on success.
#### Attributes
| Name | Type |
| -------- | -------- | 
| send_collection | `T::CollectionId` | 
| send_item | `T::ItemId` | 
| receive_collection | `T::CollectionId` | 
| receive_item | `T::ItemId` | 
| witness_price | `Option<PriceWithDirection<ItemPrice<T, I>>>` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'claim_swap', {
    'receive_collection': 'u32',
    'receive_item': 'u32',
    'send_collection': 'u32',
    'send_item': 'u32',
    'witness_price': (
        None,
        {
            'amount': 'u128',
            'direction': (
                'Send',
                'Receive',
            ),
        },
    ),
}
)
```

---------
### clear_all_transfer_approvals
Cancel all the approvals of a specific item.

Origin must be either:
- the `Force` origin;
- `Signed` with the signer being the Owner of the `item`;

Arguments:
- `collection`: The collection of the item of whose approvals will be cleared.
- `item`: The item of the collection of whose approvals will be cleared.

Emits `AllApprovalsCancelled` on success.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'clear_all_transfer_approvals', {'collection': 'u32', 'item': 'u32'}
)
```

---------
### clear_attribute
Clear an attribute for a collection or item.

Origin must be either `ForceOrigin` or Signed and the sender should be the Owner of the
attribute.

Any deposit is freed for the collection&\#x27;s owner.

- `collection`: The identifier of the collection whose item&\#x27;s metadata to clear.
- `maybe_item`: The identifier of the item whose metadata to clear.
- `namespace`: Attribute&\#x27;s namespace.
- `key`: The key of the attribute.

Emits `AttributeCleared`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| maybe_item | `Option<T::ItemId>` | 
| namespace | `AttributeNamespace<T::AccountId>` | 
| key | `BoundedVec<u8, T::KeyLimit>` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'clear_attribute', {
    'collection': 'u32',
    'key': 'Bytes',
    'maybe_item': (None, 'u32'),
    'namespace': {
        'Account': 'AccountId',
        'CollectionOwner': None,
        'ItemOwner': None,
        'Pallet': None,
    },
}
)
```

---------
### clear_collection_metadata
Clear the metadata for a collection.

Origin must be either `ForceOrigin` or `Signed` and the sender should be the Admin of
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
    'Nfts', 'clear_collection_metadata', {'collection': 'u32'}
)
```

---------
### clear_metadata
Clear the metadata for an item.

Origin must be either `ForceOrigin` or Signed and the sender should be the Admin of the
`collection`.

Any deposit is freed for the collection&\#x27;s owner.

- `collection`: The identifier of the collection whose item&\#x27;s metadata to clear.
- `item`: The identifier of the item whose metadata to clear.

Emits `ItemMetadataCleared`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'clear_metadata', {'collection': 'u32', 'item': 'u32'}
)
```

---------
### create
Issue a new collection of non-fungible items from a public origin.

This new collection has no items initially and its owner is the origin.

The origin must be Signed and the sender must have sufficient funds free.

`ItemDeposit` funds of sender are reserved.

Parameters:
- `admin`: The admin of this collection. The admin is the initial address of each
member of the collection&\#x27;s admin team.

Emits `Created` event when successful.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| admin | `AccountIdLookupOf<T>` | 
| config | `CollectionConfigFor<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'create', {
    'admin': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'config': {
        'max_supply': (None, 'u32'),
        'mint_settings': {
            'default_item_settings': 'u64',
            'end_block': (None, 'u32'),
            'mint_type': {
                'HolderOf': 'u32',
                'Issuer': None,
                'Public': None,
            },
            'price': (None, 'u128'),
            'start_block': (
                None,
                'u32',
            ),
        },
        'settings': 'u64',
    },
}
)
```

---------
### create_swap
Register a new atomic swap, declaring an intention to send an `item` in exchange for
`desired_item` from origin to target on the current blockchain.
The target can execute the swap during the specified `duration` of blocks (if set).
Additionally, the price could be set for the desired `item`.

Origin must be Signed and must be an owner of the `item`.

- `collection`: The collection of the item.
- `item`: The item an owner wants to give.
- `desired_collection`: The collection of the desired item.
- `desired_item`: The desired item an owner wants to receive.
- `maybe_price`: The price an owner is willing to pay or receive for the desired `item`.
- `duration`: A deadline for the swap. Specified by providing the number of blocks
	after which the swap will expire.

Emits `SwapCreated` on success.
#### Attributes
| Name | Type |
| -------- | -------- | 
| offered_collection | `T::CollectionId` | 
| offered_item | `T::ItemId` | 
| desired_collection | `T::CollectionId` | 
| maybe_desired_item | `Option<T::ItemId>` | 
| maybe_price | `Option<PriceWithDirection<ItemPrice<T, I>>>` | 
| duration | `<T as SystemConfig>::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'create_swap', {
    'desired_collection': 'u32',
    'duration': 'u32',
    'maybe_desired_item': (
        None,
        'u32',
    ),
    'maybe_price': (
        None,
        {
            'amount': 'u128',
            'direction': (
                'Send',
                'Receive',
            ),
        },
    ),
    'offered_collection': 'u32',
    'offered_item': 'u32',
}
)
```

---------
### destroy
Destroy a collection of fungible items.

The origin must conform to `ForceOrigin` or must be `Signed` and the sender must be the
owner of the `collection`.

NOTE: The collection must have 0 items to be destroyed.

- `collection`: The identifier of the collection to be destroyed.
- `witness`: Information on the items minted in the collection. This must be
correct.

Emits `Destroyed` event when successful.

Weight: `O(m + c + a)` where:
- `m = witness.item_metadatas`
- `c = witness.item_configs`
- `a = witness.attributes`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| witness | `DestroyWitness` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'destroy', {
    'collection': 'u32',
    'witness': {
        'attributes': 'u32',
        'item_configs': 'u32',
        'item_metadatas': 'u32',
    },
}
)
```

---------
### force_collection_config
Change the config of a collection.

Origin must be `ForceOrigin`.

- `collection`: The identifier of the collection.
- `config`: The new config of this collection.

Emits `CollectionConfigChanged`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| config | `CollectionConfigFor<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'force_collection_config', {
    'collection': 'u32',
    'config': {
        'max_supply': (None, 'u32'),
        'mint_settings': {
            'default_item_settings': 'u64',
            'end_block': (None, 'u32'),
            'mint_type': {
                'HolderOf': 'u32',
                'Issuer': None,
                'Public': None,
            },
            'price': (None, 'u128'),
            'start_block': (
                None,
                'u32',
            ),
        },
        'settings': 'u64',
    },
}
)
```

---------
### force_collection_owner
Change the Owner of a collection.

Origin must be `ForceOrigin`.

- `collection`: The identifier of the collection.
- `owner`: The new Owner of this collection.

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
    'Nfts', 'force_collection_owner', {
    'collection': 'u32',
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
### force_create
Issue a new collection of non-fungible items from a privileged origin.

This new collection has no items initially.

The origin must conform to `ForceOrigin`.

Unlike `create`, no funds are reserved.

- `owner`: The owner of this collection of items. The owner has full superuser
  permissions over this item, but may later change and configure the permissions using
  `transfer_ownership` and `set_team`.

Emits `ForceCreated` event when successful.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner | `AccountIdLookupOf<T>` | 
| config | `CollectionConfigFor<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'force_create', {
    'config': {
        'max_supply': (None, 'u32'),
        'mint_settings': {
            'default_item_settings': 'u64',
            'end_block': (None, 'u32'),
            'mint_type': {
                'HolderOf': 'u32',
                'Issuer': None,
                'Public': None,
            },
            'price': (None, 'u128'),
            'start_block': (
                None,
                'u32',
            ),
        },
        'settings': 'u64',
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
### force_mint
Mint an item of a particular collection from a privileged origin.

The origin must conform to `ForceOrigin` or must be `Signed` and the sender must be the
Issuer of the `collection`.

- `collection`: The collection of the item to be minted.
- `item`: An identifier of the new item.
- `mint_to`: Account into which the item will be minted.
- `item_config`: A config of the new item.

Emits `Issued` event when successful.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| mint_to | `AccountIdLookupOf<T>` | 
| item_config | `ItemConfig` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'force_mint', {
    'collection': 'u32',
    'item': 'u32',
    'item_config': {'settings': 'u64'},
    'mint_to': {
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
### force_set_attribute
Force-set an attribute for a collection or item.

Origin must be `ForceOrigin`.

If the attribute already exists and it was set by another account, the deposit
will be returned to the previous owner.

- `set_as`: An optional owner of the attribute.
- `collection`: The identifier of the collection whose item&\#x27;s metadata to set.
- `maybe_item`: The identifier of the item whose metadata to set.
- `namespace`: Attribute&\#x27;s namespace.
- `key`: The key of the attribute.
- `value`: The value to which to set the attribute.

Emits `AttributeSet`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| set_as | `Option<T::AccountId>` | 
| collection | `T::CollectionId` | 
| maybe_item | `Option<T::ItemId>` | 
| namespace | `AttributeNamespace<T::AccountId>` | 
| key | `BoundedVec<u8, T::KeyLimit>` | 
| value | `BoundedVec<u8, T::ValueLimit>` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'force_set_attribute', {
    'collection': 'u32',
    'key': 'Bytes',
    'maybe_item': (None, 'u32'),
    'namespace': {
        'Account': 'AccountId',
        'CollectionOwner': None,
        'ItemOwner': None,
        'Pallet': None,
    },
    'set_as': (None, 'AccountId'),
    'value': 'Bytes',
}
)
```

---------
### lock_collection
Disallows specified settings for the whole collection.

Origin must be Signed and the sender should be the Owner of the `collection`.

- `collection`: The collection to be locked.
- `lock_settings`: The settings to be locked.

Note: it&\#x27;s possible to only lock(set) the setting, but not to unset it.

Emits `CollectionLocked`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| lock_settings | `CollectionSettings` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'lock_collection', {
    'collection': 'u32',
    'lock_settings': 'u64',
}
)
```

---------
### lock_item_properties
Disallows changing the metadata or attributes of the item.

Origin must be either `ForceOrigin` or Signed and the sender should be the Admin
of the `collection`.

- `collection`: The collection if the `item`.
- `item`: An item to be locked.
- `lock_metadata`: Specifies whether the metadata should be locked.
- `lock_attributes`: Specifies whether the attributes in the `CollectionOwner` namespace
  should be locked.

Note: `lock_attributes` affects the attributes in the `CollectionOwner` namespace only.
When the metadata or attributes are locked, it won&\#x27;t be possible the unlock them.

Emits `ItemPropertiesLocked`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| lock_metadata | `bool` | 
| lock_attributes | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'lock_item_properties', {
    'collection': 'u32',
    'item': 'u32',
    'lock_attributes': 'bool',
    'lock_metadata': 'bool',
}
)
```

---------
### lock_item_transfer
Disallow further unprivileged transfer of an item.

Origin must be Signed and the sender should be the Freezer of the `collection`.

- `collection`: The collection of the item to be changed.
- `item`: The item to become non-transferable.

Emits `ItemTransferLocked`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'lock_item_transfer', {'collection': 'u32', 'item': 'u32'}
)
```

---------
### mint
Mint an item of a particular collection.

The origin must be Signed and the sender must comply with the `mint_settings` rules.

- `collection`: The collection of the item to be minted.
- `item`: An identifier of the new item.
- `mint_to`: Account into which the item will be minted.
- `witness_data`: When the mint type is `HolderOf(collection_id)`, then the owned
  item_id from that collection needs to be provided within the witness data object.

Note: the deposit will be taken from the `origin` and not the `owner` of the `item`.

Emits `Issued` event when successful.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| mint_to | `AccountIdLookupOf<T>` | 
| witness_data | `Option<MintWitness<T::ItemId>>` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'mint', {
    'collection': 'u32',
    'item': 'u32',
    'mint_to': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'witness_data': (
        None,
        {'owned_item': 'u32'},
    ),
}
)
```

---------
### mint_pre_signed
Mint an item by providing the pre-signed approval.

Origin must be Signed.

- `mint_data`: The pre-signed approval that consists of the information about the item,
  its metadata, attributes, who can mint it (`None` for anyone) and until what block
  number.
- `signature`: The signature of the `data` object.
- `signer`: The `data` object&\#x27;s signer. Should be an Issuer of the collection.

Emits `Issued` on success.
Emits `AttributeSet` if the attributes were provided.
Emits `ItemMetadataSet` if the metadata was not empty.
#### Attributes
| Name | Type |
| -------- | -------- | 
| mint_data | `PreSignedMintOf<T, I>` | 
| signature | `T::OffchainSignature` | 
| signer | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'mint_pre_signed', {
    'mint_data': {
        'attributes': [
            ('Bytes', 'Bytes'),
        ],
        'collection': 'u32',
        'deadline': 'u32',
        'item': 'u32',
        'metadata': 'Bytes',
        'only_account': (
            None,
            'AccountId',
        ),
    },
    'signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
    'signer': 'AccountId',
}
)
```

---------
### pay_tips
Allows to pay the tips.

Origin must be Signed.

- `tips`: Tips array.

Emits `TipSent` on every tip transfer.
#### Attributes
| Name | Type |
| -------- | -------- | 
| tips | `BoundedVec<ItemTipOf<T, I>, T::MaxTips>` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'pay_tips', {
    'tips': [
        {
            'amount': 'u128',
            'collection': 'u32',
            'item': 'u32',
            'receiver': 'AccountId',
        },
    ],
}
)
```

---------
### redeposit
Re-evaluate the deposits on some items.

Origin must be Signed and the sender should be the Owner of the `collection`.

- `collection`: The collection of the items to be reevaluated.
- `items`: The items of the collection whose deposits will be reevaluated.

NOTE: This exists as a best-effort function. Any items which are unknown or
in the case that the owner account does not have reservable funds to pay for a
deposit increase are ignored. Generally the owner isn&\#x27;t going to call this on items
whose existing deposit is less than the refreshed deposit as it would only cost them,
so it&\#x27;s of little consequence.

It will still return an error in the case that the collection is unknown or the signer
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
    'Nfts', 'redeposit', {'collection': 'u32', 'items': ['u32']}
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
    'Nfts', 'set_accept_ownership', {'maybe_collection': (None, 'u32')}
)
```

---------
### set_attribute
Set an attribute for a collection or item.

Origin must be Signed and must conform to the namespace ruleset:
- `CollectionOwner` namespace could be modified by the `collection` Admin only;
- `ItemOwner` namespace could be modified by the `maybe_item` owner only. `maybe_item`
  should be set in that case;
- `Account(AccountId)` namespace could be modified only when the `origin` was given a
  permission to do so;

The funds of `origin` are reserved according to the formula:
`AttributeDepositBase + DepositPerByte * (key.len + value.len)` taking into
account any already reserved funds.

- `collection`: The identifier of the collection whose item&\#x27;s metadata to set.
- `maybe_item`: The identifier of the item whose metadata to set.
- `namespace`: Attribute&\#x27;s namespace.
- `key`: The key of the attribute.
- `value`: The value to which to set the attribute.

Emits `AttributeSet`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| maybe_item | `Option<T::ItemId>` | 
| namespace | `AttributeNamespace<T::AccountId>` | 
| key | `BoundedVec<u8, T::KeyLimit>` | 
| value | `BoundedVec<u8, T::ValueLimit>` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'set_attribute', {
    'collection': 'u32',
    'key': 'Bytes',
    'maybe_item': (None, 'u32'),
    'namespace': {
        'Account': 'AccountId',
        'CollectionOwner': None,
        'ItemOwner': None,
        'Pallet': None,
    },
    'value': 'Bytes',
}
)
```

---------
### set_attributes_pre_signed
Set attributes for an item by providing the pre-signed approval.

Origin must be Signed and must be an owner of the `data.item`.

- `data`: The pre-signed approval that consists of the information about the item,
  attributes to update and until what block number.
- `signature`: The signature of the `data` object.
- `signer`: The `data` object&\#x27;s signer. Should be an Admin of the collection for the
  `CollectionOwner` namespace.

Emits `AttributeSet` for each provided attribute.
Emits `ItemAttributesApprovalAdded` if the approval wasn&\#x27;t set before.
Emits `PreSignedAttributesSet` on success.
#### Attributes
| Name | Type |
| -------- | -------- | 
| data | `PreSignedAttributesOf<T, I>` | 
| signature | `T::OffchainSignature` | 
| signer | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'set_attributes_pre_signed', {
    'data': {
        'attributes': [
            ('Bytes', 'Bytes'),
        ],
        'collection': 'u32',
        'deadline': 'u32',
        'item': 'u32',
        'namespace': {
            'Account': 'AccountId',
            'CollectionOwner': None,
            'ItemOwner': None,
            'Pallet': None,
        },
    },
    'signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
    'signer': 'AccountId',
}
)
```

---------
### set_collection_max_supply
Set the maximum number of items a collection could have.

Origin must be either `ForceOrigin` or `Signed` and the sender should be the Owner of
the `collection`.

- `collection`: The identifier of the collection to change.
- `max_supply`: The maximum number of items a collection could have.

Emits `CollectionMaxSupplySet` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| max_supply | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'set_collection_max_supply', {
    'collection': 'u32',
    'max_supply': 'u32',
}
)
```

---------
### set_collection_metadata
Set the metadata for a collection.

Origin must be either `ForceOrigin` or `Signed` and the sender should be the Admin of
the `collection`.

If the origin is `Signed`, then funds of signer are reserved according to the formula:
`MetadataDepositBase + DepositPerByte * data.len` taking into
account any already reserved funds.

- `collection`: The identifier of the item whose metadata to update.
- `data`: The general information of this item. Limited in length by `StringLimit`.

Emits `CollectionMetadataSet`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| data | `BoundedVec<u8, T::StringLimit>` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'set_collection_metadata', {'collection': 'u32', 'data': 'Bytes'}
)
```

---------
### set_metadata
Set the metadata for an item.

Origin must be either `ForceOrigin` or Signed and the sender should be the Admin of the
`collection`.

If the origin is Signed, then funds of signer are reserved according to the formula:
`MetadataDepositBase + DepositPerByte * data.len` taking into
account any already reserved funds.

- `collection`: The identifier of the collection whose item&\#x27;s metadata to set.
- `item`: The identifier of the item whose metadata to set.
- `data`: The general information of this item. Limited in length by `StringLimit`.

Emits `ItemMetadataSet`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| data | `BoundedVec<u8, T::StringLimit>` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'set_metadata', {
    'collection': 'u32',
    'data': 'Bytes',
    'item': 'u32',
}
)
```

---------
### set_price
Set (or reset) the price for an item.

Origin must be Signed and must be the owner of the `item`.

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
    'Nfts', 'set_price', {
    'collection': 'u32',
    'item': 'u32',
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

Origin must be either `ForceOrigin` or Signed and the sender should be the Owner of the
`collection`.

Note: by setting the role to `None` only the `ForceOrigin` will be able to change it
after to `Some(account)`.

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
| issuer | `Option<AccountIdLookupOf<T>>` | 
| admin | `Option<AccountIdLookupOf<T>>` | 
| freezer | `Option<AccountIdLookupOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'set_team', {
    'admin': (
        None,
        {
            'Address20': '[u8; 20]',
            'Address32': '[u8; 32]',
            'Id': 'AccountId',
            'Index': (),
            'Raw': 'Bytes',
        },
    ),
    'collection': 'u32',
    'freezer': (
        None,
        {
            'Address20': '[u8; 20]',
            'Address32': '[u8; 32]',
            'Id': 'AccountId',
            'Index': (),
            'Raw': 'Bytes',
        },
    ),
    'issuer': (
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
### transfer
Move an item from the sender account to another.

Origin must be Signed and the signing account must be either:
- the Owner of the `item`;
- the approved delegate for the `item` (in this case, the approval is reset).

Arguments:
- `collection`: The collection of the item to be transferred.
- `item`: The item to be transferred.
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
    'Nfts', 'transfer', {
    'collection': 'u32',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'item': 'u32',
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
    'Nfts', 'transfer_ownership', {
    'collection': 'u32',
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
### unlock_item_transfer
Re-allow unprivileged transfer of an item.

Origin must be Signed and the sender should be the Freezer of the `collection`.

- `collection`: The collection of the item to be changed.
- `item`: The item to become transferable.

Emits `ItemTransferUnlocked`.

Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'unlock_item_transfer', {'collection': 'u32', 'item': 'u32'}
)
```

---------
### update_mint_settings
Update mint settings.

Origin must be either `ForceOrigin` or `Signed` and the sender should be the Issuer
of the `collection`.

- `collection`: The identifier of the collection to change.
- `mint_settings`: The new mint settings.

Emits `CollectionMintSettingsUpdated` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| mint_settings | `MintSettings<BalanceOf<T, I>,<T as SystemConfig>::BlockNumber, T::
CollectionId,>` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'update_mint_settings', {
    'collection': 'u32',
    'mint_settings': {
        'default_item_settings': 'u64',
        'end_block': (None, 'u32'),
        'mint_type': {
            'HolderOf': 'u32',
            'Issuer': None,
            'Public': None,
        },
        'price': (None, 'u128'),
        'start_block': (None, 'u32'),
    },
}
)
```

---------
## Events

---------
### AllApprovalsCancelled
All approvals of an item got cancelled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| owner | `T::AccountId` | ```AccountId```

---------
### ApprovalCancelled
An approval for a `delegate` account to transfer the `item` of an item
`collection` was cancelled by its `owner`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| owner | `T::AccountId` | ```AccountId```
| delegate | `T::AccountId` | ```AccountId```

---------
### AttributeCleared
Attribute metadata has been cleared for a `collection` or `item`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| maybe_item | `Option<T::ItemId>` | ```(None, 'u32')```
| key | `BoundedVec<u8, T::KeyLimit>` | ```Bytes```
| namespace | `AttributeNamespace<T::AccountId>` | ```{'Pallet': None, 'CollectionOwner': None, 'ItemOwner': None, 'Account': 'AccountId'}```

---------
### AttributeSet
New attribute metadata has been set for a `collection` or `item`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| maybe_item | `Option<T::ItemId>` | ```(None, 'u32')```
| key | `BoundedVec<u8, T::KeyLimit>` | ```Bytes```
| value | `BoundedVec<u8, T::ValueLimit>` | ```Bytes```
| namespace | `AttributeNamespace<T::AccountId>` | ```{'Pallet': None, 'CollectionOwner': None, 'ItemOwner': None, 'Account': 'AccountId'}```

---------
### Burned
An `item` was destroyed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| owner | `T::AccountId` | ```AccountId```

---------
### CollectionConfigChanged
A `collection` has had its config changed by the `Force` origin.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```

---------
### CollectionLocked
Some `collection` was locked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```

---------
### CollectionMaxSupplySet
Max supply has been set for a collection.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| max_supply | `u32` | ```u32```

---------
### CollectionMetadataCleared
Metadata has been cleared for a `collection`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```

---------
### CollectionMetadataSet
New metadata has been set for a `collection`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| data | `BoundedVec<u8, T::StringLimit>` | ```Bytes```

---------
### CollectionMintSettingsUpdated
Mint settings for a collection had changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```

---------
### Created
A `collection` was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| creator | `T::AccountId` | ```AccountId```
| owner | `T::AccountId` | ```AccountId```

---------
### Destroyed
A `collection` was destroyed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```

---------
### ForceCreated
A `collection` was force-created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| owner | `T::AccountId` | ```AccountId```

---------
### Issued
An `item` was issued.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| owner | `T::AccountId` | ```AccountId```

---------
### ItemAttributesApprovalAdded
A new approval to modify item attributes was added.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| delegate | `T::AccountId` | ```AccountId```

---------
### ItemAttributesApprovalRemoved
A new approval to modify item attributes was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| delegate | `T::AccountId` | ```AccountId```

---------
### ItemBought
An item was bought.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| price | `ItemPrice<T, I>` | ```u128```
| seller | `T::AccountId` | ```AccountId```
| buyer | `T::AccountId` | ```AccountId```

---------
### ItemMetadataCleared
Metadata has been cleared for an item.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```

---------
### ItemMetadataSet
New metadata has been set for an item.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| data | `BoundedVec<u8, T::StringLimit>` | ```Bytes```

---------
### ItemPriceRemoved
The price for the item was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```

---------
### ItemPriceSet
The price was set for the item.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| price | `ItemPrice<T, I>` | ```u128```
| whitelisted_buyer | `Option<T::AccountId>` | ```(None, 'AccountId')```

---------
### ItemPropertiesLocked
`item` metadata or attributes were locked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| lock_metadata | `bool` | ```bool```
| lock_attributes | `bool` | ```bool```

---------
### ItemTransferLocked
An `item` became non-transferable.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```

---------
### ItemTransferUnlocked
An `item` became transferable.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```

---------
### NextCollectionIdIncremented
Event gets emitted when the `NextCollectionId` gets incremented.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| next_id | `T::CollectionId` | ```u32```

---------
### OwnerChanged
The owner changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| new_owner | `T::AccountId` | ```AccountId```

---------
### OwnershipAcceptanceChanged
Ownership acceptance has changed for an account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| maybe_collection | `Option<T::CollectionId>` | ```(None, 'u32')```

---------
### PalletAttributeSet
A new attribute in the `Pallet` namespace was set for the `collection` or an `item`
within that `collection`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `Option<T::ItemId>` | ```(None, 'u32')```
| attribute | `PalletAttributes<T::CollectionId>` | ```{'UsedToClaim': 'u32'}```
| value | `BoundedVec<u8, T::ValueLimit>` | ```Bytes```

---------
### PreSignedAttributesSet
New attributes have been set for an `item` of the `collection`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| namespace | `AttributeNamespace<T::AccountId>` | ```{'Pallet': None, 'CollectionOwner': None, 'ItemOwner': None, 'Account': 'AccountId'}```

---------
### Redeposited
The deposit for a set of `item`s within a `collection` has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| successful_items | `Vec<T::ItemId>` | ```['u32']```

---------
### SwapCancelled
The swap was cancelled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| offered_collection | `T::CollectionId` | ```u32```
| offered_item | `T::ItemId` | ```u32```
| desired_collection | `T::CollectionId` | ```u32```
| desired_item | `Option<T::ItemId>` | ```(None, 'u32')```
| price | `Option<PriceWithDirection<ItemPrice<T, I>>>` | ```(None, {'amount': 'u128', 'direction': ('Send', 'Receive')})```
| deadline | `<T as SystemConfig>::BlockNumber` | ```u32```

---------
### SwapClaimed
The swap has been claimed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sent_collection | `T::CollectionId` | ```u32```
| sent_item | `T::ItemId` | ```u32```
| sent_item_owner | `T::AccountId` | ```AccountId```
| received_collection | `T::CollectionId` | ```u32```
| received_item | `T::ItemId` | ```u32```
| received_item_owner | `T::AccountId` | ```AccountId```
| price | `Option<PriceWithDirection<ItemPrice<T, I>>>` | ```(None, {'amount': 'u128', 'direction': ('Send', 'Receive')})```
| deadline | `<T as SystemConfig>::BlockNumber` | ```u32```

---------
### SwapCreated
An `item` swap intent was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| offered_collection | `T::CollectionId` | ```u32```
| offered_item | `T::ItemId` | ```u32```
| desired_collection | `T::CollectionId` | ```u32```
| desired_item | `Option<T::ItemId>` | ```(None, 'u32')```
| price | `Option<PriceWithDirection<ItemPrice<T, I>>>` | ```(None, {'amount': 'u128', 'direction': ('Send', 'Receive')})```
| deadline | `<T as SystemConfig>::BlockNumber` | ```u32```

---------
### TeamChanged
The management team changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| issuer | `Option<T::AccountId>` | ```(None, 'AccountId')```
| admin | `Option<T::AccountId>` | ```(None, 'AccountId')```
| freezer | `Option<T::AccountId>` | ```(None, 'AccountId')```

---------
### TipSent
A tip was sent.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| sender | `T::AccountId` | ```AccountId```
| receiver | `T::AccountId` | ```AccountId```
| amount | `DepositBalanceOf<T, I>` | ```u128```

---------
### TransferApproved
An `item` of a `collection` has been approved by the `owner` for transfer by
a `delegate`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| owner | `T::AccountId` | ```AccountId```
| delegate | `T::AccountId` | ```AccountId```
| deadline | `Option<<T as SystemConfig>::BlockNumber>` | ```(None, 'u32')```

---------
### Transferred
An `item` was transferred.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
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
    'Nfts', 'Account', ['AccountId', 'u32', 'u32']
)
```

#### Return value
```python
()
```
---------
### Attribute
 Attributes of a collection.

#### Python
```python
result = substrate.query(
    'Nfts', 'Attribute', [
    'u32',
    (None, 'u32'),
    {
        'Account': 'AccountId',
        'CollectionOwner': None,
        'ItemOwner': None,
        'Pallet': None,
    },
    'Bytes',
]
)
```

#### Return value
```python
('Bytes', {'account': (None, 'AccountId'), 'amount': 'u128'})
```
---------
### Collection
 Details of a collection.

#### Python
```python
result = substrate.query(
    'Nfts', 'Collection', ['u32']
)
```

#### Return value
```python
{
    'attributes': 'u32',
    'item_configs': 'u32',
    'item_metadatas': 'u32',
    'items': 'u32',
    'owner': 'AccountId',
    'owner_deposit': 'u128',
}
```
---------
### CollectionAccount
 The collections owned by any given account; set out this way so that collections owned by
 a single account can be enumerated.

#### Python
```python
result = substrate.query(
    'Nfts', 'CollectionAccount', ['AccountId', 'u32']
)
```

#### Return value
```python
()
```
---------
### CollectionConfigOf
 Config of a collection.

#### Python
```python
result = substrate.query(
    'Nfts', 'CollectionConfigOf', ['u32']
)
```

#### Return value
```python
{
    'max_supply': (None, 'u32'),
    'mint_settings': {
        'default_item_settings': 'u64',
        'end_block': (None, 'u32'),
        'mint_type': {'HolderOf': 'u32', 'Issuer': None, 'Public': None},
        'price': (None, 'u128'),
        'start_block': (None, 'u32'),
    },
    'settings': 'u64',
}
```
---------
### CollectionMetadataOf
 Metadata of a collection.

#### Python
```python
result = substrate.query(
    'Nfts', 'CollectionMetadataOf', ['u32']
)
```

#### Return value
```python
{'data': 'Bytes', 'deposit': 'u128'}
```
---------
### CollectionRoleOf
 The items in existence and their ownership details.
 Stores collection roles as per account.

#### Python
```python
result = substrate.query(
    'Nfts', 'CollectionRoleOf', ['u32', 'AccountId']
)
```

#### Return value
```python
'u8'
```
---------
### Item
 The items in existence and their ownership details.

#### Python
```python
result = substrate.query(
    'Nfts', 'Item', ['u32', 'u32']
)
```

#### Return value
```python
{
    'approvals': 'scale_info::354',
    'deposit': {'account': 'AccountId', 'amount': 'u128'},
    'owner': 'AccountId',
}
```
---------
### ItemAttributesApprovalsOf
 Item attribute approvals.

#### Python
```python
result = substrate.query(
    'Nfts', 'ItemAttributesApprovalsOf', ['u32', 'u32']
)
```

#### Return value
```python
'scale_info::364'
```
---------
### ItemConfigOf
 Config of an item.

#### Python
```python
result = substrate.query(
    'Nfts', 'ItemConfigOf', ['u32', 'u32']
)
```

#### Return value
```python
{'settings': 'u64'}
```
---------
### ItemMetadataOf
 Metadata of an item.

#### Python
```python
result = substrate.query(
    'Nfts', 'ItemMetadataOf', ['u32', 'u32']
)
```

#### Return value
```python
{'data': 'Bytes', 'deposit': {'account': (None, 'AccountId'), 'amount': 'u128'}}
```
---------
### ItemPriceOf
 A price of an item.

#### Python
```python
result = substrate.query(
    'Nfts', 'ItemPriceOf', ['u32', 'u32']
)
```

#### Return value
```python
('u128', (None, 'AccountId'))
```
---------
### NextCollectionId
 Stores the `CollectionId` that is going to be used for the next collection.
 This gets incremented whenever a new collection is created.

#### Python
```python
result = substrate.query(
    'Nfts', 'NextCollectionId', []
)
```

#### Return value
```python
'u32'
```
---------
### OwnershipAcceptance
 The collection, if any, of which an account is willing to take ownership.

#### Python
```python
result = substrate.query(
    'Nfts', 'OwnershipAcceptance', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### PendingSwapOf
 Handles all the pending swaps.

#### Python
```python
result = substrate.query(
    'Nfts', 'PendingSwapOf', ['u32', 'u32']
)
```

#### Return value
```python
{
    'deadline': 'u32',
    'desired_collection': 'u32',
    'desired_item': (None, 'u32'),
    'price': (None, {'amount': 'u128', 'direction': ('Send', 'Receive')}),
}
```
---------
## Constants

---------
### ApprovalsLimit
 The maximum approvals an item could have.
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('Nfts', 'ApprovalsLimit')
```
---------
### AttributeDepositBase
 The basic amount of funds that must be reserved when adding an attribute to an item.
#### Value
```python
6666666660
```
#### Python
```python
constant = substrate.get_constant('Nfts', 'AttributeDepositBase')
```
---------
### CollectionDeposit
 The basic amount of funds that must be reserved for collection.
#### Value
```python
100000000000
```
#### Python
```python
constant = substrate.get_constant('Nfts', 'CollectionDeposit')
```
---------
### DepositPerByte
 The additional funds that must be reserved for the number of bytes store in metadata,
 either &quot;normal&quot; metadata or attribute metadata.
#### Value
```python
333333
```
#### Python
```python
constant = substrate.get_constant('Nfts', 'DepositPerByte')
```
---------
### Features
 Disables some of pallet&#x27;s features.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Nfts', 'Features')
```
---------
### ItemAttributesApprovalsLimit
 The maximum attributes approvals an item could have.
#### Value
```python
30
```
#### Python
```python
constant = substrate.get_constant('Nfts', 'ItemAttributesApprovalsLimit')
```
---------
### ItemDeposit
 The basic amount of funds that must be reserved for an item.
#### Value
```python
1000000000
```
#### Python
```python
constant = substrate.get_constant('Nfts', 'ItemDeposit')
```
---------
### KeyLimit
 The maximum length of an attribute key.
#### Value
```python
64
```
#### Python
```python
constant = substrate.get_constant('Nfts', 'KeyLimit')
```
---------
### MaxAttributesPerCall
 The max number of attributes a user could set per call.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Nfts', 'MaxAttributesPerCall')
```
---------
### MaxDeadlineDuration
 The max duration in blocks for deadlines.
#### Value
```python
2592000
```
#### Python
```python
constant = substrate.get_constant('Nfts', 'MaxDeadlineDuration')
```
---------
### MaxTips
 The max number of tips a user could send.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Nfts', 'MaxTips')
```
---------
### MetadataDepositBase
 The basic amount of funds that must be reserved when adding metadata to your item.
#### Value
```python
6709666617
```
#### Python
```python
constant = substrate.get_constant('Nfts', 'MetadataDepositBase')
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
constant = substrate.get_constant('Nfts', 'StringLimit')
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
constant = substrate.get_constant('Nfts', 'ValueLimit')
```
---------
## Errors

---------
### AlreadyClaimed
The provided Item was already used for claiming.

---------
### AlreadyExists
The item ID has already been used for an item.

---------
### ApprovalExpired
The approval had a deadline that expired, so the approval isn&\#x27;t valid anymore.

---------
### AttributeNotFound
The provided attribute can&\#x27;t be found.

---------
### BadWitness
The witness data given does not match the current state of the chain.

---------
### BidTooLow
The provided bid is too low.

---------
### CollectionIdInUse
Collection ID is already taken.

---------
### CollectionNotEmpty
Can&\#x27;t delete non-empty collections.

---------
### DeadlineExpired
The deadline has already expired.

---------
### InconsistentItemConfig
Item&\#x27;s config already exists and should be equal to the provided one.

---------
### IncorrectData
The provided data is incorrect.

---------
### IncorrectMetadata
The provided metadata might be too long.

---------
### ItemLocked
The item is locked (non-transferable).

---------
### ItemsNonTransferable
Items within that collection are non-transferable.

---------
### LockedCollectionAttributes
Collection&\#x27;s attributes are locked.

---------
### LockedCollectionMetadata
Collection&\#x27;s metadata is locked.

---------
### LockedItemAttributes
Item&\#x27;s attributes are locked.

---------
### LockedItemMetadata
Item&\#x27;s metadata is locked.

---------
### MaxAttributesLimitReached
Can&\#x27;t set more attributes per one call.

---------
### MaxSupplyLocked
The max supply is locked and can&\#x27;t be changed.

---------
### MaxSupplyReached
All items have been minted.

---------
### MaxSupplyTooSmall
The provided max supply is less than the number of items a collection already has.

---------
### MetadataNotFound
The given item has no metadata set.

---------
### MethodDisabled
The method is disabled by system settings.

---------
### MintEnded
Mint has already ended.

---------
### MintNotStarted
Mint has not started yet.

---------
### NoConfig
Config for a collection or an item can&\#x27;t be found.

---------
### NoPermission
The signing account has no permission to do the operation.

---------
### NotDelegate
The provided account is not a delegate.

---------
### NotForSale
Item is not for sale.

---------
### ReachedApprovalLimit
The item has reached its approval limit.

---------
### RolesNotCleared
Some roles were not cleared.

---------
### Unaccepted
The named owner has not signed ownership acceptance of the collection.

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
### UnknownSwap
Swap doesn&\#x27;t exist.

---------
### WrongDelegate
The delegate turned out to be different to what was expected.

---------
### WrongDuration
The duration provided should be less than or equal to `MaxDeadlineDuration`.

---------
### WrongNamespace
The provided namespace isn&\#x27;t supported in this call.

---------
### WrongOrigin
The extrinsic was sent by the wrong origin.

---------
### WrongOwner
The owner turned out to be different to what was expected.

---------
### WrongSetting
The provided setting can&\#x27;t be set.

---------
### WrongSignature
The provided signature is incorrect.

---------