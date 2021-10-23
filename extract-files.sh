#!/bin/bash -e

BASE_DIR="$(dirname "${0}")"
EXTRACT_DIR="${1}"

if [ -z "${EXTRACT_DIR}" ]; then
    >&2 echo "error: No asset directory given"
    exit 1
fi

mkdir -p "${BASE_DIR}/.git/info"

while read -r line; do
    if [ -z "${line}" ]; then
        continue
    fi

    if [[ ${line} = \#* ]]; then
        continue
    fi

    IFS=':' read -r destination_file source_file <<< "${line}"

    echo "${destination_file}" >> "${BASE_DIR}/.git/info/exclude"

    if [ -f "${BASE_DIR}/${destination_file}" ]; then
        echo "Skipping file '${destination_file}' as it already exists"
        continue
    fi

    mkdir -p "$(dirname "${BASE_DIR}/${destination_file}")"

    case "${source_file}" in
    *.bmp)
        echo "Converting BMP file from '${source_file}' to '${destination_file}'"
        convert "${EXTRACT_DIR}/${source_file}" "${BASE_DIR}/${destination_file}"
        ;;
    *)
        echo "Copying file from '${source_file}' to '${destination_file}'"
        cp -f "${EXTRACT_DIR}/${source_file}" "${BASE_DIR}/${destination_file}"
        ;;
    esac
done < proprietary-files.txt
