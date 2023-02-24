
# Pools

---------
## Calls

---------
### mutate_pools
Mutate the pools. Can only be called by root.
#### Attributes
| Name | Type |
| -------- | -------- | 
| mutation | `PoolsMutation` | 

#### Python
```python
call = substrate.compose_call(
    'Pools', 'mutate_pools', {
    'mutation': {
        'collator': {
            'fee_share': 'u32',
        },
        'community': {
            'fee_share': 'u32',
        },
        'fuel_tanks': {
            'fee_share': 'u32',
        },
        'price_discovery': {
            'fee_share': 'u32',
        },
    },
}
)
```

---------
## Events

---------
### PoolsMutated
Pools storage was modified by `PoolsMutation`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolsMutation` | ```{'community': {'fee_share': 'u32'}, 'collator': {'fee_share': 'u32'}, 'fuel_tanks': {'fee_share': 'u32'}, 'price_discovery': {'fee_share': 'u32'}}```

---------
## Storage functions

---------
### Pools
 Information about the pools

#### Python
```python
result = substrate.query(
    'Pools', 'Pools', []
)
```

#### Return value
```python
'scale_info::554'
```
---------
## Constants

---------
### FeeDistributorAccountId
 The `AccountId` that holds fees until they are distributed
#### Value
```python
'efRd63tR845wJTXfddgZNfNZ55o23Erydfz8esAmo1HfgMZMS'
```
#### Python
```python
constant = substrate.get_constant('Pools', 'FeeDistributorAccountId')
```
---------
### PoolAccountIds
 The `AccountId` for each pool
#### Value
```python
{
    'collator': 'efRd63tR845wJ4KW17VFyzzS38m2zRjMbabQa5VyTNTikSqdy',
    'community': 'efRd63tR845wJ4FxoUfFgrDpxfAQ2t1iydU7LyzJCf577hgTH',
    'fuel_tanks': 'efRd63tR845wJU26BdopK9W8Gw8D3SCNynXMfjiWGcNMJn9yZ',
    'price_discovery': 'efRd63tR845wKpKPu3FxnN1JrKddzhuynU94yiEXzKGRqwsWv',
}
```
#### Python
```python
constant = substrate.get_constant('Pools', 'PoolAccountIds')
```
---------
### PoolCount
 The number of pools
#### Value
```python
4
```
#### Python
```python
constant = substrate.get_constant('Pools', 'PoolCount')
```
---------
## Errors

---------
### InvalidFeeShares
The fee shares must add up to 100 percent

---------
### PoolCountExceeded
The number of pools was exceeded

---------