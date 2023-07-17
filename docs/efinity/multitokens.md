
# MultiTokens

---------
## Calls

---------
### approve_collection
Approve the `operator` to manage all of `origin`&\#x27;s tokens belonging to `collection_id`.
If an `expiration` is provided, the approval will end when it expires.

\# Errors

- [`Error::CannotApproveSelf`] if `origin == operator`
- [`Error::AlreadyExpired`] if `expiration` is earlier than now
- [`Error::CollectionAccountNotFound`] if the collection account does not exist
- [`Error::MaxApprovalsExceeded`] if approval count has exceeded the maximum
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| operator | `T::AccountId` | 
| expiration | `T::Expiration` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'approve_collection', {
    'collection_id': 'u128',
    'expiration': (None, 'u32'),
    'operator': 'AccountId',
}
)
```

---------
### approve_token
Approve `operator` to transfer up to `amount` of `caller`&\#x27;s balance for `token_id` of
`collection_id`. An `expiration` can be provided. `current_amount` must match the
current approved amount.

\# Errors
- [`Error::CannotApproveSelf`] if `origin == operator`
- [`Error::CollectionAlreadyApproved`] if `collection_id` is already approved
- [`Error::AlreadyExpired`] if `expiration` is earlier than now
- [`Error::TokenAccountNotFound`] if the token account does not exist
- [`Error::MaxApprovalsExceeded`] if approval count has exceeded the maximum
- [`Error::WrongCurrentApprovedAmount`] if `current_amount` does not match the current
  approval amount
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| token_id | `T::TokenId` | 
| operator | `T::AccountId` | 
| amount | `T::TokenBalance` | 
| expiration | `T::Expiration` | 
| current_amount | `T::TokenBalance` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'approve_token', {
    'amount': 'u128',
    'collection_id': 'u128',
    'current_amount': 'u128',
    'expiration': (None, 'u32'),
    'operator': 'AccountId',
    'token_id': 'u128',
}
)
```

---------
### batch_mint
Collection owner mints tokens of `collection_id` to `recipients` consisting of an
[`AccountId`](frame_system::Config::AccountId) and [`MintParams`]. A single mint failure
will fail all of them in the batch.

\# Errors
- [`Error::AmountZero`] if `amount == 0`.
- [`Error::CollectionNotFound`] if `collection` does **not** exist.
- [`Error::NoPermission`] if `caller` is not allowed to mint the `collection`.
- [`Error::TokenMintCapExceeded`] if the mint policy TokenCap does not allow minting
- [`Error::MaxTokenCountExceeded`] if the mint policy max_token_count is exceeded
- [`Error::DepositReserveFailed`] if the issuer does not have sufficent balance for
  token deposit
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| recipients | `MintRecipientsOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'batch_mint', {
    'collection_id': 'u128',
    'recipients': [
        {
            'account_id': 'AccountId',
            'params': {
                'CreateToken': {
                    'attributes': [
                        'scale_info::372',
                    ],
                    'behavior': (
                        None,
                        'scale_info::150',
                    ),
                    'cap': (
                        None,
                        'scale_info::177',
                    ),
                    'foreign_params': (
                        None,
                        'scale_info::383',
                    ),
                    'freeze_state': (
                        None,
                        'scale_info::156',
                    ),
                    'initial_supply': 'u128',
                    'listing_forbidden': 'bool',
                    'sufficiency': {
                        'Insufficient': 'InnerStruct',
                        'Sufficient': 'InnerStruct',
                    },
                    'token_id': 'u128',
                },
                'Mint': {
                    'amount': 'u128',
                    'token_id': 'u128',
                    'unit_price': (
                        None,
                        'u128',
                    ),
                },
            },
        },
    ],
}
)
```

---------
### batch_set_attribute
Collection owner sets `attributes` to `collection_id`

If `token_id` is [`None`], the attribute is added to the collection. If it is [`Some`],
the attribute is added to the token.

\# Errors

- [`Error::InvalidAttributeKey`] if `key.len() == 0`
- [`Error::CollectionNotFound`] if `collection_id` does not exist.
- [`Error::TokenNotFound`] if `token_id` is `Some` and does not exist.
- [`Error::NoPermission`] if `source` account is not the owner of the collection.
- [`Error::DepositReserveFailed`] if unable to reserve the deposit for the attribute
  storage.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| token_id | `Option<T::TokenId>` | 
| attributes | `AttributesOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'batch_set_attribute', {
    'attributes': [
        {
            'key': 'Bytes',
            'value': 'Bytes',
        },
    ],
    'collection_id': 'u128',
    'token_id': (None, 'u128'),
}
)
```

---------
### batch_transfer
Transfers the specific amount of tokens of `collection` to `recipients` from `origin`
account. A single failure will fail all transfers.

\# Errors

- [`Error::AmountZero`] if `amount == 0`.
- [`Error::BalanceLow`] if `source` does not own enough amount of `collection`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| recipients | `TransferRecipientsOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'batch_transfer', {
    'collection_id': 'u128',
    'recipients': [
        {
            'account_id': 'AccountId',
            'params': {
                'Operator': {
                    'amount': 'u128',
                    'keep_alive': 'bool',
                    'source': 'AccountId',
                    'token_id': 'u128',
                },
                'Simple': {
                    'amount': 'u128',
                    'keep_alive': 'bool',
                    'token_id': 'u128',
                },
            },
        },
    ],
}
)
```

---------
### burn
Reduces the balance of `owner` by `amount` of `token_id` from `collection_id`.
It also updates the total supply of `collection_id`.

\# Errors
- [`Error::CollectionNotFound`] if `collection` does not exist.
- [`Error::BalanceLow`] if `owner` account does not has enough amount of any token in
  `tokens` of `collection`.
- [`Error::DepositUnreserveFailed`] if caller does not have enough reserved balance to
  unreserve
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| params | `BurnParamsOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'burn', {
    'collection_id': 'u128',
    'params': {
        'amount': 'u128',
        'keep_alive': 'bool',
        'remove_token_storage': 'bool',
        'token_id': 'u128',
    },
}
)
```

---------
### create_collection
Creates a new [`Collection`](ep_multi_tokens::Collection) from `descriptor`

\# Errors

- [`Error::DepositReserveFailed`] if the deposit cannot be reserved
#### Attributes
| Name | Type |
| -------- | -------- | 
| descriptor | `T::CollectionDescriptor` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'create_collection', {
    'descriptor': {
        'attributes': [
            {
                'key': 'Bytes',
                'value': 'Bytes',
            },
        ],
        'explicit_royalty_currencies': [
            {
                'collection_id': 'u128',
                'token_id': 'u128',
            },
        ],
        'policy': {
            'attribute': {},
            'burn': {},
            'market': {
                'royalty': (
                    None,
                    {
                        'beneficiary': 'AccountId',
                        'percentage': 'u32',
                    },
                ),
            },
            'mint': {
                'force_single_mint': 'bool',
                'max_token_count': (
                    None,
                    'u64',
                ),
                'max_token_supply': (
                    None,
                    'u128',
                ),
            },
            'transfer': {},
        },
    },
}
)
```

---------
### destroy_collection
Destroys [`Collection`](ep_multi_tokens::Collection) with `id`. `origin` must be the
owner of the [`Collection`](ep_multi_tokens::Collection).

\# Errors

- [`Error::NoPermission`] if `origin` is not the owner of the collection.
- [`Error::CollectionNotFound`] if `Collection` with `id` does not exist.
- [`Error::DestroyForbiddenByCollectionEvent`] if another pallet is blocking the
  collection&\#x27;s destruction
- [`Error::DestroyForbiddenByRemainingTokens`] if collection still has tokens when
  destroying
- [`Error::DestroyForbiddenByAttributeCount`] if collection still has attributes when
  destroying
current number of collection attributes.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'destroy_collection', {'collection_id': 'u128'}
)
```

---------
### force_create_collection
Creates a new collection from `descriptor` at `collection_id`, origin must be root

\# Errors
- [`Error::DepositReserveFailed`] if the deposit cannot be reserved
- [`Error::CollectionIdAlreadyInUse`] if the collection id is already in use
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner | `T::AccountId` | 
| collection_id | `T::CollectionId` | 
| descriptor | `T::CollectionDescriptor` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'force_create_collection', {
    'collection_id': 'u128',
    'descriptor': {
        'attributes': [
            {
                'key': 'Bytes',
                'value': 'Bytes',
            },
        ],
        'explicit_royalty_currencies': [
            {
                'collection_id': 'u128',
                'token_id': 'u128',
            },
        ],
        'policy': {
            'attribute': {},
            'burn': {},
            'market': {
                'royalty': (
                    None,
                    {
                        'beneficiary': 'AccountId',
                        'percentage': 'u32',
                    },
                ),
            },
            'mint': {
                'force_single_mint': 'bool',
                'max_token_count': (
                    None,
                    'u64',
                ),
                'max_token_supply': (
                    None,
                    'u128',
                ),
            },
            'transfer': {},
        },
    },
    'owner': 'AccountId',
}
)
```

---------
### force_mutate_collection
Exactly as [`mutate_collection`](Self::mutate_collection), except the origin must be
root and the `caller` account should be specified.

\# Errors

Same as [`mutate_collection`](Self::mutate_collection)
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| mutation | `T::CollectionMutation` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'force_mutate_collection', {
    'collection_id': 'u128',
    'mutation': {
        'explicit_royalty_currencies': (
            None,
            [
                {
                    'collection_id': 'u128',
                    'token_id': 'u128',
                },
            ],
        ),
        'owner': (None, 'AccountId'),
        'royalty': {
            'NoMutation': None,
            'SomeMutation': (
                None,
                {
                    'beneficiary': 'AccountId',
                    'percentage': 'u32',
                },
            ),
        },
    },
}
)
```

---------
### force_set_attribute
Set the Tokens storage to the given `value`, origin must be root
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| token_id | `Option<T::TokenId>` | 
| key | `T::AttributeKey` | 
| value | `Option<AttributeOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'force_set_attribute', {
    'collection_id': 'u128',
    'key': 'Bytes',
    'token_id': (None, 'u128'),
    'value': (
        None,
        {
            'deposit': 'u128',
            'value': 'Bytes',
        },
    ),
}
)
```

---------
### force_set_collection
Set the Collections storage to the given `value`, origin must be root
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| value | `Option<CollectionOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'force_set_collection', {
    'collection_id': 'u128',
    'value': (
        None,
        {
            'attribute_count': 'u32',
            'explicit_royalty_currencies': 'scale_info::171',
            'owner': 'AccountId',
            'policy': {
                'attribute': {},
                'burn': {},
                'market': {
                    'royalty': (
                        None,
                        {
                            'beneficiary': 'AccountId',
                            'percentage': 'u32',
                        },
                    ),
                },
                'mint': {
                    'force_single_mint': 'bool',
                    'max_token_count': (
                        None,
                        'u64',
                    ),
                    'max_token_supply': (
                        None,
                        'u128',
                    ),
                },
                'transfer': {
                    'is_frozen': 'bool',
                },
            },
            'token_count': 'u64',
            'total_deposit': 'u128',
        },
    ),
}
)
```

---------
### force_set_collection_account
Set the CollectionAccounts storage to the given `value`, origin must be root
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| account_id | `<T::Lookup as StaticLookup>::Source` | 
| value | `Option<CollectionAccountOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'force_set_collection_account', {
    'account_id': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'collection_id': 'u128',
    'value': (
        None,
        {
            'account_count': 'u32',
            'approvals': 'scale_info::183',
            'is_frozen': 'bool',
        },
    ),
}
)
```

---------
### force_set_token
Set the Tokens storage to the given `value`, origin must be root
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| token_id | `T::TokenId` | 
| value | `Option<TokenOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'force_set_token', {
    'collection_id': 'u128',
    'token_id': 'u128',
    'value': (
        None,
        {
            'attribute_count': 'u32',
            'cap': (
                None,
                {
                    'CollapsingSupply': 'u128',
                    'SingleMint': None,
                    'Supply': 'u128',
                },
            ),
            'freeze_state': (
                None,
                (
                    'Permanent',
                    'Temporary',
                    'Never',
                ),
            ),
            'listing_forbidden': 'bool',
            'market_behavior': (
                None,
                {
                    'HasRoyalty': {
                        'beneficiary': 'AccountId',
                        'percentage': 'u32',
                    },
                    'IsCurrency': None,
                },
            ),
            'metadata': {
                'Foreign': {
                    'decimal_count': 'u32',
                    'location': (
                        None,
                        {
                            'interior': 'scale_info::68',
                            'parents': 'u8',
                        },
                    ),
                    'name': 'Bytes',
                    'preminted_supply': 'u128',
                    'symbol': 'Bytes',
                    'units_per_second': (
                        None,
                        'u128',
                    ),
                },
                'Native': None,
            },
            'minimum_balance': 'u128',
            'mint_deposit': 'u128',
            'sufficiency': {
                'Insufficient': {
                    'unit_price': 'u128',
                },
                'Sufficient': None,
            },
            'supply': 'u128',
        },
    ),
}
)
```

---------
### force_set_token_account
Set the TokenAccounts storage to the given `value`, origin must be root
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| token_id | `T::TokenId` | 
| account_id | `<T::Lookup as StaticLookup>::Source` | 
| value | `Option<TokenAccountOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'force_set_token_account', {
    'account_id': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'collection_id': 'u128',
    'token_id': 'u128',
    'value': (
        None,
        {
            'approvals': 'scale_info::197',
            'balance': 'u128',
            'is_frozen': 'bool',
            'locked_balance': 'u128',
            'locks': 'scale_info::192',
            'named_reserves': 'scale_info::192',
            'reserved_balance': 'u128',
        },
    ),
}
)
```

---------
### force_transfer
Exactly as [`transfer`](Self::transfer), except the origin must be root and the source
account should be specified.

\# Errors

Same as [`transfer`](Self::transfer)
#### Attributes
| Name | Type |
| -------- | -------- | 
| source | `<T::Lookup as StaticLookup>::Source` | 
| destination | `<T::Lookup as StaticLookup>::Source` | 
| collection_id | `T::CollectionId` | 
| params | `TransferParamsOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'force_transfer', {
    'collection_id': 'u128',
    'destination': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'params': {
        'Operator': {
            'amount': 'u128',
            'keep_alive': 'bool',
            'source': 'AccountId',
            'token_id': 'u128',
        },
        'Simple': {
            'amount': 'u128',
            'keep_alive': 'bool',
            'token_id': 'u128',
        },
    },
    'source': {
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
Freeze collection, token or account
#### Attributes
| Name | Type |
| -------- | -------- | 
| info | `FreezeOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'freeze', {
    'info': {
        'collection_id': 'u128',
        'freeze_type': {
            'Collection': None,
            'CollectionAccount': 'AccountId',
            'Token': {
                'freeze_state': (
                    None,
                    (
                        'Permanent',
                        'Temporary',
                        'Never',
                    ),
                ),
                'token_id': 'u128',
            },
            'TokenAccount': {
                'account_id': 'AccountId',
                'token_id': 'u128',
            },
        },
    },
}
)
```

---------
### mint
`origin` mints to `recipient` for `collection_id` with `params` using the pallet&\#x27;s
[`MintPolicy`](traits::CollectionPolicy::Mint).

\# Errors

- [`Error::AmountZero`] if `amount == 0`.
- [`Error::CollectionNotFound`] if `Collection` does not exist.
- [`Error::TokenNotFound`] if `Token` does not exist.
- [`Error::TokenAlreadyExists`] if attempting to create a token that already exists
- [`Error::NoPermission`] if `caller` is not allowed to mint the `collection`.
- [`Error::TokenMintCapExceeded`] if the mint policy TokenCap does not allow minting
- `MaxTokenCountExceeded` if the mint policy max_token_count is exceeded
- [`Error::DepositReserveFailed`] if the issuer does not have sufficent balance for
  token deposit
- [`Error::ConflictingLocation`] if the token is foreign and the location is already
  mapped to another asset in `AssetIdsByLocation`
#### Attributes
| Name | Type |
| -------- | -------- | 
| recipient | `<T::Lookup as StaticLookup>::Source` | 
| collection_id | `T::CollectionId` | 
| params | `MintParamsOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'mint', {
    'collection_id': 'u128',
    'params': {
        'CreateToken': {
            'attributes': [
                {
                    'key': 'Bytes',
                    'value': 'Bytes',
                },
            ],
            'behavior': (
                None,
                {
                    'HasRoyalty': {
                        'beneficiary': 'AccountId',
                        'percentage': 'u32',
                    },
                    'IsCurrency': None,
                },
            ),
            'cap': (
                None,
                {
                    'CollapsingSupply': 'u128',
                    'SingleMint': None,
                    'Supply': 'u128',
                },
            ),
            'foreign_params': (
                None,
                {
                    'decimal_count': 'u32',
                    'location': (
                        None,
                        {
                            'interior': 'scale_info::68',
                            'parents': 'u8',
                        },
                    ),
                    'name': 'Bytes',
                    'symbol': 'Bytes',
                    'units_per_second': (
                        None,
                        'u128',
                    ),
                },
            ),
            'freeze_state': (
                None,
                (
                    'Permanent',
                    'Temporary',
                    'Never',
                ),
            ),
            'initial_supply': 'u128',
            'listing_forbidden': 'bool',
            'sufficiency': {
                'Insufficient': {
                    'unit_price': (
                        None,
                        'u128',
                    ),
                },
                'Sufficient': {
                    'minimum_balance': 'u128',
                },
            },
            'token_id': 'u128',
        },
        'Mint': {
            'amount': 'u128',
            'token_id': 'u128',
            'unit_price': (
                None,
                'u128',
            ),
        },
    },
    'recipient': {
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
### mutate_collection
Modify [`Collection`](ep_multi_tokens::Collection) with `id` by applying `mutation`

\# Errors

- [`Error::CollectionNotFound`] if `collection_id` does not exist.
- [`Error::NoPermission`] if `origin` is not the owner of `collection`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| mutation | `T::CollectionMutation` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'mutate_collection', {
    'collection_id': 'u128',
    'mutation': {
        'explicit_royalty_currencies': (
            None,
            [
                {
                    'collection_id': 'u128',
                    'token_id': 'u128',
                },
            ],
        ),
        'owner': (None, 'AccountId'),
        'royalty': {
            'NoMutation': None,
            'SomeMutation': (
                None,
                {
                    'beneficiary': 'AccountId',
                    'percentage': 'u32',
                },
            ),
        },
    },
}
)
```

---------
### mutate_token
Modify [`Token`](ep_multi_tokens::Token) with `token_id`  from
[`Collection`](ep_multi_tokens::Collection) with `collection_id` by applying `mutation`

\# Errors

- [`Error::CurrencyIncompatibleWithCollectionRoyalty`] if token has already been
  assigned a royalty
- [`Error::NoPermission`] if not the collection owner
- [`Error::TokenNotFound`] if Token does not exist
- [`Error::ConflictingLocation`] if the new location is already occupied
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| token_id | `T::TokenId` | 
| mutation | `T::TokenMutation` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'mutate_token', {
    'collection_id': 'u128',
    'mutation': {
        'behavior': {
            'NoMutation': None,
            'SomeMutation': (
                None,
                {
                    'HasRoyalty': {
                        'beneficiary': 'AccountId',
                        'percentage': 'u32',
                    },
                    'IsCurrency': None,
                },
            ),
        },
        'listing_forbidden': {
            'NoMutation': None,
            'SomeMutation': 'bool',
        },
        'metadata': {
            'NoMutation': None,
            'SomeMutation': {
                'Foreign': {
                    'decimal_count': 'u32',
                    'location': (
                        None,
                        {
                            'interior': 'scale_info::68',
                            'parents': 'u8',
                        },
                    ),
                    'name': 'Bytes',
                    'preminted_supply': 'u128',
                    'symbol': 'Bytes',
                    'units_per_second': (
                        None,
                        'u128',
                    ),
                },
                'Native': None,
            },
        },
    },
    'token_id': 'u128',
}
)
```

---------
### remove_all_attributes
Removes all attributes from the given `collection_id` or `token_id`.

\# Errors
- `InvalidAttributeCount` if `attribute_count` doesn&\#x27;t match the number of attributes
- [`Error::CollectionNotFound`] if Collection with `collection_id` does not exist.
- [`Error::TokenNotFound`] if Token with `token_id` does not exist.
- [`Error::NoPermission`] if `origin` account is not the owner of the Collection or
  Token
- other errors from `remove_attribute`
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| token_id | `Option<T::TokenId>` | 
| attribute_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'remove_all_attributes', {
    'attribute_count': 'u32',
    'collection_id': 'u128',
    'token_id': (None, 'u128'),
}
)
```

---------
### remove_attribute
Removes the `key` attribute from the given `collection_id` or `token_id`.

\# Errors
- [`Error::InvalidAttributeKey`] if `key.len() == 0`
- [`Error::CollectionNotFound`] if `collection_id` does not exist.
- [`Error::TokenNotFound`] if `token_id` is `Some` and does not exist.
- [`Error::NoPermission`] if `caller` is not the owner of the collection.
- `Underflow` if an attribute counter underflows
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| token_id | `Option<T::TokenId>` | 
| key | `T::AttributeKey` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'remove_attribute', {
    'collection_id': 'u128',
    'key': 'Bytes',
    'token_id': (None, 'u128'),
}
)
```

---------
### set_attribute
Sets the attribute `key` to `value` for `collection_id`.
If `token_id` is [`None`], the attribute is added to the collection. If it is [`Some`],
the attribute is added to the token.

\# Errors
- [`Error::InvalidAttributeKey`] if `key.len() == 0`
- [`Error::CollectionNotFound`] if `collection_id` does not exist.
- [`Error::TokenNotFound`] if `token_id` is `Some` and does not exist.
- [`Error::NoPermission`] if `source` account is not the owner of the collection.
- [`Error::DepositReserveFailed`] if unable to reserve the deposit for the attribute
  storage.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| token_id | `Option<T::TokenId>` | 
| key | `T::AttributeKey` | 
| value | `T::AttributeValue` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'set_attribute', {
    'collection_id': 'u128',
    'key': 'Bytes',
    'token_id': (None, 'u128'),
    'value': 'Bytes',
}
)
```

---------
### thaw
Thaw collection, token or account
#### Attributes
| Name | Type |
| -------- | -------- | 
| info | `FreezeOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'thaw', {
    'info': {
        'collection_id': 'u128',
        'freeze_type': {
            'Collection': None,
            'CollectionAccount': 'AccountId',
            'Token': {
                'freeze_state': (
                    None,
                    (
                        'Permanent',
                        'Temporary',
                        'Never',
                    ),
                ),
                'token_id': 'u128',
            },
            'TokenAccount': {
                'account_id': 'AccountId',
                'token_id': 'u128',
            },
        },
    },
}
)
```

---------
### transfer
`operator` transfers to `recipient` for `collection_id` with `params`

\# Errors

- [`Error::AmountZero`] if `amount == 0`.
- [`Error::BalanceLow`] if `source` does not own enough amount of `collection`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| recipient | `<T::Lookup as StaticLookup>::Source` | 
| collection_id | `T::CollectionId` | 
| params | `TransferParamsOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'transfer', {
    'collection_id': 'u128',
    'params': {
        'Operator': {
            'amount': 'u128',
            'keep_alive': 'bool',
            'source': 'AccountId',
            'token_id': 'u128',
        },
        'Simple': {
            'amount': 'u128',
            'keep_alive': 'bool',
            'token_id': 'u128',
        },
    },
    'recipient': {
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
### unapprove_collection
Unapprove the `operator` to manage all of `origin`&\#x27;s tokens belonging to `collection`

\# Errors

- [`Error::CollectionAccountNotFound`] if the collection account cannot be found
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| operator | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'unapprove_collection', {
    'collection_id': 'u128',
    'operator': 'AccountId',
}
)
```

---------
### unapprove_token
Unapprove `operator` to transfer `origin`&\#x27;s `token_id` of `collection_id`

\# Errors

- [`Error::TokenAccountNotFound`] if the token account does not exist
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `T::CollectionId` | 
| token_id | `T::TokenId` | 
| operator | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'MultiTokens', 'unapprove_token', {
    'collection_id': 'u128',
    'operator': 'AccountId',
    'token_id': 'u128',
}
)
```

---------
## Events

---------
### Approved
An approval took place. If `token_id` is [`None`], it applies to the whole collection.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `Option<T::TokenId>` | ```(None, 'u128')```
| owner | `T::AccountId` | ```AccountId```
| operator | `T::AccountId` | ```AccountId```
| amount | `Option<T::TokenBalance>` | ```(None, 'u128')```
| expiration | `T::Expiration` | ```(None, 'u32')```

---------
### AttributeRemoved
An attribute has been removed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `Option<T::TokenId>` | ```(None, 'u128')```
| key | `T::AttributeKey` | ```Bytes```

---------
### AttributeSet
New attribute has been set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `Option<T::TokenId>` | ```(None, 'u128')```
| key | `T::AttributeKey` | ```Bytes```
| value | `T::AttributeValue` | ```Bytes```

---------
### BalanceSet
The balance of an account was set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `T::TokenId` | ```u128```
| account_id | `T::AccountId` | ```AccountId```
| balance | `T::TokenBalance` | ```u128```
| reserved_balance | `T::TokenBalance` | ```u128```

---------
### Burned
Units of a [`Token`](ep_multi_tokens::Token) were burned
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `T::TokenId` | ```u128```
| account_id | `T::AccountId` | ```AccountId```
| amount | `T::TokenBalance` | ```u128```

---------
### CollectionAccountCreated
A new [`CollectionAccount`] was created
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| account_id | `T::AccountId` | ```AccountId```

---------
### CollectionAccountDestroyed
A [`CollectionAccount`] was destroyed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| account_id | `T::AccountId` | ```AccountId```

---------
### CollectionAccountUpdated
TokenAccount storage was set to `value`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| account_id | `T::AccountId` | ```AccountId```
| value | `Option<CollectionAccountOf<T>>` | ```(None, {'is_frozen': 'bool', 'approvals': 'scale_info::183', 'account_count': 'u32'})```

---------
### CollectionCreated
A new [`Collection`](ep_multi_tokens::Collection) was created
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| owner | `T::AccountId` | ```AccountId```

---------
### CollectionDestroyed
A [`Collection`](ep_multi_tokens::Collection) was destroyed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| caller | `T::AccountId` | ```AccountId```

---------
### CollectionMutated
A [`Collection`](ep_multi_tokens::Collection) was mutated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| mutation | `T::CollectionMutation` | ```{'owner': (None, 'AccountId'), 'royalty': {'NoMutation': None, 'SomeMutation': (None, {'beneficiary': 'AccountId', 'percentage': 'u32'})}, 'explicit_royalty_currencies': (None, [{'collection_id': 'u128', 'token_id': 'u128'}])}```

---------
### CollectionUpdated
Collection storage was set to `value`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| value | `Option<CollectionOf<T>>` | ```(None, {'owner': 'AccountId', 'policy': {'mint': {'max_token_count': (None, 'u64'), 'max_token_supply': (None, 'u128'), 'force_single_mint': 'bool'}, 'burn': {}, 'transfer': {'is_frozen': 'bool'}, 'attribute': {}, 'market': {'royalty': (None, 'scale_info::129')}}, 'token_count': 'u64', 'attribute_count': 'u32', 'total_deposit': 'u128', 'explicit_royalty_currencies': 'scale_info::171'})```

---------
### Deposit
Token units were deposited
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `T::TokenId` | ```u128```
| account_id | `T::AccountId` | ```AccountId```
| amount | `T::TokenBalance` | ```u128```

---------
### Frozen
Collection, token or account was frozen
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `FreezeOf<T>` | ```{'collection_id': 'u128', 'freeze_type': {'Collection': None, 'Token': {'token_id': 'u128', 'freeze_state': (None, ('Permanent', 'Temporary', 'Never'))}, 'CollectionAccount': 'AccountId', 'TokenAccount': {'token_id': 'u128', 'account_id': 'AccountId'}}}```

---------
### MigrationStatusUpdated
Migration stage updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| stage | `MigrationStage` | ```('NotStarted', 'InProgress', 'Completed', 'Failed')```

---------
### Minted
Units of a [`Token`](ep_multi_tokens::Token) were minted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `T::TokenId` | ```u128```
| issuer | `RootOrSigned<T::AccountId>` | ```{'Root': None, 'Signed': 'AccountId'}```
| recipient | `T::AccountId` | ```AccountId```
| amount | `T::TokenBalance` | ```u128```

---------
### MovedReserves
Reserved token units were moved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `T::TokenId` | ```u128```
| source | `T::AccountId` | ```AccountId```
| destination | `T::AccountId` | ```AccountId```
| amount | `T::TokenBalance` | ```u128```
| reserve_id | `Option<T::ReserveIdentifierType>` | ```(None, '[u8; 8]')```

---------
### NextCollectionIdUpdated
NextCollectionId storage was set to `collection_id`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```

---------
### ReserveRepatriated
Reserved token units were transferred
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `T::TokenId` | ```u128```
| source | `T::AccountId` | ```AccountId```
| destination | `T::AccountId` | ```AccountId```
| amount | `T::TokenBalance` | ```u128```
| reserve_id | `Option<T::ReserveIdentifierType>` | ```(None, '[u8; 8]')```

---------
### Reserved
Token units were reserved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `T::TokenId` | ```u128```
| account_id | `T::AccountId` | ```AccountId```
| amount | `T::TokenBalance` | ```u128```
| reserve_id | `Option<T::ReserveIdentifierType>` | ```(None, '[u8; 8]')```

---------
### Slashed
An amount of tokens were slashed from account
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `T::TokenId` | ```u128```
| account_id | `T::AccountId` | ```AccountId```
| amount | `T::TokenBalance` | ```u128```

---------
### Thawed
Collection, token or account was unfrozen
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `FreezeOf<T>` | ```{'collection_id': 'u128', 'freeze_type': {'Collection': None, 'Token': {'token_id': 'u128', 'freeze_state': (None, ('Permanent', 'Temporary', 'Never'))}, 'CollectionAccount': 'AccountId', 'TokenAccount': {'token_id': 'u128', 'account_id': 'AccountId'}}}```

---------
### TokenAccountCreated
A new [`TokenAccount`] was created
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `T::TokenId` | ```u128```
| account_id | `T::AccountId` | ```AccountId```
| balance | `T::TokenBalance` | ```u128```

---------
### TokenAccountDestroyed
A [`TokenAccount`] was destroyed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `T::TokenId` | ```u128```
| account_id | `T::AccountId` | ```AccountId```

---------
### TokenAccountUpdated
TokenAccount storage was set to `value`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `T::TokenId` | ```u128```
| account_id | `T::AccountId` | ```AccountId```
| value | `Option<TokenAccountOf<T>>` | ```(None, {'balance': 'u128', 'reserved_balance': 'u128', 'locked_balance': 'u128', 'named_reserves': 'scale_info::192', 'locks': 'scale_info::192', 'approvals': 'scale_info::197', 'is_frozen': 'bool'})```

---------
### TokenCreated
A [`Token`](ep_multi_tokens::Token) was created
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `T::TokenId` | ```u128```
| issuer | `RootOrSigned<T::AccountId>` | ```{'Root': None, 'Signed': 'AccountId'}```
| initial_supply | `T::TokenBalance` | ```u128```

---------
### TokenDestroyed
A [`Token`](ep_multi_tokens::Token) was destroyed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `T::TokenId` | ```u128```
| caller | `T::AccountId` | ```AccountId```

---------
### TokenMutated
A [`Token`](ep_multi_tokens::Token) was mutated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `T::TokenId` | ```u128```
| mutation | `T::TokenMutation` | ```{'behavior': {'NoMutation': None, 'SomeMutation': (None, {'HasRoyalty': {'beneficiary': 'AccountId', 'percentage': 'u32'}, 'IsCurrency': None})}, 'listing_forbidden': {'NoMutation': None, 'SomeMutation': 'bool'}, 'metadata': {'NoMutation': None, 'SomeMutation': {'Native': None, 'Foreign': {'decimal_count': 'u32', 'name': 'Bytes', 'symbol': 'Bytes', 'location': (None, 'scale_info::67'), 'units_per_second': (None, 'u128'), 'preminted_supply': 'u128'}}}}```

---------
### TokenUpdated
Token storage was set to `value`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `T::TokenId` | ```u128```
| value | `Option<TokenOf<T>>` | ```(None, {'supply': 'u128', 'cap': (None, {'SingleMint': None, 'Supply': 'u128', 'CollapsingSupply': 'u128'}), 'freeze_state': (None, ('Permanent', 'Temporary', 'Never')), 'minimum_balance': 'u128', 'sufficiency': {'Sufficient': None, 'Insufficient': {'unit_price': 'u128'}}, 'mint_deposit': 'u128', 'attribute_count': 'u32', 'market_behavior': (None, {'HasRoyalty': {'beneficiary': 'AccountId', 'percentage': 'u32'}, 'IsCurrency': None}), 'listing_forbidden': 'bool', 'metadata': {'Native': None, 'Foreign': {'decimal_count': 'u32', 'name': 'Bytes', 'symbol': 'Bytes', 'location': (None, 'scale_info::67'), 'units_per_second': (None, 'u128'), 'preminted_supply': 'u128'}}})```

---------
### Transferred
Units of a [`Token`](ep_multi_tokens::Token) were transferred
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `T::TokenId` | ```u128```
| operator | `T::AccountId` | ```AccountId```
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `T::TokenBalance` | ```u128```

---------
### Unapproved
An unapproval took place. If `token_id` is [`None`], it applies to the collection.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `Option<T::TokenId>` | ```(None, 'u128')```
| owner | `T::AccountId` | ```AccountId```
| operator | `T::AccountId` | ```AccountId```

---------
### Unreserved
Token units were unreserved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `T::TokenId` | ```u128```
| account_id | `T::AccountId` | ```AccountId```
| amount | `T::TokenBalance` | ```u128```
| reserve_id | `Option<T::ReserveIdentifierType>` | ```(None, '[u8; 8]')```

---------
### Withdraw
Token units were withdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `T::CollectionId` | ```u128```
| token_id | `T::TokenId` | ```u128```
| account_id | `T::AccountId` | ```AccountId```
| amount | `T::TokenBalance` | ```u128```

---------
## Storage functions

---------
### AssetIdsByLocation
 Map of Locations to AssetIds of Foreign Tokens

#### Python
```python
result = substrate.query(
    'MultiTokens', 'AssetIdsByLocation', [
    {
        'interior': {
            'Here': None,
            'X1': {
                'AccountId32': {
                    'id': '[u8; 32]',
                    'network': (
                        None,
                        {
                            'BitcoinCash': None,
                            'BitcoinCore': None,
                            'ByFork': 'InnerStruct',
                            'ByGenesis': '[u8; 32]',
                            'Ethereum': 'InnerStruct',
                            'Kusama': None,
                            'Polkadot': None,
                            'Rococo': None,
                            'Westend': None,
                            'Wococo': None,
                        },
                    ),
                },
                'AccountIndex64': {
                    'index': 'u64',
                    'network': (
                        None,
                        {
                            'BitcoinCash': None,
                            'BitcoinCore': None,
                            'ByFork': 'InnerStruct',
                            'ByGenesis': '[u8; 32]',
                            'Ethereum': 'InnerStruct',
                            'Kusama': None,
                            'Polkadot': None,
                            'Rococo': None,
                            'Westend': None,
                            'Wococo': None,
                        },
                    ),
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': (
                        None,
                        {
                            'BitcoinCash': None,
                            'BitcoinCore': None,
                            'ByFork': 'InnerStruct',
                            'ByGenesis': '[u8; 32]',
                            'Ethereum': 'InnerStruct',
                            'Kusama': None,
                            'Polkadot': None,
                            'Rococo': None,
                            'Westend': None,
                            'Wococo': None,
                        },
                    ),
                },
                'GeneralIndex': 'u128',
                'GeneralKey': {
                    'data': '[u8; 32]',
                    'length': 'u8',
                },
                'GlobalConsensus': {
                    'BitcoinCash': None,
                    'BitcoinCore': None,
                    'ByFork': {
                        'block_hash': '[u8; 32]',
                        'block_number': 'u64',
                    },
                    'ByGenesis': '[u8; 32]',
                    'Ethereum': {
                        'chain_id': 'u64',
                    },
                    'Kusama': None,
                    'Polkadot': None,
                    'Rococo': None,
                    'Westend': None,
                    'Wococo': None,
                },
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': {
                        'Administration': None,
                        'Defense': None,
                        'Executive': None,
                        'Index': 'u32',
                        'Judicial': None,
                        'Legislative': None,
                        'Moniker': '[u8; 4]',
                        'Technical': None,
                        'Treasury': None,
                        'Unit': None,
                    },
                    'part': {
                        'AtLeastProportion': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Fraction': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Members': {
                            'count': 'u32',
                        },
                        'MoreThanProportion': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Voice': None,
                    },
                },
            },
            'X2': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
            'X3': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
            'X4': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
            'X5': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
            'X6': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
            'X7': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
            'X8': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': (
                            None,
                            'scale_info::72',
                        ),
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': {
                        'data': '[u8; 32]',
                        'length': 'u8',
                    },
                    'GlobalConsensus': {
                        'BitcoinCash': None,
                        'BitcoinCore': None,
                        'ByFork': {
                            'block_hash': '[u8; 32]',
                            'block_number': 'u64',
                        },
                        'ByGenesis': '[u8; 32]',
                        'Ethereum': {
                            'chain_id': 'u64',
                        },
                        'Kusama': None,
                        'Polkadot': None,
                        'Rococo': None,
                        'Westend': None,
                        'Wococo': None,
                    },
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Administration': None,
                            'Defense': None,
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Moniker': '[u8; 4]',
                            'Technical': None,
                            'Treasury': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
        },
        'parents': 'u8',
    },
]
)
```

#### Return value
```python
{'collection_id': 'u128', 'token_id': 'u128'}
```
---------
### Attributes
 Metadata of collections and tokens.

#### Python
```python
result = substrate.query(
    'MultiTokens', 'Attributes', ['u128', (None, 'u128'), 'Bytes']
)
```

#### Return value
```python
{'deposit': 'u128', 'value': 'Bytes'}
```
---------
### CollectionAccounts
 Stores information for an account per collection

#### Python
```python
result = substrate.query(
    'MultiTokens', 'CollectionAccounts', ['u128', 'AccountId']
)
```

#### Return value
```python
{'account_count': 'u32', 'approvals': 'scale_info::183', 'is_frozen': 'bool'}
```
---------
### Collections
 The collections in existence and their ownership details.

#### Python
```python
result = substrate.query(
    'MultiTokens', 'Collections', ['u128']
)
```

#### Return value
```python
{
    'attribute_count': 'u32',
    'explicit_royalty_currencies': 'scale_info::171',
    'owner': 'AccountId',
    'policy': {
        'attribute': {},
        'burn': {},
        'market': {
            'royalty': (
                None,
                {'beneficiary': 'AccountId', 'percentage': 'u32'},
            ),
        },
        'mint': {
            'force_single_mint': 'bool',
            'max_token_count': (None, 'u64'),
            'max_token_supply': (None, 'u128'),
        },
        'transfer': {'is_frozen': 'bool'},
    },
    'token_count': 'u64',
    'total_deposit': 'u128',
}
```
---------
### IdleOperations
 Pending operations to be executed on [`Hooks::on_idle`].

#### Python
```python
result = substrate.query(
    'MultiTokens', 'IdleOperations', []
)
```

#### Return value
```python
[
    {
        'estimated_weight': {'proof_size': 'u64', 'ref_time': 'u64'},
        'operation': {
            'DeleteAttributes': {
                'attribute_count': 'u32',
                'collection_id': 'u128',
                'token_id': (None, 'u128'),
            },
        },
    },
]
```
---------
### MigrationStatus
 Status of the current multi-block migration

#### Python
```python
result = substrate.query(
    'MultiTokens', 'MigrationStatus', []
)
```

#### Return value
```python
('NotStarted', 'InProgress', 'Completed', 'Failed')
```
---------
### Migrations
 Stores last iterated keys for migrations. Used by multi block migrations
 to resume from the last iterated key.

 Key is the storage prefix, value is the status of migration and last iterated key, if any.
 i.e `[&quot;MultiTokens&quot;, &quot;TokenAccounts&quot;] -&gt; (collection_id, token_id, account_id)`

#### Python
```python
result = substrate.query(
    'MultiTokens', 'Migrations', ['Bytes']
)
```

#### Return value
```python
{
    'last_iterated_key': (None, 'Bytes'),
    'stage': ('NotStarted', 'InProgress', 'Completed', 'Failed'),
}
```
---------
### NextCollectionId
 Sequencer for collectionID generators.

#### Python
```python
result = substrate.query(
    'MultiTokens', 'NextCollectionId', []
)
```

#### Return value
```python
'u128'
```
---------
### TokenAccounts
 Accounts per token

#### Python
```python
result = substrate.query(
    'MultiTokens', 'TokenAccounts', ['u128', 'u128', 'AccountId']
)
```

#### Return value
```python
{
    'approvals': 'scale_info::197',
    'balance': 'u128',
    'is_frozen': 'bool',
    'locked_balance': 'u128',
    'locks': 'scale_info::192',
    'named_reserves': 'scale_info::192',
    'reserved_balance': 'u128',
}
```
---------
### Tokens
 Tokens storage

#### Python
```python
result = substrate.query(
    'MultiTokens', 'Tokens', ['u128', 'u128']
)
```

#### Return value
```python
{
    'attribute_count': 'u32',
    'cap': (
        None,
        {'CollapsingSupply': 'u128', 'SingleMint': None, 'Supply': 'u128'},
    ),
    'freeze_state': (None, ('Permanent', 'Temporary', 'Never')),
    'listing_forbidden': 'bool',
    'market_behavior': (
        None,
        {'HasRoyalty': {'beneficiary': 'AccountId', 'percentage': 'u32'}, 'IsCurrency': None},
    ),
    'metadata': {
        'Foreign': {
            'decimal_count': 'u32',
            'location': (None, {'interior': 'scale_info::68', 'parents': 'u8'}),
            'name': 'Bytes',
            'preminted_supply': 'u128',
            'symbol': 'Bytes',
            'units_per_second': (None, 'u128'),
        },
        'Native': None,
    },
    'minimum_balance': 'u128',
    'mint_deposit': 'u128',
    'sufficiency': {'Insufficient': {'unit_price': 'u128'}, 'Sufficient': None},
    'supply': 'u128',
}
```
---------
## Constants

---------
### AttributeDepositBase
 The base deposit required for setting an attribute
#### Value
```python
200000000000000000
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'AttributeDepositBase')
```
---------
### AttributeDepositPerByte
 Additional deposit per byte for setting an attribute
#### Value
```python
100000000000000
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'AttributeDepositPerByte')
```
---------
### CollectionCreationDeposit
 Amount of [`Balance`](BalanceOf) reserved to create a collection
#### Value
```python
25000000000000000000
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'CollectionCreationDeposit')
```
---------
### MaxBatchAttributesPerCall
 The max number of attributes to set in one call
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'MaxBatchAttributesPerCall')
```
---------
### MaxExplicitRoyaltyCurrencies
 The maximum number of explicit royalty currencies
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'MaxExplicitRoyaltyCurrencies')
```
---------
### MaxIdleOperationQueueLength
 The maximum length of the idle operation queue
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'MaxIdleOperationQueueLength')
```
---------
### MaxIdleOperationQueueWeight
 The maximum weight of the idle operation queue
#### Value
```python
{'proof_size': 0, 'ref_time': 100000000000}
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'MaxIdleOperationQueueWeight')
```
---------
### MaxLocks
 The maximum number of locks that can exist on a token account
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'MaxLocks')
```
---------
### MaxMigrationExtrinsicInfosToPause
 Bound for the number of extrinsics to pause during multi block migration
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'MaxMigrationExtrinsicInfosToPause')
```
---------
### MaxMigrationKeyLength
 Max length for the [`Migrations`] storage
#### Value
```python
1024
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'MaxMigrationKeyLength')
```
---------
### MaxOperatorsPerAccount
 The max number of operators a [`TokenAccount`] and an [`CollectionAccount`] can have
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'MaxOperatorsPerAccount')
```
---------
### MaxRecipientsPerBatchMint
 The max number of recipients allowed in a batch mint
#### Value
```python
250
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'MaxRecipientsPerBatchMint')
```
---------
### MaxRecipientsPerBatchTransfer
 The max number of recipients allowed in a batch transfer
#### Value
```python
250
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'MaxRecipientsPerBatchTransfer')
```
---------
### MaxReserves
 The maximum number of named reserves that can exist on an account
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'MaxReserves')
```
---------
### MaxTokensPerBatchTransfer
 The max number of tokens allowed in a batch transfer
#### Value
```python
500
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'MaxTokensPerBatchTransfer')
```
---------
### MigrationExtrinsicsInfosToPause
 List of extrinsics to pause during multi block migration (this pallet is excluded)
#### Value
```python
[
    {'extrinsic_name': None, 'pallet_name': 'Marketplace'},
    {'extrinsic_name': None, 'pallet_name': 'FuelTanks'},
    {'extrinsic_name': None, 'pallet_name': 'EfinityXcm'},
]
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'MigrationExtrinsicsInfosToPause')
```
---------
### MigrationWeightLimitPercentage
 Percentage of block weight to consume during migration
#### Value
```python
100000000
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'MigrationWeightLimitPercentage')
```
---------
### NativeAssetInfo
 The [`NativeAssetInfo`](ep_multi_tokens::NativeAssetInfo) for this pallet
#### Value
```python
{'id': {'collection_id': 0, 'token_id': 0}, 'units_per_second': 87990000000000000000}
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'NativeAssetInfo')
```
---------
### ReserveIdentifier
 The id used for making reservations with this pallet
#### Value
```python
'0x6d756c746f6b656e'
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'ReserveIdentifier')
```
---------
### TokenAccountDeposit
 The amount of [`Balance`](BalanceOf) that must be reserved for a token account to be
 maintained
#### Value
```python
10000000000000000
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'TokenAccountDeposit')
```
---------
### TokenMetadataMaxNameLength
 Max length of name stored in [`TokenMetadata`]
#### Value
```python
32
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'TokenMetadataMaxNameLength')
```
---------
### TokenMetadataMaxSymbolLength
 Max length of symbol stored in [`TokenMetadata`]
#### Value
```python
8
```
#### Python
```python
constant = substrate.get_constant('MultiTokens', 'TokenMetadataMaxSymbolLength')
```
---------
## Errors

---------
### AlreadyExpired
Tried to set an expiration that has already passed

---------
### AmountZero
An amount of zero was used when it&\#x27;s not allowed

---------
### BalanceBelowMinimumRequirement
The balance is below the minimum required balance

---------
### BalanceLow
Not enough balance to perform the operation.

---------
### CannotApproveSelf
An account cannot approve itself as an operator

---------
### CannotTransferToSelf
An account cannot transfer tokens to itself

---------
### CollectionAccountNotFound
CollectionAccount was not found

---------
### CollectionAlreadyApproved
The collection is already approved for all, so it is useless to approve for a single
token

---------
### CollectionIdAlreadyInUse
Collection ID is already in use

---------
### CollectionNotFound
Collection was not found

---------
### ConflictingLocation
Conflicting MultiLocation for an AssetId

---------
### CurrencyIncompatibleWithCollectionRoyalty
Token cannot act as a
[`currency`](ep_multi_tokens::Collection::explicit_royalty_currencies) and also a
[`Royalty`](Config::Royalty)

---------
### DepositReserveFailed
Unable to reserve the amount to create a new collection/token

---------
### DepositUnreserveFailed
Unable to unreserve the amount to burn an existing collection/token

---------
### DestroyForbiddenByAttributeCount
The collection cannot be destroyed because it has attributes

---------
### DestroyForbiddenByCollectionEvent
The [`OnCollectionEvent`] trait has forbidden burning of the collection

---------
### DestroyForbiddenByRemainingTokens
Destroy is not allowed on collections that have tokens. Destroy all tokens before
calling [`destroy_collection`](Pallet::destroy_collection). Keep in mind that the
[`Tokens`] storage can remain even if all of [`Token`](ep_multi_tokens::Token)&\#x27;s units
were burned. A [`Token`](ep_multi_tokens::Token) can only be destroyed by setting
[`remove_token_storage`](OnBurnInput::remove_token_storage) to true in
[`burn`](Pallet::burn).

---------
### FreezeStateRequired
Freeze state is required when freezing a token

---------
### Frozen
The operation failed due to an item being frozen

---------
### HasNeverFreezeState
The token has a never freeze state. The state cannot be changed and the token cannot be
frozen.

---------
### IdleOperationQueueFull
The idle operation queue is full and cannot accept new operations

---------
### InsufficientAllowance
Not enough allowance to perform the operation

---------
### InvalidAttributeCount
Provided attribute count doesnt match the count is storage

---------
### InvalidAttributeKey
Attribute key invalid

---------
### InvalidExplicitRoyaltyCurrencies
One or more of the explicit royalty currencies are invalid

---------
### InvalidFreezeState
The freeze state is not valid

---------
### InvalidUnitPrice
The unit price cannot be zero, cannot decrease, and `unit_price * total_supply` must
be greater than [`Config::TokenAccountDeposit`]

---------
### LiquidityRestrictions
The balance is locked or restricted

---------
### MaxApprovalsExceeded
The max number of approvals for this account was exceeded

---------
### MaxTokenCountExceeded
Tried to mint more tokens than allowed

---------
### MintFailedRequirements
The minting did not meet the requirements set by the
[`MintPolicy`](traits::CollectionPolicy::Mint)

---------
### NoPermission
Caller is not allowed to execute this extrinsic

---------
### OperationNotAllowedForNativeToken
This operation is not allowed for the native token

---------
### PercentageOutOfBounds
Royalty percentage is above or below allowed bounds

---------
### PermanentlyFrozen
The token is permanently frozen

---------
### PremintExceeded
The preminted amount would be exceeded by the mint operation

---------
### ReservesLow
Reserved balance is not enough to perform the operation

---------
### TokenAccountNotFound
TokenAccount was not found

---------
### TokenAlreadyExists
Tried to create [`Token`](ep_multi_tokens::Token) that already exists

---------
### TokenMetadataCreationFailed
Token metadata could not be created from mint params

---------
### TokenMintCapExceeded
The cap for the token was exceeded during mint

---------
### TokenNotFound
Token was not found

---------
### TooManyLocks
Max named locks for an account are exceeded

---------
### TooManyReserves
Max named reserves for an account are exceeded

---------
### TransferParamCreationFailed
Transfer params could not be created

---------
### WrongCurrentApprovedAmount
The passed `current_amount` does not match the actual current amount of the approval

---------