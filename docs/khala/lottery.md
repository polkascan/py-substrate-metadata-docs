
# Lottery

---------
## Calls

---------
### buy_ticket
See [`Pallet::buy_ticket`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Lottery', 'buy_ticket', {'call': 'Call'}
)
```

---------
### set_calls
See [`Pallet::set_calls`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Lottery', 'set_calls', {'calls': ['Call']}
)
```

---------
### start_lottery
See [`Pallet::start_lottery`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| price | `BalanceOf<T>` | 
| length | `BlockNumberFor<T>` | 
| delay | `BlockNumberFor<T>` | 
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
See [`Pallet::stop_repeat`].
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