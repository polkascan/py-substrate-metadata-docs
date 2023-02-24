
# HotfixSufficients

---------
## Calls

---------
### hotfix_inc_account_sufficients
Increment `sufficients` for existing accounts having a nonzero `nonce` but zero `sufficients`, `consumers` and `providers` value.
This state was caused by a previous bug in EVM create account dispatchable.

Any accounts in the input list not satisfying the above condition will remain unaffected.
#### Attributes
| Name | Type |
| -------- | -------- | 
| addresses | `Vec<H160>` | 

#### Python
```python
call = substrate.compose_call(
    'HotfixSufficients', 'hotfix_inc_account_sufficients', {'addresses': ['[u8; 20]']}
)
```

---------
## Errors

---------
### MaxAddressCountExceeded
Maximum address count exceeded

---------