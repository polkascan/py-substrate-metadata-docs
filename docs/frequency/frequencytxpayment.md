
# FrequencyTxPayment

---------
## Calls

---------
### pay_with_capacity
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'FrequencyTxPayment', 'pay_with_capacity', {'call': 'Call'}
)
```

---------
### pay_with_capacity_batch_all
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'FrequencyTxPayment', 'pay_with_capacity_batch_all', {'calls': ['Call']}
)
```

---------
## Constants

---------
### MaximumCapacityBatchLength
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('FrequencyTxPayment', 'MaximumCapacityBatchLength')
```
---------
## Errors

---------
### BatchedCallAmountExceedsMaximum

---------