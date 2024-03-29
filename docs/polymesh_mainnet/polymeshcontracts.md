
# PolymeshContracts

---------
## Calls

---------
### instantiate_with_code_as_primary_key
Instantiates a smart contract defining it with the given `code` and `salt`.

The contract will be attached as a primary key of a newly created child identity of the caller.

\# Arguments
- `endowment`: Amount of POLYX to transfer to the contract.
- `gas_limit`: For how much gas the `deploy` code in the contract may at most consume.
- `storage_deposit_limit`: The maximum amount of balance that can be charged/reserved from the caller to pay for the storage consumed.
- `code`: The WASM binary defining the smart contract.
- `data`: The input data to pass to the contract constructor.
- `salt`: Used for contract address derivation. By varying this, the same `code` can be used under the same identity.

#### Attributes
| Name | Type |
| -------- | -------- | 
| endowment | `Balance` | 
| gas_limit | `Weight` | 
| storage_deposit_limit | `Option<Balance>` | 
| code | `Vec<u8>` | 
| data | `Vec<u8>` | 
| salt | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'PolymeshContracts', 'instantiate_with_code_as_primary_key', {
    'code': 'Bytes',
    'data': 'Bytes',
    'endowment': 'u128',
    'gas_limit': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
    'salt': 'Bytes',
    'storage_deposit_limit': (
        None,
        'u128',
    ),
}
)
```

---------
### instantiate_with_code_perms
Instantiates a smart contract defining it with the given `code` and `salt`.

The contract will be attached as a secondary key,
with `perms` as its permissions, to `origin`&\#x27;s identity.

The contract is transferred `endowment` amount of POLYX.
This is distinct from the `gas_limit`,
which controls how much gas the deployment code may at most consume.

\# Arguments
- `endowment` amount of POLYX to transfer to the contract.
- `gas_limit` for how much gas the `deploy` code in the contract may at most consume.
- `storage_deposit_limit` The maximum amount of balance that can be charged/reserved
  from the caller to pay for the storage consumed.
- `code` with the WASM binary defining the smart contract.
- `data` The input data to pass to the contract constructor.
- `salt` used for contract address derivation.
   By varying this, the same `code` can be used under the same identity.
- `perms` that the new secondary key will have.

\# Errors
- All the errors in `pallet_contracts::Call::instantiate_with_code` can also happen here.
- CDD/Permissions are checked, unlike in `pallet_contracts`.
- Errors that arise when adding a new secondary key can also occur here.
#### Attributes
| Name | Type |
| -------- | -------- | 
| endowment | `Balance` | 
| gas_limit | `Weight` | 
| storage_deposit_limit | `Option<Balance>` | 
| code | `Vec<u8>` | 
| data | `Vec<u8>` | 
| salt | `Vec<u8>` | 
| perms | `Permissions` | 

#### Python
```python
call = substrate.compose_call(
    'PolymeshContracts', 'instantiate_with_code_perms', {
    'code': 'Bytes',
    'data': 'Bytes',
    'endowment': 'u128',
    'gas_limit': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
    'perms': {
        'asset': {
            'Except': 'scale_info::44',
            'These': 'scale_info::44',
            'Whole': None,
        },
        'extrinsic': {
            'Except': 'scale_info::53',
            'These': 'scale_info::53',
            'Whole': None,
        },
        'portfolio': {
            'Except': 'scale_info::59',
            'These': 'scale_info::59',
            'Whole': None,
        },
    },
    'salt': 'Bytes',
    'storage_deposit_limit': (
        None,
        'u128',
    ),
}
)
```

---------
### instantiate_with_hash_as_primary_key
Instantiates a smart contract defining using the given `code_hash` and `salt`.

Unlike `instantiate_with_code`, this assumes that at least one contract with the same WASM code has already been uploaded.

The contract will be attached as a primary key of a newly created child identity of the caller.

\# Arguments
- `endowment`: amount of POLYX to transfer to the contract.
- `gas_limit`: for how much gas the `deploy` code in the contract may at most consume.
- `storage_deposit_limit`: The maximum amount of balance that can be charged/reserved from the caller to pay for the storage consumed.
- `code_hash`: of an already uploaded WASM binary.
- `data`: The input data to pass to the contract constructor.
- `salt`: used for contract address derivation. By varying this, the same `code` can be used under the same identity.

#### Attributes
| Name | Type |
| -------- | -------- | 
| endowment | `Balance` | 
| gas_limit | `Weight` | 
| storage_deposit_limit | `Option<Balance>` | 
| code_hash | `CodeHash<T>` | 
| data | `Vec<u8>` | 
| salt | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'PolymeshContracts', 'instantiate_with_hash_as_primary_key', {
    'code_hash': 'scale_info::11',
    'data': 'Bytes',
    'endowment': 'u128',
    'gas_limit': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
    'salt': 'Bytes',
    'storage_deposit_limit': (
        None,
        'u128',
    ),
}
)
```

---------
### instantiate_with_hash_perms
Instantiates a smart contract defining using the given `code_hash` and `salt`.

Unlike `instantiate_with_code`,
this assumes that at least one contract with the same WASM code has already been uploaded.

The contract will be attached as a secondary key,
with `perms` as its permissions, to `origin`&\#x27;s identity.

The contract is transferred `endowment` amount of POLYX.
This is distinct from the `gas_limit`,
which controls how much gas the deployment code may at most consume.

\# Arguments
- `endowment` amount of POLYX to transfer to the contract.
- `gas_limit` for how much gas the `deploy` code in the contract may at most consume.
- `storage_deposit_limit` The maximum amount of balance that can be charged/reserved
  from the caller to pay for the storage consumed.
- `code_hash` of an already uploaded WASM binary.
- `data` The input data to pass to the contract constructor.
- `salt` used for contract address derivation.
   By varying this, the same `code` can be used under the same identity.
- `perms` that the new secondary key will have.

\# Errors
- All the errors in `pallet_contracts::Call::instantiate` can also happen here.
- CDD/Permissions are checked, unlike in `pallet_contracts`.
- Errors that arise when adding a new secondary key can also occur here.
#### Attributes
| Name | Type |
| -------- | -------- | 
| endowment | `Balance` | 
| gas_limit | `Weight` | 
| storage_deposit_limit | `Option<Balance>` | 
| code_hash | `CodeHash<T>` | 
| data | `Vec<u8>` | 
| salt | `Vec<u8>` | 
| perms | `Permissions` | 

#### Python
```python
call = substrate.compose_call(
    'PolymeshContracts', 'instantiate_with_hash_perms', {
    'code_hash': 'scale_info::11',
    'data': 'Bytes',
    'endowment': 'u128',
    'gas_limit': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
    'perms': {
        'asset': {
            'Except': 'scale_info::44',
            'These': 'scale_info::44',
            'Whole': None,
        },
        'extrinsic': {
            'Except': 'scale_info::53',
            'These': 'scale_info::53',
            'Whole': None,
        },
        'portfolio': {
            'Except': 'scale_info::59',
            'These': 'scale_info::59',
            'Whole': None,
        },
    },
    'salt': 'Bytes',
    'storage_deposit_limit': (
        None,
        'u128',
    ),
}
)
```

---------
### update_call_runtime_whitelist
Update CallRuntime whitelist.

\# Arguments

\# Errors
#### Attributes
| Name | Type |
| -------- | -------- | 
| updates | `Vec<(ExtrinsicId, bool)>` | 

#### Python
```python
call = substrate.compose_call(
    'PolymeshContracts', 'update_call_runtime_whitelist', {'updates': [(('u8', 'u8'), 'bool')]}
)
```

---------
### upgrade_api
#### Attributes
| Name | Type |
| -------- | -------- | 
| api | `Api` | 
| next_upgrade | `NextUpgrade<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PolymeshContracts', 'upgrade_api', {
    'api': {
        'desc': '[u8; 4]',
        'major': 'u32',
    },
    'next_upgrade': {
        'api_hash': {
            'hash': 'scale_info::11',
        },
        'chain_version': {
            'spec_version': 'u32',
            'tx_version': 'u32',
        },
    },
}
)
```

---------
## Events

---------
### ApiHashUpdated
Emitted when a contract starts supporting a new API upgrade.
Contains the [`Api`], [`ChainVersion`], and the bytes for the code hash.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Api` | ```{'desc': '[u8; 4]', 'major': 'u32'}```
| None | `ChainVersion` | ```{'spec_version': 'u32', 'tx_version': 'u32'}```
| None | `Hash` | ```scale_info::11```

---------
### SCRuntimeCall
Emitted when a contract calls into the runtime.
Contains the account id set by the contract owner and the [`ExtrinsicId`].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `ExtrinsicId` | ```('u8', 'u8')```

---------
## Storage functions

---------
### ApiNextUpgrade
 Stores the chain version and code hash for the next chain upgrade.

#### Python
```python
result = substrate.query(
    'PolymeshContracts', 'ApiNextUpgrade', [{'desc': '[u8; 4]', 'major': 'u32'}]
)
```

#### Return value
```python
{
    'api_hash': {'hash': 'scale_info::11'},
    'chain_version': {'spec_version': 'u32', 'tx_version': 'u32'},
}
```
---------
### CallRuntimeWhitelist
 Whitelist of extrinsics allowed to be called from contracts.

#### Python
```python
result = substrate.query(
    'PolymeshContracts', 'CallRuntimeWhitelist', [('u8', 'u8')]
)
```

#### Return value
```python
'bool'
```
---------
### CurrentApiHash
 Stores the code hash for the current api.

#### Python
```python
result = substrate.query(
    'PolymeshContracts', 'CurrentApiHash', [{'desc': '[u8; 4]', 'major': 'u32'}]
)
```

#### Return value
```python
{'hash': 'scale_info::11'}
```
---------
### StorageVersion
 Storage version.

#### Python
```python
result = substrate.query(
    'PolymeshContracts', 'StorageVersion', []
)
```

#### Return value
```python
'u8'
```
---------
## Errors

---------
### CallerNotAPrimaryKey
The caller is not a primary key.

---------
### DataLeftAfterDecoding
Data left in input when decoding arguments of a call.

---------
### InLenTooLarge
Input data that a contract passed when using the ChainExtension was too large.

---------
### InstantiatorWithNoIdentity
A contract was attempted to be instantiated,
but no identity was given to associate the new contract&\#x27;s key with.

---------
### InvalidChainVersion
Only future chain versions are allowed.

---------
### InvalidFuncId
Invalid `func_id` provided from contract.

---------
### InvalidRuntimeCall
Failed to decode a valid `RuntimeCall`.

---------
### MissingKeyPermissions
Secondary key permissions are missing.

---------
### NoUpgradesSupported
There are no api upgrades supported for the contract.

---------
### OutLenTooLarge
Output data returned from the ChainExtension was too large.

---------
### ReadStorageFailed
`ReadStorage` failed to write value into the contract&\#x27;s buffer.

---------
### RuntimeCallDenied
Extrinsic is not allowed to be called by contracts.

---------