
# StateTrieMigration

---------
## Calls

---------
### continue_migrate
See [`Pallet::continue_migrate`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| limits | `MigrationLimits` | 
| real_size_upper | `u32` | 
| witness_task | `MigrationTask<T>` | 

#### Python
```python
call = substrate.compose_call(
    'StateTrieMigration', 'continue_migrate', {
    'limits': {
        'item': 'u32',
        'size': 'u32',
    },
    'real_size_upper': 'u32',
    'witness_task': {
        'child_items': 'u32',
        'progress_child': {
            'Complete': None,
            'LastKey': 'Bytes',
            'ToStart': None,
        },
        'progress_top': {
            'Complete': None,
            'LastKey': 'Bytes',
            'ToStart': None,
        },
        'size': 'u32',
        'top_items': 'u32',
    },
}
)
```

---------
### control_auto_migration
See [`Pallet::control_auto_migration`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| maybe_config | `Option<MigrationLimits>` | 

#### Python
```python
call = substrate.compose_call(
    'StateTrieMigration', 'control_auto_migration', {
    'maybe_config': (
        None,
        {'item': 'u32', 'size': 'u32'},
    ),
}
)
```

---------
### force_set_progress
See [`Pallet::force_set_progress`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| progress_top | `ProgressOf<T>` | 
| progress_child | `ProgressOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'StateTrieMigration', 'force_set_progress', {
    'progress_child': {
        'Complete': None,
        'LastKey': 'Bytes',
        'ToStart': None,
    },
    'progress_top': {
        'Complete': None,
        'LastKey': 'Bytes',
        'ToStart': None,
    },
}
)
```

---------
### migrate_custom_child
See [`Pallet::migrate_custom_child`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| root | `Vec<u8>` | 
| child_keys | `Vec<Vec<u8>>` | 
| total_size | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'StateTrieMigration', 'migrate_custom_child', {
    'child_keys': ['Bytes'],
    'root': 'Bytes',
    'total_size': 'u32',
}
)
```

---------
### migrate_custom_top
See [`Pallet::migrate_custom_top`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| keys | `Vec<Vec<u8>>` | 
| witness_size | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'StateTrieMigration', 'migrate_custom_top', {'keys': ['Bytes'], 'witness_size': 'u32'}
)
```

---------
### set_signed_max_limits
See [`Pallet::set_signed_max_limits`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| limits | `MigrationLimits` | 

#### Python
```python
call = substrate.compose_call(
    'StateTrieMigration', 'set_signed_max_limits', {
    'limits': {
        'item': 'u32',
        'size': 'u32',
    },
}
)
```

---------
## Events

---------
### AutoMigrationFinished
The auto migration task finished.
#### Attributes
No attributes

---------
### Halted
Migration got halted due to an error or miss-configuration.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| error | `Error<T>` | ```('MaxSignedLimits', 'KeyTooLong', 'NotEnoughFunds', 'BadWitness', 'SignedMigrationNotAllowed', 'BadChildRoot')```

---------
### Migrated
Given number of `(top, child)` keys were migrated respectively, with the given
`compute`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| top | `u32` | ```u32```
| child | `u32` | ```u32```
| compute | `MigrationCompute` | ```('Signed', 'Auto')```

---------
### Slashed
Some account got slashed by the given amount.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### AutoLimits
 The limits that are imposed on automatic migrations.

 If set to None, then no automatic migration happens.

#### Python
```python
result = substrate.query(
    'StateTrieMigration', 'AutoLimits', []
)
```

#### Return value
```python
(None, {'item': 'u32', 'size': 'u32'})
```
---------
### MigrationProcess
 Migration progress.

 This stores the snapshot of the last migrated keys. It can be set into motion and move
 forward by any of the means provided by this pallet.

#### Python
```python
result = substrate.query(
    'StateTrieMigration', 'MigrationProcess', []
)
```

#### Return value
```python
{
    'child_items': 'u32',
    'progress_child': {'Complete': None, 'LastKey': 'Bytes', 'ToStart': None},
    'progress_top': {'Complete': None, 'LastKey': 'Bytes', 'ToStart': None},
    'size': 'u32',
    'top_items': 'u32',
}
```
---------
### SignedMigrationMaxLimits
 The maximum limits that the signed migration could use.

 If not set, no signed submission is allowed.

#### Python
```python
result = substrate.query(
    'StateTrieMigration', 'SignedMigrationMaxLimits', []
)
```

#### Return value
```python
{'item': 'u32', 'size': 'u32'}
```
---------
## Constants

---------
### MaxKeyLen
 Maximal number of bytes that a key can have.

 FRAME itself does not limit the key length.
 The concrete value must therefore depend on your storage usage.
 A [`frame_support::storage::StorageNMap`] for example can have an arbitrary number of
 keys which are then hashed and concatenated, resulting in arbitrarily long keys.

 Use the *state migration RPC* to retrieve the length of the longest key in your
 storage: &lt;https://github.com/paritytech/substrate/issues/11642&gt;

 The migration will halt with a `Halted` event if this value is too small.
 Since there is no real penalty from over-estimating, it is advised to use a large
 value. The default is 512 byte.

 Some key lengths for reference:
 - [`frame_support::storage::StorageValue`]: 32 byte
 - [`frame_support::storage::StorageMap`]: 64 byte
 - [`frame_support::storage::StorageDoubleMap`]: 96 byte

 For more info see
 &lt;https://www.shawntabrizi.com/substrate/querying-substrate-storage-via-rpc/&gt;
#### Value
```python
512
```
#### Python
```python
constant = substrate.get_constant('StateTrieMigration', 'MaxKeyLen')
```
---------
## Errors

---------
### BadChildRoot
Bad child root provided.

---------
### BadWitness
Bad witness data provided.

---------
### KeyTooLong
A key was longer than the configured maximum.

This means that the migration halted at the current [`Progress`] and
can be resumed with a larger [`crate::Config::MaxKeyLen`] value.
Retrying with the same [`crate::Config::MaxKeyLen`] value will not work.
The value should only be increased to avoid a storage migration for the currently
stored [`crate::Progress::LastKey`].

---------
### MaxSignedLimits
Max signed limits not respected.

---------
### NotEnoughFunds
submitter does not have enough funds.

---------
### SignedMigrationNotAllowed
Signed migration is not allowed because the maximum limit is not set yet.

---------