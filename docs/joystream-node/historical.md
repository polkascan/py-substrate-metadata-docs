
# Historical

---------
## Storage functions

---------
### HistoricalSessions
 Mapping from historical session indices to session-data root hash and validator count.

#### Python
```python
result = substrate.query(
    'Historical', 'HistoricalSessions', ['u32']
)
```

#### Return value
```python
('[u8; 32]', 'u32')
```
---------
### StoredRange
 The range of historical sessions we store. [first, last)

#### Python
```python
result = substrate.query(
    'Historical', 'StoredRange', []
)
```

#### Return value
```python
('u32', 'u32')
```
---------