
# MantaPay

---------
## Calls

---------
### private_transfer
Transfers private assets encoded in `post`.

\# Note

In this transaction, `origin` is just signing the `post` and is not necessarily related
to any of the participants in the transaction itself.
#### Attributes
| Name | Type |
| -------- | -------- | 
| post | `TransferPost` | 

#### Python
```python
call = substrate.compose_call(
    'MantaPay', 'private_transfer', {
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
### public_transfer
Transfers public `asset` from `origin` to the `sink` account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `Asset` | 
| sink | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'MantaPay', 'public_transfer', {
    'asset': {
        'id': '[u8; 32]',
        'value': '[u8; 16]',
    },
    'sink': 'AccountId',
}
)
```

---------
### to_private
Transforms some public assets into private ones using `post`, withdrawing the public
assets from the `origin` account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| post | `TransferPost` | 

#### Python
```python
call = substrate.compose_call(
    'MantaPay', 'to_private', {
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
### to_public
Transforms some private assets into public ones using `post`, depositing the public
assets in the `origin` account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| post | `TransferPost` | 

#### Python
```python
call = substrate.compose_call(
    'MantaPay', 'to_public', {
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
## Events

---------
### PrivateTransfer
Private Transfer Event
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| origin | `Option<T::AccountId>` | ```(None, 'AccountId')```

---------
### ToPrivate
To Private Event
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset | `Asset` | ```{'id': '[u8; 32]', 'value': '[u8; 16]'}```
| source | `T::AccountId` | ```AccountId```

---------
### ToPublic
To Public Event
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset | `Asset` | ```{'id': '[u8; 32]', 'value': '[u8; 16]'}```
| sink | `T::AccountId` | ```AccountId```

---------
### Transfer
Public Transfer Event
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset | `Asset` | ```{'id': '[u8; 32]', 'value': '[u8; 16]'}```
| source | `T::AccountId` | ```AccountId```
| sink | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### NullifierCommitmentSet
 Nullifier Commitment Set

#### Python
```python
result = substrate.query(
    'MantaPay', 'NullifierCommitmentSet', ['[u8; 32]']
)
```

#### Return value
```python
()
```
---------
### NullifierSetInsertionOrder
 Nullifiers Ordered by Insertion

#### Python
```python
result = substrate.query(
    'MantaPay', 'NullifierSetInsertionOrder', ['u64']
)
```

#### Return value
```python
(
    '[u8; 32]',
    {'ciphertext': '[[u8; 32]; 2]', 'ephemeral_public_key': '[u8; 32]'},
)
```
---------
### NullifierSetSize
 Nullifier Set Size

#### Python
```python
result = substrate.query(
    'MantaPay', 'NullifierSetSize', []
)
```

#### Return value
```python
'u64'
```
---------
### ShardTrees
 Shard Merkle Tree Paths

#### Python
```python
result = substrate.query(
    'MantaPay', 'ShardTrees', ['u8']
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
    'MantaPay', 'Shards', ['u8', 'u64']
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
### UtxoAccumulatorOutputs
 Outputs of Utxo Accumulator

#### Python
```python
result = substrate.query(
    'MantaPay', 'UtxoAccumulatorOutputs', ['[u8; 32]']
)
```

#### Return value
```python
()
```
---------
### UtxoSet
 UTXO Set

#### Python
```python
result = substrate.query(
    'MantaPay', 'UtxoSet', [
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
## Errors

---------
### AssetRegistered
Asset Registered

An asset present in this transfer has already been registered to the ledger.

---------
### AssetSpent
Asset Spent

An asset present in this transfer has already been spent.

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
### InvalidUtxoAccumulatorOutput
Invalid UTXO Accumulator Output

The sender was constructed on an invalid version of the ledger state.

---------
### Marker
Marker Error, this error exists for `PhantomData` should never happen

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
### TransferLedgerChecksumError
Transfer Ledger Wrong Checksum Error

---------
### TransferLedgerFpEncodeError
Transer Ledger Field Element Encoding Error

---------
### TransferLedgerProofSystemFailed
Transfer Ledger Proof Error

---------
### TransferLedgerUnknownAsset
Transfer Ledger Unknown Asset

---------
### TransferLedgerVerifyingContextDecodeError
Transfer Ledger `VerifyingContext` cannont be decoded

---------
### ZeroTransfer
Zero Transfer

Transfers cannot include amounts equal to zero.

---------