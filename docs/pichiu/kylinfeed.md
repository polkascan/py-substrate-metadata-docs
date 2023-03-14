
# KylinFeed

---------
## Calls

---------
### accept_nft
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 
| new_owner | `AccountIdOrCollectionNftTuple<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinFeed', 'accept_nft', {
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
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 
| resource_id | `ResourceId` | 

#### Python
```python
call = substrate.compose_call(
    'KylinFeed', 'accept_resource', {
    'collection_id': 'u32',
    'nft_id': 'u32',
    'resource_id': 'u32',
}
)
```

---------
### accept_resource_removal
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 
| resource_id | `ResourceId` | 

#### Python
```python
call = substrate.compose_call(
    'KylinFeed', 'accept_resource_removal', {
    'collection_id': 'u32',
    'nft_id': 'u32',
    'resource_id': 'u32',
}
)
```

---------
### add_basic_resource
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 
| resource | `BasicResource<StringLimitOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinFeed', 'add_basic_resource', {
    'collection_id': 'u32',
    'nft_id': 'u32',
    'resource': {
        'license': (None, 'Bytes'),
        'metadata': (None, 'Bytes'),
        'src': (None, 'Bytes'),
        'thumb': (None, 'Bytes'),
    },
}
)
```

---------
### burn_nft
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 

#### Python
```python
call = substrate.compose_call(
    'KylinFeed', 'burn_nft', {
    'collection_id': 'u32',
    'nft_id': 'u32',
}
)
```

---------
### change_collection_issuer
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| new_issuer | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'KylinFeed', 'change_collection_issuer', {
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
#### Attributes
| Name | Type |
| -------- | -------- | 
| metadata | `BoundedVec<u8, T::StringLimit>` | 
| max | `Option<u32>` | 
| symbol | `BoundedCollectionSymbolOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinFeed', 'create_collection', {
    'max': (None, 'u32'),
    'metadata': 'Bytes',
    'symbol': 'Bytes',
}
)
```

---------
### destroy_collection
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'KylinFeed', 'destroy_collection', {'collection_id': 'u32'}
)
```

---------
### lock_collection
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'KylinFeed', 'lock_collection', {'collection_id': 'u32'}
)
```

---------
### mint_nft
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner | `Option<T::AccountId>` | 
| collection_id | `CollectionId` | 
| metadata | `BoundedVec<u8, T::StringLimit>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinFeed', 'mint_nft', {
    'collection_id': 'u32',
    'metadata': 'Bytes',
    'owner': (None, 'AccountId'),
}
)
```

---------
### reject_nft
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 

#### Python
```python
call = substrate.compose_call(
    'KylinFeed', 'reject_nft', {
    'collection_id': 'u32',
    'nft_id': 'u32',
}
)
```

---------
### remove_resource
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 
| resource_id | `ResourceId` | 

#### Python
```python
call = substrate.compose_call(
    'KylinFeed', 'remove_resource', {
    'collection_id': 'u32',
    'nft_id': 'u32',
    'resource_id': 'u32',
}
)
```

---------
### send
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 
| new_owner | `AccountIdOrCollectionNftTuple<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinFeed', 'send', {
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
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| nft_id | `NftId` | 
| priorities | `BoundedVec<ResourceId, T::MaxPriorities>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinFeed', 'set_priority', {
    'collection_id': 'u32',
    'nft_id': 'u32',
    'priorities': ['u32'],
}
)
```

---------
### set_property
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| maybe_nft_id | `Option<NftId>` | 
| key | `KeyLimitOf<T>` | 
| value | `ValueLimitOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'KylinFeed', 'set_property', {
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
| collection_id | `CollectionId` | ```u32```

---------
### CollectionDestroyed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| issuer | `T::AccountId` | ```AccountId```
| collection_id | `CollectionId` | ```u32```

---------
### CollectionLocked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| issuer | `T::AccountId` | ```AccountId```
| collection_id | `CollectionId` | ```u32```

---------
### IssuerChanged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_issuer | `T::AccountId` | ```AccountId```
| new_issuer | `T::AccountId` | ```AccountId```
| collection_id | `CollectionId` | ```u32```

---------
### NFTAccepted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| recipient | `AccountIdOrCollectionNftTuple<T::AccountId>` | ```{'AccountId': 'AccountId', 'CollectionAndNftTuple': ('u32', 'u32')}```
| collection_id | `CollectionId` | ```u32```
| nft_id | `NftId` | ```u32```

---------
### NFTBurned
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| nft_id | `NftId` | ```u32```

---------
### NFTRejected
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| collection_id | `CollectionId` | ```u32```
| nft_id | `NftId` | ```u32```

---------
### NFTSent
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| recipient | `AccountIdOrCollectionNftTuple<T::AccountId>` | ```{'AccountId': 'AccountId', 'CollectionAndNftTuple': ('u32', 'u32')}```
| collection_id | `CollectionId` | ```u32```
| nft_id | `NftId` | ```u32```
| approval_required | `bool` | ```bool```

---------
### NftMinted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| collection_id | `CollectionId` | ```u32```
| nft_id | `NftId` | ```u32```

---------
### PrioritySet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `CollectionId` | ```u32```
| nft_id | `NftId` | ```u32```

---------
### PropertySet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `CollectionId` | ```u32```
| maybe_nft_id | `Option<NftId>` | ```(None, 'u32')```
| key | `KeyLimitOf<T>` | ```Bytes```
| value | `ValueLimitOf<T>` | ```Bytes```

---------
### ResourceAccepted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| nft_id | `NftId` | ```u32```
| resource_id | `ResourceId` | ```u32```

---------
### ResourceAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| nft_id | `NftId` | ```u32```
| resource_id | `ResourceId` | ```u32```

---------
### ResourceRemoval
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| nft_id | `NftId` | ```u32```
| resource_id | `ResourceId` | ```u32```

---------
### ResourceRemovalAccepted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| nft_id | `NftId` | ```u32```
| resource_id | `ResourceId` | ```u32```

---------
## Storage functions

---------
### Children

#### Python
```python
result = substrate.query(
    'KylinFeed', 'Children', [('u32', 'u32'), ('u32', 'u32')]
)
```

#### Return value
```python
()
```
---------
### CollectionIndex

#### Python
```python
result = substrate.query(
    'KylinFeed', 'CollectionIndex', []
)
```

#### Return value
```python
'u32'
```
---------
### Collections

#### Python
```python
result = substrate.query(
    'KylinFeed', 'Collections', ['u32']
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
### Lock

#### Python
```python
result = substrate.query(
    'KylinFeed', 'Lock', [('u32', 'u32')]
)
```

#### Return value
```python
'bool'
```
---------
### NextNftId

#### Python
```python
result = substrate.query(
    'KylinFeed', 'NextNftId', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### NextResourceId

#### Python
```python
result = substrate.query(
    'KylinFeed', 'NextResourceId', ['u32', 'u32']
)
```

#### Return value
```python
'u32'
```
---------
### Nfts

#### Python
```python
result = substrate.query(
    'KylinFeed', 'Nfts', ['u32', 'u32']
)
```

#### Return value
```python
{
    'metadata': 'Bytes',
    'owner': {
        'AccountId': 'AccountId',
        'CollectionAndNftTuple': ('u32', 'u32'),
    },
    'pending': 'bool',
    'transferable': 'bool',
}
```
---------
### Priorities

#### Python
```python
result = substrate.query(
    'KylinFeed', 'Priorities', ['u32', 'u32', 'u32']
)
```

#### Return value
```python
'u32'
```
---------
### Properties

#### Python
```python
result = substrate.query(
    'KylinFeed', 'Properties', ['u32', (None, 'u32'), 'Bytes']
)
```

#### Return value
```python
'Bytes'
```
---------
### Resources

#### Python
```python
result = substrate.query(
    'KylinFeed', 'Resources', ['u32', 'u32', 'u32']
)
```

#### Return value
```python
{
    'id': 'u32',
    'pending': 'bool',
    'pending_removal': 'bool',
    'resource': {
        'Basic': {
            'license': (None, 'Bytes'),
            'metadata': (None, 'Bytes'),
            'src': (None, 'Bytes'),
            'thumb': (None, 'Bytes'),
        },
        'Composable': {
            'base': 'u32',
            'license': (None, 'Bytes'),
            'metadata': (None, 'Bytes'),
            'parts': ['u32'],
            'src': (None, 'Bytes'),
            'thumb': (None, 'Bytes'),
        },
        'Slot': {
            'base': 'u32',
            'license': (None, 'Bytes'),
            'metadata': (None, 'Bytes'),
            'slot': 'u32',
            'src': (None, 'Bytes'),
            'thumb': (None, 'Bytes'),
        },
    },
}
```
---------
## Constants

---------
### MaxPriorities
#### Value
```python
25
```
#### Python
```python
constant = substrate.get_constant('KylinFeed', 'MaxPriorities')
```
---------
### PartsLimit
#### Value
```python
25
```
#### Python
```python
constant = substrate.get_constant('KylinFeed', 'PartsLimit')
```
---------
### ResourceSymbolLimit
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('KylinFeed', 'ResourceSymbolLimit')
```
---------
## Errors

---------
### CannotAcceptNonOwnedNft

---------
### CannotRejectNonOwnedNft

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
### MetadataNotSet

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
### StorageOverflow
Errors should have helpful documentation associated with them.

---------
### TooLong

---------
### TooManyRecursions

---------