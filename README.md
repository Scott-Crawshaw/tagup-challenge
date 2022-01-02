# Tagup Backend Challenge
## Instructions
### Running the Server
Ensure that docker is installed on your machine. To build the docker image, navigate to `tagup-challenge` and run the following command.

    docker build -t exercise:latest .

Once the image is built, boot up a container using the following command.

    docker run --rm -it -p 8080:8080 exercise:latest

The server should now be running, and is accessible at `localhost:8080`. Available endpoints include the following.

    GET /healthz
    POST /data
    GET /statistics
    DELETE /statistics

Further information regarding these endpoints can be found at https://github.com/tagup/ops-challenges/tree/master/backend

### Testing
To run the test suite, begin by booting up a container using the preceding instructions. Next, ensure that `pytest` is installed on your machine by running the following command.

    pip3 install pytest

Once pytest is installed, navigate to the `tagup-challenge/tests` directory and run the following command.

    pytest

The test suite ensures that all four endpoints are functioning properly, failing and succeeding when expected.

## GitHub Actions
For any API, a robust testing protocol is crucial. However, manual testing, even when simply executing an automated test suite, can be tedious. For this reason, I often try to implement GitHub Actions to create a continuous, autonomous testing scheme.  
  
For this repository, I implemented a GitHub Actions testing protocol, which builds the Dockerfile, boots up a container, and runs the pytest suite. This is executed upon push to any branch, as well as upon pull request. The code for the action can be found at `tagup-challenge/.github/workflows/test.yml`, and the action results can be explored via the Actions tab on GitHub.

## Issues & Branching
To stay organized, I always incorporate GitHub issues and proper branching in my projects. While it proves less useful on small personal projects, it serves as a valuable practice for more robust team efforts. Feel free to take a look at the issues and merging history for this project to see how this was incorporated.

## Author
Scott Crawshaw  
scott.r.crawshaw.22@dartmouth.edu  
January 2nd, 2022  
Submission for the Tagup Backend Challenge