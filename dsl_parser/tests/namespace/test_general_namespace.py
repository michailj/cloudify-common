########
# Copyright (c) 2018 Cloudify Platform Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

from dsl_parser import exceptions, constants
from dsl_parser.tests.abstract_test_parser import AbstractTestParser


class TestGeneralNamspace(AbstractTestParser):
    def test_import_with_two_namespace(self):
        imported_yaml = """
inputs:
    port:
        default: 8080
"""
        import_file_name = self.make_yaml_file(imported_yaml)

        main_yaml = self.BASIC_VERSION_SECTION_DSL_1_3 + """
imports:
    -   {0}->{0}->{1}
""".format('test', import_file_name)
        self.assertRaises(exceptions.DSLParsingLogicException,
                          self.parse,
                          main_yaml)

    def test_namespace_delimiter_can_be_used_with_no_import_related(self):
        imported_yaml = """
inputs:
    ->port:
        default: 8080
"""
        import_file_name = self.make_yaml_file(imported_yaml)

        main_yaml = self.BASIC_VERSION_SECTION_DSL_1_3 + """
imports:
    -   {0}
""".format(import_file_name)
        parsed_yaml = self.parse(main_yaml)
        self.assertEqual(1, len(parsed_yaml[constants.INPUTS]))
        self.assertEqual(
            8080,
            parsed_yaml[constants.INPUTS]['->port']['default'])
