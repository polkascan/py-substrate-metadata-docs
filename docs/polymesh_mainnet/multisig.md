
# MultiSig

---------
## Calls

---------
### accept_multisig_signer_as_identity
Accepts a multisig signer authorization given to signer&\#x27;s identity.

\# Arguments
* `auth_id` - Auth id of the authorization.
#### Attributes
| Name | Type |
| -------- | -------- | 
| auth_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'accept_multisig_signer_as_identity', {'auth_id': 'u64'}
)
```

---------
### accept_multisig_signer_as_key
Accepts a multisig signer authorization given to signer&\#x27;s key (AccountId).

\# Arguments
* `auth_id` - Auth id of the authorization.
#### Attributes
| Name | Type |
| -------- | -------- | 
| auth_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'accept_multisig_signer_as_key', {'auth_id': 'u64'}
)
```

---------
### add_multisig_signer
Adds a signer to the multisig. This must be called by the multisig itself.

\# Arguments
* `signer` - Signatory to add.
#### Attributes
| Name | Type |
| -------- | -------- | 
| signer | `Signatory<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'add_multisig_signer', {
    'signer': {
        'Account': 'AccountId',
        'Identity': '[u8; 32]',
    },
}
)
```

---------
### add_multisig_signers_via_creator
Adds a signer to the multisig. This must be called by the creator identity of the
multisig.

\# Arguments
* `multisig` - Address of the multi sig
* `signers` - Signatories to add.

\# Weight
`900_000_000 + 3_000_000 * signers.len()`
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| signers | `Vec<Signatory<T::AccountId>>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'add_multisig_signers_via_creator', {
    'multisig': 'AccountId',
    'signers': [
        {
            'Account': 'AccountId',
            'Identity': '[u8; 32]',
        },
    ],
}
)
```

---------
### approve_as_identity
Approves a multisig proposal using the caller&\#x27;s identity.

\# Arguments
* `multisig` - MultiSig address.
* `proposal_id` - Proposal id to approve.
If quorum is reached, the proposal will be immediately executed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| proposal_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'approve_as_identity', {
    'multisig': 'AccountId',
    'proposal_id': 'u64',
}
)
```

---------
### approve_as_key
Approves a multisig proposal using the caller&\#x27;s secondary key (`AccountId`).

\# Arguments
* `multisig` - MultiSig address.
* `proposal_id` - Proposal id to approve.
If quorum is reached, the proposal will be immediately executed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| proposal_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'approve_as_key', {
    'multisig': 'AccountId',
    'proposal_id': 'u64',
}
)
```

---------
### change_sigs_required
Changes the number of signatures required by a multisig. This must be called by the
multisig itself.

\# Arguments
* `sigs_required` - New number of required signatures.
#### Attributes
| Name | Type |
| -------- | -------- | 
| sigs_required | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'change_sigs_required', {'sigs_required': 'u64'}
)
```

---------
### create_multisig
Creates a multisig

\# Arguments
* `signers` - Signers of the multisig (They need to accept authorization before they are actually added).
* `sigs_required` - Number of sigs required to process a multi-sig tx.
#### Attributes
| Name | Type |
| -------- | -------- | 
| signers | `Vec<Signatory<T::AccountId>>` | 
| sigs_required | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'create_multisig', {
    'signers': [
        {
            'Account': 'AccountId',
            'Identity': '[u8; 32]',
        },
    ],
    'sigs_required': 'u64',
}
)
```

---------
### create_or_approve_proposal_as_identity
Creates a multisig proposal if it hasn&\#x27;t been created or approves it if it has.

\# Arguments
* `multisig` - MultiSig address.
* `proposal` - Proposal to be voted on.
* `expiry` - Optional proposal expiry time.
* `auto_close` - Close proposal on receiving enough reject votes.
If this is 1 out of `m` multisig, the proposal will be immediately executed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| proposal | `Box<T::Proposal>` | 
| expiry | `Option<T::Moment>` | 
| auto_close | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'create_or_approve_proposal_as_identity', {
    'auto_close': 'bool',
    'expiry': (None, 'u64'),
    'multisig': 'AccountId',
    'proposal': 'Call',
}
)
```

---------
### create_or_approve_proposal_as_key
Creates a multisig proposal if it hasn&\#x27;t been created or approves it if it has.

\# Arguments
* `multisig` - MultiSig address.
* `proposal` - Proposal to be voted on.
* `expiry` - Optional proposal expiry time.
* `auto_close` - Close proposal on receiving enough reject votes.
If this is 1 out of `m` multisig, the proposal will be immediately executed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| proposal | `Box<T::Proposal>` | 
| expiry | `Option<T::Moment>` | 
| auto_close | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'create_or_approve_proposal_as_key', {
    'auto_close': 'bool',
    'expiry': (None, 'u64'),
    'multisig': 'AccountId',
    'proposal': 'Call',
}
)
```

---------
### create_proposal_as_identity
Creates a multisig proposal

\# Arguments
* `multisig` - MultiSig address.
* `proposal` - Proposal to be voted on.
* `expiry` - Optional proposal expiry time.
* `auto_close` - Close proposal on receiving enough reject votes.
If this is 1 out of `m` multisig, the proposal will be immediately executed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| proposal | `Box<T::Proposal>` | 
| expiry | `Option<T::Moment>` | 
| auto_close | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'create_proposal_as_identity', {
    'auto_close': 'bool',
    'expiry': (None, 'u64'),
    'multisig': 'AccountId',
    'proposal': 'Call',
}
)
```

---------
### create_proposal_as_key
Creates a multisig proposal

\# Arguments
* `multisig` - MultiSig address.
* `proposal` - Proposal to be voted on.
* `expiry` - Optional proposal expiry time.
* `auto_close` - Close proposal on receiving enough reject votes.
If this is 1 out of `m` multisig, the proposal will be immediately executed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| proposal | `Box<T::Proposal>` | 
| expiry | `Option<T::Moment>` | 
| auto_close | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'create_proposal_as_key', {
    'auto_close': 'bool',
    'expiry': (None, 'u64'),
    'multisig': 'AccountId',
    'proposal': 'Call',
}
)
```

---------
### execute_scheduled_proposal
Root callable extrinsic, used as an internal call for executing scheduled multisig proposal.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| proposal_id | `u64` | 
| multisig_did | `IdentityId` | 
| _proposal_weight | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'execute_scheduled_proposal', {
    '_proposal_weight': 'u64',
    'multisig': 'AccountId',
    'multisig_did': '[u8; 32]',
    'proposal_id': 'u64',
}
)
```

---------
### make_multisig_primary
Adds a multisig as the primary key of the current did if the current DID is the creator
of the multisig.

\# Arguments
* `multi_sig` - multi sig address
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| optional_cdd_auth_id | `Option<u64>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'make_multisig_primary', {
    'multisig': 'AccountId',
    'optional_cdd_auth_id': (
        None,
        'u64',
    ),
}
)
```

---------
### make_multisig_secondary
Adds a multisig as a secondary key of current did if the current did is the creator of the
multisig.

\# Arguments
* `multisig` - multi sig address
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'make_multisig_secondary', {'multisig': 'AccountId'}
)
```

---------
### reject_as_identity
Rejects a multisig proposal using the caller&\#x27;s identity.

\# Arguments
* `multisig` - MultiSig address.
* `proposal_id` - Proposal id to reject.
If quorum is reached, the proposal will be immediately executed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| proposal_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'reject_as_identity', {
    'multisig': 'AccountId',
    'proposal_id': 'u64',
}
)
```

---------
### reject_as_key
Rejects a multisig proposal using the caller&\#x27;s secondary key (`AccountId`).

\# Arguments
* `multisig` - MultiSig address.
* `proposal_id` - Proposal id to reject.
If quorum is reached, the proposal will be immediately executed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| proposal_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'reject_as_key', {
    'multisig': 'AccountId',
    'proposal_id': 'u64',
}
)
```

---------
### remove_multisig_signer
Removes a signer from the multisig. This must be called by the multisig itself.

\# Arguments
* `signer` - Signatory to remove.
#### Attributes
| Name | Type |
| -------- | -------- | 
| signer | `Signatory<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'remove_multisig_signer', {
    'signer': {
        'Account': 'AccountId',
        'Identity': '[u8; 32]',
    },
}
)
```

---------
### remove_multisig_signers_via_creator
Removes a signer from the multisig.
This must be called by the creator identity of the multisig.

\# Arguments
* `multisig` - Address of the multisig.
* `signers` - Signatories to remove.

\# Weight
`900_000_000 + 3_000_000 * signers.len()`
#### Attributes
| Name | Type |
| -------- | -------- | 
| multisig | `T::AccountId` | 
| signers | `Vec<Signatory<T::AccountId>>` | 

#### Python
```python
call = substrate.compose_call(
    'MultiSig', 'remove_multisig_signers_via_creator', {
    'multisig': 'AccountId',
    'signers': [
        {
            'Account': 'AccountId',
            'Identity': '[u8; 32]',
        },
    ],
}
)
```

---------
## Events

---------
### MultiSigCreated
Event emitted after creation of a multisig.
Arguments: caller DID, multisig address, signers (pending approval), signatures required.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `AccountId` | ```AccountId```
| None | `Vec<Signatory<AccountId>>` | ```[{'Identity': '[u8; 32]', 'Account': 'AccountId'}]```
| None | `u64` | ```u64```

---------
### MultiSigSignaturesRequiredChanged
Event emitted when the number of required signatures is changed.
Arguments: caller DID, multisig, new required signatures.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `u64` | ```u64```

---------
### MultiSigSignerAdded
Event emitted when a signatory is added.
Arguments: caller DID, multisig, added signer.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Signatory<AccountId>` | ```{'Identity': '[u8; 32]', 'Account': 'AccountId'}```

---------
### MultiSigSignerAuthorized
Event emitted when a multisig signatory is authorized to be added.
Arguments: caller DID, multisig, authorized signer.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Signatory<AccountId>` | ```{'Identity': '[u8; 32]', 'Account': 'AccountId'}```

---------
### MultiSigSignerRemoved
Event emitted when a multisig signatory is removed.
Arguments: caller DID, multisig, removed signer.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Signatory<AccountId>` | ```{'Identity': '[u8; 32]', 'Account': 'AccountId'}```

---------
### ProposalAdded
Event emitted after adding a proposal.
Arguments: caller DID, multisig, proposal ID.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `u64` | ```u64```

---------
### ProposalApproved
Event emitted when the proposal get approved.
Arguments: caller DID, multisig, authorized signer, proposal id.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Signatory<AccountId>` | ```{'Identity': '[u8; 32]', 'Account': 'AccountId'}```
| None | `u64` | ```u64```

---------
### ProposalExecuted
Event emitted when a proposal is executed.
Arguments: caller DID, multisig, proposal ID, result.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `u64` | ```u64```
| None | `bool` | ```bool```

---------
### ProposalExecutionFailed
Event emitted when there&\#x27;s an error in proposal execution
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}```

---------
### ProposalRejected
Event emitted when a proposal is rejected.
Arguments: caller DID, multisig, proposal ID.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `u64` | ```u64```

---------
### ProposalRejectionVote
Event emitted when a vote is cast in favor of rejecting a proposal.
Arguments: caller DID, multisig, authorized signer, proposal id.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Signatory<AccountId>` | ```{'Identity': '[u8; 32]', 'Account': 'AccountId'}```
| None | `u64` | ```u64```

---------
### SchedulingFailed
Scheduling of proposal fails.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}```

---------
## Storage functions

---------
### MultiSigNonce
 Nonce to ensure unique MultiSig addresses are generated; starts from 1.

#### Python
```python
result = substrate.query(
    'MultiSig', 'MultiSigNonce', []
)
```

#### Return value
```python
'u64'
```
---------
### MultiSigSigners
 Signers of a multisig. (multisig, signer) =&gt; bool.

#### Python
```python
result = substrate.query(
    'MultiSig', 'MultiSigSigners', [
    'AccountId',
    {
        'Account': 'AccountId',
        'Identity': '[u8; 32]',
    },
]
)
```

#### Return value
```python
'bool'
```
---------
### MultiSigSignsRequired
 Confirmations required before processing a multisig tx.

#### Python
```python
result = substrate.query(
    'MultiSig', 'MultiSigSignsRequired', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### MultiSigToIdentity
 Maps a multisig account to its identity.

#### Python
```python
result = substrate.query(
    'MultiSig', 'MultiSigToIdentity', ['AccountId']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### MultiSigTxDone
 Number of transactions proposed in a multisig. Used as tx id; starts from 0.

#### Python
```python
result = substrate.query(
    'MultiSig', 'MultiSigTxDone', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### NumberOfSigners
 Number of approved/accepted signers of a multisig.

#### Python
```python
result = substrate.query(
    'MultiSig', 'NumberOfSigners', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### ProposalDetail
 Details of a multisig proposal

#### Python
```python
result = substrate.query(
    'MultiSig', 'ProposalDetail', [('AccountId', 'u64')]
)
```

#### Return value
```python
{
    'approvals': 'u64',
    'auto_close': 'bool',
    'expiry': (None, 'u64'),
    'rejections': 'u64',
    'status': (
        'Invalid',
        'ActiveOrExpired',
        'ExecutionSuccessful',
        'ExecutionFailed',
        'Rejected',
    ),
}
```
---------
### ProposalIds
 A mapping of proposals to their IDs.

#### Python
```python
result = substrate.query(
    'MultiSig', 'ProposalIds', ['AccountId', 'Call']
)
```

#### Return value
```python
'u64'
```
---------
### Proposals
 Proposals presented for voting to a multisig (multisig, proposal id) =&gt; Option&lt;T::Proposal&gt;.

#### Python
```python
result = substrate.query(
    'MultiSig', 'Proposals', [('AccountId', 'u64')]
)
```

#### Return value
```python
'Call'
```
---------
### StorageVersion
 Storage version.

#### Python
```python
result = substrate.query(
    'MultiSig', 'StorageVersion', []
)
```

#### Return value
```python
'u8'
```
---------
### TransactionVersion
 The last transaction version, used for `on_runtime_upgrade`.

#### Python
```python
result = substrate.query(
    'MultiSig', 'TransactionVersion', []
)
```

#### Return value
```python
'u32'
```
---------
### Votes
 Individual multisig signer votes. (multi sig, signer, proposal) =&gt; vote.

#### Python
```python
result = substrate.query(
    'MultiSig', 'Votes', [
    (
        'AccountId',
        {
            'Account': 'AccountId',
            'Identity': '[u8; 32]',
        },
        'u64',
    ),
]
)
```

#### Return value
```python
'bool'
```
---------
## Errors

---------
### AlreadyASigner
Already a signer.

---------
### AlreadyVoted
Already voted.

---------
### CddMissing
The multisig is not attached to a CDD&\#x27;d identity.

---------
### ChangeNotAllowed
Changing multisig parameters not allowed since multisig is a primary key.

---------
### DecodingError
Multisig address.

---------
### FailedToChargeFee
Couldn&\#x27;t charge fee for the transaction.

---------
### FailedToSchedule
Scheduling of a proposal fails

---------
### IdentityNotCreator
Identity provided is not the multisig&\#x27;s creator.

---------
### MissingCurrentIdentity
Current DID is missing

---------
### MultisigMissingIdentity
Multisig is not attached to an identity

---------
### MultisigNotAllowedToLinkToItself
Multisig not allowed to add itself as a signer.

---------
### NoSigners
No signers.

---------
### NoSuchMultisig
No such multisig.

---------
### NonceOverflow
A nonce overflow.

---------
### NotASigner
Not a signer.

---------
### NotEnoughSigners
Not enough signers.

---------
### NotPrimaryKey
The function can only be called by the primary key of the did

---------
### ProposalAlreadyExecuted
Proposal was executed earlier

---------
### ProposalAlreadyRejected
Proposal was rejected earlier

---------
### ProposalExpired
Proposal has expired

---------
### ProposalMissing
The proposal does not exist.

---------
### RequiredSignaturesOutOfBounds
Too few or too many required signatures.

---------
### SignerAlreadyLinkedToIdentity
Signer is an account key that is already associated with an identity.

---------
### SignerAlreadyLinkedToMultisig
Signer is an account key that is already associated with a multisig.

---------
### TooManySigners
More signers than required.

---------