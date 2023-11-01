
# Beefy

---------
## Storage functions

---------
### Authorities
 The current authorities set

#### Python
```python
result = substrate.query(
    'Beefy', 'Authorities', []
)
```

#### Return value
```python
['[u8; 33]']
```
---------
### NextAuthorities
 Authorities set scheduled to be used with the next session

#### Python
```python
result = substrate.query(
    'Beefy', 'NextAuthorities', []
)
```

#### Return value
```python
['[u8; 33]']
```
---------
### ValidatorSetId
 The current validator set id

#### Python
```python
result = substrate.query(
    'Beefy', 'ValidatorSetId', []
)
```

#### Return value
```python
'u64'
```
---------