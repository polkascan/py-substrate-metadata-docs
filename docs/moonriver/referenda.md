
# Referenda

---------
## Calls

---------
### cancel
Cancel an ongoing referendum.

- `origin`: must be the `CancelOrigin`.
- `index`: The index of the referendum to be cancelled.

Emits `Cancelled`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Referenda', 'cancel', {'index': 'u32'}
)
```

---------
### kill
Cancel an ongoing referendum and slash the deposits.

- `origin`: must be the `KillOrigin`.
- `index`: The index of the referendum to be cancelled.

Emits `Killed` and `DepositSlashed`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Referenda', 'kill', {'index': 'u32'}
)
```

---------
### nudge_referendum
Advance a referendum onto its next logical state. Only used internally.

- `origin`: must be `Root`.
- `index`: the referendum to be advanced.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Referenda', 'nudge_referendum', {'index': 'u32'}
)
```

---------
### one_fewer_deciding
Advance a track onto its next logical state. Only used internally.

- `origin`: must be `Root`.
- `track`: the track to be advanced.

Action item for when there is now one fewer referendum in the deciding phase and the
`DecidingCount` is not yet updated. This means that we should either:
- begin deciding another referendum (and leave `DecidingCount` alone); or
- decrement `DecidingCount`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| track | `TrackIdOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'Referenda', 'one_fewer_deciding', {'track': 'u16'}
)
```

---------
### place_decision_deposit
Post the Decision Deposit for a referendum.

- `origin`: must be `Signed` and the account must have funds available for the
  referendum&\#x27;s track&\#x27;s Decision Deposit.
- `index`: The index of the submitted referendum whose Decision Deposit is yet to be
  posted.

Emits `DecisionDepositPlaced`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Referenda', 'place_decision_deposit', {'index': 'u32'}
)
```

---------
### refund_decision_deposit
Refund the Decision Deposit for a closed referendum back to the depositor.

- `origin`: must be `Signed` or `Root`.
- `index`: The index of a closed referendum whose Decision Deposit has not yet been
  refunded.

Emits `DecisionDepositRefunded`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Referenda', 'refund_decision_deposit', {'index': 'u32'}
)
```

---------
### refund_submission_deposit
Refund the Submission Deposit for a closed referendum back to the depositor.

- `origin`: must be `Signed` or `Root`.
- `index`: The index of a closed referendum whose Submission Deposit has not yet been
  refunded.

Emits `SubmissionDepositRefunded`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Referenda', 'refund_submission_deposit', {'index': 'u32'}
)
```

---------
### set_metadata
Set or clear metadata of a referendum.

Parameters:
- `origin`: Must be `Signed` by a creator of a referendum or by anyone to clear a
  metadata of a finished referendum.
- `index`:  The index of a referendum to set or clear metadata for.
- `maybe_hash`: The hash of an on-chain stored preimage. `None` to clear a metadata.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ReferendumIndex` | 
| maybe_hash | `Option<PreimageHash>` | 

#### Python
```python
call = substrate.compose_call(
    'Referenda', 'set_metadata', {
    'index': 'u32',
    'maybe_hash': (None, '[u8; 32]'),
}
)
```

---------
### submit
Propose a referendum on a privileged action.

- `origin`: must be `SubmitOrigin` and the account must have `SubmissionDeposit` funds
  available.
- `proposal_origin`: The origin from which the proposal should be executed.
- `proposal`: The proposal.
- `enactment_moment`: The moment that the proposal should be enacted.

Emits `Submitted`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_origin | `Box<PalletsOriginOf<T>>` | 
| proposal | `BoundedCallOf<T, I>` | 
| enactment_moment | `DispatchTime<T::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'Referenda', 'submit', {
    'enactment_moment': {
        'After': 'u32',
        'At': 'u32',
    },
    'proposal': {
        'Inline': 'Bytes',
        'Legacy': {'hash': '[u8; 32]'},
        'Lookup': {
            'hash': '[u8; 32]',
            'len': 'u32',
        },
    },
    'proposal_origin': {
        'CouncilCollective': {
            'Member': '[u8; 20]',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'CumulusXcm': {
            'Relay': None,
            'SiblingParachain': 'u32',
        },
        'Ethereum': {
            'EthereumTransaction': '[u8; 20]',
        },
        'EthereumXcm': {
            'XcmEthereumTransaction': '[u8; 20]',
        },
        'OpenTechCommitteeCollective': {
            'Member': '[u8; 20]',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'Origins': (
            'WhitelistedCaller',
            'GeneralAdmin',
            'ReferendumCanceller',
            'ReferendumKiller',
        ),
        'PolkadotXcm': {
            'Response': {
                'interior': {
                    'Here': None,
                    'X1': {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::133',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::133',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::133',
                            ),
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': {
                            'data': '[u8; 32]',
                            'length': 'u8',
                        },
                        'GlobalConsensus': {
                            'BitcoinCash': None,
                            'BitcoinCore': None,
                            'ByFork': 'InnerStruct',
                            'ByGenesis': '[u8; 32]',
                            'Ethereum': 'InnerStruct',
                            'Kusama': None,
                            'Polkadot': None,
                            'Rococo': None,
                            'Westend': None,
                            'Wococo': None,
                        },
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::134',
                            'part': 'scale_info::135',
                        },
                    },
                    'X2': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X3': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X4': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X5': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X6': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X7': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X8': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                    ),
                },
                'parents': 'u8',
            },
            'Xcm': {
                'interior': {
                    'Here': None,
                    'X1': {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': (
                                None,
                                'scale_info::133',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::133',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::133',
                            ),
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': {
                            'data': '[u8; 32]',
                            'length': 'u8',
                        },
                        'GlobalConsensus': {
                            'BitcoinCash': None,
                            'BitcoinCore': None,
                            'ByFork': 'InnerStruct',
                            'ByGenesis': '[u8; 32]',
                            'Ethereum': 'InnerStruct',
                            'Kusama': None,
                            'Polkadot': None,
                            'Rococo': None,
                            'Westend': None,
                            'Wococo': None,
                        },
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::134',
                            'part': 'scale_info::135',
                        },
                    },
                    'X2': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X3': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X4': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X5': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X6': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X7': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X8': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::133',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                    ),
                },
                'parents': 'u8',
            },
        },
        'TechCommitteeCollective': {
            'Member': '[u8; 20]',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'TreasuryCouncilCollective': {
            'Member': '[u8; 20]',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'Void': (),
        'system': {
            'None': None,
            'Root': None,
            'Signed': '[u8; 20]',
        },
        None: None,
    },
}
)
```

---------
## Events

---------
### Approved
A referendum has been approved and its proposal has been scheduled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```

---------
### Cancelled
A referendum has been cancelled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| tally | `T::Tally` | ```{'ayes': 'u128', 'nays': 'u128', 'support': 'u128'}```

---------
### ConfirmAborted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```

---------
### ConfirmStarted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```

---------
### Confirmed
A referendum has ended its confirmation phase and is ready for approval.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| tally | `T::Tally` | ```{'ayes': 'u128', 'nays': 'u128', 'support': 'u128'}```

---------
### DecisionDepositPlaced
The decision deposit has been placed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| who | `T::AccountId` | ```[u8; 20]```
| amount | `BalanceOf<T, I>` | ```u128```

---------
### DecisionDepositRefunded
The decision deposit has been refunded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| who | `T::AccountId` | ```[u8; 20]```
| amount | `BalanceOf<T, I>` | ```u128```

---------
### DecisionStarted
A referendum has moved into the deciding phase.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| track | `TrackIdOf<T, I>` | ```u16```
| proposal | `BoundedCallOf<T, I>` | ```{'Legacy': {'hash': '[u8; 32]'}, 'Inline': 'Bytes', 'Lookup': {'hash': '[u8; 32]', 'len': 'u32'}}```
| tally | `T::Tally` | ```{'ayes': 'u128', 'nays': 'u128', 'support': 'u128'}```

---------
### DepositSlashed
A deposit has been slashaed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```[u8; 20]```
| amount | `BalanceOf<T, I>` | ```u128```

---------
### Killed
A referendum has been killed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| tally | `T::Tally` | ```{'ayes': 'u128', 'nays': 'u128', 'support': 'u128'}```

---------
### MetadataCleared
Metadata for a referendum has been cleared.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| hash | `PreimageHash` | ```[u8; 32]```

---------
### MetadataSet
Metadata for a referendum has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| hash | `PreimageHash` | ```[u8; 32]```

---------
### Rejected
A proposal has been rejected by referendum.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| tally | `T::Tally` | ```{'ayes': 'u128', 'nays': 'u128', 'support': 'u128'}```

---------
### SubmissionDepositRefunded
The submission deposit has been refunded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| who | `T::AccountId` | ```[u8; 20]```
| amount | `BalanceOf<T, I>` | ```u128```

---------
### Submitted
A referendum has been submitted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| track | `TrackIdOf<T, I>` | ```u16```
| proposal | `BoundedCallOf<T, I>` | ```{'Legacy': {'hash': '[u8; 32]'}, 'Inline': 'Bytes', 'Lookup': {'hash': '[u8; 32]', 'len': 'u32'}}```

---------
### TimedOut
A referendum has been timed out without being decided.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| tally | `T::Tally` | ```{'ayes': 'u128', 'nays': 'u128', 'support': 'u128'}```

---------
## Storage functions

---------
### DecidingCount
 The number of referenda being decided currently.

#### Python
```python
result = substrate.query(
    'Referenda', 'DecidingCount', ['u16']
)
```

#### Return value
```python
'u32'
```
---------
### MetadataOf
 The metadata is a general information concerning the referendum.
 The `PreimageHash` refers to the preimage of the `Preimages` provider which can be a JSON
 dump or IPFS hash of a JSON file.

 Consider a garbage collection for a metadata of finished referendums to `unrequest` (remove)
 large preimages.

#### Python
```python
result = substrate.query(
    'Referenda', 'MetadataOf', ['u32']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### ReferendumCount
 The next free referendum index, aka the number of referenda started so far.

#### Python
```python
result = substrate.query(
    'Referenda', 'ReferendumCount', []
)
```

#### Return value
```python
'u32'
```
---------
### ReferendumInfoFor
 Information concerning any given referendum.

#### Python
```python
result = substrate.query(
    'Referenda', 'ReferendumInfoFor', ['u32']
)
```

#### Return value
```python
{
    'Approved': (
        'u32',
        (None, {'amount': 'u128', 'who': '[u8; 20]'}),
        (None, {'amount': 'u128', 'who': '[u8; 20]'}),
    ),
    'Cancelled': (
        'u32',
        (None, {'amount': 'u128', 'who': '[u8; 20]'}),
        (None, {'amount': 'u128', 'who': '[u8; 20]'}),
    ),
    'Killed': 'u32',
    'Ongoing': {
        'alarm': (None, ('u32', ('u32', 'u32'))),
        'deciding': (None, {'confirming': (None, 'u32'), 'since': 'u32'}),
        'decision_deposit': (None, {'amount': 'u128', 'who': '[u8; 20]'}),
        'enactment': {'After': 'u32', 'At': 'u32'},
        'in_queue': 'bool',
        'origin': {
            'Ethereum': {'EthereumTransaction': '[u8; 20]'},
            None: None,
            'CouncilCollective': {
                'Member': '[u8; 20]',
                'Members': ('u32', 'u32'),
                '_Phantom': None,
            },
            'CumulusXcm': {'Relay': None, 'SiblingParachain': 'u32'},
            'EthereumXcm': {'XcmEthereumTransaction': '[u8; 20]'},
            'OpenTechCommitteeCollective': {
                'Member': '[u8; 20]',
                'Members': ('u32', 'u32'),
                '_Phantom': None,
            },
            'Origins': (
                'WhitelistedCaller',
                'GeneralAdmin',
                'ReferendumCanceller',
                'ReferendumKiller',
            ),
            'PolkadotXcm': {
                'Response': {'interior': 'scale_info::129', 'parents': 'u8'},
                'Xcm': {'interior': 'scale_info::129', 'parents': 'u8'},
            },
            'TechCommitteeCollective': {
                'Member': '[u8; 20]',
                'Members': ('u32', 'u32'),
                '_Phantom': None,
            },
            'TreasuryCouncilCollective': {
                'Member': '[u8; 20]',
                'Members': ('u32', 'u32'),
                '_Phantom': None,
            },
            'Void': (),
            'system': {'None': None, 'Root': None, 'Signed': '[u8; 20]'},
        },
        'proposal': {
            'Inline': 'Bytes',
            'Legacy': {'hash': '[u8; 32]'},
            'Lookup': {'hash': '[u8; 32]', 'len': 'u32'},
        },
        'submission_deposit': {'amount': 'u128', 'who': '[u8; 20]'},
        'submitted': 'u32',
        'tally': {'ayes': 'u128', 'nays': 'u128', 'support': 'u128'},
        'track': 'u16',
    },
    'Rejected': (
        'u32',
        (None, {'amount': 'u128', 'who': '[u8; 20]'}),
        (None, {'amount': 'u128', 'who': '[u8; 20]'}),
    ),
    'TimedOut': (
        'u32',
        (None, {'amount': 'u128', 'who': '[u8; 20]'}),
        (None, {'amount': 'u128', 'who': '[u8; 20]'}),
    ),
}
```
---------
### TrackQueue
 The sorted list of referenda ready to be decided but not yet being decided, ordered by
 conviction-weighted approvals.

 This should be empty if `DecidingCount` is less than `TrackInfo::max_deciding`.

#### Python
```python
result = substrate.query(
    'Referenda', 'TrackQueue', ['u16']
)
```

#### Return value
```python
[('u32', 'u128')]
```
---------
## Constants

---------
### AlarmInterval
 Quantization level for the referendum wakeup scheduler. A higher number will result in
 fewer storage reads/writes needed for smaller voters, but also result in delays to the
 automatic referendum status changes. Explicit servicing instructions are unaffected.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Referenda', 'AlarmInterval')
```
---------
### MaxQueued
 Maximum size of the referendum queue for a single track.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Referenda', 'MaxQueued')
```
---------
### SubmissionDeposit
 The minimum amount to be used as a deposit for a public referendum proposal.
#### Value
```python
10000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Referenda', 'SubmissionDeposit')
```
---------
### Tracks
 Information concerning the different referendum tracks.
#### Value
```python
[
    (
        0,
        {
            'confirm_period': 7200,
            'decision_deposit': 100000000000000000000000,
            'decision_period': 100800,
            'max_deciding': 5,
            'min_approval': {
                'Reciprocal': {
                    'factor': 999999999,
                    'x_offset': 999999999,
                    'y_offset': 0,
                },
            },
            'min_enactment_period': 7200,
            'min_support': {
                'LinearDecreasing': {
                    'ceil': 250000000,
                    'floor': 5000000,
                    'length': 1000000000,
                },
            },
            'name': 'root',
            'prepare_period': 7200,
        },
    ),
    (
        1,
        {
            'confirm_period': 50,
            'decision_deposit': 10000000000000000000000,
            'decision_period': 100800,
            'max_deciding': 100,
            'min_approval': {
                'Reciprocal': {
                    'factor': 999999999,
                    'x_offset': 999999999,
                    'y_offset': 0,
                },
            },
            'min_enactment_period': 150,
            'min_support': {
                'Reciprocal': {
                    'factor': 60061,
                    'x_offset': 2994150,
                    'y_offset': -59882,
                },
            },
            'name': 'whitelisted_caller',
            'prepare_period': 50,
        },
    ),
    (
        2,
        {
            'confirm_period': 7200,
            'decision_deposit': 500000000000000000000,
            'decision_period': 100800,
            'max_deciding': 10,
            'min_approval': {
                'Reciprocal': {
                    'factor': 999999999,
                    'x_offset': 999999999,
                    'y_offset': 0,
                },
            },
            'min_enactment_period': 7200,
            'min_support': {
                'Reciprocal': {
                    'factor': 222222224,
                    'x_offset': 333333335,
                    'y_offset': -166666668,
                },
            },
            'name': 'general_admin',
            'prepare_period': 300,
        },
    ),
    (
        3,
        {
            'confirm_period': 900,
            'decision_deposit': 10000000000000000000000,
            'decision_period': 100800,
            'max_deciding': 20,
            'min_approval': {
                'Reciprocal': {
                    'factor': 999999999,
                    'x_offset': 999999999,
                    'y_offset': 0,
                },
            },
            'min_enactment_period': 50,
            'min_support': {
                'Reciprocal': {
                    'factor': 869501,
                    'x_offset': 8620680,
                    'y_offset': -862069,
                },
            },
            'name': 'referendum_canceller',
            'prepare_period': 300,
        },
    ),
    (
        4,
        {
            'confirm_period': 900,
            'decision_deposit': 20000000000000000000000,
            'decision_period': 100800,
            'max_deciding': 100,
            'min_approval': {
                'Reciprocal': {
                    'factor': 999999999,
                    'x_offset': 999999999,
                    'y_offset': 0,
                },
            },
            'min_enactment_period': 50,
            'min_support': {
                'Reciprocal': {
                    'factor': 869501,
                    'x_offset': 8620680,
                    'y_offset': -862069,
                },
            },
            'name': 'referendum_killer',
            'prepare_period': 300,
        },
    ),
]
```
#### Python
```python
constant = substrate.get_constant('Referenda', 'Tracks')
```
---------
### UndecidingTimeout
 The number of blocks after submission that a referendum must begin being decided by.
 Once this passes, then anyone may cancel the referendum.
#### Value
```python
100800
```
#### Python
```python
constant = substrate.get_constant('Referenda', 'UndecidingTimeout')
```
---------
## Errors

---------
### BadReferendum
The referendum index provided is invalid in this context.

---------
### BadStatus
The referendum status is invalid for this operation.

---------
### BadTrack
The track identifier given was invalid.

---------
### Full
There are already a full complement of referenda in progress for this track.

---------
### HasDeposit
Referendum&\#x27;s decision deposit is already paid.

---------
### NoDeposit
The deposit cannot be refunded since none was made.

---------
### NoPermission
The deposit refunder is not the depositor.

---------
### NoTrack
No track exists for the proposal origin.

---------
### NotOngoing
Referendum is not ongoing.

---------
### NothingToDo
There was nothing to do in the advancement.

---------
### PreimageNotExist
The preimage does not exist.

---------
### QueueEmpty
The queue of the track is empty.

---------
### Unfinished
Any deposit cannot be refunded until after the decision is over.

---------