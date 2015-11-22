#LOCATION OF SRC FOLDER
srcDirLocation="source "$(pwd)
BashyLocation="/Bashy.sh"
BashyAliasLocation="/bashy_aliases"
#ADD BASHY TO BASH ALIASES
echo $srcDirLocation$BashyLocation >> ~/.bash_aliases
echo $srcDirLocation$BashyAliasLocation >> ~/.bash_aliases

