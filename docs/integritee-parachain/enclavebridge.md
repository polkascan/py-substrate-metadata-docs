
# EnclaveBridge

---------
## Calls

---------
### confirm_processed_parentchain_block
See [`Pallet::confirm_processed_parentchain_block`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| block_hash | `H256` | 
| block_number | `BlockNumberFor<T>` | 
| trusted_calls_merkle_root | `H256` | 

#### Python
```python
call = substrate.compose_call(
    'EnclaveBridge', 'confirm_processed_parentchain_block', {
    'block_hash': 'scale_info::12',
    'block_number': 'u32',
    'shard': 'scale_info::12',
    'trusted_calls_merkle_root': 'scale_info::12',
}
)
```

---------
### invoke
See [`Pallet::invoke`].
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
        'shard': 'scale_info::12',
    },
}
)
```

---------
### publish_hash
See [`Pallet::publish_hash`].
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
    'extra_topics': ['scale_info::12'],
    'hash': 'scale_info::12',
}
)
```

---------
### purge_enclave_from_shard_status
See [`Pallet::purge_enclave_from_shard_status`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| subject | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'EnclaveBridge', 'purge_enclave_from_shard_status', {
    'shard': 'scale_info::12',
    'subject': 'AccountId',
}
)
```

---------
### shield_funds
See [`Pallet::shield_funds`].
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
    'shard': 'scale_info::12',
}
)
```

---------
### unshield_funds
See [`Pallet::unshield_funds`].
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
    'call_hash': 'scale_info::12',
    'shard': 'scale_info::12',
}
)
```

---------
### update_shard_config
See [`Pallet::update_shard_config`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| shard | `ShardIdentifier` | 
| shard_config | `ShardConfig<T::AccountId>` | 
| enactment_delay | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'EnclaveBridge', 'update_shard_config', {
    'enactment_delay': 'u32',
    'shard': 'scale_info::12',
    'shard_config': {
        'authorities': (
            None,
            ['AccountId'],
        ),
        'enclave_fingerprint': 'scale_info::12',
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
| None | `ShardIdentifier` | ```scale_info::12```

---------
### ProcessedParentchainBlock
L2 confirmed processing of a parentchain block
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```scale_info::12```
| block_hash | `H256` | ```scale_info::12```
| trusted_calls_merkle_root | `H256` | ```scale_info::12```
| block_number | `BlockNumberFor<T>` | ```u32```

---------
### PublishedHash
An enclave has published some [hash] with some metadata [data].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| enclave_fingerprint | `EnclaveFingerprint` | ```scale_info::12```
| hash | `H256` | ```scale_info::12```
| data | `Vec<u8>` | ```Bytes```

---------
### PurgedEnclaveFromShardConfig
An enclave has been purged from a shard status. Most likely due to inactivity
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```scale_info::12```
| subject | `T::AccountId` | ```AccountId```

---------
### ShardConfigUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ShardIdentifier` | ```scale_info::12```

---------
### ShieldFunds
funds have been shielded to L2
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```scale_info::12```
| encrypted_beneficiary | `Vec<u8>` | ```Bytes```
| amount | `BalanceOf<T>` | ```u128```

---------
### UnshieldedFunds
funds have been unshielded from L2 back to L1
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| shard | `ShardIdentifier` | ```scale_info::12```
| beneficiary | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### ExecutedUnshieldCalls

#### Python
```python
result = substrate.query(
    'EnclaveBridge', 'ExecutedUnshieldCalls', ['scale_info::12']
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
    'EnclaveBridge', 'ShardConfigRegistry', ['scale_info::12']
)
```

#### Return value
```python
{
    'active_config': {
        'authorities': (None, ['AccountId']),
        'enclave_fingerprint': 'scale_info::12',
        'maintenance_mode': 'bool',
        'max_instances': (None, 'u32'),
    },
    'pending_upgrade': (
        None,
        {
            'authorities': (None, ['AccountId']),
            'enclave_fingerprint': 'scale_info::12',
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
    'EnclaveBridge', 'ShardStatus', ['scale_info::12']
)
```

#### Return value
```python
[
    {
        'fingerprint': 'scale_info::12',
        'last_activity': 'u32',
        'signer': 'AccountId',
    },
]
```
---------
## Errors

---------
### DataTooLong
The length of the `data` passed to `publish_hash` exceeds the limit.

---------
### EnclaveNotFoundInShardStatus
No such enclave was found in shard status

---------
### ShardNotFound
Shard not found

---------
### TooManyEnclaves
Too many enclaves in ShardStatus

---------
### TooManyTopics
The number of `extra_topics` passed to `publish_hash` exceeds the limit.

---------
### WrongFingerprintForShard
The shard doesn&\#x27;t match the enclave.

---------