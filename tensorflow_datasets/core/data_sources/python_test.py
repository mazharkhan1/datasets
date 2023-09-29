# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Tests for the PythonDataSource."""

import pickle

from tensorflow_datasets.core.data_sources import python


def getitem(i):
  return i


def test_create_a_python_data_source():
  source = python.PythonDataSource(length=2, getitem=getitem)
  assert len(source) == 2
  assert source[0] == 0
  assert source[1] == 1
  assert source[2] == 2


def test_iterate_on_a_python_data_source():
  source = python.PythonDataSource(length=42, getitem=getitem)
  i = 0
  for i, j in enumerate(iter(source)):
    assert i == j
  assert i == 41


def test_python_data_source_is_pickable():
  def _getitem(i):
    return i

  source = python.PythonDataSource(length=42, getitem=_getitem)
  source = pickle.loads(pickle.dumps(source))
  assert source[0] == 0
