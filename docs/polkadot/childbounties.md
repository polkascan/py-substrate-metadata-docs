
# ChildBounties

---------
## Calls

---------
### accept_curator
Accept the curator role for the child-bounty.

The dispatch origin for this call must be the curator of this
child-bounty.

A deposit will be reserved from the curator and refund upon
successful payout or cancellation.

Fee for curator is deducted from curator fee of parent bounty.

Parent bounty must be in active state, for this child-bounty call to
work.

Child-bounty must be in &quot;CuratorProposed&quot; state, for processing the
call. And state of child-bounty is moved to &quot;Active&quot; on successful
call completion.

- `parent_bounty_id`: Index of parent bounty.
- `child_bounty_id`: Index of child bounty.
#### Attributes
| Name | Type |
| -------- | -------- | 
| parent_bounty_id | `BountyIndex` | 
| child_bounty_id | `BountyIndex` | 

#### Python
```python
call = substrate.compose_call(
    'ChildBounties', 'accept_curator', {
    'child_bounty_id': 'u32',
    'parent_bounty_id': 'u32',
}
)
```

---------
### add_child_bounty
Add a new child-bounty.

The dispatch origin for this call must be the curator of parent
bounty and the parent bounty must be in &quot;active&quot; state.

Child-bounty gets added successfully &amp; fund gets transferred from
parent bounty to child-bounty account, if parent bounty has enough
funds, else the call fails.

Upper bound to maximum number of active  child bounties that can be
added are managed via runtime trait config
[`Config::MaxActiveChildBountyCount`].

If the call is success, the status of child-bounty is updated to
&quot;Added&quot;.

- `parent_bounty_id`: Index of parent bounty for which child-bounty is being added.
- `value`: Value for executing the proposal.
- `description`: Text description for the child-bounty.
#### Attributes
| Name | Type |
| -------- | -------- | 
| parent_bounty_id | `BountyIndex` | 
| value | `BalanceOf<T>` | 
| description | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'ChildBounties', 'add_child_bounty', {
    'description': 'Bytes',
    'parent_bounty_id': 'u32',
    'value': 'u128',
}
)
```

---------
### award_child_bounty
Award child-bounty to a beneficiary.

The beneficiary will be able to claim the funds after a delay.

The dispatch origin for this call must be the parent curator or
curator of this child-bounty.

Parent bounty must be in active state, for this child-bounty call to
work.

Child-bounty must be in active state, for processing the call. And
state of child-bounty is moved to &quot;PendingPayout&quot; on successful call
completion.

- `parent_bounty_id`: Index of parent bounty.
- `child_bounty_id`: Index of child bounty.
- `beneficiary`: Beneficiary account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| parent_bounty_id | `BountyIndex` | 
| child_bounty_id | `BountyIndex` | 
| beneficiary | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ChildBounties', 'award_child_bounty', {
    'beneficiary': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'child_bounty_id': 'u32',
    'parent_bounty_id': 'u32',
}
)
```

---------
### claim_child_bounty
Claim the payout from an awarded child-bounty after payout delay.

The dispatch origin for this call may be any signed origin.

Call works independent of parent bounty state, No need for parent
bounty to be in active state.

The Beneficiary is paid out with agreed bounty value. Curator fee is
paid &amp; curator deposit is unreserved.

Child-bounty must be in &quot;PendingPayout&quot; state, for processing the
call. And instance of child-bounty is removed from the state on
successful call completion.

- `parent_bounty_id`: Index of parent bounty.
- `child_bounty_id`: Index of child bounty.
#### Attributes
| Name | Type |
| -------- | -------- | 
| parent_bounty_id | `BountyIndex` | 
| child_bounty_id | `BountyIndex` | 

#### Python
```python
call = substrate.compose_call(
    'ChildBounties', 'claim_child_bounty', {
    'child_bounty_id': 'u32',
    'parent_bounty_id': 'u32',
}
)
```

---------
### close_child_bounty
Cancel a proposed or active child-bounty. Child-bounty account funds
are transferred to parent bounty account. The child-bounty curator
deposit may be unreserved if possible.

The dispatch origin for this call must be either parent curator or
`T::RejectOrigin`.

If the state of child-bounty is `Active`, curator deposit is
unreserved.

If the state of child-bounty is `PendingPayout`, call fails &amp;
returns `PendingPayout` error.

For the origin other than T::RejectOrigin, parent bounty must be in
active state, for this child-bounty call to work. For origin
T::RejectOrigin execution is forced.

Instance of child-bounty is removed from the state on successful
call completion.

- `parent_bounty_id`: Index of parent bounty.
- `child_bounty_id`: Index of child bounty.
#### Attributes
| Name | Type |
| -------- | -------- | 
| parent_bounty_id | `BountyIndex` | 
| child_bounty_id | `BountyIndex` | 

#### Python
```python
call = substrate.compose_call(
    'ChildBounties', 'close_child_bounty', {
    'child_bounty_id': 'u32',
    'parent_bounty_id': 'u32',
}
)
```

---------
### propose_curator
Propose curator for funded child-bounty.

The dispatch origin for this call must be curator of parent bounty.

Parent bounty must be in active state, for this child-bounty call to
work.

Child-bounty must be in &quot;Added&quot; state, for processing the call. And
state of child-bounty is moved to &quot;CuratorProposed&quot; on successful
call completion.

- `parent_bounty_id`: Index of parent bounty.
- `child_bounty_id`: Index of child bounty.
- `curator`: Address of child-bounty curator.
- `fee`: payment fee to child-bounty curator for execution.
#### Attributes
| Name | Type |
| -------- | -------- | 
| parent_bounty_id | `BountyIndex` | 
| child_bounty_id | `BountyIndex` | 
| curator | `AccountIdLookupOf<T>` | 
| fee | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ChildBounties', 'propose_curator', {
    'child_bounty_id': 'u32',
    'curator': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'fee': 'u128',
    'parent_bounty_id': 'u32',
}
)
```

---------
### unassign_curator
Unassign curator from a child-bounty.

The dispatch origin for this call can be either `RejectOrigin`, or
the curator of the parent bounty, or any signed origin.

For the origin other than T::RejectOrigin and the child-bounty
curator, parent bounty must be in active state, for this call to
work. We allow child-bounty curator and T::RejectOrigin to execute
this call irrespective of the parent bounty state.

If this function is called by the `RejectOrigin` or the
parent bounty curator, we assume that the child-bounty curator is
malicious or inactive. As a result, child-bounty curator deposit is
slashed.

If the origin is the child-bounty curator, we take this as a sign
that they are unable to do their job, and are willingly giving up.
We could slash the deposit, but for now we allow them to unreserve
their deposit and exit without issue. (We may want to change this if
it is abused.)

Finally, the origin can be anyone iff the child-bounty curator is
&quot;inactive&quot;. Expiry update due of parent bounty is used to estimate
inactive state of child-bounty curator.

This allows anyone in the community to call out that a child-bounty
curator is not doing their due diligence, and we should pick a new
one. In this case the child-bounty curator deposit is slashed.

State of child-bounty is moved to Added state on successful call
completion.

- `parent_bounty_id`: Index of parent bounty.
- `child_bounty_id`: Index of child bounty.
#### Attributes
| Name | Type |
| -------- | -------- | 
| parent_bounty_id | `BountyIndex` | 
| child_bounty_id | `BountyIndex` | 

#### Python
```python
call = substrate.compose_call(
    'ChildBounties', 'unassign_curator', {
    'child_bounty_id': 'u32',
    'parent_bounty_id': 'u32',
}
)
```

---------
## Events

---------
### Added
A child-bounty is added.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```
| child_index | `BountyIndex` | ```u32```

---------
### Awarded
A child-bounty is awarded to a beneficiary.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```
| child_index | `BountyIndex` | ```u32```
| beneficiary | `T::AccountId` | ```AccountId```

---------
### Canceled
A child-bounty is cancelled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```
| child_index | `BountyIndex` | ```u32```

---------
### Claimed
A child-bounty is claimed by beneficiary.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```
| child_index | `BountyIndex` | ```u32```
| payout | `BalanceOf<T>` | ```u128```
| beneficiary | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### ChildBounties
 Child bounties that have been added.

#### Python
```python
result = substrate.query(
    'ChildBounties', 'ChildBounties', ['u32', 'u32']
)
```

#### Return value
```python
{
    'curator_deposit': 'u128',
    'fee': 'u128',
    'parent_bounty': 'u32',
    'status': {
        'Active': {'curator': 'AccountId'},
        'Added': None,
        'CuratorProposed': {'curator': 'AccountId'},
        'PendingPayout': {
            'beneficiary': 'AccountId',
            'curator': 'AccountId',
            'unlock_at': 'u32',
        },
    },
    'value': 'u128',
}
```
---------
### ChildBountyCount
 Number of total child bounties.

#### Python
```python
result = substrate.query(
    'ChildBounties', 'ChildBountyCount', []
)
```

#### Return value
```python
'u32'
```
---------
### ChildBountyDescriptions
 The description of each child-bounty.

#### Python
```python
result = substrate.query(
    'ChildBounties', 'ChildBountyDescriptions', ['u32']
)
```

#### Return value
```python
'Bytes'
```
---------
### ChildrenCuratorFees
 The cumulative child-bounty curator fee for each parent bounty.

#### Python
```python
result = substrate.query(
    'ChildBounties', 'ChildrenCuratorFees', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### ParentChildBounties
 Number of child bounties per parent bounty.
 Map of parent bounty index to number of child bounties.

#### Python
```python
result = substrate.query(
    'ChildBounties', 'ParentChildBounties', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### ChildBountyValueMinimum
 Minimum value for a child-bounty.
#### Value
```python
10000000000
```
#### Python
```python
constant = substrate.get_constant('ChildBounties', 'ChildBountyValueMinimum')
```
---------
### MaxActiveChildBountyCount
 Maximum number of child bounties that can be added to a parent bounty.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('ChildBounties', 'MaxActiveChildBountyCount')
```
---------
## Errors

---------
### InsufficientBountyBalance
The bounty balance is not enough to add new child-bounty.

---------
### ParentBountyNotActive
The parent bounty is not in active state.

---------
### TooManyChildBounties
Number of child bounties exceeds limit `MaxActiveChildBountyCount`.

---------