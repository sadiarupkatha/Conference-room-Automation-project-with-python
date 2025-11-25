@echo off
REM Windows batch script to run smoke tests
echo Running Smoke Tests against: https://muntasir101.github.io/CRBA/
echo.
pytest tests/test_smoke.py -v --html=reports/smoke_report.html --self-contained-html
echo.
echo Smoke test report generated at reports/smoke_report.html
pause

