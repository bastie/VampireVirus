#!/bin/zsh

cd $PWD/dotnet      &&      /bin/zsh $PWD/build.zsh             &&      cd $PWD/..
cd $PWD/python      &&      /bin/zsh $PWD/build.zsh             &&      cd $PWD/..
cd $PWD/java        &&      /bin/zsh $PWD/build.zsh             &&      cd $PWD/..

