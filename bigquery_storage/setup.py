# -*- coding: utf-8 -*-
#
# Copyright 2018 Google LLC
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

import io
import os

import setuptools

name = "google-cloud-bigquery-storage"
description = "BigQuery Storage API API client library"
version = "0.6.0"
release_status = "Development Status :: 4 - Beta"
dependencies = [
    "google-api-core[grpc] >= 1.6.0, < 2.0.0dev",
    "googleapis-common-protos >= 1.5.9, < 2.0.0dev",
    'enum34; python_version < "3.4"',
]
extras = {
    "pandas": "pandas>=0.17.1",
    "fastavro": "fastavro>=0.21.2",
    "pyarrow": "pyarrow>=0.13.0, != 0.14.0",
}

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

packages = [
    package for package in setuptools.find_packages() if package.startswith("google")
]

namespaces = ["google"]
if "google.cloud" in packages:
    namespaces.append("google.cloud")

setuptools.setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    author="Google LLC",
    author_email="googleapis-packages@google.com",
    license="Apache 2.0",
    url="https://github.com/GoogleCloudPlatform/google-cloud-python",
    classifiers=[
        release_status,
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "Topic :: Internet",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=packages,
    namespace_packages=namespaces,
    install_requires=dependencies,
    extras_require=extras,
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
    include_package_data=True,
    zip_safe=False,
)
