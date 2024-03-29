
# AuraExt

---------
## Storage functions

---------
### Authorities

#### Python
```python
result = substrate.query(
    'AuraExt', 'Authorities', []
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### SlotInfo

#### Python
```python
result = substrate.query(
    'AuraExt', 'SlotInfo', []
)
```

#### Return value
```python
('u64', 'u32')
```
---------