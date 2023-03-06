
# BridgeKusamaParachain

---------
## Calls

---------
### submit_parachain_heads
Submit proof of one or several parachain heads.

The proof is supposed to be proof of some `Heads` entries from the
`polkadot-runtime-parachains::paras` pallet instance, deployed at the bridged chain.
The proof is supposed to be crafted at the `relay_header_hash` that must already be
imported by corresponding GRANDPA pallet at this chain.
#### Attributes
| Name | Type |
| -------- | -------- | 
| relay_block_hash | `RelayBlockHash` | 
| parachains | `Vec<ParaId>` | 
| parachain_heads_proof | `ParachainHeadsProof` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeKusamaParachain', 'submit_parachain_heads', {
    'parachain_heads_proof': ['Bytes'],
    'parachains': ['u32'],
    'relay_block_hash': '[u8; 32]',
}
)
```

---------
## Storage functions

---------
### BestParaHeads
 Best parachain heads.

#### Python
```python
result = substrate.query(
    'BridgeKusamaParachain', 'BestParaHeads', ['u32']
)
```

#### Return value
```python
{
    'at_relay_block_number': 'u32',
    'head_hash': '[u8; 32]',
    'next_imported_hash_position': 'u32',
}
```
---------
### ImportedParaHashes
 A ring buffer of imported parachain head hashes. Ordered by the insertion time.

#### Python
```python
result = substrate.query(
    'BridgeKusamaParachain', 'ImportedParaHashes', ['u32', 'u32']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### ImportedParaHeads
 Parachain heads which have been imported into the pallet.

#### Python
```python
result = substrate.query(
    'BridgeKusamaParachain', 'ImportedParaHeads', ['u32', '[u8; 32]']
)
```

#### Return value
```python
'Bytes'
```
---------
## Constants

---------
### HeadsToKeep
 Maximal number of single parachain heads to keep in the storage.

 The setting is there to prevent growing the on-chain state indefinitely. Note
 the setting does not relate to parachain block numbers - we will simply keep as much
 items in the storage, so it doesn&#x27;t guarantee any fixed timeframe for heads.
#### Value
```python
500
```
#### Python
```python
constant = substrate.get_constant('BridgeKusamaParachain', 'HeadsToKeep')
```
---------
## Errors

---------
### FailedToExtractStateRoot
Failed to extract state root from given parachain head.

---------
### InvalidStorageProof
Invalid storage proof has been passed.

---------
### StorageRootMismatch
The storage proof doesn&\#x27;t contains storage root. So it is invalid for given header.

---------
### UnknownParaHead
Given parachain head is unknown.

---------
### UnknownRelayChainBlock
Relay chain block is unknown to us.

---------