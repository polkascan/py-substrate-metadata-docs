
# LiquidStakingAgentsMembership

---------
## Calls

---------
### add_member
Add a member `who` to the set.

May only be called from `T::AddOrigin`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidStakingAgentsMembership', 'add_member', {
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
Swap out the sending member for some other key `new`.

May only be called from `Signed` origin of a current member.

Prime membership is passed from the origin account to `new`, if extant.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidStakingAgentsMembership', 'change_key', {
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
Remove the prime member if it exists.

May only be called from `T::PrimeOrigin`.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'LiquidStakingAgentsMembership', 'clear_prime', {}
)
```

---------
### remove_member
Remove a member `who` from the set.

May only be called from `T::RemoveOrigin`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidStakingAgentsMembership', 'remove_member', {
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
Change the membership to a new set, disregarding the existing membership. Be nice and
pass `members` pre-sorted.

May only be called from `T::ResetOrigin`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| members | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidStakingAgentsMembership', 'reset_members', {'members': ['AccountId']}
)
```

---------
### set_prime
Set the prime member. Must be a current member.

May only be called from `T::PrimeOrigin`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidStakingAgentsMembership', 'set_prime', {
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
Swap out one member `remove` for another `add`.

May only be called from `T::SwapOrigin`.

Prime membership is *not* passed from `remove` to `add`, if extant.
#### Attributes
| Name | Type |
| -------- | -------- | 
| remove | `AccountIdLookupOf<T>` | 
| add | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidStakingAgentsMembership', 'swap_member', {
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
    'LiquidStakingAgentsMembership', 'Members', []
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
    'LiquidStakingAgentsMembership', 'Prime', []
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