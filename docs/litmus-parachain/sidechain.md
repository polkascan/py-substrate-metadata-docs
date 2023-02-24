
# Sidechain

---------
## Calls

---------
### confirm_imported_sidechain_block
The integritee worker calls this function for every imported sidechain_block.
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard_id | `ShardIdentifier` | 
| block_number | `u64` | 
| block_header_hash | `H256` | 

#### Python
```python
call = substrate.compose_call(
    'Sidechain', 'confirm_imported_sidechain_block', {
    'block_header_hash': '[u8; 32]',
    'block_number': 'u64',
    'shard_id': '[u8; 32]',
}
)
```

---------
## Events

---------
### FinalizedSidechainBlock
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `H256` | ```[u8; 32]```

---------
### ProposedSidechainBlock
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `H256` | ```[u8; 32]```

---------
## Storage functions

---------
### LatestSidechainBlockConfirmation

#### Python
```python
result = substrate.query(
    'Sidechain', 'LatestSidechainBlockConfirmation', ['[u8; 32]']
)
```

#### Return value
```python
{'block_header_hash': '[u8; 32]', 'block_number': 'u64'}
```
---------
### SidechainBlockConfirmationQueue

#### Python
```python
result = substrate.query(
    'Sidechain', 'SidechainBlockConfirmationQueue', [('[u8; 32]', 'u64')]
)
```

#### Return value
```python
{'block_header_hash': '[u8; 32]', 'block_number': 'u64'}
```
---------
### WorkerForShard

#### Python
```python
result = substrate.query(
    'Sidechain', 'WorkerForShard', ['[u8; 32]']
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### EarlyBlockProposalLenience
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Sidechain', 'EarlyBlockProposalLenience')
```
---------
## Errors

---------
### BlockNumberTooHigh
A proposed block is too early.

---------
### OutdatedBlockNumber
A propsed block is too late and already outdated.

---------