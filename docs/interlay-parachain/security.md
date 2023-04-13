
# Security

---------
## Calls

---------
### insert_parachain_error
Insert a new parachain error.

\# Arguments

* `origin` - the dispatch origin of this call (must be _Root_)
* `error_code` - the error code to insert

\# Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| error_code | `ErrorCode` | 

#### Python
```python
call = substrate.compose_call(
    'Security', 'insert_parachain_error', {
    'error_code': (
        'None',
        'OracleOffline',
    ),
}
)
```

---------
### remove_parachain_error
Remove a parachain error.

\# Arguments

* `origin` - the dispatch origin of this call (must be _Root_)
* `error_code` - the error code to remove

\# Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| error_code | `ErrorCode` | 

#### Python
```python
call = substrate.compose_call(
    'Security', 'remove_parachain_error', {
    'error_code': (
        'None',
        'OracleOffline',
    ),
}
)
```

---------
### set_parachain_status
Set the parachain status code.

\# Arguments

* `origin` - the dispatch origin of this call (must be _Root_)
* `status_code` - the status code to set

\# Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| status_code | `StatusCode` | 

#### Python
```python
call = substrate.compose_call(
    'Security', 'set_parachain_status', {'status_code': ('Running', 'Error')}
)
```

---------
## Events

---------
### RecoverFromErrors
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| new_status | `StatusCode` | ```('Running', 'Error')```
| cleared_errors | `Vec<ErrorCode>` | ```[('None', 'OracleOffline')]```

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
### Errors
 Set of ErrorCodes, indicating the reason for an &quot;Error&quot; ParachainStatus.

#### Python
```python
result = substrate.query(
    'Security', 'Errors', []
)
```

#### Return value
```python
'scale_info::412'
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
'[u64; 4]'
```
---------
### ParachainStatus
 Integer/Enum defining the current state of the BTC-Parachain.

#### Python
```python
result = substrate.query(
    'Security', 'ParachainStatus', []
)
```

#### Return value
```python
('Running', 'Error')
```
---------
## Errors

---------
### ParachainNotRunning
Parachain is not running.

---------