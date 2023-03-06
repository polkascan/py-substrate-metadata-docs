
# AresOracle

---------
## Calls

---------
### revoke_update_request_propose
Revoke the `key-pair` on the request token list.

The dispatch origin for this call must be _Signed_ of Technical-Committee.

- price_key: A price key, such as `btc-usdt`
#### Attributes
| Name | Type |
| -------- | -------- | 
| price_key | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'AresOracle', 'revoke_update_request_propose', {'price_key': 'Bytes'}
)
```

---------
### submit_ask_price
Submit an ares-price request, The request is processed by all online validators,
and the aggregated result is returned immediately.

The dispatch origin for this call must be _Signed_.

- max_fee: The highest asking fee accepted by the signer.
- request_keys: A list of `Trading pairs`, separated by commas if multiple, such as: `eth-usdt, dot-sudt`, etc.
#### Attributes
| Name | Type |
| -------- | -------- | 
| max_fee | `BalanceOf<T>` | 
| request_keys | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'AresOracle', 'submit_ask_price', {
    'max_fee': 'u128',
    'request_keys': 'Bytes',
}
)
```

---------
### submit_create_pre_check_task
Submit a pre-check task.
When a new validator is elected, a pre_check_task task will be submitted through this method
within a specific period.

This task is used to ensure that the ares-price response function of the validator node can be used normally.

The dispatch origin fo this call must be __none__.

- precheck_payload: Pre-Check task data, including validators and their authority account data.
#### Attributes
| Name | Type |
| -------- | -------- | 
| precheck_payload | `PreCheckPayload<T::Public, T::BlockNumber, T::AccountId, T::
AuthorityAres>` | 
| signature | `OffchainSignature<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AresOracle', 'submit_create_pre_check_task', {
    'precheck_payload': {
        'auth': '[u8; 32]',
        'block_number': 'u32',
        'pre_check_auth': '[u8; 32]',
        'pre_check_stash': 'AccountId',
        'public': {
            'Ecdsa': '[u8; 33]',
            'Ed25519': '[u8; 32]',
            'Sr25519': '[u8; 32]',
        },
    },
    'signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### submit_forced_clear_purchased_price_payload_signed
An offline method that submits and saves the purchase-result data.
If the count of validator submitted by `purchase-id` already
reached the threshold requirements, then average price will be
aggregation and mark [PURCHASED_FINAL_TYPE_IS_PART_PARTICIPATE](PURCHASED_FINAL_TYPE_IS_PART_PARTICIPATE)

The dispatch origin fo this call must be __none__.

-- price_payload: Submitted data.
#### Attributes
| Name | Type |
| -------- | -------- | 
| price_payload | `PurchasedForceCleanPayload<T::Public, T::BlockNumber, T::AuthorityAres
>` | 
| signature | `OffchainSignature<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AresOracle', 'submit_forced_clear_purchased_price_payload_signed', {
    'price_payload': {
        'auth': '[u8; 32]',
        'block_number': 'u32',
        'public': {
            'Ecdsa': '[u8; 33]',
            'Ed25519': '[u8; 32]',
            'Sr25519': '[u8; 32]',
        },
        'purchase_id_list': ['Bytes'],
    },
    'signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### submit_local_xray
An offline method that submits and saves the local publicly data by the validator node to the chain for debugging.

The dispatch origin fo this call must be __none__.

- host_key: A random `u32` for a node
	- request_domain: The warehouse parameter currently set by the node.
	- authority_list: List of ares-authority public keys stored locally
	- network_is_validator: Whether the node validator
#### Attributes
| Name | Type |
| -------- | -------- | 
| host_key | `u32` | 
| request_domain | `RequestBaseVecU8` | 
| authority_list | `AuthorityAresVec<T::AuthorityAres>` | 
| network_is_validator | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'AresOracle', 'submit_local_xray', {
    'authority_list': ['[u8; 32]'],
    'host_key': 'u32',
    'network_is_validator': 'bool',
    'request_domain': 'Bytes',
}
)
```

---------
### submit_offchain_http_err_trace_result
When there is an error in the offchain http request, the error data will be submitted to the chain through this Call

The dispatch origin fo this call must be __none__.

- err_payload: Http err data.
#### Attributes
| Name | Type |
| -------- | -------- | 
| err_payload | `HttpErrTracePayload<T::Public, T::BlockNumber, T::AuthorityAres, T::
AccountId>` | 
| signature | `OffchainSignature<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AresOracle', 'submit_offchain_http_err_trace_result', {
    'err_payload': {
        'auth': '[u8; 32]',
        'public': {
            'Ecdsa': '[u8; 33]',
            'Ed25519': '[u8; 32]',
            'Sr25519': '[u8; 32]',
        },
        'trace_data': {
            'block_number': 'u32',
            'err_auth': 'AccountId',
            'err_status': {
                'IoErr': 'Bytes',
                'ParseErr': 'Bytes',
                'StatusErr': (
                    'Bytes',
                    'u16',
                ),
                'TimeOut': 'Bytes',
            },
            'tip': 'Bytes',
        },
    },
    'signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### submit_offchain_pre_check_result
When the validator responds to the pre-check task, the pre-check result data is submitted to the chain.
If approved, it will be passed in the next election cycle, not immediately.

The dispatch origin fo this call must be __none__.

- preresult_payload: Review response result data, which will be compared on-chain.
#### Attributes
| Name | Type |
| -------- | -------- | 
| preresult_payload | `PreCheckResultPayload<T::Public, T::BlockNumber, T::AccountId, T::
AuthorityAres>` | 
| signature | `OffchainSignature<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AresOracle', 'submit_offchain_pre_check_result', {
    'preresult_payload': {
        'block_number': 'u32',
        'pre_check_auth': '[u8; 32]',
        'pre_check_list': [
            {
                'max_offset': 'u8',
                'number_val': {
                    'exponent': 'i32',
                    'fraction': 'u64',
                    'fraction_length': 'u32',
                    'integer': 'u64',
                },
                'price_key': 'Bytes',
                'timestamp': 'u64',
            },
        ],
        'pre_check_stash': 'AccountId',
        'public': {
            'Ecdsa': '[u8; 33]',
            'Ed25519': '[u8; 32]',
            'Sr25519': '[u8; 32]',
        },
        'task_at': 'u32',
    },
    'signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### submit_price_unsigned_with_signed_payload
An offline method that submits and saves the free ares-price results.

The dispatch origin fo this call must be __none__.

- price_payload: Ares-price data to be uploaded.
#### Attributes
| Name | Type |
| -------- | -------- | 
| price_payload | `PricePayload<T::Public, T::BlockNumber, T::AuthorityAres>` | 
| signature | `OffchainSignature<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AresOracle', 'submit_price_unsigned_with_signed_payload', {
    'price_payload': {
        'auth': '[u8; 32]',
        'block_number': 'u32',
        'jump_block': [('Bytes', 'u8')],
        'price': [
            (
                'Bytes',
                'u64',
                'u32',
                {
                    'exponent': 'i32',
                    'fraction': 'u64',
                    'fraction_length': 'u32',
                    'integer': 'u64',
                },
                'u64',
            ),
        ],
        'public': {
            'Ecdsa': '[u8; 33]',
            'Ed25519': '[u8; 32]',
            'Sr25519': '[u8; 32]',
        },
    },
    'signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### submit_purchased_price_unsigned_with_signed_payload
An offline method that submits and saves the purchase-result data.
If all validators submit price-result, then average price will be
aggregation and mark [PURCHASED_FINAL_TYPE_IS_ALL_PARTICIPATE](PURCHASED_FINAL_TYPE_IS_ALL_PARTICIPATE)

The dispatch origin fo this call must be __none__.

-- price_payload: Submitted data.
#### Attributes
| Name | Type |
| -------- | -------- | 
| price_payload | `PurchasedPricePayload<T::Public, T::BlockNumber, T::AuthorityAres>` | 
| signature | `OffchainSignature<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AresOracle', 'submit_purchased_price_unsigned_with_signed_payload', {
    'price_payload': {
        'auth': '[u8; 32]',
        'block_number': 'u32',
        'price': [
            (
                'Bytes',
                'u64',
                'u32',
                {
                    'exponent': 'i32',
                    'fraction': 'u64',
                    'fraction_length': 'u32',
                    'integer': 'u64',
                },
                'u64',
            ),
        ],
        'public': {
            'Ecdsa': '[u8; 33]',
            'Ed25519': '[u8; 32]',
            'Sr25519': '[u8; 32]',
        },
        'purchase_id': 'Bytes',
    },
    'signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### update_allowable_offset_propose
Update the value of the `allowable offset` parameter to determine the abnormal range of the submitted price

The dispatch origin for this call must be _Signed_ of Technical-Committee.

- offset: A Percent value.
#### Attributes
| Name | Type |
| -------- | -------- | 
| offset | `Percent` | 

#### Python
```python
call = substrate.compose_call(
    'AresOracle', 'update_allowable_offset_propose', {'offset': 'u8'}
)
```

---------
### update_config_of_data_submission_interval
Updating the ConfDataSubmissionInterval parameter settings requires the `Technical-Committee` signature to execute.

The dispatch origin for this call must be _Signed_ of Technical-Committee.

- interval: Maximum allowed interval
#### Attributes
| Name | Type |
| -------- | -------- | 
| interval | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'AresOracle', 'update_config_of_data_submission_interval', {'interval': 'u32'}
)
```

---------
### update_ocw_control_setting
Update the control parameters of ares-oracle

The dispatch origin for this call must be _Signed_ of Technical-Committee.

- need_verifier_check: Whether to start the validator checker.
- open_free_price_reporter: Whether the `free-price` moudle is enabled.
- open_paid_price_reporter: Whether the `ask-price` moudle is enabled.
#### Attributes
| Name | Type |
| -------- | -------- | 
| need_verifier_check | `bool` | 
| open_free_price_reporter | `bool` | 
| open_paid_price_reporter | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'AresOracle', 'update_ocw_control_setting', {
    'need_verifier_check': 'bool',
    'open_free_price_reporter': 'bool',
    'open_paid_price_reporter': 'bool',
}
)
```

---------
### update_pool_depth_propose
Update the depth of the price pool. When the price pool reaches the maximum value,
the average price will be aggregated and put on the chain.

The dispatch origin for this call must be _Signed_ of Technical-Committee.

- depth: u32 integer
#### Attributes
| Name | Type |
| -------- | -------- | 
| depth | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'AresOracle', 'update_pool_depth_propose', {'depth': 'u32'}
)
```

---------
### update_pre_check_allowable_offset
The maximum offset allowed for `pre-check` when validation.

The dispatch origin for this call must be _Signed_ of Technical-Committee.

- offset: Percent
#### Attributes
| Name | Type |
| -------- | -------- | 
| offset | `Percent` | 

#### Python
```python
call = substrate.compose_call(
    'AresOracle', 'update_pre_check_allowable_offset', {'offset': 'u8'}
)
```

---------
### update_pre_check_session_multi
`session-multi` indicates the trigger `pre-check` session period before the era.

The dispatch origin for this call must be _Signed_ of Technical-Committee.

- multi: integer
#### Attributes
| Name | Type |
| -------- | -------- | 
| multi | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'AresOracle', 'update_pre_check_session_multi', {'multi': 'u32'}
)
```

---------
### update_pre_check_token_list
Update the pre-checked `Trading pairs` list for checking the validator price feature.

The dispatch origin for this call must be _Signed_ of Technical-Committee.

- token_list: [`PriceToken`](ares_oracle_provider_support::PriceToken)
#### Attributes
| Name | Type |
| -------- | -------- | 
| token_list | `TokenList` | 

#### Python
```python
call = substrate.compose_call(
    'AresOracle', 'update_pre_check_token_list', {'token_list': ['Bytes']}
)
```

---------
### update_purchased_param
Updating the purchase-related parameter settings requires the `Technical-Committee` signature to execute.

The dispatch origin for this call must be _Signed_ of Technical-Committee.

- submit_threshold: The threshold for aggregation is a percentage
- max_duration: Maximum delay to wait for full node response.
- avg_keep_duration: Maximum length to keep aggregated results.
#### Attributes
| Name | Type |
| -------- | -------- | 
| submit_threshold | `Percent` | 
| max_duration | `u64` | 
| avg_keep_duration | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'AresOracle', 'update_purchased_param', {
    'avg_keep_duration': 'u64',
    'max_duration': 'u64',
    'submit_threshold': 'u8',
}
)
```

---------
### update_request_propose
Modify or add a `key-pair` to the request list.

The dispatch origin for this call must be _Signed_ of Technical-Committee.

- price_key: A price key, such as `btc-usdt`.
- price_token: A price token, such as `btc`.
- parse_version: Parse version, currently only parameter 2 is supported.
- fraction_num: Fractions when parsing numbers.
- request_interval: The interval between validators submitting price on chain.
#### Attributes
| Name | Type |
| -------- | -------- | 
| price_key | `Vec<u8>` | 
| price_token | `Vec<u8>` | 
| parse_version | `u32` | 
| fraction_num | `FractionLength` | 
| request_interval | `RequestInterval` | 

#### Python
```python
call = substrate.compose_call(
    'AresOracle', 'update_request_propose', {
    'fraction_num': 'u32',
    'parse_version': 'u32',
    'price_key': 'Bytes',
    'price_token': 'Bytes',
    'request_interval': 'u8',
}
)
```

---------
## Events

---------
### AddPriceRequest
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| price_key | `PriceKey` | ```Bytes```
| price_token | `PriceToken` | ```Bytes```
| parse_version | `u32` | ```u32```
| fraction | `FractionLength` | ```u32```

---------
### AggregatedPrice
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| results | `Vec<
(PriceKey, u64, FractionLength, Vec<(T::AccountId, T::BlockNumber)>, T
::BlockNumber)>` | ```[('Bytes', 'u64', 'u32', [('AccountId', 'u32')], 'u32')]```

---------
### InsufficientCountOfValidators
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| purchase_id | `PurchaseId` | ```Bytes```

---------
### NewPreCheckResult
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| created_at | `T::BlockNumber` | ```u32```
| pre_check_list | `PreCheckList` | ```[{'price_key': 'Bytes', 'number_val': {'integer': 'u64', 'fraction': 'u64', 'fraction_length': 'u32', 'exponent': 'i32'}, 'max_offset': 'u8', 'timestamp': 'u64'}]```
| task_at | `T::BlockNumber` | ```u32```
| check_result | `PreCheckStatus` | ```('Review', 'Prohibit', 'Pass')```

---------
### NewPreCheckTask
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| authority | `T::AuthorityAres` | ```[u8; 32]```
| block | `T::BlockNumber` | ```u32```

---------
### NewPurchasedPrice
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| created_at | `T::BlockNumber` | ```u32```
| price_list | `PricePayloadSubPriceList` | ```[('Bytes', 'u64', 'u32', {'integer': 'u64', 'fraction': 'u64', 'fraction_length': 'u32', 'exponent': 'i32'}, 'u64')]```
| who | `T::AccountId` | ```AccountId```
| finance_era | `EraIndex` | ```u32```
| purchase_id | `PurchaseId` | ```Bytes```

---------
### NewPurchasedRequest
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| purchase_id | `PurchaseId` | ```Bytes```
| request_data | `PurchasedRequestData<T::AccountId, BalanceOf<T>, T::BlockNumber>` | ```{'account_id': 'AccountId', 'offer': 'u128', 'create_bn': 'u32', 'submit_threshold': 'u8', 'max_duration': 'u64', 'request_keys': ['Bytes']}```
| value | `BalanceOf<T>` | ```u128```
| finance_era | `EraIndex` | ```u32```

---------
### PriceAllowableOffsetUpdate
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| offset | `Percent` | ```u8```

---------
### PricePoolDepthUpdate
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| depth | `u32` | ```u32```

---------
### ProblemWithRefund
#### Attributes
No attributes

---------
### PurchasedAvgPrice
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| purchase_id | `PurchaseId` | ```Bytes```
| event_results | `Vec<Option<(PriceKey, PurchasedAvgPriceData, Vec<T::AccountId>)>>` | ```[(None, ('Bytes', {'create_bn': 'u64', 'reached_type': 'u8', 'price_data': ('u64', 'u32')}, ['AccountId']))]```
| finance_era | `EraIndex` | ```u32```

---------
### PurchasedRequestWorkHasEnded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| purchase_id | `PurchaseId` | ```Bytes```
| who | `T::AccountId` | ```AccountId```
| finance_era | `EraIndex` | ```u32```

---------
### RevokePriceRequest
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| price_key | `PriceKey` | ```Bytes```

---------
### ToBeConvertedError
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| to_be | `DataTipVec` | ```Bytes```
| size | `u32` | ```u32```

---------
### UpdateDataSubmissionInterval
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| interval | `T::BlockNumber` | ```u32```

---------
### UpdateOcwControlSetting
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| setting | `OcwControlData` | ```{'need_verifier_check': 'bool', 'open_free_price_reporter': 'bool', 'open_paid_price_reporter': 'bool'}```

---------
### UpdatePriceRequest
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| price_key | `PriceKey` | ```Bytes```
| price_token | `PriceToken` | ```Bytes```
| parse_version | `u32` | ```u32```
| fraction | `FractionLength` | ```u32```

---------
### UpdatePurchasedDefaultSetting
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| setting | `PurchasedDefaultData` | ```{'submit_threshold': 'u8', 'max_duration': 'u64', 'avg_keep_duration': 'u64'}```

---------
## Storage functions

---------
### AggregatedMission

#### Python
```python
result = substrate.query(
    'AresOracle', 'AggregatedMission', ['[u8; 32]']
)
```

#### Return value
```python
('Bytes', 'u32', 'bool')
```
---------
### AresAbnormalPrice
 The lookup table for names.

#### Python
```python
result = substrate.query(
    'AresOracle', 'AresAbnormalPrice', ['Bytes']
)
```

#### Return value
```python
[
    (
        {
            'account_id': 'AccountId',
            'create_bn': 'u32',
            'fraction_len': 'u32',
            'price': 'u64',
            'raw_number': {
                'exponent': 'i32',
                'fraction': 'u64',
                'fraction_length': 'u32',
                'integer': 'u64',
            },
            'timestamp': 'u64',
            'update_bn': 'u32',
        },
        {'fraction_len': 'u32', 'integer': 'u64'},
    ),
]
```
---------
### AresAvgPrice

#### Python
```python
result = substrate.query(
    'AresOracle', 'AresAvgPrice', ['Bytes']
)
```

#### Return value
```python
('u64', 'u32', 'u32')
```
---------
### AresPrice
 The lookup table for names.

#### Python
```python
result = substrate.query(
    'AresOracle', 'AresPrice', ['Bytes']
)
```

#### Return value
```python
[
    {
        'account_id': 'AccountId',
        'create_bn': 'u32',
        'fraction_len': 'u32',
        'price': 'u64',
        'raw_number': {
            'exponent': 'i32',
            'fraction': 'u64',
            'fraction_length': 'u32',
            'integer': 'u64',
        },
        'timestamp': 'u64',
        'update_bn': 'u32',
    },
]
```
---------
### Authorities
 The current authority set.

#### Python
```python
result = substrate.query(
    'AresOracle', 'Authorities', []
)
```

#### Return value
```python
[('AccountId', '[u8; 32]')]
```
---------
### BlockAuthor

#### Python
```python
result = substrate.query(
    'AresOracle', 'BlockAuthor', []
)
```

#### Return value
```python
'AccountId'
```
---------
### BlockAuthorTrace

#### Python
```python
result = substrate.query(
    'AresOracle', 'BlockAuthorTrace', []
)
```

#### Return value
```python
[('AccountId', 'u32')]
```
---------
### ConfDataSubmissionInterval

#### Python
```python
result = substrate.query(
    'AresOracle', 'ConfDataSubmissionInterval', []
)
```

#### Return value
```python
'u32'
```
---------
### ConfPreCheckAllowableOffset

#### Python
```python
result = substrate.query(
    'AresOracle', 'ConfPreCheckAllowableOffset', []
)
```

#### Return value
```python
'u8'
```
---------
### ConfPreCheckSessionMulti

#### Python
```python
result = substrate.query(
    'AresOracle', 'ConfPreCheckSessionMulti', []
)
```

#### Return value
```python
'u32'
```
---------
### ConfPreCheckTokenList

#### Python
```python
result = substrate.query(
    'AresOracle', 'ConfPreCheckTokenList', []
)
```

#### Return value
```python
['Bytes']
```
---------
### FinalPerCheckResult

#### Python
```python
result = substrate.query(
    'AresOracle', 'FinalPerCheckResult', ['AccountId']
)
```

#### Return value
```python
(
    None,
    (
        'u32',
        ('Review', 'Prohibit', 'Pass'),
        (
            None,
            {
                'chain_avg_price_list': 'scale_info::508',
                'raw_precheck_list': ['scale_info::81'],
                'validator_up_price_list': 'scale_info::508',
            },
        ),
        '[u8; 32]',
    ),
)
```
---------
### HttpErrTraceLogV1

#### Python
```python
result = substrate.query(
    'AresOracle', 'HttpErrTraceLogV1', []
)
```

#### Return value
```python
[
    {
        'block_number': 'u32',
        'err_auth': 'AccountId',
        'err_status': {
            'IoErr': 'Bytes',
            'ParseErr': 'Bytes',
            'StatusErr': ('Bytes', 'u16'),
            'TimeOut': 'Bytes',
        },
        'tip': 'Bytes',
    },
]
```
---------
### JumpBlockNumber

#### Python
```python
result = substrate.query(
    'AresOracle', 'JumpBlockNumber', ['Bytes']
)
```

#### Return value
```python
'u64'
```
---------
### LastPriceAuthor

#### Python
```python
result = substrate.query(
    'AresOracle', 'LastPriceAuthor', ['Bytes']
)
```

#### Return value
```python
('AccountId', 'u32')
```
---------
### LocalXRay

#### Python
```python
result = substrate.query(
    'AresOracle', 'LocalXRay', ['u32']
)
```

#### Return value
```python
('u32', 'Bytes', ['[u8; 32]'], 'bool')
```
---------
### OcwControlSetting

#### Python
```python
result = substrate.query(
    'AresOracle', 'OcwControlSetting', []
)
```

#### Return value
```python
{
    'need_verifier_check': 'bool',
    'open_free_price_reporter': 'bool',
    'open_paid_price_reporter': 'bool',
}
```
---------
### PreCheckTaskList

#### Python
```python
result = substrate.query(
    'AresOracle', 'PreCheckTaskList', []
)
```

#### Return value
```python
[('AccountId', '[u8; 32]', 'u32')]
```
---------
### PriceAllowableOffset

#### Python
```python
result = substrate.query(
    'AresOracle', 'PriceAllowableOffset', []
)
```

#### Return value
```python
'u8'
```
---------
### PriceCounter

#### Python
```python
result = substrate.query(
    'AresOracle', 'PriceCounter', ['Bytes']
)
```

#### Return value
```python
'u32'
```
---------
### PricePoolDepth

#### Python
```python
result = substrate.query(
    'AresOracle', 'PricePoolDepth', []
)
```

#### Return value
```python
'u32'
```
---------
### PricesRequests

#### Python
```python
result = substrate.query(
    'AresOracle', 'PricesRequests', []
)
```

#### Return value
```python
[('Bytes', 'Bytes', 'u32', 'u32', 'u8')]
```
---------
### PurchasedAvgPrice

#### Python
```python
result = substrate.query(
    'AresOracle', 'PurchasedAvgPrice', ['Bytes', 'Bytes']
)
```

#### Return value
```python
{'create_bn': 'u64', 'price_data': ('u64', 'u32'), 'reached_type': 'u8'}
```
---------
### PurchasedAvgTrace

#### Python
```python
result = substrate.query(
    'AresOracle', 'PurchasedAvgTrace', ['Bytes']
)
```

#### Return value
```python
'u32'
```
---------
### PurchasedDefaultSetting

#### Python
```python
result = substrate.query(
    'AresOracle', 'PurchasedDefaultSetting', []
)
```

#### Return value
```python
{'avg_keep_duration': 'u64', 'max_duration': 'u64', 'submit_threshold': 'u8'}
```
---------
### PurchasedOrderPool

#### Python
```python
result = substrate.query(
    'AresOracle', 'PurchasedOrderPool', ['Bytes', 'AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### PurchasedPricePool

#### Python
```python
result = substrate.query(
    'AresOracle', 'PurchasedPricePool', ['Bytes', 'Bytes']
)
```

#### Return value
```python
[
    {
        'account_id': 'AccountId',
        'create_bn': 'u32',
        'fraction_len': 'u32',
        'price': 'u64',
        'raw_number': {
            'exponent': 'i32',
            'fraction': 'u64',
            'fraction_length': 'u32',
            'integer': 'u64',
        },
        'timestamp': 'u64',
        'update_bn': 'u32',
    },
]
```
---------
### PurchasedRequestPool

#### Python
```python
result = substrate.query(
    'AresOracle', 'PurchasedRequestPool', ['Bytes']
)
```

#### Return value
```python
{
    'account_id': 'AccountId',
    'create_bn': 'u32',
    'max_duration': 'u64',
    'offer': 'u128',
    'request_keys': ['Bytes'],
    'submit_threshold': 'u8',
}
```
---------
### RequestBaseOnchain

#### Python
```python
result = substrate.query(
    'AresOracle', 'RequestBaseOnchain', []
)
```

#### Return value
```python
'Bytes'
```
---------
### StorageVersion

#### Python
```python
result = substrate.query(
    'AresOracle', 'StorageVersion', []
)
```

#### Return value
```python
(
    'V1_0_0_Ancestral',
    'V1_0_1_HttpErrUpgrade',
    'V1_1_0_HttpErrUpgrade',
    'V1_2_0',
)
```
---------
### SymbolFraction

#### Python
```python
result = substrate.query(
    'AresOracle', 'SymbolFraction', ['Bytes']
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### CalculationKind
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('AresOracle', 'CalculationKind')
```
---------
### ErrLogPoolDepth
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('AresOracle', 'ErrLogPoolDepth')
```
---------
### UnsignedPriority
#### Value
```python
1048576
```
#### Python
```python
constant = substrate.get_constant('AresOracle', 'UnsignedPriority')
```
---------
## Errors

---------
### BlockAuthorNotFound
Block author not found.

---------
### BoundedVecExceededMaxLength
BoundedVec exceeded its maximum length

---------
### DruationNumberNotBeZero
Waiting for delay block must be greater than 0 after ask priced.

---------
### InsufficientBalance
Insufficient balance when the ask price to pay.

---------
### InsufficientMaxFee
The `MaxFee` of the ask price payment limit is too low.

---------
### NoPricePairsAvailable
No available `Trading pairs` are found.

---------
### PayToPurchaseFeeFailed
Occurred while requesting payment, please check if `Balance` is sufficient.

---------
### PerCheckTaskAlreadyExists
The validator `pre-check task` already exists, no need to resubmit.

---------
### PreCheckTokenListNotEmpty
The list of pre-checked token pairs cannot be empty.

---------
### PurchaseIdNotFoundInThePool
The purchase ID was not found in the request pool.

---------
### SubmitThresholdRangeError
The value range of the ask price threshold value must be 1~100 .

---------