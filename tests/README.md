# To run the tests

### Via PyCharm
- Confirm that PyCharm has been configured correctly: project interpreter and environment variables
- Navigate to any of the `tests/test_*` files and use the PyCharm UI to run the test
It should pass first time.

### Via CLI

To run all the tasks, it's advisable to do that via the command line. This can be done via the following command
from the `kseniya-test-framework` folder:

```shell
poetry shell
poetry run python -m pytest tests/
```

### Via Docker

To run the tests inside a container using the image inside root folder of this repository.

```shell
docker build . -t  jenkins-docker 
docker run jenkins-docker pytest -s -v tests/"
```

### Via Jenkins & Docker

Before completing the below steps make sure that Jenkins user has access to interaction with Docker. Enter the following command in your CLI:
```
sudo usermod -a -G docker jenkins
grep docker /etc/group
```
The output should be something like this 
```
docker:x:1001:<YOUR_PROFILE_NAME>,jenkins
```

After that you are ready to go further!
Start jenkins 
```
sudo service jenkins start
```
**
1. Login to Jenkins via http://localhost:8080/
2. Click "New Item"
3. Fill in the name of the job, select Pipeline option and proceed
4. In **Pipeline** section select "Pipeline script from SCM" option
5. In SCM dropdown select GIT.
6. Repository URL, insert https://github.com/sticey-epam/py-framework-ui
7. Leave "None" option in credentials as the repository is public
8. In "Branch Specifier" change 'master' value to 'main'
9. Make sure that script path has value "Jenkinsfile"
10. Click "Save" and then run the build.
**


### Expected successful pytest report
```
=================================================================== test session starts ===================================================================
platform linux -- Python 3.9.7, pytest-7.1.2, pluggy-1.0.0 -- /home/sticey/.pyenv/versions/3.9.7/bin/python
cachedir: .pytest_cache
rootdir: /home/sticey/sticey-project, configfile: pytest.ini
collected 6 items                                                                                                                                         

test_add_remove.py::TestAddRemove::test_add_element PASSED                                                                                          [ 16%]
test_dropdown.py::TestDropdown::test_select_element PASSED                                                                                          [ 33%]
test_lesson22.py::TestPages::test_demo_guru99 PASSED                                                                                                [ 50%]
test_lesson22.py::TestPages::test_herokuapp PASSED                                                                                                  [ 66%]
test_main_page.py::TestMainPage::test_main_page PASSED                                                                                              [ 83%]
test_requests.py::test_requests PASSED                                                                                                              [100%]

=================================================================== 6 passed in 30.42s ====================================================================
```