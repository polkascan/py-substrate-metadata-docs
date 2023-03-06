
# ComplianceManager

---------
## Calls

---------
### add_compliance_requirement
Adds a compliance requirement to an asset&\#x27;s compliance by ticker.
If the compliance requirement is a duplicate, it does nothing.

\# Arguments
* origin - Signer of the dispatchable. It should be the owner of the ticker
* ticker - Symbol of the asset
* sender_conditions - Sender transfer conditions.
* receiver_conditions - Receiver transfer conditions.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| sender_conditions | `Vec<Condition>` | 
| receiver_conditions | `Vec<Condition>` | 

#### Python
```python
call = substrate.compose_call(
    'ComplianceManager', 'add_compliance_requirement', {
    'receiver_conditions': [
        {
            'condition_type': {
                'IsAbsent': {
                    'Accredited': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'Affiliate': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'Blocked': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'BuyLockup': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'Custom': (
                        'u32',
                        (
                            None,
                            'scale_info::62',
                        ),
                    ),
                    'CustomerDueDiligence': '[u8; 32]',
                    'Exempted': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'InvestorUniqueness': (
                        {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        '[u8; 32]',
                        '[u8; 32]',
                    ),
                    'InvestorUniquenessV2': '[u8; 32]',
                    'Jurisdiction': (
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
                            'BA',
                            'BW',
                            'BV',
                            'BR',
                            'VG',
                            'IO',
                            'BN',
                            'BG',
                            'BF',
                            'BI',
                            'KH',
                            'CM',
                            'CA',
                            'CV',
                            'KY',
                            'CF',
                            'TD',
                            'CL',
                            'CN',
                            'HK',
                            'MO',
                            'CX',
                            'CC',
                            'CO',
                            'KM',
                            'CG',
                            'CD',
                            'CK',
                            'CR',
                            'CI',
                            'HR',
                            'CU',
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
                            'AN',
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
                            'SZ',
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
                            'US',
                            'UM',
                            'UY',
                            'UZ',
                            'VU',
                            'VE',
                            'VN',
                            'VI',
                            'WF',
                            'EH',
                            'YE',
                            'ZM',
                            'ZW',
                            'BQ',
                            'CW',
                            'SX',
                        ),
                        {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                    ),
                    'KnowYourCustomer': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'NoData': None,
                    'SellLockup': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                },
                'IsAnyOf': [
                    {
                        'Accredited': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Affiliate': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Blocked': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'BuyLockup': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Custom': (
                            'u32',
                            (
                                None,
                                'scale_info::62',
                            ),
                        ),
                        'CustomerDueDiligence': '[u8; 32]',
                        'Exempted': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'InvestorUniqueness': (
                            'scale_info::62',
                            '[u8; 32]',
                            '[u8; 32]',
                        ),
                        'InvestorUniquenessV2': '[u8; 32]',
                        'Jurisdiction': (
                            'scale_info::64',
                            'scale_info::62',
                        ),
                        'KnowYourCustomer': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'NoData': None,
                        'SellLockup': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                    },
                ],
                'IsIdentity': {
                    'ExternalAgent': None,
                    'Specific': '[u8; 32]',
                },
                'IsNoneOf': [
                    {
                        'Accredited': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Affiliate': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Blocked': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'BuyLockup': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Custom': (
                            'u32',
                            (
                                None,
                                'scale_info::62',
                            ),
                        ),
                        'CustomerDueDiligence': '[u8; 32]',
                        'Exempted': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'InvestorUniqueness': (
                            'scale_info::62',
                            '[u8; 32]',
                            '[u8; 32]',
                        ),
                        'InvestorUniquenessV2': '[u8; 32]',
                        'Jurisdiction': (
                            'scale_info::64',
                            'scale_info::62',
                        ),
                        'KnowYourCustomer': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'NoData': None,
                        'SellLockup': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                    },
                ],
                'IsPresent': {
                    'Accredited': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'Affiliate': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'Blocked': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'BuyLockup': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'Custom': (
                        'u32',
                        (
                            None,
                            'scale_info::62',
                        ),
                    ),
                    'CustomerDueDiligence': '[u8; 32]',
                    'Exempted': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'InvestorUniqueness': (
                        {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        '[u8; 32]',
                        '[u8; 32]',
                    ),
                    'InvestorUniquenessV2': '[u8; 32]',
                    'Jurisdiction': (
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
                            'BA',
                            'BW',
                            'BV',
                            'BR',
                            'VG',
                            'IO',
                            'BN',
                            'BG',
                            'BF',
                            'BI',
                            'KH',
                            'CM',
                            'CA',
                            'CV',
                            'KY',
                            'CF',
                            'TD',
                            'CL',
                            'CN',
                            'HK',
                            'MO',
                            'CX',
                            'CC',
                            'CO',
                            'KM',
                            'CG',
                            'CD',
                            'CK',
                            'CR',
                            'CI',
                            'HR',
                            'CU',
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
                            'AN',
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
                            'SZ',
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
                            'US',
                            'UM',
                            'UY',
                            'UZ',
                            'VU',
                            'VE',
                            'VN',
                            'VI',
                            'WF',
                            'EH',
                            'YE',
                            'ZM',
                            'ZW',
                            'BQ',
                            'CW',
                            'SX',
                        ),
                        {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                    ),
                    'KnowYourCustomer': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'NoData': None,
                    'SellLockup': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                },
            },
            'issuers': [
                {
                    'issuer': '[u8; 32]',
                    'trusted_for': {
                        'Any': None,
                        'Specific': [
                            'scale_info::181',
                        ],
                    },
                },
            ],
        },
    ],
    'sender_conditions': [
        {
            'condition_type': {
                'IsAbsent': {
                    'Accredited': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'Affiliate': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'Blocked': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'BuyLockup': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'Custom': (
                        'u32',
                        (
                            None,
                            'scale_info::62',
                        ),
                    ),
                    'CustomerDueDiligence': '[u8; 32]',
                    'Exempted': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'InvestorUniqueness': (
                        {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        '[u8; 32]',
                        '[u8; 32]',
                    ),
                    'InvestorUniquenessV2': '[u8; 32]',
                    'Jurisdiction': (
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
                            'BA',
                            'BW',
                            'BV',
                            'BR',
                            'VG',
                            'IO',
                            'BN',
                            'BG',
                            'BF',
                            'BI',
                            'KH',
                            'CM',
                            'CA',
                            'CV',
                            'KY',
                            'CF',
                            'TD',
                            'CL',
                            'CN',
                            'HK',
                            'MO',
                            'CX',
                            'CC',
                            'CO',
                            'KM',
                            'CG',
                            'CD',
                            'CK',
                            'CR',
                            'CI',
                            'HR',
                            'CU',
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
                            'AN',
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
                            'SZ',
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
                            'US',
                            'UM',
                            'UY',
                            'UZ',
                            'VU',
                            'VE',
                            'VN',
                            'VI',
                            'WF',
                            'EH',
                            'YE',
                            'ZM',
                            'ZW',
                            'BQ',
                            'CW',
                            'SX',
                        ),
                        {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                    ),
                    'KnowYourCustomer': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'NoData': None,
                    'SellLockup': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                },
                'IsAnyOf': [
                    {
                        'Accredited': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Affiliate': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Blocked': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'BuyLockup': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Custom': (
                            'u32',
                            (
                                None,
                                'scale_info::62',
                            ),
                        ),
                        'CustomerDueDiligence': '[u8; 32]',
                        'Exempted': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'InvestorUniqueness': (
                            'scale_info::62',
                            '[u8; 32]',
                            '[u8; 32]',
                        ),
                        'InvestorUniquenessV2': '[u8; 32]',
                        'Jurisdiction': (
                            'scale_info::64',
                            'scale_info::62',
                        ),
                        'KnowYourCustomer': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'NoData': None,
                        'SellLockup': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                    },
                ],
                'IsIdentity': {
                    'ExternalAgent': None,
                    'Specific': '[u8; 32]',
                },
                'IsNoneOf': [
                    {
                        'Accredited': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Affiliate': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Blocked': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'BuyLockup': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Custom': (
                            'u32',
                            (
                                None,
                                'scale_info::62',
                            ),
                        ),
                        'CustomerDueDiligence': '[u8; 32]',
                        'Exempted': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'InvestorUniqueness': (
                            'scale_info::62',
                            '[u8; 32]',
                            '[u8; 32]',
                        ),
                        'InvestorUniquenessV2': '[u8; 32]',
                        'Jurisdiction': (
                            'scale_info::64',
                            'scale_info::62',
                        ),
                        'KnowYourCustomer': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'NoData': None,
                        'SellLockup': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                    },
                ],
                'IsPresent': {
                    'Accredited': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'Affiliate': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'Blocked': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'BuyLockup': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'Custom': (
                        'u32',
                        (
                            None,
                            'scale_info::62',
                        ),
                    ),
                    'CustomerDueDiligence': '[u8; 32]',
                    'Exempted': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'InvestorUniqueness': (
                        {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        '[u8; 32]',
                        '[u8; 32]',
                    ),
                    'InvestorUniquenessV2': '[u8; 32]',
                    'Jurisdiction': (
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
                            'BA',
                            'BW',
                            'BV',
                            'BR',
                            'VG',
                            'IO',
                            'BN',
                            'BG',
                            'BF',
                            'BI',
                            'KH',
                            'CM',
                            'CA',
                            'CV',
                            'KY',
                            'CF',
                            'TD',
                            'CL',
                            'CN',
                            'HK',
                            'MO',
                            'CX',
                            'CC',
                            'CO',
                            'KM',
                            'CG',
                            'CD',
                            'CK',
                            'CR',
                            'CI',
                            'HR',
                            'CU',
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
                            'AN',
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
                            'SZ',
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
                            'US',
                            'UM',
                            'UY',
                            'UZ',
                            'VU',
                            'VE',
                            'VN',
                            'VI',
                            'WF',
                            'EH',
                            'YE',
                            'ZM',
                            'ZW',
                            'BQ',
                            'CW',
                            'SX',
                        ),
                        {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                    ),
                    'KnowYourCustomer': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                    'NoData': None,
                    'SellLockup': {
                        'Custom': 'Bytes',
                        'Identity': '[u8; 32]',
                        'Ticker': '[u8; 12]',
                    },
                },
            },
            'issuers': [
                {
                    'issuer': '[u8; 32]',
                    'trusted_for': {
                        'Any': None,
                        'Specific': [
                            'scale_info::181',
                        ],
                    },
                },
            ],
        },
    ],
    'ticker': '[u8; 12]',
}
)
```

---------
### add_default_trusted_claim_issuer
Adds another default trusted claim issuer at the ticker level.

\# Arguments
* origin - Signer of the dispatchable. It should be the owner of the ticker.
* ticker - Symbol of the asset.
* issuer - IdentityId of the trusted claim issuer.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| issuer | `TrustedIssuer` | 

#### Python
```python
call = substrate.compose_call(
    'ComplianceManager', 'add_default_trusted_claim_issuer', {
    'issuer': {
        'issuer': '[u8; 32]',
        'trusted_for': {
            'Any': None,
            'Specific': [
                {
                    'Accredited': None,
                    'Affiliate': None,
                    'Blocked': None,
                    'BuyLockup': None,
                    'Custom': 'u32',
                    'CustomerDueDiligence': None,
                    'Exempted': None,
                    'InvestorUniqueness': None,
                    'InvestorUniquenessV2': None,
                    'Jurisdiction': None,
                    'KnowYourCustomer': None,
                    'NoType': None,
                    'SellLockup': None,
                },
            ],
        },
    },
    'ticker': '[u8; 12]',
}
)
```

---------
### change_compliance_requirement
Modify an existing compliance requirement of a given ticker.

\# Arguments
* origin - Signer of the dispatchable. It should be the owner of the ticker.
* ticker - Symbol of the asset.
* new_req - Compliance requirement.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| new_req | `ComplianceRequirement` | 

#### Python
```python
call = substrate.compose_call(
    'ComplianceManager', 'change_compliance_requirement', {
    'new_req': {
        'id': 'u32',
        'receiver_conditions': [
            {
                'condition_type': {
                    'IsAbsent': {
                        'Accredited': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Affiliate': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Blocked': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'BuyLockup': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Custom': (
                            'u32',
                            (
                                None,
                                'scale_info::62',
                            ),
                        ),
                        'CustomerDueDiligence': '[u8; 32]',
                        'Exempted': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'InvestorUniqueness': (
                            'scale_info::62',
                            '[u8; 32]',
                            '[u8; 32]',
                        ),
                        'InvestorUniquenessV2': '[u8; 32]',
                        'Jurisdiction': (
                            'scale_info::64',
                            'scale_info::62',
                        ),
                        'KnowYourCustomer': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'NoData': None,
                        'SellLockup': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                    },
                    'IsAnyOf': [
                        {
                            'Accredited': 'scale_info::62',
                            'Affiliate': 'scale_info::62',
                            'Blocked': 'scale_info::62',
                            'BuyLockup': 'scale_info::62',
                            'Custom': (
                                'u32',
                                (
                                    None,
                                    'scale_info::62',
                                ),
                            ),
                            'CustomerDueDiligence': '[u8; 32]',
                            'Exempted': 'scale_info::62',
                            'InvestorUniqueness': (
                                'scale_info::62',
                                '[u8; 32]',
                                '[u8; 32]',
                            ),
                            'InvestorUniquenessV2': '[u8; 32]',
                            'Jurisdiction': (
                                'scale_info::64',
                                'scale_info::62',
                            ),
                            'KnowYourCustomer': 'scale_info::62',
                            'NoData': None,
                            'SellLockup': 'scale_info::62',
                        },
                    ],
                    'IsIdentity': {
                        'ExternalAgent': None,
                        'Specific': '[u8; 32]',
                    },
                    'IsNoneOf': [
                        {
                            'Accredited': 'scale_info::62',
                            'Affiliate': 'scale_info::62',
                            'Blocked': 'scale_info::62',
                            'BuyLockup': 'scale_info::62',
                            'Custom': (
                                'u32',
                                (
                                    None,
                                    'scale_info::62',
                                ),
                            ),
                            'CustomerDueDiligence': '[u8; 32]',
                            'Exempted': 'scale_info::62',
                            'InvestorUniqueness': (
                                'scale_info::62',
                                '[u8; 32]',
                                '[u8; 32]',
                            ),
                            'InvestorUniquenessV2': '[u8; 32]',
                            'Jurisdiction': (
                                'scale_info::64',
                                'scale_info::62',
                            ),
                            'KnowYourCustomer': 'scale_info::62',
                            'NoData': None,
                            'SellLockup': 'scale_info::62',
                        },
                    ],
                    'IsPresent': {
                        'Accredited': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Affiliate': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Blocked': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'BuyLockup': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Custom': (
                            'u32',
                            (
                                None,
                                'scale_info::62',
                            ),
                        ),
                        'CustomerDueDiligence': '[u8; 32]',
                        'Exempted': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'InvestorUniqueness': (
                            'scale_info::62',
                            '[u8; 32]',
                            '[u8; 32]',
                        ),
                        'InvestorUniquenessV2': '[u8; 32]',
                        'Jurisdiction': (
                            'scale_info::64',
                            'scale_info::62',
                        ),
                        'KnowYourCustomer': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'NoData': None,
                        'SellLockup': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                    },
                },
                'issuers': [
                    {
                        'issuer': '[u8; 32]',
                        'trusted_for': {
                            'Any': None,
                            'Specific': [
                                'scale_info::181',
                            ],
                        },
                    },
                ],
            },
        ],
        'sender_conditions': [
            {
                'condition_type': {
                    'IsAbsent': {
                        'Accredited': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Affiliate': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Blocked': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'BuyLockup': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Custom': (
                            'u32',
                            (
                                None,
                                'scale_info::62',
                            ),
                        ),
                        'CustomerDueDiligence': '[u8; 32]',
                        'Exempted': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'InvestorUniqueness': (
                            'scale_info::62',
                            '[u8; 32]',
                            '[u8; 32]',
                        ),
                        'InvestorUniquenessV2': '[u8; 32]',
                        'Jurisdiction': (
                            'scale_info::64',
                            'scale_info::62',
                        ),
                        'KnowYourCustomer': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'NoData': None,
                        'SellLockup': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                    },
                    'IsAnyOf': [
                        {
                            'Accredited': 'scale_info::62',
                            'Affiliate': 'scale_info::62',
                            'Blocked': 'scale_info::62',
                            'BuyLockup': 'scale_info::62',
                            'Custom': (
                                'u32',
                                (
                                    None,
                                    'scale_info::62',
                                ),
                            ),
                            'CustomerDueDiligence': '[u8; 32]',
                            'Exempted': 'scale_info::62',
                            'InvestorUniqueness': (
                                'scale_info::62',
                                '[u8; 32]',
                                '[u8; 32]',
                            ),
                            'InvestorUniquenessV2': '[u8; 32]',
                            'Jurisdiction': (
                                'scale_info::64',
                                'scale_info::62',
                            ),
                            'KnowYourCustomer': 'scale_info::62',
                            'NoData': None,
                            'SellLockup': 'scale_info::62',
                        },
                    ],
                    'IsIdentity': {
                        'ExternalAgent': None,
                        'Specific': '[u8; 32]',
                    },
                    'IsNoneOf': [
                        {
                            'Accredited': 'scale_info::62',
                            'Affiliate': 'scale_info::62',
                            'Blocked': 'scale_info::62',
                            'BuyLockup': 'scale_info::62',
                            'Custom': (
                                'u32',
                                (
                                    None,
                                    'scale_info::62',
                                ),
                            ),
                            'CustomerDueDiligence': '[u8; 32]',
                            'Exempted': 'scale_info::62',
                            'InvestorUniqueness': (
                                'scale_info::62',
                                '[u8; 32]',
                                '[u8; 32]',
                            ),
                            'InvestorUniquenessV2': '[u8; 32]',
                            'Jurisdiction': (
                                'scale_info::64',
                                'scale_info::62',
                            ),
                            'KnowYourCustomer': 'scale_info::62',
                            'NoData': None,
                            'SellLockup': 'scale_info::62',
                        },
                    ],
                    'IsPresent': {
                        'Accredited': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Affiliate': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Blocked': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'BuyLockup': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'Custom': (
                            'u32',
                            (
                                None,
                                'scale_info::62',
                            ),
                        ),
                        'CustomerDueDiligence': '[u8; 32]',
                        'Exempted': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'InvestorUniqueness': (
                            'scale_info::62',
                            '[u8; 32]',
                            '[u8; 32]',
                        ),
                        'InvestorUniquenessV2': '[u8; 32]',
                        'Jurisdiction': (
                            'scale_info::64',
                            'scale_info::62',
                        ),
                        'KnowYourCustomer': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                        'NoData': None,
                        'SellLockup': {
                            'Custom': 'Bytes',
                            'Identity': '[u8; 32]',
                            'Ticker': '[u8; 12]',
                        },
                    },
                },
                'issuers': [
                    {
                        'issuer': '[u8; 32]',
                        'trusted_for': {
                            'Any': None,
                            'Specific': [
                                'scale_info::181',
                            ],
                        },
                    },
                ],
            },
        ],
    },
    'ticker': '[u8; 12]',
}
)
```

---------
### pause_asset_compliance
Pauses the verification of conditions for `ticker` during transfers.

\# Arguments
* origin - Signer of the dispatchable. It should be the owner of the ticker
* ticker - Symbol of the asset

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 

#### Python
```python
call = substrate.compose_call(
    'ComplianceManager', 'pause_asset_compliance', {'ticker': '[u8; 12]'}
)
```

---------
### remove_compliance_requirement
Removes a compliance requirement from an asset&\#x27;s compliance.

\# Arguments
* origin - Signer of the dispatchable. It should be the owner of the ticker
* ticker - Symbol of the asset
* id - Compliance requirement id which is need to be removed

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| id | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ComplianceManager', 'remove_compliance_requirement', {'id': 'u32', 'ticker': '[u8; 12]'}
)
```

---------
### remove_default_trusted_claim_issuer
Removes the given `issuer` from the set of default trusted claim issuers at the ticker level.

\# Arguments
* origin - Signer of the dispatchable. It should be the owner of the ticker.
* ticker - Symbol of the asset.
* issuer - IdentityId of the trusted claim issuer.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| issuer | `IdentityId` | 

#### Python
```python
call = substrate.compose_call(
    'ComplianceManager', 'remove_default_trusted_claim_issuer', {
    'issuer': '[u8; 32]',
    'ticker': '[u8; 12]',
}
)
```

---------
### replace_asset_compliance
Replaces an asset&\#x27;s compliance by ticker with a new compliance.

Compliance requirements will be sorted (ascending by id) before
replacing the current requirements.

\# Arguments
* `ticker` - the asset ticker,
* `asset_compliance - the new asset compliance.

\# Errors
* `Unauthorized` if `origin` is not the owner of the ticker.
* `DuplicateAssetCompliance` if `asset_compliance` contains multiple entries with the same `requirement_id`.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| asset_compliance | `Vec<ComplianceRequirement>` | 

#### Python
```python
call = substrate.compose_call(
    'ComplianceManager', 'replace_asset_compliance', {
    'asset_compliance': [
        {
            'id': 'u32',
            'receiver_conditions': [
                {
                    'condition_type': {
                        'IsAbsent': {
                            'Accredited': 'scale_info::62',
                            'Affiliate': 'scale_info::62',
                            'Blocked': 'scale_info::62',
                            'BuyLockup': 'scale_info::62',
                            'Custom': (
                                'u32',
                                (
                                    None,
                                    'scale_info::62',
                                ),
                            ),
                            'CustomerDueDiligence': '[u8; 32]',
                            'Exempted': 'scale_info::62',
                            'InvestorUniqueness': (
                                'scale_info::62',
                                '[u8; 32]',
                                '[u8; 32]',
                            ),
                            'InvestorUniquenessV2': '[u8; 32]',
                            'Jurisdiction': (
                                'scale_info::64',
                                'scale_info::62',
                            ),
                            'KnowYourCustomer': 'scale_info::62',
                            'NoData': None,
                            'SellLockup': 'scale_info::62',
                        },
                        'IsAnyOf': [
                            'scale_info::61',
                        ],
                        'IsIdentity': {
                            'ExternalAgent': None,
                            'Specific': '[u8; 32]',
                        },
                        'IsNoneOf': [
                            'scale_info::61',
                        ],
                        'IsPresent': {
                            'Accredited': 'scale_info::62',
                            'Affiliate': 'scale_info::62',
                            'Blocked': 'scale_info::62',
                            'BuyLockup': 'scale_info::62',
                            'Custom': (
                                'u32',
                                (
                                    None,
                                    'scale_info::62',
                                ),
                            ),
                            'CustomerDueDiligence': '[u8; 32]',
                            'Exempted': 'scale_info::62',
                            'InvestorUniqueness': (
                                'scale_info::62',
                                '[u8; 32]',
                                '[u8; 32]',
                            ),
                            'InvestorUniquenessV2': '[u8; 32]',
                            'Jurisdiction': (
                                'scale_info::64',
                                'scale_info::62',
                            ),
                            'KnowYourCustomer': 'scale_info::62',
                            'NoData': None,
                            'SellLockup': 'scale_info::62',
                        },
                    },
                    'issuers': [
                        {
                            'issuer': '[u8; 32]',
                            'trusted_for': 'scale_info::179',
                        },
                    ],
                },
            ],
            'sender_conditions': [
                {
                    'condition_type': {
                        'IsAbsent': {
                            'Accredited': 'scale_info::62',
                            'Affiliate': 'scale_info::62',
                            'Blocked': 'scale_info::62',
                            'BuyLockup': 'scale_info::62',
                            'Custom': (
                                'u32',
                                (
                                    None,
                                    'scale_info::62',
                                ),
                            ),
                            'CustomerDueDiligence': '[u8; 32]',
                            'Exempted': 'scale_info::62',
                            'InvestorUniqueness': (
                                'scale_info::62',
                                '[u8; 32]',
                                '[u8; 32]',
                            ),
                            'InvestorUniquenessV2': '[u8; 32]',
                            'Jurisdiction': (
                                'scale_info::64',
                                'scale_info::62',
                            ),
                            'KnowYourCustomer': 'scale_info::62',
                            'NoData': None,
                            'SellLockup': 'scale_info::62',
                        },
                        'IsAnyOf': [
                            'scale_info::61',
                        ],
                        'IsIdentity': {
                            'ExternalAgent': None,
                            'Specific': '[u8; 32]',
                        },
                        'IsNoneOf': [
                            'scale_info::61',
                        ],
                        'IsPresent': {
                            'Accredited': 'scale_info::62',
                            'Affiliate': 'scale_info::62',
                            'Blocked': 'scale_info::62',
                            'BuyLockup': 'scale_info::62',
                            'Custom': (
                                'u32',
                                (
                                    None,
                                    'scale_info::62',
                                ),
                            ),
                            'CustomerDueDiligence': '[u8; 32]',
                            'Exempted': 'scale_info::62',
                            'InvestorUniqueness': (
                                'scale_info::62',
                                '[u8; 32]',
                                '[u8; 32]',
                            ),
                            'InvestorUniquenessV2': '[u8; 32]',
                            'Jurisdiction': (
                                'scale_info::64',
                                'scale_info::62',
                            ),
                            'KnowYourCustomer': 'scale_info::62',
                            'NoData': None,
                            'SellLockup': 'scale_info::62',
                        },
                    },
                    'issuers': [
                        {
                            'issuer': '[u8; 32]',
                            'trusted_for': 'scale_info::179',
                        },
                    ],
                },
            ],
        },
    ],
    'ticker': '[u8; 12]',
}
)
```

---------
### reset_asset_compliance
Removes an asset&\#x27;s compliance

\# Arguments
* origin - Signer of the dispatchable. It should be the owner of the ticker
* ticker - Symbol of the asset

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 

#### Python
```python
call = substrate.compose_call(
    'ComplianceManager', 'reset_asset_compliance', {'ticker': '[u8; 12]'}
)
```

---------
### resume_asset_compliance
Resumes the verification of conditions for `ticker` during transfers.

\# Arguments
* origin - Signer of the dispatchable. It should be the owner of the ticker
* ticker - Symbol of the asset

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 

#### Python
```python
call = substrate.compose_call(
    'ComplianceManager', 'resume_asset_compliance', {'ticker': '[u8; 12]'}
)
```

---------
## Events

---------
### AssetCompliancePaused
Emitted when an asset compliance for a given ticker gets paused.
(caller DID, Ticker).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```

---------
### AssetComplianceReplaced
Emitted when an asset compliance is replaced.
Parameters: caller DID, ticker, new asset compliance.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `Vec<ComplianceRequirement>` | ```[{'sender_conditions': [{'condition_type': {'IsPresent': 'scale_info::61', 'IsAbsent': 'scale_info::61', 'IsAnyOf': ['scale_info::61'], 'IsNoneOf': ['scale_info::61'], 'IsIdentity': 'scale_info::176'}, 'issuers': ['scale_info::178']}], 'receiver_conditions': [{'condition_type': {'IsPresent': 'scale_info::61', 'IsAbsent': 'scale_info::61', 'IsAnyOf': ['scale_info::61'], 'IsNoneOf': ['scale_info::61'], 'IsIdentity': 'scale_info::176'}, 'issuers': ['scale_info::178']}], 'id': 'u32'}]```

---------
### AssetComplianceReset
Emitted when an asset compliance of a ticker is reset.
(caller DID, Ticker).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```

---------
### AssetComplianceResumed
Emitted when an asset compliance for a given ticker gets resume.
(caller DID, Ticker).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```

---------
### ComplianceRequirementChanged
Emitted when compliance requirement get modified/change.
(caller DID, Ticker, ComplianceRequirement).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `ComplianceRequirement` | ```{'sender_conditions': [{'condition_type': {'IsPresent': {'Accredited': 'scale_info::62', 'Affiliate': 'scale_info::62', 'BuyLockup': 'scale_info::62', 'SellLockup': 'scale_info::62', 'CustomerDueDiligence': '[u8; 32]', 'KnowYourCustomer': 'scale_info::62', 'Jurisdiction': ('scale_info::64', 'scale_info::62'), 'Exempted': 'scale_info::62', 'Blocked': 'scale_info::62', 'InvestorUniqueness': ('scale_info::62', '[u8; 32]', '[u8; 32]'), 'NoData': None, 'InvestorUniquenessV2': '[u8; 32]', 'Custom': ('u32', (None, 'scale_info::62'))}, 'IsAbsent': {'Accredited': 'scale_info::62', 'Affiliate': 'scale_info::62', 'BuyLockup': 'scale_info::62', 'SellLockup': 'scale_info::62', 'CustomerDueDiligence': '[u8; 32]', 'KnowYourCustomer': 'scale_info::62', 'Jurisdiction': ('scale_info::64', 'scale_info::62'), 'Exempted': 'scale_info::62', 'Blocked': 'scale_info::62', 'InvestorUniqueness': ('scale_info::62', '[u8; 32]', '[u8; 32]'), 'NoData': None, 'InvestorUniquenessV2': '[u8; 32]', 'Custom': ('u32', (None, 'scale_info::62'))}, 'IsAnyOf': ['scale_info::61'], 'IsNoneOf': ['scale_info::61'], 'IsIdentity': {'ExternalAgent': None, 'Specific': '[u8; 32]'}}, 'issuers': [{'issuer': '[u8; 32]', 'trusted_for': 'scale_info::179'}]}], 'receiver_conditions': [{'condition_type': {'IsPresent': {'Accredited': 'scale_info::62', 'Affiliate': 'scale_info::62', 'BuyLockup': 'scale_info::62', 'SellLockup': 'scale_info::62', 'CustomerDueDiligence': '[u8; 32]', 'KnowYourCustomer': 'scale_info::62', 'Jurisdiction': ('scale_info::64', 'scale_info::62'), 'Exempted': 'scale_info::62', 'Blocked': 'scale_info::62', 'InvestorUniqueness': ('scale_info::62', '[u8; 32]', '[u8; 32]'), 'NoData': None, 'InvestorUniquenessV2': '[u8; 32]', 'Custom': ('u32', (None, 'scale_info::62'))}, 'IsAbsent': {'Accredited': 'scale_info::62', 'Affiliate': 'scale_info::62', 'BuyLockup': 'scale_info::62', 'SellLockup': 'scale_info::62', 'CustomerDueDiligence': '[u8; 32]', 'KnowYourCustomer': 'scale_info::62', 'Jurisdiction': ('scale_info::64', 'scale_info::62'), 'Exempted': 'scale_info::62', 'Blocked': 'scale_info::62', 'InvestorUniqueness': ('scale_info::62', '[u8; 32]', '[u8; 32]'), 'NoData': None, 'InvestorUniquenessV2': '[u8; 32]', 'Custom': ('u32', (None, 'scale_info::62'))}, 'IsAnyOf': ['scale_info::61'], 'IsNoneOf': ['scale_info::61'], 'IsIdentity': {'ExternalAgent': None, 'Specific': '[u8; 32]'}}, 'issuers': [{'issuer': '[u8; 32]', 'trusted_for': 'scale_info::179'}]}], 'id': 'u32'}```

---------
### ComplianceRequirementCreated
Emitted when new compliance requirement is created.
(caller DID, Ticker, ComplianceRequirement).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `ComplianceRequirement` | ```{'sender_conditions': [{'condition_type': {'IsPresent': {'Accredited': 'scale_info::62', 'Affiliate': 'scale_info::62', 'BuyLockup': 'scale_info::62', 'SellLockup': 'scale_info::62', 'CustomerDueDiligence': '[u8; 32]', 'KnowYourCustomer': 'scale_info::62', 'Jurisdiction': ('scale_info::64', 'scale_info::62'), 'Exempted': 'scale_info::62', 'Blocked': 'scale_info::62', 'InvestorUniqueness': ('scale_info::62', '[u8; 32]', '[u8; 32]'), 'NoData': None, 'InvestorUniquenessV2': '[u8; 32]', 'Custom': ('u32', (None, 'scale_info::62'))}, 'IsAbsent': {'Accredited': 'scale_info::62', 'Affiliate': 'scale_info::62', 'BuyLockup': 'scale_info::62', 'SellLockup': 'scale_info::62', 'CustomerDueDiligence': '[u8; 32]', 'KnowYourCustomer': 'scale_info::62', 'Jurisdiction': ('scale_info::64', 'scale_info::62'), 'Exempted': 'scale_info::62', 'Blocked': 'scale_info::62', 'InvestorUniqueness': ('scale_info::62', '[u8; 32]', '[u8; 32]'), 'NoData': None, 'InvestorUniquenessV2': '[u8; 32]', 'Custom': ('u32', (None, 'scale_info::62'))}, 'IsAnyOf': ['scale_info::61'], 'IsNoneOf': ['scale_info::61'], 'IsIdentity': {'ExternalAgent': None, 'Specific': '[u8; 32]'}}, 'issuers': [{'issuer': '[u8; 32]', 'trusted_for': 'scale_info::179'}]}], 'receiver_conditions': [{'condition_type': {'IsPresent': {'Accredited': 'scale_info::62', 'Affiliate': 'scale_info::62', 'BuyLockup': 'scale_info::62', 'SellLockup': 'scale_info::62', 'CustomerDueDiligence': '[u8; 32]', 'KnowYourCustomer': 'scale_info::62', 'Jurisdiction': ('scale_info::64', 'scale_info::62'), 'Exempted': 'scale_info::62', 'Blocked': 'scale_info::62', 'InvestorUniqueness': ('scale_info::62', '[u8; 32]', '[u8; 32]'), 'NoData': None, 'InvestorUniquenessV2': '[u8; 32]', 'Custom': ('u32', (None, 'scale_info::62'))}, 'IsAbsent': {'Accredited': 'scale_info::62', 'Affiliate': 'scale_info::62', 'BuyLockup': 'scale_info::62', 'SellLockup': 'scale_info::62', 'CustomerDueDiligence': '[u8; 32]', 'KnowYourCustomer': 'scale_info::62', 'Jurisdiction': ('scale_info::64', 'scale_info::62'), 'Exempted': 'scale_info::62', 'Blocked': 'scale_info::62', 'InvestorUniqueness': ('scale_info::62', '[u8; 32]', '[u8; 32]'), 'NoData': None, 'InvestorUniquenessV2': '[u8; 32]', 'Custom': ('u32', (None, 'scale_info::62'))}, 'IsAnyOf': ['scale_info::61'], 'IsNoneOf': ['scale_info::61'], 'IsIdentity': {'ExternalAgent': None, 'Specific': '[u8; 32]'}}, 'issuers': [{'issuer': '[u8; 32]', 'trusted_for': 'scale_info::179'}]}], 'id': 'u32'}```

---------
### ComplianceRequirementRemoved
Emitted when a compliance requirement is removed.
(caller DID, Ticker, requirement_id).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `u32` | ```u32```

---------
### TrustedDefaultClaimIssuerAdded
Emitted when default claim issuer list for a given ticker gets added.
(caller DID, Ticker, Added TrustedIssuer).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `TrustedIssuer` | ```{'issuer': '[u8; 32]', 'trusted_for': {'Any': None, 'Specific': [{'Accredited': None, 'Affiliate': None, 'BuyLockup': None, 'SellLockup': None, 'CustomerDueDiligence': None, 'KnowYourCustomer': None, 'Jurisdiction': None, 'Exempted': None, 'Blocked': None, 'InvestorUniqueness': None, 'NoType': None, 'InvestorUniquenessV2': None, 'Custom': 'u32'}]}}```

---------
### TrustedDefaultClaimIssuerRemoved
Emitted when default claim issuer list for a given ticker get removed.
(caller DID, Ticker, Removed TrustedIssuer).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `IdentityId` | ```[u8; 32]```

---------
## Storage functions

---------
### AssetCompliances
 Asset compliance for a ticker (Ticker -&gt; AssetCompliance)

#### Python
```python
result = substrate.query(
    'ComplianceManager', 'AssetCompliances', ['[u8; 12]']
)
```

#### Return value
```python
{
    'paused': 'bool',
    'requirements': [
        {
            'id': 'u32',
            'receiver_conditions': [
                {
                    'condition_type': 'scale_info::174',
                    'issuers': ['scale_info::178'],
                },
            ],
            'sender_conditions': [
                {
                    'condition_type': 'scale_info::174',
                    'issuers': ['scale_info::178'],
                },
            ],
        },
    ],
}
```
---------
### StorageVersion
 Storage version.

#### Python
```python
result = substrate.query(
    'ComplianceManager', 'StorageVersion', []
)
```

#### Return value
```python
'u8'
```
---------
### TrustedClaimIssuer
 List of trusted claim issuer Ticker -&gt; Issuer Identity

#### Python
```python
result = substrate.query(
    'ComplianceManager', 'TrustedClaimIssuer', ['[u8; 12]']
)
```

#### Return value
```python
[
    {
        'issuer': '[u8; 32]',
        'trusted_for': {
            'Any': None,
            'Specific': [
                {
                    'Accredited': None,
                    'Affiliate': None,
                    'Blocked': None,
                    'BuyLockup': None,
                    'Custom': 'u32',
                    'CustomerDueDiligence': None,
                    'Exempted': None,
                    'InvestorUniqueness': None,
                    'InvestorUniquenessV2': None,
                    'Jurisdiction': None,
                    'KnowYourCustomer': None,
                    'NoType': None,
                    'SellLockup': None,
                },
            ],
        },
    },
]
```
---------
## Constants

---------
### MaxConditionComplexity
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('ComplianceManager', 'MaxConditionComplexity')
```
---------
## Errors

---------
### ComplianceRequirementTooComplex
The worst case scenario of the compliance requirement is too complex

---------
### DidNotExist
Did not exist

---------
### DuplicateComplianceRequirements
There are duplicate compliance requirements.

---------
### IncorrectOperationOnTrustedIssuer
Issuer exist but trying to add it again

---------
### InvalidComplianceRequirementId
Compliance requirement id doesn&\#x27;t exist

---------
### Unauthorized
User is not authorized.

---------