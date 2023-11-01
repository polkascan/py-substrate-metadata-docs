
# DCA

---------
## Calls

---------
### schedule
Creates a new DCA (Dollar-Cost Averaging) schedule and plans the next execution
for the specified block.

If the block is not specified, the execution is planned for the next block.
If the given block is full, the execution will be planned in the subsequent block.

Once the schedule is created, the specified `total_amount` will be reserved for DCA.
The reservation currency will be the `amount_in` currency of the order.

Trades are executed as long as there is budget remaining
from the initial `total_amount` allocation.

If a trade fails due to slippage limit or price stability errors, it will be retried.
If the number of retries reaches the maximum allowed,
the schedule will be terminated permanently.
In the case of a successful trade, the retry counter is reset.

Parameters:
- `origin`: schedule owner
- `schedule`: schedule details
- `start_execution_block`: start execution block for the schedule

Emits `Scheduled` and `ExecutionPlanned` event when successful.

#### Attributes
| Name | Type |
| -------- | -------- | 
| schedule | `Schedule<T::AccountId, T::AssetId, BlockNumberFor<T>>` | 
| start_execution_block | `Option<BlockNumberFor<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'DCA', 'schedule', {
    'schedule': {
        'max_retries': (None, 'u8'),
        'order': {
            'Buy': {
                'amount_out': 'u128',
                'asset_in': 'u32',
                'asset_out': 'u32',
                'max_amount_in': 'u128',
                'route': [
                    {
                        'asset_in': 'u32',
                        'asset_out': 'u32',
                        'pool': {
                            'LBP': None,
                            'Omnipool': None,
                            'Stableswap': 'u32',
                            'XYK': None,
                        },
                    },
                ],
            },
            'Sell': {
                'amount_in': 'u128',
                'asset_in': 'u32',
                'asset_out': 'u32',
                'min_amount_out': 'u128',
                'route': [
                    {
                        'asset_in': 'u32',
                        'asset_out': 'u32',
                        'pool': {
                            'LBP': None,
                            'Omnipool': None,
                            'Stableswap': 'u32',
                            'XYK': None,
                        },
                    },
                ],
            },
        },
        'owner': 'AccountId',
        'period': 'u32',
        'slippage': (None, 'u32'),
        'stability_threshold': (
            None,
            'u32',
        ),
        'total_amount': 'u128',
    },
    'start_execution_block': (
        None,
        'u32',
    ),
}
)
```

---------
### terminate
Terminates a DCA schedule and remove it completely from the chain.

This can be called by both schedule owner or the configured `T::TechnicalOrigin`

Parameters:
- `origin`: schedule owner
- `schedule_id`: schedule id
- `next_execution_block`: block number where the schedule is planned.

Emits `Terminated` event when successful.

#### Attributes
| Name | Type |
| -------- | -------- | 
| schedule_id | `ScheduleId` | 
| next_execution_block | `Option<BlockNumberFor<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'DCA', 'terminate', {
    'next_execution_block': (
        None,
        'u32',
    ),
    'schedule_id': 'u32',
}
)
```

---------
## Events

---------
### Completed
The DCA is completed and completely removed from the chain
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `ScheduleId` | ```u32```
| who | `T::AccountId` | ```AccountId```

---------
### ExecutionPlanned
The DCA is planned for blocknumber
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `ScheduleId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| block | `BlockNumberFor<T>` | ```u32```

---------
### ExecutionStarted
The DCA execution is started
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `ScheduleId` | ```u32```
| block | `BlockNumberFor<T>` | ```u32```

---------
### RandomnessGenerationFailed
Randomness generation failed possibly coming from missing data about relay chain
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| block | `BlockNumberFor<T>` | ```u32```
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
### Scheduled
The DCA is scheduled for next execution
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `ScheduleId` | ```u32```
| who | `T::AccountId` | ```AccountId```

---------
### Terminated
The DCA is terminated and completely removed from the chain
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `ScheduleId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
### TradeExecuted
The DCA trade is successfully executed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `ScheduleId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount_in | `Balance` | ```u128```
| amount_out | `Balance` | ```u128```

---------
### TradeFailed
The DCA trade execution is failed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `ScheduleId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
## Storage functions

---------
### RemainingAmounts
 Keep tracking the remaining amounts to spend for DCA schedules

#### Python
```python
result = substrate.query(
    'DCA', 'RemainingAmounts', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### RetriesOnError
 Keep tracking the retry on error flag for DCA schedules

#### Python
```python
result = substrate.query(
    'DCA', 'RetriesOnError', ['u32']
)
```

#### Return value
```python
'u8'
```
---------
### ScheduleIdSequencer
 Id sequencer for schedules

#### Python
```python
result = substrate.query(
    'DCA', 'ScheduleIdSequencer', []
)
```

#### Return value
```python
'u32'
```
---------
### ScheduleIdsPerBlock
 Keep tracking of the schedule ids to be executed in the block

#### Python
```python
result = substrate.query(
    'DCA', 'ScheduleIdsPerBlock', ['u32']
)
```

#### Return value
```python
['u32']
```
---------
### ScheduleOwnership
 Storing schedule ownership

#### Python
```python
result = substrate.query(
    'DCA', 'ScheduleOwnership', ['AccountId', 'u32']
)
```

#### Return value
```python
()
```
---------
### Schedules
 Storing schedule details

#### Python
```python
result = substrate.query(
    'DCA', 'Schedules', ['u32']
)
```

#### Return value
```python
{
    'max_retries': (None, 'u8'),
    'order': {
        'Buy': {
            'amount_out': 'u128',
            'asset_in': 'u32',
            'asset_out': 'u32',
            'max_amount_in': 'u128',
            'route': [
                {
                    'asset_in': 'u32',
                    'asset_out': 'u32',
                    'pool': 'scale_info::290',
                },
            ],
        },
        'Sell': {
            'amount_in': 'u128',
            'asset_in': 'u32',
            'asset_out': 'u32',
            'min_amount_out': 'u128',
            'route': [
                {
                    'asset_in': 'u32',
                    'asset_out': 'u32',
                    'pool': 'scale_info::290',
                },
            ],
        },
    },
    'owner': 'AccountId',
    'period': 'u32',
    'slippage': (None, 'u32'),
    'stability_threshold': (None, 'u32'),
    'total_amount': 'u128',
}
```
---------
## Constants

---------
### FeeReceiver
The fee receiver for transaction fees
#### Value
```python
'7L53bUTBopuwFt3mKUfmkzgGLayYa1Yvn1hAg9v5UMrQzTfh'
```
#### Python
```python
constant = substrate.get_constant('DCA', 'FeeReceiver')
```
---------
### MaxNumberOfRetriesOnError
The number of max retries in case of trade limit error
#### Value
```python
3
```
#### Python
```python
constant = substrate.get_constant('DCA', 'MaxNumberOfRetriesOnError')
```
---------
### MaxPriceDifferenceBetweenBlocks
Max price difference allowed between blocks
#### Value
```python
15000
```
#### Python
```python
constant = substrate.get_constant('DCA', 'MaxPriceDifferenceBetweenBlocks')
```
---------
### MaxSchedulePerBlock
The number of max schedules to be executed per block
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('DCA', 'MaxSchedulePerBlock')
```
---------
### MinBudgetInNativeCurrency
Minimum budget to be able to schedule a DCA, specified in native currency
#### Value
```python
1000000000000000
```
#### Python
```python
constant = substrate.get_constant('DCA', 'MinBudgetInNativeCurrency')
```
---------
### MinimumTradingLimit
 Minimum trading limit for a single trade
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('DCA', 'MinimumTradingLimit')
```
---------
### NamedReserveId
 Named reserve identifier to store named reserves for orders of each users
#### Value
```python
'0x6463616f72646572'
```
#### Python
```python
constant = substrate.get_constant('DCA', 'NamedReserveId')
```
---------
### NativeAssetId
 Native Asset Id
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('DCA', 'NativeAssetId')
```
---------
## Errors

---------
### BlockNumberIsNotInFuture
The next execution block number is not in the future

---------
### BudgetTooLow
The budget is too low for executing one DCA

---------
### CalculatingPriceError
Error occurred when calculating price

---------
### Forbidden
Forbidden as the user is not the owner of the schedule

---------
### InvalidState
Error that should not really happen only in case of invalid state of the schedule storage entries

---------
### ManuallyTerminated
The DCA schedule has been manually terminated

---------
### MaxRetryReached
Max number of retries reached for schedule

---------
### MinTradeAmountNotReached
The min trade amount is not reached

---------
### NoFreeBlockFound
There is no free block found to plan DCA execution

---------
### NoParentHashFound
No parent hash has been found from relay chain

---------
### PriceUnstable
Price is unstable as price change from oracle data is bigger than max allowed

---------
### RouteNotSpecified
The route to execute the trade on is not specified

---------
### ScheduleNotFound
Schedule not exist

---------
### SlippageLimitReached
Slippage limit calculated from oracle is reached, leading to retry

---------
### TotalAmountIsSmallerThanMinBudget
The total amount to be reserved is smaller than min budget

---------
### TradeLimitReached
Absolutely trade limit reached reached, leading to retry

---------