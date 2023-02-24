
# LiquidityMining

---------
## Calls

---------
### set_per_block_distribution
#### Attributes
| Name | Type |
| -------- | -------- | 
| per_block_distribution | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityMining', 'set_per_block_distribution', {'per_block_distribution': 'u128'}
)
```

---------
## Events

---------
### AddedIncentives
The number of markets that received incentives in a block
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MaxRuntimeUsize` | ```u64```

---------
### DistributedIncentives
The total amount of incentives distributed to accounts along side the number
of accounts that received these incentives.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T>` | ```u128```
| None | `MaxRuntimeUsize` | ```u64```

---------
### SubtractedIncentives
The number of markets that subtracted incentives in a block
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MaxRuntimeUsize` | ```u64```

---------
## Storage functions

---------
### BlockBoughtShares
 Shares bought in the current block being constructed. Automatically *erased* after each finalized block.

#### Python
```python
result = substrate.query(
    'LiquidityMining', 'BlockBoughtShares', ['u128', 'AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### BlockSoldShares
 Shares sold in the current block being constructed. Automatically *erased* after each finalized block.

#### Python
```python
result = substrate.query(
    'LiquidityMining', 'BlockSoldShares', ['u128', 'AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### OwnedValues
 Owned balances (not shares) that are going to be distributed as incentives. Automatically
 *updated* after each finalized block.

#### Python
```python
result = substrate.query(
    'LiquidityMining', 'OwnedValues', ['u128', 'AccountId']
)
```

#### Return value
```python
{
    'participated_blocks': 'u64',
    'perpetual_incentives': 'u128',
    'total_incentives': 'u128',
    'total_shares': 'u128',
}
```
---------
### PerBlockIncentive
 Per block distribution. How much each block will distribute across bought shares.

#### Python
```python
result = substrate.query(
    'LiquidityMining', 'PerBlockIncentive', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### PalletId
#### Value
```python
'0x7a67652f6c796d67'
```
#### Python
```python
constant = substrate.get_constant('LiquidityMining', 'PalletId')
```
---------
## Errors

---------
### FundDoesNotHaveEnoughBalance
Pallet account does not have enough funds

---------