
# Anchor

---------
## Calls

---------
### commit
Commits a `document_root` of a merklized off chain document in Centrifuge p2p network as
the latest version id(`anchor_id`) obtained by hashing `anchor_id_preimage`.
If a pre-commit exists for the obtained `anchor_id`, hash of pre-committed
`signing_root + proof` must match the given `doc_root`.
Any pre-committed data is automatically removed on a succesful commit and the reserved
funds from [`Pallet::pre_commit()`] are returned to the same account.
To avoid state bloat on chain,
the committed anchor would be evicted after the given `stored_until_date`.
The calling account would be charged accordingly for the storage period.
For a more detailed explanation refer section 3.4 of
[Centrifuge Protocol Paper](https://staticw.centrifuge.io/assets/centrifuge_os_protocol_paper.pdf)
#### Attributes
| Name | Type |
| -------- | -------- | 
| anchor_id_preimage | `T::Hash` | 
| doc_root | `T::Hash` | 
| proof | `T::Hash` | 
| stored_until_date | `T::Moment` | 

#### Python
```python
call = substrate.compose_call(
    'Anchor', 'commit', {
    'anchor_id_preimage': '[u8; 32]',
    'doc_root': '[u8; 32]',
    'proof': '[u8; 32]',
    'stored_until_date': 'u64',
}
)
```

---------
### evict_anchors
Initiates eviction of expired anchors. Since anchors are stored on a child trie indexed by
their eviction date, what this function does is to remove those child tries which has
date_represented_by_root &lt; current_date. Additionally it needs to take care of indexes
created for accessing anchors, eg: to find an anchor given an id.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Anchor', 'evict_anchors', {}
)
```

---------
### evict_pre_commits
Initiates eviction of pre-commits that has expired given a list on anchor ids.
For each evicted pre-commits, the deposit holded by [`Pallet::pre_commit()`] call
will be returned to the same account that made it originally.
#### Attributes
| Name | Type |
| -------- | -------- | 
| anchor_ids | `BoundedVec<T::Hash, ConstU32<EVICT_PRE_COMMIT_LIST_SIZE>>` | 

#### Python
```python
call = substrate.compose_call(
    'Anchor', 'evict_pre_commits', {'anchor_ids': ['[u8; 32]']}
)
```

---------
### pre_commit
Obtains an exclusive lock to make the next update to a certain document version
identified by `anchor_id` on Centrifuge p2p network for a number of blocks given
by [`PRE_COMMIT_EXPIRATION_DURATION_BLOCKS`] value. `signing_root` is a child node of
the off-chain merkle tree of that document. In Centrifuge protocol, a document is
committed only after reaching consensus with the other collaborators on the document.
Consensus is reached by getting a cryptographic signature from other parties by
sending them the `signing_root`. To deny the counter-party the free option of publishing
its own state commitment upon receiving a request for signature, the node can first
publish a pre-commit. Only the pre-committer account in the Centrifuge chain is
allowed to `commit` a corresponding anchor before the pre-commit has expired.
Some funds are reserved on a succesful pre-commit call.
These funds are returned to the same account after a succesful [`Pallet::commit()`] call
or explicitely if evicting the pre-commits by calling [`Pallet::evict_pre_commits()`].
For a more detailed explanation refer section 3.4 of
[Centrifuge Protocol Paper](https://staticw.centrifuge.io/assets/centrifuge_os_protocol_paper.pdf)
#### Attributes
| Name | Type |
| -------- | -------- | 
| anchor_id | `T::Hash` | 
| signing_root | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Anchor', 'pre_commit', {
    'anchor_id': '[u8; 32]',
    'signing_root': '[u8; 32]',
}
)
```

---------
## Storage functions

---------
### AnchorEvictDates
 Map to find the eviction date given an anchor id

#### Python
```python
result = substrate.query(
    'Anchor', 'AnchorEvictDates', ['[u8; 32]']
)
```

#### Return value
```python
'u32'
```
---------
### AnchorIndexes
 Map to find anchorID by index

#### Python
```python
result = substrate.query(
    'Anchor', 'AnchorIndexes', ['u64']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### EvictedAnchorRoots
 Storage for evicted anchor child trie roots. Anchors with a given expiry/eviction date
 are stored on-chain in a single child trie. This child trie is removed after the expiry
 date has passed while its root is stored permanently for proving an existence of an
 evicted anchor.

#### Python
```python
result = substrate.query(
    'Anchor', 'EvictedAnchorRoots', ['u32']
)
```

#### Return value
```python
'Bytes'
```
---------
### LatestAnchorIndex
 Latest anchored index that was recently used

#### Python
```python
result = substrate.query(
    'Anchor', 'LatestAnchorIndex', []
)
```

#### Return value
```python
'u64'
```
---------
### LatestEvictedAnchorIndex
 Latest evicted anchor index. This would keep track of the latest evicted anchor index so
 that we can start the removal of AnchorEvictDates index from that index onwards. Going
 from AnchorIndexes =&gt; AnchorEvictDates

#### Python
```python
result = substrate.query(
    'Anchor', 'LatestEvictedAnchorIndex', []
)
```

#### Return value
```python
'u64'
```
---------
### LatestEvictedDate
 This is to keep track of the date when a child trie of anchors was evicted last. It is
 to evict historic anchor data child tries if they weren&#x27;t evicted in a timely manner.

#### Python
```python
result = substrate.query(
    'Anchor', 'LatestEvictedDate', []
)
```

#### Return value
```python
'u32'
```
---------
### PreCommits
 PreCommits store the map of anchor Id to the pre-commit, which is a lock on an anchor id to be committed later

#### Python
```python
result = substrate.query(
    'Anchor', 'PreCommits', ['[u8; 32]']
)
```

#### Return value
```python
{
    'deposit': 'u128',
    'expiration_block': 'u32',
    'identity': 'AccountId',
    'signing_root': '[u8; 32]',
}
```
---------
## Errors

---------
### AnchorAlreadyExists
Anchor with anchor_id already exists

---------
### AnchorStoreDateAboveMaxLimit
Anchor store date must not be more than max store date

---------
### AnchorStoreDateInPast
Anchor store date must be in now or future

---------
### EvictionDateTooBig
Eviction date too big for conversion

---------
### FailedToConvertEpochToDays
Failed to convert epoch in MS to days

---------
### InvalidPreCommitProof
Invalid pre commit proof

---------
### NotOwnerOfPreCommit
Sender is not the owner of pre commit

---------
### PreCommitAlreadyExists
Pre-commit already exists

---------