
# CrowdloanClaim

---------
## Calls

---------
### claim_reward
Claim for a reward payout
#### Attributes
| Name | Type |
| -------- | -------- | 
| relaychain_account_id | `T::RelayChainAccountId` | 
| parachain_account_id | `ParachainAccountIdOf<T>` | 
| identity_proof | `MultiSignature` | 
| contribution_proof | `Proof<T::Hash>` | 
| contribution | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanClaim', 'claim_reward', {
    'contribution': 'u128',
    'contribution_proof': {
        'leaf_hash': 'scale_info::12',
        'sorted_hashes': [
            'scale_info::12',
        ],
    },
    'identity_proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
    'parachain_account_id': 'AccountId',
    'relaychain_account_id': 'AccountId',
}
)
```

---------
### initialize
Initialize the claim pallet

This administrative function is used to transfer the list of
contributors and their respective contributions, stored as a child
trie root hash in the relay chain&\#x27;s [`crowdloan`](https://github.com/paritytech/polkadot/blob/rococo-v1/runtime/common/src/crowdloan.rs)
pallet, to `Contributions` storage item.
This transaction can only be called via a signed transactions.
The `contributions` parameter contains the hash of the crowdloan
pallet&\#x27;s child trie root. It is later used for proving that a
contributor effectively contributed to the crowdloan campaign, and
that the amount of the contribution is correct as well.
#### Attributes
| Name | Type |
| -------- | -------- | 
| contributions | `RootHashOf<T>` | 
| locked_at | `T::BlockNumber` | 
| index | `TrieIndex` | 
| lease_start | `T::BlockNumber` | 
| lease_period | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanClaim', 'initialize', {
    'contributions': 'scale_info::12',
    'index': 'u32',
    'lease_period': 'u32',
    'lease_start': 'u32',
    'locked_at': 'u32',
}
)
```

---------
### set_contributions_root
Set the root-hash of the relay-chain, we locked the relay-chain
contributions at.

This root-hash MUST be the root-hash of the relay-chain at the block
we locked at. This root-hash will be used to verify proofs of
contribution.
#### Attributes
| Name | Type |
| -------- | -------- | 
| root | `RootHashOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanClaim', 'set_contributions_root', {'root': 'scale_info::12'}
)
```

---------
### set_crowdloan_trie_index
Set the index of the crowdloan.

This index comes from the relay-chain crowdloan pallet. More
specifically, this index is used to derive the internal patricia key
inside the child trie. The index is stored in the `FundInfo` of the
relay chain crowdloan pallet.
#### Attributes
| Name | Type |
| -------- | -------- | 
| trie_index | `TrieIndex` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanClaim', 'set_crowdloan_trie_index', {'trie_index': 'u32'}
)
```

---------
### set_lease_period
Set the lease period.
#### Attributes
| Name | Type |
| -------- | -------- | 
| period | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanClaim', 'set_lease_period', {'period': 'u32'}
)
```

---------
### set_lease_start
Set the start of the lease period.
#### Attributes
| Name | Type |
| -------- | -------- | 
| start | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanClaim', 'set_lease_start', {'start': 'u32'}
)
```

---------
### set_locked_at
Set the block of the relay at which we lock the contributions.

This means, that all generated proofs MUST generate the proof of
their contribution at this block, as otherwise the root-hash we
store here will not be found in the generated proof of the
contributor, which will lead to a rejection of the proof.
#### Attributes
| Name | Type |
| -------- | -------- | 
| locked_at | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'CrowdloanClaim', 'set_locked_at', {'locked_at': 'u32'}
)
```

---------
## Events

---------
### ClaimPalletInitialized
Event emitted when the crowdloan claim pallet is properly
configured.
#### Attributes
No attributes

---------
### ContributionsRootUpdated
Relay-chain Root hash which allows to verify contributions
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `RootHashOf<T>` | ```scale_info::12```

---------
### CrowdloanTrieIndexUpdated
Trie index of the crowdloan inside the relay-chains crowdloan child
storage
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TrieIndex` | ```u32```

---------
### LeasePeriodUpdated
The lease period of the parachain slot. Used to define when we can
initialize the next time
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```

---------
### LeaseStartUpdated
The lease start of the parachain slot. Used to define when we can
initialize the next time
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```

---------
### LockedAtUpdated
The block number, where we lock the contributions has been updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```

---------
### RewardClaimed
Event emitted when a reward has been claimed successfully.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::RelayChainAccountId` | ```AccountId```
| None | `ParachainAccountIdOf<T>` | ```AccountId```
| None | `T::Balance` | ```u128```

---------
## Storage functions

---------
### Contributions
 Root of hash of the relay chain at the time of initialization.

#### Python
```python
result = substrate.query(
    'CrowdloanClaim', 'Contributions', []
)
```

#### Return value
```python
'scale_info::12'
```
---------
### CrowdloanTrieIndex
 TrieIndex of the crowdloan campaign inside the relay-chain crowdloan
 pallet.

 This is needed in order to build the correct keys for proof check.

#### Python
```python
result = substrate.query(
    'CrowdloanClaim', 'CrowdloanTrieIndex', []
)
```

#### Return value
```python
'u32'
```
---------
### CurrIndex

#### Python
```python
result = substrate.query(
    'CrowdloanClaim', 'CurrIndex', []
)
```

#### Return value
```python
'u32'
```
---------
### LeasePeriod

#### Python
```python
result = substrate.query(
    'CrowdloanClaim', 'LeasePeriod', []
)
```

#### Return value
```python
'u32'
```
---------
### LeaseStart

#### Python
```python
result = substrate.query(
    'CrowdloanClaim', 'LeaseStart', []
)
```

#### Return value
```python
'u32'
```
---------
### LockedAt

#### Python
```python
result = substrate.query(
    'CrowdloanClaim', 'LockedAt', []
)
```

#### Return value
```python
'u32'
```
---------
### PrevIndex

#### Python
```python
result = substrate.query(
    'CrowdloanClaim', 'PrevIndex', []
)
```

#### Return value
```python
'u32'
```
---------
### ProcessedClaims
 A map containing the list of claims for reward payouts that were
 successfuly processed

#### Python
```python
result = substrate.query(
    'CrowdloanClaim', 'ProcessedClaims', [('AccountId', 'u32')]
)
```

#### Return value
```python
'bool'
```
---------
## Constants

---------
### PalletId
 Constant configuration parameter to store the pallet identifier for
 the pallet.

 The pallet identifier may be of the form
 ```PalletId(*b&quot;cc/claim&quot;)```.
#### Value
```python
'0x63632f636c61696d'
```
#### Python
```python
constant = substrate.get_constant('CrowdloanClaim', 'PalletId')
```
---------
## Errors

---------
### ClaimAlreadyProcessed
Claim has already been processed (replay attack, probably)

---------
### ClaimedAmountIsOutOfBoundaries
Claimed amount is out of boundaries (too low or too high)

---------
### InvalidClaimAmount
The reward amount that is claimed does not correspond to the one of
the contribution

---------
### InvalidContributorSignature
The signature provided by the contributor when registering is not
valid.

The consequence is that the relaychain and parachain accounts being
not associated, the contributor is not elligible for a reward
payout.

---------
### InvalidProofOfContribution
The proof of a contribution is invalid

---------
### MustBeAdministrator
Sensitive transactions can only be performed by administrator entity
(e.g. Sudo or Democracy pallet)

---------
### OngoingLease
A lease is ongoging and the pallet can henced not be initialized
again

---------
### OutOfLeasePeriod
Claiming rewards is only possible during a lease

---------
### PalletAlreadyInitialized
Cannot re-initialize the pallet

---------
### PalletNotInitialized
Cannot call reward before pallet is initialized

---------