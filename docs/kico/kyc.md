
# Kyc

---------
## Calls

---------
### add_ias
 Add a identity authentication service(IAS)  provider to the system

Selection through Congress

- `ias_index`: KYCIndex.
- `ias_info`: IASInfo&lt;BalanceOf&lt;T&gt;, T::AccountId&gt;.

Emits `IASAdded` if successful.

\# &lt;weight&gt;
- TODO
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| ias_index | `KYCIndex` | 
| ias_info | `IASInfo<BalanceOf<T>, T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Kyc', 'add_ias', {
    'ias_index': 'u32',
    'ias_info': {
        'account': 'AccountId',
        'curve_public_key': '[u8; 32]',
        'fee': 'u128',
        'fields': (
            'Name',
            'Area',
            'CurvePubicKey',
            'Email',
        ),
    },
}
)
```

---------
### add_sword_holder
 add a sword holder  provider to the system

- `ias_index`: KYCIndex.
- `ias_info`: IASInfo&lt;BalanceOf&lt;T&gt;, T::AccountId&gt;.

Emits `IASAdded` if successful.

\# &lt;weight&gt;
- TODO
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| sword_index | `KYCIndex` | 
| sword_info | `IASInfo<BalanceOf<T>, T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Kyc', 'add_sword_holder', {
    'sword_index': 'u32',
    'sword_info': {
        'account': 'AccountId',
        'curve_public_key': '[u8; 32]',
        'fee': 'u128',
        'fields': (
            'Name',
            'Area',
            'CurvePubicKey',
            'Email',
        ),
    },
}
)
```

---------
### apply_certification
The user applies for verification by ias

The user must have submitted KYC and have not been added to the blacklist

- `kyc_fields`: KYCFields.
- `max_fee`: BalanceOf&lt;T&gt;.

Emits `ApplyCertification` if successful.

\# &lt;weight&gt;
- TODO
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| kyc_fields | `KYCFields` | 
| max_fee | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Kyc', 'apply_certification', {
    'kyc_fields': (
        'Name',
        'Area',
        'CurvePubicKey',
        'Email',
    ),
    'max_fee': 'u128',
}
)
```

---------
### clear_kyc
Users clean up their own KYC

The `ApplicationFormList` will also be cleaned up while cleaning up

Emits `KYCCleared` if successful.

\# &lt;weight&gt;
- TODO
\# &lt;/weight&gt;
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Kyc', 'clear_kyc', {}
)
```

---------
### ias_provide_judgement
IAS provide judgement

Only one passport can be provided, so when the passport is used for the second time,
the authentication fails

- `kyc_fields`: KYCFields.
- `kyc_index`: KYCIndex.
- `target`: AccountId.
- `judgement`: Judgement.
- `id`: Data. User&\#x27;s passport ID
- `message`: Message. Information sent to sword holder

Emits `JudgementGiven` if successful.

\# &lt;weight&gt;
- TODO
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| kyc_fields | `KYCFields` | 
| kyc_index | `KYCIndex` | 
| target | `T::AccountId` | 
| judgement | `Judgement<BalanceOf<T>>` | 
| id | `Data` | 
| message | `Message` | 

#### Python
```python
call = substrate.compose_call(
    'Kyc', 'ias_provide_judgement', {
    'id': 'Bytes',
    'judgement': {
        'Erroneous': None,
        'FeePaid': 'u128',
        'LowQuality': None,
        'OutOfDate': None,
        'PASS': None,
        'Repeat': None,
    },
    'kyc_fields': (
        'Name',
        'Area',
        'CurvePubicKey',
        'Email',
    ),
    'kyc_index': 'u32',
    'message': '[u8; 128]',
    'target': 'AccountId',
}
)
```

---------
### ias_set_fee
IAS sets its own service fees

- `kyc_fields`: KYCFields.
- `fee`: Balance.

Emits `SetFee` if successful.

\# &lt;weight&gt;
- TODO
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| kyc_fields | `KYCFields` | 
| fee | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Kyc', 'ias_set_fee', {
    'fee': 'u128',
    'kyc_fields': (
        'Name',
        'Area',
        'CurvePubicKey',
        'Email',
    ),
}
)
```

---------
### kill_ias
 remove a identity authentication service(IAS)  provider to the system

- `ias_index`: KYCIndex.
- `kyc_fields`: KYCFields.

Emits `IASRemoved` if successful.

\# &lt;weight&gt;
- TODO
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| ias_index | `KYCIndex` | 
| kyc_fields | `KYCFields` | 

#### Python
```python
call = substrate.compose_call(
    'Kyc', 'kill_ias', {
    'ias_index': 'u32',
    'kyc_fields': (
        'Name',
        'Area',
        'CurvePubicKey',
        'Email',
    ),
}
)
```

---------
### kill_sword_holder
 remove a sword holder  provider to the system

- `sword_holder_index`: KYCIndex.
- `kyc_fields`: KYCFields.

Emits `SwordHolderRemoved` if successful.

\# &lt;weight&gt;
- TODO
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| sword_holder_index | `KYCIndex` | 
| kyc_fields | `KYCFields` | 

#### Python
```python
call = substrate.compose_call(
    'Kyc', 'kill_sword_holder', {
    'kyc_fields': (
        'Name',
        'Area',
        'CurvePubicKey',
        'Email',
    ),
    'sword_holder_index': 'u32',
}
)
```

---------
### remove_kyc
ForceOrigin delete a kyc of accounts and add blacklist

This requires Congress to operate

- `target`: The deleted user.
- `black`: The reason for joining blacklist

Emits `KYCRemove` if successful.

\# &lt;weight&gt;
- TODO
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `T::AccountId` | 
| black | `Black<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Kyc', 'remove_kyc', {
    'black': {
        'Cheat': None,
        'Fraud': 'u128',
        'Unknown': None,
    },
    'target': 'AccountId',
}
)
```

---------
### request_judgement
IAS reviews the KYC submitted by the user, and then draws a conclusion on the
information submitted by the user

some tips.

- `kyc_fields`: KYCFields.
- `ias_index`: KYCIndex.
- `message`: Message.

Emits `JudgementRequested` if successful.

\# &lt;weight&gt;
- TODO
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| kyc_fields | `KYCFields` | 
| ias_index | `KYCIndex` | 
| message | `Message` | 

#### Python
```python
call = substrate.compose_call(
    'Kyc', 'request_judgement', {
    'ias_index': 'u32',
    'kyc_fields': (
        'Name',
        'Area',
        'CurvePubicKey',
        'Email',
    ),
    'message': '[u8; 128]',
}
)
```

---------
### set_kyc
User setting KYC

If the user is added to the blacklist, cannot be set

- `info`: KYCInfo.

Emits `KYCSet` if successful.

\# &lt;weight&gt;
- TODO
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| info | `KYCInfo` | 

#### Python
```python
call = substrate.compose_call(
    'Kyc', 'set_kyc', {
    'info': {
        'area': (
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
        'curve_public_key': 'Bytes',
        'email': 'Bytes',
        'name': 'Bytes',
    },
}
)
```

---------
### sword_holder_provide_judgement
sword_holder make review  on the information provided by IAS

- `kyc_fields`: KYCFields.
- `kyc_index`: KYCIndex.
- `target`: T::AccountId.
- `auth`: Authentication.
- `id`: Data.

Emits `AuthenticationGiven` if successful.

\# &lt;weight&gt;
- TODO
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| kyc_fields | `KYCFields` | 
| kyc_index | `KYCIndex` | 
| target | `T::AccountId` | 
| auth | `Authentication` | 
| id | `Data` | 

#### Python
```python
call = substrate.compose_call(
    'Kyc', 'sword_holder_provide_judgement', {
    'auth': (
        'Pending',
        'Success',
        'Failure',
    ),
    'id': 'Bytes',
    'kyc_fields': (
        'Name',
        'Area',
        'CurvePubicKey',
        'Email',
    ),
    'kyc_index': 'u32',
    'target': 'AccountId',
}
)
```

---------
### sword_holder_set_fee
sword holder set fee

- `kyc_fields`: KYCFields.
- `KYCFields`: Balance.

Emits `SetFee` if successful.

\# &lt;weight&gt;
- TODO
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| kyc_fields | `KYCFields` | 
| fee | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Kyc', 'sword_holder_set_fee', {
    'fee': 'u128',
    'kyc_fields': (
        'Name',
        'Area',
        'CurvePubicKey',
        'Email',
    ),
}
)
```

---------
## Events

---------
### ApplyCertification
A ApplyCertification . \[kyc_index, kyc_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### AuthenticationGiven
A authentication was given by a registrar. \[target, kyc_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `KYCIndex` | ```u32```

---------
### GetIAS
Randomly get identity authentication service(IAS)
provider.\[kyc_index,curve_public_key\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `KYCIndex` | ```u32```
| None | `CurvePubicKey` | ```[u8; 32]```

---------
### GetSwordHolder
Randomly get a sword holder  provider. \[kyc_index, curve_public_key\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `KYCIndex` | ```u32```
| None | `CurvePubicKey` | ```[u8; 32]```

---------
### IASAdded
A identity authentication service(IAS)  provider was added.\[kyc_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `KYCIndex` | ```u32```

---------
### IASJudgementRequested
A judgement was asked from a registrar. \[who, kyc_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `KYCIndex` | ```u32```

---------
### IASKilled
IAS killed. \[who\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### IASRemoved
A identity authentication service(IAS)  provider was removed.\[kyc_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `KYCIndex` | ```u32```

---------
### JudgementGiven
A judgement was given by a registrar. \[target, kyc_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `KYCIndex` | ```u32```

---------
### JudgementRequested
A judgement was asked from a registrar. \[who, kyc_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `KYCIndex` | ```u32```

---------
### JudgementUnrequested
A judgement request was retracted. \[who, kyc_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `KYCIndex` | ```u32```

---------
### KYCCleared
A kyc was cleared, and the given balance returned. \[who, deposit\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### KYCRemove
remove kyc. \[who\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### KYCSet
A kyc was set or reset (which will remove all judgements). \[who\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### SetFee
SetFee
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T>` | ```u128```

---------
### SwordHolderAdded
A sword holder  provider was added. \[kyc_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `KYCIndex` | ```u32```

---------
### SwordHolderKilled
SwordHolder killed. \[who\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### SwordHolderRemoved
A sword holder  provider was added. \[kyc_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `KYCIndex` | ```u32```

---------
## Storage functions

---------
### ApplicationFormList
ApplicationFormList: AccountId -&gt; Vec&lt;ApplicationForm&gt;

#### Python
```python
result = substrate.query(
    'Kyc', 'ApplicationFormList', ['AccountId']
)
```

#### Return value
```python
[
    (
        None,
        {
            'ias': (
                'u32',
                {
                    'account': 'AccountId',
                    'curve_public_key': '[u8; 32]',
                    'fee': 'u128',
                    'fields': 'scale_info::246',
                },
            ),
            'progress': (
                'NeedReset',
                'Pending',
                'IasDoing',
                'IasDone',
                'SwordHolderDone',
                'Success',
                'Failure',
            ),
            'sword_holder': (
                'u32',
                {
                    'account': 'AccountId',
                    'curve_public_key': '[u8; 32]',
                    'fee': 'u128',
                    'fields': 'scale_info::246',
                },
            ),
        },
    ),
]
```
---------
### AreaData
 area data of user account

#### Python
```python
result = substrate.query(
    'Kyc', 'AreaData', [
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
]
)
```

#### Return value
```python
'u64'
```
---------
### BlackListOf
 the black list of kyc user

#### Python
```python
result = substrate.query(
    'Kyc', 'BlackListOf', ['AccountId']
)
```

#### Return value
```python
{'info': [{'Cheat': None, 'Fraud': 'u128', 'Unknown': None}]}
```
---------
### IASListOf
 List of identity authentication service(IAS) in a  kyc field

#### Python
```python
result = substrate.query(
    'Kyc', 'IASListOf', [
    (
        'Name',
        'Area',
        'CurvePubicKey',
        'Email',
    ),
]
)
```

#### Return value
```python
[
    (
        None,
        {
            'account': 'AccountId',
            'curve_public_key': '[u8; 32]',
            'fee': 'u128',
            'fields': ('Name', 'Area', 'CurvePubicKey', 'Email'),
        },
    ),
]
```
---------
### KYCOf
 kyc of account

#### Python
```python
result = substrate.query(
    'Kyc', 'KYCOf', ['AccountId']
)
```

#### Return value
```python
{
    'deposit': 'u128',
    'info': {
        'area': (
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
        'curve_public_key': 'Bytes',
        'email': 'Bytes',
        'name': 'Bytes',
    },
    'judgements': [
        (
            ('Name', 'Area', 'CurvePubicKey', 'Email'),
            'u32',
            {
                'Erroneous': None,
                'FeePaid': 'u128',
                'LowQuality': None,
                'OutOfDate': None,
                'PASS': None,
                'Repeat': None,
            },
            ('Pending', 'Success', 'Failure'),
        ),
    ],
}
```
---------
### MessageList
 message: (sender, recipient -&gt; data)

#### Python
```python
result = substrate.query(
    'Kyc', 'MessageList', ['AccountId', 'AccountId']
)
```

#### Return value
```python
['[u8; 128]']
```
---------
### Nonce
 Keeps track of the Nonce used in the randomness generator.

#### Python
```python
result = substrate.query(
    'Kyc', 'Nonce', []
)
```

#### Return value
```python
'u64'
```
---------
### RecordsOf
 Records Of IAS/SwordHolder

#### Python
```python
result = substrate.query(
    'Kyc', 'RecordsOf', ['AccountId']
)
```

#### Return value
```python
[
    {
        'account': 'AccountId',
        'fields': ('Name', 'Area', 'CurvePubicKey', 'Email'),
        'progress': (
            'NeedReset',
            'Pending',
            'IasDoing',
            'IasDone',
            'SwordHolderDone',
            'Success',
            'Failure',
        ),
    },
]
```
---------
### SwordHolderOf
 List of SwordHolder in a  kyc field

#### Python
```python
result = substrate.query(
    'Kyc', 'SwordHolderOf', [
    (
        'Name',
        'Area',
        'CurvePubicKey',
        'Email',
    ),
]
)
```

#### Return value
```python
[
    (
        None,
        {
            'account': 'AccountId',
            'curve_public_key': '[u8; 32]',
            'fee': 'u128',
            'fields': ('Name', 'Area', 'CurvePubicKey', 'Email'),
        },
    ),
]
```
---------
### UniqueIdOf
 Unique information storage filtering

#### Python
```python
result = substrate.query(
    'Kyc', 'UniqueIdOf', [
    (
        'Name',
        'Area',
        'CurvePubicKey',
        'Email',
    ),
]
)
```

#### Return value
```python
['Bytes']
```
---------
## Constants

---------
### BasicDeposit
 The amount held on deposit for a registered user.
#### Value
```python
10000000000000000
```
#### Python
```python
constant = substrate.get_constant('Kyc', 'BasicDeposit')
```
---------
### MaxIAS
 Maxmimum number of IAS
#### Value
```python
200
```
#### Python
```python
constant = substrate.get_constant('Kyc', 'MaxIAS')
```
---------
### MaxSwordHolder
 MaxSwordHolder:
#### Value
```python
200
```
#### Python
```python
constant = substrate.get_constant('Kyc', 'MaxSwordHolder')
```
---------
### PalletId
#### Value
```python
'0x6469636f2f6b7963'
```
#### Python
```python
constant = substrate.get_constant('Kyc', 'PalletId')
```
---------
### ServiceDeposit
 The amount held on deposit for a ias/sword holder
#### Value
```python
20000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Kyc', 'ServiceDeposit')
```
---------
## Errors

---------
### AccountExists
Account already exists

---------
### AuthenticationGiven
 SwordHolder Authentication given

---------
### Blacklisted
has been blacklisted

---------
### CountOverflow
Count Overflow

---------
### EmptyIndex
Sticky judgement.

---------
### FeeChanged
Fee is changed.

---------
### FeeNonNegative
Fee Non Negative

---------
### FeeNotEnough
Fee is not enough.

---------
### InProgress
InProgress

---------
### InsufficientPermissions
Insufficient permissions

---------
### InvalidFee
Invalid fee

---------
### InvalidIndex
The index is invalid.

---------
### InvalidJudgement
Invalid judgement.

---------
### InvalidKYCField
The kyc field is invalid.

---------
### InvalidTarget
The target is invalid.

---------
### JudgementGiven
IAS Judgement given.

---------
### KYCFieldFound
The kyc field is contained in list.

---------
### KYCFound
The kyc of account is contained in list.

---------
### NoApplication
No application

---------
### NoIAS
NO IAS

---------
### NoKYC
No KYC found.

---------
### NonceOverflow
Nonce has overflowed past u64 limits

---------
### NotContainsUniqueID
not contains Unique identification code

---------
### NotFound
Account isn&\#x27;t found.

---------
### NotUniqueID
not Unique identification code

---------
### OutofBounds
out of bounds

---------
### PendingAuthentication
The authentication&\#x27;s is pending.

---------
### RepeatApplication
Repeat application

---------
### StickyJudgement
Sticky judgement.

---------
### ThisFeeNotFoundIASOrSwordHolder
this fee not found ias or sword holder

---------
### TooManyAccount
Maximum amount of IAS/SwordHolder reached. Cannot add any more.

---------