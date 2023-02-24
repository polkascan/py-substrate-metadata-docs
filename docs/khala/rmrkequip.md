
# RmrkEquip

---------
## Calls

---------
### change_base_issuer
Change the issuer of a Base

Parameters:
- `origin`: sender of the transaction
- `base_id`: base_id to change issuer of
- `new_issuer`: Base&\#x27;s new issuer
#### Attributes
| Name | Type |
| -------- | -------- | 
| base_id | `BaseId` | 
| new_issuer | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkEquip', 'change_base_issuer', {
    'base_id': 'u32',
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
### create_base
Creates a new Base.
Modeled after [base interaction](https://github.com/rmrk-team/rmrk-spec/blob/master/standards/rmrk2.0.0/interactions/base.md)

Parameters:
- origin: Caller, will be assigned as the issuer of the Base
- base_type: media type, e.g. &quot;svg&quot;
- symbol: arbitrary client-chosen symbol, e.g. &quot;kanaria_superbird&quot;
- parts: array of Fixed and Slot parts composing the base, confined in length by
  PartsLimit
#### Attributes
| Name | Type |
| -------- | -------- | 
| base_type | `BoundedVec<u8, T::StringLimit>` | 
| symbol | `BoundedVec<u8, T::StringLimit>` | 
| parts | `BoundedVec<PartType<StringLimitOf<T>, BoundedVec<T::CollectionId, T
::MaxCollectionsEquippablePerPart>,>, T::PartsLimit,>` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkEquip', 'create_base', {
    'base_type': 'Bytes',
    'parts': [
        {
            'FixedPart': {
                'id': 'u32',
                'src': 'Bytes',
                'z': 'u32',
            },
            'SlotPart': {
                'equippable': {
                    'All': None,
                    'Custom': ['u32'],
                    'Empty': None,
                },
                'id': 'u32',
                'src': (None, 'Bytes'),
                'z': 'u32',
            },
        },
    ],
    'symbol': 'Bytes',
}
)
```

---------
### equip
Equips a child NFT&\#x27;s resource to a parent&\#x27;s slot, if all are available.
Equipping operations are maintained inside the Equippings storage.
Modeled after [equip interaction](https://github.com/rmrk-team/rmrk-spec/blob/master/standards/rmrk2.0.0/interactions/equip.md)

Parameters:
- origin: The caller of the function, not necessarily anything else
- item: Child NFT being equipped
- equipper: Parent NFT which will equip the item
- base: ID of the base which the item and equipper must each have a resource referencing
- slot: ID of the slot which the item and equipper must each have a resource referencing
#### Attributes
| Name | Type |
| -------- | -------- | 
| item | `(T::CollectionId, T::ItemId)` | 
| equipper | `(T::CollectionId, T::ItemId)` | 
| resource_id | `ResourceId` | 
| base | `BaseId` | 
| slot | `SlotId` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkEquip', 'equip', {
    'base': 'u32',
    'equipper': ('u32', 'u32'),
    'item': ('u32', 'u32'),
    'resource_id': 'u32',
    'slot': 'u32',
}
)
```

---------
### equippable
Updates the array of Collections allowed to be equipped to a Base&\#x27;s specified Slot Part.
Modeled after [equippable interaction](https://github.com/rmrk-team/rmrk-spec/blob/master/standards/rmrk2.0.0/interactions/equippable.md)

Parameters:
- origin: The caller of the function, must be issuer of the base
- base_id: The Base containing the Slot Part to be updated
- part_id: The Slot Part whose Equippable List is being updated
- equippables: The list of equippables that will override the current Equippaables list
#### Attributes
| Name | Type |
| -------- | -------- | 
| base_id | `BaseId` | 
| slot_id | `SlotId` | 
| equippables | `EquippableList<BoundedVec<T::CollectionId, T::
MaxCollectionsEquippablePerPart>,>` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkEquip', 'equippable', {
    'base_id': 'u32',
    'equippables': {
        'All': None,
        'Custom': ['u32'],
        'Empty': None,
    },
    'slot_id': 'u32',
}
)
```

---------
### equippable_add
Adds a new collection that is allowed to be equipped to a Base&\#x27;s specified Slot Part.

Parameters:
- origin: The caller of the function, must be issuer of the base
- base_id: The Base containing the Slot Part to be updated
- part_id: The Slot Part whose Equippable List is being updated
- equippable: The equippable that will be added to the current Equippaables list
#### Attributes
| Name | Type |
| -------- | -------- | 
| base_id | `BaseId` | 
| slot_id | `SlotId` | 
| equippable | `T::CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkEquip', 'equippable_add', {
    'base_id': 'u32',
    'equippable': 'u32',
    'slot_id': 'u32',
}
)
```

---------
### equippable_remove
Remove a collection from the equippables list.

Parameters:
- origin: The caller of the function, must be issuer of the base
- base_id: The Base containing the Slot Part to be updated
- part_id: The Slot Part whose Equippable List is being updated
- equippable: The equippable that will be removed from the current Equippaables list
#### Attributes
| Name | Type |
| -------- | -------- | 
| base_id | `BaseId` | 
| slot_id | `SlotId` | 
| equippable | `T::CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkEquip', 'equippable_remove', {
    'base_id': 'u32',
    'equippable': 'u32',
    'slot_id': 'u32',
}
)
```

---------
### theme_add
Adds a Theme to a Base.
Modeled after [themeadd interaction](https://github.com/rmrk-team/rmrk-spec/blob/master/standards/rmrk2.0.0/interactions/themeadd.md)
Themes are stored in the Themes storage
A Theme named &quot;default&quot; is required prior to adding other Themes.

Parameters:
- origin: The caller of the function, must be issuer of the base
- base_id: The Base containing the Theme to be updated
- theme: The Theme to add to the Base.  A Theme has a name and properties, which are an
  array of [key, value, inherit].  This array is bounded by MaxPropertiesPerTheme.
  - key: arbitrary BoundedString, defined by client
  - value: arbitrary BoundedString, defined by client
  - inherit: optional bool
#### Attributes
| Name | Type |
| -------- | -------- | 
| base_id | `BaseId` | 
| theme | `BoundedThemeOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkEquip', 'theme_add', {
    'base_id': 'u32',
    'theme': {
        'inherit': 'bool',
        'name': 'Bytes',
        'properties': [
            {
                'key': 'Bytes',
                'value': 'Bytes',
            },
        ],
    },
}
)
```

---------
### unequip
Unequips a child NFT&\#x27;s resource from its parent&\#x27;s slot.
Can be successful if
- Item has beeen burned
- Item is equipped and extrinsic called by equipping item owner
- Item is equipped and extrinsic called by equipper NFT owner
Equipping operations are maintained inside the Equippings storage.
Modeled after [equip interaction](https://github.com/rmrk-team/rmrk-spec/blob/master/standards/rmrk2.0.0/interactions/equip.md)

Parameters:
- origin: The caller of the function, not necessarily anything else
- item: Child NFT being unequipped
- unequipper: Parent NFT which will unequip the item
- base: ID of the base which the item and equipper must each have a resource referencing
- slot: ID of the slot which the item and equipper must each have a resource referencing
#### Attributes
| Name | Type |
| -------- | -------- | 
| item | `(T::CollectionId, T::ItemId)` | 
| unequipper | `(T::CollectionId, T::ItemId)` | 
| base | `BaseId` | 
| slot | `SlotId` | 

#### Python
```python
call = substrate.compose_call(
    'RmrkEquip', 'unequip', {
    'base': 'u32',
    'item': ('u32', 'u32'),
    'slot': 'u32',
    'unequipper': ('u32', 'u32'),
}
)
```

---------
## Events

---------
### BaseCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| issuer | `T::AccountId` | ```AccountId```
| base_id | `BaseId` | ```u32```

---------
### BaseIssuerChanged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_issuer | `T::AccountId` | ```AccountId```
| new_issuer | `T::AccountId` | ```AccountId```
| base_id | `BaseId` | ```u32```

---------
### EquippablesUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| base_id | `BaseId` | ```u32```
| slot_id | `SlotId` | ```u32```

---------
### SlotEquipped
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| item_collection | `T::CollectionId` | ```u32```
| item_nft | `T::ItemId` | ```u32```
| base_id | `BaseId` | ```u32```
| slot_id | `SlotId` | ```u32```

---------
### SlotUnequipped
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| item_collection | `T::CollectionId` | ```u32```
| item_nft | `T::ItemId` | ```u32```
| base_id | `BaseId` | ```u32```
| slot_id | `SlotId` | ```u32```

---------
## Storage functions

---------
### Bases
 Stores Bases info (issuer, base_type, symbol, parts)
 TODO https://github.com/rmrk-team/rmrk-substrate/issues/98
 Delete Parts from Bases info, as it&#x27;s kept in Parts storage

#### Python
```python
result = substrate.query(
    'RmrkEquip', 'Bases', ['u32']
)
```

#### Return value
```python
{'base_type': 'Bytes', 'issuer': 'AccountId', 'symbol': 'Bytes'}
```
---------
### Equippings
 Stores Equippings info ((equipper, base, slot), equipped_resource)

#### Python
```python
result = substrate.query(
    'RmrkEquip', 'Equippings', [('u32', 'u32'), 'u32', 'u32']
)
```

#### Return value
```python
'u32'
```
---------
### NextBaseId
 Stores the incrementing NextBaseId

#### Python
```python
result = substrate.query(
    'RmrkEquip', 'NextBaseId', []
)
```

#### Return value
```python
'u32'
```
---------
### NextPartId
 Stores the incrementing NextPartId

#### Python
```python
result = substrate.query(
    'RmrkEquip', 'NextPartId', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### Parts
 Stores Parts (either FixedPart or SlotPart)
 - SlotPart: id, equippable (list), src, z
 - FixedPart: id, src, z

#### Python
```python
result = substrate.query(
    'RmrkEquip', 'Parts', ['u32', 'u32']
)
```

#### Return value
```python
{
    'FixedPart': {'id': 'u32', 'src': 'Bytes', 'z': 'u32'},
    'SlotPart': {
        'equippable': {'All': None, 'Custom': ['u32'], 'Empty': None},
        'id': 'u32',
        'src': (None, 'Bytes'),
        'z': 'u32',
    },
}
```
---------
### Themes
 Stores Theme info ((base, theme name, property key), property value)

#### Python
```python
result = substrate.query(
    'RmrkEquip', 'Themes', ['u32', 'Bytes', 'Bytes']
)
```

#### Return value
```python
'Bytes'
```
---------
## Constants

---------
### MaxCollectionsEquippablePerPart
 Maximum number of Properties allowed for any Theme
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('RmrkEquip', 'MaxCollectionsEquippablePerPart')
```
---------
### MaxPropertiesPerTheme
 Maximum allowed Parts (either Fixed or Slot) per Base
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('RmrkEquip', 'MaxPropertiesPerTheme')
```
---------
## Errors

---------
### BaseDoesntExist

---------
### CantEquipFixedPart

---------
### CollectionNotEquippable

---------
### EquipperDoesntExist

---------
### ExceedsMaxPartsPerBase

---------
### ItemAlreadyEquipped

---------
### ItemDoesntExist

---------
### ItemHasNoResourceToEquipThere

---------
### ItemNotEquipped

---------
### MustBeDirectParent

---------
### NeedsDefaultThemeFirst

---------
### NoAvailableBaseId

---------
### NoAvailablePartId

---------
### NoEquippableOnFixedPart

---------
### NoResourceForThisBaseFoundOnNft

---------
### PartDoesntExist

---------
### PermissionError

---------
### SlotAlreadyEquipped

---------
### SlotNotEquipped

---------
### TooManyEquippables

---------
### TooManyProperties

---------
### UnequipperMustOwnEitherItemOrEquipper

---------
### UnexpectedTryFromIntError

---------
### UnexpectedVecConversionError

---------
### UnknownError

---------