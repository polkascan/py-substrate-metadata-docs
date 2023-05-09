
# Nfts

---------
## Calls

---------
### validate_mint
Validates the proofs provided against the document root associated with the anchor_id.
Once the proofs are verified, we create a bundled hash `(deposit_address + [proof[i].hash])`
Bundled Hash is deposited to an DepositAsset event for bridging purposes.

Adds additional fee to compensate the current cost of target chains
\# &lt;weight&gt;
- depends on the arguments
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| anchor_id | `SystemHashOf<T>` | 
| deposit_address | `DepositAddress` | 
| proofs | `Vec<Proof<HasherHashOf<BundleHasher>>>` | 
| static_proofs | `FixedArray<HasherHashOf<BundleHasher>, 3>` | 
| dest_id | `<T as Config>::ChainId` | 

#### Python
```python
call = substrate.compose_call(
    'Nfts', 'validate_mint', {
    'anchor_id': '[u8; 32]',
    'deposit_address': '[u8; 20]',
    'dest_id': 'u8',
    'proofs': [
        {
            'leaf_hash': '[u8; 32]',
            'sorted_hashes': [
                '[u8; 32]',
            ],
        },
    ],
    'static_proofs': '[[u8; 32]; 3]',
}
)
```

---------
## Events

---------
### DepositAsset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `<T as frame_system::Config>::Hash` | ```[u8; 32]```

---------
## Constants

---------
### NftProofValidationFeeKey
 Additional fee charged for validating NFT proof (when minting a NFT).
#### Value
```python
'NftProofValidation'
```
#### Python
```python
constant = substrate.get_constant('Nfts', 'NftProofValidationFeeKey')
```
---------
### ResourceHashId
 Resource hash id.

 This type was initially declared in the bridge pallet but was moved here
 to avoid circular dependencies.
#### Value
```python
'0x0000000000000000000000000000000cb3858f3e48815bfd35c5347aa3b34c01'
```
#### Python
```python
constant = substrate.get_constant('Nfts', 'ResourceHashId')
```
---------
## Errors

---------
### DocumentNotAnchored
A given document id does not match a corresponding document in the anchor storage.

---------
### InvalidProofs
Unable to recreate the anchor hash from the proofs and data provided.

---------