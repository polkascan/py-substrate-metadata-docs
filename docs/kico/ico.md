
# Ico

---------
## Calls

---------
### cancel_request
The project party cancels the request for release of funds.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `AssetId` | 
| index | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Ico', 'cancel_request', {'currency_id': 'u32', 'index': 'u32'}
)
```

---------
### get_reward
When the end of the ico, users get the reward.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `AssetId` | 
| index | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Ico', 'get_reward', {'currency_id': 'u32', 'index': 'u32'}
)
```

---------
### initiate_ico
The project party initiates an ICO
#### Attributes
| Name | Type |
| -------- | -------- | 
| info | `IcoParameters<T::BlockNumber, MultiBalanceOf<T>, AssetId, AreaCode>` | 

#### Python
```python
call = substrate.compose_call(
    'Ico', 'initiate_ico', {
    'info': {
        'currency_id': 'u32',
        'desc': 'Bytes',
        'exchange_token': 'u32',
        'exchange_token_total_amount': 'u128',
        'exclude_area': [
            (
                'AF',
                'AX',
                'AL',
                'DZ',
                'AS',
                'AD',
                'AO',
                'AI',
                'AQ',
                'AG',
                'AR',
                'AM',
                'AW',
                'AU',
                'AT',
                'AZ',
                'BS',
                'BH',
                'BD',
                'BB',
                'BY',
                'BE',
                'BZ',
                'BJ',
                'BM',
                'BT',
                'BO',
                'BQ',
                'BA',
                'BW',
                'BV',
                'BR',
                'IO',
                'BN',
                'BG',
                'BF',
                'BI',
                'CV',
                'KH',
                'CM',
                'CA',
                'KY',
                'CF',
                'TD',
                'CL',
                'CN',
                'CX',
                'CC',
                'CO',
                'KM',
                'CD',
                'CG',
                'CK',
                'CR',
                'CI',
                'HR',
                'CU',
                'CW',
                'CY',
                'CZ',
                'DK',
                'DJ',
                'DM',
                'DO',
                'EC',
                'EG',
                'SV',
                'GQ',
                'ER',
                'EE',
                'SZ',
                'ET',
                'FK',
                'FO',
                'FJ',
                'FI',
                'FR',
                'GF',
                'PF',
                'TF',
                'GA',
                'GM',
                'GE',
                'DE',
                'GH',
                'GI',
                'GR',
                'GL',
                'GD',
                'GP',
                'GU',
                'GT',
                'GG',
                'GN',
                'GW',
                'GY',
                'HT',
                'HM',
                'VA',
                'HN',
                'HK',
                'HU',
                'IS',
                'IN',
                'ID',
                'IR',
                'IQ',
                'IE',
                'IM',
                'IL',
                'IT',
                'JM',
                'JP',
                'JE',
                'JO',
                'KZ',
                'KE',
                'KI',
                'KP',
                'KR',
                'KW',
                'KG',
                'LA',
                'LV',
                'LB',
                'LS',
                'LR',
                'LY',
                'LI',
                'LT',
                'LU',
                'MO',
                'MK',
                'MG',
                'MW',
                'MY',
                'MV',
                'ML',
                'MT',
                'MH',
                'MQ',
                'MR',
                'MU',
                'YT',
                'MX',
                'FM',
                'MD',
                'MC',
                'MN',
                'ME',
                'MS',
                'MA',
                'MZ',
                'MM',
                'NA',
                'NR',
                'NP',
                'NL',
                'NC',
                'NZ',
                'NI',
                'NE',
                'NG',
                'NU',
                'NF',
                'MP',
                'NO',
                'OM',
                'PK',
                'PW',
                'PS',
                'PA',
                'PG',
                'PY',
                'PE',
                'PH',
                'PN',
                'PL',
                'PT',
                'PR',
                'QA',
                'RE',
                'RO',
                'RU',
                'RW',
                'BL',
                'SH',
                'KN',
                'LC',
                'MF',
                'PM',
                'VC',
                'WS',
                'SM',
                'ST',
                'SA',
                'SN',
                'RS',
                'SC',
                'SL',
                'SG',
                'SX',
                'SK',
                'SI',
                'SB',
                'SO',
                'ZA',
                'GS',
                'SS',
                'ES',
                'LK',
                'SD',
                'SR',
                'SJ',
                'SE',
                'CH',
                'SY',
                'TW',
                'TJ',
                'TZ',
                'TH',
                'TL',
                'TG',
                'TK',
                'TO',
                'TT',
                'TN',
                'TR',
                'TM',
                'TC',
                'TV',
                'UG',
                'UA',
                'AE',
                'GB',
                'UM',
                'US',
                'UY',
                'UZ',
                'VU',
                'VE',
                'VN',
                'VG',
                'VI',
                'WF',
                'EH',
                'YE',
                'ZM',
                'ZW',
            ),
        ],
        'ico_duration': 'u32',
        'is_must_kyc': 'bool',
        'lock_proportion': 'u8',
        'official_website': 'Bytes',
        'per_duration_unlock_amount': 'u128',
        'total_circulation': 'u128',
        'total_ico_amount': 'u128',
        'total_issuance': 'u128',
        'unlock_duration': 'u32',
        'user_ico_max_times': 'u8',
        'user_max_amount': 'u128',
        'user_min_amount': 'u128',
    },
}
)
```

---------
### initiator_set_ico_amount_bound
The initiator set the maximum and minimum ico amount.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `AssetId` | 
| index | `u32` | 
| min_amount | `MultiBalanceOf<T>` | 
| max_amount | `MultiBalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Ico', 'initiator_set_ico_amount_bound', {
    'currency_id': 'u32',
    'index': 'u32',
    'max_amount': 'u128',
    'min_amount': 'u128',
}
)
```

---------
### initiator_set_ico_max_times
The initiator sets per user ico max times of him project.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `AssetId` | 
| index | `u32` | 
| max_times | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'Ico', 'initiator_set_ico_max_times', {
    'currency_id': 'u32',
    'index': 'u32',
    'max_times': 'u8',
}
)
```

---------
### join
User participation in ICO
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `AssetId` | 
| index | `u32` | 
| amount | `MultiBalanceOf<T>` | 
| inviter | `Option<<T::Lookup as StaticLookup>::Source>` | 

#### Python
```python
call = substrate.compose_call(
    'Ico', 'join', {
    'amount': 'u128',
    'currency_id': 'u32',
    'index': 'u32',
    'inviter': (
        None,
        {
            'Address20': '[u8; 20]',
            'Address32': '[u8; 32]',
            'Id': 'AccountId',
            'Index': (),
            'Raw': 'Bytes',
        },
    ),
}
)
```

---------
### permit_ico
The foundation agrees to the ICO of the project party
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'Ico', 'permit_ico', {'currency_id': 'u32'}
)
```

---------
### permit_release
DAO allow asset release
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `AssetId` | 
| index | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Ico', 'permit_release', {'currency_id': 'u32', 'index': 'u32'}
)
```

---------
### reject_ico
The foundation opposes the ICO of the project party
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'Ico', 'reject_ico', {'currency_id': 'u32'}
)
```

---------
### request_release
The project party requests the release of the funds
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `AssetId` | 
| index | `u32` | 
| percent | `Percent` | 

#### Python
```python
call = substrate.compose_call(
    'Ico', 'request_release', {
    'currency_id': 'u32',
    'index': 'u32',
    'percent': 'u8',
}
)
```

---------
### set_asset_power_multiple
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `AssetId` | 
| multiple | `PowerMultiple` | 

#### Python
```python
call = substrate.compose_call(
    'Ico', 'set_asset_power_multiple', {
    'currency_id': 'u32',
    'multiple': {
        'down': 'u32',
        'up': 'u32',
    },
}
)
```

---------
### set_system_ico_amount_bound
The root sets the maximum and minimum ico amount.

This two values applies to all ICOs.
#### Attributes
| Name | Type |
| -------- | -------- | 
| min_amount | `MultiBalanceOf<T>` | 
| max_amount | `MultiBalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Ico', 'set_system_ico_amount_bound', {
    'max_amount': 'u128',
    'min_amount': 'u128',
}
)
```

---------
### terminate_ico
DAO terminate the ico
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `AssetId` | 
| index | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Ico', 'terminate_ico', {'currency_id': 'u32', 'index': 'u32'}
)
```

---------
### unlock
Users unlock their funds.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `AssetId` | 
| index | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Ico', 'unlock', {'currency_id': 'u32', 'index': 'u32'}
)
```

---------
### user_release_ico_amount
Users release their own asset.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `AssetId` | 
| index | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Ico', 'user_release_ico_amount', {'currency_id': 'u32', 'index': 'u32'}
)
```

---------
## Events

---------
### CancelRequest
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```
| None | `u32` | ```u32```

---------
### GetReward
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```
| None | `u32` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `MultiBalanceOf<T>` | ```u128```

---------
### InitiateIco
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetId` | ```u32```
| None | `MultiBalanceOf<T>` | ```u128```

---------
### InitiatorSetIcoAmountBound
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```
| None | `u32` | ```u32```
| None | `MultiBalanceOf<T>` | ```u128```
| None | `MultiBalanceOf<T>` | ```u128```

---------
### Join
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetId` | ```u32```
| None | `u32` | ```u32```
| None | `MultiBalanceOf<T>` | ```u128```
| None | `MultiBalanceOf<T>` | ```u128```

---------
### PermitIco
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetId` | ```u32```

---------
### PermitRelease
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```
| None | `u32` | ```u32```
| None | `Release<<T as system::Config>::AccountId,<T as system::Config>::
BlockNumber, AssetId, BalanceOf<T>>` | ```{'who': 'AccountId', 'currency_id': 'u32', 'index': 'u32', 'request_time': 'u32', 'percent': 'u8', 'pledge': 'u128'}```

---------
### RejectIco
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetId` | ```u32```

---------
### RequestRelease
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```
| None | `u32` | ```u32```
| None | `Percent` | ```u8```

---------
### SetAssetPowerMultiple
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```
| None | `PowerMultiple` | ```{'up': 'u32', 'down': 'u32'}```

---------
### SetIcoMaxCount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```
| None | `u32` | ```u32```
| None | `u8` | ```u8```

---------
### SetSystemIcoAmountBound
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MultiBalanceOf<T>` | ```u128```
| None | `MultiBalanceOf<T>` | ```u128```

---------
### TerminateIco
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```
| None | `u32` | ```u32```

---------
### TerminatedGiveBackAmount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetId` | ```u32```
| None | `u32` | ```u32```
| None | `MultiBalanceOf<T>` | ```u128```

---------
### Test
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### UnlockAsset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `MultiBalanceOf<T>` | ```u128```

---------
### UnreservedInitiatorRemainPledgeAmount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```
| None | `u32` | ```u32```
| None | `MultiBalanceOf<T>` | ```u128```

---------
### UserReleaseIcoAmount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```
| None | `u32` | ```u32```
| None | `MultiBalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### Ico

#### Python
```python
result = substrate.query(
    'Ico', 'Ico', ['u32', 'u32']
)
```

#### Return value
```python
{
    'already_released_proportion': 'u8',
    'currency_id': 'u32',
    'decimals': 'u8',
    'desc': 'Bytes',
    'exchange_token': 'u32',
    'exchange_token_total_amount': 'u128',
    'exclude_area': [
        (
            'AF',
            'AX',
            'AL',
            'DZ',
            'AS',
            'AD',
            'AO',
            'AI',
            'AQ',
            'AG',
            'AR',
            'AM',
            'AW',
            'AU',
            'AT',
            'AZ',
            'BS',
            'BH',
            'BD',
            'BB',
            'BY',
            'BE',
            'BZ',
            'BJ',
            'BM',
            'BT',
            'BO',
            'BQ',
            'BA',
            'BW',
            'BV',
            'BR',
            'IO',
            'BN',
            'BG',
            'BF',
            'BI',
            'CV',
            'KH',
            'CM',
            'CA',
            'KY',
            'CF',
            'TD',
            'CL',
            'CN',
            'CX',
            'CC',
            'CO',
            'KM',
            'CD',
            'CG',
            'CK',
            'CR',
            'CI',
            'HR',
            'CU',
            'CW',
            'CY',
            'CZ',
            'DK',
            'DJ',
            'DM',
            'DO',
            'EC',
            'EG',
            'SV',
            'GQ',
            'ER',
            'EE',
            'SZ',
            'ET',
            'FK',
            'FO',
            'FJ',
            'FI',
            'FR',
            'GF',
            'PF',
            'TF',
            'GA',
            'GM',
            'GE',
            'DE',
            'GH',
            'GI',
            'GR',
            'GL',
            'GD',
            'GP',
            'GU',
            'GT',
            'GG',
            'GN',
            'GW',
            'GY',
            'HT',
            'HM',
            'VA',
            'HN',
            'HK',
            'HU',
            'IS',
            'IN',
            'ID',
            'IR',
            'IQ',
            'IE',
            'IM',
            'IL',
            'IT',
            'JM',
            'JP',
            'JE',
            'JO',
            'KZ',
            'KE',
            'KI',
            'KP',
            'KR',
            'KW',
            'KG',
            'LA',
            'LV',
            'LB',
            'LS',
            'LR',
            'LY',
            'LI',
            'LT',
            'LU',
            'MO',
            'MK',
            'MG',
            'MW',
            'MY',
            'MV',
            'ML',
            'MT',
            'MH',
            'MQ',
            'MR',
            'MU',
            'YT',
            'MX',
            'FM',
            'MD',
            'MC',
            'MN',
            'ME',
            'MS',
            'MA',
            'MZ',
            'MM',
            'NA',
            'NR',
            'NP',
            'NL',
            'NC',
            'NZ',
            'NI',
            'NE',
            'NG',
            'NU',
            'NF',
            'MP',
            'NO',
            'OM',
            'PK',
            'PW',
            'PS',
            'PA',
            'PG',
            'PY',
            'PE',
            'PH',
            'PN',
            'PL',
            'PT',
            'PR',
            'QA',
            'RE',
            'RO',
            'RU',
            'RW',
            'BL',
            'SH',
            'KN',
            'LC',
            'MF',
            'PM',
            'VC',
            'WS',
            'SM',
            'ST',
            'SA',
            'SN',
            'RS',
            'SC',
            'SL',
            'SG',
            'SX',
            'SK',
            'SI',
            'SB',
            'SO',
            'ZA',
            'GS',
            'SS',
            'ES',
            'LK',
            'SD',
            'SR',
            'SJ',
            'SE',
            'CH',
            'SY',
            'TW',
            'TJ',
            'TZ',
            'TH',
            'TL',
            'TG',
            'TK',
            'TO',
            'TT',
            'TN',
            'TR',
            'TM',
            'TC',
            'TV',
            'UG',
            'UA',
            'AE',
            'GB',
            'UM',
            'US',
            'UY',
            'UZ',
            'VU',
            'VE',
            'VN',
            'VG',
            'VI',
            'WF',
            'EH',
            'YE',
            'ZM',
            'ZW',
        ),
    ],
    'ico_duration': 'u32',
    'index': (None, 'u32'),
    'initiator': 'AccountId',
    'is_already_kyc': 'bool',
    'is_must_kyc': 'bool',
    'is_terminated': 'bool',
    'lock_proportion': 'u8',
    'official_website': 'Bytes',
    'per_duration_unlock_amount': 'u128',
    'project_name': 'Bytes',
    'start_time': (None, 'u32'),
    'tag': (None, 'u128'),
    'token_symbol': 'Bytes',
    'total_circulation': 'u128',
    'total_ico_amount': 'u128',
    'total_issuance': 'u128',
    'total_usdt': 'u128',
    'unlock_duration': 'u32',
    'user_ico_max_times': 'u8',
    'user_max_amount': 'u128',
    'user_min_amount': 'u128',
}
```
---------
### IcoLocks

#### Python
```python
result = substrate.query(
    'Ico', 'IcoLocks', ['AccountId', 'u32']
)
```

#### Return value
```python
[
    {
        'index': 'u32',
        'per_duration_unlock_amount': 'u128',
        'start_block': 'u32',
        'total_amount': 'u128',
        'unlock_amount': 'u128',
        'unlock_duration': 'u32',
    },
]
```
---------
### IcoMaxUsdtAmount

#### Python
```python
result = substrate.query(
    'Ico', 'IcoMaxUsdtAmount', []
)
```

#### Return value
```python
'u128'
```
---------
### IcoMinUsdtAmount

#### Python
```python
result = substrate.query(
    'Ico', 'IcoMinUsdtAmount', []
)
```

#### Return value
```python
'u128'
```
---------
### IcoesOf

#### Python
```python
result = substrate.query(
    'Ico', 'IcoesOf', ['AccountId']
)
```

#### Return value
```python
[('u32', 'u32')]
```
---------
### Indexs

#### Python
```python
result = substrate.query(
    'Ico', 'Indexs', ['u32']
)
```

#### Return value
```python
['u32']
```
---------
### InitiatedIcoesOf

#### Python
```python
result = substrate.query(
    'Ico', 'InitiatedIcoesOf', ['AccountId']
)
```

#### Return value
```python
[
    {
        'amount': 'u128',
        'currency_id': 'u32',
        'decimals': 'u8',
        'desc': 'Bytes',
        'index': 'u32',
        'status': ('Checking', 'Failed', 'Passed'),
        'token_symbol': 'Bytes',
    },
]
```
---------
### InviteInfoOf

#### Python
```python
result = substrate.query(
    'Ico', 'InviteInfoOf', ['AccountId', 'u32']
)
```

#### Return value
```python
[
    {
        'currency_id': 'u32',
        'index': 'u32',
        'invitee': 'AccountId',
        'inviter': 'AccountId',
        'reward': (None, 'u128'),
    },
]
```
---------
### IsUnservePledge

#### Python
```python
result = substrate.query(
    'Ico', 'IsUnservePledge', ['u32', 'u32']
)
```

#### Return value
```python
'bool'
```
---------
### PassedIcoes

#### Python
```python
result = substrate.query(
    'Ico', 'PassedIcoes', []
)
```

#### Return value
```python
[('u32', 'u32')]
```
---------
### PendingIco

#### Python
```python
result = substrate.query(
    'Ico', 'PendingIco', []
)
```

#### Return value
```python
[
    {
        'ico': {
            'already_released_proportion': 'u8',
            'currency_id': 'u32',
            'decimals': 'u8',
            'desc': 'Bytes',
            'exchange_token': 'u32',
            'exchange_token_total_amount': 'u128',
            'exclude_area': [
                (
                    'AF',
                    'AX',
                    'AL',
                    'DZ',
                    'AS',
                    'AD',
                    'AO',
                    'AI',
                    'AQ',
                    'AG',
                    'AR',
                    'AM',
                    'AW',
                    'AU',
                    'AT',
                    'AZ',
                    'BS',
                    'BH',
                    'BD',
                    'BB',
                    'BY',
                    'BE',
                    'BZ',
                    'BJ',
                    'BM',
                    'BT',
                    'BO',
                    'BQ',
                    'BA',
                    'BW',
                    'BV',
                    'BR',
                    'IO',
                    'BN',
                    'BG',
                    'BF',
                    'BI',
                    'CV',
                    'KH',
                    'CM',
                    'CA',
                    'KY',
                    'CF',
                    'TD',
                    'CL',
                    'CN',
                    'CX',
                    'CC',
                    'CO',
                    'KM',
                    'CD',
                    'CG',
                    'CK',
                    'CR',
                    'CI',
                    'HR',
                    'CU',
                    'CW',
                    'CY',
                    'CZ',
                    'DK',
                    'DJ',
                    'DM',
                    'DO',
                    'EC',
                    'EG',
                    'SV',
                    'GQ',
                    'ER',
                    'EE',
                    'SZ',
                    'ET',
                    'FK',
                    'FO',
                    'FJ',
                    'FI',
                    'FR',
                    'GF',
                    'PF',
                    'TF',
                    'GA',
                    'GM',
                    'GE',
                    'DE',
                    'GH',
                    'GI',
                    'GR',
                    'GL',
                    'GD',
                    'GP',
                    'GU',
                    'GT',
                    'GG',
                    'GN',
                    'GW',
                    'GY',
                    'HT',
                    'HM',
                    'VA',
                    'HN',
                    'HK',
                    'HU',
                    'IS',
                    'IN',
                    'ID',
                    'IR',
                    'IQ',
                    'IE',
                    'IM',
                    'IL',
                    'IT',
                    'JM',
                    'JP',
                    'JE',
                    'JO',
                    'KZ',
                    'KE',
                    'KI',
                    'KP',
                    'KR',
                    'KW',
                    'KG',
                    'LA',
                    'LV',
                    'LB',
                    'LS',
                    'LR',
                    'LY',
                    'LI',
                    'LT',
                    'LU',
                    'MO',
                    'MK',
                    'MG',
                    'MW',
                    'MY',
                    'MV',
                    'ML',
                    'MT',
                    'MH',
                    'MQ',
                    'MR',
                    'MU',
                    'YT',
                    'MX',
                    'FM',
                    'MD',
                    'MC',
                    'MN',
                    'ME',
                    'MS',
                    'MA',
                    'MZ',
                    'MM',
                    'NA',
                    'NR',
                    'NP',
                    'NL',
                    'NC',
                    'NZ',
                    'NI',
                    'NE',
                    'NG',
                    'NU',
                    'NF',
                    'MP',
                    'NO',
                    'OM',
                    'PK',
                    'PW',
                    'PS',
                    'PA',
                    'PG',
                    'PY',
                    'PE',
                    'PH',
                    'PN',
                    'PL',
                    'PT',
                    'PR',
                    'QA',
                    'RE',
                    'RO',
                    'RU',
                    'RW',
                    'BL',
                    'SH',
                    'KN',
                    'LC',
                    'MF',
                    'PM',
                    'VC',
                    'WS',
                    'SM',
                    'ST',
                    'SA',
                    'SN',
                    'RS',
                    'SC',
                    'SL',
                    'SG',
                    'SX',
                    'SK',
                    'SI',
                    'SB',
                    'SO',
                    'ZA',
                    'GS',
                    'SS',
                    'ES',
                    'LK',
                    'SD',
                    'SR',
                    'SJ',
                    'SE',
                    'CH',
                    'SY',
                    'TW',
                    'TJ',
                    'TZ',
                    'TH',
                    'TL',
                    'TG',
                    'TK',
                    'TO',
                    'TT',
                    'TN',
                    'TR',
                    'TM',
                    'TC',
                    'TV',
                    'UG',
                    'UA',
                    'AE',
                    'GB',
                    'UM',
                    'US',
                    'UY',
                    'UZ',
                    'VU',
                    'VE',
                    'VN',
                    'VG',
                    'VI',
                    'WF',
                    'EH',
                    'YE',
                    'ZM',
                    'ZW',
                ),
            ],
            'ico_duration': 'u32',
            'index': (None, 'u32'),
            'initiator': 'AccountId',
            'is_already_kyc': 'bool',
            'is_must_kyc': 'bool',
            'is_terminated': 'bool',
            'lock_proportion': 'u8',
            'official_website': 'Bytes',
            'per_duration_unlock_amount': 'u128',
            'project_name': 'Bytes',
            'start_time': (None, 'u32'),
            'tag': (None, 'u128'),
            'token_symbol': 'Bytes',
            'total_circulation': 'u128',
            'total_ico_amount': 'u128',
            'total_issuance': 'u128',
            'total_usdt': 'u128',
            'unlock_duration': 'u32',
            'user_ico_max_times': 'u8',
            'user_max_amount': 'u128',
            'user_min_amount': 'u128',
        },
        'pledge_dico': 'u128',
        'pledge_exchange_token': 'u128',
    },
]
```
---------
### PowerMultipleOf

#### Python
```python
result = substrate.query(
    'Ico', 'PowerMultipleOf', ['u32']
)
```

#### Return value
```python
{'down': 'u32', 'up': 'u32'}
```
---------
### RequestReleaseInfo

#### Python
```python
result = substrate.query(
    'Ico', 'RequestReleaseInfo', []
)
```

#### Return value
```python
[
    {
        'currency_id': 'u32',
        'index': 'u32',
        'percent': 'u8',
        'pledge': 'u128',
        'request_time': 'u32',
        'who': 'AccountId',
    },
]
```
---------
### TotalNum

#### Python
```python
result = substrate.query(
    'Ico', 'TotalNum', []
)
```

#### Return value
```python
'u32'
```
---------
### TotalPowerOf

#### Python
```python
result = substrate.query(
    'Ico', 'TotalPowerOf', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### TotalUsdt

#### Python
```python
result = substrate.query(
    'Ico', 'TotalUsdt', []
)
```

#### Return value
```python
'u128'
```
---------
### UnReleaseAssets

#### Python
```python
result = substrate.query(
    'Ico', 'UnReleaseAssets', ['AccountId']
)
```

#### Return value
```python
[
    {
        'currency_id': 'u32',
        'index': 'u32',
        'inviter': (None, 'AccountId'),
        'refund': 'u128',
        'released': 'u128',
        'reward': (None, 'u128'),
        'tags': [('u128', 'u128', 'u128', 'u128')],
        'total': 'u128',
        'total_usdt': 'u128',
        'unreleased_currency_id': 'u32',
    },
]
```
---------
## Constants

---------
### ChillDuration
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('Ico', 'ChillDuration')
```
---------
### IcoTotalReward
#### Value
```python
200000000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Ico', 'IcoTotalReward')
```
---------
### InitiatorBond
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Ico', 'InitiatorBond')
```
---------
### InitiatorPledge
#### Value
```python
10000000000000000
```
#### Python
```python
constant = substrate.get_constant('Ico', 'InitiatorPledge')
```
---------
### InviteeRewardProportion
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Ico', 'InviteeRewardProportion')
```
---------
### InviterRewardProportion
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Ico', 'InviterRewardProportion')
```
---------
### ReleaseProtectPeriod
#### Value
```python
33
```
#### Python
```python
constant = substrate.get_constant('Ico', 'ReleaseProtectPeriod')
```
---------
### RequestExpire
#### Value
```python
36000
```
#### Python
```python
constant = substrate.get_constant('Ico', 'RequestExpire')
```
---------
### RequestPledge
#### Value
```python
30000000000000000
```
#### Python
```python
constant = substrate.get_constant('Ico', 'RequestPledge')
```
---------
### TerminateProtectPeriod
#### Value
```python
33
```
#### Python
```python
constant = substrate.get_constant('Ico', 'TerminateProtectPeriod')
```
---------
### USDCurrencyId
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Ico', 'USDCurrencyId')
```
---------
## Errors

---------
### AlreadyGetReward

---------
### AlreadyRequest

---------
### AmountIsZero

---------
### AmountNotMeetProjectRequirement

---------
### AmountNotMeetSystemRequirement

---------
### BadOrigin

---------
### BalanceInsufficient

---------
### BeingIco

---------
### CanNotInviteYouself

---------
### CirculationMoreThanIssuance

---------
### DivByZero

---------
### DownIsZero

---------
### DuplicateSet

---------
### DurationIsZero

---------
### ExchangeTokenBalanceTooLow

---------
### IcoAmountMoreThanCirculation

---------
### IcoExpire

---------
### IcoIndexNotExists

---------
### IcoNotExists123

---------
### IcoNotExpireOrTerminated

---------
### IcoTerminated

---------
### IcoTimesToMax

---------
### InExcludeArea

---------
### InitiatorIsYourself

---------
### InviterNotInIco

---------
### IsNotStartIcoTime

---------
### IsPendingIco

---------
### LockIsEmpty

---------
### MaxAmountIsZero

---------
### MaxAmountTooLarge

---------
### MaxIsZero

---------
### MaxLessThanMin

---------
### MinAmountTooLow

---------
### MultipleNotChange

---------
### NativeCurrencyId

---------
### NotIcoMember

---------
### NotInitiator

---------
### NotKycUser

---------
### Overflow

---------
### PendingIcoNotExists123

---------
### PowerIsZero

---------
### PriceNotExists

---------
### ProjectIcoAmountToMax

---------
### ProportionTooLow

---------
### ReleaseProtectTime

---------
### RequestExpire

---------
### RequestNotExists

---------
### RewardIsZero

---------
### StartTimeNotExists

---------
### TerminateProtectTime

---------
### TokenShouldBeDifferent

---------
### UnlockAmountIsZero

---------
### UnreleaseAmountIsZero

---------
### UnreleasedAmountIsZero

---------
### UserAreaNotExists

---------
### UserIcoAmountToMax

---------
### UserIcoAmountTooLow

---------