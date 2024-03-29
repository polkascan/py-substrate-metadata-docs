
# RmrkEquip

---------
## Calls

---------
### change_base_issuer
See [`Pallet::change_base_issuer`].
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
See [`Pallet::create_base`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| base_type | `BoundedVec<u8, T::StringLimit>` | 
| symbol | `BoundedVec<u8, T::StringLimit>` | 
| parts | `BoundedVec<PartType<StringLimitOf<T>, BoundedVec<CollectionIdOf<T
>, T::MaxCollectionsEquippablePerPart>,>, T::PartsLimit,>` | 

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
See [`Pallet::equip`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| item | `(CollectionIdOf<T>, ItemIdOf<T>)` | 
| equipper | `(CollectionIdOf<T>, ItemIdOf<T>)` | 
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
See [`Pallet::equippable`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| base_id | `BaseId` | 
| slot_id | `SlotId` | 
| equippables | `EquippableList<BoundedVec<CollectionIdOf<T>, T::
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
See [`Pallet::equippable_add`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| base_id | `BaseId` | 
| slot_id | `SlotId` | 
| equippable | `CollectionIdOf<T>` | 

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
See [`Pallet::equippable_remove`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| base_id | `BaseId` | 
| slot_id | `SlotId` | 
| equippable | `CollectionIdOf<T>` | 

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
See [`Pallet::theme_add`].
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
See [`Pallet::unequip`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| item | `(CollectionIdOf<T>, ItemIdOf<T>)` | 
| unequipper | `(CollectionIdOf<T>, ItemIdOf<T>)` | 
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
| item_collection | `CollectionIdOf<T>` | ```u32```
| item_nft | `ItemIdOf<T>` | ```u32```
| base_id | `BaseId` | ```u32```
| slot_id | `SlotId` | ```u32```

---------
### SlotUnequipped
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| item_collection | `CollectionIdOf<T>` | ```u32```
| item_nft | `ItemIdOf<T>` | ```u32```
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