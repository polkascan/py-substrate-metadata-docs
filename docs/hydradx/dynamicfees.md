
# DynamicFees

---------
## Storage functions

---------
### AssetFee
 Stores last calculated fee of an asset and block number in which it was changed..
 Stored as (Asset fee, Protocol fee, Block number)

#### Python
```python
result = substrate.query(
    'DynamicFees', 'AssetFee', ['u32']
)
```

#### Return value
```python
{'asset_fee': 'u32', 'protocol_fee': 'u32', 'timestamp': 'u32'}
```
---------
## Constants

---------
### AssetFeeParameters
#### Value
```python
{
    'amplification': 2000000000000000000,
    'decay': 10000000000000,
    'max_fee': 50000,
    'min_fee': 2500,
}
```
#### Python
```python
constant = substrate.get_constant('DynamicFees', 'AssetFeeParameters')
```
---------
### ProtocolFeeParameters
#### Value
```python
{
    'amplification': 1000000000000000000,
    'decay': 5000000000000,
    'max_fee': 1000,
    'min_fee': 500,
}
```
#### Python
```python
constant = substrate.get_constant('DynamicFees', 'ProtocolFeeParameters')
```
---------