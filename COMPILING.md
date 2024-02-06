# Document Builder
**Note - this method is still in testing**

## Document Compilation Instructions
1. Install Docker on your computer (see instructions for different architectures [in the Docker docs](https://docs.docker.com/engine/install/))
2. Build the docker image: `docker build ./docker -t llmsvs-builder`
3. Change directory to the target version. E.g `cd 0.1`
4. Optionally perform a clean with `docker run -it  --rm -v "$(pwd):/data" llmsvs-builder clean`
5. Build the PDF with `docker run -it  --rm -v "$(pwd):/data" llmsvs-builder pdf`
6. The PDF will be located within the `TARGET_VERSION/dist`
directory.