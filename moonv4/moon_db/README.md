# moon_db

This package contains the database module for the Moon project
It is designed to provide a driver to access the Moon database.

For any other information, refer to the parent project:

    https://git.opnfv.org/moon

## Build
### Build Python Package
- `cd ${MOON_HOME}/moonv4/moon_utilities/`
- `python3 setup.py sdist bdist_wheel`

### Upload moon_db to PIP
- `python setup.py upload`
or 
- `gpg --detach-sign -u "${GPG_ID}" -a dist/moon_db-X.Y.Z-py3-none-any.whl`
- `gpg --detach-sign -u "${GPG_ID}" -a dist/moon_db-X.Y.Z.tar.gz`
- `twine upload dist/moon_db-X.Y.Z-py3-none-any.whl dist/moon_db-X.Y.Z-py3-none-any.whl.asc`
- `twine upload dist/moon_db-X.Y.Z.tar.gz dist/moon_db-X.Y.Z.tar.gz.asc`


## Test
### Python Unit Test
launch Docker for Python unit tests
- `cd ${MOON_HOME}/moonv4/moon_utilities`
- `docker run --rm --volume $(pwd):/data wukongsun/moon_python_unit_test:latest`
