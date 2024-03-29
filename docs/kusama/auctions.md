
# Auctions

---------
## Calls

---------
### bid
See [`Pallet::bid`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 
| auction_index | `AuctionIndex` | 
| first_slot | `LeasePeriodOf<T>` | 
| last_slot | `LeasePeriodOf<T>` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Auctions', 'bid', {
    'amount': 'u128',
    'auction_index': 'u32',
    'first_slot': 'u32',
    'last_slot': 'u32',
    'para': 'u32',
}
)
```

---------
### cancel_auction
See [`Pallet::cancel_auction`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Auctions', 'cancel_auction', {}
)
```

---------
### new_auction
See [`Pallet::new_auction`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| duration | `BlockNumberFor<T>` | 
| lease_period_index | `LeasePeriodOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Auctions', 'new_auction', {
    'duration': 'u32',
    'lease_period_index': 'u32',
}
)
```

---------
## Events

---------
### AuctionClosed
An auction ended. All funds become unreserved.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| auction_index | `AuctionIndex` | ```u32```

---------
### AuctionStarted
An auction started. Provides its index and the block number where it will begin to
close and the first lease period of the quadruplet that is auctioned.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| auction_index | `AuctionIndex` | ```u32```
| lease_period | `LeasePeriodOf<T>` | ```u32```
| ending | `BlockNumberFor<T>` | ```u32```

---------
### BidAccepted
A new bid has been accepted as the current winner.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| bidder | `T::AccountId` | ```AccountId```
| para_id | `ParaId` | ```u32```
| amount | `BalanceOf<T>` | ```u128```
| first_slot | `LeasePeriodOf<T>` | ```u32```
| last_slot | `LeasePeriodOf<T>` | ```u32```

---------
### ReserveConfiscated
Someone attempted to lease the same slot twice for a parachain. The amount is held in
reserve but no parachain slot has been leased.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_id | `ParaId` | ```u32```
| leaser | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### Reserved
Funds were reserved for a winning bid. First balance is the extra amount reserved.
Second is the total.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| bidder | `T::AccountId` | ```AccountId```
| extra_reserved | `BalanceOf<T>` | ```u128```
| total_amount | `BalanceOf<T>` | ```u128```

---------
### Unreserved
Funds were unreserved since bidder is no longer active. `[bidder, amount]`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| bidder | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### WinningOffset
The winning offset was chosen for an auction. This will map into the `Winning` storage
map.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| auction_index | `AuctionIndex` | ```u32```
| block_number | `BlockNumberFor<T>` | ```u32```

---------
## Storage functions

---------
### AuctionCounter
 Number of auctions started so far.

#### Python
```python
result = substrate.query(
    'Auctions', 'AuctionCounter', []
)
```

#### Return value
```python
'u32'
```
---------
### AuctionInfo
 Information relating to the current auction, if there is one.

 The first item in the tuple is the lease period index that the first of the four
 contiguous lease periods on auction is for. The second is the block number when the
 auction will &quot;begin to end&quot;, i.e. the first block of the Ending Period of the auction.

#### Python
```python
result = substrate.query(
    'Auctions', 'AuctionInfo', []
)
```

#### Return value
```python
('u32', 'u32')
```
---------
### ReservedAmounts
 Amounts currently reserved in the accounts of the bidders currently winning
 (sub-)ranges.

#### Python
```python
result = substrate.query(
    'Auctions', 'ReservedAmounts', [('AccountId', 'u32')]
)
```

#### Return value
```python
'u128'
```
---------
### Winning
 The winning bids for each of the 10 ranges at each sample in the final Ending Period of
 the current auction. The map&#x27;s key is the 0-based index into the Sample Size. The
 first sample of the ending period is 0; the last is `Sample Size - 1`.

#### Python
```python
result = substrate.query(
    'Auctions', 'Winning', ['u32']
)
```

#### Return value
```python
"[(None, ('AccountId', 'u32', 'u128')); 36]"
```
---------
## Constants

---------
### EndingPeriod
 The number of blocks over which an auction may be retroactively ended.
#### Value
```python
72000
```
#### Python
```python
constant = substrate.get_constant('Auctions', 'EndingPeriod')
```
---------
### LeasePeriodsPerSlot
#### Value
```python
8
```
#### Python
```python
constant = substrate.get_constant('Auctions', 'LeasePeriodsPerSlot')
```
---------
### SampleLength
 The length of each sample to take during the ending period.

 `EndingPeriod` / `SampleLength` = Total \# of Samples
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('Auctions', 'SampleLength')
```
---------
### SlotRangeCount
#### Value
```python
36
```
#### Python
```python
constant = substrate.get_constant('Auctions', 'SlotRangeCount')
```
---------
## Errors

---------
### AlreadyLeasedOut
The para is already leased out for part of this range.

---------
### AuctionEnded
Auction has already ended.

---------
### AuctionInProgress
This auction is already in progress.

---------
### LeasePeriodInPast
The lease period is in the past.

---------
### NotAuction
Not an auction.

---------
### NotCurrentAuction
Not a current auction.

---------
### ParaNotRegistered
Para is not registered

---------