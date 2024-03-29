
# DynamicEvmBaseFee

---------
## Calls

---------
### set_base_fee_per_gas
See [`Pallet::set_base_fee_per_gas`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| fee | `U256` | 

#### Python
```python
call = substrate.compose_call(
    'DynamicEvmBaseFee', 'set_base_fee_per_gas', {'fee': 'scale_info::135'}
)
```

---------
## Events

---------
### NewBaseFeePerGas
New `base fee per gas` value has been force-set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| fee | `U256` | ```scale_info::135```

---------
## Storage functions

---------
### BaseFeePerGas

#### Python
```python
result = substrate.query(
    'DynamicEvmBaseFee', 'BaseFeePerGas', []
)
```

#### Return value
```python
'scale_info::135'
```
---------
## Errors

---------
### ValueOutOfBounds
Specified value is outside of the allowed range.

---------