@Echo OFF
IF EXIST "%APPDATA%\krita\pykrita" (
	FOR /f %%f IN ('dir /b plugin') DO (
		IF EXIST "%APPDATA%\krita\pykrita\%%f" (
			echo Plugin already installed.
			goto end
		)
	)
	xcopy /s /E "plugin\*.*" "%APPDATA%\krita\pykrita"
	echo Plugin successfully installed.
	:end
	timeout 5
	EXIT
)