
# Migration

---------
## Calls

---------
### finalize
Update the migration status to `Complete`
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Migration', 'finalize', {}
)
```

---------
### migrate_balances_issuance
Migrates a the `TotalIssuance`.

The provide balance here, will be ADDED to the existing
`TotalIssuance` of the system. Calley better be sure, that the total
issuance matches the actual total issuance in the system,
which means, that the `AccountInfo` from the frame_system is
migrated afterwards.
#### Attributes
| Name | Type |
| -------- | -------- | 
| additional_issuance | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Migration', 'migrate_balances_issuance', {'additional_issuance': 'u128'}
)
```

---------
### migrate_proxy_proxies
Migrates to `Proxies` storage from another chain.

As the `Proxies` storage changed between v2 and v3, a transformation
for the v2 data is done off-chain. The input defines an array of of
tuples, where each tuple defines, the proxied account, the reserve
that must be done on this account and the proxies for this account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| proxies | `Vec<
(T::AccountId,<<T as pallet_proxy::Config>::Currency as
frame_support::traits::Currency<<T as frame_system::Config>::
AccountId,>>::Balance,
(BoundedVec<ProxyDefinition<T::AccountId, T::ProxyType, T::
BlockNumber>,<T as pallet_proxy::Config>::MaxProxies,>,<<T as
pallet_proxy::Config>::Currency as frame_support::traits::Currency<
<T as frame_system::Config>::AccountId,>>::Balance,),)>` | 

#### Python
```python
call = substrate.compose_call(
    'Migration', 'migrate_proxy_proxies', {
    'proxies': [
        (
            'AccountId',
            'u128',
            (
                [
                    {
                        'delay': 'u32',
                        'delegate': 'AccountId',
                        'proxy_type': (
                            'Any',
                            'NonTransfer',
                            'Governance',
                            '_Staking',
                            'NonProxy',
                        ),
                    },
                ],
                'u128',
            ),
        ),
    ],
}
)
```

---------
### migrate_system_account
Migrating the Account informations from frame_system.

This call takes the raw scale encoded key (= patricia-key for each
account in the `Account` storage and inserts the provided scale
encoded value (= `AccountInfo`) into the underlying DB.

Note: As we are converting from substrate-v2 to substrate-v3 we must
do type-conversions. Those conversions are done off-chain.
#### Attributes
| Name | Type |
| -------- | -------- | 
| accounts | `Vec<(Vec<u8>, Vec<u8>)>` | 

#### Python
```python
call = substrate.compose_call(
    'Migration', 'migrate_system_account', {'accounts': [('Bytes', 'Bytes')]}
)
```

---------
### migrate_vesting_vesting
Migrates vesting information to this system.

The `VestingInfo` is adapted off-chain, so that it represents the
correct vesting information on this chain.
#### Attributes
| Name | Type |
| -------- | -------- | 
| vestings | `Vec<(T::AccountId, VestingInfo<BalanceOf<T>, T::BlockNumber>)>` | 

#### Python
```python
call = substrate.compose_call(
    'Migration', 'migrate_vesting_vesting', {
    'vestings': [
        (
            'AccountId',
            {
                'locked': 'u128',
                'per_block': 'u128',
                'starting_block': 'u32',
            },
        ),
    ],
}
)
```

---------
## Events

---------
### FailedToMigrateProxyDataFor
Indicates if a migration of proxy data failed, this should NEVER
happen, and can only happen due to insufficient balances during
reserve
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### FailedToMigrateVestingFor
This is an error that must be dispatched as an Event, as we do not
want to fail the whole batch when one account fails. Should also not
happen, as we take them from mainnet. But...
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### MigratedProxyDataFor
Indicates that proxy data has been migrated succesfully for
[`ProxiedAccount`, `DepositOnProxiesAccount`, `NumberOfProxies`]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `<<T as pallet_proxy::Config>::Currency as frame_support::traits::
Currency<<T as frame_system::Config>::AccountId,>>::Balance` | ```u128```
| None | `u64` | ```u64```

---------
### MigratedProxyProxies
Number of proxies that have been migrated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### MigratedSystemAccounts
Number of accounts that have been migrated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### MigratedTotalIssuance
The new and the old issuance after the migration of issuance.
[`OldIssuance`, `NewIssuance`]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```

---------
### MigratedVestingAccounts
Number of vesting that have been migrated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### MigratedVestingFor
Defines the vesting we migrated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `<<T as pallet_vesting::Config>::Currency as frame_support::traits::
Currency<<T as frame_system::Config>::AccountId,>>::Balance` | ```u128```
| None | `<<T as pallet_vesting::Config>::Currency as frame_support::traits::
Currency<<T as frame_system::Config>::AccountId,>>::Balance` | ```u128```
| None | `T::BlockNumber` | ```u32```

---------
### MigrationFinished
Indicates that the migration is finished
#### Attributes
No attributes

---------
## Storage functions

---------
### Status

#### Python
```python
result = substrate.query(
    'Migration', 'Status', []
)
```

#### Return value
```python
('Inactive', 'Ongoing', 'Complete')
```
---------
## Constants

---------
### MigrationMaxAccounts
 Maximum number of accounts that can be migrated at once
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Migration', 'MigrationMaxAccounts')
```
---------
### MigrationMaxProxies
 Maximum number of vestings that can be migrated at once
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Migration', 'MigrationMaxProxies')
```
---------
### MigrationMaxVestings
 Maximum number of vestings that can be migrated at once
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Migration', 'MigrationMaxVestings')
```
---------
## Errors

---------
### MigrationAlreadyCompleted
Indicates that a migration call happened, although the migration is
already closed

---------
### OnlyFinalizeOngoing
Indicates that a finalize call happened, although the migration
pallet is not in an ongoing migration

---------
### TooManyAccounts
Too many accounts in the vector for the call of
`migrate_system_account`.

---------
### TooManyProxies
Too many proxies in the vector for the call of
`migrate_proxy_proxies`.

---------
### TooManyVestings
Too many vestingInfos in the vector for the call of
`migrate_veting_vesting`.

---------