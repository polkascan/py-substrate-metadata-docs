
# AuraExt

---------
## Storage functions

---------
### Authorities
 Serves as cache for the authorities.

 The authorities in AuRa are overwritten in `on_initialize` when we switch to a new session,
 but we require the old authorities to verify the seal when validating a PoV. This will
 always be updated to the latest AuRa authorities in `on_finalize`.

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
 Current slot paired with a number of authored blocks.

 Updated on each block initialization.

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