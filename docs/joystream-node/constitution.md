
# Constitution

---------
## Calls

---------
### amend_constitution
Sets the current constitution hash. Requires root origin.
\# &lt;weight&gt;
- Complexity: `O(C)` where C is the length of the constitution text.
- Db reads: 0
- Db writes: 1 (constant value)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| constitution_text | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Constitution', 'amend_constitution', {'constitution_text': 'Bytes'}
)
```

---------
## Events

---------
### ConstutionAmended
Emits on constitution amendment.
Parameters:
- constitution text hash
- constitution text
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Hash` | ```[u8; 32]```
| None | `Vec<u8>` | ```Bytes```

---------
## Storage functions

---------
### Constitution

#### Python
```python
result = substrate.query(
    'Constitution', 'Constitution', []
)
```

#### Return value
```python
{'text_hash': '[u8; 32]'}
```
---------