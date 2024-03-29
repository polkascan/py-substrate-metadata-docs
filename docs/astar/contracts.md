
# Contracts

---------
## Calls

---------
### call
See [`Pallet::call`].
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
See [`Pallet::call_old_weight`].
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
See [`Pallet::instantiate`].
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
    'code_hash': 'scale_info::12',
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
See [`Pallet::instantiate_old_weight`].
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
    'code_hash': 'scale_info::12',
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
See [`Pallet::instantiate_with_code`].
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
See [`Pallet::instantiate_with_code_old_weight`].
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
See [`Pallet::migrate`].
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
See [`Pallet::remove_code`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| code_hash | `CodeHash<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Contracts', 'remove_code', {'code_hash': 'scale_info::12'}
)
```

---------
### set_code
See [`Pallet::set_code`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `AccountIdLookupOf<T>` | 
| code_hash | `CodeHash<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Contracts', 'set_code', {
    'code_hash': 'scale_info::12',
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
See [`Pallet::upload_code`].
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
| code_hash | `T::Hash` | ```scale_info::12```
| deposit_released | `BalanceOf<T>` | ```u128```
| remover | `T::AccountId` | ```AccountId```

---------
### CodeStored
Code with the specified hash has been stored.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| code_hash | `T::Hash` | ```scale_info::12```
| deposit_held | `BalanceOf<T>` | ```u128```
| uploader | `T::AccountId` | ```AccountId```

---------
### ContractCodeUpdated
A contract&\#x27;s code was updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| contract | `T::AccountId` | ```AccountId```
| new_code_hash | `T::Hash` | ```scale_info::12```
| old_code_hash | `T::Hash` | ```scale_info::12```

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
| code_hash | `CodeHash<T>` | ```scale_info::12```

---------
### Instantiated
Contract deployed by address at the specified address.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| deployer | `T::AccountId` | ```AccountId```
| contract | `T::AccountId` | ```AccountId```

---------
### StorageDepositTransferredAndHeld
Some funds have been transferred and held as storage deposit.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### StorageDepositTransferredAndReleased
Some storage deposit funds have been transferred and released.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

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
### CodeInfoOf
 A mapping from a contract&#x27;s code hash to its code info.

#### Python
```python
result = substrate.query(
    'Contracts', 'CodeInfoOf', ['scale_info::12']
)
```

#### Return value
```python
{
    'code_len': 'u32',
    'deposit': 'u128',
    'determinism': ('Enforced', 'Relaxed'),
    'owner': 'AccountId',
    'refcount': 'u64',
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
    'code_hash': 'scale_info::12',
    'delegate_dependencies': 'scale_info::507',
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
 A migration can span across multiple blocks. This storage defines a cursor to track the
 progress of the migration, enabling us to resume from the last completed position.

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
### PristineCode
 A mapping from a contract&#x27;s code hash to its code.

#### Python
```python
result = substrate.query(
    'Contracts', 'PristineCode', ['scale_info::12']
)
```

#### Return value
```python
'Bytes'
```
---------
## Constants

---------
### CodeHashLockupDepositPercent
 The percentage of the storage deposit that should be held for using a code hash.
 Instantiating a contract, or calling [`chain_extension::Ext::add_delegate_dependency`]
 protects the code from being removed. In order to prevent abuse these actions are
 protected with a percentage of the code deposit.
#### Value
```python
100000000
```
#### Python
```python
constant = substrate.get_constant('Contracts', 'CodeHashLockupDepositPercent')
```
---------
### DefaultDepositLimit
 Fallback value to limit the storage deposit if it&#x27;s not being set by the caller.
#### Value
```python
391680000000000000
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
20000000000000
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
4000000000000000
```
#### Python
```python
constant = substrate.get_constant('Contracts', 'DepositPerItem')
```
---------
### Environment
 Type that bundles together all the runtime configurable interface types.

 This is not a real config. We just mention the type here as constant so that
 its type appears in the metadata. Only valid value is `()`.
#### Value
```python
{
    'account_id': {},
    'balance': {},
    'block_number': {},
    'hash': {},
    'hasher': {},
    'timestamp': {},
}
```
#### Python
```python
constant = substrate.get_constant('Contracts', 'Environment')
```
---------
### MaxCodeLen
 The maximum length of a contract code in bytes.

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
### MaxDelegateDependencies
 The maximum number of delegate_dependencies that a contract can lock with
 [`chain_extension::Ext::add_delegate_dependency`].
#### Value
```python
32
```
#### Python
```python
constant = substrate.get_constant('Contracts', 'MaxDelegateDependencies')
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
        'account_reentrance_count': {'proof_size': 40, 'ref_time': 318129},
        'add_delegate_dependency': {'proof_size': 2606, 'ref_time': 131695172},
        'address': {'proof_size': 6, 'ref_time': 343762},
        'balance': {'proof_size': 6, 'ref_time': 1656237},
        'block_number': {'proof_size': 6, 'ref_time': 330788},
        'call': {'proof_size': 2721, 'ref_time': 498206665},
        'call_per_cloned_byte': {'proof_size': 0, 'ref_time': 1111},
        'call_transfer_surcharge': {'proof_size': 5227, 'ref_time': 607425411},
        'caller': {'proof_size': 6, 'ref_time': 339309},
        'caller_is_origin': {'proof_size': 3, 'ref_time': 183053},
        'caller_is_root': {'proof_size': 3, 'ref_time': 165364},
        'clear_storage': {'proof_size': 289, 'ref_time': 131927074},
        'clear_storage_per_byte': {'proof_size': 1, 'ref_time': 4},
        'code_hash': {'proof_size': 2688, 'ref_time': 29720110},
        'contains_storage': {'proof_size': 289, 'ref_time': 30548039},
        'contains_storage_per_byte': {'proof_size': 1, 'ref_time': 83},
        'debug_message': {'proof_size': 7, 'ref_time': 241240},
        'debug_message_per_byte': {'proof_size': 0, 'ref_time': 1102},
        'delegate_call': {'proof_size': 2637, 'ref_time': 424943483},
        'deposit_event': {'proof_size': 10, 'ref_time': 3808788},
        'deposit_event_per_byte': {'proof_size': 0, 'ref_time': 731},
        'deposit_event_per_topic': {'proof_size': 2508, 'ref_time': 128683455},
        'ecdsa_recover': {'proof_size': 77, 'ref_time': 46037637},
        'ecdsa_to_eth_address': {'proof_size': 42, 'ref_time': 11949979},
        'gas_left': {'proof_size': 6, 'ref_time': 371542},
        'get_storage': {'proof_size': 297, 'ref_time': 30707060},
        'get_storage_per_byte': {'proof_size': 1, 'ref_time': 1010},
        'hash_blake2_128': {'proof_size': 8, 'ref_time': 505330},
        'hash_blake2_128_per_byte': {'proof_size': 0, 'ref_time': 1252},
        'hash_blake2_256': {'proof_size': 8, 'ref_time': 480457},
        'hash_blake2_256_per_byte': {'proof_size': 0, 'ref_time': 1254},
        'hash_keccak_256': {'proof_size': 8, 'ref_time': 802363},
        'hash_keccak_256_per_byte': {'proof_size': 0, 'ref_time': 3410},
        'hash_sha2_256': {'proof_size': 8, 'ref_time': 400604},
        'hash_sha2_256_per_byte': {'proof_size': 0, 'ref_time': 1134},
        'input': {'proof_size': 6, 'ref_time': 282718},
        'input_per_byte': {'proof_size': 0, 'ref_time': 1052},
        'instantiate': {'proof_size': 2731, 'ref_time': 1038311259},
        'instantiate_per_input_byte': {'proof_size': 0, 'ref_time': 1963},
        'instantiate_per_salt_byte': {'proof_size': 0, 'ref_time': 2060},
        'instantiate_transfer_surcharge': {
            'proof_size': 2549,
            'ref_time': 125000000,
        },
        'instantiation_nonce': {'proof_size': 3, 'ref_time': 152842},
        'is_contract': {'proof_size': 2684, 'ref_time': 28788924},
        'minimum_balance': {'proof_size': 6, 'ref_time': 337202},
        'now': {'proof_size': 6, 'ref_time': 337860},
        'own_code_hash': {'proof_size': 6, 'ref_time': 428765},
        'r#return': {'proof_size': 45, 'ref_time': 0},
        'random': {'proof_size': 10, 'ref_time': 2057388},
        'reentrance_count': {'proof_size': 3, 'ref_time': 180655},
        'remove_delegate_dependency': {
            'proof_size': 2568,
            'ref_time': 130895043,
        },
        'return_per_byte': {'proof_size': 0, 'ref_time': 391},
        'set_code_hash': {'proof_size': 3090, 'ref_time': 302627005},
        'set_storage': {'proof_size': 293, 'ref_time': 132145641},
        'set_storage_per_new_byte': {'proof_size': 0, 'ref_time': 547},
        'set_storage_per_old_byte': {'proof_size': 1, 'ref_time': 558},
        'sr25519_verify': {'proof_size': 112, 'ref_time': 56127492},
        'sr25519_verify_per_byte': {'proof_size': 1, 'ref_time': 6155},
        'take_storage': {'proof_size': 297, 'ref_time': 131895457},
        'take_storage_per_byte': {'proof_size': 1, 'ref_time': 643},
        'terminate': {'proof_size': 5266, 'ref_time': 1301508132},
        'transfer': {'proof_size': 2520, 'ref_time': 163468091},
        'value_transferred': {'proof_size': 6, 'ref_time': 347368},
        'weight_to_fee': {'proof_size': 14, 'ref_time': 1446663},
    },
    'instruction_weights': {'base': 4903},
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
### CannotAddSelfAsDelegateDependency
Can not add a delegate dependency to the code hash of the contract itself.

---------
### CodeInUse
Code removal was denied because the code is still in use by at least one contract.

---------
### CodeInfoNotFound
No code info could be found at the supplied code hash.

---------
### CodeNotFound
No code could be found at the supplied code hash.

---------
### CodeRejected
The contract&\#x27;s code was found to be invalid during validation.

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
### DelegateDependencyAlreadyExists
The contract already depends on the given delegate dependency.

---------
### DelegateDependencyNotFound
The dependency was not found in the contract&\#x27;s delegate dependencies.

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
### InvalidSchedule
Invalid schedule supplied, e.g. with zero weight of a basic operation.

---------
### MaxCallDepthReached
Performing a call was denied because the calling depth reached the limit
of what is specified in the schedule.

---------
### MaxDelegateDependenciesReached
The contract has reached its maximum number of delegate dependencies.

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