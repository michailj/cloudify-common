########
# Copyright (c) 2017 GigaSpaces Technologies Ltd. All rights reserved
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


class _Wrapper(object):
    def __init__(self, response_dict):
        self.response_dict = response_dict

    def __getattr__(self, item):
        return self.response_dict[item]


def wrap(obj_dict, cls_name):
    return type('Rest{0}'.format(cls_name), (_Wrapper, ), {})(obj_dict)
