
# LiquidityPoolsGateway

---------
## Calls

---------
### add_instance
Add a known instance of a deployed liquidity pools integration for a
specific domain.
#### Attributes
| Name | Type |
| -------- | -------- | 
| instance | `DomainAddress` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPoolsGateway', 'add_instance', {
    'instance': {
        'Centrifuge': '[u8; 32]',
        'EVM': ('u64', '[u8; 20]'),
    },
}
)
```

---------
### add_relayer
Add a known instance of a deployed liquidity pools integration for a
specific domain.
#### Attributes
| Name | Type |
| -------- | -------- | 
| relayer | `DomainAddress` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPoolsGateway', 'add_relayer', {
    'relayer': {
        'Centrifuge': '[u8; 32]',
        'EVM': ('u64', '[u8; 20]'),
    },
}
)
```

---------
### process_msg
Process an incoming message.
#### Attributes
| Name | Type |
| -------- | -------- | 
| msg | `BoundedVec<u8, T::MaxIncomingMessageSize>` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPoolsGateway', 'process_msg', {'msg': 'Bytes'}
)
```

---------
### remove_instance
Remove an instance from a specific domain.
#### Attributes
| Name | Type |
| -------- | -------- | 
| instance | `DomainAddress` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPoolsGateway', 'remove_instance', {
    'instance': {
        'Centrifuge': '[u8; 32]',
        'EVM': ('u64', '[u8; 20]'),
    },
}
)
```

---------
### remove_relayer
Remove an instance from a specific domain.
#### Attributes
| Name | Type |
| -------- | -------- | 
| relayer | `DomainAddress` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPoolsGateway', 'remove_relayer', {
    'relayer': {
        'Centrifuge': '[u8; 32]',
        'EVM': ('u64', '[u8; 20]'),
    },
}
)
```

---------
### set_domain_router
Set a domain&\#x27;s router,
#### Attributes
| Name | Type |
| -------- | -------- | 
| domain | `Domain` | 
| router | `T::Router` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPoolsGateway', 'set_domain_router', {
    'domain': {
        'Centrifuge': None,
        'EVM': 'u64',
    },
    'router': {
        'AxelarEVM': {
            'evm_chain': 'Bytes',
            'liquidity_pools_contract_address': '[u8; 20]',
            'router': {
                'evm_domain': {
                    'fee_values': {
                        'gas_limit': '[u64; 4]',
                        'gas_price': '[u64; 4]',
                        'value': '[u64; 4]',
                    },
                    'target_contract_address': '[u8; 20]',
                    'target_contract_hash': '[u8; 32]',
                },
            },
        },
        'AxelarXCM': {
            'axelar_target_chain': 'Bytes',
            'axelar_target_contract': '[u8; 20]',
            'router': {
                'xcm_domain': {
                    'contract_address': '[u8; 20]',
                    'ethereum_xcm_transact_call_index': 'Bytes',
                    'fee_amount': 'u128',
                    'fee_currency': {
                        'AUSD': None,
                        'ForeignAsset': 'u32',
                        'Native': None,
                        'Tranche': (
                            'u64',
                            '[u8; 16]',
                        ),
                        None: None,
                        'Staking': (
                            'BlockRewards',
                        ),
                    },
                    'location': {
                        'V2': {
                            'interior': 'scale_info::108',
                            'parents': 'u8',
                        },
                        None: None,
                        'V3': {
                            'interior': 'scale_info::117',
                            'parents': 'u8',
                        },
                    },
                    'max_gas_limit': 'u64',
                    'overall_weight': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                    'transact_required_weight_at_most': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                },
            },
        },
        'EthereumXCM': {
            'router': {
                'xcm_domain': {
                    'contract_address': '[u8; 20]',
                    'ethereum_xcm_transact_call_index': 'Bytes',
                    'fee_amount': 'u128',
                    'fee_currency': {
                        'Native': None,
                        'Tranche': (
                            'u64',
                            '[u8; 16]',
                        ),
                        None: None,
                        'AUSD': None,
                        'ForeignAsset': 'u32',
                        'Staking': (
                            'BlockRewards',
                        ),
                    },
                    'location': {
                        None: None,
                        'V2': {
                            'interior': 'scale_info::108',
                            'parents': 'u8',
                        },
                        'V3': {
                            'interior': 'scale_info::117',
                            'parents': 'u8',
                        },
                    },
                    'max_gas_limit': 'u64',
                    'overall_weight': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                    'transact_required_weight_at_most': {
                        'proof_size': 'u64',
                        'ref_time': 'u64',
                    },
                },
            },
        },
    },
}
)
```

---------
## Events

---------
### DomainRouterSet
The router for a given domain was set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| domain | `Domain` | ```{'Centrifuge': None, 'EVM': 'u64'}```
| router | `T::Router` | ```{'EthereumXCM': {'router': {'xcm_domain': {'location': {None: None, 'V2': 'scale_info::107', 'V3': 'scale_info::116'}, 'ethereum_xcm_transact_call_index': 'Bytes', 'contract_address': '[u8; 20]', 'max_gas_limit': 'u64', 'transact_required_weight_at_most': {'ref_time': 'u64', 'proof_size': 'u64'}, 'overall_weight': {'ref_time': 'u64', 'proof_size': 'u64'}, 'fee_currency': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': 'scale_info::72'}, 'fee_amount': 'u128'}}}, 'AxelarEVM': {'router': {'evm_domain': {'target_contract_address': '[u8; 20]', 'target_contract_hash': '[u8; 32]', 'fee_values': {'value': '[u64; 4]', 'gas_price': '[u64; 4]', 'gas_limit': '[u64; 4]'}}}, 'evm_chain': 'Bytes', 'liquidity_pools_contract_address': '[u8; 20]'}, 'AxelarXCM': {'router': {'xcm_domain': {'location': {None: None, 'V2': 'scale_info::107', 'V3': 'scale_info::116'}, 'ethereum_xcm_transact_call_index': 'Bytes', 'contract_address': '[u8; 20]', 'max_gas_limit': 'u64', 'transact_required_weight_at_most': {'ref_time': 'u64', 'proof_size': 'u64'}, 'overall_weight': {'ref_time': 'u64', 'proof_size': 'u64'}, 'fee_currency': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': 'scale_info::72'}, 'fee_amount': 'u128'}}, 'axelar_target_chain': 'Bytes', 'axelar_target_contract': '[u8; 20]'}}```

---------
### InstanceAdded
An instance was added to a domain.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| instance | `DomainAddress` | ```{'Centrifuge': '[u8; 32]', 'EVM': ('u64', '[u8; 20]')}```

---------
### InstanceRemoved
An instance was removed from a domain.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| instance | `DomainAddress` | ```{'Centrifuge': '[u8; 32]', 'EVM': ('u64', '[u8; 20]')}```

---------
### OutboundMessageSubmitted
An outbound message has been submitted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| domain | `Domain` | ```{'Centrifuge': None, 'EVM': 'u64'}```
| message | `T::Message` | ```{'Invalid': None, 'AddCurrency': {'currency': 'u128', 'evm_address': '[u8; 20]'}, 'AddPool': {'pool_id': 'u64'}, 'AllowInvestmentCurrency': {'pool_id': 'u64', 'currency': 'u128'}, 'AddTranche': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'token_name': '[u8; 128]', 'token_symbol': '[u8; 32]', 'decimals': 'u8'}, 'UpdateTrancheTokenPrice': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'currency': 'u128', 'price': 'u128'}, 'UpdateMember': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'member': '[u8; 32]', 'valid_until': 'u64'}, 'Transfer': {'currency': 'u128', 'sender': '[u8; 32]', 'receiver': '[u8; 32]', 'amount': 'u128'}, 'TransferTrancheTokens': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'sender': '[u8; 32]', 'domain': {'Centrifuge': None, 'EVM': 'u64'}, 'receiver': '[u8; 32]', 'amount': 'u128'}, 'IncreaseInvestOrder': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128', 'amount': 'u128'}, 'DecreaseInvestOrder': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128', 'amount': 'u128'}, 'IncreaseRedeemOrder': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128', 'amount': 'u128'}, 'DecreaseRedeemOrder': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128', 'amount': 'u128'}, 'CollectInvest': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128'}, 'CollectRedeem': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128'}, 'ExecutedDecreaseInvestOrder': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128', 'currency_payout': 'u128', 'remaining_invest_amount': 'u128'}, 'ExecutedDecreaseRedeemOrder': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128', 'tranche_tokens_payout': 'u128', 'remaining_redeem_amount': 'u128'}, 'ExecutedCollectInvest': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128', 'currency_payout': 'u128', 'tranche_tokens_payout': 'u128', 'remaining_invest_amount': 'u128'}, 'ExecutedCollectRedeem': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128', 'currency_payout': 'u128', 'tranche_tokens_payout': 'u128', 'remaining_redeem_amount': 'u128'}, 'CancelInvestOrder': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128'}, 'CancelRedeemOrder': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128'}, 'ScheduleUpgrade': {'contract': '[u8; 20]'}, 'CancelUpgrade': {'contract': '[u8; 20]'}, 'UpdateTrancheTokenMetadata': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'token_name': '[u8; 128]', 'token_symbol': '[u8; 32]'}}```

---------
### RelayerAdded
A relayer was added.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| relayer | `DomainAddress` | ```{'Centrifuge': '[u8; 32]', 'EVM': ('u64', '[u8; 20]')}```

---------
### RelayerRemoved
A relayer was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| relayer | `DomainAddress` | ```{'Centrifuge': '[u8; 32]', 'EVM': ('u64', '[u8; 20]')}```

---------
## Storage functions

---------
### Allowlist
 Storage that contains a limited number of whitelisted instances of
 deployed liquidity pools for a particular domain.

 This can only be modified by an admin.

#### Python
```python
result = substrate.query(
    'LiquidityPoolsGateway', 'Allowlist', [
    {'Centrifuge': None, 'EVM': 'u64'},
    {
        'Centrifuge': '[u8; 32]',
        'EVM': ('u64', '[u8; 20]'),
    },
]
)
```

#### Return value
```python
()
```
---------
### DomainRouters
 Storage for domain routers.

 This can only be set by an admin.

#### Python
```python
result = substrate.query(
    'LiquidityPoolsGateway', 'DomainRouters', [{'Centrifuge': None, 'EVM': 'u64'}]
)
```

#### Return value
```python
{
    'AxelarEVM': {
        'evm_chain': 'Bytes',
        'liquidity_pools_contract_address': '[u8; 20]',
        'router': {
            'evm_domain': {
                'fee_values': {
                    'gas_limit': '[u64; 4]',
                    'gas_price': '[u64; 4]',
                    'value': '[u64; 4]',
                },
                'target_contract_address': '[u8; 20]',
                'target_contract_hash': '[u8; 32]',
            },
        },
    },
    'AxelarXCM': {
        'axelar_target_chain': 'Bytes',
        'axelar_target_contract': '[u8; 20]',
        'router': {
            'xcm_domain': {
                'contract_address': '[u8; 20]',
                'ethereum_xcm_transact_call_index': 'Bytes',
                'fee_amount': 'u128',
                'fee_currency': {
                    'AUSD': None,
                    'ForeignAsset': 'u32',
                    'Native': None,
                    'Staking': 'scale_info::72',
                    None: None,
                    'Tranche': ('u64', '[u8; 16]'),
                },
                'location': {
                    None: None,
                    'V2': 'scale_info::107',
                    'V3': 'scale_info::116',
                },
                'max_gas_limit': 'u64',
                'overall_weight': {'proof_size': 'u64', 'ref_time': 'u64'},
                'transact_required_weight_at_most': {
                    'proof_size': 'u64',
                    'ref_time': 'u64',
                },
            },
        },
    },
    'EthereumXCM': {
        'router': {
            'xcm_domain': {
                'contract_address': '[u8; 20]',
                'ethereum_xcm_transact_call_index': 'Bytes',
                'fee_amount': 'u128',
                'fee_currency': {
                    None: None,
                    'AUSD': None,
                    'ForeignAsset': 'u32',
                    'Native': None,
                    'Staking': 'scale_info::72',
                    'Tranche': ('u64', '[u8; 16]'),
                },
                'location': {
                    None: None,
                    'V2': 'scale_info::107',
                    'V3': 'scale_info::116',
                },
                'max_gas_limit': 'u64',
                'overall_weight': {'proof_size': 'u64', 'ref_time': 'u64'},
                'transact_required_weight_at_most': {
                    'proof_size': 'u64',
                    'ref_time': 'u64',
                },
            },
        },
    },
}
```
---------
### RelayerList
 Storage that contains a limited number of whitelisted instances of
 deployed liquidity pools for a particular domain.

 This can only be modified by an admin.

#### Python
```python
result = substrate.query(
    'LiquidityPoolsGateway', 'RelayerList', [
    {'Centrifuge': None, 'EVM': 'u64'},
    {
        'Centrifuge': '[u8; 32]',
        'EVM': ('u64', '[u8; 20]'),
    },
]
)
```

#### Return value
```python
()
```
---------
## Constants

---------
### MaxIncomingMessageSize
 Maximum size of an incoming message.
#### Value
```python
1024
```
#### Python
```python
constant = substrate.get_constant('LiquidityPoolsGateway', 'MaxIncomingMessageSize')
```
---------
### Sender
 The sender account that will be used in the OutboundQueue
 implementation.
#### Value
```python
'4dx57qdyveJ8kD3JGaPgR8aUSvtZvqX7LV1YaU98LiHztinf'
```
#### Python
```python
constant = substrate.get_constant('LiquidityPoolsGateway', 'Sender')
```
---------
## Errors

---------
### DomainNotSupported
The domain is not supported.

---------
### InstanceAlreadyAdded
Instance was already added to the domain.

---------
### InvalidMessageOrigin
The origin of the message to be processed is invalid.

---------
### MaxDomainInstances
Maximum number of instances for a domain was reached.

---------
### MessageDecodingFailed
Message decoding error.

---------
### RelayerAlreadyAdded
Relayer was already added to the domain

---------
### RelayerMessageDecodingFailed
Relayer messages need to prepend the with
the original source chain and source address
that triggered the message.
Decoding that is essential and this error
signals malforming of the wrapping information.

---------
### RouterInitFailed
Router initialization failed.

---------
### RouterNotFound
Router not found.

---------
### UnknownInstance
Unknown instance.

---------
### UnknownRelayer
Unknown relayer

---------