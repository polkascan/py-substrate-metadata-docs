
# ChainBridge

---------
## Calls

---------
### acknowledge_proposal
Commits a vote in favour of the provided proposal.

If a proposal with the given nonce and source chain ID does not already exist,
it will be created with an initial vote in favour from the caller.

\# &lt;weight&gt;
- weight of proposed call, regardless of whether execution is performed
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| nonce | `u64` | 
| src_id | `u8` | 
| r_id | `[u8; 32]` | 
| call | `Box<<T as Config>::Proposal>` | 

#### Python
```python
call = substrate.compose_call(
    'ChainBridge', 'acknowledge_proposal', {
    'call': 'Call',
    'nonce': 'u64',
    'r_id': '[u8; 32]',
    'src_id': 'u8',
}
)
```

---------
### add_relayer
Adds a new relayer to the relayer set.

\# &lt;weight&gt;
- O(1) lookup and removal
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| v | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'ChainBridge', 'add_relayer', {'v': 'AccountId'}
)
```

---------
### eval_vote_state
Evaluate the state of a proposal given the current vote threshold.

A proposal with enough votes will be either executed or cancelled, and the status
will be updated accordingly.

\# &lt;weight&gt;
- weight of proposed call, regardless of whether execution is performed
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| nonce | `u64` | 
| src_id | `u8` | 
| prop | `Box<<T as Config>::Proposal>` | 

#### Python
```python
call = substrate.compose_call(
    'ChainBridge', 'eval_vote_state', {
    'nonce': 'u64',
    'prop': 'Call',
    'src_id': 'u8',
}
)
```

---------
### reject_proposal
Commits a vote against a provided proposal.

\# &lt;weight&gt;
- Fixed, since execution of proposal should not be included
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| nonce | `u64` | 
| src_id | `u8` | 
| r_id | `[u8; 32]` | 
| call | `Box<<T as Config>::Proposal>` | 

#### Python
```python
call = substrate.compose_call(
    'ChainBridge', 'reject_proposal', {
    'call': 'Call',
    'nonce': 'u64',
    'r_id': '[u8; 32]',
    'src_id': 'u8',
}
)
```

---------
### remove_relayer
Removes an existing relaye to the set.

\# &lt;weight&gt;
- O(1) lookup and removal
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| v | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'ChainBridge', 'remove_relayer', {'v': 'AccountId'}
)
```

---------
### remove_resource
Removes a resource ID from the resource mapping.

After this call, bridge transfers with the associated resource ID will
be rejected.

\# &lt;weight&gt;
- O(1) removeal
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `[u8; 32]` | 

#### Python
```python
call = substrate.compose_call(
    'ChainBridge', 'remove_resource', {'id': '[u8; 32]'}
)
```

---------
### set_resource
Stores a method name on chain under an associated resource ID.

\# &lt;weight&gt;
- O(1) write
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `[u8; 32]` | 
| method | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'ChainBridge', 'set_resource', {'id': '[u8; 32]', 'method': 'Bytes'}
)
```

---------
### set_threshold
Sets the vote threshold for proposals.

This threshold is used to determine how many votes are required
before a proposal is executed.

\# &lt;weight&gt;
- O(1) lookup and insert
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| threshold | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ChainBridge', 'set_threshold', {'threshold': 'u32'}
)
```

---------
### whitelist_chain
Adds a new relayer to the relayer set.

\# &lt;weight&gt;
- O(1) lookup and insert
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'ChainBridge', 'whitelist_chain', {'id': 'u8'}
)
```

---------
## Events

---------
### ChainWhitelisted
Chain now available for transfers (chain_id)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u8` | ```u8```

---------
### FungibleTransfer
FunglibleTransfer is for relaying fungibles (dest_id, nonce, resource_id, amount, recipient, metadata)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u8` | ```u8```
| None | `u64` | ```u64```
| None | `ResourceId` | ```[u8; 32]```
| None | `U256` | ```[u64; 4]```
| None | `Vec<u8>` | ```Bytes```

---------
### GenericTransfer
GenericTransfer is for a generic data payload (dest_id, nonce, resource_id, metadata)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u8` | ```u8```
| None | `u64` | ```u64```
| None | `ResourceId` | ```[u8; 32]```
| None | `Vec<u8>` | ```Bytes```

---------
### NonFungibleTransfer
NonFungibleTransfer is for relaying NFTS (dest_id, nonce, resource_id, token_id, recipient, metadata)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u8` | ```u8```
| None | `u64` | ```u64```
| None | `ResourceId` | ```[u8; 32]```
| None | `Vec<u8>` | ```Bytes```
| None | `Vec<u8>` | ```Bytes```
| None | `Vec<u8>` | ```Bytes```

---------
### ProposalApproved
Voting successful for a proposal
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u8` | ```u8```
| None | `u64` | ```u64```

---------
### ProposalFailed
Execution of call failed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u8` | ```u8```
| None | `u64` | ```u64```

---------
### ProposalRejected
Voting rejected a proposal
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u8` | ```u8```
| None | `u64` | ```u64```

---------
### ProposalSucceeded
Execution of call succeeded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u8` | ```u8```
| None | `u64` | ```u64```

---------
### RelayerAdded
Relayer added to set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### RelayerRemoved
Relayer removed from set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### RelayerThresholdChanged
Vote threshold has changed (new_threshold)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
### VoteAgainst
Vot submitted against proposal
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u8` | ```u8```
| None | `u64` | ```u64```
| None | `T::AccountId` | ```AccountId```

---------
### VoteFor
Vote submitted in favour of proposal
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u8` | ```u8```
| None | `u64` | ```u64```
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### BridgeEvents
 All whitelisted chains and their respective transaction counts

#### Python
```python
result = substrate.query(
    'ChainBridge', 'BridgeEvents', []
)
```

#### Return value
```python
[
    {
        'FungibleTransfer': ('u8', 'u64', '[u8; 32]', '[u64; 4]', 'Bytes'),
        'GenericTransfer': ('u8', 'u64', '[u8; 32]', 'Bytes'),
        'NonFungibleTransfer': (
            'u8',
            'u64',
            '[u8; 32]',
            'Bytes',
            'Bytes',
            'Bytes',
        ),
    },
]
```
---------
### ChainNonces
 All whitelisted chains and their respective transaction counts

#### Python
```python
result = substrate.query(
    'ChainBridge', 'ChainNonces', ['u8']
)
```

#### Return value
```python
(None, 'u64')
```
---------
### RelayerCount

#### Python
```python
result = substrate.query(
    'ChainBridge', 'RelayerCount', []
)
```

#### Return value
```python
'u32'
```
---------
### RelayerThreshold
 Number of votes required for a proposal to execute

#### Python
```python
result = substrate.query(
    'ChainBridge', 'RelayerThreshold', []
)
```

#### Return value
```python
'u32'
```
---------
### Relayers
 Tracks current relayer set

#### Python
```python
result = substrate.query(
    'ChainBridge', 'Relayers', ['AccountId']
)
```

#### Return value
```python
()
```
---------
### Resources
 Utilized by the bridge software to map resource IDs to actual methods

#### Python
```python
result = substrate.query(
    'ChainBridge', 'Resources', ['[u8; 32]']
)
```

#### Return value
```python
'Bytes'
```
---------
### Votes
 All known proposals.
 The key is the hash of the call and the deposit ID, to ensure it&#x27;s unique.

#### Python
```python
result = substrate.query(
    'ChainBridge', 'Votes', ['u8', ('u64', 'Call')]
)
```

#### Return value
```python
{
    'expiry': 'u32',
    'status': ('Initiated', 'Approved', 'Rejected'),
    'votes_against': ['AccountId'],
    'votes_for': ['AccountId'],
}
```
---------
## Constants

---------
### BridgeChainId
 The identifier for this chain.
 This must be unique and must not collide with existing IDs within a set of bridged
 chains.
#### Value
```python
3
```
#### Python
```python
constant = substrate.get_constant('ChainBridge', 'BridgeChainId')
```
---------
### PalletId
 Constant configuration parameter to store the module identifier for the pallet.

 The module identifier may be of the form ```PalletId(*b&quot;chnbrdge&quot;)``` and set
 using the [`parameter_types`](https://substrate.dev/docs/en/knowledgebase/runtime/macros\#parameter_types)
#### Value
```python
'0x6372636c61696d73'
```
#### Python
```python
constant = substrate.get_constant('ChainBridge', 'PalletId')
```
---------
### ProposalLifetime
#### Value
```python
50400
```
#### Python
```python
constant = substrate.get_constant('ChainBridge', 'ProposalLifetime')
```
---------
## Errors

---------
### ChainAlreadyWhitelisted
Chain has already been enabled

---------
### ChainNotWhitelisted
Interactions with this chain is not permitted

---------
### InvalidChainId
Provided chain Id is not valid

---------
### InvalidThreshold
Relayer threshold cannot be 0

---------
### MustBeRelayer
Protected operation, must be performed by relayer

---------
### ProposalAlreadyComplete
Proposal has either failed or succeeded

---------
### ProposalAlreadyExists
A proposal with these parameters has already been submitted

---------
### ProposalDoesNotExist
No proposal with the ID was found

---------
### ProposalExpired
Lifetime of proposal has been exceeded

---------
### ProposalNotComplete
Cannot complete proposal, needs more votes

---------
### RelayerAlreadyExists
Relayer already in set

---------
### RelayerAlreadyVoted
Relayer has already submitted some vote for this proposal

---------
### RelayerInvalid
Provided accountId is not a relayer

---------
### ResourceDoesNotExist
Resource ID provided isn&\#x27;t mapped to anything

---------
### ThresholdNotSet
Relayer threshold not set

---------