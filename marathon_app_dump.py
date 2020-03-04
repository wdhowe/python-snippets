#!/usr/bin/env python3
"""
Title: marathon_app_dump.py
Description: Backup/Restore Marathon App Config to/from files
Author: Bill Howe
"""

# =======================
# Import Modules
# =======================
# argparse: Command line arguments
import argparse

# ConfigParser: Use variables from external file
import configparser

# os: Use bash environment variables
import os

# json format library
import json

# requests: http library
import requests

# =======================
# Get Script Arguments
# =======================
# Build argument parser information
PARSER = argparse.ArgumentParser(
    description="Backup/Restore Marathon Apps in JSON format via the API."
)
PARSER.add_argument(
    "-b",
    "--backup",
    help="Perform a job backup operation.[backup or restore Required]",
    action="store_true",
    required=False,
)
PARSER.add_argument(
    "-r",
    "--restore",
    help="Perform a job restore operation.[backup or restore Required]",
    action="store_true",
    required=False,
)
PARSER.add_argument(
    "-e", "--env", help="Marathon Environment Name(dev|prod)[Required]", required=True
)
PARSER.add_argument(
    "-j",
    "--job",
    help="Job name beginning match (Ex: 'all' for all jobs or 'admin' for only jobs that start with admin)[Required]",
    required=True,
)
PARSER.add_argument(
    "-f",
    "--file",
    help="Backup to or restore from this file.[Optional]",
    required=False,
)
PARSER.add_argument(
    "-t",
    "--test",
    help="Do NOT make any changes. Run test and output what would have happened.",
    action="store_true",
    required=False,
)
ARGS = vars(PARSER.parse_args())

# backup|restore validation: Must backup or restore, but not both
if ARGS["backup"] and ARGS["restore"]:
    print(">> ERROR! Cannot perform both backup (-b) and restore (-r). Exiting.")
    PARSER.print_help()
    exit(1)
elif not ARGS["backup"] and not ARGS["restore"]:
    print(">> ERROR! Must perform either backup (-b) or restore (-r). Exiting.")
    PARSER.print_help()
    exit(1)

# env validation: Ensure a good environment is provided
if ARGS["env"] == "dev":
    MARATHON_SITE = "https://mymarathondev.domain.org:8443/v2/apps"

elif ARGS["env"] == "prod":
    MARATHON_SITE = "https://mymarathonprod.domain.org:8443/v2/apps"

else:
    print(f">> ERROR! Unknown passed environment (Env: {ARGS['env']}). Exiting.")
    PARSER.print_help()
    exit(1)

# file validation
if not ARGS["file"]:
    FILE_PATH = "marathon_apps_" + ARGS["env"] + ".json"
    print(f">> No file input detected, using filename: {FILE_PATH}")
else:
    FILE_PATH = ARGS["file"]


# =======================
# Config Settings
# =======================
CONFIG = configparser.ConfigParser()
CONFIG_PATH = os.environ.get("HOME") + "/.marathon-api.conf"
CONFIG.read(CONFIG_PATH)

# Parse config file settings
try:
    MARATHON_LOGIN = CONFIG.get("marathon", "username")
    MARATHON_PASSWORD = CONFIG.get("marathon", "password")
except (configparser.NoSectionError, configparser.NoOptionError):
    print(
        ">> ERROR! Was unable to read config section or option ("
        + CONFIG_PATH
        + "). Ensure that config file exists."
    )
    print("-> File must also contain the following: ")
    print("[marathon]")
    print("username = USERNAME-HERE")
    print("password = PASSWORD-HERE")
    exit(1)


def get_apps_data():
    """
    Download Marathon application configuration
    """
    # Marathon endpoint we are contacting
    print("\n>> Backup jobs from Marathon Endpoint: " + MARATHON_SITE)

    # Perform HTTP GET on Marathon API
    response = requests.get(MARATHON_SITE, auth=(MARATHON_LOGIN, MARATHON_PASSWORD))
    print("-> HTTP Status Code was: " + str(response.status_code))

    if response.status_code != 200:
        print("--> ERROR! Response code was NOT 200(OK), exiting now.")
        exit(1)

    return response.json()


def put_apps_data(loaded_jobs):
    """
    Restore Marathon application configuration
    """
    print("\n>> Restoring jobs to Marathon Endpoint: " + MARATHON_SITE)

    if ARGS["job"] == "all":
        print("-> Restoring all jobs.")
    else:
        print(f"-> Restoring a subset of jobs that start with '{ARGS['job']}'.")

    for job in loaded_jobs["apps"]:
        if ARGS["test"]:
            if (ARGS["job"] != "all" and job["id"].startswith("/" + ARGS["job"])) or (
                ARGS["job"] == "all"
            ):
                print(f"--> [TEST] I would have restored job: {job['id']}")
        else:
            if (ARGS["job"] != "all" and job["id"].startswith("/" + ARGS["job"])) or (
                ARGS["job"] == "all"
            ):
                print(f"--> Restoring job: {job['id']}")
                response = requests.post(
                    MARATHON_SITE, auth=(MARATHON_LOGIN, MARATHON_PASSWORD), json=job
                )

                if response.status_code == 200 or response.status_code == 201:
                    print(f"---> OK. (HTTP: {str(response.status_code)})")
                else:
                    print(
                        f"---> WARNING! Job might not have deployed (HTTP: {str(response.status_code)})"
                    )
                    print(f"     Response: {str(response.json())})")


def format_pretty_json(response_data):
    """
    Format json object into string formatted output
    """
    # Format the JSON output
    formatted_output = json.dumps(response_data, indent=2)

    return formatted_output


def save_output(pretty_output):
    """
    Save the json output to a file
    """
    if ARGS["test"]:
        print(">> [TEST] I would have saved output to: " + FILE_PATH)
        display = input("-> Display job outputs that would have been saved? (y/n): ")
        if display == "y":
            print(pretty_output)

    else:
        print(">> Saving output to: " + FILE_PATH)

        with open(FILE_PATH, "w") as file_handle:
            # Write output each line at a time
            for line in pretty_output:
                file_handle.write(line)


def load_job_file():
    """
    Load the json job data to variable
    """
    print("-> Loading jobs from: " + FILE_PATH)

    with open(FILE_PATH, "r") as file_handle:
        job_data = json.load(file_handle)

    return job_data


def filter_jobs(job_list):
    """
    Filter out only matching job names (or don't change if all specified)
    """

    if ARGS["job"] != "all":
        print(f">> Save only jobs that start with {ARGS['job']}")

        # Start app dictionary list
        filtered_output = {"apps": []}

        for job in job_list["apps"]:
            # Add job definition to filtered output if name match
            if job["id"].startswith("/" + ARGS["job"]):
                print(f"--> Saving job: {job['id']}")
                filtered_output["apps"].append(job)

    else:
        # All jobs - no filter
        print(f">> Save all jobs.")
        filtered_output = job_list

    return filtered_output


def main():
    """
    Backup or Restore Marathon job definitions
    """

    if ARGS["backup"]:

        print(f"-> Endpoint: {MARATHON_SITE}")
        if ARGS["job"] == "all":
            print(f"-> Job Name Filter: All Jobs")
        else:
            print(f"-> Job Name Filter: {ARGS['job']}")

        # Get endpoint apps data
        response_data = get_apps_data()

        # Filter out jobs from output (if specified)
        filtered_output = filter_jobs(response_data)

        # Convert response_data to pretty formatted JSON
        pretty_output = format_pretty_json(filtered_output)

        # Write output to a file
        save_output(pretty_output)

    elif ARGS["restore"]:

        print(f"-> Endpoint: {MARATHON_SITE}")
        if ARGS["job"] == "all":
            print(f"-> Job Name Filter: All Jobs")
        else:
            print(f"-> Job Name Filter: {ARGS['job']}")

        # Load output from a file
        loaded_jobs = load_job_file()

        if ARGS["test"]:
            restore_continue = input(
                "\n>> [TEST] Not restoring jobs: Will output job names instead. Proceed? (y/n):"
            )
        else:
            # Send data to the Marathon endpoint
            restore_continue = input(
                "\n>> WARNING: Restoring jobs to a marathon endpoint is destructive. Proceed? (y/n):"
            )

        if restore_continue == "y":
            print("-> Proceeding with job config restore.")
            put_apps_data(loaded_jobs)
        else:
            print("-> Will NOT restore job configs.")


if __name__ == "__main__":
    main()
