from cx_Freeze import setup, Executable

buildOptions = {
    'include_files': ['data/', 'objects/', 'state/'],
    'includes': ['numpy.core._methods', 'numpy.lib.format']
}

setup(
    name='Operation MoonLight',
    version='0.0.1',
    options={
        'build_exe': buildOptions
    },
    executables=[Executable('main.py')]
)