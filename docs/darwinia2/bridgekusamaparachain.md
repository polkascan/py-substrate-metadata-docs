
# BridgeKusamaParachain

---------
## Calls

---------
### set_operating_mode
Halt or resume all pallet operations.

May only be called either by root, or by `PalletOwner`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| operating_mode | `BasicOperatingMode` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeKusamaParachain', 'set_operating_mode', {
    'operating_mode': (
        'Normal',
        'Halted',
    ),
}
)
```

---------
### set_owner
Change `PalletOwner`.

May only be called either by root, or by `PalletOwner`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_owner | `Option<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeKusamaParachain', 'set_owner', {'new_owner': (None, '[u8; 20]')}
)
```

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
| at_relay_block | `(RelayBlockNumber, RelayBlockHash)` | 
| parachains | `Vec<(ParaId, ParaHash)>` | 
| parachain_heads_proof | `ParaHeadsProof` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeKusamaParachain', 'submit_parachain_heads', {
    'at_relay_block': (
        'u32',
        '[u8; 32]',
    ),
    'parachain_heads_proof': ['Bytes'],
    'parachains': [('u32', '[u8; 32]')],
}
)
```

---------
## Events

---------
### IncorrectParachainHeadHash
The caller has provided parachain head hash that is not matching the hash read from the
storage proof.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| parachain | `ParaId` | ```u32```
| parachain_head_hash | `ParaHash` | ```[u8; 32]```
| actual_parachain_head_hash | `ParaHash` | ```[u8; 32]```

---------
### MissingParachainHead
The caller has declared that he has provided given parachain head, but it is missing
from the storage proof.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| parachain | `ParaId` | ```u32```

---------
### RejectedLargeParachainHead
The caller has provided parachain head that exceeds the maximal configured head size.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| parachain | `ParaId` | ```u32```
| parachain_head_hash | `ParaHash` | ```[u8; 32]```
| parachain_head_size | `u32` | ```u32```

---------
### RejectedObsoleteParachainHead
The caller has provided obsolete parachain head, which is already known to the pallet.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| parachain | `ParaId` | ```u32```
| parachain_head_hash | `ParaHash` | ```[u8; 32]```

---------
### UntrackedParachainRejected
The caller has provided head of parachain that the pallet is not configured to track.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| parachain | `ParaId` | ```u32```

---------
### UpdatedParachainHead
Parachain head has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| parachain | `ParaId` | ```u32```
| parachain_head_hash | `ParaHash` | ```[u8; 32]```

---------
## Storage functions

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
### PalletOperatingMode
 The current operating mode of the pallet.

 Depending on the mode either all, or no transactions will be allowed.

#### Python
```python
result = substrate.query(
    'BridgeKusamaParachain', 'PalletOperatingMode', []
)
```

#### Return value
```python
('Normal', 'Halted')
```
---------
### PalletOwner
 Optional pallet owner.

 Pallet owner has a right to halt all pallet operations and then resume them. If it is
 `None`, then there are no direct ways to halt/resume pallet operations, but other
 runtime methods may still be used to do that (i.e. democracy::referendum to update halt
 flag directly or call the `halt_operations`).

#### Python
```python
result = substrate.query(
    'BridgeKusamaParachain', 'PalletOwner', []
)
```

#### Return value
```python
'[u8; 20]'
```
---------
### ParasInfo
 Parachains info.

 Contains the following info:
 - best parachain head hash
 - the head of the `ImportedParaHashes` ring buffer

#### Python
```python
result = substrate.query(
    'BridgeKusamaParachain', 'ParasInfo', ['u32']
)
```

#### Return value
```python
{'best_head_hash': {'at_relay_block_number': 'u32', 'head_hash': '[u8; 32]'}, 'next_imported_hash_position': 'u32'}
```
---------
## Constants

---------
### HeadsToKeep
 Maximal number of single parachain heads to keep in the storage.

 The setting is there to prevent growing the on-chain state indefinitely. Note
 the setting does not relate to parachain block numbers - we will simply keep as much
 items in the storage, so it doesn&#x27;t guarantee any fixed timeframe for heads.

 Incautious change of this constant may lead to orphan entries in the runtime storage.
#### Value
```python
500
```
#### Python
```python
constant = substrate.get_constant('BridgeKusamaParachain', 'HeadsToKeep')
```
---------
### MaxParaHeadSize
 Maximal size (in bytes) of the SCALE-encoded parachain head.

 Keep in mind that the size of any tracked parachain header must not exceed this value.
 So if you&#x27;re going to track multiple parachains, one of which is storing large digests
 in its headers, you shall choose this maximal value.

 There&#x27;s no mandatory headers in this pallet, so it can&#x27;t stall if there&#x27;s some header
 that exceeds this bound.
#### Value
```python
1024
```
#### Python
```python
constant = substrate.get_constant('BridgeKusamaParachain', 'MaxParaHeadSize')
```
---------
### ParasPalletName
 Name of the original `paras` pallet in the `construct_runtime!()` call at the bridged
 chain.

 Please keep in mind that this should be the name of the `runtime_parachains::paras`
 pallet from polkadot repository, not the `pallet-bridge-parachains`.
#### Value
```python
'Paras'
```
#### Python
```python
constant = substrate.get_constant('BridgeKusamaParachain', 'ParasPalletName')
```
---------
## Errors

---------
### BridgeModule
Error generated by the `OwnedBridgeModule` trait.

---------
### FailedToExtractStateRoot
Failed to extract state root from given parachain head.

---------
### InvalidRelayChainBlockNumber
The number of stored relay block is different from what the relayer has provided.

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
Relay chain block hash is unknown to us.

---------