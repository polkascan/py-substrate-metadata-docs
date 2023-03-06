
# ExternalAgents

---------
## Calls

---------
### abdicate
Abdicate agentship for `ticker`.

\# Arguments
- `ticker` of which the caller is an agent.

\# Errors
- `NotAnAgent` if the caller is not an agent of `ticker`.
- `RemovingLastFullAgent` if the caller is the last full agent.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 

#### Python
```python
call = substrate.compose_call(
    'ExternalAgents', 'abdicate', {'ticker': '[u8; 12]'}
)
```

---------
### accept_become_agent
Accept an authorization by an agent &quot;Alice&quot; who issued `auth_id`
to also become an agent of the ticker Alice specified.

\# Arguments
- `auth_id` identifying the authorization to accept.

\# Errors
- `AuthorizationError::Invalid` if `auth_id` does not exist for the given caller.
- `AuthorizationError::Expired` if `auth_id` is for an auth that has expired.
- `AuthorizationError::BadType` if `auth_id` was not for a `BecomeAgent` auth type.
- `UnauthorizedAgent` if &quot;Alice&quot; is not permissioned to provide the auth.
- `NoSuchAG` if the group referred to a custom that does not exist.
- `AlreadyAnAgent` if the caller is already an agent of the ticker.

\# Permissions
* Agent
#### Attributes
| Name | Type |
| -------- | -------- | 
| auth_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'ExternalAgents', 'accept_become_agent', {'auth_id': 'u64'}
)
```

---------
### change_group
Change the agent group that `agent` belongs to in `ticker`.

\# Arguments
- `ticker` that has the `agent`.
- `agent` of `ticker` to change the group for.
- `group` that `agent` will belong to in `ticker`.

\# Errors
- `UnauthorizedAgent` if `origin` was not authorized as an agent to call this.
- `NoSuchAG` if `id` does not identify a custom AG.
- `NotAnAgent` if `agent` is not an agent of `ticker`.
- `RemovingLastFullAgent` if `agent` was a `Full` one and is being demoted.

\# Permissions
* Asset
* Agent
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| agent | `IdentityId` | 
| group | `AgentGroup` | 

#### Python
```python
call = substrate.compose_call(
    'ExternalAgents', 'change_group', {
    'agent': '[u8; 32]',
    'group': {
        'Custom': 'u32',
        'ExceptMeta': None,
        'Full': None,
        'PolymeshV1CAA': None,
        'PolymeshV1PIA': None,
    },
    'ticker': '[u8; 12]',
}
)
```

---------
### create_and_change_custom_group
Utility extrinsic to batch `create_group` and  `change_group` for custom groups only.

\# Permissions
* Asset
* Agent
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| perms | `ExtrinsicPermissions` | 
| agent | `IdentityId` | 

#### Python
```python
call = substrate.compose_call(
    'ExternalAgents', 'create_and_change_custom_group', {
    'agent': '[u8; 32]',
    'perms': {
        'Except': 'scale_info::50',
        'These': 'scale_info::50',
        'Whole': None,
    },
    'ticker': '[u8; 12]',
}
)
```

---------
### create_group
Creates a custom agent group (AG) for the given `ticker`.

The AG will have the permissions as given by `perms`.
This new AG is then assigned `id = AGIdSequence::get() + 1` as its `AGId`,
which you can use as `AgentGroup::Custom(id)` when adding agents for `ticker`.

\# Arguments
- `ticker` to add the custom group for.
- `perms` that the new AG will have.

\# Errors
- `UnauthorizedAgent` if `origin` was not authorized as an agent to call this.
- `TooLong` if `perms` had some string or list length that was too long.
- `CounterOverflow` if `AGIdSequence::get() + 1` would exceed `u32::MAX`.

\# Permissions
* Asset
* Agent
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| perms | `ExtrinsicPermissions` | 

#### Python
```python
call = substrate.compose_call(
    'ExternalAgents', 'create_group', {
    'perms': {
        'Except': 'scale_info::50',
        'These': 'scale_info::50',
        'Whole': None,
    },
    'ticker': '[u8; 12]',
}
)
```

---------
### create_group_and_add_auth
Utility extrinsic to batch `create_group` and  `add_auth`.

\# Permissions
* Asset
* Agent
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| perms | `ExtrinsicPermissions` | 
| target | `IdentityId` | 
| expiry | `Option<T::Moment>` | 

#### Python
```python
call = substrate.compose_call(
    'ExternalAgents', 'create_group_and_add_auth', {
    'expiry': (None, 'u64'),
    'perms': {
        'Except': 'scale_info::50',
        'These': 'scale_info::50',
        'Whole': None,
    },
    'target': '[u8; 32]',
    'ticker': '[u8; 12]',
}
)
```

---------
### remove_agent
Remove the given `agent` from `ticker`.

\# Arguments
- `ticker` that has the `agent` to remove.
- `agent` of `ticker` to remove.

\# Errors
- `UnauthorizedAgent` if `origin` was not authorized as an agent to call this.
- `NotAnAgent` if `agent` is not an agent of `ticker`.
- `RemovingLastFullAgent` if `agent` is the last full one.

\# Permissions
* Asset
* Agent
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| agent | `IdentityId` | 

#### Python
```python
call = substrate.compose_call(
    'ExternalAgents', 'remove_agent', {
    'agent': '[u8; 32]',
    'ticker': '[u8; 12]',
}
)
```

---------
### set_group_permissions
Updates the permissions of the custom AG identified by `id`, for the given `ticker`.

\# Arguments
- `ticker` the custom AG belongs to.
- `id` for the custom AG within `ticker`.
- `perms` to update the custom AG to.

\# Errors
- `UnauthorizedAgent` if `origin` was not authorized as an agent to call this.
- `TooLong` if `perms` had some string or list length that was too long.
- `NoSuchAG` if `id` does not identify a custom AG.

\# Permissions
* Asset
* Agent
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| id | `AGId` | 
| perms | `ExtrinsicPermissions` | 

#### Python
```python
call = substrate.compose_call(
    'ExternalAgents', 'set_group_permissions', {
    'id': 'u32',
    'perms': {
        'Except': 'scale_info::50',
        'These': 'scale_info::50',
        'Whole': None,
    },
    'ticker': '[u8; 12]',
}
)
```

---------
## Events

---------
### AgentAdded
An agent was added.

(Caller/Agent DID, Agent&\#x27;s ticker, Agent&\#x27;s group)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventDid` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `AgentGroup` | ```{'Full': None, 'Custom': 'u32', 'ExceptMeta': None, 'PolymeshV1CAA': None, 'PolymeshV1PIA': None}```

---------
### AgentRemoved
An agent was removed.

(Caller DID, Agent&\#x27;s ticker, Agent&\#x27;s DID)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventDid` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `IdentityId` | ```[u8; 32]```

---------
### GroupChanged
An agent&\#x27;s group was changed.

(Caller DID, Agent&\#x27;s ticker, Agent&\#x27;s DID, The new group of the agent)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventDid` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `IdentityId` | ```[u8; 32]```
| None | `AgentGroup` | ```{'Full': None, 'Custom': 'u32', 'ExceptMeta': None, 'PolymeshV1CAA': None, 'PolymeshV1PIA': None}```

---------
### GroupCreated
An Agent Group was created.

(Caller DID, AG&\#x27;s ticker, AG&\#x27;s ID, AG&\#x27;s permissions)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventDid` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `AGId` | ```u32```
| None | `ExtrinsicPermissions` | ```{'Whole': None, 'These': 'scale_info::50', 'Except': 'scale_info::50'}```

---------
### GroupPermissionsUpdated
An Agent Group&\#x27;s permissions was updated.

(Caller DID, AG&\#x27;s ticker, AG&\#x27;s ID, AG&\#x27;s new permissions)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventDid` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `AGId` | ```u32```
| None | `ExtrinsicPermissions` | ```{'Whole': None, 'These': 'scale_info::50', 'Except': 'scale_info::50'}```

---------
## Storage functions

---------
### AGIdSequence
 The next per-`Ticker` AG ID in the sequence.

 The full ID is defined as a combination of `Ticker` and a number in this sequence,
 which starts from 1, rather than 0.

#### Python
```python
result = substrate.query(
    'ExternalAgents', 'AGIdSequence', ['[u8; 12]']
)
```

#### Return value
```python
'u32'
```
---------
### AgentOf
 Maps an agent (`IdentityId`) to all all `Ticker`s they belong to, if any.

#### Python
```python
result = substrate.query(
    'ExternalAgents', 'AgentOf', ['[u8; 32]', '[u8; 12]']
)
```

#### Return value
```python
()
```
---------
### GroupOfAgent
 Maps agents (`IdentityId`) for a `Ticker` to what AG they belong to, if any.

#### Python
```python
result = substrate.query(
    'ExternalAgents', 'GroupOfAgent', ['[u8; 12]', '[u8; 32]']
)
```

#### Return value
```python
{
    'Custom': 'u32',
    'ExceptMeta': None,
    'Full': None,
    'PolymeshV1CAA': None,
    'PolymeshV1PIA': None,
}
```
---------
### GroupPermissions
 For custom AGs of a `Ticker`, maps to what permissions an agent in that AG would have.

#### Python
```python
result = substrate.query(
    'ExternalAgents', 'GroupPermissions', ['[u8; 12]', 'u32']
)
```

#### Return value
```python
{'Except': 'scale_info::50', 'These': 'scale_info::50', 'Whole': None}
```
---------
### NumFullAgents
 Maps a `Ticker` to the number of `Full` agents for it.

#### Python
```python
result = substrate.query(
    'ExternalAgents', 'NumFullAgents', ['[u8; 12]']
)
```

#### Return value
```python
'u32'
```
---------
## Errors

---------
### AlreadyAnAgent
The provided `agent` is already an agent for the `Ticker`.

---------
### NoSuchAG
An AG with the given `AGId` did not exist for the `Ticker`.

---------
### NotAnAgent
The provided `agent` is not an agent for the `Ticker`.

---------
### RemovingLastFullAgent
This agent is the last full one, and it&\#x27;s being removed,
making the asset orphaned.

---------
### SecondaryKeyNotAuthorizedForAsset
The caller&\#x27;s secondary key does not have the required asset permission.

---------
### UnauthorizedAgent
The agent is not authorized to call the current extrinsic.

---------