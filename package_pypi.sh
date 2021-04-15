python setup.py sdist
# shellcheck disable=SC2012
FILE=$(ls -t dist | head -1)
twine upload "dist/$FILE" --username venafi-spi --password 'huc*thek4RALD*cugh'
