
# ChainBridge

---------
## Calls

---------
### acknowledge_proposal
See [`Pallet::acknowledge_proposal`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| nonce | `DepositNonce` | 
| src_id | `BridgeChainId` | 
| r_id | `ResourceId` | 
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
See [`Pallet::add_relayer`].
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
See [`Pallet::eval_vote_state`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| nonce | `DepositNonce` | 
| src_id | `BridgeChainId` | 
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
### handle_fungible_transfer
See [`Pallet::handle_fungible_transfer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `Vec<u8>` | 
| amount | `BalanceOf<T>` | 
| rid | `ResourceId` | 

#### Python
```python
call = substrate.compose_call(
    'ChainBridge', 'handle_fungible_transfer', {
    'amount': 'u128',
    'dest': 'Bytes',
    'rid': '[u8; 32]',
}
)
```

---------
### reject_proposal
See [`Pallet::reject_proposal`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| nonce | `DepositNonce` | 
| src_id | `BridgeChainId` | 
| r_id | `ResourceId` | 
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
See [`Pallet::remove_relayer`].
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
### set_threshold
See [`Pallet::set_threshold`].
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
### update_fee
See [`Pallet::update_fee`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| fee | `u128` | 
| dest_id | `BridgeChainId` | 

#### Python
```python
call = substrate.compose_call(
    'ChainBridge', 'update_fee', {'dest_id': 'u8', 'fee': 'u128'}
)
```

---------
### whitelist_chain
See [`Pallet::whitelist_chain`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `BridgeChainId` | 

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
| None | `BridgeChainId` | ```u8```

---------
### FeeUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dest_id | `BridgeChainId` | ```u8```
| fee | `u128` | ```u128```

---------
### FungibleTransfer
FungibleTransfer is for relaying fungibles (dest_id, nonce, resource_id, amount, recipient)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BridgeChainId` | ```u8```
| None | `DepositNonce` | ```u64```
| None | `ResourceId` | ```[u8; 32]```
| None | `U256` | ```scale_info::131```
| None | `Vec<u8>` | ```Bytes```

---------
### GenericTransfer
GenericTransfer is for a generic data payload (dest_id, nonce, resource_id, metadata)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BridgeChainId` | ```u8```
| None | `DepositNonce` | ```u64```
| None | `ResourceId` | ```[u8; 32]```
| None | `Vec<u8>` | ```Bytes```

---------
### NonFungibleTransfer
NonFungibleTransfer is for relaying NFTs (dest_id, nonce, resource_id, token_id, recipient, metadata)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BridgeChainId` | ```u8```
| None | `DepositNonce` | ```u64```
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
| None | `BridgeChainId` | ```u8```
| None | `DepositNonce` | ```u64```

---------
### ProposalFailed
Execution of call failed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BridgeChainId` | ```u8```
| None | `DepositNonce` | ```u64```

---------
### ProposalRejected
Voting rejected a proposal
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BridgeChainId` | ```u8```
| None | `DepositNonce` | ```u64```

---------
### ProposalSucceeded
Execution of call succeeded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BridgeChainId` | ```u8```
| None | `DepositNonce` | ```u64```

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
| None | `BridgeChainId` | ```u8```
| None | `DepositNonce` | ```u64```
| None | `T::AccountId` | ```AccountId```

---------
### VoteFor
Vote submitted in favour of proposal
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BridgeChainId` | ```u8```
| None | `DepositNonce` | ```u64```
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### BridgeEvents

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
        'FungibleTransfer': (
            'u8',
            'u64',
            '[u8; 32]',
            'scale_info::131',
            'Bytes',
        ),
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
### BridgeFee

#### Python
```python
result = substrate.query(
    'ChainBridge', 'BridgeFee', ['u8']
)
```

#### Return value
```python
'u128'
```
---------
### ChainNonces

#### Python
```python
result = substrate.query(
    'ChainBridge', 'ChainNonces', ['u8']
)
```

#### Return value
```python
'u64'
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

#### Python
```python
result = substrate.query(
    'ChainBridge', 'Relayers', ['AccountId']
)
```

#### Return value
```python
'bool'
```
---------
### Votes

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
 This must be unique and must not collide with existing IDs within a set of bridged chains.
#### Value
```python
3
```
#### Python
```python
constant = substrate.get_constant('ChainBridge', 'BridgeChainId')
```
---------
### BridgeEventLimit
 Maximum number of bridge events  allowed to exist in a single block
#### Value
```python
1024
```
#### Python
```python
constant = substrate.get_constant('ChainBridge', 'BridgeEventLimit')
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
### ResourceIdGenerationSalt
 Salt used to generation rid
#### Value
```python
3
```
#### Python
```python
constant = substrate.get_constant('ChainBridge', 'ResourceIdGenerationSalt')
```
---------
## Errors

---------
### AssetConversionFailed
Convertion failed from resource id

---------
### AssetNotRegistered
Assets not registered through pallet-assets or pallet-uniques

---------
### BridgeEventOverflow
Trying to push bridge event count more than `BridgeEventLimit`

---------
### CannotDepositAsset
Can not transfer assets to dest due to some reasons

---------
### CannotDetermineReservedLocation
Can not extract asset reserve location

---------
### CannotPayAsFee
Asset can not pay as fee

---------
### ChainAlreadyWhitelisted
Chain has already been enabled

---------
### ChainNotWhitelisted
Interactions with this chain is not permitted

---------
### DestUnrecognized
Can not extract dest location

---------
### ExtractAssetFailed
Unkonwn asset

---------
### ExtractDestFailed
Unknown destnation

---------
### FeeTooExpensive
Too expensive fee for withdrawn asset

---------
### InsufficientBalance
Infusficient balance to withdraw

---------
### InvalidChainId
Provided chain Id is not valid

---------
### InvalidFeeOption
Got wrong paremeter when update fee

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
### TransactFailed
Transfer failed

---------
### Unimplemented
Function unimplemented

---------
### _ResourceDoesNotExist
Resource ID provided isn&\#x27;t mapped to anything

---------
### _ThresholdNotSet
Relayer threshold not set

---------