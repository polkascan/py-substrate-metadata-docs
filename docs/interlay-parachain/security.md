
# Security

---------
## Calls

---------
### activate_counter
Activate or deactivate active block counting.
#### Attributes
| Name | Type |
| -------- | -------- | 
| is_active | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Security', 'activate_counter', {'is_active': 'bool'}
)
```

---------
## Events

---------
### Activated
#### Attributes
No attributes

---------
### Deactivated
#### Attributes
No attributes

---------
### UpdateActiveBlock
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| block_number | `T::BlockNumber` | ```u32```

---------
## Storage functions

---------
### ActiveBlockCount
 Like frame_system::block_number, but this one only increments if the parachain status is RUNNING.
 This variable is used to keep track of durations, such as the issue/redeem/replace expiry. If the
 parachain is not RUNNING, no payment proofs can be submitted, and it wouldn&#x27;t be fair to punish
 the user/vault. By using this variable we ensure that they have sufficient time to submit their
 proof.

#### Python
```python
result = substrate.query(
    'Security', 'ActiveBlockCount', []
)
```

#### Return value
```python
'u32'
```
---------
### IsDeactivated

#### Python
```python
result = substrate.query(
    'Security', 'IsDeactivated', []
)
```

#### Return value
```python
'bool'
```
---------
### Nonce
 Integer increment-only counter, used to prevent collisions when generating identifiers
 for e.g. issue, redeem or replace requests (for OP_RETURN field in Bitcoin).

#### Python
```python
result = substrate.query(
    'Security', 'Nonce', []
)
```

#### Return value
```python
'scale_info::186'
```
---------