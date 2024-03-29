
# Uniques

---------
## Calls

---------
### approve_transfer
See [`Pallet::approve_transfer`].
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
### burn
See [`Pallet::burn`].
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
    'collection': 'u32',
    'item': 'u32',
}
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
    'Uniques', 'buy_item', {
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
| maybe_check_delegate | `Option<AccountIdLookupOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'cancel_approval', {
    'collection': 'u32',
    'item': 'u32',
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
See [`Pallet::clear_attribute`].
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
    'collection': 'u32',
    'key': 'Bytes',
    'maybe_item': (None, 'u32'),
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
    'Uniques', 'clear_collection_metadata', {'collection': 'u32'}
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
    'Uniques', 'clear_metadata', {'collection': 'u32', 'item': 'u32'}
)
```

---------
### create
See [`Pallet::create`].
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
    'collection': 'u32',
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
    'Uniques', 'destroy', {
    'collection': 'u32',
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
See [`Pallet::force_create`].
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
    'collection': 'u32',
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
See [`Pallet::force_item_status`].
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
    'collection': 'u32',
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
See [`Pallet::freeze`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'freeze', {'collection': 'u32', 'item': 'u32'}
)
```

---------
### freeze_collection
See [`Pallet::freeze_collection`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'freeze_collection', {'collection': 'u32'}
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
| owner | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'mint', {
    'collection': 'u32',
    'item': 'u32',
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
See [`Pallet::redeposit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| items | `Vec<T::ItemId>` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'redeposit', {'collection': 'u32', 'items': ['u32']}
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
    'Uniques', 'set_accept_ownership', {'maybe_collection': (None, 'u32')}
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
| key | `BoundedVec<u8, T::KeyLimit>` | 
| value | `BoundedVec<u8, T::ValueLimit>` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'set_attribute', {
    'collection': 'u32',
    'key': 'Bytes',
    'maybe_item': (None, 'u32'),
    'value': 'Bytes',
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
    'Uniques', 'set_collection_max_supply', {
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
| is_frozen | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'set_collection_metadata', {
    'collection': 'u32',
    'data': 'Bytes',
    'is_frozen': 'bool',
}
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
| is_frozen | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'set_metadata', {
    'collection': 'u32',
    'data': 'Bytes',
    'is_frozen': 'bool',
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
    'Uniques', 'set_price', {
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
    'collection': 'u32',
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
See [`Pallet::thaw`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 
| item | `T::ItemId` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'thaw', {'collection': 'u32', 'item': 'u32'}
)
```

---------
### thaw_collection
See [`Pallet::thaw_collection`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection | `T::CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'Uniques', 'thaw_collection', {'collection': 'u32'}
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
    'Uniques', 'transfer', {
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
    'Uniques', 'transfer_ownership', {
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
## Events

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
### ApprovedTransfer
An `item` of a `collection` has been approved by the `owner` for transfer by
a `delegate`.
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
### CollectionFrozen
Some `collection` was frozen.
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
| is_frozen | `bool` | ```bool```

---------
### CollectionThawed
Some `collection` was thawed.
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
### Frozen
Some `item` was frozen.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```

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
### ItemPriceRemoved
The price for the instance was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```

---------
### ItemPriceSet
The price was set for the instance.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| price | `ItemPrice<T, I>` | ```u128```
| whitelisted_buyer | `Option<T::AccountId>` | ```(None, 'AccountId')```

---------
### ItemStatusChanged
A `collection` has had its attributes changed by the `Force` origin.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```

---------
### MetadataCleared
Metadata has been cleared for an item.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```

---------
### MetadataSet
New metadata has been set for an item.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```
| data | `BoundedVec<u8, T::StringLimit>` | ```Bytes```
| is_frozen | `bool` | ```bool```

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
### Redeposited
Metadata has been cleared for an item.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| successful_items | `Vec<T::ItemId>` | ```['u32']```

---------
### TeamChanged
The management team changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| issuer | `T::AccountId` | ```AccountId```
| admin | `T::AccountId` | ```AccountId```
| freezer | `T::AccountId` | ```AccountId```

---------
### Thawed
Some `item` was thawed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection | `T::CollectionId` | ```u32```
| item | `T::ItemId` | ```u32```

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
    'Uniques', 'Account', ['AccountId', 'u32', 'u32']
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
    'Uniques', 'Asset', ['u32', 'u32']
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
    'Uniques', 'Attribute', ['u32', (None, 'u32'), 'Bytes']
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
    'Uniques', 'Class', ['u32']
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
    'Uniques', 'ClassAccount', ['AccountId', 'u32']
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
    'Uniques', 'ClassMetadataOf', ['u32']
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
    'Uniques', 'CollectionMaxSupply', ['u32']
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
    'Uniques', 'InstanceMetadataOf', ['u32', 'u32']
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
    'Uniques', 'ItemPriceOf', ['u32', 'u32']
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
'u32'
```
---------
## Constants

---------
### AttributeDepositBase
 The basic amount of funds that must be reserved when adding an attribute to an item.
#### Value
```python
0
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
0
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
0
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
0
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
32
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
0
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
50
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