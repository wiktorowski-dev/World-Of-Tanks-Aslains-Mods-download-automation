#!/usr/bin/env bash

function download_mod() {
    python download_mod.py $1
    cd $FILEPATH$1
}