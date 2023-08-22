
# Randomness

---------
## Calls

---------
### set_babe_randomness_results
Populates `RandomnessResults` due this epoch with BABE epoch randomness
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Randomness', 'set_babe_randomness_results', {}
)
```

---------
## Storage functions

---------
### InherentIncluded
 Ensures the mandatory inherent was included in the block

#### Python
```python
result = substrate.query(
    'Randomness', 'InherentIncluded', []
)
```

#### Return value
```python
()
```
---------
### RandomnessResults
 Snapshot of randomness to fulfill all requests that are for the same raw randomness
 Removed once $value.request_count == 0

#### Python
```python
result = substrate.query(
    'Randomness', 'RandomnessResults', [{'BabeEpoch': 'u64'}]
)
```

#### Return value
```python
{'randomness': (None, '[u8; 32]'), 'request_count': 'u64'}
```
---------
### RelayEpoch
 Relay epoch

#### Python
```python
result = substrate.query(
    'Randomness', 'RelayEpoch', []
)
```

#### Return value
```python
'u64'
```
---------
## Errors

---------
### CannotRequestRandomnessAfterMaxDelay

---------