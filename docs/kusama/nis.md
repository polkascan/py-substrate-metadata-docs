
# Nis

---------
## Calls

---------
### fund_deficit
Ensure we have sufficient funding for all potential payouts.

- `origin`: Must be accepted by `FundOrigin`.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Nis', 'fund_deficit', {}
)
```

---------
### place_bid
Place a bid.

Origin must be Signed, and account must have at least `amount` in free balance.

- `amount`: The amount of the bid; these funds will be reserved, and if/when
  consolidated, removed. Must be at least `MinBid`.
- `duration`: The number of periods before which the newly consolidated bid may be
  thawed. Must be greater than 1 and no more than `QueueCount`.

Complexities:
- `Queues[duration].len()` (just take max).
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 
| duration | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Nis', 'place_bid', {'amount': 'u128', 'duration': 'u32'}
)
```

---------
### retract_bid
Retract a previously placed bid.

Origin must be Signed, and the account should have previously issued a still-active bid
of `amount` for `duration`.

- `amount`: The amount of the previous bid.
- `duration`: The duration of the previous bid.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 
| duration | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Nis', 'retract_bid', {'amount': 'u128', 'duration': 'u32'}
)
```

---------
### thaw
Reduce or remove an outstanding receipt, placing the according proportion of funds into
the account of the owner.

- `origin`: Must be Signed and the account must be the owner of the receipt `index` as
  well as any fungible counterpart.
- `index`: The index of the receipt.
- `portion`: If `Some`, then only the given portion of the receipt should be thawed. If
  `None`, then all of it should be.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ReceiptIndex` | 
| portion | `Option<<T::Counterpart as FungibleInspect<T::AccountId>>::Balance
>` | 

#### Python
```python
call = substrate.compose_call(
    'Nis', 'thaw', {
    'index': 'u32',
    'portion': (None, 'u128'),
}
)
```

---------
## Events

---------
### BidDropped
A bid was dropped from a queue because of another, more substantial, bid was present.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```
| duration | `u32` | ```u32```

---------
### BidPlaced
A bid was successfully placed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```
| duration | `u32` | ```u32```

---------
### BidRetracted
A bid was successfully removed (before being accepted).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```
| duration | `u32` | ```u32```

---------
### Funded
An automatic funding of the deficit was made.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| deficit | `BalanceOf<T>` | ```u128```

---------
### Issued
A bid was accepted. The balance may not be released until expiry.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReceiptIndex` | ```u32```
| expiry | `T::BlockNumber` | ```u32```
| who | `T::AccountId` | ```AccountId```
| proportion | `Perquintill` | ```u64```
| amount | `BalanceOf<T>` | ```u128```

---------
### Thawed
An receipt has been (at least partially) thawed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReceiptIndex` | ```u32```
| who | `T::AccountId` | ```AccountId```
| proportion | `Perquintill` | ```u64```
| amount | `BalanceOf<T>` | ```u128```
| dropped | `bool` | ```bool```

---------
### Transferred
A receipt was transfered.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| index | `ReceiptIndex` | ```u32```

---------
## Storage functions

---------
### QueueTotals
 The totals of items and balances within each queue. Saves a lot of storage reads in the
 case of sparsely packed queues.

 The vector is indexed by duration in `Period`s, offset by one, so information on the queue
 whose duration is one `Period` would be storage `0`.

#### Python
```python
result = substrate.query(
    'Nis', 'QueueTotals', []
)
```

#### Return value
```python
[('u32', 'u128')]
```
---------
### Queues
 The queues of bids. Indexed by duration (in `Period`s).

#### Python
```python
result = substrate.query(
    'Nis', 'Queues', ['u32']
)
```

#### Return value
```python
[{'amount': 'u128', 'who': 'AccountId'}]
```
---------
### Receipts
 The currently outstanding receipts, indexed according to the order of creation.

#### Python
```python
result = substrate.query(
    'Nis', 'Receipts', ['u32']
)
```

#### Return value
```python
{'expiry': 'u32', 'proportion': 'u64', 'who': 'AccountId'}
```
---------
### Summary
 Summary information over the general state.

#### Python
```python
result = substrate.query(
    'Nis', 'Summary', []
)
```

#### Return value
```python
{
    'index': 'u32',
    'last_period': 'u32',
    'proportion_owed': 'u64',
    'thawed': 'u64',
}
```
---------
## Constants

---------
### BasePeriod
 The base period for the duration queues. This is the common multiple across all
 supported freezing durations that can be bid upon.
#### Value
```python
100800
```
#### Python
```python
constant = substrate.get_constant('Nis', 'BasePeriod')
```
---------
### FifoQueueLen
 Portion of the queue which is free from ordering and just a FIFO.

 Must be no greater than `MaxQueueLen`.
#### Value
```python
250
```
#### Python
```python
constant = substrate.get_constant('Nis', 'FifoQueueLen')
```
---------
### IntakePeriod
 The number of blocks between consecutive attempts to dequeue bids and create receipts.

 A larger value results in fewer storage hits each block, but a slower period to get to
 the target.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('Nis', 'IntakePeriod')
```
---------
### MaxIntakeWeight
 The maximum amount of bids that can consolidated into receipts in a single intake. A
 larger value here means less of the block available for transactions should there be a
 glut of bids.
#### Value
```python
{'proof_size': 1844674407370955161, 'ref_time': 200000000000}
```
#### Python
```python
constant = substrate.get_constant('Nis', 'MaxIntakeWeight')
```
---------
### MaxQueueLen
 Maximum number of items that may be in each duration queue.

 Must be larger than zero.
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('Nis', 'MaxQueueLen')
```
---------
### MinBid
 The minimum amount of funds that may be placed in a bid. Note that this
 does not actually limit the amount which may be represented in a receipt since bids may
 be split up by the system.

 It should be at least big enough to ensure that there is no possible storage spam attack
 or queue-filling attack.
#### Value
```python
3333333333300
```
#### Python
```python
constant = substrate.get_constant('Nis', 'MinBid')
```
---------
### MinReceipt
 The minimum amount of funds which may intentionally be left remaining under a single
 receipt.
#### Value
```python
100000000000
```
#### Python
```python
constant = substrate.get_constant('Nis', 'MinReceipt')
```
---------
### PalletId
 The treasury&#x27;s pallet id, used for deriving its sovereign account ID.
#### Value
```python
'0x70792f6e69732020'
```
#### Python
```python
constant = substrate.get_constant('Nis', 'PalletId')
```
---------
### QueueCount
 Number of duration queues in total. This sets the maximum duration supported, which is
 this value multiplied by `Period`.
#### Value
```python
500
```
#### Python
```python
constant = substrate.get_constant('Nis', 'QueueCount')
```
---------
### ThawThrottle
 The maximum proportion which may be thawed and the period over which it is reset.
#### Value
```python
(250000000000000000, 5)
```
#### Python
```python
constant = substrate.get_constant('Nis', 'ThawThrottle')
```
---------
## Errors

---------
### AmountTooSmall
The amount of the bid is less than the minimum allowed.

---------
### BidTooLow
The queue for the bid&\#x27;s duration is full and the amount bid is too low to get in
through replacing an existing bid.

---------
### DurationTooBig
The duration is the bid is greater than the number of queues.

---------
### DurationTooSmall
The duration of the bid is less than one.

---------
### Funded
There are enough funds for what is required.

---------
### MakesDust
The operation would result in a receipt worth an insignficant value.

---------
### NotExpired
Bond not yet at expiry date.

---------
### NotFound
The given bid for retraction is not found.

---------
### NotOwner
Not the owner of the receipt.

---------
### Throttled
The thaw throttle has been reached for this period.

---------
### TooMuch
The portion supplied is beyond the value of the receipt.

---------
### Unfunded
Not enough funds are held to pay out.

---------
### Unknown
Bond index is unknown.

---------