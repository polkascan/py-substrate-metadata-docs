
# DynamicEvmFee

---------
## Storage functions

---------
### BaseFeePerGas
 Base fee per gas

#### Python
```python
result = substrate.query(
    'DynamicEvmFee', 'BaseFeePerGas', []
)
```

#### Return value
```python
'scale_info::337'
```
---------
## Constants

---------
### WethAssetId
 WETH Asset Id
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('DynamicEvmFee', 'WethAssetId')
```
---------