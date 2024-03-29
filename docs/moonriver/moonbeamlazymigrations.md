
# MoonbeamLazyMigrations

---------
## Calls

---------
### clear_local_assets_storage
See [`Pallet::clear_local_assets_storage`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| limit | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'MoonbeamLazyMigrations', 'clear_local_assets_storage', {'limit': 'u32'}
)
```

---------
### clear_suicided_storage
See [`Pallet::clear_suicided_storage`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| addresses | `BoundedVec<H160, GetArrayLimit>` | 
| limit | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'MoonbeamLazyMigrations', 'clear_suicided_storage', {'addresses': ['[u8; 20]'], 'limit': 'u32'}
)
```

---------
### unlock_democracy_funds
See [`Pallet::unlock_democracy_funds`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| limit | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'MoonbeamLazyMigrations', 'unlock_democracy_funds', {'limit': 'u32'}
)
```

---------
## Storage functions

---------
### DemocracyLocksMigrationCompleted
 If true, it means that Democracy funds have been unlocked.

#### Python
```python
result = substrate.query(
    'MoonbeamLazyMigrations', 'DemocracyLocksMigrationCompleted', []
)
```

#### Return value
```python
'bool'
```
---------
### LocalAssetsMigrationCompleted
 If true, it means that LocalAssets storage has been removed.

#### Python
```python
result = substrate.query(
    'MoonbeamLazyMigrations', 'LocalAssetsMigrationCompleted', []
)
```

#### Return value
```python
'bool'
```
---------
### SuicidedContractsRemoved
 The total number of suicided contracts that were removed

#### Python
```python
result = substrate.query(
    'MoonbeamLazyMigrations', 'SuicidedContractsRemoved', []
)
```

#### Return value
```python
'u32'
```
---------
## Errors

---------
### AddressesLengthCannotBeZero
There must be at least one address

---------
### AllDemocracyFundsUnlocked
There are no more VotingOf entries to be removed and democracy funds to be unlocked

---------
### AllStorageEntriesHaveBeenRemoved
There are no more storage entries to be removed

---------
### ContractNotCorrupted
The contract is not corrupted (Still exist or properly suicided)

---------
### LimitCannotBeZero
The limit cannot be zero

---------
### UnlockLimitTooHigh
The limit for unlocking funds is too high

---------