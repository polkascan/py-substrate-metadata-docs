
# Sidechain

---------
## Calls

---------
### confirm_imported_sidechain_block
See [`Pallet::confirm_imported_sidechain_block`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| block_number | `u64` | 
| next_finalization_candidate_block_number | `u64` | 
| block_header_hash | `H256` | 

#### Python
```python
call = substrate.compose_call(
    'Sidechain', 'confirm_imported_sidechain_block', {
    'block_header_hash': 'scale_info::12',
    'block_number': 'u64',
    'next_finalization_candidate_block_number': 'u64',
    'shard': 'scale_info::12',
}
)
```

---------
## Events

---------
### FinalizedSidechainBlock
a sidechain block has been finalized
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```scale_info::12```
| block_number | `SidechainBlockNumber` | ```u64```
| block_header_hash | `H256` | ```scale_info::12```
| validateer | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### LatestSidechainBlockConfirmation

#### Python
```python
result = substrate.query(
    'Sidechain', 'LatestSidechainBlockConfirmation', ['scale_info::12']
)
```

#### Return value
```python
{'block_header_hash': 'scale_info::12', 'block_number': 'u64'}
```
---------
## Errors

---------
### InvalidNextFinalizationCandidateBlockNumber
The value for the next finalization candidate is invalid.

---------
### ReceivedUnexpectedSidechainBlock
A proposed block is unexpected.

---------