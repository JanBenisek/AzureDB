# Azure storage webapp

Simple cloud storage website built with Flask and Azure blob storage.

### How to start:
  - install `az` cli on your PC
  - create a resource group
  - add a storage account
    - `az storage account create --kind StorageV2 --resource-group [group-name] --location centralus --name [storage-name]`
  - add a container
    -  `az storage container create -n [container-name] --fail-on-exist --connection-string [conn-string]`
  - give public read access to the container otherwise users cannot download the files
    - `az storage container set-permission --name [container-name] --account-name [storage-name] --public-access container --account-key [storage-access-key] --auth-mode key`
  - make sure that `config.py` file is modified accordingly (azure account and container)
  - connection keys (connection string for azure and secret key for flask) are stored in `connection_secrets.py` which you need to supplement
  - run `app.py` and enjoy the page


### Useful resources:
  - https://flask-dropzone.readthedocs.io/en/latest/
  - https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
  - https://docs.faculty.ai/user-guide/apis/flask_apis/flask_file_upload_download.html
  - https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/
  - https://hackersandslackers.com/flask-jinja-templates
  - https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask
  - https://stackoverflow.com/questions/58900507/upload-and-delete-azure-storage-blob-using-azure-storage-blob-or-azure-storage/58900508#58900508