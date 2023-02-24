
# Lottery

---------
## Calls

---------
### buy_ticket
Buy a ticket to enter the lottery.

This extrinsic acts as a passthrough function for `call`. In all
situations where `call` alone would succeed, this extrinsic should
succeed.

If `call` is successful, then we will attempt to purchase a ticket,
which may fail silently. To detect success of a ticket purchase, you
should listen for the `TicketBought` event.

This extrinsic must be called by a signed origin.
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'Lottery', 'buy_ticket', {'call': 'Call'}
)
```

---------
### set_calls
Set calls in storage which can be used to purchase a lottery ticket.

This function only matters if you use the `ValidateCall` implementation
provided by this pallet, which uses storage to determine the valid calls.

This extrinsic must be called by the Manager origin.
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'Lottery', 'set_calls', {'calls': ['Call']}
)
```

---------
### start_lottery
Start a lottery using the provided configuration.

This extrinsic must be called by the `ManagerOrigin`.

Parameters:

* `price`: The cost of a single ticket.
* `length`: How long the lottery should run for starting at the current block.
* `delay`: How long after the lottery end we should wait before picking a winner.
* `repeat`: If the lottery should repeat when completed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| price | `BalanceOf<T>` | 
| length | `T::BlockNumber` | 
| delay | `T::BlockNumber` | 
| repeat | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Lottery', 'start_lottery', {
    'delay': 'u32',
    'length': 'u32',
    'price': 'u128',
    'repeat': 'bool',
}
)
```

---------
### stop_repeat
If a lottery is repeating, you can use this to stop the repeat.
The lottery will continue to run to completion.

This extrinsic must be called by the `ManagerOrigin`.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Lottery', 'stop_repeat', {}
)
```

---------
## Events

---------
### CallsUpdated
A new set of calls have been set!
#### Attributes
No attributes

---------
### LotteryStarted
A lottery has been started!
#### Attributes
No attributes

---------
### TicketBought
A ticket has been bought!
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| call_index | `CallIndex` | ```('u8', 'u8')```

---------
### Winner
A winner has been chosen!
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| winner | `T::AccountId` | ```AccountId```
| lottery_balance | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### CallIndices
 The calls stored in this pallet to be used in an active lottery if configured
 by `Config::ValidateCall`.

#### Python
```python
result = substrate.query(
    'Lottery', 'CallIndices', []
)
```

#### Return value
```python
[('u8', 'u8')]
```
---------
### Lottery
 The configuration for the current lottery.

#### Python
```python
result = substrate.query(
    'Lottery', 'Lottery', []
)
```

#### Return value
```python
{
    'delay': 'u32',
    'length': 'u32',
    'price': 'u128',
    'repeat': 'bool',
    'start': 'u32',
}
```
---------
### LotteryIndex

#### Python
```python
result = substrate.query(
    'Lottery', 'LotteryIndex', []
)
```

#### Return value
```python
'u32'
```
---------
### Participants
 Users who have purchased a ticket. (Lottery Index, Tickets Purchased)

#### Python
```python
result = substrate.query(
    'Lottery', 'Participants', ['AccountId']
)
```

#### Return value
```python
('u32', [('u8', 'u8')])
```
---------
### Tickets
 Each ticket&#x27;s owner.

 May have residual storage from previous lotteries. Use `TicketsCount` to see which ones
 are actually valid ticket mappings.

#### Python
```python
result = substrate.query(
    'Lottery', 'Tickets', ['u32']
)
```

#### Return value
```python
'AccountId'
```
---------
### TicketsCount
 Total number of tickets sold.

#### Python
```python
result = substrate.query(
    'Lottery', 'TicketsCount', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### MaxCalls
 The max number of calls available in a single lottery.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Lottery', 'MaxCalls')
```
---------
### MaxGenerateRandom
 Number of time we should try to generate a random number that has no modulo bias.
 The larger this number, the more potential computation is used for picking the winner,
 but also the more likely that the chosen winner is done fairly.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Lottery', 'MaxGenerateRandom')
```
---------
### PalletId
 The Lottery&#x27;s pallet id
#### Value
```python
'0x70792f6c6f74746f'
```
#### Python
```python
constant = substrate.get_constant('Lottery', 'PalletId')
```
---------
## Errors

---------
### AlreadyEnded
A lottery has already ended.

---------
### AlreadyParticipating
You are already participating in the lottery with this call.

---------
### EncodingFailed
Failed to encode calls

---------
### InProgress
A lottery is already in progress.

---------
### InvalidCall
The call is not valid for an open lottery.

---------
### NotConfigured
A lottery has not been configured.

---------
### TooManyCalls
Too many calls for a single lottery.

---------