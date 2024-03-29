
# RmrkCore

---------
## Calls

---------
### accept_nft
See [`Pallet::accept_nft`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| nft_id | `ItemIdOf<T>` | 
| new_owner | `AccountIdOrCollectionNftTuple<T::AccountId, CollectionIdOf<T>, ItemIdOf
<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'accept_nft', {
    'collection_id': 'u32',
    'new_owner': {
        'AccountId': 'AccountId',
        'CollectionAndNftTuple': (
            'u32',
            'u32',
        ),
    },
    'nft_id': 'u32',
}
)
```

---------
### accept_resource
See [`Pallet::accept_resource`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| nft_id | `ItemIdOf<T>` | 
| resource_id | `ResourceId` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'accept_resource', {
    'collection_id': 'u32',
    'nft_id': 'u32',
    'resource_id': 'u32',
}
)
```

---------
### accept_resource_removal
See [`Pallet::accept_resource_removal`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| nft_id | `ItemIdOf<T>` | 
| resource_id | `ResourceId` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'accept_resource_removal', {
    'collection_id': 'u32',
    'nft_id': 'u32',
    'resource_id': 'u32',
}
)
```

---------
### add_basic_resource
See [`Pallet::add_basic_resource`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| nft_id | `ItemIdOf<T>` | 
| resource | `BasicResource<StringLimitOf<T>>` | 
| resource_id | `ResourceId` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'add_basic_resource', {
    'collection_id': 'u32',
    'nft_id': 'u32',
    'resource': {'metadata': 'Bytes'},
    'resource_id': 'u32',
}
)
```

---------
### add_composable_resource
See [`Pallet::add_composable_resource`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| nft_id | `ItemIdOf<T>` | 
| resource | `ComposableResource<StringLimitOf<T>, BoundedVec<PartId, T::PartsLimit
>>` | 
| resource_id | `ResourceId` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'add_composable_resource', {
    'collection_id': 'u32',
    'nft_id': 'u32',
    'resource': {
        'base': 'u32',
        'metadata': (None, 'Bytes'),
        'parts': ['u32'],
        'slot': (None, ('u32', 'u32')),
    },
    'resource_id': 'u32',
}
)
```

---------
### add_slot_resource
See [`Pallet::add_slot_resource`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| nft_id | `ItemIdOf<T>` | 
| resource | `SlotResource<StringLimitOf<T>>` | 
| resource_id | `ResourceId` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'add_slot_resource', {
    'collection_id': 'u32',
    'nft_id': 'u32',
    'resource': {
        'base': 'u32',
        'metadata': (None, 'Bytes'),
        'slot': 'u32',
    },
    'resource_id': 'u32',
}
)
```

---------
### burn_nft
See [`Pallet::burn_nft`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| nft_id | `ItemIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'burn_nft', {
    'collection_id': 'u32',
    'nft_id': 'u32',
}
)
```

---------
### change_collection_issuer
See [`Pallet::change_collection_issuer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| new_issuer | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'change_collection_issuer', {
    'collection_id': 'u32',
    'new_issuer': {
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
### create_collection
See [`Pallet::create_collection`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| metadata | `BoundedVec<u8, T::StringLimit>` | 
| max | `Option<u32>` | 
| symbol | `BoundedCollectionSymbolOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'create_collection', {
    'collection_id': 'u32',
    'max': (None, 'u32'),
    'metadata': 'Bytes',
    'symbol': 'Bytes',
}
)
```

---------
### destroy_collection
See [`Pallet::destroy_collection`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'destroy_collection', {'collection_id': 'u32'}
)
```

---------
### lock_collection
See [`Pallet::lock_collection`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'lock_collection', {'collection_id': 'u32'}
)
```

---------
### mint_nft
See [`Pallet::mint_nft`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner | `Option<T::AccountId>` | 
| nft_id | `ItemIdOf<T>` | 
| collection_id | `CollectionIdOf<T>` | 
| royalty_recipient | `Option<T::AccountId>` | 
| royalty | `Option<Permill>` | 
| metadata | `BoundedVec<u8, T::StringLimit>` | 
| transferable | `bool` | 
| resources | `Option<BoundedResourceInfoTypeOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'mint_nft', {
    'collection_id': 'u32',
    'metadata': 'Bytes',
    'nft_id': 'u32',
    'owner': (None, 'AccountId'),
    'resources': (
        None,
        [
            {
                'id': 'u32',
                'resource': {
                    'Basic': {
                        'metadata': 'Bytes',
                    },
                    'Composable': {
                        'base': 'u32',
                        'metadata': (
                            None,
                            'Bytes',
                        ),
                        'parts': [
                            'u32',
                        ],
                        'slot': (
                            None,
                            (
                                'u32',
                                'u32',
                            ),
                        ),
                    },
                    'Slot': {
                        'base': 'u32',
                        'metadata': (
                            None,
                            'Bytes',
                        ),
                        'slot': 'u32',
                    },
                },
            },
        ],
    ),
    'royalty': (None, 'u32'),
    'royalty_recipient': (
        None,
        'AccountId',
    ),
    'transferable': 'bool',
}
)
```

---------
### mint_nft_directly_to_nft
See [`Pallet::mint_nft_directly_to_nft`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner | `(CollectionIdOf<T>, ItemIdOf<T>)` | 
| nft_id | `ItemIdOf<T>` | 
| collection_id | `CollectionIdOf<T>` | 
| royalty_recipient | `Option<T::AccountId>` | 
| royalty | `Option<Permill>` | 
| metadata | `BoundedVec<u8, T::StringLimit>` | 
| transferable | `bool` | 
| resources | `Option<BoundedResourceInfoTypeOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'mint_nft_directly_to_nft', {
    'collection_id': 'u32',
    'metadata': 'Bytes',
    'nft_id': 'u32',
    'owner': ('u32', 'u32'),
    'resources': (
        None,
        [
            {
                'id': 'u32',
                'resource': {
                    'Basic': {
                        'metadata': 'Bytes',
                    },
                    'Composable': {
                        'base': 'u32',
                        'metadata': (
                            None,
                            'Bytes',
                        ),
                        'parts': [
                            'u32',
                        ],
                        'slot': (
                            None,
                            (
                                'u32',
                                'u32',
                            ),
                        ),
                    },
                    'Slot': {
                        'base': 'u32',
                        'metadata': (
                            None,
                            'Bytes',
                        ),
                        'slot': 'u32',
                    },
                },
            },
        ],
    ),
    'royalty': (None, 'u32'),
    'royalty_recipient': (
        None,
        'AccountId',
    ),
    'transferable': 'bool',
}
)
```

---------
### reject_nft
See [`Pallet::reject_nft`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| nft_id | `ItemIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'reject_nft', {
    'collection_id': 'u32',
    'nft_id': 'u32',
}
)
```

---------
### remove_resource
See [`Pallet::remove_resource`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| nft_id | `ItemIdOf<T>` | 
| resource_id | `ResourceId` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'remove_resource', {
    'collection_id': 'u32',
    'nft_id': 'u32',
    'resource_id': 'u32',
}
)
```

---------
### replace_resource
See [`Pallet::replace_resource`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| nft_id | `ItemIdOf<T>` | 
| resource | `ResourceTypes<StringLimitOf<T>, BoundedVec<PartId, T::PartsLimit>>` | 
| resource_id | `ResourceId` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'replace_resource', {
    'collection_id': 'u32',
    'nft_id': 'u32',
    'resource': {
        'Basic': {'metadata': 'Bytes'},
        'Composable': {
            'base': 'u32',
            'metadata': (
                None,
                'Bytes',
            ),
            'parts': ['u32'],
            'slot': (
                None,
                ('u32', 'u32'),
            ),
        },
        'Slot': {
            'base': 'u32',
            'metadata': (
                None,
                'Bytes',
            ),
            'slot': 'u32',
        },
    },
    'resource_id': 'u32',
}
)
```

---------
### send
See [`Pallet::send`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| nft_id | `ItemIdOf<T>` | 
| new_owner | `AccountIdOrCollectionNftTuple<T::AccountId, CollectionIdOf<T>, ItemIdOf
<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'send', {
    'collection_id': 'u32',
    'new_owner': {
        'AccountId': 'AccountId',
        'CollectionAndNftTuple': (
            'u32',
            'u32',
        ),
    },
    'nft_id': 'u32',
}
)
```

---------
### set_priority
See [`Pallet::set_priority`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| nft_id | `ItemIdOf<T>` | 
| priorities | `BoundedVec<ResourceId, T::MaxPriorities>` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'set_priority', {
    'collection_id': 'u32',
    'nft_id': 'u32',
    'priorities': ['u32'],
}
)
```

---------
### set_property
See [`Pallet::set_property`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionIdOf<T>` | 
| maybe_nft_id | `Option<ItemIdOf<T>>` | 
| key | `KeyLimitOf<T>` | 
| value | `ValueLimitOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkCore', 'set_property', {
    'collection_id': 'u32',
    'key': 'Bytes',
    'maybe_nft_id': (None, 'u32'),
    'value': 'Bytes',
}
)
```

---------
## Events

---------
### CollectionCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| issuer | `T::AccountId` | ```AccountId```
| collection_id | `CollectionIdOf<T>` | ```u32```

---------
### CollectionDestroyed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| issuer | `T::AccountId` | ```AccountId```
| collection_id | `CollectionIdOf<T>` | ```u32```

---------
### CollectionLocked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| issuer | `T::AccountId` | ```AccountId```
| collection_id | `CollectionIdOf<T>` | ```u32```

---------
### IssuerChanged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_issuer | `T::AccountId` | ```AccountId```
| new_issuer | `T::AccountId` | ```AccountId```
| collection_id | `CollectionIdOf<T>` | ```u32```

---------
### NFTAccepted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| recipient | `AccountIdOrCollectionNftTuple<T::AccountId, CollectionIdOf<T>, ItemIdOf
<T>>` | ```{'AccountId': 'AccountId', 'CollectionAndNftTuple': ('u32', 'u32')}```
| collection_id | `CollectionIdOf<T>` | ```u32```
| nft_id | `ItemIdOf<T>` | ```u32```

---------
### NFTBurned
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| collection_id | `CollectionIdOf<T>` | ```u32```
| nft_id | `ItemIdOf<T>` | ```u32```

---------
### NFTRejected
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| collection_id | `CollectionIdOf<T>` | ```u32```
| nft_id | `ItemIdOf<T>` | ```u32```

---------
### NFTSent
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| recipient | `AccountIdOrCollectionNftTuple<T::AccountId, CollectionIdOf<T>, ItemIdOf
<T>>` | ```{'AccountId': 'AccountId', 'CollectionAndNftTuple': ('u32', 'u32')}```
| collection_id | `CollectionIdOf<T>` | ```u32```
| nft_id | `ItemIdOf<T>` | ```u32```
| approval_required | `bool` | ```bool```

---------
### NftMinted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `AccountIdOrCollectionNftTuple<T::AccountId, CollectionIdOf<T>, ItemIdOf
<T>>` | ```{'AccountId': 'AccountId', 'CollectionAndNftTuple': ('u32', 'u32')}```
| collection_id | `CollectionIdOf<T>` | ```u32```
| nft_id | `ItemIdOf<T>` | ```u32```

---------
### PrioritySet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `CollectionIdOf<T>` | ```u32```
| nft_id | `ItemIdOf<T>` | ```u32```

---------
### PropertiesRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `CollectionIdOf<T>` | ```u32```
| maybe_nft_id | `Option<ItemIdOf<T>>` | ```(None, 'u32')```

---------
### PropertyRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `CollectionIdOf<T>` | ```u32```
| maybe_nft_id | `Option<ItemIdOf<T>>` | ```(None, 'u32')```
| key | `KeyLimitOf<T>` | ```Bytes```

---------
### PropertySet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `CollectionIdOf<T>` | ```u32```
| maybe_nft_id | `Option<ItemIdOf<T>>` | ```(None, 'u32')```
| key | `KeyLimitOf<T>` | ```Bytes```
| value | `ValueLimitOf<T>` | ```Bytes```

---------
### ResourceAccepted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| nft_id | `ItemIdOf<T>` | ```u32```
| resource_id | `ResourceId` | ```u32```
| collection_id | `CollectionIdOf<T>` | ```u32```

---------
### ResourceAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| nft_id | `ItemIdOf<T>` | ```u32```
| resource_id | `ResourceId` | ```u32```
| collection_id | `CollectionIdOf<T>` | ```u32```

---------
### ResourceRemoval
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| nft_id | `ItemIdOf<T>` | ```u32```
| resource_id | `ResourceId` | ```u32```
| collection_id | `CollectionIdOf<T>` | ```u32```

---------
### ResourceRemovalAccepted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| nft_id | `ItemIdOf<T>` | ```u32```
| resource_id | `ResourceId` | ```u32```
| collection_id | `CollectionIdOf<T>` | ```u32```

---------
### ResourceReplaced
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| nft_id | `ItemIdOf<T>` | ```u32```
| resource_id | `ResourceId` | ```u32```
| collection_id | `CollectionIdOf<T>` | ```u32```

---------
## Storage functions

---------
### Children
 Stores nft children info

#### Python
```python
result = substrate.query(
    'RmrkCore', 'Children', [('u32', 'u32'), ('u32', 'u32')]
)
```

#### Return value
```python
()
```
---------
### Collections
 Stores collections info

#### Python
```python
result = substrate.query(
    'RmrkCore', 'Collections', ['u32']
)
```

#### Return value
```python
{
    'issuer': 'AccountId',
    'max': (None, 'u32'),
    'metadata': 'Bytes',
    'nfts_count': 'u32',
    'symbol': 'Bytes',
}
```
---------
### DummyStorage
 This storage is not used by the chain.
 It is need only for PolkadotJS types generation.

 The stored types are use in the RPC interface only,
 PolkadotJS won&#x27;t generate TS types for them without this storage.

#### Python
```python
result = substrate.query(
    'RmrkCore', 'DummyStorage', []
)
```

#### Return value
```python
({'collection_id': 'u32', 'nft_id': 'u32'}, "[{'key': 'Bytes', 'value': 'Bytes'}; 0]")
```
---------
### EquippableBases
 Stores the existence of a base for a particular NFT
 This is populated on `add_composable_resource`, and is
 used in the rmrk-equip pallet when equipping a resource.

#### Python
```python
result = substrate.query(
    'RmrkCore', 'EquippableBases', ['u32', 'u32', 'u32']
)
```

#### Return value
```python
()
```
---------
### EquippableSlots
 Stores the existence of a Base + Slot for a particular
 NFT&#x27;s particular resource.  This is populated on
 `add_slot_resource`, and is used in the rmrk-equip
 pallet when equipping a resource.

#### Python
```python
result = substrate.query(
    'RmrkCore', 'EquippableSlots', ['u32', 'u32', 'u32', 'u32', 'u32']
)
```

#### Return value
```python
()
```
---------
### Lock
 Lock for NFTs

#### Python
```python
result = substrate.query(
    'RmrkCore', 'Lock', [('u32', 'u32')]
)
```

#### Return value
```python
'bool'
```
---------
### Nfts
 Stores nft info

#### Python
```python
result = substrate.query(
    'RmrkCore', 'Nfts', ['u32', 'u32']
)
```

#### Return value
```python
{
    'equipped': (None, ('u32', 'u32')),
    'metadata': 'Bytes',
    'owner': {
        'AccountId': 'AccountId',
        'CollectionAndNftTuple': ('u32', 'u32'),
    },
    'pending': 'bool',
    'royalty': (None, {'amount': 'u32', 'recipient': 'AccountId'}),
    'transferable': 'bool',
}
```
---------
### Priorities
 Stores priority info

#### Python
```python
result = substrate.query(
    'RmrkCore', 'Priorities', ['u32', 'u32', 'u32']
)
```

#### Return value
```python
'u32'
```
---------
### Properties
 Arbitrary properties / metadata of an asset.

#### Python
```python
result = substrate.query(
    'RmrkCore', 'Properties', ['u32', (None, 'u32'), 'Bytes']
)
```

#### Return value
```python
'Bytes'
```
---------
### Resources
 Stores resource info

#### Python
```python
result = substrate.query(
    'RmrkCore', 'Resources', ['u32', 'u32', 'u32']
)
```

#### Return value
```python
{
    'id': 'u32',
    'pending': 'bool',
    'pending_removal': 'bool',
    'resource': {
        'Basic': {'metadata': 'Bytes'},
        'Composable': {
            'base': 'u32',
            'metadata': (None, 'Bytes'),
            'parts': ['u32'],
            'slot': (None, ('u32', 'u32')),
        },
        'Slot': {'base': 'u32', 'metadata': (None, 'Bytes'), 'slot': 'u32'},
    },
}
```
---------
## Constants

---------
### MaxPriorities
 The maximum number of resources that can be included in a setpriority extrinsic
#### Value
```python
25
```
#### Python
```python
constant = substrate.get_constant('RmrkCore', 'MaxPriorities')
```
---------
### NestingBudget
 The maximum nesting allowed in the pallet extrinsics.
#### Value
```python
200
```
#### Python
```python
constant = substrate.get_constant('RmrkCore', 'NestingBudget')
```
---------
### PartsLimit
 The maximum number of parts each resource may have
#### Value
```python
25
```
#### Python
```python
constant = substrate.get_constant('RmrkCore', 'PartsLimit')
```
---------
### PropertiesLimit
 The maximum number of properties each can have
#### Value
```python
15
```
#### Python
```python
constant = substrate.get_constant('RmrkCore', 'PropertiesLimit')
```
---------
### ResourceSymbolLimit
 The maximum resource symbol length
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('RmrkCore', 'ResourceSymbolLimit')
```
---------
## Errors

---------
### CannotAcceptNonOwnedNft

---------
### CannotAcceptToNewOwner

---------
### CannotRejectNonOwnedNft

---------
### CannotRejectNonPendingNft

---------
### CannotSendEquippedItem

---------
### CannotSendToDescendentOrSelf

---------
### CollectionFullOrLocked

---------
### CollectionNotEmpty

---------
### CollectionUnknown

---------
### EmptyResource

---------
### FailedTransferHooksPostTransfer

---------
### FailedTransferHooksPreCheck

---------
### MetadataNotSet

---------
### NftAlreadyExists

---------
### NftIsLocked

---------
### NoAvailableCollectionId

---------
### NoAvailableNftId

---------
### NoAvailableResourceId

---------
### NoPermission

---------
### NoWitness

---------
### NonTransferable

---------
### NoneValue
Error names should be descriptive.

---------
### NotInRange

---------
### RecipientNotSet

---------
### ResourceAlreadyExists

---------
### ResourceDoesntExist

---------
### ResourceNotPending
Accepting a resource that is not pending should fail

---------
### RoyaltyNotSet

---------
### StorageOverflow
Errors should have helpful documentation associated with them.

---------
### TooLong

---------
### TooManyRecursions
The recursion limit has been reached.

---------