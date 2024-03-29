
# Nfts

---------
## Calls

---------
### approve_item_attributes
See [`Pallet::approve_item_attributes`].
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
See [`Pallet::approve_transfer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| delegate | `AccountIdLookupOf<T>` | 
| maybe_deadline | `Option<BlockNumberFor<T>>` | 

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
See [`Pallet::burn`].
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
See [`Pallet::buy_item`].
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
See [`Pallet::cancel_approval`].
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
See [`Pallet::cancel_item_attributes_approval`].
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
See [`Pallet::cancel_swap`].
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
See [`Pallet::claim_swap`].
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
See [`Pallet::clear_all_transfer_approvals`].
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
See [`Pallet::clear_attribute`].
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
See [`Pallet::clear_collection_metadata`].
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
See [`Pallet::clear_metadata`].
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
See [`Pallet::create`].
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
See [`Pallet::create_swap`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| offered_collection | `T::CollectionId` | 
| offered_item | `T::ItemId` | 
| desired_collection | `T::CollectionId` | 
| maybe_desired_item | `Option<T::ItemId>` | 
| maybe_price | `Option<PriceWithDirection<ItemPrice<T, I>>>` | 
| duration | `BlockNumberFor<T>` | 

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
See [`Pallet::destroy`].
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
See [`Pallet::force_collection_config`].
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
See [`Pallet::force_collection_owner`].
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
See [`Pallet::force_create`].
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
See [`Pallet::force_mint`].
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
See [`Pallet::force_set_attribute`].
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
See [`Pallet::lock_collection`].
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
See [`Pallet::lock_item_properties`].
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
See [`Pallet::lock_item_transfer`].
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
See [`Pallet::mint`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 
| mint_to | `AccountIdLookupOf<T>` | 
| witness_data | `Option<MintWitness<T::ItemId, DepositBalanceOf<T, I>>>` | 

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
        {
            'mint_price': (
                None,
                'u128',
            ),
            'owned_item': (
                None,
                'u32',
            ),
        },
    ),
}
)
```

---------
### mint_pre_signed
See [`Pallet::mint_pre_signed`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| mint_data | `Box<PreSignedMintOf<T, I>>` | 
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
        'mint_price': (None, 'u128'),
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
See [`Pallet::pay_tips`].
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
See [`Pallet::redeposit`].
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
See [`Pallet::set_accept_ownership`].
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
See [`Pallet::set_attribute`].
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
See [`Pallet::set_attributes_pre_signed`].
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
See [`Pallet::set_collection_max_supply`].
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
See [`Pallet::set_collection_metadata`].
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
See [`Pallet::set_metadata`].
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
See [`Pallet::set_price`].
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
See [`Pallet::set_team`].
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
See [`Pallet::transfer`].
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
See [`Pallet::transfer_ownership`].
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
See [`Pallet::unlock_item_transfer`].
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
See [`Pallet::update_mint_settings`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| mint_settings | `MintSettings<BalanceOf<T, I>, BlockNumberFor<T>, T::CollectionId>` | 

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
| next_id | `Option<T::CollectionId>` | ```(None, 'u32')```

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
| attribute | `PalletAttributes<T::CollectionId>` | ```{'UsedToClaim': 'u32', 'TransferDisabled': None}```
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
| deadline | `BlockNumberFor<T>` | ```u32```

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
| deadline | `BlockNumberFor<T>` | ```u32```

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
| deadline | `BlockNumberFor<T>` | ```u32```

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
| deadline | `Option<BlockNumberFor<T>>` | ```(None, 'u32')```

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
    'approvals': 'scale_info::388',
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
'scale_info::398'
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
### WitnessRequired
The witness data should be provided.

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