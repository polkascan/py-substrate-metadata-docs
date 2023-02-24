
# Common

---------
## Events

---------
### Approved
Amount pieces of token owned by `sender` was approved for `spender`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CollectionId` | ```u32```
| None | `TokenId` | ```u32```
| None | `T::CrossAccountId` | ```{'Substrate': 'AccountId', 'Ethereum': '[u8; 20]'}```
| None | `T::CrossAccountId` | ```{'Substrate': 'AccountId', 'Ethereum': '[u8; 20]'}```
| None | `u128` | ```u128```

---------
### CollectionCreated
New collection was created
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CollectionId` | ```u32```
| None | `u8` | ```u8```
| None | `T::AccountId` | ```AccountId```

---------
### CollectionDestroyed
New collection was destroyed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CollectionId` | ```u32```

---------
### CollectionPropertyDeleted
The property has been deleted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CollectionId` | ```u32```
| None | `PropertyKey` | ```Bytes```

---------
### CollectionPropertySet
The colletion property has been added or edited.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CollectionId` | ```u32```
| None | `PropertyKey` | ```Bytes```

---------
### ItemCreated
New item was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CollectionId` | ```u32```
| None | `TokenId` | ```u32```
| None | `T::CrossAccountId` | ```{'Substrate': 'AccountId', 'Ethereum': '[u8; 20]'}```
| None | `u128` | ```u128```

---------
### ItemDestroyed
Collection item was burned.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CollectionId` | ```u32```
| None | `TokenId` | ```u32```
| None | `T::CrossAccountId` | ```{'Substrate': 'AccountId', 'Ethereum': '[u8; 20]'}```
| None | `u128` | ```u128```

---------
### PropertyPermissionSet
The token property permission of a collection has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CollectionId` | ```u32```
| None | `PropertyKey` | ```Bytes```

---------
### TokenPropertyDeleted
The token property has been deleted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CollectionId` | ```u32```
| None | `TokenId` | ```u32```
| None | `PropertyKey` | ```Bytes```

---------
### TokenPropertySet
The token property has been added or edited.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CollectionId` | ```u32```
| None | `TokenId` | ```u32```
| None | `PropertyKey` | ```Bytes```

---------
### Transfer
Item was transferred
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CollectionId` | ```u32```
| None | `TokenId` | ```u32```
| None | `T::CrossAccountId` | ```{'Substrate': 'AccountId', 'Ethereum': '[u8; 20]'}```
| None | `T::CrossAccountId` | ```{'Substrate': 'AccountId', 'Ethereum': '[u8; 20]'}```
| None | `u128` | ```u128```

---------
## Storage functions

---------
### AdminAmount
 Storage of the amount of collection admins.

#### Python
```python
result = substrate.query(
    'Common', 'AdminAmount', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### Allowlist
 Allowlisted collection users.

#### Python
```python
result = substrate.query(
    'Common', 'Allowlist', [
    'u32',
    {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
]
)
```

#### Return value
```python
'bool'
```
---------
### CollectionById
 Storage of collection info.

#### Python
```python
result = substrate.query(
    'Common', 'CollectionById', ['u32']
)
```

#### Return value
```python
{
    'description': ['u16'],
    'flags': '[u8; 1]',
    'limits': {
        'account_token_ownership_limit': (None, 'u32'),
        'owner_can_destroy': (None, 'bool'),
        'owner_can_transfer': (None, 'bool'),
        'sponsor_approve_timeout': (None, 'u32'),
        'sponsor_transfer_timeout': (None, 'u32'),
        'sponsored_data_rate_limit': (
            None,
            {'Blocks': 'u32', 'SponsoringDisabled': None},
        ),
        'sponsored_data_size': (None, 'u32'),
        'token_limit': (None, 'u32'),
        'transfers_enabled': (None, 'bool'),
    },
    'mode': {'Fungible': 'u8', 'NFT': None, 'ReFungible': None},
    'name': ['u16'],
    'owner': 'AccountId',
    'permissions': {
        'access': (None, ('Normal', 'AllowList')),
        'mint_mode': (None, 'bool'),
        'nesting': (
            None,
            {
                'collection_admin': 'bool',
                'restricted': (None, 'scale_info::247'),
                'token_owner': 'bool',
            },
        ),
    },
    'sponsorship': {
        'Confirmed': 'AccountId',
        'Disabled': None,
        'Unconfirmed': 'AccountId',
    },
    'token_prefix': 'Bytes',
}
```
---------
### CollectionProperties
 Storage of collection properties.

#### Python
```python
result = substrate.query(
    'Common', 'CollectionProperties', ['u32']
)
```

#### Return value
```python
{'consumed_space': 'u32', 'map': 'scale_info::342', 'space_limit': 'u32'}
```
---------
### CollectionPropertyPermissions
 Storage of token property permissions of a collection.

#### Python
```python
result = substrate.query(
    'Common', 'CollectionPropertyPermissions', ['u32']
)
```

#### Return value
```python
'scale_info::347'
```
---------
### CreatedCollectionCount
 Storage of the count of created collections. Essentially contains the last collection ID.

#### Python
```python
result = substrate.query(
    'Common', 'CreatedCollectionCount', []
)
```

#### Return value
```python
'u32'
```
---------
### DestroyedCollectionCount
 Storage of the count of deleted collections.

#### Python
```python
result = substrate.query(
    'Common', 'DestroyedCollectionCount', []
)
```

#### Return value
```python
'u32'
```
---------
### DummyStorageValue
 Not used by code, exists only to provide some types to metadata.

#### Python
```python
result = substrate.query(
    'Common', 'DummyStorageValue', []
)
```

#### Return value
```python
(
    {'alive': 'u32', 'created': 'u32', 'destroyed': 'u32'},
    'u32',
    'u32',
    {'collection': 'u32', 'token': 'u32'},
    "[({'properties': ['scale_info::254'], 'owner': (None, 'scale_info::90'), 'pieces': 'u128'}, {'owner': 'AccountId', 'mode': 'scale_info::231', 'name': ['u16'], 'description': ['u16'], 'token_prefix': 'Bytes', 'sponsorship': 'scale_info::337', 'limits': 'scale_info::236', 'permissions': 'scale_info::241', 'token_property_permissions': ['scale_info::250'], 'properties': ['scale_info::254'], 'read_only': 'bool', 'flags': 'scale_info::359'}, {'issuer': 'AccountId', 'metadata': 'Bytes', 'max': (None, 'u32'), 'symbol': 'Bytes', 'nfts_count': 'u32'}, {'owner': 'scale_info::364', 'royalty': (None, 'scale_info::366'), 'metadata': 'Bytes', 'equipped': 'bool', 'pending': 'bool'}, {'id': 'u32', 'resource': 'scale_info::369', 'pending': 'bool', 'pending_removal': 'bool'}, {'key': 'Bytes', 'value': 'Bytes'}, {'issuer': 'AccountId', 'base_type': 'Bytes', 'symbol': 'Bytes'}, {'FixedPart': 'scale_info::380', 'SlotPart': 'scale_info::381'}, {'name': 'Bytes', 'properties': ['scale_info::385'], 'inherit': 'bool'}, {'collection_id': 'u32', 'nft_id': 'u32'}); 0]",
)
```
---------
### IsAdmin
 List of collection admins.

#### Python
```python
result = substrate.query(
    'Common', 'IsAdmin', [
    'u32',
    {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
]
)
```

#### Return value
```python
'bool'
```
---------
## Constants

---------
### CollectionCreationPrice
 Set price to create a collection.
#### Value
```python
2000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Common', 'CollectionCreationPrice')
```
---------
### collection_admins_limit
 Maximum admins per collection.
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Common', 'collection_admins_limit')
```
---------
## Errors

---------
### AccountTokenLimitExceeded
Account token limit exceeded per collection

---------
### AddressIsZero
Can&\#x27;t transfer tokens to ethereum zero address

---------
### AddressNotInAllowlist
Address is not in allow list.

---------
### ApprovedValueTooLow
Requested value is more than the approved

---------
### CantApproveMoreThanOwned
Tried to approve more than owned

---------
### CantDestroyNotEmptyCollection
Destroying only empty collections is allowed

---------
### CollectionAdminCountExceeded
Exceeded max admin count

---------
### CollectionDescriptionLimitExceeded
Collection description can not be longer than 255 char.

---------
### CollectionFieldSizeExceeded
Tried to store more data than allowed in collection field

---------
### CollectionIsExternal
Tried to access an external collection with an internal API

---------
### CollectionIsInternal
Tried to access an internal collection with an external API

---------
### CollectionLimitBoundsExceeded
Collection limit bounds per collection exceeded

---------
### CollectionNameLimitExceeded
Collection name can not be longer than 63 char.

---------
### CollectionNotFound
This collection does not exist.

---------
### CollectionTokenLimitExceeded
Collection token limit exceeded

---------
### CollectionTokenPrefixLimitExceeded
Token prefix can not be longer than 15 char.

---------
### EmptyPropertyKey
Empty property keys are forbidden

---------
### InvalidCharacterInPropertyKey
Only ASCII letters, digits, and symbols `_`, `-`, and `.` are allowed

---------
### MetadataFlagFrozen
Metadata flag frozen

---------
### MustBeTokenOwner
Sender parameter and item owner must be equal.

---------
### NoPermission
No permission to perform action

---------
### NoSpaceForProperty
Tried to store more property data than allowed

---------
### NotSufficientFounds
Insufficient funds to perform an action

---------
### OwnerPermissionsCantBeReverted
Tried to enable permissions which are only permitted to be disabled

---------
### PropertyKeyIsTooLong
Property key is too long

---------
### PropertyLimitReached
Tried to store more property keys than allowed

---------
### PublicMintingNotAllowed
Collection is not in mint mode.

---------
### SourceCollectionIsNotAllowedToNest
Only tokens from specific collections may nest tokens under this one

---------
### TokenNotFound
Item does not exist

---------
### TokenValueTooLow
Item is balance not enough

---------
### TotalCollectionsLimitExceeded
Total collections bound exceeded.

---------
### TransferNotAllowed
Collection settings not allowing items transferring

---------
### UnsupportedOperation
The operation is not supported

---------
### UserIsNotAllowedToNest
User does not satisfy the nesting rule

---------