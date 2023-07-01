# DLI: Deep Learning Inference Benchmark

## Introduction

This is a repo of deep learning inference benchmark, called DLI.
DLI is a benchmark for deep learning inference on various hardware.
The goal of the project is to develop a software for measuring
the performance of a wide range of deep learning models
inferring on various popular frameworks and various hardware,
as well as regularly publishing the obtained measurements.

The main advantage of DLI from the existing benchmarks
is the availability of performance results for a large number
of deep models inferred on Intel-platforms (Intel CPUs, Intel
Processor Graphics, Intel Movidius Neural Compute Stick).

DLI supports inference using the following frameworks:

- [Intel® Distribution of OpenVINO™ Toolkit][openvino-toolkit].
- [Intel® Optimization for Caffe][intel-caffe].
- [Intel® Optimizations for TensorFlow][intel-tensorflow].
- [TensorFlow Lite][tensorflow-lite].
- [ONNX Runtime][onnx-runtime] (C++ and Python APIs).
- [MXNet][mxnet].
- [OpenCV DNN][opencv-dnn] (C++ and Python APIs).
- [PyTorch][pytorch].

More information about DLI is available on the web-site
([here][dli-ru-web-page] (in Russian)
or [here][dli-web-page] (in English)) or on the [Wiki page][dli-wiki].

## License

This project is licensed under the terms of the [Apache 2.0 license](LICENSE).

## Cite

Please consider citing the following papers.

1. Kustikova V., Vasilyev E., Khvatov A., Kumbrasiev P., Rybkin R.,
Kogteva N. DLI: Deep Learning Inference Benchmark //
Communications in Computer and Information Science.
V.1129. 2019. P. 542-553.

1. Sidorova A.K.,  Alibekov M.R., Makarov A.A., Vasiliev E.P., 
Kustikova V.D. Automation of collecting performance indicators 
for the inference of deep neural networks in Deep Learning 
Inference Benchmark // Mathematical modeling and supercomputer 
technologies. Proceedings of the XXI International Conference 
(N. Novgorod, November 22–26, 2021). – Nizhny Novgorod: Nizhny
Novgorod State University Publishing House, 2021. – 423 p.
[https://hpc-education.unn.ru/files/conference_hpc/2021/MMST2021_Proceedings.pdf][mmst-2021].
(In Russian)

## Repo structure

- `demo` directory contains demos for different frameworks
  and operating systems.

  - `OpenVINO_DLDT` is directory that contains demos
    for Intel® Distribution of OpenVINO™ Toolkit.

- `docker` directory contains Dockerfiles.

  - `Caffe` is a directory of Dockerfiles for Intel® Optimization
    for Caffe.
  - `OpenVINO_DLDT` is a directory of Dockerfiles for Intel®
    Distribution of OpenVINO™ Toolkit.
  - `TensorFlow` is a directory of Dockerfiles for Intel® Optimizations
    for TensorFlow.
  - `MXNet` is a directory of Dockerfiles for MXNet.
  - `ONNXRuntime` is a directory of Dockerfiles for ONNX Runtime.
  - `OpenCV` is a directory of Dockerfiles for OpenCV.

- `docs` directory contains auxiliary documentation. Please, find
  complete documentation at the [Wiki page][dli-wiki].

- `results` directory contains benchmarking and validation results.

  - [`benchmarking`](results/benchmarking) contains benchmarking 
    results in html- and xslx-formats.
  - [`accuracy`](results/accuracy) contains accuracy
    results in html- and xslx-formats.
  - [`validation`](results/validation) contains tables that confirms 
    correctness of inference implementation for the benchmarked models.

    - [`validation_results_openvino_public_models.md`](results/validation/validation_results_openvino_public_models.md)
      is a table that confirms correctness of inference implementation
      based on Intel Distribution of OpenVINO™ toolkit for public models.
    - [`validation_results_openvino_intel_models.md`](results/validation/validation_results_openvino_intel_models.md)
      is a table that confirms correctness of inference implementation
      based on Intel® Distribution of OpenVINO™ toolkit for models trained
      by Intel engineers and available in [Open Model Zoo][open-model-zoo].
    - [`validation_results_opencv.md`](results/validation/validation_results_opencv.md)
      is a table that confirms correctness of inference implementation
      based on OpenCV DNN.
    - [`validation_results_caffe.md`](results/validation/validation_results_caffe.md)
      is a table that confirms correctness of inference implementation
      based on Intel® Optimization for Caffe for several public models.
    - [`validation_results_tensorflow.md`](results/validation/validation_results_tensorflow.md)
      is a table that confirms correctness of inference implementation
      based on Intel® Optimizations for TensorFlow for several public models.
    - [`validation_results_tflite.md`](results/validation/validation_results_tflite.md)
      is a table that confirms correctness of inference implementation
      based on TensorFlow Lite for public models.
    - [`validation_results_mxnet_gluon_modelzoo.md`](results/validation/validation_results_mxnet_gluon_modelzoo.md)
      is a table that confirms correctness of inference implementation
      based on MXNet for [GluonCV-models][gluoncv-omz].
    - [`validation_results_pytorch.md`](results/validation/validation_results_pytorch.md)
      is a table that confirms correctness of inference implementation
      based on PyTorch for [TorchVision][torchvision].

  - [`mxnet_models_checklist.md`](results/mxnet_models_checklist.md) contains a list
    of deep models inferred by MXNet checked in the DLI benchmark.
  - [`openvino_models_checklist.md`](results/openvino_models_checklist.md) contains a list
    of deep models inferred by the OpenVINO toolkit checked in the DLI benchmark.
  - [`opencv_models_checklist.md`](results/opencv_models_checklist.md) contains a list
    of deep models inferred by OpenCV DNN.
  - [`tensorflow_models_checklist.md`](results/tensorflow_models_checklist.md) contains a list
    of deep models inferred by TensorFlow checked in the DLI benchmark.
  - [`tflite_models_checklist.md`](results/tflite_models_checklist.md) contains a list
    of deep models inferred by TensorFlow Lite checked in the DLI benchmark.
  - [`pytorch_models_checklist.md`](results/pytorch_models_checklist.md) contains a list
    of deep models inferred by PyTorch checked in the DLI benchmark.

- `src` directory contains benchmark sources.

  - `accuracy_checker` contains scripts to check deep model accuracy
    using Accuracy Checker of Intel® Distribution of OpenVINO™ toolkit.
  - `benchmark` is a set of scripts to estimate inference
    performance of different models at the single local computer.
  - `config_maker`contains GUI-application to make configuration files
    of the benchmark components.
  - `configs` contains template configuration files.
  - `cpp_dl_benchmark` contains C++ tools that allow to measure
    deep learning models inference performance with
    [ONNX Runtime][onnx-runtime-github]
    and [OpenCV DNN][opencv-dnn] in C++ API implementation.
    This implementation inspired by [OpenVINO Benchmark C++ tool][benchmark-app]
    as a reference and stick to its measurement methodology,
    thus provide consistent performance results.
  - `csv2html` is a set of scripts to convert performance and accuracy
     tables from csv to html.
  - `csv2xlsx` is a set of scripts to convert performance and accuracy
     tables from csv to xlsx.
  - `deployment` is a set of deployment tools.
  - `inference` contains python inference implementation.
  - `model_converters` contains converters of deep models.
  - `node_info` contains a set of functions to get information about
    computational node.
  - `quantization` contains scripts to quantize model to INT8-precision
    using Post-Training Optimization Tool (POT)
    of Intel® Distribution of OpenVINO™ toolkit.
  - `remote_control` contains scripts to execute benchmark
    remotely.
  - `utils` is a package of auxiliary utilities.

- `test` contains smoke tests.

## Documentation

The latest documentation for the Deep Learning Inference
Benchmark (DLI) is available [here][dli-wiki]. This documentation
contains detailed information about the DLI components and provides
step-by-step guides to build and run the DLI benchmark on your own
test infrastructure.

### How to build

See the [DLI Wiki][dli-wiki-build] to get more information.

### How to deploy

See the [DLI Wiki][dli-wiki-deploy] to get more information.

### How to contribute

See the [DLI Wiki][dli-wiki-contribute] to get more information.

### Available benchmarking results

See the [DLI Wiki][dli-wiki-bench-results] to get more information
about benchmaring results on available hardware.

### Get a support

Report questions, issues and suggestions, using:

- [GitHub Issues][dli-github-issues]


<!-- LINKS -->
[openvino-toolkit]: https://software.intel.com/en-us/openvino-toolkit
[intel-caffe]: https://github.com/intel/caffe
[intel-tensorflow]: https://www.intel.com/content/www/us/en/developer/articles/guide/optimization-for-tensorflow-installation-guide.html
[tensorflow-lite]: https://www.tensorflow.org/lite
[onnx-runtime]: https://onnxruntime.ai
[onnx-runtime-github]: https://github.com/microsoft/onnxruntime
[mxnet]: https://mxnet.apache.org
[opencv-dnn]: https://docs.opencv.org/4.7.0/d2/d58/tutorial_table_of_content_dnn.html
[pytorch]: https://pytorch.org
[benchmark-app]: https://github.com/openvinotoolkit/openvino/tree/master/samples/cpp/benchmark_app
[dli-ru-web-page]: http://hpc-education.unn.ru/dli-ru
[dli-web-page]: http://hpc-education.unn.ru/dli
[open-model-zoo]: https://github.com/opencv/open_model_zoo
[gluoncv-omz]: https://cv.gluon.ai/model_zoo/index.html
[torchvision]: https://pytorch.org/vision/stable/models.html
[mmst-2021]: https://hpc-education.unn.ru/files/conference_hpc/2021/MMST2021_Proceedings.pdf
[dli-wiki]: https://github.com/itlab-vision/dl-benchmark/wiki
[dli-wiki-build]: https://github.com/itlab-vision/dl-benchmark/wiki#how-to-build
[dli-wiki-contribute]: https://github.com/itlab-vision/dl-benchmark/wiki#developer-documentation
[dli-wiki-deploy]: https://github.com/itlab-vision/dl-benchmark/wiki#how-to-deploy-and-run
[dli-wiki-bench-results]: https://github.com/itlab-vision/dl-benchmark/wiki#benchmarking-results
[dli-github-issues]: https://github.com/itlab-vision/dl-benchmark/issues
