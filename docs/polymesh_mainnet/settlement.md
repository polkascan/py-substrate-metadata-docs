
# Settlement

---------
## Calls

---------
### add_and_affirm_instruction
Adds and affirms a new instruction.

\# Arguments
* `venue_id` - ID of the venue this instruction belongs to.
* `settlement_type` - Defines if the instruction should be settled in the next block, after receiving all affirmations
or waiting till a specific block.
* `trade_date` - Optional date from which people can interact with this instruction.
* `value_date` - Optional date after which the instruction should be settled (not enforced)
* `legs` - Legs included in this instruction.
* `portfolios` - Portfolios that the sender controls and wants to use in this affirmations.
* `instruction_memo` - Memo field for this instruction.

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
| instruction_memo | `Option<Memo>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'add_and_affirm_instruction', {
    'instruction_memo': (
        None,
        '[u8; 32]',
    ),
    'legs': [
        {
            'Fungible': {
                'amount': 'u128',
                'receiver': {
                    'did': '[u8; 32]',
                    'kind': {
                        'Default': None,
                        'User': 'u64',
                    },
                },
                'sender': {
                    'did': '[u8; 32]',
                    'kind': {
                        'Default': None,
                        'User': 'u64',
                    },
                },
                'ticker': '[u8; 12]',
            },
            'NonFungible': {
                'nfts': {
                    'ids': ['u64'],
                    'ticker': '[u8; 12]',
                },
                'receiver': {
                    'did': '[u8; 32]',
                    'kind': {
                        'Default': None,
                        'User': 'u64',
                    },
                },
                'sender': {
                    'did': '[u8; 32]',
                    'kind': {
                        'Default': None,
                        'User': 'u64',
                    },
                },
            },
            'OffChain': {
                'amount': 'u128',
                'receiver_identity': '[u8; 32]',
                'sender_identity': '[u8; 32]',
                'ticker': '[u8; 12]',
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
Adds a new instruction.

\# Arguments
* `venue_id` - ID of the venue this instruction belongs to.
* `settlement_type` - Defines if the instruction should be settled in the next block, after receiving all affirmations
or waiting till a specific block.
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
| instruction_memo | `Option<Memo>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'add_instruction', {
    'instruction_memo': (
        None,
        '[u8; 32]',
    ),
    'legs': [
        {
            'Fungible': {
                'amount': 'u128',
                'receiver': {
                    'did': '[u8; 32]',
                    'kind': {
                        'Default': None,
                        'User': 'u64',
                    },
                },
                'sender': {
                    'did': '[u8; 32]',
                    'kind': {
                        'Default': None,
                        'User': 'u64',
                    },
                },
                'ticker': '[u8; 12]',
            },
            'NonFungible': {
                'nfts': {
                    'ids': ['u64'],
                    'ticker': '[u8; 12]',
                },
                'receiver': {
                    'did': '[u8; 32]',
                    'kind': {
                        'Default': None,
                        'User': 'u64',
                    },
                },
                'sender': {
                    'did': '[u8; 32]',
                    'kind': {
                        'Default': None,
                        'User': 'u64',
                    },
                },
            },
            'OffChain': {
                'amount': 'u128',
                'receiver_identity': '[u8; 32]',
                'sender_identity': '[u8; 32]',
                'ticker': '[u8; 12]',
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
* `id` - the [`InstructionId`] of the instruction being affirmed.
* `portfolios` - a vector of [`PortfolioId`] under the caller&\#x27;s control and intended for affirmation.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| portfolios | `Vec<PortfolioId>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'affirm_instruction', {
    'id': 'u64',
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
### affirm_instruction_with_count
Provide affirmation to an existing instruction.

\# Arguments
* `id` - the [`InstructionId`] of the instruction being affirmed.
* `portfolios` - a vector of [`PortfolioId`] under the caller&\#x27;s control and intended for affirmation.
* `number_of_assets` - an optional [`AffirmationCount`] that will be used for a precise fee estimation before executing the extrinsic.

Note: calling the rpc method `get_affirmation_count` returns an instance of [`AffirmationCount`].

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| portfolios | `Vec<PortfolioId>` | 
| number_of_assets | `Option<AffirmationCount>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'affirm_instruction_with_count', {
    'id': 'u64',
    'number_of_assets': (
        None,
        {
            'offchain_count': 'u32',
            'receiver_asset_count': {
                'fungible': 'u32',
                'non_fungible': 'u32',
                'off_chain': 'u32',
            },
            'sender_asset_count': {
                'fungible': 'u32',
                'non_fungible': 'u32',
                'off_chain': 'u32',
            },
        },
    ),
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
Affirms an instruction using receipts for offchain transfers.

\# Arguments
* `id` - the [`InstructionId`] of the instruction being affirmed.
* `receipt_details` - a vector of [`ReceiptDetails`], which contain the details about the offchain transfer.
* `portfolios` - a vector of [`PortfolioId`] under the caller&\#x27;s control and intended for affirmation.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| receipt_details | `Vec<ReceiptDetails<T::AccountId, T::OffChainSignature>>` | 
| portfolios | `Vec<PortfolioId>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'affirm_with_receipts', {
    'id': 'u64',
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
            'instruction_id': 'u64',
            'leg_id': 'u64',
            'metadata': (
                None,
                '[u8; 32]',
            ),
            'signature': {
                'Ecdsa': '[u8; 65]',
                'Ed25519': '[u8; 64]',
                'Sr25519': '[u8; 64]',
            },
            'signer': 'AccountId',
            'uid': 'u64',
        },
    ],
}
)
```

---------
### affirm_with_receipts_with_count
Affirms an instruction using receipts for offchain transfers.

\# Arguments
* `id` - the [`InstructionId`] of the instruction being affirmed.
* `receipt_details` - a vector of [`ReceiptDetails`], which contain the details about the offchain transfer.
* `portfolios` - a vector of [`PortfolioId`] under the caller&\#x27;s control and intended for affirmation.
* `number_of_assets` - an optional [`AffirmationCount`] that will be used for a precise fee estimation before executing the extrinsic.

Note: calling the rpc method `get_affirmation_count` returns an instance of [`AffirmationCount`].

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| receipt_details | `Vec<ReceiptDetails<T::AccountId, T::OffChainSignature>>` | 
| portfolios | `Vec<PortfolioId>` | 
| number_of_assets | `Option<AffirmationCount>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'affirm_with_receipts_with_count', {
    'id': 'u64',
    'number_of_assets': (
        None,
        {
            'offchain_count': 'u32',
            'receiver_asset_count': {
                'fungible': 'u32',
                'non_fungible': 'u32',
                'off_chain': 'u32',
            },
            'sender_asset_count': {
                'fungible': 'u32',
                'non_fungible': 'u32',
                'off_chain': 'u32',
            },
        },
    ),
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
            'instruction_id': 'u64',
            'leg_id': 'u64',
            'metadata': (
                None,
                '[u8; 32]',
            ),
            'signature': {
                'Ecdsa': '[u8; 65]',
                'Ed25519': '[u8; 64]',
                'Sr25519': '[u8; 64]',
            },
            'signer': 'AccountId',
            'uid': 'u64',
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
Manually executes an instruction.

\# Arguments
* `id`: The [`InstructionId`] of the instruction to be executed.
* `portfolio`:  One of the caller&\#x27;s [`PortfolioId`] which is also a counter patry in the instruction.
If None, the caller must be the venue creator or a counter party in a [`Leg::OffChain`].
* `fungible_transfers`: The number of fungible legs in the instruction.
* `nfts_transfers`: The number of nfts being transferred in the instruction.
* `offchain_transfers`: The number of offchain legs in the instruction.
* `weight_limit`: An optional maximum [`Weight`] value to be charged for executing the instruction.
If the `weight_limit` is less than the required amount, the instruction will fail execution.

Note: calling the rpc method `get_execute_instruction_info` returns an instance of [`ExecuteInstructionInfo`], which contains the count parameters.
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| portfolio | `Option<PortfolioId>` | 
| fungible_transfers | `u32` | 
| nfts_transfers | `u32` | 
| offchain_transfers | `u32` | 
| weight_limit | `Option<Weight>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'execute_manual_instruction', {
    'fungible_transfers': 'u32',
    'id': 'u64',
    'nfts_transfers': 'u32',
    'offchain_transfers': 'u32',
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
    'weight_limit': (
        None,
        {
            'proof_size': 'u64',
            'ref_time': 'u64',
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
| weight_limit | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'execute_scheduled_instruction', {
    'id': 'u64',
    'weight_limit': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
### reject_instruction
Rejects an existing instruction.

\# Arguments
* `id` - the [`InstructionId`] of the instruction being rejected.
* `portfolio` - the [`PortfolioId`] that belongs to the instruction and is rejecting it.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| portfolio | `PortfolioId` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'reject_instruction', {
    'id': 'u64',
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
### reject_instruction_with_count
Rejects an existing instruction.

\# Arguments
* `id` - the [`InstructionId`] of the instruction being rejected.
* `portfolio` - the [`PortfolioId`] that belongs to the instruction and is rejecting it.
* `number_of_assets` - an optional [`AssetCount`] that will be used for a precise fee estimation before executing the extrinsic.

Note: calling the rpc method `get_execute_instruction_info` returns an instance of [`ExecuteInstructionInfo`], which contain the asset count.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| portfolio | `PortfolioId` | 
| number_of_assets | `Option<AssetCount>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'reject_instruction_with_count', {
    'id': 'u64',
    'number_of_assets': (
        None,
        {
            'fungible': 'u32',
            'non_fungible': 'u32',
            'off_chain': 'u32',
        },
    ),
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
* `id` - the [`InstructionId`] of the instruction getting an affirmation withdrawn.
* `portfolios` - a vector of [`PortfolioId`] under the caller&\#x27;s control and intended for affirmation withdrawal.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| portfolios | `Vec<PortfolioId>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'withdraw_affirmation', {
    'id': 'u64',
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
### withdraw_affirmation_with_count
Withdraw an affirmation for a given instruction.

\# Arguments
* `id` - the [`InstructionId`] of the instruction getting an affirmation withdrawn.
* `portfolios` - a vector of [`PortfolioId`] under the caller&\#x27;s control and intended for affirmation withdrawal.
* `number_of_assets` - an optional [`AffirmationCount`] that will be used for a precise fee estimation before executing the extrinsic.

Note: calling the rpc method `get_affirmation_count` returns an instance of [`AffirmationCount`].

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `InstructionId` | 
| portfolios | `Vec<PortfolioId>` | 
| number_of_assets | `Option<AffirmationCount>` | 

#### Python
```python
call = substrate.compose_call(
    'Settlement', 'withdraw_affirmation_with_count', {
    'id': 'u64',
    'number_of_assets': (
        None,
        {
            'offchain_count': 'u32',
            'receiver_asset_count': {
                'fungible': 'u32',
                'non_fungible': 'u32',
                'off_chain': 'u32',
            },
            'sender_asset_count': {
                'fungible': 'u32',
                'non_fungible': 'u32',
                'off_chain': 'u32',
            },
        },
    ),
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
| None | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

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
### InstructionAutomaticallyAffirmed
An instruction has been automatically affirmed.
Parameters: [`IdentityId`] of the caller, [`PortfolioId`] of the receiver, and [`InstructionId`] of the instruction.
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
| None | `Vec<Leg>` | ```[{'Fungible': {'sender': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}, 'receiver': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}, 'ticker': '[u8; 12]', 'amount': 'u128'}, 'NonFungible': {'sender': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}, 'receiver': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}, 'nfts': {'ticker': '[u8; 12]', 'ids': ['u64']}}, 'OffChain': {'sender_identity': '[u8; 32]', 'receiver_identity': '[u8; 32]', 'ticker': '[u8; 12]', 'amount': 'u128'}}]```
| None | `Option<Memo>` | ```(None, '[u8; 32]')```

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
| None | `Option<ReceiptMetadata>` | ```(None, '[u8; 32]')```

---------
### SchedulingFailed
Scheduling of instruction fails.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

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
    'Fungible': {
        'amount': 'u128',
        'receiver': {
            'did': '[u8; 32]',
            'kind': {'Default': None, 'User': 'u64'},
        },
        'sender': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}},
        'ticker': '[u8; 12]',
    },
    'NonFungible': {
        'nfts': {'ids': ['u64'], 'ticker': '[u8; 12]'},
        'receiver': {
            'did': '[u8; 32]',
            'kind': {'Default': None, 'User': 'u64'},
        },
        'sender': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}},
    },
    'OffChain': {
        'amount': 'u128',
        'receiver_identity': '[u8; 32]',
        'sender_identity': '[u8; 32]',
        'ticker': '[u8; 12]',
    },
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
### InstructionStatuses
 Instruction statuses. instruction_id -&gt; InstructionStatus

#### Python
```python
result = substrate.query(
    'Settlement', 'InstructionStatuses', ['u64']
)
```

#### Return value
```python
{
    'Failed': None,
    'Pending': None,
    'Rejected': 'u32',
    'Success': 'u32',
    'Unknown': None,
}
```
---------
### NumberOfVenueSigners
 Tracks the number of signers each venue has.

#### Python
```python
result = substrate.query(
    'Settlement', 'NumberOfVenueSigners', ['u64']
)
```

#### Return value
```python
'u32'
```
---------
### OffChainAffirmations
 Tracks the affirmation status for offchain legs in a instruction. [`(InstructionId, LegId)`] -&gt; [`AffirmationStatus`]

#### Python
```python
result = substrate.query(
    'Settlement', 'OffChainAffirmations', ['u64', 'u64']
)
```

#### Return value
```python
('Unknown', 'Pending', 'Affirmed')
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
 Venues create by an identity.
 Only needed for the UI.

 identity -&gt; venue_id ()

#### Python
```python
result = substrate.query(
    'Settlement', 'UserVenues', ['[u8; 32]', 'u64']
)
```

#### Return value
```python
()
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
### DuplicateReceiptUid
No duplicate uid are allowed for different receipts.

---------
### FailedToReleaseLockOrTransferAssets
The instruction failed to release asset locks or transfer the assets.

---------
### FailedToSchedule
Scheduling of an instruction fails.

---------
### InputWeightIsLessThanMinimum
The input weight is less than the minimum required.

---------
### InstructionDatesInvalid
Instruction has invalid dates

---------
### InstructionNotAffirmed
Instruction has not been affirmed.

---------
### InstructionSettleBlockNotReached
Instruction settlement block has not yet been reached.

---------
### InstructionSettleBlockPassed
Instruction&\#x27;s target settle block reached.

---------
### InvalidInstructionStatusForExecution
Only [`InstructionStatus::Pending`] or [`InstructionStatus::Failed`] instructions can be executed.

---------
### InvalidSignature
Offchain signature is invalid.

---------
### InvalidVenue
Venue does not exist.

---------
### LegNotFound
No leg with the given id was found

---------
### MaxNumberOfFungibleAssetsExceeded
The maximum number of fungible assets was exceeded.

---------
### MaxNumberOfNFTsExceeded
The number of nfts being transferred in the instruction was exceeded.

---------
### MaxNumberOfOffChainAssetsExceeded
The maximum number of off-chain assets was exceeded.

---------
### MaxNumberOfReceiptsExceeded
The maximum number of receipts was exceeded.

---------
### MultipleReceiptsForOneLeg
Multiple receipts for the same leg are not allowed.

---------
### NotAllAffirmationsHaveBeenReceived
There are parties who have not affirmed the instruction.

---------
### NumberOfFungibleTransfersUnderestimated
The given number of fungible transfers was underestimated.

---------
### NumberOfOffChainTransfersUnderestimated
The given number of off-chain transfers was underestimated.

---------
### NumberOfTransferredNFTsUnderestimated
The given number of nfts being transferred was underestimated.

---------
### NumberOfVenueSignersExceeded
The maximum number of venue signers was exceeded.

---------
### OffChainAssetCantBeLocked
Off-Chain assets cannot be locked.

---------
### ReceiptAlreadyClaimed
Receipt already used.

---------
### ReceiptForInvalidLegType
Off-chain receipts can only be used for off-chain leg type.

---------
### ReceiptInstructionIdMissmatch
The instruction id in all receipts must match the extrinsic parameter.

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
### UnexpectedLegStatus
An invalid has been reached.

---------
### UnexpectedOFFChainAsset
Ticker could not be found on chain.

---------
### UnknownInstruction
Instruction status is unknown

---------
### WeightLimitExceeded
The maximum weight limit for executing the function was exceeded.

---------
### ZeroAmount
Instruction leg amount can&\#x27;t be zero.

---------