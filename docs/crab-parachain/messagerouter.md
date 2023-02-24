
# MessageRouter

---------
## Calls

---------
### forward
Deliver received LCMP messages to other parachains.
1. Calculate the fee for xcm remote execution
2. Transfer xcm fee to target sovereign account
3. Assemble xcm that needs to be executed remotely
4. Send xcm to target chain
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `Target` | 
| message | `Box<VersionedXcm<<T as frame_system::Config>::Call>>` | 

#### Python
```python
call = substrate.compose_call(
    'MessageRouter', 'forward', {
    'message': {
        'V0': {
            'HrmpChannelAccepted': {
                'recipient': 'u32',
            },
            'HrmpChannelClosing': {
                'initiator': 'u32',
                'recipient': 'u32',
                'sender': 'u32',
            },
            'HrmpNewChannelOpenRequest': {
                'max_capacity': 'u32',
                'max_message_size': 'u32',
                'sender': 'u32',
            },
            'QueryResponse': {
                'query_id': 'u64',
                'response': {
                    'Assets': [
                        {
                            'AbstractFungible': 'InnerStruct',
                            'AbstractNonFungible': 'InnerStruct',
                            'All': None,
                            'AllAbstractFungible': 'InnerStruct',
                            'AllAbstractNonFungible': 'InnerStruct',
                            'AllConcreteFungible': 'InnerStruct',
                            'AllConcreteNonFungible': 'InnerStruct',
                            'AllFungible': None,
                            'AllNonFungible': None,
                            'ConcreteFungible': 'InnerStruct',
                            'ConcreteNonFungible': 'InnerStruct',
                            'None': None,
                        },
                    ],
                },
            },
            'RelayedFrom': {
                'message': {
                    'HrmpChannelAccepted': {
                        'recipient': 'u32',
                    },
                    'HrmpChannelClosing': {
                        'initiator': 'u32',
                        'recipient': 'u32',
                        'sender': 'u32',
                    },
                    'HrmpNewChannelOpenRequest': {
                        'max_capacity': 'u32',
                        'max_message_size': 'u32',
                        'sender': 'u32',
                    },
                    'QueryResponse': {
                        'query_id': 'u64',
                        'response': {
                            'Assets': [
                                'scale_info::77',
                            ],
                        },
                    },
                    'RelayedFrom': {
                        'message': {
                            'HrmpChannelAccepted': 'InnerStruct',
                            'HrmpChannelClosing': 'InnerStruct',
                            'HrmpNewChannelOpenRequest': 'InnerStruct',
                            'QueryResponse': 'InnerStruct',
                            'RelayedFrom': 'InnerStruct',
                            'ReserveAssetDeposit': 'InnerStruct',
                            'TeleportAsset': 'InnerStruct',
                            'Transact': 'InnerStruct',
                            'TransferAsset': 'InnerStruct',
                            'TransferReserveAsset': 'InnerStruct',
                            'WithdrawAsset': 'InnerStruct',
                        },
                        'who': {
                            'Null': None,
                            'X1': 'scale_info::79',
                            'X2': (
                                'scale_info::79',
                                'scale_info::79',
                            ),
                            'X3': (
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                            ),
                            'X4': (
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                            ),
                            'X5': (
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                            ),
                            'X6': (
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                            ),
                            'X7': (
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                            ),
                            'X8': (
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                            ),
                        },
                    },
                    'ReserveAssetDeposit': {
                        'assets': [
                            'scale_info::77',
                        ],
                        'effects': [
                            'scale_info::225',
                        ],
                    },
                    'TeleportAsset': {
                        'assets': [
                            'scale_info::77',
                        ],
                        'effects': [
                            'scale_info::225',
                        ],
                    },
                    'Transact': {
                        'call': {
                            'encoded': 'Bytes',
                        },
                        'origin_type': (
                            'Native',
                            'SovereignAccount',
                            'Superuser',
                            'Xcm',
                        ),
                        'require_weight_at_most': 'u64',
                    },
                    'TransferAsset': {
                        'assets': [
                            'scale_info::77',
                        ],
                        'dest': {
                            'Null': None,
                            'X1': 'scale_info::79',
                            'X2': (
                                'scale_info::79',
                                'scale_info::79',
                            ),
                            'X3': (
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                            ),
                            'X4': (
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                            ),
                            'X5': (
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                            ),
                            'X6': (
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                            ),
                            'X7': (
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                            ),
                            'X8': (
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                            ),
                        },
                    },
                    'TransferReserveAsset': {
                        'assets': [
                            'scale_info::77',
                        ],
                        'dest': {
                            'Null': None,
                            'X1': 'scale_info::79',
                            'X2': (
                                'scale_info::79',
                                'scale_info::79',
                            ),
                            'X3': (
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                            ),
                            'X4': (
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                            ),
                            'X5': (
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                            ),
                            'X6': (
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                            ),
                            'X7': (
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                            ),
                            'X8': (
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                                'scale_info::79',
                            ),
                        },
                        'effects': [
                            'scale_info::214',
                        ],
                    },
                    'WithdrawAsset': {
                        'assets': [
                            'scale_info::77',
                        ],
                        'effects': [
                            'scale_info::225',
                        ],
                    },
                },
                'who': {
                    'Null': None,
                    'X1': {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::47',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::47',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::47',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Parent': None,
                        'Plurality': {
                            'id': 'scale_info::52',
                            'part': 'scale_info::53',
                        },
                    },
                    'X2': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X3': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X4': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X5': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X6': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X7': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X8': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                },
            },
            'ReserveAssetDeposit': {
                'assets': [
                    {
                        'AbstractFungible': {
                            'amount': 'u128',
                            'id': 'Bytes',
                        },
                        'AbstractNonFungible': {
                            'class': 'Bytes',
                            'instance': 'scale_info::62',
                        },
                        'All': None,
                        'AllAbstractFungible': {
                            'id': 'Bytes',
                        },
                        'AllAbstractNonFungible': {
                            'class': 'Bytes',
                        },
                        'AllConcreteFungible': {
                            'id': 'scale_info::78',
                        },
                        'AllConcreteNonFungible': {
                            'class': 'scale_info::78',
                        },
                        'AllFungible': None,
                        'AllNonFungible': None,
                        'ConcreteFungible': {
                            'amount': 'u128',
                            'id': 'scale_info::78',
                        },
                        'ConcreteNonFungible': {
                            'class': 'scale_info::78',
                            'instance': 'scale_info::62',
                        },
                        'None': None,
                    },
                ],
                'effects': [
                    {
                        'BuyExecution': {
                            'debt': 'u64',
                            'fees': 'scale_info::77',
                            'halt_on_error': 'bool',
                            'weight': 'u64',
                            'xcm': [
                                'scale_info::223',
                            ],
                        },
                        'DepositAsset': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'dest': 'scale_info::78',
                        },
                        'DepositReserveAsset': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'dest': 'scale_info::78',
                            'effects': [
                                'scale_info::214',
                            ],
                        },
                        'ExchangeAsset': {
                            'give': [
                                'scale_info::77',
                            ],
                            'receive': [
                                'scale_info::77',
                            ],
                        },
                        'InitiateReserveWithdraw': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'effects': [
                                'scale_info::214',
                            ],
                            'reserve': 'scale_info::78',
                        },
                        'InitiateTeleport': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'dest': 'scale_info::78',
                            'effects': [
                                'scale_info::214',
                            ],
                        },
                        'Null': None,
                        'QueryHolding': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'dest': 'scale_info::78',
                            'query_id': 'u64',
                        },
                    },
                ],
            },
            'TeleportAsset': {
                'assets': [
                    {
                        'AbstractFungible': {
                            'amount': 'u128',
                            'id': 'Bytes',
                        },
                        'AbstractNonFungible': {
                            'class': 'Bytes',
                            'instance': 'scale_info::62',
                        },
                        'All': None,
                        'AllAbstractFungible': {
                            'id': 'Bytes',
                        },
                        'AllAbstractNonFungible': {
                            'class': 'Bytes',
                        },
                        'AllConcreteFungible': {
                            'id': 'scale_info::78',
                        },
                        'AllConcreteNonFungible': {
                            'class': 'scale_info::78',
                        },
                        'AllFungible': None,
                        'AllNonFungible': None,
                        'ConcreteFungible': {
                            'amount': 'u128',
                            'id': 'scale_info::78',
                        },
                        'ConcreteNonFungible': {
                            'class': 'scale_info::78',
                            'instance': 'scale_info::62',
                        },
                        'None': None,
                    },
                ],
                'effects': [
                    {
                        'BuyExecution': {
                            'debt': 'u64',
                            'fees': 'scale_info::77',
                            'halt_on_error': 'bool',
                            'weight': 'u64',
                            'xcm': [
                                'scale_info::223',
                            ],
                        },
                        'DepositAsset': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'dest': 'scale_info::78',
                        },
                        'DepositReserveAsset': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'dest': 'scale_info::78',
                            'effects': [
                                'scale_info::214',
                            ],
                        },
                        'ExchangeAsset': {
                            'give': [
                                'scale_info::77',
                            ],
                            'receive': [
                                'scale_info::77',
                            ],
                        },
                        'InitiateReserveWithdraw': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'effects': [
                                'scale_info::214',
                            ],
                            'reserve': 'scale_info::78',
                        },
                        'InitiateTeleport': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'dest': 'scale_info::78',
                            'effects': [
                                'scale_info::214',
                            ],
                        },
                        'Null': None,
                        'QueryHolding': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'dest': 'scale_info::78',
                            'query_id': 'u64',
                        },
                    },
                ],
            },
            'Transact': {
                'call': {
                    'encoded': 'Bytes',
                },
                'origin_type': (
                    'Native',
                    'SovereignAccount',
                    'Superuser',
                    'Xcm',
                ),
                'require_weight_at_most': 'u64',
            },
            'TransferAsset': {
                'assets': [
                    {
                        'AbstractFungible': {
                            'amount': 'u128',
                            'id': 'Bytes',
                        },
                        'AbstractNonFungible': {
                            'class': 'Bytes',
                            'instance': 'scale_info::62',
                        },
                        'All': None,
                        'AllAbstractFungible': {
                            'id': 'Bytes',
                        },
                        'AllAbstractNonFungible': {
                            'class': 'Bytes',
                        },
                        'AllConcreteFungible': {
                            'id': 'scale_info::78',
                        },
                        'AllConcreteNonFungible': {
                            'class': 'scale_info::78',
                        },
                        'AllFungible': None,
                        'AllNonFungible': None,
                        'ConcreteFungible': {
                            'amount': 'u128',
                            'id': 'scale_info::78',
                        },
                        'ConcreteNonFungible': {
                            'class': 'scale_info::78',
                            'instance': 'scale_info::62',
                        },
                        'None': None,
                    },
                ],
                'dest': {
                    'Null': None,
                    'X1': {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::47',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::47',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::47',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Parent': None,
                        'Plurality': {
                            'id': 'scale_info::52',
                            'part': 'scale_info::53',
                        },
                    },
                    'X2': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X3': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X4': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X5': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X6': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X7': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X8': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                },
            },
            'TransferReserveAsset': {
                'assets': [
                    {
                        'AbstractFungible': {
                            'amount': 'u128',
                            'id': 'Bytes',
                        },
                        'AbstractNonFungible': {
                            'class': 'Bytes',
                            'instance': 'scale_info::62',
                        },
                        'All': None,
                        'AllAbstractFungible': {
                            'id': 'Bytes',
                        },
                        'AllAbstractNonFungible': {
                            'class': 'Bytes',
                        },
                        'AllConcreteFungible': {
                            'id': 'scale_info::78',
                        },
                        'AllConcreteNonFungible': {
                            'class': 'scale_info::78',
                        },
                        'AllFungible': None,
                        'AllNonFungible': None,
                        'ConcreteFungible': {
                            'amount': 'u128',
                            'id': 'scale_info::78',
                        },
                        'ConcreteNonFungible': {
                            'class': 'scale_info::78',
                            'instance': 'scale_info::62',
                        },
                        'None': None,
                    },
                ],
                'dest': {
                    'Null': None,
                    'X1': {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::47',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::47',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::47',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Parent': None,
                        'Plurality': {
                            'id': 'scale_info::52',
                            'part': 'scale_info::53',
                        },
                    },
                    'X2': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X3': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X4': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X5': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X6': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X7': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                    'X8': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Parent': None,
                            'Plurality': 'InnerStruct',
                        },
                    ),
                },
                'effects': [
                    {
                        'BuyExecution': {
                            'debt': 'u64',
                            'fees': 'scale_info::77',
                            'halt_on_error': 'bool',
                            'weight': 'u64',
                            'xcm': [
                                'scale_info::212',
                            ],
                        },
                        'DepositAsset': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'dest': 'scale_info::78',
                        },
                        'DepositReserveAsset': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'dest': 'scale_info::78',
                            'effects': [
                                'scale_info::214',
                            ],
                        },
                        'ExchangeAsset': {
                            'give': [
                                'scale_info::77',
                            ],
                            'receive': [
                                'scale_info::77',
                            ],
                        },
                        'InitiateReserveWithdraw': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'effects': [
                                'scale_info::214',
                            ],
                            'reserve': 'scale_info::78',
                        },
                        'InitiateTeleport': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'dest': 'scale_info::78',
                            'effects': [
                                'scale_info::214',
                            ],
                        },
                        'Null': None,
                        'QueryHolding': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'dest': 'scale_info::78',
                            'query_id': 'u64',
                        },
                    },
                ],
            },
            'WithdrawAsset': {
                'assets': [
                    {
                        'AbstractFungible': {
                            'amount': 'u128',
                            'id': 'Bytes',
                        },
                        'AbstractNonFungible': {
                            'class': 'Bytes',
                            'instance': 'scale_info::62',
                        },
                        'All': None,
                        'AllAbstractFungible': {
                            'id': 'Bytes',
                        },
                        'AllAbstractNonFungible': {
                            'class': 'Bytes',
                        },
                        'AllConcreteFungible': {
                            'id': 'scale_info::78',
                        },
                        'AllConcreteNonFungible': {
                            'class': 'scale_info::78',
                        },
                        'AllFungible': None,
                        'AllNonFungible': None,
                        'ConcreteFungible': {
                            'amount': 'u128',
                            'id': 'scale_info::78',
                        },
                        'ConcreteNonFungible': {
                            'class': 'scale_info::78',
                            'instance': 'scale_info::62',
                        },
                        'None': None,
                    },
                ],
                'effects': [
                    {
                        'BuyExecution': {
                            'debt': 'u64',
                            'fees': 'scale_info::77',
                            'halt_on_error': 'bool',
                            'weight': 'u64',
                            'xcm': [
                                'scale_info::223',
                            ],
                        },
                        'DepositAsset': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'dest': 'scale_info::78',
                        },
                        'DepositReserveAsset': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'dest': 'scale_info::78',
                            'effects': [
                                'scale_info::214',
                            ],
                        },
                        'ExchangeAsset': {
                            'give': [
                                'scale_info::77',
                            ],
                            'receive': [
                                'scale_info::77',
                            ],
                        },
                        'InitiateReserveWithdraw': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'effects': [
                                'scale_info::214',
                            ],
                            'reserve': 'scale_info::78',
                        },
                        'InitiateTeleport': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'dest': 'scale_info::78',
                            'effects': [
                                'scale_info::214',
                            ],
                        },
                        'Null': None,
                        'QueryHolding': {
                            'assets': [
                                'scale_info::77',
                            ],
                            'dest': 'scale_info::78',
                            'query_id': 'u64',
                        },
                    },
                ],
            },
        },
        'V1': {
            'HrmpChannelAccepted': {
                'recipient': 'u32',
            },
            'HrmpChannelClosing': {
                'initiator': 'u32',
                'recipient': 'u32',
                'sender': 'u32',
            },
            'HrmpNewChannelOpenRequest': {
                'max_capacity': 'u32',
                'max_message_size': 'u32',
                'sender': 'u32',
            },
            'QueryResponse': {
                'query_id': 'u64',
                'response': {
                    'Assets': [
                        'scale_info::59',
                    ],
                    'Version': 'u32',
                },
            },
            'ReceiveTeleportedAsset': {
                'assets': [
                    {
                        'fun': 'scale_info::61',
                        'id': 'scale_info::60',
                    },
                ],
                'effects': [
                    {
                        'BuyExecution': {
                            'debt': 'u64',
                            'fees': 'scale_info::59',
                            'halt_on_error': 'bool',
                            'instructions': [
                                'scale_info::228',
                            ],
                            'weight': 'u64',
                        },
                        'DepositAsset': {
                            'assets': 'scale_info::70',
                            'beneficiary': 'scale_info::43',
                            'max_assets': 'u32',
                        },
                        'DepositReserveAsset': {
                            'assets': 'scale_info::70',
                            'dest': 'scale_info::43',
                            'effects': [
                                'scale_info::219',
                            ],
                            'max_assets': 'u32',
                        },
                        'ExchangeAsset': {
                            'give': 'scale_info::70',
                            'receive': [
                                'scale_info::59',
                            ],
                        },
                        'InitiateReserveWithdraw': {
                            'assets': 'scale_info::70',
                            'effects': [
                                'scale_info::219',
                            ],
                            'reserve': 'scale_info::43',
                        },
                        'InitiateTeleport': {
                            'assets': 'scale_info::70',
                            'dest': 'scale_info::43',
                            'effects': [
                                'scale_info::219',
                            ],
                        },
                        'Noop': None,
                        'QueryHolding': {
                            'assets': 'scale_info::70',
                            'dest': 'scale_info::43',
                            'query_id': 'u64',
                        },
                    },
                ],
            },
            'RelayedFrom': {
                'message': {
                    'HrmpChannelAccepted': {
                        'recipient': 'u32',
                    },
                    'HrmpChannelClosing': {
                        'initiator': 'u32',
                        'recipient': 'u32',
                        'sender': 'u32',
                    },
                    'HrmpNewChannelOpenRequest': {
                        'max_capacity': 'u32',
                        'max_message_size': 'u32',
                        'sender': 'u32',
                    },
                    'QueryResponse': {
                        'query_id': 'u64',
                        'response': {
                            'Assets': [
                                'scale_info::59',
                            ],
                            'Version': 'u32',
                        },
                    },
                    'ReceiveTeleportedAsset': {
                        'assets': [
                            'scale_info::59',
                        ],
                        'effects': [
                            'scale_info::230',
                        ],
                    },
                    'RelayedFrom': {
                        'message': {
                            'HrmpChannelAccepted': 'InnerStruct',
                            'HrmpChannelClosing': 'InnerStruct',
                            'HrmpNewChannelOpenRequest': 'InnerStruct',
                            'QueryResponse': 'InnerStruct',
                            'ReceiveTeleportedAsset': 'InnerStruct',
                            'RelayedFrom': 'InnerStruct',
                            'ReserveAssetDeposited': 'InnerStruct',
                            'SubscribeVersion': 'InnerStruct',
                            'Transact': 'InnerStruct',
                            'TransferAsset': 'InnerStruct',
                            'TransferReserveAsset': 'InnerStruct',
                            'UnsubscribeVersion': None,
                            'WithdrawAsset': 'InnerStruct',
                        },
                        'who': {
                            'Here': None,
                            'X1': 'scale_info::45',
                            'X2': (
                                'scale_info::45',
                                'scale_info::45',
                            ),
                            'X3': (
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                            ),
                            'X4': (
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                            ),
                            'X5': (
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                            ),
                            'X6': (
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                            ),
                            'X7': (
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                            ),
                            'X8': (
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                                'scale_info::45',
                            ),
                        },
                    },
                    'ReserveAssetDeposited': {
                        'assets': [
                            'scale_info::59',
                        ],
                        'effects': [
                            'scale_info::230',
                        ],
                    },
                    'SubscribeVersion': {
                        'max_response_weight': 'u64',
                        'query_id': 'u64',
                    },
                    'Transact': {
                        'call': {
                            'encoded': 'Bytes',
                        },
                        'origin_type': (
                            'Native',
                            'SovereignAccount',
                            'Superuser',
                            'Xcm',
                        ),
                        'require_weight_at_most': 'u64',
                    },
                    'TransferAsset': {
                        'assets': [
                            'scale_info::59',
                        ],
                        'beneficiary': {
                            'interior': 'scale_info::44',
                            'parents': 'u8',
                        },
                    },
                    'TransferReserveAsset': {
                        'assets': [
                            'scale_info::59',
                        ],
                        'dest': {
                            'interior': 'scale_info::44',
                            'parents': 'u8',
                        },
                        'effects': [
                            'scale_info::219',
                        ],
                    },
                    'UnsubscribeVersion': None,
                    'WithdrawAsset': {
                        'assets': [
                            'scale_info::59',
                        ],
                        'effects': [
                            'scale_info::230',
                        ],
                    },
                },
                'who': {
                    'Here': None,
                    'X1': {
                        'AccountId32': {
                            'id': '[u8; 32]',
                            'network': 'scale_info::47',
                        },
                        'AccountIndex64': {
                            'index': 'u64',
                            'network': 'scale_info::47',
                        },
                        'AccountKey20': {
                            'key': '[u8; 20]',
                            'network': 'scale_info::47',
                        },
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': {
                            'id': 'scale_info::52',
                            'part': 'scale_info::53',
                        },
                    },
                    'X2': (
                        {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
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
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                    ),
                },
            },
            'ReserveAssetDeposited': {
                'assets': [
                    {
                        'fun': 'scale_info::61',
                        'id': 'scale_info::60',
                    },
                ],
                'effects': [
                    {
                        'BuyExecution': {
                            'debt': 'u64',
                            'fees': 'scale_info::59',
                            'halt_on_error': 'bool',
                            'instructions': [
                                'scale_info::228',
                            ],
                            'weight': 'u64',
                        },
                        'DepositAsset': {
                            'assets': 'scale_info::70',
                            'beneficiary': 'scale_info::43',
                            'max_assets': 'u32',
                        },
                        'DepositReserveAsset': {
                            'assets': 'scale_info::70',
                            'dest': 'scale_info::43',
                            'effects': [
                                'scale_info::219',
                            ],
                            'max_assets': 'u32',
                        },
                        'ExchangeAsset': {
                            'give': 'scale_info::70',
                            'receive': [
                                'scale_info::59',
                            ],
                        },
                        'InitiateReserveWithdraw': {
                            'assets': 'scale_info::70',
                            'effects': [
                                'scale_info::219',
                            ],
                            'reserve': 'scale_info::43',
                        },
                        'InitiateTeleport': {
                            'assets': 'scale_info::70',
                            'dest': 'scale_info::43',
                            'effects': [
                                'scale_info::219',
                            ],
                        },
                        'Noop': None,
                        'QueryHolding': {
                            'assets': 'scale_info::70',
                            'dest': 'scale_info::43',
                            'query_id': 'u64',
                        },
                    },
                ],
            },
            'SubscribeVersion': {
                'max_response_weight': 'u64',
                'query_id': 'u64',
            },
            'Transact': {
                'call': {
                    'encoded': 'Bytes',
                },
                'origin_type': (
                    'Native',
                    'SovereignAccount',
                    'Superuser',
                    'Xcm',
                ),
                'require_weight_at_most': 'u64',
            },
            'TransferAsset': {
                'assets': [
                    {
                        'fun': 'scale_info::61',
                        'id': 'scale_info::60',
                    },
                ],
                'beneficiary': {
                    'interior': {
                        'Here': None,
                        'X1': {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        'X2': (
                            'scale_info::45',
                            'scale_info::45',
                        ),
                        'X3': (
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                        ),
                        'X4': (
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                        ),
                        'X5': (
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                        ),
                        'X6': (
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                        ),
                        'X7': (
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                        ),
                        'X8': (
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                        ),
                    },
                    'parents': 'u8',
                },
            },
            'TransferReserveAsset': {
                'assets': [
                    {
                        'fun': 'scale_info::61',
                        'id': 'scale_info::60',
                    },
                ],
                'dest': {
                    'interior': {
                        'Here': None,
                        'X1': {
                            'AccountId32': 'InnerStruct',
                            'AccountIndex64': 'InnerStruct',
                            'AccountKey20': 'InnerStruct',
                            'GeneralIndex': 'u128',
                            'GeneralKey': 'Bytes',
                            'OnlyChild': None,
                            'PalletInstance': 'u8',
                            'Parachain': 'u32',
                            'Plurality': 'InnerStruct',
                        },
                        'X2': (
                            'scale_info::45',
                            'scale_info::45',
                        ),
                        'X3': (
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                        ),
                        'X4': (
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                        ),
                        'X5': (
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                        ),
                        'X6': (
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                        ),
                        'X7': (
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                        ),
                        'X8': (
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                            'scale_info::45',
                        ),
                    },
                    'parents': 'u8',
                },
                'effects': [
                    {
                        'BuyExecution': {
                            'debt': 'u64',
                            'fees': 'scale_info::59',
                            'halt_on_error': 'bool',
                            'instructions': [
                                'scale_info::217',
                            ],
                            'weight': 'u64',
                        },
                        'DepositAsset': {
                            'assets': 'scale_info::70',
                            'beneficiary': 'scale_info::43',
                            'max_assets': 'u32',
                        },
                        'DepositReserveAsset': {
                            'assets': 'scale_info::70',
                            'dest': 'scale_info::43',
                            'effects': [
                                'scale_info::219',
                            ],
                            'max_assets': 'u32',
                        },
                        'ExchangeAsset': {
                            'give': 'scale_info::70',
                            'receive': [
                                'scale_info::59',
                            ],
                        },
                        'InitiateReserveWithdraw': {
                            'assets': 'scale_info::70',
                            'effects': [
                                'scale_info::219',
                            ],
                            'reserve': 'scale_info::43',
                        },
                        'InitiateTeleport': {
                            'assets': 'scale_info::70',
                            'dest': 'scale_info::43',
                            'effects': [
                                'scale_info::219',
                            ],
                        },
                        'Noop': None,
                        'QueryHolding': {
                            'assets': 'scale_info::70',
                            'dest': 'scale_info::43',
                            'query_id': 'u64',
                        },
                    },
                ],
            },
            'UnsubscribeVersion': None,
            'WithdrawAsset': {
                'assets': [
                    {
                        'fun': 'scale_info::61',
                        'id': 'scale_info::60',
                    },
                ],
                'effects': [
                    {
                        'BuyExecution': {
                            'debt': 'u64',
                            'fees': 'scale_info::59',
                            'halt_on_error': 'bool',
                            'instructions': [
                                'scale_info::228',
                            ],
                            'weight': 'u64',
                        },
                        'DepositAsset': {
                            'assets': 'scale_info::70',
                            'beneficiary': 'scale_info::43',
                            'max_assets': 'u32',
                        },
                        'DepositReserveAsset': {
                            'assets': 'scale_info::70',
                            'dest': 'scale_info::43',
                            'effects': [
                                'scale_info::219',
                            ],
                            'max_assets': 'u32',
                        },
                        'ExchangeAsset': {
                            'give': 'scale_info::70',
                            'receive': [
                                'scale_info::59',
                            ],
                        },
                        'InitiateReserveWithdraw': {
                            'assets': 'scale_info::70',
                            'effects': [
                                'scale_info::219',
                            ],
                            'reserve': 'scale_info::43',
                        },
                        'InitiateTeleport': {
                            'assets': 'scale_info::70',
                            'dest': 'scale_info::43',
                            'effects': [
                                'scale_info::219',
                            ],
                        },
                        'Noop': None,
                        'QueryHolding': {
                            'assets': 'scale_info::70',
                            'dest': 'scale_info::43',
                            'query_id': 'u64',
                        },
                    },
                ],
            },
        },
        'V2': [
            {
                'BuyExecution': {
                    'fees': {
                        'fun': 'scale_info::61',
                        'id': 'scale_info::60',
                    },
                    'weight_limit': {
                        'Limited': 'u64',
                        'Unlimited': None,
                    },
                },
                'ClaimAsset': {
                    'assets': [
                        'scale_info::59',
                    ],
                    'ticket': {
                        'interior': 'scale_info::44',
                        'parents': 'u8',
                    },
                },
                'ClearError': None,
                'ClearOrigin': None,
                'DepositAsset': {
                    'assets': {
                        'Definite': [
                            'scale_info::59',
                        ],
                        'Wild': 'scale_info::71',
                    },
                    'beneficiary': {
                        'interior': 'scale_info::44',
                        'parents': 'u8',
                    },
                    'max_assets': 'u32',
                },
                'DepositReserveAsset': {
                    'assets': {
                        'Definite': [
                            'scale_info::59',
                        ],
                        'Wild': 'scale_info::71',
                    },
                    'dest': {
                        'interior': 'scale_info::44',
                        'parents': 'u8',
                    },
                    'max_assets': 'u32',
                    'xcm': [
                        'scale_info::56',
                    ],
                },
                'DescendOrigin': {
                    'Here': None,
                    'X1': {
                        'AccountId32': 'InnerStruct',
                        'AccountIndex64': 'InnerStruct',
                        'AccountKey20': 'InnerStruct',
                        'GeneralIndex': 'u128',
                        'GeneralKey': 'Bytes',
                        'OnlyChild': None,
                        'PalletInstance': 'u8',
                        'Parachain': 'u32',
                        'Plurality': 'InnerStruct',
                    },
                    'X2': (
                        'scale_info::45',
                        'scale_info::45',
                    ),
                    'X3': (
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                    ),
                    'X4': (
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                    ),
                    'X5': (
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                    ),
                    'X6': (
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                    ),
                    'X7': (
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                    ),
                    'X8': (
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                        'scale_info::45',
                    ),
                },
                'ExchangeAsset': {
                    'give': {
                        'Definite': [
                            'scale_info::59',
                        ],
                        'Wild': 'scale_info::71',
                    },
                    'receive': [
                        'scale_info::59',
                    ],
                },
                'HrmpChannelAccepted': {
                    'recipient': 'u32',
                },
                'HrmpChannelClosing': {
                    'initiator': 'u32',
                    'recipient': 'u32',
                    'sender': 'u32',
                },
                'HrmpNewChannelOpenRequest': {
                    'max_capacity': 'u32',
                    'max_message_size': 'u32',
                    'sender': 'u32',
                },
                'InitiateReserveWithdraw': {
                    'assets': {
                        'Definite': [
                            'scale_info::59',
                        ],
                        'Wild': 'scale_info::71',
                    },
                    'reserve': {
                        'interior': 'scale_info::44',
                        'parents': 'u8',
                    },
                    'xcm': [
                        'scale_info::56',
                    ],
                },
                'InitiateTeleport': {
                    'assets': {
                        'Definite': [
                            'scale_info::59',
                        ],
                        'Wild': 'scale_info::71',
                    },
                    'dest': {
                        'interior': 'scale_info::44',
                        'parents': 'u8',
                    },
                    'xcm': [
                        'scale_info::56',
                    ],
                },
                'QueryHolding': {
                    'assets': {
                        'Definite': [
                            'scale_info::59',
                        ],
                        'Wild': 'scale_info::71',
                    },
                    'dest': {
                        'interior': 'scale_info::44',
                        'parents': 'u8',
                    },
                    'max_response_weight': 'u64',
                    'query_id': 'u64',
                },
                'QueryResponse': {
                    'max_weight': 'u64',
                    'query_id': 'u64',
                    'response': {
                        'Assets': [
                            'scale_info::59',
                        ],
                        'ExecutionResult': (
                            None,
                            (
                                'u32',
                                'scale_info::39',
                            ),
                        ),
                        'Null': None,
                        'Version': 'u32',
                    },
                },
                'ReceiveTeleportedAsset': [
                    'scale_info::59',
                ],
                'RefundSurplus': None,
                'ReportError': {
                    'dest': {
                        'interior': 'scale_info::44',
                        'parents': 'u8',
                    },
                    'max_response_weight': 'u64',
                    'query_id': 'u64',
                },
                'ReserveAssetDeposited': [
                    'scale_info::59',
                ],
                'SetAppendix': [
                    'scale_info::234',
                ],
                'SetErrorHandler': [
                    'scale_info::234',
                ],
                'SubscribeVersion': {
                    'max_response_weight': 'u64',
                    'query_id': 'u64',
                },
                'Transact': {
                    'call': {
                        'encoded': 'Bytes',
                    },
                    'origin_type': (
                        'Native',
                        'SovereignAccount',
                        'Superuser',
                        'Xcm',
                    ),
                    'require_weight_at_most': 'u64',
                },
                'TransferAsset': {
                    'assets': [
                        'scale_info::59',
                    ],
                    'beneficiary': {
                        'interior': 'scale_info::44',
                        'parents': 'u8',
                    },
                },
                'TransferReserveAsset': {
                    'assets': [
                        'scale_info::59',
                    ],
                    'dest': {
                        'interior': 'scale_info::44',
                        'parents': 'u8',
                    },
                    'xcm': [
                        'scale_info::56',
                    ],
                },
                'Trap': 'u64',
                'UnsubscribeVersion': None,
                'WithdrawAsset': [
                    'scale_info::59',
                ],
            },
        ],
    },
    'target': ('Moonbeam', 'Astar'),
}
)
```

---------
### set_target_xcm_exec_config
Update the units per second of local asset used in target chain.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target_location | `MultiLocation` | 
| local_asset_units_per_second | `AssetUnitsPerSecond` | 

#### Python
```python
call = substrate.compose_call(
    'MessageRouter', 'set_target_xcm_exec_config', {
    'local_asset_units_per_second': 'u128',
    'target_location': {
        'interior': {
            'Here': None,
            'X1': {
                'AccountId32': {
                    'id': '[u8; 32]',
                    'network': {
                        'Any': None,
                        'Kusama': None,
                        'Named': 'Bytes',
                        'Polkadot': None,
                    },
                },
                'AccountIndex64': {
                    'index': 'u64',
                    'network': {
                        'Any': None,
                        'Kusama': None,
                        'Named': 'Bytes',
                        'Polkadot': None,
                    },
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': {
                        'Any': None,
                        'Kusama': None,
                        'Named': 'Bytes',
                        'Polkadot': None,
                    },
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': {
                        'Executive': None,
                        'Index': 'u32',
                        'Judicial': None,
                        'Legislative': None,
                        'Named': 'Bytes',
                        'Technical': None,
                        'Unit': None,
                    },
                    'part': {
                        'AtLeastProportion': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Fraction': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Members': {
                            'count': 'u32',
                        },
                        'MoreThanProportion': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Voice': None,
                    },
                },
            },
            'X2': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
            'X3': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
            'X4': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
            'X5': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
            'X6': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
            'X7': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
            'X8': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
        },
        'parents': 'u8',
    },
}
)
```

---------
## Events

---------
### ForwardTo
Deposited when successfully routed.
(send origin, route target, remote xcm, required weight, tokens used)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MultiLocation` | ```{'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': {'Any': None, 'Named': 'Bytes', 'Polkadot': None, 'Kusama': None}, 'id': '[u8; 32]'}, 'AccountIndex64': {'network': {'Any': None, 'Named': 'Bytes', 'Polkadot': None, 'Kusama': None}, 'index': 'u64'}, 'AccountKey20': {'network': {'Any': None, 'Named': 'Bytes', 'Polkadot': None, 'Kusama': None}, 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': {'Unit': None, 'Named': 'Bytes', 'Index': 'u32', 'Executive': None, 'Technical': None, 'Legislative': None, 'Judicial': None}, 'part': {'Voice': None, 'Members': 'InnerStruct', 'Fraction': 'InnerStruct', 'AtLeastProportion': 'InnerStruct', 'MoreThanProportion': 'InnerStruct'}}}, 'X2': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}), 'X3': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}), 'X4': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}), 'X5': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}), 'X6': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}), 'X7': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}), 'X8': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}})}}```
| None | `Target` | ```('Moonbeam', 'Astar')```
| None | `Xcm<()>` | ```[{'WithdrawAsset': ['scale_info::59'], 'ReserveAssetDeposited': ['scale_info::59'], 'ReceiveTeleportedAsset': ['scale_info::59'], 'QueryResponse': {'query_id': 'u64', 'response': {'Null': None, 'Assets': ['scale_info::59'], 'ExecutionResult': (None, ('u32', 'scale_info::39')), 'Version': 'u32'}, 'max_weight': 'u64'}, 'TransferAsset': {'assets': ['scale_info::59'], 'beneficiary': {'parents': 'u8', 'interior': 'scale_info::44'}}, 'TransferReserveAsset': {'assets': ['scale_info::59'], 'dest': {'parents': 'u8', 'interior': 'scale_info::44'}, 'xcm': ['scale_info::56']}, 'Transact': {'origin_type': ('Native', 'SovereignAccount', 'Superuser', 'Xcm'), 'require_weight_at_most': 'u64', 'call': {'encoded': 'Bytes'}}, 'HrmpNewChannelOpenRequest': {'sender': 'u32', 'max_message_size': 'u32', 'max_capacity': 'u32'}, 'HrmpChannelAccepted': {'recipient': 'u32'}, 'HrmpChannelClosing': {'initiator': 'u32', 'sender': 'u32', 'recipient': 'u32'}, 'ClearOrigin': None, 'DescendOrigin': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': 'InnerStruct', 'AccountIndex64': 'InnerStruct', 'AccountKey20': 'InnerStruct', 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': 'InnerStruct'}, 'X2': ('scale_info::45', 'scale_info::45'), 'X3': ('scale_info::45', 'scale_info::45', 'scale_info::45'), 'X4': ('scale_info::45', 'scale_info::45', 'scale_info::45', 'scale_info::45'), 'X5': ('scale_info::45', 'scale_info::45', 'scale_info::45', 'scale_info::45', 'scale_info::45'), 'X6': ('scale_info::45', 'scale_info::45', 'scale_info::45', 'scale_info::45', 'scale_info::45', 'scale_info::45'), 'X7': ('scale_info::45', 'scale_info::45', 'scale_info::45', 'scale_info::45', 'scale_info::45', 'scale_info::45', 'scale_info::45'), 'X8': ('scale_info::45', 'scale_info::45', 'scale_info::45', 'scale_info::45', 'scale_info::45', 'scale_info::45', 'scale_info::45', 'scale_info::45')}, 'ReportError': {'query_id': 'u64', 'dest': {'parents': 'u8', 'interior': 'scale_info::44'}, 'max_response_weight': 'u64'}, 'DepositAsset': {'assets': {'Definite': ['scale_info::59'], 'Wild': 'scale_info::71'}, 'max_assets': 'u32', 'beneficiary': {'parents': 'u8', 'interior': 'scale_info::44'}}, 'DepositReserveAsset': {'assets': {'Definite': ['scale_info::59'], 'Wild': 'scale_info::71'}, 'max_assets': 'u32', 'dest': {'parents': 'u8', 'interior': 'scale_info::44'}, 'xcm': ['scale_info::56']}, 'ExchangeAsset': {'give': {'Definite': ['scale_info::59'], 'Wild': 'scale_info::71'}, 'receive': ['scale_info::59']}, 'InitiateReserveWithdraw': {'assets': {'Definite': ['scale_info::59'], 'Wild': 'scale_info::71'}, 'reserve': {'parents': 'u8', 'interior': 'scale_info::44'}, 'xcm': ['scale_info::56']}, 'InitiateTeleport': {'assets': {'Definite': ['scale_info::59'], 'Wild': 'scale_info::71'}, 'dest': {'parents': 'u8', 'interior': 'scale_info::44'}, 'xcm': ['scale_info::56']}, 'QueryHolding': {'query_id': 'u64', 'dest': {'parents': 'u8', 'interior': 'scale_info::44'}, 'assets': {'Definite': ['scale_info::59'], 'Wild': 'scale_info::71'}, 'max_response_weight': 'u64'}, 'BuyExecution': {'fees': {'id': 'scale_info::60', 'fun': 'scale_info::61'}, 'weight_limit': {'Unlimited': None, 'Limited': 'u64'}}, 'RefundSurplus': None, 'SetErrorHandler': ['scale_info::56'], 'SetAppendix': ['scale_info::56'], 'ClearError': None, 'ClaimAsset': {'assets': ['scale_info::59'], 'ticket': {'parents': 'u8', 'interior': 'scale_info::44'}}, 'Trap': 'u64', 'SubscribeVersion': {'query_id': 'u64', 'max_response_weight': 'u64'}, 'UnsubscribeVersion': None}]```
| None | `Weight` | ```u64```
| None | `u128` | ```u128```

---------
### TargetXcmExecConfigChanged
Changed the amount of units target chain charging per execution second for local asset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| target_location | `MultiLocation` | ```{'parents': 'u8', 'interior': {'Here': None, 'X1': {'Parachain': 'u32', 'AccountId32': {'network': {'Any': None, 'Named': 'Bytes', 'Polkadot': None, 'Kusama': None}, 'id': '[u8; 32]'}, 'AccountIndex64': {'network': {'Any': None, 'Named': 'Bytes', 'Polkadot': None, 'Kusama': None}, 'index': 'u64'}, 'AccountKey20': {'network': {'Any': None, 'Named': 'Bytes', 'Polkadot': None, 'Kusama': None}, 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': {'Unit': None, 'Named': 'Bytes', 'Index': 'u32', 'Executive': None, 'Technical': None, 'Legislative': None, 'Judicial': None}, 'part': {'Voice': None, 'Members': 'InnerStruct', 'Fraction': 'InnerStruct', 'AtLeastProportion': 'InnerStruct', 'MoreThanProportion': 'InnerStruct'}}}, 'X2': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}), 'X3': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}), 'X4': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}), 'X5': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}), 'X6': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}), 'X7': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}), 'X8': ({'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}}, {'Parachain': 'u32', 'AccountId32': {'network': 'scale_info::47', 'id': '[u8; 32]'}, 'AccountIndex64': {'network': 'scale_info::47', 'index': 'u64'}, 'AccountKey20': {'network': 'scale_info::47', 'key': '[u8; 20]'}, 'PalletInstance': 'u8', 'GeneralIndex': 'u128', 'GeneralKey': 'Bytes', 'OnlyChild': None, 'Plurality': {'id': 'scale_info::52', 'part': 'scale_info::53'}})}}```
| local_asset_units_per_second | `AssetUnitsPerSecond` | ```u128```

---------
## Storage functions

---------
### TargetXcmExecConfig
 Stores the units per second executed by the target chain for local asset(e.g. CRAB).
 This is used to know how to pay for XCM remote execution use local asset.
 For example:
 key: {parents: 1, Parachain(2023)}, val: 14719736222326895902025
 represents the units per second of CRAB token on moonriver

#### Python
```python
result = substrate.query(
    'MessageRouter', 'TargetXcmExecConfig', [
    {
        'interior': {
            'Here': None,
            'X1': {
                'AccountId32': {
                    'id': '[u8; 32]',
                    'network': {
                        'Any': None,
                        'Kusama': None,
                        'Named': 'Bytes',
                        'Polkadot': None,
                    },
                },
                'AccountIndex64': {
                    'index': 'u64',
                    'network': {
                        'Any': None,
                        'Kusama': None,
                        'Named': 'Bytes',
                        'Polkadot': None,
                    },
                },
                'AccountKey20': {
                    'key': '[u8; 20]',
                    'network': {
                        'Any': None,
                        'Kusama': None,
                        'Named': 'Bytes',
                        'Polkadot': None,
                    },
                },
                'GeneralIndex': 'u128',
                'GeneralKey': 'Bytes',
                'OnlyChild': None,
                'PalletInstance': 'u8',
                'Parachain': 'u32',
                'Plurality': {
                    'id': {
                        'Executive': None,
                        'Index': 'u32',
                        'Judicial': None,
                        'Legislative': None,
                        'Named': 'Bytes',
                        'Technical': None,
                        'Unit': None,
                    },
                    'part': {
                        'AtLeastProportion': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Fraction': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Members': {
                            'count': 'u32',
                        },
                        'MoreThanProportion': {
                            'denom': 'u32',
                            'nom': 'u32',
                        },
                        'Voice': None,
                    },
                },
            },
            'X2': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
            'X3': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
            'X4': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
            'X5': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
            'X6': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
            'X7': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
            'X8': (
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
                {
                    'AccountId32': {
                        'id': '[u8; 32]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountIndex64': {
                        'index': 'u64',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'AccountKey20': {
                        'key': '[u8; 20]',
                        'network': {
                            'Any': None,
                            'Kusama': None,
                            'Named': 'Bytes',
                            'Polkadot': None,
                        },
                    },
                    'GeneralIndex': 'u128',
                    'GeneralKey': 'Bytes',
                    'OnlyChild': None,
                    'PalletInstance': 'u8',
                    'Parachain': 'u32',
                    'Plurality': {
                        'id': {
                            'Executive': None,
                            'Index': 'u32',
                            'Judicial': None,
                            'Legislative': None,
                            'Named': 'Bytes',
                            'Technical': None,
                            'Unit': None,
                        },
                        'part': {
                            'AtLeastProportion': 'InnerStruct',
                            'Fraction': 'InnerStruct',
                            'Members': 'InnerStruct',
                            'MoreThanProportion': 'InnerStruct',
                            'Voice': None,
                        },
                    },
                },
            ),
        },
        'parents': 'u8',
    },
]
)
```

#### Return value
```python
'u128'
```
---------
## Errors

---------
### AccountIdConversionFailed
Failed to convert account id to [u8; 32].

---------
### BadVersion

---------
### FailedPayXcmFee
Failed to transfer xcm fee.

---------
### MultiLocationFull
MultiLocation value too large to descend further.

---------
### TargetXcmExecNotConfig
Not config the target paraId&\#x27;s info for XCM execution.

---------
### UnweighableMessage
The message&\#x27;s weight could not be determined.

---------
### XcmSendFailed
Failed to send xcm.

---------