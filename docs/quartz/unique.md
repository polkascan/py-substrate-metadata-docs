
# Unique

---------
## Calls

---------
### add_collection_admin
Add an admin to a collection.

NFT Collection can be controlled by multiple admin addresses
(some which can also be servers, for example). Admins can issue
and burn NFTs, as well as add and remove other admins,
but cannot change NFT or Collection ownership.

\# Permissions

* Collection owner
* Collection admin

\# Arguments

* `collection_id`: ID of the Collection to add an admin for.
* `new_admin`: Address of new admin to add.
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
Add an address to allow list.

\# Permissions

* Collection owner
* Collection admin

\# Arguments

* `collection_id`: ID of the modified collection.
* `address`: ID of the address to be added to the allowlist.
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
Allow a non-permissioned address to transfer or burn an item.

\# Permissions

* Collection owner
* Collection admin
* Current item owner

\# Arguments

* `spender`: Account to be approved to make specific transactions on non-owned tokens.
* `collection_id`: ID of the collection the item belongs to.
* `item_id`: ID of the item transactions on which are now approved.
* `amount`: Number of pieces of the item approved for a transaction (maximum of 1 for NFTs).
Set to 0 to revoke the approval.
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
Allow a non-permissioned address to transfer or burn an item from owner&\#x27;s eth mirror.

\# Permissions

* Collection owner
* Collection admin
* Current item owner

\# Arguments

* `from`: Owner&\#x27;s account eth mirror
* `to`: Account to be approved to make specific transactions on non-owned tokens.
* `collection_id`: ID of the collection the item belongs to.
* `item_id`: ID of the item transactions on which are now approved.
* `amount`: Number of pieces of the item approved for a transaction (maximum of 1 for NFTs).
Set to 0 to revoke the approval.
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
Destroy a token on behalf of the owner as a non-owner account.

See also: [`approve`][`Pallet::approve`].

After this method executes, one approval is removed from the total so that
the approved address will not be able to transfer this item again from this owner.

\# Permissions

* Collection owner
* Collection admin
* Current token owner
* Address approved by current item owner

\# Arguments

* `from`: The owner of the burning item.
* `collection_id`: ID of the collection to which the item belongs.
* `item_id`: ID of item to burn.
* `value`: Number of pieces to burn.
	* Non-Fungible Mode: An NFT is indivisible, there is always 1 corresponding to an ID.
    * Fungible Mode: The desired number of pieces to burn.
    * Re-Fungible Mode: The desired number of pieces to burn.
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
Destroy an item.

\# Permissions

* Collection owner
* Collection admin
* Current item owner

\# Arguments

* `collection_id`: ID of the collection to which the item belongs.
* `item_id`: ID of item to burn.
* `value`: Number of pieces of the item to destroy.
	* Non-Fungible Mode: An NFT is indivisible, there is always 1 corresponding to an ID.
    * Fungible Mode: The desired number of pieces to burn.
    * Re-Fungible Mode: The desired number of pieces to burn.
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
Change the owner of the collection.

\# Permissions

* Collection owner

\# Arguments

* `collection_id`: ID of the modified collection.
* `new_owner`: ID of the account that will become the owner.
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
Confirm own sponsorship of a collection, becoming the sponsor.

An invitation must be pending, see [`set_collection_sponsor`][`Pallet::set_collection_sponsor`].
Sponsor can pay the fees of a transaction instead of the sender,
but only within specified limits.

\# Permissions

* Sponsor-to-be

\# Arguments

* `collection_id`: ID of the collection with the pending sponsor.
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
Create a collection of tokens.

Each Token may have multiple properties encoded as an array of bytes
of certain length. The initial owner of the collection is set
to the address that signed the transaction and can be changed later.

Prefer the more advanced [`create_collection_ex`][`Pallet::create_collection_ex`] instead.

\# Permissions

* Anyone - becomes the owner of the new collection.

\# Arguments

* `collection_name`: Wide-character string with collection name
(limit [`MAX_COLLECTION_NAME_LENGTH`]).
* `collection_description`: Wide-character string with collection description
(limit [`MAX_COLLECTION_DESCRIPTION_LENGTH`]).
* `token_prefix`: Byte string containing the token prefix to mark a collection
to which a token belongs (limit [`MAX_TOKEN_PREFIX_LENGTH`]).
* `mode`: Type of items stored in the collection and type dependent data.

returns collection ID

Deprecated: `create_collection_ex` is more up-to-date and advanced, prefer it instead.
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
Create a collection with explicit parameters.

Prefer it to the deprecated [`create_collection`][`Pallet::create_collection`] method.

\# Permissions

* Anyone - becomes the owner of the new collection.

\# Arguments

* `data`: Explicit data of a collection used for its creation.
#### Attributes
| Name | Type |
| -------- | -------- | 
| data | `CreateCollectionData<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Unique', 'create_collection_ex', {
    'data': {
        'access': (
            None,
            ('Normal', 'AllowList'),
        ),
        'description': ['u16'],
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
            'AccountId',
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
                            'scale_info::323',
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
Mint an item within a collection.

A collection must exist first, see [`create_collection_ex`][`Pallet::create_collection_ex`].

\# Permissions

* Collection owner
* Collection admin
* Anyone if
    * Allow List is enabled, and
    * Address is added to allow list, and
    * MintPermission is enabled (see [`set_collection_permissions`][`Pallet::set_collection_permissions`])

\# Arguments

* `collection_id`: ID of the collection to which an item would belong.
* `owner`: Address of the initial owner of the item.
* `data`: Token data describing the item to store on chain.
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
Create multiple items within a collection.

A collection must exist first, see [`create_collection_ex`][`Pallet::create_collection_ex`].

\# Permissions

* Collection owner
* Collection admin
* Anyone if
    * Allow List is enabled, and
    * Address is added to the allow list, and
    * MintPermission is enabled (see [`set_collection_permissions`][`Pallet::set_collection_permissions`])

\# Arguments

* `collection_id`: ID of the collection to which the tokens would belong.
* `owner`: Address of the initial owner of the tokens.
* `items_data`: Vector of data describing each item to be created.
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
Create multiple items within a collection with explicitly specified initial parameters.

\# Permissions

* Collection owner
* Collection admin
* Anyone if
    * Allow List is enabled, and
    * Address is added to allow list, and
    * MintPermission is enabled (see [`set_collection_permissions`][`Pallet::set_collection_permissions`])

\# Arguments

* `collection_id`: ID of the collection to which the tokens would belong.
* `data`: Explicit item creation data.
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
        'Fungible': 'scale_info::344',
        'NFT': [
            {
                'owner': {
                    'Ethereum': '[u8; 20]',
                    'Substrate': 'AccountId',
                },
                'properties': [
                    {
                        'key': 'Bytes',
                        'value': 'Bytes',
                    },
                ],
            },
        ],
        'RefungibleMultipleItems': [
            {
                'pieces': 'u128',
                'properties': [
                    {
                        'key': 'Bytes',
                        'value': 'Bytes',
                    },
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
            'users': 'scale_info::344',
        },
    },
}
)
```

---------
### delete_collection_properties
Delete specified collection properties.

\# Permissions

* Collection Owner
* Collection Admin

\# Arguments

* `collection_id`: ID of the modified collection.
* `property_keys`: Vector of keys of the properties to be deleted.
Keys support Latin letters, `-`, `_`, and `.` as symbols.
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
Delete specified token properties. Currently properties only work with NFTs.

\# Permissions

* Depends on collection&\#x27;s token property permissions and specified property mutability:
	* Collection owner
	* Collection admin
	* Token owner

\# Arguments

* `collection_id`: ID of the collection to which the token belongs.
* `token_id`: ID of the modified token.
* `property_keys`: Vector of keys of the properties to be deleted.
Keys support Latin letters, `-`, `_`, and `.` as symbols.
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
Destroy a collection if no tokens exist within.

\# Permissions

* Collection owner

\# Arguments

* `collection_id`: Collection to destroy.
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
Repairs a collection if the data was somehow corrupted.

\# Arguments

* `collection_id`: ID of the collection to repair.
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
Repairs a token if the data was somehow corrupted.

\# Arguments

* `collection_id`: ID of the collection the item belongs to.
* `item_id`: ID of the item.
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
Remove admin of a collection.

An admin address can remove itself. List of admins may become empty,
in which case only Collection Owner will be able to add an Admin.

\# Permissions

* Collection owner
* Collection admin

\# Arguments

* `collection_id`: ID of the collection to remove the admin for.
* `account_id`: Address of the admin to remove.
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
Remove a collection&\#x27;s a sponsor, making everyone pay for their own transactions.

\# Permissions

* Collection owner

\# Arguments

* `collection_id`: ID of the collection with the sponsor to remove.
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
Remove an address from allow list.

\# Permissions

* Collection owner
* Collection admin

\# Arguments

* `collection_id`: ID of the modified collection.
* `address`: ID of the address to be removed from the allowlist.
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
Re-partition a refungible token, while owning all of its parts/pieces.

\# Permissions

* Token owner (must own every part)

\# Arguments

* `collection_id`: ID of the collection the RFT belongs to.
* `token_id`: ID of the RFT.
* `amount`: New number of parts/pieces into which the token shall be partitioned.
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
Sets or unsets the approval of a given operator.

The `operator` is allowed to transfer all tokens of the `owner` on their behalf.

\# Arguments

* `owner`: Token owner
* `operator`: Operator
* `approve`: Should operator status be granted or revoked?
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
Set specific limits of a collection. Empty, or None fields mean chain default.

\# Permissions

* Collection owner
* Collection admin

\# Arguments

* `collection_id`: ID of the modified collection.
* `new_limit`: New limits of the collection. Fields that are not set (None)
will not overwrite the old ones.
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
Set specific permissions of a collection. Empty, or None fields mean chain default.

\# Permissions

* Collection owner
* Collection admin

\# Arguments

* `collection_id`: ID of the modified collection.
* `new_permission`: New permissions of the collection. Fields that are not set (None)
will not overwrite the old ones.
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
                    'scale_info::323',
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
Add or change collection properties.

\# Permissions

* Collection owner
* Collection admin

\# Arguments

* `collection_id`: ID of the modified collection.
* `properties`: Vector of key-value pairs stored as the collection&\#x27;s metadata.
Keys support Latin letters, `-`, `_`, and `.` as symbols.
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
Set (invite) a new collection sponsor.

If successful, confirmation from the sponsor-to-be will be pending.

\# Permissions

* Collection owner
* Collection admin

\# Arguments

* `collection_id`: ID of the modified collection.
* `new_sponsor`: ID of the account of the sponsor-to-be.
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
Add or change token properties according to collection&\#x27;s permissions.
Currently properties only work with NFTs.

\# Permissions

* Depends on collection&\#x27;s token property permissions and specified property mutability:
	* Collection owner
	* Collection admin
	* Token owner

See [`set_token_property_permissions`][`Pallet::set_token_property_permissions`].

\# Arguments

* `collection_id: ID of the collection to which the token belongs.
* `token_id`: ID of the modified token.
* `properties`: Vector of key-value pairs stored as the token&\#x27;s metadata.
Keys support Latin letters, `-`, `_`, and `.` as symbols.
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
Add or change token property permissions of a collection.

Without a permission for a particular key, a property with that key
cannot be created in a token.

\# Permissions

* Collection owner
* Collection admin

\# Arguments

* `collection_id`: ID of the modified collection.
* `property_permissions`: Vector of permissions for property keys.
Keys support Latin letters, `-`, `_`, and `.` as symbols.
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
Completely allow or disallow transfers for a particular collection.

\# Permissions

* Collection owner

\# Arguments

* `collection_id`: ID of the collection.
* `value`: New value of the flag, are transfers allowed?
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
Change ownership of the token.

\# Permissions

* Collection owner
* Collection admin
* Current token owner

\# Arguments

* `recipient`: Address of token recipient.
* `collection_id`: ID of the collection the item belongs to.
* `item_id`: ID of the item.
    * Non-Fungible Mode: Required.
    * Fungible Mode: Ignored.
    * Re-Fungible Mode: Required.

* `value`: Amount to transfer.
	* Non-Fungible Mode: An NFT is indivisible, there is always 1 corresponding to an ID.
    * Fungible Mode: The desired number of pieces to transfer.
    * Re-Fungible Mode: The desired number of pieces to transfer.
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
Change ownership of an item on behalf of the owner as a non-owner account.

See the [`approve`][`Pallet::approve`] method for additional information.

After this method executes, one approval is removed from the total so that
the approved address will not be able to transfer this item again from this owner.

\# Permissions

* Collection owner
* Collection admin
* Current item owner
* Address approved by current item owner

\# Arguments

* `from`: Address that currently owns the token.
* `recipient`: Address of the new token-owner-to-be.
* `collection_id`: ID of the collection the item.
* `item_id`: ID of the item to be transferred.
* `value`: Amount to transfer.
	* Non-Fungible Mode: An NFT is indivisible, there is always 1 corresponding to an ID.
    * Fungible Mode: The desired number of pieces to transfer.
    * Re-Fungible Mode: The desired number of pieces to transfer.
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
### VariableMetaDataBasket
 Variable metadata sponsoring
 Collection id (controlled?2), token id (controlled?2)

#### Python
```python
result = substrate.query(
    'Unique', 'VariableMetaDataBasket', ['u32', 'u32']
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### COLLECTION_ADMINS_LIMIT
Maximum admins per collection.
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Unique', 'COLLECTION_ADMINS_LIMIT')
```
---------
### FT_DEFAULT_COLLECTION_LIMITS
Default FT collection limit.
#### Value
```python
{
    'account_token_ownership_limit': 1000000,
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
constant = substrate.get_constant('Unique', 'FT_DEFAULT_COLLECTION_LIMITS')
```
---------
### MAX_COLLECTION_DESCRIPTION_LENGTH
Maximal length of a collection description.
#### Value
```python
256
```
#### Python
```python
constant = substrate.get_constant('Unique', 'MAX_COLLECTION_DESCRIPTION_LENGTH')
```
---------
### MAX_COLLECTION_NAME_LENGTH
Maximal length of a collection name.
#### Value
```python
64
```
#### Python
```python
constant = substrate.get_constant('Unique', 'MAX_COLLECTION_NAME_LENGTH')
```
---------
### MAX_COLLECTION_PROPERTIES_SIZE
Maximum size for all collection properties.
#### Value
```python
40960
```
#### Python
```python
constant = substrate.get_constant('Unique', 'MAX_COLLECTION_PROPERTIES_SIZE')
```
---------
### MAX_PROPERTIES_PER_ITEM
A maximum number of token properties.
#### Value
```python
64
```
#### Python
```python
constant = substrate.get_constant('Unique', 'MAX_PROPERTIES_PER_ITEM')
```
---------
### MAX_PROPERTY_KEY_LENGTH
Maximal length of a property key.
#### Value
```python
256
```
#### Python
```python
constant = substrate.get_constant('Unique', 'MAX_PROPERTY_KEY_LENGTH')
```
---------
### MAX_PROPERTY_VALUE_LENGTH
Maximal length of a property value.
#### Value
```python
32768
```
#### Python
```python
constant = substrate.get_constant('Unique', 'MAX_PROPERTY_VALUE_LENGTH')
```
---------
### MAX_TOKEN_PREFIX_LENGTH
Maximal length of a token prefix.
#### Value
```python
16
```
#### Python
```python
constant = substrate.get_constant('Unique', 'MAX_TOKEN_PREFIX_LENGTH')
```
---------
### MAX_TOKEN_PROPERTIES_SIZE
Maximum size of all token properties.
#### Value
```python
32768
```
#### Python
```python
constant = substrate.get_constant('Unique', 'MAX_TOKEN_PROPERTIES_SIZE')
```
---------
### NESTING_BUDGET
A maximum number of levels of depth in the token nesting tree.
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Unique', 'NESTING_BUDGET')
```
---------
### NFT_DEFAULT_COLLECTION_LIMITS
Default NFT collection limit.
#### Value
```python
{
    'account_token_ownership_limit': 1000000,
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
constant = substrate.get_constant('Unique', 'NFT_DEFAULT_COLLECTION_LIMITS')
```
---------
### RFT_DEFAULT_COLLECTION_LIMITS
Default RFT collection limit.
#### Value
```python
{
    'account_token_ownership_limit': 1000000,
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
constant = substrate.get_constant('Unique', 'RFT_DEFAULT_COLLECTION_LIMITS')
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