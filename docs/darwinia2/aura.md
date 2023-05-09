
# Aura

---------
## Storage functions

---------
### Authorities
 The current authority set.

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
 The current slot of this block.

 This will be set in `on_initialize`.

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