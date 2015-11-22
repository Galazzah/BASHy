#LOCATION OF SRC FOLDER
srcDirLocation="source "$(pwd)
BashyLocation="/Bashy.sh"
BashyAliasLocation="/bashy_aliases"
#ADD BASHY TO BASH ALIASES
echo $srcDirLocation$BashyLocation >> ~/.bash_aliases
echo $srcDirLocation$BashyAliasLocation >> ~/.bash_aliases
echo "Enter in your BASHy profile API key"
read api
echo "export PROFILEURL='$api'" >> $(pwd)"/bashy_aliases"

