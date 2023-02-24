
# Delegation

---------
## Calls

---------
### add_delegation
Create a new delegation node.

The new delegation node represents a new trust hierarchy that
considers the new node as its root. The owner of this node has full
control over any of its direct and indirect descendants.

For the creation to succeed, the delegatee must provide a valid
signature over the (blake256) hash of the creation operation details
which include (in order) delegation id, root node id, parent id, and
permissions of the new node.

There must be no delegation with the same id stored on chain.
Furthermore, the referenced root and parent nodes must already be
present on chain and contain the valid permissions and revocation
status (i.e., not revoked).

The dispatch origin must be split into
* a submitter of type `AccountId` who is responsible for paying the
  transaction fee and
* a DID subject of type `DelegationEntityId` who creates, owns and
  can revoke the delegation.

Requires the sender of the transaction to have a reservable balance
of at least `Deposit` many tokens.

Emits `DelegationCreated`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: [Origin Account], Roots, Delegations
- Writes: Delegations
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegation_id | `DelegationNodeIdOf<T>` | 
| parent_id | `DelegationNodeIdOf<T>` | 
| delegate | `DelegatorIdOf<T>` | 
| permissions | `Permissions` | 
| delegate_signature | `DelegateSignatureTypeOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Delegation', 'add_delegation', {
    'delegate': 'AccountId',
    'delegate_signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
    'delegation_id': '[u8; 32]',
    'parent_id': '[u8; 32]',
    'permissions': {'bits': 'u32'},
}
)
```

---------
### change_deposit_owner
Changes the deposit owner.

The balance that is reserved by the current deposit owner will be
freed and balance of the new deposit owner will get reserved.

The subject of the call must be the owner of the delegation node.
The sender of the call will be the new deposit owner.
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegation_id | `DelegationNodeIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Delegation', 'change_deposit_owner', {'delegation_id': '[u8; 32]'}
)
```

---------
### create_hierarchy
Create a new delegation root associated with a given CType hash.

The new root will allow a new trust hierarchy to be created by
adding children delegations to the root.

There must be no delegation with the same ID stored on chain, while
there must be already a CType with the given hash stored in the
CType pallet.

The dispatch origin must be split into
* a submitter of type `AccountId` who is responsible for paying the
  transaction fee and
* a DID subject of type `DelegationEntityId` who creates, owns and
  can revoke the delegation.

Requires the sender of the transaction to have a reservable balance
of at least `Deposit` many tokens.

Emits `RootCreated`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: [Origin Account], Roots, CTypes
- Writes: Roots
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| root_node_id | `DelegationNodeIdOf<T>` | 
| ctype_hash | `CtypeHashOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Delegation', 'create_hierarchy', {
    'ctype_hash': '[u8; 32]',
    'root_node_id': '[u8; 32]',
}
)
```

---------
### reclaim_deposit
Reclaim the deposit for a delegation node (potentially a root
node), removing the node and all its children.

Returns the delegation deposit to the deposit owner for each
removed DelegationNode by unreserving it.

Removing a delegation node results in the trust hierarchy starting
from the given node being removed. Nevertheless, removal starts
from the leave nodes upwards, so if the operation ends prematurely
because it runs out of gas, the delegation state would be consistent
as no child would &quot;survive&quot; its parent. As a consequence, if the
given node is removed, the trust hierarchy with the node as root is
to be considered removed.

The dispatch origin must be signed by the delegation deposit owner.

`DepositReclaimed`.

\# &lt;weight&gt;
Weight: O(C) where C is the number of children of the delegation
node which is bounded by `max_removals`.
- Reads: [Origin Account], Roots, C * Delegations, C * Children.
- Writes: Roots, 2 * C * Delegations
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegation_id | `DelegationNodeIdOf<T>` | 
| max_removals | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Delegation', 'reclaim_deposit', {
    'delegation_id': '[u8; 32]',
    'max_removals': 'u32',
}
)
```

---------
### remove_delegation
Remove a delegation node (potentially a root node) and all its
children.

Returns the delegation deposit to the deposit owner for each
removed DelegationNode by unreserving it.

Removing a delegation node results in the trust hierarchy starting
from the given node being removed. Nevertheless, removal starts
from the leave nodes upwards, so if the operation ends prematurely
because it runs out of gas, the delegation state would be consistent
as no child would &quot;survive&quot; its parent. As a consequence, if the
given node is removed, the trust hierarchy with the node as root is
to be considered removed.

The dispatch origin must be split into
* a submitter of type `AccountId` who is responsible for paying the
  transaction fee and
* a DID subject of type `DelegationEntityId` who creates, owns and
  can revoke the delegation.

Emits C * `DelegationRemoved`.

\# &lt;weight&gt;
Weight: O(C) where C is the number of children of the delegation
node which is bounded by `max_children`.
- Reads: [Origin Account], Roots, C * Delegations, C * Children.
- Writes: Roots, 2 * C * Delegations
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegation_id | `DelegationNodeIdOf<T>` | 
| max_removals | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Delegation', 'remove_delegation', {
    'delegation_id': '[u8; 32]',
    'max_removals': 'u32',
}
)
```

---------
### revoke_delegation
Revoke a delegation node (potentially a root node) and all its
children.

Does not refund the delegation back to the deposit owner as the
node is still stored on chain. Requires to additionally call
`remove_delegation` to unreserve the deposit.

Revoking a delegation node results in the trust hierarchy starting
from the given node being revoked. Nevertheless, revocation starts
from the leave nodes upwards, so if the operation ends prematurely
because it runs out of gas, the delegation state would be consistent
as no child would &quot;survive&quot; its parent. As a consequence, if the
given node is revoked, the trust hierarchy with the node as root is
to be considered revoked.

The dispatch origin must be split into
* a submitter of type `AccountId` who is responsible for paying the
  transaction fee and
* a DID subject of type `DelegationEntityId` who creates, owns and
  can revoke the delegation.

Emits C * `DelegationRevoked`.

\# &lt;weight&gt;
Weight: O(C) where C is the number of children of the delegation
node which is bounded by `max_children`.
- Reads: [Origin Account], Roots, C * Delegations, C * Children.
- Writes: Roots, C * Delegations
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegation_id | `DelegationNodeIdOf<T>` | 
| max_parent_checks | `u32` | 
| max_revocations | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Delegation', 'revoke_delegation', {
    'delegation_id': '[u8; 32]',
    'max_parent_checks': 'u32',
    'max_revocations': 'u32',
}
)
```

---------
### update_deposit
Updates the deposit amount to the current deposit rate.

The sender must be the deposit owner.
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegation_id | `DelegationNodeIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Delegation', 'update_deposit', {'delegation_id': '[u8; 32]'}
)
```

---------
## Events

---------
### DelegationCreated
A new delegation has been created.
\[creator ID, root node ID, delegation node ID, parent node ID,
delegate ID, permissions\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DelegatorIdOf<T>` | ```AccountId```
| None | `DelegationNodeIdOf<T>` | ```[u8; 32]```
| None | `DelegationNodeIdOf<T>` | ```[u8; 32]```
| None | `DelegationNodeIdOf<T>` | ```[u8; 32]```
| None | `DelegatorIdOf<T>` | ```AccountId```
| None | `Permissions` | ```{'bits': 'u32'}```

---------
### DelegationRemoved
A delegation has been removed.
\[remover ID, delegation node ID\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `DelegationNodeIdOf<T>` | ```[u8; 32]```

---------
### DelegationRevoked
A delegation has been revoked.
\[revoker ID, delegation node ID\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DelegatorIdOf<T>` | ```AccountId```
| None | `DelegationNodeIdOf<T>` | ```[u8; 32]```

---------
### DepositReclaimed
The deposit owner reclaimed a deposit by removing a delegation
subtree. \[revoker ID, delegation node ID\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `DelegationNodeIdOf<T>` | ```[u8; 32]```

---------
### HierarchyCreated
A new hierarchy has been created.
\[creator ID, root node ID, CTYPE hash\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DelegatorIdOf<T>` | ```AccountId```
| None | `DelegationNodeIdOf<T>` | ```[u8; 32]```
| None | `CtypeHashOf<T>` | ```[u8; 32]```

---------
### HierarchyRemoved
A hierarchy has been removed from the storage on chain.
\[remover ID, root node ID\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DelegatorIdOf<T>` | ```AccountId```
| None | `DelegationNodeIdOf<T>` | ```[u8; 32]```

---------
### HierarchyRevoked
A hierarchy has been revoked.
\[revoker ID, root node ID\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DelegatorIdOf<T>` | ```AccountId```
| None | `DelegationNodeIdOf<T>` | ```[u8; 32]```

---------
## Storage functions

---------
### DelegationHierarchies
 Delegation hierarchies stored on chain.

 It maps for a (root) node ID to the hierarchy details.

#### Python
```python
result = substrate.query(
    'Delegation', 'DelegationHierarchies', ['[u8; 32]']
)
```

#### Return value
```python
{'ctype_hash': '[u8; 32]'}
```
---------
### DelegationNodes
 Delegation nodes stored on chain.

 It maps from a node ID to the node details.

#### Python
```python
result = substrate.query(
    'Delegation', 'DelegationNodes', ['[u8; 32]']
)
```

#### Return value
```python
{
    'children': 'scale_info::405',
    'deposit': {'amount': 'u128', 'owner': 'AccountId'},
    'details': {'owner': 'AccountId', 'permissions': {'bits': 'u32'}, 'revoked': 'bool'},
    'hierarchy_root_id': '[u8; 32]',
    'parent': (None, '[u8; 32]'),
}
```
---------
## Constants

---------
### Deposit
 The deposit that is required for storing a delegation.
#### Value
```python
1000000000000000
```
#### Python
```python
constant = substrate.get_constant('Delegation', 'Deposit')
```
---------
### MaxChildren
 Maximum number of all children for a delegation node. For a binary
 tree, this should be twice the maximum depth of the tree, i.e.
 `2 ^ MaxParentChecks`.
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('Delegation', 'MaxChildren')
```
---------
### MaxParentChecks
 Maximum number of upwards traversals of the delegation tree from a
 node to the root and thus the depth of the delegation tree.
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Delegation', 'MaxParentChecks')
```
---------
### MaxRemovals
 Maximum number of removals. Should be same as MaxRevocations
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Delegation', 'MaxRemovals')
```
---------
### MaxRevocations
 Maximum number of revocations.
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Delegation', 'MaxRevocations')
```
---------
### MaxSignatureByteLength
#### Value
```python
64
```
#### Python
```python
constant = substrate.get_constant('Delegation', 'MaxSignatureByteLength')
```
---------
## Errors

---------
### AccessDenied
The operation wasn&\#x27;t allowed because of insufficient rights.

---------
### DelegateNotFound
No delegate with the given ID stored on chain.

---------
### DelegationAlreadyExists
There is already a delegation node with the same ID stored on chain.

---------
### DelegationNotFound
No delegation with the given ID stored on chain.

---------
### ExceededRemovalBounds
Max number of removals for delegation nodes has been reached for the
operation.

---------
### ExceededRevocationBounds
Max number of revocations for delegation nodes has been reached for
the operation.

---------
### HierarchyAlreadyExists
There is already a hierarchy with the same ID stored on chain.

---------
### HierarchyNotFound
No hierarchy with the given ID stored on chain.

---------
### InternalError
An error that is not supposed to take place, yet it happened.

---------
### InvalidDelegateSignature
The delegate&\#x27;s signature for the delegation creation operation is
invalid.

---------
### MaxChildrenExceeded
The max number of all children has been reached for the
corresponding delegation node.

---------
### MaxParentChecksTooLarge
The max number of parent checks exceeds the limit for the pallet.

---------
### MaxRemovalsTooLarge
The max number of removals exceeds the limit for the pallet.

---------
### MaxRevocationsTooLarge
The max number of revocation exceeds the limit for the pallet.

---------
### MaxSearchDepthReached
Max number of nodes checked without verifying the given condition.

---------
### NotOwnerOfDelegationHierarchy
The delegation creator is not allowed to write the delegation
because they are not the owner of the delegation root node.

---------
### NotOwnerOfParentDelegation
The delegation creator is not allowed to write the delegation
because they are not the owner of the delegation parent node.

---------
### ParentDelegationNotFound
No parent delegation with the given ID stored on chain.

---------
### ParentDelegationRevoked
The parent delegation has previously been revoked.

---------
### UnauthorizedDelegation
The delegation creator is not allowed to create the delegation.

---------
### UnauthorizedRemoval
The call origin is not authorized to remove the delegation.

---------
### UnauthorizedRevocation
The delegation revoker is not allowed to revoke the delegation.

---------