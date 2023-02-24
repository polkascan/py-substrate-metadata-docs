
# Contracts

---------
## Calls

---------
### call
Makes a call to an account, optionally transferring some balance.

\# Parameters

* `dest`: Address of the contract to call.
* `value`: The balance to transfer from the `origin` to `dest`.
* `gas_limit`: The gas limit enforced when executing the constructor.
* `storage_deposit_limit`: The maximum amount of balance that can be charged from the
  caller to pay for the storage consumed.
* `data`: The input data to pass to the contract.

* If the account is a smart-contract account, the associated code will be
executed and any value will be transferred.
* If the account is a regular account, any value will be transferred.
* If no account exists and the call value is not less than `existential_deposit`,
a regular account will be created and any value will be transferred.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `AccountIdLookupOf<T>` | 
| value | `BalanceOf<T>` | 
| gas_limit | `Weight` | 
| storage_deposit_limit | `Option<<BalanceOf<T> as codec::HasCompact>::Type>` | 
| data | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Contracts', 'call', {
    'data': 'Bytes',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'gas_limit': {'ref_time': 'u64'},
    'storage_deposit_limit': (
        None,
        'u128',
    ),
    'value': 'u128',
}
)
```

---------
### instantiate
Instantiates a contract from a previously deployed wasm binary.

This function is identical to [`Self::instantiate_with_code`] but without the
code deployment step. Instead, the `code_hash` of an on-chain deployed wasm binary
must be supplied.
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `BalanceOf<T>` | 
| gas_limit | `Weight` | 
| storage_deposit_limit | `Option<<BalanceOf<T> as codec::HasCompact>::Type>` | 
| code_hash | `CodeHash<T>` | 
| data | `Vec<u8>` | 
| salt | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Contracts', 'instantiate', {
    'code_hash': '[u8; 32]',
    'data': 'Bytes',
    'gas_limit': {'ref_time': 'u64'},
    'salt': 'Bytes',
    'storage_deposit_limit': (
        None,
        'u128',
    ),
    'value': 'u128',
}
)
```

---------
### instantiate_with_code
Instantiates a new contract from the supplied `code` optionally transferring
some balance.

This dispatchable has the same effect as calling [`Self::upload_code`] +
[`Self::instantiate`]. Bundling them together provides efficiency gains. Please
also check the documentation of [`Self::upload_code`].

\# Parameters

* `value`: The balance to transfer from the `origin` to the newly created contract.
* `gas_limit`: The gas limit enforced when executing the constructor.
* `storage_deposit_limit`: The maximum amount of balance that can be charged/reserved
  from the caller to pay for the storage consumed.
* `code`: The contract code to deploy in raw bytes.
* `data`: The input data to pass to the contract constructor.
* `salt`: Used for the address derivation. See [`Pallet::contract_address`].

Instantiation is executed as follows:

- The supplied `code` is instrumented, deployed, and a `code_hash` is created for that
  code.
- If the `code_hash` already exists on the chain the underlying `code` will be shared.
- The destination address is computed based on the sender, code_hash and the salt.
- The smart-contract account is created at the computed address.
- The `value` is transferred to the new account.
- The `deploy` function is executed in the context of the newly-created account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `BalanceOf<T>` | 
| gas_limit | `Weight` | 
| storage_deposit_limit | `Option<<BalanceOf<T> as codec::HasCompact>::Type>` | 
| code | `Vec<u8>` | 
| data | `Vec<u8>` | 
| salt | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Contracts', 'instantiate_with_code', {
    'code': 'Bytes',
    'data': 'Bytes',
    'gas_limit': {'ref_time': 'u64'},
    'salt': 'Bytes',
    'storage_deposit_limit': (
        None,
        'u128',
    ),
    'value': 'u128',
}
)
```

---------
### remove_code
Remove the code stored under `code_hash` and refund the deposit to its owner.

A code can only be removed by its original uploader (its owner) and only if it is
not used by any contract.
#### Attributes
| Name | Type |
| -------- | -------- | 
| code_hash | `CodeHash<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Contracts', 'remove_code', {'code_hash': '[u8; 32]'}
)
```

---------
### set_code
Privileged function that changes the code of an existing contract.

This takes care of updating refcounts and all other necessary operations. Returns
an error if either the `code_hash` or `dest` do not exist.

\# Note

This does **not** change the address of the contract in question. This means
that the contract address is no longer derived from its code hash after calling
this dispatchable.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `AccountIdLookupOf<T>` | 
| code_hash | `CodeHash<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Contracts', 'set_code', {
    'code_hash': '[u8; 32]',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### upload_code
Upload new `code` without instantiating a contract from it.

If the code does not already exist a deposit is reserved from the caller
and unreserved only when [`Self::remove_code`] is called. The size of the reserve
depends on the instrumented size of the the supplied `code`.

If the code already exists in storage it will still return `Ok` and upgrades
the in storage version to the current
[`InstructionWeights::version`](InstructionWeights).

\# Note

Anyone can instantiate a contract from any uploaded code and thus prevent its removal.
To avoid this situation a constructor could employ access control so that it can
only be instantiated by permissioned entities. The same is true when uploading
through [`Self::instantiate_with_code`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| code | `Vec<u8>` | 
| storage_deposit_limit | `Option<<BalanceOf<T> as codec::HasCompact>::Type>` | 

#### Python
```python
call = substrate.compose_call(
    'Contracts', 'upload_code', {
    'code': 'Bytes',
    'storage_deposit_limit': (
        None,
        'u128',
    ),
}
)
```

---------
## Events

---------
### Called
A contract was called either by a plain account or another contract.

\# Note

Please keep in mind that like all events this is only emitted for successful
calls. This is because on failure all storage changes including events are
rolled back.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| caller | `T::AccountId` | ```AccountId```
| contract | `T::AccountId` | ```AccountId```

---------
### CodeRemoved
A code with the specified hash was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| code_hash | `T::Hash` | ```[u8; 32]```

---------
### CodeStored
Code with the specified hash has been stored.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| code_hash | `T::Hash` | ```[u8; 32]```

---------
### ContractCodeUpdated
A contract&\#x27;s code was updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| contract | `T::AccountId` | ```AccountId```
| new_code_hash | `T::Hash` | ```[u8; 32]```
| old_code_hash | `T::Hash` | ```[u8; 32]```

---------
### ContractEmitted
A custom event emitted by the contract.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| contract | `T::AccountId` | ```AccountId```
| data | `Vec<u8>` | ```Bytes```

---------
### DelegateCalled
A contract delegate called a code hash.

\# Note

Please keep in mind that like all events this is only emitted for successful
calls. This is because on failure all storage changes including events are
rolled back.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| contract | `T::AccountId` | ```AccountId```
| code_hash | `CodeHash<T>` | ```[u8; 32]```

---------
### Instantiated
Contract deployed by address at the specified address.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| deployer | `T::AccountId` | ```AccountId```
| contract | `T::AccountId` | ```AccountId```

---------
### Terminated
Contract has been removed.

\# Note

The only way for a contract to be removed and emitting this event is by calling
`seal_terminate`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| contract | `T::AccountId` | ```AccountId```
| beneficiary | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### CodeStorage
 A mapping between an original code hash and instrumented wasm code, ready for execution.

#### Python
```python
result = substrate.query(
    'Contracts', 'CodeStorage', ['[u8; 32]']
)
```

#### Return value
```python
{
    'code': 'Bytes',
    'initial': 'u32',
    'instruction_weights_version': 'u32',
    'maximum': 'u32',
}
```
---------
### ContractInfoOf
 The code associated with a given account.

 TWOX-NOTE: SAFE since `AccountId` is a secure hash.

#### Python
```python
result = substrate.query(
    'Contracts', 'ContractInfoOf', ['AccountId']
)
```

#### Return value
```python
{
    'code_hash': '[u8; 32]',
    'storage_base_deposit': 'u128',
    'storage_byte_deposit': 'u128',
    'storage_bytes': 'u32',
    'storage_item_deposit': 'u128',
    'storage_items': 'u32',
    'trie_id': 'Bytes',
}
```
---------
### DeletionQueue
 Evicted contracts that await child trie deletion.

 Child trie deletion is a heavy operation depending on the amount of storage items
 stored in said trie. Therefore this operation is performed lazily in `on_initialize`.

#### Python
```python
result = substrate.query(
    'Contracts', 'DeletionQueue', []
)
```

#### Return value
```python
[{'trie_id': 'Bytes'}]
```
---------
### Nonce
 This is a **monotonic** counter incremented on contract instantiation.

 This is used in order to generate unique trie ids for contracts.
 The trie id of a new contract is calculated from hash(account_id, nonce).
 The nonce is required because otherwise the following sequence would lead to
 a possible collision of storage:

 1. Create a new contract.
 2. Terminate the contract.
 3. Immediately recreate the contract with the same account_id.

 This is bad because the contents of a trie are deleted lazily and there might be
 storage of the old instantiation still in it when the new contract is created. Please
 note that we can&#x27;t replace the counter by the block number because the sequence above
 can happen in the same block. We also can&#x27;t keep the account counter in memory only
 because storage is the only way to communicate across different extrinsics in the
 same block.

 \# Note

 Do not use it to determine the number of contracts. It won&#x27;t be decremented if
 a contract is destroyed.

#### Python
```python
result = substrate.query(
    'Contracts', 'Nonce', []
)
```

#### Return value
```python
'u64'
```
---------
### OwnerInfoOf
 A mapping between an original code hash and its owner information.

#### Python
```python
result = substrate.query(
    'Contracts', 'OwnerInfoOf', ['[u8; 32]']
)
```

#### Return value
```python
{'deposit': 'u128', 'owner': 'AccountId', 'refcount': 'u64'}
```
---------
### PristineCode
 A mapping from an original code hash to the original code, untouched by instrumentation.

#### Python
```python
result = substrate.query(
    'Contracts', 'PristineCode', ['[u8; 32]']
)
```

#### Return value
```python
'Bytes'
```
---------
## Constants

---------
### ContractAccessWeight
 The weight per byte of code that is charged when loading a contract from storage.

 Currently, FRAME only charges fees for computation incurred but not for PoV
 consumption caused for storage access. This is usually not exploitable because
 accessing storage carries some substantial weight costs, too. However in case
 of contract code very much PoV consumption can be caused while consuming very little
 computation. This could be used to keep the chain busy without paying the
 proper fee for it. Until this is resolved we charge from the weight meter for
 contract access.

 For more information check out: &lt;https://github.com/paritytech/substrate/issues/10301&gt;

 [`DefaultContractAccessWeight`] is a safe default to be used for Polkadot or Kusama
 parachains.

 \# Note

 This is only relevant for parachains. Set to zero in case of a standalone chain.
#### Value
```python
{'ref_time': 286102}
```
#### Python
```python
constant = substrate.get_constant('Contracts', 'ContractAccessWeight')
```
---------
### DeletionQueueDepth
 The maximum number of contracts that can be pending for deletion.

 When a contract is deleted by calling `seal_terminate` it becomes inaccessible
 immediately, but the deletion of the storage items it has accumulated is performed
 later. The contract is put into the deletion queue. This defines how many
 contracts can be queued up at the same time. If that limit is reached `seal_terminate`
 will fail. The action must be retried in a later block in that case.

 The reasons for limiting the queue depth are:

 1. The queue is in storage in order to be persistent between blocks. We want to limit
 	the amount of storage that can be consumed.
 2. The queue is stored in a vector and needs to be decoded as a whole when reading
		it at the end of each block. Longer queues take more weight to decode and hence
		limit the amount of items that can be deleted per block.
#### Value
```python
230591
```
#### Python
```python
constant = substrate.get_constant('Contracts', 'DeletionQueueDepth')
```
---------
### DeletionWeightLimit
 The maximum amount of weight that can be consumed per block for lazy trie removal.

 The amount of weight that is dedicated per block to work on the deletion queue. Larger
 values allow more trie keys to be deleted in each block but reduce the amount of
 weight that is left for transactions. See [`Self::DeletionQueueDepth`] for more
 information about the deletion queue.
#### Value
```python
{'ref_time': 1500000000000}
```
#### Python
```python
constant = substrate.get_constant('Contracts', 'DeletionWeightLimit')
```
---------
### DepositPerByte
 The amount of balance a caller has to pay for each byte of storage.

 \# Note

 Changing this value for an existing chain might need a storage migration.
#### Value
```python
50000000000000
```
#### Python
```python
constant = substrate.get_constant('Contracts', 'DepositPerByte')
```
---------
### DepositPerItem
 The amount of balance a caller has to pay for each storage item.

 \# Note

 Changing this value for an existing chain might need a storage migration.
#### Value
```python
1000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Contracts', 'DepositPerItem')
```
---------
### Schedule
 Cost schedule and limits.
#### Value
```python
{
    'host_fn_weights': {
        'address': 442525,
        'balance': 1377950,
        'block_number': 432650,
        'call': 468816012,
        'call_per_cloned_byte': 121637,
        'call_transfer_surcharge': 141047725,
        'caller': 442662,
        'caller_is_origin': 197825,
        'clear_storage': 130084975,
        'clear_storage_per_byte': 11544,
        'code_hash': 28362287,
        'contains_storage': 28817512,
        'contains_storage_per_byte': 2892,
        'debug_message': 331700,
        'delegate_call': 365235837,
        'deposit_event': 3029212,
        'deposit_event_per_byte': 822,
        'deposit_event_per_topic': 127204062,
        'ecdsa_recover': 37107962,
        'ecdsa_to_eth_address': 25775162,
        'gas': 195437,
        'gas_left': 439300,
        'get_storage': 29128050,
        'get_storage_per_byte': 4004,
        'hash_blake2_128': 560587,
        'hash_blake2_128_per_byte': 1189,
        'hash_blake2_256': 564612,
        'hash_blake2_256_per_byte': 1189,
        'hash_keccak_256': 845325,
        'hash_keccak_256_per_byte': 3024,
        'hash_sha2_256': 688337,
        'hash_sha2_256_per_byte': 3910,
        'input': 418462,
        'input_per_byte': 117,
        'instantiate': 910381512,
        'instantiate_per_salt_byte': 1539,
        'instantiate_transfer_surcharge': 1525,
        'is_contract': 27588837,
        'minimum_balance': 438762,
        'now': 434750,
        'own_code_hash': 484962,
        'r#return': 2090000,
        'random': 1717575,
        'return_per_byte': 179,
        'set_code_hash': 260615237,
        'set_storage': 130209787,
        'set_storage_per_new_byte': 11826,
        'set_storage_per_old_byte': 11520,
        'take_storage': 130367487,
        'take_storage_per_byte': 12659,
        'terminate': 777855000,
        'transfer': 142091337,
        'value_transferred': 440200,
        'weight_to_fee': 1247837,
    },
    'instruction_weights': {
        'br': 7060,
        'br_if': 7425,
        'br_table': 9425,
        'br_table_per_entry': 30,
        'call': 64000,
        'call_indirect': 78055,
        'call_indirect_per_param': 795,
        'global_get': 10285,
        'global_set': 10795,
        'i32wrapi64': 4230,
        'i64add': 4265,
        'i64and': 4445,
        'i64clz': 4250,
        'i64const': 4665,
        'i64ctz': 4330,
        'i64divs': 11565,
        'i64divu': 8905,
        'i64eq': 4235,
        'i64eqz': 4210,
        'i64extendsi32': 4220,
        'i64extendui32': 4250,
        'i64ges': 4265,
        'i64geu': 4335,
        'i64gts': 4255,
        'i64gtu': 4275,
        'i64les': 4315,
        'i64leu': 4295,
        'i64load': 20440,
        'i64lts': 4345,
        'i64ltu': 4185,
        'i64mul': 4255,
        'i64ne': 4155,
        'i64or': 4445,
        'i64popcnt': 4230,
        'i64rems': 11505,
        'i64remu': 9405,
        'i64rotl': 4795,
        'i64rotr': 4615,
        'i64shl': 4415,
        'i64shrs': 4505,
        'i64shru': 4455,
        'i64store': 17530,
        'i64sub': 4305,
        'i64xor': 4365,
        'local_get': 5855,
        'local_set': 5315,
        'local_tee': 5340,
        'memory_current': 4675,
        'memory_grow': 11379594,
        'r#if': 12295,
        'select': 5080,
        'version': 3,
    },
    'limits': {
        'br_table_size': 256,
        'call_depth': 32,
        'event_topics': 4,
        'globals': 256,
        'memory_pages': 16,
        'parameters': 128,
        'payload_len': 16384,
        'stack_height': None,
        'subject_len': 32,
        'table_size': 4096,
    },
}
```
#### Python
```python
constant = substrate.get_constant('Contracts', 'Schedule')
```
---------
## Errors

---------
### CodeInUse
Code removal was denied because the code is still in use by at least one contract.

---------
### CodeNotFound
No code could be found at the supplied code hash.

---------
### CodeRejected
The contract&\#x27;s code was found to be invalid during validation or instrumentation.
A more detailed error can be found on the node console if debug messages are enabled
or in the debug buffer which is returned to RPC clients.

---------
### CodeTooLarge
The code supplied to `instantiate_with_code` exceeds the limit specified in the
current schedule.

---------
### ContractNotFound
No contract was found at the specified address.

---------
### ContractReverted
The contract ran to completion but decided to revert its storage changes.
Please note that this error is only returned from extrinsics. When called directly
or via RPC an `Ok` will be returned. In this case the caller needs to inspect the flags
to determine whether a reversion has taken place.

---------
### ContractTrapped
Contract trapped during execution.

---------
### DebugMessageInvalidUTF8
The debug message specified to `seal_debug_message` does contain invalid UTF-8.

---------
### DecodingFailed
Input passed to a contract API function failed to decode as expected type.

---------
### DeletionQueueFull
Removal of a contract failed because the deletion queue is full.

This can happen when calling `seal_terminate`.
The queue is filled by deleting contracts and emptied by a fixed amount each block.
Trying again during another block is the only way to resolve this issue.

---------
### DuplicateContract
A contract with the same AccountId already exists.

---------
### DuplicateTopics
The topics passed to `seal_deposit_events` contains at least one duplicate.

---------
### InputForwarded
`seal_call` forwarded this contracts input. It therefore is no longer available.

---------
### InvalidCallFlags
Invalid combination of flags supplied to `seal_call` or `seal_delegate_call`.

---------
### InvalidScheduleVersion
A new schedule must have a greater version than the current one.

---------
### MaxCallDepthReached
Performing a call was denied because the calling depth reached the limit
of what is specified in the schedule.

---------
### NoChainExtension
The chain does not provide a chain extension. Calling the chain extension results
in this error. Note that this usually  shouldn&\#x27;t happen as deploying such contracts
is rejected.

---------
### OutOfBounds
A buffer outside of sandbox memory was passed to a contract API function.

---------
### OutOfGas
The executed contract exhausted its gas limit.

---------
### OutputBufferTooSmall
The output buffer supplied to a contract API call was too small.

---------
### RandomSubjectTooLong
The subject passed to `seal_random` exceeds the limit.

---------
### ReentranceDenied
A call tried to invoke a contract that is flagged as non-reentrant.

---------
### StorageDepositLimitExhausted
More storage was created than allowed by the storage deposit limit.

---------
### StorageDepositNotEnoughFunds
Origin doesn&\#x27;t have enough balance to pay the required storage deposits.

---------
### TerminatedInConstructor
A contract self destructed in its constructor.

This can be triggered by a call to `seal_terminate`.

---------
### TerminatedWhileReentrant
Termination of a contract is not allowed while the contract is already
on the call stack. Can be triggered by `seal_terminate`.

---------
### TooManyTopics
The amount of topics passed to `seal_deposit_events` exceeds the limit.

---------
### TransferFailed
Performing the requested transfer failed. Probably because there isn&\#x27;t enough
free balance in the sender&\#x27;s account.

---------
### ValueTooLarge
The size defined in `T::MaxValueSize` was exceeded.

---------