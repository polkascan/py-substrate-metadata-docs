
# Migrations

---------
## Events

---------
### FailedToResumeIdleXcmExecution
XCM execution resume failed with inner error
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}```

---------
### FailedToSuspendIdleXcmExecution
XCM execution suspension failed with inner error
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}```

---------
### MigrationCompleted
Migration completed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| migration_name | `Vec<u8>` | ```Bytes```
| consumed_weight | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### MigrationStarted
Migration started
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| migration_name | `Vec<u8>` | ```Bytes```

---------
### RuntimeUpgradeCompleted
Runtime upgrade completed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| weight | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### RuntimeUpgradeStarted
Runtime upgrade started
#### Attributes
No attributes

---------
## Storage functions

---------
### FullyUpgraded
 True if all required migrations have completed

#### Python
```python
result = substrate.query(
    'Migrations', 'FullyUpgraded', []
)
```

#### Return value
```python
'bool'
```
---------
### MigrationState
 MigrationState tracks the progress of a migration.
 Maps name (Vec&lt;u8&gt;) -&gt; whether or not migration has been completed (bool)

#### Python
```python
result = substrate.query(
    'Migrations', 'MigrationState', ['Bytes']
)
```

#### Return value
```python
'bool'
```
---------
### ShouldPauseXcm
 Temporary value that is set to true at the beginning of the block during which the execution
 of xcm messages must be paused.

#### Python
```python
result = substrate.query(
    'Migrations', 'ShouldPauseXcm', []
)
```

#### Return value
```python
'bool'
```
---------
## Errors

---------
### PreimageAlreadyExists
Preimage already exists in the new storage.

---------
### PreimageIsTooBig
Preimage is larger than the new max size.

---------
### PreimageMissing
Missing preimage in original democracy storage

---------
### WrongUpperBound
Provided upper bound is too low.

---------