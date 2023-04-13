
# Settlement

---------
## Calls

---------
### add_and_affirm_instruction
Deprecated. Use `add_and_affirm_instruction_with_memo` instead.
Adds and affirms a new instruction.

\# Arguments
* `venue_id` - ID of the venue this instruction belongs to.
* `settlement_type` - Defines if the instruction should be settled
   in the next block after receiving all affirmations or waiting till a specific block.
* `trade_date` - Optional date from which people can interact with this instruction.
* `value_date` - Optional date after which the instruction should be settled (not enforced)
* `legs` - Legs included in this instruction.
* `portfolios` - Portfolios that the sender controls and wants to use in this affirmations.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| venue_id | `VenueId` | 
| settlement_type | `SettlementType<T::BlockNumber>` | 
| trade_date | `Option<T::Moment>` | 
| value_date | `Option<T::Moment>` | 
| legs | `Vec<Leg>` | 
| portfolios | `Vec<PortfolioId>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'add_and_affirm_instruction', {
    'legs': [
        {
            'amount': 'u128',
            'asset': '[u8; 12]',
            'from': {
                'did': '[u8; 32]',
                'kind': {
                    'Default': None,
                    'User': 'u64',
                },
            },
            'to': {
                'did': '[u8; 32]',
                'kind': {
                    'Default': None,
                    'User': 'u64',
                },
            },
        },
    ],
    'portfolios': [
        {
            'did': '[u8; 32]',
            'kind': {
                'Default': None,
                'User': 'u64',
            },
        },
    ],
    'settlement_type': {
        'SettleManual': 'u32',
        'SettleOnAffirmation': None,
        'SettleOnBlock': 'u32',
    },
    'trade_date': (None, 'u64'),
    'value_date': (None, 'u64'),
    'venue_id': 'u64',
}
)
```

---------
### add_and_affirm_instruction_with_memo
Adds and affirms a new instruction.

\# Arguments
* `venue_id` - ID of the venue this instruction belongs to.
* `settlement_type` - Defines if the instruction should be settled
   in the next block after receiving all affirmations or waiting till a specific block.
* `trade_date` - Optional date from which people can interact with this instruction.
* `value_date` - Optional date after which the instruction should be settled (not enforced)
* `legs` - Legs included in this instruction.
* `portfolios` - Portfolios that the sender controls and wants to use in this affirmations.
* `memo` - Memo field for this instruction.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| venue_id | `VenueId` | 
| settlement_type | `SettlementType<T::BlockNumber>` | 
| trade_date | `Option<T::Moment>` | 
| value_date | `Option<T::Moment>` | 
| legs | `Vec<Leg>` | 
| portfolios | `Vec<PortfolioId>` | 
| instruction_memo | `Option<InstructionMemo>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'add_and_affirm_instruction_with_memo', {
    'instruction_memo': (
        None,
        '[u8; 32]',
    ),
    'legs': [
        {
            'amount': 'u128',
            'asset': '[u8; 12]',
            'from': {
                'did': '[u8; 32]',
                'kind': {
                    'Default': None,
                    'User': 'u64',
                },
            },
            'to': {
                'did': '[u8; 32]',
                'kind': {
                    'Default': None,
                    'User': 'u64',
                },
            },
        },
    ],
    'portfolios': [
        {
            'did': '[u8; 32]',
            'kind': {
                'Default': None,
                'User': 'u64',
            },
        },
    ],
    'settlement_type': {
        'SettleManual': 'u32',
        'SettleOnAffirmation': None,
        'SettleOnBlock': 'u32',
    },
    'trade_date': (None, 'u64'),
    'value_date': (None, 'u64'),
    'venue_id': 'u64',
}
)
```

---------
### add_and_affirm_instruction_with_memo_v2
Adds and affirms a new instruction.

\# Arguments
* `venue_id` - ID of the venue this instruction belongs to.
* `settlement_type` - Defines if the instruction should be settled
   in the next block after receiving all affirmations or waiting till a specific block.
* `trade_date` - Optional date from which people can interact with this instruction.
* `value_date` - Optional date after which the instruction should be settled (not enforced)
* `legs` - Legs included in this instruction.
* `portfolios` - Portfolios that the sender controls and wants to use in this affirmations.
* `memo` - Memo field for this instruction.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| venue_id | `VenueId` | 
| settlement_type | `SettlementType<T::BlockNumber>` | 
| trade_date | `Option<T::Moment>` | 
| value_date | `Option<T::Moment>` | 
| legs | `Vec<LegV2>` | 
| portfolios | `Vec<PortfolioId>` | 
| instruction_memo | `Option<InstructionMemo>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'add_and_affirm_instruction_with_memo_v2', {
    'instruction_memo': (
        None,
        '[u8; 32]',
    ),
    'legs': [
        {
            'asset': {
                'Fungible': {
                    'amount': 'u128',
                    'ticker': '[u8; 12]',
                },
                'NonFungible': {
                    'ids': ['u64'],
                    'ticker': '[u8; 12]',
                },
            },
            'from': {
                'did': '[u8; 32]',
                'kind': {
                    'Default': None,
                    'User': 'u64',
                },
            },
            'to': {
                'did': '[u8; 32]',
                'kind': {
                    'Default': None,
                    'User': 'u64',
                },
            },
        },
    ],
    'portfolios': [
        {
            'did': '[u8; 32]',
            'kind': {
                'Default': None,
                'User': 'u64',
            },
        },
    ],
    'settlement_type': {
        'SettleManual': 'u32',
        'SettleOnAffirmation': None,
        'SettleOnBlock': 'u32',
    },
    'trade_date': (None, 'u64'),
    'value_date': (None, 'u64'),
    'venue_id': 'u64',
}
)
```

---------
### add_instruction
Deprecated. Use `add_instruction_with_memo` instead.
Adds a new instruction.

\# Arguments
* `venue_id` - ID of the venue this instruction belongs to.
* `settlement_type` - Defines if the instruction should be settled
   in the next block after receiving all affirmations or waiting till a specific block.
* `trade_date` - Optional date from which people can interact with this instruction.
* `value_date` - Optional date after which the instruction should be settled (not enforced)
* `legs` - Legs included in this instruction.

\# Weight
`950_000_000 + 1_000_000 * legs.len()`
#### Attributes
| Name | Type |
| -------- | -------- | 
| venue_id | `VenueId` | 
| settlement_type | `SettlementType<T::BlockNumber>` | 
| trade_date | `Option<T::Moment>` | 
| value_date | `Option<T::Moment>` | 
| legs | `Vec<Leg>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'add_instruction', {
    'legs': [
        {
            'amount': 'u128',
            'asset': '[u8; 12]',
            'from': {
                'did': '[u8; 32]',
                'kind': {
                    'Default': None,
                    'User': 'u64',
                },
            },
            'to': {
                'did': '[u8; 32]',
                'kind': {
                    'Default': None,
                    'User': 'u64',
                },
            },
        },
    ],
    'settlement_type': {
        'SettleManual': 'u32',
        'SettleOnAffirmation': None,
        'SettleOnBlock': 'u32',
    },
    'trade_date': (None, 'u64'),
    'value_date': (None, 'u64'),
    'venue_id': 'u64',
}
)
```

---------
### add_instruction_with_memo
Adds a new instruction with memo.

\# Arguments
* `venue_id` - ID of the venue this instruction belongs to.
* `settlement_type` - Defines if the instruction should be settled
   in the next block after receiving all affirmations or waiting till a specific block.
* `trade_date` - Optional date from which people can interact with this instruction.
* `value_date` - Optional date after which the instruction should be settled (not enforced)
* `legs` - Legs included in this instruction.
* `memo` - Memo field for this instruction.

\# Weight
`950_000_000 + 1_000_000 * legs.len()`
#### Attributes
| Name | Type |
| -------- | -------- | 
| venue_id | `VenueId` | 
| settlement_type | `SettlementType<T::BlockNumber>` | 
| trade_date | `Option<T::Moment>` | 
| value_date | `Option<T::Moment>` | 
| legs | `Vec<Leg>` | 
| instruction_memo | `Option<InstructionMemo>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'add_instruction_with_memo', {
    'instruction_memo': (
        None,
        '[u8; 32]',
    ),
    'legs': [
        {
            'amount': 'u128',
            'asset': '[u8; 12]',
            'from': {
                'did': '[u8; 32]',
                'kind': {
                    'Default': None,
                    'User': 'u64',
                },
            },
            'to': {
                'did': '[u8; 32]',
                'kind': {
                    'Default': None,
                    'User': 'u64',
                },
            },
        },
    ],
    'settlement_type': {
        'SettleManual': 'u32',
        'SettleOnAffirmation': None,
        'SettleOnBlock': 'u32',
    },
    'trade_date': (None, 'u64'),
    'value_date': (None, 'u64'),
    'venue_id': 'u64',
}
)
```

---------
### add_instruction_with_memo_v2
Adds a new instruction with memo.

\# Arguments
* `venue_id` - ID of the venue this instruction belongs to.
* `settlement_type` - Defines if the instruction should be settled
   in the next block after receiving all affirmations or waiting till a specific block.
* `trade_date` - Optional date from which people can interact with this instruction.
* `value_date` - Optional date after which the instruction should be settled (not enforced)
* `legs` - Legs included in this instruction.
* `memo` - Memo field for this instruction.

\# Weight
`950_000_000 + 1_000_000 * legs.len()`
#### Attributes
| Name | Type |
| -------- | -------- | 
| venue_id | `VenueId` | 
| settlement_type | `SettlementType<T::BlockNumber>` | 
| trade_date | `Option<T::Moment>` | 
| value_date | `Option<T::Moment>` | 
| legs | `Vec<LegV2>` | 
| instruction_memo | `Option<InstructionMemo>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'add_instruction_with_memo_v2', {
    'instruction_memo': (
        None,
        '[u8; 32]',
    ),
    'legs': [
        {
            'asset': {
                'Fungible': {
                    'amount': 'u128',
                    'ticker': '[u8; 12]',
                },
                'NonFungible': {
                    'ids': ['u64'],
                    'ticker': '[u8; 12]',
                },
            },
            'from': {
                'did': '[u8; 32]',
                'kind': {
                    'Default': None,
                    'User': 'u64',
                },
            },
            'to': {
                'did': '[u8; 32]',
                'kind': {
                    'Default': None,
                    'User': 'u64',
                },
            },
        },
    ],
    'settlement_type': {
        'SettleManual': 'u32',
        'SettleOnAffirmation': None,
        'SettleOnBlock': 'u32',
    },
    'trade_date': (None, 'u64'),
    'value_date': (None, 'u64'),
    'venue_id': 'u64',
}
)
```

---------
### affirm_instruction
Provide affirmation to an existing instruction.

\# Arguments
* `id` - Instruction id to affirm.
* `portfolios` - Portfolios that the sender controls and wants to affirm this instruction.
* `max_legs_count` - Number of legs that need to be  affirmed.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| portfolios | `Vec<PortfolioId>` | 
| max_legs_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'affirm_instruction', {
    'id': 'u64',
    'max_legs_count': 'u32',
    'portfolios': [
        {
            'did': '[u8; 32]',
            'kind': {
                'Default': None,
                'User': 'u64',
            },
        },
    ],
}
)
```

---------
### affirm_instruction_v2
Provide affirmation to an existing instruction.

\# Arguments
* `id` - Instruction id to affirm.
* `portfolios` - Portfolios that the sender controls and wants to affirm this instruction.
* `fungible_transfers` - number of fungible transfers in the instruction.
* `nfts_transfers` - total number of NFTs being transferred in the instruction.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| portfolios | `Vec<PortfolioId>` | 
| fungible_transfers | `u32` | 
| nfts_transfers | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'affirm_instruction_v2', {
    'fungible_transfers': 'u32',
    'id': 'u64',
    'nfts_transfers': 'u32',
    'portfolios': [
        {
            'did': '[u8; 32]',
            'kind': {
                'Default': None,
                'User': 'u64',
            },
        },
    ],
}
)
```

---------
### affirm_with_receipts
Accepts an instruction and claims a signed receipt.

\# Arguments
* `id` - Target instruction id.
* `leg_id` - Target leg id for the receipt
* `receipt_uid` - Receipt ID generated by the signer.
* `signer` - Signer of the receipt.
* `signed_data` - Signed receipt.
* `portfolios` - Portfolios that the sender controls and wants to accept this instruction with

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| receipt_details | `Vec<ReceiptDetails<T::AccountId, T::OffChainSignature>>` | 
| portfolios | `Vec<PortfolioId>` | 
| max_legs_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'affirm_with_receipts', {
    'id': 'u64',
    'max_legs_count': 'u32',
    'portfolios': [
        {
            'did': '[u8; 32]',
            'kind': {
                'Default': None,
                'User': 'u64',
            },
        },
    ],
    'receipt_details': [
        {
            'leg_id': 'u64',
            'metadata': 'Bytes',
            'receipt_uid': 'u64',
            'signature': {
                'Ecdsa': '[u8; 65]',
                'Ed25519': '[u8; 64]',
                'Sr25519': '[u8; 64]',
            },
            'signer': 'AccountId',
        },
    ],
}
)
```

---------
### allow_venues
Allows additional venues to create instructions involving an asset.

* `ticker` - Ticker of the token in question.
* `venues` - Array of venues that are allowed to create instructions for the token in question.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| venues | `Vec<VenueId>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'allow_venues', {
    'ticker': '[u8; 12]',
    'venues': ['u64'],
}
)
```

---------
### change_receipt_validity
Marks a receipt issued by the caller as claimed or not claimed.
This allows the receipt issuer to invalidate an already issued receipt or revalidate an already claimed receipt.

* `receipt_uid` - Unique ID of the receipt.
* `validity` - New validity of the receipt.
#### Attributes
| Name | Type |
| -------- | -------- | 
| receipt_uid | `u64` | 
| validity | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'change_receipt_validity', {
    'receipt_uid': 'u64',
    'validity': 'bool',
}
)
```

---------
### create_venue
Registers a new venue.

* `details` - Extra details about a venue
* `signers` - Array of signers that are allowed to sign receipts for this venue
* `typ` - Type of venue being created
#### Attributes
| Name | Type |
| -------- | -------- | 
| details | `VenueDetails` | 
| signers | `Vec<T::AccountId>` | 
| typ | `VenueType` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'create_venue', {
    'details': 'Bytes',
    'signers': ['AccountId'],
    'typ': (
        'Other',
        'Distribution',
        'Sto',
        'Exchange',
    ),
}
)
```

---------
### disallow_venues
Revokes permission given to venues for creating instructions involving a particular asset.

* `ticker` - Ticker of the token in question.
* `venues` - Array of venues that are no longer allowed to create instructions for the token in question.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| venues | `Vec<VenueId>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'disallow_venues', {
    'ticker': '[u8; 12]',
    'venues': ['u64'],
}
)
```

---------
### execute_manual_instruction
Manually execute settlement

\# Arguments
* `id` - Target instruction id to reschedule.
* `_legs_count` - Legs included in this instruction.

\# Errors
* `InstructionNotFailed` - Instruction not in a failed state or does not exist.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| legs_count | `u32` | 
| portfolio | `Option<PortfolioId>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'execute_manual_instruction', {
    'id': 'u64',
    'legs_count': 'u32',
    'portfolio': (
        None,
        {
            'did': '[u8; 32]',
            'kind': {
                'Default': None,
                'User': 'u64',
            },
        },
    ),
}
)
```

---------
### execute_scheduled_instruction
Root callable extrinsic, used as an internal call to execute a scheduled settlement instruction.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| _legs_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'execute_scheduled_instruction', {'_legs_count': 'u32', 'id': 'u64'}
)
```

---------
### execute_scheduled_instruction_v2
Root callable extrinsic, used as an internal call to execute a scheduled settlement instruction.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| _fungible_transfers | `u32` | 
| _nfts_transfers | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'execute_scheduled_instruction_v2', {
    '_fungible_transfers': 'u32',
    '_nfts_transfers': 'u32',
    'id': 'u64',
}
)
```

---------
### placeholder_claim_receipt
Placeholder for removed `claim_receipt`
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'placeholder_claim_receipt', {}
)
```

---------
### placeholder_unclaim_receipt
Placeholder for removed `unclaim_receipt`
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'placeholder_unclaim_receipt', {}
)
```

---------
### reject_instruction
Rejects an existing instruction.

\# Arguments
* `id` - Instruction id to reject.
* `portfolio` - Portfolio to reject the instruction.
* `num_of_legs` - Number of legs in the instruction.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| portfolio | `PortfolioId` | 
| num_of_legs | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'reject_instruction', {
    'id': 'u64',
    'num_of_legs': 'u32',
    'portfolio': {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
}
)
```

---------
### reject_instruction_v2
Rejects an existing instruction.

\# Arguments
* `id` - Instruction id to reject.
* `portfolio` - Portfolio to reject the instruction.
* `fungible_transfers` - number of fungible transfers in the instruction.
* `nfts_transfers` - total number of NFTs being transferred in the instruction.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| portfolio | `PortfolioId` | 
| fungible_transfers | `u32` | 
| nfts_transfers | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'reject_instruction_v2', {
    'fungible_transfers': 'u32',
    'id': 'u64',
    'nfts_transfers': 'u32',
    'portfolio': {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
}
)
```

---------
### reschedule_instruction
Reschedules a failed instruction.

\# Arguments
* `id` - Target instruction id to reschedule.

\# Permissions
* Portfolio

\# Errors
* `InstructionNotFailed` - Instruction not in a failed state or does not exist.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'reschedule_instruction', {'id': 'u64'}
)
```

---------
### set_venue_filtering
Enables or disabled venue filtering for a token.

\# Arguments
* `ticker` - Ticker of the token in question.
* `enabled` - Boolean that decides if the filtering should be enabled.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| enabled | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'set_venue_filtering', {
    'enabled': 'bool',
    'ticker': '[u8; 12]',
}
)
```

---------
### update_venue_details
Edit a venue&\#x27;s details.

* `id` specifies the ID of the venue to edit.
* `details` specifies the updated venue details.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `VenueId` | 
| details | `VenueDetails` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'update_venue_details', {'details': 'Bytes', 'id': 'u64'}
)
```

---------
### update_venue_signers
Edit a venue&\#x27;s signers.
* `id` specifies the ID of the venue to edit.
* `signers` specifies the signers to add/remove.
* `add_signers` specifies the update type add/remove of venue where add is true and remove is false.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `VenueId` | 
| signers | `Vec<T::AccountId>` | 
| add_signers | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'update_venue_signers', {
    'add_signers': 'bool',
    'id': 'u64',
    'signers': ['AccountId'],
}
)
```

---------
### update_venue_type
Edit a venue&\#x27;s type.

* `id` specifies the ID of the venue to edit.
* `type` specifies the new type of the venue.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `VenueId` | 
| typ | `VenueType` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'update_venue_type', {
    'id': 'u64',
    'typ': (
        'Other',
        'Distribution',
        'Sto',
        'Exchange',
    ),
}
)
```

---------
### withdraw_affirmation
Withdraw an affirmation for a given instruction.

\# Arguments
* `id` - Instruction id for that affirmation get withdrawn.
* `portfolios` - Portfolios that the sender controls and wants to withdraw affirmation.
* `max_legs_count` - Number of legs that need to be un-affirmed.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| portfolios | `Vec<PortfolioId>` | 
| max_legs_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'withdraw_affirmation', {
    'id': 'u64',
    'max_legs_count': 'u32',
    'portfolios': [
        {
            'did': '[u8; 32]',
            'kind': {
                'Default': None,
                'User': 'u64',
            },
        },
    ],
}
)
```

---------
### withdraw_affirmation_v2
Withdraw an affirmation for a given instruction.

\# Arguments
* `id` - Instruction id for that affirmation get withdrawn.
* `portfolios` - Portfolios that the sender controls and wants to withdraw affirmation.
* `fungible_transfers` - number of fungible transfers in the instruction.
* `nfts_transfers` - total number of NFTs being transferred in the instruction.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| portfolios | `Vec<PortfolioId>` | 
| fungible_transfers | `u32` | 
| nfts_transfers | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'withdraw_affirmation_v2', {
    'fungible_transfers': 'u32',
    'id': 'u64',
    'nfts_transfers': 'u32',
    'portfolios': [
        {
            'did': '[u8; 32]',
            'kind': {
                'Default': None,
                'User': 'u64',
            },
        },
    ],
}
)
```

---------
## Events

---------
### AffirmationWithdrawn
An affirmation has been withdrawn (did, portfolio, instruction_id)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `PortfolioId` | ```{'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}```
| None | `InstructionId` | ```u64```

---------
### FailedToExecuteInstruction
Failed to execute instruction.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `InstructionId` | ```u64```
| None | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}```

---------
### InstructionAffirmed
An instruction has been affirmed (did, portfolio, instruction_id)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `PortfolioId` | ```{'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}```
| None | `InstructionId` | ```u64```

---------
### InstructionCreated
A new instruction has been created
(did, venue_id, instruction_id, settlement_type, trade_date, value_date, legs, memo)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `VenueId` | ```u64```
| None | `InstructionId` | ```u64```
| None | `SettlementType<BlockNumber>` | ```{'SettleOnAffirmation': None, 'SettleOnBlock': 'u32', 'SettleManual': 'u32'}```
| None | `Option<Moment>` | ```(None, 'u64')```
| None | `Option<Moment>` | ```(None, 'u64')```
| None | `Vec<Leg>` | ```[{'from': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}, 'to': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}, 'asset': '[u8; 12]', 'amount': 'u128'}]```
| None | `Option<InstructionMemo>` | ```(None, '[u8; 32]')```

---------
### InstructionExecuted
Instruction executed successfully(did, instruction_id)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `InstructionId` | ```u64```

---------
### InstructionFailed
Instruction failed execution (did, instruction_id)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `InstructionId` | ```u64```

---------
### InstructionRejected
An instruction has been rejected (did, instruction_id)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `InstructionId` | ```u64```

---------
### InstructionRescheduled
Instruction is rescheduled.
(caller DID, instruction_id)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `InstructionId` | ```u64```

---------
### InstructionV2Created
A new instruction has been created
(did, venue_id, instruction_id, settlement_type, trade_date, value_date, legs, memo)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `VenueId` | ```u64```
| None | `InstructionId` | ```u64```
| None | `SettlementType<BlockNumber>` | ```{'SettleOnAffirmation': None, 'SettleOnBlock': 'u32', 'SettleManual': 'u32'}```
| None | `Option<Moment>` | ```(None, 'u64')```
| None | `Option<Moment>` | ```(None, 'u64')```
| None | `Vec<LegV2>` | ```[{'from': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}, 'to': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}, 'asset': {'Fungible': {'ticker': '[u8; 12]', 'amount': 'u128'}, 'NonFungible': {'ticker': '[u8; 12]', 'ids': ['u64']}}}]```
| None | `Option<InstructionMemo>` | ```(None, '[u8; 32]')```

---------
### LegFailedExecution
Execution of a leg failed (did, instruction_id, leg_id)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `InstructionId` | ```u64```
| None | `LegId` | ```u64```

---------
### ReceiptClaimed
A receipt has been claimed (did, instruction_id, leg_id, receipt_uid, signer, receipt metadata)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `InstructionId` | ```u64```
| None | `LegId` | ```u64```
| None | `u64` | ```u64```
| None | `AccountId` | ```AccountId```
| None | `ReceiptMetadata` | ```Bytes```

---------
### ReceiptUnclaimed
A receipt has been unclaimed (did, instruction_id, leg_id, receipt_uid, signer)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `InstructionId` | ```u64```
| None | `LegId` | ```u64```
| None | `u64` | ```u64```
| None | `AccountId` | ```AccountId```

---------
### ReceiptValidityChanged
A receipt has been invalidated (did, signer, receipt_uid, validity)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `u64` | ```u64```
| None | `bool` | ```bool```

---------
### SchedulingFailed
Scheduling of instruction fails.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}```

---------
### SettlementManuallyExecuted
Settlement manually executed (did, id)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `InstructionId` | ```u64```

---------
### VenueCreated
A new venue has been created (did, venue_id, details, type)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `VenueId` | ```u64```
| None | `VenueDetails` | ```Bytes```
| None | `VenueType` | ```('Other', 'Distribution', 'Sto', 'Exchange')```

---------
### VenueDetailsUpdated
An existing venue&\#x27;s details has been updated (did, venue_id, details)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `VenueId` | ```u64```
| None | `VenueDetails` | ```Bytes```

---------
### VenueFiltering
Venue filtering has been enabled or disabled for a ticker (did, ticker, filtering_enabled)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `bool` | ```bool```

---------
### VenueSignersUpdated
An existing venue&\#x27;s signers has been updated (did, venue_id, signers, update_type)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `VenueId` | ```u64```
| None | `Vec<AccountId>` | ```['AccountId']```
| None | `bool` | ```bool```

---------
### VenueTypeUpdated
An existing venue&\#x27;s type has been updated (did, venue_id, type)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `VenueId` | ```u64```
| None | `VenueType` | ```('Other', 'Distribution', 'Sto', 'Exchange')```

---------
### VenueUnauthorized
Venue not part of the token&\#x27;s allow list (did, Ticker, venue_id)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `VenueId` | ```u64```

---------
### VenuesAllowed
Venues added to allow list (did, ticker, vec&lt;venue_id&gt;)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `Vec<VenueId>` | ```['u64']```

---------
### VenuesBlocked
Venues added to block list (did, ticker, vec&lt;venue_id&gt;)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `Vec<VenueId>` | ```['u64']```

---------
## Storage functions

---------
### AffirmsReceived
 Tracks affirmations received for an instruction. (instruction_id, counter_party) -&gt; AffirmationStatus

#### Python
```python
result = substrate.query(
    'Settlement', 'AffirmsReceived', [
    'u64',
    {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
]
)
```

#### Return value
```python
('Unknown', 'Pending', 'Affirmed')
```
---------
### Details
 Free-form text about a venue. venue_id -&gt; `VenueDetails`
 Only needed for the UI.

#### Python
```python
result = substrate.query(
    'Settlement', 'Details', ['u64']
)
```

#### Return value
```python
'Bytes'
```
---------
### InstructionAffirmsPending
 Number of affirmations pending before instruction is executed. instruction_id -&gt; affirm_pending

#### Python
```python
result = substrate.query(
    'Settlement', 'InstructionAffirmsPending', ['u64']
)
```

#### Return value
```python
'u64'
```
---------
### InstructionCounter
 Number of instructions in the system (It&#x27;s one more than the actual number)

#### Python
```python
result = substrate.query(
    'Settlement', 'InstructionCounter', []
)
```

#### Return value
```python
'u64'
```
---------
### InstructionDetails
 Details about an instruction. instruction_id -&gt; instruction_details

#### Python
```python
result = substrate.query(
    'Settlement', 'InstructionDetails', ['u64']
)
```

#### Return value
```python
{
    'created_at': (None, 'u64'),
    'instruction_id': 'u64',
    'settlement_type': {
        'SettleManual': 'u32',
        'SettleOnAffirmation': None,
        'SettleOnBlock': 'u32',
    },
    'status': ('Unknown', 'Pending', 'Failed'),
    'trade_date': (None, 'u64'),
    'value_date': (None, 'u64'),
    'venue_id': 'u64',
}
```
---------
### InstructionLegStatus
 Status of a leg under an instruction. (instruction_id, leg_id) -&gt; LegStatus

#### Python
```python
result = substrate.query(
    'Settlement', 'InstructionLegStatus', ['u64', 'u64']
)
```

#### Return value
```python
{
    'ExecutionPending': None,
    'ExecutionToBeSkipped': ('AccountId', 'u64'),
    'PendingTokenLock': None,
}
```
---------
### InstructionLegs
 Legs under an instruction. (instruction_id, leg_id) -&gt; Leg

#### Python
```python
result = substrate.query(
    'Settlement', 'InstructionLegs', ['u64', 'u64']
)
```

#### Return value
```python
{
    'amount': 'u128',
    'asset': '[u8; 12]',
    'from': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}},
    'to': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}},
}
```
---------
### InstructionLegsV2
 Legs under an instruction. (instruction_id, leg_id) -&gt; Leg

#### Python
```python
result = substrate.query(
    'Settlement', 'InstructionLegsV2', ['u64', 'u64']
)
```

#### Return value
```python
{
    'asset': {
        'Fungible': {'amount': 'u128', 'ticker': '[u8; 12]'},
        'NonFungible': {'ids': ['u64'], 'ticker': '[u8; 12]'},
    },
    'from': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}},
    'to': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}},
}
```
---------
### InstructionMemos
 Instruction memo

#### Python
```python
result = substrate.query(
    'Settlement', 'InstructionMemos', ['u64']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### ReceiptsUsed
 Tracks redemption of receipts. (signer, receipt_uid) -&gt; receipt_used

#### Python
```python
result = substrate.query(
    'Settlement', 'ReceiptsUsed', ['AccountId', 'u64']
)
```

#### Return value
```python
'bool'
```
---------
### StorageVersion
 Storage version.

#### Python
```python
result = substrate.query(
    'Settlement', 'StorageVersion', []
)
```

#### Return value
```python
'u8'
```
---------
### UserAffirmations
 Helps a user track their pending instructions and affirmations (only needed for UI).
 (counter_party, instruction_id) -&gt; AffirmationStatus

#### Python
```python
result = substrate.query(
    'Settlement', 'UserAffirmations', [
    {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
    'u64',
]
)
```

#### Return value
```python
('Unknown', 'Pending', 'Affirmed')
```
---------
### UserVenues
 Array of venues created by an identity. Only needed for the UI. IdentityId -&gt; Vec&lt;venue_id&gt;

#### Python
```python
result = substrate.query(
    'Settlement', 'UserVenues', ['[u8; 32]']
)
```

#### Return value
```python
['u64']
```
---------
### VenueAllowList
 Venues that are allowed to create instructions involving a particular ticker. Only used if filtering is enabled.
 (ticker, venue_id) -&gt; allowed

#### Python
```python
result = substrate.query(
    'Settlement', 'VenueAllowList', ['[u8; 12]', 'u64']
)
```

#### Return value
```python
'bool'
```
---------
### VenueCounter
 Number of venues in the system (It&#x27;s one more than the actual number)

#### Python
```python
result = substrate.query(
    'Settlement', 'VenueCounter', []
)
```

#### Return value
```python
'u64'
```
---------
### VenueFiltering
 Tracks if a token has enabled filtering venues that can create instructions involving their token. Ticker -&gt; filtering_enabled

#### Python
```python
result = substrate.query(
    'Settlement', 'VenueFiltering', ['[u8; 12]']
)
```

#### Return value
```python
'bool'
```
---------
### VenueInfo
 Info about a venue. venue_id -&gt; venue

#### Python
```python
result = substrate.query(
    'Settlement', 'VenueInfo', ['u64']
)
```

#### Return value
```python
{
    'creator': '[u8; 32]',
    'venue_type': ('Other', 'Distribution', 'Sto', 'Exchange'),
}
```
---------
### VenueInstructions
 Instructions under a venue.
 Only needed for the UI.

 venue_id -&gt; instruction_id -&gt; ()

#### Python
```python
result = substrate.query(
    'Settlement', 'VenueInstructions', ['u64', 'u64']
)
```

#### Return value
```python
()
```
---------
### VenueSigners
 Signers allowed by the venue. (venue_id, signer) -&gt; bool

#### Python
```python
result = substrate.query(
    'Settlement', 'VenueSigners', ['u64', 'AccountId']
)
```

#### Return value
```python
'bool'
```
---------
## Errors

---------
### CallerIsNotAParty
The caller is not a party of this instruction.

---------
### DeprecatedCallOnV2Instruction
Deprecated function has been called on a v2 instruction.

---------
### FailedToLockTokens
While affirming the transfer, system failed to lock the assets involved.

---------
### FailedToSchedule
Scheduling of an instruction fails.

---------
### InstructionDatesInvalid
Instruction has invalid dates

---------
### InstructionFailed
Instruction failed to execute.

---------
### InstructionHasTooManyLegs
Maximum legs that can be in a single instruction.

---------
### InstructionNotAffirmed
Instruction has not been affirmed.

---------
### InstructionNotFailed
Provided instruction is not failing execution.

---------
### InstructionNotPending
Provided instruction is not pending execution.

---------
### InstructionSettleBlockNotReached
Instruction settlement block has not yet been reached.

---------
### InstructionSettleBlockPassed
Instruction&\#x27;s target settle block reached.

---------
### InvalidLegAsset
Expected a different type of asset in a leg.

---------
### InvalidSignature
Offchain signature is invalid.

---------
### InvalidVenue
Venue does not exist.

---------
### LegCountTooSmall
Legs count should matches with the total number of legs in which given portfolio act as `from_portfolio`.

---------
### LegNotPending
Provided leg is not pending execution.

---------
### MaxNumberOfNFTsExceeded
The number of nfts being transferred in the instruction was exceeded.

---------
### MaxNumberOfNFTsPerLegExceeded
The maximum number of nfts being transferred in one leg was exceeded.

---------
### NoPendingAffirm
No pending affirmation for the provided instruction.

---------
### NoPortfolioProvided
Portfolio based actions require at least one portfolio to be provided as input.

---------
### NumberOfTransferredNFTsUnderestimated
The given number of nfts being transferred was underestimated.

---------
### PortfolioMismatch
Portfolio in receipt does not match with portfolios provided by the user.

---------
### ReceiptAlreadyClaimed
Receipt already used.

---------
### ReceiptForNonFungibleAsset
Off-chain receipts are not accepted for non-fungible tokens.

---------
### ReceiptNotClaimed
Receipt not used yet.

---------
### SameSenderReceiver
Sender and receiver are the same.

---------
### SettleOnPastBlock
The provided settlement block number is in the past and cannot be used by the scheduler.

---------
### SignerAlreadyExists
Signer is already added to venue.

---------
### SignerDoesNotExist
Signer is not added to venue.

---------
### Unauthorized
Sender does not have required permissions.

---------
### UnauthorizedSigner
Signer is not authorized by the venue.

---------
### UnauthorizedVenue
Venue does not have required permissions.

---------
### UnexpectedAffirmationStatus
The current instruction affirmation status does not support the requested action.

---------
### UnknownInstruction
Instruction status is unknown

---------
### ZeroAmount
Instruction leg amount can&\#x27;t be zero.

---------