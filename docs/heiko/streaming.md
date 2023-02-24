
# Streaming

---------
## Calls

---------
### cancel
Cancel a existed stream and return back the deposit to sender and recipient

Can only be called by the sender

- `stream_id`: the stream id which will be canceled
#### Attributes
| Name | Type |
| -------- | -------- | 
| stream_id | `StreamId` | 

#### Python
```python
call = substrate.compose_call(
    'Streaming', 'cancel', {'stream_id': 'u128'}
)
```

---------
### create
Create a new stream between sender and recipient

Transfer assets to another account in the form of stream
Any supported assets in parallel/heiko can be used to stream.
The sender&\#x27;s assets will be locked into palletId
Will transfer to recipient as the stream progresses

- `recipient`: the receiving address
- `deposit`: the amount sender will deposit to create the stream
- `asset_id`: asset should be able to lookup.
- `start_time`: the time when the stream will start
- `end_time`: the time when the stream will end
#### Attributes
| Name | Type |
| -------- | -------- | 
| recipient | `AccountOf<T>` | 
| deposit | `BalanceOf<T>` | 
| asset_id | `AssetIdOf<T>` | 
| start_time | `Timestamp` | 
| end_time | `Timestamp` | 
| cancellable | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Streaming', 'create', {
    'asset_id': 'u32',
    'cancellable': 'bool',
    'deposit': 'u128',
    'end_time': 'u64',
    'recipient': 'AccountId',
    'start_time': 'u64',
}
)
```

---------
### set_minimum_deposit
Set the minimum deposit for a stream

Can only be called by the UpdateOrigin

- `asset_id`: the stream id which will be set the minimum deposit
- `minimum_deposit`: the minimum deposit for a stream
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 
| minimum_deposit | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Streaming', 'set_minimum_deposit', {
    'asset_id': 'u32',
    'minimum_deposit': 'u128',
}
)
```

---------
### withdraw
Withdraw from a existed stream

Can be called by the sender or the recipient

- `stream_id`: the stream id which will be withdraw from
` `amount`: the amount of asset to withdraw
#### Attributes
| Name | Type |
| -------- | -------- | 
| stream_id | `StreamId` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Streaming', 'withdraw', {
    'amount': 'u128',
    'stream_id': 'u128',
}
)
```

---------
## Events

---------
### MinimumDepositSet
Set minimum deposit for creating a stream
\[asset_id, minimum_deposit\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetIdOf<T>` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### StreamCancelled
Cancel an existing stream.
\[stream_id, sender, recipient, asset_id, sender_balance, recipient_balance]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `StreamId` | ```u128```
| None | `AccountOf<T>` | ```AccountId```
| None | `AccountOf<T>` | ```AccountId```
| None | `AssetIdOf<T>` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### StreamCreated
Creates a payment stream.
\[stream_id, sender, recipient, deposit, asset_id, start_time, end_time, cancellable\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `StreamId` | ```u128```
| None | `AccountOf<T>` | ```AccountId```
| None | `AccountOf<T>` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `AssetIdOf<T>` | ```u32```
| None | `Timestamp` | ```u64```
| None | `Timestamp` | ```u64```
| None | `bool` | ```bool```

---------
### StreamWithdrawn
Withdraw payment from stream.
\[stream_id, recipient, asset_id, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `StreamId` | ```u128```
| None | `AccountOf<T>` | ```AccountId```
| None | `AssetIdOf<T>` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### MinimumDeposits
 Minimum deposit for each asset

#### Python
```python
result = substrate.query(
    'Streaming', 'MinimumDeposits', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### NextStreamId
 Next Stream Id

#### Python
```python
result = substrate.query(
    'Streaming', 'NextStreamId', []
)
```

#### Return value
```python
'u128'
```
---------
### StreamLibrary
 Streams holds by each account
 account_id =&gt; stream_kind =&gt; stream_id

#### Python
```python
result = substrate.query(
    'Streaming', 'StreamLibrary', [
    'AccountId',
    ('Send', 'Receive', 'Finish'),
]
)
```

#### Return value
```python
['u128']
```
---------
### Streams
 Global storage for streams

#### Python
```python
result = substrate.query(
    'Streaming', 'Streams', ['u128']
)
```

#### Return value
```python
{
    'asset_id': 'u32',
    'cancellable': 'bool',
    'deposit': 'u128',
    'end_time': 'u64',
    'rate_per_sec': 'u128',
    'recipient': 'AccountId',
    'remaining_balance': 'u128',
    'sender': 'AccountId',
    'start_time': 'u64',
    'status': {
        'Completed': {'cancelled': 'bool'},
        'Ongoing': {'as_collateral': 'bool'},
    },
}
```
---------
## Constants

---------
### MaxFinishedStreamsCount
 The max count of streams that has been cancelled or completed for an account
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Streaming', 'MaxFinishedStreamsCount')
```
---------
### MaxStreamsCount
 The max count of streams for an account
#### Value
```python
128
```
#### Python
```python
constant = substrate.get_constant('Streaming', 'MaxStreamsCount')
```
---------
### NativeCurrencyId
 Currency id of the native token
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Streaming', 'NativeCurrencyId')
```
---------
### NativeExistentialDeposit
 The essential balance for an existed account
#### Value
```python
10000000000
```
#### Python
```python
constant = substrate.get_constant('Streaming', 'NativeExistentialDeposit')
```
---------
### PalletId
 The streaming module id, keep all collaterals of CDPs.
#### Value
```python
'0x7061722f7374726d'
```
#### Python
```python
constant = substrate.get_constant('Streaming', 'PalletId')
```
---------
## Errors

---------
### CannotBeCancelled
Stream cannot be cancelled

---------
### DepositLowerThanMinimum
Insufficient deposit size

---------
### EndTimeBeforeStartTime
End time is before start time

---------
### ExcessMaxStreamsCount
Excess max streams count

---------
### HasFinished
Stream was cancelled or completed

---------
### InsufficientStreamBalance
Amount exceeds balance

---------
### InvalidAssetId
Asset is not supported to create stream

---------
### InvalidDuration
The duration calculated is too short or too long

---------
### InvalidRatePerSecond
The rate per second calculated is zero

---------
### InvalidStreamId
The stream id is not found

---------
### NotStarted
Stream not started

---------
### NotTheRecipient
Caller is not the stream recipient

---------
### NotTheSender
Caller is not the stream sender

---------
### RecipientIsAlsoSender
Sender as specified themselves as the recipient

---------
### StartTimeBeforeCurrentTime
Start time is before current block time

---------