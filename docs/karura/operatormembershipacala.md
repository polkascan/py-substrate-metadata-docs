
# OperatorMembershipAcala

---------
## Calls

---------
### add_member
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'OperatorMembershipAcala', 'add_member', {
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### change_key
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'OperatorMembershipAcala', 'change_key', {
    'new': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### clear_prime
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'OperatorMembershipAcala', 'clear_prime', {}
)
```

---------
### remove_member
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'OperatorMembershipAcala', 'remove_member', {
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### reset_members
#### Attributes
| Name | Type |
| -------- | -------- | 
| members | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'OperatorMembershipAcala', 'reset_members', {'members': ['AccountId']}
)
```

---------
### set_prime
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'OperatorMembershipAcala', 'set_prime', {
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### swap_member
#### Attributes
| Name | Type |
| -------- | -------- | 
| remove | `AccountIdLookupOf<T>` | 
| add | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'OperatorMembershipAcala', 'swap_member', {
    'add': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'remove': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
## Events

---------
### Dummy
#### Attributes
No attributes

---------
### KeyChanged
#### Attributes
No attributes

---------
### MemberAdded
#### Attributes
No attributes

---------
### MemberRemoved
#### Attributes
No attributes

---------
### MembersReset
#### Attributes
No attributes

---------
### MembersSwapped
#### Attributes
No attributes

---------
## Storage functions

---------
### Members

#### Python
```python
result = substrate.query(
    'OperatorMembershipAcala', 'Members', []
)
```

#### Return value
```python
['AccountId']
```
---------
### Prime

#### Python
```python
result = substrate.query(
    'OperatorMembershipAcala', 'Prime', []
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

---------
### NotMember

---------
### TooManyMembers

---------