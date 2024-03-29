
# TipsMembership

---------
## Calls

---------
### add_member
See [`Pallet::add_member`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'TipsMembership', 'add_member', {
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### change_key
See [`Pallet::change_key`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'TipsMembership', 'change_key', {
    'new': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### clear_prime
See [`Pallet::clear_prime`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'TipsMembership', 'clear_prime', {}
)
```

---------
### remove_member
See [`Pallet::remove_member`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'TipsMembership', 'remove_member', {
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### reset_members
See [`Pallet::reset_members`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| members | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'TipsMembership', 'reset_members', {'members': ['AccountId']}
)
```

---------
### set_prime
See [`Pallet::set_prime`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'TipsMembership', 'set_prime', {
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### swap_member
See [`Pallet::swap_member`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| remove | `AccountIdLookupOf<T>` | 
| add | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'TipsMembership', 'swap_member', {
    'add': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'remove': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
## Events

---------
### Dummy
Phantom member, never used.
#### Attributes
No attributes

---------
### KeyChanged
One of the members&\#x27; keys changed.
#### Attributes
No attributes

---------
### MemberAdded
The given member was added; see the transaction for who.
#### Attributes
No attributes

---------
### MemberRemoved
The given member was removed; see the transaction for who.
#### Attributes
No attributes

---------
### MembersReset
The membership was reset; see the transaction for who the new set is.
#### Attributes
No attributes

---------
### MembersSwapped
Two members were swapped; see the transaction for who.
#### Attributes
No attributes

---------
## Storage functions

---------
### Members
 The current membership, stored as an ordered Vec.

#### Python
```python
result = substrate.query(
    'TipsMembership', 'Members', []
)
```

#### Return value
```python
['AccountId']
```
---------
### Prime
 The current prime member, if one exists.

#### Python
```python
result = substrate.query(
    'TipsMembership', 'Prime', []
)
```

#### Return value
```python
'AccountId'
```
---------
## Errors

---------
### AlreadyMember
Already a member.

---------
### NotMember
Not a member.

---------
### TooManyMembers
Too many members.

---------