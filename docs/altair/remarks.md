
# Remarks

---------
## Calls

---------
### remark
Add remarks to a call.

The weight calculation is similar to the one in the Proxy.proxy.
#### Attributes
| Name | Type |
| -------- | -------- | 
| remarks | `BoundedVec<T::Remark, T::MaxRemarksPerCall>` | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Remarks', 'remark', {
    'call': 'Call',
    'remarks': [
        {
            'IpfsHash': 'Bytes',
            'Loan': ('u64', 'u64'),
            'Named': 'Bytes',
        },
    ],
}
)
```

---------
## Events

---------
### Remark
A remark was made.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| remarks | `BoundedVec<T::Remark, T::MaxRemarksPerCall>` | ```[{'IpfsHash': 'Bytes', 'Named': 'Bytes', 'Loan': ('u64', 'u64')}]```
| call | `<T as Config>::RuntimeCall` | ```Call```

---------
## Errors

---------
### NoRemarks
No remarks were provided.

---------