
# Auction

---------
## Calls

---------
### bid
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::AuctionId` | 
| value | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Auction', 'bid', {'id': 'u32', 'value': 'u128'}
)
```

---------
## Events

---------
### Bid
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| auction_id | `T::AuctionId` | ```u32```
| bidder | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
## Storage functions

---------
### AuctionEndTime

#### Python
```python
result = substrate.query(
    'Auction', 'AuctionEndTime', ['u32', 'u32']
)
```

#### Return value
```python
()
```
---------
### Auctions

#### Python
```python
result = substrate.query(
    'Auction', 'Auctions', ['u32']
)
```

#### Return value
```python
{'bid': (None, ('AccountId', 'u128')), 'end': (None, 'u32'), 'start': 'u32'}
```
---------
### AuctionsIndex

#### Python
```python
result = substrate.query(
    'Auction', 'AuctionsIndex', []
)
```

#### Return value
```python
'u32'
```
---------
## Errors

---------
### AuctionNotExist

---------
### AuctionNotStarted

---------
### BidNotAccepted

---------
### InvalidBidPrice

---------
### NoAvailableAuctionId

---------