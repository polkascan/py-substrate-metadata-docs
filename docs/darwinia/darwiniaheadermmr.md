
# DarwiniaHeaderMmr

---------
## Storage functions

---------
### MmrSize
 Size of the MMR

#### Python
```python
result = substrate.query(
    'DarwiniaHeaderMmr', 'MmrSize', []
)
```

#### Return value
```python
'u64'
```
---------
### Peaks
 Peaks of the MMR

#### Python
```python
result = substrate.query(
    'DarwiniaHeaderMmr', 'Peaks', ['u64']
)
```

#### Return value
```python
'[u8; 32]'
```
---------