@echo off
REM Windows batch script to run tests
echo Setting up test environment...
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
echo.
echo Running tests...
pytest --html=reports/report.html --self-contained-html
echo.
echo Test report generated at reports/report.html
pause

