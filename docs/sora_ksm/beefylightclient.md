
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
    'network_id': {
        'Custom': 'u32',
        'Kusama': None,
        'Mainnet': None,
        'Polkadot': None,
        'Rococo': None,
    },
    'next_validator_set': {
        'id': 'u64',
        'len': 'u32',
        'root': '[u8; 32]',
    },
    'validator_set': {
        'id': 'u64',
        'len': 'u32',
        'root': '[u8; 32]',
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
            'root': '[u8; 32]',
        },
        'leaf_extra': {
            'digest_hash': '[u8; 32]',
            'random_seed': '[u8; 32]',
        },
        'parent_number_and_hash': (
            'u32',
            '[u8; 32]',
        ),
        'version': 'u8',
    },
    'network_id': {
        'Custom': 'u32',
        'Kusama': None,
        'Mainnet': None,
        'Polkadot': None,
        'Rococo': None,
    },
    'proof': {
        'items': ['[u8; 32]'],
        'order': 'u64',
    },
    'validator_proof': {
        'positions': ['u128'],
        'public_key_merkle_proofs': [
            ['[u8; 32]'],
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
| None | `SubNetworkId` | ```{'Mainnet': None, 'Kusama': None, 'Polkadot': None, 'Rococo': None, 'Custom': 'u32'}```
| None | `H256` | ```[u8; 32]```
| None | `u64` | ```u64```

---------
### ValidatorRegistryUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SubNetworkId` | ```{'Mainnet': None, 'Kusama': None, 'Polkadot': None, 'Rococo': None, 'Custom': 'u32'}```
| None | `H256` | ```[u8; 32]```
| None | `u32` | ```u32```
| None | `u64` | ```u64```

---------
### VerificationSuccessful
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SubNetworkId` | ```{'Mainnet': None, 'Kusama': None, 'Polkadot': None, 'Rococo': None, 'Custom': 'u32'}```
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
    {
        'Custom': 'u32',
        'Kusama': None,
        'Mainnet': None,
        'Polkadot': None,
        'Rococo': None,
    },
]
)
```

#### Return value
```python
{'id': 'u64', 'len': 'u32', 'root': '[u8; 32]'}
```
---------
### LatestBeefyBlock

#### Python
```python
result = substrate.query(
    'BeefyLightClient', 'LatestBeefyBlock', [
    {
        'Custom': 'u32',
        'Kusama': None,
        'Mainnet': None,
        'Polkadot': None,
        'Rococo': None,
    },
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
    {
        'Custom': 'u32',
        'Kusama': None,
        'Mainnet': None,
        'Polkadot': None,
        'Rococo': None,
    },
]
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### LatestRandomSeed

#### Python
```python
result = substrate.query(
    'BeefyLightClient', 'LatestRandomSeed', [
    {
        'Custom': 'u32',
        'Kusama': None,
        'Mainnet': None,
        'Polkadot': None,
        'Rococo': None,
    },
]
)
```

#### Return value
```python
('[u8; 32]', 'u32')
```
---------
### NextValidatorSet

#### Python
```python
result = substrate.query(
    'BeefyLightClient', 'NextValidatorSet', [
    {
        'Custom': 'u32',
        'Kusama': None,
        'Mainnet': None,
        'Polkadot': None,
        'Rococo': None,
    },
]
)
```

#### Return value
```python
{'id': 'u64', 'len': 'u32', 'root': '[u8; 32]'}
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
{
    'Custom': 'u32',
    'Kusama': None,
    'Mainnet': None,
    'Polkadot': None,
    'Rococo': None,
}
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