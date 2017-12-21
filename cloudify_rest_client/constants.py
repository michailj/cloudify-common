########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
############

import copy


class AvailabilityState(object):
    PRIVATE = 'private'
    TENANT = 'tenant'
    GLOBAL = 'global'

    STATES = [PRIVATE, TENANT, GLOBAL]


states_except_private = copy.deepcopy(AvailabilityState.STATES)
states_except_private.remove(AvailabilityState.PRIVATE)
AVAILABILITY_EXCEPT_PRIVATE = states_except_private

states_except_global = copy.deepcopy(AvailabilityState.STATES)
states_except_global.remove(AvailabilityState.GLOBAL)
AVAILABILITY_EXCEPT_GLOBAL = states_except_global
