
# AutomationPrice

---------
## Calls

---------
### add_asset
Initialize an asset

Add a new asset

\# Parameters
* `asset`: asset type
* `target_price`: baseline price of the asset
* `upper_bound`: TBD - highest executable percentage increase for asset
* `lower_bound`: TBD - highest executable percentage decrease for asset
* `asset_owner`: owner of the asset
* `expiration_period`: how frequently the tasks for an asset should expire

\# Errors
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetName` | 
| target_price | `AssetPrice` | 
| upper_bound | `u16` | 
| lower_bound | `u8` | 
| asset_owner | `AccountOf<T>` | 
| expiration_period | `UnixTime` | 

#### Python
```python
call = substrate.compose_call(
    'AutomationPrice', 'add_asset', {
    'asset': 'Bytes',
    'asset_owner': 'AccountId',
    'expiration_period': 'u64',
    'lower_bound': 'u8',
    'target_price': 'u128',
    'upper_bound': 'u16',
}
)
```

---------
### asset_price_update
Post asset update

Update the asset price

\# Parameters
* `asset`: asset type
* `value`: value of asset

\# Errors
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetName` | 
| value | `AssetPrice` | 

#### Python
```python
call = substrate.compose_call(
    'AutomationPrice', 'asset_price_update', {'asset': 'Bytes', 'value': 'u128'}
)
```

---------
### delete_asset
Delete an asset

\# Parameters
* `asset`: asset type
* `directions`: number of directions of data input. (up, down, ?)

\# Errors
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetName` | 

#### Python
```python
call = substrate.compose_call(
    'AutomationPrice', 'delete_asset', {'asset': 'Bytes'}
)
```

---------
### schedule_transfer_task
Schedule a task to fire an event with a custom message.

Schedule a transfer task for price triggers

\# Parameters
* `provided_id`: An id provided by the user. This id must be unique for the user.
* `asset`: asset type
* `direction`: direction of trigger movement
* `trigger_percentage`: what percentage task should be triggered at
* `recipient`: person to transfer money to
* `amount`: amount to transfer

\# Errors
#### Attributes
| Name | Type |
| -------- | -------- | 
| provided_id | `Vec<u8>` | 
| asset | `AssetName` | 
| direction | `AssetDirection` | 
| trigger_percentage | `AssetPercentage` | 
| recipient | `T::AccountId` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AutomationPrice', 'schedule_transfer_task', {
    'amount': 'u128',
    'asset': 'Bytes',
    'direction': ('Up', 'Down'),
    'provided_id': 'Bytes',
    'recipient': 'AccountId',
    'trigger_percentage': 'u128',
}
)
```

---------
## Events

---------
### AssetCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset | `AssetName` | ```Bytes```

---------
### AssetDeleted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset | `AssetName` | ```Bytes```

---------
### AssetPeriodReset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset | `AssetName` | ```Bytes```

---------
### AssetUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset | `AssetName` | ```Bytes```

---------
### Notify
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message | `Vec<u8>` | ```Bytes```

---------
### SuccessfullyTransferredFunds
Successfully transferred funds
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task_id | `T::Hash` | ```[u8; 32]```

---------
### TaskNotFound
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task_id | `T::Hash` | ```[u8; 32]```

---------
### TaskScheduled
Schedule task success.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountOf<T>` | ```AccountId```
| task_id | `T::Hash` | ```[u8; 32]```

---------
### TransferFailed
Transfer Failed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task_id | `T::Hash` | ```[u8; 32]```
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
## Storage functions

---------
### AssetBaselinePrices

#### Python
```python
result = substrate.query(
    'AutomationPrice', 'AssetBaselinePrices', ['Bytes']
)
```

#### Return value
```python
'u128'
```
---------
### AssetMetadata

#### Python
```python
result = substrate.query(
    'AutomationPrice', 'AssetMetadata', ['Bytes']
)
```

#### Return value
```python
{
    'asset_sudo': 'AccountId',
    'expiration_period': 'u64',
    'lower_bound': 'u8',
    'upper_bound': 'u16',
}
```
---------
### AssetPrices

#### Python
```python
result = substrate.query(
    'AutomationPrice', 'AssetPrices', ['Bytes']
)
```

#### Return value
```python
'u128'
```
---------
### NumberOfAssets

#### Python
```python
result = substrate.query(
    'AutomationPrice', 'NumberOfAssets', []
)
```

#### Return value
```python
'u8'
```
---------
### ScheduledAssetDeletion

#### Python
```python
result = substrate.query(
    'AutomationPrice', 'ScheduledAssetDeletion', ['u64']
)
```

#### Return value
```python
['Bytes']
```
---------
### ScheduledTasks

#### Python
```python
result = substrate.query(
    'AutomationPrice', 'ScheduledTasks', ['Bytes', ('Up', 'Down'), 'u128']
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### Shutdown

#### Python
```python
result = substrate.query(
    'AutomationPrice', 'Shutdown', []
)
```

#### Return value
```python
'bool'
```
---------
### TaskQueue

#### Python
```python
result = substrate.query(
    'AutomationPrice', 'TaskQueue', []
)
```

#### Return value
```python
[('Bytes', '[u8; 32]')]
```
---------
### Tasks

#### Python
```python
result = substrate.query(
    'AutomationPrice', 'Tasks', ['Bytes', '[u8; 32]']
)
```

#### Return value
```python
{
    'action': {
        'NativeTransfer': {
            'amount': 'u128',
            'recipient': 'AccountId',
            'sender': 'AccountId',
        },
    },
    'asset': 'Bytes',
    'direction': ('Up', 'Down'),
    'owner_id': 'AccountId',
    'provided_id': 'Bytes',
    'trigger_percentage': 'u128',
}
```
---------
## Constants

---------
### ExecutionWeightFee
#### Value
```python
12
```
#### Python
```python
constant = substrate.get_constant('AutomationPrice', 'ExecutionWeightFee')
```
---------
### MaxBlockWeight
 The maximum weight per block.
#### Value
```python
500000000000
```
#### Python
```python
constant = substrate.get_constant('AutomationPrice', 'MaxBlockWeight')
```
---------
### MaxTasksPerSlot
 The maximum number of tasks that can be scheduled for a time slot.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('AutomationPrice', 'MaxTasksPerSlot')
```
---------
### MaxWeightPercentage
 The maximum percentage of weight per block used for scheduled tasks.
#### Value
```python
50000000
```
#### Python
```python
constant = substrate.get_constant('AutomationPrice', 'MaxWeightPercentage')
```
---------
## Errors

---------
### AssetAlreadySupported
Asset already supported

---------
### AssetLimitReached
Too Many Assets Created

---------
### AssetNotInTriggerableRange
Asset must be in triggerable range.

---------
### AssetNotSupported
Non existent asset

---------
### BlockTimeNotSet
Block Time not set

---------
### DirectionNotSupported
Direction Not Supported

---------
### DuplicateTask
Duplicate task

---------
### EmptyProvidedId
The provided_id cannot be empty

---------
### InsufficientBalance
Insufficient Balance

---------
### InvalidAssetExpirationWindow
Invalid Expiration Window for new asset

---------
### InvalidAssetSudo
Asset cannot be updated by this account

---------
### InvalidTime
Time must end in a whole hour.

---------
### LiquidityRestrictions
Restrictions on Liquidity in Account

---------
### MaxTasksReached
Maximum tasks reached for the slot

---------
### TaskInsertionFailure
Failed to insert task

---------