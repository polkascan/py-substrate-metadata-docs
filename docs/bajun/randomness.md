
# Randomness

---------
## Storage functions

---------
### RandomMaterial
 Series of block headers from the last 81 blocks that acts as random seed material. This
 is arranged as a ring buffer with `block_number % 81` being the index into the `Vec` of
 the oldest hash.

#### Python
```python
result = substrate.query(
    'Randomness', 'RandomMaterial', []
)
```

#### Return value
```python
['scale_info::12']
```
---------