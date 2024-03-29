
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
        'shard': 'scale_info::11',
    },
}
)
```

---------
### confirm_processed_parentchain_block
The integritee worker calls this function for every processed parentchain_block to
confirm a state update.
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
    'block_hash': 'scale_info::11',
    'block_number': 'u32',
    'trusted_calls_merkle_root': 'scale_info::11',
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
    'extra_topics': ['scale_info::11'],
    'hash': 'scale_info::11',
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
### register_enclave
#### Attributes
| Name | Type |
| -------- | -------- | 
| ra_report | `Vec<u8>` | 
| worker_url | `Vec<u8>` | 
| shielding_key | `Option<Vec<u8>>` | 
| vc_pubkey | `Option<Vec<u8>>` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'register_enclave', {
    'ra_report': 'Bytes',
    'shielding_key': (None, 'Bytes'),
    'vc_pubkey': (None, 'Bytes'),
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
### remove_scheduled_enclave
#### Attributes
| Name | Type |
| -------- | -------- | 
| sidechain_block_number | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'remove_scheduled_enclave', {'sidechain_block_number': 'u32'}
)
```

---------
### set_heartbeat_timeout
#### Attributes
| Name | Type |
| -------- | -------- | 
| timeout | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'set_heartbeat_timeout', {'timeout': 'u64'}
)
```

---------
### shield_funds
Sent by a client who requests to get shielded funds managed by an enclave. For this
on-chain balance is sent to the bonding_account of the enclave. The bonding_account does
not have a private key as the balance on this account is exclusively managed from
withing the pallet_teerex. Note: The bonding_account is bit-equivalent to the worker
shard.
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
    'call_hash': 'scale_info::11',
    'public_account': 'AccountId',
}
)
```

---------
### update_scheduled_enclave
#### Attributes
| Name | Type |
| -------- | -------- | 
| sidechain_block_number | `u32` | 
| mr_enclave | `MrEnclave` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'update_scheduled_enclave', {
    'mr_enclave': '[u8; 32]',
    'sidechain_block_number': 'u32',
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
| None | `T::AccountId` | ```AccountId```
| None | `Vec<u8>` | ```Bytes```

---------
### Forwarded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ShardIdentifier` | ```scale_info::11```

---------
### ProcessedParentchainBlock
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `H256` | ```scale_info::11```
| None | `H256` | ```scale_info::11```
| None | `T::BlockNumber` | ```u32```

---------
### PublishedHash
An enclave with [mr_enclave] has published some [hash] with some metadata [data].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| mr_enclave | `MrEnclave` | ```[u8; 32]```
| hash | `H256` | ```scale_info::11```
| data | `Vec<u8>` | ```Bytes```

---------
### RemovedEnclave
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### RemovedScheduledEnclave
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### SetHeartbeatTimeout
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u64` | ```u64```

---------
### ShieldFunds
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<u8>` | ```Bytes```

---------
### UnshieldedFunds
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### UpdatedScheduledEnclave
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```
| None | `MrEnclave` | ```[u8; 32]```

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
    'shielding_key': (None, 'Bytes'),
    'timestamp': 'u64',
    'url': 'Bytes',
    'vc_pubkey': (None, 'Bytes'),
}
```
---------
### ExecutedCalls

#### Python
```python
result = substrate.query(
    'Teerex', 'ExecutedCalls', ['scale_info::11']
)
```

#### Return value
```python
'u64'
```
---------
### HeartbeatTimeout

#### Python
```python
result = substrate.query(
    'Teerex', 'HeartbeatTimeout', []
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
### ScheduledEnclave

#### Python
```python
result = substrate.query(
    'Teerex', 'ScheduledEnclave', ['u32']
)
```

#### Return value
```python
'[u8; 32]'
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
### EnclaveNotInSchedule
Enclave not in the scheduled list, therefore unexpected.

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
### ScheduledEnclaveNotExist
Can not found the desired scheduled enclave.

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