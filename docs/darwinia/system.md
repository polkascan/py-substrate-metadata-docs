
# System

---------
## Calls

---------
### fill_block
A dispatch that will fill the block weight up to the given ratio.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ratio | `Perbill` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'fill_block', {'ratio': 'u32'}
)
```

---------
### kill_prefix
Kill all storage items with a key that starts with the given prefix.

**NOTE:** We rely on the Root origin to provide us the number of subkeys under
the prefix we are removing to accurately calculate the weight of this function.
#### Attributes
| Name | Type |
| -------- | -------- | 
| prefix | `Key` | 
| subkeys | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'kill_prefix', {'prefix': 'Bytes', 'subkeys': 'u32'}
)
```

---------
### kill_storage
Kill some items from storage.
#### Attributes
| Name | Type |
| -------- | -------- | 
| keys | `Vec<Key>` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'kill_storage', {'keys': ['Bytes']}
)
```

---------
### remark
Make some on-chain remark.

\# &lt;weight&gt;
- `O(1)`
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| remark | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'remark', {'remark': 'Bytes'}
)
```

---------
### remark_with_event
Make some on-chain remark and emit event.

\# &lt;weight&gt;
- `O(b)` where b is the length of the remark.
- 1 event.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| remark | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'remark_with_event', {'remark': 'Bytes'}
)
```

---------
### set_code
Set the new runtime code.

\# &lt;weight&gt;
- `O(C + S)` where `C` length of `code` and `S` complexity of `can_set_code`
- 1 call to `can_set_code`: `O(S)` (calls `sp_io::misc::runtime_version` which is
  expensive).
- 1 storage write (codec `O(C)`).
- 1 digest item.
- 1 event.
The weight of this function is dependent on the runtime, but generally this is very
expensive. We will treat this as a full block.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| code | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'set_code', {'code': 'Bytes'}
)
```

---------
### set_code_without_checks
Set the new runtime code without doing any checks of the given `code`.

\# &lt;weight&gt;
- `O(C)` where `C` length of `code`
- 1 storage write (codec `O(C)`).
- 1 digest item.
- 1 event.
The weight of this function is dependent on the runtime. We will treat this as a full
block. \# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| code | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'set_code_without_checks', {'code': 'Bytes'}
)
```

---------
### set_heap_pages
Set the number of pages in the WebAssembly environment&\#x27;s heap.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pages | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'set_heap_pages', {'pages': 'u64'}
)
```

---------
### set_storage
Set some items of storage.
#### Attributes
| Name | Type |
| -------- | -------- | 
| items | `Vec<KeyValue>` | 

#### Python
```python
call = substrate.compose_call(
    'System', 'set_storage', {'items': [('Bytes', 'Bytes')]}
)
```

---------
## Events

---------
### CodeUpdated
`:code` was updated.
#### Attributes
No attributes

---------
### ExtrinsicFailed
An extrinsic failed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispatch_error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': 'u8'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero')}```
| dispatch_info | `DispatchInfo` | ```{'weight': 'u64', 'class': ('Normal', 'Operational', 'Mandatory'), 'pays_fee': ('Yes', 'No')}```

---------
### ExtrinsicSuccess
An extrinsic completed successfully.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| dispatch_info | `DispatchInfo` | ```{'weight': 'u64', 'class': ('Normal', 'Operational', 'Mandatory'), 'pays_fee': ('Yes', 'No')}```

---------
### KilledAccount
An account was reaped.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
### NewAccount
A new account was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
### Remarked
On on-chain remark happened.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| hash | `T::Hash` | ```[u8; 32]```

---------
## Storage functions

---------
### Account
 The full account information for a particular account ID.

#### Python
```python
result = substrate.query(
    'System', 'Account', ['AccountId']
)
```

#### Return value
```python
{
    'consumers': 'u32',
    'data': {
        'free': 'u128',
        'free_kton': 'u128',
        'reserved': 'u128',
        'reserved_kton': 'u128',
    },
    'nonce': 'u32',
    'providers': 'u32',
    'sufficients': 'u32',
}
```
---------
### AllExtrinsicsLen
 Total length (in bytes) for all extrinsics put together, for the current block.

#### Python
```python
result = substrate.query(
    'System', 'AllExtrinsicsLen', []
)
```

#### Return value
```python
'u32'
```
---------
### BlockHash
 Map of block numbers to block hashes.

#### Python
```python
result = substrate.query(
    'System', 'BlockHash', ['u32']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### BlockWeight
 The current weight for the block.

#### Python
```python
result = substrate.query(
    'System', 'BlockWeight', []
)
```

#### Return value
```python
{'mandatory': 'u64', 'normal': 'u64', 'operational': 'u64'}
```
---------
### Digest
 Digest of the current block, also part of the block header.

#### Python
```python
result = substrate.query(
    'System', 'Digest', []
)
```

#### Return value
```python
{
    'logs': [
        {
            'Other': 'Bytes',
            None: None,
            'Consensus': ('[u8; 4]', 'Bytes'),
            'PreRuntime': ('[u8; 4]', 'Bytes'),
            'RuntimeEnvironmentUpdated': None,
            'Seal': ('[u8; 4]', 'Bytes'),
        },
    ],
}
```
---------
### EventCount
 The number of events in the `Events&lt;T&gt;` list.

#### Python
```python
result = substrate.query(
    'System', 'EventCount', []
)
```

#### Return value
```python
'u32'
```
---------
### EventTopics
 Mapping between a topic (represented by T::Hash) and a vector of indexes
 of events in the `&lt;Events&lt;T&gt;&gt;` list.

 All topic vectors have deterministic storage locations depending on the topic. This
 allows light-clients to leverage the changes trie storage tracking mechanism and
 in case of changes fetch the list of events of interest.

 The value has the type `(T::BlockNumber, EventIndex)` because if we used only just
 the `EventIndex` then in case if the topic has the same contents on the next block
 no notification will be triggered thus the event might be lost.

#### Python
```python
result = substrate.query(
    'System', 'EventTopics', ['[u8; 32]']
)
```

#### Return value
```python
[('u32', 'u32')]
```
---------
### Events
 Events deposited for the current block.

 NOTE: This storage item is explicitly unbounded since it is never intended to be read
 from within the runtime.

#### Python
```python
result = substrate.query(
    'System', 'Events', []
)
```

#### Return value
```python
[
    {
        'event': {
            'Balances': {
                'BalanceSet': {
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Deposit': {'amount': 'u128', 'who': 'AccountId'},
                'DustLost': {'account': 'AccountId', 'amount': 'u128'},
                'Endowed': {'account': 'AccountId', 'free_balance': 'u128'},
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'destination_status': 'scale_info::26',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Reserved': {'amount': 'u128', 'who': 'AccountId'},
                'Slashed': {'amount': 'u128', 'who': 'AccountId'},
                'Transfer': {
                    'amount': 'u128',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unreserved': {'amount': 'u128', 'who': 'AccountId'},
                'Withdraw': {'amount': 'u128', 'who': 'AccountId'},
            },
            'BaseFee': {
                'BaseFeeOverflow': None,
                'IsActive': 'bool',
                'NewBaseFeePerGas': '[u64; 4]',
                'NewElasticity': 'u32',
            },
            'Bounties': {
                'BountyAwarded': {'beneficiary': 'AccountId', 'index': 'u32'},
                'BountyBecameActive': {'index': 'u32'},
                'BountyCanceled': {'index': 'u32'},
                'BountyClaimed': {
                    'beneficiary': 'AccountId',
                    'index': 'u32',
                    'payout': 'u128',
                },
                'BountyExtended': {'index': 'u32'},
                'BountyProposed': {'index': 'u32'},
                'BountyRejected': {'bond': 'u128', 'index': 'u32'},
            },
            'BridgeCrabDispatch': {
                'MessageCallDecodeFailed': ('[u8; 4]', ('[u8; 4]', 'u64')),
                'MessageCallValidateFailed': (
                    '[u8; 4]',
                    ('[u8; 4]', 'u64'),
                    'scale_info::116',
                ),
                'MessageDispatchPaymentFailed': (
                    '[u8; 4]',
                    ('[u8; 4]', 'u64'),
                    'AccountId',
                    'u64',
                ),
                'MessageDispatched': ('[u8; 4]', ('[u8; 4]', 'u64'), 'scale_info::63'),
                'MessageRejected': ('[u8; 4]', ('[u8; 4]', 'u64')),
                'MessageSignatureMismatch': ('[u8; 4]', ('[u8; 4]', 'u64')),
                'MessageVersionSpecMismatch': ('[u8; 4]', ('[u8; 4]', 'u64'), 'u32', 'u32'),
                'MessageWeightMismatch': ('[u8; 4]', ('[u8; 4]', 'u64'), 'u64', 'u64'),
                '_Dummy': None,
            },
            'BridgeCrabMessages': {
                'MessageAccepted': ('[u8; 4]', 'u64'),
                'MessagesDelivered': ('[u8; 4]', 'scale_info::111'),
                'ParameterUpdated': {'CrabToDarwiniaConversionRate': 'u128'},
            },
            'BridgeDarwiniaParachainDispatch': {
                'MessageCallDecodeFailed': ('[u8; 4]', ('[u8; 4]', 'u64')),
                'MessageCallValidateFailed': (
                    '[u8; 4]',
                    ('[u8; 4]', 'u64'),
                    'scale_info::116',
                ),
                'MessageDispatchPaymentFailed': (
                    '[u8; 4]',
                    ('[u8; 4]', 'u64'),
                    'AccountId',
                    'u64',
                ),
                'MessageDispatched': ('[u8; 4]', ('[u8; 4]', 'u64'), 'scale_info::63'),
                'MessageRejected': ('[u8; 4]', ('[u8; 4]', 'u64')),
                'MessageSignatureMismatch': ('[u8; 4]', ('[u8; 4]', 'u64')),
                'MessageVersionSpecMismatch': ('[u8; 4]', ('[u8; 4]', 'u64'), 'u32', 'u32'),
                'MessageWeightMismatch': ('[u8; 4]', ('[u8; 4]', 'u64'), 'u64', 'u64'),
                '_Dummy': None,
            },
            'BridgeDarwiniaParachainMessages': {
                'MessageAccepted': ('[u8; 4]', 'u64'),
                'MessagesDelivered': ('[u8; 4]', 'scale_info::111'),
                'ParameterUpdated': {
                    'DarwiniaParachainToDarwiniaConversionRate': 'u128',
                },
            },
            'Council': {
                'Approved': {'proposal_hash': '[u8; 32]'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': '[u8; 32]'},
                'Executed': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::63',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::63',
                },
                'Proposed': {
                    'account': 'AccountId',
                    'proposal_hash': '[u8; 32]',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'Voted': {
                    'account': 'AccountId',
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'voted': 'bool',
                    'yes': 'u32',
                },
            },
            'DarwiniaParachainFeeMarket': {
                'CancelEnrollment': 'AccountId',
                'Enroll': ('AccountId', 'u128', 'u128'),
                'FeeMarketSlash': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'confirm_time': (None, 'u32'),
                    'delay_time': (None, 'u32'),
                    'lane': '[u8; 4]',
                    'message': 'u64',
                    'sent_time': 'u32',
                },
                'OrderCreated': (
                    '[u8; 4]',
                    'u64',
                    'u128',
                    ['AccountId'],
                    (None, 'u32'),
                ),
                'OrderReward': ('[u8; 4]', 'u64', 'scale_info::124'),
                'UpdateAssignedRelayersNumber': 'u32',
                'UpdateCollateralSlashProtect': 'u128',
                'UpdateLockedCollateral': ('AccountId', 'u128'),
                'UpdateRelayFee': ('AccountId', 'u128'),
            },
            'Democracy': {
                'Blacklisted': {'proposal_hash': '[u8; 32]'},
                'Cancelled': {'ref_index': 'u32'},
                'Delegated': {'target': 'AccountId', 'who': 'AccountId'},
                'Executed': {'ref_index': 'u32', 'result': 'scale_info::63'},
                'ExternalTabled': None,
                'NotPassed': {'ref_index': 'u32'},
                'Passed': {'ref_index': 'u32'},
                'PreimageInvalid': {
                    'proposal_hash': '[u8; 32]',
                    'ref_index': 'u32',
                },
                'PreimageMissing': {
                    'proposal_hash': '[u8; 32]',
                    'ref_index': 'u32',
                },
                'PreimageNoted': {
                    'deposit': 'u128',
                    'proposal_hash': '[u8; 32]',
                    'who': 'AccountId',
                },
                'PreimageReaped': {
                    'deposit': 'u128',
                    'proposal_hash': '[u8; 32]',
                    'provider': 'AccountId',
                    'reaper': 'AccountId',
                },
                'PreimageUsed': {
                    'deposit': 'u128',
                    'proposal_hash': '[u8; 32]',
                    'provider': 'AccountId',
                },
                'Proposed': {'deposit': 'u128', 'proposal_index': 'u32'},
                'Seconded': {'prop_index': 'u32', 'seconder': 'AccountId'},
                'Started': {'ref_index': 'u32', 'threshold': 'scale_info::62'},
                'Tabled': {
                    'deposit': 'u128',
                    'depositors': ['AccountId'],
                    'proposal_index': 'u32',
                },
                'Undelegated': {'account': 'AccountId'},
                'Vetoed': {
                    'proposal_hash': '[u8; 32]',
                    'until': 'u32',
                    'who': 'AccountId',
                },
                'Voted': {
                    'ref_index': 'u32',
                    'vote': 'scale_info::65',
                    'voter': 'AccountId',
                },
            },
            'EVM': {
                'Created': {'address': '[u8; 20]'},
                'CreatedFailed': {'address': '[u8; 20]'},
                'Executed': {'address': '[u8; 20]'},
                'ExecutedFailed': {'address': '[u8; 20]'},
                'Log': {'log': 'scale_info::94'},
            },
            'EcdsaAuthority': {
                'CollectedEnoughAuthoritiesChangeSignatures': {
                    'message': '[u8; 32]',
                    'new_threshold': (None, 'u32'),
                    'operation': 'scale_info::51',
                    'signatures': [('[u8; 20]', '[u8; 65]')],
                },
                'CollectedEnoughNewMessageRootSignatures': {
                    'commitment': 'scale_info::59',
                    'message': '[u8; 32]',
                    'signatures': [('[u8; 20]', '[u8; 65]')],
                },
                'CollectingAuthoritiesChangeSignatures': {
                    'message': '[u8; 32]',
                },
                'CollectingNewMessageRootSignatures': {'message': '[u8; 32]'},
            },
            'ElectionProviderMultiPhase': {
                'ElectionFinalized': {
                    'election_compute': (None, 'scale_info::29'),
                },
                'Rewarded': {'account': 'AccountId', 'value': 'u128'},
                'SignedPhaseStarted': {'round': 'u32'},
                'Slashed': {'account': 'AccountId', 'value': 'u128'},
                'SolutionStored': {
                    'election_compute': 'scale_info::29',
                    'prev_ejected': 'bool',
                },
                'UnsignedPhaseStarted': {'round': 'u32'},
            },
            'Ethereum': {
                'DVMTransfer': {
                    'amount': '[u64; 4]',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Executed': {
                    'exit_reason': 'scale_info::97',
                    'from': '[u8; 20]',
                    'to': '[u8; 20]',
                    'transaction_hash': '[u8; 32]',
                },
                'KtonDVMTransfer': {
                    'amount': '[u64; 4]',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
            },
            'FeeMarket': {
                'CancelEnrollment': 'AccountId',
                'Enroll': ('AccountId', 'u128', 'u128'),
                'FeeMarketSlash': {
                    'account_id': 'AccountId',
                    'amount': 'u128',
                    'confirm_time': (None, 'u32'),
                    'delay_time': (None, 'u32'),
                    'lane': '[u8; 4]',
                    'message': 'u64',
                    'sent_time': 'u32',
                },
                'OrderCreated': (
                    '[u8; 4]',
                    'u64',
                    'u128',
                    ['AccountId'],
                    (None, 'u32'),
                ),
                'OrderReward': ('[u8; 4]', 'u64', 'scale_info::124'),
                'UpdateAssignedRelayersNumber': 'u32',
                'UpdateCollateralSlashProtect': 'u128',
                'UpdateLockedCollateral': ('AccountId', 'u128'),
                'UpdateRelayFee': ('AccountId', 'u128'),
            },
            'Grandpa': {
                'NewAuthorities': {'authority_set': [('[u8; 32]', 'u64')]},
                'Paused': None,
                'Resumed': None,
            },
            'Identity': {
                'IdentityCleared': {'deposit': 'u128', 'who': 'AccountId'},
                'IdentityKilled': {'deposit': 'u128', 'who': 'AccountId'},
                'IdentitySet': {'who': 'AccountId'},
                'JudgementGiven': {
                    'registrar_index': 'u32',
                    'target': 'AccountId',
                },
                'JudgementRequested': {
                    'registrar_index': 'u32',
                    'who': 'AccountId',
                },
                'JudgementUnrequested': {
                    'registrar_index': 'u32',
                    'who': 'AccountId',
                },
                'RegistrarAdded': {'registrar_index': 'u32'},
                'SubIdentityAdded': {
                    'deposit': 'u128',
                    'main': 'AccountId',
                    'sub': 'AccountId',
                },
                'SubIdentityRemoved': {
                    'deposit': 'u128',
                    'main': 'AccountId',
                    'sub': 'AccountId',
                },
                'SubIdentityRevoked': {
                    'deposit': 'u128',
                    'main': 'AccountId',
                    'sub': 'AccountId',
                },
            },
            'ImOnline': {
                'AllGood': None,
                'HeartbeatReceived': {'authority_id': '[u8; 32]'},
                'SomeOffline': {'offline': [('AccountId', 'scale_info::46')]},
            },
            'Kton': {
                'BalanceSet': {
                    'free': 'u128',
                    'reserved': 'u128',
                    'who': 'AccountId',
                },
                'Deposit': {'amount': 'u128', 'who': 'AccountId'},
                'DustLost': {'account': 'AccountId', 'amount': 'u128'},
                'Endowed': {'account': 'AccountId', 'free_balance': 'u128'},
                'ReserveRepatriated': {
                    'amount': 'u128',
                    'destination_status': 'scale_info::26',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Reserved': {'amount': 'u128', 'who': 'AccountId'},
                'Slashed': {'amount': 'u128', 'who': 'AccountId'},
                'Transfer': {
                    'amount': 'u128',
                    'from': 'AccountId',
                    'to': 'AccountId',
                },
                'Unreserved': {'amount': 'u128', 'who': 'AccountId'},
                'Withdraw': {'amount': 'u128', 'who': 'AccountId'},
            },
            'Multisig': {
                'MultisigApproval': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::92',
                },
                'MultisigCancelled': {
                    'call_hash': '[u8; 32]',
                    'cancelling': 'AccountId',
                    'multisig': 'AccountId',
                    'timepoint': 'scale_info::92',
                },
                'MultisigExecuted': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                    'result': 'scale_info::63',
                    'timepoint': 'scale_info::92',
                },
                'NewMultisig': {
                    'approving': 'AccountId',
                    'call_hash': '[u8; 32]',
                    'multisig': 'AccountId',
                },
            },
            'Offences': {'Offence': {'kind': '[u8; 16]', 'timeslot': 'Bytes'}},
            'PhragmenElection': {
                'CandidateSlashed': {
                    'amount': 'u128',
                    'candidate': 'AccountId',
                },
                'ElectionError': None,
                'EmptyTerm': None,
                'MemberKicked': {'member': 'AccountId'},
                'NewTerm': {'new_members': [('AccountId', 'u128')]},
                'Renounced': {'candidate': 'AccountId'},
                'SeatHolderSlashed': {
                    'amount': 'u128',
                    'seat_holder': 'AccountId',
                },
            },
            'Preimage': {
                'Cleared': {'hash': '[u8; 32]'},
                'Noted': {'hash': '[u8; 32]'},
                'Requested': {'hash': '[u8; 32]'},
            },
            'Proxy': {
                'Announced': {
                    'call_hash': '[u8; 32]',
                    'proxy': 'AccountId',
                    'real': 'AccountId',
                },
                'AnonymousCreated': {
                    'anonymous': 'AccountId',
                    'disambiguation_index': 'u16',
                    'proxy_type': 'scale_info::89',
                    'who': 'AccountId',
                },
                'ProxyAdded': {
                    'delay': 'u32',
                    'delegatee': 'AccountId',
                    'delegator': 'AccountId',
                    'proxy_type': 'scale_info::89',
                },
                'ProxyExecuted': {'result': 'scale_info::63'},
            },
            'Recovery': {
                'AccountRecovered': {
                    'lost_account': 'AccountId',
                    'rescuer_account': 'AccountId',
                },
                'RecoveryClosed': {
                    'lost_account': 'AccountId',
                    'rescuer_account': 'AccountId',
                },
                'RecoveryCreated': {'account': 'AccountId'},
                'RecoveryInitiated': {
                    'lost_account': 'AccountId',
                    'rescuer_account': 'AccountId',
                },
                'RecoveryRemoved': {'lost_account': 'AccountId'},
                'RecoveryVouched': {
                    'lost_account': 'AccountId',
                    'rescuer_account': 'AccountId',
                    'sender': 'AccountId',
                },
            },
            'Scheduler': {
                'CallLookupFailed': {
                    'error': 'scale_info::86',
                    'id': (None, 'Bytes'),
                    'task': ('u32', 'u32'),
                },
                'Canceled': {'index': 'u32', 'when': 'u32'},
                'Dispatched': {
                    'id': (None, 'Bytes'),
                    'result': 'scale_info::63',
                    'task': ('u32', 'u32'),
                },
                'Scheduled': {'index': 'u32', 'when': 'u32'},
            },
            'Session': {'NewSession': {'session_index': 'u32'}},
            'Society': {
                'AutoUnbid': {'candidate': 'AccountId'},
                'Bid': {'candidate_id': 'AccountId', 'offer': 'u128'},
                'CandidateSuspended': {'candidate': 'AccountId'},
                'Challenged': {'member': 'AccountId'},
                'DefenderVote': {'vote': 'bool', 'voter': 'AccountId'},
                'Deposit': {'value': 'u128'},
                'Founded': {'founder': 'AccountId'},
                'Inducted': {'candidates': ['AccountId'], 'primary': 'AccountId'},
                'MemberSuspended': {'member': 'AccountId'},
                'NewMaxMembers': {'max': 'u32'},
                'SuspendedMemberJudgement': {
                    'judged': 'bool',
                    'who': 'AccountId',
                },
                'Unbid': {'candidate': 'AccountId'},
                'Unfounded': {'founder': 'AccountId'},
                'Unvouch': {'candidate': 'AccountId'},
                'Vote': {
                    'candidate': 'AccountId',
                    'vote': 'bool',
                    'voter': 'AccountId',
                },
                'Vouch': {
                    'candidate_id': 'AccountId',
                    'offer': 'u128',
                    'vouching': 'AccountId',
                },
            },
            'Staking': {
                'Chilled': 'AccountId',
                'DepositsClaimed': 'AccountId',
                'DepositsClaimedWithPunish': ('AccountId', 'u128'),
                'EraPaid': ('u32', 'u128', 'u128'),
                'Kicked': ('AccountId', 'AccountId'),
                'KtonBonded': ('AccountId', 'u128'),
                'KtonUnbonded': ('AccountId', 'u128'),
                'OldSlashingReportDiscarded': 'u32',
                'PayoutStarted': ('u32', 'AccountId'),
                'Rewarded': ('AccountId', 'u128'),
                'RingBonded': ('AccountId', 'u128', 'u64', 'u64'),
                'RingUnbonded': ('AccountId', 'u128'),
                'Slashed': ('AccountId', 'u128', 'u128'),
                'StakersElected': None,
                'StakingElectionFailed': None,
            },
            'Sudo': {
                'KeyChanged': {'old_sudoer': (None, 'AccountId')},
                'Sudid': {'sudo_result': 'scale_info::63'},
                'SudoAsDone': {'sudo_result': 'scale_info::63'},
            },
            'System': {
                'CodeUpdated': None,
                'ExtrinsicFailed': {
                    'dispatch_error': 'scale_info::22',
                    'dispatch_info': 'scale_info::19',
                },
                'ExtrinsicSuccess': {'dispatch_info': 'scale_info::19'},
                'KilledAccount': {'account': 'AccountId'},
                'NewAccount': {'account': 'AccountId'},
                'Remarked': {'hash': '[u8; 32]', 'sender': 'AccountId'},
            },
            'Tips': {
                'NewTip': {'tip_hash': '[u8; 32]'},
                'TipClosed': {
                    'payout': 'u128',
                    'tip_hash': '[u8; 32]',
                    'who': 'AccountId',
                },
                'TipClosing': {'tip_hash': '[u8; 32]'},
                'TipRetracted': {'tip_hash': '[u8; 32]'},
                'TipSlashed': {
                    'deposit': 'u128',
                    'finder': 'AccountId',
                    'tip_hash': '[u8; 32]',
                },
            },
            'Treasury': {
                'Awarded': {
                    'account': 'AccountId',
                    'award': 'u128',
                    'proposal_index': 'u32',
                },
                'Burnt': {'burnt_funds': 'u128'},
                'Deposit': {'value': 'u128'},
                'Proposed': {'proposal_index': 'u32'},
                'Rejected': {'proposal_index': 'u32', 'slashed': 'u128'},
                'Rollover': {'rollover_balance': 'u128'},
                'Spending': {'budget_remaining': 'u128'},
            },
            'Utility': {
                'BatchCompleted': None,
                'BatchInterrupted': {
                    'error': 'scale_info::22',
                    'index': 'u32',
                },
                'DispatchedAs': {'result': 'scale_info::63'},
                'ItemCompleted': None,
            },
            None: None,
            'TechnicalCommittee': {
                'Approved': {'proposal_hash': '[u8; 32]'},
                'Closed': {
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'yes': 'u32',
                },
                'Disapproved': {'proposal_hash': '[u8; 32]'},
                'Executed': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::63',
                },
                'MemberExecuted': {
                    'proposal_hash': '[u8; 32]',
                    'result': 'scale_info::63',
                },
                'Proposed': {
                    'account': 'AccountId',
                    'proposal_hash': '[u8; 32]',
                    'proposal_index': 'u32',
                    'threshold': 'u32',
                },
                'Voted': {
                    'account': 'AccountId',
                    'no': 'u32',
                    'proposal_hash': '[u8; 32]',
                    'voted': 'bool',
                    'yes': 'u32',
                },
            },
            'TechnicalMembership': (
                'MemberAdded',
                'MemberRemoved',
                'MembersSwapped',
                'MembersReset',
                'KeyChanged',
                'Dummy',
            ),
            'Vesting': {
                'VestingCompleted': {'account': 'AccountId'},
                'VestingUpdated': {'account': 'AccountId', 'unvested': 'u128'},
            },
        },
        'phase': {
            'ApplyExtrinsic': 'u32',
            'Finalization': None,
            'Initialization': None,
        },
        'topics': ['[u8; 32]'],
    },
]
```
---------
### ExecutionPhase
 The execution phase of the block.

#### Python
```python
result = substrate.query(
    'System', 'ExecutionPhase', []
)
```

#### Return value
```python
{'ApplyExtrinsic': 'u32', 'Finalization': None, 'Initialization': None}
```
---------
### ExtrinsicCount
 Total extrinsics count for the current block.

#### Python
```python
result = substrate.query(
    'System', 'ExtrinsicCount', []
)
```

#### Return value
```python
'u32'
```
---------
### ExtrinsicData
 Extrinsics data for the current block (maps an extrinsic&#x27;s index to its data).

#### Python
```python
result = substrate.query(
    'System', 'ExtrinsicData', ['u32']
)
```

#### Return value
```python
'Bytes'
```
---------
### LastRuntimeUpgrade
 Stores the `spec_version` and `spec_name` of when the last runtime upgrade happened.

#### Python
```python
result = substrate.query(
    'System', 'LastRuntimeUpgrade', []
)
```

#### Return value
```python
{'spec_name': 'Str', 'spec_version': 'u32'}
```
---------
### Number
 The current block number being processed. Set by `execute_block`.

#### Python
```python
result = substrate.query(
    'System', 'Number', []
)
```

#### Return value
```python
'u32'
```
---------
### ParentHash
 Hash of the previous block.

#### Python
```python
result = substrate.query(
    'System', 'ParentHash', []
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### UpgradedToTripleRefCount
 True if we have upgraded so that AccountInfo contains three types of `RefCount`. False
 (default) if not.

#### Python
```python
result = substrate.query(
    'System', 'UpgradedToTripleRefCount', []
)
```

#### Return value
```python
'bool'
```
---------
### UpgradedToU32RefCount
 True if we have upgraded so that `type RefCount` is `u32`. False (default) if not.

#### Python
```python
result = substrate.query(
    'System', 'UpgradedToU32RefCount', []
)
```

#### Return value
```python
'bool'
```
---------
## Constants

---------
### BlockHashCount
 Maximum number of block number to block hash mappings to keep (oldest pruned first).
#### Value
```python
2400
```
#### Python
```python
constant = substrate.get_constant('System', 'BlockHashCount')
```
---------
### BlockLength
 The maximum length of a block (in bytes).
#### Value
```python
{'max': {'mandatory': 5242880, 'normal': 3932160, 'operational': 5242880}}
```
#### Python
```python
constant = substrate.get_constant('System', 'BlockLength')
```
---------
### BlockWeights
 Block &amp; extrinsics weights: base values and limits.
#### Value
```python
{
    'base_block': 5000000000,
    'max_block': 2000000000000,
    'per_class': {
        'mandatory': {
            'base_extrinsic': 125000000,
            'max_extrinsic': None,
            'max_total': None,
            'reserved': None,
        },
        'normal': {
            'base_extrinsic': 125000000,
            'max_extrinsic': 1449875000000,
            'max_total': 1500000000000,
            'reserved': 0,
        },
        'operational': {
            'base_extrinsic': 125000000,
            'max_extrinsic': 1949875000000,
            'max_total': 2000000000000,
            'reserved': 500000000000,
        },
    },
}
```
#### Python
```python
constant = substrate.get_constant('System', 'BlockWeights')
```
---------
### DbWeight
 The weight of runtime database operations the runtime can invoke.
#### Value
```python
{'read': 25000000, 'write': 100000000}
```
#### Python
```python
constant = substrate.get_constant('System', 'DbWeight')
```
---------
### SS58Prefix
 The designated SS85 prefix of this chain.

 This replaces the &quot;ss58Format&quot; property declared in the chain spec. Reason is
 that the runtime should know about the prefix in order to make use of it as
 an identifier of the chain.
#### Value
```python
18
```
#### Python
```python
constant = substrate.get_constant('System', 'SS58Prefix')
```
---------
### Version
 Get the chain&#x27;s current version.
#### Value
```python
{
    'apis': [
        ('0xdf6acb689907609b', 4),
        ('0x37e397fc7c91f5e4', 1),
        ('0x40fe3ad401f8959a', 5),
        ('0xbc9d89904f5b923f', 1),
        ('0xd2bc9897eed08f15', 3),
        ('0xf78b278be53f454c', 2),
        ('0xcbca25e39f142387', 2),
        ('0xed99c5acb25eedf5', 3),
        ('0x687ad44ad37f03c2', 1),
        ('0xab3c0572291feb8b', 1),
        ('0x37c8bb1350a9a2a8', 1),
        ('0x582211f65bb14b89', 4),
        ('0xe65b00e46cedd0aa', 2),
        ('0xbd78255d4feeea1f', 4),
    ],
    'authoring_version': 0,
    'impl_name': 'Darwinia',
    'impl_version': 0,
    'spec_name': 'Darwinia',
    'spec_version': 1250,
    'state_version': 0,
    'transaction_version': 0,
}
```
#### Python
```python
constant = substrate.get_constant('System', 'Version')
```
---------
## Errors

---------
### CallFiltered
The origin filter prevent the call to be dispatched.

---------
### FailedToExtractRuntimeVersion
Failed to extract the runtime version from the new runtime.

Either calling `Core_version` or decoding `RuntimeVersion` failed.

---------
### InvalidSpecName
The name of specification does not match between the current runtime
and the new runtime.

---------
### NonDefaultComposite
Suicide called when the account has non-default composite data.

---------
### NonZeroRefCount
There is a non-zero reference count preventing the account from being purged.

---------
### SpecVersionNeedsToIncrease
The specification version is not allowed to decrease between the current runtime
and the new runtime.

---------