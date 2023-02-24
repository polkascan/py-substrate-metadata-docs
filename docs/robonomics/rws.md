
# RWS

---------
## Calls

---------
### bid
Plasce a bid for live subscription auction.

\# &lt;weight&gt;
- reads auction &amp; auction_queue
- writes auction bid
- AuctionCurrency reserve &amp; unreserve
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `T::AuctionIndex` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'RWS', 'bid', {'amount': 'u128', 'index': 'u32'}
)
```

---------
### call
Authenticates the RWS staker and dispatches a free function call.

The dispatch origin for this call must be _Signed_.

\# &lt;weight&gt;
- Dependes of call method.
- Basically this sould be free by concept.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| subscription_id | `T::AccountId` | 
| call | `Box<<T as Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'RWS', 'call', {
    'call': 'Call',
    'subscription_id': 'AccountId',
}
)
```

---------
### set_devices
Set RWS subscription devices.

\# &lt;weight&gt;
- O(1).
- Limited storage reads.
- One DB change.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| devices | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'RWS', 'set_devices', {'devices': ['AccountId']}
)
```

---------
### set_oracle
Change account bandwidth share rate by authority.

Change RWS oracle account.

The dispatch origin for this call must be _Root_.

\# &lt;weight&gt;
- O(1).
- Limited storage reads.
- One DB change.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'RWS', 'set_oracle', {
    'new': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### set_subscription
Change account bandwidth share rate by authority.

The dispatch origin for this call must be _oracle_.

\# &lt;weight&gt;
- O(1).
- Limited storage reads.
- One DB change.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `T::AccountId` | 
| subscription | `Subscription` | 

#### Python
```python
call = substrate.compose_call(
    'RWS', 'set_subscription', {
    'subscription': {
        'Daily': {'days': 'u32'},
        'Lifetime': {'tps': 'u32'},
    },
    'target': 'AccountId',
}
)
```

---------
### start_auction
Start subscription auction.

The dispatch origin for this call must be _root_.

\# &lt;weight&gt;
- O(1).
- Limited storage reads.
- One DB change.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| kind | `Subscription` | 

#### Python
```python
call = substrate.compose_call(
    'RWS', 'start_auction', {
    'kind': {
        'Daily': {'days': 'u32'},
        'Lifetime': {'tps': 'u32'},
    },
}
)
```

---------
## Events

---------
### NewAuction
Started new RWS subscription auction.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Subscription` | ```{'Lifetime': {'tps': 'u32'}, 'Daily': {'days': 'u32'}}```
| None | `T::AuctionIndex` | ```u32```

---------
### NewBid
New subscription auction bid received.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AuctionIndex` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### NewCall
Runtime method executed using RWS subscription.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### NewDevices
Registered RWS subscription devices.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Vec<T::AccountId>` | ```['AccountId']```

---------
### NewSubscription
Registered new RWS subscription.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Subscription` | ```{'Lifetime': {'tps': 'u32'}, 'Daily': {'days': 'u32'}}```

---------
## Storage functions

---------
### Auction
 Indexed auction ledger.

#### Python
```python
result = substrate.query(
    'RWS', 'Auction', ['u32']
)
```

#### Return value
```python
{
    'best_price': 'u128',
    'kind': {'Daily': {'days': 'u32'}, 'Lifetime': {'tps': 'u32'}},
    'winner': (None, 'AccountId'),
}
```
---------
### AuctionNext
 Next auction index.

#### Python
```python
result = substrate.query(
    'RWS', 'AuctionNext', []
)
```

#### Return value
```python
'u32'
```
---------
### AuctionQueue
 Ongoing subscription auctions.

#### Python
```python
result = substrate.query(
    'RWS', 'AuctionQueue', []
)
```

#### Return value
```python
['u32']
```
---------
### Devices
 Subscription linked devices.

#### Python
```python
result = substrate.query(
    'RWS', 'Devices', ['AccountId']
)
```

#### Return value
```python
['AccountId']
```
---------
### Ledger
 RWS subscriptions storage.

#### Python
```python
result = substrate.query(
    'RWS', 'Ledger', ['AccountId']
)
```

#### Return value
```python
{
    'free_weight': 'u64',
    'issue_time': 'u64',
    'kind': {'Daily': {'days': 'u32'}, 'Lifetime': {'tps': 'u32'}},
    'last_update': 'u64',
}
```
---------
### Oracle
 The `AccountId` of Ethereum RWS oracle.

#### Python
```python
result = substrate.query(
    'RWS', 'Oracle', []
)
```

#### Return value
```python
'AccountId'
```
---------
### UnspendBondValue
 This is intermediate value used to escape bonded value loss.
 For each bond if value is not enough to issue new subscription then bonded value will
 be written here.

#### Python
```python
result = substrate.query(
    'RWS', 'UnspendBondValue', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### AuctionCost
 How much token should be bonded to launch new auction.
#### Value
```python
25000000000000
```
#### Python
```python
constant = substrate.get_constant('RWS', 'AuctionCost')
```
---------
### AuctionDuration
 Subscription auction duration in blocks.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('RWS', 'AuctionDuration')
```
---------
### MinimalBid
 Minimal auction bid.
#### Value
```python
1000000000
```
#### Python
```python
constant = substrate.get_constant('RWS', 'MinimalBid')
```
---------
### ReferenceCallWeight
 Reference call weight, general transaction consumes this weight.
#### Value
```python
70952000
```
#### Python
```python
constant = substrate.get_constant('RWS', 'ReferenceCallWeight')
```
---------
### WeightLimit
 Subscription weight accumulator limit.
#### Value
```python
9223372036854775807
```
#### Python
```python
constant = substrate.get_constant('RWS', 'WeightLimit')
```
---------
## Errors

---------
### FreeWeightIsNotEnough
The origin account have no enough free weight to process these call: [free_weight, required_weight].

---------
### NoSubscription
Subscription is not registered.

---------
### NotExistAuction
Auction with the index doesn&\#x27;t exist.

---------
### NotLinkedDevice
Devices isn&\#x27;t assigned to this subscription.

---------
### NotLiveAuction
Auction is not ongoing.

---------
### OracleOnlyCall
This call is for oracle only.

---------
### TooSmallBid
The bid is too small.

---------