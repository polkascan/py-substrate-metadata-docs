
# PhalaPhatContracts

---------
## Calls

---------
### add_cluster
Create a new cluster

\# Arguments
- `owner` - The owner of the cluster.
- `permission` - Who can deploy contracts in the cluster.
- `deploy_workers` - Workers included in the cluster.
- `deposit` - Transfer amount of tokens from the owner on chain to the owner in cluster.
- `gas_price` - Gas price for contract transactions.
- `deposit_per_item` - Price for contract storage per item.
- `deposit_per_byte` - Price for contract storage per byte.
- `treasury_account` - The treasury account used to collect the gas and storage fee.
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner | `T::AccountId` | 
| permission | `ClusterPermission<T::AccountId>` | 
| deploy_workers | `Vec<WorkerPublicKey>` | 
| deposit | `BalanceOf<T>` | 
| gas_price | `BalanceOf<T>` | 
| deposit_per_item | `BalanceOf<T>` | 
| deposit_per_byte | `BalanceOf<T>` | 
| treasury_account | `AccountId32` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaPhatContracts', 'add_cluster', {
    'deploy_workers': ['[u8; 32]'],
    'deposit': 'u128',
    'deposit_per_byte': 'u128',
    'deposit_per_item': 'u128',
    'gas_price': 'u128',
    'owner': 'AccountId',
    'permission': {
        'OnlyOwner': 'AccountId',
        'Public': None,
    },
    'treasury_account': 'AccountId',
}
)
```

---------
### add_worker_to_cluster
Add a new worker to a cluster
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_pubkey | `WorkerPublicKey` | 
| cluster_id | `ContractClusterId` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaPhatContracts', 'add_worker_to_cluster', {
    'cluster_id': '[u8; 32]',
    'worker_pubkey': '[u8; 32]',
}
)
```

---------
### cluster_destroy
#### Attributes
| Name | Type |
| -------- | -------- | 
| cluster | `ContractClusterId` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaPhatContracts', 'cluster_destroy', {'cluster': '[u8; 32]'}
)
```

---------
### cluster_upload_resource
#### Attributes
| Name | Type |
| -------- | -------- | 
| cluster_id | `ContractClusterId` | 
| resource_type | `ResourceType` | 
| resource_data | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaPhatContracts', 'cluster_upload_resource', {
    'cluster_id': '[u8; 32]',
    'resource_data': 'Bytes',
    'resource_type': (
        'InkCode',
        'SidevmCode',
        'IndeterministicInkCode',
    ),
}
)
```

---------
### instantiate_contract
#### Attributes
| Name | Type |
| -------- | -------- | 
| code_index | `CodeIndex<CodeHash<T>>` | 
| data | `Vec<u8>` | 
| salt | `Vec<u8>` | 
| cluster_id | `ContractClusterId` | 
| transfer | `BalanceOf<T>` | 
| gas_limit | `u64` | 
| storage_deposit_limit | `Option<BalanceOf<T>>` | 
| deposit | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaPhatContracts', 'instantiate_contract', {
    'cluster_id': '[u8; 32]',
    'code_index': {
        'WasmCode': '[u8; 32]',
    },
    'data': 'Bytes',
    'deposit': 'u128',
    'gas_limit': 'u64',
    'salt': 'Bytes',
    'storage_deposit_limit': (
        None,
        'u128',
    ),
    'transfer': 'u128',
}
)
```

---------
### push_contract_message
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract_id | `ContractId` | 
| payload | `Vec<u8>` | 
| deposit | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaPhatContracts', 'push_contract_message', {
    'contract_id': '[u8; 32]',
    'deposit': 'u128',
    'payload': 'Bytes',
}
)
```

---------
### remove_worker_from_cluster
Remove a new worker from a cluster
#### Attributes
| Name | Type |
| -------- | -------- | 
| worker_pubkey | `WorkerPublicKey` | 
| cluster_id | `ContractClusterId` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaPhatContracts', 'remove_worker_from_cluster', {
    'cluster_id': '[u8; 32]',
    'worker_pubkey': '[u8; 32]',
}
)
```

---------
### set_pink_runtime_version
#### Attributes
| Name | Type |
| -------- | -------- | 
| version | `(u32, u32)` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaPhatContracts', 'set_pink_runtime_version', {'version': ('u32', 'u32')}
)
```

---------
### set_pink_system_code
#### Attributes
| Name | Type |
| -------- | -------- | 
| code | `BoundedVec<u8, T::InkCodeSizeLimit>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaPhatContracts', 'set_pink_system_code', {'code': 'Bytes'}
)
```

---------
### transfer_to_cluster
Transfer `amount` of on-chain token to the `dest_account` in the cluster of id `cluster_id`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 
| cluster_id | `ContractClusterId` | 
| dest_account | `AccountId32` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaPhatContracts', 'transfer_to_cluster', {
    'amount': 'u128',
    'cluster_id': '[u8; 32]',
    'dest_account': 'AccountId',
}
)
```

---------
## Events

---------
### ClusterCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| cluster | `ContractClusterId` | ```[u8; 32]```
| system_contract | `ContractId` | ```[u8; 32]```

---------
### ClusterDeployed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| cluster | `ContractClusterId` | ```[u8; 32]```
| pubkey | `ClusterPublicKey` | ```[u8; 32]```
| worker | `WorkerPublicKey` | ```[u8; 32]```

---------
### ClusterDeploymentFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| cluster | `ContractClusterId` | ```[u8; 32]```
| worker | `WorkerPublicKey` | ```[u8; 32]```

---------
### ClusterDestroyed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| cluster | `ContractClusterId` | ```[u8; 32]```

---------
### ClusterPubkeyAvailable
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| cluster | `ContractClusterId` | ```[u8; 32]```
| pubkey | `ClusterPublicKey` | ```[u8; 32]```

---------
### ContractPubkeyAvailable
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| contract | `ContractId` | ```[u8; 32]```
| cluster | `ContractClusterId` | ```[u8; 32]```
| pubkey | `ContractPublicKey` | ```[u8; 32]```

---------
### Instantiated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| contract | `ContractId` | ```[u8; 32]```
| cluster | `ContractClusterId` | ```[u8; 32]```
| deployer | `H256` | ```[u8; 32]```

---------
### Instantiating
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| contract | `ContractId` | ```[u8; 32]```
| cluster | `ContractClusterId` | ```[u8; 32]```
| deployer | `T::AccountId` | ```AccountId```

---------
### Transfered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| cluster | `ContractClusterId` | ```[u8; 32]```
| account | `H256` | ```[u8; 32]```
| amount | `BalanceOf<T>` | ```u128```

---------
### WorkerAddedToCluster
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| worker | `WorkerPublicKey` | ```[u8; 32]```
| cluster | `ContractClusterId` | ```[u8; 32]```

---------
### WorkerRemovedFromCluster
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| worker | `WorkerPublicKey` | ```[u8; 32]```
| cluster | `ContractClusterId` | ```[u8; 32]```

---------
## Storage functions

---------
### ClusterByWorkers

#### Python
```python
result = substrate.query(
    'PhalaPhatContracts', 'ClusterByWorkers', ['[u8; 32]']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### ClusterContracts

#### Python
```python
result = substrate.query(
    'PhalaPhatContracts', 'ClusterContracts', ['[u8; 32]']
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### ClusterCounter
 The contract cluster counter, it always equals to the latest cluster id.

#### Python
```python
result = substrate.query(
    'PhalaPhatContracts', 'ClusterCounter', []
)
```

#### Return value
```python
'u64'
```
---------
### ClusterWorkers

#### Python
```python
result = substrate.query(
    'PhalaPhatContracts', 'ClusterWorkers', ['[u8; 32]']
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### Clusters

#### Python
```python
result = substrate.query(
    'PhalaPhatContracts', 'Clusters', ['[u8; 32]']
)
```

#### Return value
```python
{
    'deposit_per_byte': 'u128',
    'deposit_per_item': 'u128',
    'gas_price': 'u128',
    'owner': 'AccountId',
    'permission': {'OnlyOwner': 'AccountId', 'Public': None},
    'system_contract': '[u8; 32]',
    'workers': ['[u8; 32]'],
}
```
---------
### Contracts

#### Python
```python
result = substrate.query(
    'PhalaPhatContracts', 'Contracts', ['[u8; 32]']
)
```

#### Return value
```python
{'cluster': '[u8; 32]', 'deployer': 'AccountId'}
```
---------
### NextPinkSystemCode
 The next pink-system contract code to be applied from the next block

#### Python
```python
result = substrate.query(
    'PhalaPhatContracts', 'NextPinkSystemCode', []
)
```

#### Return value
```python
'Bytes'
```
---------
### PinkRuntimeVersion
 The pink-runtime version used to deploy new clusters.
 See also: `phactory::storage::pink_runtime_version`.

#### Python
```python
result = substrate.query(
    'PhalaPhatContracts', 'PinkRuntimeVersion', []
)
```

#### Return value
```python
('u32', 'u32')
```
---------
### PinkSystemCode
 The pink-system contract code used to deploy new clusters

#### Python
```python
result = substrate.query(
    'PhalaPhatContracts', 'PinkSystemCode', []
)
```

#### Return value
```python
('u16', 'Bytes')
```
---------
### PinkSystemCodeHash
 The blake2_256 hash of the pink-system contract code.

#### Python
```python
result = substrate.query(
    'PhalaPhatContracts', 'PinkSystemCodeHash', []
)
```

#### Return value
```python
'[u8; 32]'
```
---------
## Errors

---------
### ClusterNotDeployed

---------
### ClusterNotFound

---------
### ClusterPermissionDenied

---------
### CodeNotFound

---------
### ContractNotFound

---------
### DuplicatedContract

---------
### DuplicatedDeployment

---------
### InvalidSender

---------
### NoPinkSystemCode

---------
### NoWorkerSpecified

---------
### PayloadTooLarge

---------
### WorkerIsBusy

---------
### WorkerNotFound

---------