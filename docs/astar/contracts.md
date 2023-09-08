
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
### migrate
When a migration is in progress, this dispatchable can be used to run migration steps.
Calls that contribute to advancing the migration have their fees waived, as it&\#x27;s helpful
for the chain. Note that while the migration is in progress, the pallet will also
leverage the `on_idle` hooks to run migration steps.
#### Attributes
| Name | Type |
| -------- | -------- | 
| weight_limit | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'Contracts', 'migrate', {
    'weight_limit': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
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

- `determinism`: If this is set to any other value but [`Determinism::Enforced`] then
  the only way to use this code is to delegate call into it from an offchain execution.
  Set to [`Determinism::Enforced`] if in doubt.

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
        'Enforced',
        'Relaxed',
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
| caller | `Origin<T>` | ```{'Root': None, 'Signed': 'AccountId'}```
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
    'determinism': ('Enforced', 'Relaxed'),
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
 stored in said trie. Therefore this operation is performed lazily in `on_idle`.

#### Python
```python
result = substrate.query(
    'Contracts', 'DeletionQueue', ['u32']
)
```

#### Return value
```python
'Bytes'
```
---------
### DeletionQueueCounter
 A pair of monotonic counters used to track the latest contract marked for deletion
 and the latest deleted contract in queue.

#### Python
```python
result = substrate.query(
    'Contracts', 'DeletionQueueCounter', []
)
```

#### Return value
```python
{'delete_counter': 'u32', 'insert_counter': 'u32'}
```
---------
### MigrationInProgress

#### Python
```python
result = substrate.query(
    'Contracts', 'MigrationInProgress', []
)
```

#### Return value
```python
'Bytes'
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
### DefaultDepositLimit
 Fallback value to limit the storage deposit if it&#x27;s not being set by the caller.
#### Value
```python
39168000000000000000
```
#### Python
```python
constant = substrate.get_constant('Contracts', 'DefaultDepositLimit')
```
---------
### DepositPerByte
 The amount of balance a caller has to pay for each byte of storage.

 \# Note

 Changing this value for an existing chain might need a storage migration.
#### Value
```python
2000000000000000
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
400000000000000000
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
        'account_reentrance_count': {'proof_size': 40, 'ref_time': 262830},
        'address': {'proof_size': 6, 'ref_time': 323232},
        'balance': {'proof_size': 6, 'ref_time': 1496444},
        'block_number': {'proof_size': 6, 'ref_time': 314645},
        'call': {'proof_size': 2752, 'ref_time': 467429651},
        'call_per_cloned_byte': {'proof_size': 0, 'ref_time': 600},
        'call_transfer_surcharge': {'proof_size': 5154, 'ref_time': 286399297},
        'caller': {'proof_size': 6, 'ref_time': 328424},
        'caller_is_origin': {'proof_size': 3, 'ref_time': 169642},
        'caller_is_root': {'proof_size': 3, 'ref_time': 146485},
        'clear_storage': {'proof_size': 289, 'ref_time': 131134319},
        'clear_storage_per_byte': {'proof_size': 1, 'ref_time': 629},
        'code_hash': {'proof_size': 2719, 'ref_time': 29162946},
        'contains_storage': {'proof_size': 289, 'ref_time': 29813682},
        'contains_storage_per_byte': {'proof_size': 1, 'ref_time': 61},
        'debug_message': {'proof_size': 7, 'ref_time': 233911},
        'debug_message_per_byte': {'proof_size': 0, 'ref_time': 738},
        'delegate_call': {'proof_size': 2572, 'ref_time': 362316013},
        'deposit_event': {'proof_size': 10, 'ref_time': 3510388},
        'deposit_event_per_byte': {'proof_size': 0, 'ref_time': 648},
        'deposit_event_per_topic': {'proof_size': 2508, 'ref_time': 127236764},
        'ecdsa_recover': {'proof_size': 77, 'ref_time': 37725489},
        'ecdsa_to_eth_address': {'proof_size': 42, 'ref_time': 9421877},
        'gas': {'proof_size': 0, 'ref_time': 133811},
        'gas_left': {'proof_size': 6, 'ref_time': 543651},
        'get_storage': {'proof_size': 297, 'ref_time': 29992231},
        'get_storage_per_byte': {'proof_size': 1, 'ref_time': 659},
        'hash_blake2_128': {'proof_size': 8, 'ref_time': 414108},
        'hash_blake2_128_per_byte': {'proof_size': 0, 'ref_time': 914},
        'hash_blake2_256': {'proof_size': 8, 'ref_time': 421533},
        'hash_blake2_256_per_byte': {'proof_size': 0, 'ref_time': 914},
        'hash_keccak_256': {'proof_size': 8, 'ref_time': 735528},
        'hash_keccak_256_per_byte': {'proof_size': 0, 'ref_time': 3099},
        'hash_sha2_256': {'proof_size': 8, 'ref_time': 578001},
        'hash_sha2_256_per_byte': {'proof_size': 0, 'ref_time': 3947},
        'input': {'proof_size': 6, 'ref_time': 268456},
        'input_per_byte': {'proof_size': 0, 'ref_time': 596},
        'instantiate': {'proof_size': 5205, 'ref_time': 999510405},
        'instantiate_per_input_byte': {'proof_size': 0, 'ref_time': 1163},
        'instantiate_per_salt_byte': {'proof_size': 0, 'ref_time': 1336},
        'instantiate_transfer_surcharge': {
            'proof_size': 2634,
            'ref_time': 239920186,
        },
        'instantiation_nonce': {'proof_size': 3, 'ref_time': 139180},
        'is_contract': {'proof_size': 2715, 'ref_time': 28331316},
        'minimum_balance': {'proof_size': 6, 'ref_time': 320095},
        'now': {'proof_size': 6, 'ref_time': 323005},
        'own_code_hash': {'proof_size': 6, 'ref_time': 423863},
        'r#return': {'proof_size': 45, 'ref_time': 3361624},
        'random': {'proof_size': 10, 'ref_time': 1876317},
        'reentrance_count': {'proof_size': 3, 'ref_time': 162123},
        'return_per_byte': {'proof_size': 0, 'ref_time': 178},
        'set_code_hash': {'proof_size': 3090, 'ref_time': 296837058},
        'set_storage': {'proof_size': 293, 'ref_time': 131146995},
        'set_storage_per_new_byte': {'proof_size': 0, 'ref_time': 433},
        'set_storage_per_old_byte': {'proof_size': 1, 'ref_time': 0},
        'sr25519_verify': {'proof_size': 112, 'ref_time': 48144071},
        'sr25519_verify_per_byte': {'proof_size': 1, 'ref_time': 4668},
        'take_storage': {'proof_size': 297, 'ref_time': 131206728},
        'take_storage_per_byte': {'proof_size': 1, 'ref_time': 383},
        'terminate': {'proof_size': 7781, 'ref_time': 1067358926},
        'transfer': {'proof_size': 2520, 'ref_time': 161086917},
        'value_transferred': {'proof_size': 6, 'ref_time': 318979},
        'weight_to_fee': {'proof_size': 14, 'ref_time': 1396737},
    },
    'instruction_weights': {
        'br': 1619,
        'br_if': 2529,
        'br_table': 4988,
        'br_table_per_entry': 0,
        'call': 14952,
        'call_indirect': 19020,
        'call_per_local': 1176,
        'fallback': 0,
        'global_get': 6903,
        'global_set': 7301,
        'i32wrapi64': 740,
        'i64add': 1386,
        'i64and': 1176,
        'i64clz': 1055,
        'i64const': 1498,
        'i64ctz': 786,
        'i64divs': 7405,
        'i64divu': 6155,
        'i64eq': 1471,
        'i64eqz': 672,
        'i64extendsi32': 983,
        'i64extendui32': 815,
        'i64ges': 1477,
        'i64geu': 1480,
        'i64gts': 1326,
        'i64gtu': 1624,
        'i64les': 1494,
        'i64leu': 1593,
        'i64load': 3420,
        'i64lts': 1496,
        'i64ltu': 1510,
        'i64mul': 1269,
        'i64ne': 1474,
        'i64or': 1252,
        'i64popcnt': 776,
        'i64rems': 7839,
        'i64remu': 6158,
        'i64rotl': 1517,
        'i64rotr': 1384,
        'i64shl': 1441,
        'i64shrs': 1638,
        'i64shru': 1447,
        'i64store': 3021,
        'i64sub': 1536,
        'i64xor': 1403,
        'local_get': 1019,
        'local_set': 2122,
        'local_tee': 969,
        'memory_current': 2336,
        'memory_grow': 13191908,
        'r#if': 6345,
        'select': 1933,
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
        'runtime_memory': 134217728,
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
False
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
node. This happens if an older node is used with a new version of ink!. Try updating
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
### MigrationInProgress
A pending migration needs to complete before the extrinsic can be called.

---------
### NoChainExtension
The chain does not provide a chain extension. Calling the chain extension results
in this error. Note that this usually  shouldn&\#x27;t happen as deploying such contracts
is rejected.

---------
### NoMigrationPerformed
Migrate dispatch call was attempted but no migration was performed.

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