
# Teerex

---------
## Calls

---------
### call_worker
#### Attributes
| Name | Type |
| -------- | -------- | 
| request | `Request` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'call_worker', {
    'request': {
        'cyphertext': 'Bytes',
        'shard': '[u8; 32]',
    },
}
)
```

---------
### confirm_processed_parentchain_block
The integritee worker calls this function for every processed parentchain_block to confirm a state update.
#### Attributes
| Name | Type |
| -------- | -------- | 
| block_hash | `H256` | 
| block_number | `T::BlockNumber` | 
| trusted_calls_merkle_root | `H256` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'confirm_processed_parentchain_block', {
    'block_hash': '[u8; 32]',
    'block_number': 'u32',
    'trusted_calls_merkle_root': '[u8; 32]',
}
)
```

---------
### publish_hash
Publish a hash as a result of an arbitrary enclave operation.

The `mrenclave` of the origin will be used as an event topic a client can subscribe to.
`extra_topics`, if any, will be used as additional event topics.

`data` can be anything worthwhile publishing related to the hash. If it is a
utf8-encoded string, the UIs will usually even render the text.
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `H256` | 
| extra_topics | `Vec<T::Hash>` | 
| data | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'publish_hash', {
    'data': 'Bytes',
    'extra_topics': ['[u8; 32]'],
    'hash': '[u8; 32]',
}
)
```

---------
### register_dcap_enclave
#### Attributes
| Name | Type |
| -------- | -------- | 
| dcap_quote | `Vec<u8>` | 
| worker_url | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'register_dcap_enclave', {
    'dcap_quote': 'Bytes',
    'worker_url': 'Bytes',
}
)
```

---------
### register_ias_enclave
#### Attributes
| Name | Type |
| -------- | -------- | 
| ra_report | `Vec<u8>` | 
| worker_url | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'register_ias_enclave', {
    'ra_report': 'Bytes',
    'worker_url': 'Bytes',
}
)
```

---------
### register_quoting_enclave
#### Attributes
| Name | Type |
| -------- | -------- | 
| enclave_identity | `Vec<u8>` | 
| signature | `Vec<u8>` | 
| certificate_chain | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'register_quoting_enclave', {
    'certificate_chain': 'Bytes',
    'enclave_identity': 'Bytes',
    'signature': 'Bytes',
}
)
```

---------
### register_tcb_info
#### Attributes
| Name | Type |
| -------- | -------- | 
| tcb_info | `Vec<u8>` | 
| signature | `Vec<u8>` | 
| certificate_chain | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'register_tcb_info', {
    'certificate_chain': 'Bytes',
    'signature': 'Bytes',
    'tcb_info': 'Bytes',
}
)
```

---------
### shield_funds
Sent by a client who requests to get shielded funds managed by an enclave. For this on-chain balance is sent to the bonding_account of the enclave.
The bonding_account does not have a private key as the balance on this account is exclusively managed from withing the pallet_teerex.
Note: The bonding_account is bit-equivalent to the worker shard.
#### Attributes
| Name | Type |
| -------- | -------- | 
| incognito_account_encrypted | `Vec<u8>` | 
| amount | `BalanceOf<T>` | 
| bonding_account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'shield_funds', {
    'amount': 'u128',
    'bonding_account': 'AccountId',
    'incognito_account_encrypted': 'Bytes',
}
)
```

---------
### unregister_enclave
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'unregister_enclave', {}
)
```

---------
### unshield_funds
Sent by enclaves only as a result of an `unshield` request from a client to an enclave.
#### Attributes
| Name | Type |
| -------- | -------- | 
| public_account | `T::AccountId` | 
| amount | `BalanceOf<T>` | 
| bonding_account | `T::AccountId` | 
| call_hash | `H256` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'unshield_funds', {
    'amount': 'u128',
    'bonding_account': 'AccountId',
    'call_hash': '[u8; 32]',
    'public_account': 'AccountId',
}
)
```

---------
## Events

---------
### AddedEnclave
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| registered_by | `T::AccountId` | ```AccountId```
| worker_url | `Vec<u8>` | ```Bytes```
| tcb_status | `Option<SgxStatus>` | ```(None, ('Invalid', 'Ok', 'GroupOutOfDate', 'GroupRevoked', 'ConfigurationNeeded'))```
| attestation_method | `AttestationMethod` | ```('Dcap', 'Ias', 'Skip')```

---------
### Forwarded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ShardIdentifier` | ```[u8; 32]```

---------
### ProcessedParentchainBlock
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `H256` | ```[u8; 32]```
| None | `H256` | ```[u8; 32]```
| None | `T::BlockNumber` | ```u32```

---------
### PublishedHash
An enclave with [mr_enclave] has published some [hash] with some metadata [data].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| mr_enclave | `MrEnclave` | ```[u8; 32]```
| hash | `H256` | ```[u8; 32]```
| data | `Vec<u8>` | ```Bytes```

---------
### QuotingEnclaveRegistered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| quoting_enclave | `QuotingEnclave` | ```{'issue_date': 'u64', 'next_update': 'u64', 'miscselect': '[u8; 4]', 'miscselect_mask': '[u8; 4]', 'attributes': '[u8; 16]', 'attributes_mask': '[u8; 16]', 'mrsigner': '[u8; 32]', 'isvprodid': 'u16', 'tcb': [{'isvsvn': 'u16'}]}```

---------
### RemovedEnclave
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### ShieldFunds
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<u8>` | ```Bytes```

---------
### TcbInfoRegistered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| fmspc | `Fmspc` | ```[u8; 6]```
| on_chain_info | `TcbInfoOnChain` | ```{'issue_date': 'u64', 'next_update': 'u64', 'tcb_levels': [{'cpusvn': '[u8; 16]', 'pcesvn': 'u16'}]}```

---------
### UnshieldedFunds
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### AllowSGXDebugMode

#### Python
```python
result = substrate.query(
    'Teerex', 'AllowSGXDebugMode', []
)
```

#### Return value
```python
'bool'
```
---------
### EnclaveCount

#### Python
```python
result = substrate.query(
    'Teerex', 'EnclaveCount', []
)
```

#### Return value
```python
'u64'
```
---------
### EnclaveIndex

#### Python
```python
result = substrate.query(
    'Teerex', 'EnclaveIndex', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### EnclaveRegistry

#### Python
```python
result = substrate.query(
    'Teerex', 'EnclaveRegistry', ['u64']
)
```

#### Return value
```python
{
    'mr_enclave': '[u8; 32]',
    'pubkey': 'AccountId',
    'sgx_mode': ('Debug', 'Production'),
    'timestamp': 'u64',
    'url': 'Bytes',
}
```
---------
### ExecutedCalls

#### Python
```python
result = substrate.query(
    'Teerex', 'ExecutedCalls', ['[u8; 32]']
)
```

#### Return value
```python
'u64'
```
---------
### QuotingEnclaveRegistry

#### Python
```python
result = substrate.query(
    'Teerex', 'QuotingEnclaveRegistry', []
)
```

#### Return value
```python
{
    'attributes': '[u8; 16]',
    'attributes_mask': '[u8; 16]',
    'issue_date': 'u64',
    'isvprodid': 'u16',
    'miscselect': '[u8; 4]',
    'miscselect_mask': '[u8; 4]',
    'mrsigner': '[u8; 32]',
    'next_update': 'u64',
    'tcb': [{'isvsvn': 'u16'}],
}
```
---------
### TcbInfo

#### Python
```python
result = substrate.query(
    'Teerex', 'TcbInfo', ['[u8; 6]']
)
```

#### Return value
```python
{
    'issue_date': 'u64',
    'next_update': 'u64',
    'tcb_levels': [{'cpusvn': '[u8; 16]', 'pcesvn': 'u16'}],
}
```
---------
## Constants

---------
### MaxSilenceTime
 If a worker does not re-register within `MaxSilenceTime`, it will be unregistered.
#### Value
```python
172800000
```
#### Python
```python
constant = substrate.get_constant('Teerex', 'MaxSilenceTime')
```
---------
### MomentsPerDay
#### Value
```python
86400000
```
#### Python
```python
constant = substrate.get_constant('Teerex', 'MomentsPerDay')
```
---------
## Errors

---------
### CollateralInvalid
The provided collateral data is invalid

---------
### DataTooLong
The length of the `data` passed to `publish_hash` exceeds the limit.

---------
### EmptyEnclaveRegistry
No enclave is registered.

---------
### EnclaveIsNotRegistered
The enclave is not registered.

---------
### EnclaveSignerDecodeError
Failed to decode enclave signer.

---------
### EnclaveUrlTooLong
The worker url is too long.

---------
### RaReportTooLong
The Remote Attestation report is too long.

---------
### RemoteAttestationTooOld

---------
### RemoteAttestationVerificationFailed
Verifying RA report failed.

---------
### SenderIsNotAttestedEnclave
Sender does not match attested enclave in report.

---------
### SgxModeNotAllowed
The enclave cannot attest, because its building mode is not allowed.

---------
### TooManyTopics
The number of `extra_topics` passed to `publish_hash` exceeds the limit.

---------
### WrongMrenclaveForBondingAccount
The bonding account doesn&\#x27;t match the enclave.

---------
### WrongMrenclaveForShard
The shard doesn&\#x27;t match the enclave.

---------