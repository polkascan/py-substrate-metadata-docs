
# Cosmwasm

---------
## Calls

---------
### execute
Execute a previously instantiated contract.

* Emits an `Executed` event.
* Possibly emit `Emitted` events.

\# Arguments

* `origin` the origin dispatching the extrinsic.
* `code_id` the unique code id generated when the code has been uploaded via [`upload`].
* `salt` the salt, usually used to instantiate the same contract multiple times.
* `funds` the assets transferred to the contract prior to calling it&\#x27;s `instantiate`
  export.
* `gas` the maximum gas to use, the remaining is refunded at the end of the transaction.
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract | `AccountIdOf<T>` | 
| funds | `FundsOf<T>` | 
| gas | `u64` | 
| message | `ContractMessageOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Cosmwasm', 'execute', {
    'contract': 'AccountId',
    'funds': 'scale_info::398',
    'gas': 'u64',
    'message': 'Bytes',
}
)
```

---------
### instantiate
Instantiate a previously uploaded code resulting in a new contract being generated.

* Emits an `Instantiated` event on success.
* Emits an `Executed` event.
* Possibly emit `Emitted` events.

\# Arguments

* `origin` the origin dispatching the extrinsic.
* `code_identifier` the unique code id generated when the code has been uploaded via
  [`upload`].
* `salt` the salt, usually used to instantiate the same contract multiple times.
* `funds` the assets transferred to the contract prior to calling it&\#x27;s `instantiate`
  export.
* `gas` the maximum gas to use, the remaining is refunded at the end of the transaction.
#### Attributes
| Name | Type |
| -------- | -------- | 
| code_identifier | `CodeIdentifier` | 
| salt | `ContractSaltOf<T>` | 
| admin | `Option<AccountIdOf<T>>` | 
| label | `ContractLabelOf<T>` | 
| funds | `FundsOf<T>` | 
| gas | `u64` | 
| message | `ContractMessageOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Cosmwasm', 'instantiate', {
    'admin': (None, 'AccountId'),
    'code_identifier': {
        'CodeHash': '[u8; 32]',
        'CodeId': 'u64',
    },
    'funds': 'scale_info::398',
    'gas': 'u64',
    'label': 'Bytes',
    'message': 'Bytes',
    'salt': 'Bytes',
}
)
```

---------
### migrate
Migrate a previously instantiated contract.

* Emits a `Migrated` event on success.
* Emits an `Executed` event.
* Possibly emit `Emitted` events.

\# Arguments

* `origin` the origin dispatching the extrinsic.
* `contract` the address of the contract that we want to migrate
* `new_code_identifier` the code identifier that we want to switch to.
* `gas` the maximum gas to use, the remaining is refunded at the end of the transaction.
* `message` MigrateMsg, that will be passed to the contract.
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract | `AccountIdOf<T>` | 
| new_code_identifier | `CodeIdentifier` | 
| gas | `u64` | 
| message | `ContractMessageOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Cosmwasm', 'migrate', {
    'contract': 'AccountId',
    'gas': 'u64',
    'message': 'Bytes',
    'new_code_identifier': {
        'CodeHash': '[u8; 32]',
        'CodeId': 'u64',
    },
}
)
```

---------
### update_admin
Update the admin of a contract.

* Emits a `AdminUpdated` event on success.

\# Arguments

* `origin` the origin dispatching the extrinsic.
* `contract` the address of the contract that we want to migrate.
* `new_admin` new admin of the contract that we want to update to.
* `gas` the maximum gas to use, the remaining is refunded at the end of the transaction.
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract | `AccountIdOf<T>` | 
| new_admin | `Option<AccountIdOf<T>>` | 
| gas | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Cosmwasm', 'update_admin', {
    'contract': 'AccountId',
    'gas': 'u64',
    'new_admin': (None, 'AccountId'),
}
)
```

---------
### upload
Upload a CosmWasm contract.
The function will ensure that the wasm module is well formed and that it fits the
according limits. The module exports are going to be checked against the expected
CosmWasm export signatures.

* Emits an `Uploaded` event on success.

\# Arguments

- `origin` the original dispatching the extrinsic.
- `code` the actual wasm code.
#### Attributes
| Name | Type |
| -------- | -------- | 
| code | `ContractCodeOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Cosmwasm', 'upload', {'code': 'Bytes'}
)
```

---------
## Events

---------
### AdminUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| contract | `AccountIdOf<T>` | ```AccountId```
| new_admin | `Option<AccountIdOf<T>>` | ```(None, 'AccountId')```

---------
### Emitted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| contract | `AccountIdOf<T>` | ```AccountId```
| ty | `Vec<u8>` | ```Bytes```
| attributes | `Vec<(Vec<u8>, Vec<u8>)>` | ```[('Bytes', 'Bytes')]```

---------
### Executed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| contract | `AccountIdOf<T>` | ```AccountId```
| entrypoint | `EntryPoint` | ```('Instantiate', 'Execute', 'Migrate', 'Reply', 'IbcChannelOpen', 'IbcChannelConnect', 'IbcChannelClose', 'IbcPacketTimeout', 'IbcPacketReceive', 'IbcPacketAck')```
| data | `Option<Vec<u8>>` | ```(None, 'Bytes')```

---------
### ExecutionFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| contract | `AccountIdOf<T>` | ```AccountId```
| entrypoint | `EntryPoint` | ```('Instantiate', 'Execute', 'Migrate', 'Reply', 'IbcChannelOpen', 'IbcChannelConnect', 'IbcChannelClose', 'IbcPacketTimeout', 'IbcPacketReceive', 'IbcPacketAck')```
| error | `Vec<u8>` | ```Bytes```

---------
### Instantiated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| contract | `AccountIdOf<T>` | ```AccountId```
| info | `ContractInfoOf<T>` | ```{'code_id': 'u64', 'trie_id': 'Bytes', 'instantiator': 'AccountId', 'admin': (None, 'AccountId'), 'label': 'Bytes'}```

---------
### Migrated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| contract | `AccountIdOf<T>` | ```AccountId```
| to | `CosmwasmCodeId` | ```u64```

---------
### Uploaded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| code_hash | `[u8; 32]` | ```[u8; 32]```
| code_id | `CosmwasmCodeId` | ```u64```

---------
## Storage functions

---------
### CodeHashToId
 A mapping between a code hash and it&#x27;s unique ID.

#### Python
```python
result = substrate.query(
    'Cosmwasm', 'CodeHashToId', ['[u8; 32]']
)
```

#### Return value
```python
'u64'
```
---------
### CodeIdToInfo
 A mapping between an original code hash and its metadata.

#### Python
```python
result = substrate.query(
    'Cosmwasm', 'CodeIdToInfo', ['u64']
)
```

#### Return value
```python
{
    'creator': 'AccountId',
    'ibc_capable': 'bool',
    'instrumentation_version': 'u16',
    'pristine_code_hash': '[u8; 32]',
    'refcount': 'u32',
}
```
---------
### ContractToInfo
 A mapping between a contract&#x27;s account id and it&#x27;s metadata.

#### Python
```python
result = substrate.query(
    'Cosmwasm', 'ContractToInfo', ['AccountId']
)
```

#### Return value
```python
{
    'admin': (None, 'AccountId'),
    'code_id': 'u64',
    'instantiator': 'AccountId',
    'label': 'Bytes',
    'trie_id': 'Bytes',
}
```
---------
### CurrentCodeId
 Monotonic counter incremented on code creation.

#### Python
```python
result = substrate.query(
    'Cosmwasm', 'CurrentCodeId', []
)
```

#### Return value
```python
'u64'
```
---------
### CurrentNonce
 This is a **monotonic** counter incremented on contract instantiation.
 The purpose of this nonce is just to make sure that contract trie are unique.

#### Python
```python
result = substrate.query(
    'Cosmwasm', 'CurrentNonce', []
)
```

#### Return value
```python
'u64'
```
---------
### InstrumentedCode
 A mapping between an original code id and instrumented wasm code, ready for execution.

#### Python
```python
result = substrate.query(
    'Cosmwasm', 'InstrumentedCode', ['u64']
)
```

#### Return value
```python
'Bytes'
```
---------
### PristineCode
 A mapping from an original code id to the original code, untouched by instrumentation.

#### Python
```python
result = substrate.query(
    'Cosmwasm', 'PristineCode', ['u64']
)
```

#### Return value
```python
'Bytes'
```
---------
## Constants

---------
### ChainId
 Current chain ID. Provided to the contract via the [`Env`].
#### Value
```python
'composable-network-picasso'
```
#### Python
```python
constant = substrate.get_constant('Cosmwasm', 'ChainId')
```
---------
### CodeBranchTableSizeLimit
 Max wasm branch table size limit.
#### Value
```python
256
```
#### Python
```python
constant = substrate.get_constant('Cosmwasm', 'CodeBranchTableSizeLimit')
```
---------
### CodeGlobalVariableLimit
 Max wasm globals limit.
#### Value
```python
256
```
#### Python
```python
constant = substrate.get_constant('Cosmwasm', 'CodeGlobalVariableLimit')
```
---------
### CodeParameterLimit
 Max wasm functions parameters limit.
#### Value
```python
128
```
#### Python
```python
constant = substrate.get_constant('Cosmwasm', 'CodeParameterLimit')
```
---------
### CodeStackLimit
 Max wasm stack size limit.
#### Value
```python
4294967295
```
#### Python
```python
constant = substrate.get_constant('Cosmwasm', 'CodeStackLimit')
```
---------
### CodeStorageByteDeposit
 Price of a byte when uploading new code.
 The price is expressed in [`Self::NativeAsset`].
 This amount is reserved from the owner and released when the code is destroyed.
#### Value
```python
1000000
```
#### Python
```python
constant = substrate.get_constant('Cosmwasm', 'CodeStorageByteDeposit')
```
---------
### CodeTableSizeLimit
 Max wasm table size.
#### Value
```python
4096
```
#### Python
```python
constant = substrate.get_constant('Cosmwasm', 'CodeTableSizeLimit')
```
---------
### ContractStorageByteReadPrice
 Price of extracting a byte from the storage.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Cosmwasm', 'ContractStorageByteReadPrice')
```
---------
### ContractStorageByteWritePrice
 Price of writing a byte in the storage.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Cosmwasm', 'ContractStorageByteWritePrice')
```
---------
### MaxCodeSize
 Max accepted code size in bytes.
#### Value
```python
1048576
```
#### Python
```python
constant = substrate.get_constant('Cosmwasm', 'MaxCodeSize')
```
---------
### MaxContractLabelSize
 Max contract label size.
#### Value
```python
64
```
#### Python
```python
constant = substrate.get_constant('Cosmwasm', 'MaxContractLabelSize')
```
---------
### MaxContractTrieIdSize
 Max contract trie id size.
#### Value
```python
32
```
#### Python
```python
constant = substrate.get_constant('Cosmwasm', 'MaxContractTrieIdSize')
```
---------
### MaxFundsAssets
 Max assets in a [`FundsOf`] batch.
#### Value
```python
32
```
#### Python
```python
constant = substrate.get_constant('Cosmwasm', 'MaxFundsAssets')
```
---------
### MaxInstantiateSaltSize
 Max instantiate salt.
#### Value
```python
128
```
#### Python
```python
constant = substrate.get_constant('Cosmwasm', 'MaxInstantiateSaltSize')
```
---------
### MaxInstrumentedCodeSize
 Max code size after gas instrumentation.
#### Value
```python
2097152
```
#### Python
```python
constant = substrate.get_constant('Cosmwasm', 'MaxInstrumentedCodeSize')
```
---------
### MaxMessageSize
 Max message size in bytes.
#### Value
```python
65536
```
#### Python
```python
constant = substrate.get_constant('Cosmwasm', 'MaxMessageSize')
```
---------
### PalletId
 Pallet unique ID.
#### Value
```python
'0x636f736d7761736d'
```
#### Python
```python
constant = substrate.get_constant('Cosmwasm', 'PalletId')
```
---------
### WasmCostRules
#### Value
```python
{
    'br': 0,
    'brif': 3332,
    'brtable': 8514,
    'brtable_per_elem': 0,
    'call': 117147,
    'call_indirect': 232674,
    'currentmemory': 7990,
    'else_': 6960,
    'f64abs': 8321,
    'f64add': 12551,
    'f64ceil': 8920,
    'f64const': 1667,
    'f64copysign': 13838,
    'f64div': 13746,
    'f64eq': 15860,
    'f64floor': 9438,
    'f64ge': 14540,
    'f64gt': 14442,
    'f64le': 14114,
    'f64load': 15153,
    'f64lt': 13759,
    'f64max': 23315,
    'f64min': 21056,
    'f64mul': 21030,
    'f64ne': 12824,
    'f64nearest': 15823,
    'f64neg': 3264,
    'f64sqrt': 9394,
    'f64store': 27972,
    'f64sub': 17010,
    'f64trunc': 9250,
    'getglobal': 0,
    'getlocal': 0,
    'growmemory': 29368061,
    'i32wrapi64': 4331,
    'i64add': 18324,
    'i64and': 19046,
    'i64clz': 4710,
    'i64const': 6246,
    'i64ctz': 3884,
    'i64divs': 22314,
    'i64divu': 27382,
    'i64eq': 16698,
    'i64eqz': 5261,
    'i64extendsi32': 4064,
    'i64ges': 23801,
    'i64gts': 18374,
    'i64les': 14607,
    'i64load': 19220,
    'i64lts': 14341,
    'i64mul': 22177,
    'i64ne': 14049,
    'i64or': 26363,
    'i64popcnt': 5694,
    'i64rems': 22113,
    'i64rotl': 30800,
    'i64rotr': 12926,
    'i64shl': 17835,
    'i64shrs': 20001,
    'i64store': 33807,
    'i64sub': 22566,
    'i64xor': 23564,
    'if_': 319,
    'select': 29397,
    'setglobal': 0,
    'setlocal': 0,
    'teelocal': 0,
}
```
#### Python
```python
constant = substrate.get_constant('Cosmwasm', 'WasmCostRules')
```
---------
## Errors

---------
### Aborted

---------
### AccountConversionFailure

---------
### AssetConversion

---------
### CodeAlreadyExists

---------
### CodeDecoding

---------
### CodeEncoding

---------
### CodeInstrumentation

---------
### CodeNotFound

---------
### CodeValidation

---------
### ContractAlreadyExists

---------
### ContractHasNoInfo

---------
### ContractNotFound

---------
### ExecuteDeserialize

---------
### ExecuteSerialize

---------
### FailedToSerialize

---------
### Ibc

---------
### Instrumentation

---------
### InstrumentedCodeIsTooBig

---------
### Interpreter

---------
### InvalidAccount

---------
### InvalidGasCheckpoint

---------
### InvalidSalt

---------
### IteratorIdOverflow

---------
### IteratorNotFound

---------
### IteratorValueNotFound

---------
### LabelTooBig

---------
### NonceOverflow

---------
### NotAuthorized

---------
### NotEnoughFundsForUpload

---------
### NotImplemented

---------
### OutOfGas

---------
### Precompile

---------
### QueryDeserialize

---------
### ReadOnlyViolation

---------
### RefcountOverflow

---------
### Rpc

---------
### SignatureVerificationError

---------
### StackOverflow

---------
### SubstrateDispatch

---------
### TransferFailed

---------
### UnknownDenom

---------
### Unsupported

---------
### VMDepthOverflow

---------
### VirtualMachine

---------
### VmCreation

---------