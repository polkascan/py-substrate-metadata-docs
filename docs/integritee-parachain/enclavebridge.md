
# EnclaveBridge

---------
## Calls

---------
### confirm_processed_parentchain_block
The integritee worker calls this function for every processed parentchain_block to confirm a state update.
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| block_hash | `H256` | 
| block_number | `T::BlockNumber` | 
| trusted_calls_merkle_root | `H256` | 

#### Python
```python
call = substrate.compose_call(
    'EnclaveBridge', 'confirm_processed_parentchain_block', {
    'block_hash': '[u8; 32]',
    'block_number': 'u32',
    'shard': '[u8; 32]',
    'trusted_calls_merkle_root': '[u8; 32]',
}
)
```

---------
### invoke
#### Attributes
| Name | Type |
| -------- | -------- | 
| request | `Request` | 

#### Python
```python
call = substrate.compose_call(
    'EnclaveBridge', 'invoke', {
    'request': {
        'cyphertext': 'Bytes',
        'shard': '[u8; 32]',
    },
}
)
```

---------
### publish_hash
Publish a hash as a result of an arbitrary enclave operation.

The `mrenclave` of the origin will be used as an event topic a client can subscribe to.
The concept of shards isn&\#x27;t applied here because a proof of computation should be bound
to the fingerprint of the enclave. A shard would only be necessary if state needs to be
persisted across upgrades.

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
    'EnclaveBridge', 'publish_hash', {
    'data': 'Bytes',
    'extra_topics': ['[u8; 32]'],
    'hash': '[u8; 32]',
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
| shard | `ShardIdentifier` | 
| incognito_account_encrypted | `Vec<u8>` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'EnclaveBridge', 'shield_funds', {
    'amount': 'u128',
    'incognito_account_encrypted': 'Bytes',
    'shard': '[u8; 32]',
}
)
```

---------
### unshield_funds
Sent by enclaves only as a result of an `unshield` request from a client to an enclave.
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| beneficiary | `T::AccountId` | 
| amount | `BalanceOf<T>` | 
| call_hash | `H256` | 

#### Python
```python
call = substrate.compose_call(
    'EnclaveBridge', 'unshield_funds', {
    'amount': 'u128',
    'beneficiary': 'AccountId',
    'call_hash': '[u8; 32]',
    'shard': '[u8; 32]',
}
)
```

---------
### update_shard_config
Update shard config
To be respected by L2 instances after `enactment_delay` parentchain blocks
If no previous config exists, the `enactment_delay` parameter will be ignored
and the `shard_config` will be active immediately
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| shard_config | `ShardConfig<T::AccountId>` | 
| enactment_delay | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'EnclaveBridge', 'update_shard_config', {
    'enactment_delay': 'u32',
    'shard': '[u8; 32]',
    'shard_config': {
        'authorities': (
            None,
            ['AccountId'],
        ),
        'enclave_fingerprint': '[u8; 32]',
        'maintenance_mode': 'bool',
        'max_instances': (None, 'u32'),
    },
}
)
```

---------
## Events

---------
### IndirectInvocationRegistered
an indirect invocation has been registered for execution on L2
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ShardIdentifier` | ```[u8; 32]```

---------
### ProcessedParentchainBlock
L2 confirmed processing of a parentchain block
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```[u8; 32]```
| block_hash | `H256` | ```[u8; 32]```
| trusted_calls_merkle_root | `H256` | ```[u8; 32]```
| block_number | `T::BlockNumber` | ```u32```

---------
### PublishedHash
An enclave has published some [hash] with some metadata [data].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| enclave_fingerprint | `EnclaveFingerprint` | ```[u8; 32]```
| hash | `H256` | ```[u8; 32]```
| data | `Vec<u8>` | ```Bytes```

---------
### ShardConfigUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ShardIdentifier` | ```[u8; 32]```

---------
### ShieldFunds
funds have been shielded to L2
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```[u8; 32]```
| encrypted_beneficiary | `Vec<u8>` | ```Bytes```
| amount | `BalanceOf<T>` | ```u128```

---------
### UnshieldedFunds
funds have been unshielded from L2 back to L1
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```[u8; 32]```
| beneficiary | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### ExecutedUnshieldCalls

#### Python
```python
result = substrate.query(
    'EnclaveBridge', 'ExecutedUnshieldCalls', ['[u8; 32]']
)
```

#### Return value
```python
'u64'
```
---------
### ShardConfigRegistry
 this registry holds shard configurations as well as pending updates thereof.
 We decided to put config and update data in the same storage for performance reasons.
 see argumentation and benchmarks here:
 https://github.com/integritee-network/pallets/pull/201\#discussion_r1263668271

#### Python
```python
result = substrate.query(
    'EnclaveBridge', 'ShardConfigRegistry', ['[u8; 32]']
)
```

#### Return value
```python
{
    'active_config': {
        'authorities': (None, ['AccountId']),
        'enclave_fingerprint': '[u8; 32]',
        'maintenance_mode': 'bool',
        'max_instances': (None, 'u32'),
    },
    'pending_upgrade': (
        None,
        {
            'authorities': (None, ['AccountId']),
            'enclave_fingerprint': '[u8; 32]',
            'maintenance_mode': 'bool',
            'max_instances': (None, 'u32'),
        },
    ),
    'upgrade_at': (None, 'u32'),
}
```
---------
### ShardStatus

#### Python
```python
result = substrate.query(
    'EnclaveBridge', 'ShardStatus', ['[u8; 32]']
)
```

#### Return value
```python
[{'fingerprint': '[u8; 32]', 'last_activity': 'u32', 'signer': 'AccountId'}]
```
---------
## Errors

---------
### DataTooLong
The length of the `data` passed to `publish_hash` exceeds the limit.

---------
### TooManyTopics
The number of `extra_topics` passed to `publish_hash` exceeds the limit.

---------
### WrongFingerprintForShard
The shard doesn&\#x27;t match the enclave.

---------