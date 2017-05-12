# Archive.org collection transfer scripts

The provided Shell/Python scripts use the [Internet Archive Python-/CL-interface](https://github.com/jjjake/internetarchive) to transfer selected filetypes from Internet Archive collections to a [Hadoop](http://hadoop.apache.org/) cluster (HDFS).

The transfer happens in two steps:

1. A list of all files to transfer will be created ([`create_filelist.py`](create_filelist.py))
2. While the files are being transfered, the script keeps track of the already transfered files to allow restarting the process anytime and continue where it stopped ([`download_files.py`](download_files.py))

The downloaded files are being separated into different folders corresponding to their filetypes.

During transfer, a specified number of files will be downloaded into a local staging directory and copied to HDFS in a bunch (default 10, `max_staging` in `download_files.py`).

## Usage

First of all, please install https://github.com/jjjake/internetarchive to have the required `ia` command available.

Next, please modify [`download.sh`](download.sh) according to your needs to include your paths and required filetypes.
`download.sh` calls the python scripts and should be used to start off the transfer process.

#### [`download.sh`](download.sh)

To be called with `./download.sh <COLLECTION_NAME>`.<br>
E.g., `./download.sh ArchiveIt-Collection-1234`

#### [`create_filelist.py`](create_filelist.py)

Called by `download.sh`: `./create_filelist.py <COLLECTION_NAME> <GLOB_PATTERNS>`.<br>
E.g., `./create_filelist.py ArchiveIt-Collection-1234 *.cdx *.cdx.gz *.warc.gz`

#### [`download_files.py`](download_files.py)

Called by `download.sh`: `./download_files.py <COLLECTION_NAME> <LOCAL_STAGING_PATH> <HDFS_PATH>`<br>
E.g., `./download_files.py ArchiveIt-Collection-1234 /mnt/ephemeral0/holzmann/tmp /user/holzmann/ia1`
