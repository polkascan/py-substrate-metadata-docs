
# Unique

---------
## Calls

---------
### add_collection_admin
See [`Pallet::add_collection_admin`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| new_admin_id | `T::CrossAccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'add_collection_admin', {
    'collection_id': 'u32',
    'new_admin_id': {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
}
)
```

---------
### add_to_allow_list
See [`Pallet::add_to_allow_list`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| address | `T::CrossAccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'add_to_allow_list', {
    'address': {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
    'collection_id': 'u32',
}
)
```

---------
### approve
See [`Pallet::approve`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| spender | `T::CrossAccountId` | 
| collection_id | `CollectionId` | 
| item_id | `TokenId` | 
| amount | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'approve', {
    'amount': 'u128',
    'collection_id': 'u32',
    'item_id': 'u32',
    'spender': {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
}
)
```

---------
### approve_from
See [`Pallet::approve_from`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| from | `T::CrossAccountId` | 
| to | `T::CrossAccountId` | 
| collection_id | `CollectionId` | 
| item_id | `TokenId` | 
| amount | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'approve_from', {
    'amount': 'u128',
    'collection_id': 'u32',
    'from': {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
    'item_id': 'u32',
    'to': {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
}
)
```

---------
### burn_from
See [`Pallet::burn_from`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| from | `T::CrossAccountId` | 
| item_id | `TokenId` | 
| value | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'burn_from', {
    'collection_id': 'u32',
    'from': {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
    'item_id': 'u32',
    'value': 'u128',
}
)
```

---------
### burn_item
See [`Pallet::burn_item`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| item_id | `TokenId` | 
| value | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'burn_item', {
    'collection_id': 'u32',
    'item_id': 'u32',
    'value': 'u128',
}
)
```

---------
### change_collection_owner
See [`Pallet::change_collection_owner`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| new_owner | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'change_collection_owner', {
    'collection_id': 'u32',
    'new_owner': 'AccountId',
}
)
```

---------
### confirm_sponsorship
See [`Pallet::confirm_sponsorship`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'confirm_sponsorship', {'collection_id': 'u32'}
)
```

---------
### create_collection
See [`Pallet::create_collection`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_name | `BoundedVec<u16, ConstU32<MAX_COLLECTION_NAME_LENGTH>>` | 
| collection_description | `BoundedVec<u16, ConstU32<MAX_COLLECTION_DESCRIPTION_LENGTH>>` | 
| token_prefix | `BoundedVec<u8, ConstU32<MAX_TOKEN_PREFIX_LENGTH>>` | 
| mode | `CollectionMode` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'create_collection', {
    'collection_description': ['u16'],
    'collection_name': ['u16'],
    'mode': {
        'Fungible': 'u8',
        'NFT': None,
        'ReFungible': None,
    },
    'token_prefix': 'Bytes',
}
)
```

---------
### create_collection_ex
See [`Pallet::create_collection_ex`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| data | `CreateCollectionData<T::CrossAccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'create_collection_ex', {
    'data': {
        'access': (
            None,
            ('Normal', 'AllowList'),
        ),
        'admin_list': [
            {
                'Ethereum': '[u8; 20]',
                'Substrate': 'AccountId',
            },
        ],
        'description': ['u16'],
        'flags': '[u8; 1]',
        'limits': (
            None,
            {
                'account_token_ownership_limit': (
                    None,
                    'u32',
                ),
                'owner_can_destroy': (
                    None,
                    'bool',
                ),
                'owner_can_transfer': (
                    None,
                    'bool',
                ),
                'sponsor_approve_timeout': (
                    None,
                    'u32',
                ),
                'sponsor_transfer_timeout': (
                    None,
                    'u32',
                ),
                'sponsored_data_rate_limit': (
                    None,
                    {
                        'Blocks': 'u32',
                        'SponsoringDisabled': None,
                    },
                ),
                'sponsored_data_size': (
                    None,
                    'u32',
                ),
                'token_limit': (
                    None,
                    'u32',
                ),
                'transfers_enabled': (
                    None,
                    'bool',
                ),
            },
        ),
        'mode': {
            'Fungible': 'u8',
            'NFT': None,
            'ReFungible': None,
        },
        'name': ['u16'],
        'pending_sponsor': (
            None,
            {
                'Ethereum': '[u8; 20]',
                'Substrate': 'AccountId',
            },
        ),
        'permissions': (
            None,
            {
                'access': (
                    None,
                    (
                        'Normal',
                        'AllowList',
                    ),
                ),
                'mint_mode': (
                    None,
                    'bool',
                ),
                'nesting': (
                    None,
                    {
                        'collection_admin': 'bool',
                        'restricted': (
                            None,
                            'scale_info::281',
                        ),
                        'token_owner': 'bool',
                    },
                ),
            },
        ),
        'properties': [
            {
                'key': 'Bytes',
                'value': 'Bytes',
            },
        ],
        'token_prefix': 'Bytes',
        'token_property_permissions': [
            {
                'key': 'Bytes',
                'permission': {
                    'collection_admin': 'bool',
                    'mutable': 'bool',
                    'token_owner': 'bool',
                },
            },
        ],
    },
}
)
```

---------
### create_item
See [`Pallet::create_item`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| owner | `T::CrossAccountId` | 
| data | `CreateItemData` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'create_item', {
    'collection_id': 'u32',
    'data': {
        'Fungible': {'value': 'u128'},
        'NFT': {
            'properties': [
                {
                    'key': 'Bytes',
                    'value': 'Bytes',
                },
            ],
        },
        'ReFungible': {
            'pieces': 'u128',
            'properties': [
                {
                    'key': 'Bytes',
                    'value': 'Bytes',
                },
            ],
        },
    },
    'owner': {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
}
)
```

---------
### create_multiple_items
See [`Pallet::create_multiple_items`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| owner | `T::CrossAccountId` | 
| items_data | `Vec<CreateItemData>` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'create_multiple_items', {
    'collection_id': 'u32',
    'items_data': [
        {
            'Fungible': {
                'value': 'u128',
            },
            'NFT': {
                'properties': [
                    {
                        'key': 'Bytes',
                        'value': 'Bytes',
                    },
                ],
            },
            'ReFungible': {
                'pieces': 'u128',
                'properties': [
                    {
                        'key': 'Bytes',
                        'value': 'Bytes',
                    },
                ],
            },
        },
    ],
    'owner': {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
}
)
```

---------
### create_multiple_items_ex
See [`Pallet::create_multiple_items_ex`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| data | `CreateItemExData<T::CrossAccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'create_multiple_items_ex', {
    'collection_id': 'u32',
    'data': {
        'Fungible': 'scale_info::306',
        'NFT': [
            {
                'owner': {
                    'Ethereum': '[u8; 20]',
                    'Substrate': 'AccountId',
                },
                'properties': [
                    'scale_info::289',
                ],
            },
        ],
        'RefungibleMultipleItems': [
            {
                'pieces': 'u128',
                'properties': [
                    'scale_info::289',
                ],
                'user': {
                    'Ethereum': '[u8; 20]',
                    'Substrate': 'AccountId',
                },
            },
        ],
        'RefungibleMultipleOwners': {
            'properties': [
                {
                    'key': 'Bytes',
                    'value': 'Bytes',
                },
            ],
            'users': 'scale_info::306',
        },
    },
}
)
```

---------
### delete_collection_properties
See [`Pallet::delete_collection_properties`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| property_keys | `Vec<PropertyKey>` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'delete_collection_properties', {
    'collection_id': 'u32',
    'property_keys': ['Bytes'],
}
)
```

---------
### delete_token_properties
See [`Pallet::delete_token_properties`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| token_id | `TokenId` | 
| property_keys | `Vec<PropertyKey>` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'delete_token_properties', {
    'collection_id': 'u32',
    'property_keys': ['Bytes'],
    'token_id': 'u32',
}
)
```

---------
### destroy_collection
See [`Pallet::destroy_collection`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'destroy_collection', {'collection_id': 'u32'}
)
```

---------
### force_repair_collection
See [`Pallet::force_repair_collection`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'force_repair_collection', {'collection_id': 'u32'}
)
```

---------
### force_repair_item
See [`Pallet::force_repair_item`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| item_id | `TokenId` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'force_repair_item', {
    'collection_id': 'u32',
    'item_id': 'u32',
}
)
```

---------
### remove_collection_admin
See [`Pallet::remove_collection_admin`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| account_id | `T::CrossAccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'remove_collection_admin', {
    'account_id': {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
    'collection_id': 'u32',
}
)
```

---------
### remove_collection_sponsor
See [`Pallet::remove_collection_sponsor`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'remove_collection_sponsor', {'collection_id': 'u32'}
)
```

---------
### remove_from_allow_list
See [`Pallet::remove_from_allow_list`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| address | `T::CrossAccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'remove_from_allow_list', {
    'address': {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
    'collection_id': 'u32',
}
)
```

---------
### repartition
See [`Pallet::repartition`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| token_id | `TokenId` | 
| amount | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'repartition', {
    'amount': 'u128',
    'collection_id': 'u32',
    'token_id': 'u32',
}
)
```

---------
### set_allowance_for_all
See [`Pallet::set_allowance_for_all`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| operator | `T::CrossAccountId` | 
| approve | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'set_allowance_for_all', {
    'approve': 'bool',
    'collection_id': 'u32',
    'operator': {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
}
)
```

---------
### set_collection_limits
See [`Pallet::set_collection_limits`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| new_limit | `CollectionLimits` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'set_collection_limits', {
    'collection_id': 'u32',
    'new_limit': {
        'account_token_ownership_limit': (
            None,
            'u32',
        ),
        'owner_can_destroy': (
            None,
            'bool',
        ),
        'owner_can_transfer': (
            None,
            'bool',
        ),
        'sponsor_approve_timeout': (
            None,
            'u32',
        ),
        'sponsor_transfer_timeout': (
            None,
            'u32',
        ),
        'sponsored_data_rate_limit': (
            None,
            {
                'Blocks': 'u32',
                'SponsoringDisabled': None,
            },
        ),
        'sponsored_data_size': (
            None,
            'u32',
        ),
        'token_limit': (None, 'u32'),
        'transfers_enabled': (
            None,
            'bool',
        ),
    },
}
)
```

---------
### set_collection_permissions
See [`Pallet::set_collection_permissions`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| new_permission | `CollectionPermissions` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'set_collection_permissions', {
    'collection_id': 'u32',
    'new_permission': {
        'access': (
            None,
            ('Normal', 'AllowList'),
        ),
        'mint_mode': (None, 'bool'),
        'nesting': (
            None,
            {
                'collection_admin': 'bool',
                'restricted': (
                    None,
                    'scale_info::281',
                ),
                'token_owner': 'bool',
            },
        ),
    },
}
)
```

---------
### set_collection_properties
See [`Pallet::set_collection_properties`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| properties | `Vec<Property>` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'set_collection_properties', {
    'collection_id': 'u32',
    'properties': [
        {
            'key': 'Bytes',
            'value': 'Bytes',
        },
    ],
}
)
```

---------
### set_collection_sponsor
See [`Pallet::set_collection_sponsor`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| new_sponsor | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'set_collection_sponsor', {
    'collection_id': 'u32',
    'new_sponsor': 'AccountId',
}
)
```

---------
### set_token_properties
See [`Pallet::set_token_properties`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| token_id | `TokenId` | 
| properties | `Vec<Property>` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'set_token_properties', {
    'collection_id': 'u32',
    'properties': [
        {
            'key': 'Bytes',
            'value': 'Bytes',
        },
    ],
    'token_id': 'u32',
}
)
```

---------
### set_token_property_permissions
See [`Pallet::set_token_property_permissions`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| property_permissions | `Vec<PropertyKeyPermission>` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'set_token_property_permissions', {
    'collection_id': 'u32',
    'property_permissions': [
        {
            'key': 'Bytes',
            'permission': {
                'collection_admin': 'bool',
                'mutable': 'bool',
                'token_owner': 'bool',
            },
        },
    ],
}
)
```

---------
### set_transfers_enabled_flag
See [`Pallet::set_transfers_enabled_flag`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 
| value | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'set_transfers_enabled_flag', {
    'collection_id': 'u32',
    'value': 'bool',
}
)
```

---------
### transfer
See [`Pallet::transfer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| recipient | `T::CrossAccountId` | 
| collection_id | `CollectionId` | 
| item_id | `TokenId` | 
| value | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'transfer', {
    'collection_id': 'u32',
    'item_id': 'u32',
    'recipient': {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
    'value': 'u128',
}
)
```

---------
### transfer_from
See [`Pallet::transfer_from`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| from | `T::CrossAccountId` | 
| recipient | `T::CrossAccountId` | 
| collection_id | `CollectionId` | 
| item_id | `TokenId` | 
| value | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'transfer_from', {
    'collection_id': 'u32',
    'from': {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
    'item_id': 'u32',
    'recipient': {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
    'value': 'u128',
}
)
```

---------
## Storage functions

---------
### ChainVersion
 Used for migrations

#### Python
```python
result = substrate.query(
    'Unique', 'ChainVersion', []
)
```

#### Return value
```python
'u64'
```
---------
### CreateItemBasket
 (Collection id (controlled?2), who created (real))
 TODO: Off chain worker should remove from this map when collection gets removed

#### Python
```python
result = substrate.query(
    'Unique', 'CreateItemBasket', [('u32', 'AccountId')]
)
```

#### Return value
```python
'u32'
```
---------
### FungibleApproveBasket
 Last sponsoring of fungible tokens approval in a collection

#### Python
```python
result = substrate.query(
    'Unique', 'FungibleApproveBasket', ['u32', 'AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### FungibleTransferBasket
 Collection id (controlled?2), owning user (real)

#### Python
```python
result = substrate.query(
    'Unique', 'FungibleTransferBasket', ['u32', 'AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### NftApproveBasket
 Last sponsoring of NFT approval in a collection

#### Python
```python
result = substrate.query(
    'Unique', 'NftApproveBasket', ['u32', 'u32']
)
```

#### Return value
```python
'u32'
```
---------
### NftTransferBasket
 Collection id (controlled?2), token id (controlled?2)

#### Python
```python
result = substrate.query(
    'Unique', 'NftTransferBasket', ['u32', 'u32']
)
```

#### Return value
```python
'u32'
```
---------
### ReFungibleTransferBasket
 Collection id (controlled?2), token id (controlled?2)

#### Python
```python
result = substrate.query(
    'Unique', 'ReFungibleTransferBasket', ['u32', 'u32', 'AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### RefungibleApproveBasket
 Last sponsoring of RFT approval in a collection

#### Python
```python
result = substrate.query(
    'Unique', 'RefungibleApproveBasket', ['u32', 'u32', 'AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### TokenPropertyBasket
 Last sponsoring of token property setting // todo:doc rephrase this and the following

#### Python
```python
result = substrate.query(
    'Unique', 'TokenPropertyBasket', ['u32', 'u32']
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### collection_admins_limit
 Maximum admins per collection.
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Unique', 'collection_admins_limit')
```
---------
### ft_default_collection_limits
 Default FT collection limit.
#### Value
```python
{
    'account_token_ownership_limit': 100000000,
    'owner_can_destroy': True,
    'owner_can_transfer': False,
    'sponsor_approve_timeout': 5,
    'sponsor_transfer_timeout': 5,
    'sponsored_data_rate_limit': 'SponsoringDisabled',
    'sponsored_data_size': 2048,
    'token_limit': 4294967295,
    'transfers_enabled': True,
}
```
#### Python
```python
constant = substrate.get_constant('Unique', 'ft_default_collection_limits')
```
---------
### max_collection_description_length
 Maximal length of a collection description.
#### Value
```python
256
```
#### Python
```python
constant = substrate.get_constant('Unique', 'max_collection_description_length')
```
---------
### max_collection_name_length
 Maximal length of a collection name.
#### Value
```python
64
```
#### Python
```python
constant = substrate.get_constant('Unique', 'max_collection_name_length')
```
---------
### max_collection_properties_size
 Maximum size for all collection properties.
#### Value
```python
40960
```
#### Python
```python
constant = substrate.get_constant('Unique', 'max_collection_properties_size')
```
---------
### max_properties_per_item
 A maximum number of token properties.
#### Value
```python
64
```
#### Python
```python
constant = substrate.get_constant('Unique', 'max_properties_per_item')
```
---------
### max_property_key_length
 Maximal length of a property key.
#### Value
```python
256
```
#### Python
```python
constant = substrate.get_constant('Unique', 'max_property_key_length')
```
---------
### max_property_value_length
 Maximal length of a property value.
#### Value
```python
32768
```
#### Python
```python
constant = substrate.get_constant('Unique', 'max_property_value_length')
```
---------
### max_token_prefix_length
 Maximal length of a token prefix.
#### Value
```python
16
```
#### Python
```python
constant = substrate.get_constant('Unique', 'max_token_prefix_length')
```
---------
### max_token_properties_size
 Maximum size of all token properties.
#### Value
```python
32768
```
#### Python
```python
constant = substrate.get_constant('Unique', 'max_token_properties_size')
```
---------
### nesting_budget
 A maximum number of levels of depth in the token nesting tree.
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Unique', 'nesting_budget')
```
---------
### nft_default_collection_limits
 Default NFT collection limit.
#### Value
```python
{
    'account_token_ownership_limit': 100000000,
    'owner_can_destroy': True,
    'owner_can_transfer': False,
    'sponsor_approve_timeout': 5,
    'sponsor_transfer_timeout': 5,
    'sponsored_data_rate_limit': 'SponsoringDisabled',
    'sponsored_data_size': 2048,
    'token_limit': 4294967295,
    'transfers_enabled': True,
}
```
#### Python
```python
constant = substrate.get_constant('Unique', 'nft_default_collection_limits')
```
---------
### rft_default_collection_limits
 Default RFT collection limit.
#### Value
```python
{
    'account_token_ownership_limit': 100000000,
    'owner_can_destroy': True,
    'owner_can_transfer': False,
    'sponsor_approve_timeout': 5,
    'sponsor_transfer_timeout': 5,
    'sponsored_data_rate_limit': 'SponsoringDisabled',
    'sponsored_data_size': 2048,
    'token_limit': 4294967295,
    'transfers_enabled': True,
}
```
#### Python
```python
constant = substrate.get_constant('Unique', 'rft_default_collection_limits')
```
---------
## Errors

---------
### CollectionDecimalPointLimitExceeded
Decimal_points parameter must be lower than [`up_data_structs::MAX_DECIMAL_POINTS`].

---------
### EmptyArgument
Length of items properties must be greater than 0.

---------
### RepartitionCalledOnNonRefungibleCollection
Repertition is only supported by refungible collection.

---------