# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Setup file for the TensorFlow Neural Structured Learning pip package."""

import os
import sys
import textwrap

import setuptools

INSTALL_REQUIRES = [
    "absl-py",
    "attrs",
    "scipy",
    "six",
]

NSL_OVERVIEW = textwrap.dedent("""\
    Neural Structured Learning (NSL) is a new learning paradigm to train neural
    networks by leveraging structured signals in addition to feature inputs.
    Structure can be explicit as represented by a graph or implicit as induced
    by adversarial perturbation.

    Structured signals are commonly used to represent relations or similarity
    among samples that may be labeled or unlabeled. Leveraging these signals
    during neural network training harnesses both labeled and unlabeled data,
    which can improve model accuracy, particularly when the amount of labeled
    data is relatively small. Additionally, models trained with samples that are
    generated by adversarial perturbation have been shown to be robust against
    malicious attacks, which are designed to mislead a model's prediction or
    classification.

    NSL generalizes to Neural Graph Learning as well as to Adversarial Learning.
    The NSL framework in TensorFlow provides the following easy-to-use APIs and
    tools for developers to train models with structured signals:

    * Keras APIs to enable training with graphs (explicit structure) and
      adversarial perturbations (implicit structure).

    * TF ops and functions to enable training with structure when using
      lower-level TensorFlow APIs.

    * Tools to build graphs and construct graph inputs for training.

    The NSL framework is designed to be flexible and can be used to train any
    kind of neural network. For example, feed-forward, convolution, and
    recurrent neural networks can all be trained using the NSL framework. In
    addition to supervised and semi-supervised learning (a low amount of
    supervision), NSL can in theory be generalized to unsupervised learning.
    Incorporating structured signals is done only during training, so the
    performance of the serving/inference workflow remains unchanged.""")

# Adds the path to sys.path so that we can import version.py.
version_path = os.path.join(os.path.dirname(__file__),
                            "neural_structured_learning")
sys.path.append(version_path)
from version import __version__  # pylint: disable=g-import-not-at-top

setuptools.setup(
    name="neural-structured-learning",
    version=__version__,
    author="Google LLC",
    description="Neural Structured Learning is an open-source TensorFlow "
    "framework to train neural networks with structured signals",
    long_description=NSL_OVERVIEW,
    long_description_content_type="text/plain",
    url="https://github.com/tensorflow/neural-structured-learning",
    packages=setuptools.find_packages(),
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)

# attrs
