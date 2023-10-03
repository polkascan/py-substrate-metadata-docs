
# AccountMigration

---------
## Calls

---------
### complete_multisig_migration
To complete the pending multisig migration.

The `_signature` should be provided by `submitter`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `AccountId32` | 
| submitter | `AccountId32` | 
| signature | `Signature` | 

#### Python
```python
call = substrate.compose_call(
    'AccountMigration', 'complete_multisig_migration', {
    'multisig': 'AccountId',
    'signature': '[u8; 64]',
    'submitter': 'AccountId',
}
)
```

---------
### migrate
Migrate all the account data under the `from` to `to`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| from | `AccountId32` | 
| to | `AccountId20` | 
| signature | `Signature` | 

#### Python
```python
call = substrate.compose_call(
    'AccountMigration', 'migrate', {
    'from': 'AccountId',
    'signature': '[u8; 64]',
    'to': '[u8; 20]',
}
)
```

---------
### migrate_multisig
Similar to `migrate` but for multisig accounts.

The `_signature` should be provided by `who`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| submitter | `AccountId32` | 
| others | `Vec<AccountId32>` | 
| threshold | `u16` | 
| to | `AccountId20` | 
| signature | `Signature` | 
| new_multisig_params | `Option<MultisigParams>` | 

#### Python
```python
call = substrate.compose_call(
    'AccountMigration', 'migrate_multisig', {
    'new_multisig_params': (
        None,
        {
            'address': '[u8; 20]',
            'members': ['[u8; 20]'],
            'threshold': 'u16',
        },
    ),
    'others': ['AccountId'],
    'signature': '[u8; 64]',
    'submitter': 'AccountId',
    'threshold': 'u16',
    'to': '[u8; 20]',
}
)
```

---------
## Events

---------
### Migrated
An account has been migrated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `AccountId32` | ```AccountId```
| to | `AccountId20` | ```[u8; 20]```

---------
### MultisigMigrated
A multisig account has been migrated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `AccountId32` | ```AccountId```
| detail | `MultisigMigrationDetail` | ```{'to': '[u8; 20]', 'members': [('AccountId', 'bool')], 'threshold': 'u16'}```

---------
### NewMultisigParamsNoted
A new multisig account params was noted/recorded on-chain.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `AccountId32` | ```AccountId```
| to | `MultisigParams` | ```{'address': '[u8; 20]', 'members': ['[u8; 20]'], 'threshold': 'u16'}```

---------
## Storage functions

---------
### Accounts
 [`frame_system::Account`] data.

 &lt;https://github.dev/paritytech/substrate/blob/19162e43be45817b44c7d48e50d03f074f60fbf4/frame/system/src/lib.rs\#L545&gt;

#### Python
```python
result = substrate.query(
    'AccountMigration', 'Accounts', ['AccountId']
)
```

#### Return value
```python
{
    'consumers': 'u32',
    'data': {
        'flags': 'u128',
        'free': 'u128',
        'frozen': 'u128',
        'reserved': 'u128',
    },
    'nonce': 'u32',
    'providers': 'u32',
    'sufficients': 'u32',
}
```
---------
### Deposits
 [`darwinia_deposit::Deposits`] data.

#### Python
```python
result = substrate.query(
    'AccountMigration', 'Deposits', ['AccountId']
)
```

#### Return value
```python
[
    {
        'expired_time': 'u128',
        'id': 'u16',
        'in_use': 'bool',
        'start_time': 'u128',
        'value': 'u128',
    },
]
```
---------
### Identities
 [`pallet_identity::IdentityOf`] data.

 &lt;https://github.com/paritytech/substrate/blob/polkadot-v0.9.30/frame/identity/src/lib.rs\#L163&gt;

#### Python
```python
result = substrate.query(
    'AccountMigration', 'Identities', ['AccountId']
)
```

#### Return value
```python
{
    'deposit': 'u128',
    'info': {
        'additional': [('scale_info::275', 'scale_info::275')],
        'display': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
        'email': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
        'image': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
        'legal': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
        'pgp_fingerprint': (None, '[u8; 20]'),
        'riot': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
        'twitter': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
        'web': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
    },
    'judgements': [
        (
            'u32',
            {
                'Erroneous': None,
                'FeePaid': 'u128',
                'KnownGood': None,
                'LowQuality': None,
                'OutOfDate': None,
                'Reasonable': None,
                'Unknown': None,
            },
        ),
    ],
}
```
---------
### KtonAccounts
 [`pallet_asset::AssetAccount`] data.

 https://github.dev/paritytech/substrate/blob/polkadot-v0.9.30/frame/assets/src/types.rs\#L115

#### Python
```python
result = substrate.query(
    'AccountMigration', 'KtonAccounts', ['AccountId']
)
```

#### Return value
```python
{
    'balance': 'u128',
    'extra': (),
    'is_frozen': 'bool',
    'reason': {
        'Consumer': None,
        'DepositHeld': 'u128',
        'DepositRefunded': None,
        'Sufficient': None,
    },
}
```
---------
### Ledgers
 [`darwinia_staking::Ledgers`] data.

#### Python
```python
result = substrate.query(
    'AccountMigration', 'Ledgers', ['AccountId']
)
```

#### Return value
```python
{
    'staked_deposits': ['u16'],
    'staked_kton': 'u128',
    'staked_ring': 'u128',
    'unstaking_deposits': [('u16', 'u32')],
    'unstaking_kton': [('u128', 'u32')],
    'unstaking_ring': [('u128', 'u32')],
}
```
---------
### Multisigs
 Multisig migration caches.

#### Python
```python
result = substrate.query(
    'AccountMigration', 'Multisigs', ['AccountId']
)
```

#### Return value
```python
{'members': [('AccountId', 'bool')], 'threshold': 'u16', 'to': '[u8; 20]'}
```
---------
## Errors

---------
### AccountAlreadyExisted
The migration destination was already taken by someone.

---------
### ExceedMaxDeposits
Exceed maximum deposit count.

---------
### ExceedMaxVestings
Exceed maximum vesting count.

---------