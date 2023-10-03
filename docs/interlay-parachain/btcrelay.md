
# BTCRelay

---------
## Calls

---------
### initialize
One time function to initialize the BTC-Relay with the first block

\# Arguments

* `block_header` - Bitcoin block header.
* `block_height` - starting Bitcoin block height of the submitted block header.

\#\# Complexity
- O(1)
#### Attributes
| Name | Type |
| -------- | -------- | 
| block_header | `BlockHeader` | 
| block_height | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'BTCRelay', 'initialize', {
    'block_header': {
        'hash': {
            'content': '[u8; 32]',
        },
        'hash_prev_block': {
            'content': '[u8; 32]',
        },
        'merkle_root': {
            'content': '[u8; 32]',
        },
        'nonce': 'u32',
        'target': '[u64; 4]',
        'timestamp': 'u32',
        'version': 'i32',
    },
    'block_height': 'u32',
}
)
```

---------
### store_block_header
Stores a single new block header

\# Arguments

* `block_header` - Bitcoin block header.

\#\# Complexity
- `O(F)` where `F` is the number of forks
#### Attributes
| Name | Type |
| -------- | -------- | 
| block_header | `BlockHeader` | 
| fork_bound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'BTCRelay', 'store_block_header', {
    'block_header': {
        'hash': {
            'content': '[u8; 32]',
        },
        'hash_prev_block': {
            'content': '[u8; 32]',
        },
        'merkle_root': {
            'content': '[u8; 32]',
        },
        'nonce': 'u32',
        'target': '[u64; 4]',
        'timestamp': 'u32',
        'version': 'i32',
    },
    'fork_bound': 'u32',
}
)
```

---------
## Events

---------
### ChainReorg
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| new_chain_tip_hash | `H256Le` | ```{'content': '[u8; 32]'}```
| new_chain_tip_height | `u32` | ```u32```
| fork_depth | `u32` | ```u32```

---------
### ForkAheadOfMainChain
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| main_chain_height | `u32` | ```u32```
| fork_height | `u32` | ```u32```
| fork_id | `u32` | ```u32```

---------
### Initialized
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| block_height | `u32` | ```u32```
| block_hash | `H256Le` | ```{'content': '[u8; 32]'}```
| relayer_id | `T::AccountId` | ```AccountId```

---------
### StoreForkHeader
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| chain_id | `u32` | ```u32```
| fork_height | `u32` | ```u32```
| block_hash | `H256Le` | ```{'content': '[u8; 32]'}```
| relayer_id | `T::AccountId` | ```AccountId```

---------
### StoreMainChainHeader
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| block_height | `u32` | ```u32```
| block_hash | `H256Le` | ```{'content': '[u8; 32]'}```
| relayer_id | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### BestBlock
 Store the current blockchain tip

#### Python
```python
result = substrate.query(
    'BTCRelay', 'BestBlock', []
)
```

#### Return value
```python
{'content': '[u8; 32]'}
```
---------
### BestBlockHeight
 Store the height of the best block

#### Python
```python
result = substrate.query(
    'BTCRelay', 'BestBlockHeight', []
)
```

#### Return value
```python
'u32'
```
---------
### BlockHeaders
 Store Bitcoin block headers

#### Python
```python
result = substrate.query(
    'BTCRelay', 'BlockHeaders', [{'content': '[u8; 32]'}]
)
```

#### Return value
```python
{
    'block_header': {
        'hash': {'content': '[u8; 32]'},
        'hash_prev_block': {'content': '[u8; 32]'},
        'merkle_root': {'content': '[u8; 32]'},
        'nonce': 'u32',
        'target': '[u64; 4]',
        'timestamp': 'u32',
        'version': 'i32',
    },
    'block_height': 'u32',
    'chain_id': 'u32',
    'para_height': 'u32',
}
```
---------
### ChainCounter
 Increment-only counter used to track new BlockChain entries

#### Python
```python
result = substrate.query(
    'BTCRelay', 'ChainCounter', []
)
```

#### Return value
```python
'u32'
```
---------
### Chains
 Priority queue of BlockChain elements, ordered by the maximum height (descending).
 The first index into this mapping (0) is considered to be the longest chain. The value
 of the entry is the index into `ChainsIndex` to retrieve the `BlockChain`.

#### Python
```python
result = substrate.query(
    'BTCRelay', 'Chains', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### ChainsHashes
 Stores a mapping from (chain_index, block_height) to block hash

#### Python
```python
result = substrate.query(
    'BTCRelay', 'ChainsHashes', ['u32', 'u32']
)
```

#### Return value
```python
{'content': '[u8; 32]'}
```
---------
### ChainsIndex
 Auxiliary mapping of chains ids to `BlockChain` entries. The first index into this
 mapping (0) is considered to be the Bitcoin main chain.

#### Python
```python
result = substrate.query(
    'BTCRelay', 'ChainsIndex', ['u32']
)
```

#### Return value
```python
{'chain_id': 'u32', 'max_height': 'u32', 'start_height': 'u32'}
```
---------
### DisableDifficultyCheck
 Whether the module should perform difficulty checks.

#### Python
```python
result = substrate.query(
    'BTCRelay', 'DisableDifficultyCheck', []
)
```

#### Return value
```python
'bool'
```
---------
### DisableInclusionCheck
 Whether the module should perform inclusion checks.

#### Python
```python
result = substrate.query(
    'BTCRelay', 'DisableInclusionCheck', []
)
```

#### Return value
```python
'bool'
```
---------
### StableBitcoinConfirmations
 Global security parameter k for stable Bitcoin transactions

#### Python
```python
result = substrate.query(
    'BTCRelay', 'StableBitcoinConfirmations', []
)
```

#### Return value
```python
'u32'
```
---------
### StableParachainConfirmations
 Global security parameter k for stable Parachain transactions

#### Python
```python
result = substrate.query(
    'BTCRelay', 'StableParachainConfirmations', []
)
```

#### Return value
```python
'u32'
```
---------
### StartBlockHeight
 BTC height when the relay was initialized

#### Python
```python
result = substrate.query(
    'BTCRelay', 'StartBlockHeight', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### ParachainBlocksPerBitcoinBlock
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('BTCRelay', 'ParachainBlocksPerBitcoinBlock')
```
---------
## Errors

---------
### AlreadyInitialized
Already initialized

---------
### AlreadyReported
Error code already reported

---------
### ArithmeticOverflow
Arithmetic overflow

---------
### ArithmeticUnderflow
Arithmetic underflow

---------
### BitcoinConfirmations
Transaction has less confirmations of Bitcoin blocks than required

---------
### BlockHeightOverflow
Overflow of block height

---------
### BlockNotFound
Block header not found for given hash

---------
### BoundExceeded
Weight bound exceeded

---------
### ChainCounterOverflow
Overflow of chain counter

---------
### ChainsUnderflow
Underflow of stored blockchains counter

---------
### DiffTargetHeader
Incorrect difficulty target specified in block header

---------
### DuplicateBlock
Block already stored

---------
### EndOfFile
EndOfFile reached while parsing

---------
### ForkIdNotFound
Blockchain with requested ID not found

---------
### InvalidBlockVersion
Invalid block header version

---------
### InvalidBtcAddress
Specified invalid Bitcoin address

---------
### InvalidBtcHash
User supplied an invalid address

---------
### InvalidChainID
Invalid chain ID

---------
### InvalidCoinbasePosition
Coinbase tx must be the first transaction in the block

---------
### InvalidCompact
Invalid compact value in header

---------
### InvalidHeaderSize
Invalid block header size

---------
### InvalidMerkleProof
Invalid merkle proof

---------
### InvalidOpReturn
Incorrect identifier in OP_RETURN field

---------
### InvalidOpReturnTransaction
Transaction does meet the requirements to be a valid op-return payment

---------
### InvalidOutputFormat
Incorrect transaction output format

---------
### InvalidPayment
Incorrect recipient Bitcoin address

---------
### InvalidPaymentAmount
Invalid payment amount

---------
### InvalidScript
User supplied an invalid script

---------
### InvalidStartHeight
Start height must be start of difficulty period

---------
### InvalidTransaction
Transaction does meet the requirements to be considered valid

---------
### InvalidTxVersion
Invalid transaction version

---------
### InvalidTxid
Transaction hash does not match given txid

---------
### LowDiff
PoW hash does not meet difficulty target of header

---------
### MalformedHeader
Format of the header is invalid

---------
### MalformedMerkleProof
Merkle proof is malformed

---------
### MalformedOpReturnOutput
Format of the OP_RETURN transaction output is invalid

---------
### MalformedP2PKHOutput

---------
### MalformedP2SHOutput

---------
### MalformedTransaction
Transaction has incorrect format

---------
### MalformedTxid
Malformed transaction identifier

---------
### MalformedWitnessOutput
Format of the BIP141 witness transaction output is invalid

---------
### MissingBlockHeight
Missing the block at this height

---------
### OngoingFork
Current fork ongoing

---------
### ParachainConfirmations
Transaction has less confirmations of Parachain blocks than required

---------
### PrevBlock
Previous block hash not found

---------
### Shutdown
BTC Parachain has shut down

---------
### TryIntoIntError
TryInto failed on integer

---------
### UnauthorizedRelayer
Unauthorized staked relayer

---------
### UnknownErrorcode
Error code not applicable to blocks

---------
### UnsupportedInputFormat

---------
### UnsupportedOutputFormat

---------
### WrongForkBound
Wrong fork bound, should be higher

---------