
# BeefyLightClient

---------
## Calls

---------
### initialize
#### Attributes
| Name | Type |
| -------- | -------- | 
| network_id | `SubNetworkId` | 
| latest_beefy_block | `u64` | 
| validator_set | `ValidatorSet` | 
| next_validator_set | `ValidatorSet` | 

#### Python
```python
call = substrate.compose_call(
    'BeefyLightClient', 'initialize', {
    'latest_beefy_block': 'u64',
    'network_id': (
        'Mainnet',
        'Kusama',
        'Polkadot',
        'Rococo',
        'Alphanet',
        'Liberland',
    ),
    'next_validator_set': {
        'id': 'u64',
        'len': 'u32',
        'root': 'scale_info::11',
    },
    'validator_set': {
        'id': 'u64',
        'len': 'u32',
        'root': 'scale_info::11',
    },
}
)
```

---------
### submit_signature_commitment
#### Attributes
| Name | Type |
| -------- | -------- | 
| network_id | `SubNetworkId` | 
| commitment | `Commitment` | 
| validator_proof | `ValidatorProof` | 
| latest_mmr_leaf | `BeefyMMRLeaf` | 
| proof | `Proof<H256>` | 

#### Python
```python
call = substrate.compose_call(
    'BeefyLightClient', 'submit_signature_commitment', {
    'commitment': {
        'block_number': 'u32',
        'payload': [
            ('[u8; 2]', 'Bytes'),
        ],
        'validator_set_id': 'u64',
    },
    'latest_mmr_leaf': {
        'beefy_next_authority_set': {
            'id': 'u64',
            'len': 'u32',
            'root': 'scale_info::11',
        },
        'leaf_extra': {
            'digest_hash': 'scale_info::11',
            'random_seed': 'scale_info::11',
        },
        'parent_number_and_hash': (
            'u32',
            'scale_info::11',
        ),
        'version': 'u8',
    },
    'network_id': (
        'Mainnet',
        'Kusama',
        'Polkadot',
        'Rococo',
        'Alphanet',
        'Liberland',
    ),
    'proof': {
        'items': ['scale_info::11'],
        'order': 'u64',
    },
    'validator_proof': {
        'positions': ['u128'],
        'public_key_merkle_proofs': [
            ['scale_info::11'],
        ],
        'public_keys': ['[u8; 20]'],
        'signatures': ['Bytes'],
        'validator_claims_bitfield': 'BitVec',
    },
}
)
```

---------
## Events

---------
### NewMMRRoot
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SubNetworkId` | ```('Mainnet', 'Kusama', 'Polkadot', 'Rococo', 'Alphanet', 'Liberland')```
| None | `H256` | ```scale_info::11```
| None | `u64` | ```u64```

---------
### ValidatorRegistryUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SubNetworkId` | ```('Mainnet', 'Kusama', 'Polkadot', 'Rococo', 'Alphanet', 'Liberland')```
| None | `H256` | ```scale_info::11```
| None | `u32` | ```u32```
| None | `u64` | ```u64```

---------
### VerificationSuccessful
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SubNetworkId` | ```('Mainnet', 'Kusama', 'Polkadot', 'Rococo', 'Alphanet', 'Liberland')```
| None | `T::AccountId` | ```AccountId```
| None | `u32` | ```u32```

---------
## Storage functions

---------
### CurrentValidatorSet

#### Python
```python
result = substrate.query(
    'BeefyLightClient', 'CurrentValidatorSet', [
    (
        'Mainnet',
        'Kusama',
        'Polkadot',
        'Rococo',
        'Alphanet',
        'Liberland',
    ),
]
)
```

#### Return value
```python
{'id': 'u64', 'len': 'u32', 'root': 'scale_info::11'}
```
---------
### LatestBeefyBlock

#### Python
```python
result = substrate.query(
    'BeefyLightClient', 'LatestBeefyBlock', [
    (
        'Mainnet',
        'Kusama',
        'Polkadot',
        'Rococo',
        'Alphanet',
        'Liberland',
    ),
]
)
```

#### Return value
```python
'u64'
```
---------
### LatestMMRRoots

#### Python
```python
result = substrate.query(
    'BeefyLightClient', 'LatestMMRRoots', [
    (
        'Mainnet',
        'Kusama',
        'Polkadot',
        'Rococo',
        'Alphanet',
        'Liberland',
    ),
]
)
```

#### Return value
```python
['scale_info::11']
```
---------
### LatestRandomSeed

#### Python
```python
result = substrate.query(
    'BeefyLightClient', 'LatestRandomSeed', [
    (
        'Mainnet',
        'Kusama',
        'Polkadot',
        'Rococo',
        'Alphanet',
        'Liberland',
    ),
]
)
```

#### Return value
```python
('scale_info::11', 'u32')
```
---------
### NextValidatorSet

#### Python
```python
result = substrate.query(
    'BeefyLightClient', 'NextValidatorSet', [
    (
        'Mainnet',
        'Kusama',
        'Polkadot',
        'Rococo',
        'Alphanet',
        'Liberland',
    ),
]
)
```

#### Return value
```python
{'id': 'u64', 'len': 'u32', 'root': 'scale_info::11'}
```
---------
### ThisNetworkId

#### Python
```python
result = substrate.query(
    'BeefyLightClient', 'ThisNetworkId', []
)
```

#### Return value
```python
('Mainnet', 'Kusama', 'Polkadot', 'Rococo', 'Alphanet', 'Liberland')
```
---------
## Errors

---------
### CannotSwitchOldValidatorSet

---------
### CommitmentNotFoundInDigest

---------
### InvalidDigestHash

---------
### InvalidMMRProof

---------
### InvalidNetworkId

---------
### InvalidNumberOfPositions

---------
### InvalidNumberOfPublicKeys

---------
### InvalidNumberOfSignatures

---------
### InvalidSignature

---------
### InvalidValidatorSetId

---------
### MMRPayloadNotFound

---------
### MerklePositionTooHigh

---------
### MerkleProofTooHigh

---------
### MerkleProofTooShort

---------
### NotEnoughValidatorSignatures

---------
### PalletNotInitialized

---------
### PayloadBlocknumberTooNew

---------
### PayloadBlocknumberTooOld

---------
### ValidatorNotOnceInbitfield

---------
### ValidatorSetIncorrectPosition

---------