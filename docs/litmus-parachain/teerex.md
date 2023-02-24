
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
### register_enclave
#### Attributes
| Name | Type |
| -------- | -------- | 
| ra_report | `Vec<u8>` | 
| worker_url | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'register_enclave', {
    'ra_report': 'Bytes',
    'worker_url': 'Bytes',
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
| None | `T::AccountId` | ```AccountId```
| None | `Vec<u8>` | ```Bytes```

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
## Errors

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
### WrongMrenclaveForBondingAccount
The bonding account doesn&\#x27;t match the enclave.

---------
### WrongMrenclaveForShard
The shard doesn&\#x27;t match the enclave.

---------