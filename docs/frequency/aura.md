
# Aura

---------
## Storage functions

---------
### Authorities

#### Python
```python
result = substrate.query(
    'Aura', 'Authorities', []
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### CurrentSlot

#### Python
```python
result = substrate.query(
    'Aura', 'CurrentSlot', []
)
```

#### Return value
```python
'u64'
```
---------