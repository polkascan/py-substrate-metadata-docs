
# AuthorInherent

---------
## Calls

---------
### kick_off_authorship_validation
This inherent is a workaround to run code after the &quot;real&quot; inherents have executed,
but before transactions are executed.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'AuthorInherent', 'kick_off_authorship_validation', {}
)
```

---------
## Storage functions

---------
### Author
 Author of current block.

#### Python
```python
result = substrate.query(
    'AuthorInherent', 'Author', []
)
```

#### Return value
```python
'[u8; 20]'
```
---------
### HighestSlotSeen
 The highest slot that has been seen in the history of this chain.
 This is a strictly-increasing value.

#### Python
```python
result = substrate.query(
    'AuthorInherent', 'HighestSlotSeen', []
)
```

#### Return value
```python
'u32'
```
---------
## Errors

---------
### AuthorAlreadySet
Author already set in block.

---------
### CannotBeAuthor
The author in the inherent is not an eligible author.

---------
### NoAccountId
No AccountId was found to be associated with this author

---------