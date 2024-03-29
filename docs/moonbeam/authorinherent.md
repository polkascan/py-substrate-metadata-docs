
# AuthorInherent

---------
## Calls

---------
### kick_off_authorship_validation
See [`Pallet::kick_off_authorship_validation`].
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