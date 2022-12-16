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
from time import strftime

import yaml
from pprintpp import pformat
from scalecodec import ScaleBytes
from scalecodec.exceptions import RemainingScaleBytesNotEmptyException

from substrateinterface import SubstrateInterface

logging.basicConfig(level=logging.INFO)


def generate_docs(node_url: str):

    with SubstrateInterface(url=node_url) as substrate:

        logging.info(f"Generating docs for {node_url}")

        version_info = substrate.get_constant('System', 'Version')
        runtime_name = version_info['spec_name'].value

        doc_file_name = os.path.join(
            os.path.dirname(__file__), 'docs', f'{runtime_name.replace(" ", "-").lower()}.md'
        )

        doc = [f"# {runtime_name}"]
        doc += ['---------']

        # doc += [f"Document generated: {strftime('%Y-%m-%d %H:%M:%S')}"]

        doc += ["| Properties |  |"]
        doc += ["| -------- | -------- |"]
        doc += [f"| Spec name     | {version_info['spec_name']}     |"]
        doc += [f"| Implementation name     | {version_info['impl_name']}     |"]
        doc += [f"| Spec version     | {version_info['spec_version']}     |"]
        doc += [f"| SS58 Format     | {substrate.ss58_format}     |"]
        doc += [f"| Token symbol      | {substrate.token_symbol}     |"]
        doc += [f"| Token decimals      | {substrate.token_decimals}     |"]

        for pallet in substrate.get_metadata().pallets:

            doc.append(f'\n## {pallet.name}')
            doc += ['---------']

            # Call functions
            if pallet.calls:

                doc.append(f'### Calls')
                doc += ['---------']

                for call_function in pallet.calls:

                    doc.append(f"#### {call_function.value['name']}")

                    for d in call_function.value['docs']:
                        d = html.escape(d)
                        doc.append(d.replace('#', '\\#'))

                    doc += [f'##### Attributes']

                    if call_function.args:
                        doc += [f'| Name | Type |']
                        doc += [f'| -------- | -------- | ']

                        for arg in call_function.args:
                            doc += [f'| {arg.name} | `{arg.value["typeName"]}` | ']
                    else:
                        doc += ['No attributes']

                    doc += ['', f'##### Python']
                    doc += [f'```python']
                    doc += [f"call = substrate.compose_call(\n    '{pallet.name}', '{call_function.name}', {pformat(call_function.get_param_info(max_recursion=5), indent=4, width=40)}\n)"]
                    doc += [f'```']
                    doc += ['\n---------']

            # Events
            if pallet.events:

                doc.append(f'### Events')
                doc += ['---------']

                for event in pallet.events:

                    doc.append(f"#### {event.name}")

                    for d in event.docs:
                        d = html.escape(d).replace('#', '\\#')
                        doc.append(d)

                    doc += [f'##### Attributes']

                    if event.args:

                        doc += [f'| Name | Type | Composition']
                        doc += [f'| -------- | -------- | -------- |']

                        for arg in event.args:
                            if type(arg.value) is str:
                                scale_type = arg.value
                            elif arg.value.get('typeName'):
                                scale_type = arg.value.get('typeName')
                            else:
                                scale_type = arg.type

                            scale_cls = substrate.runtime_config.get_decoder_class(arg.type)

                            doc += [f'| {arg.name} | `{scale_type}` | ```{scale_cls.generate_type_decomposition(max_recursion=4)}```']

                    else:
                        doc += ['No attributes']

                    doc += ['\n---------']

            # Storage functions
            if pallet.storage:

                doc.append(f'### Storage functions')
                doc += ['---------']
                for storage_function in pallet.storage:

                    doc.append(f"#### {storage_function.value['name']}")

                    for d in storage_function.docs:
                        d = html.escape(d.replace('#', '\\#'))
                        doc.append(d)

                    doc += ['', f'##### Python']
                    doc += [f'```python']
                    doc += [
                        f"call = substrate.query(\n    '{pallet.name}', '{storage_function.name}', {pformat(storage_function.get_param_info(max_recursion=5), indent=4, width=40)}\n)"]
                    doc += [f'```']

                    return_obj = substrate.runtime_config.create_scale_object(storage_function.get_value_type_string())

                    doc += ['', f'##### Return value']
                    doc += [f'```python']
                    doc += [pformat(return_obj.generate_type_decomposition(max_recursion=4))]
                    doc += [f'```']

                    doc += ['---------']

            # Constants
            if len(pallet.constants or []) > 0:

                doc += [f'### Constants']
                doc += ['---------']

                for constant in pallet.constants:

                    # Decode constant value
                    try:
                        value_obj = substrate.runtime_config.create_scale_object(constant.type)
                        value_obj.decode(ScaleBytes(constant.constant_value))
                        value = value_obj.serialize()
                    except (ValueError, RemainingScaleBytesNotEmptyException, NotImplementedError):
                        value = constant.constant_value

                    doc += [f'#### {constant.name}']

                    for d in constant.docs:
                        d = html.escape(d.replace('#', '\\#'))
                        doc.append(d)

                    doc += [f'##### Value']
                    doc += [f'```python']
                    doc += [pformat(value)]
                    doc += [f'```']

                    doc += [f'##### Python']
                    doc += [f'```python']
                    doc += [f"constant = substrate.get_constant('{pallet.name}', '{constant.name}')"]
                    doc += [f'```']

                    doc += ['---------']

            # Errors
            if len(pallet.errors or []) > 0:

                doc += [f'### Errors']
                doc += ['---------']

                for error in pallet.errors:
                    doc += [f'#### {error.name}']

                    for d in error.docs:
                        d = html.escape(d).replace('#', '\\#')
                        doc.append(d)

                    doc += ['\n---------']

        with open(doc_file_name, "w") as file:
            file.write('\n'.join(doc))


if __name__ == "__main__":

    with open("config.yml", "r") as yaml_file:
        config = yaml.load(yaml_file, Loader=yaml.FullLoader)

    for network in config["networks"]:
        generate_docs(network)
