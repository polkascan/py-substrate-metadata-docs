
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
    'gas_limit': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
    'storage_deposit_limit': (
        None,
        'u128',
    ),
    'value': 'u128',
}
)
```

---------
### call_old_weight
Deprecated version if [`Self::call`] for use in an in-storage `Call`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `AccountIdLookupOf<T>` | 
| value | `BalanceOf<T>` | 
| gas_limit | `OldWeight` | 
| storage_deposit_limit | `Option<<BalanceOf<T> as codec::HasCompact>::Type>` | 
| data | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Contracts', 'call_old_weight', {
    'data': 'Bytes',
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'gas_limit': 'u64',
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
    'gas_limit': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
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
### instantiate_old_weight
Deprecated version if [`Self::instantiate`] for use in an in-storage `Call`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `BalanceOf<T>` | 
| gas_limit | `OldWeight` | 
| storage_deposit_limit | `Option<<BalanceOf<T> as codec::HasCompact>::Type>` | 
| code_hash | `CodeHash<T>` | 
| data | `Vec<u8>` | 
| salt | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Contracts', 'instantiate_old_weight', {
    'code_hash': '[u8; 32]',
    'data': 'Bytes',
    'gas_limit': 'u64',
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
    'gas_limit': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
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
### instantiate_with_code_old_weight
Deprecated version if [`Self::instantiate_with_code`] for use in an in-storage `Call`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `BalanceOf<T>` | 
| gas_limit | `OldWeight` | 
| storage_deposit_limit | `Option<<BalanceOf<T> as codec::HasCompact>::Type>` | 
| code | `Vec<u8>` | 
| data | `Vec<u8>` | 
| salt | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Contracts', 'instantiate_with_code_old_weight', {
    'code': 'Bytes',
    'data': 'Bytes',
    'gas_limit': 'u64',
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

- `determinism`: If this is set to any other value but [`Determinism::Deterministic`]
  then the only way to use this code is to delegate call into it from an offchain
  execution. Set to [`Determinism::Deterministic`] if in doubt.

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
| determinism | `Determinism` | 

#### Python
```python
call = substrate.compose_call(
    'Contracts', 'upload_code', {
    'code': 'Bytes',
    'determinism': (
        'Deterministic',
        'AllowIndeterminism',
    ),
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
    'determinism': ('Deterministic', 'AllowIndeterminism'),
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
    'deposit_account': 'AccountId',
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
128
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
{'proof_size': 3932160, 'ref_time': 375000000000}
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
5000000
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
100000000000
```
#### Python
```python
constant = substrate.get_constant('Contracts', 'DepositPerItem')
```
---------
### MaxCodeLen
 The maximum length of a contract code in bytes. This limit applies to the instrumented
 version of the code. Therefore `instantiate_with_code` can fail even when supplying
 a wasm binary below this maximum size.

 The value should be chosen carefully taking into the account the overall memory limit
 your runtime has, as well as the [maximum allowed callstack
 depth](\#associatedtype.CallStack). Look into the `integrity_test()` for some insights.
#### Value
```python
125952
```
#### Python
```python
constant = substrate.get_constant('Contracts', 'MaxCodeLen')
```
---------
### MaxDebugBufferLen
 The maximum length of the debug buffer in bytes.
#### Value
```python
2097152
```
#### Python
```python
constant = substrate.get_constant('Contracts', 'MaxDebugBufferLen')
```
---------
### MaxStorageKeyLen
 The maximum allowable length in bytes for storage keys.
#### Value
```python
128
```
#### Python
```python
constant = substrate.get_constant('Contracts', 'MaxStorageKeyLen')
```
---------
### Schedule
 Cost schedule and limits.
#### Value
```python
{
    'host_fn_weights': {
        'account_reentrance_count': {'proof_size': 198, 'ref_time': 225716},
        'address': {'proof_size': 30, 'ref_time': 221053},
        'balance': {'proof_size': 30, 'ref_time': 1228637},
        'block_number': {'proof_size': 30, 'ref_time': 211709},
        'call': {'proof_size': 6393, 'ref_time': 612280314},
        'call_per_cloned_byte': {'proof_size': 0, 'ref_time': 120},
        'call_transfer_surcharge': {'proof_size': 3562, 'ref_time': 143940274},
        'caller': {'proof_size': 30, 'ref_time': 221445},
        'caller_is_origin': {'proof_size': 15, 'ref_time': 141995},
        'clear_storage': {'proof_size': 288, 'ref_time': 130666449},
        'clear_storage_per_byte': {'proof_size': 2, 'ref_time': 11496},
        'code_hash': {'proof_size': 3856, 'ref_time': 28777188},
        'contains_storage': {'proof_size': 288, 'ref_time': 29464186},
        'contains_storage_per_byte': {'proof_size': 2, 'ref_time': 2890},
        'debug_message': {'proof_size': 35, 'ref_time': 185463},
        'debug_message_per_byte': {'proof_size': 0, 'ref_time': 800},
        'delegate_call': {'proof_size': 8249, 'ref_time': 499579339},
        'deposit_event': {'proof_size': 50, 'ref_time': 2865176},
        'deposit_event_per_byte': {'proof_size': 0, 'ref_time': 874},
        'deposit_event_per_topic': {'proof_size': 2637, 'ref_time': 127268381},
        'ecdsa_recover': {'proof_size': 380, 'ref_time': 37763755},
        'ecdsa_to_eth_address': {'proof_size': 210, 'ref_time': 9228220},
        'gas': {'proof_size': 0, 'ref_time': 100691},
        'gas_left': {'proof_size': 30, 'ref_time': 214407},
        'get_storage': {'proof_size': 296, 'ref_time': 29640163},
        'get_storage_per_byte': {'proof_size': 2, 'ref_time': 4100},
        'hash_blake2_128': {'proof_size': 42, 'ref_time': 449169},
        'hash_blake2_128_per_byte': {'proof_size': 0, 'ref_time': 1261},
        'hash_blake2_256': {'proof_size': 40, 'ref_time': 416839},
        'hash_blake2_256_per_byte': {'proof_size': 0, 'ref_time': 1260},
        'hash_keccak_256': {'proof_size': 40, 'ref_time': 722259},
        'hash_keccak_256_per_byte': {'proof_size': 0, 'ref_time': 3185},
        'hash_sha2_256': {'proof_size': 40, 'ref_time': 528644},
        'hash_sha2_256_per_byte': {'proof_size': 0, 'ref_time': 3961},
        'input': {'proof_size': 30, 'ref_time': 198355},
        'input_per_byte': {'proof_size': 0, 'ref_time': 118},
        'instantiate': {'proof_size': 17088, 'ref_time': 1098810328},
        'instantiate_per_input_byte': {'proof_size': 0, 'ref_time': 1539},
        'instantiate_per_salt_byte': {'proof_size': 0, 'ref_time': 1545},
        'instantiate_transfer_surcharge': {
            'proof_size': 33,
            'ref_time': 2621493,
        },
        'instantiation_nonce': {'proof_size': 18, 'ref_time': 117264},
        'is_contract': {'proof_size': 3836, 'ref_time': 28113744},
        'minimum_balance': {'proof_size': 30, 'ref_time': 214348},
        'now': {'proof_size': 30, 'ref_time': 216705},
        'own_code_hash': {'proof_size': 30, 'ref_time': 279709},
        'r#return': {'proof_size': 225, 'ref_time': 1737397},
        'random': {'proof_size': 60, 'ref_time': 1391359},
        'reentrance_count': {'proof_size': 15, 'ref_time': 143540},
        'return_per_byte': {'proof_size': 0, 'ref_time': 227},
        'set_code_hash': {'proof_size': 11786, 'ref_time': 277142535},
        'set_storage': {'proof_size': 292, 'ref_time': 130806878},
        'set_storage_per_new_byte': {'proof_size': 0, 'ref_time': 11875},
        'set_storage_per_old_byte': {'proof_size': 2, 'ref_time': 11484},
        'take_storage': {'proof_size': 296, 'ref_time': 130815165},
        'take_storage_per_byte': {'proof_size': 2, 'ref_time': 12714},
        'terminate': {'proof_size': 15004, 'ref_time': 920441665},
        'transfer': {'proof_size': 2701, 'ref_time': 142456889},
        'value_transferred': {'proof_size': 30, 'ref_time': 218025},
        'weight_to_fee': {'proof_size': 60, 'ref_time': 1106625},
    },
    'instruction_weights': {
        'br': 2287,
        'br_if': 3316,
        'br_table': 5457,
        'br_table_per_entry': 46,
        'call': 19203,
        'call_indirect': 23063,
        'call_indirect_per_param': 2289,
        'call_per_local': 913,
        'fallback': 0,
        'global_get': 6908,
        'global_set': 7138,
        'i32wrapi64': 2058,
        'i64add': 2786,
        'i64and': 2793,
        'i64clz': 2136,
        'i64const': 2060,
        'i64ctz': 2224,
        'i64divs': 9041,
        'i64divu': 8400,
        'i64eq': 2914,
        'i64eqz': 2410,
        'i64extendsi32': 2066,
        'i64extendui32': 1995,
        'i64ges': 2906,
        'i64geu': 2958,
        'i64gts': 2889,
        'i64gtu': 3016,
        'i64les': 2903,
        'i64leu': 3121,
        'i64load': 6640,
        'i64lts': 2843,
        'i64ltu': 2887,
        'i64mul': 2688,
        'i64ne': 2896,
        'i64or': 3456,
        'i64popcnt': 2470,
        'i64rems': 9322,
        'i64remu': 8353,
        'i64rotl': 2850,
        'i64rotr': 2789,
        'i64shl': 2818,
        'i64shrs': 2855,
        'i64shru': 2845,
        'i64store': 5894,
        'i64sub': 2686,
        'i64xor': 2793,
        'local_get': 2534,
        'local_set': 2795,
        'local_tee': 2460,
        'memory_current': 6071,
        'memory_grow': 14803549,
        'r#if': 6979,
        'select': 3255,
        'version': 4,
    },
    'limits': {
        'br_table_size': 256,
        'event_topics': 4,
        'globals': 256,
        'locals': 1024,
        'memory_pages': 16,
        'parameters': 128,
        'payload_len': 16384,
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
### UnsafeUnstableInterface
 Make contract callable functions marked as `\#[unstable]` available.

 Contracts that use `\#[unstable]` functions won&#x27;t be able to be uploaded unless
 this is set to `true`. This is only meant for testnets and dev nodes in order to
 experiment with new features.

 \# Warning

 Do **not** set to `true` on productions chains.
#### Value
```python
True
```
#### Python
```python
constant = substrate.get_constant('Contracts', 'UnsafeUnstableInterface')
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

The most likely cause of this is that an API was used which is not supported by the
node. This hapens if an older node is used with a new version of ink!. Try updating
your node to the newest available version.

A more detailed error can be found on the node console if debug messages are enabled
by supplying `-lruntime::contracts=debug`.

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
### Indeterministic
An indetermistic code was used in a context where this is not permitted.

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
The only other cause is that a call from a contract into the runtime tried to call back
into `pallet-contracts`. This would make the whole pallet reentrant with regard to
contract code execution which is not supported.

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