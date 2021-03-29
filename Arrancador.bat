::Este batch levanta el servidor Django automaticamente
@echo off
cls

::Arrancar server
@cd %CD%
cls
python manage.py runserver 0.0.0.0:8000
pause