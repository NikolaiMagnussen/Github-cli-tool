# Github cli tool
This is a simple Github cli tool that allow to easily interact with github repositories.

## Features
Lets you do perform certain actions with repos whose name contain some specified substring
The following operations are supported:

- List the matching repositories
- Clone the matching the repositories
- Revoke write-access to matching repositories that are owned by an organization

## Usage
1. Before using the tool, you need to get an access token for your github account: https://github.com/settings/tokens
2. Paste the token accordingly into the script file.
3. For revoking write-access to the matching repositories, you can define a list of login names that will not be affected by the revokation in the script file.

For help with running the tool:

	./github_cli.py help

Listing repos containing the substring `kake`:

	./github_cli.py ls kake

Cloning repos containing the substring `kake` into a directory named **kake**:

	./github_cli.py clone kake

Revoke write-access for users other that the ones specified in the script file for repos containing the substring `kake`:

	./github_cli.py set_readonly kake

## Note
As of this day (02. jan 2017), the [Github](https://github.com/PyGithub/PyGithub) does not support specifying the access leves when adding a collaborator to a repo owned by an organization.
The solution is to currently use my [version](https://github.com/NikolaiMagnussen/PyGithub) that hopefully will be merged into the actual library.
