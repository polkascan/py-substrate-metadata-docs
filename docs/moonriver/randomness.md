
# Randomness

---------
## Calls

---------
### set_babe_randomness_results
Populates `RandomnessResults` due this epoch with BABE epoch randomness
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Randomness', 'set_babe_randomness_results', {}
)
```

---------
## Events

---------
### RandomnessRequestedBabeEpoch
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `RequestId` | ```u64```
| refund_address | `H160` | ```[u8; 20]```
| contract_address | `H160` | ```[u8; 20]```
| fee | `BalanceOf<T>` | ```u128```
| gas_limit | `u64` | ```u64```
| num_words | `u8` | ```u8```
| salt | `H256` | ```[u8; 32]```
| earliest_epoch | `u64` | ```u64```

---------
### RandomnessRequestedLocal
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `RequestId` | ```u64```
| refund_address | `H160` | ```[u8; 20]```
| contract_address | `H160` | ```[u8; 20]```
| fee | `BalanceOf<T>` | ```u128```
| gas_limit | `u64` | ```u64```
| num_words | `u8` | ```u8```
| salt | `H256` | ```[u8; 32]```
| earliest_block | `T::BlockNumber` | ```u32```

---------
### RequestExpirationExecuted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `RequestId` | ```u64```

---------
### RequestFeeIncreased
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `RequestId` | ```u64```
| new_fee | `BalanceOf<T>` | ```u128```

---------
### RequestFulfilled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `RequestId` | ```u64```

---------
## Storage functions

---------
### InherentIncluded
 Ensures the mandatory inherent was included in the block

#### Python
```python
result = substrate.query(
    'Randomness', 'InherentIncluded', []
)
```

#### Return value
```python
()
```
---------
### LocalVrfOutput
 Current local per-block VRF randomness
 Set in `on_initialize`

#### Python
```python
result = substrate.query(
    'Randomness', 'LocalVrfOutput', []
)
```

#### Return value
```python
(None, '[u8; 32]')
```
---------
### NotFirstBlock
 Records whether this is the first block (genesis or runtime upgrade)

#### Python
```python
result = substrate.query(
    'Randomness', 'NotFirstBlock', []
)
```

#### Return value
```python
()
```
---------
### PreviousLocalVrfOutput
 Previous local per-block VRF randomness
 Set in `on_finalize` of last block

#### Python
```python
result = substrate.query(
    'Randomness', 'PreviousLocalVrfOutput', []
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### RandomnessResults
 Snapshot of randomness to fulfill all requests that are for the same raw randomness
 Removed once $value.request_count == 0

#### Python
```python
result = substrate.query(
    'Randomness', 'RandomnessResults', [{'BabeEpoch': 'u64', 'Local': 'u32'}]
)
```

#### Return value
```python
{'randomness': (None, '[u8; 32]'), 'request_count': 'u64'}
```
---------
### RelayEpoch
 Relay epoch

#### Python
```python
result = substrate.query(
    'Randomness', 'RelayEpoch', []
)
```

#### Return value
```python
'u64'
```
---------
### RequestCount
 Number of randomness requests made so far, used to generate the next request&#x27;s uid

#### Python
```python
result = substrate.query(
    'Randomness', 'RequestCount', []
)
```

#### Return value
```python
'u64'
```
---------
### Requests
 Randomness requests not yet fulfilled or purged

#### Python
```python
result = substrate.query(
    'Randomness', 'Requests', ['u64']
)
```

#### Return value
```python
{
    'deposit': 'u128',
    'request': {
        'contract_address': '[u8; 20]',
        'fee': 'u128',
        'gas_limit': 'u64',
        'info': {'BabeEpoch': ('u64', 'u64'), 'Local': ('u32', 'u32')},
        'num_words': 'u8',
        'refund_address': '[u8; 20]',
        'salt': '[u8; 32]',
    },
}
```
---------
## Constants

---------
### BlockExpirationDelay
 Local requests expire and can be purged from storage after this many blocks/epochs
#### Value
```python
10000
```
#### Python
```python
constant = substrate.get_constant('Randomness', 'BlockExpirationDelay')
```
---------
### Deposit
 The amount that should be taken as a security deposit when requesting randomness.
#### Value
```python
1000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Randomness', 'Deposit')
```
---------
### EpochExpirationDelay
 Babe requests expire and can be purged from storage after this many blocks/epochs
#### Value
```python
10000
```
#### Python
```python
constant = substrate.get_constant('Randomness', 'EpochExpirationDelay')
```
---------
### MaxBlockDelay
 Local per-block VRF requests must be at most this many blocks after the block in which
 they were requested
#### Value
```python
2000
```
#### Python
```python
constant = substrate.get_constant('Randomness', 'MaxBlockDelay')
```
---------
### MaxRandomWords
 Maximum number of random words that can be requested per request
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Randomness', 'MaxRandomWords')
```
---------
### MinBlockDelay
 Local per-block VRF requests must be at least this many blocks after the block in which
 they were requested
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('Randomness', 'MinBlockDelay')
```
---------
## Errors

---------
### CannotRequestMoreWordsThanMax

---------
### CannotRequestRandomnessAfterMaxDelay

---------
### CannotRequestRandomnessBeforeMinDelay

---------
### MustRequestAtLeastOneWord

---------
### OnlyRequesterCanIncreaseFee

---------
### RandomnessResultDNE

---------
### RandomnessResultNotFilled

---------
### RequestCannotYetBeFulfilled

---------
### RequestCounterOverflowed

---------
### RequestDNE

---------
### RequestFeeOverflowed

---------
### RequestHasNotExpired

---------