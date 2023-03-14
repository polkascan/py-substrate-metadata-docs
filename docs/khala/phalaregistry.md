
# PhalaRegistry

---------
## Calls

---------
### add_pruntime
Registers a pruntime binary to [`PRuntimeAllowList`]

Can only be called by `GovernanceOrigin`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pruntime_hash | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaRegistry', 'add_pruntime', {'pruntime_hash': 'Bytes'}
)
```

---------
### add_relaychain_genesis_block_hash
Adds an entry in [`RelaychainGenesisBlockHashAllowList`]

Can only be called by `GovernanceOrigin`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| genesis_block_hash | `H256` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaRegistry', 'add_relaychain_genesis_block_hash', {'genesis_block_hash': '[u8; 32]'}
)
```

---------
### force_register_topic_pubkey
Force register a topic pubkey

For test only.
#### Attributes
| Name | Type |
| -------- | -------- | 
| topic | `Vec<u8>` | 
| pubkey | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaRegistry', 'force_register_topic_pubkey', {'pubkey': 'Bytes', 'topic': 'Bytes'}
)
```

---------
### force_register_worker
Force register a worker with the given pubkey with sudo permission

For test only.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pubkey | `WorkerPublicKey` | 
| ecdh_pubkey | `EcdhPublicKey` | 
| operator | `Option<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaRegistry', 'force_register_worker', {
    'ecdh_pubkey': '[u8; 32]',
    'operator': (None, 'AccountId'),
    'pubkey': '[u8; 32]',
}
)
```

---------
### force_set_benchmark_duration
Sets [`BenchmarkDuration`]

Can only be called by `GovernanceOrigin`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaRegistry', 'force_set_benchmark_duration', {'value': 'u32'}
)
```

---------
### register_gatekeeper
Register a gatekeeper.

Can only be called by `GovernanceOrigin`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| gatekeeper | `WorkerPublicKey` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaRegistry', 'register_gatekeeper', {'gatekeeper': '[u8; 32]'}
)
```

---------
### register_worker
Registers a worker on the blockchain
This is the legacy version that support EPID attestation type only.

Usually called by a bridging relayer program (`pherry` and `prb`). Can be called by
anyone on behalf of a worker.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pruntime_info | `WorkerRegistrationInfo<T::AccountId>` | 
| attestation | `Attestation` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaRegistry', 'register_worker', {
    'attestation': {
        'SgxIas': {
            'ra_report': 'Bytes',
            'raw_signing_cert': 'Bytes',
            'signature': 'Bytes',
        },
    },
    'pruntime_info': {
        'ecdh_pubkey': '[u8; 32]',
        'features': ['u32'],
        'genesis_block_hash': '[u8; 32]',
        'machine_id': 'Bytes',
        'operator': (
            None,
            'AccountId',
        ),
        'pubkey': '[u8; 32]',
        'version': 'u32',
    },
}
)
```

---------
### register_worker_v2
Registers a worker on the blockchain.
This is the version 2 that both support DCAP attestation type.

Usually called by a bridging relayer program (`pherry` and `prb`). Can be called by
anyone on behalf of a worker.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pruntime_info | `WorkerRegistrationInfoV2<T::AccountId>` | 
| attestation | `Option<AttestationReport>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaRegistry', 'register_worker_v2', {
    'attestation': (
        None,
        {
            'SgxIas': {
                'ra_report': 'Bytes',
                'raw_signing_cert': 'Bytes',
                'signature': 'Bytes',
            },
        },
    ),
    'pruntime_info': {
        'ecdh_pubkey': '[u8; 32]',
        'features': ['u32'],
        'genesis_block_hash': '[u8; 32]',
        'machine_id': 'Bytes',
        'max_consensus_version': 'u32',
        'operator': (
            None,
            'AccountId',
        ),
        'para_id': 'u32',
        'pubkey': '[u8; 32]',
        'version': 'u32',
    },
}
)
```

---------
### remove_pruntime
Removes a pruntime binary from [`PRuntimeAllowList`]

Can only be called by `GovernanceOrigin`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pruntime_hash | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaRegistry', 'remove_pruntime', {'pruntime_hash': 'Bytes'}
)
```

---------
### remove_relaychain_genesis_block_hash
Deletes an entry in [`RelaychainGenesisBlockHashAllowList`]

Can only be called by `GovernanceOrigin`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| genesis_block_hash | `H256` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaRegistry', 'remove_relaychain_genesis_block_hash', {'genesis_block_hash': '[u8; 32]'}
)
```

---------
### rotate_master_key
Rotate the master key
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'PhalaRegistry', 'rotate_master_key', {}
)
```

---------
### set_minimum_pruntime_version
Set minimum pRuntime version. Versions less than MinimumPRuntimeVersion would be forced to quit.

Can only be called by `GovernanceOrigin`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| major | `u32` | 
| minor | `u32` | 
| patch | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaRegistry', 'set_minimum_pruntime_version', {
    'major': 'u32',
    'minor': 'u32',
    'patch': 'u32',
}
)
```

---------
### set_pruntime_consensus_version
Set the consensus version used by pruntime. PRuntimes would switch some code path according
the current consensus version.

Can only be called by `GovernanceOrigin`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| version | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaRegistry', 'set_pruntime_consensus_version', {'version': 'u32'}
)
```

---------
### unregister_gatekeeper
Unregister a gatekeeper

At least one gatekeeper should be available
#### Attributes
| Name | Type |
| -------- | -------- | 
| gatekeeper | `WorkerPublicKey` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaRegistry', 'unregister_gatekeeper', {'gatekeeper': '[u8; 32]'}
)
```

---------
### update_worker_endpoint
#### Attributes
| Name | Type |
| -------- | -------- | 
| endpoint_payload | `WorkerEndpointPayload` | 
| signature | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaRegistry', 'update_worker_endpoint', {
    'endpoint_payload': {
        'pubkey': '[u8; 32]',
        'signing_time': 'u64',
        'versioned_endpoints': {
            'V1': ['Str'],
        },
    },
    'signature': 'Bytes',
}
)
```

---------
## Events

---------
### GatekeeperAdded
A new Gatekeeper is enabled on the blockchain
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pubkey | `WorkerPublicKey` | ```[u8; 32]```

---------
### GatekeeperRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pubkey | `WorkerPublicKey` | ```[u8; 32]```

---------
### InitialScoreSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pubkey | `WorkerPublicKey` | ```[u8; 32]```
| init_score | `u32` | ```u32```

---------
### MasterKeyRotated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| rotation_id | `u64` | ```u64```
| master_pubkey | `MasterPublicKey` | ```[u8; 32]```

---------
### MasterKeyRotationFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| rotation_lock | `Option<u64>` | ```(None, 'u64')```
| gatekeeper_rotation_id | `u64` | ```u64```

---------
### MinimumPRuntimeVersionChangedTo
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```
| None | `u32` | ```u32```
| None | `u32` | ```u32```

---------
### PRuntimeConsensusVersionChangedTo
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### WorkerAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pubkey | `WorkerPublicKey` | ```[u8; 32]```
| attestation_provider | `Option<AttestationProvider>` | ```(None, ('Root', 'Ias'))```
| confidence_level | `u8` | ```u8```

---------
### WorkerUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pubkey | `WorkerPublicKey` | ```[u8; 32]```
| attestation_provider | `Option<AttestationProvider>` | ```(None, ('Root', 'Ias'))```
| confidence_level | `u8` | ```u8```

---------
## Storage functions

---------
### BenchmarkDuration
 The number of blocks to run the benchmark

#### Python
```python
result = substrate.query(
    'PhalaRegistry', 'BenchmarkDuration', []
)
```

#### Return value
```python
'u32'
```
---------
### ClusterKeys

#### Python
```python
result = substrate.query(
    'PhalaRegistry', 'ClusterKeys', ['[u8; 32]']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### ContractKeys
 Mapping from contract address to pubkey

#### Python
```python
result = substrate.query(
    'PhalaRegistry', 'ContractKeys', ['[u8; 32]']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### Endpoints
 Mapping from worker pubkey to Phala Network identity

#### Python
```python
result = substrate.query(
    'PhalaRegistry', 'Endpoints', ['[u8; 32]']
)
```

#### Return value
```python
{'V1': ['Str']}
```
---------
### Gatekeeper
 Gatekeeper pubkey list

#### Python
```python
result = substrate.query(
    'PhalaRegistry', 'Gatekeeper', []
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### GatekeeperMasterPubkey
 Gatekeeper master pubkey

#### Python
```python
result = substrate.query(
    'PhalaRegistry', 'GatekeeperMasterPubkey', []
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### MasterKeyRotationLock
 Current rotation info including rotation id

 Only one rotation process is allowed at one time.
 Since the rotation request is broadcasted to all gatekeepers, it should be finished only if there is one functional
 gatekeeper.

#### Python
```python
result = substrate.query(
    'PhalaRegistry', 'MasterKeyRotationLock', []
)
```

#### Return value
```python
(None, 'u64')
```
---------
### MaxKnownPRuntimeConsensusVersion
 The max consensus version that pruntime has report via register_worker

#### Python
```python
result = substrate.query(
    'PhalaRegistry', 'MaxKnownPRuntimeConsensusVersion', []
)
```

#### Return value
```python
{'count': 'u32', 'version': 'u32'}
```
---------
### MinimumPRuntimeVersion
 PRuntimes whoes version less than MinimumPRuntimeVersion would be forced to quit.

#### Python
```python
result = substrate.query(
    'PhalaRegistry', 'MinimumPRuntimeVersion', []
)
```

#### Return value
```python
('u32', 'u32', 'u32')
```
---------
### PRuntimeAddedAt
 The effective height of pRuntime binary

#### Python
```python
result = substrate.query(
    'PhalaRegistry', 'PRuntimeAddedAt', ['Bytes']
)
```

#### Return value
```python
'u32'
```
---------
### PRuntimeAllowList
 Allow list of pRuntime binary digest

 Only pRuntime within the list can register.

#### Python
```python
result = substrate.query(
    'PhalaRegistry', 'PRuntimeAllowList', []
)
```

#### Return value
```python
['Bytes']
```
---------
### PRuntimeConsensusVersion
 The consensus version used by pruntime. PRuntimes would switch some code path according
 the current consensus version.

#### Python
```python
result = substrate.query(
    'PhalaRegistry', 'PRuntimeConsensusVersion', []
)
```

#### Return value
```python
'u32'
```
---------
### RelaychainGenesisBlockHashAllowList
 Allow list of relaychain genesis

 Only genesis within the list can do register.

#### Python
```python
result = substrate.query(
    'PhalaRegistry', 'RelaychainGenesisBlockHashAllowList', []
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### RotationCounter
 The rotation counter starting from 1, it always equals to the latest rotation id.
 The totation id 0 is reserved for the first master key before we introduce the rotation.

#### Python
```python
result = substrate.query(
    'PhalaRegistry', 'RotationCounter', []
)
```

#### Return value
```python
'u64'
```
---------
### TempWorkersIterKey
 Allow list of pRuntime binary digest

 Only pRuntime within the list can register.

#### Python
```python
result = substrate.query(
    'PhalaRegistry', 'TempWorkersIterKey', []
)
```

#### Return value
```python
(None, 'Bytes')
```
---------
### TopicKey
 Pubkey for secret topics.

#### Python
```python
result = substrate.query(
    'PhalaRegistry', 'TopicKey', ['Bytes']
)
```

#### Return value
```python
'Bytes'
```
---------
### WorkerAddedAt
 The first time registered block number for each worker.

#### Python
```python
result = substrate.query(
    'PhalaRegistry', 'WorkerAddedAt', ['[u8; 32]']
)
```

#### Return value
```python
'u32'
```
---------
### Workers
 Mapping from worker pubkey to WorkerInfo

#### Python
```python
result = substrate.query(
    'PhalaRegistry', 'Workers', ['[u8; 32]']
)
```

#### Return value
```python
{
    'attestation_provider': (None, ('Root', 'Ias')),
    'confidence_level': 'u8',
    'ecdh_pubkey': '[u8; 32]',
    'features': ['u32'],
    'initial_score': (None, 'u32'),
    'last_updated': 'u64',
    'operator': (None, 'AccountId'),
    'pubkey': '[u8; 32]',
    'runtime_version': 'u32',
}
```
---------
## Constants

---------
### NoneAttestationEnabled
 Enable None Attestation, SHOULD BE SET TO FALSE ON PRODUCTION !!!
#### Value
```python
False
```
#### Python
```python
constant = substrate.get_constant('PhalaRegistry', 'NoneAttestationEnabled')
```
---------
### VerifyPRuntime
 Verify attestation

 SHOULD NOT SET TO FALSE ON PRODUCTION!!!
#### Value
```python
True
```
#### Python
```python
constant = substrate.get_constant('PhalaRegistry', 'VerifyPRuntime')
```
---------
### VerifyRelaychainGenesisBlockHash
 Verify relaychain genesis

 SHOULD NOT SET TO FALSE ON PRODUCTION!!!
#### Value
```python
True
```
#### Python
```python
constant = substrate.get_constant('PhalaRegistry', 'VerifyRelaychainGenesisBlockHash')
```
---------
## Errors

---------
### BadIASReport

---------
### CannotHandleUnknownMessage

---------
### CannotRemoveLastGatekeeper

---------
### GenesisBlockHashAlreadyExists

---------
### GenesisBlockHashNotFound

---------
### GenesisBlockHashRejected

---------
### InvalidBenchReport

---------
### InvalidConsensusVersion

---------
### InvalidEndpointSigningTime

---------
### InvalidGatekeeper

---------
### InvalidIASSigningCert

---------
### InvalidInput

---------
### InvalidMasterPubkey

---------
### InvalidPubKey

---------
### InvalidQuoteStatus

---------
### InvalidReport

---------
### InvalidRotatedMasterPubkey

---------
### InvalidRuntimeInfo

---------
### InvalidRuntimeInfoHash

---------
### InvalidSender

---------
### InvalidSignature

---------
### InvalidSignatureLength

---------
### MalformedSignature

---------
### MasterKeyInRotation

---------
### MasterKeyMismatch

---------
### MasterKeyUninitialized

---------
### NoneAttestationDisabled

---------
### NotImplemented

---------
### NotMigrationRoot
Migration root not authorized

---------
### OutdatedIASReport

---------
### PRuntimeAlreadyExists

---------
### PRuntimeNotFound

---------
### PRuntimeRejected

---------
### ParachainIdMismatch

---------
### UnknownCluster

---------
### UnknownContract

---------
### UnknownQuoteBodyFormat

---------
### WorkerNotFound

---------