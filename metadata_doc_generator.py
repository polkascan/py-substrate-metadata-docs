# PySubstrate Metadata Docs
#
# Copyright 2018-2022 Stichting Polkascan (Polkascan Foundation).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import html
import logging
import os

import yaml
from pprintpp import pformat
from scalecodec import ScaleBytes
from scalecodec.exceptions import RemainingScaleBytesNotEmptyException

from substrateinterface import SubstrateInterface
from websocket import WebSocketBadStatusException, WebSocketAddressException, WebSocketTimeoutException

logging.basicConfig(level=logging.INFO)


def generate_docs(node_url: str):

    with SubstrateInterface(url=node_url) as substrate:

        version_info = substrate.get_constant('System', 'Version')
        runtime_name = version_info['spec_name'].value

        doc_dir_name = os.path.join(
            os.path.dirname(__file__), 'docs', runtime_name.replace(" ", "-").lower()
        )

        doc_file_name = os.path.join(
            doc_dir_name, 'index.md'
        )

        result = {'name': substrate.chain, 'file': f'{runtime_name.replace(" ", "-").lower()}/index.md', 'pallets': []}

        os.makedirs(doc_dir_name, exist_ok=True)

        doc = [f"# {substrate.chain}"]
        doc += ['\n---------\n']

        # doc += [f"Document generated: {strftime('%Y-%m-%d %H:%M:%S')}"]

        doc += [f"## Properties"]

        doc += ["| Name | Value |"]
        doc += ["| -------- | -------- |"]
        doc += [f"| Spec name     | {version_info['spec_name']}     |"]
        doc += [f"| Implementation name     | {version_info['impl_name']}     |"]
        doc += [f"| Spec version     | {version_info['spec_version']}     |"]
        doc += [f"| SS58 Format     | {substrate.ss58_format}     |"]
        doc += [f"| Token symbol      | {substrate.token_symbol}     |"]
        doc += [f"| Token decimals      | {substrate.token_decimals}     |"]

        pallets = substrate.get_metadata().pallets
        pallets.sort(key=lambda x: x.name)

        if len(pallets) > 0:
            doc += [f"\n## Pallets"]

            doc += ["| Name | Calls | Events | Storage functions | Constants | Errors |"]
            doc += ["| -------- | -------- | -------- | -------- | -------- | -------- |"]

        for pallet in pallets:

            pallet_file_name = os.path.join(doc_dir_name, f'{pallet.name.lower()}.md')
            rel_link = f'{runtime_name.replace(" ", "-").lower()}/{pallet.name.lower()}.md'

            result['pallets'].append({'name': pallet.name, 'file': rel_link})

            pallet_doc = [f'\n# {pallet.name}']
            pallet_doc += ['\n---------']

            # Call functions
            if pallet.calls:

                pallet_doc.append(f'## Calls')
                pallet_doc += ['\n---------']

                # Sort by name
                call_functions = pallet.calls.elements
                call_functions.sort(key=lambda x: x.name)

                for call_function in call_functions:

                    pallet_doc.append(f"### {call_function.value['name']}")

                    for d in call_function.value['docs']:
                        d = html.escape(d)
                        pallet_doc.append(d.replace('#', '\\#'))

                    pallet_doc += [f'#### Attributes']

                    if call_function.args:
                        pallet_doc += [f'| Name | Type |']
                        pallet_doc += [f'| -------- | -------- | ']

                        for arg in call_function.args:
                            pallet_doc += [f'| {arg.name} | `{arg.value["typeName"]}` | ']
                    else:
                        pallet_doc += ['No attributes']

                    pallet_doc += ['', f'#### Python']
                    pallet_doc += [f'```python']
                    pallet_doc += [f"call = substrate.compose_call(\n    '{pallet.name}', '{call_function.name}', {pformat(call_function.get_param_info(max_recursion=5), indent=4, width=40)}\n)"]
                    pallet_doc += [f'```']
                    pallet_doc += ['\n---------']

            # Events
            if pallet.events:

                pallet_doc.append(f'## Events')
                pallet_doc += ['\n---------']

                # Sort by name
                events = pallet.events.elements
                events.sort(key=lambda x: x.name)

                for event in events:

                    pallet_doc.append(f"### {event.name}")

                    for d in event.docs:
                        d = html.escape(d).replace('#', '\\#')
                        pallet_doc.append(d)

                    pallet_doc += [f'#### Attributes']

                    if event.args:

                        pallet_doc += [f'| Name | Type | Composition']
                        pallet_doc += [f'| -------- | -------- | -------- |']

                        for arg in event.args:
                            if type(arg.value) is str:
                                scale_type = arg.value
                            elif arg.value.get('typeName'):
                                scale_type = arg.value.get('typeName')
                            else:
                                scale_type = arg.type

                            scale_cls = substrate.runtime_config.get_decoder_class(arg.type)

                            pallet_doc += [f'| {arg.name} | `{scale_type}` | ```{scale_cls.generate_type_decomposition(max_recursion=4)}```']

                    else:
                        pallet_doc += ['No attributes']

                    pallet_doc += ['\n---------']

            # Storage functions
            if pallet.storage:

                pallet_doc.append(f'## Storage functions')
                pallet_doc += ['\n---------']

                # Sort by name
                storage_functions = pallet.storage
                storage_functions.sort(key=lambda x: x.name)

                for storage_function in storage_functions:

                    pallet_doc.append(f"### {storage_function.value['name']}")

                    for d in storage_function.docs:
                        d = html.escape(d.replace('#', '\\#'))
                        pallet_doc.append(d)

                    pallet_doc += ['', f'#### Python']
                    pallet_doc += [f'```python']
                    pallet_doc += [
                        f"result = substrate.query(\n    '{pallet.name}', '{storage_function.name}', {pformat(storage_function.get_param_info(max_recursion=5), indent=4, width=40)}\n)"]
                    pallet_doc += [f'```']

                    return_obj = substrate.runtime_config.create_scale_object(storage_function.get_value_type_string())

                    pallet_doc += ['', f'#### Return value']
                    pallet_doc += [f'```python']
                    pallet_doc += [pformat(return_obj.generate_type_decomposition(max_recursion=4))]
                    pallet_doc += [f'```']

                    pallet_doc += ['---------']

            # Constants
            if len(pallet.constants or []) > 0:

                pallet_doc += [f'## Constants']
                pallet_doc += ['\n---------']

                # Sort by name
                constants = pallet.constants
                constants.sort(key=lambda x: x.name)

                for constant in constants:

                    # Decode constant value
                    try:
                        value_obj = substrate.runtime_config.create_scale_object(constant.type)
                        value_obj.decode(ScaleBytes(constant.constant_value))
                        value = value_obj.serialize()
                    except (ValueError, RemainingScaleBytesNotEmptyException, NotImplementedError):
                        value = constant.constant_value

                    pallet_doc += [f'### {constant.name}']

                    for d in constant.docs:
                        d = html.escape(d.replace('#', '\\#'))
                        pallet_doc.append(d)

                    pallet_doc += [f'#### Value']
                    pallet_doc += [f'```python']
                    pallet_doc += [pformat(value)]
                    pallet_doc += [f'```']

                    pallet_doc += [f'#### Python']
                    pallet_doc += [f'```python']
                    pallet_doc += [f"constant = substrate.get_constant('{pallet.name}', '{constant.name}')"]
                    pallet_doc += [f'```']

                    pallet_doc += ['---------']

            # Errors
            if len(pallet.errors or []) > 0:

                pallet_doc += [f'## Errors']
                pallet_doc += ['\n---------']

                errors = pallet.errors.elements
                errors.sort(key=lambda x: x.name)

                for error in errors:
                    pallet_doc += [f'### {error.name}']

                    for d in error.docs:
                        d = html.escape(d).replace('#', '\\#')
                        pallet_doc.append(d)

                    pallet_doc += ['\n---------']

            doc += [f"| [{pallet.name}]({pallet.name.lower()}.md) | [{len(pallet.calls or [])}]({pallet.name.lower()}.md#calls) | [{len(pallet.events or [])}]({pallet.name.lower()}.md#events) | [{len(pallet.storage or [])}]({pallet.name.lower()}.md#storage-functions) | [{len(pallet.constants or [])}]({pallet.name.lower()}.md#constants) | [{len(pallet.errors or [])}]({pallet.name.lower()}.md#errors) |"]

            # Write pallet doc
            with open(pallet_file_name, "w") as file:
                file.write('\n'.join(pallet_doc))

        with open(doc_file_name, "w") as file:
            file.write('\n'.join(doc))

        return result


if __name__ == "__main__":

    with open("config.yml", "r") as yaml_file:
        config = yaml.load(yaml_file, Loader=yaml.FullLoader)

    for section in config["networks"]:

        section_name, networks = list(section.items())[0]

        print(f'- {section_name}: ')
        for network in networks:
            logging.info(f"Generating docs for {network}")
            try:
                info = generate_docs(network)
                print(f'  - {info["name"]}: ')
                print(f'    - {info["file"]}')
                for pallet in info["pallets"]:
                    print(f'    - {pallet["name"]}: {pallet["file"]}')
            except (WebSocketBadStatusException, WebSocketAddressException, WebSocketTimeoutException):
                logging.error(f"Failed to generate docs for {network}")
