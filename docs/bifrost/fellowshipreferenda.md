
# FellowshipReferenda

---------
## Calls

---------
### cancel
See [`Pallet::cancel`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipReferenda', 'cancel', {'index': 'u32'}
)
```

---------
### kill
See [`Pallet::kill`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipReferenda', 'kill', {'index': 'u32'}
)
```

---------
### nudge_referendum
See [`Pallet::nudge_referendum`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipReferenda', 'nudge_referendum', {'index': 'u32'}
)
```

---------
### one_fewer_deciding
See [`Pallet::one_fewer_deciding`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| track | `TrackIdOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipReferenda', 'one_fewer_deciding', {'track': 'u16'}
)
```

---------
### place_decision_deposit
See [`Pallet::place_decision_deposit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipReferenda', 'place_decision_deposit', {'index': 'u32'}
)
```

---------
### refund_decision_deposit
See [`Pallet::refund_decision_deposit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipReferenda', 'refund_decision_deposit', {'index': 'u32'}
)
```

---------
### refund_submission_deposit
See [`Pallet::refund_submission_deposit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipReferenda', 'refund_submission_deposit', {'index': 'u32'}
)
```

---------
### set_metadata
See [`Pallet::set_metadata`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ReferendumIndex` | 
| maybe_hash | `Option<T::Hash>` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipReferenda', 'set_metadata', {
    'index': 'u32',
    'maybe_hash': (
        None,
        'scale_info::12',
    ),
}
)
```

---------
### submit
See [`Pallet::submit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| proposal_origin | `Box<PalletsOriginOf<T>>` | 
| proposal | `BoundedCallOf<T, I>` | 
| enactment_moment | `DispatchTime<BlockNumberFor<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'FellowshipReferenda', 'submit', {
    'enactment_moment': {
        'After': 'u32',
        'At': 'u32',
    },
    'proposal': {
        'Inline': 'Bytes',
        'Legacy': {
            'hash': 'scale_info::12',
        },
        'Lookup': {
            'hash': 'scale_info::12',
            'len': 'u32',
        },
    },
    'proposal_origin': {
        None: None,
        'Council': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'CumulusXcm': {
            'Relay': None,
            'SiblingParachain': 'u32',
        },
        'Origins': (
            'WhitelistedCaller',
            'FellowshipAdmin',
            'ReferendumCanceller',
            'ReferendumKiller',
            'LiquidStaking',
            'SALPAdmin',
            'FellowshipInitiates',
            'Fellows',
            'FellowshipExperts',
            'FellowshipMasters',
            'Fellowship1Dan',
            'Fellowship2Dan',
            'Fellowship3Dan',
            'Fellowship4Dan',
            'Fellowship5Dan',
            'Fellowship6Dan',
            'Fellowship7Dan',
            'Fellowship8Dan',
            'Fellowship9Dan',
            'TechAdmin',
            'CoreAdmin',
            'TreasurySpend',
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
                                'scale_info::124',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::124',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::124',
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
                            'id': 'scale_info::125',
                            'part': 'scale_info::126',
                        },
                    },
                    'X2': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                                'scale_info::124',
                            ),
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': (
                                None,
                                'scale_info::124',
                            ),
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': (
                                None,
                                'scale_info::124',
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
                            'id': 'scale_info::125',
                            'part': 'scale_info::126',
                        },
                    },
                    'X2': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'InnerStruct',
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
                            'GlobalConsensus': 'scale_info::124',
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
        'TechnicalCommittee': {
            'Member': 'AccountId',
            'Members': ('u32', 'u32'),
            '_Phantom': None,
        },
        'Void': (),
        'system': {
            'None': None,
            'Root': None,
            'Signed': 'AccountId',
        },
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
| tally | `T::Tally` | ```{'bare_ayes': 'u32', 'ayes': 'u32', 'nays': 'u32'}```

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
| tally | `T::Tally` | ```{'bare_ayes': 'u32', 'ayes': 'u32', 'nays': 'u32'}```

---------
### DecisionDepositPlaced
The decision deposit has been placed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T, I>` | ```u128```

---------
### DecisionDepositRefunded
The decision deposit has been refunded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T, I>` | ```u128```

---------
### DecisionStarted
A referendum has moved into the deciding phase.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| track | `TrackIdOf<T, I>` | ```u16```
| proposal | `BoundedCallOf<T, I>` | ```{'Legacy': {'hash': 'scale_info::12'}, 'Inline': 'Bytes', 'Lookup': {'hash': 'scale_info::12', 'len': 'u32'}}```
| tally | `T::Tally` | ```{'bare_ayes': 'u32', 'ayes': 'u32', 'nays': 'u32'}```

---------
### DepositSlashed
A deposit has been slashaed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T, I>` | ```u128```

---------
### Killed
A referendum has been killed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| tally | `T::Tally` | ```{'bare_ayes': 'u32', 'ayes': 'u32', 'nays': 'u32'}```

---------
### MetadataCleared
Metadata for a referendum has been cleared.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| hash | `T::Hash` | ```scale_info::12```

---------
### MetadataSet
Metadata for a referendum has been set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| hash | `T::Hash` | ```scale_info::12```

---------
### Rejected
A proposal has been rejected by referendum.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| tally | `T::Tally` | ```{'bare_ayes': 'u32', 'ayes': 'u32', 'nays': 'u32'}```

---------
### SubmissionDepositRefunded
The submission deposit has been refunded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T, I>` | ```u128```

---------
### Submitted
A referendum has been submitted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| track | `TrackIdOf<T, I>` | ```u16```
| proposal | `BoundedCallOf<T, I>` | ```{'Legacy': {'hash': 'scale_info::12'}, 'Inline': 'Bytes', 'Lookup': {'hash': 'scale_info::12', 'len': 'u32'}}```

---------
### TimedOut
A referendum has been timed out without being decided.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `ReferendumIndex` | ```u32```
| tally | `T::Tally` | ```{'bare_ayes': 'u32', 'ayes': 'u32', 'nays': 'u32'}```

---------
## Storage functions

---------
### DecidingCount
 The number of referenda being decided currently.

#### Python
```python
result = substrate.query(
    'FellowshipReferenda', 'DecidingCount', ['u16']
)
```

#### Return value
```python
'u32'
```
---------
### MetadataOf
 The metadata is a general information concerning the referendum.
 The `Hash` refers to the preimage of the `Preimages` provider which can be a JSON
 dump or IPFS hash of a JSON file.

 Consider a garbage collection for a metadata of finished referendums to `unrequest` (remove)
 large preimages.

#### Python
```python
result = substrate.query(
    'FellowshipReferenda', 'MetadataOf', ['u32']
)
```

#### Return value
```python
'scale_info::12'
```
---------
### ReferendumCount
 The next free referendum index, aka the number of referenda started so far.

#### Python
```python
result = substrate.query(
    'FellowshipReferenda', 'ReferendumCount', []
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
    'FellowshipReferenda', 'ReferendumInfoFor', ['u32']
)
```

#### Return value
```python
{
    'Approved': (
        'u32',
        (None, {'amount': 'u128', 'who': 'AccountId'}),
        (None, {'amount': 'u128', 'who': 'AccountId'}),
    ),
    'Cancelled': (
        'u32',
        (None, {'amount': 'u128', 'who': 'AccountId'}),
        (None, {'amount': 'u128', 'who': 'AccountId'}),
    ),
    'Killed': 'u32',
    'Ongoing': {
        'alarm': (None, ('u32', ('u32', 'u32'))),
        'deciding': (None, {'confirming': (None, 'u32'), 'since': 'u32'}),
        'decision_deposit': (None, {'amount': 'u128', 'who': 'AccountId'}),
        'enactment': {'After': 'u32', 'At': 'u32'},
        'in_queue': 'bool',
        'origin': {
            'Council': {
                'Member': 'AccountId',
                'Members': ('u32', 'u32'),
                '_Phantom': None,
            },
            'CumulusXcm': {'Relay': None, 'SiblingParachain': 'u32'},
            'Origins': (
                'WhitelistedCaller',
                'FellowshipAdmin',
                'ReferendumCanceller',
                'ReferendumKiller',
                'LiquidStaking',
                'SALPAdmin',
                'FellowshipInitiates',
                'Fellows',
                'FellowshipExperts',
                'FellowshipMasters',
                'Fellowship1Dan',
                'Fellowship2Dan',
                'Fellowship3Dan',
                'Fellowship4Dan',
                'Fellowship5Dan',
                'Fellowship6Dan',
                'Fellowship7Dan',
                'Fellowship8Dan',
                'Fellowship9Dan',
                'TechAdmin',
                'CoreAdmin',
                'TreasurySpend',
            ),
            'PolkadotXcm': {
                'Response': {'interior': 'scale_info::121', 'parents': 'u8'},
                'Xcm': {'interior': 'scale_info::121', 'parents': 'u8'},
            },
            'TechnicalCommittee': {
                'Member': 'AccountId',
                'Members': ('u32', 'u32'),
                '_Phantom': None,
            },
            'Void': (),
            'system': {'None': None, 'Root': None, 'Signed': 'AccountId'},
            None: None,
        },
        'proposal': {
            'Inline': 'Bytes',
            'Legacy': {'hash': 'scale_info::12'},
            'Lookup': {'hash': 'scale_info::12', 'len': 'u32'},
        },
        'submission_deposit': {'amount': 'u128', 'who': 'AccountId'},
        'submitted': 'u32',
        'tally': {'ayes': 'u32', 'bare_ayes': 'u32', 'nays': 'u32'},
        'track': 'u16',
    },
    'Rejected': (
        'u32',
        (None, {'amount': 'u128', 'who': 'AccountId'}),
        (None, {'amount': 'u128', 'who': 'AccountId'}),
    ),
    'TimedOut': (
        'u32',
        (None, {'amount': 'u128', 'who': 'AccountId'}),
        (None, {'amount': 'u128', 'who': 'AccountId'}),
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
    'FellowshipReferenda', 'TrackQueue', ['u16']
)
```

#### Return value
```python
[('u32', 'u32')]
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
constant = substrate.get_constant('FellowshipReferenda', 'AlarmInterval')
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
constant = substrate.get_constant('FellowshipReferenda', 'MaxQueued')
```
---------
### SubmissionDeposit
 The minimum amount to be used as a deposit for a public referendum proposal.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('FellowshipReferenda', 'SubmissionDeposit')
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
            'confirm_period': 25,
            'decision_deposit': 100000000000000,
            'decision_period': 14400,
            'max_deciding': 10,
            'min_approval': {
                'LinearDecreasing': {
                    'ceil': 1000000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'min_enactment_period': 5,
            'min_support': {
                'LinearDecreasing': {
                    'ceil': 600000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'name': 'candidates',
            'prepare_period': 5,
        },
    ),
    (
        1,
        {
            'confirm_period': 25,
            'decision_deposit': 10000000000000,
            'decision_period': 14400,
            'max_deciding': 10,
            'min_approval': {
                'LinearDecreasing': {
                    'ceil': 1000000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'min_enactment_period': 5,
            'min_support': {
                'LinearDecreasing': {
                    'ceil': 600000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'name': 'members',
            'prepare_period': 5,
        },
    ),
    (
        2,
        {
            'confirm_period': 25,
            'decision_deposit': 10000000000000,
            'decision_period': 14400,
            'max_deciding': 10,
            'min_approval': {
                'LinearDecreasing': {
                    'ceil': 1000000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'min_enactment_period': 5,
            'min_support': {
                'LinearDecreasing': {
                    'ceil': 600000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'name': 'proficients',
            'prepare_period': 5,
        },
    ),
    (
        3,
        {
            'confirm_period': 25,
            'decision_deposit': 10000000000000,
            'decision_period': 14400,
            'max_deciding': 10,
            'min_approval': {
                'LinearDecreasing': {
                    'ceil': 1000000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'min_enactment_period': 5,
            'min_support': {
                'LinearDecreasing': {
                    'ceil': 600000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'name': 'fellows',
            'prepare_period': 5,
        },
    ),
    (
        4,
        {
            'confirm_period': 25,
            'decision_deposit': 10000000000000,
            'decision_period': 14400,
            'max_deciding': 10,
            'min_approval': {
                'LinearDecreasing': {
                    'ceil': 1000000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'min_enactment_period': 5,
            'min_support': {
                'LinearDecreasing': {
                    'ceil': 600000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'name': 'senior fellows',
            'prepare_period': 5,
        },
    ),
    (
        5,
        {
            'confirm_period': 25,
            'decision_deposit': 1000000000000,
            'decision_period': 14400,
            'max_deciding': 10,
            'min_approval': {
                'LinearDecreasing': {
                    'ceil': 1000000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'min_enactment_period': 5,
            'min_support': {
                'LinearDecreasing': {
                    'ceil': 600000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'name': 'experts',
            'prepare_period': 5,
        },
    ),
    (
        6,
        {
            'confirm_period': 25,
            'decision_deposit': 1000000000000,
            'decision_period': 14400,
            'max_deciding': 10,
            'min_approval': {
                'LinearDecreasing': {
                    'ceil': 1000000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'min_enactment_period': 5,
            'min_support': {
                'LinearDecreasing': {
                    'ceil': 600000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'name': 'senior experts',
            'prepare_period': 5,
        },
    ),
    (
        7,
        {
            'confirm_period': 25,
            'decision_deposit': 1000000000000,
            'decision_period': 14400,
            'max_deciding': 10,
            'min_approval': {
                'LinearDecreasing': {
                    'ceil': 1000000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'min_enactment_period': 5,
            'min_support': {
                'LinearDecreasing': {
                    'ceil': 600000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'name': 'masters',
            'prepare_period': 5,
        },
    ),
    (
        8,
        {
            'confirm_period': 25,
            'decision_deposit': 1000000000000,
            'decision_period': 14400,
            'max_deciding': 10,
            'min_approval': {
                'LinearDecreasing': {
                    'ceil': 1000000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'min_enactment_period': 5,
            'min_support': {
                'LinearDecreasing': {
                    'ceil': 600000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'name': 'senior masters',
            'prepare_period': 5,
        },
    ),
    (
        9,
        {
            'confirm_period': 25,
            'decision_deposit': 1000000000000,
            'decision_period': 14400,
            'max_deciding': 10,
            'min_approval': {
                'LinearDecreasing': {
                    'ceil': 1000000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'min_enactment_period': 5,
            'min_support': {
                'LinearDecreasing': {
                    'ceil': 600000000,
                    'floor': 500000000,
                    'length': 1000000000,
                },
            },
            'name': 'grand masters',
            'prepare_period': 5,
        },
    ),
]
```
#### Python
```python
constant = substrate.get_constant('FellowshipReferenda', 'Tracks')
```
---------
### UndecidingTimeout
 The number of blocks after submission that a referendum must begin being decided by.
 Once this passes, then anyone may cancel the referendum.
#### Value
```python
50400
```
#### Python
```python
constant = substrate.get_constant('FellowshipReferenda', 'UndecidingTimeout')
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