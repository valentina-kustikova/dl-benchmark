# To run smoke test

1. Perform common installation
   [steps](../../README.md#software-installation).

1. Run tests using the following command:

   ```
   cd test/smoke_test
   ./run_smoke_test.sh
   ```

   This script performs download and convert steps for test models,
   runs `inference_benchmark.py` on simple config, and checks result file:
   * There are 20 tests
   * All the tests are passed
