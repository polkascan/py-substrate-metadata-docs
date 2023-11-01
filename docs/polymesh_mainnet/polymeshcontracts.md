
# PolymeshContracts

---------
## Calls

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
    'code_hash': '[u8; 32]',
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
## Storage functions

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
### InvalidFuncId
Invalid `func_id` provided from contract.

---------
### InvalidRuntimeCall
Failed to decode a valid `RuntimeCall`.

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