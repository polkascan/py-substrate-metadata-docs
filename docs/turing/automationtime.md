
# AutomationTime

---------
## Calls

---------
### cancel_task
Cancel a task.

Tasks can only can be cancelled by their owners.

\# Parameters
* `task_id`: The id of the task.

\# Errors
* `TaskDoesNotExist`: The task does not exist.
#### Attributes
| Name | Type |
| -------- | -------- | 
| task_id | `TaskId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AutomationTime', 'cancel_task', {'task_id': '[u8; 32]'}
)
```

---------
### force_cancel_task
Sudo can force cancel a task.

\# Parameters
* `owner_id`: The owner of the task.
* `task_id`: The id of the task.

\# Errors
* `TaskDoesNotExist`: The task does not exist.
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner_id | `AccountOf<T>` | 
| task_id | `TaskId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AutomationTime', 'force_cancel_task', {
    'owner_id': 'AccountId',
    'task_id': '[u8; 32]',
}
)
```

---------
### schedule_auto_compound_delegated_stake_task
Schedule a task to increase delegation to a specified up to a minimum balance
Task will reschedule itself to run on a given frequency until a failure occurs

\# Parameters
* `execution_time`: The unix timestamp when the task should run for the first time
* `frequency`: Number of seconds to wait inbetween task executions
* `collator_id`: Account ID of the target collator
* `account_minimum`: The minimum amount of funds that should be left in the wallet

\# Errors
* `InvalidTime`: Execution time and frequency must end in a whole hour.
* `PastTime`: Time must be in the future.
* `DuplicateTask`: There can be no duplicate tasks.
* `TimeSlotFull`: Time slot is full. No more tasks can be scheduled for this time.
* `TimeTooFarOut`: Execution time or frequency are past the max time horizon.
* `InsufficientBalance`: Not enough funds to pay execution fee.
#### Attributes
| Name | Type |
| -------- | -------- | 
| execution_time | `UnixTime` | 
| frequency | `Seconds` | 
| collator_id | `AccountOf<T>` | 
| account_minimum | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AutomationTime', 'schedule_auto_compound_delegated_stake_task', {
    'account_minimum': 'u128',
    'collator_id': 'AccountId',
    'execution_time': 'u64',
    'frequency': 'u64',
}
)
```

---------
### schedule_dynamic_dispatch_task
Schedule a task that will dispatch a call.
** This is currently limited to calls from the System and Balances pallets.

\# Parameters
* `provided_id`: An id provided by the user. This id must be unique for the user.
* `execution_times`: The list of unix standard times in seconds for when the task should run.
* `call`: The call that will be dispatched.

\# Errors
* `InvalidTime`: Execution time and frequency must end in a whole hour.
* `PastTime`: Time must be in the future.
* `DuplicateTask`: There can be no duplicate tasks.
* `TimeSlotFull`: Time slot is full. No more tasks can be scheduled for this time.
* `TimeTooFarOut`: Execution time or frequency are past the max time horizon.
#### Attributes
| Name | Type |
| -------- | -------- | 
| provided_id | `Vec<u8>` | 
| schedule | `ScheduleParam` | 
| call | `Box<<T as Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'AutomationTime', 'schedule_dynamic_dispatch_task', {
    'call': 'Call',
    'provided_id': 'Bytes',
    'schedule': {
        'Fixed': {
            'execution_times': ['u64'],
        },
        'Recurring': {
            'frequency': 'u64',
            'next_execution_time': 'u64',
        },
    },
}
)
```

---------
### schedule_native_transfer_task
Schedule a task to transfer native token balance from sender to recipient.

Before the task can be scheduled the task must past validation checks.
* The transaction is signed
* The provided_id&\#x27;s length &gt; 0
* The times are valid
* Larger transfer amount than the acceptable minimum
* Transfer to account other than to self

\# Parameters
* `provided_id`: An id provided by the user. This id must be unique for the user.
* `execution_times`: The list of unix standard times in seconds for when the task should run.
* `recipient_id`: Account ID of the recipient.
* `amount`: Amount of balance to transfer.

\# Errors
* `InvalidTime`: Time must end in a whole hour.
* `PastTime`: Time must be in the future.
* `DuplicateTask`: There can be no duplicate tasks.
* `TimeTooFarOut`: Execution time or frequency are past the max time horizon.
* `TimeSlotFull`: Time slot is full. No more tasks can be scheduled for this time.
* `InvalidAmount`: Amount has to be larger than 0.1 OAK.
* `TransferToSelf`: Sender cannot transfer money to self.
#### Attributes
| Name | Type |
| -------- | -------- | 
| provided_id | `Vec<u8>` | 
| execution_times | `Vec<UnixTime>` | 
| recipient_id | `AccountOf<T>` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AutomationTime', 'schedule_native_transfer_task', {
    'amount': 'u128',
    'execution_times': ['u64'],
    'provided_id': 'Bytes',
    'recipient_id': 'AccountId',
}
)
```

---------
### schedule_notify_task
Schedule a task to fire an event with a custom message.

Before the task can be scheduled the task must past validation checks.
* The transaction is signed
* The provided_id&\#x27;s length &gt; 0
* The message&\#x27;s length &gt; 0
* The times are valid

\# Parameters
* `provided_id`: An id provided by the user. This id must be unique for the user.
* `execution_times`: The list of unix standard times in seconds for when the task should run.
* `message`: The message you want the event to have.

\# Errors
* `InvalidTime`: Time must end in a whole hour.
* `PastTime`: Time must be in the future.
* `EmptyMessage`: The message cannot be empty.
* `DuplicateTask`: There can be no duplicate tasks.
* `TimeTooFarOut`: Execution time or frequency are past the max time horizon.
* `TimeSlotFull`: Time slot is full. No more tasks can be scheduled for this time.
#### Attributes
| Name | Type |
| -------- | -------- | 
| provided_id | `Vec<u8>` | 
| execution_times | `Vec<UnixTime>` | 
| message | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'AutomationTime', 'schedule_notify_task', {
    'execution_times': ['u64'],
    'message': 'Bytes',
    'provided_id': 'Bytes',
}
)
```

---------
### schedule_xcmp_task
Schedule a task through XCMP to fire an XCMP message with a provided call.

Before the task can be scheduled the task must past validation checks.
* The transaction is signed
* The provided_id&\#x27;s length &gt; 0
* The times are valid
* The chain/currency pair is supported

\# Parameters
* `provided_id`: An id provided by the user. This id must be unique for the user.
* `execution_times`: The list of unix standard times in seconds for when the task should run.
* `para_id`: Parachain id the XCMP call will be sent to.
* `currency_id`: The currency in which fees will be paid.
* `encoded_call`: Call that will be sent via XCMP to the parachain id provided.
* `encoded_call_weight`: Required weight at most the provided call will take.

\# Errors
* `InvalidTime`: Time must end in a whole hour.
* `PastTime`: Time must be in the future.
* `DuplicateTask`: There can be no duplicate tasks.
* `TimeTooFarOut`: Execution time or frequency are past the max time horizon.
* `TimeSlotFull`: Time slot is full. No more tasks can be scheduled for this time.
#### Attributes
| Name | Type |
| -------- | -------- | 
| provided_id | `Vec<u8>` | 
| schedule | `ScheduleParam` | 
| para_id | `ParaId` | 
| currency_id | `T::CurrencyId` | 
| encoded_call | `Vec<u8>` | 
| encoded_call_weight | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AutomationTime', 'schedule_xcmp_task', {
    'currency_id': 'u32',
    'encoded_call': 'Bytes',
    'encoded_call_weight': 'u64',
    'para_id': 'u32',
    'provided_id': 'Bytes',
    'schedule': {
        'Fixed': {
            'execution_times': ['u64'],
        },
        'Recurring': {
            'frequency': 'u64',
            'next_execution_time': 'u64',
        },
    },
}
)
```

---------
## Events

---------
### AutoCompoundDelegatorStakeFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task_id | `TaskId<T>` | ```[u8; 32]```
| error_message | `Vec<u8>` | ```Bytes```
| error | `DispatchErrorWithPostInfo` | ```{'post_info': {'actual_weight': (None, {'ref_time': 'u64'}), 'pays_fee': ('Yes', 'No')}, 'error': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### CallCannotBeDecoded
The call for the DynamicDispatch action can no longer be decoded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountOf<T>` | ```AccountId```
| task_id | `TaskId<T>` | ```[u8; 32]```

---------
### DynamicDispatchResult
The result of the DynamicDispatch action.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountOf<T>` | ```AccountId```
| task_id | `TaskId<T>` | ```[u8; 32]```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### Notify
Notify event for the task.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| message | `Vec<u8>` | ```Bytes```

---------
### SuccesfullyAutoCompoundedDelegatorStake
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task_id | `TaskId<T>` | ```[u8; 32]```
| amount | `BalanceOf<T>` | ```u128```

---------
### SuccessfullyTransferredFunds
Successfully transferred funds
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task_id | `TaskId<T>` | ```[u8; 32]```

---------
### TaskCancelled
Cancelled a task.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountOf<T>` | ```AccountId```
| task_id | `TaskId<T>` | ```[u8; 32]```

---------
### TaskFailedToReschedule
A recurring task attempted but failed to be rescheduled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountOf<T>` | ```AccountId```
| task_id | `TaskId<T>` | ```[u8; 32]```
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}```

---------
### TaskMissed
The task could not be run at the scheduled time.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountOf<T>` | ```AccountId```
| task_id | `TaskId<T>` | ```[u8; 32]```
| execution_time | `UnixTime` | ```u64```

---------
### TaskNotFound
A Task was not found.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountOf<T>` | ```AccountId```
| task_id | `TaskId<T>` | ```[u8; 32]```

---------
### TaskNotRescheduled
A recurring task was not rescheduled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountOf<T>` | ```AccountId```
| task_id | `TaskId<T>` | ```[u8; 32]```
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}```

---------
### TaskRescheduled
A recurring task was rescheduled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountOf<T>` | ```AccountId```
| task_id | `TaskId<T>` | ```[u8; 32]```

---------
### TaskScheduled
Schedule task success.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountOf<T>` | ```AccountId```
| task_id | `TaskId<T>` | ```[u8; 32]```

---------
### TransferFailed
Transfer Failed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task_id | `TaskId<T>` | ```[u8; 32]```
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}```

---------
### XcmpTaskFailed
Failed to send XCMP
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task_id | `T::Hash` | ```[u8; 32]```
| para_id | `ParaId` | ```u32```
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}```

---------
### XcmpTaskSucceeded
Successfully sent XCMP
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| task_id | `T::Hash` | ```[u8; 32]```
| para_id | `ParaId` | ```u32```

---------
## Storage functions

---------
### AccountTasks

#### Python
```python
result = substrate.query(
    'AutomationTime', 'AccountTasks', ['AccountId', '[u8; 32]']
)
```

#### Return value
```python
{
    'action': {
        'AutoCompoundDelegatedStake': {
            'account_minimum': 'u128',
            'collator': 'AccountId',
            'delegator': 'AccountId',
        },
        'DynamicDispatch': {'encoded_call': 'Bytes'},
        'NativeTransfer': {
            'amount': 'u128',
            'recipient': 'AccountId',
            'sender': 'AccountId',
        },
        'Notify': {'message': 'Bytes'},
        'XCMP': {
            'currency_id': 'u32',
            'encoded_call': 'Bytes',
            'encoded_call_weight': 'u64',
            'para_id': 'u32',
        },
    },
    'owner_id': 'AccountId',
    'provided_id': 'Bytes',
    'schedule': {
        'Fixed': {'execution_times': ['u64'], 'executions_left': 'u32'},
        'Recurring': {'frequency': 'u64', 'next_execution_time': 'u64'},
    },
}
```
---------
### LastTimeSlot

#### Python
```python
result = substrate.query(
    'AutomationTime', 'LastTimeSlot', []
)
```

#### Return value
```python
('u64', 'u64')
```
---------
### MissedQueueV2

#### Python
```python
result = substrate.query(
    'AutomationTime', 'MissedQueueV2', []
)
```

#### Return value
```python
[{'execution_time': 'u64', 'owner_id': 'AccountId', 'task_id': '[u8; 32]'}]
```
---------
### ScheduledTasksV3

#### Python
```python
result = substrate.query(
    'AutomationTime', 'ScheduledTasksV3', ['u64']
)
```

#### Return value
```python
{'tasks': [('AccountId', '[u8; 32]')], 'weight': 'u128'}
```
---------
### Shutdown

#### Python
```python
result = substrate.query(
    'AutomationTime', 'Shutdown', []
)
```

#### Return value
```python
'bool'
```
---------
### TaskQueueV2

#### Python
```python
result = substrate.query(
    'AutomationTime', 'TaskQueueV2', []
)
```

#### Return value
```python
[('AccountId', '[u8; 32]')]
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
constant = substrate.get_constant('AutomationTime', 'ExecutionWeightFee')
```
---------
### GetNativeCurrencyId
 The currencyId for the native currency.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('AutomationTime', 'GetNativeCurrencyId')
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
constant = substrate.get_constant('AutomationTime', 'MaxBlockWeight')
```
---------
### MaxExecutionTimes
 The maximum number of times that a task can be scheduled for.
#### Value
```python
24
```
#### Python
```python
constant = substrate.get_constant('AutomationTime', 'MaxExecutionTimes')
```
---------
### MaxScheduleSeconds
 The farthest out a task can be scheduled.
#### Value
```python
15552000
```
#### Python
```python
constant = substrate.get_constant('AutomationTime', 'MaxScheduleSeconds')
```
---------
### MaxTasksPerSlot
 The maximum number of tasks that can be scheduled for a time slot.
#### Value
```python
256
```
#### Python
```python
constant = substrate.get_constant('AutomationTime', 'MaxTasksPerSlot')
```
---------
### MaxWeightPerSlot
 The maximum supported execution weight per automation slot
#### Value
```python
150000000000
```
#### Python
```python
constant = substrate.get_constant('AutomationTime', 'MaxWeightPerSlot')
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
constant = substrate.get_constant('AutomationTime', 'MaxWeightPercentage')
```
---------
### UpdateQueueRatio
 The maximum percentage of weight per block used for scheduled tasks.
#### Value
```python
500000000
```
#### Python
```python
constant = substrate.get_constant('AutomationTime', 'UpdateQueueRatio')
```
---------
## Errors

---------
### BlockTimeNotSet
Block time not set.

---------
### CallCannotBeDecoded
The call can no longer be decoded.

---------
### DuplicateTask
There can be no duplicate tasks.

---------
### EmptyMessage
The message cannot be empty.

---------
### EmptyProvidedId
The provided_id cannot be empty

---------
### InsufficientBalance
Insufficient balance to pay execution fee.

---------
### InvalidAmount
Amount has to be larger than 0.1 OAK.

---------
### InvalidTime
Time must end in a whole hour.

---------
### LiquidityRestrictions
Account liquidity restrictions prevent withdrawal.

---------
### PastTime
Time must be in the future.

---------
### TaskDoesNotExist
The task does not exist.

---------
### TimeSlotFull
Time slot is full. No more tasks can be scheduled for this time.

---------
### TimeTooFarOut
Time cannot be too far in the future.

---------
### TooManyExecutionsTimes
Too many execution times provided.

---------
### TransferToSelf
Sender cannot transfer money to self.

---------