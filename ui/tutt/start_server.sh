
# Does the symlink in public directory exist?  If not, create it
if [ ! -L public/dataset ]; then
    echo "Creating symlink to dataset directory since it doesn't exist"
    ln -s ../../../dataset public/dataset
fi

npm run dev
