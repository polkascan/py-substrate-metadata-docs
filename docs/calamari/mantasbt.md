
# MantaSbt

---------
## Calls

---------
### allowlist_evm_account
Adds EvmAddress to allowlist and reserve an unique AssetId for this account. Requires caller to be the `AllowlistAccount`.

Uses `mint_id` to specify which mint, this is so an `EvmAddress` can have multiple free mints for different `MintIds`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| mint_id | `MintId` | 
| evm_address | `EvmAddress` | 

#### Python
```python
call = substrate.compose_call(
    'MantaSbt', 'allowlist_evm_account', {
    'evm_address': '[u8; 20]',
    'mint_id': 'u32',
}
)
```

---------
### change_allowlist_account
Sets the privileged allowlist account. Requires `AdminOrigin`
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `Option<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'MantaSbt', 'change_allowlist_account', {'account': (None, 'AccountId')}
)
```

---------
### change_force_account
Sets the privileged reserve account. Requires `AdminOrigin`
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `Option<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'MantaSbt', 'change_force_account', {'account': (None, 'AccountId')}
)
```

---------
### change_free_reserve_account
Sets the privileged reserve account. Requires `AdminOrigin`
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `Option<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'MantaSbt', 'change_free_reserve_account', {'account': (None, 'AccountId')}
)
```

---------
### force_mint_sbt_eth
#### Attributes
| Name | Type |
| -------- | -------- | 
| post | `Box<TransferPost>` | 
| mint_id | `MintId` | 
| address | `EvmAddress` | 
| collection_id | `Option<u128>` | 
| item_id | `Option<u128>` | 
| metadata | `BoundedVec<u8, T::SbtMetadataBound>` | 
| minting_account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'MantaSbt', 'force_mint_sbt_eth', {
    'address': '[u8; 20]',
    'collection_id': (None, 'u128'),
    'item_id': (None, 'u128'),
    'metadata': 'Bytes',
    'mint_id': 'u32',
    'minting_account': 'AccountId',
    'post': {
        'asset_id': (None, '[u8; 32]'),
        'authorization_signature': (
            None,
            {
                'authorization_key': '[u8; 32]',
                'signature': (
                    '[u8; 32]',
                    '[u8; 32]',
                ),
            },
        ),
        'proof': '[u8; 128]',
        'receiver_posts': [
            {
                'full_incoming_note': {
                    'address_partition': 'u8',
                    'incoming_note': {
                        'ciphertext': '[[u8; 32]; 3]',
                        'ephemeral_public_key': '[u8; 32]',
                        'tag': '[u8; 32]',
                    },
                    'light_incoming_note': {
                        'ciphertext': '[[u8; 32]; 3]',
                        'ephemeral_public_key': '[u8; 32]',
                    },
                },
                'utxo': {
                    'commitment': '[u8; 32]',
                    'is_transparent': 'bool',
                    'public_asset': {
                        'id': '[u8; 32]',
                        'value': '[u8; 16]',
                    },
                },
            },
        ],
        'sender_posts': [
            {
                'nullifier_commitment': '[u8; 32]',
                'outgoing_note': {
                    'ciphertext': '[[u8; 32]; 2]',
                    'ephemeral_public_key': '[u8; 32]',
                },
                'utxo_accumulator_output': '[u8; 32]',
            },
        ],
        'sink_accounts': ['[u8; 32]'],
        'sinks': ['[u8; 16]'],
        'sources': ['[u8; 16]'],
    },
}
)
```

---------
### force_to_private
#### Attributes
| Name | Type |
| -------- | -------- | 
| post | `Box<TransferPost>` | 
| mint_id | `MintId` | 
| metadata | `BoundedVec<u8, T::SbtMetadataBound>` | 
| minting_account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'MantaSbt', 'force_to_private', {
    'metadata': 'Bytes',
    'mint_id': 'u32',
    'minting_account': 'AccountId',
    'post': {
        'asset_id': (None, '[u8; 32]'),
        'authorization_signature': (
            None,
            {
                'authorization_key': '[u8; 32]',
                'signature': (
                    '[u8; 32]',
                    '[u8; 32]',
                ),
            },
        ),
        'proof': '[u8; 128]',
        'receiver_posts': [
            {
                'full_incoming_note': {
                    'address_partition': 'u8',
                    'incoming_note': {
                        'ciphertext': '[[u8; 32]; 3]',
                        'ephemeral_public_key': '[u8; 32]',
                        'tag': '[u8; 32]',
                    },
                    'light_incoming_note': {
                        'ciphertext': '[[u8; 32]; 3]',
                        'ephemeral_public_key': '[u8; 32]',
                    },
                },
                'utxo': {
                    'commitment': '[u8; 32]',
                    'is_transparent': 'bool',
                    'public_asset': {
                        'id': '[u8; 32]',
                        'value': '[u8; 16]',
                    },
                },
            },
        ],
        'sender_posts': [
            {
                'nullifier_commitment': '[u8; 32]',
                'outgoing_note': {
                    'ciphertext': '[[u8; 32]; 2]',
                    'ephemeral_public_key': '[u8; 32]',
                },
                'utxo_accumulator_output': '[u8; 32]',
            },
        ],
        'sink_accounts': ['[u8; 32]'],
        'sinks': ['[u8; 16]'],
        'sources': ['[u8; 16]'],
    },
}
)
```

---------
### mint_sbt_eth
Mint zkSBT using Evm allowlist, signature must correspond to an `EvmAddress` which has been added to allowlist.

Requires a valid `Eip712Signature` which is generated from signing the zkp with an eth private key
#### Attributes
| Name | Type |
| -------- | -------- | 
| post | `Box<TransferPost>` | 
| chain_id | `u64` | 
| eth_signature | `Eip712Signature` | 
| mint_id | `MintId` | 
| collection_id | `Option<u128>` | 
| item_id | `Option<u128>` | 
| metadata | `Option<BoundedVec<u8, T::SbtMetadataBound>>` | 

#### Python
```python
call = substrate.compose_call(
    'MantaSbt', 'mint_sbt_eth', {
    'chain_id': 'u64',
    'collection_id': (None, 'u128'),
    'eth_signature': '[u8; 65]',
    'item_id': (None, 'u128'),
    'metadata': (None, 'Bytes'),
    'mint_id': 'u32',
    'post': {
        'asset_id': (None, '[u8; 32]'),
        'authorization_signature': (
            None,
            {
                'authorization_key': '[u8; 32]',
                'signature': (
                    '[u8; 32]',
                    '[u8; 32]',
                ),
            },
        ),
        'proof': '[u8; 128]',
        'receiver_posts': [
            {
                'full_incoming_note': {
                    'address_partition': 'u8',
                    'incoming_note': {
                        'ciphertext': '[[u8; 32]; 3]',
                        'ephemeral_public_key': '[u8; 32]',
                        'tag': '[u8; 32]',
                    },
                    'light_incoming_note': {
                        'ciphertext': '[[u8; 32]; 3]',
                        'ephemeral_public_key': '[u8; 32]',
                    },
                },
                'utxo': {
                    'commitment': '[u8; 32]',
                    'is_transparent': 'bool',
                    'public_asset': {
                        'id': '[u8; 32]',
                        'value': '[u8; 16]',
                    },
                },
            },
        ],
        'sender_posts': [
            {
                'nullifier_commitment': '[u8; 32]',
                'outgoing_note': {
                    'ciphertext': '[[u8; 32]; 2]',
                    'ephemeral_public_key': '[u8; 32]',
                },
                'utxo_accumulator_output': '[u8; 32]',
            },
        ],
        'sink_accounts': ['[u8; 32]'],
        'sinks': ['[u8; 16]'],
        'sources': ['[u8; 16]'],
    },
}
)
```

---------
### new_mint_info
#### Attributes
| Name | Type |
| -------- | -------- | 
| start_time | `Moment<T>` | 
| end_time | `Option<Moment<T>>` | 
| mint_name | `BoundedVec<u8, T::RegistryBound>` | 
| public | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'MantaSbt', 'new_mint_info', {
    'end_time': (None, 'u64'),
    'mint_name': 'Bytes',
    'public': 'bool',
    'start_time': 'u64',
}
)
```

---------
### remove_allowlist_evm_account
Remove allowlist evm account. Requires `AdminOrigin`
#### Attributes
| Name | Type |
| -------- | -------- | 
| mint_id | `MintId` | 
| evm_address | `EvmAddress` | 

#### Python
```python
call = substrate.compose_call(
    'MantaSbt', 'remove_allowlist_evm_account', {
    'evm_address': '[u8; 20]',
    'mint_id': 'u32',
}
)
```

---------
### reserve_sbt
Reserves AssetIds to be used subsequently in `to_private` above.

Increments AssetManager&\#x27;s AssetId counter.
#### Attributes
| Name | Type |
| -------- | -------- | 
| reservee | `Option<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'MantaSbt', 'reserve_sbt', {'reservee': (None, 'AccountId')}
)
```

---------
### set_next_sbt_id
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `Option<StandardAssetId>` | 

#### Python
```python
call = substrate.compose_call(
    'MantaSbt', 'set_next_sbt_id', {'asset_id': (None, 'u128')}
)
```

---------
### to_private
Mints a zkSBT

`TransferPost` is posted to private ledger and SBT metadata is stored onchain.
`signature` parameter can be used to relay a tx.
#### Attributes
| Name | Type |
| -------- | -------- | 
| mint_id | `Option<MintId>` | 
| chain_id | `Option<u64>` | 
| signature | `Option<SignatureInfoOf<T>>` | 
| post | `Box<TransferPost>` | 
| metadata | `BoundedVec<u8, T::SbtMetadataBound>` | 

#### Python
```python
call = substrate.compose_call(
    'MantaSbt', 'to_private', {
    'chain_id': (None, 'u64'),
    'metadata': 'Bytes',
    'mint_id': (None, 'u32'),
    'post': {
        'asset_id': (None, '[u8; 32]'),
        'authorization_signature': (
            None,
            {
                'authorization_key': '[u8; 32]',
                'signature': (
                    '[u8; 32]',
                    '[u8; 32]',
                ),
            },
        ),
        'proof': '[u8; 128]',
        'receiver_posts': [
            {
                'full_incoming_note': {
                    'address_partition': 'u8',
                    'incoming_note': {
                        'ciphertext': '[[u8; 32]; 3]',
                        'ephemeral_public_key': '[u8; 32]',
                        'tag': '[u8; 32]',
                    },
                    'light_incoming_note': {
                        'ciphertext': '[[u8; 32]; 3]',
                        'ephemeral_public_key': '[u8; 32]',
                    },
                },
                'utxo': {
                    'commitment': '[u8; 32]',
                    'is_transparent': 'bool',
                    'public_asset': {
                        'id': '[u8; 32]',
                        'value': '[u8; 16]',
                    },
                },
            },
        ],
        'sender_posts': [
            {
                'nullifier_commitment': '[u8; 32]',
                'outgoing_note': {
                    'ciphertext': '[[u8; 32]; 2]',
                    'ephemeral_public_key': '[u8; 32]',
                },
                'utxo_accumulator_output': '[u8; 32]',
            },
        ],
        'sink_accounts': ['[u8; 32]'],
        'sinks': ['[u8; 16]'],
        'sources': ['[u8; 16]'],
    },
    'signature': (
        None,
        {
            'pub_key': {
                'Ecdsa': '[u8; 33]',
                'Ed25519': '[u8; 32]',
                'Sr25519': '[u8; 32]',
            },
            'sig': {
                'Ecdsa': '[u8; 65]',
                'Ed25519': '[u8; 64]',
                'Sr25519': '[u8; 64]',
            },
        },
    ),
}
)
```

---------
### update_mint_info
Updates the time range of which a `MintId` will be valid. Also can update `mint_name` Requires `AdminOrigin`
#### Attributes
| Name | Type |
| -------- | -------- | 
| mint_id | `MintId` | 
| start_time | `Moment<T>` | 
| end_time | `Option<Moment<T>>` | 
| mint_name | `BoundedVec<u8, T::RegistryBound>` | 
| public | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'MantaSbt', 'update_mint_info', {
    'end_time': (None, 'u64'),
    'mint_id': 'u32',
    'mint_name': 'Bytes',
    'public': 'bool',
    'start_time': 'u64',
}
)
```

---------
## Events

---------
### AllowlistEvmAddress
Evm Address is Allowlisted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| address | `EvmAddress` | ```[u8; 20]```
| mint_id | `MintId` | ```u32```
| asset_id | `StandardAssetId` | ```u128```

---------
### ChangeAllowlistAccount
Privileged `AllowlistAccount` is changed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `Option<T::AccountId>` | ```(None, 'AccountId')```

---------
### ChangeForceAccount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `Option<T::AccountId>` | ```(None, 'AccountId')```

---------
### ChangeFreeReserveAccount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `Option<T::AccountId>` | ```(None, 'AccountId')```

---------
### ForceMintSbtEvm
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| address | `EvmAddress` | ```[u8; 20]```
| mint_id | `MintId` | ```u32```
| asset_id | `StandardAssetId` | ```u128```

---------
### ForceToPrivate
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset | `StandardAssetId` | ```u128```
| source | `T::AccountId` | ```AccountId```

---------
### MintSbt
Mints SBTs to private ledger
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset | `StandardAssetId` | ```u128```
| source | `T::AccountId` | ```AccountId```

---------
### MintSbtEvm
Sbt is minted using Allowlisted Eth account
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| address | `EvmAddress` | ```[u8; 20]```
| mint_id | `MintId` | ```u32```
| asset_id | `StandardAssetId` | ```u128```

---------
### NewMintInfo
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| mint_id | `MintId` | ```u32```
| start_time | `Moment<T>` | ```u64```
| end_time | `Option<Moment<T>>` | ```(None, 'u64')```
| mint_name | `Vec<u8>` | ```Bytes```

---------
### RemoveAllowlistEvmAddress
Evm Address is removed from allowlist
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| address | `EvmAddress` | ```[u8; 20]```
| mint_id | `MintId` | ```u32```

---------
### SBTReserved
Reserve `AssetIds` as SBT
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| reserve_account | `T::AccountId` | ```AccountId```
| start_id | `StandardAssetId` | ```u128```
| stop_id | `StandardAssetId` | ```u128```

---------
### SetNextSbtId
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `Option<StandardAssetId>` | ```(None, 'u128')```

---------
### UpdateMintInfo
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| mint_id | `MintId` | ```u32```
| start_time | `Moment<T>` | ```u64```
| end_time | `Option<Moment<T>>` | ```(None, 'u64')```
| mint_name | `Vec<u8>` | ```Bytes```

---------
## Storage functions

---------
### AllowlistAccount
 Account that can add evm accounts to allowlist

#### Python
```python
result = substrate.query(
    'MantaSbt', 'AllowlistAccount', []
)
```

#### Return value
```python
'AccountId'
```
---------
### EvmAccountAllowlist
 Allowlist for Evm Accounts

#### Python
```python
result = substrate.query(
    'MantaSbt', 'EvmAccountAllowlist', ['u32', '[u8; 20]']
)
```

#### Return value
```python
{'AlreadyMinted': None, 'Available': 'u128'}
```
---------
### ForceAccount
 Account that can access to force calls

#### Python
```python
result = substrate.query(
    'MantaSbt', 'ForceAccount', []
)
```

#### Return value
```python
'AccountId'
```
---------
### FreeReserveAccount
 Account that can reserve `AssetId` for free

#### Python
```python
result = substrate.query(
    'MantaSbt', 'FreeReserveAccount', []
)
```

#### Return value
```python
'AccountId'
```
---------
### MintIdRegistry
 Registers a number for mint type

#### Python
```python
result = substrate.query(
    'MantaSbt', 'MintIdRegistry', ['u32']
)
```

#### Return value
```python
{'end_time': (None, 'u64'), 'mint_name': 'Bytes', 'start_time': 'u64'}
```
---------
### NextMintId
 Counter for MintId. Increments by one every time a new mint type is created (Bab, Galxe, etc.)

 Should only ever be modified by `next_mint_id_and_increment()`

#### Python
```python
result = substrate.query(
    'MantaSbt', 'NextMintId', []
)
```

#### Return value
```python
'u32'
```
---------
### NextSbtId
 Counter for SBT AssetId. Increments by one every time a new asset id is requested.

 Should only ever be modified by `next_sbt_id_and_increment()`

#### Python
```python
result = substrate.query(
    'MantaSbt', 'NextSbtId', []
)
```

#### Return value
```python
'u128'
```
---------
### PublicMintList
 Allows mint type to be public

#### Python
```python
result = substrate.query(
    'MantaSbt', 'PublicMintList', ['u32']
)
```

#### Return value
```python
()
```
---------
### ReservedIds
 Allowlist accounts to be able to mint SBTs with designated `StandardAssetId`

#### Python
```python
result = substrate.query(
    'MantaSbt', 'ReservedIds', ['AccountId']
)
```

#### Return value
```python
('u128', 'u128')
```
---------
### SbtMetadataV2
 SBT Metadata maps `StandardAsset` to the corresponding SBT metadata

 Metadata is raw bytes that correspond to an image

#### Python
```python
result = substrate.query(
    'MantaSbt', 'SbtMetadataV2', ['u128']
)
```

#### Return value
```python
{
    'collection_id': (None, 'u128'),
    'extra': (None, 'Bytes'),
    'item_id': (None, 'u128'),
    'mint_id': 'u32',
}
```
---------
### ShardTrees
 Shard Merkle Tree Paths

#### Python
```python
result = substrate.query(
    'MantaSbt', 'ShardTrees', ['u8']
)
```

#### Return value
```python
{
    'current_path': {
        'inner_path': ['[u8; 32]'],
        'leaf_index': 'u32',
        'sibling_digest': '[u8; 32]',
    },
    'leaf_digest': (None, '[u8; 32]'),
}
```
---------
### Shards
 UTXOs and Incoming Notes Grouped by Shard

#### Python
```python
result = substrate.query(
    'MantaSbt', 'Shards', ['u8', 'u64']
)
```

#### Return value
```python
(
    {
        'commitment': '[u8; 32]',
        'is_transparent': 'bool',
        'public_asset': {'id': '[u8; 32]', 'value': '[u8; 16]'},
    },
    {
        'address_partition': 'u8',
        'incoming_note': {
            'ciphertext': '[[u8; 32]; 3]',
            'ephemeral_public_key': '[u8; 32]',
            'tag': '[u8; 32]',
        },
        'light_incoming_note': {
            'ciphertext': '[[u8; 32]; 3]',
            'ephemeral_public_key': '[u8; 32]',
        },
    },
)
```
---------
### UtxoSet
 UTXO Set

#### Python
```python
result = substrate.query(
    'MantaSbt', 'UtxoSet', [
    {
        'commitment': '[u8; 32]',
        'is_transparent': 'bool',
        'public_asset': {
            'id': '[u8; 32]',
            'value': '[u8; 16]',
        },
    },
]
)
```

#### Return value
```python
()
```
---------
## Constants

---------
### MintsPerReserve
 Number of unique Asset Ids reserved per `reserve_sbt` call, is the amount of SBTs allowed to be minted
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('MantaSbt', 'MintsPerReserve')
```
---------
### PalletId
 Pallet ID
#### Value
```python
'0x6d616e7461736274'
```
#### Python
```python
constant = substrate.get_constant('MantaSbt', 'PalletId')
```
---------
### RegistryBound
 Max size in bytes of `mint_name` entered in `RegisteredMint`
#### Value
```python
300
```
#### Python
```python
constant = substrate.get_constant('MantaSbt', 'RegistryBound')
```
---------
### ReservePrice
 Price to reserve Asset Ids
#### Value
```python
5000000000000000
```
#### Python
```python
constant = substrate.get_constant('MantaSbt', 'ReservePrice')
```
---------
### SbtMetadataBound
 Max size in bytes of stored metadata
#### Value
```python
300
```
#### Python
```python
constant = substrate.get_constant('MantaSbt', 'SbtMetadataBound')
```
---------
## Errors

---------
### AlreadyInAllowlist
`EvmAddress` is already in the allowlist

---------
### AlreadyMinted
SBT has already been minted with this `EvmAddress`

---------
### AssetIdsAlreadyReserved
Already has unused AssetIds reserved

---------
### AssetRegistered
Asset Registered

An asset present in this transfer has already been registered to the ledger.

---------
### AssetSpent
Asset Spent

An asset present in this transfer has already been spent.

---------
### BadSignature
Crypto Signature was not valid

---------
### DuplicateAssetId
Duplicate asset id

---------
### DuplicateRegister
Duplicate Register

There were multiple register entries for the same underlying asset in this transfer.

---------
### DuplicateSpend
Duplicate Spend

There were multiple spend entries for the same underlying asset in this transfer.

---------
### FungibleLedgerEncodeError
Fungible Ledger Encode Error

---------
### InvalidAssetId
Invalid Asset Id

The asset id of the transfer could not be converted correctly to the standard format.

---------
### InvalidAuthorizationSignature
Invalid Authorization Signature

---------
### InvalidMintId
MintId does not exist, cannot update a nonexistent MintId

---------
### InvalidProof
Invalid Proof

The submitted proof did not pass validation, or errored during validation.

---------
### InvalidSerializedForm
Invalid Serialized Form

The transfer could not be interpreted because of an issue during deserialization.

---------
### InvalidShape
Invalid Shape

The transfer had an invalid shape.

---------
### InvalidSinkAccount
Invalid Sink Account

At least one of the sink accounts in invalid.

---------
### InvalidSourceAccount
Invalid Source Account

At least one of the source accounts is invalid.

---------
### InvalidTimeRange
Time range is invalid (start_time &gt; end_time)

---------
### InvalidUtxoAccumulatorOutput
Invalid UTXO Accumulator Output

The sender was constructed on an invalid version of the ledger state.

---------
### Marker
Marker Error, this error exists for `PhantomData` should never happen

---------
### MintNotAvailable
Minting SBT is outside defined time range or chain_id is not set

---------
### MintNotPublic
Mint type is not public, only permissioned accounts can use this mint

---------
### NoSenderLedger
SBT only allows `ToPrivate` Transactions

---------
### NotAllowlistAccount
Account is not the privileged account able to allowlist eth addresses

---------
### NotAllowlisted
Eth account is not allowlisted for free mint, can also be caused by an incorrect signature (recovers an invalid account)

---------
### NotForceAccount
Account is not privileged account able to do force mints

---------
### NotReserved
`AssetId` was not reserved by this account to mint

---------
### PublicUpdateBelowMinimum
[`BelowMinimum`](FungibleLedgerError::BelowMinimum) from [`FungibleLedgerError`]

---------
### PublicUpdateCannotCreate
[`CannotCreate`](FungibleLedgerError::CannotCreate) from [`FungibleLedgerError`]

---------
### PublicUpdateCannotWithdraw
[`CannotWithdraw`](FungibleLedgerError::CannotWithdrawMoreThan) from [`FungibleLedgerError`]

---------
### PublicUpdateInvalidAssetId
[`InvalidAssetId`](FungibleLedgerError::InvalidAssetId) from [`FungibleLedgerError`]

---------
### PublicUpdateInvalidBurn
[`InvalidBurn`](FungibleLedgerError::InvalidBurn) from [`FungibleLedgerError`]

---------
### PublicUpdateInvalidMint
[`InvalidMint`](FungibleLedgerError::InvalidMint) from [`FungibleLedgerError`]

---------
### PublicUpdateInvalidTransfer
[`InvalidTransfer`](FungibleLedgerError::InvalidTransfer) from [`FungibleLedgerError`]

---------
### PublicUpdateOverflow
[`Overflow`](FungibleLedgerError::Overflow) from [`FungibleLedgerError`]

---------
### PublicUpdateUnknownAsset
[`UnknownAsset`](FungibleLedgerError::UnknownAsset) from [`FungibleLedgerError`]

---------
### ReceiverLedgerChecksumError
Receiver Ledger Wrong Checksum Error

---------
### ReceiverLedgerFpDecodeError
Receiver Ledger Field Element Decoding Error

---------
### ReceiverLedgerFpEncodeError
Receiver Ledger Field Element Encoding Error

---------
### ReceiverLedgerFullNoteDecodeError
Receiver Ledger Full Incoming Note Decoding Error

---------
### ReceiverLedgerMTParametersDecodeError
Receiver Ledger Merkle Tree Parameters Decoding Error

---------
### ReceiverLedgerMerkleTreeCapacityError
Receiver Ledger Merkle Tree Out of Capacity Error

---------
### ReceiverLedgerPathDecodeError
Receiver Ledger Path Decoding Error

---------
### ReceiverLedgerUtxoAccumulatorItemHashDecodeError
Receiver Ledger Utxo Accumulator Item Hash Decoding Error

---------
### ReceiverLedgerUtxoDecodeFailed
Reciever Ledger Utxo decode failed

---------
### SenderLedgerFpEncodeError
Sender Ledger Fp Encoding failed.

---------
### SenderLedgerOutgoingNodeDecodeFailed
Sender Ledger [`OutgoingNote`] failed to decode

---------
### TooHighAssetId
Force call is trying to use asset id above the maximum

---------
### TransferLedgerChecksumError
Transfer Ledger Wrong Checksum Error

---------
### TransferLedgerFpEncodeError
Transfer Ledger Field Element Encoding Error

---------
### TransferLedgerProofSystemFailed
Transfer Ledger Proof Error

---------
### TransferLedgerUnknownAsset
Transfer Ledger Unknown Asset

---------
### TransferLedgerVerifyingContextDecodeError
Transfer Ledger `VerifyingContext` cannot be decoded

---------
### ValueNotOne
Value of `ToPrivate` post must be one.

---------
### ZeroMints
Pallet is configured to allow no SBT mints, only happens when `MintsPerReserve` is zero

---------