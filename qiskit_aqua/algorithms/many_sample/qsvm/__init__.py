# -*- coding: utf-8 -*-

# Copyright 2018 IBM.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

from .data_preprocess import get_points_and_labels, get_points
from .qpsolver import optimize_SVM
from .quantum_circuit_kernel import (entangler_map_creator, inner_prod_circuit_ML,
                                     get_zero_string, kernel_join)
from .svm_qkernel_abc import SVM_QKernel_ABC

__all__ = ['get_points_and_labels',
           'get_points',
           'optimize_SVM',
           'entangler_map_creator',
           'inner_prod_circuit_ML',
           'get_zero_string',
           'kernel_join',
           'SVM_QKernel_ABC'
           ]
